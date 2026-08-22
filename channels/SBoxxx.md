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
<img src="https://cdn4.telesco.pe/file/eGbwzji4ecvrHl-kBLisQ_0ezKpfhXfnmRl8MSgweSojllJIYKyWv1XGT0I2pP_qZKJWKwRk6YzxbvDmsg6JilQ81Nb16P2fLYV7AXfzuPZ1ZFrpE3dpS2MnvwSpdT4QvGM17tCipWC1cAk5SvJMw7Zd4SN-Z0o8m8VrNw6Mm0AewiHCESxirk2Rwp7ooKSEFkfRJOKKG9cVTZkR2E06Vfa6_jBKB6Kfk9PGyHFJ65saWeSppeqkLgWM1Oi2bBmYvAXlL8LOxi1Vdi9sWsjS8NDpxF0wG8ILvv0VOdx-7dHHGjVpApq4U34k6nCGHNSHWeNm07aA9brqbEfF2LYx_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 04:12:49</div>
<hr>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:  آیا تا به حال کمونیست شاد دیده‌اید؟  آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.  ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 264 · <a href="https://t.me/SBoxxx/20093" target="_blank">📅 03:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
آیا تا به حال کمونیست شاد دیده‌اید؟
آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.
ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 317 · <a href="https://t.me/SBoxxx/20092" target="_blank">📅 03:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سفیر ایالات متحده در ترکیه، تام باراک:  اسرائیل هنوز جولان را در اشغال خود دارد، برخلاف قطعنامه‌های سازمان ملل، برخلاف کل نظم بین‌المللی که جولان را متعلق به سوریه می‌داند.</div>
<div class="tg-footer">👁️ 403 · <a href="https://t.me/SBoxxx/20091" target="_blank">📅 03:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 413 · <a href="https://t.me/SBoxxx/20090" target="_blank">📅 03:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 449 · <a href="https://t.me/SBoxxx/20089" target="_blank">📅 03:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانم با چه کسی در ایران مذاکره کنم. این واقعاً یکی از بزرگ‌ترین مشکلات من است.
هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد. می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور باشد؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور باشم.»</div>
<div class="tg-footer">👁️ 468 · <a href="https://t.me/SBoxxx/20088" target="_blank">📅 03:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارشگر: با توجه به اینکه ایران به سمت جنگ اقتصادی پیش می‌رود، آیا این بدان معناست که گزینه‌های نظامی برای ایالات متحده محدود شده است؟
ترامپ: خیر، اصلاً.</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/20087" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روسیه برای اولین بار در بیش از یک دهه، هیچ کشتی جنگی در مدیترانه ندارد، زیرا مسکو کشتی‌ها را برای محافظت از تانکرهای نفتی تحریم‌شده از دستگیری توسط ناتو منحرف کرده است.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/20086" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نماینده مجلس  ابراهیم عزیزی:
آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را درک نمی‌کنند، بنابراین نه تحریم‌ها را برمی‌دارند، نه منابع را آزاد می‌کنند و نه به دزدی دریایی در دریاها پایان می‌دهند.
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها به این اقدامات مجبور خواهند شد، بلکه منطقه را با عذرخواهی از ملت بزرگ ایران ترک خواهند کرد.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20085" target="_blank">📅 19:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">افزایش تنش ها میان اسرائیل  و ترکیه    دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.  دولت ترکیه درخواست صدور اعلان قرمز اینترپل را برای بنیامین نتانیاهو  به دلیل جرایم علیه فعالان ناوگان جهانی "صمود"، از جمله جنایات علیه بشریت و نسل‌کشی، صادر کرده است.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20084" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:  به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.  به نظر من، این بیشتر یک هشدار بود تا تلاشی برای…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20083" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:
به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.
به نظر من، این بیشتر یک هشدار بود تا تلاشی برای ایجاد تنش.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20082" target="_blank">📅 16:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اخبار تاییدنشده از حرکت انبوه نیروهای زرهی و توپخانه ترکیه به سمت سوریه</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20081" target="_blank">📅 16:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20080" target="_blank">📅 16:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دولت باغچلی، سیاستمدار ملی‌گرای ترکیه، نسبت به حمله هوایی اسرائیل به پایگاه هوایی در سوریه، هشدار شدیدی صادر کرد:  وقتی ملت ترکیه قیام می‌کند، هیچ نیرویی نمی‌تواند در برابر آن مقاومت کند.  ترکیه، کشوری نیست که در برابر حملات به حقوق حاکمیتی خود، منفعلانه عمل…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20079" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-text">🔥
نفت ایران در بازار چین کمیاب شد و تخفیف منفی!
🔹
رویترز: پیشنهادهای فروش نفت ایران به خریداران چینی کاهش و قیمت محموله‌ها افزایش یافته.
🔹
برخی محموله‌های ایران به‌جای تخفیف معمول، با قیمت بالاتر از شاخص برنت عرضه می‌شوند.
🔹
صادرات نفت ایران در ماه جاری به ۵۳۴ هزار بشکه کاهش یافته؛ در حالی که میانگین صادرات در سال گذشته ۱.۴ میلیون بشکه بوده.
🔹
همچنین ذخایر نفت ایران روی آب از ۱۰۵ به حدود ۸۰ میلیون بشکه کاهش یافته و پالایشگاه‌های مستقل چین برای تأمین خوراک به دنبال نفت جایگزین از کشورهایی مانند عراق و برزیل هستند.
@khate_energy</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20078" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH25n8OHJLWI9nBCUtLHRdl1TZfIvfi02zYr4JWX0ar2x8QXEfHkVNt1LxIiABOcmI7rNP7N3RbZYb_-gZJP8C8J8TYjMuK4tVyQDZEdwwNqxA4TkA_Zx5teT9hjs_uiMEpoTo4NhcqS4f1bfN-Sb77kjDJWm71UJ8YKryWde-fjhf2uKI5WunPbgB46sco6fIKEOLyPd9bejvZtkNfYuAY3fHu3X4M__WjvlLkwPDsQS3ftZ_FXkEV16vRagDavguLpUs8O2uwevnDbjElbiaeQZzuH4pJcVuAz-d0d1BDS-GCtskxFoSJI9Ql5_U7HD8Z81z4GCaDwQarZey0mKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20077" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McmSxAxLIOV4iU3tdTh2OYqO7AaLBBvrgTw1248I_xHBJ1ZhhHcv8Dh6xv4iy6lEH1bQVnJ5r5FwidF93j-WEm2NN16g1HXgjCwp9-1Sp-j5Qc3y3EufroaZknsNbZBH5Cao8aWNEsrI4dzFJP1bFEQwnBRsBDA1CYsSwgfqfgB3tRQo-_o_mCd7lp161XC_Y3FE2-wx3jWMd81GjeBYCdhy725r9XFTfd_YuguqnBueWvjcFwLBKpeqS9p3HFYS4nQPccaRJlW-diaUT8qw7mrr6W2AJeH413N4jnkDDoD43MNmKQAA2wCSe8qzgTzGoInUcM2vWcBZ2fP2h3nyPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20076" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">– طبق گزارش رویترز با استناد به داده‌های کپلر، تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند همچنان در محدوده تک‌رقمی است.
فقط ۷ کشتی در روز پنجشنبه از تنگه عبور کردند که ۴ کشتی وارد و ۳ کشتی خارج شدند. برخی از این کشتی‌ها از مسیر ایران استفاده کردند، از جمله یک کشتی بزرگ حمل گاز. هیچ کشتی بسیار بزرگ حمل نفت خام (VLCC) در هیچ‌جا دیده نشد.
ترافیک در تنگه بابرالمندب نیز کند شده است؛ به طوری که تنها ۲۳ کشتی در روز پنجشنبه عبور کردند، در حالی که این عدد در روزهای سه‌شنبه و چهارشنبه ۳۴ کشتی بود.
این در حالی است که ترامپ و اکسیوس ادعا کرده‌اند که روزانه ده‌ها میلیون بشکه نفت با هدایت ایالات متحده از تنگه عبور کرده و به بازارهای جهانی رسیده است.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20075" target="_blank">📅 09:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">- یک مقام ارشد ایرانی اظهار داشت که ایران در حال آماده شدن برای آسیب رساندن به ریاست جمهوری ترامپ از طریق جنگ اقتصادی است، با هدف اینکه او در انتخابات میان‌دوره‌ای نوامبر شکست بخورد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20074" target="_blank">📅 08:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20073" target="_blank">📅 01:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1CQtyg0UJnq7GQajqlQSMtOOjzJoe2BPliGW-eE07bW86urmqOZJaQFBSVs0CUf0_25xrwllDxe4CXsp6b9_wMYuE1Q15DOsPuloE6LKtJr9iXT3s9rTjzkHDOSTKnP5dckukDRtk4OODezUrvkrdcoep62SNjNpgTY5-QDEzyPpe4cGH7I8p_kkY_1CvWdz0bOQwXmLtM9MzSDSkT6IgJNygbnKGM4-E7iLJTs8bZQnoqqltPeyP2QW1e2I3fQIEATWjyaoAmeV--dZ-mBEB5Li-8CNDqxTi-qqcJ7si54CYCfc9tC7OIu57fxyKanqmcDXen55uetvXglF2IuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلن ایر دیپلمات سابق ارشد آمریکایی خطاب به ترامپ</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20072" target="_blank">📅 01:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اظهارات معاون رئیس‌جمهور، جِی. دی. ونس، درباره ایران:
ما اکنون در یک مرحله جدید قرار داریم که موثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آنها وارد کنیم.
این یک تعادل ظریف است، زیرا ما فشار اقتصادی بر آنها وارد می‌کنیم. آنها نیز تلاش خواهند کرد که فشار اقتصادی بر ما وارد کنند.
اما آنچه در چند هفته گذشته صادق بوده این است که آنها احساس فشار بسیار بیشتری نسبت به آنچه ما تجربه کرده‌ایم، داشته‌اند.
ما این روند را ادامه خواهیم داد، زیرا معتقدیم که این بهترین راه برای دستیابی نهایی به هدف مورد نظر است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20071" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20070" target="_blank">📅 23:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBMt7SR9AnX97Q7SF0SkXqe3imPZGMNHtbn1LYEnLAMdw7MpKhntmy8VwkmVFYOaxEhdh-S5k9kBilLOoGBmkfo1E7xaRSY2MLOigxc4kU37vMPcW-yZDzpYLYQOkRMmU9pdHZ3FY053sKRLtahfcy_Xrv_M5na1zryIqT4PbZQVC5yImMhud3DlqMPfR7V0VpZshxBc3Ft28n6kpZ-3XmubfsHYknnx2pQeGGkEzwiPSULRaglsPm0W6k83Waer5PtMQDQUh0EmNvDijlQSYFQ4iiO9KDEdYIK0bXZ80qgpns60kUvmlaDiugh7nhx6Tk93BZTD0M3JB49xzW_cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20069" target="_blank">📅 21:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایالات متحده آمریکا تحریم‌های جدیدی علیه حزب‌الله اعمال کرد و آن را مجدداً تحت یک قانون مربوط به تروریسم طبقه‌بندی کرد تا بر پیوندهای آن با نیروی قدس سپاه پاسداران انقلاب اسلامی ایران تأکید کند.
واشنگتن همچنین ۱۰ نفری را که متهم به قاچاق پول نقد برای حزب‌الله هستند، تحریم کرد.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20068" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20067" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20066" target="_blank">📅 20:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ضرغامی:   از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20065" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ضرغامی:
از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20063" target="_blank">📅 19:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20062" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که دو حمله پهپادی را علیه فرودگاه ابها و تأسیسات آرامکو در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20061" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">— مرکز فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که گروه ضربتی ناو هواپیمابر یواس‌اس جورج واشینگتن به خاورمیانه رسیده و اکنون در منطقه مسئولیت خود عملیات می‌کند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20060" target="_blank">📅 17:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20059" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL-F90ee9IZEc08smi70hzMuXRkLJZ55nPqzoyDeKy5FuCKLSWk6jK9YxDKkByFsHwwMAlFdrX6IdP-koa3wmb8YYhvlxX3D6Mx50YjYVsYWOcustldFP6V9kUXnnMIpdFYTMVLUa9oNTOReYEzN9euIyGeiR2OW1dU5DXEwCH3ldIUvrrqpag-8ryw9IRGSsdjO7P5aIkwFdmqGNL6RgWahhYdd2By7H0bnCIm5kLtcxCaW3q7gG01LdN3CTeYS3BSjti-ZPq0spXPfAU8MBnleGaRMRjvoncty5TIPnQYAG3CdxE4OeRq9q-TrsKpH9GKMy9Y3zX7ZyTO6gpOwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!  انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20058" target="_blank">📅 16:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اردوغان: «ترکیه در دامی که نتانیاهو برای سوریه چیده است، نمی‌افتد»</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20057" target="_blank">📅 15:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20056" target="_blank">📅 15:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.  انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20055" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv92sAWe1U3m049Eha6I7qAjx-spEO_TBlCTYFIpZdGSeClt-BuwEZP3IGCUFjAxOelVyXjxDfkXFZ2kCgYHx6I3Pr7ypPob5Sy2vTkST72f1-0cm3VNO-y87SZBXqFcBcsiXCMZ-voEAukLSxXADPfUlz6lSf9NUNGc7KzYj53T9Nu4fIrgqYXYx31A1IYBGXf9D4RBAzJL43DzNbg6-uDr_4Xn6e3hXJE9dqDbY5_r8B2j1alkw6ndBkhpPoBejuGnPccGC8Q2ZPDUQrefScsTNtkjjZ4ne1fKM-sgWhfdIL1GoGM4defOwjcjuN3fhOVOT80byDBG0sjVMgpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!
انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20054" target="_blank">📅 15:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بفرمایید:  ‏ فواد ایزدی: اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!  با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد. ‎</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20053" target="_blank">📅 14:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نه دارو داریم نه بنزین نه برق نه نت نه گاز با تورم 300 درصد و رشد اقتصادی منفی و ریاست جمهوری دکتر پزشکیان و 2 جنگ بزرگ در 1 سال اخیر با گرمای 50 درجه تابستان و سرمای 20 درجه زیر صفر زمستان اما دغدغه جوان ما این است که رامین رضاییان به آن دختره چی دایرکت داده!…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20052" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20051" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20050" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHbHG6_c5bOF1UMO0GBai7VVz3vbwoOepqS7WkY6WgDe-bME3XP0ajGelGCEwX3HVhM828m62n3LYK3WiROCdof16LEuEp-cFsZoO3LWJj-JSo9Js3q8jHje6BjbdjecKeFLrL80DAjX8j5LxwyFCrFZUjm2crgI6RmWbnRWIF-9hrKRfn8ynyrtovMHe8W0HyFTE7GMGy4-ACAripxP88dR80OvaizDjK4lJhLKYy465Ll6nAMwnul17Z-sAM1WwQtf2X7WpAxhli3Ud1Nq9qeEuAuZmeZ8aktfaJufUTUhClzCWyM9ozFywUChlf9T2qCZFoKWJX73xqYmwFmXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفت کش در خلیج عدن!
به نظر می رسد حوثی ها تصمیم دارند کشتی را بدزدند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20049" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگر آلمانی ها به جای ما در این میهن اهورایی می زیستند تا الان نسلشان افتاده بود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20048" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">طبق داده‌های دولتی، آلمان در این تابستان ۱۴۰۰۰ مورد مرگ ناشی از گرما را ثبت کرده است</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20047" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20046" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:  «ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.  ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20045" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نماینده مجلس ایران، ابراهیم رضایی:
بهترین پاسخ به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20044" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سخنگوی سپاه پاسداران انقلاب اسلامی:
قدرت تخریبی سر جنگی موشکهای مورد استفاده در موشک‌های جدید سپاه، بسیار بیشتر از سر جنگی هایی است که در جنگ‌های قبلی استفاده می‌شد.
اگر جنگی آغاز شود، سلاح‌های ما در تمام جنبه‌ها کاملاً با گذشته متفاوت خواهند بود.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20043" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDDkz-VuvRjSlAIo3jbAa6PF2eMFJKetYTuUJQXjYuwxQD7JP2ntoAIs9SHwzFu6SlcWHtWUjNvR66qhwQbuvwWs7caQIsXZ5m2wklrOCLtX6_8j2YlMr_dCaYn71ye4TSjwpD2zgSej0AZlKyuFXzn77mFWSv7wRjDgbfCrYNKCXZKSSjToVX8hoQbucmgz2qT81uCjX8N04Aj8wGo6LxQiH9K-boWrPcg5HOqjbhcsuASUPD4125vpgXSFOv10LvDa9tiDSSD4Y3TtDh5kGr4dDMkBcHtDbxOC-TO2So9sLMWlRjf_nbk8tbq23x-blAudKs5B5KlSe46jxa_XLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.
انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20042" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20041" target="_blank">📅 02:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20040" target="_blank">📅 02:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20039" target="_blank">📅 02:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20038" target="_blank">📅 02:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:
هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.
بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی آنها نابود شده، نیروی هوایی آنها نابود شده، کارخانه‌های نظامی آنها ویران شده، پول آنها بی‌ارزش شده و کشورشان در آستانه فروپاشی است.
علاوه بر این، من امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع حمایتی از ایران ارائه دهند، با عواقب شدید اقتصادی روبرو خواهد شد.
قاچاق نفت، خطوط مبادله، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی - همه اینها باید اکنون متوقف شوند. خودتان می‌دانید. این یک روز اقتصادی محوری خواهد بود و ما به همه متحدان خود نیاز داریم تا در کنار ایالات متحده بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها در آستانه فروپاشی هستند و این اقدامات تاریخی آنها را فلج می‌کند و توانایی آنها را برای گسترش ترور در سراسر جهان از بین می‌برد. ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع متشکرم.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20037" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: من خردکننده‌ترین عملیات اقتصادی علیه ایران را اعلام می‌کنم</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20036" target="_blank">📅 02:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=GbsqF9aRGGrtVca-8EEaiNr8hz9vGNJMupnQpwB6bX7H2QRHOVHhDnfGQx20RfWU7S_VUpthHXDh7US1iAX-PX3OHnKq_NbZACwIJQllyY_X_T8c8ciOd3K2Jx7pWgXQjhZu7Kc-Mp4mEPrfgv7WRr7CwUVlocabNxVWA6t-z1CxWOCK_LE_1Ja8agl0N5hukKrFlSytsXElflYB1rMG8hwJVyZTayA-EBsKcPYELemsHeylA4WVcnbuT1EHADzpY3RO8ikAXYCSSB8SWfFd0ZkfohxfftEvroNNHXxgihHS33Q0QT-beLE3sFIcV1LdEA5ZpatcHK0UJsAjigMAgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=GbsqF9aRGGrtVca-8EEaiNr8hz9vGNJMupnQpwB6bX7H2QRHOVHhDnfGQx20RfWU7S_VUpthHXDh7US1iAX-PX3OHnKq_NbZACwIJQllyY_X_T8c8ciOd3K2Jx7pWgXQjhZu7Kc-Mp4mEPrfgv7WRr7CwUVlocabNxVWA6t-z1CxWOCK_LE_1Ja8agl0N5hukKrFlSytsXElflYB1rMG8hwJVyZTayA-EBsKcPYELemsHeylA4WVcnbuT1EHADzpY3RO8ikAXYCSSB8SWfFd0ZkfohxfftEvroNNHXxgihHS33Q0QT-beLE3sFIcV1LdEA5ZpatcHK0UJsAjigMAgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حمله امشب به کیف این احتمالا موشک اسکندر نیست. این احتمالا موشک بالستیک سری KN کره شمالی است که با سرعت بیشتری روی هدف فرود می آید. مانور pull-up شاید کمتر باشد. اما باز هم زاویه نزدیک به عمودی و تیز را مشاهده میکنیم. سرجنگی هم مشخصا بسی سنگین است.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20034" target="_blank">📅 01:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروهای ایالات متحده به‌صورت پنهانی یک کریدور حمل‌ونقلی محافظت‌شده از طریق بخش جنوبی تنگه هرمز را گشوده‌اند که به ۱۵ تا ۲۰ کشتی تانکر اجازه می‌دهد هر شب از آن عبور کنند.  مسئولان می‌گویند این عملیات اکنون تقریباً ۱۰ میلیون بشکه نفت در روز را جابه‌جا می‌کند—که…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20033" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20032" target="_blank">📅 00:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:
«ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.
ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی انجام داده‌ایم تا مطمئن شویم که آنها این موضوع را بهتر درک می‌کنند.»</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20031" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نافتالی بنِت، نخست‌وزیر سابق اسرائیل:  ما ایالات متحده را از دست داده‌ایم. ما دنیا را از دست داده‌ایم.  ما در پایین‌ترین سطح ممکن از اعتبار بین‌المللی اسرائیل، از زمان تأسیس این کشور، قرار داریم.  باید روی این موضوع کار کنیم.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20030" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمد رضا نقدی، فرمانده بسیج:
ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
ما باید امنیت خود را حفظ کنیم. چه این امنیت از طریق دیپلماسی و چه از طریق جنگ به دست آید، ما باید آن را به دست آوریم. این نکته اساسی است.
نه دیپلماسی و نه جنگ، به خودی خود ارزشی ذاتی ندارند؛ هر دو ابزار و روش هستند. ما باید بازدارندگی خود را بازیابی کنیم.
چگونه بازدارندگی ما بازیابی می‌شود؟ با این کار که مشخص کنیم حمله به ایران هزینه‌ای دارد.
اگر آمریکا این هزینه را از طریق دیپلماسی بپردازد – اگر بیاید و به این درخواست‌هایی که سردار رضایی به تازگی به آنها اشاره کرد، عمل کند، از طریق دیپلماسی عمل کند، غرامت پرداخت کند و بپذیرد که در هر صورت، باید هزینه‌ای را بپردازد – آنگاه به سادگی باز نخواهد گشت و دوباره تلاش نخواهد کرد. این می‌تواند بازدارندگی ما را بازیابی کند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20029" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است   اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.  مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20028" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20027" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  ایران نباید سلاح هسته‌ای داشته باشد. شما می‌دانید چرا؟ چون آن‌ها از آن استفاده خواهند کرد.  ما اجازه نخواهیم داد که آن‌ها از آن استفاده کنند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20026" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟  ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20025" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟
ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20024" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1C5BUmsHRwRwthQG5hfkhfNvkP4KRNKKvqHISXonn3DXm3w7Rcqp9z36EeiOlsOiWi6JadDhmG5ZiuZc_lzH2wmY518-vz-5PJFsUXD2xt1wRX0IRBxCfo9D_NY0bDievLbkO0EG6f1UzTp5K7BoArUabTiQuXo1TAUHvLH5hEILQyU151JHeQRRTq6K7-TISyw-LvM39SKoUsXwrZydtUTBozRyVAdYSf3v7peAbtmw3LksNok4kicJDbNetjc77FRZNwpGNOqRcXQojxreLZNo0ibRtmkpKSmjxI0rWGoGjYlyF17StFTDPKx3KNvqKRJgI95rapeVw5BFgR_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درین بازار اگر سودیست با درویش خرسند است</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20023" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20022" target="_blank">📅 16:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش اسرائیل در جنگ شدیدی با حزب الله برای تسلط بر تپه های علی الطاهر است که به شهر راهبردی نبطیه اشراف کامل دارند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20021" target="_blank">📅 15:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20020" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20019" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.  هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20018" target="_blank">📅 15:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک جوری میگویند خویشتن داری کند انگار می‌تواند خویشتن نداری هم بکند  چیزی نمانده برای این وامانده های غارنشین حرامزاده تروریست</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20017" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:
اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.
هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال خواهند شد.
در دولت بعدی، ما این سیاست "مجازات" را به طور کامل اجرا خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20016" target="_blank">📅 15:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20015" target="_blank">📅 14:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEtVzySPaUi5W1_DO2Gmd2GIMPeKE4OGfxycmB8YDLhw-dsyX_hnrLDUzKD0M5P-zOsuRPECwzyTIs0IXhVwe0S64Ab7cvtKG2rbVOqdhr-4nT3ljZmGF6uwnpUAHMHknpETWQlbRBXbqL7LdkkVagUZF6bA4G4OPj-YhbhitFQraSax3SnXsLGgl4JsvExZ4M3ju_5Ok63KgS9PrddbrbqMlPtIO3AVWOZ90N812BqdGIdr__tRbkia3K37zEowD5rLCVSxBtH7pt-BhgxxbDycWxopI7AjJj7VqeLc8Suny07Lt4M83SJ-ULrATUinzOizOd1h_14TZ0sbPPaGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20014" target="_blank">📅 13:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNsx-HsKKVBfEOgjjOK9-kmZhO8_zoR8WTtNdo_4sJ97we4FFCbuM2M_6kXEXJsGlm9rbFANogoOUAIAUm2d3rqjv3Myw0t4fDqJA7KPkpLgFNfIhp-AGJv5Yc9q964A_TDJxKrsS0aK0K0NRXZ2p3lzO48YkIS89K5cwpglXhj0fLbNHRBhzGU5--cIMsCmOC4BC-vJ4aH1-w7p67ycYTwkwXa_l4eGdIh6eOOEcx7KkxPrYwFD9qv30qtTunnwgJqMytSakiDKeld0FkfsWWZbOeE1-Z-KXxMR26GLy08Nda9I75X6VVJ_4XJ8ExyWCaxhagCigKdYrPlIOJnhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20013" target="_blank">📅 13:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است
اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.
مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های حیاتی ایران می‌تواند جنگ را فراتر از خاورمیانه ببرد.
منبع: FT</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20012" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOby2o8Bd2h61yN55ehevuOjm-U1i2IH5wqqAXWlLRtM6eYDYFtAY3456KXj6DRxYkzYgqjYp599oqqwbi0LCFpbLIY21b75aVJvHS-ETVu6lYfVXifV6n6HC0QVPo7V34WdstPz-bTeK5hdWo4krg72CZyXmYI_B1g3zmRoqnmZiPW9_d1-6Q1hU-HZld6CsWwz00U0Z5RWj2Ln3QM9shhWUhGv0C0AIhdm35Zqhb55Je5FsflcksiriS9_3s0KmYy3N0MgcB1vH_qf3xpeCF4FbBzkwnsKVYQ4vrRzUjRn-SNKYBlxWFvtK6PVVZoVNbhHw-jdoPMVyrH1WMKajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج انتخابات داخلی حزب لیکود و چالش‌های پیش رو
در انتخابات داخلی حزب لیکود که روز دوشنبه برگزار شد،
الی کوهن
(وزیر انرژی) در رتبه اول قرار گرفت و پس از او
امیر اوحانا
(رئیس کنست)،
یاریو لوین
(وزیر دادگستری) و
میری رگف
(وزیر حمل‌ونقل) به عنوان برندگان اصلی شناخته شدند.
بنیامین نتانیاهو
از این نتایج ابراز رضایت کرد و اعلام کرد که حزب لیکود در انتخابات
۲۷ اکتبر ۲۰۲۶
به «پیروزی بزرگی» دست خواهد یافت.
گادی آیزنکوت
， رهبر حزب یاشار و رقیب اصلی نتانیاهو، لیست کنونی لیکود را
«لیست ۷ اکتبر»
نامید و آن را مسئول «بدترین فاجعه اسرائیل از زمان تاسیس» دانست. او در پستی در شبکه X، کاندیداهای لیکود را به تقسیم جامعه اسرائیل، عدم پذیرش مسئولیت و ترویج فرار از خدمت سربازی متهم کرد.
لیست تقریبا نهایی حزب لیکود شامل
۲۵ نفر
است که
۸ جایگاه رزرو شده
برای انتخاب‌های شخصی نتانیاهو در نظر گرفته شده است.
گیدئون ساعر
(وزیر خارجه)،
حایم کاتس
(رئیس کمیته مرکزی لیکود) و
اورن دبرونسکی
از جمله افرادی هستند که نتانیاهو آن‌ها را برای این جایگاه‌ها انتخاب کرده است. همچنین،
نیر بارکات
(وزیر اقتصاد) که در رتبه ۲۴ قرار دارد، ممکن است به جایگاهی پایین‌تر منتقل شود.
بر اساس نتایج،
زئو الکین
،
مای گلان
،
یدیت سیلمان
و
اوی دیختر
احتمالاً در انتخابات آینده کرسی خود را در کنست از دست خواهند داد. نظرسنجی‌ها نشان می‌دهد که حزب لیکود در انتخابات آینده بین
۲۲ تا ۲۴ کرسی
به دست خواهد آورد، در حالی که در حال حاضر
۳۲ کرسی
دارد.
مشارکت در انتخابات داخلی لیکود
۵۳.۵٪
بود که نسبت به انتخابات داخلی سال ۲۰۲۲ (۵۸٪) کاهش یافته است. این کاهش مشارکت و همچنین تغییرات در سیستم انتخابات داخلی، که به نتانیاهو اجازه می‌دهد
۸ کاندید
را در بین ۳۰ نفر اول لیست به صورت دستی انتخاب کند، باعث شده است که رقابت برای کرسی‌ها شدیدتر شود.
انتخابات داخلی لیکود نه تنها لیست کاندیداهای حزب را برای انتخابات سراسری تعیین می‌کند، بلکه نشان‌دهنده چالش‌های داخلی و رقابت‌های سیاسی در داخل حزب است. با نزدیک شدن به انتخابات، این لیست می‌تواند تأثیر زیادی بر سرنوشت سیاسی نتانیاهو و حزب لیکود داشته باشد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20011" target="_blank">📅 08:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:   دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20010" target="_blank">📅 02:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نشریه "اکسیوس" به نقل از مقامات آمریکایی:
دولت ترامپ از دولت سوریه خواسته بود که خویشتن‌داری کند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20009" target="_blank">📅 02:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USbkufe4YAVGdU8I2LnN7VIh150nQj3xzPoTPPw2fFxgLNK2TOdwiV1rZc2lMowqUBT6Cr-GoPavAgpTDUyF0GNs6wdj3FnsqphjTe_6debVBI9WVL9v-eCo02ssL6ogDm_2UMRTeW85mFxavB1XusGUDsPGVnaebh4qXEflsz-iGknSnNFS6iQDbliOuZPnGncObQFS1FgSUY2ZuEydKr1u-ESO581ILHG5IhkSgPXgkcu_Qy0MyfHA5YpfOXgotPvzLQm8xUifM4nzB-Vk21Pko4AEK3TGpCAW2jwy_sjmPT_g6eekfiYnFcSP2k_GAG_fSiflhllPpm5F5T92Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید فکر کنید ایشان امام جمعه خارطوم در سودان باشد اما نه این مرد همان روبرتو کارلوس است که به دین حنیف اسلام مشرف شده و با یک دختر مسلمان به نام سهیلا ازدواج کرده است.</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SBoxxx/20007" target="_blank">📅 00:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به مشاورین ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند!
دولت ترامپ در حال فاصله گرفتن از تلاش برای "فشار حداکثری فوری بر ایران" و حرکت به سمت یک تلاش بلندمدت برای "تحمیل فشار" بر تهران از طریق فشار اقتصادی و نظامی مداوم است.
به نظر می‌رسد هدف، افزایش تدریجی فشار بر ایران است تا زمانی که این کشور تمایل بیشتری برای پذیرش شرایط ترامپ پیدا کند.
منبع: CNN</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20006" target="_blank">📅 00:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97XGE8O931K5raN0A9gBtXcPWwKeWga2uMIql-Gzatr34tXVSJQLagyEIiwfPhKR1vogsu9tJJfH2cIoIME5TUw8Eqf4S1M9OCB0FpjFwAvSpWvd7zKolTQiwlio3uyLWcrrqi2vjT-k24DkABNceCDySBJIJwstImxxVhhYPZLLQIhohprwrtt1m9tCJ3qFgCBeXgDEbjzVvZ7DwiTqkq-QRElm6_vhoQmbW6Na29-RQ2nIEx5iOSjD_eqr-J_oixuqTmX-vhfuf5iSV97x_KaU7h8MUC86ztEQjhZUrwYl8rHsh_Ml5F8EnrAHlrA7M5tQX-1ASyVg6HUEd_dnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نتانیاهو:  اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.  اسرائیل بارها به سوریه هشدار داد که چنین استقراری…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20005" target="_blank">📅 00:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دفتر نتانیاهو:
اسرائیل و سوریه بر سر حفظ وضعیت موجود در مسائل امنیتی به توافق رسیدند، توافقی که سوریه در آستانه نقض آن بود، با اجازه دادن به نیروهای ترکیه ای برای استقرار در یک پایگاه هوایی نزدیک به حلب.
اسرائیل بارها به سوریه هشدار داد که چنین استقراری تهدیدی برای امنیت اسرائیل خواهد بود. سوریه این هشدارها را نادیده گرفت.
اسرائیل تهدیدهایی را که امنیت خود را به خطر می‌اندازند، نمی‌پذیرد و از بازگشت به وضعیت موجود استقبال خواهد کرد.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20004" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امارات متحده عربی، تمامی مبادلات تجاری با ایران را به حالت تعلیق درآورد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20003" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پروفسور خوش چشم:  باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20002" target="_blank">📅 23:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=O94mp05lbzQs13sn_LnjOUJWb0wGr0ldCd2T1dcZhKAgvpVFIZBrL7p62y_bGY4T0DdEpYDD150Pz5M251Y9vv0_YagnA6bwnQUHPATqzTjeh4_gEIalIYh4dnVuBs6HwwKsNTEyt8MsYmC-sHJZ4TMvZQE01zLoGjFapNtigw5I7ITr1xoo37hYNKcdVMaME66p235fUnPiTAwUkVq0bJP-tv8OGN9idouEJ1VOmoosf8OWJ7osxbWpxq1zc9Su42XyoFsrrqUr_uKfCX6AHueN9Xu_GXtRXryKkXS9ki4QGnjdaKXsznawZ_r3aCxroisqQVZT1cD0mDAeU28TYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e373b297.mp4?token=O94mp05lbzQs13sn_LnjOUJWb0wGr0ldCd2T1dcZhKAgvpVFIZBrL7p62y_bGY4T0DdEpYDD150Pz5M251Y9vv0_YagnA6bwnQUHPATqzTjeh4_gEIalIYh4dnVuBs6HwwKsNTEyt8MsYmC-sHJZ4TMvZQE01zLoGjFapNtigw5I7ITr1xoo37hYNKcdVMaME66p235fUnPiTAwUkVq0bJP-tv8OGN9idouEJ1VOmoosf8OWJ7osxbWpxq1zc9Su42XyoFsrrqUr_uKfCX6AHueN9Xu_GXtRXryKkXS9ki4QGnjdaKXsznawZ_r3aCxroisqQVZT1cD0mDAeU28TYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروفسور خوش چشم:
باید برویم آب های فلوریدا را مین گذاری کنیم ...</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20001" target="_blank">📅 22:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20000" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تاکر کارلسون می گوید که اعتقاد ندارد که انسان‌ها بمب اتمی را ساخته‌اند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19999" target="_blank">📅 21:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgnFov1kdQj1wCwZ5N0jALr_W8RTh1malljCwhTnfR59cVZ3FAQIA5A0-B_vyDs61aWuwgQXIi65B-du332F39nbF1BH4cJkamY4g7z5P8a6LMhNWfPdvFvFbjNuPQrTlmnMvT3Q0SU6ZPd7SPhPwgDMi3Vmq8eDBy97qhguuHi5wnvYPY8Ajsbn1s1qqHnjY5V5OHwLLS-WyOhA4eAaQO4D_MPM7TASmImT8UwTqIrw9vP1G2NwiIci6-9Q5DIkluA5aHbFn6LbSlmESe7jwXigbnNWeWidQ4KgHIaKLA5qMw5_brMMgenfUM4BVzOlzUtwVTLmNKN56EGxQM9u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دردناک!
تادالافیل ۷۰۶ درصد افزایش نرخ گرفت
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19998" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یکی رهگیری شده و دیگری در آب افتاده!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19997" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد  : وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19996" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت دفاع امارات در پلتفرم ایکس اعلام کرد
: وزارت دفاع امارات دو موشک بالستیک پرتاب‌شده از ایران را شناسایی کرده است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19995" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً بالایی قرار دارد و افت قیمت طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19994" target="_blank">📅 18:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گویا حمله به امارات کار انصارالله (حوثی ها) است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19993" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19992" target="_blank">📅 18:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات در بندر جبل علی امارات</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19991" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
