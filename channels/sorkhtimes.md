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
<img src="https://cdn4.telesco.pe/file/rkdFbq4FaUT-jWbuyhy3PgoAF91wCKLGCzd2_E1MQkPK6EpP5vpqiGAtEnUiq5IRo3eDEjiC_z-jshNY8jh8cVpwBVFXJVFchR9TAhPYgTgGF0t4o4wvVVoLEiUr7hjqHQgSh-dRzj81aCvSJwcJra-dI38CdWxBXWTniS7HdQyV-iFjIfYjORL2C3QqzFrVISmtIat2GAsAF4C9NBx4nEoh19hhuAFRKsxVTSK4-XJlf_RulHDzlyh2GS2SwX3e_b2-RKYFNhAyVw5Btc01vkEH0GRAo8vSpPGyPOLjCTiUTm9Nozds8hvkrqpnhQp7Cyg-pAPgOGdylbsmjQekRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/140205" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtBtqR_TgKlqL-lLkvwCQXMarzitSBpY_VIYi73uygs06MAFl0X1hB16Z8DBue9F28_ZHdYwRz2salyvL7fwpvVMZfGQZfKCqRyd4bdZdfTuE7MfhaTofyTL9k80UH-gUQR4M-0WfqDede6jf5lxfKdIVP4MNk6s4w6VNraiheOn_fZLvx0JFdfwwfC2jqxmeRoCvbZ88PYYcK8XXHPzmD08Cw7TdUv2dL0w7AONdePQzB8oxptc_ajFbwy-99yVT6eaWuQS6GiVToY5Q_YcjWta3S-G3pokBb_gZPjKfeTw1J9G9TwDuB4vAkk9pdUusqvNw1rNcF3KjEc5f4kglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/140204" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140203" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=SykwPOKREXyi8ozAn1xOfNxf1pb5yzgcJQdoWcVDFH--_X3N_yYQkOYoJQuaRRRRoAelxgnMotGyT4r6-e12L7StN1Y64ryi85zX41Mj1XL0TT2XeZqNQzQ4klG8qb4RF0MhINSaZseVQ4GeTMYpcnFS8_Ut4Z9_2jt0oonBv-oBNg24VCBQro2gPDVNj90fZ_uETMI8CjG4ezGLMtYZr6M7zcfGO9QkWFvK4VkO0bXHqlrK5TySgTl1SY5yDvNjCx2c2N5f8QnGLLY03lRHAtS1Yn5Bns5DAuuSJFIfZFm6wAdKhw8Zit5nnxzesjCabdHlDFAHg5E9TnqZ7_m5GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=SykwPOKREXyi8ozAn1xOfNxf1pb5yzgcJQdoWcVDFH--_X3N_yYQkOYoJQuaRRRRoAelxgnMotGyT4r6-e12L7StN1Y64ryi85zX41Mj1XL0TT2XeZqNQzQ4klG8qb4RF0MhINSaZseVQ4GeTMYpcnFS8_Ut4Z9_2jt0oonBv-oBNg24VCBQro2gPDVNj90fZ_uETMI8CjG4ezGLMtYZr6M7zcfGO9QkWFvK4VkO0bXHqlrK5TySgTl1SY5yDvNjCx2c2N5f8QnGLLY03lRHAtS1Yn5Bns5DAuuSJFIfZFm6wAdKhw8Zit5nnxzesjCabdHlDFAHg5E9TnqZ7_m5GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/140202" target="_blank">📅 21:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140201" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
#فوری | ترامپ: هر اتفاقی ممکن است بیفتد
🔻
تصمیم بزرگی در پیش دارم؛ آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است
🔻
به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140200" target="_blank">📅 21:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0ZXofgs6TcZeXkdBwxZYBh2rQ7SAbg03LJch0Dd_ttg05HcPF5nt1jeTRYnGZy4hxvFchHZu-xplVaeu-AJ5XhyKVXxIqdxW29fERumy7cNgcNBBRXMaQmhcbRnTFDwkeBeeUyPeeZfhfXlCZaXxk8v2O6Oc0zpzAnRIWlcseDfvj1v97-cS3x6KdU5pJ-0vgScHk95w6xjo5j8gulX9BVRGYxZPIASlPxS2ZR6ZQaQbQI2k_GlKS8j2za8VuZPxgyS9it2EEvg_IvdcYrFLyA8l2FG0uoI7lkw5VEeZE5qgcFPWVyttVTRe6lC6g5oAzM4OtMm_FYvgoyglysl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
❌
❌
در اقدامی عجیب علیرضا اشرف مدیر رسانه‌ای پرسپولیس اشتباهی عکس لخت خودش و پسرشو فرستاد توچنل‌رسمی پرسپولیس و زود پاکش کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/140199" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140198">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔄
🔄
علیرضا اشرف، مدیر رسانه‌ای پرسپولیس: خوشبختانه آسیب دیدگی ابوالفضل جلالی جدی نیست و با استراحت و ریکاوری مناسب، به بازی بعدی میرسه  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/140198" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140197">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140197" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140196">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
پرسپولیس قصد داره قرارداد امیرحسین محمودی رو با بند فسخ ۱.۸ میلیون یورویی تمدید کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/140196" target="_blank">📅 19:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140195">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
سازمان نظام وظیفه به علیرضا جهانبخش اعلام کرده که معافیت‌تحصیلی‌اش رو به‌پایان است و باید تا اواخر آذر ماه تکلیف خود را روشن کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140195" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140194">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB1DV-EppOpCYW2AKZgEgueZ_woHpG_gF0nbMNMWLICYQAxgvk0Qa0NSo0wJY8DON9Q4r7R0c-fjJq8y_q6iWhyAms_iX4ycrgFRMacZ1J4CCETIzBLVNFpre5BR52GM5w7ESZbiFDDuRf26d9AE7D9C57CTObp2tLQU8yEB21jSoocWZFKjDNWcKCrVLwIBjD0VLxtKocwuSIUvtGCWOAV22g30OAtRlnN-fvcoV5zQn3mKFAZPB-O8cTWxtzVqb-W4Xgx1js8E9zrjOWDS23PTx72dx7-vXiJBhqcEBqyWL_jUSteriVJH7Vj6OywuI8kC9YyaeMsQ38GDwq2p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیتی و نوریچ؛ شبِ امتحان برای سیتیزن‌ها، با یک حریف که چیزی برای از دست دادن ندارد.
[
منچسترسیتی
🔵
🆚
🟢
نوریچ‌سیتی
]
⚽️
سیتی با مالکیت و گردش سریع توپ، از همان ابتدا برای کنترل بازی جلو می‌کشد. نوریچ احتمالاً با دفاع فشرده و ضدحملات به دنبال ایجاد خطر خواهد بود. اختلاف کیفیت دو تیم به سود سیتی است، اما باز کردن خط دفاعی نوریچ چالش اصلی بازی خواهد بود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/140194" target="_blank">📅 19:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140193" target="_blank">📅 17:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140192" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
مراقبت از پوریا شهرآبادی از دست ایجنت‌ها جزو اولویت‌های اصلی باشگاه در ادامه فصل باید باشه. پس از درخشش این بازیکن در بازی امروز و احتمالا ادامه تورنمنت آسیایی، اسم پوریا بیشتر سر زبون‌ها میفته و مدیریت رفتار و دقایق بازی کردن این ستاره جوان، جزو مهمترین…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140191" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/140190" target="_blank">📅 16:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140189" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
شکایت پرسپولیس از آسانی رد شد
✅
با اعلام کمیته انضباطی، شکایت پرسپولیس از استقلال بابت حضور یاسر آسانی در داربی رد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140188" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140187" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140186" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140185" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140184" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
اورونوف به همراه برادرش که چند روزی کنارش بود، دیروز ایران رو ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140183" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140182" target="_blank">📅 11:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
✅
علی قلی زاده: من از ته قلبم پرسپولیسی هستم و دوست دارم برای این تیم بازی کنم
❌
❌
اینکه به جام ملت‌های آسیا برسم یا نه بستگی به شرایط ریکاوری زانو دارد/ حضور من در جام ملت‌های آسیا نشدنی نیست و باید منتظر باشم
❌
❌
فعلا فقط دو ماه از مصدومیتم گذشته.خدا را…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140181" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140180" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140179" target="_blank">📅 11:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140178" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ9utubfO9Vbw4PTk_iFLja-jVRWnqQtx1B2XS8axVKYSGBoCxrGy02toJ1e_p0LFXjeKQbeOTy1NsDM4h496VJVZQy8Ajcw_hrKUY_8bmuihTtLUDmMg3n4_K3eMI49Bx56TVXwMWe8UHgmWk806O7EAn3cwexbo9S2WCicM9oWi1pf_vwDBQ0hg74iub77Re1_cjAaS4BIcsZA9YmSTcxkDv3TVSYQ3RGCq_mrPxWKWf1aM_KeWabR44XpMwnCPfFSqZo214a1tlJklXV3Oad3LN873wruksmeYNonI18R_PKvBDP0e-OAYXeX3JW0RaCNpzgR4eJoFhwHKP_KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Juventus -
⚫️
Nijmegen
⏰
Tonight 22:30
🏟
Allianz Stadium
🟠
یوونتوس بعد از شکست پرگل مقابل ساسولو، در شروع اروپایی به دنبال بازگشت به مسیر برد است و فشار بیشتری روی خط حمله خواهد داشت. نایمخن با فوتبال تهاجمی و پرس مداوم وارد بازی می‌شود؛ بنابراین یووه در کنار مالکیت، باید مراقب فضاهای پشت خط میانی باشد. با توجه به شرایط دو تیم، انتظار می‌رود یوونتوس بازی را کنترل کند اما نایمخن می‌تواند در انتقال‌ها دردسرساز شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140177" target="_blank">📅 11:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140176" target="_blank">📅 09:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140175" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140174" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxvFZUFjy-dErWH1x1GzCApFHVlQUV1H4WHEfqSMm8S_brnKkI2vJReo0AoRKKLj_nHcUB5_U-naSnHV_LE8QLxxML3F9Q51QEQebsjkfInOdX4NrA77Zs_JIv4YuYc9hgKrzwHw8uugfolOwj2PqZOGwVi62T5K83nuPOTA6ZzBuFKM5-Xx5bmVnwmY3UbYhYQqo6n8AUBv6kqk_SE7OxCZV9JmAX3HPqdZ0gaV0P-IcT74iRVwArdMAyb3lmpEZYBXaTdHPuNDVxdlDVw9LgsWbJMALZGt-CbBxBWGX1O2hSMx6ehEtRBwQD2LTFxYDLFb7ZXSjY4M6AvwQiVMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140173" target="_blank">📅 08:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8euJ_xJrwbFORDE2t7yDk1xYbq2tE0LraDH96ObpdKgOGdhdOLWvLk3Akaw5xfMr4lkcTVOEWaofF_ypq3ApFMPjyX4M9j_lw4YQhmXno5rwK5J4ixkid24fSz_vF7zc13RPNDV2xufesytxSXio9i5xbhlaNOk8S1eJqhXb-16VCnZOxzkqg0i6SqTZOMf7dGe_hb7VT_lIZQp3GV0x-WSRob6LoCblJAyVPrV-p-0Mbn4aBU6yuJeJHXu09ZZ5GwasHb9OwUdZ3MvxdMocZZZm4gr97aV4ZZuSzKQEPPIq3LAhd35puq_m397XDoTdxhDtUhbu3Zza7sjvAa2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140172" target="_blank">📅 08:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140171" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140170" target="_blank">📅 22:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140169" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
❌
مدیریت پرسپولیس در حال انجام کارهای تمدید قرارداد ۲ساله سید پیام نیازمند، است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140168" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140167" target="_blank">📅 22:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
👤
مدیرعامل فجر:
📍
انتقال علی بیرو به تیم ما قطعی شد
❌
چون پنجره نقل و انتقالاتی بستس تا نیم فصل باید بشینه سکو
😃
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140166" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkUDqtg0HhljxEX0HaIXAUax2paV3C1nSVw8OpGDV4MqC8K-Th-AgDMyp3r6Yb_bqijMitSoiHexwdIITXXfgxg1kKHkiYiME3_AaRRQYII1KETtvJntYoPJ3ias1R17wCn0aXm5o65vLPF9hiBV1k-yXdJISS0vzeqrus5g_TgKGpRwnrbCapgqZ0NxDAfHrmAD4PG2nGkslmR45i2gOuV9zrtE9-eTu7mj_T8FRTev6O2w4n0TEEXVHUF_PcNCmxcI88xK6RyaFhDz2TZFrlLNf6jjfon1lu2pI6tI9XVU6FGHwAzsgC-IXZvQm0dCiowIjU2PfcUnmH_1GSDy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140165" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
❌
باشگاه پرسپولیس کارهای تمدید قرارداد ستارگان خود را آغاز کرده و امیدوار است بتواند آنها را حفظ کند/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140164" target="_blank">📅 20:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
مدیرعامل باشگاه فجر سپاسی؛ انتقال علیرضا بیرانوند دروازه‌بان تیم تراکتور به فجر سپاسی قطعی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140163" target="_blank">📅 20:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gdx8UF9WvRMf6RGQ653pCEcp0p4CQxc-mlmLK-I-KP5781EKl-Ji7gIYqokOOTqmrvb1w6S3rWhlauN0TqzYOim-toR9Lo9xtRx9L-91ISAXdSsbG2ryEt3lA2o6udovCjovdU24uHInBDhW_yaFaCN5u5hYC1jgWWXZ_1aJ7nfW8IxYjrg_akIbERTjsL1_NeZo2VzYOJ8EjK36RDF_zW3aVlW-_5SQvHP_GaDVl7rBrZ_Pn48E8oaUhWWeR7A25CXoGmYqT1Qpzn45pcdBgpsfRp8HHalFalYl3pRns2amKkFfTq-r-Xh0Iqhc7gQxvovxa_rzTB4DTKNguLPCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سن‌سیرو امشب شاهد تقابل دو تیم بزرگ اروپایی است؛ میلان و بنفیکا در دیداری که می‌تواند از همان دقایق اول با فشار و درگیری زیادی دنبال شود.
[
🔴
AC Milan
Vs
🔴
Benfica
]
⚽️
میلان روی بازی در عرض و نفوذ از کناره‌ها حساب می‌کند و بنفیکا هم با جابه‌جایی سریع بازیکنانش می‌تواند فضاهایی میان خطوط پیدا کند. اگر پرتغالی‌ها بتوانند از پرس میلان عبور کنند، ضدحملاتشان می‌تواند جدی باشد؛ در طرف مقابل، حفظ توپ و صبر در ساخت حمله برای روسونری اهمیت زیادی خواهد داشت.
🟢
امشب چه کسی برنده این نبرد اروپایی خواهد بود؟
📌
میلان و بنفیکا را با وینکوبت دنبال کنید؛ همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140162" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140161" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
النصر هم به طور عجیبی سه گل خورده از العین ..خدا به داد کیسه برسه با این العین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140160" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140159" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140158" target="_blank">📅 18:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140156">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
رسانه های عراقی: بشار رسن دنبال اینه برگرده به پرسپولیس
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140156" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140155">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140155" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140154">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140154" target="_blank">📅 18:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140153" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
شنیده ها: تراکتور نیم‌ فصل برای جذب حسین ابرقویی وارد میشه!
✔️
✔️
گفته میشه تراکتوری‌ها ابرقویی رو زیر نظر دارن و احتمال اقدام برای جذبش در نیم‌فصل وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140152" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
❌
حسین ابرقویی مدافع میانی29ساله پرسپولیس چند پیشنهاد لیگ برتری دریافت کرده و قصد داره توافقی از جمع شاگردان مهدی تارتار جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140151" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyX705MWvBcgGh031h9MOnNh8yEoNdGiTeWl_uvWj7tjCGohV2TEnj7Fs0niLG6KFcyfHI3u29RKXd1DPsH9da-Zx9L87MqPKcTHUzbcBqU9wZV0zefK2og8llh6BM9PB50DhmeK5RJ-jvrwABfOozTOmcmPhG_uJEqDPwtfInN0cBBkomBXmWQPy9POIaSOEAe9vCkRY7Bac7SSRrhhvx9CgmKrwX2io16WRUN82z0Gf6j7rc2WlfLFa33CUdJZC4OAQzkeS6ZlZ7-iimNr3FXrRisXMdAroL_V2KnE7vR8B5sPnGatyJ2AeYPocM8qvX_ojAZ--fGa40UsxzurOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❤️
ایشون بعد از اردو ترکیه که مصدوم شد حتی تو یک تمرین تیم شرکت نکرده و حتی نمیدونیم مصدومیت‌ش دقیقا چی هست و داره چی کار می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140150" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkxG8KumBWAVmkZG81GUIcW2DQuq2j6YajO9s4z8M1mpkog7IBZDi_ng9BOKvIpKhhF92lPf0vVcKPVyzFQMkqmyey3JxcpF5UyoIwiclAziBYs36-bHu2YEM3uni40ot1A6XrqXy2yQHksWtCgWJxwWcsGZHjOFBVYz4q5HLK7YsNZetE3ys8IFP-XKVRjfQB_BGSwNAfLoI6DR7ER_G2IcweFSGgrsFyUHmMmS1xXVJj7VlOKSGL_n80NjONvClx8oOJBS-Hsq06ehEswsdT3JrIDP6ICEeAI5cj6tCAO9mdqRobDoXpXIh2IDegtJT4MJkuEBYq3b2m3xoBPHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته میشود باشگاه پرسپولیس دیگر برنامه‌ای برای خرید امتیاز تیم لیگ یکی ندارد و به دنبال خرید تیم لیگ دویی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140149" target="_blank">📅 14:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140148" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdXvOq34kdvOwtCowmizuUkmewhiPV6vSdlfUCljb25vvjKWJpnYhlQLS8TseKg488_8nDCnkumSmNtISyOwHyQdA3ZDiOYK6CoZoZa7y_hQ85qnNZfK_iNU2A0DMemx0bDLzJ_evyV-TTT3g9b5rvz7Wuvw4kmS6TFr99OB3Z8YvLF2XWK9-qE4VFQ8FYwx5SGedIBwbU09auZR-8Whb4eRAVgAgmT_FFWnzdg7KLytsEqPcZ4-VdUHAZqiBpvu3tKojvh4rNv-ck1OsflL5veUJeC8rV2L8x82DjMCLNg5TXZdAgeII-3xjDzO_Jidq7cqBfOmovkYRJGaQD_8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimrK9U0LWXWYC0LGOPvw-LqkyPvWtXvOnfAMHfypAKhtcgqUnl_y5NI-jMBlOcVOZDgRtvWcLrUf3oz6J_3mOiYh7SuEKOZwBbPO4vOrw_TgJSaqcQ47IMk_h8SyepP9BvnfNsFDNDOxqXulYIrJHfsU-iL31g3bof_aI-H9TbFV5fzI9RC4X_fRjJlIARh0DoFOsTRyP26X7PrRQWg2lGXd7ChVIVCOe8g9UoJSkanUQl1Mu8q5RIavT3GCCBcBp1DhdUi59_zimNLrxpujq3HGFXWuW0bZ1v7b1o1LjEZEPqVdOwAxMYc65hGcZQ_zScgO8qlTASIzLJQsSd09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHVO1L2dmus793pDVvMIFg3Gipf0lnN8v5qdzlqPbVaXver6qISlaeXn1tRGH01KdTe5N8oAk-aXWM9UfSGtha9r2LbiygYCBnTJ-mFoPyFdvqwZMcl3QrqBIqdkP-YyoRmk99JwNWD_o76jtPlfx90QCQ-m_OfSdSdNwEPYA5hBxkSqm2C1_ROySpz182BsMF2ZD7NuO04s_psHvvMjAd_7ztnczh_AfUela-AjxzvUHChxUTx9obYcdyWr7JDlGM-cwXOchbVRDvz6sz0uYbQ_CEz20Ps-64iOS08c3deQ36sAMH5xxW1qTGzJ47o0CqM1cWEM3sPPKa2OUOEpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=vCYL4WJe4AhjABTF7eqgsuPHcfSmxiHEh1MqJBeTTbjPafMmvSyBS8-aGR2a0R6wXHw_e9wuFCDUhxGv8DP3Ex9V3lVpV2EsLBHqUPQoN8ARqoK0a6tdZubB9BtYDxO2rL6KAyqJ11KZiaDoiyUfRG6q7_5YZUjaYrlPvq6IWtH7qNsYZRUDUYTkcJhFYvIP3BpJf7MxiFy9PZ4ZktgL15lndN8Ugxoy1EZ_xxUBsfvZbOksxZkqHwcHsXB2LB03si5mZgw2jeKy3csJ85SZNBPMbaTDB_iP5bW4nfss16Jafln__7aRY9L2gFo7FrTTMpYjKa7NoaZbut6oiv4cNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=vCYL4WJe4AhjABTF7eqgsuPHcfSmxiHEh1MqJBeTTbjPafMmvSyBS8-aGR2a0R6wXHw_e9wuFCDUhxGv8DP3Ex9V3lVpV2EsLBHqUPQoN8ARqoK0a6tdZubB9BtYDxO2rL6KAyqJ11KZiaDoiyUfRG6q7_5YZUjaYrlPvq6IWtH7qNsYZRUDUYTkcJhFYvIP3BpJf7MxiFy9PZ4ZktgL15lndN8Ugxoy1EZ_xxUBsfvZbOksxZkqHwcHsXB2LB03si5mZgw2jeKy3csJ85SZNBPMbaTDB_iP5bW4nfss16Jafln__7aRY9L2gFo7FrTTMpYjKa7NoaZbut6oiv4cNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=RjE9J2QzuecpxAmRdRAUPCBtuB9pA6HQmzznlaWjbocS5gHYD602XZ62IimNEtswzE4-ltKCLzvhGWBVHLHy7UKJaLvwe_OG-LMJR2GWnGoXpvyVvFeRWHD-2dB_vFNHIrpBsWb0IYbEjauBTSfO1_SKAORhJczgsk6OUd5GJNw6lGCKo3sFBPgeWJU2_N8hVjqrmSVJZNbtutg22-PSksb39FVJgyESy2vQ_0ZeoHQSDlmzPvzxHdit8NnirOm5YYxu240ZZ5sXgJ8QMu30HFiWU28htuR2DIp2IBGMMiORPdiGMOKuYZCXDWH6cVDHeAGcwd98kOZUVKwxw9xdqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=RjE9J2QzuecpxAmRdRAUPCBtuB9pA6HQmzznlaWjbocS5gHYD602XZ62IimNEtswzE4-ltKCLzvhGWBVHLHy7UKJaLvwe_OG-LMJR2GWnGoXpvyVvFeRWHD-2dB_vFNHIrpBsWb0IYbEjauBTSfO1_SKAORhJczgsk6OUd5GJNw6lGCKo3sFBPgeWJU2_N8hVjqrmSVJZNbtutg22-PSksb39FVJgyESy2vQ_0ZeoHQSDlmzPvzxHdit8NnirOm5YYxu240ZZ5sXgJ8QMu30HFiWU28htuR2DIp2IBGMMiORPdiGMOKuYZCXDWH6cVDHeAGcwd98kOZUVKwxw9xdqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=bf_TJ53WRMOT4MfsYNAOR9q6cJmnajZEG52tT3KM-1OM-KUklef-TO2gPGbPRp9smQLTqNyAiILlvG7Te7JVX1hFZm7_mmhFQGm8D_BTcjaXIkl8-7N6-YlHFnJqz87e35Zfrwk4s_vArHjwWxBCDCaH4hqkjdRYF45xcYzq25K39XyJsx3kmCdn7H_rrm7iLzwcS66enb8OAbrY1tg_4AixeDoi1YqiGcfAELsTjpJLdje2-VEh83SO_0jDc2TwC4Cp3W-rppSrESrTdEHp2wNJTKHh-BhjMNRFoPllmx4REYsyhY2ScFj-a8CY9Cg9mMue-xcrbU2t7nfPouBA1JTJf0kqRHl0JG4tm436C0b4W-S3wA70znyE4o45s_7pT_mIck3clR-jzwyENXqohni_9UMa2aHLmVivxCPI145SnC0Es8jYoYZ3kexcxvTAWIKVWih283ZXoZAuKjkLBOiZeGNfNr1EmZaHEbit6RF3j9ukHEqJdeuW2WSrRdSFUAHfEhVk9FWm4nuJwK_AhdQw5WJ1N_EjHHAIZA62GVCkh1WQlwRYl4pO7hCWHSCGZElnjpXVHEIXsXTI_LvPx36Uf5J9LEx52gVWutHIwYLBE4xRaejVTwLxTtK3Zb9DlxJzCDigPoUvZJ0RMe9_v_gwVej-Xab0eoLHBRQ9My8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=bf_TJ53WRMOT4MfsYNAOR9q6cJmnajZEG52tT3KM-1OM-KUklef-TO2gPGbPRp9smQLTqNyAiILlvG7Te7JVX1hFZm7_mmhFQGm8D_BTcjaXIkl8-7N6-YlHFnJqz87e35Zfrwk4s_vArHjwWxBCDCaH4hqkjdRYF45xcYzq25K39XyJsx3kmCdn7H_rrm7iLzwcS66enb8OAbrY1tg_4AixeDoi1YqiGcfAELsTjpJLdje2-VEh83SO_0jDc2TwC4Cp3W-rppSrESrTdEHp2wNJTKHh-BhjMNRFoPllmx4REYsyhY2ScFj-a8CY9Cg9mMue-xcrbU2t7nfPouBA1JTJf0kqRHl0JG4tm436C0b4W-S3wA70znyE4o45s_7pT_mIck3clR-jzwyENXqohni_9UMa2aHLmVivxCPI145SnC0Es8jYoYZ3kexcxvTAWIKVWih283ZXoZAuKjkLBOiZeGNfNr1EmZaHEbit6RF3j9ukHEqJdeuW2WSrRdSFUAHfEhVk9FWm4nuJwK_AhdQw5WJ1N_EjHHAIZA62GVCkh1WQlwRYl4pO7hCWHSCGZElnjpXVHEIXsXTI_LvPx36Uf5J9LEx52gVWutHIwYLBE4xRaejVTwLxTtK3Zb9DlxJzCDigPoUvZJ0RMe9_v_gwVej-Xab0eoLHBRQ9My8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0uNaOnY-32G3CellajVxj_kgoJzEC61HjzUOq06guqSJmlBy9TcncTVb54_cS1fDLOnl2gEwS_rUbVQXWwtwq2s6Q8dPUljmU0W5kiXHUe9ElfpoVkETtkevprdM2SuNvailOWftjvJiswyDIFrCl7qIww5rU8KzJH9Rjxdt9qtt7p7roguO6ctKusZxgwz8bqZW5nhbxxLfF0rZKazjKh77PZMSUfTPmCpBtOwEBq-XsURdgDnfiWHGxLuCVNwlg6dhJAqixI-WS2-Ze8Sw-fIGsKlRZqUcSCSzzCE7EXcguu5qivW-jAR-5rEt_bXJsMs3bIj5bfvfh3r_Ma0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t24fOCaB-3DHG_HX9LasiwlTFT28SyDCuCQVSPb1KAGM3-V8yXpZG9C819obHXWFpSl6i7bXmOXp5CFmxAzeguKtQTAhyn01pscYWDSnNpbD8JH69yQo_3Srx4ZIbj80qlBgMtLrvIc54sRZnM7qFmm_S0zfgTtWHRVhnLTJAJ7-NApzi2Wwt-OioGT-aI9Ppxwzs7KqWZsflqwjkJqdOZitWPf7rmqW6pT8yn3YqONb7Xs28zlEjEcMmzmICK8Fd4u8_cnUZTB4NX1GUDlcIq_RtrIuihS9Y3o_EIOWmnYCmnWhGpSFzOK2eufdhHIjMrGVIOFoqrGSck_pAJm_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwIqHhaXt7lzrDqjfaSX0DdxdCh6bE_r7FQJ9pJ5fWcMopQ_jy25o0aK8nBLsK41HXUY7PR4PVYcvxMXo25hZxATtifq8oqsevYVXzJXFfgi3Qf1Kqm_RSUSfWTLsIh7246f6ZSK2dgSKef5JSGsqPGyjLqGWOzRekOt_-apKGnK0tCQbpkw7BXanDWjYjF38Csn6g_HGIyZQslq1Rs8qhRSy_Lv9J_QMrD_Zt_BLsAYSIkqq7C6c3fqOPY5lJN0ldssxXd3KufrJTi62ckehB4FwRBatFFvB4El-dklSQqsUFaCJxQSV7CuWuqsUNbDclswZ3GJ1ny-FZxN_TmaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7D3JiQrbpU3hSLser_qXFjUDcTdP2Ra6UW4PvWECnCYw15daS5p34K91y2fX-nVmNajICTQ0bWtQhnING7V9DDZzJYCNzq_IKDMwnbuF61amhP8cvg0Xs5rzVS9doKWJPN7pPkQftPI0_nmKFOtkYXLRDWQ_GwFDjsbkG2HuePVpEql69dyFGyx1xD053tJpUdDrsrBFn6WZd4SnWUX7lGgk8R0GfOLk1rJvq7fdPMhk1Ahqqx8zXUWqwPUvL52Rrm9eCKuyo51NXsk7RE4cJs9glRLYtjQn1WQk_-Zvkm3erydPobNuUToc_MWowjQtO215yie8Heuml34AJE0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=ib5YQUoRl_FEVgHhQWaLxnZYi9upyzbDyBXehpdI0n9j3ZparbYQvuYTXhZbNzPUPCSU7vFDsTGVHYk4izqlpxhxqW2VndA5hIwz05-3kpm3nlHkIrv-Nvjvu5hJc1Yq01EPefmsCCyVnZ9DyP4eiskM2VLweEw_PVpgv6iGtoCNysWFDI6uHuGbtGChuTYCUtGl_GePsuX7CQCN_Zit7KnJsetHTx-P89ZT2RRKlSwwC26p5Jg_iqWc0k-W6jMa077zQ47H-FFk6EkiCLtlmeTaL_5PGVAuSynXRMzWxWFDYSNxPgmyDjKWdB17flj8-HCLRRKqJ9NhM9ep2v7tdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=ib5YQUoRl_FEVgHhQWaLxnZYi9upyzbDyBXehpdI0n9j3ZparbYQvuYTXhZbNzPUPCSU7vFDsTGVHYk4izqlpxhxqW2VndA5hIwz05-3kpm3nlHkIrv-Nvjvu5hJc1Yq01EPefmsCCyVnZ9DyP4eiskM2VLweEw_PVpgv6iGtoCNysWFDI6uHuGbtGChuTYCUtGl_GePsuX7CQCN_Zit7KnJsetHTx-P89ZT2RRKlSwwC26p5Jg_iqWc0k-W6jMa077zQ47H-FFk6EkiCLtlmeTaL_5PGVAuSynXRMzWxWFDYSNxPgmyDjKWdB17flj8-HCLRRKqJ9NhM9ep2v7tdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=j-BM2pW8NxzedTFethjYFVuufXL48NhjlagLr9FCZ9-xMp-23FwaTq2WoHtBktRVTEWq0_v0VV5iMwwZcaWFFCRSmpx2ET5jnGJrtJF6ywTvE48MtOmJFJskfuKBh2zrpMCRocGF7OmsBUlGgHvT-EPctY0gmUqZELcxQLkIjVpSrpI02u1NwEDDUQygahJ6D0BKyyl1EV9Es2ax7YOWzIClLB8HinM9HEdOTbyKKqh85JNBz3cKo-mJ2BCnbiUJ9gZ6PhvGVwFxsVn1P0DsRXmi2rUPjtGVcwohEC7-wOusUb9XcXa6e4jzmYZAMzO39-xtUpWEg4PNFt8gZgPhUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=j-BM2pW8NxzedTFethjYFVuufXL48NhjlagLr9FCZ9-xMp-23FwaTq2WoHtBktRVTEWq0_v0VV5iMwwZcaWFFCRSmpx2ET5jnGJrtJF6ywTvE48MtOmJFJskfuKBh2zrpMCRocGF7OmsBUlGgHvT-EPctY0gmUqZELcxQLkIjVpSrpI02u1NwEDDUQygahJ6D0BKyyl1EV9Es2ax7YOWzIClLB8HinM9HEdOTbyKKqh85JNBz3cKo-mJ2BCnbiUJ9gZ6PhvGVwFxsVn1P0DsRXmi2rUPjtGVcwohEC7-wOusUb9XcXa6e4jzmYZAMzO39-xtUpWEg4PNFt8gZgPhUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=bDdbqheSrsPzrSCj4ZZyWpX9K_lXoLTpI5Cc63_9be5SwxHg720--miWJNzdk_Lywg8WvivtoOKX_-wDlZOOjib5Dw-xL7nG-8yNCGGFyaSEYzXqvavn-k7AGDLyhNXWHJ6S6iPbKEfa1wnYGnBsCG1shbfco3CtZq2bEfXP3jE_Fw0Xg8-taupb-F95ilpKbk3cZvKfFub3jxgvUXDYscKfOYhROS6slqgS6Z-YeeJId7HHAWdFrT3os13ugsf0AbaUhWXu2LsjTeueRtu_J6KRII9qu4zJb2ll-fGK2n9s11O52OaSxmOelik3degs662PqLn7gElPVXbKFPJtrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=bDdbqheSrsPzrSCj4ZZyWpX9K_lXoLTpI5Cc63_9be5SwxHg720--miWJNzdk_Lywg8WvivtoOKX_-wDlZOOjib5Dw-xL7nG-8yNCGGFyaSEYzXqvavn-k7AGDLyhNXWHJ6S6iPbKEfa1wnYGnBsCG1shbfco3CtZq2bEfXP3jE_Fw0Xg8-taupb-F95ilpKbk3cZvKfFub3jxgvUXDYscKfOYhROS6slqgS6Z-YeeJId7HHAWdFrT3os13ugsf0AbaUhWXu2LsjTeueRtu_J6KRII9qu4zJb2ll-fGK2n9s11O52OaSxmOelik3degs662PqLn7gElPVXbKFPJtrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=NG9jsyBGCnSaGc9Ayfelq3ahA4hqTCBLYeUJzA1D_JyWnMscPmUNrSyJk25cc4FUSB20CoCcc09naRtMdPhpA_-PcnN6nowgOf2VkCBEiKr_gTeCXS_Sius-iKn_g6GXnmuNYGj3TtE4KI5gHmPpY2WtiAWzR21_-ns98JTMyJ0umzR7T2OXW-EENvwi2D50pctIKXUOUg8I8kMGs4kVHXI_Nwf7cBpp6_988DdmvuF6j7PTFTQJiK7bBY4L3ss-PpGXyvZc4lyeehoFbVdd-kDjGeofcp8z82QsfSppdRkaIpNuo761eqzWPCCfj2FbDlnkLGovXVvFxX1sDEL9Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=NG9jsyBGCnSaGc9Ayfelq3ahA4hqTCBLYeUJzA1D_JyWnMscPmUNrSyJk25cc4FUSB20CoCcc09naRtMdPhpA_-PcnN6nowgOf2VkCBEiKr_gTeCXS_Sius-iKn_g6GXnmuNYGj3TtE4KI5gHmPpY2WtiAWzR21_-ns98JTMyJ0umzR7T2OXW-EENvwi2D50pctIKXUOUg8I8kMGs4kVHXI_Nwf7cBpp6_988DdmvuF6j7PTFTQJiK7bBY4L3ss-PpGXyvZc4lyeehoFbVdd-kDjGeofcp8z82QsfSppdRkaIpNuo761eqzWPCCfj2FbDlnkLGovXVvFxX1sDEL9Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=F3ZyKwMnXhn_yEHTDqeOGV_SVzBoz3OswfVDxSRPQDnfTPf-8uKN_bS9btfaq7HVG6q7BS7S5tOTZ52W7v0vs-6KCp6RedWaxMNUZW0ZVU7B8hrzt59Bc_wLsKm_hV3D_H8Zq_tGhPt42Uy81ktpd7WJHIMvxrYX_QVu6GH5YOlTe_jatRY09AfO-WysGddxtQV5EjTzZ7UBAVwx_T9IIgLmUmvCCA64ks7NlL99BxEwkMcpFSZIyD_wq_SgaomBSwgTvKGheEVbyiYHQGTb5QLQPNYlmm6Sda2vOiw91zSEUIwzoKFVHzutLMVADps9E6lKd7NFG1UqwjhjiaZRSXSyIAxZwilNZhNpJBNyJxKwqIyfIdy70uEaeECUVcnbezt5N8XvrBibHPUb7Dl-MOUSRWruvkG9RRKQ42IxQldLXlTv-Ye0xnK4KCywTOVJvhVcdKhUuLyeWea7lhkrnHU2PpQMcoNz0fnG4a9rxfmpE9YLv-ZNuT-75Dd6ArS4RgRSsokvmzgihWoayK6l4_UglPOuvlVcYgNLOAtvyAb4kk7EucyA1IqoAKyg1dD1iasCFb_fjhbVDAlbR6S4BzSNnbP2r7UYRLxyBDqZRiRtIKqELDEx2KFx01KNIwa5rj3S9MrVImLCJisjinwYhLj4cPHrzOF3ADh9lQJJhpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=F3ZyKwMnXhn_yEHTDqeOGV_SVzBoz3OswfVDxSRPQDnfTPf-8uKN_bS9btfaq7HVG6q7BS7S5tOTZ52W7v0vs-6KCp6RedWaxMNUZW0ZVU7B8hrzt59Bc_wLsKm_hV3D_H8Zq_tGhPt42Uy81ktpd7WJHIMvxrYX_QVu6GH5YOlTe_jatRY09AfO-WysGddxtQV5EjTzZ7UBAVwx_T9IIgLmUmvCCA64ks7NlL99BxEwkMcpFSZIyD_wq_SgaomBSwgTvKGheEVbyiYHQGTb5QLQPNYlmm6Sda2vOiw91zSEUIwzoKFVHzutLMVADps9E6lKd7NFG1UqwjhjiaZRSXSyIAxZwilNZhNpJBNyJxKwqIyfIdy70uEaeECUVcnbezt5N8XvrBibHPUb7Dl-MOUSRWruvkG9RRKQ42IxQldLXlTv-Ye0xnK4KCywTOVJvhVcdKhUuLyeWea7lhkrnHU2PpQMcoNz0fnG4a9rxfmpE9YLv-ZNuT-75Dd6ArS4RgRSsokvmzgihWoayK6l4_UglPOuvlVcYgNLOAtvyAb4kk7EucyA1IqoAKyg1dD1iasCFb_fjhbVDAlbR6S4BzSNnbP2r7UYRLxyBDqZRiRtIKqELDEx2KFx01KNIwa5rj3S9MrVImLCJisjinwYhLj4cPHrzOF3ADh9lQJJhpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZpi2brhU3I2EEFoSqTsXkEB_T6gdVC4niWOmo2O-RgXu1etlFWQTbxBrwXhAY11RXFvV1WxKEIBos7raloADJYXedqtv0oeHIVXU4R43X8SqrXDLAd4D5hpS5T44zToBE799mR_VspWaIHy4oPHAt_1Rco0JxY0W2Fj_dFuoLwHny0TD3Z3vwTYdgQNi6f-eXCH7xdKgQACMhoj6MUXexklGdiLHMkIX8K_yRbFYuCU16ClhOAmjkKuUAI1quNrfQySpYOY8cGbn06SYK2YV_4yihQffc0unUOxhX-XyG68_LwwNhAfTiFsahwZpNfNgOK09nJby9_yLGwWGTLUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc0k7UkI746ZYyNl-R8BNF_dX_yoECUoHHc9TOyCNgfo_NjPx889z5vyLUZuBaBbqUehO6rm2ket437vCzSFKvdQS4SGbPDQmBpEiGeSYuipwl-yzpJf6yTMJcRFalOMJo2XA7AF-1MT1zaEz0ino9zBxnaipYHzt12nHWjXEhsyF-3U32Kd5xghPS3d7hxNX8CwjUheZ5R_BvhZ5w27rKtFl7VZhUUWiPmDhOfazztxNkUc4LJqyVV3_IEb1VUXiaRlsYTZuLh6Og4a_FXKANS7d8nNrLyTDaEoS4zfUi_-v8CJaXvvasUvymexjEKcVE2tOQQqdyh7pEuWOppa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9AG2eyQitrlOp0WHpnc7YboisaFX0Jtjy7jpuO0DcilQCpsK-9ZkyizC5xiQlFvQKaRjWAoPMI1BcjIh95fKCmkcHgXhWv1CSKYGuR47K_XNRFBV8pVIdxC-HJZN2LvHIY7d_qo_J7QRZvO1hPxJiGCw1CEMqz01cpttwFJejYH38GVmWmhd3bUq7F-X3Gp-UeqgHjUhvFlo7oGLS55uKSo498TCWAd479hyahX0l0q8lu-X0XCBWyrbCENNE0UoLTQFgfzrguhRqcHHt0xTxZhqqeSSYZKliQTr_iYTv-Kt0VIJJ2pvtb3E6Hmu7WvOhfY0MvhKYKQxnDIUUKXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa2_OufHtylycuiLtdWe4aP0P-TP7r3CFbT7kMJL2yW9C54RKqRYYUSOtdBsiIgRPxqFv48eYQuIUBs5ehRnu6oa4ju6QIcYr9l4zbI_GinFRlzV-g3z42r4NawLlt9uFh5ctE-cMDXCqXBaQrQ0eJTQHzqliYck72ZJVkz_Gi5L2PGjBI4oxe12q_aZDO7HKuz7p38NrGxdq5aXE_BawCxtR2Sn-3-SupmfjL4EXcBoHxSBdlPOHji9IghKd4Wk_D5uO3mKf3BkQeb0U0D-FANbgvj8WsMwfxxxqZ8SQz8nI4J5CfmeInTnvgrYe_YyEEUn4E6v9w18mcadm4mCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNPMvlYzHhZRYrlADp0ax9bEvqZChbuNGnWYhCTAibL3Zzfc_09SJ9EvBFZJ20q8Al_FEQrV-vPv-jJyJYNLBWAZAJFwbWr_SFan651kXeVJLdlfrpq5znEz-6pwW607G1zhhy_YMCAmMBcrdUrkwJfcxcPHoQ7S_ANSopyxWC6p8gfbdrq6HRAdUavF7tRUjOuIu6xQv4cRQJ6cwcLVP4m74QNMzeS6QfyHbhzbh8NWSrWnmobetJHDI8nMGzVMKn9EfCR9xArnRwapfUMcBfqhRVjoKnblhyqaEdHJlsRDfyZ8xNVTmYnune-0hIxuDDwwpEhtr9UulO3WOoG5OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=gF5KdtG5ovDKEhoQyiy92ZPw5i6IO9yFSP4SymtReuZuS9sdX7d9Q2fkF446N3n99Cs68PLMpwhdQtxBGPFElV1a9-aqeY1w4q89K7LhHMonsnhtOr329z6RoVbhO1OwlftkhqC5O8Aa3oGXSUIO3G5BUf1ZG52pXoJES2NZaDX7UjbMt2dckq-HThjuc2QFm1jIHOhOGVEUA-QXvRSsE1_ma8tG_wjum3qv2ouyDMLGaOlG12kOfdWpSuQFPRav7usLkC26i8Zxsl6RQZK1vR32eaDcR9q2wS62DNeVBZpFCJDX81OdBSXLHF22SWPr_ilEzKyI2Q4iwF7OIlvhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=gF5KdtG5ovDKEhoQyiy92ZPw5i6IO9yFSP4SymtReuZuS9sdX7d9Q2fkF446N3n99Cs68PLMpwhdQtxBGPFElV1a9-aqeY1w4q89K7LhHMonsnhtOr329z6RoVbhO1OwlftkhqC5O8Aa3oGXSUIO3G5BUf1ZG52pXoJES2NZaDX7UjbMt2dckq-HThjuc2QFm1jIHOhOGVEUA-QXvRSsE1_ma8tG_wjum3qv2ouyDMLGaOlG12kOfdWpSuQFPRav7usLkC26i8Zxsl6RQZK1vR32eaDcR9q2wS62DNeVBZpFCJDX81OdBSXLHF22SWPr_ilEzKyI2Q4iwF7OIlvhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
