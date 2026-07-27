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
<img src="https://cdn4.telesco.pe/file/cQ79wbpHrLoLNW_V08LYYBqZCW7DauVVwShr6iOeZvfqQdj8SSg-QuMkso11oqHTqQ3kA_-RV7rQwWNWbd_IHFnkC2rzvJC5f8KRCUf0ft9FSZ31PPiYFuhXweAr9el7ZlYmsJylD68F1Dl5R0cRVmosC6OFYK5hOxDaagLqNpKLO9rxMsZuq8DPo_xr7XYAxWPVsxPuJ7OwgwsZstWrHJK6vlTukEQzy2amHc6oDbSQS9GRmOTgu4F_oLGQUQawHmhKYo-eiA7WFop5JXz3r1yk_kYn83BgNruI1Eu6Yc0aQsGDmR_pLnuvFR-SvnmcAa6e2pHwqNVtgz6_ndJnBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 962K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-137941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری / ترامپ هم اکنون: در حال گفتگوهای عمیق با ایران هستیم و اگر موفق نشدند، به عملیات نظامی گسترده باز می‌گردیم
🔴
مهلت زیادی به مذاکره نمی‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/137941" target="_blank">📅 18:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / ترامپ هم اکنون: در حال گفتگوهای عمیق با ایران هستیم و اگر موفق نشدند، به عملیات نظامی گسترده باز می‌گردیم
🔴
مهلت زیادی به مذاکره نمی‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137940" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9JnNiXIhKTlcK2xk_bmLME5BkLrS6EtlfHrGpVvxZLvM7cDhYXSetnbqh_wiN9ci2ABadiYGdYK7-yqH5RgXJ1gPgC3TWvSoJzSjgy-7XdxRpIk8_5SrgvF8TNaDY_nd9m5Z2k57LmkfnMldOD1h-5xmlW5_-XcxcuZQs_czWtK2241QyJdT-jyxB-g-1bYUa5tIh3vjCjWYqJBu7hWgIR-jugDSkBu-ADzW9rYOoUVYy2MdKV7azAPVqnUpccK7rD4G4CPDiUFH8Vu001_lF7tNFec8sz2PcJUA5KIzjsAqHkkeCHzccTNPtkctxPkN2rn0jj2wmCwXvcQNNz_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش خبرگزاری آسوشیتدپرس، میانجیان قطری و پاکستانی پیشرفت‌هایی در راستای از سرگیری مذاکرات بین ایالات متحده و ایران و همچنین احیای آتش‌بس موقت داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/137939" target="_blank">📅 18:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X86BEkK267ijHTO0AF35UaqYdMREU3iLqR8sPmT5ae4CU5TfQQS5uLozcgRSUntgx8tEN4jqrhBZ6cgJY9lRzHB1Y6_Ueilx4X4NhuAvQFqDpLwWoDoncCQct1Pm9apMoTj3iPrd99RgCBqPziyO8y20v1CmjrmBoIFmk1yycaNDrE8Sps6YKwHHMFohze3x64eL4anaSKk4on-N-YYtENNGsGxFVN0QmzmV-bx72DX6ezDNPt4wmjLaHgXE_pELabMdCieg5vEQrZ7GIXRR_ahr33KfUhlC-rG22sYULC4mJQvzRCmwz-jvCfgc2hw7d-IRH3YoCPMokTRRL98ySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت قراردادی به ارزش ۱۶ میلیارد دلار برای احداث خط لوله انتقال نفت خام با شرکت‌های خصوصی آمریکای شمالی به نام‌های بلاک‌استون، بروکفیلد مدیریت دارایی و کی‌کا‌ار امضا کرده است. این بزرگترین سرمایه‌گذاری مستقیم خارجی در تاریخ این کشور است.
🔴
بر اساس این توافق، هر یک از این سه شرکت، سهم مساوی از ۴۹ درصد سهام یک مشارکت جدید با شرکت ملی نفت کویت (KPC) را خریداری خواهند کرد. این شرکت، حق استفاده از خط لوله را به KPC اجاره خواهد داد.
🔴
کویت از این معامله، مبلغ ۷.۸۵ میلیارد دلار به عنوان پیش پرداخت دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/137938" target="_blank">📅 18:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
معاون شرکت آب منطقه‌ای تهران: شنا در سدها ممنوع است؛ تاکنون ۲ مورد غرق‌شدگی در سد لتیان گزارش شده و از مردم خواسته شده برای شنا به محدوده سدها مراجعه نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137937" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرگزاری عمان:وزیر امور خارجه، بدر بن حمد البوسعیدی، در تماس‌هایی با تعدادی از همتایان خود در منطقه، تحولات جاری و تلاش‌ها برای کاهش تنش را مورد بحث و بررسی قرار داد.
🔴
وزیر امور خارجه با همتایان خود در منطقه بر اهمیت دستیابی به تفاهمی که ایمنی تردد در تنگه هرمز را تضمین کند، تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/137936" target="_blank">📅 18:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Sw0Saubo_7YPjva0kW9KFnEED625QpgQMQn3ac-B_DTBOYASCl_oglzfrb1jub5soKPQbwNAwihx0nyzXy6xZb9jo0GAMYyLJzJdHXKChKhTJuXxXwt05l9IEl_x8ZnPIHY6qASr7b1x0uIMXuMtCo24pRmTI9-RRVHefl54fwk_MJ-8jbvPRCYlluK4qGbFPCJ_EFCJ7Y37cyWnuLBIZJrw8s8Wl0EghLd53HoNFUJ6x2rW0Tmk4cVpGYITtzSr5kHfKR366SnuiFFb4hinhSZkNMzUvA8idR_-VLiLk1l_RjvoEy42UdNQuF42bl0rckB57IuIw-uHiRAgaoAF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Sw0Saubo_7YPjva0kW9KFnEED625QpgQMQn3ac-B_DTBOYASCl_oglzfrb1jub5soKPQbwNAwihx0nyzXy6xZb9jo0GAMYyLJzJdHXKChKhTJuXxXwt05l9IEl_x8ZnPIHY6qASr7b1x0uIMXuMtCo24pRmTI9-RRVHefl54fwk_MJ-8jbvPRCYlluK4qGbFPCJ_EFCJ7Y37cyWnuLBIZJrw8s8Wl0EghLd53HoNFUJ6x2rW0Tmk4cVpGYITtzSr5kHfKR366SnuiFFb4hinhSZkNMzUvA8idR_-VLiLk1l_RjvoEy42UdNQuF42bl0rckB57IuIw-uHiRAgaoAF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
مسیرهای جایگزین پل‌های آسیب‌دیدۀ هرمزگان آسفالت شد
‏
🔴
این پل‌ها در حملات آمریکا آسیب دیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/137935" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad2169d47.mp4?token=sjJUIfbHaR6wrP1FIqiK2-GPVBsDvutp3ZTC6hwN6TwMHTbxfMIv8OkbWSlZ6D0T2kDnCExFrSe0zowx8PCxMNRjKPu2LvDhZgTkHs3gVvqLEzkhDcqH2Ah67VvmOl9hJKV0lPasR_1Ljm1RD5Ds_QHuoNMoESBRJM6WoxmUNpJZnio8ayd3p0bInPEhgZdjjvGgeikKb9P5BUtgr4bJ-WEXy1BzZAARATTI-5D5aMATWDkrmMGp4Gxe0oOHo92oI4QRW0GtfXM8GDGdrYu3tZAvs4UY_9iJNl7nS0T2E3nO8KbfauFnQQtW_mvgiMVtG1dapRci_8N1s8QBXMQ9PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad2169d47.mp4?token=sjJUIfbHaR6wrP1FIqiK2-GPVBsDvutp3ZTC6hwN6TwMHTbxfMIv8OkbWSlZ6D0T2kDnCExFrSe0zowx8PCxMNRjKPu2LvDhZgTkHs3gVvqLEzkhDcqH2Ah67VvmOl9hJKV0lPasR_1Ljm1RD5Ds_QHuoNMoESBRJM6WoxmUNpJZnio8ayd3p0bInPEhgZdjjvGgeikKb9P5BUtgr4bJ-WEXy1BzZAARATTI-5D5aMATWDkrmMGp4Gxe0oOHo92oI4QRW0GtfXM8GDGdrYu3tZAvs4UY_9iJNl7nS0T2E3nO8KbfauFnQQtW_mvgiMVtG1dapRci_8N1s8QBXMQ9PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون مجلس، خضریان :
عمان به لحاظ حقوقی نمیتونه بدون هماهنگی با ایران تنگه رو باز کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/137933" target="_blank">📅 18:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی سپاه: ما حقیقتاً از فرصت آتش‌بس استفاده کردیم و آمریکا نتوانسته از این فرصت استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/137932" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
روسیه به ایران پیشنهاد داده است که درصورت تمایل میتواند از خاک روسیه برای پاسخ به اوکراین استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/137931" target="_blank">📅 18:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ترامپ یک تاجر است، اما در مورد ایران بسیار ساده‌لوح است
🔴
مذاکره با ایرانی‌ها هیچ فایده‌ای ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/137930" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW8_T5SrR-wtSAW1tQfI3OahI6TiSthE8l-dtgffICXto1hijE1sv5LlDoC1mRyzy6migsdnbnBEUJLcp_H_4TZXyupDTWPXXLDQH0HXbo-XmwxXokcTrqHCWI_Cpb7YXR7XJJa96Zy0vfIRK3gcCF7H3ZPIjygD4Q5--cO6H_ngXbOtB90TnATMhExGCDP00bW7kFY8I6udnrIFYX8HmW-7KpIz_sFkIEqT7NeXD3K_w0Fgbsa-iYpREAx8vT8CkWSrL9P90IARtC6VAb0_Evpp4AyK707WfZ6lakVVifaKh3iYKU8j3BishTr7WGeDYMZc64tvmRtypB62o8B6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای و ویدیوها نشان می‌دهند که دود غلیظی در مجتمع پایانه نفتی جنوب یانبو در عربستان سعودی، واقع در دریای سرخ، مشاهده می‌شود.
🔴
این مجتمع برای صادرات نفت خام عربستان، به ویژه با توجه به مسدود شدن تنگه هرمز، از اهمیت بالایی برخوردار است، زیرا یکی از دو نقطه پایانی غربی خط لوله شرق-غرب این کشور را تشکیل می‌دهد. نقطه پایانی دیگر، پایانه نفتی شمال یانبو است.
🔴
به احتمال زیاد، این حمله در شامگاه جمعه یا صبح روز شنبه، به وقت محلی، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137929" target="_blank">📅 17:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqzDgXbEAHeqC-zjna3580GP31CwGmVqNGjb2ABhUkp-YBHiLrufO_-l2IM4rhkEGKwmOZr3jH_oa3_1a3OKYovZ1m5vC5-GWPpi5KuaGKwVyyztTAMiUqpdJ3XOQE1jEN04h9KrdacAInyx_bw-fqt4jvTR7mkwaIGakoohI6XwEwuQ-FNmWncCqXALmJxRoG83Jp1lWnYc0mptF5tcaM-mw1o7HjFwn0X_PyBaaijdsPoHMFmgFKZs1XDU0A17JwkPDzXabZy39cN8orgdY-zljCwz8ZassTFD6yuseDQgf5z_dsg_eH23t9TaFZG-GpHPdHjc2BXrfheaKTak3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم ایران با میانگین درآمد ماهیانه ۸۵ دلار در در بین کشورهایی که پایین ترین دستمزد ماهیانه رو میگیرن رتبه ی سوم رو بدست آوردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137928" target="_blank">📅 17:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKOUoqnkEY1Dh-qcmEBIkH-nXaiQONtAJFykFV9zoe-yGHeeqA3GK9y4Wq-PZYy3onmUShRkWKc7L3JK1Nn6Jh2XMUUETFKRRg5TabtjE8bKdRJWhBKCYB80In0noRmccIKQOi-T22ntpz98n9KNcl1NA_4C5q69fzgC7TC23JkhlL9oiN1OOdkCm3bQpmiYhgz3hjRLH-9df5xURQ0AQp5uMAdaqyPsCOXWSR5oA_8JZ2GoFysgSaZ0jN5sZZoUwMGySHGYhkM03WhIldF4LFSNKc0Cuw1J_hEf_bmn1OgLtqm0klJqCKCjvEtXitsvg9RIXkcxipOvee8Rsbg6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfZ8XrDfK90YShmPNnOlsxcoZ-2w2kJwZJ9iCFS_lXq6QbuC3_dxcANnMQHrkTk0kcW_KBpD6EufjHSgoBoZtjQuPmMoxVMQep0fS4kZglc1dk96japOBQbxT1wD1lgtx7S2VxNYRbtvVOew-wQ9rw9UcwSLHKKHy04JGwYrVg4D4R33FFfYYH1Go3wrYrhE0SxezV39cg4C1Zfyvadct72--MX1F3LlaB1m73voehDEvPvI00b07P6Z-eOCAkg2ScmCWw_eLPLX0loNcyrVx7YLOoAchcswt5t2eXBl32hGR2K5yCPkkYvmVYxg-w5bxrnwqcjLRyLEY2yBNdaYKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیما تکیدو به جرم برگزاری ایونت مختلط(اقدام علیه زیر شکم بعضیا) بازداشت و صفحه ی یوتیوبش توسط پلیس بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137925" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2YNmQ1BhcWGX21TbTxOtOPJGDeNSz081wxL8CX5RiQoraMu0mxP_0slkoihwWya9OeUKll-QQsNFvwJPK8gr6tPKU2R4OKX3Gw0WpHqEpLaq9IRyKeZ4HaWeh5bvBkTdcb4C2WKTwmq5hzQUWaW5nQpr5Jv0A3IAIgLfFZqUs_ywKGRkuvzvc0s5CY9rkFPbrMY9YaQeebJQiwE6sGmiPxWTSCP-e374cmRd68sMN4n7GzppNjkSeP0Q5LI1S6ry7cDQspe8oSMwJe3Nezq15E4JAsIpMBcBxR0ieelPFrsOGQ5aBOyMIm4eD0WuBdv1TLmeWF3eXEw0Q2C9EhjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaRi1bPP9OJmSxrZY3IplcpTqoEGDk7xSWng88RiMp5Yl8E7v6DlTb45wM2C4BGAOs2YHR2XcTHlBZY_2MkYgTwUM2vlwRT5mdgRUP7sEUmHWRzAEI-Zv2KQua6GHvzN4fRtNA78RITFoRTvPzyiQ8AyRx7TMBMYaAxe0XADoPYncXEtmtLaXBBMRE_JlMRKZMjJI3y7kJpAggJXQY5v0tZTFAeYUwo03YH4z_2qMygXrRFg92EehDZKJNjgP67W3yCaWv4lJ1uXZVRA7Q_31kj6KKmNpXuAjf6HX1wMS20BOcCMrRhvPcSSJRigPhfbgCFbgNM3nzn8ecqJMjgn5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از خطوط انتقال نفت عربستان در شهر ینبع که توسط انصارالله یمن مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/137923" target="_blank">📅 17:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJv4fkM1JjiFVhLP2eRAVk4LBRRF3VIpLwxyRy5mESN1i4iugg1WhqxQ3J5OcHuMlJ8w8hG1rbuyrOB9s24ZLknVChakjezY-W50RoQMQ7sBMBx7abaWLGTHWrOl3GGUBFqb2cvPlwbTblOKLEcpw24c-fwc4BhmtLG01NOk2V1kvUgdMR19qOuNh_vVn9FzT7KyDgV85PuVfdAGCDsGylAEqQu_quZTBTyjq5JzzBIlngkFLlo2vDgwo5ObALiDoBVPYVKi0KNKq3lM_I5-9H8Mneo7z773aTVUSxomeas1kQQqZp8TS2hedIngn0CW6ynh3kMQ7WrW4Io3_2mAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf188f0688.mp4?token=q1RqZdWi247pL0DynhKhl9oEEsFiXPOfdF1L0LxR-Jvc6divaBbllhTOJ0hqZTKqioAF_8O1nZEiBl2ZvVVLD-h4lgc6f7Hmqejkwi1YtC8ZeIbU_L1lIhaF8cPXZizYMgOoLu0LsDVnF3rMyonO-xi8Lt9PacWV7hQKXSWaj-irElqRnuxlYkia-1-iFGIkxjnPbZks01gdGS6ct7TUwYRtbISKSukuAZUyEAKyak7vMB-t51jZ_n8QyHbLYTUvR0kvIvdFI2MzXH3MD9mDM1V9DfB7rcsN0GTDowkNMt1U929n9ymEoE87UPdf8QjZu6gLAWOth_kBgkI727UfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf188f0688.mp4?token=q1RqZdWi247pL0DynhKhl9oEEsFiXPOfdF1L0LxR-Jvc6divaBbllhTOJ0hqZTKqioAF_8O1nZEiBl2ZvVVLD-h4lgc6f7Hmqejkwi1YtC8ZeIbU_L1lIhaF8cPXZizYMgOoLu0LsDVnF3rMyonO-xi8Lt9PacWV7hQKXSWaj-irElqRnuxlYkia-1-iFGIkxjnPbZks01gdGS6ct7TUwYRtbISKSukuAZUyEAKyak7vMB-t51jZ_n8QyHbLYTUvR0kvIvdFI2MzXH3MD9mDM1V9DfB7rcsN0GTDowkNMt1U929n9ymEoE87UPdf8QjZu6gLAWOth_kBgkI727UfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در حالی که وزارت دفاع عربستان اعلام کرد پهپادهای پرتاب شده از عراق را سرنگون کردیم اما تصویر ماهواره‌ای امروز از تاسیسات نفتی عربستان سعودی در بقیق منتشر شده که مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137920" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b27761eb0.mp4?token=PS6KACaSKjd3nU7e8wA-htPQdS-taS3cu9qiL4RitBaTRvFXNoGw1ZRsGTZhw7OSqQjXXbgT4nWmy6aVPJEewu9F1tQzlhT0_rViouRDxJVUp3kv42hWnCr0QN5Oo5KegHe4T3k8HgB-FwzUyGksNCDfmXlmj1Tw4L5uyvSq5iBFfpdFVRJXNERl-y-jpG_EohtJDWz83ueiRXt0-6BtP_HrKTf15R2D__gwgiGSKTiIPnWqkkBDKRAcJlfJlcpodyVLBCIcYx2etUNiMyw28Kl-Gs6ZpBKygRwGiI5FoQUM_BgZ7FUpkGRj9dfhl1_Us1_QiR6ouQbJ3GK8fE4u0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b27761eb0.mp4?token=PS6KACaSKjd3nU7e8wA-htPQdS-taS3cu9qiL4RitBaTRvFXNoGw1ZRsGTZhw7OSqQjXXbgT4nWmy6aVPJEewu9F1tQzlhT0_rViouRDxJVUp3kv42hWnCr0QN5Oo5KegHe4T3k8HgB-FwzUyGksNCDfmXlmj1Tw4L5uyvSq5iBFfpdFVRJXNERl-y-jpG_EohtJDWz83ueiRXt0-6BtP_HrKTf15R2D__gwgiGSKTiIPnWqkkBDKRAcJlfJlcpodyVLBCIcYx2etUNiMyw28Kl-Gs6ZpBKygRwGiI5FoQUM_BgZ7FUpkGRj9dfhl1_Us1_QiR6ouQbJ3GK8fE4u0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
من خوشحال خواهم شد اگر دستور اعدام یک تروریست صادر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/137919" target="_blank">📅 17:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0828052249.mp4?token=fMkNcO0pjjsGOJVOqFZj05yAPkeThM4R8LmT3yjaJiGYvOxeq6uAxv31uPV-MvtZMKfvJ5UJ0Ok6au4VSlbFbASndjdWDPkV_sgkco3NvfLKvcNIIsy58zl7g2VCZZH5TslsaIR7MTXPGaR2_x2DHXZo40tXsUP3dXf8y9IN9qnWijvVSF8YO1zPqiqRsy7laYvucNSkcTmv5TmMhpGLQylzsFnV-wuu72tCRkZ5A9e_C3KRaiRHI_mQsU9yymC8sFQDyYNS3tgLVzheZl7DYGI6bog7UUVpDsLQWAb-NmfwDN4N2o6ZcqU8RjmI9m5CHEgdDjOssaA8fWgld8crJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0828052249.mp4?token=fMkNcO0pjjsGOJVOqFZj05yAPkeThM4R8LmT3yjaJiGYvOxeq6uAxv31uPV-MvtZMKfvJ5UJ0Ok6au4VSlbFbASndjdWDPkV_sgkco3NvfLKvcNIIsy58zl7g2VCZZH5TslsaIR7MTXPGaR2_x2DHXZo40tXsUP3dXf8y9IN9qnWijvVSF8YO1zPqiqRsy7laYvucNSkcTmv5TmMhpGLQylzsFnV-wuu72tCRkZ5A9e_C3KRaiRHI_mQsU9yymC8sFQDyYNS3tgLVzheZl7DYGI6bog7UUVpDsLQWAb-NmfwDN4N2o6ZcqU8RjmI9m5CHEgdDjOssaA8fWgld8crJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: ذخایر نظامی آمریکا رو به اتمام است در حالی که جوانان ایرانی زیر درخت موشک تولید می‌کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/137918" target="_blank">📅 17:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMlzNs24liae848A0-MDCubzqDVFrJG53Fgdl6wPASy2i-yd4xApuC8J9pzn9D2R1AmejkYXgmpmUpuYtMePdXyfvMTowV7Seb-Za-LdE8sjAMeKV7eoiTqBB0-t3pYfTL_2RN05VJYLmunZscEhhbHUWSKRqpjPcmUHUzQ24Dr1nygA7SIEwQ2Pj49amKcvof7KEkWm_3Gc8AcGbwXtvpBaPdCO1--Rc6t2nymRyV45mz8X9cSqr8P9cw-dCtvPBXsky4ondaRgTod5rD_dzaEV1vuoSZELWvNY5yGLTwbQYgSiqIDxBUXdccZL2UnnBWcnwJWn2BenfJFtHOW92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر بار دیگر از ۱۹۰ هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/137917" target="_blank">📅 17:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QphYDPatfEFUIa_jhSZgH97nJmpUAb4rMjgPddABQy1eMzZg4ilERh8eCMGnNrPOEg1KCXsxFkJdwX50YuKS0qOu1Y81ZZbS3P_bPah6REygpRq9bhHAATWu4FkLpUZNspp09KHT4RJdkpoFpxRA4apawAjku2xdwM4tfIL_vppxnutWOKzfRsmycN3VXakeTFr_Yi4c2e4BGiTtGgbEH6mt8f1cEcQtNhUBSSOMS6NgwWqbCbxL6-N_TBUmciwSRSfbwXaOIdiM5pZ4WdqUsOAyAOGIfJT1NT_6uFU8bi2cC1MM2gYWMvYKA5Fh87Tr_JZyYwg7ithPeGzS01vq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اندری سیبیها، وزیر امور خارجه اوکراین در پاسخ به توییت عباس عراقچی: «تهدیدات ایران غیرموجه و بی‌اساس است. رژیم تهران همدست مستقیم تجاوز روسیه به اوکراین است و با ارسال سلاح، جنگ جنایتکارانه مسکو را تشدید می‌کند، سلاح‌هایی که از سال 2022 باعث کشته شدن مردم اوکراین شده‌اند. ایران هیچ حقی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه تهدیدات خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند. ایران با این اظهارات، تلاش می‌کند توجه را از تروریسم روسیه علیه کشتی‌های غیرنظامی در دریای سیاه دور کند، که امنیت غذایی جهانی را تهدید می‌کند.
اما موفق نخواهد شد.حملات روسیه به آزادی تردد دریایی، محور اصلی جلسه اضطراری امروز شورای امنیت سازمان ملل خواهد بود، و ما انتظار داریم واکنش‌های قوی از سوی جامعه بین‌المللی شاهد باشیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137916" target="_blank">📅 17:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/137915" target="_blank">📅 17:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjD6Rz5jjJ1ljv8V-RukV43MG3pNGC6TeyxZX6zp6VESn4R3ORN0cOwVHit7E6Xvhw2xlOYtGl_fUr-j1N-rVflVDp_xPFx2PKyCmSgppnrwLaCgOra0t2krUrSxFY8Eq058t9o80tbqFcZDeO1V9_p1ajAPTglC1pnEReUi_lpjTdePDbiNZ2dAL6cylR0lbuGpbrOdmuVwLw1u-GddaHYr6QcIvji_fX-aTqqQxcMUY5v1y-ZMwHZoXDJN8h6a7qVBefzXsiR2kWA3hNWQyzsX8WYEwFT_eArif8R7DozpB9jb3x11A9xi0eljyYqsUb1z9wPQ98RB09PIk8EH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJVYNMmAQETuvgrdMyxNI6w7ZeO_q3HOf74jdb7ZhhBOlQjYm2Ci48e09z6TNoZoyPKkqHPpFkPXsc0zllKfvXJT1O8YUyrvFO04a2A7REmqtX2d65MdDGHsHdX_r9GIcUK0S2izwBFv_aKGz8gQGbykhUlA0hfkiMBBu0U-XYlW-HhcwO6OoOvr8rv5UHmvMRc1LvLJwkb9OKYF7FtOawsoxmKsDnerrTALzEwa-wsbct7s40eTZp104ooUft62U4CMaAUY-zTyJFr-daje_2KMsLY8Yie7giheiaIZ8oQm3dMX7tIuKhIermp3dDDmOIz_FE2T4u2S8wgAo1wjbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dd49a21f.mp4?token=QOaiFgox4ILWQQgkXkRjFHzbDdOcTWnKWmAPeASan_nJH4eCK-kryHmBmXfA6lH6R1I7z7Xx4qGa7I36afM3Jw32oqbqPT_jidmIcwxMydwsW1kgbms9ZFMrZsU6SUubq-9XhEmO0T2qwxl4RGPZwprZQQ50wXsjE2GXMENaR3ij24lk_a8R4o2QH1u9C9JyrSxuGBE6noP8w1hyOhB_6O9IAW6L36H4RWVgl-9sU1M-BcXTV1ZLPOZ9X-9yf_xDhQcOiIxK-Jn9wZu6LnM62GrSHZnHtOLdGhU0nmvkR0O6WiFT2sWLXFIgUAjQkiTnxLYhOwOB70EzV6162zo4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dd49a21f.mp4?token=QOaiFgox4ILWQQgkXkRjFHzbDdOcTWnKWmAPeASan_nJH4eCK-kryHmBmXfA6lH6R1I7z7Xx4qGa7I36afM3Jw32oqbqPT_jidmIcwxMydwsW1kgbms9ZFMrZsU6SUubq-9XhEmO0T2qwxl4RGPZwprZQQ50wXsjE2GXMENaR3ij24lk_a8R4o2QH1u9C9JyrSxuGBE6noP8w1hyOhB_6O9IAW6L36H4RWVgl-9sU1M-BcXTV1ZLPOZ9X-9yf_xDhQcOiIxK-Jn9wZu6LnM62GrSHZnHtOLdGhU0nmvkR0O6WiFT2sWLXFIgUAjQkiTnxLYhOwOB70EzV6162zo4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز تو صادقیه تهران یه تاور افتاده رو خونه‌ها و ماشینای مردم و این خسارات به بار آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/137912" target="_blank">📅 17:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
بی‌بی‌سی:
از آغاز جنگ با جمهوری اسلامی ایران در ماه فوریه، بیش از ۶۰۰ سرباز آمریکایی زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/137911" target="_blank">📅 17:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سی‌ان‌ان:
موساد اطلاعات کوه کلنگ را به آمریکا داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137910" target="_blank">📅 17:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137909">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGALzuyd2abpGV08bgZqfA_-r_zopQqG2Bp3_hlEaSPmfUQytyiZ5X5GT7o1nulb4g9V6PmQ0DbDATwJQnzHEWQ-Wld4_lhWQmHGywGzRZkF6v5p21luacCM_DW4fpf7oir8cGE2iWIK2d7g-_MeAcWCuNUIPlLj0wOt67UHvAFszP1TdJM-WFyT2WPqYoOvhSj90Rtvs_RDFw_A8sU5q0z25x_ktsuXGhckX9nXzlI496V6hGOeL7f4iWw0LcxTQ-JxFq8pGggh7I-pTrseUKZ-9nKwzgaUETpIDGLH5okrcsLFLo-HpxY9weOQ9ZFRjTd0DaedVFL_Zl9XaEDMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاجی‌بابایی، نایب رئیس مجلس : ما هیچ‌وقت با آمریکا به تفاهم نخواهیم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137909" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137908">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حوثی‌ها:
خطوط انتقال نفت عربستان را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/137908" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137906">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جنگ آمریکا و ایران موقتاً متوقف شد. ترامپ راه مذاکرات برای رفع بن‌بست تنگه هرمز را باز کرد، اما دولت او اعلام کرده تقویت نظامی ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137906" target="_blank">📅 16:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137905">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
بنزین لیتری ۱۰هزار تومانی تا چند روز دیگه تو جایگاه‌های سوخت ثبت میشه و هرکی ناراضی باشه میشه عامل کودتای صهیونی
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137905" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137904">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ایندیپندنت:
پس از حملات ایران به پایگاه‌های آمریکا در کویت، ارتش این کشور فراخوان جذب نیروی نظامی منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137904" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137903">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
میزان سوختگیری با کارت آزاد جایگاه‌ها در سه استان افزایش یافت
‏
🔴
نواز، سخنگوی صنف جایگاه‌های سوخت کشور: بر اساس تمهیدات جهت تسهیل در سوخت رسانی برای زائرین اربعین، میزان سوختگیری با کارت آزاد جایگاه‌ها در سه استان کردستان، ایلام و کرمانشاه از ۱۵ لیتر به ۳۰ لیتر افزایش یافت. سوختگیری با کارت سوخت شخصی ۴۵ لیتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137903" target="_blank">📅 16:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137902">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دقایقی قبل به تاسیسات نفتی در شرق عربستان از خاک عراق حمله پهپادی شد، وزارت دفاع عربستان اعلام کرد پهپاد ها را در آسمان رهگیری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137902" target="_blank">📅 15:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgERP5YguZtJ9LcpnqxywA4k53RRNpl92jK-poFUYgm474GbAPv8g4m9ZZg2plo7JMTwf50abz9Yre2PhheAQMWLDoVW8QZqOmNKG6pJhB1rgHoy9ZoPLgFY85ujkG4HRQUBxy36kEaWh7vFzYWFdI8oKPtl0f5f7jqDgBMgBz4q_-lwXMAmUSWk7ZAS7uxdRm1UGIWYQ9KvZWLcosNIujJS-tq3YzoZDrMHki989fjb0hBSyQNRacdD0olerin2kebKoVUVfAKsTSfIqMGxQAkXkPgEcu3Rxl6HDXG9nNDNwK6uyG2GbJciE4hxgcZTooRQk8601_AGXnXvTvmwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش روزنامه جروزالم پست، اسرائیل معتقد است که ترکیه در تلاش است تا از طریق شبکه‌های اجتماعی، بر انتخابات پیش رو در این کشور تأثیر بگذارد.
🔴
مقامات امنیتی می‌گویند هدف این کمپین، شکل‌دهی به افکار عمومی، ایجاد اختلال در روند انتخابات و تشدید اختلافات در داخل جامعه اسرائیل است. این مقامات، نام حساب‌های کاربری، پلتفرم‌ها یا سازمان‌های دخیل را فاش نکردند، همچنین مشخص نکردند که آیا این فعالیت‌ها تحت رهبری دولت ترکیه انجام می‌شود یا خیر.
🔴
این ارزیابی، ترکیه را در کنار ایران قرار می‌دهد، یعنی کشورهایی که مقامات اسرائیلی مشکوک هستند که در تلاش برای تأثیرگذاری بر انتخابات هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137901" target="_blank">📅 15:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKHgbeqKugIMiLVNgFPqkTlS1C_ViRma-QHqKyoe6EVFnZB1xMmxLgdkqlp2ZNY-L-Vy1GeVb79Agk--g6XjUtBnlqWT9LAxDZ4jelJfUcrfo0ffCCE5rFGMSuELQtz9HR5Buh6C7FLkwGh4nY5Y14Pq7atH-Mejn9eZV3zvA6FnXBWeQNUApDkTBbeVAQVHW2bv0tEZkRI-F_Ug_F8vEymgr8LhoGxGhcUHo3Hy5XHpbMBE36dFoHeLfgzgA3c4DGxx9W8OIt3_0FGlzcVFUS2L6wo6Z8v1ZVIVvodVQ39FYdCAbeuiVe8YpTmmvlGXzBGYwxdD9GOzFZEmgJmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که آتش توپخانه اسرائیل را بر تپه علی الطاهر در جنوب لبنان نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137900" target="_blank">📅 15:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
معاون رئیس‌جمهور در امور زنان و خانواده: منتظر هستیم پلیس راهور و فرماندهی انتظامی در هفته‌های آینده زمانی را برای آیین افتتاح صدور گواهینامه موتورسیکلت بانوان اعلام کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137899" target="_blank">📅 15:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmZ45DvF_NrqxeaW9ZPyqhMonXdIaQJr5PmmE-Ql57GOs4S6tQgEkWZd3I-cA1wW8z2TRgBSsR_swxGzQREMj1IJeVl3AZZ7_L7Ra9D0lE5CkORhXZBIsHGA8qj4XiH4TCMeLhd3kD-7SWk_ut0Lk4a3WjU0AofXH9tQzOs9SHFXhoKeh3DOj-62cFF-h74h7DokeaiTbgFp5vNv9y1l1cBIaX0JK9TfDhckDEKsqqfnLXr9AeIGV3vLCe9p9bWB27fOCiUU7wvYfJCZ3GngCKy86WWMwfYmLkV4DC7ZW-1BxpAYZo4nU6dgoHCzDjJ2n8NxU6GUjdSDyzx3bXVgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی به بریتانیا رسید، جایی که قرار است با نخست وزیر بریتانیا، اندی برنهام، دیدار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137898" target="_blank">📅 15:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvHCiZa1VJUf1R7652CDtdtVYYvpZdK1QFWfUsvFLh0C86hHhQkTHvPzagYln3QoOz0qc3BiwsPpXsrYlRCrgf_HQkF6uHOyyQ1hn_ATZjSmjuhbW0eJ9Wzh_BANTjAat4tWdsYsisYC10GE60soA4YCA7VMPmp07cJ342gJw6ClxL-zcYc-8NStYJqr9w9jNRfyo2bM_1_8oHwe42i2Yx8_zOX16yRzvt9DYDGBkkJECjaAcj4hDDFYTItsi8EDGWWCdraTLVp0GW7h0Y_yPa5Fmq5_jJYNQW16Ejm_nJvW3X0QvSP64Ds6WumsFKKSnr20ySPqQpfxPLTCkHfPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: در سه چهار سال اخیر، ما بر خلاف بسیاری از کشور های پیشرفته، رشد اقتصادی خوبی داشتیم. ما الان بعد از چین و آمریکا و هند، چهارمین اقتصاد برتر دنیا و بهترین رشد اقتصاد اروپا داریم، حتی بالا تر از اتحادیه اروپا
🔴
البته که می توانیم سریعتر هم پیشرفت کنیم، اما خطر تورم و نتایجش رو باید در نظر بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137897" target="_blank">📅 15:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نیویورک‌تایمز: به نظر می‌رسد که ترامپ به دام افتاده؛ او اکنون برای یافتن راهی جهت خروج از درگیری که آبرویش را هم حفظ کند، دست و پا می‌زند
🔴
ترامپ سه گزینه اصلی پیش رو دارد: تشدید نظامی، سرکوب اقتصادی یا اعلام پیروزی
🔴
شاید دلیل تردید او برای شروع مجدد حملات علیه ایران این باشد که جنگ، ذخایر موشک‌های رهگیر آمریکا را کاهش داده؛ زیرا پس از ۱۳ شب متوالی حملات در این ماه، این اعداد به سطوح بحرانی رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137896" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668353b1c2.mp4?token=A5NbShaCC4xOzZo185EgOrhSsMgHU1bctpKHE0a49T2zsZWwc0YqhbOXAgW2PBryexIojnaiZ927hZ4IQTnUeVkNGsA_P35sO7C_5RNSdcGfIfcPf090aWr8yxDHdR8XaF0lvpQqM0JZfIsubc7oNCHsuZvtMRWJpL3n0FrVQ-YmKaqN2nG-7asXu5xehxzDZCOcL87a7mVVa4u5e2lxffpUzRfpM84FkuYzuvF5MJ8pJbMJFOe6UrY82Pkj98Zk1cAYbzgzP0XKcnqdJ-ZHL1I_vJdvElgPIhmoHLkUlmPHCQ_8p0W3W6R_Sd5BW2oCCa7AmJcmvY-2QxnrfJtqUCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668353b1c2.mp4?token=A5NbShaCC4xOzZo185EgOrhSsMgHU1bctpKHE0a49T2zsZWwc0YqhbOXAgW2PBryexIojnaiZ927hZ4IQTnUeVkNGsA_P35sO7C_5RNSdcGfIfcPf090aWr8yxDHdR8XaF0lvpQqM0JZfIsubc7oNCHsuZvtMRWJpL3n0FrVQ-YmKaqN2nG-7asXu5xehxzDZCOcL87a7mVVa4u5e2lxffpUzRfpM84FkuYzuvF5MJ8pJbMJFOe6UrY82Pkj98Zk1cAYbzgzP0XKcnqdJ-ZHL1I_vJdvElgPIhmoHLkUlmPHCQ_8p0W3W6R_Sd5BW2oCCa7AmJcmvY-2QxnrfJtqUCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد تند جی دی ونس به اقدامات اسرائیل و منحرف کردن مسیر مذاکرات با ایران
🔴
«جی. دی. ونس»، معاون رئیس‌جمهور آمریکا، در مصاحبه‌ای با «جو روگان»، مجری و یوتیوبر آمریکایی، به انتقاد از اسرائیل پرداخت و گفت: «من قطعاً فکر می‌کنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بوده‌ایم که تلاش می‌کند مذاکرات را منحرف کند و مانع رسیدن به توافق شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137895" target="_blank">📅 15:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3afd948ec2.mp4?token=BJ6WhT1h2K8Mv9jMpzV6Br86aamywTH0qgsfdN6f4QswgPNzRgYFT36o0hP5GCcxXtS8484D7MzlcUI8Egtj1KPSOeIBe1pnlT_ubk607Xtouc_ah9jYy0OGhm87wqgrF0loBpnH0S-KpZGWfvdEvKxjThuFctEsZ8X4ar74sh8O8lfpDba63q11MrYveUCwyj1tDEeXj7gmmAAuRybnUMUqf334LPOvT8WaXtPfdj5GVslB6L8DJ8Id9n_Kd3GG4zTynEplYuARXboB8DIvRNwri8RcHGrdUqb2KogUpevr6qdxxRw7thYxRlJw7yNW5KjGAEBQ4Gmhbbd95wOpgrDlV3ukpRKeqG6JTrxKRfjqXqpkX-gMVGNOtjNS3g_ZAZjE2YNPwNwZXf9T99FY62cIuwz6RScmTbyk2Og-uKRHyqWmwX-7trI0vslfKzVCCUGYpgp4e3DVvKn3itxrvFZCREpVk9WHH2qlMGow8CTy2jKD-STfmr1Rvbj1F9Cei7CAGpguAv4BHIh8cpPXuwALQxRIHkUl7e6NH2c7dqzw4eSu0ZI9nHEwJkpSqaFGCQnVuFdV-2CTuvMWlDEjq0IqgvSezC9Esnysk5Wx4aXoGrjvMl39lotKZupnA-jz85dHFHI_YVDrUKAbXfhkeTx4s9YEbVcj2UCKasQnoO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3afd948ec2.mp4?token=BJ6WhT1h2K8Mv9jMpzV6Br86aamywTH0qgsfdN6f4QswgPNzRgYFT36o0hP5GCcxXtS8484D7MzlcUI8Egtj1KPSOeIBe1pnlT_ubk607Xtouc_ah9jYy0OGhm87wqgrF0loBpnH0S-KpZGWfvdEvKxjThuFctEsZ8X4ar74sh8O8lfpDba63q11MrYveUCwyj1tDEeXj7gmmAAuRybnUMUqf334LPOvT8WaXtPfdj5GVslB6L8DJ8Id9n_Kd3GG4zTynEplYuARXboB8DIvRNwri8RcHGrdUqb2KogUpevr6qdxxRw7thYxRlJw7yNW5KjGAEBQ4Gmhbbd95wOpgrDlV3ukpRKeqG6JTrxKRfjqXqpkX-gMVGNOtjNS3g_ZAZjE2YNPwNwZXf9T99FY62cIuwz6RScmTbyk2Og-uKRHyqWmwX-7trI0vslfKzVCCUGYpgp4e3DVvKn3itxrvFZCREpVk9WHH2qlMGow8CTy2jKD-STfmr1Rvbj1F9Cei7CAGpguAv4BHIh8cpPXuwALQxRIHkUl7e6NH2c7dqzw4eSu0ZI9nHEwJkpSqaFGCQnVuFdV-2CTuvMWlDEjq0IqgvSezC9Esnysk5Wx4aXoGrjvMl39lotKZupnA-jz85dHFHI_YVDrUKAbXfhkeTx4s9YEbVcj2UCKasQnoO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رامبد جوان، بازیگر و کارگردان سینما و تلویزیون تاک‌شوی جدیدی برای نمایش خانگی طراحی کرده که به زودی وارد تولید می‌شود.
🔴
نام اولیه این برنامه «اتاق رامبد» است و قرار است در آن چهره‌های محبوب حوزه‌های مختلف فرهنگ و هنر و ورزش از ناگفته‌های خود درباره زندگی و زمانه با رامبد حرف بزنند. احتمالا رامبد جوان این تاک‌شو را برای پخش به فیلیمو بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137894" target="_blank">📅 15:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6qim61unEYps80rmtW5MdKX3BYdVl5KwVbfR3OpjjyY5Q4eDW2RVPM_ZiVeSrMVbRLTdp6AYejcGUbpilkuFjFOQhcNjPsbwnLqpMCnH-DT49WI3HkDAMZKqk4BWusVuzw3L4VedoRuy19FRFFFxjguufMIAFptmrkrHWoJx2lCQj4AdyFopdW3zdRrGHVBWZpDx-d1F-2Nca2ou5dJk9oaz4YBJrz6RM33RbY3id4AlZq-Lh3QUPfm7xa45HVvwOljXqitly6hjrwowT8WFLmNLpU5jPW2I6y_lP2pjsuISaO6w51eGUP5IVnHIqeLgA3H5CD8O7zvnUTgts9Krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال کاربران از قم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137893" target="_blank">📅 15:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQL8LiBvAoop-r1NyUnl-3M-LMkZtR77WPKQZ_wjSI1ZI1-DR_GX5b31nfx4Xhe4TiQpgwzPcTxDElW2tvJYHk2nRHijt03VOR-6hemhPCx-q1UKNcCSHQzoAFYsFR4wN369aj3NOh6dzW_PPYiUpG91A7NeWHGhY2APOy5m5j-WVvXi9oKrKxy8qLuuxhCXP2jUI3xcWURx_Chn-TCEPsj-RkekTdUe_F15HsYBU6Pq6NayIOP4RcTgXJKN11GzLVYxQW9WFOm3g0jHp7SUJAcuVlfVt3qKY-SuopndE3-Om6jmb82UbthyDlJBi6D74eJtkwSEy6o9iV6pIiiTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
🔴
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/137892" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343c49ad52.mp4?token=ZAp_r8HHAPT7aRKYJH3v9GK8BlKUUqdR30GsG-u2Q68nYQgywlQIgjAxzD1xvUNjUWXvzcle4qeyiVseNdnvhQ6Qy5B3xvnMNiUotq1uLv-Z8pXcfpxC-WmjfwRB-qHTKfSLIdc1Z81gHlJW4G9_zggI4RGTVweRz4hDTD7Tt-FQxe2pYuDcyXUHvzIaRnUFA0UZDiVsbynSkAWeI6AVrRZt84GmpgDpvHL5q1nOkwSb4hV2OwRs3TstDXTwX8CLGOfawAoxTamic-c5LBd9AR_Zulso3FSF0R_10J2qMAE8XLO4x1Ba-dOW7oHs9zkjrrrnY7fKdoqGuvdFniyj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343c49ad52.mp4?token=ZAp_r8HHAPT7aRKYJH3v9GK8BlKUUqdR30GsG-u2Q68nYQgywlQIgjAxzD1xvUNjUWXvzcle4qeyiVseNdnvhQ6Qy5B3xvnMNiUotq1uLv-Z8pXcfpxC-WmjfwRB-qHTKfSLIdc1Z81gHlJW4G9_zggI4RGTVweRz4hDTD7Tt-FQxe2pYuDcyXUHvzIaRnUFA0UZDiVsbynSkAWeI6AVrRZt84GmpgDpvHL5q1nOkwSb4hV2OwRs3TstDXTwX8CLGOfawAoxTamic-c5LBd9AR_Zulso3FSF0R_10J2qMAE8XLO4x1Ba-dOW7oHs9zkjrrrnY7fKdoqGuvdFniyj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای جدید از آتش‌سوزی در پالایشگاه نفت جیزان شرکت آرامکوی عربستان سعودی پس از حمله انصارالله یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137891" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اطلاعات نظامی اوکراین (GUR) در شب ۲۵ و ۲۶ جولای، یک پرتابگر و یک رادار 96L6 را از سیستم پدافند هوایی روسی S-400 "تریومف" در کریمه منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137890" target="_blank">📅 15:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb592bb5c.mp4?token=V-KGqloZxW8jL2Hl8R7XhtQZO-qp6hy_vwg1Wv3jKUWZEacRV9q1LBvFQhBOE69dWqp4Cy9N0Ekj6YwddMHvqWNQcGESPo_AOk13VFFMySQGjV-DmhWyokt244UCfCLqoGv3Nk9hNT0W6HDUhDheUmvdSofPJ7pvLiU6zY-JT-JSfmykV-mF0YWEC4AqO37fMTa3NwasC9YaRPMOexJacILO8waKmcWSLjSLChfHv2HbRLdD4XELaOsDibDpExq6vHC9Sfs5H_A0_Tt8a_AtiR0tX19fd-VDikEIF0rHX-iAuFNzuuP377I0263oBizUjfkytUPAuuRMEq6AdTSwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb592bb5c.mp4?token=V-KGqloZxW8jL2Hl8R7XhtQZO-qp6hy_vwg1Wv3jKUWZEacRV9q1LBvFQhBOE69dWqp4Cy9N0Ekj6YwddMHvqWNQcGESPo_AOk13VFFMySQGjV-DmhWyokt244UCfCLqoGv3Nk9hNT0W6HDUhDheUmvdSofPJ7pvLiU6zY-JT-JSfmykV-mF0YWEC4AqO37fMTa3NwasC9YaRPMOexJacILO8waKmcWSLjSLChfHv2HbRLdD4XELaOsDibDpExq6vHC9Sfs5H_A0_Tt8a_AtiR0tX19fd-VDikEIF0rHX-iAuFNzuuP377I0263oBizUjfkytUPAuuRMEq6AdTSwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو پیش از عزیمت به واشنگتن: ما درباره تمام موضوعات دستور کار، به سرکردگی ایران، بحث خواهیم کرد.
🔴
من با یک هدف روشن عازم این مأموریت می‌شوم: تضمین امنیت، قدرت و آینده کشور عزیزمان، اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137889" target="_blank">📅 15:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صداوسیما: علت حادثه آتش گرفتن انبار ضایعات پشت هتل استقلال بود
🔴
این حادثه تلفات جانی نداشت فقط ۳ نفر دچار دودزدگی شدند.
🔴
آتش‌سوزی در حال مهار شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137888" target="_blank">📅 14:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جنگ آمریکا و ایران موقتاً متوقف شد. ترامپ راه مذاکرات برای رفع بن‌بست تنگه هرمز را باز کرد، اما دولت او اعلام کرده تقویت نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137887" target="_blank">📅 14:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3777c0bf3c.mp4?token=snwrk-Pqj2nUfnZMIduZEcH9QyJKTvo1BX9GLNu6ivrQRAiovlpAyY_eOUj35lXiFNUhzsJ2-GB0Hdk7y0p9VU-W4j0naydFl-2R3qiSax88eVZuAdhyf9JyYtf6M5R7NEspOSTJYpsbH9fAX_80dswGkAXGcc6tS6Cd9hJ_YMjShAf2CWa4k2f6q2Flyixlq1_QzpiwTg6cbHMopUxwjvyCotdxS1FqXWpASkjacP77MCumHOaFel9_sd--kYx2Q92IaVt-Ps6zWRHPA99BvMdX3vdDTuMQ6J1cFK0420fh1sui2s61QY4FoFWCXQyHliF96pX9nNqNW2JxgtvJgCuTFNlILLNYcKIrez77Pu97sc5v5DRyVFgiGgF-qA6LTFO6Hzg1GlNE1rOtdpSLeUJqn7NMaXxo_8O5IzvYsv6Gea3dqgw6x_TzZ6NnwGLXm95oNJ3Hm2tmwuV15Q9iOrGYDgXepwsZQ6SHTMHfXLa3_W27HTJ8u_y2UJh3YzZCTTWMkWFRcy9vIkhCvIuvDfT54GK0RP9L9YGsfoQle2zl3pqL5v6EB7uO4Wscr3APsvZmn0FruFE7EFukQcKL9m2TmI9CMIxMoHY6y4455fGZImpR7hBP3IYXM8WHKtsaNJd_x8KgMfluiGHlr5tlyjDo5irCf1j2V2MW63czMrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3777c0bf3c.mp4?token=snwrk-Pqj2nUfnZMIduZEcH9QyJKTvo1BX9GLNu6ivrQRAiovlpAyY_eOUj35lXiFNUhzsJ2-GB0Hdk7y0p9VU-W4j0naydFl-2R3qiSax88eVZuAdhyf9JyYtf6M5R7NEspOSTJYpsbH9fAX_80dswGkAXGcc6tS6Cd9hJ_YMjShAf2CWa4k2f6q2Flyixlq1_QzpiwTg6cbHMopUxwjvyCotdxS1FqXWpASkjacP77MCumHOaFel9_sd--kYx2Q92IaVt-Ps6zWRHPA99BvMdX3vdDTuMQ6J1cFK0420fh1sui2s61QY4FoFWCXQyHliF96pX9nNqNW2JxgtvJgCuTFNlILLNYcKIrez77Pu97sc5v5DRyVFgiGgF-qA6LTFO6Hzg1GlNE1rOtdpSLeUJqn7NMaXxo_8O5IzvYsv6Gea3dqgw6x_TzZ6NnwGLXm95oNJ3Hm2tmwuV15Q9iOrGYDgXepwsZQ6SHTMHfXLa3_W27HTJ8u_y2UJh3YzZCTTWMkWFRcy9vIkhCvIuvDfT54GK0RP9L9YGsfoQle2zl3pqL5v6EB7uO4Wscr3APsvZmn0FruFE7EFukQcKL9m2TmI9CMIxMoHY6y4455fGZImpR7hBP3IYXM8WHKtsaNJd_x8KgMfluiGHlr5tlyjDo5irCf1j2V2MW63czMrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
مردم روسیه هرگز تسلیم نخواهند شد.
🔴
این هرگز اتفاق نیفتاده و هرگز هم نخواهد افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137886" target="_blank">📅 14:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT8f59t8-SrZi0QjlB6b5NJwaL9Qgai_jPHHmW5g97eRvoRXL2-tjrrvIeT7JouZLFPmaYflDuUfYjyf3WIUqCEUFe13AHm77RQkgOb0SFm3xYAf5RQ1X5FKr5A9v6EpuvnmuAqpeF6P-mC4Rll991WUN3hi-Tc9IKhkuUngEWISiods_fr1zczn4GO3SVljp7nXu6xYZyFGx3vdNGoRjHpFkjC8Ocg59TY4S62A08K9fVuOuKAZ7l6-msUyEClQc6G-DLpcLnpVsv5VZRuOeS--GZ-jm6VLEyG42YN8EzSgq6aWMzpGlsmYSRnRFxEdfiBL7dzFFVKvGgJPLobHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آموزشی مدل L-39 متعلق به روسیه در منطقه کراسنودار سقوط کرد. این حادثه در حالی رخ داد که خدمه هواپیما در حال انجام مانورهای هوایی پیشرفته در ارتفاع پایین بودند.
🔴
هنوز هیچ اطلاعاتی درباره وضعیت خدمه هواپیما منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137885" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWYDYem2SZj9w1-ie-iBU8BDKd19ecmgPT5e8H3r-TQBKKxtMVhRsQIsKyPbSwVrImB-L7zTNiSG6_DZGlJv9HSRIHyTHlgunEVwoXGIMYeIKDjRgWQ-iQn1q1fa1PgMHexhys4ASfs7VN2b6u5lx3ly0-X_VDi1GEPvIhiE3u1PSBRjOTfHOI826JeXdgFcTz3gK6wdz9JyiiGzzsoSLo7oP7r_4uM4nwVbTiI9ffKqmbHxoUjJoaViPqJ4Cpi-auyd24cEFBxbPgu_k5L5QDYll2hkvh-ISD97NN3YZrFE8elwIgsvBPgxd46_tTHSiKecVLuen39krM2zdN9YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاملا هریس آمادگی خود برای شرکت در انتخابات ۲۰۲۸ آمریکا را اعلام کرد.
🔴
این موضوع باعث جشن در بین جمهوری خواهان شده، چون معتقدند گوین نیوسام به مراتب رقیب سخت تری برای جمهوری خواهان می تونه باشه تا هریس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137884" target="_blank">📅 14:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گزارش از صدای انفجار در شهر کرَکِ در جنوب اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137883" target="_blank">📅 14:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تلاش آتش نشانی برای نجات ۳ نفر که در طبقات هتل استقلال تهران محبوس شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137882" target="_blank">📅 14:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd0y9twe9nIVWjY2f_kBm04UdKdjo_IstXCptv8x1nNp38bScaK_61qM8DJfRcNeN6B8qJRBgLT2tbAF39xGi9NQQwMb6imXqcBTXITh1k-Z_pVscTW6nKkgFjqrZ-3Sng3GkZA9TjHs0ytyE4VfFpmOj9UgIpMvJsyqnQBUZJKcku-ZV9VYKYaSpaTWzqzdzO4x7SspHnjKe8Cb96tu-n63NMq2_4VbxeKiySSkk_Ka33-H-z3KzNawefMWQcqH6fLMhmZ8BwXoE8pC2VbDb6jduvoKbo3bFnFaGvbT2L9eOwBCjeE8t-Swos0SNyO9KMOG0RCAAtnsuzScjzJNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انصارالله یمن: تاکید میکنم تنگه باب المندب به طور کامل به روی عربستان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/137881" target="_blank">📅 14:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4aac8d1c2.mp4?token=QqRPJEiidVkugm-p8Fpz6Hnp2JHq4S2yBOPU3sJDlXb6d5K4_LivkczMLrykBZdt0RLraZwflLWO2_P5fwl-30b5DA9G3DnanJvE6tpjObUtxEQB7Bsp5EvfVgVok8pVumwG80XhisNcQmzS1Z804JkdL8Z4A16qAvAjilbTaMc8D5BdJ5HhvogPm8xuTbCtAbvSuF_38CBV65ohMroreSEw1Mnvlwruw7NCMqDNMhbzkaTSGxG99I-CeHhKaMJhx31U2wfhxYC9xkky8FYG2dJ7WQjeKBRN6U8OeQYmhBS1nzx_hPlB0XYzJeOvSJdVu8nIVpiGHhg3I49cNzmLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4aac8d1c2.mp4?token=QqRPJEiidVkugm-p8Fpz6Hnp2JHq4S2yBOPU3sJDlXb6d5K4_LivkczMLrykBZdt0RLraZwflLWO2_P5fwl-30b5DA9G3DnanJvE6tpjObUtxEQB7Bsp5EvfVgVok8pVumwG80XhisNcQmzS1Z804JkdL8Z4A16qAvAjilbTaMc8D5BdJ5HhvogPm8xuTbCtAbvSuF_38CBV65ohMroreSEw1Mnvlwruw7NCMqDNMhbzkaTSGxG99I-CeHhKaMJhx31U2wfhxYC9xkky8FYG2dJ7WQjeKBRN6U8OeQYmhBS1nzx_hPlB0XYzJeOvSJdVu8nIVpiGHhg3I49cNzmLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نفتالی بنِت، نخست‌وزیر سابق اسرائیل:
نتانیاهو قطر را یک کشور پیچیده می‌داند. این کشور پیچیده نیست. این موضوع ساده است: قطر یک دشمن است.
🔴
ما باید از این کشور فاصله بگیریم و علیه قطر به عنوان یک دشمن تمام‌عیار که می‌خواهد ما را نابود کند، عمل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137880" target="_blank">📅 14:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137878" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137877" target="_blank">📅 14:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137876">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / نتانیاهو، نخست وزیر اسرائیل به سمت واشیتگن پرواز کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137876" target="_blank">📅 14:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137875">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
العربیه گزارش داده است از سال 2011 تاکنون 35 میلیارد دلار درآمد نفتی دولت عراق گم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137875" target="_blank">📅 14:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137874">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
زلنسکی :  ما سمت درست تاریخ ایستادیم
🔴
اینجا کشور خودمونه، خونه خودمونه. این خانواده منه و این کشور منه
🔴
من کشورم رو دوست دارم و هیچ‌کس نمی‌تونه منو ازش بیرون کنه
🔴
چون اگه ما ضعیف بشیم و پوتین موفق بشه، مطمئنم همه‌چیز رو از دست می‌دیم؛ آینده بچه‌ها و نوه‌هامون
🔴
ما نمی‌تونیم اجازه بدیم این اتفاق بیفته، چون پوتین هیچ‌وقت دست‌بردار نیست، فکر نکنید فقط اوکراینه؛ اون جنگ رو ادامه می‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137874" target="_blank">📅 14:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر دفاع جدید انگلیس: از اقدامات تهاجمی علیه ایران حمایت نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137873" target="_blank">📅 13:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137872">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oehLTtG9hpJuDXGY740XgHRMrgOgi8Qo50XPC3IdaPO7jUsyzTe3inzT1iN-YFfU2uQmh-4IuD8bPRfktp4KwH86JjVdYQx-7F5lUyxqb3y2Okr-dfhMx3-tSYULgJ3nho6-hfuFaxsaAJBOVd_ed928sjsXcIrHH9sIvTGl4Y3DaUSltY6D_uidw_Tr1iekyvCHDMEOhpWVTJaHK1hFLxYff1JERlFQUUuPtDT7FX8A9w-_X3L9JajscCH3lFujfkorSVU9Si_eyCxyioYmYCPac913H-05wxM5TbPRmHEZRzHSIVfo5b2LobJsY_mFDnAFsucebsRvtKlPEOBbmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که ترامپ از دیدارش با قالیباف (هوش مصنوعی) منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137872" target="_blank">📅 13:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137871">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFMEDnXeQtN6z3Hn4mEuq78QfAMQpmIlOMSlcQlKzyp6cAuzojizuVsePXEV82qumZEIV3_qE8fBo-1Jtni7HEuzfYMBv8WwVs9aurgEomFvhqlCd-EO7ypcHsm4bC-ajaoUmasJUT6yT_4IVLgXM6Ae5c4hRWY2jzzKWANRhp3JuRSZurvAsZGkP24G7kXdxpvTwyk_6ZNSORFK_JwQP1Kuav1PG2Lud_L2ISMKjseCVMhn7ZW7rhtqSLjt1est1YLmCdN-4zvs6exvVxSNqykbSZcarbendgIgUaLocVOeWcKpsBH2aXFE_2K2Sl_ROSosWzM496tsHXViYyInQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس: الان اسبابش را نداریم که از آمریکا و اسرائیل انتقام بگیریم، اما بعدا انتقاممون را خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137871" target="_blank">📅 13:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز با افزایش نسبت به روز گذشته، ۱۸۹/۴۰۰ تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137870" target="_blank">📅 13:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ادعای نفتالی بنت، نخست وزیر پیشین اسرائیل: قطعا کشور ما توانایی سرنگونی حکومت جمهوری اسلامی را دارد. اما یکی از فرصت ها از دست رفت، چون نتانیاهو قبل از حمله به ایران اقدامات لازم رو انجام نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137869" target="_blank">📅 13:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O506F6x_FxUk9O6fx_Ka-FP1n_ZknZRWDigeMOZd8BzUphNkcKX0z_BVYzEQS9X0mLkKzBNOjX0wbbkviUd0dXA7r1sN0QxHJxexdHosd1qJ8My_J5t_9CacxrlpuUl9eOKSxwGeFk1pkMTbSJaZMHhPlvUnyEOwD6DWqLtt7f7thuEGLnHTbq1KmOJYKxzYaAe8E76rnkd75Y1aS0z5NByqYhAdoB3onCCr--tFEW_aH1Jy9yVfgRLHPiEG4kFQVMGmc7nV71acMyRZJO83doPbOpO7ql1wKBO4V55wR5vxV7UmdLeuO5lZmXRarVFBMfsD3Tm1rQDVjPaYWuKkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری دیگر از آتش سوزی در هتل استقلال تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137868" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
تایمز اسرائیل: پرواز نتانیاهو به واشنگتن به دلیل نامشخص به تأخیر افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137867" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وقوع چندین انفجار در استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137866" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959eba656f.mp4?token=ma2o4TFbqMla0M4FjuS4J0AY0bDy-Y59IxfdyNba5Meguw8eSuAdFYLdoutVk5NcYekinAwJzqWGothWKB2ZpFX6rTgtiEPh__xr9_AGEZZzPLk4LtX5RuBa4iw5bOSmBnKBEG15m0FB-eGBy6idaQj-nHPehEOijtyZeKtQ0cyqtyGg5rUJXXdLG7kuSyY4ejzXsMm8mh4xiIEj7yKLZt1DMjGnIbbl73sciUyZEw9T_AzFJYnhEGYn9Dg4a8JWDZL9WXrMYECqU-9au0XQVIikPYyjCgbOHEsTCaL4DEOXPmzYbmZWhQs0A8Xeboz8WJW18kgrBXc_lfomtj64Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959eba656f.mp4?token=ma2o4TFbqMla0M4FjuS4J0AY0bDy-Y59IxfdyNba5Meguw8eSuAdFYLdoutVk5NcYekinAwJzqWGothWKB2ZpFX6rTgtiEPh__xr9_AGEZZzPLk4LtX5RuBa4iw5bOSmBnKBEG15m0FB-eGBy6idaQj-nHPehEOijtyZeKtQ0cyqtyGg5rUJXXdLG7kuSyY4ejzXsMm8mh4xiIEj7yKLZt1DMjGnIbbl73sciUyZEw9T_AzFJYnhEGYn9Dg4a8JWDZL9WXrMYECqU-9au0XQVIikPYyjCgbOHEsTCaL4DEOXPmzYbmZWhQs0A8Xeboz8WJW18kgrBXc_lfomtj64Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلاش آتش نشانی برای نجات ۳ نفر که در طبقات هتل استقلال تهران محبوس شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137865" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304d57163d.mp4?token=GjAicN5eForgMOecigC5fptB8jvsWUhNFrhWPAoZo7i3WyWwNZCtJlbLzK6toL2hQDlsEwwdwT3H7RHpAsE21EGHVazAI-glFeOCrVankXPGziXn-sUboR_rlJ1zir9xUWaj3jnWd_A54r3VZlxNDIlHCIZOOwNqTJ44tXrkRk4djliErXKsuiQczPqfqrpR4tKdney_dqyIATqXsMLTLM68v3wgKSratwqSoqMgpprH5MkpMaqrU3drygZq8l-LD33d7zFqPEOYqxb9Fbbq-WeERznRzcFzoA6Ruo8KZ5Wvha-mIb0zT4YXTVHByeQjrHDewKUJEDCvbxLAnLrtqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304d57163d.mp4?token=GjAicN5eForgMOecigC5fptB8jvsWUhNFrhWPAoZo7i3WyWwNZCtJlbLzK6toL2hQDlsEwwdwT3H7RHpAsE21EGHVazAI-glFeOCrVankXPGziXn-sUboR_rlJ1zir9xUWaj3jnWd_A54r3VZlxNDIlHCIZOOwNqTJ44tXrkRk4djliErXKsuiQczPqfqrpR4tKdney_dqyIATqXsMLTLM68v3wgKSratwqSoqMgpprH5MkpMaqrU3drygZq8l-LD33d7zFqPEOYqxb9Fbbq-WeERznRzcFzoA6Ruo8KZ5Wvha-mIb0zT4YXTVHByeQjrHDewKUJEDCvbxLAnLrtqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
زبان انگلیسی را ترویج نکنید چون میراث دوران طلایی پهلوی است!
🔴
مدرک تافل مجتبی خامنه‌ای موضوعی است که توسط طیبه ماهروزاده (مادر همسر وی و همسر غلامعلی حداد عادل) در خرداد ۱۴۰۵ رسانه‌ای شد. او اعلام کرد که مجتبی خامنه‌ای پیش از خواستگاری از دخترشان، مدرک تافل زبان انگلیسی را دریافت کرده بود.
🤔
خودشون اگه یادبگیرین ایراد نداره ولی واسه مردم عادی خار داره. یکی نیست بگه این مشت گوسفندی که عربی یادگرفتن به چه درد خوردن جز اینکه بالا منبر نشستن دروغ تحویل مردم دادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137864" target="_blank">📅 13:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=i63Dv2isbNTDo41XIySaF2ogdruEY-H9LZdU2HUddMy2jiUDlEyCqzPvHVHKV8vpsATS-mfW7JI6kTaJ0yznHmpsV8LorNEskYulrC5DZ3zzDv9eYGmBeXWnQbi8J_9W9DUU7YsI4zrn2xxwIokDbK13Hht-GaGMEBXSyqKgCEVrbu6wTgZgHQs6FZ9qf1juoj89AgOzw5YvJ2bKf-BVaXgcbphZNRh8Yqs83__6PgwHvvbv9md_gLG3TnzLXp2B7srMzTU2nd9QCr9duxaeto2WEDmfNpzWZRP5hFvAH3ooHEtpwvxEP8DfRhqch862ZLktmQzTKXNuF6VNHh84eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d584dd517.mp4?token=i63Dv2isbNTDo41XIySaF2ogdruEY-H9LZdU2HUddMy2jiUDlEyCqzPvHVHKV8vpsATS-mfW7JI6kTaJ0yznHmpsV8LorNEskYulrC5DZ3zzDv9eYGmBeXWnQbi8J_9W9DUU7YsI4zrn2xxwIokDbK13Hht-GaGMEBXSyqKgCEVrbu6wTgZgHQs6FZ9qf1juoj89AgOzw5YvJ2bKf-BVaXgcbphZNRh8Yqs83__6PgwHvvbv9md_gLG3TnzLXp2B7srMzTU2nd9QCr9duxaeto2WEDmfNpzWZRP5hFvAH3ooHEtpwvxEP8DfRhqch862ZLktmQzTKXNuF6VNHh84eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از حمله پهپادی ایران به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137863" target="_blank">📅 13:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mujO9Vl0W48_tm_v-K4NM74KFdcuUDW5_l1ngXl4RL9qB7hgdTmHk2MY7ajcth6LA6vz1BEFvK2YCVwYyhmJDtNv3ceulH5BJNmR7B6EuU8WCJvm1vlFO_zRABDqbVOPKuKJG5_6tTU-6e-FHI06G1APbVyfxLPbb7wPFh_nbBQNNwjmyqvX7zzoEVomB1WWIHDu_Q_yqRsOH0o7fZQDP2XWcNsk25wXTW_z3GVWanIZCDwQDasfyfiyHzWsmGeEcciMI-JDj8QjG1tDZRWReCEfyhUfYdZWG7nS810XfCpnGBlcFxA5M8y09HXfS5PXziBarBJ5_JMWRK80aHC7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بروجردی، عضو کمیسیون امنیت ملی مجلس: اکنون فرصت بسیار خوبی برای ما فراهم شده تا تحریم های آمریکا را آغاز کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137862" target="_blank">📅 13:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وقوع چندین انفجار در استان اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137861" target="_blank">📅 13:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فووووری / برخی منابع خبری از وقوع انفجار در اردن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137860" target="_blank">📅 13:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0203c0440.mp4?token=SGbGFli1gZ7xO6qIKRQsCIkvYoFrpZSCJKdL6TLzOZyrqYb7FSZFimjCQim4v649j4Pgmv8foFYua8DpaaIatTkGSZonpOBjZpKVWeCYsrqwUqWBF2-1pbAJmKNSLgpZiHZXDLxOzNLrUEvphWQpuYpqxyVa4CfnJpa91mwH-X4RYgsmDwI2lSAVljPJiNt5-fGBWAZsf73omgKGyC55Mrdvdb17DqMOYKxqwOW_g4HeDzyf9p1VhYEqOamkixJUvP87lsv68OAOicC9ZJvoNxmJih2zPfJuzXL2LxPHdSYcV5ZlyN1L4o4tVbdX6Yw5FAsb-QCB_23PrTJR5kiIrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0203c0440.mp4?token=SGbGFli1gZ7xO6qIKRQsCIkvYoFrpZSCJKdL6TLzOZyrqYb7FSZFimjCQim4v649j4Pgmv8foFYua8DpaaIatTkGSZonpOBjZpKVWeCYsrqwUqWBF2-1pbAJmKNSLgpZiHZXDLxOzNLrUEvphWQpuYpqxyVa4CfnJpa91mwH-X4RYgsmDwI2lSAVljPJiNt5-fGBWAZsf73omgKGyC55Mrdvdb17DqMOYKxqwOW_g4HeDzyf9p1VhYEqOamkixJUvP87lsv68OAOicC9ZJvoNxmJih2zPfJuzXL2LxPHdSYcV5ZlyN1L4o4tVbdX6Yw5FAsb-QCB_23PrTJR5kiIrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویری از آتش سوزی در هتل پارسیان استقلال
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/137859" target="_blank">📅 13:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137858">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فووووری / برخی منابع خبری از وقوع انفجار در اردن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137858" target="_blank">📅 13:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137857">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ریاض: گفت‌وگوی تلفنی وزرای خارجه عربستان و عمان در مورد تضمین آزادی و امنیت تردد در تنگه هرمز
🔴
وزارت خارجه عربستان اعلام کرد: وزیر خارجه عربستان با همتای عمانی خود در مورد تضمین آزادی و امنیت تردد در تنگه هرمز گفتگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137857" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137856">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / دفتر نخست‌وزیر اسراییل از به تعویق افتادن سفر وی به واشنگتن خبر داد، اما بدون ارائه توضیحی درباره علت این تصمیم، زمان جدیدی برای انجام این سفر اعلام نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137856" target="_blank">📅 12:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137855">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، اعلام کرد که در صورت بازگشت به قدرت، قطر را «کشور دشمن» معرفی خواهد کرد؛ او قطر را به تلاش برای نابودی اسرائیل متهم کرد و مدعی شد که این کشور بودجه سپاه پاسداران ایران، حماس و جبهه النصره سوریه را تأمین کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/137855" target="_blank">📅 12:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwNbnM-7Dmidd9MuNDtOEgHDH_dbK0AqqqxuWxV820g6U6CgWmRDCX4T6fbByh7ayAIXkoZJ3TYYFlscMHV0iho-FUcpCMcLJ3iAsKlvLRMF8K46QCrgTng3GjXf8cGzjbZIIhnd8Co2YyTtvR24nQko_g25ihIlzXEyLSk4pa3miokQxOPjfQ0rLvvn0515z2oqjlzbgzLs1O302fCKi6gonO9u66CtIlIKqcKZShq9IgAV0mcBeCogL11QOoiyJvAC5m2z8DuEAqlpyk8rFX_vhKrUVMlMXXbvi-iReKi7VgR6naISgvC_s-PmTP6-5SaVQn8GqFqikX_lqjyRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در جریان معاملات امروز شاخص کل‌ بورس با رشد ۴۹ هزار و ۷۱۳ واحد در ارتفاع ۵ میلیون و ۵۲ هزار واحدی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137854" target="_blank">📅 12:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سازمان امنیت داخلی اسرائیل (شین بت)، گفته است که ایران در تلاش است تا در انتخابات پیش رو در اسرائیل دخالت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137853" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8195b31d40.mp4?token=d-BgWc-XGLxN6xFsyccFCPEO6je0-1FPn9_rPTtdGwigmnrwTFSjEETmATmyGHH44B8vTJ5XNMY1g_MuFPPQfUDU71f-XIGCR6gTxDGIgN4mPtcoVwo9i6NKWLp1d-fRRlIcdJDEipp00wpponpFxVl5u5Z0fpgqV2SUXX81L0qFC_RDUsEDlULvkmTaaAJumVQlMW8WgqbFnuhz0iqFnFWQLQjZEAnQ-23NHhEYDhbtC2skfwnI6k-LcYtQSyO-w9NHC3p62r_-IZQ4AqZ-aJ3TxTlAJH5r1nW2BqsHIOhYiaZQa4zibyrf5F4-_X_1SrFQQ7AMSOqQeLY3UvoV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8195b31d40.mp4?token=d-BgWc-XGLxN6xFsyccFCPEO6je0-1FPn9_rPTtdGwigmnrwTFSjEETmATmyGHH44B8vTJ5XNMY1g_MuFPPQfUDU71f-XIGCR6gTxDGIgN4mPtcoVwo9i6NKWLp1d-fRRlIcdJDEipp00wpponpFxVl5u5Z0fpgqV2SUXX81L0qFC_RDUsEDlULvkmTaaAJumVQlMW8WgqbFnuhz0iqFnFWQLQjZEAnQ-23NHhEYDhbtC2skfwnI6k-LcYtQSyO-w9NHC3p62r_-IZQ4AqZ-aJ3TxTlAJH5r1nW2BqsHIOhYiaZQa4zibyrf5F4-_X_1SrFQQ7AMSOqQeLY3UvoV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آنتونی جاشوآ بوکسور سرشناس بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه دیشب خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی خواننده سرشناس ایرانی وارد سالن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137852" target="_blank">📅 12:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رویترز: کاهش حجم حمل و نقل دریایی در دریای سرخ همچنان ادامه دارد، این در حالی است که حوثی‌ها به تأسیسات نفتی عربستان سعودی در دریای سرخ حمله کرده‌اند. تنها 11 کشتی باری روز یکشنبه از تنگه باب‌المندب عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137851" target="_blank">📅 12:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2gRVJTxO3KxusR-fDc1TsE3vvyoXyfGVsdvVCOiVhNMVFq3qPOrbcwPwfXlnclh9gc9BCXxCXRoYIeOnGwZnkkVnzWRkMzzT0JeUh7RlAuMJMOkbwl9qmJfGVsQdWKv_4inrgXIO3algHxhwcupGJlwNudV1EQnCNc93wFGFRZqvS1Zqiy2M1Kz-QLNY0krtsudkWv8MldfBpd9YjZ7j4UsA4xZ4EmCx3LBE2MlY7dIjyUg1h32h3qRCryvH6fVMwXwxcVMK7U0fiLOggDqbqyVQQmYEGO8WpyzfsNhfsWB_2jXtvaCa1TcFsu9Tm7t288Vf1c633s7BeTqHQrJxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری پر بازدید در ۲۴ساعت اخیر
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137850" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137849">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68be3b8cf.mp4?token=a_BE0Gi0YdVzw5tdyrZDd0hV7itZDRNP-dxpkd93JiavkjZmZP3d1rFS7WsuiZkjBfgvQIdJ3Son5HwAAQYG8yg9flQT-ups-_QOyu7-sf7ByWUXXIgn8zC6lexAX6klrU-HZyYcMU-w16vSnlYxbtYF-Qocfk0Ft73jpAFbF3s5ZIMq28EING0UrFiJgUPkCRlSMfXckXbXnbiFZT0jgjTHasHFaUdt9doGLq-B5O5EADKVRh6JrXftiU7OwraNwR15X4HH9H6V9VWzPKeLHuzuw2XGjtD_-Tg_yNdnWp1qL2xo5OqETIBFPYvL5GV7RMhH1l635LHZXJmK2ozD5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68be3b8cf.mp4?token=a_BE0Gi0YdVzw5tdyrZDd0hV7itZDRNP-dxpkd93JiavkjZmZP3d1rFS7WsuiZkjBfgvQIdJ3Son5HwAAQYG8yg9flQT-ups-_QOyu7-sf7ByWUXXIgn8zC6lexAX6klrU-HZyYcMU-w16vSnlYxbtYF-Qocfk0Ft73jpAFbF3s5ZIMq28EING0UrFiJgUPkCRlSMfXckXbXnbiFZT0jgjTHasHFaUdt9doGLq-B5O5EADKVRh6JrXftiU7OwraNwR15X4HH9H6V9VWzPKeLHuzuw2XGjtD_-Tg_yNdnWp1qL2xo5OqETIBFPYvL5GV7RMhH1l635LHZXJmK2ozD5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشون می‌ده یه مخزن سوخت تو پایگاه «موفق السلطي» اردن، مستقیماً هدف حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137849" target="_blank">📅 12:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137848">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت دفاع روسیه: بامداد امروز نیروهای مسلح روسیه به حملات خود به بنادر مورد استفاده برای تحویل محموله به نیروهای مسلح اوکراین ادامه دادند.
🔴
دو کشتی باری در بندر نیکولایف در حالی که محموله‌های نظامی را تخلیه می‌کردند، با پهپادهای تهاجمی روسیه مورد اصابت قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137848" target="_blank">📅 12:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رئیس اتحادیه تلفن همراه و لوازم جانبی تهران : با توجه به نوسانات شدید نرخ ارز در کشور، امکان پیش‌بینی دقیق روند قیمت‌ها وجود ندارد، لذا توصیه می‌شود متقاضیان، تلفن همراه را در زمان نیاز خریداری کنند؛ چرا که موبایل کالای مصرفی است و نباید به چشم یک ابزار سرمایه‌گذاری به آن نگاه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137847" target="_blank">📅 12:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چین نیز مانند ما نگران وضعیت صلح و امنیت در منطقه و در سطح بین‌المللی است.
🔴
هر دو کشور نگرانی جدی نسبت به استمرار یک‌جانبه‌گرایی بسیار مخرب از سوی آمریکا داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137846" target="_blank">📅 12:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=uqcCog760TCcd8YmdVord3YlHjU319Fm4Bi3r-h2fYQR7taMwlqwuEK6Mq3K6ofaVJOeBrBMULv7dm-tQoBH7f7oWJrlPawAZS5WKvYq2gMMN8dwvMM3t4NoVAfEvUO4uPdO7mawsqM1HUiO4QlvBy1s1aHeKUjCVI91PiPn4wgCkcR4klGawxf-axjmFaWOdj8veiFFn3XkCA1Qg21EZ2NzF2Adw0OcBP2-HEuHOgpI1FOriOE0Vo8k7eKajd3jMIWzDW1UterJhwlD9n8SV1amNCkIuV_8zwF4gr_rjVGncqq405kZFCe0OS4zSt3ENqtVFHhfvDQwBIwCmUbQfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9015499bb8.mp4?token=uqcCog760TCcd8YmdVord3YlHjU319Fm4Bi3r-h2fYQR7taMwlqwuEK6Mq3K6ofaVJOeBrBMULv7dm-tQoBH7f7oWJrlPawAZS5WKvYq2gMMN8dwvMM3t4NoVAfEvUO4uPdO7mawsqM1HUiO4QlvBy1s1aHeKUjCVI91PiPn4wgCkcR4klGawxf-axjmFaWOdj8veiFFn3XkCA1Qg21EZ2NzF2Adw0OcBP2-HEuHOgpI1FOriOE0Vo8k7eKajd3jMIWzDW1UterJhwlD9n8SV1amNCkIuV_8zwF4gr_rjVGncqq405kZFCe0OS4zSt3ENqtVFHhfvDQwBIwCmUbQfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت ساحل دریاچه ارومیه را مشاهده می کنید که غرق در زباله و کثافت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137845" target="_blank">📅 12:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNqeOmTPiQt9IG6PEsm9roK5PEJTTJC1BVtMLPjjgc8clatlK4LRierpP1pfTy_SXIHvMMqLX_RBWAMkiYNSj4Mf4uI7HpYe6HFnP6A8BySX29fiSWPpfHlQ2oh6RqY8w68rtp9ivPkmd1NZ1PFCedlIlBCecZ8aTqr0NnlOe719WphuyecKo4Uhq6WKiVQk5CEyk35QeCZHWwr1PFItPQ4DzaNCxgWLJqegqIpdkr_JLWAc0qdbEvEKKsqN88ZpEscZwqqygpTtmIdkJtb6iQX-PgG31X0rGvxmuKwJLtDRzBx4H3mmFcwjIfkfINnMZUBL1V87ubDzAa7j1uwFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نیما مرادی، جوان انزلیچی که در حمله اوکراین به کشتی ایرانی در دریای خزر جان خودش رو از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137844" target="_blank">📅 12:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26576790db.mp4?token=g1JWFZK99-hTC73CSEXMAisi5PRAOZAqQC1uh4KvjU-oZVzRUekiT4nmQSmFFTBoqif_S5CQEcSCqNcwIyAzENfB-1BNbL5bPxRKyFwdzCtsHfnWsmOpeiV4IG1xRERtHZDOv-syUtpQ3TonHzl-pWGQOQVtjq8JfJ50xK6PI-lA2NiV9saiwzlD8MNA7pENczXJOB3LgSlIL5xVxYkjaTfTohjEuFNSMh-nPW_xFcc2vj6J95CsdeTV3UdfiagWvMjGWcBm8Wkn0udpNu2DSgoffgr_RbjJCzwvsxjWP_mUaRn_3m2p3HNervcKtdMiB3fHYpWswdTbMKs3MO5wTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26576790db.mp4?token=g1JWFZK99-hTC73CSEXMAisi5PRAOZAqQC1uh4KvjU-oZVzRUekiT4nmQSmFFTBoqif_S5CQEcSCqNcwIyAzENfB-1BNbL5bPxRKyFwdzCtsHfnWsmOpeiV4IG1xRERtHZDOv-syUtpQ3TonHzl-pWGQOQVtjq8JfJ50xK6PI-lA2NiV9saiwzlD8MNA7pENczXJOB3LgSlIL5xVxYkjaTfTohjEuFNSMh-nPW_xFcc2vj6J95CsdeTV3UdfiagWvMjGWcBm8Wkn0udpNu2DSgoffgr_RbjJCzwvsxjWP_mUaRn_3m2p3HNervcKtdMiB3fHYpWswdTbMKs3MO5wTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی :  بخش زیادی از مردم و نمایندگان پارلمان بلغارستان با میزبانی از هواپیماهای نظامی آمریکا مخالفند
🔴
دولت بلغارستان باید بابت این تصمیم پاسخگو باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137843" target="_blank">📅 12:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بقایی:  موافقت ایران با آتش‌بس ده روزه واقعیت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137842" target="_blank">📅 11:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری /
بقایی: هرگونه اقدام آمریکا با پاسخ قاطع ایران روبه‌رو خواهد شد ، در حال حاضر هیچ مذاکره‌ای با آمریکا در جریان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137841" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بقایی: نمی‌توان اسم وضعیت فعلی را آتش‌بس گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137840" target="_blank">📅 11:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:  چند دور مذاکره روزهای جمعه و شنبه بین ایران و عمان برگزار شد که مفید و سازنده‌ای بود.
🔴
این گفت‌وگوها درباره نحوه مدیریت تردد کشتیرانی در تنگه هرمز انجام شده است.
🔴
هدف این است که ایران و عمان، به‌عنوان دو دولت ساحلی، سازوکارهایی را برای اطمینان از کشتیرانی ایمن در تنگه هرمز، با رعایت حقوق حاکمیتی دو دولت ساحلی و همچنین حفظ امنیت و منافع ملی ایران، تدوین کنند.
🔴
درباره وضعیت تنگه هرمز نیز تأکید می‌کنم که هیچ تغییری ایجاد نشده است. کماکان، به دلیل اقدامات تجاوزکارانه آمریکا و ناامنی‌ای که این کشور بر منطقه تحمیل کرده، تنگه هرمز بسته است.
🔴
این مذاکرات هیچ ارتباطی با آمریکا ندارد. موضوعی دوجانبه میان ایران و عمان است و گفت‌وگوها نیز همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137839" target="_blank">📅 11:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137838">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در مورد ماجرای دو دیپلمات فرانسوی در ایران:
آنها به بهانه ارتباط با جامعه مدنی، مرتکب مداخله در امور داخلی ایران شدند و برای خود مأموریت‌هایی تعریف کردند که اساساً، طبق همه تفاسیر معتبر از کنوانسیون روابط دیپلماتیک، مصداق دخالت در امور داخلی یک کشور محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137838" target="_blank">📅 11:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=IWcbcTVbTZfig2a2zOl-Z87WHx8rO_c_Y1HBp7GYrFykZkoa5pEoe2FcD6xyHiMUXG6SqozcvOCJx0hngQSWhvhp7PLIDQch6YGsxex7deBwMH7LfGEHnBflixlgBwCo-C5YIpKuYfVEfQ9l4yllNOyjPEt-lEKazmamHt7smbxXCVrNWW57Ly5zS7YHy8DyxYh15zdmxMdYnG49L4Ge3YEUDhLmCFjpDNu18Ou0jRYWNrxjUCAGqB0esiLw_q0HEeh_R_Dzn6iTnonayl-evf53tGBFzo_S-hToR0Xm4AeKOeyTWVGNJjFegJUO3EGAxsXL_0M_zGBKp1sOw1082w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a72fd89b2.mp4?token=IWcbcTVbTZfig2a2zOl-Z87WHx8rO_c_Y1HBp7GYrFykZkoa5pEoe2FcD6xyHiMUXG6SqozcvOCJx0hngQSWhvhp7PLIDQch6YGsxex7deBwMH7LfGEHnBflixlgBwCo-C5YIpKuYfVEfQ9l4yllNOyjPEt-lEKazmamHt7smbxXCVrNWW57Ly5zS7YHy8DyxYh15zdmxMdYnG49L4Ge3YEUDhLmCFjpDNu18Ou0jRYWNrxjUCAGqB0esiLw_q0HEeh_R_Dzn6iTnonayl-evf53tGBFzo_S-hToR0Xm4AeKOeyTWVGNJjFegJUO3EGAxsXL_0M_zGBKp1sOw1082w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: شایعه تعطیلی سفارتخانه‌های اروپایی در ایران را به حساب جنگ روانی آمریکا بگذارید که در آن استاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137837" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تصمیم‌گیران بلغارستان باید در قبال تصمیم خطرناک استقرار هواپیمای سوخت‌رسان آمریکا در پایگاه‎های خود پاسخگو باشند
🔴
اطلاع داریم که بلغارستان پیش‌تر نیز اجازه استفاده از فرودگاه صوفیه را برای استقرار و بهره‌گیری هواپیماهای آمریکایی، به‌منظور پشتیبانی از تجاوز نظامی این کشور علیه ایران، صادر کرده بود.
🔴
مردم بلغارستان به‌خوبی آگاه هستند که مردم ایران هیچ مسئله‌ای با این کشور نداشته‌اند. ما طی دهه‌ها روابطی مبتنی بر احترام متقابل با بلغارستان داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137836" target="_blank">📅 11:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdIvaY6xwpJUZfk5iRoe24F8FPAzxc58mYEr12x8syYmrk7NJWOj1GD_-XDtLWQ_GpajHWCaHftliKqoaFpCiVoPvNOd_w5zRXWHQPJZ-5RRrv7aKnfr-eSZfyzOyibrOz1fJPBEOjr4oUSFSdvFPLQnSVNtctylJ8b6RWi5ZA_KHtjp16ygiPdlpXgNRTERCQlx-Fc_fRBArUG7afiflKMUhjKZR9BqRN1WyIFTNJId9IzVqfbwkIXAvDvWCMvTuZILEQI564ZbdHyz_caNq7ByzSfP550Jh7dKumHDHxMuCvvGQulVtulp-BwAcGzYG7x7bMeU5F4WVzjoLcO5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماجرای عجیب قاتلی که همسر اول و دومش را به فاصله ۱۵ سال به قتل رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137835" target="_blank">📅 11:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : دو پهپاد تو مرز اردن منهدم شد؛ منبع پرتاب در حال بررسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137834" target="_blank">📅 11:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=p6dkNK74_XcZiQEm-AO0jueKgkNW9dQbcam6fgwbcQUosuuB9a77L4LJUOq0T2wLJ9riPIFQ-xkGrRzc9vEdhnjx4-oRMGt_ijNLVknvRD9nJLpbk5dvJa9G8ZIN2f3L2kKCLG17ib2J7LoIwfqIskkClZO6Mj84VnI1a2tWQwBVXHq9MvpF9G00HjRWHq-_WSLWRZeBFIVLrjc90p6q07k3BWqaPyp9TDRyePORf5-TUhquyn0EN1fuFI5BrUadAr-9kHR2c-2N1rRFAgXpVnis7rr8rVMN-t-yUiT8JRaFOyctIIvh-H_IjaKAEED7jxdiNHM2vNnlUMCiTwF9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e738b35e9c.mp4?token=p6dkNK74_XcZiQEm-AO0jueKgkNW9dQbcam6fgwbcQUosuuB9a77L4LJUOq0T2wLJ9riPIFQ-xkGrRzc9vEdhnjx4-oRMGt_ijNLVknvRD9nJLpbk5dvJa9G8ZIN2f3L2kKCLG17ib2J7LoIwfqIskkClZO6Mj84VnI1a2tWQwBVXHq9MvpF9G00HjRWHq-_WSLWRZeBFIVLrjc90p6q07k3BWqaPyp9TDRyePORf5-TUhquyn0EN1fuFI5BrUadAr-9kHR2c-2N1rRFAgXpVnis7rr8rVMN-t-yUiT8JRaFOyctIIvh-H_IjaKAEED7jxdiNHM2vNnlUMCiTwF9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا می‌خواست در ۳ روز ایران را تسلیم کند اما حالا بعداز ۵ ماه در باتلاق خودساخته گیر کرده
🔴
تصمیم‌گیری دربارهٔ منافع ملی کشور معادله‌ای چندمجهولی است که در یک روند مشخص با مشارکت همهٔ دستگاه‌های تصمیم‌گیر انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137833" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس پارلمان لبنان: اهمیت ضمانت ایران، عربستان و ایالات متحده برای حفظ ثبات لبنان
🔴
تنها راه قابل قبول، عقب‌نشینی کامل اسرائیل در کشور ما است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/137832" target="_blank">📅 11:16 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
