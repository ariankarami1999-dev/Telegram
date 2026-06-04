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
<img src="https://cdn4.telesco.pe/file/IneErGZv4QmiBZWoqkdC5QVDewi_CXjRNhA98r2ou6B8t6Zzo3rYfPodQlbVVtnesRz3XrJQ6X-er5cMu_nUUs_jLnq8qzitOg1BaCX14xfKcIaxbqx187YvQ-E08lFOXZ3KXqqxGg8zj1danBEYZXkSQ9Nm7igGUyY3Ne4QKIDOkkJ0gv9r59GpUwiPLrUtY-tFL0WzD3PWC7W0aRcKkx3DFTg-nOhA4Fhuy6xOBIqZArF5JE4NU-4pnLgi5sH9y4lVBWyWJuQ8u7H_1DrEUl0qB32z80IG5LVBZfuU68NYFMaeTEU0p5SBWnLLJ3ZLx1-yIjmg-17RN4qVcR9StQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 228K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-65301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW6QzzcH7sAByDqhnIgzfXAKywLp0F2OzgdNHxw_cECxT7S695axbNurYpxtNjzH6CypwR4r8gktUzOpZ394LzVo0DTLvfLLS2DXXMnKhGNJDBeUVXpD6DupzdJUZR5k7xUIQkU8tU_q17ZznZPRlVdRqFMvmN2DEPTOtGgHlACQrMSYT4nDSeHX-JmJMTv8_HWV5r2avL4NCHQhOwbeGMI2rI1Vx_YUGZYe-Hbpb2sAczwCqOqTOQqfFkTgA3KQoukS7-TUtrbpD38XyClw6qDUPPEdXMxtynEucxPziULYOxN0IG71-9MCJrSq8WZPPjb7EbC2faSquHLgjmlwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
@News_Hut</div>
<div class="tg-footer">👁️ 335 · <a href="https://t.me/news_hut/65301" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsiWpIoiWa59JCirB-yWGcp1RYcec4qOhsHaCDZI-ACRkhio3gHWYx8LQYrYEWCAVmMFKzKPZwQoalFkVx2uBAjapbw3dnM72phchMMKQ2jo8PoVLK8yMvCwvp3olmdsPTAguLub27THsX9UGLzBvzsWRsFFf80JzT5qqfW0He2fosXL9TXhp0KlWYP2ePhQ84w0N7qwY_vcRe3xqKTI0mrFGgOWqxWBleBVTRu0AFTRJHwISY6JSnaUu8W12RtgZBGiiR8HQzktoxBwtj1TxTsaep-0WyyHGuTSvxkLizv-HMtInhWl2gRdVxwGLFNmx0Zpm7GRJvdOkkML7722WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در ۱۰ دیدار اخیر خود، شش برد و سه تساوی کسب کرده و در یک بازی شکست خورده است.
✅
شیلی در ۱۰ دیدار اخیر خود، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پرتغال  ۳.۶ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر شیلی  ۲.۵ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب: ۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 211 · <a href="https://t.me/news_hut/65300" target="_blank">📅 22:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSpLB7R954pqKR3nK0GbeGDKpAeTShzqNCzb5Bkem596pQ1aEmK5Mc4TZRozoL3wxbObScv7xkCEWcxD8FU3r2Rc0pcMYWfob4F1MKzs9Ft-EdD8BqDbyehStx_QLhU42SeDTW-tECbH1vtSmmGMTjdgYjN5QeEdTPlw2NjY7hstg3iBrQKrisQYYqoBFj5-D8lb_L_N8KInGRR6SuxjF5KVRM0I0Q4N7QD8qeusUi0Y9DLe1yTqg0uSht98LHzMHV2RTsyScbmYWQxYnjR8AKN98DTYQUKUsKHVg8JSgyPbr_AMvqGyl8HtQ8N6ZI6ykNLOmW5JNmUNCQMxa84iRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن های chatgpt، grok و deepseek رفع فیلتر شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/news_hut/65299" target="_blank">📅 22:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7628778a5e.mp4?token=fybURIH05ezZ_KU9Ax9L6PW2EK18upX27p8MccGlRt2_x9n_RT6TDsKCXO6TCxbAYqG8MULPdv6BlXh1kllhsMvyeguMyvok_-rkvY5YOs6YcJfeF4mqpQbH4BpK5HGarQ4YIVxcBQTFpOwxi5bI8WGWTEyor0Q3smNa8N5u-y_mc5Mh6hwyHxDIYxLKCdifU-VzpJLZQr-J2xuD2iVXKdJV7_n0Hg2SdijzprVmHG9B2mLqKwUhf5BylaJxX4z-mv2d-bSom7R8zt4JEE6BUY_1sqvy77oeAeQVPQF22gyZg48PInvBVlB9TwUrEr_LCOXzR3sToymotDxicdF--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روز اول جنگ مجری صداوسیما حواسش نبود میکروفونش بازه، میگه همه گذاشتن فرار کردن، هیچکس نمونده
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/65298" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/news_hut/65297" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt5BlmMY1rl23oiPymSG8BHNVOtBKTjGkfjBSYOLLdvwpZx_6dyv6nwKJz2IEZinSnDhnjnyr835Uj_NxvSveyCud5Q3YLuNXpjVocLx8-DzDKwFbStMp5JPco0b2C1rwLTsdPCuUfgN4ROPzBZuDqlT7hFDdECRsF2ewUj8B8pvQBumHyq4OXrED9QAWwTMBn9DcHxwRFRIxGG5zHYXFwpCS7D4OTm-O1BKcD1DlnvY2EWqoTTg1RTZzF33D5POoJrZNuwHEgAmaJljkAzmnwHTVgFwos6P4-0gz9cZKzsIgKvradLGUqkf1wlZ_1Pctr2vR6jp56ZmmKzv_-OV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/65296" target="_blank">📅 20:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
ایران موافقت کرده اورانیوم ها تو خاک خودش از بین بره
📌
با این حساب ترامپ از یکی دیگه از خواسته هاش که دریافت اورانیوم توسط آمریکا بوده هم کوتاه اومده
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65295" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt7nduve4exKx4-lsPAwZVO_ec_yezO0Z21lqvcdXt7xXLOPhwIXzfmBJdvjRwG95rhZfAfApO5d_gC6bm3v4-W-OFYHB8bdfqhbL3rXRUzBOHN1QUhkqEe1TYqpRK6h9bMotPOlViZ6gsAbx3TdNYTxJqo7qbApxeY0hZfmh5I5lAF2DFPbAR0znmbYcUzIkYbSQ3h99SuX6S1_Z9_kA_TCFmLoOnAvRXu0OJ4Cn2o5MFezjVE9_18HDzyN_Ca5wlRzCCZqBwoC2Prtys92eOG_pEXuBw_XyA6tUeOiwXprGFSxNve8xUL5ymx759mbBvHbQ_nOYrjVWTvw8P7K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: ترامپ به طور خصوصی به دستیاراش گفته که در صورت کشته شدن نیروهای آمریکایی توسط تهران، آتش‌بس با ایران رو تموم و جنگ رو شروع کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65294" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlWqJHnUTJwIsAfpUOBHQyiFV2V1C_8PcQtZ8KHq6mAmN-b5Y6nlzvUIVVN0TL0JRtH8yjxTH2NIEKVu3GshZMh1oOhc5yqaVZPT_9_b055v4QOCnD6u2ohZjOsLgNWU8EGqFb-rzRqkxxH_9pdlrpr0XvIKDNhMchYXLfkrmHKgPvI8fjQf5x8sMdP1rsLY3zAdClK6ptpvRBnTDpEJoa9INACWRQEcFIOoz1Q8OmzEstyvrPnNocTbRREAEPqba7Fbxa9cddfUE3b4CGKuJt7Jg-7F6G9tByXvOXlWKFrnMW82AHVwAbokZsyCo6sTWTPN_4cJH5ML4HilZE9PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65293" target="_blank">📅 16:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2074c6ee2.mp4?token=p4Pm88pMnIS2Rqqcdg0CDRhtWE3agT47hTLIciGZ6Td6AY-8htw9pFw1ngcD0LGMsa4JVQIINty88bzRzU63WKqol7dpsLO3EQXe62HEz5A_evIrwR5D75CIvoEyMtX7pi_RdTBToo2ySbuPc8X0s4WafbEKR-9cc70AfsNa2Z0we-U98YmFUUK0y6Lh3ZEjufoN9MmF4D0DDmga96uJv1KP4R1nNJarpKTkrf24OD2fNhgYfaxyhcV_sphKYRENsyIjuh2fYS0p44jsgWAjMsKbsMfcsuP6B0kpSuUZK7gMZ05C9nzeVaC_5GDr1llw4BWZMGkhna-irSzU_Zhfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه آتش‌بس تو اسرائیل و لبنان اعلام شده امروز جنگنده‌های اسرائیلی اهدافی تو تبنین و حاروف تو جنوب لبنان رو منهدم کردند
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65292" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=kuRFKVI1ubI9vVZ_Dz4w_OUBuKbJDnc_YV4oSUFN6MCWLAvz3QN5fY4t2MzRef4oCIsgdD1oP6cUkXXtCBZqqIsrZTwv3AHTulGbF1Gbrue4Ey-6ihiSAh8XW73EHgB4r2USAsq3vt89Od-lXC-1TGH3MC_tbqE34Q54BkqCR0YA7dm8XfA1KFQkaFjWOrdidKLeBm3Bg2uquJLgcDDATT1X1bD-Z_Rcv2O4p9dan9ZJ47UsHA9lmdnMXsSvOXCgMsYkJUXZdamufERkQa_wsc_XEumu_zIe5yEYuwfZbW_y60jYJdDTA0QQzaInSt74q9gbFCuDF4M80znTlVxoOjqR4m7oHKahVvhP2gqcGoDptuFTMH4zPqRWbNUv9zMlr8AWi8b_rZznhy4lFPN9oRBZMS4R7C4ucnrOzGWHu1ZqXXKq8YlImSXLtdegJkoOJ_bow6WtocoaXzMVhW9rJTia2kOmfTzAQ6-ISc3EeZ35CRs1yl6g4gghUyQ2bM4LXqHp-fodBQ97-3C4tZXdYFbH50S8DVG4zRlbeA8jAg8cilRPQA6MbxmCv9FzC9cRceYgbXKsjpGvTx5Icj4ZhTsTpB9Ta30K29FCZD4vAujAX-carFlPcLqsiKMQRyWDkZgEByETYE5Ep5Gaz36siFyY1T34Y7E6Un9PsbTcAoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
فیلم جدید و ویرال شده از حمله هوایی آمریکا به پل B1 در کرج
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65291" target="_blank">📅 15:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-XPh0l_IM15R_0h3Qw84Kslmt0VUVNibWhrBr8mZ5iHEDBSSd35pH2zYhSIjhLAlFsrSRabRwGthyBxNMsofw1r2nYWkHtRd-JXEpHNkd09JakrhiIcrQV4TpMyK1lF7D_jXx4dTspQNiV8mPIeyLcGYUIBC3r-Dq-dOW-UW9sxI1QaQB2EWjMGJQnuZpiuU0HNlcSmepiM-mLE7SDJ1VWGgIaYRbl_jsozxJbzorqQqkBaE0oEQceSPlOMy8N7Sj7GF_fIhe73-qE3CmtqwInf9HONtE05aOp89MM4tMl_w1JYFh-zPoR5Q9KkbKL9ujFPKoTI1G0MXhsmUlV9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تو ۲۴ ساعت گذشته بیش از ۲۰۰ میلیارد دلار از ارزش بازار رمز‌ارزها ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65290" target="_blank">📅 14:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🔵
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65289" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/65288" target="_blank">📅 14:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f7496394.mp4?token=iYqUgHKr2IfeX4B5PTHOrZUiZAE930c_t-IluMrx6_yjVv6q9M3029qS30WXi8BFuVNyW07dep-vBCKCaycq6e-0O0PCtmZ5hEXoMWcsN1GunfjgZhuiGTZ6npNUTotZM9yVycdeVKxgud6eINoRu8Li9eZMlm0hrsoI_83lTPCFSbh3ppkO8aO62WkcD5NtWVFUntQGf3rK8b0k-e-SkkBt6DajA4zj3kBlnbYO4FYYc1nS03UqDvpYeVEnwqbdYHvVV8_W8UqFuFjT2Yzx03X0sEILwV3mxjlksPBbNdIFs2ho75m8mHYciy74UzMELSaQAB3qr3i678viSM8w8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئویی آخرالزمانی از بمباران پایگاه چهارم شکاری دزفول در یک فروردین که به تازگی وایرال شده!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65287" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gngehLb536bd5d7zN4l0GqiWdfwLwLV_DvB5zfnH3S3gbLR6gyEg0jg_GYz-2Vv8BEGSQhRs-TXzUI9RWUpYdiYkctPpCWBODGab0jPQPw6P5zGotcrB2cGdrF2vEPavdP0_qCLtwBW0Lo3zlhseq3BIGgDl6yBtGxN74gSh1thAGPHOKxygE62wfbTF8Tny4Um1QrWUDCn8VbvhBcOVIu5QskHkPw_27RRV4BsTZigb6O8EbCwT0gYNVyIxPL8pedVn_fd4BkI02IsOsWQpk4mRvLRL_wGyyMq_mKH1lysVPyefTOYtPeiE4fXnbLCEciVONk00LUB-GFTEjCp0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال دن کین، رئیس ستاد ارتش امریکا برای اولین بار به کاراکاس پایتخت ونزوئلا سفر کرد و نشون میده روابط دو کشور بعد از افتتاح سفارت داره بهتر و بهتر میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65286" target="_blank">📅 10:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
کویت تصویر لحظه اولیه حمله با پهپاد شاهد از طرف جمهوری اسلامی به فرودگاه این کشور رو منتشر کرد؛
وزارت بهداشت کویت هم اعلام کرد طی این حمله یه تبعه هندی کشته و ۶۳ نفر هم زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65285" target="_blank">📅 09:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e323d6f5.mp4?token=ERH5cqv82efEExSUNs1_5cc5OmUKWqf-8yK7f4lJRTJ2MSLlAXxnR_A3r5u-xS7wqzJbY2AbKQiHncw6bAHAGNFGu2EKUqD1czGKGTY21kAeHvzX4fJxbEWFEpjqOtxJUR7EPaOd9sv-aghIZEkj48Vb_iXbfOi4NPWCLxJ5-ekUSWaqECHKb5MOQZru_cPQq4s5iWJLBHayPzPx7XtsjWPp-BMDmrF9L24ODCbdQJKwu1s09Lm96zz7SdENUXOgbC2f9VVJVTvTcidhmQ4X2212bGVSk5OEM7_RtK7jhjgekBJAnVfUbR5gNdqqrPBwcDI_BP34dxqRvHXYVxXdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مجلس نمایندگان ایالات متحده قطعنامه‌ اختیارات جنگی رئیس جمهور ترامپ رو با رای ۲۱۵ به ۲۰۸ تصویب کرد.
برای اولین بار مجلس نمایندگان تونست رای بیشتر رو بیاره حالا این قطعنامه نیاز به تصویب مجلس سنا رو داره و بعدش میره روی میز ترامپ برای وتو!
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65284" target="_blank">📅 08:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVertigo</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce5X2rIXdp0Ty3x6kiXL9QQelw70iE6pjNynlEBWJ6hZFyWPHpf8KRkqyGfMV1FRwBCtCufvgiRP63PbII_fHPjcznroR_OSrTBRKCbtkBaBf-EAirTPLwkYzyLU7tDDm4LYVHLryMUAl8a5aUoZBxITXp8vhoBmmab0qRHlFVz9v4sVijBk0Ds3RDQHsLyx0JrW-jLW8-HID4RNgeS6VaYOEtHxfozi5gP6CrN5J6dLSwk0SeTgco9INXWgeVDhccHb3V5r5_oORbYmwQ4HulJam3Ri_21XETDZNb503vg_T3j6Teb6UvlSLlyEFfr5m_P6EgslktJd3rMsNWT6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Vertigo Vpn
⚡️
🔥
آفر ویژه محدود
🔥
♾️
نامحدود تک‌کاربره 739 هزار تومان
♾️
نامحدود دوکاربره  879 هزار تومان
💎
سایر پلن‌ها
🔹
10 گیگ
⬅️
120 تومان
🔹
30 گیگ
⬅️
299 تومان
🎁
طرح معرفی دوستان
هر 2 نفر که معرفی کنی، 10 گیگ هدیه می‌گیری!
✅
سرعت بالا
✅
اتصال پایدار
✅
مناسب گیم و استریم
✅
پشتیبانی سریع
📩
برای خرید و اکانت تست پیام بده
@VertigoSupport
➖
➖
➖
➖
➖
➖
🫆
@Vertigo_Vpn</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65281" target="_blank">📅 00:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426918b893.mp4?token=GhcgLByLADbWnWwS9l4YBdIaVG-1pLCEPF0shwOkwmNSdE0Xm_iFGKfLS0mWZrd24l_UM_OLseh39D-VrjT2Hn77I4D2Mx3tXo2I_ilJBFTCxGfD5dwG1qfkYEVMek-fygCTdU-OtIQMy37lgl90PaUldb4dmCPtfj8KSJDSbfA0P8JaNP-SoNbAoJYGx8tZHnxnWQBQ7n9eBYUdCT5jJAyh5z5gEx95F-E0QZ9yxEmzfNoMntXfPHTlhMG_KIKQ7jL9IXoW2eEcWSmJQ_DNZeBZ_nGvUygUmdZwySTu-785dVtzGUn330PWQFYfMla1G3mB_9uIwXj5ren2TQzDzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درمورد نقض آتش‌بس: تو اون منطقه از دنیا، آتش‌بس یعنی وقتی دارن با یه شدت کمتر و کنترل‌شده‌تر همدیگه رو می‌زنن
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65278" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7323f0dce0.mp4?token=oLlnEW5sBTvlrz2y9sATniQzhJDSZCvvRxB2gNJg7qt55aGFQp1KD53l0h7dxhtTggupzBSt7atM5oKHcuyGNMlLLJdcR3takABNi-nSaE385ygDUyFL8O1x-Sf0vNhyD2_gCCqeKVdWz1nAxoXWUhVJsDjSqeUCEkCOVOJdKKW5pvaKj3RDsa-LKUPaSACIlFkoiu3Xfb3Y2XINaucWECTvcauNfEh2fx87F6rwnkIBzPwkNwRFTE8Lzw2tjIcfLUMS-a3PZJ2O2pVZ_nA3XaH7GpDrQtwhualDdrSrZUm8HADFuSOt2TBsJainTIYEBjO-pu5DEuZprcl8Bseg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی: مذاکره بسیار خوب پیش می‌رود... ممکن است اتفاق نیفتد، اما اگر بیفتد، احتمال می‌دهم در طول آخر هفته رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65277" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBI0WcjaE_syMQSrkLGGORbIwldp7Kj58J4qMh3VZRSfoU6RQ8Vqr1q4XEqAig_xfeT_riXzXmEjMcnSm-WR8FlHN6yfeVO8Xq3-uhb7HYP8g6igo4hBHhSWShj5wb-tOU9sW_mEd1g12_7DDKUIQfoYWfRyZ5sPnP2xYN-seTl-pvonpNObcuV1gMEV2CNMST2EaX32gtky3FKfygCtHYJTZZJ814bvFAw3GrWXgYF8THBzVhXFD79wUm-lFeEn9ILm2FPVt5IkQ_jOFJLDKuA29sCwJoJncZOcHQkYgeoXAuAa7PDpjhup7xZwJyLA4af-DCYYDGVyw4JJxwDmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام:
❌
ادعا: ایران امروز ادعا کرد که به ترمینال مسافران فرودگاه بین‌المللی کویت حمله نکرده و خسارات وارد شده در واقع توسط یک موشک رهگیر آمریکایی ایجاد شده است. کاملاً غلط.
✔️
حقیقت: ایران با پهپادها به فرودگاه غیرنظامی حمله کرد؛ این یک حمله عمدی، محاسبه‌شده و بی‌توجیه بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65276" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=a60lxCdTzmoe0nJ8TckZ38V6J5-L1F3coUwF4wW91bl5FydrR2TOdTITQ4oaCkHqLl704a0tAQ8r2BBPeYm29diDAAbJJB-igXSJ2L0QHBboVUVIdGc0i-Pa5VJ94S8YW__m7D2CG6-feZth6TIVbwEFYa9-7U4ZIGavSLfLDFpUunro2EtZ2vwO-VPfL9XbqPVTAZSMiym8O4f8lftHyMtJ_M0E_TmqJ2x0BLHuEgmYDqIPqzaQl97dIUGjOaDxvE38A8bOSNhm7tIJ_kQ3sVLr14UVH1aBGHrHPIekbZoOkf-AEZpEg_VExGu6nLKtSa0AvVIl66kQ8MAZCyWoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیده شدن ترامپ تو پارک زرقان شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65274" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAGQNRyoniCJaEZJBpdogyhKtZNCTxaeexG58E8NOEUrUwMZI6q5sVOlqJ-yy19xdsj5ZjqOy1wddGdjdtIlLy_xC4pUId58lOalg6HFAZ3sKhiGdM8dRxdKAw7mPLVcHtQsurkW4MSDWg6oASg07M1UvDBgiX-PCh_yAn39Z7M4szIYeHM86bhwxQfx574JWh4BYDQBXUD2ZEesxsB6aaE4BP1VjAD_0kKrJ6ZCMv2fnHwzbayl9Am_iwXLk1dZPTqIFqEnM7DI5U1QkAg4dSqMknjrGdW1lK88RneYWiNuVtrwhNtaYYeknf4ZdIpNcAS8js8ou2TJ5iUCMT1fpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در ۲۸ بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در ۷ بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپانیا  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر عراق  ۱.۸ گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۲.۵ - ضریب : ۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65273" target="_blank">📅 23:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdAGETwjCKi2T_PlQTFNfAvCzBr5heK8nkKbAxqK2h9xNTEYuhPxY0kSbJGX4CbKUi64q41xulvP_IXaFICHxfKWeJB_tahJyTeixRQqQXpRcJ-1JvYHQACiIr3BDYlvFohpYWNNdaLWyVQ19pNADxzEUAqC433g5umn-Isel8xMLAYsQLtZGM5gj183ECgzZfKTSu4newgQo4tkJXwhY4WuKnwIT051CN3c-rQPdSe-Iw0-dZvL2AwZ8t_EjPno4AlUjIlEIuPjK2YMQFSdYnA5bwqqMuQZvTp4NthjiehK1mpKzyOL5zMA5wvd0yfplIANLDbU-8sv4aMk-aTALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا مامان روبیکا گم شده دست کسیه بره تحویل بده شر نشه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65272" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BXazy1pIZ8ZrZYxbW8-2ACv3iRY9_0m9KOgU2q5a4vMSk5ncN9vJfLNBlYs3Hdgb3cDwKjZnqZK-uJaH-C2x87oxZCFyLi3UhE3b9te9qCxxTeLeFe0RFv03ECZmW6kKZ9fsKbLXmnMuFcz36K2kKxpwzMX12G_8zM7723wppfYNGWWjTsFVIekQcKlKF9nDhA5AcR8qJaqP1-n4afYF5n43s87urfR-zQNX6EO6FthRN1CDlZtuaqL6Ed9zeT-2F9nXq5F79w7tF-Dk_q7T_eipvJYF1zCRiZsPIeAQyQdOI5G2URK5kdbnA6dKj3IVUz99ejS-h5FJqqkRsNd7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2c124cf3.mp4?token=BXazy1pIZ8ZrZYxbW8-2ACv3iRY9_0m9KOgU2q5a4vMSk5ncN9vJfLNBlYs3Hdgb3cDwKjZnqZK-uJaH-C2x87oxZCFyLi3UhE3b9te9qCxxTeLeFe0RFv03ECZmW6kKZ9fsKbLXmnMuFcz36K2kKxpwzMX12G_8zM7723wppfYNGWWjTsFVIekQcKlKF9nDhA5AcR8qJaqP1-n4afYF5n43s87urfR-zQNX6EO6FthRN1CDlZtuaqL6Ed9zeT-2F9nXq5F79w7tF-Dk_q7T_eipvJYF1zCRiZsPIeAQyQdOI5G2URK5kdbnA6dKj3IVUz99ejS-h5FJqqkRsNd7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: شما درباره تغییر رژیم صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
🇮🇱
نتانیاهو: چرا این را می‌گویید؟
🎙
خبرنگار: به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
🇮🇱
نتانیاهو: این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65271" target="_blank">📅 21:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🟢
سایت معتبر رومابت برای جام جهانی بونوس های متنوعی داره ، از دست ندید</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65270" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9rYX0VbmhX8Tq6Ahu2n4g66kyhRbFvGVOMhbqjPeeWSOz9KXZqO_1QIZO4wfkEL9lZw67SbsIY0sVBugwgOxjFYobv6Ru3NZYBMwQuiPQa4wPR10Ra7eR0vSLLz5B89_nI4tfFHz1lOPp4e4nP3hauRKoTmKoBB4oQV2omgCTo4QH3slMzo_pSmPOe2maIuJG4YNhsSH4CWvKt3yhsxxfVLDIuFk-BB79fSzXOR-I3T2IsxaURHDgWluVlRRqYHVhD4sp4RGFStErCmyAW3-_HblDZNnvzsXTFSqBDrNShcnu5QdHcsgPXu9JDtxLzBaBwy9X366zQhMDul6lyjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران ، انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65269" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: هنوز افتخار اینکه آیت‌الله خامنه‌ای را ببینم نداشتم، اما دوست دارم با او ملاقات کنم  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65268" target="_blank">📅 18:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65267" target="_blank">📅 18:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاکولدزاده تر و بی‌غیرت تر از اعراب حاشیه خلیج فارس تاریخ به خودش نمی‌بینه، به مادر این اعراب تجاوز کنی شبش بیانیه می‌ده محکومش می‌کنه
#hjAly‌
@News_Huy</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65266" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=QzQMqH6yU81hPqJ6Boki4vm9Ik1mNt2S8LUXYuciebo-W-Bt-Ko8vkRkCvHlB2VSBoDlBsIGMstqkt9t508YMI4zuC6jkX4dLMaRDrRiZMEQvp-5UirFSAavT1pc7Nh7Tzx-oaVpPNIkySRDWRUGFzu_d2G4sC9m1JnRC0c3oCpN7mfUAls_lbHTTKs7DJJ1Wp6DWDz1IufYJc9XrMWSPeY_JyzwDDOEDOt1qtDhE1T95oW0MRoUJ-gsLpb6qr8fXL0xpJyY8L9Yr883odDLk3v-20XObhjCaGFyGrigGKYV8uZE5kywVVtQMyOpzJ0Q0GujvY1lifQKLeip2CcmQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa2babe8c.mp4?token=QzQMqH6yU81hPqJ6Boki4vm9Ik1mNt2S8LUXYuciebo-W-Bt-Ko8vkRkCvHlB2VSBoDlBsIGMstqkt9t508YMI4zuC6jkX4dLMaRDrRiZMEQvp-5UirFSAavT1pc7Nh7Tzx-oaVpPNIkySRDWRUGFzu_d2G4sC9m1JnRC0c3oCpN7mfUAls_lbHTTKs7DJJ1Wp6DWDz1IufYJc9XrMWSPeY_JyzwDDOEDOt1qtDhE1T95oW0MRoUJ-gsLpb6qr8fXL0xpJyY8L9Yr883odDLk3v-20XObhjCaGFyGrigGKYV8uZE5kywVVtQMyOpzJ0Q0GujvY1lifQKLeip2CcmQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ: با مجتبی رابطه خوبی دارم. دوست دارم با او ملاقات کنم
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65265" target="_blank">📅 14:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=WPaVaS-0z5-C78oa8HhRSBFGJhf2yYxgqY241yEePAcLfUQ5mU11M3N1jO4aZstYtrwHaZU97v_De7tt1GLs4lkdwcn19GUoNxX3Ym7VnZ4UacDEX-Qo_lJMX5nn-cYTGN2HbQIl0RRT0YPK96hXDfMICP7OUtiaTOqbYfyOqXo6c4g_hk37Nw0JSBu2xWv4oLZYr7uTSOF8yGZxUa0zjBR6V2fKCLGJWanASaGdaX2GVhAp5fWEGaLKRNnyHWGUdMr4UC0gu-ijpVXSOAYako2zvesv9tVF412lAZkiWUH97LiFzy9RyFXqNPX-yj9C3MNPBXmh6P4fgSzf_lo6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa16c5af.mp4?token=WPaVaS-0z5-C78oa8HhRSBFGJhf2yYxgqY241yEePAcLfUQ5mU11M3N1jO4aZstYtrwHaZU97v_De7tt1GLs4lkdwcn19GUoNxX3Ym7VnZ4UacDEX-Qo_lJMX5nn-cYTGN2HbQIl0RRT0YPK96hXDfMICP7OUtiaTOqbYfyOqXo6c4g_hk37Nw0JSBu2xWv4oLZYr7uTSOF8yGZxUa0zjBR6V2fKCLGJWanASaGdaX2GVhAp5fWEGaLKRNnyHWGUdMr4UC0gu-ijpVXSOAYako2zvesv9tVF412lAZkiWUH97LiFzy9RyFXqNPX-yj9C3MNPBXmh6P4fgSzf_lo6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره اینکه آیا نتانیاهو او را برای جنگ با ایران فریب داده است:
منظورم این است که من کسی هستم که این را شروع کردم.
نمی‌خواهم کسی را خسته کنم، اما من این را شروع کردم زیرا نمی‌توانیم اجازه دهیم که آن‌ها سلاح اتمی داشته باشند.
اگر من نبودم، اسرائیل وجود نداشت
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65264" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=QHh8vOnKzSlbuauXuZmoiIL6p9KRCCj_HYhe9knp24K4tD9oEQTKqbeuJDQALcJnHY4fFOV3P__vftzaSKJsociJp9GfUYt2iVlZyfUsOLxc9GQB0voZoGYbH4it2IttK_csQuScPntYJFQwT4ndSvdNa4K_b-lFn3-ZprCuHY4GWP3bwQ1B5GRgXXsZlQEhncwvW2aSezwPkEUi-FIr0Kt9vTZRHjnHO0tcd1_e3iGH_7aBrZqIKfMTJGjoHv0mGpTdS1_cozAGcFdz9mEhXNnCeuKE9e7dyRzYrNpwQFXdGNyZScf3ak9cfya53C8as9k8k7M7GIOLaD8m5eNMYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ff3bf1f.mp4?token=QHh8vOnKzSlbuauXuZmoiIL6p9KRCCj_HYhe9knp24K4tD9oEQTKqbeuJDQALcJnHY4fFOV3P__vftzaSKJsociJp9GfUYt2iVlZyfUsOLxc9GQB0voZoGYbH4it2IttK_csQuScPntYJFQwT4ndSvdNa4K_b-lFn3-ZprCuHY4GWP3bwQ1B5GRgXXsZlQEhncwvW2aSezwPkEUi-FIr0Kt9vTZRHjnHO0tcd1_e3iGH_7aBrZqIKfMTJGjoHv0mGpTdS1_cozAGcFdz9mEhXNnCeuKE9e7dyRzYrNpwQFXdGNyZScf3ak9cfya53C8as9k8k7M7GIOLaD8m5eNMYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، تحلیلگر صداوسیما: انتقام کشته شدگان رو بخاطر حفظ جان قالیباف نگرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65263" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65262" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65261" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
📰
#فوری؛ نیویورک پست: ترامپ پیش‌بینی میکنه که با رهبر معظم ایران، مجتبی خامنه‌ای که احتمالا همجنسگراست، دیدار خواهد کرد؛ «رابطه بسیار خوبی دارند»!!  رئیس‌جمهور ترامپ در مصاحبه‌ای با «پاد فورس وان» که چهارشنبه منتشر شد، گفت انتظار دارد با رهبر معظم ایران، مجتبی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65260" target="_blank">📅 14:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2Zw3oTH6U6_ZFltFGI6PP05j4HVV4MsbUsii4mSNBO7TZz3sWgwr7mx03716RiXyIEOwZvldqjIWGRkNnzVGmx7Y-wfTVo9hWblWO9SsIPPjBIX_FjoVj65jxkQzXpomvoLiUuEA9UXLUMEbUbB79A4bXTCg5LTdLSMXAs0RNvmwAiVU94awis89LSCl2yOx3VDbYPFty7qRCxdZIgLd4JgozpwKF2NklzjcI3T4KD_u5SsorUMssWmFjS9A9fKOHRlLYloWs8JiwaRqfdxV16mjlDEcN7YRWL7yH0RTMemdGeX8TvMfL0xLNLIHZePzDY9Z4HQ_-5KaE-wdmkIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست قیمت جدید و نجومی خودروهای آشغال داخلی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65259" target="_blank">📅 12:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NBicZPNCelD3CJ74lkofnfr7w4eDgB5We8LEqeZmeBAIwPYiC99vDAE3sK3ib7euZVxuiLy8tdbJ3abL8IoMQ70lhQYJnwVwYjD-lILNYRtrajUCk2orGjrWEDulGvSjqJUaKVzrtaKhEV5tWprOSxtdoMggNu_ZJ8E9mBSxI7kXO2ZYbb1vxa4Tzz9x7yROlaX-BjH8vvpzUEliBLXc4TGI8XCP1YI3_6E3nhy8nC5Fin6Y52UGRbGIIkddxC84B8FOGC_kLiMs4tuKwmyAJOI7YLQivvws5D1vcomZ-UBrPcDxKuPLfn6x8gtkTMUu8ImFuaOWBqklTFiLvGe6Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکنا: آخوندای قم پیشنهاد دادن علی‌خامنه‌ای در قم دفن بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65258" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtA2JgkJPKl1Ky6XCkmvuzGb8lNjs9U3xVoynpzPyF_irHbg3bYTfu0A8P5LAGk_2svrfpWfjVZXdsNUBGqkELR1m3bg1EtDjgVxC02wx1AxQA4IbH9ZJ9E6AHWCaTWtsQGrknSOGfQhCwE-X9BhHyu2je2kY3ryHhA4QIDfTM1yQt64QIYlBxO_sB2dOh4qpU22z0yb9wltWxvAnUpchhYpvmgxbb0JZnUPn77Zo7nxq3_sT0KTnZ50pSjSOTzVe9FMwpy5GTKq97CkoH0znh0npWKF2tCJ3HIO7l6aFZ2BAd1Uit5DeNzlUn6CMtfRYHiMe7KyC2Gq0aQGuOn42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uansrqsaaak2tOMoX0eNAHjl2gntVtCOagxnVJ-8DBRF0YeelDODPjOB_ycv8Mg09Jnqg1sHjsCseFAiRoKHkOFPyPQ3-4dV_d3gx1tVxJyyv5_sxvtfwGWSB2KmTzb9YJ5IdBi6_zoUAdA7X88pXRBxoFAjap4bdoF7LVkkpQnKTcbYCV9bAA5kp8jLXv4qBL4zZ0uzyKVO0lgjl_vd_5CjsSotrBUTMx0NajU4diSV3F7FqlqyjL5H0orcRsKP2UzZq_VJqEvmEpJTUa7tqSLF8davvaZwDlgyCOhx7BMC4bjbMrRRwGOC9yhrqpfelGYSvr7NQUayKWn8Q0c67Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت فرودگاه کویت که گفته میشه مربوط به حملات دیشب سپاهه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65256" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAtSlQNbOXFVuZKTI9jDxf4OpZ8FjJ8D3kohw-V7YcbN0K1xqWrh4wvZAhVEbhT6WnhhhzpT11ZKKTbC42NJoY1whGQstVaq7kveYDeelwbYsqFXb4S3wr_AzzXXJG8vf9XsyzFd9wPv5lB5GamiA_SGkJFpNzNCvxLKZYsABh7noCKSQ3ymXeTKWQkwiBZ2ihU1TjsuZguNyVrsRp0qVlCjDpTqyh2EYsfr_lQ4y9ooJvPcMHYE_vA5f7Jy8xIgjZ7f-vORLgFs1BMgQkn5_fWKF1NQACoqMIHxJp006vIKdYiHuhiEMW7m8ajVbGjCrg1n54aNDzhR7ihwfQuXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیت کوین در ۴۸ ساعت گذشته بدون هیچ خبر منفی مهمی؛  ۸۰۰۰ دلار (۱۰٪-) سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65255" target="_blank">📅 11:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">طبق گزارش سنتکام، ایران چندین موشک بالستیک به سمت همسایگان منطقه‌ای شلیک کرد. همه آنها به اهداف مورد نظر خود اصابت نکردند.
دو موشک شلیک شده به کویت در مسیر خود به هدف نرسیدند یا متلاشی شدند.
سه موشک که به سمت بحرین شلیک شده بودند توسط پدافند هوایی ایالات متحده و بحرین رهگیری شدند. هیچ پرسنل آمریکایی آسیب ندی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65254" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هواپیمایی کشوری کویت اعلام کرد که حمله جمهوری اسلامی خسارت شدیدی به تعدادی از تاسیسات فرودگاه شهر کویت وارد کرده و همچنین شماری مجروح بر جای گذاشته است.
هواپیمایی کشوری کویت اعلام کرد که ساختمان تی۱ فرودگاه شهر کویت بامداد چهارشنبه با پهپادها و موشک‌های ایرانی هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65253" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bac9b656e.mp4?token=VGoxHatWl3zQ97o4kYaleaPodybheCKGFB7qSLSvt9DNHdU-b3ORIaTJrt92uYvepeaHhoaGMLqgKs4cAivcd593LhZhbKzbks5SHPAhxJVLPK8UwjFsPUW3raVb8GIKPWHMQvMX_4uP0OAZmsVizdAgZKnDK4y5sx438QOd_OLmC-kv-A9XXaioaM-5jZX1E-OfJhY2A_sFbt7lOUCYBsSn_ExxcCvDYMKyJzQ2jGym3eVvKNVzbF04f2Qw-etZ8BTE72QPs02unlyZBjGCeooND62tORe3A_0bFv48X-lVaRHz9K_uY4zEaQReSkeVdG57rDlXGNo0ffg1m2FQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلمی از پهپاد شاهد-۱۳۶ که دیشب به سمت آسمان کویت درحال حرکت بود
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65252" target="_blank">📅 10:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
حریم هوایی بحرین،کویت،امارات به طور کامل به روی کلیه ترددهای هوایی بسته شده است
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65251" target="_blank">📅 02:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت  @News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65250" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
حمله سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65249" target="_blank">📅 02:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
اعتبارشو صد درصد تضمین میکنیم
ارزون‌تر، مطمئن‌تر و قوی‌تر از همه جا
🔥
ضمانت بازگشت وجه در صورت عدم رضایت
.
دیگه چی‌ میخوایید؟
😍</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65248" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
آمریکا بزرگترین صرافیای ایران یعنی نوبیتکس،بیت‌پین، رمزینکس و والکس رو تحریم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65246" target="_blank">📅 00:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYviT8t1Dx7Hv_6nWB3pcz5susscObDzA_eB0TPC6fvg5h7QoH_TmqyrMN8Ts0--id1N5oe96fiAxK3uSGffhBbfTBbJ9vW9qlXW9oyRjc2Dnq2N7NAC9owC1CiH-AGH-fCM8OANJWecSGdVq-BUgbCGrLiS6YgWaba8fUhZDDWdOMyqN5o9DpPgE2no9xUtk_u0YJCuwTRgM8i3dk3FVxYeTTQI_pV_Jo-sDOuuSZ5UWWYmt99lr8x7eApcefvX1X2Il8M2yCnOfsaojSmXAwPjz9lIhi5vF3S2dTJJ3fd4_UD6RCFTu7SBBVAL-fu6TWhY3sRNETECSs9zY5XRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4OeH6yxK-EMH7Mi03aIrtwC_vy0qmnKe0BPtxgiuwJYYFMY8_V0CbINrR1CL83A3CsDi_cHkGjNAt5KkMx5LrD27-prs8XogXI58_phZiczDurDPwK4TiZuYnhkdm8fMUZ1or-92sRAx74dHyjrPHLGTql_8UxTNbbqx8yAO_P6oxaA6nFfTtBA2AuBz1FzzdRAthI9ElJLP-aB8tmiGrXRi29F15mqZIXMlkeNhjKmsDJ0oqrzhuuMSh8xxd4eO4BPGNm0JH3oNkTjddNaiuzHR1yEwWodWlg4lW19tg5qLa5SMw8tK7H2GKGQ0y4RKpQ3WLVmf-eEVUCXj86Uwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه شرکت به‌نام دکترتور اومده تور آب‌بازی تو چیتگر تهران گذاشته که مردم از جمله دخترا و پسرا میان بهم آب میپاشن و هم‌دیگه رو خیس می‌کنن
ولی خب بعد چند ساعت از بالا دستور دادن همچیزو کنسل کنن
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65242" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmN1rEAPlKVwU-RJIQH79V0X_As9tRfx5fLb5unfF2eJLSSY9OLkWQTBjpeLxViy7G6cWynbzQl3nEZmMJwipWmiyv3u9Rxbc779SCkMQFlwW7Ml5ZGf3hq2xYB1t9QeTpseTfd8MlWOkETsIhu_92KQzBb0NX1dZVPhb0rneCh4j-glT5HL0mQmgsBYaZP5qfUGmb62t5jbHA2p6eQih9-YSaYAsuedBfbj9DIZmMhJHjCVh6w4AUHhzPBHCBQ8jwqRr0I9I2BVDDFe8PDL47thoySEMMjvI-7z-2QiRQGalqtMineA6dMnhbxJj9m_4Wfb1A6_ZSu2jmtVrH5T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: ابراهیم لینکلن و نیروها همچنان به محاصره دریایی ایران ادامه میده و تاکنون ۱۲۲ کشتی رو از مسیرشون تغییر دادن
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65241" target="_blank">📅 22:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIAIPGati6uZaqlSHWZI1RAP66vVtlXm4lexUMnfMDhPhauJr0AksOIhvVPLeyihyRw6IQLKxzBDNTILHVQBwYL8ycqkjBQCS4-e3rdGr7XrcRx_vrOZdFuwhWHytV7_9U2wVf8pGd6YV3sftrMfYH2UnNyl3t6n3ye60u7YYfJMV1RfouSs3qqAunTMPNYRZg1e1HzaTfTahdsRJeDOeDobklT6BIw4Ow-uPEACHQf-H19f85Jl3Kr_Na-Qbvvx5i5QOGSpG9TSXbmTWX3G2QfG8roe4WQfEP2pbvTumnRbH5RSkO_aT7CBy-_WdZ5Hlr3Estmy7oS3zc3cwpu3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddeqecuLsj-UFM7i7NrG7kHMfbHHq9n6pEvymErsvNm1VbkPua0q8u1f0H4UbKAZ-8To9OZbXlsBVcVJwZqbmtib4MOs2e5DEdBvvSXVeuV48HzA1lPw_qanqq-UjX11lrdEHW-exYgE7cBdCkV0ns0iXzo24BOFFZMF6dPwz5eFYTjQCKz42J_moNPu_SgnYbVYawA5OwtCko0EDpTmhF347b9eAme-_vAPZgNG0pLWiefv_Y-O5C7E-p1ABhe-1UqlyZa_A_w-FktAW1FpYcGERQ0l2HU9VQW0XHy1pqfZqj-YR8udVOFbE8TJn19O1NMNmlX_qir8IhG2LpoBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAw0_P2i-zqR9AQg8jLWPoVGtVrLDD_pPzZBlMipdKgGV1ohYSfezorV8RlDK9RfScGD6pOEfJp1r-UfR5kjmYpccvj2OWt81qo4YWWixSlEEpWCZs-0e8PvYbyFyPpf8buZhvl84n5aGEPxZWwmbv0a1VvZL5UV6wrDPAn_hf4m1wXwjDRGNE_SHsKgB5cShqUVd74LxHCHR9HMIttEo58-M-7xoXy4b4W4BBXD2QGseQ4P61CtCo0XRxJ78S87fMuj2mKrttgiF4v_8k3eZU3rRGyMMZn645d5sLkGJjLZpAZ9Ij2dI5VomnQAdsuThvxxSvOSuWeehgqwAbq5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=THXzbwGQhziDsZEyZV8Mjhs8pKL62b8XBgdfvXm8B39RvIQj-cqDntR9RboH2v9UugMpzUuoV7SW8J0W-QevrcI_ZURZIJznY6fjdNXmV2hNEiGjq_ilgDmaPgHfNpor3iIgITYsF4HzqsqknnCVYQea32aQcw2ZmPoCTZ9MQV5rfe-kJicN1OHbsLMigdRrO2RBc2W_Zwm7aaVCj7jNQavTsa5pfxiCK5jvnYRc62ug8-j8vm3s2Gt-KUcaVbyRKi9YczBtYBVGQJhI9JlKIWUS52NBeSQGdMLnVheZ377ed5f3qE985D_uBnju3nYX98MytZY4y8ApssjgJCOhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=THXzbwGQhziDsZEyZV8Mjhs8pKL62b8XBgdfvXm8B39RvIQj-cqDntR9RboH2v9UugMpzUuoV7SW8J0W-QevrcI_ZURZIJznY6fjdNXmV2hNEiGjq_ilgDmaPgHfNpor3iIgITYsF4HzqsqknnCVYQea32aQcw2ZmPoCTZ9MQV5rfe-kJicN1OHbsLMigdRrO2RBc2W_Zwm7aaVCj7jNQavTsa5pfxiCK5jvnYRc62ug8-j8vm3s2Gt-KUcaVbyRKi9YczBtYBVGQJhI9JlKIWUS52NBeSQGdMLnVheZ377ed5f3qE985D_uBnju3nYX98MytZY4y8ApssjgJCOhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=IuhDch5Bs7d2rnXGk9F99XjWXMIazQ37oTUlkQfZCYej4NoB-_UM1ywZYaokjA1-Cphzv5XabwAgPnf6QAvL_9udNq76jGkAZiezwU7xJ_nwPFPHp1-lgtjqDfULO3hBEJ8iNK6GXq6mTBFGqrigMmrVZ_EOIF31trMFw4mXqFzT8jwtTT-EspOQmTm1zfb--Vtx9YW2gL8-32dGMD_hvQg6wXVxEWPg2nXOJQ2jl1PlWQE6Lh7Q9KB-LUh8IBJnx3lOCv5wMQwJ2HDEC6ulCQqOB5-x9z3Sp2qpiNm-kImTpt6ymTIZDXioFJYMJx1xAGlQhIXwhjlsvVy2rbWWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=IuhDch5Bs7d2rnXGk9F99XjWXMIazQ37oTUlkQfZCYej4NoB-_UM1ywZYaokjA1-Cphzv5XabwAgPnf6QAvL_9udNq76jGkAZiezwU7xJ_nwPFPHp1-lgtjqDfULO3hBEJ8iNK6GXq6mTBFGqrigMmrVZ_EOIF31trMFw4mXqFzT8jwtTT-EspOQmTm1zfb--Vtx9YW2gL8-32dGMD_hvQg6wXVxEWPg2nXOJQ2jl1PlWQE6Lh7Q9KB-LUh8IBJnx3lOCv5wMQwJ2HDEC6ulCQqOB5-x9z3Sp2qpiNm-kImTpt6ymTIZDXioFJYMJx1xAGlQhIXwhjlsvVy2rbWWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=vJf8X1IM7Psky2keoAP1TnYrX35tyJm423DwpwE9O17n4725b_CkPAYrjgEH7wDgscpA24mfLnrPjAF9PJmHy-lar9mZFBAeoWS-QNJ384MHI2dKFRf2Nc2NgMwIhgIdm5JoRcoNhMghMOcHjX7ID6i8bONI_RUNWpKVLj3TtFw4wOdqRdV1qlKhghlrr0jg-dk7_p5VQUq_Bog9f2U960rP6meDoUl_6OBQL0qENME20MJCibn1TlQ_Sd7x6Z-2_W3SsUBKWaW3ezCCGIdaR81mBe0L3SKmHmshzSPVszMT9ht6ydSlUVgX1lw9goTDiFsG4E-eoVkLFr0kpDetIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=vJf8X1IM7Psky2keoAP1TnYrX35tyJm423DwpwE9O17n4725b_CkPAYrjgEH7wDgscpA24mfLnrPjAF9PJmHy-lar9mZFBAeoWS-QNJ384MHI2dKFRf2Nc2NgMwIhgIdm5JoRcoNhMghMOcHjX7ID6i8bONI_RUNWpKVLj3TtFw4wOdqRdV1qlKhghlrr0jg-dk7_p5VQUq_Bog9f2U960rP6meDoUl_6OBQL0qENME20MJCibn1TlQ_Sd7x6Z-2_W3SsUBKWaW3ezCCGIdaR81mBe0L3SKmHmshzSPVszMT9ht6ydSlUVgX1lw9goTDiFsG4E-eoVkLFr0kpDetIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2wV25T7qL-d_tOehLU99d1Oxx18Q2982LJtnqxb4EqxkybYXINcLyz0t4-aCCtmzDcxVEaV3eeRdYdHQqsxI1Z7iXGrmvlnyp0NvgrUb9yxKmPXtBoqkZDeCeMD_RpEn5IM5zEcBzyK3z1OeoTaKKI7KMBdCpLDsfYGrrpkjr2xtxHD6qky9hgNPD8Z7maSSrSkdUtXX9zGHViTQrpeLtzRCX62rnVxD3QAWGYCE_kGAF6h40HW7AJZeAyz9yHfyjdXLhJDXy8i6OWh8RprYNN1Vfe3X-YOMu7gsr2Z91HclDWjZViqPffqPO8uIMhNyKa_CWFZk3HromJeMKBqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=MPEF5J_IsZALLK5jTitp7yXu4ATIZwAJ5tZfnwQdQspn4s1oOg1tfb2XaXQT9OnTwghgVzbV-wQQ_LhDB4Teuu_TM2PEDyE5dMQc7rvaWPA-CUchKb4BxYjA87RwbLJgFO47bUiCRbFYlBS7UaR3o0YsEwPEyu8ULvpT7R_9cReGlymJg3mw0gI84ssrYvf5Zk_PyiffOVcAOOp0artZRlRQbaXRxUHVNEog1otktkk_Dh1f8TcltLKkLW6iZeAiyDx8E8h55Y4qq69GCyHBl65DBsvG8-vjXAJT5-rsq__Pdhn6HeYnlIAKT9VRKv0Woe9x3RLizmPnCFC-1vZ29A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=MPEF5J_IsZALLK5jTitp7yXu4ATIZwAJ5tZfnwQdQspn4s1oOg1tfb2XaXQT9OnTwghgVzbV-wQQ_LhDB4Teuu_TM2PEDyE5dMQc7rvaWPA-CUchKb4BxYjA87RwbLJgFO47bUiCRbFYlBS7UaR3o0YsEwPEyu8ULvpT7R_9cReGlymJg3mw0gI84ssrYvf5Zk_PyiffOVcAOOp0artZRlRQbaXRxUHVNEog1otktkk_Dh1f8TcltLKkLW6iZeAiyDx8E8h55Y4qq69GCyHBl65DBsvG8-vjXAJT5-rsq__Pdhn6HeYnlIAKT9VRKv0Woe9x3RLizmPnCFC-1vZ29A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=G_r0JOZlAkz8RhZlepup_4V0WQ0k7lWRGVQedMuEolibe4k2aQ5Jrsj71rlapiVvWaDpObV0-PAswIbCOzjgnEg557N5qe0hl6pjYalO5T0zQO0w49-_4OCaFw4we4ofW5UHaS04KjPvwE8yk1b13J6c89yHqyib5LV7WkAFEd_8Uw9a06H0mL1gCU_bj3tY8_0-xLGY5IFpQT43dH8MaDguy9WNnjReTb8kbrG9YEanPjYc_zc4iytVCq6wJl_tOxO9UMbK7YF5PNDr5UbqXJQxo420PXACz8NSyax24q9KqPufy0hGw9abuQ9p77re61we00YdHOMFY3cpOLAxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=G_r0JOZlAkz8RhZlepup_4V0WQ0k7lWRGVQedMuEolibe4k2aQ5Jrsj71rlapiVvWaDpObV0-PAswIbCOzjgnEg557N5qe0hl6pjYalO5T0zQO0w49-_4OCaFw4we4ofW5UHaS04KjPvwE8yk1b13J6c89yHqyib5LV7WkAFEd_8Uw9a06H0mL1gCU_bj3tY8_0-xLGY5IFpQT43dH8MaDguy9WNnjReTb8kbrG9YEanPjYc_zc4iytVCq6wJl_tOxO9UMbK7YF5PNDr5UbqXJQxo420PXACz8NSyax24q9KqPufy0hGw9abuQ9p77re61we00YdHOMFY3cpOLAxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=cvKP_0M2EZRnhAqCIyPCScAtYMH01W2Kn8RNu6A7uWYY1J-YHTVtJzCV2cJEoly0p5SJgA6N9xQAb9nd4P8Z-GIZLeq774dItHx9aW35Ysu8TI9z6uqVvtUpX7SBL5_XqpAnvKVr7TraE-Kqz62giSZwF-jP4EtEw84zusdFiHv112FyggHnjwMH5coPd-LZ1slF3qvroaH1DjGW7vlgrxswkqtpHgUUdUZ3M3CEDPcouLdAiHwpRDjwiowB9ok7GbrqbbA1fnrwMAQPWmu5h7wDb7c6Ufd_Flg5xigZRYt8KlWZ-Gx6pKQ_k34-4IWuRlOx3GshFa72NSg0g7KFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=cvKP_0M2EZRnhAqCIyPCScAtYMH01W2Kn8RNu6A7uWYY1J-YHTVtJzCV2cJEoly0p5SJgA6N9xQAb9nd4P8Z-GIZLeq774dItHx9aW35Ysu8TI9z6uqVvtUpX7SBL5_XqpAnvKVr7TraE-Kqz62giSZwF-jP4EtEw84zusdFiHv112FyggHnjwMH5coPd-LZ1slF3qvroaH1DjGW7vlgrxswkqtpHgUUdUZ3M3CEDPcouLdAiHwpRDjwiowB9ok7GbrqbbA1fnrwMAQPWmu5h7wDb7c6Ufd_Flg5xigZRYt8KlWZ-Gx6pKQ_k34-4IWuRlOx3GshFa72NSg0g7KFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vpMXZzqib-SM4NiBX0GRfxoWutiPU6BL5p2Xu0v5Ctn5fCKOR6sqS-C-hg-PXpcuy6PLV1Vhuo2P-XFYSxOeT3w0TU0rU6Md0jo7J4zJUeREBpw25T19ufiRIdGrG5ChbNmzFeGXSd7G4mdM88mo1nxdF3G7Oz7EBH9K4gACvv5ygJ62DT8SpZaayRRbAqKXa0m7SiWfcXm3IK0eJGeyG339BCe3oHbLGaMAzP6jx1RemVMzDO8_AuT777v_-oN7vfG8MgBcU9GqIY82fM0p8LbCs2XEW1Z3yUvo2xSAqWK-KM7lHSFN0BQEmZSAxwozl8egYyEuIUkevBoAcXHOXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=vpMXZzqib-SM4NiBX0GRfxoWutiPU6BL5p2Xu0v5Ctn5fCKOR6sqS-C-hg-PXpcuy6PLV1Vhuo2P-XFYSxOeT3w0TU0rU6Md0jo7J4zJUeREBpw25T19ufiRIdGrG5ChbNmzFeGXSd7G4mdM88mo1nxdF3G7Oz7EBH9K4gACvv5ygJ62DT8SpZaayRRbAqKXa0m7SiWfcXm3IK0eJGeyG339BCe3oHbLGaMAzP6jx1RemVMzDO8_AuT777v_-oN7vfG8MgBcU9GqIY82fM0p8LbCs2XEW1Z3yUvo2xSAqWK-KM7lHSFN0BQEmZSAxwozl8egYyEuIUkevBoAcXHOXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnPq6c0AZLrzQgGmPOoP_buyuWH-PH-rh1Y8G9iJyf3i20kAZncG_rDDw8-l3rFiJNw26L_oKmTVQFqzZR303Asab29VuOad6pznqBdGD8a1zXgsM1PPHaEhSMdNFuXOVebkGu-yagUiYzAZanY-nwwXeKLAc1FNG1Dml5uhoJNIx3yoC_3OMCC2RsvSRmXQXETjyt72Er2WxyJK4lo3tCwO8JuRO0ZeQqCkIB_ggmma8vPTt-wW1CsTUWjPpvvazyc597dDxMbWdlGky7PdfHjMR3jZ0L29dwiJGklutjnfH0WXEjcsl161pxZKqCxp6lhqYCWzNNTbR8B2a_X-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tqXqK0x4mPh0o5kl_-0guwn9Fks3VLlMRxKkoYmNRHe-1ZWaHgRbZh7h5KdMazyNhBCBaYNH6eUtMIZc3tg6LT-JZi6O6Nqs_CeNkwNeLSL9oM7oy-DhyB8asslCuWXfDLaX-QBq2rvH3tTA_tz8PNBZMVVWqFJnuHxKJfZBMF_yf3YHyBQRlbR96obBUPCiAGK2rU-VV6gJJEnTe9arsYUMFvRpdvWnCErw5a1exNDkdGzLsJIhZINaFzFhqwHqixv-SWdgY7GfJsNpuHqcXjwteiEcUrikYFB7LtMZEXFKcBWsjn0dcSQcXqyi53IUN8lYv5w3fQcX-mW2zQ6tag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYMpvX__mce_4LkVRDtsQo0nJAtFxpC28BO7BgifBPt67eNXQeihizZ5uSXHP0xDZIFL_or6lBXzpzNdM7o_QVFPmg_9ebt9IFNEoNEruPJfXpLixbPV4r9OWHJzqOYiWlkeKYwRqoybwCaW-O4I4cjdTNBNgDSm5yIzvf8edPcqRe22NqfsqPIQJAMK5fmapeh2ejm8UkCrEK3zn6f4KozdI7z5etVu7eKuPtOFDwgOvHlVw6b1g4Ohw-_3aiq40D4J519QJc0wv8IVKkso96jsm4bzcO007N9nqN5hM5pkkYK_gGWx2XHbrSPwVHfbhWdX5h9-kR014-nScXaZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p0ce_i3RMQY7E7hFXPmTnKxin6VJVgYki_76TcQ9BhPFCTnfg0TX8rE5wj48ys0fcku0bJa33DTNrqgiuZn4MHgXyf3V6-X6Jq-tkn3wNQ_l2BNTbeMTI5sfbT3Af3kf1BJm9JQcvFddr-zYSPfd-xG6oDPiNwfSbNMwUJCJE6CaS1TDgn4fmsvfOAv8amXjbyNqS8ALcsGXnwKi3hM8OkLFk6JHAy7inY2YEkq7atVFKKTnrxXs5n8WWgydnwV90KIaHHEQ9GcHYedNt6MS8b2YOZxo_lAnfWALtlbwyMWSi9Riy7OlPkrd6FL-Zoaj3o_DnxLwzXcHQi2YAMZ_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLshA4ZSJdpn-tXULXAJpNtotqnrnmZHVnO79sllpUNdOF5RpDFsvPPJzM4XxABJ3Gq-TpU51mD0vQQmj0l0_8n1Qs9q8mk_accTutKsCaMWOevCr33B75YM9s5Cx9fpsLoMmLZmchoW0Li83GGHrrP5LZvoPnMWoWhCvi6epq8MlJQvlmRq9j5dgy8cO93YxIjQ5KbmS5Q-L_95Yx1IiYLF1kyeZcACZ0jKs7Xz6ZTl9cYNcR7Mx2-qHwQZmPmNHoNDnr5DYwrTMToPMxVVgjOgdpGosVlM69HKUcam7KYmQavTUtP5hA5-PNBSy-CJgpqU2WI5bpmKAZ-YG1QraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuC3pXTlLXJf6r92Ioi7KyPFBK0IJ7nlTJ7Q4kY22KEz97vurRMD1zpEjOUensd9_3LwOjdSRU_icwUX-DyBQbT3Sst2ulw_HRu6GHwn8TQ0wPj975ogST5CVXt9HBDuPs3igF91-3HmZCEeBQMe6zU1GtBUCHLSix0UAY4mLktIX2tf_n6AJQYwfmKNBIoNuex6agjDyZmIrGY0oLsn7s8meZRT7PuICwR57gg3OriVXGa-LreCIe01uQkGgkfMwGelVJc9IqSmzw32KfQ_PN3_HYqSFKHHvyNUhGpwXjNUqwaLXXtlieDvnvgKX_jXIWDIqpQjDuhBBpY15T95nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAYirOGL5i1peW_yNH-KPFfqxG4EV2S1xgq01EF_qQE-QM5_6bvpsMrbPMA8umU9d47fbk-YCYnwiiCb-Rn7YofUxE_4KsiynRcdFugO-6x-0WteiAN8fUJ7veeMarO9bP5xGW-WPxwKyg8GoksUWLYPQMVXbQyORiccV1NH5tr2jexsE_495M3YXxWnnraSMISJL_9VAQGEBOZhEOuHns-1UM76QnjFuzRP_21pl7cB-X-1eQoAqArz4psojx8JRk6qGsmEkeN_STwxEGjZELBDVQTaYEcU5hwS7mb6kPP_cp9aMDwZsOoCJGQTuJROCxE7y2C2ZA_0l39A0SXQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKehMlriRwYDe4WJhfNnUsRF_L7XEsAqmHt8Obw8T4LnTePd5Nfk3vo_FY05qpIuEAtMbu1M8rVLNHperTrSLdq68gDESve0K6rpHw0Pap2leTUBbsL8mxECzMt5oS-fevHn1KTxZgp1vhtsVP63SW2o9xVzTAcOV8dZ5lmIVuWudEwp3Kjtqo_CU94icThXyTAlEHC9wnneeUL4SQKCuX7inSt5WIMZzy51fjTSOhp2N3v1Y-cbuSIV1D7Vtm0WBvLzdetZkilv_Z3gF4VHaU2m-7GuDREDIRQzH4ZTqcV28rGXApj0mPLPLpV9_SjzQig7Gwnk2DUQTdiRSAQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHc2SLVfKPieegQUl7FgmQH_Wzzr8xzCyiAmz_5ALdsVaZw38fAQbWkOcWWoQZipre7Qrwo-FOAl_mGOAAZn11_VXeUiLSPKnDcuIO5ZJv1bMMGMabN73G94F-9O60YbPjA-495Ogru4mGaJIRuYRJFZEjrImjwTNrjDbpAVa34AjkmzX5OQL4KMWD6tVxUslr8MHSqvGaQzKqFCEDiTGvzgNTznXc0liQ70sSt-KRpgoRt-Si6fgGSXR77z8G5Qf9bsL4sYK5J-8YBfoeuoTewqsvdiJC2y18HBHHCLY2MkSoSIreG3pYLRaZvKeEND3LpwieP9pfrokR0cPvnW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=Is9Th-Qfq_IKKj7_zFYwvmXhdn4pzzAzet4Ooy4nV5jMEQhFmvL2FcBTQ7O5tPdywSKQwwan1LJmXOMthNlwHF0MipMBXL-To-HkV4XuQwFTnhM59_JVF5dCupNBA7oQoZUuD7BFOi6PsSv5naRoqvYNIThm3LMLlTV1PDQV4bXKVjlmpq59ucbBWvkQ40RHnoj10tUtYCL_YRQKmhi-FJsHEeN5SO2fpAfO5cYmPpedxZXtodzCAkAHXVBCdY26eW-DnWrpSZExxU2FT0H0meuP-c2_qVob-VSf1lYb8PHNrdS9oC3Vwe1jXoOM-bYgnm4CShUD7adErJE0mCI1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=Is9Th-Qfq_IKKj7_zFYwvmXhdn4pzzAzet4Ooy4nV5jMEQhFmvL2FcBTQ7O5tPdywSKQwwan1LJmXOMthNlwHF0MipMBXL-To-HkV4XuQwFTnhM59_JVF5dCupNBA7oQoZUuD7BFOi6PsSv5naRoqvYNIThm3LMLlTV1PDQV4bXKVjlmpq59ucbBWvkQ40RHnoj10tUtYCL_YRQKmhi-FJsHEeN5SO2fpAfO5cYmPpedxZXtodzCAkAHXVBCdY26eW-DnWrpSZExxU2FT0H0meuP-c2_qVob-VSf1lYb8PHNrdS9oC3Vwe1jXoOM-bYgnm4CShUD7adErJE0mCI1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8aCFEVntNyD7H5PMm8SvrouWiD_ZzJS2qozqQbEQPYz9nvnNRDCHQcuw6TZXajMTIznIB45ehqSxnMZumDIOwXauy2BjTi-IfaBcZPA00_9nyAe2g-nS_-3b05mSZwfmfrnvo6OzJjGwKc-Dv3dSykdYp_H8rBtZ5VBGgS9xp66nJ0HxVmqYALQ1VW1qVNp4NhB8f-Oai4kbkdbzu7m3qbdOGJ6bJ-kh0b1LdJo75GniJTLuXkUoYGfvZIMknxaBeNQFFzmGbFSZjjQOQbsE0CH2bFCsvYDkz5iy4F0VSa0NfsC6FrXl61JGvrqCqTpCVCJRDpGWthAqtS3kDI8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcO-9VNRA0ENlRIR2AmKon3jlYXUlrsCF8vOMC1YpDzV6VdQ1YUJLxb99kNPHATESWopmgfAokGOscNCx1C06mB-mfY5apDEJPZinXVYlI7AG2XN2bmMscl0Fgz6Z-mS3D8UW7AR6W1yDdc62xIUY3aIHpEXXHJS89hLuUonhMeo79Ya0ZMR753iVoXb-0e_cPc5XvLCsUJ99Nu9vl0J2Z1PT7hvroNcLcYQWqI9NOMTb7jN_xZXaJN2SzW-1TfyJ1Vcwv8EAoccxLPLDYQwotbJlAOJv31OM5wYghq35eyyGlMRceglTyBvfJaYf1kF4aAvQjzRWCd5MvbMcwg6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKfyEKuDS-kszkMlyBJ-aM5-nCb8Gy1eqPKPSkySzHK6mfDMYXAtVpr7Vl_23uUfETteSogwhVNT-XDo0NfLAsa8m_Le6rBQ2QcJITBm-zVkOJ5SqYyR2cZpf_4Fj0ZrIUlA8qSN96M2KTM33ZLBx5TTDqxnFrLZ4nEy_ZW11ApAPk893oF1YaeAyyyVzFzfbmgC2k40TdItdRz6qJjUcnqeCz0xdJwsnaoY9wqMhTaHPsFaJ3T68w-gZqdh3JkGAQk3uWlS9LFKp4MLTImSRP8e71lMx_liZih2SL8uMMWJZ0TP4V2i8UFMGpCFi9zh-C4kj8vfEfjUpZCxqPzYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDMFkQAT4QqsSm2jVvNHoLAgvVafzm6l5QdOhQY_FsALpLZmKU_Qs-5VzwfPA2fbu7EQ6W2qZE9svE70FiuX0cJ9fRCxDW3FOSoeMXpKptYRHwBvEsaqr2dDWHtrpG8Ag3oq2NcHvfza55W6pgRthBPnTrQmaBDxFbtFdsKjxgt7wsLLt5cIAw4bAQ9cXoex9HbLOmLiB8D0Z5pzmyr-iaYlpPwLmMOq8UQOAU6G61tmQ5p5iBccRCy_iIUpOdskRgIThIkW2Zz2FgOjm5qNPkdSVGIu_jO43NMHbk2I5HC_CzeX_XEk6UOFVFsRTco2EVJfw-I9TJNNdgiclpbt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=izXmKJm8S8nVOI4ShPL7tFwcndRdErOr1F1PU1ZYh24g3ZZVkFl0sQtcmts3y6bJSaQPMVQD9VBo2iNa54LqKS87q8D9V2lf2L6smUq9DxzMH2jAI75zqM-_dIcfhJLy-xu8hRqcR9iwi-vbL7A2Fktpx2UTmmP-_xzlNGyTRR7x813lGAdZ-RJzeeAWsXrH7V5fTOy2MqyLxC918FBuKzo5VGTKcLH-HeL1ouUZekBMVwHzRlRJihkCpGaHXF3dFqecp17rNUYBTbsBNs3RqU-sss3dglEMOg4V5U5OMOXhG7z5QD7RGsZodG-_b1iGdInvdtwf6qSF4TYyfnHQ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=izXmKJm8S8nVOI4ShPL7tFwcndRdErOr1F1PU1ZYh24g3ZZVkFl0sQtcmts3y6bJSaQPMVQD9VBo2iNa54LqKS87q8D9V2lf2L6smUq9DxzMH2jAI75zqM-_dIcfhJLy-xu8hRqcR9iwi-vbL7A2Fktpx2UTmmP-_xzlNGyTRR7x813lGAdZ-RJzeeAWsXrH7V5fTOy2MqyLxC918FBuKzo5VGTKcLH-HeL1ouUZekBMVwHzRlRJihkCpGaHXF3dFqecp17rNUYBTbsBNs3RqU-sss3dglEMOg4V5U5OMOXhG7z5QD7RGsZodG-_b1iGdInvdtwf6qSF4TYyfnHQ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQjZNtWGnewJYwWXficXEGO9UBj_mWnod86xd_NmBDKHIksEiX_jV0C9Z3SLr_xmqC_UIXXM0zwf51Ezn6IjkhfsMHViATu6V69wR1yXYGh59pWmBIhvT-TBu4w5Iwj_ChR0Ft0yd1E1qtv24r7ZKKcGuQfqsFUUctRl7KDMrvlA2umYWXHwa84_WJt587U7GK4gc2DUa70VkxHG7r1UGuoo5cZlMJHsdVCxtxxwAym6lfyKZkwJTakRtlELsS089TDsH42KchMBo-qQj6loLtJjKy3pHuKM_zTsA_w78nIlQRv2Dc64BQ1SHMk8lYVi_zVj3hvAc0ilWGln7pwzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=AumfPknwwFlwqDbkxt1MkAQ2EjjpXd9b3Q1iDxG_UDAr7s9V36vEIpnBcJGtXlCi_Qk2-3dURkPi2ilI2idvr5SXt5cvTRyDB1itZNgGV05hV5tjOql07v6LXYITgtW4XDQtCauVzuThv8ztR7q4fG1VGWacmODVCvrSywNVrnC45V92E__BzauriovwbW6tbYmWLv1skydiTo2Wc83jVAr5WI_NiKgYHOM-CK1rdz8MFOLZnHeW9zd_BiMPP4P-A8mlcKP24Ktp7QdQnCCxf8vxYffA1ENhEwvlRVlX6DR1TroVXVoXXsY78M-2D1DV8owTMtOKhOF96MjZ-V3hDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=AumfPknwwFlwqDbkxt1MkAQ2EjjpXd9b3Q1iDxG_UDAr7s9V36vEIpnBcJGtXlCi_Qk2-3dURkPi2ilI2idvr5SXt5cvTRyDB1itZNgGV05hV5tjOql07v6LXYITgtW4XDQtCauVzuThv8ztR7q4fG1VGWacmODVCvrSywNVrnC45V92E__BzauriovwbW6tbYmWLv1skydiTo2Wc83jVAr5WI_NiKgYHOM-CK1rdz8MFOLZnHeW9zd_BiMPP4P-A8mlcKP24Ktp7QdQnCCxf8vxYffA1ENhEwvlRVlX6DR1TroVXVoXXsY78M-2D1DV8owTMtOKhOF96MjZ-V3hDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PADgCmR3JyqxNPLhj8jwsU2ifw4JkLpmdemUmx6jBlgMAJoNMvNyEAnx7W5LK_g9Ygea7y8QjCpRpTbp-9qb-cqWdBGcrpiXEa_mGBr5wQrv35WJlJg1_dwpMvqz_g6jXN9LVLvFrIjT233gSUVs2w7lnMkk5vPep_Lu5sJSCRX0HLs_YmIm4sboqeUATTaekZKg_m2awtZ_KOQfNowv9jkLQ4f1OQu-Avm7PACxQ74kaq18jxq3EGXapWWAMaVRUPDBzXwCBXMSLa6kCQ65ExFS1QK1MctQtQDKs7bn8h7F5eB12KImIR6YVYM2ImlGlrq70SVL-EdDJb8589gAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=XeMklhTotYn0WBOGuE7mvru7OZNjFppxUdB1WazqJVLxViVbI31bkDzb0tZzINLOqGbWrg3W_uXegcZRs80bvdU3Ao7J7JZH7TwfYGtEsL-QJ0wx3b9bCKp8w_D-a8XyaBG4l_RW7Oh9OPJwjvJyovH9olGGKKthdfNd1R_N0a10iojDEl8oDbZt9ks5YvFIrvM-8JH5UDfOafDvAlEr2gGOPzVakLWqwrze7I3fenJUcsRuON6TW3xT70xwo7Y2EWZ5FoE0hIeD2YpLUtXSPkUP0xSLp_kabcOyPn8706wsM_kXlGa63GotL-wMNF9AajGiSQtrriEYLpSmEnHYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=XeMklhTotYn0WBOGuE7mvru7OZNjFppxUdB1WazqJVLxViVbI31bkDzb0tZzINLOqGbWrg3W_uXegcZRs80bvdU3Ao7J7JZH7TwfYGtEsL-QJ0wx3b9bCKp8w_D-a8XyaBG4l_RW7Oh9OPJwjvJyovH9olGGKKthdfNd1R_N0a10iojDEl8oDbZt9ks5YvFIrvM-8JH5UDfOafDvAlEr2gGOPzVakLWqwrze7I3fenJUcsRuON6TW3xT70xwo7Y2EWZ5FoE0hIeD2YpLUtXSPkUP0xSLp_kabcOyPn8706wsM_kXlGa63GotL-wMNF9AajGiSQtrriEYLpSmEnHYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=sVW1Q8C6pmcnJauCm_yHvi1idqznwtxEwqxU_YR1w3TTzaBFsO7yqLpb_xWMtCKjq50o0W9vAsF1WECdWzxXPHG0Ma04ZQYruRLTG83oElWeR6sZwNkB6mQXiCNfhMGfyDGYdMewZlQ3In4KzBfIfOS8HmeUyZsakosUO-SB17UtY2S0kmVvn4gXVTSyxzDGE7aCB2ynvQkDAdzDj7sRnNdn-Ff12heUaK1bfDUYhfse5Bl8IvC57ydRa_hUyTmN9zoCoAj7_oyEEUh5tSna967vGceOTnF7wTE3DypkSN2zY2cl1rTKhl6xCA273_VqS4mp1Pq0W3r1vnKIZ51c-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=sVW1Q8C6pmcnJauCm_yHvi1idqznwtxEwqxU_YR1w3TTzaBFsO7yqLpb_xWMtCKjq50o0W9vAsF1WECdWzxXPHG0Ma04ZQYruRLTG83oElWeR6sZwNkB6mQXiCNfhMGfyDGYdMewZlQ3In4KzBfIfOS8HmeUyZsakosUO-SB17UtY2S0kmVvn4gXVTSyxzDGE7aCB2ynvQkDAdzDj7sRnNdn-Ff12heUaK1bfDUYhfse5Bl8IvC57ydRa_hUyTmN9zoCoAj7_oyEEUh5tSna967vGceOTnF7wTE3DypkSN2zY2cl1rTKhl6xCA273_VqS4mp1Pq0W3r1vnKIZ51c-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=m3L1mWLABV_ns9kATs6MK5h38senDc54VF7k52P2MSicaW4QX6cInSQbwG2mAsoVJe-M4mSOUuPocq4pNiZdsGtZyyVSed5PMVqVurkHY_fYVITzot9BvH07J03QWXbOAVC-XPSepeD1YnhhMOOhj7tXu6Gkc_0Y-y4YU3RSURYy0iEUY1bn7FjZvU-Y6wPZwvLqTabCY6q1OjNZkXWTuhpeq7djQOMUm5qdfKIC7GdsXuyjZUsKzb1QpcIJSGi45oVYpIaBJC12LnVdhldSnBlyFo-Vsd7aATXCk-kVLxoY_ikvxYrFEG82efbDkpiu5Y26z634Wp5AipC3WO0zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=m3L1mWLABV_ns9kATs6MK5h38senDc54VF7k52P2MSicaW4QX6cInSQbwG2mAsoVJe-M4mSOUuPocq4pNiZdsGtZyyVSed5PMVqVurkHY_fYVITzot9BvH07J03QWXbOAVC-XPSepeD1YnhhMOOhj7tXu6Gkc_0Y-y4YU3RSURYy0iEUY1bn7FjZvU-Y6wPZwvLqTabCY6q1OjNZkXWTuhpeq7djQOMUm5qdfKIC7GdsXuyjZUsKzb1QpcIJSGi45oVYpIaBJC12LnVdhldSnBlyFo-Vsd7aATXCk-kVLxoY_ikvxYrFEG82efbDkpiu5Y26z634Wp5AipC3WO0zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvA_d-UN0zPkgOIo9tosyINwfBzqOm683Xp5y-uWp2quLjOVCDubpH70o-SRAazYIftr4wv8n6wPBP9NfjpPokcs1JFMSqqlE-Xesz_e_dVPuAWAkJaO8wGojpUw64sHB1rhIPv1X60HFP5o_8hfREJu_23BIQ2X-WceAMvYHvqq_1SmSDS5yqBS66rFflx3EyQ60VCXZFnJ8pEU3TxQvl5R5Ltk6tWrLGG-NoQAkIJOzj8FQqUlPMH_9379jy2nvUTmeYNxUbgTcU5SZ-EFQq3rwXS2vLy3XF4kvJNW8MBRYMAtOh0eNX1y2ihsJqHQsKAsN9CVEvLXuqwdx5QuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pWojT8I7HJAUgKf-NHTGGHTutMRr03WYmhLLapimNhwJSE8N_Sl0DYSQ82jyCpHRg8cq60QdjFiGiafZcdQhAIusb0tcHe6MBkK7oVTAljxr61BeKOgq5CiGwfIoCQl9zR4-X7pHwF2o6ti_TgJea9J8O_PaM4LYdxnQiVZnmRf-rVpOaY86OPZHpuXWYFTw9Pgrx5MAEsvO7SQR35O3Sd9sj0ELTed6joqhePb_pQ-Ywa8-cckqNhVElBtmB9HUEgH45Djlykiw-3lbRAoTlkorQjgsEq7oJmYRpcIR5ZQFgNpjTs-OZv0_OBKZedhMy0WqlkHGmBfvyzj_OQbMuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=S-qyWufuzvhFH57O4AvT2tWS9WMW1tYGWLe4wDIX_gC0whFGQNXlKvMhwtYa4EKRz7iaMPpIqlh50tWlqbfReIL8eVnpPMgXvEXlXeGEXNcnXsXVB80YWw65lIdDhEuFDSAnqIZu0D5l-guB29zOgo3vc0Tl_UW-R2O0m8tdGxhovA-l-d8lRTnTqX5d6d7XRiX95LHWDhfK3XW5Ie3GV0ngAQ2in3mWWI0CT1YTBE5pRZ-EOjD-WegaBjxR5zwlKFtJAPK00_viSWa1tnqw3XbKv-_W2k_oQmhjPQi6Zl5pKbOG6VmR7RD3dCel8c8HIJpRBGD-3DTv0MEr8fTjfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=S-qyWufuzvhFH57O4AvT2tWS9WMW1tYGWLe4wDIX_gC0whFGQNXlKvMhwtYa4EKRz7iaMPpIqlh50tWlqbfReIL8eVnpPMgXvEXlXeGEXNcnXsXVB80YWw65lIdDhEuFDSAnqIZu0D5l-guB29zOgo3vc0Tl_UW-R2O0m8tdGxhovA-l-d8lRTnTqX5d6d7XRiX95LHWDhfK3XW5Ie3GV0ngAQ2in3mWWI0CT1YTBE5pRZ-EOjD-WegaBjxR5zwlKFtJAPK00_viSWa1tnqw3XbKv-_W2k_oQmhjPQi6Zl5pKbOG6VmR7RD3dCel8c8HIJpRBGD-3DTv0MEr8fTjfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=pq7dLaoQU1oAvVd9GJfLCN10k2V950klsr1kQBgh4Lchww95C1-paSxAO0a5sZQBNM69NlHQFa-1GW6o4A3jJT3cqXCQhy7jSPnzHbLEbRLmxMCOqqLaj_FLfrjtrAwQ4DMvqP54LO0WRy2bkTgTUWvYoYTpciKnOADIWBAIb0wY1J0Z4oGaF1OFMwwpXFIIhDNE2FdiVXsuchS0bqcYmagCa1LvqkTljbjs39RkpsL5kcQm_vfWhJF5jITDvqEhyuxVEMIh4VY8WexY4c_53_UOH8pL9SaZzga6lkW1NG1pAYPHJ4s7phjQSElFS-1Vq4UyySlVC2c008AiyUuswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=pq7dLaoQU1oAvVd9GJfLCN10k2V950klsr1kQBgh4Lchww95C1-paSxAO0a5sZQBNM69NlHQFa-1GW6o4A3jJT3cqXCQhy7jSPnzHbLEbRLmxMCOqqLaj_FLfrjtrAwQ4DMvqP54LO0WRy2bkTgTUWvYoYTpciKnOADIWBAIb0wY1J0Z4oGaF1OFMwwpXFIIhDNE2FdiVXsuchS0bqcYmagCa1LvqkTljbjs39RkpsL5kcQm_vfWhJF5jITDvqEhyuxVEMIh4VY8WexY4c_53_UOH8pL9SaZzga6lkW1NG1pAYPHJ4s7phjQSElFS-1Vq4UyySlVC2c008AiyUuswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
