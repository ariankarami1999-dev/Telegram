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
<p>@alonews • 👥 980K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-127010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
انفجار مجدد در بندرعباس</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/127010" target="_blank">📅 01:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
به گزارش آکسیوس، مذاکرات ایران و آمریکا به طور کامل فرو پاشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/127009" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیویورک تایمز:
چشم‌انداز پیشرفت دیپلماتیک در مذاکرات آمریکا و ایران زمانی تیره‌تر شد که یک هیئت میانجی‌گر قطری عصر چهارشنبه بدون هیچ پیشرفتی در مذاکرات، تهران را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/127008" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127007">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گزارشات از تحرکات شدید در اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/127007" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127006">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوووووووری/زود بیایید اینجا
⬇️
https://t.me/+4Sqp5RRoEUE5ZGM0
https://t.me/+4Sqp5RRoEUE5ZGM0</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/127006" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127005">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/فاکس نیوز به نقل از یک مقام ارشد آمریکایی: امشب چندین موج حمله دیگر نیز وجود دارد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/127005" target="_blank">📅 01:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127004">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/فاکس نیوز به نقل از یک مقام ارشد آمریکایی:
امشب چندین موج حمله دیگر نیز وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/127004" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127003">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یه موشک خورده تو فرودگاه بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/127003" target="_blank">📅 01:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
صداوسیما:برخی منابع از رهگیری یک پرتابه کروز دشمن در عسلویه خبر می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/127002" target="_blank">📅 01:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127001">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک مقام آمریکایی به Axios گفت: تمام اهدافی که مورد حمله قرار گرفتند در جنوب ایران هستند و شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/127001" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127000">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام‌های آمریکایی:
هدف از این حملات فشار بر تهران برای امضای توافقه، اما ممکنه به تشدید نظامی منجر بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/127000" target="_blank">📅 01:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13dc5f5965.mp4?token=qXrgo9oMOZWr9O_0p9e55bi_T8wnb4mTZrkhvOKNSJjfF_XE_Mw84LyMFcbb4uJSDciUDOdNFrfBp286z7RFTkPMSS5PpCU5Tw8xtxU3xCPFcr_O0SiV4cFMi06k0HzMpIemNN6RrHwHj_0rzBykwjg9YgSWzkOZ135SHmO5lYcbGTLrnj41RWf7aI_-g0GDIjPpfLNtJrAJuc8FhsAfkTTpHlHv4DeolvSMHXxcf32eJZRhnCEA7ujHGBbkzlHH_HJPXpADbQo7Z8SBNRDdXTNsVm6wGkRwkNot7RE6Af3Luf0RrDLerfC6fJ5SNe79ix6zsemN9FsQlepqB-wzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13dc5f5965.mp4?token=qXrgo9oMOZWr9O_0p9e55bi_T8wnb4mTZrkhvOKNSJjfF_XE_Mw84LyMFcbb4uJSDciUDOdNFrfBp286z7RFTkPMSS5PpCU5Tw8xtxU3xCPFcr_O0SiV4cFMi06k0HzMpIemNN6RrHwHj_0rzBykwjg9YgSWzkOZ135SHmO5lYcbGTLrnj41RWf7aI_-g0GDIjPpfLNtJrAJuc8FhsAfkTTpHlHv4DeolvSMHXxcf32eJZRhnCEA7ujHGBbkzlHH_HJPXpADbQo7Z8SBNRDdXTNsVm6wGkRwkNot7RE6Af3Luf0RrDLerfC6fJ5SNe79ix6zsemN9FsQlepqB-wzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قدرتنمایی جنگنده‌های ارتش جمهوری اسلامی بر فراز تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/126999" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126998">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
طبق گزارش‌ها، پایگاه نیروی دریایی کنگان برای چندمین بار هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/126998" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126997">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/126997" target="_blank">📅 01:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126996">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع شخصی بیشتری را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تجاوز بی‌دلیل و مداوم ایران انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/126996" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126995">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش آماده پیوستن به ایالات متحده در کارزار جدید علیه ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/126995" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126994">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فووووری و رسمی/حملات آمریکا شروع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126994" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126993">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پدافند عسلویه فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/126993" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126992">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رسایی: اینترنت رو فورا قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126992" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126991">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از غرب کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126991" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خط ساحل جنوبی ایران زیر آتش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126989" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انفجار مهیب در میناب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126988" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گزارشات از انفجار های گسترده در برخی از شهر های جنوبی کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/126987" target="_blank">📅 00:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126985" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/126984" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/126983" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری/پدافند غرب تهران فعال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126982" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126981">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی بر فراز عراق درحال پرواز هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126981" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
صدای انفجار در حوالی قشم شنیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/126980" target="_blank">📅 00:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126979">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تسنیم:  ایران به ایالات متحده هشدار داده است که هرگونه اقدام نظامی جدید با پاسخ فوری و قوی روبرو خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126979" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش‌ها از انفجار در کیش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126977" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما از آتش‌بس برای توسعه اطلاعات و به‌روزرسانی بانک اهداف خود در ایران استفاده کردیم
🔴
بانک اهداف و قابلیت‌های فعلی ما بسیار فراتر از آن چیزی است که در آغاز عملیات خشم حماسی وجود داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/126976" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد به تمام شهروندان آمریکایی در عراق هشدار فوری امنیتی صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/126975" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/ترور آلارم: شماره معکوس شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/126974" target="_blank">📅 00:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a221ec730a.mp4?token=k8AdZt1U2hWWwRdxBw3THlajYknIg9DxHVfuK15YGXcvUPbIWsccJzqprEUh_z-__A_2CgFT-iA6FHWNZZUm9SR0YZkNhC35HE9eC33OTM8Hq-pUYHUBIUXfxEa36P51bmforQnpWcbexw76J-HZLfuUrkv5YI1pc3jCI-yorbgxe3KTiqBCZ1JqnXgQH07-qzwhg2BiV-SX4_41DiWOsIELvcU3ZFjpPiTnT_YqZg8832DD3ZxEHhiy6N5j6nby__Adui5-2ENEjOYd3Js-HsHfNawLOU5P-Hp6Kiey3brNhPEP80RHlZ0fM_HL0JDCsyR59WlxT3-jqnkeaSQVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a221ec730a.mp4?token=k8AdZt1U2hWWwRdxBw3THlajYknIg9DxHVfuK15YGXcvUPbIWsccJzqprEUh_z-__A_2CgFT-iA6FHWNZZUm9SR0YZkNhC35HE9eC33OTM8Hq-pUYHUBIUXfxEa36P51bmforQnpWcbexw76J-HZLfuUrkv5YI1pc3jCI-yorbgxe3KTiqBCZ1JqnXgQH07-qzwhg2BiV-SX4_41DiWOsIELvcU3ZFjpPiTnT_YqZg8832DD3ZxEHhiy6N5j6nby__Adui5-2ENEjOYd3Js-HsHfNawLOU5P-Hp6Kiey3brNhPEP80RHlZ0fM_HL0JDCsyR59WlxT3-jqnkeaSQVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ : تپ‌تپ بمب‌هایی که روی تأسیسات کلیدی ایران از طرف ایالات متحده فرود میاد
- و این به این خاطر نیست که ما بخوایم چیزی رو دوباره شروع کنیم که لازم نباشه شروعش کنیم؛
- بلکه چون وزارت جنگ آماده‌ست شرایط رو طوری تنظیم کنه که همون توافقی که رئیس‌جمهور ترامپ انتظار داره بهش برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126973" target="_blank">📅 00:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ایران طرف ضعیف‌تر است و حمله‌ای که امروز یا فردا انجام خواهیم داد، قدرتمند خواهد بود.
🔴
تأسیسات کلیدی در ایران را بمباران خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/126972" target="_blank">📅 00:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر ارتباطات: از سرعت اینترنت راضی نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126971" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ادعای منبع پاکستانی به الحدث: ما امروز از امضای توافقنامه صلح، دور شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126970" target="_blank">📅 00:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126969">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2770689aa.mp4?token=ZrCIH00wS-H7safWmHX44v8OIOA0-31ZTjwG7lqgVSHSBtQD9J_c3fdKEikgmQI_Kn6wOCx9nDRzg15uwHFp7N4Y6Td-ImXYF7TPudrwOMRT8qhh0mkhX8ft9Nk6c6p9OA-Eez_ba2sXayvEEoW-8GOe0ap5WwwA1MZvrt2BX74d4PuLroEr7ppW5QgHl9hPEElTijBFfRWhK6VszYaeyG-OS2xtodJvlFOxFosPrmholdfCE1XatdbKIfq_S4gUdhjNdCXmGLthkQ546Kp58Nuwv96-NxNsDFvtEHXvwYbNvNLadeJk36lSpgLBK4XQT4CpSYoPPpOkwFT7ffEd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2770689aa.mp4?token=ZrCIH00wS-H7safWmHX44v8OIOA0-31ZTjwG7lqgVSHSBtQD9J_c3fdKEikgmQI_Kn6wOCx9nDRzg15uwHFp7N4Y6Td-ImXYF7TPudrwOMRT8qhh0mkhX8ft9Nk6c6p9OA-Eez_ba2sXayvEEoW-8GOe0ap5WwwA1MZvrt2BX74d4PuLroEr7ppW5QgHl9hPEElTijBFfRWhK6VszYaeyG-OS2xtodJvlFOxFosPrmholdfCE1XatdbKIfq_S4gUdhjNdCXmGLthkQ546Kp58Nuwv96-NxNsDFvtEHXvwYbNvNLadeJk36lSpgLBK4XQT4CpSYoPPpOkwFT7ffEd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ؛ هگِستِ : اونا قرار نیست به توافق برسن و ما هم با قدرت روشون فشار میاریم
🔴
سنتکام این کار رو خیلی خوب انجام می‌ده، بهتر از هر کسی تو دنیا، و ما هم همون نتیجه‌ای رو که می‌خوایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/126969" target="_blank">📅 00:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126968">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb62aa25a5.mp4?token=Uhf9rO_nbrw3wZ6RDbUfMn4iAWqyqZb-MxALkaNk2UZlmMjla1ly1pWXnMxZPx83-q3pj5fxK_3HCmOLsFGuR_EXVjr5yctdgzsXmrQ6axnwiXTzEtqiCRYGtMqp1GQXXRy0I3pdMQSWUf1qc1bCoCD3yma3fkf0Ow76jIRKW40-HQ7qtjTM0eGRbNkhsGTPVF7GfIm7MnsoOVZCHs2oHrbNbOvqJ_qm_mlFpIWDKPKgBwGq6qkL8CduRrEge6Of61Xy6IcRIaS3VPoSuSYum8I7_7U3CnRHGLe4k7hkixeGR8h_g11u_nWzlfAIYpJp2mE7XhFzSbfBtPi44q5bDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb62aa25a5.mp4?token=Uhf9rO_nbrw3wZ6RDbUfMn4iAWqyqZb-MxALkaNk2UZlmMjla1ly1pWXnMxZPx83-q3pj5fxK_3HCmOLsFGuR_EXVjr5yctdgzsXmrQ6axnwiXTzEtqiCRYGtMqp1GQXXRy0I3pdMQSWUf1qc1bCoCD3yma3fkf0Ow76jIRKW40-HQ7qtjTM0eGRbNkhsGTPVF7GfIm7MnsoOVZCHs2oHrbNbOvqJ_qm_mlFpIWDKPKgBwGq6qkL8CduRrEge6Of61Xy6IcRIaS3VPoSuSYum8I7_7U3CnRHGLe4k7hkixeGR8h_g11u_nWzlfAIYpJp2mE7XhFzSbfBtPi44q5bDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ خطاب به
سرباز‌های سنتکام
:  این به مأموریت مهمی که شروع کردین و هنوز دارین ادامه‌اش می‌دین؛
🔴
تا مطمئن شین ایران هیچ‌وقت به سلاح هسته‌ای نرسه، باید خیلی افتخار کنید به خودتون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/126968" target="_blank">📅 00:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126967">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
منابع ایرانی به الجزیره گفتند:
«هرگونه حمله منجر به پایان مذاکرات خواهد شد».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/126967" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اکسیوس: دو منبع آمریکایی گفتند: ترامپ بعدازظهر چهارشنبه جلسه‌ای در اتاق وضعیت (Situation Room) برگزار کرد تا درباره حملات احتمالی جدید علیه ایران بحث کند، این جلسه ساعاتی پس از آن برگزار شد که ترامپ به خبرنگاران گفته بود آمریکا «امروز دوباره به سختی به آنها حمله خواهد کرد».
🔴
منابع گفتند یکی از گزینه‌هایی که ترامپ در نظر دارد، انجام عملیاتی با مقیاس بزرگ ولی کوتاه‌مدت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126966" target="_blank">📅 23:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
جی‌دی‌ونس در پاسخ به این سوال که آیا نتانیاهو در نحوه مدیریت رابطه خود با ایالات متحده درباره ایران اشتباهاتی داشته است یا نه گفت: «او قطعاً در برخی موارد اشتباه کرده است.»
🔴
ونس از ارائه نمونه خودداری کرد و گفت این گفت‌وگوها «بهتر است در محافل خصوصی باقی بمانند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/126965" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126964">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
جی‌دی ونس: منافع ایالات متحده و اسرائیل همیشه با یکدیگر همسو نیستند؛ رابطه ترامپ با  نتانیاهو بر سر جنگ ایران تحت فشار قرار گرفته است.
🔴
گاهی ما [و اسرائیل] در یک مسیر و هم‌نظر هستیم و گاهی نیستیم. و هر جا که این دو از هم جدا شوند، ما، باید جانب مردم آمریکا را بگیریم، و همیشه همین کار را می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/126964" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126963">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
آکسیوس: ترامپ در حال بررسی انجام عملیات نظامی جامع و سریع علیه ایران است.‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/126963" target="_blank">📅 23:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126962">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/126962" target="_blank">📅 23:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126961">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126961" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126960">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رئیس جمهور صربستان: من رئیس‌جمهور کشوری هستم که یکی از معدود کشورهای اروپا است که در همکاری و همکاری با اسرائیل تردید ندارد و به طور علنی و آشکار به این موضوع افتخار می‌کند و آن را پنهان نمی‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/126960" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126959">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گوترش: وضعیت کنونی در خاورمیانه می‌تواند به از سرگیری کامل درگیری‌ها منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/126959" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / استرالیا و کانادا از همه شهروندان خود در ایران خواسته‌اند فوراً کشور را ترک کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126958" target="_blank">📅 23:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر ارتباطات از پیامرسان سروش پلاس تمجید و تقدیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126957" target="_blank">📅 23:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126955">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/126955" target="_blank">📅 23:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126954">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/126954" target="_blank">📅 23:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126953">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126953" target="_blank">📅 23:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126952">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126952" target="_blank">📅 23:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126950">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126950" target="_blank">📅 23:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126949">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126949" target="_blank">📅 23:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126948">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رسایی: این عنو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126948" target="_blank">📅 23:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126947">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
باراک راوید: ممکنه مذاکرات ظرف ۲ تا ۳ ساعت آینده به فروپاشی کامل برسه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/126947" target="_blank">📅 22:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126946">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جنگ قطعی هست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126946" target="_blank">📅 22:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126945">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
جنگ قطعی هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126945" target="_blank">📅 22:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126944">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urm_HTUT1-wRDIOeNIEdCtTFVwjhCEnGwBnDbyMk4aOynY2QnacAQbYfcmeobeoa4OvRG8EZb8Eq24XHB-fKy1PODHdcq4dGOMo9ZyyQziDF7HcckJzXwISrKyUaxNRq-vP6Wnh_d1jBuE--QN4GfkVT71FIF0Hdsbq8EffW-EsZqlSp9t-W43v3cyZD9PKtyluaDlNGOGmARO5iCC1awc-FEcJbT5MuRsoNBuiJ_WZA2-IZDtg1KH9FBfC2r2ck-NA0kindYTfYn_k4rNC8X3MzPCb2w_hSIAsjphPynR9jjyNX3bcVL3YOwC7oUWAJRFIXGs8lrkMtM6D-udBLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی: در جنگ چهل‌روزه وسعت آب‌های سرزمینی ایران افزایش یافت؛ در جنگ بعدی شاید وسعت خاک ایران افزایش یابد!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126944" target="_blank">📅 22:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126943">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcuVmA-zOayZUy1kD12EApkiIsbJbFDf2AcVdyb4Xvf-l5oJuMMVHwnTAbFGnEBIhFRAn7H0wmrK2GNgnF6RtFAKcRuJ6eQR2D3ZrVno5WSRY_G8EPVBVMNqyb4oB_RtaDJOpQR-BrvEWIYv2aQ0hxYu0La8SiUEnUD1wMJg_Ye1sUDQ3j97Cuot0LcnoY9js7npMi1Qr5i92NbMD4wIU6h2IGkpI7GNR25CPdcIxpdxZk25ajuL9wIXJ1IyiByv-gJ6JZ5Eo6nDul0tvEO_FdiuDqBxXS2XBacnZXhx85zvjfNgea66IM95lQ4dY_-OJujdiOb6NBRdCRk7fUbZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربى: اشتباه در برنامه فلايت رادار، این هواپيما يک فروند هوایپمای P_8 آمریکایی است و در حال پرواز به سمت قطر می باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/126943" target="_blank">📅 22:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126942">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ادعای یک دیپلمات لبنانی: نتانیاهو جنگ لبنان را تا انتخابات اسرائیل ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126942" target="_blank">📅 22:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126939">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126939" target="_blank">📅 22:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126935">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی: آتش‌سوزی انبار فرش در خیابان ری تهران مهار شد
🔴
نیروهای آتش‌نشانی پایتخت در حال لکه‌گیری در محل حریق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126935" target="_blank">📅 22:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126934">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126934" target="_blank">📅 22:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126933">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس ایران: این بار، جنگ محدود به منطقه نخواهد بود، خواهیم دید چه اتفاقی می‌افتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/126933" target="_blank">📅 22:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126932">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آکسیوس: ایرانی‌ها جلسه سه‌جانبه با آمریکا و قطر رو رد کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/126932" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126931">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmHq_oKyqwkiEADcCRLQA-fzGEjgC5EkFdAP8XnaghQDesIUQ-rvEj1sCOEWpP1FxzoF0rpdJfnKlaNUkxS2hlQMM8do6IDrY1kmFmPjmx8UqL08mePNhXCnUzfM57K46wz3lyaoUNDhIBHqMVBLbsqwE-QscT0fNciQ4gJh9-eCKrRrbgbgBQGR_XiZ2dFloxqotM_PvXBbhzLGMT0dRko5DNucMrlIl_dtD2c5GN2AZYk2_bCVcldI0sYno36QRjIVkKbBc9Ob3BcePEwy0Iku4rtu7Qdj6jkpM2c9ntfzKgH-gY8sjggc7N0jJ38kiyvxCwaIXp8paTiohwcuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواد خیابانی پس از ۳۶ سال از صداسیما خدافظی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126931" target="_blank">📅 21:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126930">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ادعای عبدالخالق عبدالله مشاور سابق بن زاید: امارات در حال هموار کردن راه برای کاهش تنش با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/126930" target="_blank">📅 21:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126929">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هم اکنون ، فعالیت جنگنده، شرق عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/126929" target="_blank">📅 21:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تصاویری از شعله‌های وحشتناک حریق قیام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/126928" target="_blank">📅 21:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فروند هواپیمای سوخت‌رسان هوایی KC-135R و KC-46A نیروی هوایی آمریکا در حال حاضر بر فراز منطقه خلیج فارس و اسرائیل در پرواز هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/126927" target="_blank">📅 21:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / صدای شدید جنگنده در آسمان خرم آباد(لرستان)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/126926" target="_blank">📅 21:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126925">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/126925" target="_blank">📅 21:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126924">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
هم اکنون وزیر جنگ آمریکا در حال حرکت فوری به سمت ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام در فلوریدا می‌باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/126924" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126923">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/وزیر جنگ اسرائیل: کارزار علیه ایران تمام نشده است و ما آماده از سرگیری درگیری ها هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/126923" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126922">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ به سازمان رادیو و تلویزیون اسرائیل: جنگ با ایران به طور ممتاز پیش می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/126922" target="_blank">📅 21:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126921">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/126921" target="_blank">📅 21:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126920">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcqiinN_MStmKeUnoepd1gs1aFvcjpqQanz5WpC4VV8tbQJm5I-DWCZd7PFzq-c22b_jcxyJ2vfIFinANTIWLYym5Mgm6d6AYvCsCncNS-n9JmO4j1fS83pfrsmwxmv-ZXYCGhazULaRCyWiQG5r2G9R46_Du9TTS75ycuCQBz4wVQ3-9SLH0SeRlVPqDg37pk7du2JjryX5a1URjXI_Rp78yS04OwMSIlpBd5B4MGLsSY9Dan4uZuVnDJfHHIv_OVRBHLXM4KMCn_m6ErbVUUlLCFJe3nOtn6tOS21JIKEFyvfqVkbKmh3r3Rc-K-L3h4b7v9M9OBVLDI4mK4C65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یدونه هواپیما ترابری C-5M Super Galaxy هم از اروپا حرکت کرده بود الان تو آسمان عربستانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126920" target="_blank">📅 21:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126919">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYDgPwC8-URECFw4zXhFjuV-AwEwhSU1KfYnHUeWi13PkX8v7-Q1EW7IVFYTLeaxH9th4HjUNloXB051iiicM3iZUbquAbD349Nc1ZvRR4dITcRrR2ic1d6xXSh5I30Uz_r2Ogc3F8Q3if2Zcf1eGIO02cCy7dfNIpUq7Cp3Sc5aRhGJZuU2lHlALNBpDgsoo87o5tFdqdLLJA0fbwJp3YiIxzCCt6pKcoZkwFQ9Vm2rlYbKD8tGWcYLDNFfuT9pf64ob_8MH7v7rbisWNdlLEF6LLQmCOcyBL7BOW3bxMamnNJ-Mgn1wioaV3AzCa2WaCK6RtJbXXeksctCkUYsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون یک فروند بمب‌افکن B-52 در حال پرواز بر فراز عربستان و حرکت به سمت خلیج فارس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126919" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126918">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuEPI0SnjE37mnLmmozkXxPvNjtq56cgfo-ImlJzf6Y4q0ChvzD13x0I2Tg612pEHekiMNvwL5-rQmLJRkwgcg9xcG8MdZ55tSyANHr_YRnGWHrt0aYcYxbWcIFon7Smuw-8i9UQSGI2Ks45jRDlgGgEv-UfwHm-OqCmefkLeoce5-IZICTTsEINwifHpO4hvT1VxIzqh5XD5-s6OioExJdGKg_FTKuA1BK051mn3evHskUWrEZdJil7xhlA38kvn-u9IRdG4BLE9y5GGlYJGlsw0Gv8DiQIzsoTm3VpsJb5G1KJrZACWYRRbSyYPjQM4xmCPVYxVoywcUI6Njva4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تبریک به نیکول پاشینیان برای پیروزی قاطع او در انتخابات ملی ارمنستان. من بسیار افتخار می‌کنم که از او برای انتخاب مجدد حمایت کرده‌ام و شک ندارم که با او به عنوان رهبر کشور زیبای ارمنستان، به سطوحی از بزرگی و موفقیت فراتر از هر انتظاری دست خواهد یافت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/126918" target="_blank">📅 21:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126917">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر انرژی آمریکا رایت، در پاسخ به سوال درباره اظهارات ترامپ، می‌گوید از خارج کردن نفت از ایران توسط آمریکا مطلع نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126917" target="_blank">📅 21:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126916">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
آکسیوس: ترامپ پس از سرنگونی یک هلیکوپتر آمریکایی، حمله به ایران را دستور داد، اما مقامات می‌گویند خشم او به دلیل عدم پاسخ تهران به آخرین پیشنهادش، تقریباً دو هفته بود که در حال افزایش بود.
🔴
این حملات طوری طراحی شده بودند که بدون ایجاد تلفات انسانی یا به هم ریختن دیپلماسی، اهرم فشار را بازگردانند.
🔴
حتی در حالی که نیروهای آمریکایی به سیستم‌های نظامی ایران حمله می‌کردند، میانجی‌گران قطری گفتگوهای خود را برای احیای مذاکرات ادامه دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/126916" target="_blank">📅 21:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126915">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126915" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126914">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGXlogEJy9CZggSFS4cuLCFzq5m1nc8tttw-WfYHGxPXuxsa9GLoQxyTQ75SFwn0el1LVt87vpa6Jx5bMcmPYq3SNFbw5cyniYbFiaWK9A0ANIJOlY2XtBlFNkQOPFfX-8xdOb-GzLU-K7yqcZlhZH0k1ArCprplCnHklbau4bfZa8smSN3Ywu4LwSVU2Y4DLlEN4smFEp3GAQqn_mWJdSQwV8zmL4uIorzITRzxuu6AblfRQ5GXetgYSf2QEeD0wM-UHdlKYA4U7TjW87e5Urx5-JZ8oJwtytFWOBmdzhHLdToJuXWIfEs-lU0N-hvdfUqm9bPnosmff4PCc2WzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفیر آمریکا تو اسرائیل هاکبی :
احتمالاً اوضاع تو منطقه به‌زودی یه کم داغ و ملتهب می‌شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/126914" target="_blank">📅 20:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ خطاب به سازمان رادیو و تلویزیون اسرائیل: ما در حال پیشرفت عالی با ایران هستیم
🔴
بدون من، اسرائیل وجود نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/126913" target="_blank">📅 20:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/126912" target="_blank">📅 20:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHofscjsESmQxlzXsI8kikab18TUqHee8Yy0xPW0U9lLhYdI62JRZ3jg-Bw0LA4mJnYouIngsGheO6lbU_-nznLeSvtUQNfmU43i3ZiYwk_A6ChBEjhtgotyL6T68VegJJEL0ZVWrA9XZ4h0DykS3XdgszM9sD0oWGyILWi59KkHEqNLKWH-2s5H9JtwhEF10U9qYgvNDt8IyrU7MWCpbsrjVTgOTI7kuqulfYAi9f0vjP0IWec1rfSIT9yPsLze0HpSCi5XEH-Ki_veZtKX7uatADC7XjkhasU5pldol-0ekZekk-O5mTaQKLgA2LRatncs-KU_m4u3TZHChjOU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون / آتش‌سوزی در انبار کالا در میدان قیام
🔴
انبار فرش ، جنب پمپ بنزین پل ری!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/126911" target="_blank">📅 20:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
حنظله تهدید کرد !
🔴
گروه هکری حنظله: به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند
🔴
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست. ضربهٔ ساعت‌های آینده تلخ خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126910" target="_blank">📅 20:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126909" target="_blank">📅 20:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GARPYx6-t_uTUX6h8QM4ntTfjDT7uKb_bO8TmRE6cAiB6Jq5z2FRgnQMz95kq8IVVXJbbIRNLKhA1bmPGTQJiZ-xg58wZo4pPwDNMB4pO647uOJj7vhLJS9UNEDrY6oEGyXcIaFu3VkYxDVbffec8YN6KeJd8QNuKAX5sVzbu7NlTDVVBOnPxDQkLYfP6DgVv8i79MNzqvucFzYWq16KMF-pK7LzrYagkL_QjkQ_b8t70SvLDBGBePZqfn_iI2lXY_wy5BStQFBrv5LTZQvXxIzfSAqmTKjkARA-n5YIo3NOl0uw0YFK5zo0MBBJPvw5vqllQhERbV9EuBAzxdGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش سوزی وسیع خیابان قیام تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/126908" target="_blank">📅 20:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMIi1B3V0UdgUTKPzXv2tvCw7bWz7FwZyZZZmAM8bU-pdeFOx2Gu7UAIwUVUgIUviJdTUqZtbjNYBacBvyUngBKDSfRT1TyYvnZjXAUKxyxYi2YDG4LdxtZRfALEANJmMtGHy3mMbgJJpOFrA6QozSNt9VnpZufid0J2y5bjyspRrJCVnLuXLX4EKJnuuf9mIn8SAxHeN8QultDfW1gx6bNQeYU3yqpHiEkeRB96exn3BjjGCulKMPa11Qh3zYk8KWMgIc3GgfzRDxaIWKQ67QrskDfqqmJDXkEekzFjYDrugYjMUQ6qiOazLE_9Ult__ZLvDPFCBHMw1jgk9fzNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: زیرساخت‌های حیاتی شریان حیات مردم هستند. تهدید به هدف قرار دادن آن‌ها — از شبکه‌های حمل‌ونقل تا صنایع برق و آب — نشانه قدرت نیست، بلکه نشانه‌ای از ناامیدی در برابر اراده یک ملت است.
🔴
ایران، با تکیه بر دانش و توانایی متخصصان خود، وحدت ملی و همبستگی، در برابر هرگونه فشار یا تهدید استوار خواهد ایستاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126907" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126906">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126906" target="_blank">📅 20:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تسنیم: ترامپ باز هم از ضربات کوبنده ایران عبرت نگرفته است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/126905" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU44Tv04NH58WAGNjguzFZdFxRMqeMO1nt1FRniRH6pltEko38py2vExVgMX5lSKNBktm35CIYkJaGncThvLS6h20mxRUxavqVRI9Ru46dn6k0CqfzM9KYJw5a4ezm7nRqqAOKbkwEz5A6MGo8BeAfrteALoFizH5bIGMzC3UFI-oL1ZCSU-PzujolnOJj4mbsWgaSTj31ISMq76gTFOQCMAw9hNCGuf7AJawhuYiWOhnTl8kfaTk_NSTftg_4wsj18SxW-JqvsK5sTy1_hvEgeAZN62zddycfjAO-v2leb6TsgHb_f7ekEYefyEA9hR5StNhUI5Q50jqYiYED24Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126902" target="_blank">📅 20:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126901" target="_blank">📅 20:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز: هند معاون رئیس هیئت دیپلماتیک آمریکا در دهلی نو را در پی حمله به یک نفتکش در نزدیکی سواحل عمان احضار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126900" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ستاد فرماندهی مرکزی ایالات متحده: از زمان آغاز محاصره تنگه هرمز، تاکنون مسیر ۸ کشتی را مختل و ۱۳۴ کشتی را تغییر مسیر داده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/126899" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
