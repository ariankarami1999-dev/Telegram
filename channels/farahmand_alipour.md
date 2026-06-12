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
<img src="https://cdn4.telesco.pe/file/Xrpecfhh4mmjC7QpsJqzy92vUpklfRToNPS9WFpPAu5LFmxvA7CCLtbaB6w5MApazSfrghrSIYOcBsiklynbKJnqH7Y--eSt2D1YPu6iZJrA58YFcJYriQudrjSiml1wG2CBfRtI1ETnIX5tg2ogxaxUp6xqCVzUW_Arv404Bti_c-EOrtpc66gZImLKuYGD7lGdL8xZgHGPbrYYY9FgpwBES_dqPS4u63cu1DYEgK3HdxzQXazRS3WeQvtJSTT4FLm-GdbDb98xxZhiG8IbjK2rhA-BbD2IxWC9ydU3B3RGc2sB6ZfGDuNC2KjvkuY1StKHVdp4hmF_ckEsjQ0QQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=B5fnVtnz-zDq_qaGHzC9YM44M4_7atKagBNH1UJH035cpEy1wP6DYKK09waQJxKbsUk6ERjw0yXwXemA_DCeCxIRFMszgzJ_x1K35iQ_-80WN2NBxf3Kj2-H7Mt9eUD1DC2z8rH3bUhoOAVa_2bCDQfbobS216U74v3ShPLFrtq6CemKJSrTea1mZaPWgJgvrSdBQon1sSWYtusPmmjBMjt2M8ABJrrMaTfzLhnJig2XnVbh5iFobd4n5lagx1SM9DOCUvUOlh7y1lCpYINaKGXknkYeJBqfSz6BPn0wR7O4JdZlsjGgPBeen-IQ0-peiqSsYjoZpSUIUKqdRedEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rg5kACutvpkyY3sNxAE17vhfygDp0_U4Gpk17VX9ydYMbkReSlIEumOIdAGajs6NqkqrhyuNrJgqu8q30stWVyv0-v5r7Fdi1oQEqELbiun0h8U7pM01qXsf6PLqlHJ8zr8EI5rsPGJ54MytzEIEIT9Wmiu47yWv_vaFBMjjQnyjgD2nRFkyAKCk3uYgUThUSIqB3KNIpme_38c4rdFfFuZhqW9H8j_fYDTFw_rqfBHh83qd3GgRY0q2JPhElvPd-dEhv3opYyt9B8zAPt5p6m1GQsKq_b2tAyMJ2QpMVP0EKrdhcJzdL59v5EqqwDQW9gRfUjx_Iwi75591lhfJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=RcYulb-NLyH9YavVDYWEXvsa56GaDx9sjwfYR-7jn_4LlPuNueZgAtoC09Nnsh2oqdPoYj68Cx_hkWmztXWfWkzTce9Mx9mRFNj3KqBNo3cM_AxExF4H6eZkTPtmZNN6tSdwGPkD8HMH5j1fS9mMk2cK-B8aLQsq_hsjf9I8KvPXP7AbF-JHm-WG_vdB8tWZnRJW6WGMdW0YBSqmSFJlvyii0XrSJb9Dv64Z3beC9toZXSAl5kn_w7NJWI36PDu8dilgYoydQoyzTyXietKo6DFiuComjOordPkIr4deeqTP3DqG1u-tw5xI20bBGalm64qXCdVE5K2RwPboLzj9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzb0Pcl03Qh68m_aeP1jNKBdkDOSbZVwxuVfUTcFLuW1Y2XQCZr_HXYGeI4RvVVYozacCN2V5e72k0u9JRDGrd9cJGGZGC4yd-h4dBQCzcfOO5X_AYndSJ8E44SBJHRqLBP3bjKhZlEWWQl6sy9hQXUN9BKpwIra3YbvY47DfTfXZDaOZVM6ftYvsLoIAtCa-HOiEPbtCIP3LU1ywhTi11n5H5H8Hk239YVOiCnqadimOun3ZsDwxQYfMBgZHRh5X6a4-L80K8dEwcjQxlHCKdP6XzozW-3zUyu3o6xHI6egGeGQRaU5TOvCJVtsoltvPt2aK5Z680eRH_ZjOWul8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=XV7r8qNCBmYeidozXAHEnHJ4hr-9HoobO5ZsUyqP2yvMpaGLBCUpr9kjS_79HGVkqu50O_AuCo2O3YFLfjqel3-DQ0YIe7O8VVxfBro3zJFPTwHQ16pvkLJalaoSjdBgzz7Z6AzVXgzrtMud9ZZORWBAI3U70ZvJ-BrE3mqA-fe0MTs-0L3rANnjxtf484ZNBoUoZ1GIGIgr64t6d6SfxlC6nhySXNm6r3_7L2al1zrXKUP00HsVY07kwdCg64b_IH-oRBrQLaQJerAaonhzSUc_AkaFnPA6vzUvpX2BvJZbJAfRobBUr4AnOju4ZaUbCWdpsY5_axiL_Lt41Q_cUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=hKZOZSLlvmPJgpQYIu5hn3Zy1i_Vv1mJuMt_3coQgYMa2VLKrWQHQq8xwxVyWZ_xtJRF_n5MSPN5h19GTJh2sTRPkHCmknMwxRyWk5okBrxrm3pIjWv_auryvKXsRQEDtsoPBowrTag-XMwRnK6FwJyesxYr_qduVVorr61DP_7q2pmJ4kpcXOy-no5vOu0PS-C_cDmc4js4AX90zTHRS_51V3tgyhSmpXzng6fZaYHzZm85Pk6s9zPlS2RkCxugQFGc_8YryW7hxPpZyT6DczsRYs9Qed0tQlbWw9B72Oz99fZWLRVyBR_7eIEmqui8A1y63tZg2oGzZflAeyLfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBJ4KYnEQElbGD8Qev8OAA6qzT1bLj2XkSgNKF7Agq77OaY2Txm9uk1W20nt5P_C5LWUpFEEcfu8Uyi5_wBuh8nT3effjQv97FcbBjs6IUNZ8KhNUDVDrvS-R27PtE5Cy76iQvw3Htp0tGn2iFOBQdbjfyYDDGLnpmfF44JUaqe5jJyO-2tZHiMJ5hH4FXT4dOD5rYob5Nl_Wk9fFBkgyBMCWn_OkPodz0uAUrJY1l6MHN_2W0QOWInlVNXVFGLZbWuK3oxrh_XmPlMdad8V5o-4YlXJrEr1JYhcHhDdq9MiYAVhAtE4YGSm2dzfcPMAr3jaJ8FooBAesvlHMUeYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=YsSkQyuDqw23ckdxVd323yQEt4-DaVeOYmlwBhOnIC9X5115IAnFzKtLvjFUwwVJ1nhLqm8d97fs7Ji-8MtvCKFpqXhuEn_5GVy2Ngh0ahcDTi6oZuDIiN6gXFNa-a7mQvn5pFVqY8EaSdEKiK1zC1TlFrfmkEmISibfANJXMZxLLq9BjtVA8qAAddGp_WOlGeqRwPKWdAQX6U3VfpNtSNhw15oXzUaSrJUV_905SOS5ESK2JzMfFVhg9iGNhywXbg1NOWg64Y5XWysrvjIrGZxEeNsYv-Cib8eeb9SKNpgLwKnZ6s6Bxzm6jqjViaBAbNPcr37cTMm7Q-7mpm0v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=YsSkQyuDqw23ckdxVd323yQEt4-DaVeOYmlwBhOnIC9X5115IAnFzKtLvjFUwwVJ1nhLqm8d97fs7Ji-8MtvCKFpqXhuEn_5GVy2Ngh0ahcDTi6oZuDIiN6gXFNa-a7mQvn5pFVqY8EaSdEKiK1zC1TlFrfmkEmISibfANJXMZxLLq9BjtVA8qAAddGp_WOlGeqRwPKWdAQX6U3VfpNtSNhw15oXzUaSrJUV_905SOS5ESK2JzMfFVhg9iGNhywXbg1NOWg64Y5XWysrvjIrGZxEeNsYv-Cib8eeb9SKNpgLwKnZ6s6Bxzm6jqjViaBAbNPcr37cTMm7Q-7mpm0v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPefCKaNH6tM7-virK0YI_RnK99Qfw5eKA2_2LiYcppHzIAPEJYY3eynV4O1kecDvhrQ20884AMn2RLQbsM3UI-0s7rqVeSczY2TgOEn4L1Gfp_ZXDpWh99h7h_qLwpPnXygOb1APvCHI9hvrMqsteNYjd6koWPe52lgpuqzH1OQ8PSjBvj0Lu8mIenRyoLECymhQEZ34poXdptdmhxyzq5X9Uw2KIc_Gr6sB-5uqCMVLrtCxAH_7hoAIM3v77ILlAjXuXPJJZxu5qcyoKHbePabGfheAffxqtwvIMVOTiA0ZZhufTnS6AB2LrKTG6zLyoA44l0PcjFUm4ctSyuvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQTA_BBfIp8edXS8z-arvxvxVl4weBgpKJqwrwbnOOitfh5Xve-VMycSvj5isv6nuHIdirC954KV6GXRFQnRjiCppIKsNnkc4AYjwjYLHBvTT92Pe6YV6SAjeojXPjT36fFQuK5EkqqBXkKopOvnMK_zHDFB4X9Yzn3meGUpmSBo9F_zELOpCoFStOgbom6MVgeMP_qA1KuRV4-VFkao-cTPdcGLX6tW6sNIyIRxW5GE3MeG5HzQN8EWOrGvTOS2swV_S1NHIbd8QXyBk4hLROUWvgEBnhYviOCSNTvihjCjWEjWoMQCo-z7RwP3RLWgDEQXCeNjcD8GISOAuTWcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2kABYXI7ejYiXG8qOi2vFcX85Q32vh_-tObwdgs581LfsfIQjwmu0xvQFfUot6XTIS9MpvddQeF4uJ6VBoYnIhvWmbbqF7nuH53twj-9IDmTZjD-_nuXOGtps9CHjjJGD6iO5iULTfADrulNbXkxjlHTouz_oZROQxTMMnXvrZNB2Y4XVgRlXMlmDSOVTOzpHU026ycAsEJtWXxYaRZTYK8PSP_DJTS63Dk4-KGgohJ4OpPcXTe2bCv8cQbWyLlCQfkA9jrFShk6LqBxuDiGttaQqTp5smMV-8ziWW63l9OCdclS2SnXbfioy6YhLO043FcAq7HobdO2IQETQSaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYTv-HgUy_5s1nEdA1C03yY-_cjD5DIZc5GnZD2_8KjAlUQDMjyIA0ZL3Mk5C4w02TlWcQzneFmkQk-iNANo3fH32EkPPFfvh-mSJiaCdPn2JQ1MgEIFeBM0HK5j6gVVfeZJ2l6awhm0sdjR-Qg8_fNhqA5l3Y8jyH8qfcWTAzKSuhpz_5fynvIZRvBnqEs68ELAglolbeeKfHod5vKIvmaovpguE5m0aFLTrrBKwboA5ZoCs4jM1SLtQAPWTbm9gQFqZ-Z9KFgbyPGHgEeitj4J5Lt-_Puoph5NpVV2kXfxz4KMd263G5SCqJTm4h0vyy9-dkmdnBUw3-2hGVg_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUFdNAgOEweWvkY8xcPoMmMj8kpLAdlz-FGl9mhbKeeHBnnvFdva2cBnZsesFYvij1BICO-XN2VsgCeSOU-a8FyG-waNou2Vzx2W6AYolHdOWHR6PlDnOkGpXtXtreF8fO7rTUerBluX3a3_yk4tF8M3l95KP7MLJ2PN-lR5Wn6D3X8NHWh0Px-_LxeSd9Bqpga5I6TDMHkOVSoqFYtNX2zAxHDluCKRkvIjqsM0Clk7AlmZaojkEy_7psMxC5_h4p4CDORKn4wA7Xl5DY-mvchEAmXEMKw-QRiEuDgRdXP0DVmNhNoFCkzEEJ9IbH5W23SU9GxcLTE2njEW24q8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5UJOnBGFWgX_F4OdwivqYQtGOwzQkuIMOfDkI-LKQtUKkPPR87EDLtMe8cFsvLCo4UTq-io0e91OnTZb4Ldc0F_O5ERnNv7BPGMhemCZ_EzqjJzr5wDUeKmgIJjRhkEW1hnFe_Tta-XkDVa9MtpDC14PdK4r5kZdbMp9EPpOs4YkOtN2virduWso3VnHCgJqieSy-lS9zHkd1ACbxRxiOb55OJLcTib5gbeGTOJOzjQG12IfJfm9aIzpJX722hJHS0f80Mq61rx2ZQDa6324er_e6rBWlGC6vS7_EEgAi1ZuTLUmg0fwiA19BC-AX3VrkReoB5cvsR0OCcEXWiGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=QKTB9f3YFDS4UFrxJi3cIBCLv_gqIMvKHUyHFbpa6yNHNMcGkDm81Qfu3qhblARXCA9NZQD-Sii-9B4XpI1M0m8fqzyJTaqmG9z4TPLDcc7Se71o7DKTgj3vrwbUUvSnhAUJmPBpTQl5RjaBqENU4r-niEv0Fxb-3vMzBDmoYxOJx9AyYZ8TZ93ssh9kD1NYfjP-Mn5IAOuGWvbmuaLo1utFUG2pn_uT1jlZA2b-rceF_Q0EUjnAzlrRRH9Tn_iqMrVJ1BONBgtgAslq7g9a4OUnzMJ7_apW7PKdKQ0zR4IpwO2_MGuNRtc3a6aNTTF5_mRhr7d5mLPXC8-op4tudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=QKTB9f3YFDS4UFrxJi3cIBCLv_gqIMvKHUyHFbpa6yNHNMcGkDm81Qfu3qhblARXCA9NZQD-Sii-9B4XpI1M0m8fqzyJTaqmG9z4TPLDcc7Se71o7DKTgj3vrwbUUvSnhAUJmPBpTQl5RjaBqENU4r-niEv0Fxb-3vMzBDmoYxOJx9AyYZ8TZ93ssh9kD1NYfjP-Mn5IAOuGWvbmuaLo1utFUG2pn_uT1jlZA2b-rceF_Q0EUjnAzlrRRH9Tn_iqMrVJ1BONBgtgAslq7g9a4OUnzMJ7_apW7PKdKQ0zR4IpwO2_MGuNRtc3a6aNTTF5_mRhr7d5mLPXC8-op4tudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofYjowEw9k6dDU30Skp_JBpyH31j9YN1K9B4a_M0lZ16okjYOxc0_t4R5BlwojebKz8KJgT5G4yDGeYSeFmBHglTNhcvnFF1Qc0OWTWrs8juz7sD8yckDoC0Ng66_ukz_KLz2pvQFNcfjR3P-yNuNdqaur-E2lVb2RZw3CUs574nosqOWrekC9ifHdaBgJR_ZrxHXu4bNy_WZsUDAVVe9Odi6U6-rYGeoEzoVFMTO9vm34hqNt8MQjHoT3HgJRniregA26UACNQ1zAh2X5xCziZZGdGkBSQnnWvY4-UzbSoB3cAMhPP8sgHQ7cIEznEr_oX78s7jYWkGV6x62guITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGtVNiVX0QnIR8Hbpzp_NHn5YKx40UE9y_RXZ15PNPDWwMSC97nt0sq60p9n1AF6LlqjCGB8XFxsJMXRHIJoH2w7V6IaNnY5zyroRhsthLftrRboMHzGplrqVeXgS76h7TX8Gxld7TDSxVmmJExEbBAcTCCH0FbxZUcfTbotkh7skB7ul7NrjpYG3Pm4oa_75HoPyiF982EHamArV_f7OtbpukDAPxHa2OkwpDGqHmgfe_VOEz3E6Uo5v1skGGf0SqJzXFtHqoM1NBgHWOGP5Oj0SAsURdRJWK6Bv3rv27L-R75CqN3lzaJcShSJe8GP9e5IdzEWFWgbk_I4XsF4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgzxJSUcdS3s2X_qR1GC5yOYSje4KLBd5HlY69n7jsFVCzbmXfZk0cdtlzODE70Ujf_5GucwYarfimmYuwdXi9L_yrQofPxtBcxic8y0lANHH8YIsQkZSVq6d_t7p26UEKByIqz1b4aVka6rR6hond6U-Zt21TfTcrab54imlO5U5IVD9Bu-WFte_BrSB-EC2SM70JwmJibD14cb7lpb66XpAEWr5XT1gKYQm-528Gg33TCPbLGEZ_GDsMmG_Cz3z_MvnHk8XKFy5XIBakFnqIr8YPCRlI5f2LVM2pbRHfqzhxHMj3E1Wxgu4JqPcCTqBFecC81keXET-lY3OGIRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1r23weoFBNtc5pzbvjpQ50gm7v4OpG_NniKU8YIIUHAHQqcuw36Mli3vi5QRSnd0u3RnO-8TTk0RzIhxjGFIC3AnzhKEP3ov6gHKkF0eZmwM76ZQKb4wiDva2_YupcqZFETXJGWGEEzAHQGEQcnor5chP-gKblmi799glIjqLQFtapNt8kbliybghPeu7Aneeyq1n7IbhoH14Oxm3nfbIOsvMhm3uq86AnCjrhOBLlqy-ogHBq-I9UC-p3w7tgPCySx1hXU9u1AQPvx3x9DzB29JsbF5z5nSPBLQfUNguJOQZlHPYmY_CY_ilqu3WBw2SQdJTHWF5_D-ST4EpSTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=rSHe5a3OXCrH-wn4ofJz92duWPkiL8OSPObK4WMWZwU1Zqmn5L5bOo0SZVTjBNINwGPE3nmqZa0X1jqoL4Zk0A7reZE6wRRBmGwDT_1DkaPY3k2qqN_Z0IoqXARqaMROu5IB_185dIaqXniisBhUjaOHnxbLfYzBTblWvdmAYQjflUwBttW-eWfOLn76Oyy5vo-mMwQxdYL-CU1hBIuqWfR_95h7fHdMMl3kvUgqw1i4vtGjldLJXj8NfSVlK0LE4d7CbQPKESnSlB7SDzq5itE-iefjPXLqU49oDB_bbMCvW13JJC4TS1wPKGnzTlMEV9wPIh2FmbyhVW9k17RVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=rSHe5a3OXCrH-wn4ofJz92duWPkiL8OSPObK4WMWZwU1Zqmn5L5bOo0SZVTjBNINwGPE3nmqZa0X1jqoL4Zk0A7reZE6wRRBmGwDT_1DkaPY3k2qqN_Z0IoqXARqaMROu5IB_185dIaqXniisBhUjaOHnxbLfYzBTblWvdmAYQjflUwBttW-eWfOLn76Oyy5vo-mMwQxdYL-CU1hBIuqWfR_95h7fHdMMl3kvUgqw1i4vtGjldLJXj8NfSVlK0LE4d7CbQPKESnSlB7SDzq5itE-iefjPXLqU49oDB_bbMCvW13JJC4TS1wPKGnzTlMEV9wPIh2FmbyhVW9k17RVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx0Dij2Bxcneo-Xj9dQI6QwfQl3OezMWTYdbS1V0qBKNEy-MCclxBijcxEbGZEmHz2gIU6R0W-XrjEm0EZpTE21l5gBCpNizEcQY0GHdLjpqzp1KkoMqEd8z8LagPTrvq8ra5E01VbpHSWKKaqL4NgpBImxtNQwuDvzy3Z_XbEBdESi-Eh6SVpGBJA6nnqdStA1FJ5NWqoiI3HSclmEPdXm4ofTe0IpDpbaTBHbNZwr-oGbSmdMQ1bGTJRbL__anlXxqR8Gp1R5zY3N3HJ4ZmOa1Eu8dMIoaoxIP_76527D1l9BI2W7lKmePsxwK-1ns9sfO9E2L_SNLaxu6db9BSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0as26SMtF60DpvC1jdMOCXkWL0qaqszdKtQ_7Fu-mJnRQlGTCZJLGOyRb4Zpoi0oHoe8lwj0zOhAq7xGzKh2kQjRZOeAkQUqovJ-UNTKLRMO8RmMAh8qKdwmPHLAmWc1AyXx1mcY-nDD78jGLua2IdQVaaluTi0JR_jmZsgG40YR8uxNtPxQRcEpKP8OwR7N4OQrA88K-6aOdwKk5oH9bhnL4W9MaMBZIBkWfqmytzKYd1N6ngKQBEpRic-SEJej3PzIAMMwISlYXKX41ZN_4_8VyeYPthIlTnleNmqEg0rkQc9opHD6NJtMnj9MUEC5303sg0AaoXAkJG7BdMh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RanqY-APrRx2-WRdtNwQJqqTG-2jFV0yNKlTeKWdTdruJVgA9QBed0SIiaDzfIaTHF1CDmclY1MRCDLnmFx5ORXDYK8-askjUR06m13CwresvYYtP-Qilx93An1ZpBxbmZPyz77lkR-vtFeaDYcId9OvtBr-VwynqPqy6ZBfs0zNdagSik8Kl6rssZs0D7X69Dj6IT1_-w061uKAijAe0DxbZg_UVki0NwpNlVCJ6OKRFXONx-sbHc4xaybb_mdBMEqxARKH8BY5kIdgpI0K6D4GDc-ucus7BUPi1y7avrSzp6_Q-E5yOK6jw661m8Jnu55kjis2x_VKJq77fRaayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELdv_-yF3Vw_2Ke1ZntqQ-x3gwkX-auFdOUtxaKewRYKEWMkoTJiqjEWCBnTUpIqKMR_S3hmoCMxtfpCR9mqsxcw0sGmymcp4S3mDyZtB5eEA6Kubd0wuz3RSfMMJQRHzeEBAsXI_Y2Hjn9bPPVwL85-u1hQcPMphF2gZImI-soKnFU92vtMRUnzHmzJKfDmOYU_SBk_oWrmGMEOr0mS67OoD95Xfk0aWVgXRWe1uHdBfcQzf3bElseDluUa4AaTX7jSVySSUM2VGB-FbjyGytNKj5p8pRh9xVj_xbMSKAY7ePIy0paJVolZaG2ZPVsBqvyyPdNZin0oxTAhj1FfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggt4ksPUrZZvQXuBWv0yItl6X_WMP2Qgdzy4ob93371wGspEABtqTd4V0C6elSxs0xEP21s6w7zOOX4jomOxBLZ_7LcP__4UDviTeZW5oyLcmDJzs7cX35IdCmJ1f3P-uYlljOTTe6YUbeEuqyJeRqMRH-hnz_LD_rAMIYFHPcp4hT3I15LEUUFvm16yMIO-JKNSGLGXw9ZpEeipoHNg5ekKaBAOxtsKxAjyJWUGWxdLNw2ey66dM4GNRGJilyYRZPYiIwtECRSFMepWmu9XTDOL3jrDEy-BQPl052rFmpn7PDdRx5HFeorFuij-TDxgP0BQKur-SPopnLw0QPy1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BguSuXxAklhA_WOC2WglCX5WeEQ8rDUFvumKeZIedqdt3pfl3W1yUmLFixjGTzKCOj04JDgvexJoHJfo6SCBGy3lmdta2jhcxKYTHZWX_8VMX29h1YNM1xtOlE1jB1zoDYcH1ooVaVjmVonmrIJIg7ViDtDG4HJlgSqjmL1G2Dt5oKF4b76zmbJgUhxxQZaweGrnXpn0EDAGgNEXqS1hTU8QZSXOJzgiV8-gUoPf9WHaljjJNfcEW-vTYF3vCtKlaNWwVV0oBjL1MQ389Zc2nvmDMaOMN2uEnxiiR3cbo-WICWm8JMx0QWwHETh4VfJ0psl1g4Lvm8_l4XSnVA3XNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEXxzWhLzBr2o371NwAO_0-m9BuYwxO5_gdPz60G_XORGwOgvV53s5lVHSnxeRGiedUpg0GOZthItsMH3_8t4ZTKQtgclRDgnGk7B9sSdOXWXTZ_Hk4t_rpoW2jE94Zt9YX_FCXgiQlf7pkvAI0z5XEZMFEzuIZYU0TiXj1qsxhDZQNwxue_WuxufnkEZm-_ELJ5_9KoYt9A4ykxUpjDicY7wcyk-kJ9jdjw1012hnbGg2vUIbjGySwV3KzR2gcZm9bx_ISCkoD6rIuRsDPYNSRx-FNFq5cgWP0lPsE9feWKgXsrFa-ysdlxsUu-zqDeNRL69o93fUyKQ_9C7ESuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQ9wNWySatAkEVuAR67InyMLan4vTAcKheBo8UVtVd5n0R_5eqBog1KwBqGHcs5ZPtL6bYWKMe9brnfqk436JXv_xJs0_6nFp3duf5tBjTXBbZ_OP4b83EQ3E6Z8MHREUn15uieYwbDVYw5gbr285R8Q8LXolJQ7YqvvmSvLlUU5K3Q_jX1sYtCxqliTY2m3jq8F0ZCPq_gfQ07r3RSEVn-6aMzTKiMqx9OyvdEyqjsPdVBqf4Cl394_zis3wWNF8LBMbmxe_vEF1NzFyHbeZ9lNTOAv1l_xqEHJjnVFRkbcwhsNdrdNG6bBVNsS83paz5nqx_66xGHYUjCbc98ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY5c6j3xGf4HFJ8cvvorDVcEPlh4XRlpSaDDqKkDrEm215wGVbaJO0K4Nt7VqZ-l7fR2oL7yNCEd3OdO63stPfm_GE-qewxy5uA8ev-egJ1LQYjVr7EETs0q_fgzXKE_TqDNKyRV0LpBoYA3tG3EFe6GnpJUveJwkzJHFXGP3HsUjYNXzP3ya9Ig4BR6PFB_N9ZMXNGMqIgX8g5xmRCNqyrOeTCGip8LUuL5YHm0N4aVC0DVwFPBkAlF2dpPUbKHA-ELnzHzn2oRYQd5rnioTw-Ob29MHurmuM_hz-jk-EmAyxLi8eCbcyy5yHmuXmiJ7WwvlcPFh9Mi3yFirp3S7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ennDgthbuMlM8lWD4b-V314-ljjQsdw0PpJb4HiysLN9zERayhgUe5v8JPYotpbvGBhKIEqmYiYL_PrH9WMHzSxttX_yfgLe9o_TuqOSzUvprFaqC9BxRi0FnOqrFxnmRaZ2qPgI0ZK3m-hGMzvMrd_Hlkpyvskt1O24erRvtOEJygednnY1rQ2RtEQS9eLUd2TIbkktKR8SkW93FLifi2CdL-XTN7W5geOM5NkyIIbR-z7uy1nhMvJWHPFo3sFZC-Ez-JDjN-XMPpyKBeMmuB1acErrn-3v390CmCJpwlcddHt2t4MNiohbEAXuJnl2asxWnoHZVkvLdfsoJ8wc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=nJgrmVFZpdOwq-aSp868mQL_9_6eDxZYaLGEII6tngLWqOvU85GI9S_leMxpkBi2e2x65cDSEnjs98XSXqIyrusrvuxkMthtA7wrRESw97TWe6FRjUT5UT_w8w6LquaseD5psgHmmseh0PkYrRSPApywtvj_WarSLc1-eiJDCoxQKaPLrmWHtwmHBDDviOyt-pujsBE3AZswje0hwLWDyf3cCsU7tdZInD8M0ayia9edZzhx86rt9IElCKZlVIUYtCTd1edggh_3mH0h6sgShjfHwZ1YUfOGb1BdHb6BT1s5COjeA7ni_MmLCVqhw1IBsJYwDI5w1L4VjDVBbWp7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=nJgrmVFZpdOwq-aSp868mQL_9_6eDxZYaLGEII6tngLWqOvU85GI9S_leMxpkBi2e2x65cDSEnjs98XSXqIyrusrvuxkMthtA7wrRESw97TWe6FRjUT5UT_w8w6LquaseD5psgHmmseh0PkYrRSPApywtvj_WarSLc1-eiJDCoxQKaPLrmWHtwmHBDDviOyt-pujsBE3AZswje0hwLWDyf3cCsU7tdZInD8M0ayia9edZzhx86rt9IElCKZlVIUYtCTd1edggh_3mH0h6sgShjfHwZ1YUfOGb1BdHb6BT1s5COjeA7ni_MmLCVqhw1IBsJYwDI5w1L4VjDVBbWp7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz22bO-yn52qPrEMG9zaHV9Z4Ob-aVLj94rFyVcDuG7aBWwhHBBASORz5mpE1I2RrmfnfGY2CT-QU3IA2eXjXJP7zGYF6_nq4SIovtJXNioAxLf5GnrAZUV4DGis7IXBOAmJOHAzzu2fBW3drkeOivlxGvVnVcYf-YJPko_0XpyES9GBf3U34PAKxyinVRC5pD1JJkajCoBWJdtd9WdQ2gJRD_QxzL2IRBTok4SfpT2Fu9QIYaznndqYgmqDz-mBZWLsfcvMHtHpSk4iQRsU_70MKec-Q-I2k-rzTPDdANTYLJpdcdUKj9lhwahMHJxoBnbb7qS4kjLBT7HrP5sSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjnflJwhJI0F3l_VzBxKX_QLaW_EYI1yDL3qpGRj0232yXeotxz-4JmT04HhtWDCx9XEmbeC5dgFNhir6fmwPg6HxdmmwmF6YAASoNCYSL8GNvGpaw4RmCAxj3Ue74H-WQpSKxeoK-z5X3KgiVzcCj6g8ZvKv5s-sNHoBXFgM8O-aCtGw5RLfOgIT9rXMPEHO5B_733mpVLk3ij999EMEEDJOSQjZEJrsk3IuKmYNZjuqLsZLwGJdNPZ24w6aguVSU9QFgpDSq5-Cq-UY__SgP9R7k8pQLNGjZHQHVUobbTcL619e7dGVD_XspAjvDTA9qk5SjzE8RDrqp99Teyvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=IpXMP-jzw7bZzVSGA8nyBscuH4VvAgKQsKuKLsPfZXSluK_d_D9vDVqjZXVI04udzmi9LN6ACpGwPGiTEje7sZD-Y6QM1vlemSssk2Ii6-idTf6pe6IuAVfIfZZTZuIIDj7XxCa306ublmRzKzLsd1JTCOF_sdvvZKmO2rDLSsKpknszPU6zxsLi8bmHpls5WSuYvvhnVe0B6Z164LSrRBWOYk-IKDMkiYClyTp8SrJAafKvQZDRAxGW3p4PqX_hcj_BenP0OWhNG3gxKqmwKQIBouiRWdB1y5H4wB_O41eo4A1mUE0JQIBWs8oFSyTBDclogTuyn2FpVK11TliRiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=IpXMP-jzw7bZzVSGA8nyBscuH4VvAgKQsKuKLsPfZXSluK_d_D9vDVqjZXVI04udzmi9LN6ACpGwPGiTEje7sZD-Y6QM1vlemSssk2Ii6-idTf6pe6IuAVfIfZZTZuIIDj7XxCa306ublmRzKzLsd1JTCOF_sdvvZKmO2rDLSsKpknszPU6zxsLi8bmHpls5WSuYvvhnVe0B6Z164LSrRBWOYk-IKDMkiYClyTp8SrJAafKvQZDRAxGW3p4PqX_hcj_BenP0OWhNG3gxKqmwKQIBouiRWdB1y5H4wB_O41eo4A1mUE0JQIBWs8oFSyTBDclogTuyn2FpVK11TliRiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZcxzXjOLX3rVCAZNrQrZC0HvfwRCHEvlvYPCN4ey6QXdvmA5xK3IjFojFGCbt0p6cig3KKF4CGCNM5wrphFSlYx_qhV7m0nvIyYVomp33oPs614GeLA8Om7KjTFCSK7bd0U82goKTgYrs3EOpooSAMnO5H6UnZeQB3tvh6vP3u2uHyByD8sMMkwLpbNzBqBwWpZKQ6k08jGczy6VNyGP38oKReg8kjeoS7n8mKF7GGUAWiwt6V3t8f0XJcuJcuS_8YDRH717l7oCxAGuOpJ4VNo4Bnj_093DIa2zhvrDwljFyRgTrt6N71oma0Zli-H5y0khCgiAZ6ufuXbBjxsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLU5o98Hylm9GShV56MBr5MiMkz3XkAjXVrwTKXjD0zxZcHHt9wsgJnj6QjdjUvOBNWKlTMoxwX7zB5mAyUoocEVtW81zNkhGif9ejn6BNHYojaZYSIg8IIrxwwm3IaGGdz5iOUgrMWof4PfHU4XsO9uXlJ4zjFBJcOEP26HjsyGvIF-uejopzIcglpvwbuWHhWNURhxj9TvZdFsUHyGu7_T8jfiJ3Z5mAKrhw94eKmcfMrKrxEDs7jTTFPrfi-aeKetFnSykiBmz1OnHABL5ooGBvImL3hhDSWJZSWi7-eAxGegZVxJGFjLbiupUTMn6RADGB9Q2kgx849a6k3S_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=QDepzzQ_BsV1gnsYY-GmBdIaISIbmKn_xYtxl6JdWWDOYbqBdXFRDOA8rKjX45mMeS9KAvVcary3ho-_b1vBFU7gm7wlrRSsNmW1vIJ8ScR8zahQl41wg0aUnVz4RFqZ2EkASqMQ_gRZwbSrVlT9xSuNLAGxIUQqBcUrPeUFV21tn2oo3lZYT5nS0cEduzwWNb42m5Dc5Df8jfKCC_QLnDuQp0B0lLEsTU2iwfQfYctM_ke6vCwIBoenV0_KhdJtYmTfqenhgzAqtANW0ak_SvmNGyrWTypy15oIKyOiYqeVSuXlYolND6a1uRSihre28sLksakD0-hROMDVHJJuHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=QDepzzQ_BsV1gnsYY-GmBdIaISIbmKn_xYtxl6JdWWDOYbqBdXFRDOA8rKjX45mMeS9KAvVcary3ho-_b1vBFU7gm7wlrRSsNmW1vIJ8ScR8zahQl41wg0aUnVz4RFqZ2EkASqMQ_gRZwbSrVlT9xSuNLAGxIUQqBcUrPeUFV21tn2oo3lZYT5nS0cEduzwWNb42m5Dc5Df8jfKCC_QLnDuQp0B0lLEsTU2iwfQfYctM_ke6vCwIBoenV0_KhdJtYmTfqenhgzAqtANW0ak_SvmNGyrWTypy15oIKyOiYqeVSuXlYolND6a1uRSihre28sLksakD0-hROMDVHJJuHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzHtuWmPJRdBkbtJtC6tEQ333aeUt1av1UdX_tOVnjOpvfFFsURL8Tc8YB7ncjxSNwFqi9gV-Jc_8Yckhea0ObmXeceuo2MOOn5ijldTQlMCQ0ivrj1nv0FR7R2g7EnYsVeyEsAMOs7XlGWb6Vbtb38OcrDAIb_QqVpRtDfP10lDPn8ijHaXthIzRTtuwzUnIsLmLSTPZvP3KchXYlYQSl-p32reuaHGeo1h3wYB49us2GxiQhSa_SCwRLWmhDIXlz4fdBwC9HPYrUZqB1kKAZA0eE9dQSG4hEHp6RNwNf2mgcd-AVke5qkGURL7Jc4Ggz5tA07gqYx-owuWcdEJRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2p7XZcGiDlvaOJTUu4pplv3P0QEWr07us10RXgRHZM7TrUX5vsaMEoq4eXn179INiBpIOizjTnN-Vflrrs1xPWrygwxXALPi-a2UFWCSre6Y4nqPx54WmPkoQgQkIPrrk2OPSDUZYg9QEXMlq8Oe557GQqWALWjKw85jFS2o8vjQK4sH2bVBtlZYl2DPV7z-5pil1qumD49pbqpvHRVavtSfYIUO3VGS4PejXG3R8zWdvE4bRW48Wwc7oVgJTXhGY51YXxQmslVqCvhwgm5wYySIvBGvs7k6pSKMSnDZ3c5QOumnIlDwUgDPs8KZulN68iOC0mZO3u4E2me-rKTrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=aB60poHTi_hXF4tz0z5DIiaNfkbNXGE-A2vC3i4p6Kr05ueeHLhUNdaOfK7bBvaIJ2K1GHB07v1R4Ym3YKMLN8l7A7ax2QJW6LJeg23a7jAJUv31GMIO3M16bTiWpAK_WVfl5P3w6r8jk0sGvhwLX0_c_Qe7J8vOYcDKPenDJbZZ4u71eKKY6WXGapvRtfaGfQrz-PtlXkgEnGOH6C655BY3-5EORG3u69mnbLYMB7WxzbUURyUFejvq9ygpLzwm-ojUChCLEizsHABd5browisdsFK97N8vEAc1tqmDHGIzjUw3g7bV9XJJHcjMyZhZ0fAtW3IshxuzEn1etDiG6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=aB60poHTi_hXF4tz0z5DIiaNfkbNXGE-A2vC3i4p6Kr05ueeHLhUNdaOfK7bBvaIJ2K1GHB07v1R4Ym3YKMLN8l7A7ax2QJW6LJeg23a7jAJUv31GMIO3M16bTiWpAK_WVfl5P3w6r8jk0sGvhwLX0_c_Qe7J8vOYcDKPenDJbZZ4u71eKKY6WXGapvRtfaGfQrz-PtlXkgEnGOH6C655BY3-5EORG3u69mnbLYMB7WxzbUURyUFejvq9ygpLzwm-ojUChCLEizsHABd5browisdsFK97N8vEAc1tqmDHGIzjUw3g7bV9XJJHcjMyZhZ0fAtW3IshxuzEn1etDiG6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieoK6JblT3epgGzr9k8uyasJ8Jub3W4UGIUJscvU5Us2HlS8mYq81rRqh3WKEt2ltvRjVtuSLefGUwOCSFdr0bE8jn64C-augNJJvPQ0xaX-afkG3tj-bAAFCbiJDrWMh_Ram4C-iQcYshHxSjWVjKOHmNMjfvxIQA30HEsTE4jNcZbp0XmL3hKN7qLkgEFEk7qrYHZi6qLOXcloj6sgdexl4O1wooWQmXySoVK0HNQ2r0Z2AOM404AIiO2SFg6hJJ9e4e7_jwZkY9-FVtHD0V7kO-qcJMCAK513vQuWX-pF4FN7RTnqGADdIw3ZBjs7sOH8I8venL84UKVB0dWhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2OlQju40VSIb1W3AOoKd9bcT-rzQOBvkdjja6w-BlSg1Zk_f3U9lrlliBGjytKKvKD53kBdk1nibnezFvEHZjx8UpdOfeEa3Tt_kb6iBMCDOojFRE3xxfWGgChye6h0ow8LY0ArrNDhHa2PXFhm8PbGjheCyFP02HcqpVJgrfJ9O49rDC94CAePrEgf1RUyRjeUloKwS5astKzTAcPKKXfyF7cXBxV-DqMLPrTSa5iaRo-qxb1f6Xy2V07zlJwpQDPRQ8iZq5T1QkBcMK3W5KYiRBoQ8icEKX5zmsSE9oVL3eiIBtauBv_7byjEW9IMeNvaB0Ai0gzH_JqOQGM7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MulZqGA8AiTH4mTnNTU85MrA2XScjdQNTC-_RVWXUFqe94LwtiiaB1fu-5pywU0swDfOF9UMRiMEF1Ksh7QuK2Z1IkgE5o1U2I97XXvJh0CoJQuSBoyr7KZW0IpiQKUxruGeKMNk1d0p4fJlHd0D2UHyES5BRocPTIRYA2gHw43tUz24zyTSetqzxWdOpjKHGTtyOCPGgUbAGuzDGQkbV9iO9HK5u200BXQrOp5dkwncbbAv0jKWayeog7Cy7JFtLCr-zmGRTzri_hOTRtXdW8B24oLZkAT6s_vlcxbLunLoh5fyUv4Al0AmswGIbDzvWvfsGloxIQNUABqKgYZLcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOmNH6xZOnVZkb_YPSRRrhCZ1MIYXaiFM__gpX72B_9wxMmaexLVTiDKAiVus_fn_RSNbfB4xbAUxoKKeipepbgQ9WC_Ircp3NokTJ1X_Fg8Dc_Yc9yHdSsZwv5KqtXbpaJWCs_GUmoyTlRDxeYfcVxkMk19wR6V1gQVyGlYQbmseE_VXhf7BeqMiMCXz-EJO4Wji7jAhCfby-9o7Lymjh7z1KxnOu8p7orISYeuWpmW-7wMIN2rh1kqvirRDzfBHVbccV65-yQGgFTfvCg73GVEUR24Z9h8Ld3FmACKAOsF3wVwbBi684dWzmlLRdlcOs8C440lJi9iaKJZ3hsOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfgSN0LnTj-1aRt5oOkFwH_ilP3YdAMuR7ZeaiBPYfZz-wXMjB5037w_Lvg-z47wJb-zEZQuqyf-1urlEq63numKNFbO7-l5r6Sh5qWlHT_dG277dvve2YyK6fG1Ph9eSgQVlYHNGhYaBnnr1CFYhni77mESD8dM2-hAOh7Rc7ohH4g22hKB5zdKbuvyUlKVQhQ1Bvn8yBOr8DbHEprVuAPrGszGWF8vgojW3CGuSVQGu3oDOvqxXOr4a_KykedTP594i1qcN5nhJSdB01Rh1Y-7SeYD3qyJ_Bw2jTUNtkzT8DErBrK0nSkCgSUUsfeuSLwX2A7TnZdSiQc_p_TBXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eillSuDlEwCrhW3Tv-TFbtFa8cR6wrTf1gysgYIRGVbnW07JT14SexXqNexQpTjkRyQp2_9fCwWPDWYAs2j1AJanGqfw-0Aa4C4C-Wz_oU6daXQjzoB6H5DgaAuNRTsr5IuqO6G75YCkaJWTF1_bO2FZjs3RTIBgyzX2xTkojUDdiQ83qgztBn44FNowrcpCfIYuY2AZux-_zhCodhG1d00JMXuPr6EOKGpXBFJ0bTQVkrW1Iyumz_Np4voxLot0HjRzOSBCuGkqEMwetmeg58N4yZsER6WB5l20kg5lOSDlDFbbPjA_hwZFe-3Gk7gteJgaXbDqIsCKChdC79yQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjCb2Lp-Nsahs1HykPXv8kNOyhgixmAymqc4aghs72XJZy8NCfbuqC9rB1Ukcj4u5uGauBN8t6LTgWnE7Vv5EB1CDXgFpT7tl34k2hfECQZrPWnVIRzQuALGOx7uXnxElblwaIT9MNLQ6j8K8LJ1O-RbYlIq6DFpTKifIlZ7fbdeFGQ_kEUW_bbY-VXRy2wOJ7hFM4nJTC6jMCfsDA9lcAMaFkSlPjiz5oL_cfNVGw7lKRm8MJ4ycO6ZIHREfm0qvNKHyarJIzJhRsuGz_wTEISrgSkDual3CZyIpqXp_yrigKuoA4J1XjRfFZyTw5SWgwW6wM23_kr6W2Ezp-fEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY1lBUyMHwp1cgMel6iYSbQPCrbF9a8SreA3wwf2kRNw0hosvxzYld5Fi8qv1hySy7lcw87EIbZ_f36TyD_Mzl8anM3sMniDj84H3NSHqCjKI7rJUS-RuPeErMhcKvElIKkpk7VB1L7L57LZih2R1ky_tNMA_Vx5y7wU2ZoJej5PlJM3DTil_ZnLQT7yyo3zZz_IIpd14iUkHE3O-NqwtFi79MdRNZSzN726-3raBd2-EoWnPgP8ecihC46YdND3Fl_-L9fhra_skCCuFKmT0xgACF35o6Kcakqqw0-r7tro7O8txw9O0iztr8eGPbQNHmZCr-Xfc1A-kzVxviLAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=r8zF0wg6RRsRlJF8BLw4uIJEWaUhDwhVbtzetssnZciEdO0E3t2eEiy4H5d9_XnkGlEC-rPGoHM9d6onpPtsKbOP9xgkwR07kWfcgM19f7D6g2Jz_bPvdgMMJok1-Ale_8fessZpzr5R29cHapbdAbUD688FeDEfDr9RRFGnG7kUmw5n2YoXOkjXine0bTjfDBVMYNDDeGa8hzHZzI9tBn8jyCrHYn8JCMXOgGYtOOSHrYxU4jH466R0J7dZKEsTnE2DXQCa1OdF_VCRlLPTmL0KgrljAcyiQTL0MORC_qIOxUuHrjngJxHYhCEuP8Cin-_Uictx78WPM2jPju9Z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=r8zF0wg6RRsRlJF8BLw4uIJEWaUhDwhVbtzetssnZciEdO0E3t2eEiy4H5d9_XnkGlEC-rPGoHM9d6onpPtsKbOP9xgkwR07kWfcgM19f7D6g2Jz_bPvdgMMJok1-Ale_8fessZpzr5R29cHapbdAbUD688FeDEfDr9RRFGnG7kUmw5n2YoXOkjXine0bTjfDBVMYNDDeGa8hzHZzI9tBn8jyCrHYn8JCMXOgGYtOOSHrYxU4jH466R0J7dZKEsTnE2DXQCa1OdF_VCRlLPTmL0KgrljAcyiQTL0MORC_qIOxUuHrjngJxHYhCEuP8Cin-_Uictx78WPM2jPju9Z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muu9Icdgmi_QKoiKdAN4z9iVooMmOBpWLo7jsVrhw14c71TZI96ikaZJ7y3-Dy2a_eErtfRfIEnvNg2ti5_4azhUJrI3dx1wONNiE1DU5HfcKQCpK_BaHx-k72Z6QZSjw28m6g8rVFeVyi0FsIZmb4fSwWDUCYTDTCSHEfpPX34LH582-swn-6B_hZCbaoWb78kEPKJdA_psEIJ5rreeQVAj9wsGKbj1DQ5aaMOhrF06qLQ-R1o1Y2TQSQ_VktKdFWe1ws0El7DYSksZtksQxaJk0Q0cJuejZSYEcx5_kPkVF-D75UOCaLbrh3c_YLCiBJaPu8dnD8rYIKn2gi_5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=vyxooDU6gvuHYvC919kyTaC1McfsRL3O5Gnvio_2YqkwjeGHQpjqUV3Lq4usyx9YPUWKiLYx7k4tPRu2Rpb0ep_E_73vNatDOhcxvf6NYtx3LvbxQ2I9mGzw-xeTDkMfdmnL-uI56fYsLu4gzUcOmalxdR5PKxrrkr05csU0qqmo8A8UjJqp9ZwqiSi7yE376QMXpF9BgSqCrI5kNpOjaaqyAX_-j6KqFZFCtkDqYY2XwSoKgQXa4J66CNz30x4spxtaojMCBBbo2Q_BDqakrJQeeoUzXjcGTQpgJLi8lIj-0b6ZZsQ5Pt4WkzZcHACrlHDl0CxzqDo_KXVSatvmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=vyxooDU6gvuHYvC919kyTaC1McfsRL3O5Gnvio_2YqkwjeGHQpjqUV3Lq4usyx9YPUWKiLYx7k4tPRu2Rpb0ep_E_73vNatDOhcxvf6NYtx3LvbxQ2I9mGzw-xeTDkMfdmnL-uI56fYsLu4gzUcOmalxdR5PKxrrkr05csU0qqmo8A8UjJqp9ZwqiSi7yE376QMXpF9BgSqCrI5kNpOjaaqyAX_-j6KqFZFCtkDqYY2XwSoKgQXa4J66CNz30x4spxtaojMCBBbo2Q_BDqakrJQeeoUzXjcGTQpgJLi8lIj-0b6ZZsQ5Pt4WkzZcHACrlHDl0CxzqDo_KXVSatvmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Y23OZjXN1O9jrw3tX4sORi7DLg2BSN6ggpTPuOB89CBi9f5doRGRtV8jSsj-phGCn8osNtk1ZyJ7-t-Uk8dmN9H8bLxlADN4qvG9v1xOW4dQUPB4MVQA8sm1_0GnzIBRIOAlBSR0E9Pm3NWvRO5Y92IUl3HBHruNUFhMX4P2lpeiHj0Tfal2_V-UgyY5lDERSSjklEbnEEum9jWNt389y09LmTPGZftz4fAkWbK_2hI5AmHXvsM-X4WcuPKO0c9xVcXTmNZnUPQ6kdZ-_ctPfCDe8Am4vOkKk1BhUqv7Ly_25LvDV-6fitmPMxmQghnp8F7QqkBXI0dwcHnVS_oQoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Y23OZjXN1O9jrw3tX4sORi7DLg2BSN6ggpTPuOB89CBi9f5doRGRtV8jSsj-phGCn8osNtk1ZyJ7-t-Uk8dmN9H8bLxlADN4qvG9v1xOW4dQUPB4MVQA8sm1_0GnzIBRIOAlBSR0E9Pm3NWvRO5Y92IUl3HBHruNUFhMX4P2lpeiHj0Tfal2_V-UgyY5lDERSSjklEbnEEum9jWNt389y09LmTPGZftz4fAkWbK_2hI5AmHXvsM-X4WcuPKO0c9xVcXTmNZnUPQ6kdZ-_ctPfCDe8Am4vOkKk1BhUqv7Ly_25LvDV-6fitmPMxmQghnp8F7QqkBXI0dwcHnVS_oQoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=VUUhXtCSySxvdfth3HQkHGIkbGCGrS0HITF6zIgFhq2Y0-T-7Voujnmtz8_dKneI_xUiBZBXCOGjp_ao2klnftMHorQx7_48Q2j5-5KDshfsKT_8my7gea-U7ewTpyM7RCwu5QdTt4dI5gEM4SolM71g_o8jhch6eEemE662fxtYxrfFhnMLuwXfGde-1iAL5nSHhzmZ8uqyHNArH4QE3-jhEld_3p99gQXzSZwGFJB0JkR1fmFjPdkL9o53rF7z6QwOcl7xhE1ETpZY8AN6ffyZ8Z1Bx1f8lmk1bq54-D6WJhtfOUUujlY9iC1k7nC38_pN6PlzrcbU54jadRxCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=VUUhXtCSySxvdfth3HQkHGIkbGCGrS0HITF6zIgFhq2Y0-T-7Voujnmtz8_dKneI_xUiBZBXCOGjp_ao2klnftMHorQx7_48Q2j5-5KDshfsKT_8my7gea-U7ewTpyM7RCwu5QdTt4dI5gEM4SolM71g_o8jhch6eEemE662fxtYxrfFhnMLuwXfGde-1iAL5nSHhzmZ8uqyHNArH4QE3-jhEld_3p99gQXzSZwGFJB0JkR1fmFjPdkL9o53rF7z6QwOcl7xhE1ETpZY8AN6ffyZ8Z1Bx1f8lmk1bq54-D6WJhtfOUUujlY9iC1k7nC38_pN6PlzrcbU54jadRxCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM9F3JdmovlqksPiQbmaIS2Zp_H5t8NQjn53C9FBPd5rbgqR8HTBZLYpa-b0nx-NMPysye9JEHwiwzxyTQ_z_wQvAi0sH6TI3gXTWe-QBt9xPS8zqA0MJf9bp8TALq-OB7Ft7liXlh2yw9aEIfSN3RdCn9HaQYDOQB-IU2pTI8vZ5nWzXD0aXpja3noYhv0FFLPH4yxqmRW5aMT_j_veIpsLTada2bTK6q7vZRIh_xFYucrQZ-gIrw-KczeuQt_-dWXF6O05UE-uwnrG06Xh9mn3BTCaYyBQnWhuGWJHiVRZwMTEhqTxu6oggrrS6qvzCAOGz-L9mRKcMZ4vdVzcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-JsfrOXVdz7bG_qhXWwFRLnUyPaS3kffWBZFqYRsc6N_YIB6z6esc33_ZWYJroElAN1aDyIqDdP3dzBTToSYysDW235T0hxIeu-fj3sy3nf091vNa8zK3G8-JIiLtvWYLdUAA9ObI2Z9s5Td4krqfHn6_sOshVnqpjVkK7vEJNH1LpA-epAloy89MIlEhQ5trUy7ALX2DtXBJBbJgZIYWzN22tywKuaNzRNjyOLpQIreb4IkAOy9B7HIGaxNNVO5u25VY81PR8WRss5Gq1QCLJE5EIvm1Q32zyxEwkbo2Nltk4pONUWpk88iPIFBogB1W2FrsRDSYixZl6wmiVC1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
