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
<img src="https://cdn4.telesco.pe/file/uh8VAOUqO5UZccEO-9qIfZHYBoTPfMYHN9NcoKX-gFSrGEYth1etg3a9Nldcg90u9Br0I3Suq_SCFeSONIgt7P6_QaVdP0JBKvN_iqjHRaA2Z6Wmo7tBlLAFWzn1F78cifs7UHCD_A74viOZeXKZZIuBxgbulqEhqlW_qpzUgJse9gyfckVmdMRpVSiZ8-7ubVhznpN0apkU7MNX483kRXnV2hbJzTd2sK-6637IA5GOn6wbpCCbGsV47ZzcZ6cZseONfOStlfTabdBdYG-k2J55qM7jw9L9tGtRZhHyKdLKL-ejCdLE-_UHHttJGySuaoE0FbDmHIy8Mp4GO6o_rQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 05:39:11</div>
<hr>

<div class="tg-post" id="msg-460210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d878e5adc1.mp4?token=Hqc1oxFGPhTPdh45iqZaTTdH1ro1a95tpTLEruPmwy8N5GCmXwTnPub5DWYWN3bxiQEOa2fl1fOkpjwlox8s4h19_8DZz2ypD2eS64P7-r2lxjR50RkstMmLvKkqsaJwXKRCldwaDxTvls9tTCPnK_d-f-rYk3zCJMWkLJmGVXfEDxDIikNwIcEYLdos_k9bINRIU0m4g4xNGRKZZVnd3i-3p2WnrwrRO-b-P9ZzpeK1vBLDZhkfPOdmPRS3rYUgsQe7mrF7kgtA5DXtb0Wi4VRf9ffckXyoXGMFjkLxmC7XWggECubk6wPSx6e0KN3zHSLyNPGabJICbdWNQjhSFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d878e5adc1.mp4?token=Hqc1oxFGPhTPdh45iqZaTTdH1ro1a95tpTLEruPmwy8N5GCmXwTnPub5DWYWN3bxiQEOa2fl1fOkpjwlox8s4h19_8DZz2ypD2eS64P7-r2lxjR50RkstMmLvKkqsaJwXKRCldwaDxTvls9tTCPnK_d-f-rYk3zCJMWkLJmGVXfEDxDIikNwIcEYLdos_k9bINRIU0m4g4xNGRKZZVnd3i-3p2WnrwrRO-b-P9ZzpeK1vBLDZhkfPOdmPRS3rYUgsQe7mrF7kgtA5DXtb0Wi4VRf9ffckXyoXGMFjkLxmC7XWggECubk6wPSx6e0KN3zHSLyNPGabJICbdWNQjhSFIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش اخلاقی با اهل خانه عمرت را زیاد می‌کند
🎙
آیت‌الله مجتهدی تهرانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 648 · <a href="https://t.me/farsna/460210" target="_blank">📅 05:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">استفادۀ پنتاگون از دروغ‌سنج برای یافتن عوامل افشای کمبود مهمات
🔹
روزنامۀ نیویورک‌تایمز گزارش داده وزارت جنگ آمریکا تلاش‌های گسترده‌ای را برای یافتن کسانی که اطلاعات مربوط به کاهش ذخائر تسلیحاتی آن کشور را به رسانه‌ها درز داده‌اند آغاز کرده است.
🔹
طبق این گزارش پنتاگون حدود ۵۰ نفر از اعضای ستاد مشترک ارتش را در ارتباط با افشای اطلاعات محرمانه به خبرنگاران، از جمله اطلاعات مربوط به کاهش ذخایر مهمات حیاتی در نتیجۀ جنگ با ایران، تحت آزمایش دروغ‌سنج قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farsna/460209" target="_blank">📅 05:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
لباس سفید، شب سرخ؛ روایتی از حملۀ دشمن آمریکایی به مراسم عروسی در کوهستک سیریک
🔸
مستندی شامل نخستین لحظات جشن تا بیمارستان، وداع با شهدا، تشییع پیکرها و بازتاب این جنایت در رسانه‌های جهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/460208" target="_blank">📅 04:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">یورونیوز پیوستن رسمی اتحادیۀ اروپا به تحریم‌ها علیه ایران را تکذیب کرد
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا اعلام کرده است که اتحادیۀ اروپا رسماً به کارزار واشنگتن برای قطع ارتباط ایران با نظام مالی جهانی پیوسته است.
🔹
با وجود این یورونیوز نوشته بیانیه‌ای که بروکسل در نشست این هفتۀ وزیران دارایی گروه ۲۰ منتشر کرد، در واقع چنین چیزی را نشان نمی‌دهد.
🔹
بیانیۀ کمیسیون اروپا که بسنت به آن استناد کرد از کارزار آمریکا استقبال کرده، اما اتحادیۀ اروپا را رسماً متعهد به پیوستن به آن نمی‌کند.
🔹
اتحادیۀ اروپا اعلام کرده است که «از تلاش‌ها برای اطمینان از توقف فعالیت‌های بی‌ثبات‌کننده ایران و ورود آن به مذاکرات صلح با حسن نیت استقبال می‌کند؛ از جمله از طریق فشارهای اقتصادی بیشتر و عملیات «طرد اقتصادی» تحت رهبری آمریکا» و افزوده است که «به همکاری نزدیک با ایالات متحده و دیگر شرکای گروه ۷ و شرکای بین‌المللی ادامه خواهد داد».
🔹
اما در هیچ بخشی از این بیانیه گفته نشده که اتحادیه اروپا، آن‌گونه که بسنت ادعا کرده، به این عملیات پیوسته است.
🔹
بروکسل هیچ تحریم جدیدی اعلام نکرده، با فهرست تحریم‌های آمریکا هماهنگ نشده و تغییری نیز در نظام تحریمی خود ایجاد نکرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/460207" target="_blank">📅 03:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6yrFrNJNA3JT9lrhTnDIEqzLPOcBzVtfXYT38havYZfVl0FJo1_uKL-VvZDqF-HQTOA5z2uSRmTpnmzPkRII-EfhQkqEIMopLLRxMedi_gTkKMHQ4N71rxvH62PdBdwuKUwOhWzf72mfggVaRJMEAPXGpoiP6m7waMG7tnVdzMAxvul3K9qpcpyVuhA2Dzx8DPSsI-IdfrrmvQiOUrM2pR3E85opFEcuhhsTVeSGOpktA1y8l_xvd5TXu5fRGhWPNkKc8eKynG2kpraWWvn-GVTg69yFk5tZDajRtMqIqVtlKMj5LdWOc--eRu5iydk1xTbxeZ8fOzH7pMx0X0IEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی جدید سلطنت‌طلبان چه قابلیتی دارد؟
🔹
سلطنت‌طلبان هر عنصر آمریکایی که عناد و دشمنی بیشتری با مردم ایران داشته باشد را عموی خود می‌نامند و حالا نوبت به «اسکات بسنت» وزیر خزانه‌داری آمریکا شده که محبوب این فرقۀ تروریستی شود.
🔹
این رفتار سلطنت‌طلبان در واقع چیزی فراتر از حمایت از یک سیاستمدار آمریکایی است؛ آنان با برجسته‌سازی و قهرمان‌سازی از چهره‌هایی که مواضع خصمانه علیه ایران دارند، به اقدامات ضدایرانی نوعی وجاهت سیاسی و اجتماعی می‌بخشند و آن را تسهیل می‌کنند.
🔹
وقتی یک جریان سیاسی، تحریم‌کنندۀ ایران را «عمو» می‌نامد و از مواضع ضدایرانی او استقبال می‌کند، عملاً این پیام را مخابره می‌کند که فشار بر مردم ایران اگر در راستای اهداف سیاسی این جریان باشد، نه‌تنها مذموم نیست بلکه شایستۀ حمایت است. حملۀ نظامی و تحریم، ابزارهای آشکار خصومت هستند؛ اما مشروعیت‌بخشی به این ابزارها، لایۀ پنهان‌تری از همان پروژه است که از خود اقدام خصمانه نیز بدتر باشد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/460206" target="_blank">📅 03:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKaziMcuxtuJRgRQs5Utiv1_1605i2bIBimyxgtcML_CoCgn4AUFTiDtTmrpsN0fQIwAPkzXByDoO25XW59BBfjsxZzfF7IotAF_LLOG0W4nijykWKVrpbbnzuDOCllLPLfG9S-1wlvPMj94PlvwIQqok79g2o9cj8FYpSPNn35m-zhwEBeWV_yI8__uk9K7rlcXOz-87hOJvgO8i3gWXsxLIS_o9xXvVMaNqgFe5hdA_Tepf5V3Gb8-eMWe0cWE_5Z4NLt8XTmjPm9dHJsvBzi0-TttfRivvXlJNVLven_h3Bq9u67bPzngNWQ8jvGN5pHjk3cl6Fz6iBXqd7-CfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاشنه آشیل پرسپولیس در نیمه‌های دوم
🔹
پرسپولیس در حالی پنجمین بازی خود در لیگ برتر را پشت سر گذاشته که یکی از نکات نگران‌کننده در عملکرد این تیم، اثرگذاری پایین تعویض‌های مهدی تارتار بوده است.
🔹
این موضوع در آخرین مسابقۀ پرسپولیس مقابل استقلال در دربی ۱۰۷ بیش از هر زمان دیگری به چشم آمد. سرخ‌پوشان در شرایطی که با گل محبی از حریف خود پیش افتاده بودند، در ادامه نتوانستند برتری خود را حفظ کنند و در نهایت با دریافت گل تساوی، به یک امتیاز بسنده کردند.
🔹
در واقع مشکل تعویض‌های پرسپولیس فقط به دربی محدود نمی‌شود. پیش از این نیز در دیدار مقابل تراکتور، تغییرات انجام‌شده از سوی سرمربی سرخ‌ها نتوانست مانع شکست تیم شود و حتی در دقایق پایانی، حضور دانیال ایری به عنوان بازیکن تعویضی با اشتباهی همراه شد که در نهایت به ضرر پرسپولیس تمام شد.
🔹
در مسابقاتی که نتیجه با یک گل یا یک موقعیت تعیین می‌شود، نقش بازیکنان تعویضی و تصمیمات سرمربی روی نیمکت اهمیت ویژه‌ای پیدا می‌کند؛ موضوعی که تاکنون در تیم تارتار چندان امیدوارکننده نبوده است.
🔹
حالا یکی از چالش‌های مهم سرمربی پرسپولیس در ادامۀ فصل، پیدا کردن راهی برای استفاده مؤثرتر از نیمکت خواهد بود. اگر قرار باشد روند فعلی ادامه پیدا کند و تعویض‌ها نتوانند در لحظات حساس به کمک تیم بیایند، این مسئله می‌تواند در هفته‌های آینده به یکی از معضلات جدی پرسپولیس تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/460205" target="_blank">📅 02:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsFnUZVTF9mQJWfPtXW6MDwB9B0XiAIayr8TJgTDjqZepo6f9dFw35NmR9Gpdt1DLwtvmE0lXYrjaQheb9lO-Nrjv-j7ca7iKl0MuJ2JF3Br5BkzP5ySEMabOuXPYgDM95y0TrAfIamgsAnJWGHxfxztbGWeHrUd9H1PxXi8iD6CWEVEfeE3OsW7ATWfp1BQ3XZ1xV7djqMuMNtlHKB3oDWz6y5xOEqDqUIDz7UZQM7bHDnrltQY55eVgQi0_AGFv4HDmXB-JGg9llHH1Uc-j_BreGsO0Jagcn8s7h-Y_S7znbm5O86qlm9R86sI2OojQkQD35YXPmO0ME6XWsx8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زباله‌ها در مسیر تبدیل به سوخت جت
🔹
یک شرکت چینی در حال توسعۀ پروژه‌ای است که می‌تواند سالانه بین ۱۰ تا ۵۰ هزار تن زبالۀ پلاستیکی را به مواد اولیۀ مورد استفاده برای تولید سوخت پایدار هوانوردی تبدیل کند.
🔹
این فرایند با استفاده از «پیرولیز» انجام می‌شود؛ پلاستیک‌ها در شرایط کنترل‌شده حرارتی تجزیه شده و مواد هیدروکربنی حاصل، پس از پالایش و فرآوری، می‌توانند وارد زنجیرۀ تولید سوخت هواپیما شوند.
🔹
این طرح هنوز در مرحلۀ توسعه است، اما در صورت موفقیت می‌تواند راهی تازه برای استفاده مجدد از حجم بزرگی از پلاستیک‌های دورریختنی و تأمین بخشی از مواد اولیۀ سوخت هوانوردی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/460204" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460199">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlndK9QIuqCXOicgc2LQLprMTm_fT_Bdlma655Q5sn02Q6BDTJ4PQUoYKc82ciX72ZHjaI5IW8acnLKvq6GsFV98xQlnp53EWv8IWR2KmT1E96q97cuLnPqKthq-bfRK9us6RfImr8OE8wJna2WmbijDBb-RDpIJAiKv9GAMvNli5UAG0el6-EdJdGI0g-F2dD3fOUddXdsgqyHOfjyWHgpspCcorynkwGbGx7u6N5wCatpE0SnZcZ2QSVZtTf_yfJDgR-tcuafZ3KBr1WEuvNB40IZXWd1X0G6e0BXnzyWMG8tXa9_-1zEUULs4oP8YCtoGwhOEhhgP06EMN7-qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SN9TgahFZ8pmfB-Nzak3Fu61LGP8GUgPNCc6yFg88opq9xZ9deqZ9agrMUOTCoKEgKa6qirXOsoZTROHqCvGbjAoPZrMm1AagNfFB-lJYZ8cX6XEIhi5JR79SphpUyM4NK1kQbyzR7ssNMUM-hpnLKs1RjfbUDYUoDgECJS_60llG6fajc7OeDSvuvOjxVGXTX-W7r_lWVwy20IpZDsnbPBj_5idr7zLTzCjspAW8vOOQUEoEHy9q-hqPromZSd_9-5FwnY_H8fAND07xQb0gX6t9qOcWO0LpgBThp-zBUQR3NLEuMOrIayaWGlUkoPflcklW56haLaJGelkPpsg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kMJXMBbkYvgsdLL9YE3NC2UGSD2deOsbd3jMkac3dSBd82WmxhrVxhL5Z2xgmVSXUGLxf3BAWdX62hdR4uijl03eXxq1t-hp_ib5cJGvlV8UjaGJN5vHz7wtPqhLtrz6POxNoNhy1nQhphROiSnhN6df4nQNe8y4le_wTqlmp3GJBh07c1xS1ieRp6Si83Udvv388PIExqHn3_ahSISfvgFES3xBh76v2IzqdORBAtqYLyIB5vR1gD6SLTHPaJE6op6NNhzuTI21rXW2Gu6TwyOdXseDnAZon315R5ZLaMmr_OtqUPzpIeBk_WlPaf2j20Z0iMkOezGXbSs3qlkFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0X7a4Q3yK1kWSYvzvUscEUajr7-nuuyfDGWr35wJHknR8VLQCcbthoFy0nAwJ5xuBHtLsSNNwFh1n-6KGVqR4788eJell-xKUr9tqV4ILpzm6DgUA5U0o0qUe3sxsMxbA0FAtQ-QT9tYPx6T--s7Rjk7d46KN5M09hPEQ1pGVtsreyQ7zQFud2Pr7dVW9SbBMh06iwkgk4TCYiKySaBF_Hli3G6-rQ259naqAz2qPHSR_HYq8QzidK-FYlnvUnb0ACCsn9MYVCU4MuwUl8EgazvqypD0rEp7rx0dbgh-dI8u2-4BbSvLND6Vq0G3qBux822L2gKnCncp5x2EupMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIy65l0vmfrxaFI_0eyr908P9jSSkoP95__VxYoWAIG4P1WANFyQQ8esZNt3UaP0YKt4ySi54PCyEHNkQYYcxtze9S6LmvQyr8qt_DW3iHlqQd99MISzRERu2pypl7yXb4GI4W643bocTyHooKVW_ERBnqnt0hkk6OceJvcf_caEoO2wVcYhtQh5Ey-gXGwfc3HS4GMPsjGQS0Sz11PeBL8-4SzfqajEztwgrJUBcXE3PstEyzw3N5dfsajkn7rNjbnRKc3l5yn_s_dBYg47llmVBel8y_YlSANUTY8T7leO6vWtFimtL34A1Cm0S05sO2qq-Hq-id7B8wcqvRnNqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۴ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/460199" target="_blank">📅 02:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460189">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfdUBZTCGEGdeQP7NrLDvm2WDGGkjAWFA7BkiG8iORVCCWnCH5hp7YjN0dks2yGMOzruzk975c8-KLYdTzL_R9wqC5S4hnKVm04qqHOpfguSDcFsfIvkC1KaZ5CHUAEcHDVMhZGb8f1PoVimtEnRMOi4bIA-61jHjk9tB8_e5FWq9_CsBQ_bV7Lky8EUZBmW2KVBNr83sOUoa68X5SYPZqXyT91XY0h0IWPEFHnZA4xMNPJE6SjZKKdqWSStnYJ3uIGfCqoUT6-s0EywacnLghe-qwqJ5gu8lxEyPlYJINP7H89-ScYZVtoH8h7MVgjuqP8dNjFDddZKL-cR5jvLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmiCfNFABjKZ49sA6NO9ajhScCb7vEGJx6UifTKTn-LfJ4BKHCDYxUM7X8k2guxLI3PnnDKW66uxgCglPjzsPlFB79ZeR5QeE99sQP6MFNVtc8HS0rIZ0_xjKTNpVrv9JXCxTMiiBm4kQ_SqSN3ZiK_dsc1aXv4RmFolmkqPyDICsHRlP-RBEvB_2p7Q4NYYntmhRcR7NcF3KJDw9WgNv2BDrThpuw_cvNiogLtLZ0am9k6zA70pxhDWfe82jhbf3pDydIzd3gkhOhoUGhdeZGJfsRi0BEwmjU1bJA57j26sdK3mrlS7Husc4qLjflaWOG1jwhwNzddFCg8FMk44uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBRPi3jX5oHTwF8n8mL6fXJBYUf62JOrNMXiNbTPcwriHdQKhSIloBC1moq4EiML6dFTwHXB0Y1zercL15thmrQNh2Dp07saa9NeQfH7_NN6EqfdmSWO7NC48QIOiNUeZjPKpxvbSIrdiJx-CaU3Zk_nZAxowh71z2srcVUGq6KxW6wFIXrkvAHLeh4YIugGBe1pdAVD_VPTQpZUt0OU8w5X3xYQlBpsMwRLXw02o_UpzXn3MHov3k4SYRMSyzbaAY5CVNyDDsKPpW4EdHBUahQg3FyLnihvRrpBdEhAEKXGO_3mH6dmDorvylyNy-p89NsHqYcdc84OQq9pm2ChmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7OFpz_pkdwDyEPdeMsGNpWV99AYAlVXgkb8PE2sr335WTJQXPwXtjrqlCn1iGuHo3f5-v40SthxvaIMvltxv2HRpkcq2fwtMd71gqug3s-VQeUqdVtCyY8Y41udNBuwDiWSLUjwqRsVhtN-IzEi5-psndSrRpt5--dqiDrrrFy2JVqNOAxgT453SANdB85x74rQzWjXtTztVvhKKPP2NlT7DFYPM0UBUnF7F8cK5sobdCT7-UJpg1FUChL2mxX9QKfiOtviu6HU_BiwNkz4mQUy6CLRXj9naVPZ0NqdCqRCPNzSbPUxqSOtCCz1FAymynMzZV-9ZrgBM80KZgi8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYQBeCtCriw35rMqfrbjh3XU_2z__ND9kKgT23pcRh96De-zg8gc4qiRj0NapZ05g1fNeiQI4UHSyvst0SzxlbXwJQ3IDRpAHkLFmbgGLZl9tcEXheOlH4lJVCM2US2Lkn3H9VXjsKtleX-cqcnKedXcF2n6SINNDfbKxh8tTzN_9wgJw4vG8Ov5oxdYXHRT_gjyyOS17a01CeID1WmXA7b-eLY9-IJpTtVbmZZdVGsIGS75aiWCRacYoftwpCrsg36c-YUlZKA9PAwab-90CJLWxev69-u0W0aELcZRdnupSyNjZvpuiJkD9SWCwIClpLLHCB3NVu7VJ3gxXBDKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1PDPumZh66SsyEoykEEUnvcHoFr9vGEz7937hfZu1G_fQFyq2cSPq5iD4mGUuKkMN7Cs6DiYcyOR2OHRV4w437GkiAC5cgW0pq4Xt4V5A6t2-f85-Ce5rOP3HF9g_LUtnGkKlNJ7iXQBY0sS0QceO4tt6JTc-CQaux2IYFkub2G-LbPVxnGho--w-vaU2L-Nd7xi2NF1qmMVt8d023_g9QCmhPTwkKZRBTj-_qfFXHRNqtvTbLcG1fEoXjeq3j1KAZum6gVZ7u-4jekkarhMiSd53mipCnviZG7egeJF_geT6_1JsgYhHqqly3EoiT-F7LlS8don-p12NOcQ0gOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDW1sSZpA3LUIfyZYcO1iilH28ymfDORQPRd6OfUqT-YMNQU-DOX1IzqE8_PPbN1VViykQAtYNtgc1kcT4BZB_liu5ioHncFbxzyTw-GxC_648hX577qEka9RBPwQ9agHCdbfWS91WZQiwoCSBBrvrs2ZVu63rZi0t2sDnpcy4dkMpCoLI8mxKbuJGvIqvOt0F7V2vpjmFl5CLUtFsal9JaBofAd0uGL6qyz87wF9fmzwZtoUQeqhVpskxlgm72ZWl2Pl6XjsDgXz649Cfpnn2DUsQctnp_0fEYseccQZVwVNdAKNswhBslKqX3REjlJv6_--ce-7Vdeaq8GQdrMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XArIKC9FyJ03t1VU2FcYUZ2k9_x2O01i6GXVefzmgp2P9dmeNzSclzko-7vVs5uIe8rlY7lRXQKv8lCyibSU6gmneCT16o0Ng30BhpqM9ls_GpEEwlXIUf13yMsIyxnYS1Xr30YowTsnNT0TiYmVzjZMquDrdF3vcI-AE4tToIktYejqAgwYY-kMCaD2bRNlQNZufoIN9HtG7-BUKtxRoS3iSVoeEU8yRNNn9Kg-r-981QdemA-WPqCCpKTXx_e-neLtmhpYagvioJ7eQiy6Nl09W3aUNd19wC6wifQfGd9Di46VsvXvTWDVvZXGXrc4-S3OlJ4_JepvFsDI501O1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3DqmU6x18HYuBczpe2VPNcrTZFmTrczPCm4aofthvzBCqDkg13AaUt1KrHCtYOUPYNFr4Ih6jk58Vw3L-EXopbsFneA9V3uiQg2z8rbKqOrt5GOrxQ7aI9fuEHmCT1HSpS5892WX9ywkLjvqj4qXAfXgWO_kox-b97BF_l9d38TJoutiDfMnNLN3wGwHz6LK3_6NfCQ-1BsPeqo9Pc6FzHK6SY5_1Zxejm6Lcz-owsgFIS-pTJwTCa9lux_BdvF234D_G1jjlt6DjRnfeau23qFEe_2Gfy-a7QUyak4bn_wwyW8zdVBobXQglH8lG8dqui_c1Yk94wt-4wh6BRBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0i-yFzxcq5AJOF3IR1_Nj9Rxr95_j-yiZv-R-3CFqL0IHYrucJp-073mf-0kpsiKdrsQKfv-qpdBYC_YrofWYMwC8tgVTR_Xw8psre4lkMYNpbVsKGY6Uz6f_XDkhCnfHRoAhTCq5LMJyzgCNsIYsMRTrHveSWLk4rkyfo-w93cJ9BrlyBKXGMYCdgf1PsKZ8LdIcTSD-j4tbrAKR6BnrYZ0R_yvMAln-PRn_PkQMaWUXn4c-DBtnqJtmJqf-eAVQHhp7X0YFoY4ckBboitIwqCI2EwzyOFfse8Px6TOKPP_ybiZu_18T_9hASws_SgBLCPPrug02m7WWO8OQeAjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/460189" target="_blank">📅 02:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460188">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیش‌بینی وال‌استریت‌ژورنال از شکست پروژۀ جدید تحریم‌های آمریکا
🔹
هفتۀ گذشته، دولت ترامپ آنچه را «روز D اقتصادی» نامید، با هدف وادار کردن ایران به بازگشایی تنگه هرمز آغاز کرد.
🔹
روزنامۀ وال‌استریت‌ژورنال نوشت تجربۀ اعمال تحریم‌ها و فشارهای اقتصادی غرب علیه کشورهایی مانند کوبا، کرۀشمالی، ونزوئلا و سوریه نشان می‌دهد واشنگتن برای وادار کردن تهران به پذیرش خواسته‌هایش با چالش‌های بزرگی روبه‌رو خواهد بود.
🔹
این روزنامه در ادامه نیز نوشت، تهران که کارزار آمریکا را «تروریسم اقتصادی» نامیده، دهه‌ها تجربۀ مقابله با تحریم‌ها را در اختیار دارد.
🔸
طبق این گزارش، تجارت ایران با کشورهایی که با آن مرز زمینی دارند افزایش یافته است. ایران همچنین یک نظام مالی موازی کامل با چین ایجاد کرده که سیستم بانکی تحت رهبری آمریکا را دور می‌زند و توان واشنگتن برای اعمال و اجرای تحریم‌ها را کاهش می‌دهد.
🔹
جاواد صالحی‌اصفهانی، اقتصاددان دانشگاه ویرجینیا نیز گفت، اینکه آمریکا می‌تواند درد و فشار ایجاد کند، یک واقعیت مسلم است. اما احساس من این است که این فشارها باعث نخواهند شد دولت ایران برای سازش تحت فشار بیشتری قرار بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/460188" target="_blank">📅 01:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460187">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQvwQCaYAy9Ficp_-37D5bdmN8JUsb6wwAOkOgaunRqi-CwsiP7u4MNxyUERlL_Lrj699LvxkhHgJaXd8QyHiQWEwfnHOUm5gA40NCZ-cjxhXBkF0jY7_cqHANTKvSVH7PwnmOkMDBRrnpQySlI8ivUwa8gdSCOQASZkkLpC5aHxqxjcspmYTNHeOSIVw4MXOi9t9LN7K8M02E2GNzX4VpAkqIKpYJHb-UeRR9BfBu07zbSoUEonZz4a7aqqKPIoYJpipLmzgTyMiyQkyzn7-DEUPNLKn_SAA_PlRJC5XLgTqERGlmF9dSBKOSKEv5beyEEJsBtvXdwJ2DXzU9Kxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ایران به کرۀ‌جنوبی: اعتبار خود را فدای آمریکا نکنید
🔹
المیادین به‌نقل از یک مسئول بلندپایۀ امنیتی-سیاسی ایران گزارش داد که کرۀجنوبی نباید منافع و اعتبار خود را فدای سیاست‌های تجاوزکارانۀ آمریکا کند.
🔹
این مقام که اشاره‌ای به نامش نشده است، گفت: به کرۀجنوبی هشدار می‌دهیم که تهران هرگونه مشارکت این کشور علیه ایران در تنگۀ هرمز را به منزلۀ مشارکت نظامی در جنگ تلقی خواهد کرد.
🔸
دفتر ریاست جمهوری کرۀجنوبی روز گذشته در واکنش به فشارهای ترامپ بر این کشور برای مشارکت در جنگ علیه ایران گفته بود هنوز تصمیمی در این‌باره نگرفته، اما شاید «یگان‌های جستجو و نجات» به تنگۀ هرمز اعزام کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/460187" target="_blank">📅 01:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460186">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۳ شهید و ۲۳ مجروح در حملات دیشب اسرائیل به جنوب و شرق لبنان
🔹
وزارت بهداشت لبنان: در پی حملات هوایی دیشب ارتش رژیم صهیونیستی به مناطق جنوبی و شرقی لبنان، طبق آمار اولیه ۳ نفر شهید و ۲۳ تن دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/460186" target="_blank">📅 01:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460185">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0646001051.mp4?token=iy-AGqCrvRRzoLkA0rfN3UCOqmWPPSCzrAWJVDBL7eo_5u_uAUM55RzF4_oJ5RXuhOz0YRzXQ6hXYZiP_ivLV9uJIWzYsOogTIXHEVuVFcKdObImIPGcnQ8pj_cQEtkTfyz6TItbrEMkeSAnc2aPKal6xcLy8BGEptcCCb1nvhgk0C3_jQclZJ1x48O2B_W2dCwx9AEKAHdyEB7Btdf9TdWbJSTjSPHaqJVw_Gx6OetDm0JrXJXXoeoRxmdOS-MRXF8Ap2kZYdEfJjnOKMf6YeNr5CSq8s-437xpQunjDu8eARQkvfkR6KsZtm94gQDJ7hg0nklVePVCTznROpQZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0646001051.mp4?token=iy-AGqCrvRRzoLkA0rfN3UCOqmWPPSCzrAWJVDBL7eo_5u_uAUM55RzF4_oJ5RXuhOz0YRzXQ6hXYZiP_ivLV9uJIWzYsOogTIXHEVuVFcKdObImIPGcnQ8pj_cQEtkTfyz6TItbrEMkeSAnc2aPKal6xcLy8BGEptcCCb1nvhgk0C3_jQclZJ1x48O2B_W2dCwx9AEKAHdyEB7Btdf9TdWbJSTjSPHaqJVw_Gx6OetDm0JrXJXXoeoRxmdOS-MRXF8Ap2kZYdEfJjnOKMf6YeNr5CSq8s-437xpQunjDu8eARQkvfkR6KsZtm94gQDJ7hg0nklVePVCTznROpQZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پسرِ شهید به آغوش پدر جانبازش برگشت
🔹
در پی حملۀ دشمن آمریکایی به جزیرۀ لاوان، شهید دهه نودی «مهدی بحرانی» به شهادت رسید و پدرش نیز مجروح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460185" target="_blank">📅 00:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460184">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofAmOzagg2l4fxGf9sWA7Dpm-RWWd1foTbHRzHpB_og43cwHNkVFKouYHHHbfw-3SI3th9AZCreZSnKLrCiCNyJ5g46SE3LvafLVG0QKoHti51f1wm9Ric9cJhf28dW2sMoirglHK82cizWgMlbCdgpuBuATStWIMWv_aoFy71y4tXlfv7enZLMtvDYUSydv_0TgHJzIdH3VqVSgMst-0zXddQ1lgAPyiRJ1vEhIOJfNIYKBqvvV1Q1eBMPSduOH4wauKpOVJjge2MNmQNvZ6qCB8P_BigFRalnNc6-cs_4qD3iEAeJeNDvgnKYV7T6div4D6NWsTcje2HeaYHGZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون از ترس ایران ردیاب‌های تبلیغاتی دستگاه‌های نظامیان را غیرفعال کرد
🔹
پنتاگون در بحبوحۀ نگرانی‌ها از حملات تلافی‌جویانۀ ایران، ردیاب‌های تبلیغاتی تلفن‌ها و رایانه‌های نیروهای آمریکایی را غیرفعال کرده است.
🔹
بر اساس گزارش‌های منتشر شده، شاخه‌های مختلف ارتش آمریکا شناسه‌های تبلیغاتی دستگاه‌های الکترونیکی را غیرفعال کرده‌اند، زیرا نگران هستند داده‌های مربوط به موقعیت مکانی بتواند محل استقرار نیروهای آمریکایی را در اختیار ایران قرار دهد.
🔹
پنتاگون همچنین از نیروهای نظامی آمریکا در غرب آسیا خواسته است استفاده از خدمات موقعیت‌یابی جغرافیایی را در تلفن‌های شخصی و دستگاه‌های دولتی، فوراً متوقف کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460184" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460183">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXIHHdx0-GsoD6CosMyqnxuIFBS6wgJKjHtGqPjQNoaSH4845YQSxXER7yDpfMowXyAn3eO8Q62Z-WD8uqK74gINJIRmMoSZ95idZxoJkwSpnYENphSSR6Bq-aEyt16tvPvsqHrn8htnEpzaaM1yyRkY3SDlIAM7JNNAw6C9vBLnbfYGbckBBrLXZJlUyPOC3vDhoPVYGYEL4BHDYscwgcz3Eh3XVg51YWtRnILV5vX7yZYl0qk33JmbNx2JX5y6dDgROSNs1hFXQWFrfqufigi3-qxQc35nu9crTC5db_WCrrL4CT6BQI0wjJIyoAa968j4CDMaHNvDOXXmnoMi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی به مردم آمریکا: نگذارید اسرائیل هزینۀ جنگ‌هایش را با جان و مالیات شما بپردازد
🔹
سخنگوی وزارت خارجه با اشاره به مقاله یکی از رسانه‌های اسرائیلی که در آن پیشنهاد شده از دانشجویان بدهکار بانکی برای سربازگیری جهت جنگ علیه ایران استفاده شود، نوشت: آمریکایی‌ها، لطفا فقط یک سؤال از خودتان بپرسید: چرا باید به پسران و دختران شما وعدۀ بخشودگی بدهی بانکی داده شود تا در ازای آن در جنگی بجنگند و کشته شوند که اسرائیل خواهان تداوم و گسترش آن است؟
🔹
اورشلیم پست آشکارا دقیقاً درباره همین ابتکار بحث کرده است: استفاده از بدهی وام‌های دانشجویی و کارت‌های اعتباری جهت سربازگیری از بین آمریکایی‌های بدهکار برای اعزام آنها به جبهه جنگ با ایران!
🔹
این، یعنی جنگ دیگران با استفاده ابزاری از جان و مالیات شما!
🔹
اجازه ندهید شما را به پیاده‌نظام جبهه جنگ و پرداخت‌کننده صورت‌حساب هزینه‌های آن تبدیل کنند؛ همان جنگی که هرگز انتخاب شما نبوده است.
🔹
اجازه ندهید فرزندان شما را به مزدوران جنگ غیرقانونی‌شان تبدیل کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460183" target="_blank">📅 00:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460182">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8ac924a6.mp4?token=Spo7-sz4Pbdvkzj6CwESCwF4erg3F25aTT_Z6u80uXJFQnVx9T6i5CbU3ZIlOuz-l7rju7jVyDKuNhGWbmbsfESUwxn6bkc9dgwSc2zfLIK7oTRLWaQFKQlil5Qs2lg1eV3Zyotlj2VYyYq8JjtDRpfKuY0kt85EgY3UROmFk87oIrZ6apDhlML7IwH5ddajOHlWx0FzSKsh-88FRw3q1XkxKq_3JXGPSkgAVgGpmQSIeoX5ijocSjvcQcJBYqWg06oIZDTPgpMSpt3GikuGNRYNgVz4x52xvvQ_dBwPJuIE5oBZd6GXbeFqQRW78957dQqnj6C1A_eaf4zfEpm4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8ac924a6.mp4?token=Spo7-sz4Pbdvkzj6CwESCwF4erg3F25aTT_Z6u80uXJFQnVx9T6i5CbU3ZIlOuz-l7rju7jVyDKuNhGWbmbsfESUwxn6bkc9dgwSc2zfLIK7oTRLWaQFKQlil5Qs2lg1eV3Zyotlj2VYyYq8JjtDRpfKuY0kt85EgY3UROmFk87oIrZ6apDhlML7IwH5ddajOHlWx0FzSKsh-88FRw3q1XkxKq_3JXGPSkgAVgGpmQSIeoX5ijocSjvcQcJBYqWg06oIZDTPgpMSpt3GikuGNRYNgVz4x52xvvQ_dBwPJuIE5oBZd6GXbeFqQRW78957dQqnj6C1A_eaf4zfEpm4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان ارومیه امشب با حضور مردم نورباران بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/460182" target="_blank">📅 00:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460181">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da596b0154.mp4?token=D0hsqXoD5-XUWWTjmZSTprqW-HVedW-oEhw22lk3NehoydNwwQv_jwAp61Q6Z2vpUxcxqyMAiiNrk7oi6JuZpokcubMqm2AjiUUe5WQe6uNix3YDVeH2kppTpdJdbEFzkdaLZC8GlWTljJq3UZCZoAfDq9yurhBb8A-hZ8mhcKnjgYvoUfQb5D9a3yYoi2baERRst_Dr-p1HAiAgAGnD6bijgMznRyes0bgklz4mTvPZUTrNyOo5m0nom-DODARWu5Yp8lpbs_9PfG-qb6FOEECwhsq149xbJ1ooMvZ7Ief5SV1go7OisBVXD7dy66YKCFIj0zer337xLBRLl-xePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da596b0154.mp4?token=D0hsqXoD5-XUWWTjmZSTprqW-HVedW-oEhw22lk3NehoydNwwQv_jwAp61Q6Z2vpUxcxqyMAiiNrk7oi6JuZpokcubMqm2AjiUUe5WQe6uNix3YDVeH2kppTpdJdbEFzkdaLZC8GlWTljJq3UZCZoAfDq9yurhBb8A-hZ8mhcKnjgYvoUfQb5D9a3yYoi2baERRst_Dr-p1HAiAgAGnD6bijgMznRyes0bgklz4mTvPZUTrNyOo5m0nom-DODARWu5Yp8lpbs_9PfG-qb6FOEECwhsq149xbJ1ooMvZ7Ief5SV1go7OisBVXD7dy66YKCFIj0zer337xLBRLl-xePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع مردم بهمئی با پیکر تکاور شهید در زادگاهش
🔹
ناوسروان سید مالک موسوی‌تبار در جریان حملۀ اخیر دشمن آمریکایی، در حین انجام وظیفه در خوزستان به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460181" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460180">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOWsu4C-3RoGaz3j1UO3LbC06JZOwLT7p4ufFz6DJAhkjsrGqjwrHeHQ6fc0hVC8nf5hrnnPfzP_f5mv6KnwAu3xBcOVV7LHb1O0J5lQMueWeGRAktRoC-zgMiz83IcHttJSUTgU6MCRFLKhmCNUTa2unBNV5K_pvN5cj0jjvSvVMHPfyL2iRdPlU66TLADIK7-LxjNB_b_MARdN1FdhidDPIo-oZV3A2KHMpljcVbujrxdgv-r0rqoj_UUEe_c7-G3ifuajyJjBZYFHHh4Jo9Kmd6Zf6tUCzR1odwoEBfuWOtzSDFWpsSDud5ErSAr-lKNvc5JWA9HUoFaFLRepMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوخو۳۵ با این سامانه جنگنده‌های رادارگریز را پیدا می‌کند
🔹
جنگنده‌های پنهانکار نسل پنجم به‌گونه‌ای طراحی شده‌اند که امواج راداری را بازتاب ندهند، اما نقطه ضعف آن‌ها حرارت تولیدی موتور و اصطکاک بدنه با هوا است.
🔹
سوخو۳۵ برای غلبه بر این چالش، به سامانه الکترواپتیکال و جستجوگر فروسرخ پیشرفته OLS-35 مجهز شده که بدون انتشار کوچک‌ترین سیگنال راداری و کاملاً غیرفعال، امضای حرارتی اهداف هوایی را شکار می‌کند.
🔹
این سامانه با بهره‌گیری از حسگرهای حرارتی با تفکیک‌پذیری بالا، پرتوهای فروسرخ ساطع‌شده از جنگنده‌های رادارگریز را از فاصله ده‌ها کیلومتری شناسایی و قفل می‌کند. مسافت‌یاب و نشان‌گذار لیزری OLS-35 نیز قادر است تا فاصله ۲۰ کیلومتری، اطلاعات دقیق مسافت و مختصات هدف را برای سامانه‌های هدایت سلاح و کامپیوتر کنترل آتش سوخو فراهم کند.
🔹
ترکیب ردیابی حرارتی OLS-35 با رادار قدرتمند اربیس-E به سوخو-۳۵ اجازه می‌دهد تا در محیط‌های آلوده به جنگ الکترونیک، حتی مخفی‌کارترین پرنده‌ها را کشف و رهگیری کند، بی‌آنکه خلبان دشمن متوجه رهگیری خود شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460180" target="_blank">📅 23:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeGGQjxbj7q7k2BtOtLuMmUCgtuQgf2NAN5j6KoB33mV11iWxWJhXh_sEe3Tpov22_DWq3fTOTlAgAgbjAznd639-SNKOO7p8HrEV_gMdgiffdXZe7KRSntBScWGMui59-p-bJ6w-jWIzYOkLwPgXmVZisCbU4Q37Cp12i3VxMVEiy0r9nkGgUlpopvca9IuEIirIKk-qxX34ileFXpkpRpy_mRRIKDPflt4pYJj8Lp_-VT2TNeoS3UnzcZLx5fbSyOCKEJRbD6evFHWQ335vYlhXWLP74tGQbAY7E46UGuKNIcBkT0IwiBCBdE6sRE_BbllDx2mpA3DiDQFBXGYgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBtXR4XRowtAdxomCEU6ZHDrLP33OB2qqZhjcEuSki9BL0h0NPyhpAjYnLM2q9WJ3QatPY9LjP8ckHSB5zwF0FRfBgmjrGhLxqVzOVx28ZUwj3Xcaw3DAUh54bxKSw37KzALtutF-zdKKA8xHo9ur-lOvEFLuaNn4kKrk4eQ8niWJIlI6FRI2ju7abC_YehQ6XKhDZebe4rGNRq4j-fOSTT3qiXsrJmHiglDwC0wQVkb3mhEuCM6KqVmO1KLsfPQX9i8U5h3NZCf52MKnCik2Cc3BR_nR_YByjK_O2MTsBu-Tpt0PjI9aawOYCNfhy7ZLGyJ2NTBziUIS8KHGrEALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p75BpUipD32fSbmghevFKWBdCak78KgiPcBdpiZqTdEI5rtghv-1BsplOc7filzrAr8nMrrE9ay-15PMVjQvcMau1QZu7IwPcAQ5aBMuM5ZIvChzbjzdT1T14vBkK7AuFAz4atQrL-yyn_GqN8PHRKkWsj1fS4po6cSOrTlg-61pzOaOzG0jiNnMLnG1Af0rIinfINDUhqw6UPc2v3z5kG4syctQOAAIevMKswcz1bY-XiHHrMkvYOs-lB7b9aKXbTGe6l5ovPeOI0Kp41dRlRzpiUX43E9wO_hSsxXZ6MXbyyQpxyit8eWHCN_ENMb9wpoBq_FxOptZ2V5U7lR78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DReTNqbOLofCNduqim090c4ZhGJywIUjL7PvlMei7Cg5GtiCh5zQDUbUO_RzR6QlNdbSr4xaN5bTDo5auAELzhQYX7NrEZzmses5IZy_2M47KuTZSSsEQzVRHUW4VCyVfiI1IDTb3lg2vJ0sxkhgvyJXXVIwwwAvsoP54uxdcnGUXz_5PShedNLiJLGf3mMTjtM2xWDA7lnEQQ5dFhyuuXBheQ1xrr6kWXiOxLTzGmTHU05VWTYGd7buE8l6WmtNzSl090gyab1jc01SusEU9fRNYDygczrgi8P7o5Yd3fLOWmEq_X1JjyGK07PcQDubU2gzLuj8QnZYNDVlW8AcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pz1ubGIA96Lh4IxUVDGHQbw1XCMFALLisE9nxZdc1gJzNsS_qaKqCj-oeO337kr5aJdD9aG15JUF-u7v35u31eAiHAbkLKWyxIKh6lwQbB-iCLDyo_mYEjfQuhU2ujesrQPRdgeELTnBZV6YM1rQ9SInMMBIW6sK24_itlEhBeQ4l8cwB-ViyIXW18XVNASpWTAPKOYHf4EDEYdfscjbFwSkcMHL9Hmd4w5ZeTpR0u1TOt9w1_-f55BW4VbeFk7yFftseqbLgSCR3yAdiEEKWuiMXWaIfpvYzoFXn7aqg2K2LNYNjIZDv44qAmlVs_p2_rcH__QJzmIzFvGm78neWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORhog7bsdvf_uHpeaUBMrS3iw3yuVBdxePxrB10SD60HvBZ3LXwXLG8ymvB2uubprYVXJBbCFoCWgb2nuxNsANnz-qSs_GwD13_FEWMVVaLwUD-G28FRI7IVlInRia-iJkx5E51NLNNR-O64VG-ebJFS9RKUR63Uc02gwY7n3JrbZuzObW4ErLSTP05EsWngG_haKzlh-05oRk2DlJNBVXj0aMZ6ksklk74q99bzrI8XJd5oAjHLDemOfA6Zf3e8B2oxFGh23zmMT7P6wA26chfvF5gX4NeWIMWijqrDZ7dnHn6BQ0bqtBT7IOdBIcFN2zlDQdgfBsTMQhJGIdvfGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRaYu86UpeZ9PHvjUI_kBHnc92eZ2U3SiS3OMdaMN82TFcMUgGQGOo8QLVdZvQaNipUJ4u3J4-cuPJxfD9s9H1okDxk9F9rPJ6nnQhQmESqUgcNdWnoRUPsiMDHaPCTiO33i0jevaLsuqSTIVkBOqpp8FUra5zbpjIMkoKPt4jv9EGb23GJnr-kDYOGUC28tZilX1ztNAIIbsHX60tSjks25CZPh8gSQY8F5yeM-oB3EfoYM17s0yhrvSb4cfn2ec4h0PG1-5KcK0b5eQU3TQGM7SO9WaqYkoLnXsAkJkYR1daNpETz9GbkYIDLZ7cmF3YJFBnx64RqtMMwJ1yofOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع ۲ شهید حملۀ اخیر ارتش تروریستی آمریکا در کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/460173" target="_blank">📅 23:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93759ae0e3.mp4?token=BDiFr2rTcfoH5WVz4escVSYWRkQ6qs-T2FlfDNrLSn-U5fnxgg7bFysfQF6Lh_bwqPzv_Nh2gJzha508d0lSXx64kYJbbHwD0KCh5w6z5SaHAk_xVNeAYOu7cChomosYMyDvECpJTcJyqHgTa63yB4BPwMvWKxTJfz2RYo8nMzMr_6iVu4m-w16B03scJ5iRsXI_7iYlazPcyyTT6nsA23AzM8j_IrDK4c_HIGuo3qCJp33BJnmlPqLu6oqgzD4IsoI-x81BCK0CCmhaeHWilCoTlaQl_N8yDvqBWbia6GOBHpwH93HkT3NSt6c1fS9nlRKglU3Jhevu-aBXdDbicQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93759ae0e3.mp4?token=BDiFr2rTcfoH5WVz4escVSYWRkQ6qs-T2FlfDNrLSn-U5fnxgg7bFysfQF6Lh_bwqPzv_Nh2gJzha508d0lSXx64kYJbbHwD0KCh5w6z5SaHAk_xVNeAYOu7cChomosYMyDvECpJTcJyqHgTa63yB4BPwMvWKxTJfz2RYo8nMzMr_6iVu4m-w16B03scJ5iRsXI_7iYlazPcyyTT6nsA23AzM8j_IrDK4c_HIGuo3qCJp33BJnmlPqLu6oqgzD4IsoI-x81BCK0CCmhaeHWilCoTlaQl_N8yDvqBWbia6GOBHpwH93HkT3NSt6c1fS9nlRKglU3Jhevu-aBXdDbicQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور امشب مردم کاشمر رنگ‌وبوی مهدوی(عج) داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460172" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd179be9d.mp4?token=fb9to_RcM6GSpL5B5uxwAFlh1M_4mo7qzJUrWHneaOhspBBUenRelcxmLqlWcvj849BNi33RPZt4JLGZ1mK4F2iXEbf9ZHxShrVdXYSp_IIbjOD64Tr8fwVtb70sMp-l7xjWGDjrEKD0QdYr2CsLdvUzk1YVO7Gw-mnx4dwuaVZaCp3MhqpII1CY5mtb_jiDIkHv6n4qyRbCXNbj2q1S28MqfzpRRsDXtcCBbfUfBr5rh-UMNQPzHul9z27IBMFHBh3LoxirbwpqMTZ4uC_IX7nFrNvziuu69VolnIRgEN5ATfMmVCJekhTJrhSWcD1w_hcHfHRmIj6lTe8RZX-hiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd179be9d.mp4?token=fb9to_RcM6GSpL5B5uxwAFlh1M_4mo7qzJUrWHneaOhspBBUenRelcxmLqlWcvj849BNi33RPZt4JLGZ1mK4F2iXEbf9ZHxShrVdXYSp_IIbjOD64Tr8fwVtb70sMp-l7xjWGDjrEKD0QdYr2CsLdvUzk1YVO7Gw-mnx4dwuaVZaCp3MhqpII1CY5mtb_jiDIkHv6n4qyRbCXNbj2q1S28MqfzpRRsDXtcCBbfUfBr5rh-UMNQPzHul9z27IBMFHBh3LoxirbwpqMTZ4uC_IX7nFrNvziuu69VolnIRgEN5ATfMmVCJekhTJrhSWcD1w_hcHfHRmIj6lTe8RZX-hiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«حضور ما نقطه‌زنه، تودهنی به دشمنه» شعار امشب مردم کرمان بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460171" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
منابع لبنانی: ارتش اشغالگر صهیونیست به نقاطی در حومۀ شهر النبطیه و بقاع غربی در جنوب لبنان حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/460170" target="_blank">📅 23:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f799ea13.mp4?token=PtD-1Ieit6pShFV5FqbrZi-ys2D3ZSF45S2c1Fq0G8kuzxUPGIMC6IuOS8LKMOO10L7TAyp_cfEzOprxD0jC6RZneDqiKY0oOE82Uto5zNcSpfYNAnpH-Vhfl_-BYK078QN6SX40Wlhl9xaovEFiUA2rQFl-x1_LnxiCn2RfoEeYV52xD9cQFeSwLd2_wH2t9_SPU18dJ-azUknrMVioOkyxjdX8Cw3J6hBgFj_4z7tAfj_YHP99tcMk-hxu-rxgABxDIRLp2l1AhcBEgx8fdTzvGizIvma5wjoNqX1RJz86MtI2_wIGc5Vq1X-0iVKFdhE-6sAXR-hDY5s6BeK4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم محلات استان مرکزی به ایستگاه ۱۸۸ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/460169" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61d130790.mp4?token=cHHrEG5XQ-z2qz9lWgdGWeU_muhNf50IdVbBeD4pZfXGl_zwinXbz95AT8Y88J9wUAqaxEo9Qivey1Tr9wqZO2Kd7aGmGR5HItpsbcjVYg7CAdhto9pN6aMraej0pZtp0Zcp0aaB0Lf9Xo_O-peDHEbpMIH0uABiOcQEq9XGw_leAEANn5hep9ZFmb0yqAcl2F2hP4JU8jJmDvMiDw4ocEHstrO6SgGhOCah-J4OXp9xaGRmOtxgiKIIHNiQ4DLMlB-HdTGUS1HlLe84KmgDQ76OgBkvybFOws6jHvtbahOfJ5dU8Boml1OYyt3e3_jX0cStQ71bx3TiMvzZswNdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار بروجردی‌ها در شب ۱۸۸: لبیک یا خامنه‌ای لبیک یا حسین است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/460168" target="_blank">📅 23:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISnLhHUqSbRPdQZ-LsI3_PytYgMCG0mh9mwBCUrifNUsIltXx08GomGOrd3JJrSXzZMak5ihDmz0cEbrMkZ13o1ebgzu5BmO5BXoImkZ89RDORT-D4RaqJ35jwhM1IcUuYQC0qmARJPQWcoMLKpH1--aRwGxAf5W02sPJINd231AgPAnvd6oIcG7URLjRmnUg00O_jYZ34wuaMjSoAzIuYCAXX4Qm_YbW_z_ve2_94YWLJVqqkrSAs9_lXQ3AgwuFzHIHMecyvzr_kMemuVJK7fxWmx1_5T1my7kF-a8WEedCQ6M53NgJ_FGlC8RGvtkClXsysrIX57mFkvgjRQW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک جدید ایرانی که دشمن را آچمز می‌کند
🔹
در حالی که طی درگیری اخیر ایران برتری خود را در میدان ثابت کرده است حالا سخنگوی ارتش از تاکتیک جدید ایرانی سخن می‌گوید که استفاده از آن می‌تواند دشمن را به عقب نشینی وادار کند.
🔹
امیر سرتیپ محمد اکرمی‌نیا، امروز می‌گوید که دکترین نظامی ما پس از جنگ تحمیلی ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که «باید از جنگ پیش‌دستانه استفاده کنیم»؛ ‌البته حقوق بین‌الملل نیز به ما اجازه می‌دهد که بتوانیم به‌صورت پیش‌دستانه از خود دفاع کنیم.
🔹
یکی از آخرین مواردی که نیروهای مسلح ایران عملیات پیش دستانه را علیه دشمن اجرا کرده‌اند، بامداد ۷ مرداد بود که نیروی هوافضای سپاه، یک پایگاه هوایی و مرکز فرماندهی ارتش آمریکا در اردن را پیش از آغاز عملیات آمریکا علیه ایران با موشک‌های بالستیک هدف قرار داد و مانع از اجرای عملیات دشمن شد.
🔹
سخنگوی ارتش درباره اجرای عملیات پیش‌دستانه علیه دشمن نیز گفت که ما «اجازه نمی‌دهیم آمریکایی‌ها ابتکار عمل را در اختیار داشته باشند و در چند مورد نیز همین‌گونه عمل کردیم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460167" target="_blank">📅 22:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460165">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266a94e115.mp4?token=uNyi1X4g5c1gCsXev_5LJ6YoMNIw1egae9Dbs7rcbwUtjOZigCvCgmH0UysTI_ZSbSyC1fU8sC1rorRlsz6tUWeYwa3_7P3fSyCoX8odsgyHarhYZOIPf8ESo-N_w2hlBpdbSwD3O2yhmeARXiBmM3VXxYBJ3RY06VK3FLw_LRfkNjhvwLtaZ_41E4joRN6kwYYQsxZKTmJRvanyeZNNN1zFhUJITB0s2eFzoSaQfczPAKmaMQspFUoka6Ed3P3cYh14cd0xO1SdH8JhYd2mKty6GjY9FheeMMHtwob3fFdgcMpM-Ci7jJsFc_jpXSBtrjDeGdYgTJGK3Zc7QPt1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توهم جدید ترامپ: ما کنترل ایران را به‌دست گرفته‌ایم!
🔹
رئیس‌جمهور آمریکا: ما کنترل ونزوئلا را به دست گرفتیم و در واقع کنترل ایران را هم به دست گرفته‌ایم. اکنون چند روز است که هیچ شلیک و درگیری رخ نداده است.
🔹
تنگهٔ هرمز اکنون پذیرای کشتی‌های زیادی است؛ کشتی‌های…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/460165" target="_blank">📅 22:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460164">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c06f4c83.mp4?token=j4KzYCY8hb8Rdb7_oUk9K3Wz58yL32wv-8riKAP2gW1L0Xu1wHgOWFGRNCcSN6J0vH-jWZfnLaSN-ha53OS7O1xyB23GmFexEfvwSFmeI4BB8oo_Lg7O1Na0prqwaEf7wgoZy7QLdWdxql-ZAPQUrcvKR2Jm-dZlkChuc27h-tMth_WKV_TQU05IZHSARMwJfiDKVFkHMFmepZc4_UmQT16aHU_jDAyvgnIKHFO9rLfOvHbvwhK4CAFBduZ4T1eErV6QC_tQrfSMEFKPyaGIsWKBsFIPtiq-2yzBq2bxGLct7kOqQ3R8jINcPdAmMu9hrH8GkpqB34wZ7Q8wE2stqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/460164" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2e1fb1a6.mp4?token=Dqqd_bpwUHtXBKDEZX5mKYu1txSYAq6M7wpEMq-akPgHfUrjeweWk1ipEV_m49lsCP7DzdkyuBRXbZiS27MRyyuQeHjgun7LbAkJB8lTKb4c7gVVrKIByeYDGYW3MmD59E__SX2RV5HupH8Y0Tsgn2090Ky9JRmeXfIZh5s8Jl-eJWZZ0dmfWZbkFHG53R70AWfytsERAobcHFYFmwSxT5yJCB7UtQzRKFkpbmUmR8s4_m6cfPy1tKzDkL2J5IYkJSxzA9rQtd2Pox4ODcFQXwl43LeENHuG3TC8ZEr4zJqeLPiqin8PhMRCGk7zmsT9ozKiRqkeHWFTH3u-cNHSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شاید آمریکا قصه‌های زیادی برای دنیا ببافد اما پایان این قصه را ایرانی‌ها تعیین می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460163" target="_blank">📅 22:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4wvB7C9Wj0IddgJNxF1Y0JvGSTshYlpua7uRhEbn0IOQSkcRlGcAVLVHlqHlE1oVrkIP3jRGyweYlcL23q5ViBnxVpHmXn1xhZ58IZpecbXLgWMv8kKFnQDCeuzLPdYWr8PB5eNU6_ToE0EYR4k-F8yGqld3DnV2wGacrO3XYIWlu5kvl3dtupmUHlYQIO6JsdcR8gALEE6n0dI8CQ7hiA9X1gIRZ-KugezLrQDRTNyB0y0Dlg7575XMKDxM9R1bREcjGhIX14Eg0462Dpta2SUftdegXEPnTS_Bwxv0l4MioC-EOXnmTA8zQL5LWZc1PVnthctcdB8-LBRqUlG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ سال جنجال برای پتروشیمی میانکاله؛ روایت تازۀ پزشکیان
🔹
پزشکیان روز گذشته در جمع فعالان محیط زیست درباره پروژه پتروشیمی میانکاله گفت دولت برای توقف این پروژه تحت فشار بود و برخی می‌گفتند خود دولت مجوز اجرای آن را داده است.
🔹
پزشکیان تأکید کرد وقتی پروژه‌ای به طبیعت ضرر می‌رساند، پول آن را پرداخت می‌کنیم، اما حاضر نیستیم ادامه پیدا کند.
🔹
ماجرای پتروشیمی میانکاله از اسفند ۱۴۰۰ آغاز شد؛ زمانی که سرمایه‌گذار بر اجرای پروژه اصرار داشت، در حالی که سلاجقه، رئیس وقت سازمان حفاظت محیط زیست در آن زمان گفته بود که احداث کارخانه پتروشیمی در بهشهر بدون مجوز زیست‌محیطی امکان‌پذیر نیست.
🔹
در نهایت، سال گذشته رئیس سازمان حفاظت محیط زیست، از تصمیم دولت برای توقف پروژه خبر داد و در صفحه شخصی خود در شبکه ایکس نوشت که پزشکیان در جلسه هیئت دولت دستور توقف فعالیت پتروشیمی میانکاله را صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460162" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc7bfb46.mp4?token=k7age0-dQqM3eNFmfJ_DDC7uYXfHZm_XeEJlPZS3EzznONZnb1isremcc0yYGJ8qwbR966knmpR8ewWymbHku7R3fe4K_rm8uRoA4_dnCqGhRkMZtghYoJzq-BDIhF-juyGeuBftGt_vaIRpNmpxD0kDBVlT9RuywHS3Hz2BKGP7rTYR2FSNhpltzaOL5FfCkpB-xqrECvsSbuI7FtbBPeDeE6GanbKuUoL3sX49uE6OsiFjjVbRuSR38ubV-65wG4FNb_jpaek0XJyfIBCuFMEFXS6OMx926E-qyBnSH1Rsgfm320dm37RYUvPWofjg-XnwqcSixfLJszsm49qIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار: اگر درگیری با ایران نامش جنگ نیست، پس دقیقا چیست؟
🔸
ترامپ: خیلی‌ها به آن جنگ نمی‌گویند. من به آن می‌گویم یک «درگیری نظامی»؛ چون برای ما موضوع کوچکی است! ما در مقابل ایران فقط ۱۸ کشته داشته‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460161" target="_blank">📅 22:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db96ccdf81.mp4?token=amclsvf-TfTuWTKCvYacB_6J9nip0KYDsf4XX-kn-slEXK_Cv_wTlfrS8eTMjDdGtoH57VL2WYUEmUsjLvIDpLwx1ba5tXnjyLNHlqfcCxbiRhUoHcZU5otJwAGRHS0V_2WybofE4tiJ5aDMeJfg-DdDMpNAkjHPWjOubyyhMMcUHwCW56TlFf4MkAfKPrKpTqXry3GzQACLVLW2L85KfCqdoyUDvqnIbPfOCoEWraeD_C0rvJ9JUu_RpEEecKXKtfYTNdauiCdcdm54va6rtWegKcAhaInQJ2XtQlNXgbeKoQqpg0zAYztHBD0uvH5vCMa4QXqRGO0LU6TykPT2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های برافراشتۀ ایران اسلامی در شب ۱۸۸ تجمع مردم مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460160" target="_blank">📅 22:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4d254ab6.mp4?token=d6RsIiLWlkgvL3GVuppx3SzOOUfBkcrOEydimc4YezNsqXdb6_zqQXUBy2ZKOCUW8zsskfCH-IJHkZLi9dbOCOTsMzmCfpoNWAcsaSPrDvT9ClBZmbZ1NrU-AF_9PHmKLEAx1pLaDZfC6vBab61mYr5_I9lAsu4gDh3Xij82eQRRQ3uuFYq70eP6mkPkmK-n3cDR-9gtbXg2B2TcRsv4dPEp1EcR_oQFIzhcYOdv3iTpOiiAQmY5F6Pxz2Syzy784q4imn1in_Pm5RGkFKVko8IjlKF-wqgKOebH4ga6_xxJWYjGe0zCMFWea-fOQIOo8fXosgkzE40Vm76iC13FUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم: تنها تفاهم ما با آمریکا این است که «هیچ تفاهم‌نامه‌ای وجود ندارد»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460159" target="_blank">📅 22:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460158">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
خواهشمندم موضوع
عدم واریز مبالغ سبد کالا
به فروشگاه‌ها را پیگیری کنید.
🔹
از شهرستان شوط آذربایجان غربی پیام می‌دم. برای
بیمۀ اجباری تأمین اجتماعی
، در ماه‌های فروردین و اردیبهشت هر کدام مبلغ ۸ میلیون و ۵۰۰ هزار تومان واریز کردیم، اما برای خردادماه مبلغ ۱۱ میلیون و ۷۵۰ هزار تومان پرداخت کردیم. اگر ممکن است
علت این افزایش مبلغ
پیگیری شود. ضمن اینکه از پانزدهم مردادماه چندین بار به شعبه ماکو پیام داده‌ایم، اما متأسفانه پاسخی دریافت نکرده‌ایم.
🔹
یک
فرد دارای معلولیت
که تنها منبع درآمدش
مستمری ماهانه
۲ میلیون و ۱۰۰ هزار تومان است، چگونه باید با این مبلغ یک ماه زندگی خود را بگذراند؟ فرد دارای معلولیت نیازمند زندگی با عزت، استقلال و تأمین نیازهای اولیه است، نه مستمری‌ای که حتی پاسخگوی ابتدایی‌ترین هزینه‌های یک ماه زندگی نیست. لطفاً صدای و زبان معلولان باشید.
🔹
جمعه‌بازار خیابان بهشتی
محل خوبی برای خرید و فروش است، اما متأسفانه برخی فروشندگان به‌جای بساط‌کردن در محدوده مشخص‌شده، بساط خود را جلوتر پهن می‌کنند و مسیر عبور مردم را تنگ کرده و باعث کندی رفت‌وآمد و ازدحام می‌شوند. چندین بار این موضوع را به
مدیر بازار
تذکر داده‌ایم، اما متأسفانه تاکنون اقدامی نشده است. لطفاً مسئولان رسیدگی کنند.
🔹
لطفاً در مورد
برداشتن تعرفه تأمین اجتماعی برای داروهای شیمی‌درمانی
و همچنین قطع سهمیه این داروها هم اطلاع‌رسانی و پیگیری کنید. چرا باید سهمیه داروهای بیماران شیمی‌درمانی بی‌سروصدا قطع شود؟
🔹
بنده از طریق اداره‌مان، در تاریخ ۱۵ دی‌ماه سال گذشته از شرکت
کرمان موتور خودرو
ثبت‌نام کردم و برای تأمین مبلغ آن، طلا فروختم و وام گرفتم. طبق قرارداد قرار بود خودرو در تاریخ ۱۵ اردیبهشت‌ماه سال جاری تحویل داده شود، اما پس از گذشت ۶ ماه همچنان در بلاتکلیفی هستیم و پاسخ‌گویی مناسبی نیز از سوی شرکت صورت نگرفته است. این
تأخیر و عدم پاسخ‌گویی
باعث وارد شدن خسارت به مشتریان شده است.
🔹
حدود ۱۰ ماه است که
بانک آینده
با بانک ملی ادغام شده و ما برای
تسویۀ تسهیلاتی
که قبلاً از بانک آینده دریافت کرده‌ایم، با مشکل مواجه شده‌ایم. هرجا مراجعه می‌کنیم پاسخ مشخصی نمی‌دهند و حتی بانک ملی می‌گوید پرونده شما «مشکوک‌الوصول» است و برای تسویه باید به تهران مراجعه کنید. ما فقط می‌خواهیم تسهیلات قبلی خود را تسویه کنیم، اما چرا باید برای انجام این کار از شهر خودمان به تهران برویم؟ خیلی از مردم با این مشکل مواجه هستند و توان و شرایط رفت‌وآمد به تهران را ندارند. خواهشمندیم مسئولان این موضوع را بررسی و راهکاری برای حل مشکل مردم در شهرستان‌ها ارائه کنند.
🔹
تو را به خدا به داد مردم محله
کنارگرد حسن‌آباد فشافویه
برسید. حدود ۵ ماه است تلفن‌های منازل مرتب قطع و وصل می‌شود؛ ابتدا در طول هفته فقط دو روز وصل بود و دو روز قطع، اما حالا سه هفته است به‌طور کامل قطع شده است. مخابرات منطقه فقط می‌گوید «قطعی نداریم، به تهران گفته‌ایم و خودشان می‌دانند». بارها با ۱۹۵ تماس گرفته‌ایم، اما نتیجه‌ای نگرفته‌ایم. از طرفی برق هم تقریباً هر شب از ساعت ۲۱ تا ۲۳ قطع می‌شود. و متأسفانه
ادارات برق و مخابرات منطقه
پاسخ‌گوی مردم نیستند. لطفاً صدای مردم مظلوم کنارگرد، در ۳۰ کیلومتری تهران باشید و این مشکل را پیگیری کنید.
🔹
از
محلۀ افسریۀ تهران
پیام می‌دهم. این محله با جمعیتی حدود ۱۲۰ هزار نفر هم با
قطعی برق
خارج از برنامه مواجه است و هم تلفن همراه اول دچار اختلال شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460158" target="_blank">📅 22:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460157">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">کارشکنی کانادا گریبان بسکتبال با ویلچر ایران را گرفت
🔹
پانزدهمین دوره رقابت‌های بسکتبال با ویلچر قهرمانی جهان از چهارشنبه ۱۸ شهریور در کانادا آغاز می‌شود و تیم ملی ایران در گروه چهارم با مراکش، آلمان و کانادا هم‌گروه است.
🔹
ملی‌پوشان ایران که پیش‌ازاین برای پیگیری امور ویزا راهی ترکیه شده بودند، قرار بود امروز از طریق استانبول راهی کانادا شوند، اما این سفر هنوز انجام نشده است.
🔹
ویزای تمام بازیکنان صادر شده، اما هنوز روادید بهروز سلطانی، سرمربی تیم ملی و محمدرضا دستیار، مربی تیم صادر نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460157" target="_blank">📅 21:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460150">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTm6EnJgQ4MXQ6Of4aShXdbMx7LsZOdQZWFvA0QjdvSjOujFrBBpYbFpz60Od74frccnNZn912RoZPzDu1YF_nY-s40rnN2gx9_hFxDSITtf8gMQVJYJcAqJBGVQRfcFhqH-zwaj6qN9xLSznefvGQSMWQwThY2Rbvot4H9xHaqA1r2ODEtd_kctDq1I3P7o3VkBnRglfX8rvid-2lOamV4zBl_lwLA0PH6iJTNNZdCbPsnPWTZ65rrBj75Tkd_LxnOefWOJE3cY0_JxwRqr6AStE3p6aRmui2Q4mrR-7FT0HLZRkzB_iouyBLbzXHcZOM-tiwHADyBHf1e5Lh_4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThQUY6phNeodpixLdHgmCVrbRhqCVh1tdD8reGn15pXYQQSAUthPaZ1tRFfn04ACVkRLhXO2NKh0dn9E0VkmY2BZwD2dUII8aNGw5xf92BhVSC-EQTWvkZxyHppGmWKUmiG8-liRokm8u9UcCYr3dmSGxQ_eXIUcQ0RRZKoQl6sI69UE5ZEqZEwublSZIJgmi9iQfuGMt2Uvt8ysa18-YCoCX_k-9vGXVCZCVcqzjSByJ2uzo5El0tPwS_xDAntDep12Ck9tFLzX0O9fr2IL_kuDnGZE3OJpdRY0uaQar01Z9LMj-DsFuN8H-Jdx5ZKGoF_ymOYevLIEnYX7FchFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9ezQMoEkz3RbrsNWWP675PeootQdvNJujefgDhb_EUDg7nFk6ibz4oA7cSiKGRKlgNPjUvLtizcAJLZylmN6sm5SghjEKBN85J8J-5jk290O6w4VvtXsoTjqGgksDAJ9T4XeOTooqU70maeqTD-Zue1eKsU0a-7vc8vcJT-T8jhs_cMVwhG10-NqrPsyV0E-neUHulNjHgaykR8MH62wfg6QsH8hmOeOOfXshfgP1mw9S1N7FDcz8MVjYAAIbTkZShyFfw-_QSUyDZp4S2TjB0YbhEq77EAcLCm3JHOyBDwIK6xkIsCDiHbOUNM4xJm2jAfuvrNABhnqQfSSWFCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PU516aZXV8qz8XbRnY62e9mT0G2P1yHE7HjaMpz7n8nVkpJ47RON8Da4kFYkZwnEK1wCcH4nUKpxjj00HUuR5XwiNYMx7kgTFV4HAjYaWyh1_Av8A24AskV4b_rpywhd-qZ_aucNzeaDyvUmvVHit1MxnHgLIpaOvzJzDKFbbWhrrQl8BOMilPzv4ox1gp2ns9JC5wK5zHTZwNvtxXktvmtNhthcfPDrpvI4u-TFMiDfZqHIFtOHCWv6WlFDV8m1A_6vxRLKpv8yjszXKir7nWrLgc6FvE_fOQoD7z_j4x39HuA3nsHPpKpvMUFC0x3eXeaZm_sQ8JGhf1zf0_ngGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDk6nb7ppZE3QL9ewgZumYAr-qkardhsnF5ROZ07vLi0h4L76FXnQvBBK0zpLJjc2oWEBs6tHmtULOOvRHi10kPaD9h-mo6BOEyefDlQj7VlUJ-z3Dqxybzn9Eyin5cU6Lq59hVGOnm4O5ipoJogCXmdDFDlm49wYdhAQReW76hUHek9R1mvCLeWynvlAUc-L6LPOBdwuJ7PgmMSeYicGg-NRIBSOpFL-enco6IsXEK7noXWwRJeq2tv4TZeivATGu2SBWVt9mGaKySBr_l9IGhE7OywmrIICyzYr3i4yais-P1MXloTTYvsZh6ktBkjsr2rSetlCsQUN-1pAnu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDhbSFmDiKDfeC2MswzL4nvFIjp1vIfeEpwpMI-hO0bbct2SrPqRQxknS3s2jXlGPy083XoWneqEaEB3lU5nnt5ARp1pWLGUz49OZuoUTXnTF4JR6_MraVPjHnkSI3VgB59TN7_NKFZsoOfPwhoIJezX7msG8dzqUnrXk51FgRhq4zTOdReJHDxl5vWaMtNuMggF5ofSxpWY86nKGkI-A6-Bx2glPgvvUFsPOFzcR3DXtoV9ztnCN9-rUmNnwP3UUqRKGW_Mb2xVJ7DXbIZuYRlhuAgkrtzqYLo02Ez5AS1QArXRClKBvxkaqdptyWOPihroNqPhz43ilWeYTn6koA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW4JYiErlV-rmY-DHg2tekvEHldrIez5cj6URFIzTvwsTIicZBmxGrMBoLoLyscPUcS5ptIqrFJQRLOdyNq4vvZ-trMZ4BrWTzO65LzBjpsISV4ueEggN6PpZ6j7BRcGqDCsYLxRRsN78pHyl7_eRt2Ibqk7dZegQ-VKFiRzlBZ4OUFThquuXrGunmX8_YNA_F-PJfXSYZNIWWMjIn8mZmhrrzJchQEfILxOhbH5svlslaWwFL-RKK4DqARtrPKf6vDLc77yholb1IcjYZrNknMqA81RPIRhMqHnPCBnaeVIrYlhPoVzCXTOVenbuyrmgvUQ82leBbNKwu08f2eSmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرواز ابدی خلبان شهید مجتبی حسینوند
عکس:
علی صاحب‌محمدی‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460150" target="_blank">📅 21:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460149">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e0e7346e.mp4?token=e-zz40w_R_j9ybN4RoIh3CgOhgz7p_vFLaiDUZPCZ-Xvwl7oHTi2v2vkrFGCoFFzguf_W6p32P3OPpIFW5tcmOxcz_QFMEfosIVIgENjUAPvxT_usNntCAsCsD-xwZVulSBir4i4olCaK8MJO4X4uxSFvW9veRUvDWCNO5Iy73ulO7UebG7xNfXue3u8G5wzxtIe3_WmGGl6jrr_tE4GJGQ7BrpEayahUZTjgvGCk4w0xXw0gZCBOTJ8chsa50oIXDF6cyEtJ1VRlFY3R6DBhr6LsxzGH_QSAZexSjz6MhdZvlMEI4kySqM66i5zGltbEkDMRTBm8o2S5ejOCktaTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانۀ مردم میدان در پارک ساحلی بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/460149" target="_blank">📅 21:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460148">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2zzEnko5UMPHzc9olqNUOvbvVHR2ZW0K-_nxBX2QMRgI-hP0XiqRMI5jiseKwZB_OYpyER6J_ge3hOKmsiDt84gB1LE7qIq7Z7K41Sm7nxF9N4UKd8SyaDb84qXigYHRy_aO9EnAXjtJsSUTZZKJDDnMoyDTZywwCpNM1LK168jIKDx8wSkQd3h5Um1c5r_tZE4wD1V58XkUG4jZskv999Y_GDltXNHfzvZv8VRVMmj5uqEyO8IPk0Ki-QCTaEFlUcjRTTzD2zAZsCeGlE3VP1MWsGJi2DBNFEbLMH8LFHcpjW5ljMlw2gl6UDJoAlkYguYI5yBBYMyl09Fu1kBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار سردار شهید تنگسیری با رهبر شهید انقلاب
🔹
این تصویر روز گذشته از سوی دفتر حفظ‌ونشر آثار رهبر شهید انقلاب به خانواده معظم این شهید والامقام اهدا شد.
‌
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/460148" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460147">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07b37167a.mp4?token=ORzlwgm8nIjmi0muMUtxUZ2PcV5ng590mdbCCnW1b_Xe45n6t27IraijDIEnrqzMsKbdzvUaJtIZwHrIfp7MKUobfcJL3hWhaMTC1GmgxHYnNIyUkEXo-fzdRCAdvFGLuKGm3ZYGlRyiUbLXm3Nd0YMNZXZfNubPEZNX-OrelesN_cammKM1wDcyGYf9zNjsLpFvHLvLtcb147WwQw23G3bsqQBzmQ73kdZv8GoMWqX38pPjuHH7bL65S0I8sYewuLLUVosfzF2-yzVcSsuZWlyobMh55xsLCrhRVkH09a__NQ00MRQuiFB1c7qxh28m8NUpMlaL9s1BUdeQ6sSVgkVMI7nAlgKj4o84MWizyqBUCSv-OMVcIzplFlN5EYD0QB45UAyFVc0Honxd_-O7j2Ecq4fWYeZI5Z41vO8XLFosQQd-fDQwj8NPyi1lV-ArnmLhgcNZMZxIU9kUBjYlF3KOrHwJdktn2TG9VZxc3w1FZfpLU4A8opWaZJXC6PiQsY7cR0UNGA4IyU36rvXcJ6L5Amz-jI0SlFuB9Md2htW735oy25ioFmzFjBDcxQr3pexIU-r99B5CS5lCxQxLMpfdgJkozQzH3Zxp2Bk-cAdtNY71aihU34OWO04kQJ8RAzw5GbH5PoIWAGEpzmWZAIpqKxvi89S4IMLFHPe-fGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال از پیکر شهید نیروی دریایی ارتش در فسا
🔹
پیکر محمدرضا بادرام از شهدای نیروی دریایی ارتش در که در حملۀ ۱۰ شهریور آمریکای جنایتکار به درجه رفیع شهادت نائل آمد، با استقبال مردم وارد زادگاهش در روستای سنان شهرستان فسا استان فارس شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/460147" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460146">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حملهٔ مزدوران سعودی به یک منزل مسکونی در الحدیده یمن
🔹
مقامات محلی شهر الحدیده: در حملۀ مزدوران سعودی به یک منزل مسکونی، دو عضو یک خانواده شهید و دو نفر دیگر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460146" target="_blank">📅 21:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa844588e.mp4?token=lodG_P9jAsumMNqW3AdjWQfvD9_9UqcVoKWCdkNF93kfEa2RnSuGJK5M1iWxWK52hcbeHwxASvP-zEyFoq-vQJcX73CSrsqihyra0TOgSEZ9Zm9eH4Rtd5xC5oAYGt8sCteAIXGbU-xy4fZMqiQjo5PzgXyJhNhUPwml9pcM5YdIjhPgNyl1X9c0eEPky7ubidRdVHgsmNhZhNukhd-uwP9XFbIAasyie_sU_GbB6U7QvcuakgydVKwkPx9qvSR6bDBg4wb5B1pxM3EwHoKaXunjzbFm2kcmp8i8uIUreSXaq8Qg5Sb6LVBLE1rVExo_domV93QMJY7XiUT3hdqNITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خطایِ نقطه‌زن آمریکا در کوهستک!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/460145" target="_blank">📅 21:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fffbd748c.mp4?token=r8idoPoq-TQIrPYjIBUahExCYQMN5707ailW7MCHWjv3v09XoKJozzzayi1TqssywDpSIxEJDZFYBe6YYihjcyTJY58tEJ0rhDn_UITlIaqmEmO5e5De6eL7JmAxznTxf_IkSKbkbNywbmlnGJZ5tYylZmZa261zlUm58N_tHjvzjvCwgBm9eSbgs3n6L3lFUghJ0kDgCSlWrmeHmEkTrnGfkif_C4FmKAsJcwsOOGwy4xr1qN6TbZz9C9CuJGPMxhHhg_pURuavMttCiw7ageVDW5gIA4lj-Orack6H0fs9AF865NlpQ-A8L7Cjz7XOdr0NBTRHDe_cZo2ZDrgK6E3oUiUeYasGRMzkkhTbQNdO8wsBxQgNpHrdB6BuwytvjwncxiD4Q6_rr6Co-7Lzyv7bR3qPfiXTM63ZvU5PHpb921hCn0ms1Z292OPpapMmWgU2Gb5FgsF976tMI_RtLvT-4OJ6xf6-qmcb7roh2KoZ440QQDBzEjd2Vy5p4Mn4joVHQ6XiFBoKCK48ixqowMO0Z1pbQ_XxxXRcJ_-ugpBJ_aPSjpCYl1iRMn-AnpppxjiCC4i1xJlfxpFzN7cKMcd9xT0OQsONaFVaFXoZhfideQBvwdP2exJ8Gkln3TgBFiE1GowCRPgYZx-Yk3oazgkY4nPsR3FZyj7QEYyASwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون تعارف با تاریخ‌سازان والیبال ایران که قهرمان جهان شدند
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/460144" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a8b8a488.mp4?token=N_JvU9I0Iby399vSl1hZAtG7l37kH0QcrG9lS6gpCqLUpjXW8AqWyAqV_LuqgeAlTancx9EjtZW60jpptHM55uCHCMQmgTeikKV-w3Xg0mdp8SZdjAc7rUt4d5mAhr8YFPFCtylqbP3G4bODUXt8-rNzHPtFLk7UzqQaAxrPCW-4Gl0MGHG99i6QVVrtsOu9e5orY79BXT6MV7blwkIlcG2w0BPF-AqPHK2FYIt2JtycI_QCGujxEjZErMFwPA26s8lhmo7fWc0SNWj2mrVmyyguxd2DtCeR-H02L_C7DdC1fbCXctoeboPVCngJP7r89dJ8UbSugTaRRrQfmUvL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: دشمنان با جنگ، محاصره و تحریم به‌دنبال ایجاد اختلاف، شکاف و آشوب در داخل کشور هستند و ما نیز با تکیه بر وحدت، هم‌افزایی و انسجام ملی، این نقشه‌ها را خنثی خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/460143" target="_blank">📅 20:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twlI9ipuQ0Q8kUAEX3FUEAQrb8tLl3ndowuh4tE8W3DuoHMOqff7wAPYQnnKBBtiql6ILJo_kOXW9dDvoiXxP1Qkuji5L6SBqlrb-UV2g0zD99TyioNVSyWrzXiPLhpIitT5ONSd4gOyi9W5p-gRQmQgg5M7hcPcIJnULBmbmAFu5gGDnFjMnxN9KNAvUskQPymu1EBWLd8eZygJbc46ztcyzBilvs3T_lvNqo0aaj9-5MC91DtSjeWU02DnUR9i1SaOFUccWp7nqYphxOLXC29fXW3bW-tDSj_81fpPc1YAkr3vyj_OuzjVTTzv2PYpr84rFyCeJiR5JgcMzXARjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل عاشقی مرال‌ها؛ جنگل، مهمان اضافه نمی‌پذیرد
🔹
همزمان با نزدیک شدن فصل گاوبانگی، تبلیغ تورهای طبیعت‌گردی برای تماشای مرال‌ها در فضای مجازی افزایش یافته است اما معاون محیط زیست طبیعی و تنوع زیستی سازمان حفاظت محیط زیست، امروز اعلام کرد برگزاری هرگونه تور گاوبانگی ممنوع است.
🔹
فصل گاوبانگی یکی از حساس‌ترین دوره‌های زیستی مرال‌هاست که از اواسط شهریور تا اواخر مهر، همزمان با فصل جفت‌گیری این گوزن‌ها، ادامه دارد. در این دوره، گوزن‌های نر برای تعیین قلمرو با یکدیگر رقابت می‌کنند و با سر دادن بانگی شبیه صدای گاو، ماده‌ها را به قلمرو خود فرا می‌خوانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/460142" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQzn3bJfwEGK0VqewjNlwL405gCKtxHsGJ8Mbk2YHanDW_-e2mET7gBGvF_NxbvUjLq8FfHh1k26SGRlRkcIQsPGUFcT8joCLuUYyTKAZ81zwXNBHw30xtulgQ0K-Lgl-5g3c1UP-NKrCH5B__HMLYtJ13zKApCJyNQUdfUmRtRQvKV2ABCJvK52CwBQo92QziH819eUonrWRQ_HuzXaz5TjY7N0kI-rTkNe1eJx1V9J1HeYvQpEeB6su9CX-T7iFUlLRTbskzxf0E-GbnnrogF7jLiwGtuax2bIcUEPACC9B_fd61zwfTaE2R7EV883ZXJb_ivZTfBAA0jibRAInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: ایران از ایدهٔ چین برای ایجاد یک معماری امنیتی جدید در منطقه استقبال می‌کند
🔹
نمایندهٔ ویژهٔ جمهوری اسلامی ایران در امور چین: تأکید چین بر تقویت امنیت مشترک، بازتاب‌دهنده اصلی است که ایران نیز سال‌هاست بر آن تأکید داشته است.
🔹
کشورهای منطقه باید آیندهٔ خود را با دستان خود رقم بزنند و ثبات واقعی تنها از طریق ایجاد یک معماری امنیتی جدید و بومی در منطقه امکان‌پذیر است. ایران آماده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/460141" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930c9bbe22.mp4?token=gMzGJepo_rmpA-KVxu6IJQfisy0QqswlOFwo4e6sSNQ9PG0wV2BkZRBPhOEStl_21HlZwuba-ZX_Y4LXq2XocjblscXOfk762BX9o8Jbzj3YNlRXP8p0zyoLbIv-Gv83pc8thkRKxyOgDhWl6XIThDHVimbLqm3swcf5Tkq5wJNJZiGXf5QBmGYoLMRAfqSczqcsyJGXSdX75GtqnGXjw5pIe4QDDd5bZq9oYVKIA_Qbc2USXpPhAanKWrB9-b3rCEOjvALUewRQ6TKxkXu5gPGgw_ZrdaxicIvzS_K2HMRRsC73G8sI2bSUx-L_IJO2k34fVXL2v4sfNlQI-R8ak2aGMjS7Smdoqr1vOROu7TPhwCFBKbJD-Ut_rk2MP6kIuW8_U0kbRAm7GjhBpw24x_zayWhpzmCJ7hUAQowQ-pdQADEJYwLNTcm1sTpvEn7oDJoI1ahp3jifH84Hh0_IMfwVRWD6aeZE7DM8s3hMNEYgahcjUJt-E3Yu1qtml9qy1xCLRianDAvq4WInWTD_JLDkDEdAqmkRStQEyhxZBQDShykbh4TCSXkTrWVAE0IuolshsdHEYNmIq289oFAM-st0vkXUNWMVDitwUnoKXuRGVIt2mGT9AiKFi7dsgd4K2ge5TKbCoNdyZYwgW5qILRw1ZAMC4jXNwSXHGuV41DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادعای صهیونیست‌ها در مورد تسلط بر ارتفاعات علی‌الطاهرِ لبنان
🔹
ارتش رژیم صهیونیستی مدعی «تسلط عملیاتی» بر ارتفاعات علی‌الطاهر در جنوب لبنان و تکمیل پاکسازی زیرساخت‌های نظامی موجود در زیر آن شد.
🔹
ارتش رژیم اشغالگر همچنین ادعا کرد که برخی از افراد وابسته…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/460140" target="_blank">📅 20:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh53ER9YxqL75lBr7k_CSagnCLZ_52GaXB31fyb87oEhwZTH21qgV52OJMu22NYkEHJWtnbhN3NrWKSmZZXD1k4dePjGmCentvlfAyMCkQP9zlqAZoeRs5FkAkxlFXE_bIRRAE5xQiwV6CDr59FwuFws-wXl62AtnjH1jjcnkFAG9ItF8rHHZXzyP7tSvLtB39WzvByg0J8ARoS3VJjZwoHZrXZro6FyamU_UDZw4bryOkc-JOWTSwgXo27w77RyEjmVf5KFRozlXqDkZUjp3_gKUN-Jlgv0jB2Y3o5gb_6RWP9T_QNCzNeyD06_viPuCEhlYZ-PUgH5KeIecoBevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عصبانیت ترامپ از شدت گرفتن انتقادها از او بابت جنگ علیه ایران
ترامپ در شبکه اجتماعی تروث سوشال نوشت:
«دیوانه‌های افراطیِ چپ‌گرا، دموکرات‌ها و کمونیست‌ها ترجیح می‌دهند ما در جنگ با ایران
شکست بخوریم
تا اینکه رئیس‌جمهور دونالد جی. ترامپ این جنگ را برای آمریکا به پیروزی برساند.
به عبارت دیگر، آنها ترجیح می‌دهند ما ببازیم تا اینکه ما برنده شویم! اینها آدم‌های واقعاً بیماری هستند که به نوع شدیدی از
سندرم
TDS مبتلا هستند؛ چیزی که گاهی از آن با عنوان سندروم جنون ترامپ یاد می‌شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/460138" target="_blank">📅 20:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع عربی از حملهٔ موشکی به اهداف آمریکایی در شمال اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/460137" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_9GJIhheXr9gLpFITpOC7IiAjBgo9SDMyCIDrI2jWzgLdJGF3oUWsdpx_v4cRPLP3zwzQbOlHSrlbAGuRczKEdrfw23LxE2xToeJGF0n9yo_YjCs_CKU-8c60ZU2tuZFUwRubMHAuRRLrapQKhmw5sLOYsIj948D1USZ4W6YrOD_Wcf0AHgmHQPOEdpaYgA6iQDZ4LIiaeWXr4zWOtYw50De5hYgmz8QDwMGBrOIthoyD5uY6kXpsf92j3ldia16qNEpMjhRqJzGdWAVct9lYCDQS38ngvWhNct0_ySXmflfXKgkaHXCef6tj9PRKfsD7rD4-Xviao3WCKv1fvXdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTedLZqt1czJ5uTBRBUdohzKqldjECxBa3NSJC8WzhKJxFccn6vC9xCezUsqCDXLTDT1QcoVZOGHM4q1eAce2H--MwlyxNJpKphqNOLtVx19wWpNySbuXtMSD2dIGIYaLxcwngz7-lbzUegWuhfd_HXkU6gwYBcvyCcQek9OPdP_ZF8fYiLuGT06uH_ponWT1kS7JSjDxR8gpqYacjlht2eJ3N6LCS7sTcv3tH3rPnrnJ2h3g0zhpJU6v6GXLxaHqPvV85Flp9Ty5iw0rZZj-PtibsNXmVbSoBN5hJnsVPwvr9-B_ziHtjm0Vk2LlStuFCJICnoHX7U0-6hkcoJKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6BE9oBjzwCU1XwO2829_tVhahzyqCUayy5Lt7Ch-Az769gb4dbtObNwuEDc8OkI1kdDg04XnHo_HPXtugrrF1qC2tGxYipZ1MKccl496gV9-nnDORDBDLgk6C7_wwqasdOgPdgYvDl1MtFcDEw1MMBGGGOFzQAWh2aYfimqzmwhEdmd-gJW-hRLS-azXTdK_Uqy4JhayEX034Pvpf-26n9dUSMgNjk6zIu5aw59x1V5vr3Yon9r24SLs3HUIhdrCSlS-zl_eg2w3a5zO0VQRVqr-gMb2SfGIOMmPmG4kZQme7v1Y22BsZKPQU_s8PktDsQR3OX6GODOGD8BAu4H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4UpnRdmMdrtdR2Dr0Noj02jm82Rcbyyyx9TaPWwPjtQunHTcndE3VdmQ3ds4n76fyhf47yxPzpzAisNTlbPfxO8e9-m_dvT5_D2T3L4-flZYrubo0gsNDl4a2dnsEef-573JCoFaTFjqVDCKE7Fz7kqgWPK8BSo12dZy6Z-cxRt6zXKlsnUUwHXJy5Pv7SJjkiMVLfzRKzZa-UMVancsh8yvHPG29qMjFL0fC2ZRZ4Yt1wLAboERvwcLT9pNMVQX8AXsgoyUefzhMBNcpGeS5a0ajnK5b8FdYHWZBzU0WRRnyU4AgD_POdrFlYyDLvwjsjfM0VSFgNQOE8NeAPsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rM0nU0yarh8pl1xG-v8AECKK0HJQaZxDRWNJcEYNeg74sqWqGnc7dyybQsk2u0OHwhlyJuNvGbMzDti0PuwtDOwqNZoplwtaRzyeVF6ubAxix-AHNvp-cola_fBdE0ScuYv54-oA_Aw5MLuqc2JXzSCOYD6x0pEKbphei_DuNyPaneDjqBg1mqSwMnvL0ASJlEDyBZTNI-uY6bbBmrFpwD9WZLsAjKpBUxvBCcxjRniqGNx_DKKKeQyYM_Vnk6i6gTg87KboZum5Ycm4p_iokFBd2WRXdwP7E-dSeUKFxBiq8GfTBRaevci_Uq_sEjURr39KCeuvtz7DCIhfzE9EGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMTgrRkh0GEdcq_g35z2Kebk8cvIcKfXsKpwqQF6nWOEN_pU7fGvA-LVLcJoc9Q60nSZby4baJQ9afN7MwG22BP-unetABFM5XhmsUqRzFaJV2piT-2U5WxndWfONEYB4JwLkXTN4wcedZ2PDg-1CUw74PEr1DVsqPzZCdpxA5jS7ztFQ6Y7irsPcSY2PuWI9uDCNWA-rnLvYt4Zf03PQMfyfpoIgTlEbtvWFjxrwjXd6VPkjS04RdVxdoObnC5ynLYcRZoGH3lCTT4wIgB29VY_v8JVxr4OHP_jczf98YPCsGXcxjokGnm_C7VCJNX2C4hr_4sW1GCTF5ueO-x6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cib0uowCP8mvdqYhvqvhr95h_R4h6T_uUm64uICtbxn7cqeCbLDbr8_daiN9NsrljN9B0u2k9uTbqFNwZt50CjV9SUuAQ7DqipjBB0InUuit_kl80FlZ0OjaQszKH3sOoRSDAXXNFgg57TIVvdLkG5NgkqFCbnCXE-PwC4FQb2zN8LNp47PXPadCjHLNqtF3Xv_qPl6GVXgYO_TbPYyKjgMTNupNz9JTY6kA03xw5JjrE1OF1j83AW124K-sDszF9HmzMBvitfscLPBFgaxllCld068Sgx786CQyOs92sbPSBaHpoTL7fqnRz6Pny3u7XcCvEVhm8n0bOV6SBld8fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رقابت رزمی در «میدان‌یار» کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/460130" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdW2mm1KKcCExXMbViptcGHT_w0xHpIOQ3Y5HhdR6457tjejAhv48DH_3z37HLvGXCXm6Ymd-D1JQzfMWU9RPN-pxaXTzMDtSY_1k-7lNmzZggn85yev3gCxAoqQJs89hh7SyC22b2BeX1Y6tnlZJS7LuUD0Z67VQ-dvTPv5onrMw5DbYDeySNQ1s3LI7LPFuRO69pNUHa9AC6JXg4TEOuxuzkJdfUU3GxsTojjBbfoma9MxGgf8ENlqusE5WiboaYAuBDT4KsyKYJ_qFWJwuNiupmu1olT_gCsslmyyfatnc1m-cwv976SZI3fQ-bhkobeMBoo6bazpSeTxKmCq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1ozs6afKjepdSYc1IdyaqH4ZUXJNjsiMQXjJVgwoNaGWJODQsJzkPVh0L6PKZWdHd8butONRm9b_Lynw5l84OK1fuk_JCK3P3tsvh9S_JZlnuGU1cfsp3nOVW1vQ2_jGX6JIJp5olRiR7ss8ta_MwjN8ZOUZvZdQf8HKkOYm12rlmgfURW3UsWG0ZiKuX9ZWh1OK_PnNLSWAX4cumpuWsTtbTOg4Qs5Hkljl4FW76P0BFrQcW8Fr8ZkIVuE6-tPICZ64DTLTm5V902W_iWV_OzdRDaj5ooLMdvmfrpPSCcPb3J7nvPF9aKxHZ0ZpLjdmk8dRSUmXEhafEDUx9eCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU2SCSeSGJ9Ff-MHW8wZW67B4YZLjDfA6J7DlwmHQxBAXL5rqMKHY2eGrgQqbbgdsV8sFLNrte36ayAmBh4CunvG0D-KNrkKZQi23M36mXUNxomBRhOW8ENyMqPwWTG10woDKxfyKZ9rylqLKBwuiZ0mZqHfn9--KccISqjklm-Yhkz1ADzq8qPBdtwLWvnUiILKE0D41cL6aEi5br4Hs7H0tTBQuAQ5SxxKHOKN_t5pZfHGv5Pkg_wsbVU9SAyphkFG2qgsRmOs92WlpwvadbF9XcA27OVMMGsVptjVreWOCFoPia8hJ4i95tNG5sDPfBXEPIx5k2Dtd2VRjfRAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gskPBEfYzOBp25Ma5WPcQMHEygxhafDjwecilBUp_GySb2vNqHv78b5dugTwZtinGj6OsTYHXxiYc3t2b5FtDW926yz17YM3xWh7jPN-qd8BKE5pXOm8IkSjG3Vr7THNKJ1x-7RqLFoMRuFaK92CoTae-AJCl9O89Iu_QO0UgcLPiN4dkhZ-Yf7DnDaToh1WTG7EDDUOS5iaCIXH2BDoSkvCULJ2uQskgNOUZ7ZvotVvrVCLStuYTaFWlH7e9nQeGrgwYBp-bSPkaeV0nFDWxynLZcobeeUd49x46eWmFLhQxGv0jUiddmZkNB7pVwaguHSpg95h6tXD3lJJTiP1fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمدید بسته‌های ایرانسل اجباری شد؟
🔹
اگر در روزهای اخیر بستهٔ اینترنت ایرانسل‌تان بدون اقدام شما تمدید شده، دلیلش رویهٔ جدید ایرانسل در فعال‌کردن تمدید خودکار بسته‌هاست؛ رویه‌ای که باعث شده کاربر برای جلوگیری از تمدید، خودش دست به کار شود.
🔹
پیش از این، هنگام خرید بسته، گزینهٔ «تمدید خودکار» به‌صورت پیش‌فرض فعال نبود؛ اما حالا در اغلب بسته‌های اینترنتی، این گزینه هنگام خرید به‌طور پیش‌فرض فعال است و اگر دقت نکنید تمدید خودکار آن را هم انتخاب خواهید کرد.
🔹
در سیم‌کارت‌های دائمی، ماجرا حتی متفاوت‌تر است؛ هنگام خرید برخی بسته‌ها اساساً گزینه‌ای برای برداشتن تیک تمدید خودکار وجود ندارد و بسته با قابلیت تمدید خودکار ارائه می‌شود.
🔹
ایرانسل در پیامک‌های مربوط به حجم باقی‌ماندهٔ بسته نیز اعلام کرده بسته‌های ۵۰۰ مگابایت و بیشتر، با رسیدن حجم باقی‌مانده به ۵۰ مگابایت یا رسیدن تاریخ انقضا، به‌طور خودکار تمدید می‌شود.
🔹
در نتیجه، اگر حواستان به غیرفعال‌کردن تمدید خودکار نباشد، بسته می‌تواند دوباره و حتی چندباره تمدید شود؛ هزینهٔ آن نیز بسته به نوع سیم‌کارت، از شارژ کسر یا در قبض شما محاسبه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460126" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1869c43e13.mp4?token=Wy5H8O9Udi1idl8PnNbacI7NTI07BRyKtmyLNNrGjjsCLkalUT7SmUDMeSoGhh6CP7Imki-Ji2zB89Qd6t-TETYHBAMOYsXKElyLjtzjaHOupHnkIzRMt9EU8g47iNXsO92MXSE2LVjSqGiWJAU_Gox1T4hAaDg4t5PC8yQBhbm8veDXA7xFEQSv_an7dMVcaykUTznX-5iMwun-aDQtkiHQIubuxsarRl1iBcFC5j2hRKieKZXw_JCaX7lSKh5icdXwpYobeCpQbtAShPPdbgb9g5siOmUmKi07nmHM7kJGymCscwIGqixd1hX5UO9Sjy4Dpdr2RdXw7NDB07vEQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460125" target="_blank">📅 20:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d9f21b8c.mp4?token=eQHcDocq-LgpvA2FcOGbQsRGCCq8EmqTG1Ip0DIlGvuijaVhJ9JRoRK1W7uEp8CsawpMxdQNp5bOtzN4YmlIAHLyWbE8NOQPESInAKjsvazEAhz8Ni1KlDQhlpqz1wTuyWJrudRUO072vl7FD5xzvvnsnBJzo3ICg8ndLjIbCOPfAzSwAphtmHE9CSATbGTYS_4ykrAad5ckpCE4HGbkifiyUpDI26yc0lYJ_IJ8w3AnaDFvetgDkntLJA1u1T-oucowFKwiXcj2O5OG9_yRlUXUZc5MMblEmKJytMJIgNw5Oun741-UukhAh0DJKLSGSzrPVQDiyrvPs9tk5XpZ5QRS76wGEOEBAcU833NrtS3bBDrXNJqjvjSvnR6AdYA6rZSHdACDB9WdNqBTqd6gcMyYFkF8ITPQfjFs0R5yCbUXQp-VCiEA3-er7wvtiPGj8Q16R8wt-6iFnyoMqY9CjCGi4EP5njODOtfMxUDZ64mO-DUPJG2ruNBvT8aimD2_GzjNJhkMX7b8g_S80zUHlG7yY6t-tU0BfQx4-gIYXjDTnMBJq9unQMi_pehId9vD6g5Q8DxosLrqotwTePhvkc5s_6KDUJEJsKz3E-edFFpuScxyzwLnVpdKvLXHBscOwXpfWqTy2lKa0dq-_NGu_OueC8wDwT8SfFQ9sEJvKwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع باشکوه مردم دیّر با ۳ شهید حملۀ آمریکای جنایتکار
🔹
پیکر ۳ شهید بسیجی شهرستان دیّر که در حملۀ تروریستی آمریکا به جزیرۀ لاوان به شهادت رسیدند، عصر امروز تشییع و به خاک سپرده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460120" target="_blank">📅 19:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bfc862078.mp4?token=ntvxe8EC5N-4mrWRbNWrpdVxu48Gthv3lE0p2sdGz3PxiR3lZQxaj8sYN0j2o7hChXyDH3VP4gzuYpab7ZivJQtlrXk8RimLtnxitEvpwVXePOEsZjepwfTGb6VTyb7rh6u2hZIQs6wjnCrqckRQbn3tlUSCr7TWwN43j9wKGypb7EnYfnQNszutjrW5EZP6xUAp-OEQxV7id1KVwkaD2eKn9bZyGRLgsPf2Shfuwddk3eO7_hkIkOUvBXTR40JGC0iM6nGfz9LSQWm-VlSgYFZLtWNvNhfxbyGO4qz6grItjM61bUuO7KdcOEYowx8nQoZh9wQn3zEuBv6-eTTjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رئیس‌جمهور در حوادث دی‌ماه گفت اجازه نمی‌دهم اعتراضات به حق مردم توسط بیگانگان مصادره شود
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460119" target="_blank">📅 19:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-text">سهمی در لبخند دانش‌آموزان نیازمند داشته باشیم
🔹
مخاطبان «فارس من» با نزدیک شدن به آغاز سال تحصیلی، خواستار برپایی ایستگاه‌های جمع‌آوری کمک‌های مردمی در میادین، تجمعات شبانه و نقاط پرتردد شهرها شدند تا خیرین و مردم بتوانند در تأمین لوازم‌التحریر دانش‌آموزان کم‌برخوردار مشارکت کنند.
🔹
ثبت‌کنندگان این پویش تأکید دارند با همکاری دستگاه‌های مسئول و گروه‌های مردمی، زمینه مشارکت عمومی فراهم شود تا هیچ دانش‌آموزی به دلیل مشکلات مالی، آغاز سال تحصیلی را با کمبود لوازم ضروری آموزشی تجربه نکند.
🎉
برای حمایت از این پویش
اینجا
کلیک کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460118" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ec2c47be.mp4?token=KWo73aes9XBRp2f5YJhLzlfxSzXXBS50xrbqLn5mt5SmGmixS3XJFdukOcF3CGbF8oX5nWenp3o1BDZ0dPvQuLVo7rk9qg297TSPBcnFnrJGhJjb3mYii3gctUKU59K8pBYkvvdBgfyEmMfc0bkcO8yK94GmNYhVNzL0GXfkFIAbrqrUq2whccDmFN-MEjLQ_tM34LPoFgcEZtVFjoeK5Yc6NM8qJCgLhp_D7bwXneCBwClMxdwyHyLRmmo8lOAYISwq0ip2KxVpLs5cS7KXCdrkBRKNlCn0TlLTt42x8vl4ATmgiT1YhjUSM3rq6JqBEDdMg6zPhBOJdmFqhiszDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین نقاره‌ها به‌مناسبت سالروز ورود حضرت معصومه(س) به قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460117" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آتش‌سوزی دو کارگاه بافندگی در تهران
🔹
سخنگوی آتش‌نشانی تهران: دود مشاهده شده در آسمان مرکز پایتخت مربوط به حریق دو کارگاه بافندگی در کوچه برلن است.
🔹
آتش‌نشانان در محل حضور دارند و در حال اطفای حریق هستند.
🔹
تاکنون مصدومی در این حادثه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460116" target="_blank">📅 19:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbaf95122.mp4?token=sLnPOFCDTz4IyHfb8nOxuRODyA1bE4k2HMTRxRMKvVKQzIvVDYrsvDw6eP1kQrWsuTfU0vOOVDcK6ftsXrmmAxXPSeIGyyYkfP7iDP_g3upgzitCFEkyq1igFan6NKDEXfgDGmiP3rm9sfV9hCe2uF6KE1FiRVQzX2VoqRYQfvexUlMde1374BwjdV0Lr1PQNLdW_y84RXn_3QtnVU5UypgqXsr5gearQfN_tblR5YD2u8ELJy9ZH9eo4Kz8b3BpjSaBBCKrqtvE4AdGmBw0BvwWUPdyY5oBhaQuN2v3GJ3aI4HySJkUur7n1ngg5XFVi_cQ2JRJaT7mRgFwOZX0qTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع ۲ شهید حملۀ تروریستی آمریکا در کرمانشاه
🔹
پیکر مطهر شهیدان رضا محمدی و شهرام جعفری که در پی حمله هوایی تروریست‌های آمریکایی در شامگاه ۱۰ شهریورماه به درجه رفیع شهادت نائل آمده بودند در کرمانشاه تشییع و دفن شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/460115" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F428kHqpTJgjWQVR5H0KRdUouZ6jZPjk3Y8Mx3rIrhlzQZiPsNO34XU0OBafYn2NZ3Y8og2ybtYX0Brjeypkv38AKOFUFTVKxxZ94oYbBnBD1TMigQ12sWetD-2BQKTX3Lt5J-qtAkXSbsKxvLDGuTelZC7cGZQANOljmf11sVRPp6jDoGcjKyKEyO-tEW9xyQ79hQYnbycPvRc3NHgCivh_5ZAie9lAPBKnIQDdurdHNjPPmDZdAUZh_OlxWmdICNiXPKDlTnIeU9maqHmu4ccsiBz3Ef_KWRL1kkb0cc6XUtA9w10kLiSt9xV29Anpi0WS4j0ydB7HnMlBShQRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های لبنان: ارتش اشغالگر اسرائیل به یک نقطه در شهرک المنصوری در جنوب لبنان حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460114" target="_blank">📅 18:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eee7887d1.mp4?token=TBznAoYcuOfL-RnB3Uc0XnaWzCfRn1pFN6zg4m_RpUyjTZsViS9Ft5Kc9VeW1Th6V3i6do4lICLsqIezwEGmcozTTYHFrr3q3qw5qnxuP4le6SQm3_BiR2YWj3BO2S_Gy2M5U9etnVnuFLqIbBumcsVpyLC2OWNqivBpG8JgJ4mFD7dZNkNpBJL-5ejOP4WI8ohPluu7Mg6E6t1eJ9jWZ6UIS8NG5wlhDce_WoHQ_2wywulJmRXDSUav0ym9J63g7e8hJxsFHrGMMOtKlFxl61S1agDvbZhzkfvefaw-fzvnQ2muWkfacI8gvP6NG9sXl7YkcyeD__hqRqgGLB200A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قیمت نفت از ۹۴ دلار عبور کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460113" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBaz9A-S3eLXxb1GZfUGvO_4FMoHqh84In9O2E36WNVgsFswbRZEwIhcBrpsnAYYy9kIaigGLp0odp-JYGZ63zSE5Ad5EYEBJYh63g0JLI1WKvqSqRuIo0skBAD1bIuu0mghr7gASgLQGv-HffJao-vdYzdbv45bLzeV4b_8pczpwZdOJEFuIx2OSpIHUVY379JtNr5YxoEqU3YrElCuCZrBP2R1OJZw9WkpKaYhw8eKqqTuQk5ZNebpl7_12hk3jZd4xMABkHMxNVR2119LvIkBVRD43Rr1KFvA7-42o4JCIP0S70rb_aSlEF8bpMsi0g4varrW4go8xECquyTdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Ufa0Ps_VtE3e5Xya04svDqlBFoMtw9y9qbZbTDw7dqsedTXECJlvF8KkCYFkUWi16SnMlVAt8vrnKFHsSu0HUM-bqUZ00bslVJRjD_fuK3h6rYVc7Rr4Tfm2OCtGZ4_GfgyAtmZ6NM2iJKWre_R9ibNPzsY9eilOFqIfaO3iG8OT7qiwndjpQQYLAyN4eHTs-UxDessntUUQozZxJzNXgfJehsoTEet6NxVzWX0Gr0SKWL1dnvzcp3wqe6d66YZY1k2L8psk3rI-ZFRgWoK7nTPTFfI5KBGVle8NPCnpLCmUMR5H0CXSXj0aZLheGq_b2DDQArToKSM8woZNTMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gO4n8Zb7mzw6fanQHjd-AT7BAIPYb2yrO8Xo6dCdjGFxjJDy3ji98ElGJpGPVJCwAKfRQycgIATCJ9ebAITCYUCX_oZzJFcnyNYOl6AE5WDhlc4jyIJwAvu68ckCl-xn5ZjlPRCVwYxSWKJQe48YIpTFodniI7khHMOo3BSEjB5YPt9mUEjMy6OM5FAHY4zIdDMzzs75MjlA818jgnQTAXRUNkErTl0t_sob_Ctd0PnucjtbinsIyUU6yE03l4PZY89gR5sM20K7YcKA7Oky6tj3jGKU1qZ5F5Fo7SnWQ4Gn6ozCGjinlIIwfgNo02ZD560n7tJGFrAgR7htNnpkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbBXyYieGIpqTuQ--bH8dSNJdOa_f0FfmiTxFRUIBRebCfwhECo9OljdUd_aeN_DCM4oUEnQ81L3A_pY6MssX9FwPJP-0zvG4C5mDIW9J6owPNMaZkDiEZWL4VbcdhLLlz2YvscI1B7FBRlHvRagZD176snTqUqqLbioRF0oHggqYNduaR-JCxZMHPhiGF6J2ycHXpxUNChkaDph9QukvKyGRwCoqngMaiDcsrmrrhFg-XXBv0-LpH7lUFXH-X26Pua_hNdzKFdZ2mzsLEQQSzow6HRFpJgegl3Vsf8V0g7A-WK9JTUFm3okvJVHOZLgQ95ZQ5KS8pz8PJBuuNSVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHF3N030Dkel17hyBQ0BVHFiytsiZ3REBzn7m_iEfzcNzOJXw4thh-sqWGwIU1Qos2PhttXkHRl7vbJhWGgzGaRSHu33EeM1d2SSWCTEZWsLhITesHhsH4D0jDXM3tauDk9BSpWBvhV9yQ4P_brglOtgaZ3kmT9JlxGAj9KvVR_eWl3rkemJvzLGmbUhgUbL47oaxHl3od2w9bYsOS9VN6pqnSv5Y9nyHT-d2WuAAdOE0Wf9jN4wITIH3M_aEPX-Yr0wCQ8Ea4ERYgG4gIalX_YnmAmk9C9_I92LZOwKewqJ3E-aMYu5mMroK4a6buN3SrHeEvymiwlsoyhhiN5fjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از یاد نمی‌روی که نامت زنده‌ است، ای پیکر آرمیده در دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460108" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad405b00.mp4?token=tcca7OSG1Vcl3XFEt9yk2orY6kw7FkgkKhXhGMk6jnj1bFvcB7D4-KGKS27kgGQ_8Qq_ClwOaayTOu1YTutyIyXHM3crZRfhkPr9QMoxXXQcnpun0ODYKrPy_yzu-g3pN_yeAikbp4WaljMr9HKxZBoSnmTXJaSQvMnnUMK2op7oFaNMddzkC5ywOVtT07V6JA9xx6oseePsLRNBgcV6ERr3yMGm_Jzpi-r2m5E1CATEcD_8UeYrd6Weu5ufOlFL-WYI2M8DGvHl8KuQENt1mc2v53y-1gTmy3JaXjoHsX4BVA_dxH4QUd8tLACLmR42THSjSi_WXhLKIqCOfiK9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای:‌ آمریکا دنبال چاره برای خارج شدن از باتلاقی است که خودش برای خودش ساخته است
🔹
آمریکا و اسرائیل در سال گذشته و امسال همه توان و امکانشان را گذاشتند تا جنگ ظالمانه و غیرقانونی را بر ایران تحمیل کنند.
🔹
ایران پایداری و استقامت کرده است و آمریکا به هیچ یک از اهداف خود نرسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460107" target="_blank">📅 18:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فردا احتمال شنیده‌شدن صدای انفجار در قشم وجود دارد
🔹
فرماندار قشم از عملیات انهدام کنترل‌شده مهمات عمل‌نکرده دشمن در برخی نقاط این شهرستان در روز شنبه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460106" target="_blank">📅 18:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVVD1UThQ9HhHBfg4kYBaqZ-KdoTB7gST19CWuW_FnHOHmSDywWmeT_zYu2ZECRPJLDk50H65AWlrDSaRttcFg0_SFcAniK1n0ytG8vDHg6YehX50pT_J5nIc7oBYXCr3NROQhAoDB70iPCJnaO9JWSdxeAvHmW_XeNNS87gcotgqcGnIQ4wGzQu0oUtwcE4G8D1XNifu5suBFpU72blgd0qvlwBQsLRuvFDnQ_bZWsGmDbl55gUdLqmqmIFzx7wYSda1rUdABPPvb_kBaAO6O6E-Y95lyBxgwnamtEdwq02Kum1blHKliikhY5y-071NV-sUYko5Ykc9rmWV6s40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: تلاش آمریکا و اروپا برای ارجاع پرونده هسته‌ای ایران به شورای امنیت
🔹
خبرگزاری رویترز امروز به نقل از دیپلمات‌ها گزارش داد که آمریکا به همراه سه کشور اروپایی موسوم به تروئیکا شامل انگلیس، فرانسه و آلمان در تلاش‌ هستند شورای حکام آژانس را در نشست هفتۀ آینده تحت فشار قرار دهند تا قطعنامه‌ای را تصویب کند که بر اساس آن، این نهاد آنچه «نقض تعهدات ایران در زمینه منع اشاعه هسته‌ای» ادعا شده را به شورای امنیت سازمان ملل گزارش دهد.
@ Farsna -
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460105" target="_blank">📅 18:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکا ۳ نهاد مالی را به بهانه ارتباط با ایران تحریم کرد
🔹
وزارت خزانه‌داری آمریکا سه نهاد فعال در زمینه مسائل مالی و بیمه مستقر در ترکیه را به بهانه ارتباط با ایران در فهرست تحریم‌ها قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460104" target="_blank">📅 17:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
وداع مردم بهمئی با پیکر تکاور شهید در زادگاهش
🔹
ناوسروان سید مالک موسوی‌تبار در جریان حملۀ اخیر دشمن آمریکایی، در حین انجام وظیفه در خوزستان به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/460103" target="_blank">📅 17:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhtZEwNLVUh274EBN-NwfPkhk_lug9L-ruzAQwtXI3duSSCwKQ57i0AmXKN8yYlK5pMRlskE-JnvY4H1TlulKW6M8E-CW_qAFjUC5U2Av6A_U62mhG7vQsO0N-UV90Ha96DN_W4-cB2lR_zTEmktEVtQd6mMPheUPqsRNnsixfIdAN6YAxA18hicx2KTDAQ-xxYBC_UrHP1p5q2gL59lUOnvnb0i_yL90AFn6XYIOw4e1B1ACLzn0Oy-ddHb-NI41tH4yCkTBHr6URVuJsGoRgS8iUn5_bjkqGQmOA3ysQ96jmbEQdLXBTWdAedKQLds4Mu6ozJSK-Xeeuv--ghXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: اقتصاد کشور را نمی‌شود در اتاق بسته اداره کرد
🔹
حدود ۲۲ هزار همت نقدینگی در جامعه سرگردان است و باید این منابع به سمت تولید هدایت شود؛ اقتصاد کشور را نمی‌توان در اتاق بسته اداره کرد و باید از تمرکز خارج و به مردم واگذار شود.
🔹
دشمن به دنبال شکستن تاب‌آوری مردم و ایجاد اختلال محاسباتی است، اما بیداری و حضور مردم در صحنه، محاسبات دشمن را بر هم زده و نشان داده است که سرمایه اجتماعی و حضور مردم، از عوامل مهم عبور از شرایط بحرانی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460102" target="_blank">📅 17:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtJpHUMWopzN_KEocT18TsGeeCVLqEExuBs-P71NG-5plyfez8GnymmcOIVSVDQ_tBf-GGlHmOfS2e_mIv5sDqdA2udD6pp8dN-CQmwRs_HI5loG7g_DWs6uxYtVHROtvDQVPF11okq-lY1khblbebxRCINAr5fgvXp1o3BID0Vgv-vU7ahORW0fGDV7pK_tm_00bAfAy4zIt6NUe5V52qOXWHM3Bo6JeAvhbcjJLNpkBShx50howKOS5Z1vEbvzoOrNjEliaP9WutblqBdQGvT-qyAeblwitOR3KRg1NZ9RuQ-H_-TnFTlbwzmxKHADt83awNth1ioIvFCgVjzvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ اولیانوف به آمریکا: واشنگتن حق تعیین‌تکلیف برای روابط روسیه را ندارد
🔹
نماینده دائم روسیه در سازمان‌های بین‌المللی مستقر در وین اتریش امروز در پیامی در ایکس به درخواست آمریکا از مسکو برای دور ماندن از تهران، واکنش نشان داد و تاکید کرد «بدیهی است که واشنگتن نمی‌تواند به مسکو دیکته کند که با کدام کشورها روابط داشته باشد یا نداشته باشد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460101" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOnBkKnzRDPYN9BEVnwdBILC1TeYPAcPR5wx8xWO_TuuqWneehX6k-CdiFo5oSdKqPMt2W5Oz7H3QCvhPoHVz4NsSNc_FhxKKLWuAW-KXI6UiUmtjQKHd5XD4cx0cYHYkLprLTYQ1flCnd172ahoWyl0-eloLnlHcHIROmPSSQMN0GRbbN3GBZ-V1D6LyX4QOBirTcxDn91uTja7HI8BxBM87td5V5ylaekqqxBWb3O5Dg0znSOL7c46zg0fdq8SH1fwZqINoWfHbn-AFR_Ck-BuGNhcmahCXvzx6V17sgCzfEkU-A-Onvr0quqxERG0zymIDmPDqdelSKSrBgNd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: متروی تهران تا پایان جنگ رایگان است
🔹
متروی تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460100" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXMae0CTLzxQguQzslQvX0W2_MbRwELPLgoiFaVftB7cZ_0Fr4NwqIgDtMDhX6-YvGWe7HAWNlD8R-DctykP5okFLrpq5JITRD5memsVPklOk02KhcwbEhiiE7WGuG5mNbQM8tN6jlfUre8O4NbbPpDwQaNLcD_EqPpNBQnzJFj6VasT9DjCtIhr0y9H5svXOhMM-8F1zxSDfkJveVinqHom45RFsbXsPM2pG3cVurLnTlBzx-LPyKdk_Z1xj3G3d9zfBbOe7Bwd0M8OcDHdSCcv5a5TTH6Z2qoV4KFf2S_hdIi3JTy9IHT62RM8jMOJk2TjD8XIz99oZHLOO-fNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار عفو بین‌الملل دربارهٔ خیز اسرائیل برای اشغال کرانهٔ باختری
🔹
سازمان عفو بین‌الملل: رژیم صهیونیستی با صدور دستورات غیرقانونی برای مصادرهٔ اراضی کرانهٔ باختری، سیاست تشدید اشغالگری را در دستور کار خود قرار داده است.
🔹
اسرائیل از طریق مصادرهٔ اراضی کرانهٔ باختری، در حال گسترش شهرک‌سازی‌های غیرقانونی است.
🔹
صدور دستور صریح برای مصادره زمین‌های منطقهٔ (الف) که تحت کنترل دولت فلسطین قرار دارد، شامل این اقدامات است که بسیار نگران کننده است.
🔹
اقدام مذکور شهرک‌سازی غیرقانونی اسرائیل را بیشتر تثبیت کرده و باعث تضییع حقوق مردم فلسطین شده است؛ فقط در ماه ژوئیهٔ ۲۰۲۶، ارتش اسرائیل حداقل ۱۵ دستور برای مصادرهٔ زمین‌هایی به مساحت تقریبی ۲۰ هکتار صادر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/460099" target="_blank">📅 17:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460097">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf864b3c6.mp4?token=q8Bfkr7sFmAZHMNyMUO9zpmYw3qSIQnYCwrcfQ97tQXjkQwb_fkfMRkAY6RKGwhkzpk0Sf1Zg8JgbZgZTPAEaSKJaZEBlXxjyO0NTJ-j1TQzgvL8-ln8qmvL_QbNf6y7wGuPbM3hy5kIKEDDwdQtTEit5P8RaNFeLtv1a02cSvJrA7zrPV5qEd4q4ksZ44nMhhb4gGmg9gwVm59MmONdt5tjF2mDaSBj9RVjdIuKgFNgp-NwV4N5Bal-XfHBdiQcoU9XQvLJQdENh3A8Z2PruOsAaZ363Q2nGiB3y1mMY2SMQrV4puycheVzlEYVWaeLTAxIpc7YW9yfaDYUQpOzs4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌دست کردن رانندهٔ کامیون در لهستان منجربه تصادف وحشتناک با قطار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/460097" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxCAZQSwk_V0WFmacSJWXElkkCL7GuSrMiGKjp4tck9EKPbjk57vqyQ5a1AisDAluA0ZZSG8xPESbXy1F67H6kYjtYmN0LLbWi-azjmqNjcP_SFMkxOyMDLcXc3NfgEklNywLfrOrplsZgkjnja48pHWp7hIouFAtDRlq8KlSWnCKgxjiwFcTeoBndoZpsN6cKmws06XnVx8pyONsGOLIoSk7il2j7YBi4kGp6OABVoNiGb-VqrKWhvJ_H0QOGzqUjEvtm20_An2kU0QeRw1T9pJ-CGocrWkvQhlPvUnPedG2fbDuaH1LZoLz5358JSUKO10HSlkQg8loKGfiLRolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرستادگان ترامپ عازم مسکو و کی‌یف می‌شوند
🔹
استیو ویتکاف و جرد کوشنر در حالی قرار است فردا و پس‌فردا ابتدا به مسکو و سپس به کی‌یف سفر کنند که واشنگتن مدعی است برای ازسرگیری مذاکرات ۳ ‌جانبه میان روسیه، اوکراین و آمریکا تلاش می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460096" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460093">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16a6c9629a.mp4?token=PkAtGOYGHXJidoWaA9UAaCijOL5ynNdNilQfzSi9v5CRuhJKWp2sG6kpNv1UMTp_bLXiwX7ztpeXK4gNnZimNIDspiovsfJxkzU44O_lS5TxlovzTbk83GdmuztNTQ41kyYEuPFKGHYe9D2JT3zGvjqf5X4H_W71RmPYJYtzcfOBJ8g07UXSaK8fKUb89ciDrtGLE1HZg8BZ9cyLaxLp0BVazPAg3ERPVeSBBYj31XLUj-JJYlleKdo8EqL7YguUeIA-2crUBXfE3o8p9P1oUnpHKnaDT2wftFTa1btZ6pnhdC6yY9qYjHcYjr5rTsWsn77vWFlsbYr4bXBHEsFilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند،…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/460093" target="_blank">📅 16:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460092">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4176b4afb7.mp4?token=pdY3DLd1S7egaPaKayQOKu6JZIMbylvD3JCv6hh_-DRWosWKHZ9NA2iLCMfk0PCMLfGK-Mll-_iUKuXqs03LSvmxSrsqbb__7Fv9v5qMq08cpcrZuZ0_ZcBS4v7nIDrHYjdU9OpToJPRAt0itrSZo1MkQab3LhAhjhA6DWI3IuOVd8Keu3xAuBT_NoGz9xKn6nEvUt73a8XnzvHd50THfQyFWAiRU9pGnhRxdaA7veFainy0m34YV1mj6q-Iv2K2zgn5RmnQsVdPfC2Af4V5Xgm_JEf6mIM1RlDE8hhN0NGJjKZWeBjoVkV2EzN3WO1Mzhsn0ok5JR6gT49qrM_dEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: هرجا احساس تهدید کنیم عملیات پیش‌دستانه انجام خواهیم داد.
🔹
دکترین نظامی ما پس‌از جنگ ۱۲ روزه به‌تدریج به این سمت حرکت کرده است که مطابق منشور ملل متحد باید از جنگ پیش‌دستانه استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/460092" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460091">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9986a958.mp4?token=orx1vw2s03yHYWM0F1cikakgfYf8_TEKtqwajDt4cGyco9qnXGKTJBIIOfSnEXGMahSlJ2f0Kj9-lcHbuel1K6Dox4TZeO8EaDxfDxZzCC5nLVh3ri4G-smPqevwVg8vRBF544RWJAwkp2NdE6qGSNPFz7Ci2B4QO-gddq8e3WFGv2tsT4qI4ffTDxFq-2iUobKebSm3ksfW2ffIZxmvomyrc0yE8IQmkJp6_F3JWrp15SB0B3JV_BitUe9fegBcG6GsfrxZUz9wtGcfchtLlSgQLevjbl36mqbjAYQQ90rYlcySQxk7cGsU6jcKP8pWdQ8f7BCWAS2uBlfVIOXV9oPUhNQ31bGFBU_UnhpQp34z7LkRwXq0ef8amjt8iVg3__IKRKxPxmRtOYLdtdfKADXvQZSB3l4VgbNthUqdhseCKsRx2FUjPn6vXxLP6qEJ4oBW5VlmA99ZQNGjc3Ti7qWDayolcFMT-un3El3AaF-6zuOI55pXHK7_ovO0HMi8RdK-VyQS4KT36kaknX0LOCi9v_PVJBObq12cUZlF1Sqvue-oIl9_Sw8OfM7cm57SdoPQNlIrNp3pVicUHV1F4XLPX-AQ754Yz_ILlE3fRIRS-nXzq64cd7YT9QphwltONedOiFF6MkEFZ3EuUY__rE6yHJuSQFduJWDRxPPEJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در عملیات‌های اخیر علیه دشمن از موشک‌های زمین‌به‌زمین فتح و پهپادهای آرش ۲ استفاده کردیم که مجهز به هوش مصنوعی بودند.
🔹
درحال‌حاضر عملیا‌ت‌ها را به‌صورت ترکیبی و نامتقارن انجام می‌دهیم که آثار بسیار مثبتی داشته و توانستیم به‌راحتی اهداف را مورد…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/460091" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460090">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75ddce6d63.mp4?token=f_0derLBxDud0fLOx6VCY5592_OXg5D-NsvJvxZdXxk6DlmB6_VZyeh8VJx_YuyvoDS6Wk3NhWekylqYEXiCvED58EGLvA1rQ71DrAdB2CjRbuSdjb3lOArm7yrYLBibc5h96j5Zq1aW06xhpduMmGEk_TlJCu9PO282JEjy2kvZU3b_W1CFZAyepxnx8qQsKciKZjc8ZB2jVZ8MrqEmDVxqvzX_HphL74uwgbojfm9ao3vvoLcdrxYpDAiS4WqZ_o_RwjrlgXPRP0kvs0qPw-Qpny14azv_bMel-l5H3nhbw6_PXyK2qe2PKjUKwJ4tAgzOrluysW1ppZV6_kWx3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460090" target="_blank">📅 15:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460088">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7c7a6a7b.mp4?token=QuevQJczxhrlQqF04kkoZzWTFB-DUqXeHxflM6VtPQ6vOPPqXaJGrJBsVjOJl5dUsn1bvonESLWrHbJkUoUqeeH9EX4_np-lxgvNILCBAExLGNzhF9t8G3OPl6t2j5EDmxjLHZwoKd_iTzJAWHWvyFRI35pZWh-wcmWgrgVTQ1m6ep1nOHmHWYjEznj1AHFW_7YNh-iYl2tCUFNAE60OweNKPHAOMXsasf56KGljbSRERVVlnDM2OAgVsq4KV-tvsYs7NajT_4cNyIbZhHXYu_huPrPHIHAdinAFTzTp5zGC2d5atrceImss7B-QfMi4Ud2OaHAokTbp96uQj_LWGKUFXC3uB5rELRSXoUbYjEPrP80rDC7mXttRZYle17N36RwkuFdJlOfFVR6EbhAR38Ym9fQJYdwmUK0QJPmOHZsURvvgTuLZHJFDfzxdt51puX-mDeGx84y0LL9t4IMuNxWAfWvghStBNa7ru31dagGDyawQg6o5Fwd18jE5v63i_k4UFlJx3KkxprlnN6cYTLa-ER8DkweUteG4Q1V6eOfrbp-1i6WsmyE1lNt1EJRipA4rEViMEgTQBs3pGPJcRfq2jtbU_ZkKjJ1VIQnVt6RzTSv41sSDzNQXVq5iH0dKEBVE0PI_4nGR2sLQpcnSymPmmaTC9q-N0lX-rH1yv-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در کمتر از ۱۵ دقیقه به حملات اخیر دشمن در جنوب کشور پاسخ دادیم
🔹
آمریکایی‌ها سعی کردند کنترل نیروهای مسلح ایران بر تنگهٔ هرمز را تضعیف کنند که با پاسخ قاطع و کوبنده مواجه شدند.
🔹
در این عملیات‌ها پایگاه‌های آمریکا در سراسر منطقهٔ عربی، از اردن تا امارات، مورد هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460088" target="_blank">📅 15:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460087">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a03d5c8d.mp4?token=Y5ZdS_rbrbVQdtij44w310tV0NbbogFUt8U5WAAPVuKSnzs0ph7u-HN2KBIRcV5v0kHh_W1PR7A4y4gYOfrZzOEx-_v2rAwYZ638OnbCSUnk8z8OIRVGXtbVGUSN0hE65Az1cqn53eT7P4dFdBM1ki3e1980_zX-7oOIEIOZ3rQbiZou8ZCLObgaw8zKTttwbOc8-zrOSeoEz3XiuelwyUVPB1A9c2mCDEiEPPOVv5Ka2HtyYFpTGoMSDWyN_EAF0mDB-HPGP3jFQXaV52MVnyli1bczOoGQq5BslcTKASM_r5iAXIOD6haQ4n2BJZwqK8BJZ9zRhLRRMy1vabvgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلفات سیل نپال و چین از هزار نفر فراتر رفت
🔹
تعداد تلفات سیل مرز چین و نپال به ۱۰۰۳ نفر رسید و ۴۴۶۲ نفر از جمله ۸۴۴ تبعهٔ خارجی همچنان مفقود هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460087" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460086">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn5AlHGhYchdv6rnEa6IIU9IwaMiZg2ST8wxvS1kgoO6RkdBYMKJkTEvjyD6mDhmi7ue1dpkNXGG_EZ-wMj1rI2NdDR1Jfd0CJVoGVh0WTMyRzm4CzMpy_LzW28P30VDzSdd8WJwfUIJO8cWN-ZRiWAbOWq4cyPp8ys0EBWoOW081qoG3vu-Ws92k6MkyyOyA75PElwU-lZfn2NK4PZApSKynK629-U9_LN2jSWWfi0ZrvSGbEYgpIIAVtxYAUaA4PFo3_Rhv59_UgwS6Ng0WQ8QXB3qmFvoVe4FkzHizuBdC3128D3QUukGMcoiYM4iwK35-QqEnKcI3CwkoSygKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
افتتاح بزرگترین و مدرن ترین تم پارک ایران در مجموعه ارم با حمایت بانک شهر
🔹
طی مراسمی با حضور جمعی از مسئولان و مدیران حوزه گردشگری؛ بزرگترین و مدرن ترین تم پارک ایران با نام «دنیای گمشده» در مجموعه ارم، و با حمایت بانک شهر به بهره برداری رسید.
🔹
به گزارش روابط عمومی بانک شهر، احمد مالکی معاون اعتبارات و وصول مطالبات بانک شهر در این مراسم که با حضور معاون وزارت میراث فرهنگی،گردشگری و صنایع دستی، معاون بنیاد مستضعفان انقلاب اسلامی و برخی از مسئولان کشوری و لشکری برگزار شد، گفت: بانک شهر با سرمایه گذاری و مشارکت در پروژه های تفریحی و گردشگری گام های موثری در راستای گسترش فضاهای تفریحی مدرن و ارتقای کیفیت زندگی شهروندان در محیط‌های شهری برداشته است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/460086" target="_blank">📅 15:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuxAnRUrDndgISjXaoEMKc8Mx1JtT6a1cb4ewESUBV1U3EhCu1tKxarnlj6K2aw-dNiqVbQyxjw_z4L5lPwIUTkLoTHLBu2LWEL8IQNLGpTbtBw9_Jg5qvKWexZf5DiDnqRbbNAOz7kTlfHCPJx0JDOeE7BWKrAM8xcdN6WdA8F16URZgGWjDaVbp8m_OfkrYZiATfVB0E0eJP6LVCAgRUYxf49oOjpKFl-69HWAmnrFGaS0mCdVHquePr14gmYJFC0sQIbyK3ssUvps76ydI6dsqnGX9ADxVFQ8b3qSr-JiFhxhwYIjJzS0aGwDZ17qMKqfTCcUoh4469Vejf6S_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽
رشد ۶۰ درصدی ارزش سهام پارس خودرو در یک ماه گذشته
◽
حرکت پرشتاب به سمت افزایش تولید و ارزش آفرینی
🔻
سهام پارس‌خودرو در معاملات یک ماه گذشته با رشد ۶۰ درصدی قیمت همراه شد و در این مدت مورد توجه معامله‌گران بازار سرمایه قرار گرفت.
مشروح خبر:
🔗
saipanews.com/news/id/24634
🆔
@parskhodro_pk</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/460085" target="_blank">📅 15:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/460084" target="_blank">📅 15:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYfK88viWClHnvFTpJ7IU-gHjsysOtpSJOuVuK2pWsMeEKvSJ8fnFGb8-ah5Lh6zredQ3rzKwWk8qoLOPhOCmeXNFwbq3oomCVXXloZ_jFyavIWYEoo0PBM1zNdA53ovMsRp99JjlHk3MnE4VvnbldTAQRoDAEz127DQJZ-xwR0E78cUPvEln5EcDCNeJbcZ_tUkMkIhUnqfEImQp1_WEIJ0mrggKl_Ru4tbi7akWF0AFGCfzLGhvwYcBDgp9DzsFS-TGzgBlRR4rAw1A4MDjj4d1gp4IPApeAeLv-Gr7zEHmEcNeh2CNBnUvWY2JdeThCJ5ErU3mUSK6GkFUWqAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ارتش: راهکار مناسب برای آمریکا پرداخت هزینه‌ها و خروج از منطقه است
🔹
امیر اکرمی‌نیا: معضلات ارتش ایالات متحده در منطقه و مشکلات مردم این کشور، ناشی از اشتباهات مسئولان آمریکا در تجاوز به یک کشور مستقل و متمدن است.
🔹
راهکار مناسب برای آمریکا پذیرش واقعیات، پرداخت هزینه‌ها و خروج از منطقه است. این کار منطقه را امن و مردم آمریکا را به رفاه نزدیک‌تر می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460083" target="_blank">📅 15:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa_Y7Wa9w0c2OsBVjTHD4KU6fnmFzXl1icpxBJ6fYEFdV5dxWPH5sRyeF-YcTnkQmK-AwZHVORrzd0cyQ38XTsl3DblPKGmdXykqeHNLyV4Bue0SmjguanT-Gke1DhdOlJb04equUyT_ioSOcnKnLSXKzRaqLkNntTbwxQ6xshgBIt5Cosn6cjMmc4P9XYGauVKLVBx5MGSvQk49tBqfnQ-1kUVgYD7dNn2N8utZ_I3fItaMutG1BNdQS1aM-wgVbj9l1foHtu5nQYxZqhIEfEwn3PtJCpPe1QDSfPfRKjinEsLjmltZVgQtTS1t-QxqaTuEz3zMydqljMdbr9PhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور آمریکایی: وزیر جنگ دربارهٔ حمله به جشن عروسی پاسخگو باشد
🔹
کریس ون هولن: هگزث تلفات غیرنظامیان را موضوعی فرعی تلقی می‌کند؛ نیروهای مسئول جلوگیری از این تلفات را کاهش می‌دهد و به نبودِ قواعد احمقانهٔ درگیری افتخار می‌کند.
🔹
باید دربارهٔ حمله به شهر سیریک تحقیقات کاملی انجام شود و مسئولان آن پاسخگو شوند؛ همچنین باید همین حالا به این جنگ فاجعه‌بار پایان دهیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/460082" target="_blank">📅 14:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32f681c97.mp4?token=fXr0xx7JEuviM0s0lN7da2SCAfsiKDv84RuHJFuuhknfFTbsjZJ6W-OpzZ5G5jQQXhkKysesbXxDplgdsViMXkbh6MzseDekfWlSe8jCIxSu9mpwpsja_A7cVlVrc5_1gcrROMQQTgEzYnOe1U5SbeU3bHwfbXlgDIlwKizf8RWqKTouNOuomNwBlJvoLTs2TgFCb-_PLzUKRUpevZ2c43VZb2bC0wZm9MJyDOn9947x5R6RP6NPsbI8Fnw7gd2mYRlF8WQcGoxj4MNRiKHJSkK1qkdnPNf2qfWGrT8A19JhROzI4gORlxL2U0kaCPMKSVqMrdlk-uUMUjrcoKlMzTMKOhuZWl9JE4aNyzjnXyyIWEH75bVKL-bTYGl5XTevfDZtx_Rzr05kpjlummPReXCJmodFIP8fWiqLtzy4q9CueAsSMwGtiv12rcbV9sNLHwLTUQoCXYpRE0DPDDvvE3FqfganvPGidUISZysOEUMcH_f_SecwImffusIoDFjqP8f8fVHVVwBJoglqK0J2R1ovrL6U6r9MVoaC2WRh09T9uoqL55DH-ORTzds_KuiDlV1fIG1-wXFrlKg1yH8xHEKyqv6xAJId1w2y1mwPD3McKjFNptPFsL-fLqneR5e8ISKekAt8o15q093zN1-MlEgTOPJpLD45Gqmq13mYcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: برای اولین‌بار به صادرکنندهٔ گازوئیل تبدیل شدیم  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460081" target="_blank">📅 14:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzxzIYWYu1JaEVRcwaZ_AKN6uXTImtbRI_Lg4bZnstjvJP0n3mxkHj2duG6hUngS0H7_gtHYZpzhv2mYZmh7iP1NiiRbumC1-xMPeiJ82UAHNPBleEd_iHXsNqb_xU8Zvyn6882dGW9-f_0QzGz4uj0RloH-QdGpGtmrPX85lLYZMFRndLHRCvYWt4YcTxLTD_iX6OeGXDKMRv8Bkw6AQqFuwUO7qErLbFmbwmo6Jv6XzubVpCplvMebbCI5aAGHGDFeSAkz6IQet8cCc83IbZbuKun7KE5wmTotZsPC7o4qp-RD-lLMs4PafkBPSV7CtpfPBqiXTm5JPFt6fPbIRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک ضدانقلاب
🔹
فرمانده مرزبانی کرمانشاه: گروهبان‌یکم مرزبانی «رضا دارایی عمارتی» در جریان درگیری بامداد امروز مرزبانان هنگ مرزی پاوه با گروهک معاند و ضدانقلاب به‌شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460080" target="_blank">📅 14:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جاده‌های مازندران یک‌طرفه می‌شوند
🔹
پلیس‌راه مازندران: از ساعت ۱۴  مسیر جنوب به شمال آزادراه تهران-شمال و جادهٔ کندوان مسدود شده و از ساعت ۱۷:۳۰ تردد از خروجی مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد.
🔹
در جادهٔ هراز نیز تردد به‌صورت مقطعی به صورت یک‌طرفه انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/460079" target="_blank">📅 14:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04dc114a09.mp4?token=nOh3Nh4IHklKWPdiGZXyn2rjCcNpZ4e2128cvrfrUZvdI8IHQWSg-9jubzUplUlg584ECUIXkJmcw8AWNVhPv35IdtIpMFcZPQKyrG5VhLThFmFFW-YG0CcNLOuxnw3MkLcJPa5_2ISGiq0OY6uJD6zj4E1Y1NV3_cfbQ7xKTiVq4gqFrRozNByQG9oMSrLHi9AcIU8w1ak0K33tFjY_s5kCEvsYGfmHQWt2iluAcKBQMx31365VPO-zBdg_U9PYTLHUjySeIA4gNZ5N7zS0W86u8S4311VM9_utQFrZfMMnrWRQ20qoZKxhx6tlS9CsEsWKVdyLzdkrJNsVoWNVkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: صادرات نفت در زمان یک ساعت هم قطع نشد
🔹
بیش‌از ۵۵۰ اصابت به جزیرهٔ خارک داشتیم؛ همکاران صنعت نفت زیر بمباران بارگیری می‌کردند. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/460078" target="_blank">📅 14:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiyJ29QZyFvCcHdbfqrR9Q_ZtX6DFpHoPSdlWvLJpJypzAZcaFU1gUSI01ZPUkcm1InDSv63QiD9x2MZEyR_8Rhyfd3tH2BABJ2xyRAvqs5mnZMmNIqsr6lTiDkwuO8mr_Pr5JvP1X2wH-53qWQnNtXYiJYo_1iyjmBVrA9Eu1yuLOWQRGQZyuaXqDW2dML7UV2RKtubwQyyhsJxH0nrsn3z1G8qh78tfgHNZvSm2QaUOY3GQCV7oqBjgYLeSSH6Bq-XQpHrAYuHZ0w_C9uMv7eHz2-zbmbwCSEiVXjvI4526eX3Jf1URNhyeUW_U-vewyFMlhPBaAmR809uX3RAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: منابع حاصل از کاهش مصرف بنزین صرف تقویت کالابرگ خواهد شد
🔹
رئیس‌جمهور در جلسهٔ هماهنگی مدیریت ناترازی انرژی: سیاست دولت، مدیریت و کنترل مصرف با استفاده از ابزارها و سیاست‌های عمدتا غیرقیمتی است و به‌هیچ‌عنوان نباید تصمیمات این حوزه به‌گونه‌ای اتخاذ شود که جامعه با رفتارهای ناگهانی و شوک‌آور مواجه شود.
🔹
اطلاع‌رسانی شفاف، دقیق و به‌موقع به مردم پیش از اجرای هر تصمیم نیز باید به‌طور جدی در دستور کار قرار داشته باشد تا ضمن افزایش آگاهی عمومی، زمینهٔ اقناع و مشارکت مردم در اجرای برنامه‌ها فراهم شود.
🔹
هر میزان صرفه‌جویی و درآمد حاصل از کاهش مصرف بنزین، صرف تقویت طرح کالابرگ خواهد شد و محل مصرف دیگری برای این منابع در نظر گرفته نخواهد شد.
🔹
مهم‌ترین دغدغهٔ ما، دغدغهٔ مردم است و در تمامی مراحل اجرای برنامه‌ها و تصمیمات، از جمله موضوع سهمیه‌ها و مدیریت استفاده از کارت‌های سوخت جایگاه‌ها، باید به‌گونه‌ای عمل شود که نارضایتی و فشار مضاعف بر مردم ایجاد نشود.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/460077" target="_blank">📅 14:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b853d23c51.mp4?token=Z6kpkb8SfH6Yji3DE8Vj6vVlm5M1wohaOJyVMzBoRqWEfG7iaIdb0dWVdKubQ9G8mK8a8XI4cnGwh35EH-oAJO4IRPcMJ7RkskjKpC28skzVXtuuNUYg08C6GEyVTq09h_g8txRGtwoYxMTu3S21FgiGEBtBAgjNmJ7QePBV0jkz1OWKeMNynJp08lhTT8fC6jIClB0kvAsWQ67yrCSfP0Xt3b8okesXy9VepLI90U6QAWalgF9cFWdZqqewfCK0uIxG6VKyHmglTm_K8tzBMg77pN3Gq_mGkMhJIUyAfNMFYXbrBQazPPmsl-Czw_UIiJXKnRjMFFV_weUukvSExYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نفت: در تلاشیم تا محاصره را به‌طور کامل دور بزنیم
🔹
در زمان رفع محاصره، نفت را به آن طرف دریای عمان منتقل کردیم. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/460076" target="_blank">📅 13:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697c3ea5cd.mp4?token=NY-lfqulfL1I_3sQNfD_kaP5X-djAUyN-9LnPz7HoyXTk2yvEYteLkxZfRlenzyFHlGtm3W_6hraAQ5COgzOqpI1x9HN6W-6Fwh2j2ZUKMRFjB1W_9l44NL9MV-YLsrvahLE-DYKIPhux8Yt7ftqQs9bBkN31M_s7sHH33tcsn-PFg-Y4AMYs-PL5v_LyK0X-jNHQnshKhqKN8fGVnJoTXXqEHZFueSL7FNs7ScX-GwBvU02nHfM84geJQHyGrKKE6M9RguZwqpLuKMZQJJ1bqLuLnOphIQ8ymIoDx8xHI_MjvbYC_JBq7JOFBy_zs255c_4WYniJguIImLHlVLWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر نفت از شب حمله به انبارهای سوخت در جنگ رمضان و نحوهٔ مدیریت پیامدهای آن  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460075" target="_blank">📅 13:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6058e3237.mp4?token=NlaXj3eSfyIDtUDr12RkugtoZci1AJF27tFIBB55Qwuap3ARTOdBSLBaIx2IkC1vOl2o65QN1wRPzaSb42lbSh6BNPN6DwOiPbuCwardBtA2VYyN_tvEB3ikASkiE675-XLjGN1zr4MH6NPXXfiVLqOt000AlLQ1qHr5vScF298UinxycN4xmr5mOsavz8If-7CRI48hGkPsk4QbNtsaAF0QgBA4Km_lqsIlXrhY5oRJLJp8B1Leh6Ae59JyqmephH_xs4YAYfELJWgOR9blq0JYUx2CitQHiQ1qM6hss95HCdGxeIPlfpWnUjbk-dyLBhhktR6zAYC-ksmlTa4rZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/460074" target="_blank">📅 13:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4303f11b4.mp4?token=f0N2If2qUfX5Ns6O3CeKjMgXoOLCvT5nijz3cDVD0XEkf_tyaXNkIVDxWCrDMiK5NjRjGWn9JSMTSZLyXIPjtujmliyjR27Zq1yG9nUuFUmWX-31Xyr20SKpioqa7V-i61c1kIGI2oQjxqf_9lXyFVOn4tDlMiTu7aih9PZCvIuNT5zAZDVrLTn2HUFkOjjZwAbkcZ3-ErliVXWEwOt42soDzE5KNqdKH6ViTSMEQFIbY1vRhpd883LCBY1x5cpSTHhXNtcqTQy3TOBTVs_quoPD1qxrSixwDte4zGywCvah4d2IXtqNSwG1Dgo1dmbKFFsTM0jOgCl_Yv45J8u75zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی و توپخانه‌ای صهیونیست‌ها به جنوب لبنان
🔹
منابع لبنانی از ۳ حملهٔ هوایی رژیم صهیونیستی به شهرک المنصوری در جنوب لبنان خبر می‌دهند.
🔹
توپخانه ارتش رژیم صهیونیستی هم اطراف شهرک النبطیه الفوقا‌ و کفررمان را مورد هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/460073" target="_blank">📅 13:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK-HS5awr-F8iViZrU_FaInX5X54xZn5-FSYkbVCsF8_Godr7SnLaW7q45Fhk3fFtybJLXt4HzyWae76e0-F5heUkNVBQqXP5IXZXpW242lFYlTjE8T3dbD9ZMVKICax04yMlU6ZwklyzUWaS5sFWLn_nvJrdVLEyzAczl_4t6-x_8-MpVNmSaBbnJt_rKftfQk_jODgrwPLcFBRNGFkI7tuq7kQOuDc-_05KaeChdE_0X91CdG34rz7tvVG4hoXA5pULLNFYPTlP_c7GvIO6eNWAsOTJp0Uc9YGjhjgCn-HNN-SwhEIstXF8E_W_mNRyJ9RAv5Tgwh-KRlPe36E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعهٔ تهران: فشار اقتصادی علیه ایران شکست خواهد خورد
🔹
آیت‌الله خاتمی: از قرآن استفاده می‌شود که فشار اقتصادی موضوع تازه‌ای نیست که ترامپ به اصطلاح خودش آن را آورده باشد؛ بلکه از آغاز اسلام این فشار وجود داشته است.
🔹
همان‌گونه که دشمنان صدر اسلام شکست خوردند، تحقیقاً این‌ها نیز شکست خواهند خورد.
🔹
مسئولان نظام باید با کار جهادی بکوشند مشکلات اقتصادی مردم را حل کنند یا دست‌کم کاهش دهند.
🔹
هیچ‌کس در این نظام حق ندارد سخنی بر زبان بیاورد که بوی ضعف و ناتوانی از آن استشمام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460072" target="_blank">📅 13:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhZCkeF_fU_QkzPirZ0bZsYVYvTc6hXHXHvX5PEtV7iAk61Gl5lKbiEnYIKEcn2X8no_7QQ0m9S-CEEGhHdSb4RallpZ-EKtAhItVauML7ybqYBUMvMRR8otne8C3sKQE4M5VaDDXFkVqYaFWQOAZLKoNN-C5kZhO_tcthyvVdU61GlzoIEYZiDz5hYm3CV23EHAJPzPE-JX4CqG3x4B2YZD7uUlZuHVsCW92-QX9qgfUIxqqeQFqo0frlAhXRuEYinoWkdPcMwq7Mj5LpQ6XN6ZUre6nYxCYRHlwqjcmQwBnMUpFUqE346Fy6nDBEAZdrmRLb62V8ez85hfh-0PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۰ کیلو مخدر شیشه در آذربایجان‌غربی
🔹
فرمانده انتظامی آذربایجان‌غربی: در بازرسی از یک خودرو، ۵۰ کیلوگرم مواد مخدر شیشه کشف شد؛ در این راستا یک نفر دستگیر و خودروی حامل مخدر توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/460071" target="_blank">📅 12:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyYenCqZguxfYMd095j5LDWwTAgFiqP13wSELLNEiM2snMrat-pR418V9SY211ZQ-j2TnB_CSssQSok0c7LtOhOnmLubz0T8G3pRX_fJEJtIFHlxGbTYf4-fD4xzcekwTIHjiL9GyNBfkYQ4O1P5VccCdQDzU5ZoRMMEKE-tcNAQK1Cv1gLUylHbEglYIDtLRG0H4etLjX5ufKjo6IPjhgGXHRjzk_UdnIYk2pniihIzBhLSLvpNUyRfTfJP2AcagQQddMGTwHYwmOK15mLGhf5j8-PgLOj72fNZTHr_4Xq16Dq4xS6CtLgRAjlvM2RMLi8_c_iB-bki4bXK5TFz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر الهامی: برای هر نوع تقابل آماده‌ایم
🔹
فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا(ص): ایران با آنچه در جنگ‌های اخیر از خود به‌نمایش گذاشت، تعریف جدیدی از قدرت ملی به‌دنیا عرضه کرد.
🔹
نیروهای پدافند هوایی ارتش و سپاه در جنگ اخیر سامانهٔ پدافند هوایی تولید کردند، آن را توسعه دادند، در میدان مستقر کردند، از آن بهره‌برداری کردند و هواپیماهای دشمن متخاصم را نابود کردند.
🔹
پدافند هوایی کشور با تکیه بر توان داخلی، دانشمندان جوان، شرکت‌های دانش‌بنیان، دانشگاه‌ها و تجربیات میدانی نیروهای مسلح، در تأمین تجهیزات و سامانه‌های مورد نیاز خود به خودکفایی کامل رسیده و جنگ را اداره می‌کند.
🔹
خود را برای هر نوع تقابل در امروز و آینده آماده کرده‌ایم و آماده خواهیم کرد؛ زیرا می‌دانیم تهدید تمام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460070" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPDdjE--GSs6eccXKRF-bi9U38YVmZXHd05_5rVIC0pydH0eXG2MNClOuvzqyzIki87UVNPFqimR5ihWWsUyhrzyXjZxoupZaiS5fhPGJ8zbCKBPPG8afJ5EaKJp6Jea3adlVQ45taJeI-B-VTNK600YClo2d9H-58a4U8PNt4LIIiiuvJUvn0CI-EAfGG4gS_OOH81xL8GFXCQP4l1Xc7dkTnc9E82IzehKYP1MSPjucaG8AeHax1YhkUYlk4893DpXBKdDCmUoKug-AefklZUpj9ZQ_g2A93OHsWd2tj0aXAOWR7Wn79FiUdrfaMAAG-CNK4NJ2Sl59ZeEeUZ38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فرهنگی سازمان بسیج: ۲۹ هزار گروه مردمی، پای‌کار میدان‌اند‌
🔹
سردار مقواساز: استقبال مردم از «میدان‌یار» بیش از پیش‌بینی اولیه بوده و مردم با خلاقیت خود به گسترش آن کمک کرده‌اند.
🔹
تاکنون نزدیک به ۲۹ هزار گروه در این طرح ثبت‌نام کرده‌اند و پیش‌بینی می‌شود این رقم به ۱۰۰ هزار گروه برسد.
🔹
هدف اصلی این طرح آموزش و آمادگی عمومی مردم است؛ میدان‌یار صرفا مسابقه نیست، بلکه یک حرکت عمومی برای آموزش مردم و افزایش نقش‌آفرینی آنها در میدان‌های پیش‌روست.
🔹
این طرح در ۴ محور آموزش‌های نظامی، امدادی و خودامدادی و دگرامدادی، فرهنگی و هنری و رسانه و روایتگری اجرا می‌شود.
🔹
حضور بانوان، خانواده‌ها، نوجوانان و اقشار مختلف در این طرح چشمگیر بوده؛ قرار است گروه‌های تشکیل‌شده پس‌از پایان مسابقات نیز در محله‌ها و محیط‌های اجتماعی به فعالیت خود ادامه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460069" target="_blank">📅 12:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7xsdmUAA0hVjSX0NmNekjWy9Nec03icJOXZaLQHdxui1APBIHeNLuIayL3MP2EdsjqHIHIpst9z7obxRg011fg9uMySjvwlbs18GWohz6s4FTS3_LsUpm8e7JWeJBnRs2FogI-wRrmURGbbK2ZARK2_jM6qdXT1Q-G6SVUI9PyPN3KKQQqG-zey_NEqzwl94rqaQ5-2kacBCwpGfvAeTJLbkpU-0mTeukC0aXfB5ODQQiICJQqr9EyifRGLA0Zabih7qqlnJKTkkT78E512HELfadQMYWYAneA8UKLDQgUaqn808moqIgFmb_mV5jh3kvPNbwOsyovjEHIflljvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای حملهٔ آمریکا به مراسم عروسی در سیریک به ۵ نفر رسید
🔹
رئیس دانشگاه علوم پزشکی هرمزگان: آسیه مولایی‌نژاد، ۲۲ ساله، بعدازظهر امروز بر اثر شدت جراحات وارده به شهادت رسید و به این ترتیب شمار شهدای این حمله به ۵ نفر افزایش یافت.
🔹
در حملهٔ ۲ شب پیش آمریکا…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/460068" target="_blank">📅 12:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JprWMmjZoxYAC6y2NnjabVHSh53IDz33GbRCmKm1e0C2oVbinzZuXkUVj3pVPDcCcYEaX4Qyt73N8HNh-78ykLb2OGlaJohSScX2kwN2bBWv1uQ4jaVAv7RY5xHOy-NCSjH64QU03QXbd4IfbLHE-fxmMxxdOTVkLFI4PVESPFHqbrImHv--0oLRGljt-Iruwl4e-l9TsJDOB9psE0nT0Bv23oknPF5iP-Dyo44zVQ3XaXsMdgPJPcuDMV0goA-foquSP2iFqXOhIqHfHlQT9Uc1ordjOnSDkjViBPLDc0xPDbHihx0XpUlLA_O664qYCQg2BGMqkyfqf8ncUdB9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت
🔹
وزیر بهداشت فرانسه: تا پایان ژوئیه، حدود ۷ هزار مرگ اضافی در جریان موج‌های گرمای شدید که تابستان امسال کشور را فراگرفت، ثبت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/460067" target="_blank">📅 11:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXBnp1IquPJ5mgWnprkODE6YBWr0mJfbzHe9cHSpi3VN44OqVtBKANhqveKyPm2CU8xBw6dSV3XhD2HwTffL9WdnJhXqiNJS_U3mWVRZ6Mb3X_wS5FfdoRVHxLUv2GMyyH3fVJdSRqVTYSZSFkPLk_bP5vEo7S3YUyd2PrkECzD8VtHIJ97oAHpsAAed0s20dSMjapk1JyoE_Z7KAvan8YCYuk7cyegngMxpZ5GR3Alyn1Kykb1_ulFB7xM785QBWQc-_XM-Bm6hjF7GQIaaZRyWZ9Ri5Oj6ZAZqj84josWcR7fXBzoKApilJY7Ivv-Kg14gg6jGLgrqdgXUhHEQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پاسخ وزیر خارجهٔ اردن را داد
🔹
وزیر خارجهٔ اردن گفته: «ایران ۲ ساعت پس از آغاز جنگ، اردن و دیگر کشورهای منطقه را هدف قرار داد و این یعنی حملهٔ ایران پاسخ دفاعی نبوده است.»
🔹
عراقچی در پاسخ به او نوشت: به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔸
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/460066" target="_blank">📅 11:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmKsbLB8AgeddfVN2XkWvBztzHbuCtboM5fP-F561fB4NRtFkg0a5uLMNiat3MLP75EDJRpBians--JnFj9ixq-GoAMpzrFbQkWkwBMlEX5z11Vw-7WWbdtHDU2ClXewLoItrybpy6B_KJ5Y2trQS99dO-C6N9CjC-M0c1XAijcOGYaQbwWXk-VUWv968XxPkttC5HSWmHVmjFY2JCB2kAsvIcVVY2PIo5x_3vkAJ3mAEQCdO2QG_ynNR2Em4r97_WGl4BFADN55CImSpkVUQGcJuOFerGzVFNPneZp9jjtj8TuZPRtzwUwaT0XD31KIAhpBGyoiVwxGCP-cUXEUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامهٔ عبری: نتانیاهو و ترامپ زمین سوخته برجای می‌گذارند
🔹
معاریو: نخست‌وزیر رژیم اشغالگر و رئیس جمهور آمریکا زمین‌سوخته‌ای پشت سرشان در اراضی اشغالی و آمریکا برجای می‌گذارند.
🔹
به‌دلیل نحوهٔ رهبری ترامپ و نتانیاهو، اسرائیل و آمریکا دچار نزاع بر سر هویت و فرسایش نهادها شده‌اند.
🔹
ترامپ و نتانیاهو در یک دستورکار شخصی، قومیتی و اجتماعی اشتراک دارند که به‌هیچ‌وجه دموکراتیک نیست.
@Farsn
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/460065" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJydh2IOJrZJqhyjCCZXuhRdmgGrvQR-jXxAaPnJhwpX94_IVNqScg3Kx4dfRtsDYb-Bz0cZ1S46ApmvvEFcph5qEEAiUVqsZ_Y-kYOLAKcffe5W1zZf7HMgpK4T_5fuTNOHuOTLmtqjSfSKRtP7A8kK2EQNHp5V4WBYq9Nn8N0bhMwUh_xXyCeobN4ocMpwazWlpBDy5WxzSGIL0x9XxnAE4gS9bauY6wibjzg_B62n1MpZ7S_13FsKI20h88FwxDD4N5hnT4jJXFeLjIHGWHiPZOic3rYMZqQYaKMhdth89_0r-1BG9FUXmzALTQhSRjMIpBNX_WgGAR13mGr37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye-pJ5-2klJBhdU3vSvkuPYiRaoONgsRqOuS5wyc3cy-mBNJzbKFLIq1TwKcyAoUqH7xToU1e8aPUMPBZT2fBy4RsvaPbSZsgmMYRKygTbAaUnpw0mUc3fOzCe4k2X3fbhrSXA_B7UNnDLwQtN_KIYT8p7_BwWNDP7EmKnDdWEp-1JLAwsZZgR7xj8EV6w7lqVZMWT5KbDo9D-zTZCLj3LM9p9DjLnlJygLVIV4h7iPrgexdr0iaiy_9QgAoa9np2odWazg9ayla5uUowwaA1hxZpAL8gd92v-RBxU8dKblJffCKm0Am-jhfd4yVGiytOymZtewuSp1FyUUy16GOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A70Qv5XjPz0rifnTJmBIYYGwwojFUB9ZuwIoDic6b2PCB_M5XhNtyta2ryk0cfm7peoQTTtp2vIhizpA6319Wv5kEUY7G2t14EBtA3XZxrsfBv7CJfiYwNCXMw16KxTjUci_IM5aAM_yxu4hBllHus4O2Ni8RSP9VVcTjcBXbfB6uzxkkztsMdeWPkD3_xnIPKWH02xYHWK3oxlkEV_pXfuzvTyyX75O0yUifh1g69-nvZ6Ae83sDKcy0SFuGeNd1xA_vfqCw0ixK_aNpU0nlrak8egzRGKNlR0VknOtd_3zf8jqxCCV0fL3WMftEoMFzH4azhIdPcT4wVeCJs8UhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQC5hJPJD9Wx_aIUzCIFJo0TrGTwQAMeK2rNiJM8mQOL4e-tragWoTxmdTnUazTTC7hTMpJ81C0MufDjo0Wu0OtrFuZu4P-UWLnpstuO3Fbq6O0tCwUVi3WnvosUy7dWCFm2m_e0eD6Z1WXY2Irswjsjnmt0z6mLJ6cwWqHcmAr77yrrOp-SvGgUwye8kRC42-MaRhULZBBPYb_wKfNUNaZKyGckXe_n-lJcw0GasYkFTVEjLfFYPhqRggHwboW737P56I9uV6k9zzCrrKFfOYOZANDdPGSI6U7y3uHx2FkrrfvQ0Hv_BZzDSNqUtZeJM-llU__doc1H6m5xjCOaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuuxsWgCOPaLG1iLND4__k6-VTh3D-BfBdWtIv7Wk-atIrthCA9_WncsQLtOWp6b7dwtRjHG2RdwVNrxJGJqs93jR1DJLwv0lofHkuunUsrRk-3IL-eos4nXO_tVJ4mRmDArrXnLxe-ICLL56a-GZpN39VHRC6yTCFwUloUgmbw7OnFJEBLXZHPl8Y6ngYTbnzgluxYdhzPGFroOcVZagv6YP0-Rinx5-8DTc1FRKpFzM9IeIBKc0MFnxJmboGR41ZbIxfgOFK74eQkeKdDrUoAsdbnV5C14pGoVuUZN-23tDLaIxLSzrEKmFrwTiyN9MhRuNX1vY3qcgqUs3TV2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N15MKBp0oPbHwFKW6qtiX9sMhwIC2jDdtBHSRbH3XDy-xH30J1ok3hKD-2sRklmK_XBiJAEmEe79A5h7XwhaMYz2XEwQ4iThoL03QNpxHiIdwsiLkOanlRFZBNsIaVUJ0b7KdFMZU5YVxUth2INrkesXQlc6lUZnnA-yjEGbJBINqatlDvzDjJbhBNnF9oDqt-6zsnS1C9f4BZmF1s4i_0nRQRRCCX2ccBhK0pOznLQgFD7fpGdrCdicTJZl2kLUatoAdvkILx80XhewQUPGRpXpAe8j_hTLv338eoMg00tdzt3yWm3SJnxzrpBuNGoBceJ5N1CbXyHa3GMN-iHzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJCpk4sALVdTG3ZlrUYVfQdgG7Wt_B4mqguvukntoc9ICB7yf0SPupBWhCE5zdve8oablvp6hTFK8-J9kY5_K5VDCXA_gNuDL2IAAspwnbqYV1-imwPwhcirW1nHRh63vOkhPoXxdAP6htQOx3iVIg6PTMv9UJ7j2f3yLEAMp4RgBrHXxhL3eCI7so8sDiXPkMLjOpv8YHa9dAWtkKOl2NSQA0txutn3NvDgVeCMnpgc78wyvodaH3-TF0YD06rIjdxgUaXJH2T6p9n7puQBMgg8JMN2daICNgCuZux3JBmfAuzMHgVKdYQVo-ErEJNqB6Zi87Y3nl8L1caXJVyl6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم سیریک با شهدای عروسی کوهستک وداع کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/460058" target="_blank">📅 10:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-460057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRIxl4BKuXDqPptmWvb5b8VSEffvvrbgX3qBZGozUYz91rjsjd7NN1Vfyhcqt0e4ZBmSTxN31-aOGBgEQQNmzoMFO19ozRmw0YHp4FW0FJ4Wf_4JgyKwxU13RxnGJqIZ273P8SG2dNfVQ4fCHQH3GOxmX-fpCqQje3QOQEN7xK88j6oNT3iLmoi91QXB-29ObTCufxtXaPPpzoWAT6I4z9szzrDj_KgANuncfri04vbCanuxVzY7rvjV6huJgXoiexy77-2_4vZpJPLFqcEGYgOF0e3cjPdppWdctV1kiXmRYDtNDt8oTIpa9u_DEGQBA4Xp53TvcmM3ZMoGqenfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه شوم بن‌گویر برای آواره‌کردن ۲ میلیون فلسطینی
🔹
ایتامار بن گویر، طرحی را برای آواره‌کردن ۱.۸۶ میلیون فلسطینی از غزه طی هفت سال رونمایی کرده است؛ طرحی که بن‌گویر آن را «مهاجرت داوطلبانه» می‌نامد، اما هدف آن آواره‌ کردن بخش عمده جمعیت فلسطینی نوار غزه است.
🔹
وبگاه «کریدل» (The Cradle)، بر اساس این طرح که «جدایی ۷/۱۰» نام گرفته، قرار است در سال نخست حدود ۲۵۰ هزار فلسطینی غزه را ترک کنند و شمار آوارگان طی سه سال به حدود ۱.۱۱ میلیون نفر و طی هفت سال به ۱.۸۶ میلیون نفر برسد.
🔹
بن‌گویر اعلام کرده است این طرح یکی از مطالبات اصلی حزب «قدرت یهود» در مذاکرات برای پیوستن به دولت آینده رژیم صهیونیستی خواهد بود و این حزب اجرای آن را به‌عنوان یکی از شروط خود برای ورود به ائتلاف حاکم مطرح خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/460057" target="_blank">📅 10:10 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
