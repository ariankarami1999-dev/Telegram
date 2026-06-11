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
<img src="https://cdn4.telesco.pe/file/saS_byGfp5reUzvtezGUiLIjiag-wyM3dtgQRCrOBTgeu_nB2CLFMglZST77btbGtLzRkRb9tFcT-Bveq5KcbiYGQVrmMiYpfyDVSYVgsgHfobQXGVinItapqJMNanNnE6TzRr3PMKieIVEO8LNDs7jUxEH_ksnzDa5a9gqnjsDeYqyDWBqXXiiUUM9Xe2HifLh55PxnbvwLZVC-jhNug1Nq95DVGPxJgEha41ZrxMiTbV4KHiLzEXxY537FcOzJVJ3qy04ZooDLVh_Y7p95b-eW8TNlf-1rVr4kHpmnciv0crSJYLGNH32lk-gS6WR1f3vZtCIyfU72paFBzq-VsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-17359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SBoxxx/17359" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرنگار: پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟  ترامپ: چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SBoxxx/17358" target="_blank">📅 00:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرنگار:
پیش‌تر گفته‌اید که ایران و ایالات متحده به یک توافق نزدیک بوده‌اند. هنوز اتفاق نیفتاده است. چرا این بار آن‌قدر مطمئن هستید که شرایط متفاوت است؟
ترامپ:
چون آن‌ها کتک خورده‌اند. آن‌ها کتکی خورده‌اند که خیلی کم‌کسی می‌تواند تحمل کند. و آن‌ها بسیار بیشتر از من می‌خواهند که توافقی صورت گیرد.</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SBoxxx/17357" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-poll">
<h4>📊 به نظر شما:</h4>
<ul>
<li>✓ توافق شده طبق آنچه نتانیاهو می‌گوید (تسلیم کامل ایران)</li>
<li>✓ توافق شده طبق آنچه سپاه دیکته کرده (تحقق همه شروط ایران)</li>
<li>✓ توافق نشده</li>
<li>✓ نمیدانم؛ اطلاعی ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/17356" target="_blank">📅 00:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل نتانیاهو: توافق شامل  محدود کردن تولید موشک و پایان حمایت از نیروهای نیابتی منطقه‌ای   می‌شود</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SBoxxx/17355" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فوری | وزارت امور خارجه ایران: ایران ثابت کرده است که آنچه را که به عنوان خطوط قرمز خود تعریف کرده است، تحمل نمی‌کند.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/17354" target="_blank">📅 00:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!  از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/17353" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، اسماعیل بقایی:
تا کنون، ایران به نتیجه نهایی در خصوص توافق نرسیده است.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/17352" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالب است که ترامپ می‌گوید خودشان تنگه هرمز را پیشتر باز کرده اند و ما خبر نداشتیم اما الان گفت که بعد از امضای توافق با ایران تنگه باز خواهدشد!</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/17351" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6D0Lpr6v8zdK__kxpMog4lYXxqZOcuhK_fbEOf9A7HN8bArJ8g5z_e76LqB39hB8MeJfCZf06fAFnDnDgUBt3sYDHNa1JmqK3iomxaj3EOfKZOxXS8OOm0_fh29SXK-7yu5uW68ntU3DYv9dUYuIIiyWNAV5UfeQFDKzbDEpE81bldhLpIi0O-3bZGi-rAaU5mQpIEiNthJJCGvGeL4GDR7zxeBO_1jWE_ylkzKgmH4Ew3uSe1PHQ3ChVWPuvM6rDYxzaRyYUXjiP4Qzp8NthczhpIWUsEkA6SuqAguXt0znj3YoC9jCGbGE2762MOxtUkQOiSIeKW1_g8csFaRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر می‌رسد که شرایط توافق با ۱۰ شرطی که جانفدایان میگفتند خیلی شباهت ندارد!
از توجه شما به این موضوع سپاسگزارم !</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/17350" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دفتر نخست وزیر اسرائیل، نتانیاهو: توافق نهایی شامل خروج مواد غنی شده نیز خواهد بود.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/17349" target="_blank">📅 23:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ:   اخیراً ایران را به‌ شدت بمباران کردیم و رهبرانش حتی بیشتر از من خواهان رسیدن به توافق بودند.  ما از همان ابتدا در جنگ با ایران پیروز شدیم، ایرانی‌ ها فرصت دارند کشورشان را بازسازی کنند، چرا که به‌ شدت ویران شده است</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17348" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!   تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/17347" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عصر گفت رهبر ایران موافقت کرده حالا می‌گوید «برداشت» من است که موافقت کرده!
تف به خودت و برداشت ت</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/17346" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فوری | ترامپ: امضای توافق به زودی انجام خواهد شد و برداشت من این است که رهبر ایران با آن موافقت کرده است.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/17345" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فوری | ترامپ: امضای توافق به زودی انجام خواهد شد و برداشت من این است که رهبر ایران با آن موافقت کرده است.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/17344" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بالاخره محاصره را برمیدارد یا نه؟!</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/17343" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فوری | ترامپ: محاصره دریایی تا زمان نهایی شدن توافق پابرجا و معتبر خواهد بود و تاریخ و مکان امضای آن به زودی اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/17342" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
ادعای فارس: احتمالا مقامات ایران با توجه به عقب نشینی آمریکا توافق را بپذیرند</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/17341" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»   – نیویورک تایمز</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17340" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قبل از اینکه ترامپ حملات علیه ایران را لغو کند، با پاکستانی‌ها تماس گرفته شد که ادعا کردند «ما با ایران توافق داریم»
–
نیویورک تایمز</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/17339" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">— منبعی نزدیک به تیم مذاکره‌کننده ایرانی به خبرگزاری فارس گفت:
«هیچ متنی برای تفاهم‌نامه اولیه با آمریکا تصویب نشده است».</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/17338" target="_blank">📅 21:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منابع اسرائیلی و عرب های خلیج فارس که با کانال ۱۳ اسرائیل صحبت کردند، گفتند که از هرگونه توافق حاصل شده با ایران آگاه نیستند.</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/17337" target="_blank">📅 21:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17336">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17336" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17335">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرگزاری تسنیم:  «ترامپ اخیراً ۳۸ بار ادعا کرده است که توافق قریب‌الوقوع است، بنابراین تا زمانی که ایران رسماً اعلام نکند، ادعاهای او را باید صرفاً در چارچوب دروغ‌های قبلی‌اش بررسی کرد.»</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17335" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">باز کله زرد حرامزاده دروغ می‌گوید  محال است سپاه چنین توافق ذلت باری را بپذیرد</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17334" target="_blank">📅 21:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17333">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوری | ترامپ: محاصره دریایی تا زمان نهایی شدن توافق پابرجا و معتبر خواهد بود و تاریخ و مکان امضای آن به زودی اعلام خواهد شد.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17333" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17332">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: «با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و مورد تأیید قرار گرفته است، من به‌عنوان رئیس‌جمهور ایالات متحده آمریکا حملات و بمباران‌هایی را که برای امشب علیه ایران برنامه‌ریزی شده بود لغو کردم. همچنین مباحث و جزئیات…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17332" target="_blank">📅 21:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: «با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و مورد تأیید قرار گرفته است، من به‌عنوان رئیس‌جمهور ایالات متحده آمریکا حملات و بمباران‌هایی را که برای امشب علیه ایران برنامه‌ریزی شده بود لغو کردم. همچنین مباحث و جزئیات نهایی این توافق به تأیید تمامی طرف‌های ذی‌ربط، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران رسیده است. محاصره دریایی تا زمان نهایی شدن این توافق همچنان به‌طور کامل برقرار خواهد ماند و زمان و مکان امضای آن به‌زودی اعلام خواهد شد.»</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17331" target="_blank">📅 21:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">زیمنس انرژی:
جنگ ایران به رونق آلومینیوم افزوده است زیرا تقاضا برای توربین‌های گازی بیشتر شده است.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17330" target="_blank">📅 20:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو:  امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم که اگر حزب‌الله به حمله به شهرها و شهروندان ما پایان ندهد، اسرائیل به اهداف تروریستی در بیروت حمله خواهد کرد.  این موضع ما بدون تغییر باقی می‌ماند.  در عین حال، ارتش اسرائیل طبق برنامه در جنوب لبنان…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17329" target="_blank">📅 19:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzRkjeMP0tfZDnKbBQ9UqZd_pdSSvVszXgdHYY9Zk6wjA3ss-nZOPAmOs3CxapoIXjymkjHDYT_w3AtN-6ZCP0cbDLs_LAtIaryhalU5m0O5Rd0zRzsoxWqpVd5NmIWMkvvheWT6uGW5BzPEwfdRxgEQuC81CugqY1_p-aP5P2W_h5nvqe6l-xt0tASu64dOCOYG1PhkwvFhNU1o6TJ2vii2njUYK1gR1JTPaNR6KJlsAdjvwk-MC9UVaDStM4OOSpNrCIuvnVYCbEcdrFaVB7huT1M3srW6iy-mP2A8B5lQy3ChvlUF22mvJ5xZgO1SLHKulKzBDFPGtMuIwgkY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17328" target="_blank">📅 19:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkd1iwu_ejjA20ArMYxXZy4_DGcXUJyGaKv_tv2qkdVXewsjptsa0r-ygnYr97qs9Rz5eGQ3UMPLbowD-tMKbycJx4KNteSCjS9QY6Npl3AIUQxFDINRrPXg9yOeS9PA0DpuASErBVX2WKMPL2JAqJ7uvPxJ54ppXz9HjBiOV3PFnBgbkbzkLnWQOsevEfihKpwr4hXm4cUNlj_XVIkMzMSdwsEHhcfl9TzWMJRjCNCNXyKDG0m0PT-An7iTaaQuJPgStJgE4cKbfX2iNvERygdT5W5jDBgv7HwwR42S_6mY8vlx1Fdy4NbJkSTDaPWfjLV6ULW3NUeP01n-zvqsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بحران ذخایر استراتژیک در واشینگتن؛ تاجیکستان کلید حل بن‌بست تسلیحاتی آمریکا در برابر ایران
⬅️
گزارش‌های اخیر رسانه‌های آمریکایی، از جمله ان‌بی‌سی نیوز (NBC News)، از نگرانی عمیق مقامات دفاعی این کشور پرده برداشته است. بر اساس این تحلیل‌ها، واشینگتن در…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17327" target="_blank">📅 19:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9mgsaiUwNgf4ktF5vTOh8f_CkzyCq0R1cdC3Uv6lwYF2hBfzRGBHMfGi2CA2hrbA6K6D32cwCiO8YGNX_djRkq2tvWjNNBfkOs0NEZh4SFb1fzOkxwX9-we-F-eCLX_TmbONyShNjVSCcMOT3HQaJfb0rN2-e_P3zvnK45To-XovoKLWhwlRaqdIKitpf82OY9gB4e-atm5adRxCONzsh3oBJM-6raLiOLinCdDz8x8Y1TKJsYk8QQb1UHebFMjF6ddbdUjlf4jO6wXIyDrns6i8sQRx914J6WwvtNi1eqrnax4okSDJx7u4GKpx9bdP2ojJTucsrDceuJGd_rE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17326" target="_blank">📅 19:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
انتظار می‌رود که لشکر ۸۲ هوابرد ارتش آمریکا که به «لشکر شیطان» معروف است، به زودی کنترل جزایر نفتی ایران را به دست گیرد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/17325" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/17324" target="_blank">📅 18:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
همکاری مایکروسافت و استارلینک؛ اینترنت ماهواره‌ای در اختیار جوامع بیشتری قرار می‌گیرد
🔹
مایکروسافت همکاری جدیدی با سرویس اینترنت ماهواره‌ای استارلینک اعلام کرده تا دسترسی به اینترنت در مناطق مختلف جهان را گسترش دهد.   این همکاری شامل استفاده از اتصال ماهواره‌ای…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17323" target="_blank">📅 18:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV8GxLbdaijQxXEZBp_Wp-XUjmtWkfL28F939tojbcZ2YqqBsaUrR0W16wEANrZrfZlBZBD-D1l9CNP5pPJegGRgqsBgH3fK71WtvKsFHnR_wbh3Be41Q_WCjYPc_GzCH5jOiVhetmVbSVcrqU7hg4yIIJko_1vORgDg_FzyAk1q5brQbnnNHyyUF6wdL1gKTnDNxJeCySis5Nvwo4T70NJEpLTI9Dgxuax_P-jvw9pkm7-in63K1iym29KvE-m3E5jIK1eKSYfWvAmYUafx1yMr9eJepcesOUoWWoAfLaOUHBR4TfoEsBac0CUUvrVKLQNw_6ov4CPRHSytrQvUpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17322" target="_blank">📅 18:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ،   «هواپیماهای آمریکایی بر فراز تهران پرواز می‌کنند و خودشان خبر ندارند».</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17321" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ،
«هواپیماهای آمریکایی بر فراز تهران پرواز می‌کنند و خودشان خبر ندارند».</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17320" target="_blank">📅 16:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاش جای جراد کوشنر بودم…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17319" target="_blank">📅 16:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فوری | ترامپ به شبکه فاکس نیوز: ما هنوز به ایران به اندازه کافی ضربه نزده‌ایم.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17318" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17316" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده بسنت:   هر عوارضی که به سازمان مدیریت  تنگه هرمز پرداخت شود، از حساب‌های مسدودشده آن‌ها کسر خواهد شد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17315" target="_blank">📅 16:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:   «من این را به‌طور خاص به عمان می‌گویم؛ ایالات متحده با هر کشوری که به ایران در وضع عوارض در تنگه هرمز کمک کند، قاطعانه برخورد خواهد کرد.»</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17314" target="_blank">📅 16:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17313" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مثلاً ما میگوییم همه اقداماتمان برای ظهور امام زمان است. یا اردوغان میگوید برای اتحاد دنیای اسلام است. روسها میگفتند برای دولت جهانی پرولتاریا!
این قرمساق میگوید نفت تان را می خواهم.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17312" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ:  امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!  «ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!)…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17311" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ:
امشب به ایران حمله سنگینی میکنیم و در آینده نزدیک جزیره خارک را تصرف خواهیم کرد!
«ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار شدیدی خواهد زد.
در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.»</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17310" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از انفجارها در منطقه دریایی نزدیک به شهر سیریک منتشر شده است.
تا کنون بیانیه رسمی صادر نشده است، اما به نظر می‌رسد صداها مربوط به درگیری‌ها یا تبادل آتش جاری در خلیج فارس و تنگه هرمز باشد.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17309" target="_blank">📅 15:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر امور خارجه ترکیه از ایران و ایالات متحده خواست تا حملات تازه را متوقف کرده و به مذاکرات بازگردند.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17308" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17307" target="_blank">📅 14:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17306" target="_blank">📅 13:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حمله آمریکایی ها به 3 کشتی هندی دیگر!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17305" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">در این نشست گفته بودم که جنگ بعدی در سوریه میان اسراییل و ترکیه خواهدبود.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17304" target="_blank">📅 13:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پایان جمهوری ترکیه.pdf</div>
  <div class="tg-doc-extra">236.3 KB</div>
</div>
<a href="https://t.me/SBoxxx/17303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وزیر دفاع اسراییل:  به وزیر کشور ترکیه که تهدید می‌کند و رویای حکومت بر اورشلیم را در سر می‌پروراند - این را می‌گویم: اورشلیم قسطنطنیه نیست، و کشور اسرائیل امپراتوری صلیبی در حال فروپاشی نیست، بلکه کشوری قوی و مصمم است که توانایی خود را در دفاع از خود در برابر…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17303" target="_blank">📅 13:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17302" target="_blank">📅 13:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🇺🇸امریکانا🇺🇸</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=swtdIqpYG9H_uml8sXWZrPY5Bws-Rio9HSHzRYszJuEmjUHNKsgEeSsvLKQ5Wg2pmMKcAZm48bkxqHaVZe0bnyhGBcTq03mWc2YbD2reoUViSVtm4Kvln1cuUhgM8P7Jh9fYGR2P9eTAGPkzaQs6redI3Zul7g9xdOOlsuLDEiqbWptEYPwziTC3lnH6NXDv2VQVZw03qgCUSfNrVNOm57ITebjz7rjsb2QSCgVRy5QQ31a_v-N8Q7SjGvKMEsmGZanJvi6tYPRmCiyc0HhH735lQkqiyzuA22fO-3YhLJI-038j-cGEb8S8x82N0KsfPyhfpdbmb2wqCtM-Zo1HLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=swtdIqpYG9H_uml8sXWZrPY5Bws-Rio9HSHzRYszJuEmjUHNKsgEeSsvLKQ5Wg2pmMKcAZm48bkxqHaVZe0bnyhGBcTq03mWc2YbD2reoUViSVtm4Kvln1cuUhgM8P7Jh9fYGR2P9eTAGPkzaQs6redI3Zul7g9xdOOlsuLDEiqbWptEYPwziTC3lnH6NXDv2VQVZw03qgCUSfNrVNOm57ITebjz7rjsb2QSCgVRy5QQ31a_v-N8Q7SjGvKMEsmGZanJvi6tYPRmCiyc0HhH735lQkqiyzuA22fO-3YhLJI-038j-cGEb8S8x82N0KsfPyhfpdbmb2wqCtM-Zo1HLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تهدید تلویحی ایران به حمله اتمی / کیث کلوگ، مشاور سابق ترامپ:
«داشتن یک جنگ طولانی مدت، روش جنگی آمریکایی نیست. ما باید به روشی که در جنگ جهانی دوم و جنگ جهانی اول انجام دادیم برگردیم و کار را تمام کنیم، آنها را نابود کنیم.»
🆔
@Americana_ir</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17301" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سقوط بالگرد پاکستان با 22 کشته!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17300" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سردار فدوی، مشاور فرمانده سپاه: در آستانه پیروزی عظیمی قرار داریم!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17299" target="_blank">📅 12:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">مقامات ایرانی می‌گویند یک کشتی باری از شهرستان سیریک در هرمزگان، ایران، صبح امروز در دریای عمان توسط «پرتابۀ دشمن آمریکایی» هدف قرار گرفته است.
آنها گفتند این کشتی ۱۵۰ تنی که از خاصب به سمت سیریک در حرکت بود، حدود ۵ مایل از بندر خاصب مورد اصابت قرار گرفت. ۵ خدمه آن توسط کشتی‌های عبوری نجات یافته و به عمان منتقل شدند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17298" target="_blank">📅 11:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چیزی که امروز گفتم این بود که دقت پرتابه های ایران در جنگ اخیر نسبت به جنگ پارسال یا عملیات های وعده صادق-1 و 2  به صورت جهشی افزایش یافته و این یعنی جنگ سختی خواهدبود.  و اتفاقاً همین کار را ترسناک تر می کند چون آمریکایی ها معمولاً وقتی کارشان در جنگ گره…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17297" target="_blank">📅 10:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این ترحمه مقاله سیمور هارش — روزنامه نگار معروف — است درباره نشت اطلاعاتی مبتنی بر گرایش ترامپ به استفاده از سلاح هسته ای!  دقیقاً در راستای مطالبی که گفته شد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17296" target="_blank">📅 10:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چقدر ترامپ جنگ در ایران را تشدید خواهد کرد؟ یک منبع مطلع از کاخ سفید می‌گوید رئیس‌جمهور گزینه هسته‌ای را مطرح کرده است  چهار ماه پس از آغاز یک جنگ هوایی دشوار با ایران، محبوبیت دونالد ترامپ رئیس‌جمهور آمریکا در میان رأی‌دهندگان آمریکایی در حال کاهش است. به…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17295" target="_blank">📅 09:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK8J2hEDTJbeV0BEz_-24tFcUjvsB_S6UDrHO6C2enREzsJDOZTxxjUknBSc454OwHEHtViUgVe6q6cjHO7Cbb4c_zfiTxElHOaGfgqQkqxyrkaJBv7FISrCaPxF-wBZOM9hmZbkAQ5UVt8aKDWuLUG23UxR5ezWFF6g3_J_QnPyw7M5OQu-kPp3r_uFQcpC0NGHQ8pfbBxSHrJ0GV3H57p5P33EMh4xvsYmv2DTx7IznKwPkSrcdm-FpDfbglqdvPzTLjl_WG3eMFQ6OKYttbOR3OrxrBi_AeiAemPE55R2eh0BdoM-7EJTN7Hq31SToxPqzrQjUx_2jMGSwMxInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی که امروز گفتم این بود که دقت پرتابه های ایران در جنگ اخیر نسبت به جنگ پارسال یا عملیات های وعده صادق-1 و 2  به صورت جهشی افزایش یافته و این یعنی جنگ سختی خواهدبود.  و اتفاقاً همین کار را ترسناک تر می کند چون آمریکایی ها معمولاً وقتی کارشان در جنگ گره…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17293" target="_blank">📅 09:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دقایقی پیش انفجاری در نزدیکی سفارت آمریکا در بغداد روی داده است.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17292" target="_blank">📅 08:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUqF_Dt9EDWY7Z_Io4xSIjpQ2HO2KTltKazcwNVOiun0g6NDKTCjLugPU2Emo6jHK2V4G_FjrEkrPC8F_rJvzP6Zu1LdmL1iLB_Wf_iXNpKN1BIAskwN9mnmDDeMP6B_t4CwTu6-LskSJOsVO4LfluOnD9aenFt09ZsEp64YBx4iF16-1KRThAwSO1zd3AEspJe2lYGGk78aFwqDt16ON5_T8NaWgLqOg1JvwltNT9ulewA_DXSONcEQFZL-iLuHBFv4BGp6LQ-yqoYDwQpJmanOUqREdLqJJDuD7achcHO0ANHPcldJirnbMRThFHK-o-6HELgX5G0zYcHHlJ0A2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندی ها بدون نام بردن از آمریکا حمله به نفتکش را محکوم کرده اند و گفته اند از ۲۴ سرنشین آن، دقیقا ۰۳ نفرشان گم شده اند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17291" target="_blank">📅 08:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محل استقرار جنگنده های F35، F15، F16 آمریکایی منهدم شد
سپاه پاسداران انقلاب اسلامی:
مردم مومن و قهرمان ایران که با بیش از صد روز ایستادگی در میدان حماسه آفرینی و نصاب جدیدی از بصیرت و مقاومت را به نمایش گذاشتید؛
به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، فرزندان دلیر شما در نیروی هوافضای سپاه در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا برای تنبیه متجاوز، صبح امروز با ۱۲ فروند موشک بالستیک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین تاسیسات مهم ارتش تروریستی آمریکا واقع در پایگاه هوایی و مرکز کنترل الازرق را هدف قرار داده و آن تاسیسات و مقدار زیادی از جنگنده‌ها را منهدم کردند. عملیات رزمندگان اسلام تا زمان ادامه شرارت‌های دشمن ادامه دارد.
و ماالنصر الا من عند الله العزیز الحکیم</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17290" target="_blank">📅 08:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">— مرکز فرماندهی مرکزی ایالات متحده پایان حملات آمریکا علیه ایران را اعلام کرد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17289" target="_blank">📅 04:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارهای شدید در بحرین</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17288" target="_blank">📅 04:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرماندار اشتهارد:
صداهای انفجار احتمالا مربوط به انفجارها در خارج از استان از جمله ملارد تهران است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17287" target="_blank">📅 04:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سردار موسوی:
تنگه مقدس هرمز را ناامن می‌کنید؟! منطقه را برایتان جهنم می‌کنیم</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17286" target="_blank">📅 04:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آیا ایران در صورت حمله آمریکا، کارت برنده هسته‌ای دارد؟
پپه اسکوبار گزارش می‌دهد که اگر ایالات متحده جنگ علیه ایران را از سر بگیرد، جمهوری اسلامی می‌تواند به سرعت برای انفجار یک وسیله هسته‌ای در خاک خود اقدام کند؛ نه به عنوان یک اقدام جنگی، بلکه به عنوان یک نمایش غیرقابل برگشت و مستقل از توانایی کنترل تسلط تشدید تنش.
یک سوال واضح: آیا ایران می‌تواند در صورت لزوم به سرعت یک بمب هسته‌ای بسازد؟
به گفته استاد MIT، تد پاستول، ایران در حال حاضر مواد کافی (۴۵۰ کیلوگرم اورانیوم ۶۵٪) برای تبدیل آن به سوخت درجه تسلیحاتی برای یک بمب هسته‌ای کوچک دارد. و با همین مواد، آنها می‌توانند حداقل ۱۰ بمب از این نوع بسازند - به اندازه‌ای کوچک که روی موشک‌هایی که می‌توانند به اسرائیل برسند، نصب شوند.
چگونه؟ با استفاده از یک ترفند ساده: پیچیدن هسته هسته‌ای در یک "بازتابنده نوترونی" (ساخته شده از اورانیوم ضعیف شده یا سایر فلزات). این کار نوترون‌ها را به هسته بازمی‌گرداند و واکنش را کارآمدتر می‌کند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/17285" target="_blank">📅 02:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ایران در حال آماده‌سازی برای انجام یک حمله بزرگ علیه اسرائیل با استفاده از سلاح‌های جدید است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17284" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خب موج اول گویا تمام شده.
به نظرم از جمعه موج اصلی حملات شروع بشود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17283" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیانیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
پس از نفوذ یک فروند جنگنده اف 16 به حریم هوایی خلیج فارس و شلیک موشک از سوی سامانه پدافند هوایی سپاه پاسداران، هواپیمای مهاجم متواری شد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17282" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است  هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17281" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یمن به آمریکا هشدار داد - درصورت ادامه حملات به ایران سکوت نمی‌کنیم</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17280" target="_blank">📅 02:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17279" target="_blank">📅 02:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فاکس نیوز گزارش می‌دهد که اهداف بعدی نیروگاه‌های برق در ایران خواهند بود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17278" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17277" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=Srgl-m-NNltEBjTspMGOasO1Yhl5xy425y3CHzMvMIpp8ivuRlRs2NHkj9-Ued4_Wwzcx5ElXurnu8KomE5bwlYoHPpv8wTct-Ye58E5nyZAWqLJ5Ai_ktP3tBmTkPb7gKqADhh6W4R_GW5bX4_u3xh0QzojchATegL_poFiNz6r7HpX67NUT85nvFaZ8s05JPJfPVa-kfpiOgRV6KXGashhqa679FffuIIRVZrH1-0b8upkYioYMLT3mZE7LGkD1PxUnavIWtCwDPH4rSNuuhXUFXnH7xn9zScLR4BhfVitGn8FQ2z2I11Stju890ac-0Ol9DpX6KQ9shufwfeoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=Srgl-m-NNltEBjTspMGOasO1Yhl5xy425y3CHzMvMIpp8ivuRlRs2NHkj9-Ued4_Wwzcx5ElXurnu8KomE5bwlYoHPpv8wTct-Ye58E5nyZAWqLJ5Ai_ktP3tBmTkPb7gKqADhh6W4R_GW5bX4_u3xh0QzojchATegL_poFiNz6r7HpX67NUT85nvFaZ8s05JPJfPVa-kfpiOgRV6KXGashhqa679FffuIIRVZrH1-0b8upkYioYMLT3mZE7LGkD1PxUnavIWtCwDPH4rSNuuhXUFXnH7xn9zScLR4BhfVitGn8FQ2z2I11Stju890ac-0Ol9DpX6KQ9shufwfeoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این را بفرستید خب</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17276" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است  بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17275" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است
بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17274" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17273" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DixWPhqx270wlxZ4E-qOL4NXYTtK2BC2xY23Wez7m3e_5-PAy75rh9lM-oki_-4uNeXMFRHYTwuuM3HbMdvhYgZs0__bvIb1pkLeAp3_ewGaPlnaNBKeR6thHYBjSpTkuKAr2s36pIIyRbcEfbfjb5zOONSj7v1tWDiEf0BQRQF5naQQuzciPlhNveK0ZIbDfvsk_WDbufJgER0Sr1b4U2OeAwnE-Cb1bAypko9WiX5JpU-D5rW-BwByNXY0PkHq75I2PzJyYrTD_Agrm4KlYJfTmkCL6VQKO5JJVBUWjpdv12uOa0o9XR_EfglL0FwZes-IOOFFRLBdT1hUtHMNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17272" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=X3COCzt4_r7jBqlDc8upahGzFLVnRBsXr0DczMAFJSz0Pnt6PCfBSa1SfoE3vzal5uCqHJC-XCfeeQSFyNM_nF6xfSX9NV0UP32NlUcG0LYvVbJs1KzXlymqX8cIDoPvDW5Yn6WJJTHK7faT7OtWTU3HJNr1w78_qE19yFeMNIejxUuBfLbzwdQSqm2SavKhWlkObk1I4I5l8Ft5hG7rcEDvrEe7czLMrDpjS7JpwE4R0scOX3Acm2ubqcDevGjd3vYUHAIgnp_QneIMpAbYP4TBGhxUdDR11hkmuXRNwYZ75uRHA3BqokWkoo4yZnoDc-FLnMApmSZfQrG9u2G6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=X3COCzt4_r7jBqlDc8upahGzFLVnRBsXr0DczMAFJSz0Pnt6PCfBSa1SfoE3vzal5uCqHJC-XCfeeQSFyNM_nF6xfSX9NV0UP32NlUcG0LYvVbJs1KzXlymqX8cIDoPvDW5Yn6WJJTHK7faT7OtWTU3HJNr1w78_qE19yFeMNIejxUuBfLbzwdQSqm2SavKhWlkObk1I4I5l8Ft5hG7rcEDvrEe7czLMrDpjS7JpwE4R0scOX3Acm2ubqcDevGjd3vYUHAIgnp_QneIMpAbYP4TBGhxUdDR11hkmuXRNwYZ75uRHA3BqokWkoo4yZnoDc-FLnMApmSZfQrG9u2G6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17271" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rClsihFQQZ1iDxk2qApCHbOnBJGBLnpeCnj_6yP18jaiyZuCn1t8hJ45BaVWwFkAcy0eu1AHLLpIk9h3pjVUfJ4OKht5P-rE7u_c37jXp8sC5oJ7gTUwvog0Kdmczq-KZSTwJsAjXuO7zKdY39hpPzAkq4kbi0Ka4PIsRLLFewKtu7Rd3fFaznCZj1MvXbHy2RzZPVRgr6juT-CrpiNZ1_W89WCWWnKlrRTj44VZhxXCYFry2AQTiz-td7TN0ofkZT7NuSiC9ZakYAu5P9m1W7hQpmO93A67-VV3KRVTJuljG9hyueNqbWLxik6Kni1eUvg-ngDkZGktROghoJzNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17270" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام آمریکایی می‌گوید حملات به جنوب ایران شامل «صدها هدف» خواهد بود و به مدت ساعت‌ها ادامه خواهد داشت</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17269" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به نظرم میخواهند بگویند راه مذاکره (تسلیم) باز است و در ضمن به کنگره هم بگویند که اینها حمله نیست بلکه دفاع از خود است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17268" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک اصطکاک ریزی بین آمریکایی ها و اسرائیلی ها قابل مشاهده است که به نظر بعد از لو رفتن قضیه جاسوسی اسرائیل از سیستم اطلاعات نظامی آمریکا ایجاد شده.  اما به نظرم موقت است و راهبردی نیست.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17267" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است
هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17266" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17265" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حمله دفاعی دیگر چه صیغه ای است؟!</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17264" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرقی، با دستور فرمانده کل قوا، حمله‌های دفاعی اضافی را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تهاجم بی‌دلیل و ادامه‌دار ایران است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17263" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.  @U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17262" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17261" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17260" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شلیک موشک از غرب کشور</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17259" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تسنیم:
انفجار در سیریک</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17258" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
