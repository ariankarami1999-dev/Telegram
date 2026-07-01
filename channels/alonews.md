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
<img src="https://cdn4.telesco.pe/file/TKzzx13pQ25N9g9POIjlcvconfMgALIcTWtwV4OBNuhGcZZYkulVB1snPIMpNaqpDdVSl_cjziMJARugr5g2AQFUGhLIU1LR6pumS5yxuqqns5K91-3mW_B8VS1chc0HKpL2Rop9gLcqnJ8zsZxtcNeJF4LMnr2o0hJpYJsnt3gzLcHBpYzncTmLSQL5wb7VVPit-HvBRzEphRNonWtF8PcOy1GIQ6z31SVn2NzFnh2QKzv_gkQZJp7Ry2tzO-g08Ck0l_cUEHv55yoAh0ehS9KW0lGPUGPLpzkdtva02R1XZTCbj0-2wNQ0aa1v9C-0cFQFfu5CLY9Y8h2OfMHCsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 22:25:15</div>
<hr>

<div class="tg-post" id="msg-131325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: اگر لازم باشد نه 20 میلیون بلکه 100 میلیون بشکه نفت به نیروهای نظامی می‌دهیم، این وظیفه من است و به آن افتخار میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/131325" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خورخه رودریگز، رئیس مجلس ملی ونزوئلا، گفت که تعداد کشته‌شدگان در نتیجه زمین‌لرزه‌های هفته گذشته به ۲۲۹۵ نفر رسیده است.
🔴
او افزود که ۱۱۲۶۷ نفر زخمی شده‌اند، ۱۲۸۴۱ نفر آواره شده‌اند و ۶۴۶۱ نفر نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/131324" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ با قطار آزادی وارد داکوتای شمالی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131323" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/131322" target="_blank">📅 22:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز گزارش داد که مقامات فرانسه تجمع منافقین در پاریس را بخاطر تهدیدهای سلطنت طلبان لغو کردند.
🔴
خبرگزاری رویترز گزارشی از طرف نهادهای اطلاعاتی فرانسه را رویت کرده که در آن به تهدیدهای فعالان سلطنت طلب به بر هم زدن گردهمایی مجاهدین و حتی تهدید به بمب گذاری اشاره شده است. ظاهرا بر اساس این تهدیدها بود که دولت فرانسه تصمیم به لغو تجمع مجاهدین گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131321" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، درباره تیمی که در جام جهانی فیفا طرفدار آن است:
تیمی که من به‌ویژه دوست دارم، تیمی است که امروز در جنوب لبنان دیدم.
🔴
فرماندهان ما، سربازان ما، این ذخیره‌ها — آن‌ها قهرمانان جهان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131320" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=ugxL1jpMKh70BnEMmHyY0ZHETs-JgZOruj4RUG1apXxH0XARUtiMH8J1BgSW7Sgte90AW5SDh13SNrzwrBNPHXg7eCbu1C39_DloJpveLwVqvE4oJwYsp_1js8_9xQoNjxBEyybpjnVrSzoPlfRTEaCMuw4FoF7Y2I_ms3Ig-_QXowxYqBuf0tcXJqwBMHKRs17L37mMtEAi-hItH9y3fX4Zc89kQL5oxVBVtQCMFYorzAQlN7B4fQmN5x-aAzIn9urAsQGLYwOr7-CM-VTMTqCPM9UmcF6F4RhCqAnHdQLHHiUE88aUBxTMLHRQYMDJh0aWTR_g5YYBM9pkDfhA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=ugxL1jpMKh70BnEMmHyY0ZHETs-JgZOruj4RUG1apXxH0XARUtiMH8J1BgSW7Sgte90AW5SDh13SNrzwrBNPHXg7eCbu1C39_DloJpveLwVqvE4oJwYsp_1js8_9xQoNjxBEyybpjnVrSzoPlfRTEaCMuw4FoF7Y2I_ms3Ig-_QXowxYqBuf0tcXJqwBMHKRs17L37mMtEAi-hItH9y3fX4Zc89kQL5oxVBVtQCMFYorzAQlN7B4fQmN5x-aAzIn9urAsQGLYwOr7-CM-VTMTqCPM9UmcF6F4RhCqAnHdQLHHiUE88aUBxTMLHRQYMDJh0aWTR_g5YYBM9pkDfhA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: ممکن است روسیه امروز صلح را در اولویت خود نبیند.
🔴
ما آنها را وادار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131319" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عضو هیأت رئیسه مجلس: حتی اگه آمریکا گندم رو به ما ارزون‌تر هم بفروشه، نباید از این کشور خرید کنیم.
🔴
نباید پول به جیب قاتلان رهبر بریزیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131318" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131317" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
پیام آمریکا در دوحه به ایران این بود که «بزرگ‌تر فکر کنید؛ رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/131316" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی: در مذاکرات دوحه به تفاهم رسیدیم که تا هفته آینده آرامش اوضاع حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131315" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی اختصاصی به نقل از دو مقام اروپایی و اسناد محرمانه گزارش داده است که آموزش مخفیانه نیروهای روسیه در چین در سال ۲۰۲۵ با تایید مستقیم وزیر دفاع روسیه انجام شده و دست‌کم چهار ژنرال ارشد روس و چینی در آن مشارکت داشته‌اند
🔴
به گفته این دو مقام مشارکت فرماندهان ارشد روسیه و چین در این آموزش‌ها از اهمیت راهبردی همکاری نظامی دو کشور حکایت دارد؛ همکاری‌ که در اروپا با نگرانی دنبال می‌شود اما چین آن را انکار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/131314" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اکسیوس: طبق گفته یک منبع منطقه‌ای، در جریان مذاکرات دوحه، مذاکره‌کنندگان آمریکایی به طرف ایرانی اطلاع دادند که قصد دارند به مهار اسرائیل ادامه دهند و اطمینان حاصل کنند که تل‌آویو به آتش‌بس در لبنان پایبند می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131313" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
معاون وزیر امور خارجه ایران: در نشست قطر تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131312" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=vHO2OSfvMTaSMN5CAXiv-PVfH5NQipoO2dlSBTaKK2wu2l72bsCmDHJx044-IJaTgDX1wcEwg14MgB0tA01TWNrQREJ-ZSHz4ci14k1PtXhjs2IRmYM2t_7nw4vGFIHvYNtbgHJ-VthYE9wyTBRZLtFmrkrTzyujBO_FB8gkTGjxWKWthfCbpdEMbQrIe2PB59Qf5e1fNCIcSAkwSYU_KMYxtXpZZolHbfKRRvKvhgmzlb1fmiVgT0-g_djoCl9-fuTz2_lss96KoNb8GUPUfhtVIq4gJTQCCLKWo9QmfMELhZpHZAnCAHwpWDboskOlc18TpgsNU8xQ6zH_mRMmvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=vHO2OSfvMTaSMN5CAXiv-PVfH5NQipoO2dlSBTaKK2wu2l72bsCmDHJx044-IJaTgDX1wcEwg14MgB0tA01TWNrQREJ-ZSHz4ci14k1PtXhjs2IRmYM2t_7nw4vGFIHvYNtbgHJ-VthYE9wyTBRZLtFmrkrTzyujBO_FB8gkTGjxWKWthfCbpdEMbQrIe2PB59Qf5e1fNCIcSAkwSYU_KMYxtXpZZolHbfKRRvKvhgmzlb1fmiVgT0-g_djoCl9-fuTz2_lss96KoNb8GUPUfhtVIq4gJTQCCLKWo9QmfMELhZpHZAnCAHwpWDboskOlc18TpgsNU8xQ6zH_mRMmvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اساس گزارش Kpler، تردد کشتی‌ها از تنگه هرمز بین ۲۹ تا ۳۰ ژوئن بدون تغییر قابل‌توجه ادامه داشته است.
🔴
در این بازه زمانی، ۳۴ عبور تأییدشده ثبت شده که شامل ۱۷ کشتی در هر جهت بوده است.
🔴
با وجود باز بودن و فعال بودن مسیر، رصد ترافیک دریایی همچنان دشوار است؛ زیرا کشتی‌ها از مسیرهای مختلف از جمله آب‌های ایران، عمان، مسیرهای ثبت‌شده در سازمان و همچنین مسیرهای بدون سیگنال یا ناشناس استفاده می‌کنند.
🔴
همچنین، سامانه ثبت حوادث سازمان بین‌المللی دریانوردی تاکنون ۴۹ حادثه تأییدشده در منطقه را ثبت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131311" target="_blank">📅 20:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی ارتش: نیروهای هوایی و دریایی در آماده‌باش کامل به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/131310" target="_blank">📅 20:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131309" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سنتکام: یک گفتگوی منطقه‌ای در مورد امنیت دریایی در بحرین با مشارکت رهبران ارشد نظامی از ۱۲ کشور برگزار کردیم/رهبران نظامی ۱۲ کشور تعهد خود را برای تضمین آزادی دریانوردی از طریق تنگه هرمز تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131307" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gogUAgN2zEjttUKDHlmoIREmH6xEydSiqDKeadZfbhHo95Y3EWuRLV_gcSwGln5PQJOeh3bgFmO_fBBJuePoEmG_mnf_SEBqVy-ewohGabCSqKNkq09mVpV3olsuzcngGYbFbpp0ofDPjsGZyXWe0tYGjWzZWpeTRD5Mxv71QriOY7j2xXw487o15WvQjejOFqoGxxxsXt-W3hpOYuzXr2JRzvqawlghua50j74AQjxuh9ZrkzoUACFcKr3Vit1Auqwq-6EiekZc27oPwoSLXtC2pMJJE8ldh1Wsad8Euque-MbMRUsvrkiCAsW7iVYKzDVkkD0GTq79t0LjWkZGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث
: خبر بزرگ! شرکت Micron، یکی از بزرگ‌ترین و موفق‌ترین شرکت‌های آمریکایی، اعلام کرده که ۲۵۰ میلیون دلار در Trump Accounts سرمایه‌گذاری خواهد کرد.
🔴
این اقدام تاریخی که با تصمیم مدیرعامل فوق‌العاده این شرکت، سانجی مهروترا، انجام شده، در آینده نزدیک زندگی بسیاری از کودکان آمریکایی را بهتر خواهد کرد.
🔴
این بزرگ‌ترین سرمایه‌گذاری شرکتی از این نوع است و به میلیون‌ها کودک و خانواده آمریکایی کمک می‌کند تا زندگی خود را با امنیت مالی بیشتری آغاز کنند.
🔴
مایکرون مستقیماً روی کارگران و خانواده‌های آمریکایی سرمایه‌گذاری می‌کند.
🔴
دقیقاً به همین دلیل برنامه Trump Accounts ایجاد شد؛ تا هر کودک آمریکایی فرصت بهتری برای موفقیت داشته باشد.
🔴
سیاست‌های من جواب داده‌اند، آن هم در ابعادی بزرگ. آمریکا از هر کشور دیگری در جهان عملکرد بهتری دارد و شرکت‌هایی مانند مایکرون هر روز این موضوع را ثابت می‌کنند.
🔴
این، عصر طلایی آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131306" target="_blank">📅 20:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل با یه پهپاد به منطقه «نَبطیه الفوقا» تو جنوب لبنان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/131305" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=afP0wyxxDdiqDZKaX2lABYqv_WVf1F4wb22Fc_olL2CAxhrf6PGywQP4fNOjj7Tc6CoUO2PTmTCGZTeYyMQ2s363B-_Dij8v4So-NfBRFzxVV8xUm1ebfXjbS4HNpjswKPzsGjC19AIatsd1HAZB1CKDlM-3QrBOmQ0o5eYsRwRm3pHcyQIELUDdovZA_rMfRJ48RJVAWpYecyNl2ipcxLn6Iq-Nbm9XToGeBbWGumfj7W4O_i4ZT4aPj0kPWWm9-jLT6fh07DB3FkcW8Zzu19M0IOWeD3OXHvZjCP7JmrODKINF2h2t0iRtxTabpVeP7yRIjlL6JmFxyKOmV9DDMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=afP0wyxxDdiqDZKaX2lABYqv_WVf1F4wb22Fc_olL2CAxhrf6PGywQP4fNOjj7Tc6CoUO2PTmTCGZTeYyMQ2s363B-_Dij8v4So-NfBRFzxVV8xUm1ebfXjbS4HNpjswKPzsGjC19AIatsd1HAZB1CKDlM-3QrBOmQ0o5eYsRwRm3pHcyQIELUDdovZA_rMfRJ48RJVAWpYecyNl2ipcxLn6Iq-Nbm9XToGeBbWGumfj7W4O_i4ZT4aPj0kPWWm9-jLT6fh07DB3FkcW8Zzu19M0IOWeD3OXHvZjCP7JmrODKINF2h2t0iRtxTabpVeP7yRIjlL6JmFxyKOmV9DDMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس: بعد از بازی با مصر خواستم بگویم فوتبال [با ما سر ناسازگاری دارد] اما اشتباهی گفتم خدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131304" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
خبرنگار: آیا می‌توانید متعهد شوید که آمریکا تا پایان مهلت ۶۰ روزه این تفاهم‌نامه وارد عملیات نظامی گسترده نخواهد شد؟
🔴
جی‌دی ونس: رئیس‌جمهور ترامپ نیروهای نظامی ما را دوباره وارد جنگ نخواهد کرد، مگر اینکه واقعاً مجبور باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/131303" target="_blank">📅 20:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مقام آمریکایی در مصاحبه با جروزالم‌پست مدعی شد: همان‌طور که در تفاهم‌نامه ذکر شده است، ایالات متحده باید نحوهٔ استفاده از این وجوه را تأیید کند.
🔴
این در حالی است که در هیچ‌یک از بند‌های یادداشت تفاهم اشاره‌ای به این موضوع نشده و در بند ۱۱ آمده است: آمریکا متعهد می‌شود تا وجوه و دارایی‌های مسدود شده ایران را با اجرای این یادداشت تفاهم «به طور کامل» برای استفاده در دسترس قرار دهد.
🔴
مقام آمریکایی همچنین ادعای واشنگتن درباره خرید محصولات کشاورزی آمریکا را تکرار کرد و مدعی شد:‌ در صورت آزادسازی دارایی‌های ایران، از این وجوه برای خرید محصولات کشاورزی آمریکایی از کشاورزان آمریکایی به‌منظور تغذیهٔ مردم ایران استفاده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131302" target="_blank">📅 19:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
یدیعوت آحارانوت:پخش اذان ممنوع شد !
🔴
کنست با قرائت مقدماتی بر قانون منع اذان استفاده از بلندگوها را در مساجد شهرهای فلسطینی نشین به بهانه «سر و صدا» ممنوع و آن را تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131301" target="_blank">📅 19:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس : صادرات محصولات شیمیایی، پلیمری و پتروشیمی دوباره آزاد شده
🔴
فقط باید طبق همون قوانین و مقرراتی انجام بشه که قبل از محدودیت‌های شرایط اضطراری وجود داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131300" target="_blank">📅 19:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ونس: اگر ایران سعی در بازسازی برنامه هسته‌ای خود داشته باشد، همسایگان خود را تهدید کند و از تروریسم حمایت کند، رئیس جمهور ترامپ گزینه‌هایی برای مقابله با آن دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131299" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=piBIDPT5qNvMIWDAZNcf6nSPAgTgubAJbtaleLPoMfS8stO-36PTpDEByIOZdTwrr6F7Qv9FkRNVnhmgdzwPVlUmx2A669effNGp7WHtCleJaAAa_U5hC06qmZbBJ9M6119cIXFlfEWDTuEm47yzAa0R5iE8juU59WCFoccziODH83skEXBaZhmQH0X5kOFkK2lq5u7xM500Ddyr9AxzwOp9t2-AUvTUruqS4X9HUQ4YzLazEKvaVsvoOwSQqOQqv0U1Y-M2dvl1Ws8eSe9XXMEe_U6XVNghw6mcvkEPftYeuGLZO2iXSB2tvLa7RAvoKsinWvF1iEv6O39uHrx9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=piBIDPT5qNvMIWDAZNcf6nSPAgTgubAJbtaleLPoMfS8stO-36PTpDEByIOZdTwrr6F7Qv9FkRNVnhmgdzwPVlUmx2A669effNGp7WHtCleJaAAa_U5hC06qmZbBJ9M6119cIXFlfEWDTuEm47yzAa0R5iE8juU59WCFoccziODH83skEXBaZhmQH0X5kOFkK2lq5u7xM500Ddyr9AxzwOp9t2-AUvTUruqS4X9HUQ4YzLazEKvaVsvoOwSQqOQqv0U1Y-M2dvl1Ws8eSe9XXMEe_U6XVNghw6mcvkEPftYeuGLZO2iXSB2tvLa7RAvoKsinWvF1iEv6O39uHrx9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره ایران: ایرانی‌ها از توسعه بمب هسته‌ای، از هر زمان دیگری در 20-30 سال گذشته، دورتر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131298" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECxfRO22FAaFSkW-WFMn-Yw_u-RQcjrQscN4JSCpz9_H4WP0MZGLXybdK__b_4QuzoWF3NvToIhDK7-om0O_MDFoVl4ZC4juxk2XFhuPLYmYJCAN2VlofcrLOWPfQtQi98znFAb3D7npO5LZUIRtVM-MkqSj4cVjksEZrhGLoijhHncKPRCzRZt_yc20n7u8zro2CWxShivPPyBklfdlDvTvU6di7NaHkQ-ttw2HwEX3_RqhwMHS5xi-3UxZbW5bIVGpxzyYgfWhNuXHS8oyyzyUkMlfz3szItEUG_F93RJavtIEqaX4DsRtynew4FOobbUmYXv6sN3uomHsYoj3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمزه صفوی:
اونایی که میگن آمریکا درحال فروپاشیه و نابودش میکنیم، کصخولن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131297" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
معاون ترامپ، ونس : ترامپ از شما خواست توان نظامی متعارف ایران رو از بین ببرید و تا این لحظه که اینجا نشستیم، و نیروی دریایی ایران هم نابود شده
🔴
مأموریت شما این بود که برنامه هسته‌ای ایران رو از بین ببرید
🔴
طبق گزارش‌های اطلاعاتی آمریکا، الان ایران نسبت به قبل خیلی بیشتر از ساخت سلاح هسته‌ای فاصله گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/131296" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آخوند قاسمیان در نقد مقایسه تفاهم فعلی با صلح حدیبیه: شرایط صلح حدیبیه یعنی واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131295" target="_blank">📅 19:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک مقام کاخ سفید در مصاحبه با فاکس نیوز: تیم‌های فنی در حال بحث در مورد تمام مفاد یادداشت تفاهم با ایران هستند.
🔴
ترامپ راه‌حل‌های دیپلماتیک را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131294" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131293" target="_blank">📅 19:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=g_hMdxECfUKMQdaw6DtC8jpCAiaqpFPOt9YlyvW5Ztk6YFtUFnSeuJ_WnFxh0SicMhmIwXs_KrOLMaVzpRHffRI8ucCy-4_pOzvV9M97hItuegNhU7t5d7SStIJeQ-P1moUJdtot5CGDHLf_egAC__UF2MfCPis2QbakhtaBW72I9R7uBCwLSKFKZo4YJAKDbQkvvnXkI2HaDDDFRUKpRu71-16ZGVBdYMJEQ5xofWw-NVpLRYfqYvZl3YBdYisn1nRLk0SZe9Aobr8WbBxsZ16QDX-uktC7szbqY7-JDaCGv3C7UJbQ5kSe1E5nK7LN1ozFBdhketUDzwRsDcqB_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=g_hMdxECfUKMQdaw6DtC8jpCAiaqpFPOt9YlyvW5Ztk6YFtUFnSeuJ_WnFxh0SicMhmIwXs_KrOLMaVzpRHffRI8ucCy-4_pOzvV9M97hItuegNhU7t5d7SStIJeQ-P1moUJdtot5CGDHLf_egAC__UF2MfCPis2QbakhtaBW72I9R7uBCwLSKFKZo4YJAKDbQkvvnXkI2HaDDDFRUKpRu71-16ZGVBdYMJEQ5xofWw-NVpLRYfqYvZl3YBdYisn1nRLk0SZe9Aobr8WbBxsZ16QDX-uktC7szbqY7-JDaCGv3C7UJbQ5kSe1E5nK7LN1ozFBdhketUDzwRsDcqB_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد: تیم ما دستاوردی نداشته است
🔴
کره هم شبیه ما بود ولی سرمربیش استعفا داد
🔴
مردم خیلی فهیمی داریم
🔴
سه بازی نباختن دستاورد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131292" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wch99pzpXSYagA5m8MfZtiakIn1874e4TNmBuEM9rR380XfxJZht4az_-Xj4yJn39P88ewLyS3vA_hTMWrTqOmZGImaVwvDueB4HCow2kUtNOXYcxQM_g5EJ9uQZ6i6sfmKgAtfZzhpBWJah-hxP_gVzyfz_yaQaxRWRnvXis8EDNo1uA4hulychM2Ra3tugri3ZKTt2PBszxgz2is2BzPsG733ojfDHRFnFBM69j06ODhzIZe8MuoSqKeRJhshwcfxO-flnj9LVXJ-Sl65E5d3DxnK-svVwoFz8MVLiAW99tjYQskleAWFvM2462XQpKfhLrc2DnoN0qkB2sjv-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با حکم مجتبی خامنه‌ای، اژه‌ای برای پنج سال دیگه به ریاست قوه قضاییه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131291" target="_blank">📅 18:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxEBIUWOhR6im8Gk6FgHE8KZoMnAR13Nf-v4YA5zCTKEMklAAWVU3Bb_zp4cXl9T0NSOnQ7Ir00LhFSWb63Kdllj8yZyazfHYsa_vtujBf7pjKO9Ozo0mvOWsbSRjhoCpt36_Kl35Ora4zZSPrwG1IGdtyAtqEC2nshXJCvEk-ohDttTIZ43Y4Cb5kaMTkhoK3p1N3Igkzqfd9fPA70uazntHlpQB96NKskbj00BHVJxCRQKiHXS6tJbYzqLBGvV3DKsKOPelEyKiwx5CMw2EwVbAdktPMXcHrEKk5t7_UsaYjpYWFT1cj0SIGbNIKF8LXU3D5KQMFEfXee4QEJYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قراره به بازیکنان فوتبال به پاس وطن دوستی حواله واردات خودرو لوکس داده شود
🔴
پیشتر نیز به هر بازیکن حدود 100میلیارد پاداش داده شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131290" target="_blank">📅 18:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3SZlyFOTQHC-v_5HO4d_ZdtEPGobc4Lp4ENw17mrX6ImJMxo9f-2s0ageied74e0qIKZnh0fiXAo2ZPszMMZK_8MMdccvQ8BiGXckdeEH5GAEfCkkOQqaeD7diZyrPOL6iGa2Bx9yQjE-kO-OPeq8CcMVe6Dpfhle3jgYjMsUp1kXUQSUYO7cf7eySWtR2b0ZmVQQx7MhR81YbDD_YABMTh63GK1-FoxoPtHXu2MFEiNpqzlEX88K-EV9QbExiCoDpYoxB2UyoVTyLj82FMukEJLkC2D7WjuyY8wnfxqfI6o-ETrCLl5shBd2IPdkx_nq0y4IRgxo4vf2mkK420Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4R0k5JRZ241qBznMECmLB9owZ8f3h2W6dwPNSYok6zuK68nj7aPg5nKrdKgrW4YjF6fYdtGVI-GUw1OpvvcQorrbvR7aarh0ib7tp6OjApnuBMjQmqoDJunDjIXDSVPQTFyxX2f5NNaPowKZbFIxSYu725keEyERCWvAxmYcZ_l8NmKT230FepUo6-2Q7DYFhMdL2NbLinvPbGmUfxJtIpTQZJmEjUR65zUj2PHQjsoBgFdIwafWj2VuVkq4Qik1ycvWg9NhTnKDY6hEsVEjTobSRcTLQfAWBGfaJ5UctW3820ETwtF_xAVeWNYGtY3hrFV98Qlz5o4j9TM_6fTyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارشاتی رسیده عده‌ای بیکار توی خیابون به دخترایی که حجابشون رو رعایت نکردن از این کاغذا دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131288" target="_blank">📅 18:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=Vbss4swPngTPrBJ3q3-RzH5Djr5jDB6qvCX4MYkO6uk9l-guSQeRhuc1pkyv72TazID1e4aNIYsz_ua3hofJ-Fy2X1h0UJtF-5cxcRbdz5aOhkkFCvrLng1AnRsnmfnxIh6grSEOR9eWvQ_q5oeHvRMOffcTMoADsXAs3sJ1k9e5c3b92K_HbQOkjaFRR8ujxowHls4zGAWHyWO9RR1XBaQs7OcWx6L2MzKnYDcbPFn9qmQZGffcOFmau7U0Nx0RyPavBALM8cH9qZFlSHPh19btRr4IJx6yRq4Ax0MOPp5GNMrIGeI-0BFIn0vQux0pWZKNP1cPp0Ss2kWBKDeczw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=Vbss4swPngTPrBJ3q3-RzH5Djr5jDB6qvCX4MYkO6uk9l-guSQeRhuc1pkyv72TazID1e4aNIYsz_ua3hofJ-Fy2X1h0UJtF-5cxcRbdz5aOhkkFCvrLng1AnRsnmfnxIh6grSEOR9eWvQ_q5oeHvRMOffcTMoADsXAs3sJ1k9e5c3b92K_HbQOkjaFRR8ujxowHls4zGAWHyWO9RR1XBaQs7OcWx6L2MzKnYDcbPFn9qmQZGffcOFmau7U0Nx0RyPavBALM8cH9qZFlSHPh19btRr4IJx6yRq4Ax0MOPp5GNMrIGeI-0BFIn0vQux0pWZKNP1cPp0Ss2kWBKDeczw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین یکتا رو یادتونه توی اعتراضات دی ماه اومد گفت بچه هاتون رو بیرون نفرستین، اگه تیر خوردن مسئولیتش با خودتونه.
حالا فیلم تولد پسرش اومده بیرون، میزی از خوراکی‌های متنوع که شاید هیچوقت ما نخوریم.
ماشین های چند میلیاردی که شاید هیچوقت سوار نشیم...
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131286" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
قلعه‌نویی: گل شجاع صحیح بود حقمونو خوردن
🔴
با آمریکا جانانه جنگیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131285" target="_blank">📅 18:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4AWkFhwyPQSfUjjwLa-_ZeGLIhQPUJnXU5X23Wk28Kye6Pnsb7ElQwWKlcgg-gJomBFZ7oTD5SMTNhDsGOvExNh-xlQwMi6VAmQ2QUVE5zpyM92qE-j5ACphY4Cz6gwz61oj511epOEwmzIfmrfZiPgq7hPauaM_7EwPuS1lPBrY0BDuziYktmgO5cT3NKvrTMk0oQ3YurdQSf2q0vG5p4_V6kPWz-HRLPpPDHxkxsgZ-96Ys-7prYIWHfm1dStAqjHys6IKdgVDjATDX4wi3QVl_FaFkN_YKx36nPRP17CNAK12ZSpnCY7821vYSOuYS_jCyr_q9NdfsQgj0M4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوچیچ سرمربی جدید پرسپولیس شد
@AloSport</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131284" target="_blank">📅 18:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی کاخ سفید به فاکس نیوز:
چه یادداشت تفاهم شکست بخورد و چه نه - ما راه را برای خلع سلاح هسته‌ای ایران هموار کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131283" target="_blank">📅 18:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euxw7L-hfKfSMn9TfjkHW_ksgl99vfWyROo8qF4Q_nmpS4hY5GcwWhGhuBWbc5mED0Rs8E9G61iYnpcW7C87IhOtgfkiTtASSMSV9QkCcCfa4qwS-6ylY-NhCQD5p4TZ09Vn8FrPXM3Szl1aCOqohdWR4nv8DJ09uTPiYyDrymhdf-RS6HCe4O5GfSHnXauoJTAMWLP98USb1X4u-2gJCNR5sFTGXL7_h-X_eB0j7gB4N376__AnS_TS0ZPZwXnQqdQEi2DPuRn-0e5PvMMXb-yoEAEUA9KZDadDRCmUGmzWqitvXSPrBskusno9dGk92WrjI--dxsJAmn_ld1-rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ کرملین: پوتین برای مراسم تشییع رهبر اسبق ایران نخواهد رفت و مدودف را میفرستد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131282" target="_blank">📅 17:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0221e4.mp4?token=THftG7GC2ovA6-hahEnJnWkxdyNwxiCAINayqMEol_BKMmdWjGWkgPu4bXw19MFxI7G0StJOINkyrPQRnPLE0frCEwCYG6jdBtfam4jfMJfLpdXhI7DOckHmZ64dQkDYYi6q0K-MWHoed3Kp19N8C_4nBKJBcpOSIQBZaL9-ptgQ8ZeRofb_XoZp7KyVjgSbIPbfBqNoixY70zoCI_lQZBrBTgP7nz9pNvm4Cd-uoikIyNdqpY2-2PVOJkU4SeoIM2GfA3ktN9zQspLLLHelHLBzux2vt57mPGfSXs4fij3O0iGzIFyMP_OLh9yBOh9jonxl4KDhwg0HluvqW6XKIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0221e4.mp4?token=THftG7GC2ovA6-hahEnJnWkxdyNwxiCAINayqMEol_BKMmdWjGWkgPu4bXw19MFxI7G0StJOINkyrPQRnPLE0frCEwCYG6jdBtfam4jfMJfLpdXhI7DOckHmZ64dQkDYYi6q0K-MWHoed3Kp19N8C_4nBKJBcpOSIQBZaL9-ptgQ8ZeRofb_XoZp7KyVjgSbIPbfBqNoixY70zoCI_lQZBrBTgP7nz9pNvm4Cd-uoikIyNdqpY2-2PVOJkU4SeoIM2GfA3ktN9zQspLLLHelHLBzux2vt57mPGfSXs4fij3O0iGzIFyMP_OLh9yBOh9jonxl4KDhwg0HluvqW6XKIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: در تفاهمات اخیر دستاوردهای مهم و ارزشمندی در حوزه‌های اقتصادی و تجاری حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/131281" target="_blank">📅 17:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
کاخ سفید به فاکس نیوز گفت:
رئیس جمهور ترامپ به روشنی گفته است که اگر ایران به سمت ما شلیک کند، تلافی خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131280" target="_blank">📅 17:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131279">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131279" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131278">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c924191a.mp4?token=Vb1NPF_DBh7QUX0EUeeEf6SqsM4NHwDqBhLoQ5js9W2FXGFp09hT7wvq0X8bS_Dmp_WgdhuF5vCw9KheCGtstP97pao6X9YNSTMNRKlAOM1dNN6Tvvrt2tTKZW7TTnLLoQy4zQuI51kqL8fglhPi4b7OUmOtam9DV2f73U8VxXgiLvVMKTPhpOCH7w4y5x3JI--EHPZlKrjlGr1xlnGA1Us3DHSLgDTa37kdoBp2-TFX9Gyxv93dolGz4_MZDhIQsipyYj0z133qetcVA9Ey1k2o0ZnJswqy39k7P-hVD3OI-GTFVORGDnXw0UheIcGcXCLR5PrQYSmo5seQiolWrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c924191a.mp4?token=Vb1NPF_DBh7QUX0EUeeEf6SqsM4NHwDqBhLoQ5js9W2FXGFp09hT7wvq0X8bS_Dmp_WgdhuF5vCw9KheCGtstP97pao6X9YNSTMNRKlAOM1dNN6Tvvrt2tTKZW7TTnLLoQy4zQuI51kqL8fglhPi4b7OUmOtam9DV2f73U8VxXgiLvVMKTPhpOCH7w4y5x3JI--EHPZlKrjlGr1xlnGA1Us3DHSLgDTa37kdoBp2-TFX9Gyxv93dolGz4_MZDhIQsipyYj0z133qetcVA9Ey1k2o0ZnJswqy39k7P-hVD3OI-GTFVORGDnXw0UheIcGcXCLR5PrQYSmo5seQiolWrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از اظهارات سردار سعید قاسمی در مورد قالیباف سال ۹۸
🔴
قاسمی گفت قالیباف مانند حسن روحانی است و چه موقع جنگ ۸ساله چه الان به او بدبین هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131278" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131277">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY8iZmtiMeZWHZTBhzK4GIacgBiydji1bTiKrddzBUu6QyEpo0EaHXds5nfG3fmbAIv7MqpRIcc_v6XNNWIB9IDQDrq4GzvfMeM1Rgh35JxE8UqkpRiNok8fmvjOPtph_WGjzdAJEUfJJlMvN4AzihlZER5j2fDhJgp1FxpODNBUy8X18LpsYTxSGsR6uagYH99xEMfMXrRTOaP2KlEAjg7BmeH-WITv389UxNAZ5nIqVv99EYGfske0L8keSHmjgiO87qlsXKoEbeFh22TTdiDp_cFPJ6kVaVowKCUooX8bqORP0A19B6mrRXYHITtHrUTQ0qzt1Fe2uehPy0QRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس شِلتر: باید هرجور شده اسرائیل رو نابود کنیم و مردم باید سختی رو تحمل کنن چون ثواب داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131277" target="_blank">📅 17:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131276">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">دهم تیر، یادآور حماسه آرش کمانگیر و یکی از روزهای گرامی جشن کهن تیرگان است؛ روزی که نماد فداکاری، میهن‌دوستی، امید و پیروزی را در فرهنگ ایران‌زمین زنده نگه می‌دارد.
تیرگان، جشن آب، باران و آرزوهای نیک است و یادآور این حقیقت که با ایثار، همدلی و امید، می‌توان مرزهای ناامیدی را پشت سر گذاشت.
تیرگان خجسته باد؛
به امید روزهایی سرشار از شادی، برکت، سلامتی و سربلندی برای ایران و ایرانیان.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131276" target="_blank">📅 16:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131275">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا به ۶۸.۲۲ دلار در هر بشکه رسید که پایین‌ترین سطح از ۲۷ فوریه تاکنون است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131275" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131274">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) به شرکت‌های هواپیمایی توصیه کرده است که از حریم هوایی عراق و لبنان استفاده نکنند.
🔴
این هشدار به دلیل ابهام درباره آتش‌بس میان آمریکا و ایران و خطر تشدید ناگهانی تنش‌ها صادر شده است.
🔴
همچنین EASA هشدار مربوط به منطقه درگیری را تا ۸ ژوئیه تمدید کرده است.
این نهاد همچنین از شرکت‌های هواپیمایی خواسته در سراسر منطقه خاورمیانه با احتیاط بیشتری عمل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131274" target="_blank">📅 16:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر جهاد کشاورزی: در صورت رعایت شروط ایران، از خرید کالاهای اساسی از آمریکا استقبال می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131273" target="_blank">📅 16:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeYbtbSyBdhXtnkCGHDy3MNGDt4kf55lR6uftE3xuO6EovjugaVBDgkjaoZiShamjUnWlJ1YddLp-hJXvXEUnhVCawJSRzMhDpw9gFbXCCMPJRXkaxB2AVeNYgH4Byx-Y5kefOxbr09PhjA7vlRJTcx3sPt3kLCcdokw83Pe130gzywNXz0fxwOxmALsG3YXyk_8NLdOVtnCR9G5HFcv2v3FRlD3VbsGq-I_XlnpyP4LYLgypPWZicVk7norsa2X8ozPPXpvyV-JpEv1OpqkT3qryyXJSnvHI0MSfz3PoVxndkZhRahtYdIj6FBgub-Umk9AnSd13iJSfMDNc0l5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده شدن دود در جنوب تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131272" target="_blank">📅 16:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: تا زمانی که دوره ریاست‌جمهوری من به پایان برسد، می‌توانیم ۵۰ درصد بازار تراشه‌های جهان را در اختیار داشته باشیم.
می‌دانید الان چقدر سهم داریم؟ هیچ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131271" target="_blank">📅 16:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ
: اینتل به کمک نیاز داشت. به آن‌ها گفتم: "کمکتان می‌کنم، اما در عوض ۱۰ درصد از شرکت را به ایالات متحده آمریکا بدهید."
🔴
او گفت: "قبول است."
🔴
آن‌قدر سریع قبول کرد که با خودم گفتم، شاید باید سهم بیشتری درخواست می‌کردم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131270" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ اعلام کرد که قصد دارد بخش عمده‌ای از اسناد و اطلاعات محرمانه دولت را از طبقه‌بندی خارج کرده و در دسترس عموم قرار دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131269" target="_blank">📅 16:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ : باید ببینیم چی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131268" target="_blank">📅 16:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=S70wRnKC_lEfeWFrxIJTH5ZPRbbbhVisGrQlEbl6T1NmQR2g7ZvMb8TD0XR8fmLa91ecQmFe1RGn4LvzQEoE3dhnlnhqkIqRgq3eUFA4rPAzTAyNcYYWRsjOWAiNNr9Ew5KwqVMASM4efIC7p3kLbMF_Riv417E-fWGxGq-MSDetjv1IeKP6kEGJ9HE7CWlCFvps9JHTyBLT734kme0p8wUzQ5B79uOz0OP93DL78iSbmXqYxIzOHTRHWE9RTbc_ZOE-S-BgusujswFlRfvtHdugi-jdojoUzoPWil7859L--MlLGnSe-vd5070QK2_rbQgGC5MEpNRsYPBTigQf8S7KvHx8FfzSIu8ryqNL-2B5l7gKUT8ZqI9qyoE-okvi-0Ks_xMawrw5DMSCGhmX3SaQrj1RvqyK_11Bn-WPUdrnV2Zemvqql7U4x7qMc2HLXt63ZC_9gU4To5pYByXM1fPa8wYwrjj5Najp9EKZ-kmewfkSAg2h1Al9qelxlBPJGJKg9aD72_SIHj-rhwz5Kaw1gsVm4K0fBhFtptxygXg22V7BZEMAbhF_t_vFvsJrAdTrXnJZQHKcwBDXjb72RRTWujZptk1H_mP1wLQ0yosPCFMr70KvDdbg09Y8gNQpbxAcYzPXNMembY-in-Bw-JdnhVXzvGChZ8jQ8pTC_p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a717d0815.mp4?token=S70wRnKC_lEfeWFrxIJTH5ZPRbbbhVisGrQlEbl6T1NmQR2g7ZvMb8TD0XR8fmLa91ecQmFe1RGn4LvzQEoE3dhnlnhqkIqRgq3eUFA4rPAzTAyNcYYWRsjOWAiNNr9Ew5KwqVMASM4efIC7p3kLbMF_Riv417E-fWGxGq-MSDetjv1IeKP6kEGJ9HE7CWlCFvps9JHTyBLT734kme0p8wUzQ5B79uOz0OP93DL78iSbmXqYxIzOHTRHWE9RTbc_ZOE-S-BgusujswFlRfvtHdugi-jdojoUzoPWil7859L--MlLGnSe-vd5070QK2_rbQgGC5MEpNRsYPBTigQf8S7KvHx8FfzSIu8ryqNL-2B5l7gKUT8ZqI9qyoE-okvi-0Ks_xMawrw5DMSCGhmX3SaQrj1RvqyK_11Bn-WPUdrnV2Zemvqql7U4x7qMc2HLXt63ZC_9gU4To5pYByXM1fPa8wYwrjj5Najp9EKZ-kmewfkSAg2h1Al9qelxlBPJGJKg9aD72_SIHj-rhwz5Kaw1gsVm4K0fBhFtptxygXg22V7BZEMAbhF_t_vFvsJrAdTrXnJZQHKcwBDXjb72RRTWujZptk1H_mP1wLQ0yosPCFMr70KvDdbg09Y8gNQpbxAcYzPXNMembY-in-Bw-JdnhVXzvGChZ8jQ8pTC_p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: منتقدان شما می‌گویند از ریاست‌جمهوری برای کسب سود شخصی استفاده می‌کنید.
🔴
ترامپ: من سود می‌کنم، چون بازار سهام در حال رشد است. همه ما داریم سود می‌کنیم.
🔴
حساب بازنشستگی شما چطور است؟ ۸۵ درصد رشد کرده. باید بگویید: "متشکرم، رئیس‌جمهور ترامپ!"
🔴
من سود می‌کنم، چون پول زیادی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/131267" target="_blank">📅 16:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: هفته گذشته حملات قدرتمندی علیه ایران انجام دادیم
🔴
ایران پیشرفت قابل توجهی در توافق داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131266" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما جلسه بسیار خوبی با طرف ایرانی داشتیم.
🔴
ما در مسیر خلع سلاح هسته‌ای ایران پیش می‌رویم
🔴
همه ما از افزایش بازارهای سهام و کاهش قیمت نفت و همچنین قیمت‌های بخش خرده‌فروشی سود می‌بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131265" target="_blank">📅 16:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131264">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131264" target="_blank">📅 16:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131263">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
روزنامه آمریکایی نیویورک تایمز به نقل از یک مقام ایرانی و چهار دیپلمات منطقه‌ای آگاه گزارش داد که ایران و عمان با وجود مخالفت علنی واشنگتن، در حال پیشبرد طرحی برای دریافت عوارض از کشتی‌های عبوری از تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131263" target="_blank">📅 15:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7SMekGziLLeDQimfCA0AXgc9CW5lsW5bekSkw3QDn3dPodYHfNpBYGW-EuZkj5FhDuAarhNt5G0pp6TYZXzWAijJq5uTUN1lxtwSPw9pMmYRn9g7G1AtDRpuhKJTNNuF6_0ORdt-Ii_PQWBJ4WmWRRlcP1vDVIn1EmZ3-pzfzJcfVexO7k489NYeTSXPXdEf5K3gl75wUGLYNktG75Obaf_R1s6hxbG1acFlZqnWoUXay9f5rk6UW2pAEhgNi0CCnR_IasEUvh_uN5FPJ7noeuKXdybmOwXVXfbLu2POi95FRVa7SK1dgMCoylxS3DvDB4EAyHyPGiWi98oYId2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مردم میگن نون خشک هم بخوریم باید مقاومت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131262" target="_blank">📅 15:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شبکه الحدث: مذاکرات ایران و آمریکا در دوحه در مورد تنگه هرمز طبق طرح جدیدی که توسط عمان پیشنهاد شده در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131261" target="_blank">📅 15:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131255">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/po7_ZHMt0MjJuCg6dZ2MRQaa0jdV4i0ymUiQbECq-LbyqXn1V6JRqA2Sfgag_CfN5rT-q_V2YcOhsYErfod2I7be_lpd4taFDgP0_pC5ffWkBGc_JhFcaRYdHlhAk4OU0tj8mTfxmNYHqMG5mAVzPP6z5pFFA47FqSEcPML0Etwzp7qwN-gg8os0BDaa_9Ha-OQJp6_FuZyREGNfN8CiVZvh5gxHlvpNs5TsRhPx_jdVKVgeWmNu21y63tIVlxX2hlablzTKfh56QBl8_YxgXBPy403xEPpLyrxV7FUYiBf2ckSHwzdwvwqoM7I-TxS4xb98pIM9_uhYjJm8jli7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK51w6EcJjMu3a15mr5uu2NCVuKULHMV_QA3u-S1GozrfWzDWXKwNhQ0EnYv3GPwdGpfFiP2N6X3g_bXAdVlN_krj_DE8mzYr8A-fp-ak1yeAyfI1Gw40vsitWsUxk5TCLpSS0bvGBd9arTrlgnCpz2q4nTasOyzMSn6cBQRnUWShW3CHlTpZ78ypZOmfcsIiVr93YPXXRbde54ZPjNDJVeZ0HgczijYC8sCcpzsCmr4pPvDpgVoK1qb8WSqV-L33SYVbnARB64WzJxhXjix5c931HzQW92tdkaL7EKvQLdpk349jlOe0-k6-J8-aGjmb6cn3AxAGvd4eyUS5FuS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auDTnWl0sjkRq_D3I-KRM9QkhWpIPpNaKLvcQVjb38OK6E1V_SCw7-niHBM0u7daA0w_754PzlrJ176gCif5UZgaRh61mvEuOctg7N6DrtdnokN5YLnWM5XDoSXkW2Uo6-F3o3QhHsIf3FVeq_IlQmGxjngG1UhrzTIl0eCiqYzo8opAXOEZOgjgyXpXCGpWYwSH00rWMvxBjo0Ajtr19bEDXJbCEKNjs46gvofxkbLXPEkmzWptJCXy7PzNroNwnDUgaiqEhig8DeX5PvdSVjiIhW1wDXHEVUWlUbuQnH6bBjdQTgmnunkFbCvqHCgkhWxLwQy7s8JbytTd0Kl2JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=N-TsxyV3fed5Xy0FRrrPZfaJF9U3yJLTOymrCLtov_u3d4DajLp_blSPXRSzmsfCcj94c2rBksnDitbQb-M765j8oR218v2Ed8fstc_UVZxRQnStXPQOvQuwArMszqHt7osCTleRbVt3DJE5Mo2LkNyF8r4BYxrpnJaDyQmRUjXyZm28O-Xj0KIZeYZACqGA1gpzoN3D-FMDGp_9PLmqPfokfC78engN1pIXVgqDoqenbED9kVpgZ8g0_PcKF8nRzXBqdgni1HvdGTRsp6Q-5b39YsWA_TyNXj92L_Mp6z-RoVpXBuABqVrw01lTUGFuNc49QHRv5jfCzwRv0FReQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c1770a4f.mp4?token=N-TsxyV3fed5Xy0FRrrPZfaJF9U3yJLTOymrCLtov_u3d4DajLp_blSPXRSzmsfCcj94c2rBksnDitbQb-M765j8oR218v2Ed8fstc_UVZxRQnStXPQOvQuwArMszqHt7osCTleRbVt3DJE5Mo2LkNyF8r4BYxrpnJaDyQmRUjXyZm28O-Xj0KIZeYZACqGA1gpzoN3D-FMDGp_9PLmqPfokfC78engN1pIXVgqDoqenbED9kVpgZ8g0_PcKF8nRzXBqdgni1HvdGTRsp6Q-5b39YsWA_TyNXj92L_Mp6z-RoVpXBuABqVrw01lTUGFuNc49QHRv5jfCzwRv0FReQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایستگاه‌ برق تو شهر لوبرتسی، منطقه مسکو "روسیه" درحال سوختنه
🔴
بعد حمله اوکراین، اون منطقه بدون برق مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131255" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131254">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف بین بن سلمان و ترامپ در پی جنگ علیه ایران
🔴
رئیس‌جمهور آمریکا به دنبال کاهش حضور نظامی در سعودی است
🔴
مقامات عربستان می‌گویند عدم سفر روبیو به ریاض در هفته اخیر، برای تحقیر آن‌ها بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131254" target="_blank">📅 15:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131253">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpBwcnh6EVDYRyZEuvP3EVmQgeUcF1S2ryZUy5R_xa1SGDRODBpqS2T9tOOLC4XWNNUaYmVsQBAAgBqBwvPb5gayLzPUe0W8r7THCcc7SdrX1hr9U7PJAbQTB7Qq86oWwvP-HrvNhafaoT9QwKBBPAnC9DGotFVxT1SoFSOqJWP30YyU8mxprfNnFHy9zYVGbQ_7ZAd_6NE_nwmPM55w-xU4_ecbrZst5eXl_n4981lUjzIYPvR84sb6_-977MHNzskUyoZWKin12yBgOAilxEoDJP-8o7-o6RWlT5JrnJdkd8rwyxBePL979Td5WN8KUFRk04Z6CHrBr66mD524Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف لباس زیر طلا زنانه در بازرسی از خانه نماینده پارلمان عراق!
🔴
کشف لباس زیر از طلای خالص در میان اموال کشف‌شده از منزل یک نماینده زن پارلمان عراق، جنجالی شده است.
🔴
به تازگی و همزمان با بازداشت عالیه نصیف نماینده زن پارلمان عراق به اتهام فساد مالی، تصاویری از کشف و توقیف حجم زیادی پول ( دینار و دلار)، جواهرات، طلا و ساعت‌های گران قیمت منتشر شد. در میان این عکس‌ها، تصویری از کشف لباس زیر زنانه شامل سوتین و شورت ساخته شده از طلا با واکنش‌های زیادی در شبکه‌های اجتماعی روبه رو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131253" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131252">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مرکز تحقیقات صداوسیما: تماشای رادیو و تلویزیون در میان جوانان و نسل زد تقریباً در همه کشورهای جهان کاهش یافته و ایران نیز از این روند مستثنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131252" target="_blank">📅 15:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131251">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESe5oJ9mOG2lo8rvKI5VJhXR9Ag9SSOd4zxXuxsFdRo7n0EJYtPFelRh7hWVY1Vb7nhUaOVDwMU_ID4VkBgboWLcF_2NHKcFBxIGUAIr9kotxrr-_Nrl1cbP8OJLHdGZMZNN0qT8vcjFBMSyPStuUHkhSnbFhXCfQDW5-TTCVWHhnut-r6MuIVLQrNilKU6d9qEae_Xp1zb-PbCwW-ucuO89pUac-tNU23TZIKUMkhzjMY-6qXNAET8tvtwWiGo-H03ZdeDAv_GtXGCAFbxjuM2WTzeLUrmXWtKm-TV8btNdNCvlOVfmcJMeSptPkhZf9wdU9Djgb_h5a7l8LZWMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / منابع العربیه: توافق اولیه برای آزادسازی ۳ میلیارد دلار به ایران حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131251" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
جی‌ دی‌ ونس : فکر می‌کنم کاری که رئیس جمهور به ما گفته این است که از این تفاهم‌نامه برای پر کردن مجدد ذخایر نفت جهان استفاده کنیم و بعد ببینیم اوضاع دست کیه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131250" target="_blank">📅 15:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_jyTSvbsmJbejSRM-O_jZ9u_etzKMJQRAHEg9Ht5fNQjsMeU1tSc8UzUxqAautNHI5mCVAyy_IeJarsKCV9jh7aovSi9tqiD9C2Qak6PJ6lcWFvL6kocJIjssaREAgNO9ppXvrOLFCK_aStO0abPDYcRlAM7J5aFcmNtuf0eXOCSwXV944vbTOLA83-OP6jlITz7AF7fjfql_5mRdpOGvuu5n5Y6vDzUYfaNrWYidmoCnBJ6-Nl22FBBHI6GJGO6K8SBkraKvGvppcze_5VQfuzwCrQIUi45vY2eulY2qTI9tsQscM_vQgkgtBcXqhZZjotGbexipfGRSlnmyIrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه هواپیمای دولتی روسیه بعد از توقف یه ساعته تو تهران به سمت مسکو برگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131249" target="_blank">📅 15:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پزشکیان:ممکن است در برخی مسائل دیدگاه‌ها و سلیقه‌های متفاوتی وجود داشته باشد، اما آنچه باید در این مقطع تاریخی به نمایش گذاشته شود، وحدت، همدلی، هماهنگی و انسجام ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131248" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قدردانی پزشکیان  از تلاش‌های قالیباف، عراقچی و سایر مسئولان ذی‌ربط در پیشبرد مذاکرات:
مجموعه این تلاش‌ها در جهت تأمین منافع ملی، کاهش تنش‌ها و تقویت جایگاه جمهوری اسلامی ایران در عرصه منطقه‌ای و بین‌المللی صورت گرفته و شایسته تقدیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131247" target="_blank">📅 15:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان با اشاره به ارزیابی مثبت مراجع عظام تقلید از توافق و تفاهمات اخیر کشور: تمامی بزرگوارانی که در این سفر توفیق دیدار با آنان را داشتیم،
از روند شکل‌گرفته ابراز رضایت کردند
و آن را اقدامی مثبت و در مسیر تأمین منافع ملی دانستند
🔴
خوشبختانه دستاوردهای مهم و ارزشمندی در حوزه‌های اقتصادی و تجاری حاصل شده است
🔴
استمرار صادرات نفت، تسهیل بخشی از محدودیت‌های مالی و ارزی و فراهم شدن زمینه‌های جدید برای توسعه همکاری‌های اقتصادی از جمله نتایج این روند بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131246" target="_blank">📅 15:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSx4D5Ro3tvaBpn9u28xQOQ3W9CDyiwl6CxcPEPyIJE-pzHyXrhauF_dAwxoJT04CEsh3c2dyQg4ZjFSsmMDmrKXhTy1WGulY90v41oJAanbg2dYvgrbUaGcw1vNKL8mGfLN81ff6c7Xj_5FOGx8FGeSgGlzQkBMQ5yX_G0_vwaK7vviWndHDhuwQbzhs3ubLbmgztCQJqAEB_53x-eLn2A20Og4VqjASA6ulX9CNAvLWcCqVcuJzfjcXc3Hpi5eJJRLceQZyHwRKNDE-oN2r1YtNmcjKDnoGX7wKGlayT_ZyKB9SdCU8gYXiiK5AkdynSKpCrBS5fdDGzUetXLPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه میثاقی قشنگ اینجوریه آخ‌جون بالاخره یه نفر غیر محسن بیاتی‌نیا و سیروس دین‌محمدی داره باهام حرف‌میزنه
@AloSport</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131245" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZEvY6bJ4UBZeNv2breASC9YXm5rOH_xSXrDu0fJXspc2wFE7l3OzvLjMEi9NkQv1apZ9tLeCkn0d7zIAEW9TeuouqcrnTTy-CqPfxs-BqPDYeAezPSNouXElguckWXyBUsMIHvQO1wQ8GSiUv41HBb73rkwiJLx-DP6HFo-qvB9ih2kACkzhrvrip8uNlwb320YCvTc0OiNGAjRYHFnivl5AszlnX8CC-U-1C8Xgjt6IAZs1efazzmY_lev-8SouO8cNFn6MVqVYNb8o3bWxXWtw2aoYpZs_J7I2dPuWOdS59_Ecy8uFFNVduTiZqLyiYOnZLjZypjPW86TdSRnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی خطاب به آمریکا: اگر حیوان خانگیتان ساکت نشود، ایران به آنها درس می دهد
🔴
توییت جدید وزیر امورخارجه: ترامپ آمریکا را به «ساکت کردن حیوانات خانگی‌اش در تل‌آویو» متعهد کرده است. اگر آنها ارباب خود را نادیده بگیرند، ایران به آنها درس خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131244" target="_blank">📅 14:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
غریب آبادی، معاون وزارت خارجه: گفت‌وگوهای امروز در قطر متمرکز بر پیگیری اجرای مفاد یادداشت تفاهم است
🔴
کارگروه‌های پیگیری اجرای تفاهم و مذاکره برای توافق نهایی شکل گرفته است، اما هنوز مذاکره‌ای در این قالب‌ها شروع نشده است.
🔴
رایزنی برای تعیین زمان و مکان مذاکرات در قالب این کارگروه‌ها از طریق میانجیگران ادامه دارد و در صورت فراهم شدن شرایط لازم، مذاکرات در قالب این کارگروه‌ها آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131243" target="_blank">📅 14:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
زمین لرزه‌ ۳.۳ ریشتر تو عمق ۱۴ کیلومتری زمین، پاکدشت تهران رو لرزوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131242" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6DpotSYwUigSvWY5qTKRNAmVRi4NLy3eyg9yPWlHR9HhlAAEsOYj8IAFCCNrBqIBZLJ_PI1AKAEtl4nEkRCLCTsARNoGnMhWNqP4RIYUuHTSJpHhLuWOIFKLIuKaITUWTdoYIa574goBtqv9APnR6ldxb-A_Yyi0JrE_zBiA4Oc4ME-KV30jX-xnQ_mDcJIpj8acBj5K6tCPX0yNiFIyMYbQq53EyZejH_GlcU4yYjttdxt0mpoMAx26MlQwsa9axv51k7NQtQNO0rHz66ufozX4PkK_7-GXLdEVR2GxOrWWfsmsUG3B7W8RnfUpUuydcbiY95r8S-FYPi50VGrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم کارشناس ارشد صداوسیما:
چین باید میانجیگری کنه چون ما به قطر اعتماد نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131241" target="_blank">📅 13:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا که تحت کنترل جمهوری‌خواهان است، با ۱۸۹ رای موافق در برابر ۲۳۵ رای مخالف این قطعنامه را رد کرد. دو جمهوری‌خواه از این قطعنامه حمایت کردند و ۲۲ دموکرات به آن رای منفی دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131240" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بخشنامه تعطیلات هفته آینده ابلاغ شد
🔴
بر اساس بخشنامه رئیس سازمان اداری و استخدامی کشور به دستگاه‌های اجرایی: روزهای شنبه، یکشنبه و سه‌شنبه ۱۳، ۱۴ و ۱۶ تیر ماه استان تهران تعطیل است.
🔴
دوشنبه ‍۱۵ تیر سراسر کشور تعطیل است.
🔴
سه‌شنبه ۱۶ تیر استان قم تعطیل است.
🔴
پنج‌شنبه ۱۸ تیر خراسان رضوی تعطیل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131239" target="_blank">📅 13:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
برنامه‌های برگزاری اجلاس ناتو در سال ۲۰۲۷ در آلبانی به دلیل مقاومت دولت ترامپ و انتقاد برخی از متحدان به خاطر هزینه پایین دفاعی تیرانا، در هاله‌ای از ابهام قرار دارد، رویترز گزارش می‌دهد
🔴
پیش‌نویس بیانیه اجلاس ناتو هفته آینده در آنکارا، ترکیه، آلبانی را به عنوان میزبان بعدی ذکر نکرده است، با وجود تعهد قبلی.
🔴
یک منبع گفت برگزاری اجلاس در آنجا ممکن است رئیس‌جمهور ترامپ را عصبانی کند و تیترهای منفی ایجاد کند، در حالی که دولت آلبانی پاسخ داد «پیش‌نویس‌ها پیش‌نویس هستند، نه تصمیمات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131238" target="_blank">📅 13:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f0ade05a.mp4?token=Mh0oo5l_DN9S4lqZvKWLt0mdmjW0ltV9wsYswdlPb8RD54-M_kLcagoUlJ38zdOaDg3kFMx6QHs8s3Q0Xs9McbswMzWu--lFkhMpX_6ywdrJ4eathPsOYXK4IZozpmf7vTdjX0MWi01CgJcJQY3qGLd3gXwiIJYsHiSd75u2p4XnW1n-O1u8IIxk4i4aWdq5lQ6wuyt31FEqhLKNfozxFYJcDIGiy-KYy-pkkB9p2B-_MCtLsDigL5NTJr3Q09ZFXiT3iIafI2XaC3guubHQNtAnL29j4RkWmWwrHTkyigAEetqlU8fsmafm6T7RAl74ZoC_m-GRHTH6DQkadmqIpR5LYbjZtrlvxnKuGf-iF_RzEUgbtbHtZeN_J2XRFXKm_7bi21C2RUt4QzVmaFVyLKM7KvW00bcCchtBtS4mxM8fiQ0xexjC6-34q1QpWHHKZaG5mvsou1echxLyVfP47_brzfKBTjnB9iWoD2lGlUDc-N8K5GBGjnw2nBx9PWwcBFtNrI9w88gEH5qNl2EpzsZMia4EzdtTCo_VgV2FLt2Z_y_2ywnI35-8MAY5buK56opmIg_udoXaTcb_62YFwtastWhaklJ5yQ3j0jF12toa27iJmloC6cDqnLUwq1Fm416X6vSk4925Cu8JfEbLezsAS5DmJwEPT8rXRAo6VnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشدار گوگل به میلیون ها شهروند ونزوئلایی قبل از وقوع زلزله
🔴
در حین وقوع دو زلزله سهمگین ۷.۲ و ۷.۵ ریشتری در ونزوئلا، سیستم هوشمند هشدار زلزله گوگل توانسته بود چند ثانیه پیش از آغاز لرزش‌های مخرب، به بیش از ۱۱.۴ میلیون شهروند هشدار بدهد.
🔴
از آنجایی که ونزوئلا فاقد سیستم ملی هشدار زلزله است، این فناوری که از شتاب‌سنج گوشی‌های اندرویدی به عنوان حسگر لرزه‌نگاری استفاده می‌کند، توانست زمانی حیاتی را برای پناه گرفتن در اختیار مردم قرار دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131237" target="_blank">📅 13:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نتانیاهو: ایران سعی کرد ما را مجبور به عقب‌نشینی از جنوب لبنان کند، اما این اتفاق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131236" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/131235" target="_blank">📅 13:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c28e55c3.mp4?token=szkrMUXtmLfxUQI3UV02TRUPMWxxqOm0mlDEJJsJRgWvMCqZ2Ghc2se2vwq5XyYWlpINEnY_JAxnkGC1gCYMvFjEuF-jSWnLeXgeOZKtx3ZCsVSITJlQEYDAhrQ08u4zy6b8z1W0aSTC2lZ4UJpDKNPZarjQ5l--PVaNePdFeyCAGaMNoRuIqCDOaWSc9LUrwsPdRwFIPoL9BrW40xWfFiG2Mkpz63eB1hAsaSIKkt1KXFyITlPbS8Go5T3Sf213AqTYGMgKiw8a-r32TNk6V1n5FgTNLjS5sqAD-ie-VxA3V2ac-tnEha5ERd1xYlOS73KjXE9ZDQ0L2sh4EvTHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرین شبیه سازی حمله به جزایر ایران توسط ناو باکسر که به تازگی به نزدیکی ایران رسیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131234" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ایرانی:
مذاکرات دوحه بر تنگه هرمز و پول‌های بلوکه‌شده متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131233" target="_blank">📅 13:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وقوع حادثه دریایی در آب‌های یمن
🔴
شرکت خدمات دریایی انگلیس اعلام کرد که یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131232" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNzDuqPiL3FYfJa_6FN3cW4aubOtozkUYGVKF_2iDd1moM1AdAFZ8iBKhYXuENCEpfg1kJ2K4g79C_DSLYAFEPLfltNGt-ISz7JNrhOIqrJymoT6DyFWlN_xKO6h1hsN2m2xW-7ius1TFW5yTYV0ckZB5Y3cqDkRA1qsQUCjN3yYCVv8gq8qtBypRG1hrY6PYPO-9CWiMkSKDQQdJEAiYdjV5Sqr0dA83HB1fRwfLgf8XZ9fZb-fd6b8x7wgKbHZJWdbfVUjIN9UEjSOXWiipHEwO8Lre7Q6oEK2bYzsEW3LJSRC8iTjo1Vr3k81VesalanOQU1kPq12hpF79wV4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131231" target="_blank">📅 12:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
صداوسیما: یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131230" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: در طول ماه‌های اخیر، ۲۸ پهپاد با موفقیت وارد نوار غزه شده‌اند که بیشتر آن‌ها به دست حماس رسیده‌اند
🔴
مشخص نیست چه محموله‌ای با استفاده از آن‌ها جا‌به‌جا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131229" target="_blank">📅 12:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الجزیره : گفت‌وگوهای فنی ایران و آمریکا در قطر در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131228" target="_blank">📅 12:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کوشنر و ویتکاف روز سه‌شنبه با نخست‌وزیر قطر دیدار کردند تا زمینه‌سازی برای جلسات فنی چهارشنبه انجام شود، اما خودشان در جلسات شرکت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131227" target="_blank">📅 12:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9119f36555.mp4?token=I4PPVkeilpgGSvuvZxKupX7yc0ahdeUbIXZN9odqVFHj9xhuAqrbPn3TtsbpDKry38vusj4CYbBdmLko9G-bKlnQumaJlbwxdwUeKh4o6Ml4W0S0uTnsScmrDuqMc_8rbkHKoAsvYRiZLoYUdEWucHebmBqJfb1yPWbwOHnjMcW9J7z9FAww9PaQu58on35BHK30_8tq95716-S0goa7JD5YDFexj8Ch_748a7Dk9EAq1l_0z_XfrqpFtbA2C7DnP-kwbEFJ9Daf-afcAbKhUmuf03AeZGjCpwdZ9D-nHFuNBmv9t6QnjZnv2jMy3nP2jIayzpCtU3cXI9yG5hj1DQokPcNJbglvEnQivZspcFVOT2sfwzhUxEkK3LcKXkYzIhGZOyvMnRZFFT7gwT3joXTHT-jgDqNAHJs3KHnBSU3DQjDE1A4LgUBJVb6GbkxzG8wIjEVyq5h6R0MkOsd-4I6sgsookgKpESVoKkfejg6dzGNdZkvgQoeQaLR15alVRKh_LflpP17Af3cr5uHSiHX7h9zvR6IQZXU1Tegch7t8vHez4WUoFkkEDRtA66Y3Uc9FLHMzjyic6DAx89uByK5XEClG4yLa_OWwnKvHMPp_BrT3keKJgwClyHwhaoyLs_EzxSJW0oLrP768GvjzDAtGlSaduCDn4qVw-rA8RBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9119f36555.mp4?token=I4PPVkeilpgGSvuvZxKupX7yc0ahdeUbIXZN9odqVFHj9xhuAqrbPn3TtsbpDKry38vusj4CYbBdmLko9G-bKlnQumaJlbwxdwUeKh4o6Ml4W0S0uTnsScmrDuqMc_8rbkHKoAsvYRiZLoYUdEWucHebmBqJfb1yPWbwOHnjMcW9J7z9FAww9PaQu58on35BHK30_8tq95716-S0goa7JD5YDFexj8Ch_748a7Dk9EAq1l_0z_XfrqpFtbA2C7DnP-kwbEFJ9Daf-afcAbKhUmuf03AeZGjCpwdZ9D-nHFuNBmv9t6QnjZnv2jMy3nP2jIayzpCtU3cXI9yG5hj1DQokPcNJbglvEnQivZspcFVOT2sfwzhUxEkK3LcKXkYzIhGZOyvMnRZFFT7gwT3joXTHT-jgDqNAHJs3KHnBSU3DQjDE1A4LgUBJVb6GbkxzG8wIjEVyq5h6R0MkOsd-4I6sgsookgKpESVoKkfejg6dzGNdZkvgQoeQaLR15alVRKh_LflpP17Af3cr5uHSiHX7h9zvR6IQZXU1Tegch7t8vHez4WUoFkkEDRtA66Y3Uc9FLHMzjyic6DAx89uByK5XEClG4yLa_OWwnKvHMPp_BrT3keKJgwClyHwhaoyLs_EzxSJW0oLrP768GvjzDAtGlSaduCDn4qVw-rA8RBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
یکی از چیزهایی که وقتی سفیر شدم یاد گرفتم این است که باید هر روز خوراک شبکه‌های اجتماعی ترامپ را چک کنی.
🔴
نمی‌دانم این را می‌دانید یا نه، اما او معروف است که نیمه‌شب از طریق شبکه‌های اجتماعی افراد را اخراج می‌کند.
🔴
پس اولین کاری که هر روز صبح انجام می‌دهم این است که بیدار می‌شوم، حساب توییترش را چک می‌کنم و می‌بینم که آیا اخراج شده‌ام یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131226" target="_blank">📅 12:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: مذاکرات فنی غیرمستقیم میان آمریکا و ایران در دوحه، با میانجیگری قطر و پاکستان در حال برگزاری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131225" target="_blank">📅 12:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دلار هم اکنون 175,500 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131224" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
فارس: ارزیابی‌های اولیه حاکی از آلودگی نفتی بیش از ۲۵۰ کیلومتر از سواحل هرمزگان در پی حمله آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131223" target="_blank">📅 11:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:  خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟ پسر بچه: آره، جونم مهم تره خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد. پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131222" target="_blank">📅 11:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131221">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=E1L7-bbfeO1OM6BAvz67PQTlNGg7JUWDwCI3Z0QOA8jsGy76cFoMiqMkIASDpDB5rhxWsHx9WhGUHaeRQew9VPqpNDBMmkG-iBei5e0f04v4-j-jT0-hZ1S4YMV-6OkjzBwM7JiIu81zvSgwqbifRkBjBtSmvQlqmwmGAiKl1allN7kcLUyUiSwtkmDobBgD8kpUFoKJyz9niU_QwZuXflmppr-77wF7djaHQs-RHKGQ2cA4A0Xj7YqubveVBKsLOud_sQTzUISpVjB0xS_GPAADeX-hEH2f82Xkbj8812jye8P1vekU6wniRknqDYqwUiIR1v_zXPFP5fnie_Hhfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=E1L7-bbfeO1OM6BAvz67PQTlNGg7JUWDwCI3Z0QOA8jsGy76cFoMiqMkIASDpDB5rhxWsHx9WhGUHaeRQew9VPqpNDBMmkG-iBei5e0f04v4-j-jT0-hZ1S4YMV-6OkjzBwM7JiIu81zvSgwqbifRkBjBtSmvQlqmwmGAiKl1allN7kcLUyUiSwtkmDobBgD8kpUFoKJyz9niU_QwZuXflmppr-77wF7djaHQs-RHKGQ2cA4A0Xj7YqubveVBKsLOud_sQTzUISpVjB0xS_GPAADeX-hEH2f82Xkbj8812jye8P1vekU6wniRknqDYqwUiIR1v_zXPFP5fnie_Hhfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
پسر بچه: آره، جونم مهم تره
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131221" target="_blank">📅 11:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131220">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvzvs79DrRE_DBCugQIDqnW2nGvbTOz0Mu-Y1FqYNzViY0dHGcX7lCYzdQv-wUmSIuhQRnMMpB-pNumNsFjJLMl_peqUs35e53GVRqhCBLW7QHTUGR3-yOWnY1RNiWRcqNfMQP-vQQJafyahpgqEW0ZZ-u8dwrWShwveu2A9PAP6kFE6W8QCL9eORtnJV4_fOXk5zmevbV02a-1OOrirsVlvZp7Jkyvh2LB3n9rKWJ1azwmFQtU0FrbEG_7MThnb_Rwi_p1Eikp7NLfHg5R0jFDNA5gp5izHCylyxBB6cM2uI2we-Ghhq52x4oJmYTni1WhV_soZQZkjM9t1mOdDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: اگر مشاوران به پزشکیان اطلاع می‌دادند که ترامپ ادعای دروغ صفر شدن صادرات نفت ایران را مطرح کرده، رئیس‌جمهور نمی‌گفت «۴۰، ۵۰ روز است نتوانستیم یک بشکه نفت صادر کنیم» و ترامپ این سخن را به نشانه پیروزی خود توئیت نمی‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/131220" target="_blank">📅 11:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131219">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رسانه اسرائیلی ای ۲۴ نیوز: سیا و موساد اسرائیل نقشه‌ای محرمانه، مشترک و پیچیده برای سرنگونی دولت ایران در طول جنگ آمریکا و ایران اوایل امسال داشتند.
🔴
بخشی از این نقشه نیازمند نفوذ مسلحانه جدایی‌طلبان کرد به مرز غربی ایران بود.
🔴
معاون ترامپ، جی‌دی ونس، از این نقشه‌های محرمانه مطلع شد و بلافاصله به اردوغان ترکیه اطلاع داد، زیرا می‌دانست اردوغان سیاست‌های توسعه‌طلبانه کردها را رد خواهد کرد.
🔴
این نقشه در نهایت پس از افشای جزئیات آن توسط ونس شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131219" target="_blank">📅 11:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131218">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
کوبا: مذاکرات با آمریکا متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131218" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
