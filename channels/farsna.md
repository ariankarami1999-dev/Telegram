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
<img src="https://cdn4.telesco.pe/file/U9KhteymGvyW_nVzDiVPGBUdcfgvWfKs7G2wkOzH7hHgj6RS9Kxlv6RKVQZRv-r9BP41yHHKrHHXzhht2X5m8PTF1peelGTPPJWIlUmHlqbDnRH6-1YAbeAAFJHS99MCjw9lNwhsoPltZ27gcGE1tob63FvixuIolnvIzWVLZ0-fdrS8a2EeIcygC3UezqH7_H9FCOJNQmc-Q4e3M-tuifzhFC-fYcz9qYGjfEd6IktJ3uHWorFNtfGh9lsd51Uw8TByAuHRIBzQH-uVlI0bQXHXRLmzvE1KVSyjmAvf9yx9QpYhFkmZ20Nahxf3J-B1UnnyBP0JrIFjgNUynFoZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 14:32:04</div>
<hr>

<div class="tg-post" id="msg-440198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f07cc3ad1.mp4?token=nzJDQ0v6fPs2OJmTHoiOJd2pOjSMbbp7va_hVv7rj18k2ufZs-jZ2R3jkk9btTBpzIgNYpmhSz1x9hKYhxF9KHtamzlWVoncHt5TusS1XNepbQMUV41f1neucH0ld09Ik_uIbBUC-TTIOTmMhwGaYwcWKFUj4Nxv_71xrWzjV0XhMPYZ2EXpzlVoxKg5cF7SKgpxfRuNkKg1VQYxc1_kvzn1jINhb0EI0Z8aeXxXHWdkwu0C40JjoJua9V8cVG6iceksiQLjBj1UNtvuvh66OasFkXVgq1F6tX0J2fFDnk7-7SKRHMhbwEKAz9rvSlNPEsGB-OAdrtNoZp_OIuueew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f07cc3ad1.mp4?token=nzJDQ0v6fPs2OJmTHoiOJd2pOjSMbbp7va_hVv7rj18k2ufZs-jZ2R3jkk9btTBpzIgNYpmhSz1x9hKYhxF9KHtamzlWVoncHt5TusS1XNepbQMUV41f1neucH0ld09Ik_uIbBUC-TTIOTmMhwGaYwcWKFUj4Nxv_71xrWzjV0XhMPYZ2EXpzlVoxKg5cF7SKgpxfRuNkKg1VQYxc1_kvzn1jINhb0EI0Z8aeXxXHWdkwu0C40JjoJua9V8cVG6iceksiQLjBj1UNtvuvh66OasFkXVgq1F6tX0J2fFDnk7-7SKRHMhbwEKAz9rvSlNPEsGB-OAdrtNoZp_OIuueew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همراه همیشگی رهبر شهید را بشناسیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/farsna/440198" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23456d3ce6.mp4?token=FLwJQzLB7hFXAgbbOaYprr9MO1PWZz4nIROL-JcXYYkm3tWPfxOroMVjlb6drbBE5cvyyBOIRB-N2TIYrvuD6542atjCnLVvo9Hy469XYkpCNCxU3eYDHPyEw_NiXL5JYfMU2qhQD8urnw1o9PRMZxFUK2PF6znGybPMolKtNZSUpSGKAyBKBCV5mts31nD_PSKLdOWmUZgjxnvASTiiJquFMRuXCVDiNymu_vlhqlENQ8RzswnjzZmpCEbys2BjPLv4UQ7XWOh6mHYw2aYeuvV6f_76o6FsBCvinQQOnj23SPx0XSV1W7grhMVdQMBEmGeWjlq7O7nTk3ArelkV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23456d3ce6.mp4?token=FLwJQzLB7hFXAgbbOaYprr9MO1PWZz4nIROL-JcXYYkm3tWPfxOroMVjlb6drbBE5cvyyBOIRB-N2TIYrvuD6542atjCnLVvo9Hy469XYkpCNCxU3eYDHPyEw_NiXL5JYfMU2qhQD8urnw1o9PRMZxFUK2PF6znGybPMolKtNZSUpSGKAyBKBCV5mts31nD_PSKLdOWmUZgjxnvASTiiJquFMRuXCVDiNymu_vlhqlENQ8RzswnjzZmpCEbys2BjPLv4UQ7XWOh6mHYw2aYeuvV6f_76o6FsBCvinQQOnj23SPx0XSV1W7grhMVdQMBEmGeWjlq7O7nTk3ArelkV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا رقم کالابرگ تغییر می‌کند؟  @Farsna</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/farsna/440197" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در بندرعباس به‌مدت ۴ روز
🔹
استانداری هرمزگان: به‌دلیل خنثی‌سازی پرتابه‌های عمل‌نکردهٔ دشمن در حملات آمریکایی‌-صهیونی تا روز چهارشنبه در بندرعباس، احتمال شنیدن صدای انفجار در این ۴ روز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/440196" target="_blank">📅 14:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
شهادت سرتیپ ارتش لبنان در حمله پهپادی اسرائیل
🔹
ارتش لبنان از شهادت یک افسر عالی‌رتبه به‌همراه چند نظامی دیگر در حملهٔ پهپادی ارتش اسرائیل در جادهٔ الخردلی به النبطیه در جنوب لبنان خبر داد.
🔹
منابع لبنانی اعلام کردند که این افسر ارشد، درجهٔ سرتیپی داشته…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/440195" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌ فهرست اعضای تیم ملی ایران که آمریکا تاکنون به آن‌ها ویزا نداده است
🔹
مهدی محمدنبی(مدیر تیم)، هدایت ممبینی(دبیرکل فدراسیون)، مهدی ملک‌آباد و مسعود اردشیر(نمایندگان حراست فدراسیون)، مهرپویا اسدی و سروش سلماسی(آنالیزورهای تیم)، محمود اسلامیان(مشاور رئیس فدراسیون)،…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/440194" target="_blank">📅 13:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abxjk47SKOQFfvZ1q6jr4Tu1JuwvmRlRLxcEF70IRvmocLBVzHfxJOmdGf8URDDByyz1chqZ1CWJZgnoZfbMqksbotGzU4DrzRVb5-ZFbDJI62d2adBCiSMXICP4E42uhCUxKEq8KK3szlcx-KCrMxigN-O2VaMV76aPnbkSn5jqeGvhWxv4WfdNwMCyyEPgq0Cm672gYDL-KBbe4OFPydAnwCvbJPGEHK26BCPvjsypmY3Ez1LYBSAhhmifpzBM-Oiks-MDtf5UAD-Y4PhrpBaA7GsYWBhdZOBOp4p07xykvfha-B5XXeqWwO7fVmpHSo5aI9aA46wcGXJXhuSqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه وقت وسط‌بازی است آقای فردوسی‌پور
🔹
«گزارش این بازی را به همۀ مردمی که مظلومانه از میان ما رفتند و می‌توانستند تماشاگر این بازی باشند تقدیم می‌کنم». این را عادل فردوسی‌پور پس از ۶ ماه سکوت در آغاز گزارش فینال لیگ قهرمانان اروپا در آپارات اسپرت گفت. حرف‌هایی که جمعه با انتشار کلیپی در رسانه‌اش هم منتشر شده.
🔹
در سال‌های اخیر رسانه‌های غربی در مواجهۀ با جنایات اسرائیل از یک تکنیک استفاده می‌کنند. نوشتن اخبار در مبهم‌ترین شکل ممکن. بی‌بی‌سی انگلیسی در تیتر خبری در مورد حملۀ هوایی اسرائیل به لبنان اسمی از عامل نمی‌آورد. در مورد پاسخ موشکی ایران به تجاوز اسرائیل اما تیتر جور دیگری است. «پرتاب بیش از ۱۸۰ موشک بالستیک به اسرائیل توسط ایران».
🔹
سایت شبکۀ چهار انگلیس نیز رویۀ مشابهی دارد. آن‌ها که حمله روسیه به اوکراین را «تهاجم» تیتر می‌کنند. در مورد مشابه تجاوز اسرائیل به لبنان را «عبور نیروهای اسرائیلی از مرز» عنوان می‌کنند.
🔹
این تکنیک مبهم‌گویی حالا به ایران هم رسیده. این‌بار پشت میکروفون یک گزارشگر فوتبال. عادل فردوسی‌پور که بابت ریزش پلاسکو در ۹۰ بیانیۀ سیاسی می‌خواند، در گزارش آخرش چنین رویکردی را اتخاذ کرد.
🔹
صحبت از «کسانی که بین ما نیستند» درحالی‌که مشخص نیست این افراد چرا بین ما نیستند؟ در ۱۸-۱۹ دی شهید شدند؟ در جنگ آمریکا و اسرائیل علیه ایران بمباران شدند؟ در تصادف فوت کردند یا در بلایای طبیعی؟ در بمباران دانشگاه شریف، محلی که او در آن درس‌خوانده و استاد است، زیر آوار ماندند یا در مدرسۀ میناب؟ او که از سانسور گله داشت، حالا سانسورچی شده.
🔹
در سالیان گذشته اصطلاحی در شبکه‌های اجتماعی و میان مردم باب شد. «وسط‌باز». روزگاری شاید می‌شد از آن دفاع کرد اما اکنون پس از دیدن شدیدترین بمباران ایران توسط دو ارتش متجاوز به مدت ۴۰ روز، زدن پل افتتاح نشده در روز سیزده‌بدر، حمله به مدرسۀ ابتدایی و سالن‌های ورزشی دیگر جایی برای «وسط‌بازی» نمانده.
🔹
این دو لب جوی آنقدر از هم فاصله گرفته که کسی نمی‌تواند یک‌پایش را آن طرف بگذارد و یک پایش را این‌طرف. حالا آن جوی، دریای خون شده.
🔹
او یک‌بار خطاب به یحیی گل محمدی که در نیمه‌نهایی جام ملت‌ها با پنالتی چیپ شانس قهرمانی را از ایران گرفت گفت: «این چه وقت چیپ‌زدن بود آقای گل‌محمدی». حالا این چه وقت
وسط‌بازی
است آقای فردوسی‌پور؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/440193" target="_blank">📅 13:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📹
«مدرسه همدلی» روایتی از معلم‌های دلسوزی که نگذاشتند زنجیره آموزش قطع شود
@Farsna</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/440192" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-text">💚
لبخند رضایت شهروندان، بهترین پاداش خدمت است.
💢
همکاران بانک شهر در جشن بزرگ غدیر با عشق و افتخار، در پذیرایی و خدمت‌رسانی به مردم عزیز مشارکت کردند تا سهمی در برگزاری باشکوه این عید فرخنده داشته باشند</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/440191" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/440190" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAyvZHV1XNVba3VnB49UgUtZ4PoArCYu4nA7iSWpGzSA5hF92X1O4eMNRTo5ZYTbBXftxnecDb-9fMsuyj2fnvQVQ3_mSg72OPPG65LAzImXBZrlUQfQsgoSfwLcj99PqorNU9huuMlyyItxffMtWdT8Ncas4iXbmsbzG8y0csVI5FUaJuge5D7ADa9Uoo-OVYEBk1Wwx0Yv5xOGcjKz4xL_En-jHS8cxOpWMUx5cJO66AOmbUpeU7sKchmSzylZkmeDcPfi-nMssxw45NpEHcaNFRszXBgXsvBWE8XmmlU72c-TiRAXVswDPb7hI5FJib0U3vvUncG1rNHb4QQRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصف حقابهٔ ایران از افغانستان نقد شد
🔹
۴۱۷ میلیون متر مکعب آب از افغانستان راهی چاه‌نیمه‌های ایران در شمال سیستان‌وبلوچستان شد؛ این میزان کمتر از نصف حقابهٔ ایران است که در سال‌های نرمال آبی پرداخت می‌شود.
🔸
طبق معاهدهٔ ایران و افغانستان موسوم به هیرمند که سال ۱۳۵۳ نوشته شده، در سال نرمال آبی باید ۸۵۰ میلیون متر مکعب آب به ایران داده شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/440189" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705961b41b.mp4?token=u5QK-B38EUvHo-_HuYxR83wVlWJoQ84C-vVksySPd1YvmKk5_WNorq_I9mlc6RPtjs50Fdv79v4kn0Ti6rAErul8Dkvhallanad3-QvyfYiOzKEiDx_qKP0uAQ2EYL402kDe37WU2N4ERnnIGEe3AoJUmneJJr9W18Ui128j860vXg7fGDeeaM0GY6E5EZqqDfOu5e345sShHtb3o7pa3rnapLZg7NiQnp2IWIS9xC1b90TBdr6FWh8RhNbosvWeYMtaph47NrAYO_dx2FUXj1P5VGDuVAhQ9eY1vWAGGmoigbz7MNoTu4cFgEiDfhQgqq4toksfLvO0TzTdJVJahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705961b41b.mp4?token=u5QK-B38EUvHo-_HuYxR83wVlWJoQ84C-vVksySPd1YvmKk5_WNorq_I9mlc6RPtjs50Fdv79v4kn0Ti6rAErul8Dkvhallanad3-QvyfYiOzKEiDx_qKP0uAQ2EYL402kDe37WU2N4ERnnIGEe3AoJUmneJJr9W18Ui128j860vXg7fGDeeaM0GY6E5EZqqDfOu5e345sShHtb3o7pa3rnapLZg7NiQnp2IWIS9xC1b90TBdr6FWh8RhNbosvWeYMtaph47NrAYO_dx2FUXj1P5VGDuVAhQ9eY1vWAGGmoigbz7MNoTu4cFgEiDfhQgqq4toksfLvO0TzTdJVJahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس اراذل زمین‌خوار را در اقدسیه زمین‌گیر کرد
🔹
۸ نفر از اوباش زمین‌خوار که با شگردهای ارعاب با فراری‌دادن مالک یا ساکنان قانونی، یک ساختمان چندطبقه در اقدسیه را به پایگاه غیرقانونی خود تبدیل کرده بودند توسط پلیس اطلاعات تهران دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/440188" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5R7rtausbRMGR9Gis3rZr5vL9IwwVtrkMOjuB41CqiJInQ6iAJt8p2KGdW4DLPw1s2sItyj7KchpeF0imBqYsaF8_3ImGoTmeMKYyQ_fP4v8FdrF0zif0VVLdyNG3o29ezdbZBW5NHaTorfMvvd81vMiQlyLScUBbdIYUJFT3sBw8GPYRNISHH1FHdRQrrv_rce7pIAxt3Ca_1UUZ4zG8LL5Uk--OKPyuA215-YO3xXnTXSlCXX1ojp6eREPH8P-jwjSHvP-dZXF4GUGIZ5UF8JuF-nIaSsJshBvlP7AUTJsHtFDcStvvnUI41S79a4OAFXMe6Npt88SKsT8YHKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفتهٔ جدید بورس هم سبز آغاز شد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۳ هزار واحدی به ۴ میلیون و ۳۹۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/440187" target="_blank">📅 12:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802472a828.mp4?token=r3nLSrCFhrdg7tKg44fECf5H6gvn-ShGjtGy-gTA8UUN4upo3JVylxi2Y9ehbqUI7eY5jYrNRJzMVlSAZ-iSemmDyGIKDjJ5Kp5fklr_4LvCUggCwOEsrSwwyXtKVva1sUWaYGMVXIMiuNy_a-bBLOR8bF5QbF9ZZw5J8W9VHhqK1K6-b3Q6nTDUsaR_YGXkJx4hzgnkorpeD-lG5t5mKmz7m9r08OxEYzboq4u_16p87nlJMrWzflOgC_iLaFo3nQeZDfumAKm5d-dq-2B1brHN5AO7y2vpVOkA1X7alHFjegMohkmPr_1iy2GU75EM2dkdOMu4x17ESkEvn2wQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802472a828.mp4?token=r3nLSrCFhrdg7tKg44fECf5H6gvn-ShGjtGy-gTA8UUN4upo3JVylxi2Y9ehbqUI7eY5jYrNRJzMVlSAZ-iSemmDyGIKDjJ5Kp5fklr_4LvCUggCwOEsrSwwyXtKVva1sUWaYGMVXIMiuNy_a-bBLOR8bF5QbF9ZZw5J8W9VHhqK1K6-b3Q6nTDUsaR_YGXkJx4hzgnkorpeD-lG5t5mKmz7m9r08OxEYzboq4u_16p87nlJMrWzflOgC_iLaFo3nQeZDfumAKm5d-dq-2B1brHN5AO7y2vpVOkA1X7alHFjegMohkmPr_1iy2GU75EM2dkdOMu4x17ESkEvn2wQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهادت سرتیپ ارتش لبنان در حمله پهپادی اسرائیل
🔹
ارتش لبنان از شهادت یک افسر عالی‌رتبه به‌همراه چند نظامی دیگر در حملهٔ پهپادی ارتش اسرائیل در جادهٔ الخردلی به النبطیه در جنوب لبنان خبر داد.
🔹
منابع لبنانی اعلام کردند که این افسر ارشد، درجهٔ سرتیپی داشته و به‌جز او ۲ نظامی دیگر به شهادت رسیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/440186" target="_blank">📅 12:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59639d9290.mp4?token=SafRMd0uHl4OCslvpb0072WspwyZZGagYPfXYj4Dff_2gyGiWIWVPHcc7B_vYI9LaFjBxb4hx0asGRDY3StjWBwy48zv6Av5wVk9eG76McYRVPQ_H0vH1XeSVhIMJXZkTrrxIrKJ2C9iOLY90NbtdlpnWoBpIm9Z_er4faMJihrw9Pk1ObjUKZu1zDE8K6iSOmU-mx8EWJtLijk7mT2hAZAC7HBqjya7o5rWgaxGdckkDxDAB4e9UsLZgcrypf76FY926Wl7vABC6e1UVEP3hajCdywYu0zISwlbvPvgbTvNmlRi3qeGS_3dwu3G_31Mp0YAtRpRvVaU4-CuW0ZHSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59639d9290.mp4?token=SafRMd0uHl4OCslvpb0072WspwyZZGagYPfXYj4Dff_2gyGiWIWVPHcc7B_vYI9LaFjBxb4hx0asGRDY3StjWBwy48zv6Av5wVk9eG76McYRVPQ_H0vH1XeSVhIMJXZkTrrxIrKJ2C9iOLY90NbtdlpnWoBpIm9Z_er4faMJihrw9Pk1ObjUKZu1zDE8K6iSOmU-mx8EWJtLijk7mT2hAZAC7HBqjya7o5rWgaxGdckkDxDAB4e9UsLZgcrypf76FY926Wl7vABC6e1UVEP3hajCdywYu0zISwlbvPvgbTvNmlRi3qeGS_3dwu3G_31Mp0YAtRpRvVaU4-CuW0ZHSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مصباح: ذکری از این بهتر پیدا نمی‌کنید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/440185" target="_blank">📅 12:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ابلاغ وام مسکن ۱۴۰۵ برای خانوارهای فاقد مسکن
🔹
براساس دستورالعمل بانک‌مرکزی، تسهيلات قرض‌الحسنۀ وديعه يا خريد يا ساخت مسکن با بازپرداخت حداکثر ۱۰ ساله برای خانواده‌های فاقد مسکن، خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب ۲ فرزند يا يک فرزند می‌باشند و خانواده‌های ۲ نفر (زوج و زوجه) که تاريخ عقدشان از سال ۱۳۹۹ به بعد می‌باشد، پرداخت می‌شود.
🔹
دستورالعمل اجرایی تسهیلات به ۴ بانک عامل صادرات، تجارت، ملت و پست بانك ابلاغ شد. بانک‌ها باید فهرست شعب را در تارنمای خود برای اطلاع متقاضیان منتشر کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/440184" target="_blank">📅 11:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
آغاز بازسازی پل B1 کرج
🔹
مدیرعامل شرکت ساخت و توسعه حمل‌ونقل: در مرحلۀ اول بازسازی پلB1 کرج که در حملۀ دشمن آمریکایی‌صهیونی تخریب شده بود، عملیات آواربردای شروع شده و پیش‌بینی می‌شود یک هفته زمان ببرد.
🔹
بازسازی پل B1 کمتر از یک سال زمان خواهد برد و تلاش…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/440183" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
🔹
سپاه اصفهان: به‌دلیل امحای مهمات عمل‌نکرده در جنوب اصفهان و بهارستان تا ساعت ۱۳ امروز، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/440182" target="_blank">📅 10:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e708d74fa6.mp4?token=fZ9df_yoNM25FNnJ9GcP4Q5TcE6u78eUzHl05ZVXiujXwyTsDvsxnXjPCapIGT_iWcqTw7nb-uvRpiE4qPMml4Yqw5YqI6iwjNsjTDolQ3e6zru7FtpVLu0cog7cLN1v1zCrRnfEV6Hf8k_0f0_4rZIy8DDmzQuqhg0MODmz-5UgAs4DTXYmJvJRY8Kb-hTs1Z7J0GTL6D7PkTuzl5Z-3my-TPNoam8vmjBX6A1ne1omacJUg4reu0YB-RMNLtJYTmk-jPk03Sgw5vXr1X-ptEFnk6Oy3UZTnnAPjCclMtJuKLzsDrbulfjWyT2lpxoTdkixhtTWzDO7sTbnGQuWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e708d74fa6.mp4?token=fZ9df_yoNM25FNnJ9GcP4Q5TcE6u78eUzHl05ZVXiujXwyTsDvsxnXjPCapIGT_iWcqTw7nb-uvRpiE4qPMml4Yqw5YqI6iwjNsjTDolQ3e6zru7FtpVLu0cog7cLN1v1zCrRnfEV6Hf8k_0f0_4rZIy8DDmzQuqhg0MODmz-5UgAs4DTXYmJvJRY8Kb-hTs1Z7J0GTL6D7PkTuzl5Z-3my-TPNoam8vmjBX6A1ne1omacJUg4reu0YB-RMNLtJYTmk-jPk03Sgw5vXr1X-ptEFnk6Oy3UZTnnAPjCclMtJuKLzsDrbulfjWyT2lpxoTdkixhtTWzDO7sTbnGQuWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
ساعت ۱:۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون‌توجه به اخطارهای مکرر نیروی دریایی سپاه، قصد…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440181" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440180">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هلاکت ۶ تروریست در درگيری مسلحانه در هنگ مرزی
🔹
فرمانده مرزبانی: تیمی از گروهک تروریستی که قصد ورود به خاک ایران و حمله به مقرهای مرزبانی را داشت، با مرزبانان درگیر و پس از تبادل آتش سنگین و درگيری شديد با برتری قاطع آتش رزمندگان مرزبانی، مرزبانان موفق شدند خسارات سنگینی به گروهک تروریستی وارد کنند‌.
🔹
۶ نفر از اعضای مسلح گروهک تروریستی در این درگیری به هلاکت رسیدند و  مرزبانان در پاکسازی محل درگيری، ۲ قبضه کلت کمری و مقادیر زیادی مهمات مربوطه را کشف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/440180" target="_blank">📅 10:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440179">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPbJS176YGsvpK6NrRJfxhcemqO_b82-VOoJKfKSunfXcl3u0Tz-cHZOnQHBdOzE64WgtbJTNsKjVKhI54kbE7pLaaMnW_e43tN6dEy_5i5z3cfiqZL1QcSlgRcfU-D5eVr3etTVE2WLY9y8syNQtJar6tTHUAtPlXQOrjWwNeUMiYUB2AxQmLcU1x0JZa4g0zAXR3LE1htS8fFc9aM6djezlk6pqxRFawAgx7vz_fl38miTyV8ZprI07KR_75R2kht4KSR6IBqQQO4cBJIGhQ-HTNQ9NxlyGVr1kkr0AnH6bryD7wRXUq0zJWftc4K3tudbStwn6Xw1uW-YFU4yfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: صلح پایدار از درون موازنه قدرت می‌روید نه از دل سراب تعهدات بی‌پشتوانه
🔹
مشاور رهبر انقلاب در امور بین‌الملل: کابوس دیرینه و ترس تاریخی نظریه‌پردازان غربی از قدرت گرفتن ایران به واقعیت مبدل شد و هندسۀ جدید شکل گرفت.
🔹
اعتراف رسانه‌های غربی به نیاز ترامپ به توافق موقت برای بازگشایی تنگه هرمز، گویای شکست دکترین تهدید ایران و پیروزی اقتدار مقاومت است.
🔹
اما خطای استراتژیک بزرگ‌تر را آن‌هایی مرتکب می‌شوند که در منطقه، به سراب سازش دل‌خوش کرده‌اند.
🔹
معماری جدید هندسۀ قدرت برپایه تضعیف مقاومت قهرمان شکل نخواهد گرفت.
🔹
خوش‌خیالی دیپلماتیک، هزینۀ سنگینی دارد و صلح پایدار از درون موازنه قدرت می‌روید نه از دل سراب تعهدات بی‌پشتوانه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440179" target="_blank">📅 10:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440178">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌
🔴
آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده است
🔹
ویزای برخی اعضای کادر فنی و اجرایی تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن خودداری کرده است. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440178" target="_blank">📅 09:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440177">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ0_PFCDbTPfYUN3f4PgxW85PcBtwu9sWiPFBWjblNArRqdBUxZIVzgiP9QhL1f6a5g1ln77oRtbUBhRF8CAmZpHWDABcagC1xdMCt7Rjv5wIx-lBm1PPJ3ZvuO3nnGLkcG5S29yVD7d0UZJFUqvz7t09t66EQbSR8N25LzRqJeeqjPks5n7KYFgepOdLf7nRVkUdhgr1UoPBC1xC3VrvPD94qlXgLHVWR-Fn4WFbu6kmBsVmmdUVewkeRe8Rz8UVyuGwFhlb9rK0mY-WvNL-obwbDd7GOswNOeRdYs28V0RB_8wxfNt_RJ2mD4b82TqL328km6hLPnHWqZeB7mXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبح تعطیل ساکنان شمال فلسطین اشغالی با هشدار حملهٔ حزب‌الله آغاز شد
🔹
هشدارهای حملهٔ پهپادی در زرعیت واقع در شمال سرزمین‌های اشغالی فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440177" target="_blank">📅 09:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440176">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z985qARFWFofVabClvJVqTnGMoYKOLQpglejR_Y4wz0C5bgbhHg03I5zqV9LMgEWN0qSEz4sW_1bYCn4rv20aS7RzEAoSMWGFgf-UULrIxMu-ykoyTr9Ky_OmjOKsF9q849EVrikAJNcekuPLzDfz2AWh8YxktS2ooYnoXRrsEUx0iAq9-U0eIUJwXXdYtcEVhsuPlEH3snVJylXYewknB5V0LldxevaSjQ2OjPuUw5THpboZ8CvK0AyRO6gAV8aNC9uO2e4Kt5DaUX3xqr75ebPnabeUzCX4xxC1gavGb7huJ-IX6nqMjXS5zX4rd15oiHDZjpiWtaTrtoS6GgNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به رئیس‌جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید
🔹
براساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی‌ها را آواره کرده و کشور او را روزانه بمباران می‌کند.
🔹
اگر لبنان برای ایران ابزار چانه‌زنی بود، ما مدت‌ها پیش به توافق رسیده بودیم.
🔹
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس‌جمهور!
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440176" target="_blank">📅 07:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440166">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWhaF_DkMnH_Dz7m7tTNTxrnQbNqufSQrveFWrW8U_a5wHO4X8_VlgGCVktd0xAHD7SUnhBFJnlblRP2EyGrNjBaYznodPY05WsFnS810-Ywr7tyIaqmNm_WyplXsnQ8WpcSGlsZuTj2jK52pzKiSfYUkk_Gdd3X3GvdZb7S18G_j57rkIq7Pzfem4-oEeOMTjQ4VzzmFzJrM5hAyeVCPsyRL2WD3f86JWKG2kaUFRlszwR-nPRdwoYvCDuvTLcFFlaA69X3z30Xr8tYp029FIkGgAP_R1fxOURQfFt60M9-XhfLdwovx1_7cWw9ifOIMn2hi0UbXABjhiNkTFekYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bq_w0UHfGrk5RxUe0i-nFSvPrgpShcLO5vUomYEWt527cdfNftG71VwLTMrNaUpGUDQuCyKtDaJDrAfFGwCkkwL1Gpm4T0e8ib084OdVyKuwwuFJchWO5xaXbzvModzt1wz58hDspMToK3iY-CJvVqNb0KV0FJHX-GAOkHD4sC1eNmUQ2_uIW1SfDAQVOGXabDUI6DezyyJ2r4KJo8A4bl8pM1hxtLQe50uZ1lKHPhBcOeWbOc9qlbftAGssP5BVkCg11tdrvJQ-yW1QOQG68X5OK-phA4C3eayHpPwtxuLpyi7JfzymBMyFzoEuNDWHk4OGl2kr0l8cnqv7pNM-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXfnMGaDuIqN8pqZoUjTmdZ_hh4IxUHtuIC99v0niMV4q7B5wSL9vMnCsKFNeyczwAY9k4RuuNMHrplR9pRauTeZvHEmUXaAqF8UcS_dBbcNbkvTucYdMV_vwUhyiMHKyNRnVfq_ExOMuzEwlFQ_LaROyNms84GRIju4V5Ae_a4RyNGBJWHIq6Nkp8_CXnjRW1-PX-_2eXIi65l6ZtJsIJJy3Grw-Gw5F3VmFQpv82q7zxfXvi7yyKjJgc_4UasPY9O7kCkUFBg_5OqNwnhit_DWdKE9mxQT3cFplj_ar8bBfqhVhVPK2YVQwcOcsFbU9PnJruxXrfjyvO6Bg99fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvRgtC1WRGzlVEufw79mAlQFw-kHuxzKDUVS6Zg0wmIk2JKMZHQ4F3jSHzNYBa1szN5_jUWzRGTZTAGeL4KIqdxLV4OVtuAF9MDS18s8oyYrbpnST9l0jV3tefEWerKHa1-5yP__nbaPnstsEWYKYyYEw1e6GVGW57rklVYyK1waQX9GqqkBwAxCzQqy92qRcinrnso7HAn7brvY7iJPsH49YGOiNGm--iC_DA2fK7BnWxFn2cFk92pcOAkAup9dAWcIf2rK4t7CulzC3ZlKYF87U0jq4FgRPK9qRW3EzxSKTR8mZ5hwrLmTupnn7hwSvissrxWnQBmeeYFllrfrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDtjt3beIV18m4NqBknKOmYJynFscucLb9ybtzOpdLWphtut2Tcrenci9uflNwnxlvgb3V7GCJlJqBKdXAmtS8l9rh6RFbwjx1wV5urwn7eTith3q1kNTvX0pQK0CQ-GnJ8L2B4KTp5FeeUWLpe6H1pVlY2lv2TmeTdXpEcEJ-RXb20b5S3cztkuHp3lA7zvrbE4yAP--eJqJz_wJLpq7XCTIF6z1MSyjXkVipa24CNcF35jje1GrAOqmtn2DeYz94w7Qb3bMnAceRbNnP6F04I8IETUZczXI9lrq-a04NvzM3HdqKCdfLvxXkgnwxm7Ryeqb09on1SItzp0iIgyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiB9IQKCLvHlNs5yD8MDCRUSIb61rgtpuNfDRWMxPOfAKAJ8MnW-JPOrORN_F4Z_F1j43-9c8ifngwkDEel0IsBEBdL5Tn_xiQFUetRGcrmm8RovA5q1Iu_PjloBeocc00KdBAGWfu65tiA2Mtqh42bX5pnpNImRdUBIJcc-XtWsEbCaSO-8MqNVBaqObH-Z3XNlz93ZBjXqdeUZzGol7GL7lUgz49M9HJLkLJ7UGr_2kUDkHwOEsS5pqWMljERF3gRTd2TLkzjkL5-6qoCi6kkkM93ZHF2r57x2MbyQfEghm6a3ZPgL9k5-ukEalTrguuJ5gD8OJc8QIYGg66dXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZM0eIhDtelpizDQhhLBKcx21Zt9P26wPc4YaU402G8k0Xx4_jiXYBxEjPDqkOM7mOIjvAhLnLXrlj0b63cfye4nCniBmb4QzgXFDq3ZQSdiFsb6_xJef5tgUrquhbrsmvcTVA8ddr_lI-9a_8lxSTbh6QiJ-z4ApzodnEJ_xhuhA-OO7_Kt4dJ0W49nyHJ7yFgoapXUQlEtjLIUSgCJB4APJxl_lHAy43YILXWew_I2YlRFZzoxQmPBiRQ_wLtKTy2P8QsMblbf9wc43WZ5cUM7owje99GZSNyfnXNQv1xI8i16X8LW91uJEWB9iTQOw3ODkfjk2XwbgZ8rU4DP7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7-dxNN488kJCtVvGmTGcbAFG8m1cyxoOxAsFiH9uBKxqgR_qX7tPl5XPlTLONfeDz1ggRewf-LY77JPvQ83wWecIEHehOydTK3VnkSVfV4Ns2KzSaB6s7Faot1FuSrsUE7OXynMmEVI8FLc1nPsiMfrStOWMTQIs4QQjF7TajivmXZ7AtAVx0JHePJIVSRdldKQepLlY8g7uXkMdjld9cC6wKcRicQFzKfXWKiHcI29juEsQTyXMM5H8YlHSaZ_sHy94dqKBeSESu52Wfeas0-EpeTfCcj-NeaCmz5wL0g83zMgKwyNYaBsINGapAhsiuKq7WtfLms7XlvWDdxk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-xziwBjcMoWKKVDZzqyNtje1YVrSmeegg4TVd-jmOpzieIDf9-ZIVj4egcIjhJcuCNUBTDE9t7DN84BJfBfB44vMThbJhcsSTxDPw2O9f_n3I9b0AtLeu8z1Cc3YPjeEgbzwkbFOAHZdFSzL0MrgqOrb9Mn57J8FnVt4Kl7Dgl1i5Yoj_GQUe03DSkdZgd6AwWZb7Ibn0ok4orH1Bgm9LXPCHWWb-gt7gIbPWTJRslB1d_xri4lXLPFzUDeQ_T762_a8t-1NRJREnDwF7SbQFVW23r9B3r8pXack55pm9MtTFgUHFRhDgTZ_AaQJ6yavgsvGoXIfruiCGfvkNRjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSQpwoFRjTFmeuopyQmzQ4dFksQBa1hOrbb6uB_Rwl-h9WXJ-NYcNKTwJ6WkC9CO3eXlxkvmepJMk74CvZsQEp-uSZbhVayrQdDOhP6gmo2PEPFPq-jFy1pnZRADFza2B61975Tpv3Bxsv1PCsKwrBIkoVt-j1TDRcVqmzJjS9iCcTiC-LEBvG1v0HfhR_RlBswZpzaLqHdA6tSgBJNQetkjG56-eqGMXjIGs_uuy06QHNhMBGGpNQK1vIePK32377iiAdg5z8GKrM78R8VeigMRevejTLDHvuWcB9MvwXDHWiZSBaMZixj9_PyjtSEkesk-GaArBS9GP_aPtSDF9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارۀ «آدم برفی»، در آخرین برف‌های بهاری توچال برگزار شد.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440166" target="_blank">📅 07:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJPruParF8xU6pFN2XuiNQqKh-0fpPj8rHzE_4OdCz0u-UY_sGlwSY3F5qXHrfhduPseimZlVo4vtVDC6XDyPu8asi5mokJZmm5k3ZuT-4zpCLtlnjDE3JhKpYBz6dMUHL8QEfvMyuO2R-sU8ndbRn9yFyC8x0gaQZltRxHaSV5NTzJoCdd0gfiyK7-XiHB1R5jfP-2v6l9JQvlMfkMIRc-RlAT0qJTIjWB18osBHINaX3y4nONCNeu1WWenJVOpHwt5K1yAzH7eBe0CQJHzHEgDdggMFIziure_XpxgzLSKS9wyI-XRFJF0bXg7M94qNjqkUoVgdFuftTIJsq_Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGtBxBWkw8tVGD4AYX9BS21bYRuOyDgFRsXZ1fRVcePjE9jWJZVuYe7TmjwLczdZGnHdyGU65C-oMDnIKa5hj7NNlxyTpoHMFWIwmTy6ertKoxurUkoTCMEt7zK3G48qXYu-16hH19ZAk1t-CPI7CGtCabkAUN3mDUX5gwyOT7DgdbKkHuy-83X0S7SqAYZeV01_yUwlIGC9k0diMsYPKL5IuMUifBnnQFuWtzNES1O_TS7z0ticayqQThkaDyZY0ydh6gVwzr11w_pYaeqvyPAGfoJ-KfZeXPS7kPbpnCE0WXJAwTgmjCPfbWVLrD07c1U1LSJ2vYM_bw_jWtPAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbMkSXw2PrLoFbnRMF3N3lqhf_HpDL5Mhb6T7eVKQB02D7rZhGk4UAbBA_apFPE7L3Qx5cbCBQLsqLH6SE6_fgCkVopciZ5TDukq834B4xWtSD21zkglUh5i4kGuIkytVHXdNNk__Sw0t_3R9BUN1KQ0iqqSbUAmIcLJX-fyxajFr8RE02Rld_WyeEhXfECKiELcEW-rC0-8rVE4nGrNFNo2sh7oyNKJB8NqCe1pjZgkhvBDq6zBRKF7icI6OjkSddynDPl1xEv15l3bEIloJ9FdRz8f3EDDcjUfeTOW2oWVkU6XALLOmtIVmTNDjB-SaXfyhTHvjtp7w7zFi6yLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7eUEnU6j0M3NR_b4duulM65b79mTMipamslJuWd3tuVAq8GyWAbG0R20Fid80ntvVHQpzFfx7MK3pSnDIuXbYiOG0jbMzxmqHOssOfjcsPVS_HiUEMCzlWk4CE8xsI5t6_HjAcpU6C5NPMn3KzdvAOMCCOa4LXcWwu33okrnr0SiNhlWZi_TslD7HZELXcNbtm0NUX5LCebQefgBzHOMG7I2XDqpkxkw9sqdDUWo4wj_LubwhVCFh1-dw4d02s0EfcwjdjEKEqYe_lH40YaslFR4qAX4cYVKPGc3IPByJXnTn80kDNToVPHfy5ns3Axj7r_XI1-mqsOS1HLsDxA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bB9wSzPqbcOJbTpqveZauGEp9HSVYDypuTsQgw0zI76pEoqcHooxQTANCWlwcqFTp-T3Xb99cPJK6JFTzdjnn0I8iMuzYg4DLdQZFAW0qXrMA2eca4MVENIayI5PyFLLmy4bRhF_l553PQ3W0zR_On93R6_UP17wlqdJniK5P35ld8Jo4HtvpYOqavnlE2HSQfaJUbFQ66CfFPDEx16HukaegTCUPWW6yoCEkI4SE3iwGUAB8a_4EfRmqVf7VydOwKTJlLphbfzOxObtAdwkTAmixdebsjfUjO4KMETahqfJMcvpyD-ZygRTIKdmtVwLD6ESDu2KNkvyN1NU3rt4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVd-vasemJvFoUwKjCh8P9alHkarQA7kuo6VfAlVuMI8P3nYkCFV0cFrZEOdesrT4n6FLCREDj8juJ7JR9Wy-uUMZJ4Y6Y3bVLImv3tOjRpKDNe8knsiUyd_9GDMuHLwu_Gprj5DIJ6nf6RVOP0yJjlby727d40y4LKZNwhdLttiVzKMad0oFe_QJisBAwZGU_Xs-fUbXfFhU3DInmIv5y7UrGeIZBgj4eKfkb1dNJRy6n1Qn7iqmWYX-Pa3eOYSO5ne9f3cYFA4A_L9TkmkddB6v9xgTVgJ5FYRAEXAZ_U8-0TKK96O6U49XoA86k3sX61PcSCoDzyVouLepVGLIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام موسی‌بن‌جعفر(ع) در حرم رضوی  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440159" target="_blank">📅 06:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سپاه پاسداران: به دنبال تجاوز ارتش کودک‌کش و تروریستی آمریکا به سیریک و جزیرۀ قشم پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440158" target="_blank">📅 05:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه پاسداران: به دنبال تجاوز ارتش کودک‌کش و تروریستی آمریکا به سیریک و جزیرۀ قشم پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440157" target="_blank">📅 05:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=bqrfgQn7CFg1hJemrAd_XcnU7LAS6fCod1iJ4q5kXH7NtAgxyQoRgDRfwhUe77cgWHJUaEY0ygJw1Z3xxf8oxCz_wPWfUPyfh883uL4u5Sx9PSVFzmCl3czOlQO0gBAOm7AY3ctk-D5gg0Dx8V44B4-WN5ood4XB1Scu41zHjdzapD7RZqopoCID0HGRxv0IG9BZtC25QU3r0VBRJEgzmg5sPlpQMTmxRJV2YYF6nkr_SHMBL9CTKtlnITg9v1GqGPOBhdlrFwH_6tS6dYP2UiY7Sv2H4mKUGm26NBNdbmUwQNBxeGE2q_FGz_wZMwhH29BipbUJCMh5RROhYIlk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=bqrfgQn7CFg1hJemrAd_XcnU7LAS6fCod1iJ4q5kXH7NtAgxyQoRgDRfwhUe77cgWHJUaEY0ygJw1Z3xxf8oxCz_wPWfUPyfh883uL4u5Sx9PSVFzmCl3czOlQO0gBAOm7AY3ctk-D5gg0Dx8V44B4-WN5ood4XB1Scu41zHjdzapD7RZqopoCID0HGRxv0IG9BZtC25QU3r0VBRJEgzmg5sPlpQMTmxRJV2YYF6nkr_SHMBL9CTKtlnITg9v1GqGPOBhdlrFwH_6tS6dYP2UiY7Sv2H4mKUGm26NBNdbmUwQNBxeGE2q_FGz_wZMwhH29BipbUJCMh5RROhYIlk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوهای منتشر شده از فعالیت سامانه‌های دفاع هوایی بحرین و کویت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440155" target="_blank">📅 05:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
آژیر خطر در کویت به‌صدا درآمد
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار ‌و پدافند کویت برای مقابله با حملات موشکی و پهپادی خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440154" target="_blank">📅 04:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
آژیر خطر در کویت به‌صدا درآمد
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار ‌و پدافند کویت برای مقابله با حملات موشکی و پهپادی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440153" target="_blank">📅 04:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsxRhPVDYcGLtVu9tB0re1w9szcG033fustVrh96qghIZO01LnnYAgyNvzm6wlu-unbhv_RDtfA0K_tqkvlfRUnipQbsZ3KOJeqfCiak0RL2cx09S4CVT7xiIEQ1zpFFCUGESPi5Rc2HOsU7tblh5l7hilTH6QNAzjlparSnB7qEX6Zj-qoP0b375GYiGcEawL_ILHrF8eL48aDYPBJ8IYa0vcs0JucjIG-JVu8ZHs0mN9TSMYA3NXei_IjximVLo3B_ooQ28bJ6Y-ufaOO4mSIEacTOIHsK5ILNbh3VJrCCSDOAkR1NHpw7eyF8Kd-nGVIHkHl5byINFGYXz9srDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپادهای حزب‌الله بلای‌جان نظامیان صهیونیست شد
🔹
رسانه‌های صهیونیستی اذعان کردند ۶۸ درصد از نظامیان اسرائیل که در جنوب لبنان به هلاکت رسیده‌اند، ناشی از حملات پهپادی حزب‌الله بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/440152" target="_blank">📅 04:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e51a15280.mp4?token=HGCKBGGwTBYS4wGOFg_nJN3hrzB9Rs5gwMpKLHLOEjgwlX_FjQBi3F49-l5_FqKRSmEWbWSrTWVgYmDoe22FDm7AMMgUvNEvXrYDl6s66Alfq3VWbs9RmLrRYi_d5Y1MxRzilAqQ6MIU0kkjxfVDnhF_z9HjroLE8734FBflhdW8goO6HiRL5uE86b2LPAXDQTjHi72_VPC46AhxuStxh6AXrM1VXEhI-S0RSh1T45szQLn2kuLX24hRurO_VFSPaJEmBCMf4IpaSn1fy6fQLk3fXWPgKSneuTMUL74P2C_zX0U5dc7PerAhUz_nvqpdfa-S_iJfY10Yl3CKmdy22b6dsGKygmwHPn-KDPN-GZtPVtd9M4Cq36St8SO_bhWtZ7tlTl9y4DF_QnwRbz2PxE0gWKzQojJUJeCX1hLTt3nwFuucfR_2iKExJr5XyBUOEcuSSDME-kb2E9nMHRNsfXqdzXSKNHwjA-_VMqT2cDcWltwLy2Et9tOzWe9ZO57jvUl4oMLeMTA486uJYtsF-C9wcbkPw9bRXZMP3FqWr6JLiZYOwoIHIG_D6NQ0mdjexjihzSHtT9MX5x8fKPyZUqSZ84MNahCaLEYBtylHLNJeDCEqfz_3S2pA2H1qWaVXow_VlfhHlneFAKbDoFS_9fpdkMnqurKl13DTo9GBIwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e51a15280.mp4?token=HGCKBGGwTBYS4wGOFg_nJN3hrzB9Rs5gwMpKLHLOEjgwlX_FjQBi3F49-l5_FqKRSmEWbWSrTWVgYmDoe22FDm7AMMgUvNEvXrYDl6s66Alfq3VWbs9RmLrRYi_d5Y1MxRzilAqQ6MIU0kkjxfVDnhF_z9HjroLE8734FBflhdW8goO6HiRL5uE86b2LPAXDQTjHi72_VPC46AhxuStxh6AXrM1VXEhI-S0RSh1T45szQLn2kuLX24hRurO_VFSPaJEmBCMf4IpaSn1fy6fQLk3fXWPgKSneuTMUL74P2C_zX0U5dc7PerAhUz_nvqpdfa-S_iJfY10Yl3CKmdy22b6dsGKygmwHPn-KDPN-GZtPVtd9M4Cq36St8SO_bhWtZ7tlTl9y4DF_QnwRbz2PxE0gWKzQojJUJeCX1hLTt3nwFuucfR_2iKExJr5XyBUOEcuSSDME-kb2E9nMHRNsfXqdzXSKNHwjA-_VMqT2cDcWltwLy2Et9tOzWe9ZO57jvUl4oMLeMTA486uJYtsF-C9wcbkPw9bRXZMP3FqWr6JLiZYOwoIHIG_D6NQ0mdjexjihzSHtT9MX5x8fKPyZUqSZ84MNahCaLEYBtylHLNJeDCEqfz_3S2pA2H1qWaVXow_VlfhHlneFAKbDoFS_9fpdkMnqurKl13DTo9GBIwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچکس غیر خدا زور ندارد؛ خیالت راحت
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440151" target="_blank">📅 03:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq090s26rF2hh4JgLivr055TqIDxVKbCe2nTieDzL-on-Mofu7LSWrK9lyfLyoWXb-VIWG0X8zrECuM7n_Sk3Id1zJLTxITj8z63SDj-iL-IOlb4tIq1T_zvner4J6r8lwexjYkFb8Z2OneTTvzf5kFE_qKixAvHGmoB65i2mE6Yberz8IAH-4cQ9NZ9dfthp4yPEcmvw5KWdevk15sn2UOqVwTXQzverTNeZdTCyGmX4sJ-GGRC79LqjJO2aSGtPGSbA5ZMUEDMUT00vdQV3URj8gsyLBaHxudPb98JNx-8X4FbrKmLIC_R2RpMTiR9L3lVPdwGUgw3xGapw0oQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژگی‌‌های محبوب اینستاگرام رسماً پولی شد
🔹
شرکت متا به‌طور رسمی اشتراک پولی «اینستاگرام پلاس» را در سطح جهانی عرضه کرده است. یکی از مهم‌ترین قابلیت‌های این اشتراک، ویژگی «استوری اسپات‌لایت» است که پروفایل کاربر را در استوری‌ها برای دوستانش در اولویت نمایش قرار می‌دهد.
🔹
قابلیت «استوری اکستند» نیز مدت نمایش استوری‌ها را از ۲۴ ساعت به ۴۸ ساعت افزایش می‌دهد. کاربران اشتراکی همچنین می‌توانند چند فهرست مخاطب مختلف ایجاد کنند و برای هر استوری مشخص کنند کدام گروه آن را مشاهده کند.
🔹
کاربران می‌توانند پیش از انتشار، استوری خود را پیش‌نمایش کنند، آمار دفعات بازدید مجدد استوری‌ها را ببینند و حتی در میان افرادی که استوری را مشاهده کرده‌اند جست‌وجو کنند. همچنین اگر کاربری نخواهد یک پست در فید اصلی نمایش داده شود، می‌تواند آن را فقط در پروفایل یا بخش هایلایت‌ها منتشر کند. در بخش شخصی‌سازی نیز امکانات تازه‌ای اضافه شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/440150" target="_blank">📅 02:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادعای سنتکام: اهدافی را در جزایر گروگ و قشم بمباران کردیم
🔹
ارتش آمریکا ادعا کرد: لحظاتی پیش، چهار پهپاد تهاجمی یک‌طرفۀ ایرانی را که به‌سمت تنگۀ هرمز پرتاب شده بودند، سرنگون کرده است. این پهپادهای تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد می‌کردند.
🔹
متعاقباً، نیروهای آمریکایی برای دفاع در برابر حملات بیشتر، به سایت‌های رادار نظارت ساحلی ایران در گروگ و جزیره قشم حمله کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440149" target="_blank">📅 02:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f6a2ce16.mp4?token=T2lOMmdn6GnGc_0Nx1DbQ_UGQI3Fpp3TBiChA4CIteOlbp5XGH2eAC0JmSSfJNK8Ri8L109Gth60xIu4pl-T6y4o9TvvJrqThwEu9CpSmyrgZu5qY9DmZT8thenAlMsdg-hkxrC5e19Fc2Z6Or4vlAO_yR9B6RD9ZoK1NcR7QyNFJLcb-fBuzHFT-hh1tvJcJhr74xa9TNJQ5WOKeJ1BYP_VpYntFxhgPvBVJOfdgU8reZB3FJN_15XDrNasm9dgs-ccfOXpQ1cqOC67eY_Z-fhuD9JWl7j2oZWnCw_CpRyvsv423HnAld6WIfAcjswxx6MbcNS54yCcjrfp54-vSabxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f6a2ce16.mp4?token=T2lOMmdn6GnGc_0Nx1DbQ_UGQI3Fpp3TBiChA4CIteOlbp5XGH2eAC0JmSSfJNK8Ri8L109Gth60xIu4pl-T6y4o9TvvJrqThwEu9CpSmyrgZu5qY9DmZT8thenAlMsdg-hkxrC5e19Fc2Z6Or4vlAO_yR9B6RD9ZoK1NcR7QyNFJLcb-fBuzHFT-hh1tvJcJhr74xa9TNJQ5WOKeJ1BYP_VpYntFxhgPvBVJOfdgU8reZB3FJN_15XDrNasm9dgs-ccfOXpQ1cqOC67eY_Z-fhuD9JWl7j2oZWnCw_CpRyvsv423HnAld6WIfAcjswxx6MbcNS54yCcjrfp54-vSabxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرگرمی جدید لبنانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440148" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsNGaTP4J8ApizMr7twpLIuScqQXxW0gPa87frWL9pVn2s1pbfd0KQrSRFJZx6xJD78wLGeQj00ubJNd9qWhJgq7VpUfysDtsdQWft-f3y14kjVhJWrQdN_FBeL6n0Y5rOtVjKzKDUdusN6cG6RNFcxbvNPUWt6tf_BpiahPmXf9Qb5BQelOKTWBeK7P8zD4b9BDxXzPmocTgQO-2ZM1yS1BMJY2w7y0GxS35IACEbDW_n7HB8KV1FwZdpoJdLcOJ-ZOtwNCysN4-06mESoUeqBnJlkgeiwOsKU1ex2TY0Mb1yRUjuP68jAW_wj_-Hx5rYyvt0OGz4H_23uAOwAzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک‌های ایران مغزمتفکر هوایی آمریکا در منطقه را از کار انداخت
🔹
مقامات ارشد آمریکایی تأیید کردند که در ابتدای جنگ با ایران، چندین فروند موشک ایرانی به «مرکز عملیات ترکیبی هوایی» در پایگاه هوایی العدید در قطر اصابت کرده و این مرکز را به‌کلی از کار انداخته است.
🔹
این مرکز بیش از ۲۰ سال است به‌عنوان «مغزمتفکر» و مرکز فرماندهی تمام عملیات‌های هوایی آمریکا در خاورمیانه شناخته می‌شود.
🔗
شرح کامل این خبر را که برای نخستین‌بار توسط مجلۀ نیروی هوایی و فضایی آمریکا به‌نقل از مقام‌های ارشد آمریکایی منتشر شده،
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440147" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440141">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t819DtAOR-I_dIoRrFwtZoJ6iQSurLN-FpfSogP6QhzToWlE3d7abjsQWtkWlTVJus0x3rXeQUxGVZCHPRJtZrgfi6xtsTNd-DkAGv5Qv_Qeb7pWcwxOfUmntQ2us-OrBpM_ahtjIvBLCOdX3ZejjSbLmQ18BJlWWrvw1gno8acoij2b3s5-ySAzCdMcMcro1pfKuJiL7zflJNjaUvDsHqfcY43dOcujnlSaYljUtk-rmXAa09ZwiopZQQb0oqMTeZ8heYb5nw4WJl2f76wjIAbgkVa76xoOyyLkfhGjscBq8HuNQbLk4luq0Z4AGpCMBFNkZSEH7nGE-5jv1Gi_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5PONy6PvWlZ-gHx8-SS8NhrWHOxOklKDKtdusfiTKZ7SS6jmDnS3fKbomst06eOgYNFPCecOwRC7sJpIq0kjn8t4LHGvGYkYBmqQC_wufRjAFwOXxVqOcbn7doha-hlKWqvipR8rT_oS__TiLJPiMdbmSoXmLKOb-jRXAtIes0YMCsZYnMXxhsBpj7Ciqii0wyHQsBUURh2QsDEgD29yM9UWS1vmkcrXbK4ifGPgljx4hKs0ba8Bj2p0JNXfm9MBDwrkk3yfW_Nz4UyuyIES1XfOlfKYc3sOe8iTj53poYuJsRnLvR5d226VNhfeGwtpQTenc_iQL_WWx8QjlKZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8xYBw5gKAoKHu06xOWUSiQLMq2dydmFRbuL65UPutzUynxD0fvuqoVIXiE-7Wr-R25fjnMKb6BY9ThIdclF9_lhwrf_IGKrRUY5ASr-ZhXedd1D5rpZgbRKYhrROUwYBIHKIb0ggLsVElC-Y5Qpn_wdhfckSxLyf8e3scmUsBJ_CGKBN14KssUCTf7E4gilcbzPNqypytLIqf-V2dp088zyxlz3NDLzKd2o8KUiTSvzM_vmuTThgxToHQHN1ttms5YiqCrpIf0bVmFeZHdy0f6yF-puWgf224TgYO35vwnSeAgqCLX76p2DPkMe4MzHHGWxFJpczoeH1o-KKc7F5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LxhSnowhzLJ8BkcWRhizCGc55QmtVtZdFo8GiFV9MNWFWTOjKL0j501lIGpwXX5xAqV_uUbDDWZC1nDaE9wcnPNKp_mJ5op5YDRuCD9k_OEKSSO7jZ8UejFRhZO1P35UMfzMN3qCCzcNihsIqcH2rEJ34DoNqvgjOaxSe6Zx4OogRgqtqycBGpAAWItwz4dvqrmxTRlEJRi9MZT_1C7uhzLl7MqbJ4qw30Zkn4x5xh-xL6xmx8LUD8wuQ7tnIFZKOLLmE46SV6J3f23lUE2yMUPStwEzyzUWyErFZ7UXnu8ZACsDeKMtaESgpgu3_b87-TBStdHo9NRnByRXoMkCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdQJ0XxRf2NtJt2YMNWXyl5kkU1qdN89G-CRxW3hrIF4zuOIaLyJHwdaQsNhUNANeMMdIFqKuL-L6ZA8JlQLFKqPhMdpH9QnW1mK4Mk0uMWxvewr6tQf2oQEmTkP9sToq3CS6rzMWfAryQ186mGGohmTPwmrSsnaXd6IIidc3e5z1htEmGymMjsVOavyv6y1-Jv9R8jXyS8qxup8WDgT0MSAa_flaA7bSXTbIXaxGTSmcBQhl_xBe-s3lI6ZbSKmdlBVXgTsDfkAoGkzkIBVO9kdIiinmJHhKcUAp_gETfoDsHfTQXYT-PmXL15u031zD-04ytDx-nJgs6y4ORbe4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fd7ThJk0lSGEAtpioTr7MneRopQw2eX1ONvHDB36QGilgEVS4Vuq9Jbl9RfvacEkTdyv1c-2DnWWqQ7JbzIueqp5xgx562oMliO579_2laeK9gXcpM2dPjh0fEQDAk4_bb0AipzbzVctt7MsVaKquIW4LPvpXIB4plmXcaZNe-iJjp93j0HAKRW7wSaN12EUQS0wCL5ep-4FPngKrCSfl-mMxBc2hombZC2VXA0a8t638LJ-9aZ9lhhFOLY0GFwdwGxZysbtq613KMEUdy27lXJ831xpYqd1hs-Hy_TYab3TNFL2pFDKum3IjG5xGjQz0EJnzEAjKcqMvDc9ahbW0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۶ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440141" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EW63ctWCDHSSjqGJO8-Tsioqa2sgz2F_4ZnY7RnMv52mz9zSYCTtpJ2NJJQpWx6bWvlcMo09pIJynw0W8eKUDr3sXn7kOqsb3NrB2eG-tHWGclQOwJclc-wYra03wn-L0EHcdm7cHAWo0WgW2PvXTb52UhxnXgzy3cU5r-Pv8fHqoyWC8WDuX8FFGs0xkbJebr-vhzghDc7ttPPHsnVTeaE5Ln2Cv87eQIYI12SHwF4aL5shxCPJXcRJGbPRm5Sjvlt1eH_Zp3pUu0q5o1RERIlHbM8UiU-OAXSVqXgZMOC-79JQzfBnQGBo2vzjBCVJEPRvkhfuTU6o5lUwVSYp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAGa_eerjsxZJrgxJedr0AjClWR1l3etuvVoMA2Lf4DI_bJ-nJTrSKF6jsPLQlLqmoCTj8JHhf7AbgQrCKjdmlj6RKEj_lNjgu8zarFK-r2HuLj_31QwmyYd0YE--g1HGsXLVcH86L_pP4V8JlWIUrehUi2e4Mt_vpVGnYJKl70zwPk0VqjqzvIl28cuDmvM--Az03ECMuQyeoMykl3Jb3lHA_pkrViNVOf6Sgo-exU_COTTEkHthZuDiQcr9GXXhiXYUBXgdCRZMXOmiKQicW7C4qHuYUo2fP3uCunuQQwdwcFNiUU-Lo9XklvFxhV9UjZdccMBAaL6yx70h4zjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gwj0MjLfFTLSkGMNdnQ847mYpOy1JHcyOLj_Mmy38sWs90Jl1aF1f343JVh7x15-9DIOKixAsg8WTjmZNCvBwGnGIm_7DXkkPEvmTMedWXiHE8osDcCsGjvf9fKkzA0a9sfdzLXtSL54uAJQPJN185PDOQbj05JF3ARyCcDPcd38ocFksQbHQgJFl2Q38h53oCEbshwRWhpOLOwSVi7R4hFtUqy1HjyPQktUIGI6JRBcsjPCWp6MbvXnGrjRjwY3GzRiwtUpSxuIelVw6w-bl3OZwu2gzas3GSRCjw9RuG-Y6rDdDTq6fGJvCFfbu7VHUv_jm7361N2HajxyfFsymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E1kQazPOgQ4WzMMsjnKDEy9MLhuO6Xz14v-SGNra2OiwMJQPWpWU8V5fKX5INRuOQAolLSFtPYbrGGPcN-NfI8qqPJmjyrs6fOLQX22v7EqZcx426S60YjohHqLL7T0Yuulz-IhAslPjMd9UnibLqq289sDS0ikoK5eb7tEGOnBi-rls-qbc4uQ6HE2kL7pPQrwoWjmwrtRyGjcGKktHxk0ZJDRP2lhrqj4R50QMl4XJTriGHziZXhyrSbzhoZVrLbmBKJsEhwE3muaumaaQtapBPqS8KEKd0MonfwM-1RiJ3Q-IInjLyc6Imr7fi7neEgFU_W6KlWtzraLuqQiW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFALjyhDZpns0i_NllCDb5HBp7vlptF1mRFU-cmty2nZp6JZYHsZGpdY-CulMv7ZDinAgbMyAxD-18BEVgyj-aJsCCUICW85l-K8Iqtd_E0-avcC3d7ZJM1wretagXYu_o7E8nldxknKwXARU7tsJSu4pyQmoC-Q5KU-3OXXCjwi4_C0PfgHq-gNUoNX5E6T0O9-4G1RDUXLLIDBlHPPhU7VR0QwB2KSFko19ZdANR7bWj4PcbKU-mMhJCHAJwEZW0f7WRPLSHqK4eyTBT0UWFfNgoqnH5sv6VXPPdXb8abTbnzKl2yyevKPb81c3ECw5gqs6huzz3vq9ZAiT4OBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFyfTvHi6rEBkWvL06SIpwJw7S7YzaavMrQgwc5S4XFRpmILloN4z2MU3drWpQAjKMdHd5fXxOenovIJKBPFLSstCaY8RN4iISYyZDuBRt7po0U5styU9AgK13HUqsF4p5jfyoinaNVII0k5BYWtgSJMWIkog7pPcaaWRwlwhKxl9al0RyuZD2n212JkaG_YoRZBbhvdaW7vyX_6EJvZ24_MF2MLGPuStgWwmeLoTdzlYoXMevMj_3rMXxv7dJxA6tmxrqi-hS2pH1FfnLLslxzdNUEgUNprBTY0OoxixRN6KRbdGkROefd4g07wKH6JjRDt1Q_h_GyjcOU3OUMloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn_Pyu3rewg9FxczYW4vYTVbGphcvtDzNJllm-rmeQMBkY0dVbwauqzoioiJk2qQQPbGW9riNw9gaLbFW3iVBzPQir0cN9KVLPOfIF2G8elOlwQ6WI1QJYBvL0vVAfoszQv6306DxJGZ3WH8hNPIzoLDzfhMUH4nkMTb2mglBzfoTA8Yy650AaipBIg0isfXJT1gRJrcMDtrhbMXdAI47bIE-1gXEJuhH4n6vqxq4CazxMZFafgt1kT1bHJ_fpGvaH7XUPLn0FWl-SsESnPKuZzwC1uvzpxbSXZjV8xvnC845ms6wG-AcNM5TsKK4dScEidiq_UQ7YIJXofzB3n9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFQz7FQhcCq1OVV3x4qr8nJ4tMmXftbBWqzcr3N5tH6cuhTL6JSocL_1vVg7fes3yJeKk2P7S7p5qw17p7rQH3fuohwnsV-f_mhGyxccsY4qv1uVNhLNGl8pJX25rmNnTOVu50lD-NH4bheVHYjrzKoluTYIi8Olruu1zN2vHXq7FnkLb40MNIbqCF2gN46XYWzViGNrir8KxgdIB8SUasYRRDKd0Aa9wcwhsMZXRsHgKQOxGdw6PQlewtegaGD3Tx2fMVVZzIYGNfSAbRd10r46cXm_61EuMiVo6J97-whQWUbMcNXvfwJbPuDDVxgTlVTJcpYqIB8Sg2bO-lG8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkB5seOO6SaJGonXgJcNQONSB3QxfXcEVvn5L2S7U1QGn2RVagU-n7w-fz7s-U2GAyotbpWNV2HpGI01z5SU5_Lz7fsuzHyN6oJM8cNK4vTHN4CHb5R-fBY7YPyPX8eTmidWZH47S_Fzs9jbXAHbldnYQuiE9ai5f4LVJJoJ8cjP2wvFhn0AltVKwdfLk0tNLjgoI-mlPVspA0jynbomwCvNLVFV7uXqtz8LBGrTzmkE8eyvRR3ODy3TcK6plJgyAGUZQVpA4z1zosuxL4CGddoewzgR8oLpVzf2dC9wsJO1u2dEUIxbV3PvRDpYNIKrxYsOSCUZhQezPBiO_gKaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTITINvbYkjMPX1ri_bObEMi15kXaUzuhm5zoJKvFcjJkLqaD76JlZ1WciAOek-crQeyMLrNlTzC6hohwQWTvzZDdF8TjQdP2Nw1Y5y_fSR1l_HqWbTygsuCLW7DqQggCAwaKERgP721BXM-3Gj4mr0ZOoEpS4CTEbGs1ThCtuohlbf2agB7fEfOoaZvAgeEeIsFH1MqpQN13wjErByiw5nrcV0KVZeYCbHWHuyHVM_0yd9E8URXbsr_Mr5Sz4F0mQctIE47fUv1nNok1u4UlWeA0Ip3lPvb4eSp2TiOFEDM_JiEj3kFrz5ee_f_bpXMWhhG591D8DY3I7onF8p2IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440131" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eebbfe92.mp4?token=fb3V_uYSO47fi2TEqMZSqjrQGFYY1cBc96gGw-kKtQ-oNp0KU7z9vhMu1HrSXaXWc7re9VvqGv1PIxMB1N0NNinhUed1sfFuUazBbKUbG2HBxR0HP8rLxJUMZ9ahiUaQS0p89E1ydeX9uuqfBhEZy2jQkmcEJC8_yf0rhfU0gc884R8VCSSIVYEoEAhvf4UBWAXa7adQhnbnmhColOmz8FcehbeGAxuS8-hk78k-POfRX_GchwPta2t7LPZ0rd4Kmks1B8Y_d9nYO-ikjV14e4ZhTWJFTn9LG0TAHXPZYbqA7uMUCNTq6K9xKBRW59QB9LqY_WgZbbA46sbJKnA_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eebbfe92.mp4?token=fb3V_uYSO47fi2TEqMZSqjrQGFYY1cBc96gGw-kKtQ-oNp0KU7z9vhMu1HrSXaXWc7re9VvqGv1PIxMB1N0NNinhUed1sfFuUazBbKUbG2HBxR0HP8rLxJUMZ9ahiUaQS0p89E1ydeX9uuqfBhEZy2jQkmcEJC8_yf0rhfU0gc884R8VCSSIVYEoEAhvf4UBWAXa7adQhnbnmhColOmz8FcehbeGAxuS8-hk78k-POfRX_GchwPta2t7LPZ0rd4Kmks1B8Y_d9nYO-ikjV14e4ZhTWJFTn9LG0TAHXPZYbqA7uMUCNTq6K9xKBRW59QB9LqY_WgZbbA46sbJKnA_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یادمان بزرگ شهدای حزب‌الله در مهمانی ۱۰ کیلومتری عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440130" target="_blank">📅 01:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حزب‌الله از رهگیری و فراری‌دادن جنگنده و پهپاد اسرائیلی خبر داد
🔹
حزب‌الله اعلام کرد یک پهپاد هرمس و یک جنگندۀ اسرائیلی را رهگیری، و آن‌ها را مجبور به عقب‌نشینی کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440129" target="_blank">📅 01:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حملات جدید حزب‌الله علیه رژیم صهیونیستی
🔹
حزب‌الله اعلام کرد یک موضع تازه‌تأسیس توپخانه‌ای ارتش رژیم صهیونیستی در شهر العدیسه را با استفاده از پهپاد هدف قرار داده است.
🔹
همچنین در دو حملۀ جداگانه علیه نیروهای ارتش اشغالگر در شهر طیری در جنوب لبنان، اهدافی را با شلیک راکت و گلوله‌باران توپخانه‌ای هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440128" target="_blank">📅 01:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46dc5a452.mp4?token=N99gwASAPvwYoGgRo1cvhzWE7uT9MbvmuQ-NuGGPWUVNmDVOW7FSfiGhfwYuycVt3SrckXuUeeZoAOx_hEKi6bKUM4O7kseCBIEEzcr9BNbVMlmlNwXNPcEwwN14Ku5M8Dcc_32E4CypPf59_tRKXO1wbFBca48Dfvq5egKuim5R2T1Xh2vR72p2fo5t1MIUjUpq1xx8RyHKulZtl774RS4HUANHIiBAHOFVlZX0vWm2qw0iOYynCxWVAYoc17t4um6CvavW1JNYfgrbhASnN5gVsADwgQ1XnFRYQyf3K4MyK8hsNT5OwHdf5wYq6-mKmGDAZYtto24ozCeAaj_6XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46dc5a452.mp4?token=N99gwASAPvwYoGgRo1cvhzWE7uT9MbvmuQ-NuGGPWUVNmDVOW7FSfiGhfwYuycVt3SrckXuUeeZoAOx_hEKi6bKUM4O7kseCBIEEzcr9BNbVMlmlNwXNPcEwwN14Ku5M8Dcc_32E4CypPf59_tRKXO1wbFBca48Dfvq5egKuim5R2T1Xh2vR72p2fo5t1MIUjUpq1xx8RyHKulZtl774RS4HUANHIiBAHOFVlZX0vWm2qw0iOYynCxWVAYoc17t4um6CvavW1JNYfgrbhASnN5gVsADwgQ1XnFRYQyf3K4MyK8hsNT5OwHdf5wYq6-mKmGDAZYtto24ozCeAaj_6XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کربلا تا تهران؛ روایت کیکی که عطر غدیر دارد
🔹
سال گذشته در روزهای آغاز جنگ، گروهی از بانوان ایرانی در کربلا مشغول آماده‌سازی کیک غدیر بودند؛ کیکی که با وجود همه نگرانی‌ها در باب‌السدره حرم امام حسین(ع) برپا شد. حالا همان خادمان غدیر، امسال در وطن گرد هم آمده‌اند تا بار دیگر این سنت عاشقانه را زنده کنند.
🔹
قرار بود کیک غدیر امسال بدون گل‌آرایی باشد اما در آخرین ساعات، گل‌های آن از راه رسید.
🔗
ماجرای شنیدنی رسیدن گل‌ها را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/440127" target="_blank">📅 00:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e0a3a6216.mp4?token=gxkXUFsxp-ftZL1SFuhGw5BU3Uc7CWCVRagmTy3eu7xPKUhsy-rlLBMImAWbudzFvWcF431SqDjg1PTgL8QSg97Iildk4K9ugPoC_-lw5LBlMJLGH1PXCCvsLJ4N0gV53AJMyoLD68YH6RMYY_ar0A0r_rsW_b9ji-pMoHG_1mFMbuwzikVmfNLMI0Rw6J0uZ_SyUv0elh5_ikMM69iV077-klk9l2xbD6J2i2NZF_j454IWcSvRn1vKlPyvomVB65exUuD36CsWtvAHIWaUoF68-KXKdhkHJF3IQ_8hDfrjibu6tP3A4FyYj4nAtEELXT-9yEApgH3MR8LmG_E0C4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e0a3a6216.mp4?token=gxkXUFsxp-ftZL1SFuhGw5BU3Uc7CWCVRagmTy3eu7xPKUhsy-rlLBMImAWbudzFvWcF431SqDjg1PTgL8QSg97Iildk4K9ugPoC_-lw5LBlMJLGH1PXCCvsLJ4N0gV53AJMyoLD68YH6RMYY_ar0A0r_rsW_b9ji-pMoHG_1mFMbuwzikVmfNLMI0Rw6J0uZ_SyUv0elh5_ikMM69iV077-klk9l2xbD6J2i2NZF_j454IWcSvRn1vKlPyvomVB65exUuD36CsWtvAHIWaUoF68-KXKdhkHJF3IQ_8hDfrjibu6tP3A4FyYj4nAtEELXT-9yEApgH3MR8LmG_E0C4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی مردم تهران در میدان انقلاب
🔸
نیمۀخرداد ما شکوه یک قیام است
🔸
شکر خدا دوباره خامنه‌ای امام است
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440126" target="_blank">📅 00:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf9719bc4.mp4?token=efo6MNxrX3vML7GJ7GczYosPwIsSN4L5NP8hZBHX4ufA4mgk-hmzWGRmvVUD0FiEOYvKm3PSE8zOgmrYReAfxBBazEii0z7DI79V41YoZ6ougoBaush6H8mS4StA8Yv0jef8HdV_7ha0o9qWWFLDQ0WTjqma9bVVwi8a8dLrydVjSRBHME5fMPF8ilTQaCq6ke1SvnTXo08jSoeTmTpgfWGbBNYJwxKgU87HFZxfDIfvDfIsoBynrOz6G-4D4AbIFARYhNLAb4-DDXaG0bCftetikfQ8SgpDaAHCYJud34lQiuzgR6b9M2z50MinAvuXHEHiM2vh7JoD8znziomSwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf9719bc4.mp4?token=efo6MNxrX3vML7GJ7GczYosPwIsSN4L5NP8hZBHX4ufA4mgk-hmzWGRmvVUD0FiEOYvKm3PSE8zOgmrYReAfxBBazEii0z7DI79V41YoZ6ougoBaush6H8mS4StA8Yv0jef8HdV_7ha0o9qWWFLDQ0WTjqma9bVVwi8a8dLrydVjSRBHME5fMPF8ilTQaCq6ke1SvnTXo08jSoeTmTpgfWGbBNYJwxKgU87HFZxfDIfvDfIsoBynrOz6G-4D4AbIFARYhNLAb4-DDXaG0bCftetikfQ8SgpDaAHCYJud34lQiuzgR6b9M2z50MinAvuXHEHiM2vh7JoD8znziomSwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: پاداش ویژه‌ای برای امیرحسین محمودی در نظر می‌گیریم
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440125" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb139a6b0.mp4?token=aN3njkXugHWAg0NjCIMJzYsVfjsNs_KNrx-Xj4iQmAx00z1L_-nMdHSw0KjQI_wj-S-Ua7dce3kjRucvM0jJLRiy-SZnRaaspz-fIcvkdYX6pmDb9rSLKBcLkoLRSPCWVV4XqnGMrNFcM3oZpmaoW-J_HN8OxM7LnTFihVMxhHCZWoaIQnQAYzK3wz42Ff75kD23d3j7x-VVpQgmAKumRMhmFaSDz4ju1fSMn_441HSdsxSfBF8cejA_OuT7vzhhDDtbhIScVicTgoVCHxIYaDE1SG0TpYi8xu9DDrcWXiYy6YhQ9BN8B4-IMe-TnVn76r8yc8fGLnQ97s3-bRld7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb139a6b0.mp4?token=aN3njkXugHWAg0NjCIMJzYsVfjsNs_KNrx-Xj4iQmAx00z1L_-nMdHSw0KjQI_wj-S-Ua7dce3kjRucvM0jJLRiy-SZnRaaspz-fIcvkdYX6pmDb9rSLKBcLkoLRSPCWVV4XqnGMrNFcM3oZpmaoW-J_HN8OxM7LnTFihVMxhHCZWoaIQnQAYzK3wz42Ff75kD23d3j7x-VVpQgmAKumRMhmFaSDz4ju1fSMn_441HSdsxSfBF8cejA_OuT7vzhhDDtbhIScVicTgoVCHxIYaDE1SG0TpYi8xu9DDrcWXiYy6YhQ9BN8B4-IMe-TnVn76r8yc8fGLnQ97s3-bRld7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: در رسانه باید وارد حالت تهاجمی بشویم
🔹
اگر در حالت دفاعی بمانیم، دشمن این‌قدر ادعاهایش را تکرار می‌کند که در ذهن مردم ته‌نشین می‌شود.
🔹
وقتی رسانه در ذهن مسئولین به‌شکل یک بلندگو و ابزار زینتی بماند، رسانهٔ ما نمی‌تواند از این جلوتر…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440124" target="_blank">📅 00:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d50afa4b.mp4?token=daKFtx81XQlvNAvLKZ4W6DcQYr96cAjKwVVlfXoH2YA8un5vbIQEd_fzE184uZ34k6bUUs2kwLimn0NblWK7RfPaXYO0e3BDcsmofLhxo2s6Sy5RyIHT6gNMF5M7VXnqSU7-pagPPP1pVoKuPucHU6-bj9_eBjYbl5xtlYMz6o0aO7HvMnD-rsGCmLnfkgHUQBvUoh_lS2QI1ydUMKw8qBZ0i4sLCmfcuYc4rolJfjqaG1jaf_PDlmqr7lgoERvBMluWRrkaJxf9ytCubE2Gv_BF7k9PVIpzcFp2_U_k7XQtO542R70M0AGWNzYhM-Y-egUadB2rszzmt5hhSfMvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d50afa4b.mp4?token=daKFtx81XQlvNAvLKZ4W6DcQYr96cAjKwVVlfXoH2YA8un5vbIQEd_fzE184uZ34k6bUUs2kwLimn0NblWK7RfPaXYO0e3BDcsmofLhxo2s6Sy5RyIHT6gNMF5M7VXnqSU7-pagPPP1pVoKuPucHU6-bj9_eBjYbl5xtlYMz6o0aO7HvMnD-rsGCmLnfkgHUQBvUoh_lS2QI1ydUMKw8qBZ0i4sLCmfcuYc4rolJfjqaG1jaf_PDlmqr7lgoERvBMluWRrkaJxf9ytCubE2Gv_BF7k9PVIpzcFp2_U_k7XQtO542R70M0AGWNzYhM-Y-egUadB2rszzmt5hhSfMvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: آقای پزشکیان تدبیر خوبی داشت که آقای قالیباف را برای سکان‌داری تیم مذاکره‌کننده پیشنهاد داد
🔹
تیم مذاکره‌کننده یک بخش کار را انجام می‌دهد اما بخش مهم‌تر، توضیح‌دادن به مردم است. ما اگر معتقدیم که این مذاکره ادامهٔ جنگ است، باید در…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440123" target="_blank">📅 00:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440122">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع عراقی از حملهٔ موشکی و پهپادی به مقر تروریست‌های ضدایرانی در سلیمانیهٔ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440122" target="_blank">📅 00:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440121">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4918f6c7.mp4?token=dGdqa4X--zVRCPcD04XoWBW0CTZQNBmQqZpRPnaVdKGzZ50DXjLSAqZ32kM5Cb22BlxeXcs4EUWtzkig5EBxakOi_6bq1dJkD1gq-jz_UOsTCdZLv5rOSd2Fc-4b5tiasoSTAaxDuzafOZDizaoBIc7qLwgt1TEJ4CwksQ9vNzMJQEKd9nip2u-RH1MVGHuWWrK79Iudqg47IDYLFzfQGHagEVQOh6pT5OLPyar7a-efdrFSBUO2_l4c5V2vv5OgiBpunVCV6jKDnusXWOfomXUAhKCJx7WIRmz3ivSQcWRl-7koR4HPuWukd7o417P2B72vcibL8qoTttyGN6-9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4918f6c7.mp4?token=dGdqa4X--zVRCPcD04XoWBW0CTZQNBmQqZpRPnaVdKGzZ50DXjLSAqZ32kM5Cb22BlxeXcs4EUWtzkig5EBxakOi_6bq1dJkD1gq-jz_UOsTCdZLv5rOSd2Fc-4b5tiasoSTAaxDuzafOZDizaoBIc7qLwgt1TEJ4CwksQ9vNzMJQEKd9nip2u-RH1MVGHuWWrK79Iudqg47IDYLFzfQGHagEVQOh6pT5OLPyar7a-efdrFSBUO2_l4c5V2vv5OgiBpunVCV6jKDnusXWOfomXUAhKCJx7WIRmz3ivSQcWRl-7koR4HPuWukd7o417P2B72vcibL8qoTttyGN6-9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: مردم ما شایستهٔ این هستند که به‌جز اسرار نظامی، تمام موضوعات کشور به آن‌ها توضیح داده شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440121" target="_blank">📅 00:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440120">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده است
🔹
ویزای برخی اعضای کادر فنی و اجرایی تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن خودداری کرده است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440120" target="_blank">📅 00:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440119">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee86e98bc.mp4?token=dm3iHQdi3niulhT9RMGDlkPumhwrXETlLzBJGMhkPF8bL254R5dhIHNpvLWvvELs_uP-maFsAapYgBbGwFFLJpgsui2JZgektGueEPfvrNzY6jyDRPISqQjiOX03emNtOO2FqixhZnjqwMNMU6PcmwsgSP41kyVAXcMFeRM4qB9w7KDbc-SIvguP5aG9JZdHC039NdGRsuhYE09GU8AWFZ1qt4vEgjK4GdHPwNVJ9fTj9HtWlNYrhHdfCpAjb9yG96VxYDiKRgvOpM5opBK6GIIIYhCnuq0p8ILQxJ-Rrt94iwR0C04e6IVtGWeJ5aJlQwq2wx19QrIevMRVIfKs1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee86e98bc.mp4?token=dm3iHQdi3niulhT9RMGDlkPumhwrXETlLzBJGMhkPF8bL254R5dhIHNpvLWvvELs_uP-maFsAapYgBbGwFFLJpgsui2JZgektGueEPfvrNzY6jyDRPISqQjiOX03emNtOO2FqixhZnjqwMNMU6PcmwsgSP41kyVAXcMFeRM4qB9w7KDbc-SIvguP5aG9JZdHC039NdGRsuhYE09GU8AWFZ1qt4vEgjK4GdHPwNVJ9fTj9HtWlNYrhHdfCpAjb9yG96VxYDiKRgvOpM5opBK6GIIIYhCnuq0p8ILQxJ-Rrt94iwR0C04e6IVtGWeJ5aJlQwq2wx19QrIevMRVIfKs1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: مردم حق دارند که از ریسمان سیاه و سفید مذاکره بترسند
🔹
خسارت جنگ توسط دولت چندین برابر میزان واقعی اعلام شد و شوکی که این رقم به بازار داد، قیمت‌ها را چندین برابر کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440119" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440118">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc28a8cfb.mp4?token=PwFx8Ml5MurGP2YtUoDtlmG49Rfz1NTv_4M2gRNiphJB5elAH8JnBUfTYg9MYkINuM1_e73E7E1E_jKBQ5Bjwhu5pHMJhIWNYdi2M_SbpDRVulOddmeda5M8elEyrufy8hsI5UBz8LkxR-2TxdixBO0Vwy9U7_y6EpNaoZv1UA0bdcgi_baiglvG2P1v6MpY20MFw7YYKxFHIK7haxjX17lEqVetB1G8cFhDxJJJZJ9Ew9aZv7jhZ2mkMnX18j0P6Ykk1PuDk_KEmw7SypGUZ0m-4uGhNahOjpAyCVLHDWy_Pa_GLbcDXX7-0eWWWxdpWAWPuDM0iJyei7buaWu-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc28a8cfb.mp4?token=PwFx8Ml5MurGP2YtUoDtlmG49Rfz1NTv_4M2gRNiphJB5elAH8JnBUfTYg9MYkINuM1_e73E7E1E_jKBQ5Bjwhu5pHMJhIWNYdi2M_SbpDRVulOddmeda5M8elEyrufy8hsI5UBz8LkxR-2TxdixBO0Vwy9U7_y6EpNaoZv1UA0bdcgi_baiglvG2P1v6MpY20MFw7YYKxFHIK7haxjX17lEqVetB1G8cFhDxJJJZJ9Ew9aZv7jhZ2mkMnX18j0P6Ykk1PuDk_KEmw7SypGUZ0m-4uGhNahOjpAyCVLHDWy_Pa_GLbcDXX7-0eWWWxdpWAWPuDM0iJyei7buaWu-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: مسئولان ما پس‌از مذاکرات پاکستان صرفاً به چند توییت مبهم بسنده کردند که بعضاً خودشان هم متوجه نشدند چه گفته‌اند.
🔹
این روزها بین مردم نگرانی‌هایی بابت مذاکرات وجود دارد که به‌دلیل کم‌کاری مسئولین در توضیح‌دادن و اعتمادسازی است. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440118" target="_blank">📅 00:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440117">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50592d8c60.mp4?token=vsFt_D0ewT-HD04LvLcznhGv4RiYD3QQdGO2AKUPTcrnDrxDkhe5wnHTE38OZYc0tAN2NxfnXkVwg1k2w9tpUe5q6o8HFrQuEu2kQQBYPToDJqcjXihAv7uK309rQSEXWejlZNg3BiuUkW6wG8pmd7rIVzGXmTLBaanUpRtis2WYQK24xL62ZJJ8-M8ye7bCt3dgB_G6U5pooKipn-xhTVQJH4AIp-DhfCLdyO7Ygey49xwRfxRfmxMSEMC0i-488DLn7ulDGxwJYpb-FCL0ba_zPoqh2vdpeXC4UUMi54d9umVRXZRUvxdM745OpQ6hobnKNqKUozJ1RUsut4xgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50592d8c60.mp4?token=vsFt_D0ewT-HD04LvLcznhGv4RiYD3QQdGO2AKUPTcrnDrxDkhe5wnHTE38OZYc0tAN2NxfnXkVwg1k2w9tpUe5q6o8HFrQuEu2kQQBYPToDJqcjXihAv7uK309rQSEXWejlZNg3BiuUkW6wG8pmd7rIVzGXmTLBaanUpRtis2WYQK24xL62ZJJ8-M8ye7bCt3dgB_G6U5pooKipn-xhTVQJH4AIp-DhfCLdyO7Ygey49xwRfxRfmxMSEMC0i-488DLn7ulDGxwJYpb-FCL0ba_zPoqh2vdpeXC4UUMi54d9umVRXZRUvxdM745OpQ6hobnKNqKUozJ1RUsut4xgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: منابع آگاه ما مقام‌های مسئولی هستند که به‌دلیل برخی ملاحظات ترجیح می‌دهند نامشان بیان نشود.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440117" target="_blank">📅 23:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440116">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a44ab62b6.mp4?token=LgctVXWOnl69hIuOK90tBP2YqRKiztn8vQxDMKT3MxQzafTr_pwh3slUSeu_27G4pt7oFgksS3ceYFns47dnHzMYwN3beAbF23HRgiuFWS2m4Ob2RjxKOh7m0_v-67NBISYwo6PRa5Ej4UA-8o-7gxIc_Anlt0ZY_Y7i9My8Xux0-L1ONrSEIp9ZtxHNvGciTYL_8TxrBFigTEP5kxwAbtcfGsTcEfqzeTTAd_HMEbwwrZmlcv2sTEFMxzwuW_VAJIsb01fbd4wpkLTkkGSHAC4UhCdjAjy_IjhoyEs7WmS36fuDDHCFtZtLfK0QffPd2mDBCavYJUz8ZCHhRBzf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a44ab62b6.mp4?token=LgctVXWOnl69hIuOK90tBP2YqRKiztn8vQxDMKT3MxQzafTr_pwh3slUSeu_27G4pt7oFgksS3ceYFns47dnHzMYwN3beAbF23HRgiuFWS2m4Ob2RjxKOh7m0_v-67NBISYwo6PRa5Ej4UA-8o-7gxIc_Anlt0ZY_Y7i9My8Xux0-L1ONrSEIp9ZtxHNvGciTYL_8TxrBFigTEP5kxwAbtcfGsTcEfqzeTTAd_HMEbwwrZmlcv2sTEFMxzwuW_VAJIsb01fbd4wpkLTkkGSHAC4UhCdjAjy_IjhoyEs7WmS36fuDDHCFtZtLfK0QffPd2mDBCavYJUz8ZCHhRBzf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: جای تأسف دارد که مسئولان ما بعضاً در مقابل جنگ روانی ترامپ سکوت می‌کنند
🔹
برخلاف تصور رایج، رفتار متناقض ترامپ به‌خاطر دیوانگی نیست؛ این رفتار کاملاً براساس مدل‌های طراحی‌شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440116" target="_blank">📅 23:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440115">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be19378984.mp4?token=b9QySaC26BcQgq8c_DYIFx8r4GuJVAfZJOWOR1HMzcN-MjTW5xiGe2qkQr7vrcPS4_zHS36Dyy0Fx_g2u_PemJGn-eA4q7L6B2Cq8DSfBu2SYW1AZVZKYSz7yQt1xgFOKmtYKUAHxHPX19ECXaM0jF7bjmPzRpNEMznIk0LDLfPivk3gtT5FVx3Ozg7XHovn2aNu65TczOprlSqt34Pc_vlL-sSrphfwaxkXR9UYyI7Mn3UsodL-bL3gUAsVQfUTXojLAkaHkOQLw916ikq6Z0yVrYgCWHrkKB8DEsaL9hB61ENgEiDIK_Jg3VuKXKLsiBXOS2W3a10wR8mIGcprEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be19378984.mp4?token=b9QySaC26BcQgq8c_DYIFx8r4GuJVAfZJOWOR1HMzcN-MjTW5xiGe2qkQr7vrcPS4_zHS36Dyy0Fx_g2u_PemJGn-eA4q7L6B2Cq8DSfBu2SYW1AZVZKYSz7yQt1xgFOKmtYKUAHxHPX19ECXaM0jF7bjmPzRpNEMznIk0LDLfPivk3gtT5FVx3Ozg7XHovn2aNu65TczOprlSqt34Pc_vlL-sSrphfwaxkXR9UYyI7Mn3UsodL-bL3gUAsVQfUTXojLAkaHkOQLw916ikq6Z0yVrYgCWHrkKB8DEsaL9hB61ENgEiDIK_Jg3VuKXKLsiBXOS2W3a10wR8mIGcprEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: جای تأسف دارد که مسئولان ما بعضاً در مقابل جنگ روانی ترامپ سکوت می‌کنند
🔹
برخلاف تصور رایج، رفتار متناقض ترامپ به‌خاطر دیوانگی نیست؛ این رفتار کاملاً براساس مدل‌های طراحی‌شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440115" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440114">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0383f214.mp4?token=R7c25gQoGD9wLeIRThSECcBsNm0AWOmMikpz9qK3hsOPpG8PJmz5PxEEIh2YZcDT8PH5xC7ii7sB65BXgTH-M-H26_2p_PjcX4h1oPcYMlh-ndbOY-IxfXB-FQWQlsFZJZGnnNA0Ce1uSZblV2By-39v7v9N1bbqj3810oAZBHPL1017I2YF9qSXy2uSqg0srilt6TLFQdWu_hWSYML77ic5D8ruLb6TWWBbuXSvp7Q3gSkdsCsg9P9PQmdWcOrUgTTLSFTCVlNviYiQbntHyEOeaTF91zEjr8vqVffjxeHD0SZwFNy92Fd7dGnDq4ANW-0SCkeRcZdN6xEhc8ZxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0383f214.mp4?token=R7c25gQoGD9wLeIRThSECcBsNm0AWOmMikpz9qK3hsOPpG8PJmz5PxEEIh2YZcDT8PH5xC7ii7sB65BXgTH-M-H26_2p_PjcX4h1oPcYMlh-ndbOY-IxfXB-FQWQlsFZJZGnnNA0Ce1uSZblV2By-39v7v9N1bbqj3810oAZBHPL1017I2YF9qSXy2uSqg0srilt6TLFQdWu_hWSYML77ic5D8ruLb6TWWBbuXSvp7Q3gSkdsCsg9P9PQmdWcOrUgTTLSFTCVlNviYiQbntHyEOeaTF91zEjr8vqVffjxeHD0SZwFNy92Fd7dGnDq4ANW-0SCkeRcZdN6xEhc8ZxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حنظله مدعی شد: مدیر ارشد موساد در عملیات بمب‌گذاری به هلاکت رسید
🔹
گروه هکری «حنظله»: یکی از مدیران ارشد «واحد نفوذ جدید» موساد در بخش مرتبط با پرونده ایران، در جریان انفجار یک بمب کارگذاری‌شده در خودروی شخصی‌اش به هلاکت رسیده است.
🔹
این عملیات پس از ماه‌ها…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440114" target="_blank">📅 23:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440113">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed88e7ec67.mp4?token=vf5lRKiXgMpWxPgXkbdUvxqJh-O2lKcTwrIjAJNRCSlO-bHEUC45SvttBVKUvSgSxO6G8K41O_3wPTMRQpRowhcYRFPRhuye84EGYvXph3heYhvcAzjBQkQBJE-sr0-9UH3sbXCG5vaYRA-KbqYtVfSt-59mrxE6OT0BpTfj-9H078m05rB2G__XpbraOZsYpyGxJmrHL64FeWNRxXRiXMYzzriMXLNKDa0t9mrjcOHwpTGhbPW3vvFRK9zD4uqaGp0bh8bt_OhX07YJC_o61GpfGCAPHFEKHomSRvcE61YAPEEEjsZaVUOpzsTgM6NsK5kwCqy3osrc7zu6BWi2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed88e7ec67.mp4?token=vf5lRKiXgMpWxPgXkbdUvxqJh-O2lKcTwrIjAJNRCSlO-bHEUC45SvttBVKUvSgSxO6G8K41O_3wPTMRQpRowhcYRFPRhuye84EGYvXph3heYhvcAzjBQkQBJE-sr0-9UH3sbXCG5vaYRA-KbqYtVfSt-59mrxE6OT0BpTfj-9H078m05rB2G__XpbraOZsYpyGxJmrHL64FeWNRxXRiXMYzzriMXLNKDa0t9mrjcOHwpTGhbPW3vvFRK9zD4uqaGp0bh8bt_OhX07YJC_o61GpfGCAPHFEKHomSRvcE61YAPEEEjsZaVUOpzsTgM6NsK5kwCqy3osrc7zu6BWi2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موسی عصا زد روی نیل، با ذکر «یا حیدر مدد»
🔸
قاب‌هایی از شیعیان امیرالمؤمنین در مهمانی ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440113" target="_blank">📅 23:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
رویترز: ویزای آمریکا برای بازیکنان تیم ملی ایران صادر شد
🔹
رویترز به نقل از مقامات کاخ سفید مدعی شد «روادید بازیکنان ایران برای حضور در جام جهانی صادر شده است».
🔹
این خبر در حالی منتشر شده که رویترز دربارهٔ اعضای کادر فنی و سایر همراهان تیم ملی نکته‌ای…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440112" target="_blank">📅 22:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGr3uwkgIwiE3yLfq9A5c_VSw3r9V31lXl5Fy1Mz0yRCN22TtpdURG1HsIs838SHCD4mYqB0beQ-EzM4EaNsLKA3G9EpvhL99DaGEBmi5nlEVaWw8fKMx3EagRWhvaA7J3mETn3YOQAKkjMYkZmQhlD_w5V1JX8VlOX_pz64AZFo9aT1LvdrldkrOuRUOm-2PlXyITfdYHixjz00HHbUpBoEVuGVNOf9gMzhN8DOnDdZ6AH5UeKsuspSIsjv1eCHRPBLJT_rgLkJcp0ay5-UhatVLDRUNQ1CzdwkTzD2C7x0EInrLTnAipiAG0hdCHpXAwBNMhhFj9U04aPJ49WpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sinz5Ny41WmXqQpTnNlNFDD7aoP1mEt9nkWptk0lKUmcAvPklJdT2NWx4Z18lqzc59BsjaY2WfJgmSemhOFlVQlGcyB5wQ04xXaie5y3PCfnriSGPAhLoFaZKRiLiqvDvuJsHDVVb4CZQj-amrZlhsZw7O2xYuEKn1muzQw2P2GKDTVJlfCN_PGP4EQx6652JiZd5gcwReUEq6hMYo53Imi8tvbyCdLH1IM6855EbwDRp-_Veg_-OdgS0wnAeHda7STzPvBk5UCdtE_bA6TTri6Prx4LL-MjyaoSeedMEqsDXPQ_2Jm4d5gumQ3CW4Ox8RUMDpqoihbgU0EIDfNuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3LKltPBmH0FnaQCu__pQxXpIbi5482RB7I2fQYW3frvx3Lyiwx5TbwAO-uQBxgi5ajRCs4aXtDfOtArDAOg7IdrbWLJOBuQmpmqYSazaZssWjcaUTiXv1NfwIE4UK6tV6AqQDOok0783iaHlRwv0cVQhpvwjqvy-xfC81X-YqEu0dB3kXJcJz0YkAUsp9C_nrbk7owhR4xyJb1rl14UlYUm2jdcQ1Rd3WGlHiiWlfpOQvUJHkMzI84oTlS1LIagL61XT0B_BYq15H1vwJ-2oPK5vK9oR-FP5e8qW6StILwjkRZQHZLnbO_ZzzSU63V5r82-yjDWUwgQjfUxW5Sljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsW6GZEqeOn4Zp51HYRbuaC3l6JH1CK61dHK5OhL9Wqd5aUmF-ier3_W5Zn3OFbGm5wXMDcjPyqBVfMNCD5nFcSkBAOxO9wUUyHMsJLn5GjLMJcDGxWfksUDY-WonMjA_7rHKuRwOkhkYXFa4iFlnisCrfdtTmLkY0mLyCqhmsgNegA8NoluoMpwu4_-v_kYbgYq3Hrl9nIMEzGLkIc3fp_pPymRPZv_rdaY7ujnylyIbMqxQjGkeMBbFsyFYjYKOlNLDV9Xo7lud5-daeuvfPGcb2FdB4vhJwB1mgaobbEFUnGWA5FbzHAhrTm3nugn9bVa2_kJE1rz1VZs1aAPwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دست‌نوشته‌های مردم بندرعباس در صدمین شب تجمعات حمایت از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440108" target="_blank">📅 22:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995e2f2c66.mp4?token=RF-LOCa3V9vKFZyoF1_jGoLtHgZ6NEQMQ8IpROxC0oTII50zZnm5FSdPppgIrW3mkOSu2ILzvGMxYcW4FP_5RTUYQQeMx3iEuzu8r3466PHEbizYs-Yjmr2Tr-KbpQtwR8ctyF-DwZBA6PWX9HCzIaHeYheRdfIqCp0Y3j0GXmd_IT0Jxxqd3FlVD9oULPx-_tKQbQSfXxZijEVbPRwQDE7encGDc2AX0QU2SfZ_-mbUvhgNjtuyyl7zR2SmMKKJn01lolWC7OPrO-Na7T2yhTHW-DtmO3zqbBDZUKPDq3cUaUQ0uSN4bjHO20j6PcOAbN5Ah9xs1szplWK3fgUR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995e2f2c66.mp4?token=RF-LOCa3V9vKFZyoF1_jGoLtHgZ6NEQMQ8IpROxC0oTII50zZnm5FSdPppgIrW3mkOSu2ILzvGMxYcW4FP_5RTUYQQeMx3iEuzu8r3466PHEbizYs-Yjmr2Tr-KbpQtwR8ctyF-DwZBA6PWX9HCzIaHeYheRdfIqCp0Y3j0GXmd_IT0Jxxqd3FlVD9oULPx-_tKQbQSfXxZijEVbPRwQDE7encGDc2AX0QU2SfZ_-mbUvhgNjtuyyl7zR2SmMKKJn01lolWC7OPrO-Na7T2yhTHW-DtmO3zqbBDZUKPDq3cUaUQ0uSN4bjHO20j6PcOAbN5Ah9xs1szplWK3fgUR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه اهتزاز پرچم الله‌نشان ایران در مهمانی ۱۰ کیلومتری عید غدیر
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440107" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074de96034.mp4?token=q-XD8TnEag9WnkGlI7EGLQZwOuDJZpW2RJBRqNFOABiducbPoWLIusBt_37H-yJBmp70Jca7QRzwny7za3Cilyl1gkAjNL7GT-lrsxDg000ZPs1kWp7-9AIzXIPUShBLQWR77r-lHVTL-qB-XGcdwcDquQz8O-5BbOuhy071g7_H1znf-XxKRnb_qYCoTjZzKKWj_iWuM-Jx_86HLWZgK_9Pl3ou6IL8BU4zGELBYWXWASpEVozE-7m3u23lJoUNwck-IIAZZK53zooVXpjL6x5mqlZdKvEWQFzs8_k_ZFvIglm56pCIXkue5TmaOXj7p15jeEbPuQsX3KrSwjWtPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074de96034.mp4?token=q-XD8TnEag9WnkGlI7EGLQZwOuDJZpW2RJBRqNFOABiducbPoWLIusBt_37H-yJBmp70Jca7QRzwny7za3Cilyl1gkAjNL7GT-lrsxDg000ZPs1kWp7-9AIzXIPUShBLQWR77r-lHVTL-qB-XGcdwcDquQz8O-5BbOuhy071g7_H1znf-XxKRnb_qYCoTjZzKKWj_iWuM-Jx_86HLWZgK_9Pl3ou6IL8BU4zGELBYWXWASpEVozE-7m3u23lJoUNwck-IIAZZK53zooVXpjL6x5mqlZdKvEWQFzs8_k_ZFvIglm56pCIXkue5TmaOXj7p15jeEbPuQsX3KrSwjWtPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شتر نذری در مهمانی ۱۰ کیلومتری عید غدیر تهران!
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440105" target="_blank">📅 21:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440104">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48a299dd16.mp4?token=eV02JIE3nc3NKqLxH8d6cjckqAH1twM2S8JYRaBc54qekedVwEMw2ywPUM-8e8vjFLFXT0OCUKr6bZhlXRs_ACtXuhhry72BlKn0vD70CKlJ4UAodKVVUUNulrlcn1vJw4KDYywHzR0nTQoxGN9eAWfHUZzTFuFy0X2p81SZps2nE7dIJ9nQr3wZPV0tq1urk8UU_O5-Mu3cfyU433YisaOR1PcLMFwfNXF6setXGhtxNVO9bG1IE0fr565JvveLxUyMQWavUqUR8lzEuUD1zeMwayTWr3u0c6xbNrqfWflO7nA6qX4PW5edR8qnQHjeeQdUdcDSVwFpsN7DQI0Jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48a299dd16.mp4?token=eV02JIE3nc3NKqLxH8d6cjckqAH1twM2S8JYRaBc54qekedVwEMw2ywPUM-8e8vjFLFXT0OCUKr6bZhlXRs_ACtXuhhry72BlKn0vD70CKlJ4UAodKVVUUNulrlcn1vJw4KDYywHzR0nTQoxGN9eAWfHUZzTFuFy0X2p81SZps2nE7dIJ9nQr3wZPV0tq1urk8UU_O5-Mu3cfyU433YisaOR1PcLMFwfNXF6setXGhtxNVO9bG1IE0fr565JvveLxUyMQWavUqUR8lzEuUD1zeMwayTWr3u0c6xbNrqfWflO7nA6qX4PW5edR8qnQHjeeQdUdcDSVwFpsN7DQI0Jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از چهرهٔ گندم‌گونت، گندم برکت پیدا کرد
🔸
قاب‌هایی از مهمانی ۱۰ کیلومتری عید غدیر در تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440104" target="_blank">📅 21:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440103">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: تا زمان مشخص‌نشدن تکلیف ویزای آمریکا به مکزیک نمی‌رویم
🔹
تمام ویزاهای مربوط به مکزیک و مجموعه‌ای که باید در تیخوانا حاضر شوند، صادر شده و هیچ مشکلی بابت هیچ فردی وجود ندارد.
🔹
تیم ملی ما باید فردا با پاسپورت‌هایش به تیخوانا مکزیک برود‌.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440103" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440102">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f46f0d5c.mp4?token=AgV-k5n7qE0Sv8OwHXIyQtTsTw2bJgt65R6ll9Anu_pX8fjwbHOmkz13EQ6XXT0H3i5_GPRtJwA_cBUNr8kTM3saENHwANu5oMo3T9PjCLY1MXY5FpjqHRhT_rHV8wLfi8tARsDWt9jR0aYZApMNLNZi5aNUDlMuApSUFmzjmla0VCI1qTB3VH6ZUIvigrzJILcJWiSPSanoWUZcbOtm5_fykOrXZ_4CJGp9ahPNgMqJ3eBwVymPK7OubWamnigfTFvwU7oBFBON6aXw7m8TmJWoR3g3Inh84WKP5SkFbVqQpTWehH0uxqyYqSmWdFuylaRI-XFG-FZ3BUH-sePDb7dVHNbS2qUTE_vJOJklKUJke_vwO24RjJEEOJbucdIl0lOckMVzHx55V0X2Rm4AGa_kr0lvIlywwlr5hLVmuMe2Ki-TPvqlE884XPBjRS75uj0_LyiEA8hr32GlwVf-4ZeJkdtJb1Vmx5TpfMdD5dhLaiVm3pxRRItw0XzGtMfOU7TzbhsU_Tf5QqZS_q1VUJrK0MS3qACQls4NrC0C1wdAX834xAdZTCJgyMPXNt5qyxKPdE9sN3N_WGCI4kRYg7x-pVdyMnERjFg_L0Vcz1uXPctKcaIFb_mz6sQc9O48wXQ2t2GOK-lysAFdauGYAAV_F67vOQJLBpG9c1HgQII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f46f0d5c.mp4?token=AgV-k5n7qE0Sv8OwHXIyQtTsTw2bJgt65R6ll9Anu_pX8fjwbHOmkz13EQ6XXT0H3i5_GPRtJwA_cBUNr8kTM3saENHwANu5oMo3T9PjCLY1MXY5FpjqHRhT_rHV8wLfi8tARsDWt9jR0aYZApMNLNZi5aNUDlMuApSUFmzjmla0VCI1qTB3VH6ZUIvigrzJILcJWiSPSanoWUZcbOtm5_fykOrXZ_4CJGp9ahPNgMqJ3eBwVymPK7OubWamnigfTFvwU7oBFBON6aXw7m8TmJWoR3g3Inh84WKP5SkFbVqQpTWehH0uxqyYqSmWdFuylaRI-XFG-FZ3BUH-sePDb7dVHNbS2qUTE_vJOJklKUJke_vwO24RjJEEOJbucdIl0lOckMVzHx55V0X2Rm4AGa_kr0lvIlywwlr5hLVmuMe2Ki-TPvqlE884XPBjRS75uj0_LyiEA8hr32GlwVf-4ZeJkdtJb1Vmx5TpfMdD5dhLaiVm3pxRRItw0XzGtMfOU7TzbhsU_Tf5QqZS_q1VUJrK0MS3qACQls4NrC0C1wdAX834xAdZTCJgyMPXNt5qyxKPdE9sN3N_WGCI4kRYg7x-pVdyMnERjFg_L0Vcz1uXPctKcaIFb_mz6sQc9O48wXQ2t2GOK-lysAFdauGYAAV_F67vOQJLBpG9c1HgQII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان تبلیغات: سپهبد شهید موسوی از رهبر انقلاب نقل کرد که ایشان در روز اول جنگ ۱۲ روزه فرموده بودند که «از اذان صبح عید غدیر تا پایان تجمعات میلیونی هیچ شلیکی انجام ندهید».
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440102" target="_blank">📅 21:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440101">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e4faefd.mp4?token=bEat8Ma2RUZSHUO6-RyPJO3y2BsjrcFTNGZhZ1FJ62rzsaG0fY_EgopjuYPohu-TTTgOHhv3XdKvN-EW9gN-mhPsDzd5XhoiI5rYPEu3zHZSb29jKZAQkMf7Zto11moQkVzvWmpovE_NnbqlqTsFHd3GWMdaVdXA18PmNAy-0_M13D-IIBaio55J8fMPPYfQxkgAi2pEAtk4JCXGNip97j0JH-q-1KYB2WZmbS_oVGNi1nl784EgObsw4X9DFjWJM9AWTyk2eAHvTHJdewgAE1dazZW7ym-u2rrsV65pWrKP4HVGAHtVCBK41CvAt5aB3JAF-_YZbinlAOGnLxCuUaaloCObkyOjHPsShIZBJcKwsg1qtcdArxmF6J696XO3AwsZ6chGyEoweENVhVFQiI_Ugx6ht3NIksSLhACUNrTo9GRpkIHJg9Dnhl9Q_0is5SYmPTowPAdXMm6jVkP0RjsFuVmuLGXhJo3zSX5V7lKg5OzR_YQZZY14MUV-7wG4lzJdmkorPQVcJCiIzvX5rEtQ_-8jEBYkZ0owfwHWkxVp6ni9ljRD8lYGTJkdv5fSMUEvhcyRyRpX3F1DJMNsUGNE0gLcgfUEQiQ-Zje_xuk7ZhIeOgc_JnGE2mkZ1Ltx917cpFS3q8trZGQ9QDyc5C3x8vKD2xi14jSfs3pfgPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e4faefd.mp4?token=bEat8Ma2RUZSHUO6-RyPJO3y2BsjrcFTNGZhZ1FJ62rzsaG0fY_EgopjuYPohu-TTTgOHhv3XdKvN-EW9gN-mhPsDzd5XhoiI5rYPEu3zHZSb29jKZAQkMf7Zto11moQkVzvWmpovE_NnbqlqTsFHd3GWMdaVdXA18PmNAy-0_M13D-IIBaio55J8fMPPYfQxkgAi2pEAtk4JCXGNip97j0JH-q-1KYB2WZmbS_oVGNi1nl784EgObsw4X9DFjWJM9AWTyk2eAHvTHJdewgAE1dazZW7ym-u2rrsV65pWrKP4HVGAHtVCBK41CvAt5aB3JAF-_YZbinlAOGnLxCuUaaloCObkyOjHPsShIZBJcKwsg1qtcdArxmF6J696XO3AwsZ6chGyEoweENVhVFQiI_Ugx6ht3NIksSLhACUNrTo9GRpkIHJg9Dnhl9Q_0is5SYmPTowPAdXMm6jVkP0RjsFuVmuLGXhJo3zSX5V7lKg5OzR_YQZZY14MUV-7wG4lzJdmkorPQVcJCiIzvX5rEtQ_-8jEBYkZ0owfwHWkxVp6ni9ljRD8lYGTJkdv5fSMUEvhcyRyRpX3F1DJMNsUGNE0gLcgfUEQiQ-Zje_xuk7ZhIeOgc_JnGE2mkZ1Ltx917cpFS3q8trZGQ9QDyc5C3x8vKD2xi14jSfs3pfgPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدون‌تعارف با جان‌برکفانی که هر مأموریتشان یک وصیت لازم دارد
🔹
سردار رادان: اگر بمب سنگرشکنی که به ستاد فراجا اصابت کرده بود، منفجر می‌شد، من امروز اینجا نمی‌بودم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440101" target="_blank">📅 21:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOLIKpNynMvfPB7TD0HnxuNMFPT5tIAWKLa-OCrm4ABLv7eS6WJLQtw-2S9ASe3lh8m75ISnUFs8IhFQWcV7vLGAjRa_Rm0PmPA1ZJmKGammSW3rnP5lsrAz53IhXwy_90E3teA8Tq-sKf4HOZ767Ne1zW1wE5yWbR6pWfu270_hnVz8PYUbUijCjEtCLvuH_t54wj7tlMFiiYASny65D6L32nP5vtGdlXrsmrWVIkq6IjMi3qUR9Wfn6kwbxyvDSRh0iPALhTcEj8BUnY-4P9cO1oxiBLvOtqhFCPRLNML8FQvmDhTAf3nwokYOLSBeiq2H6u02QEJchbNyr79hFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین: ایران به‌دنبال سلاح هسته‌ای نیست
🔹
رئیس‌جمهور روسیه: ما از تصمیم توقف اقدامات نظامی در ایران حمایت می‌کنیم و معتقدیم این تصمیمی عاقلانه است که می‌تواند به صلحی پایدار منجر شود.
🔹
من هیچ تحریکی از سوی ایران نمی‌بینم. ما معتقد نیستیم ایران به‌دنبال دستیابی به سلاح هسته‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440100" target="_blank">📅 20:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d046ae554b.mp4?token=SZHCveHlD0xQfTfhiHVCfBPVCPXmPqcUuQEaeGOeK3KwMOJNLwCTbKOdlKiD5UWxyMgKpLdLm6xBb0D0cBeer4hF-7Zv6L9t34_9pPJug9T0ChX3InmkwXbkvtnTOlX7drEORgLBZ_hzAGJIpw20tvTiEPMILQRPpDXxJAlgY1HSYX8m933z1Z0o0lebapGe_Jsq596v7Uhdqg0dZ_ED9X_JsrNbbnK5EdJrxmSk_3rnScW32wF1HYPPl_bweBB32yT4ZLpP_z1tsE9_5mWSqaToDs-AcKjCBz0Vse-flpXCJQvMgXiIBtHkbpuTO7EwbQ0IHmd8meohAKt0GG3zcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d046ae554b.mp4?token=SZHCveHlD0xQfTfhiHVCfBPVCPXmPqcUuQEaeGOeK3KwMOJNLwCTbKOdlKiD5UWxyMgKpLdLm6xBb0D0cBeer4hF-7Zv6L9t34_9pPJug9T0ChX3InmkwXbkvtnTOlX7drEORgLBZ_hzAGJIpw20tvTiEPMILQRPpDXxJAlgY1HSYX8m933z1Z0o0lebapGe_Jsq596v7Uhdqg0dZ_ED9X_JsrNbbnK5EdJrxmSk_3rnScW32wF1HYPPl_bweBB32yT4ZLpP_z1tsE9_5mWSqaToDs-AcKjCBz0Vse-flpXCJQvMgXiIBtHkbpuTO7EwbQ0IHmd8meohAKt0GG3zcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگل‌های ارسباران در آذربایجان‌شرقی، بهشت سبز طبیعت‌گردان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440099" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnpYgysWyH2AyYSDjstZIfJ6d6yWJYSedYi30YBuzsBMQ1Pmq2g6imeMseUmX7nlu7thDy0ELcizjilLGxVfr3RQHFck88xSuVMkY7VJeEvjM-2z9lbijLhKM3dtqNwolpmkwqbhxSNmthLIbFM5FNuzuNSjj665Lj5DqiuZCzjCBlH1oAg0cQi1eqKSXhVqqPGv8ts6aJ6GTRsfOBOOwF330WYG2ktwnYnj7YcAWsmo0MZj-JVwC38KyAPgI7-cq_yg7ub2sPvANROF2JODg45_z3ZSYC-smj_pU4WJcIxBHQj3UmDbrEQeZmdEYC0VLr8_B9SXTxQTcDH7L81MdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان با انتشار تصویری از پرچم ایران نوشت: سرو می‌ماند ولی طوفان به‌پایان می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/440098" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">زمین‌لرزهٔ ۴.۸ ریشتری در عمق ۸ کیلومتری زمین، حوالی منطقهٔ بالاده در مرز استان‌های فارس و بوشهر را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440097" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384f94b258.mp4?token=GmpQDUpBLoiDGdkapQ8zqxoVNALaVlZPmP2Ny0Uy8vn6w4L20tGAnRQUxanFImAkzhKKN0c13GcHd6ilSxsqhd1Lspm6AEywcagH1rp3TE6w-ljfr5zANIRhAk-kwQkfHjI1gWoXboBMZnuOqhswd-TYe7xcKwyU8gFejtgzIyWsUK83p7ikMJTYdbETMDphSvOOQ-9VOyOlNhKJtIgTusugxJi9DbcLUFbuvKKoJQ-b9s48rPTvY_2wcbLMB281zR1-HH8qHU-A08Z0nwA-VqC5BkX9YQ6FGZSLufpPeD5a91pGCaxLO3iAXgg7RjVb8cO6t4dNZdPi8xFkYepFKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384f94b258.mp4?token=GmpQDUpBLoiDGdkapQ8zqxoVNALaVlZPmP2Ny0Uy8vn6w4L20tGAnRQUxanFImAkzhKKN0c13GcHd6ilSxsqhd1Lspm6AEywcagH1rp3TE6w-ljfr5zANIRhAk-kwQkfHjI1gWoXboBMZnuOqhswd-TYe7xcKwyU8gFejtgzIyWsUK83p7ikMJTYdbETMDphSvOOQ-9VOyOlNhKJtIgTusugxJi9DbcLUFbuvKKoJQ-b9s48rPTvY_2wcbLMB281zR1-HH8qHU-A08Z0nwA-VqC5BkX9YQ6FGZSLufpPeD5a91pGCaxLO3iAXgg7RjVb8cO6t4dNZdPi8xFkYepFKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین زلنسکی را مسخره کرد
🔹
ولادیمیر پوتین گفت: «همه دیدند که دونالد ترامپ چطور داشت زلنسکی را ادب می‌کرد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440096" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440095" target="_blank">📅 19:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۵۷.pdf</div>
  <div class="tg-doc-extra">6.2 MB</div>
</div>
<a href="https://t.me/farsna/440094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۶.pdf</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440094" target="_blank">📅 19:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3bb2538f7.mp4?token=iAPoYLBDOLqz5sjVMTC1OJyQ4a7I3PE3cAeR7rNEYrsHws_n6-6bTZYb_WpXneWDllnFb6xTgDoDP9gfDj_br1gdHpzVsqtEd5aJFTC-nj50IXtU81VOjFN1YxxOC-_FUgscnT63fzJjyJsBCzqJpeYW2e-XIR-bYMwhF-niQG788aSORykmLV1Q-w6B1djSP83tM-G6PQusYiY2h_O6OB3iQURbNFcut2fkIG1Fd17lTm2lEQK1nodO6of46LQ69lXSlQn6bhzyKafMrHwWF1HkWpyQJbTKEf1pjEUdjaicCySCiXCnmkeRZWgzsiEfABJQriSbUH6osXWCF4t8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3bb2538f7.mp4?token=iAPoYLBDOLqz5sjVMTC1OJyQ4a7I3PE3cAeR7rNEYrsHws_n6-6bTZYb_WpXneWDllnFb6xTgDoDP9gfDj_br1gdHpzVsqtEd5aJFTC-nj50IXtU81VOjFN1YxxOC-_FUgscnT63fzJjyJsBCzqJpeYW2e-XIR-bYMwhF-niQG788aSORykmLV1Q-w6B1djSP83tM-G6PQusYiY2h_O6OB3iQURbNFcut2fkIG1Fd17lTm2lEQK1nodO6of46LQ69lXSlQn6bhzyKafMrHwWF1HkWpyQJbTKEf1pjEUdjaicCySCiXCnmkeRZWgzsiEfABJQriSbUH6osXWCF4t8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشیع پیکر شهید «قدرت زرنگاری» در جزیره هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440093" target="_blank">📅 18:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2023097cbf.mp4?token=VwSPG_wUyH1kD6MK209eOr6THnTkHCk2eKH-akvlox5VjJEqEFPi7IVbEOeWvsmCE5hHAIVejAb4sQa1He-eTlh2_zLIqsIzCKL2_dRJMSY0IMpVLE4NYoOcVJo6E2EEFK3MwtUhgW9VuL0pW0Zzf5q-u_QrfNkpMos8yBUcMoiOfr3aM_TZWCFbFvK3HU3ClI1c9uhSH79C9Wqq3Gsff4k_omah-kz9iyCgeVqVlzFI0gZo40r4lssTkuG4Q9NEFwxlRqtybS-HXzRV6b6rPvV8VkZCbNs40k-Tw6M8FMOOFKXNP1C1pPnLX0jMcrjoM900AUMIby9U1z0OxqBv0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2023097cbf.mp4?token=VwSPG_wUyH1kD6MK209eOr6THnTkHCk2eKH-akvlox5VjJEqEFPi7IVbEOeWvsmCE5hHAIVejAb4sQa1He-eTlh2_zLIqsIzCKL2_dRJMSY0IMpVLE4NYoOcVJo6E2EEFK3MwtUhgW9VuL0pW0Zzf5q-u_QrfNkpMos8yBUcMoiOfr3aM_TZWCFbFvK3HU3ClI1c9uhSH79C9Wqq3Gsff4k_omah-kz9iyCgeVqVlzFI0gZo40r4lssTkuG4Q9NEFwxlRqtybS-HXzRV6b6rPvV8VkZCbNs40k-Tw6M8FMOOFKXNP1C1pPnLX0jMcrjoM900AUMIby9U1z0OxqBv0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با راه‌اندازی خدمات شبانه‌روزی برای مشترکان
نخستین فروشگاه دیجیتال همراه اول در تهران افتتاح شد
همراه اول از نخستین فروشگاه دیجیتال خود در تهران رونمایی کرد، مرکزی که برای نخستین بار امکان دریافت بخشی از خدمات اپراتوری را به‌صورت ۲۴ ساعته و هفت روز هفته فراهم می‌کند.
این مرکز که در محدوده ونک راه‌اندازی شده، با بهره‌گیری از کیوسک‌های هوشمند خدمات مشترکان، مراجعه حضوری را سریع‌تر و ساده‌تر کرده است. توسعه این مراکز بخشی از برنامه حرکت به سمت خدمات هوشمند، منعطف و مشتری‌محور است؛ مسیری که می‌تواند شکل دریافت خدمات اپراتوری را برای مشترکان تغییر دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/440092" target="_blank">📅 18:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVq6WdXsaSQOt6YQ_WnEHWi8gDg7DmitPSfr7ANjR7-Ln0suLVwD1EYudwFBT1pjCw3qGfTtcO6VgN9PTY6YAbBWsJJK4gXAj-O5cWOvSvwkC4U8ub_dfOJ0qTfJkQrTVVB_rdmsa2bw2aM7ItiIwarEYasKBeC8PPr8vkiavH3bfXkaJiSQMMJhEqOb1R2rpaY2_wOVEMnmP6Lm-K1feuZPVz6_k7s6xqZVOqJI-3_9L7Xl8GOrA8BTHaJ6MT2J0dEq3SwxGC6GIXCVgjHWKb6WmvXLamgEK_wQS9AnU51MN_CXPUhQBgy7ycxpLG0ldSTMIH3BZtIlkzfN9quSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/440091" target="_blank">📅 18:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440090" target="_blank">📅 18:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440089">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ef468147.mp4?token=jAAoEqBFQT_0hVSxrjPzEWLwp3cgegvx1abjMvdqIm0xEvrocYNsbqei4ATp08mkl0M_XRQVuT7xRP54j4xAAIX6NKaw8p819K62jzwvBPwtnaG9L1rfYh3GrEg7Wbux5RSRu7i2HjpwczCYsbXsLhFBxbbSONXye0jwFcwvdJQwcvzTzmF0Zs53jYtEY6TnyqvUYlvEO_K3jZ9J6J7jVmp8ri_DBBt7iDeSX194VGCxbk7-cbmtVCgvE5qDQWUWGnv0zJ7DQ5Q6ywYKKsuVVmyew1IBllWoh4XkVvKOVg8d1O1CjDXeVMkxDZQBgO6Xp0279pfIkhmjcd6ZEmsoPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ef468147.mp4?token=jAAoEqBFQT_0hVSxrjPzEWLwp3cgegvx1abjMvdqIm0xEvrocYNsbqei4ATp08mkl0M_XRQVuT7xRP54j4xAAIX6NKaw8p819K62jzwvBPwtnaG9L1rfYh3GrEg7Wbux5RSRu7i2HjpwczCYsbXsLhFBxbbSONXye0jwFcwvdJQwcvzTzmF0Zs53jYtEY6TnyqvUYlvEO_K3jZ9J6J7jVmp8ri_DBBt7iDeSX194VGCxbk7-cbmtVCgvE5qDQWUWGnv0zJ7DQ5Q6ywYKKsuVVmyew1IBllWoh4XkVvKOVg8d1O1CjDXeVMkxDZQBgO6Xp0279pfIkhmjcd6ZEmsoPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیداحمد خمینی: دلتنگ حضور رهبر شهید در مراسم سالگرد رحلت امام‌خمینی هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440089" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440088">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎥
حضور تاریخی رهبر شهید انقلاب در مراسم شب عاشورای پس‌از جنگ ۱۲ روزه
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440088" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440087">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
گوشه‌هایی از قدرت موشکی و پهپادی ایران که در بازدید سال ۱۴۰۲ رهبر شهید انقلاب از نیروی هوافضای سپاه به‌نمایش درآمد
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440087" target="_blank">📅 17:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440086">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb64ae0c52.mp4?token=Z5efArzxU5MacjR6ESXDZBf115nqaSX7MNqKCIwSsVbrmn_TC2RhBNL1Idt5g3Gl6SZHPVdjGAw8PnldTLxQi8V3XMJTla52-yU9Adqy81Ro5e38XZtAFEN1Gdt-E-U9dHFdxu1kVh5cCpHf-LkjPZQz9HJi6uZRCSfSdz9jYYnKZXz4svi-ap-ltB2MgL3lneVAbwxxsHKnszFr6QDdYkIxOBvnAbNQQ0ICOiFuUBZANp1LskByper-MTuHFRmzluitkaJpZ0V7nkDHkbGFQ4vGId7OOgfpsdD0ghLYPZideU3uekeYsSCiNDdByM34BGrDcEopjVpDJFt9U6ojwDuIICeHIWxvPfI30GISBLDbUtWcUtlGaTgTa0kPipak7Z8jy1LiVZgUMWlysziUxIwcq6vmEE5_cjD0oWyC2jJPNC6S5dKQvhHsvTaCbcLrOUSMUNGGQesf5Lmp2wF-9J6JHUvvWwHgL0VzifrB3lwscxqBxf4xQJXweUPQDMqfjsAFDIfiVV6jFEl88WaNdCO7FoPxlZUaXJ-bD0dAeJQPyNtcbXvfi2BaKDV8wqQSJiz7UrJeDAMU9lLMJj75nXTfVN5iFiKnG7BQhc0tC_kdpGS2y47tW0BekzEMmg5KjWLPYrr7rjDqRyhaFPiU_ii0jR-uYLE286HP3P9hr20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb64ae0c52.mp4?token=Z5efArzxU5MacjR6ESXDZBf115nqaSX7MNqKCIwSsVbrmn_TC2RhBNL1Idt5g3Gl6SZHPVdjGAw8PnldTLxQi8V3XMJTla52-yU9Adqy81Ro5e38XZtAFEN1Gdt-E-U9dHFdxu1kVh5cCpHf-LkjPZQz9HJi6uZRCSfSdz9jYYnKZXz4svi-ap-ltB2MgL3lneVAbwxxsHKnszFr6QDdYkIxOBvnAbNQQ0ICOiFuUBZANp1LskByper-MTuHFRmzluitkaJpZ0V7nkDHkbGFQ4vGId7OOgfpsdD0ghLYPZideU3uekeYsSCiNDdByM34BGrDcEopjVpDJFt9U6ojwDuIICeHIWxvPfI30GISBLDbUtWcUtlGaTgTa0kPipak7Z8jy1LiVZgUMWlysziUxIwcq6vmEE5_cjD0oWyC2jJPNC6S5dKQvhHsvTaCbcLrOUSMUNGGQesf5Lmp2wF-9J6JHUvvWwHgL0VzifrB3lwscxqBxf4xQJXweUPQDMqfjsAFDIfiVV6jFEl88WaNdCO7FoPxlZUaXJ-bD0dAeJQPyNtcbXvfi2BaKDV8wqQSJiz7UrJeDAMU9lLMJj75nXTfVN5iFiKnG7BQhc0tC_kdpGS2y47tW0BekzEMmg5KjWLPYrr7rjDqRyhaFPiU_ii0jR-uYLE286HP3P9hr20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعای شهادت توسط رهبر شهید انقلاب برای حاج‌قاسم سلیمانی هنگام اعطای نشان ذوالفقار
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440086" target="_blank">📅 17:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
نوشتم «تقدیم به خانواده شهید عزیز، آقای سیّدعلی خامنه‌ای!»
🔹
لحظاتی از دیدارهای صمیمانهٔ رهبر شهید انقلاب با خانواده شهدا در سفر سال ۱۳۸۴ به کرمان با همراهی شهید سلیمانی
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440085" target="_blank">📅 17:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
«صدها مثل علی خامنه‌ای در راه این آبرو جانشان را میدهند»
🔹
روایتی از علاقه و محبت رهبر شهید انقلاب نسبت به امام خمینی(ره)
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440084" target="_blank">📅 17:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afbac845cb.mp4?token=JUWYirO6XSFHedNCOKZ6zKNW3iOBqONOvSAb-Sx02ZKmR21Xsfm8QmKRF3AKO7Jav3Nd66obnSYYqM1V4ld4Zb02sbSrj5dtsgOXjF_uZuuMl-cn2Y_6cxCdTPH_D-yFuzHnPumBMwhQhhW4Vexzb5cm4i_qMEWkgCOubO1jhCo7y-iLmJYiJG-CN2cUIxNYBNpPbBHG3NIGYkodEIgs6JUA1QHamywVPr85Y2bKvegqQvjLUncOUhDjZzg8_e5XWNZgO0-PRhCw_1B0_iXnlu9Xf5unTP92vUoqzpcPxbPva8wMH9xBYpI34Od2bY-t_qSZTg7MKxl_MnSS8Lku8Tm5ipegwH7sRhKCbIxTDdFaU2rbCb78A1yvqVnDJMEITS-r85GyyTw-ZHdzkbKCGHOmgJgN-RYxG3XTGOhBVEefxwZt57cha1mvgpi7ByH24MSbyEObxFVky0-KsRAchI2M3hjIR1RCgDPll9xLmOy9mBX4Zx55gxonIu-8GaWdDCLWdC32PN0DTIxbmNrqGgGw-Cb1KgYs1wYexF9mAUNCxRL6tgqvK-BbdV2BPByZU9P377_OT1Z0TYVGvSAJDnMCWhclq2KBEQaj6HZVe-HW5yd_3qYe3Z6A55UufyUH1uJHO_YZ7cn8XU4HQA3CI2DcbyMMye8uIfz7GbqBlGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afbac845cb.mp4?token=JUWYirO6XSFHedNCOKZ6zKNW3iOBqONOvSAb-Sx02ZKmR21Xsfm8QmKRF3AKO7Jav3Nd66obnSYYqM1V4ld4Zb02sbSrj5dtsgOXjF_uZuuMl-cn2Y_6cxCdTPH_D-yFuzHnPumBMwhQhhW4Vexzb5cm4i_qMEWkgCOubO1jhCo7y-iLmJYiJG-CN2cUIxNYBNpPbBHG3NIGYkodEIgs6JUA1QHamywVPr85Y2bKvegqQvjLUncOUhDjZzg8_e5XWNZgO0-PRhCw_1B0_iXnlu9Xf5unTP92vUoqzpcPxbPva8wMH9xBYpI34Od2bY-t_qSZTg7MKxl_MnSS8Lku8Tm5ipegwH7sRhKCbIxTDdFaU2rbCb78A1yvqVnDJMEITS-r85GyyTw-ZHdzkbKCGHOmgJgN-RYxG3XTGOhBVEefxwZt57cha1mvgpi7ByH24MSbyEObxFVky0-KsRAchI2M3hjIR1RCgDPll9xLmOy9mBX4Zx55gxonIu-8GaWdDCLWdC32PN0DTIxbmNrqGgGw-Cb1KgYs1wYexF9mAUNCxRL6tgqvK-BbdV2BPByZU9P377_OT1Z0TYVGvSAJDnMCWhclq2KBEQaj6HZVe-HW5yd_3qYe3Z6A55UufyUH1uJHO_YZ7cn8XU4HQA3CI2DcbyMMye8uIfz7GbqBlGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوت قلب رزمندگان
🔹
لحظاتی از حضور رهبر شهید انقلاب با لباس سربازی در جبهه‌ها و ماجرای جمله‌ای که ایشان به امام خمینی(ره) گفتند و رضایتشان را برای حضور مجدد در جبهه‌ها گرفتند.
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب…</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/440083" target="_blank">📅 17:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440082">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎥
پزشک معالجم گفت: این دختربچه دست مجروح تو را خوب خواهد کرد!
🔹
اشاره رهبر شهید انقلاب به انس ایشان با شهید سیده‌بشری خامنه‌ای هنگام حضور نوروزی در منزل شهید آشوری در فروردین ۱۳۸۰
🔸
بخشی از مستند «روزی که با تو بودم»؛ روایتی از دلدادگی مردم به رهبر شهید انقلاب…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/440082" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440081">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42002b2f8a.mp4?token=EaJRL61g3iYnU8zqvyOLmArlgzwvAyMZCcugcEKyJE9wOqnJVDtplRtOttzdrH0aEB___mplBg6U4DkCbn301QcS3mxz-DGwJtLweaXLqoBOntDyDXe2M4mHciox-0g1jd2D8ClGZXhpzpKhojMApPyhI6cTHp1eZxlhQMAgp8VaoiCsJ6YBZncxe4Iej8VoSqK4UlekI9KPHDaCDaCFrZvDRDVYyJc9K0nDFQ5KDI8vzc6C0kJpNfdDn-WyG3rHgb_T6NRsod2C0FOShXjCknoVN-d5gCGiCM2X4t5YoMra8o34G6EAHZV-Do3KQveU1h9T2uxDkt_2qY0DxH_3m6sz8GInlxWp7locUwAHcqS2KeTnOb0LEUf8ZUOUzlW4Uz_r5RiMl_aQ5Ko4TBRQqJwMGscY1d_5i46YTiZQqdJh7qYAN8wvbOOmWMP3afq8RzCllCu28d7n8Usz2FA5lmjRTY9Ogqxtz5gWF8jReo-FOUpOxJUhL23yx1WAn4TaR7X95mR__Ay12wItP0brU5u71lgVnIUBMP9clOIN4-CLhuOzyu2WLjVYgBwSRLEc8C2IeqPJPiQKJXgSrCLAhPKxjeYDtWBeVaH9sDHgibYHDVAHN2xY8PpMrwqip5YWRfNs9k1mVJpTCgfp-3pvLBnEYcw8-FNMMnGapQkBK2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42002b2f8a.mp4?token=EaJRL61g3iYnU8zqvyOLmArlgzwvAyMZCcugcEKyJE9wOqnJVDtplRtOttzdrH0aEB___mplBg6U4DkCbn301QcS3mxz-DGwJtLweaXLqoBOntDyDXe2M4mHciox-0g1jd2D8ClGZXhpzpKhojMApPyhI6cTHp1eZxlhQMAgp8VaoiCsJ6YBZncxe4Iej8VoSqK4UlekI9KPHDaCDaCFrZvDRDVYyJc9K0nDFQ5KDI8vzc6C0kJpNfdDn-WyG3rHgb_T6NRsod2C0FOShXjCknoVN-d5gCGiCM2X4t5YoMra8o34G6EAHZV-Do3KQveU1h9T2uxDkt_2qY0DxH_3m6sz8GInlxWp7locUwAHcqS2KeTnOb0LEUf8ZUOUzlW4Uz_r5RiMl_aQ5Ko4TBRQqJwMGscY1d_5i46YTiZQqdJh7qYAN8wvbOOmWMP3afq8RzCllCu28d7n8Usz2FA5lmjRTY9Ogqxtz5gWF8jReo-FOUpOxJUhL23yx1WAn4TaR7X95mR__Ay12wItP0brU5u71lgVnIUBMP9clOIN4-CLhuOzyu2WLjVYgBwSRLEc8C2IeqPJPiQKJXgSrCLAhPKxjeYDtWBeVaH9sDHgibYHDVAHN2xY8PpMrwqip5YWRfNs9k1mVJpTCgfp-3pvLBnEYcw8-FNMMnGapQkBK2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از مراسم جشن تکلیف دختران در حضور رهبر شهید انقلاب
🔸
بخشی از مستند «روزی که با تو بودم»؛ روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/440081" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440080">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
صل علی محمد بوی خمینی آمد...
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/440080" target="_blank">📅 17:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440079">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2cb50bea.mp4?token=cTutA_I-OyEmOwrkIG2G9shoCsN_MUGRUN8NdcIXE4XDNR6ddvOKa1Hhxa8vPSDvPP8jBX5-GTWv5v3LleX5zK3EIlJoZvXsKbNA4lHtOXZwbGPm_MvyLYSYLZrNmm6FGxfHfBxWrA8-N8XTq37ApmhHDCntthJcnGjU-bRTr2zkPLyuuXDVpwiFIu0wVFHJKE1ezMNXQGJxyGmkIPPKwxtpbRZtOM8vk94EHO9cMkyg784hcnLtRFht9qNZQn_a4Ljhn2mCy-rABjZWfDQzgrmJPzhnvbSet6An4cJU9rao27Qhq8_dXYFea-mM-4w-zGqT8phdEGguE_z6MM5N7hUxTeSdQfvxAF7nQ7Zy4Muxa3q2tlOXJAikDMYki5g1HUpkTlwq8xNOvk6vyIeswht334LPWj_MFok4YkCVFsVzuR7QYpeMIaAsib4qys_cPWeoUub_ofAVnqdukMYitUqrKpAMAMiWTCEBQTf8itACa1EqOOoI3_8yJKVqsMkFbhC_dSc9KfnhZlNE1PhAGMEnvh3t4rR3qle029UQoXWLG0uji3utov6tD47yhkyeGBJd6gsY1nnjQ4agnTeqplVGCFW-gYnezIClp-GH1vCA9GAYqXvxRx6duXa7vV67WGzfqnw8rCwNC1LoU4M7VJDnXoG4BGcVNUimxeYdhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2cb50bea.mp4?token=cTutA_I-OyEmOwrkIG2G9shoCsN_MUGRUN8NdcIXE4XDNR6ddvOKa1Hhxa8vPSDvPP8jBX5-GTWv5v3LleX5zK3EIlJoZvXsKbNA4lHtOXZwbGPm_MvyLYSYLZrNmm6FGxfHfBxWrA8-N8XTq37ApmhHDCntthJcnGjU-bRTr2zkPLyuuXDVpwiFIu0wVFHJKE1ezMNXQGJxyGmkIPPKwxtpbRZtOM8vk94EHO9cMkyg784hcnLtRFht9qNZQn_a4Ljhn2mCy-rABjZWfDQzgrmJPzhnvbSet6An4cJU9rao27Qhq8_dXYFea-mM-4w-zGqT8phdEGguE_z6MM5N7hUxTeSdQfvxAF7nQ7Zy4Muxa3q2tlOXJAikDMYki5g1HUpkTlwq8xNOvk6vyIeswht334LPWj_MFok4YkCVFsVzuR7QYpeMIaAsib4qys_cPWeoUub_ofAVnqdukMYitUqrKpAMAMiWTCEBQTf8itACa1EqOOoI3_8yJKVqsMkFbhC_dSc9KfnhZlNE1PhAGMEnvh3t4rR3qle029UQoXWLG0uji3utov6tD47yhkyeGBJd6gsY1nnjQ4agnTeqplVGCFW-gYnezIClp-GH1vCA9GAYqXvxRx6duXa7vV67WGzfqnw8rCwNC1LoU4M7VJDnXoG4BGcVNUimxeYdhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به چادر ما نور آوردید...
🔹
گفت‌وگوی صمیمانهٔ رهبر شهید انقلاب با مردم زلزله‌زدهٔ سرپل‌ذهاب و تذکر ایشان به عکاسان و فیلمبردارانی که با کفش وارد چادر زلزله‌زدگان شده بودند.
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/440079" target="_blank">📅 17:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440078">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
لحظاتی از حضور رهبر شهید انقلاب در منطقه زلزله‌زدهٔ سرپل‌ذهاب با همراهی آیت‌آلله سیدمجتبی خامنه‌ای
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/440078" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440077">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ffa4d20a.mp4?token=P5d0UEEIf5p_244DR3S0uzShAsM3bWKW-sUfWNaiuJH3IYLyuZePCVm7kRsm7heQGQGNnSTuibCAfmsx4AlVuUM2dK_xuaHFW8k3x7H9nvjaWyf73FtSxwFpIwRplnmGJFmgEOGEzwJOQiq5XGuwACSPsa_pkxv7s9KYbv0ZS6ZXh9i-YKOwg1a5hL4BtKKTzFAs_3Cf6tJGfnS-0-JGW3N6VpgqYy7KhRun4NKsZteW0Co3ANq3BsYgLsWk5xjLc3TchytjK43N1wJMdTbubTsBS93xhydZ1E1uqfqD3Dvbd6NmNNm0IC0WAyKbPaOgeiZxGmz3W9PtSvjVDnWG-ozwdzjio0zHzYbiKSR6rnb8DeJwJv3RFWiz4t1JW9J9H8GbbPJEpOv5zts4OC-rlGVSHr20Fy3LVw3IfTt5X46FEjhg9b2gQtN8GUSvae90PgnKP27r7YAHD4TGnNtZC2CA0Z5hplSA8KkdpDvwXCATIr3MmuAoUfCVVIRVN3O19rX7zBcOj59kCmZSJjuII_BPxEVMQD-WaDhMHN-sBhe8f8FosUh8CNWqTHQVz8Npv-HyrHaePxSyaZGOfRZIW3QxJrQPEZMINzgfvI3fS8O79L9fEQEDXwRyWSRW2OcbBsKP_HIndBQrwQK8ULKUuwUjV3OmX_BrzsunF4iBPk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ffa4d20a.mp4?token=P5d0UEEIf5p_244DR3S0uzShAsM3bWKW-sUfWNaiuJH3IYLyuZePCVm7kRsm7heQGQGNnSTuibCAfmsx4AlVuUM2dK_xuaHFW8k3x7H9nvjaWyf73FtSxwFpIwRplnmGJFmgEOGEzwJOQiq5XGuwACSPsa_pkxv7s9KYbv0ZS6ZXh9i-YKOwg1a5hL4BtKKTzFAs_3Cf6tJGfnS-0-JGW3N6VpgqYy7KhRun4NKsZteW0Co3ANq3BsYgLsWk5xjLc3TchytjK43N1wJMdTbubTsBS93xhydZ1E1uqfqD3Dvbd6NmNNm0IC0WAyKbPaOgeiZxGmz3W9PtSvjVDnWG-ozwdzjio0zHzYbiKSR6rnb8DeJwJv3RFWiz4t1JW9J9H8GbbPJEpOv5zts4OC-rlGVSHr20Fy3LVw3IfTt5X46FEjhg9b2gQtN8GUSvae90PgnKP27r7YAHD4TGnNtZC2CA0Z5hplSA8KkdpDvwXCATIr3MmuAoUfCVVIRVN3O19rX7zBcOj59kCmZSJjuII_BPxEVMQD-WaDhMHN-sBhe8f8FosUh8CNWqTHQVz8Npv-HyrHaePxSyaZGOfRZIW3QxJrQPEZMINzgfvI3fS8O79L9fEQEDXwRyWSRW2OcbBsKP_HIndBQrwQK8ULKUuwUjV3OmX_BrzsunF4iBPk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از حضور رهبر شهید انقلاب در منطقه زلزله‌زدهٔ سرپل‌ذهاب با همراهی آیت‌آلله سیدمجتبی خامنه‌ای
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/440077" target="_blank">📅 17:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c972cadd0.mp4?token=sMaonv01NVCfs_fwdIrFm7ILMChfLIC9WNU-eI4Uhop-R8Wk5WMS9LNLUacvoYevZzZdw8LC3_ZGmO2nirJpyidse5RegXlAHyr0yOWDAEOtKiSXHjZgIbg7PBbGti_klW3mJ6slYNI0_-c6p3yHA0R8r5GkLOySOFU3f9-P9W3ySISQKQ_cPJseyzU6iAr8S9EEn7f-WlU4zdNZTPEN4z7yyDbxEl6k88YD0qHn-G7FVKOxzN8lFdRgu99uSm-cSIvWFAlNQMDkGR-NAMKlApUfTvzg_vFTpaBG9tK9CxivWM9TkjWrCo3Y_-yc4Ml17gJBsDbXLGi6evKEcYUwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c972cadd0.mp4?token=sMaonv01NVCfs_fwdIrFm7ILMChfLIC9WNU-eI4Uhop-R8Wk5WMS9LNLUacvoYevZzZdw8LC3_ZGmO2nirJpyidse5RegXlAHyr0yOWDAEOtKiSXHjZgIbg7PBbGti_klW3mJ6slYNI0_-c6p3yHA0R8r5GkLOySOFU3f9-P9W3ySISQKQ_cPJseyzU6iAr8S9EEn7f-WlU4zdNZTPEN4z7yyDbxEl6k88YD0qHn-G7FVKOxzN8lFdRgu99uSm-cSIvWFAlNQMDkGR-NAMKlApUfTvzg_vFTpaBG9tK9CxivWM9TkjWrCo3Y_-yc4Ml17gJBsDbXLGi6evKEcYUwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان اصلاح‌طلب: تا زنده هستم قلبم در غم ازدست‌دادن رهبر شهید مجروح است.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/440076" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ac7e16c0.mp4?token=a7eEz2sLP23euBnWhJuSE0CrwARYyKHcgZC7DmNOglFbFwafC5kXkWcB2Ipnb1PEGs6Omqow0sRO0VSSu7h5Hv4w_V0bxr6_aZPQ-dqYyauNYEvKuvbH3Cva8pMm3RjZ5TQwlKeO6JLXnwWDfkrPtnrHJvEbTZPyxluPhPCWJgNMpRi3E-vbCYpV8ID2Si69HlDWqV5fZQAWR05yyJXW4jcYstbgeG2C69J8F7lB52MWMoA-dkQEz_RWIyQzRNef5lP7NoR7kX3KfCA64JsRWZjIHhjQTupEFYu4N5rRd_icrqhVztSOkM0HM_ToBbACF4sYxtwdF4F4UI0DMh8PxiHplxIbJ0LeUpEXoAB2dpaWtQFo2-ioo7bolRp7F1laluhXaPay_azDF79km_WMtG0LDEX4ucK0KNa0c_EvVj6Z8PYl3tIu_nIDlZtXKmMZN63f86xy8R2CJSVg1g3rEr_TWLMlvuIXWP0ZmHXPIGeOM9TFIr75W2pJdXR-89QzdnR9ybsep_3OulO80CV37_kfoxx8n3wlEbT6V1UoUBEnx0l-qB1S6fJckT62ovw6icrSPIzGPYroPvSVm2lqD0-jOwX8z764USFaL_x6mxzDTlTpxDa51ov9no8dFX1ISu-FUOC2fpL29Old03RhExFLVZUVrSCToVl5dUxc4wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ac7e16c0.mp4?token=a7eEz2sLP23euBnWhJuSE0CrwARYyKHcgZC7DmNOglFbFwafC5kXkWcB2Ipnb1PEGs6Omqow0sRO0VSSu7h5Hv4w_V0bxr6_aZPQ-dqYyauNYEvKuvbH3Cva8pMm3RjZ5TQwlKeO6JLXnwWDfkrPtnrHJvEbTZPyxluPhPCWJgNMpRi3E-vbCYpV8ID2Si69HlDWqV5fZQAWR05yyJXW4jcYstbgeG2C69J8F7lB52MWMoA-dkQEz_RWIyQzRNef5lP7NoR7kX3KfCA64JsRWZjIHhjQTupEFYu4N5rRd_icrqhVztSOkM0HM_ToBbACF4sYxtwdF4F4UI0DMh8PxiHplxIbJ0LeUpEXoAB2dpaWtQFo2-ioo7bolRp7F1laluhXaPay_azDF79km_WMtG0LDEX4ucK0KNa0c_EvVj6Z8PYl3tIu_nIDlZtXKmMZN63f86xy8R2CJSVg1g3rEr_TWLMlvuIXWP0ZmHXPIGeOM9TFIr75W2pJdXR-89QzdnR9ybsep_3OulO80CV37_kfoxx8n3wlEbT6V1UoUBEnx0l-qB1S6fJckT62ovw6icrSPIzGPYroPvSVm2lqD0-jOwX8z764USFaL_x6mxzDTlTpxDa51ov9no8dFX1ISu-FUOC2fpL29Old03RhExFLVZUVrSCToVl5dUxc4wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه: هزینه‌های تأمین امنیت تنگه هرمز باید جبران شود
🔹
عسکر اسماعیلیان عضو هیئت علمی دانشگاه: ایران به دلیل مسئولیت در تأمین امنیت، ایمنی و مدیریت تردد دریایی در تنگه هرمز، ناچار به اجرای تدابیر کنترلی و صرف هزینه‌های مختلف است.
🔹
منطقی است که…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440075" target="_blank">📅 16:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
استاد دانشگاه: هزینه‌های تأمین امنیت تنگه هرمز باید جبران شود
🔹
عسکر اسماعیلیان عضو هیئت علمی دانشگاه: ایران به دلیل مسئولیت در تأمین امنیت، ایمنی و مدیریت تردد دریایی در تنگه هرمز، ناچار به اجرای تدابیر کنترلی و صرف هزینه‌های مختلف است.
🔹
منطقی است که برای جبران این هزینه‌ها سازوکارهایی مانند دریافت عوارض یا ارائه خدمات تخصصی دریایی به کشتی‌های عبوری در نظر گرفته شود.
🔹
اجرای چنین طرحی نیازمند تدوین چارچوب‌های حقوقی شفاف، قواعد اجرایی مشخص و ارائه خدمات مناسب در قبال دریافت هزینه‌ها است.
🔹
هدف نهایی از این اقدامات، افزایش امنیت و ایمنی تردد دریایی در تنگه هرمز عنوان شده است.
@Farspolitics</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/440074" target="_blank">📅 16:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5c520b46.mp4?token=FTHB5ERbJTcsZIpw7DkqxBIh-WpDN8_tSSjaNpnyZpL59INHTga1BhG8tySf-8UcwzSIQJmSWrKkmuUoe_9_xTDVscRCpNocBLX2MMEStDUc22DJAWp7e_9MNF04DaFOYyYGvQk9mFRGg8KZzkvVVp754xz8kENMtsFxuQKCSWOqVG1HIOgmRrbbmTNaUaOoIYn9AVvWJl-NArlRJQXPMlE3S5KnezawrJ1J7wVT0XRK-hLZb9-iygiNIJbmsnq8G6lF2TZtYFg4KGAlCa1948bHWNFUePb3_vUAfEEs6JhBCea7oXGsHHJVbMXfoqdxk0WAdI7DfbFAYWWHLheXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5c520b46.mp4?token=FTHB5ERbJTcsZIpw7DkqxBIh-WpDN8_tSSjaNpnyZpL59INHTga1BhG8tySf-8UcwzSIQJmSWrKkmuUoe_9_xTDVscRCpNocBLX2MMEStDUc22DJAWp7e_9MNF04DaFOYyYGvQk9mFRGg8KZzkvVVp754xz8kENMtsFxuQKCSWOqVG1HIOgmRrbbmTNaUaOoIYn9AVvWJl-NArlRJQXPMlE3S5KnezawrJ1J7wVT0XRK-hLZb9-iygiNIJbmsnq8G6lF2TZtYFg4KGAlCa1948bHWNFUePb3_vUAfEEs6JhBCea7oXGsHHJVbMXfoqdxk0WAdI7DfbFAYWWHLheXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک‌های صهیونیست‌ها همچنان شکار ابابیل حزب‌الله است
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440073" target="_blank">📅 16:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=vvzqxuo4lsKLdfVBVxH738xMV5F5hbwKItp4nIXRTl5-6U-mBDXY-Hr2mhjl7ptk2Q-IRskmAqxfp591j-Fkp6L12C7WHdk68YaFGHHJkwkcVxC-HaNC6CKoXg87wS4e6I1r4KY8ogCn1fCK-oWUHM-CUBltuIZfy4lXdi9hXec-r6-4Xd2Alx7GqSxKMuTuSXLonzPvKxKx8z0J9MWyZQnFvFhlbVS-gM9OVjHlwfTz9l2yocnRJu37kR74Fq3f2GONj775n_1NTMT0gH6OgZwzeVeYSQEmh2-duNdHXE9DZzXHVY24xjYGXSo0lBI-hal9qFQatzvGfm_sAoKo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=vvzqxuo4lsKLdfVBVxH738xMV5F5hbwKItp4nIXRTl5-6U-mBDXY-Hr2mhjl7ptk2Q-IRskmAqxfp591j-Fkp6L12C7WHdk68YaFGHHJkwkcVxC-HaNC6CKoXg87wS4e6I1r4KY8ogCn1fCK-oWUHM-CUBltuIZfy4lXdi9hXec-r6-4Xd2Alx7GqSxKMuTuSXLonzPvKxKx8z0J9MWyZQnFvFhlbVS-gM9OVjHlwfTz9l2yocnRJu37kR74Fq3f2GONj775n_1NTMT0gH6OgZwzeVeYSQEmh2-duNdHXE9DZzXHVY24xjYGXSo0lBI-hal9qFQatzvGfm_sAoKo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام موسی‌بن‌جعفر(ع) در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440072" target="_blank">📅 15:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b40f8bd30.mp4?token=bW96bQZepqYJyFoGJfux2acOzrBl14JOL0zbMEFrTaWN3dtUJZSU3GNwk-GrX5H6t7lCIyQBMZbDFXmEBF5AbeYzmHID1g29J93l2rX6dly6EQX_wJxwpsgV0yvcUiR8HMryllqkQQYOlAA0iZ5GALVc_pfPNy2Fky6LqcgKqG8on5b1jbumfhYBatW2Vj_sZZaeHZJfXgK351sB6anmoi9JBvwMdmTAoR5W1H9lCxMfRzxmzLF7ryprrv1zWYSLLTzWdy87mLgunLB6kx4OAN2VLdFyq21GXYg33xhtvR5ktuE5F96X0oVQ-P-3zHnA2X3MJYDJn7Okb0OqHdKXoBIjnOJ1CeBlOlBT_NVaRaLOtm8b8z49qLFRpjAAbZEtT45HF_alvi2oaeWH1x05PJmuhzzqEsIqAEiXtlDVVmIyszLMzJE1o163rhDBafqZsyYXlGNEj1jeWIZ-rpSWuBRQWaCUS5FljEQZVZMwNcd_kUkqFTD0f4Mvn_HSzH8-aRn_HCe-U_iYoU7zeA-DnQH1desw8OaQndgyI2ZCUezisufF0GFW2wpl-MExLtjqcu4VE0_bSI6qisY6vMeLsL_bq8tfJ5XPJKZtZO3TjHFZ6DIF28jF6hBASQK-wO8p_04PMA2vMfS7Jw5J4YzDQmvyl2roTPjZyc8in61oPoo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b40f8bd30.mp4?token=bW96bQZepqYJyFoGJfux2acOzrBl14JOL0zbMEFrTaWN3dtUJZSU3GNwk-GrX5H6t7lCIyQBMZbDFXmEBF5AbeYzmHID1g29J93l2rX6dly6EQX_wJxwpsgV0yvcUiR8HMryllqkQQYOlAA0iZ5GALVc_pfPNy2Fky6LqcgKqG8on5b1jbumfhYBatW2Vj_sZZaeHZJfXgK351sB6anmoi9JBvwMdmTAoR5W1H9lCxMfRzxmzLF7ryprrv1zWYSLLTzWdy87mLgunLB6kx4OAN2VLdFyq21GXYg33xhtvR5ktuE5F96X0oVQ-P-3zHnA2X3MJYDJn7Okb0OqHdKXoBIjnOJ1CeBlOlBT_NVaRaLOtm8b8z49qLFRpjAAbZEtT45HF_alvi2oaeWH1x05PJmuhzzqEsIqAEiXtlDVVmIyszLMzJE1o163rhDBafqZsyYXlGNEj1jeWIZ-rpSWuBRQWaCUS5FljEQZVZMwNcd_kUkqFTD0f4Mvn_HSzH8-aRn_HCe-U_iYoU7zeA-DnQH1desw8OaQndgyI2ZCUezisufF0GFW2wpl-MExLtjqcu4VE0_bSI6qisY6vMeLsL_bq8tfJ5XPJKZtZO3TjHFZ6DIF28jF6hBASQK-wO8p_04PMA2vMfS7Jw5J4YzDQmvyl2roTPjZyc8in61oPoo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شلیک اخطار موشکی-پهپادی نداجا به‌سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
🔹
روابط‌عمومی ارتش: در ادامه عملیات مقابله با شرارت ها و مزاحمت‌های دریایی و ربایش شناورهای تجاری و نفت کش توسط نیروی دریایی ارتش تروریستی آمریکا،  پس از شلیک‌های اخطارِ موشک قدیر و…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440071" target="_blank">📅 15:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f396a4ff6.mp4?token=f28htpfm12LseqFLT3s78SDvOH0Zj0o4k_YlMKMi4IJIFd4lzbFr5oc4oWlSkdiLuZsBJWmQEme24YbaZUP3MVk53UJlbu2l3BBbwCIn-ORaiu4OooI8i9NZPRoG2iergT1Bpn2RblVRRMCI1sEsjskemMXGOLe5RcyzeD4k4mJHNgxVAIDZV2tmX0sxcKRHC_AzlQEHIv6W0CK996JksTRh6kE3TcuqvAUM_4qZRkHeeEBozMbBn7qR-ppScfAcGbylCDwmqydggmnTW_mZ6hfWkn--qR9dYlRongGprbInmblqb_hB6BEesltPQg6jqO-D2WrgjxVAYilwvIQK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f396a4ff6.mp4?token=f28htpfm12LseqFLT3s78SDvOH0Zj0o4k_YlMKMi4IJIFd4lzbFr5oc4oWlSkdiLuZsBJWmQEme24YbaZUP3MVk53UJlbu2l3BBbwCIn-ORaiu4OooI8i9NZPRoG2iergT1Bpn2RblVRRMCI1sEsjskemMXGOLe5RcyzeD4k4mJHNgxVAIDZV2tmX0sxcKRHC_AzlQEHIv6W0CK996JksTRh6kE3TcuqvAUM_4qZRkHeeEBozMbBn7qR-ppScfAcGbylCDwmqydggmnTW_mZ6hfWkn--qR9dYlRongGprbInmblqb_hB6BEesltPQg6jqO-D2WrgjxVAYilwvIQK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شلیک اخطار موشکی-پهپادی نداجا به‌سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
🔹
روابط‌عمومی ارتش: در ادامه عملیات مقابله با شرارت ها و مزاحمت‌های دریایی و ربایش شناورهای تجاری و نفت کش توسط نیروی دریایی ارتش تروریستی آمریکا،  پس از شلیک‌های اخطارِ موشک قدیر و پهپادهای تهاجمی جدید شهید دانای نیروی دریایی ارتش جمهوری اسلامی ایران، ناوشکن‌های متجاوز DDG_103 و DDG_87 ،دریای عمان را به‌سمت اقیانوس هند ترک کردند.
🔹
به‌دنبال این عملیات و عملیات‌های روزهای گذشته، علاوه‌بر ناوشکن‌های دشمن آمریکایی صهیونی که در قالب ناوگروه جرج دبلیو بوش و مرکز فرماندهی نیروی دریایی تروریستی این کشور به‌عنوان عامل مزاحمت‌ها و اختلال در تجارت و امنیت دریایی منطقه بودند، ناوبالگرد بر  ِتهاجمی آبخاکیِ تریپولی نیز مجبور به ترک دریای عمان شده است.
🔹
مرکز فرماندهی و کنترل عملیات نیروی دریایی ارتش ضمن تاکید بر لزوم دست برداشتن دشمن آمریکایی صهیونی از دزدی و شرارت دریایی، تاکید کرد: با وجود گسترش و دور شدن ناوهای دشمن از تیررس موشک‌های استفاده‌شده، در صورت نیاز، موشک‌های این نیرو با برد بیشتر مورد استفاده قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/440070" target="_blank">📅 15:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JA8rB4Q7sGG7rvGNDzsn4FPzJeQS8ly8xCQ5IDKKB6IXIDbgOrlXvEzyAlqyfBnNFV1BZNzHpYoiQ5W78SKpoXRN5m1fFt-h8vO2xwkWNPW4swA5QicOzXBsgFP_kJptzfvYs6CGfDojxjFscTNHac20xf6JvnQ9lRbikhc8FeiypGMf46tkLLjUa2Q8wB8BEbX0PPsrcfVLS4HgSeppZwdRK5qamYqnBmnw8Sw3cr0MooI-1ywuedp0V1gMultt2Rdeul_T7BzQ2iC6Nt9DZPFQNtbFeM07vf15jdexycDnrId1W2Ddg_wg-aOsYQIfSPvfyzT7wp7rk_ym3rZpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6e1VtOwxYcGhcq7ewhrMqhmJ4PO2Azt0m_XCYOfxgNZpRZfttQaTAzfWvPTYIKqqpQ3PUnscM6D7mccue7DfrFTEUBFp1wLfHUGywxyhfmJH4Eb4cY-cqk3klzG28-47scsgY_zLSzTjk6aBoFbybbjydhxgxQev6gBK_Hdy-H4dqgNgQ5lfnpFVvURj2al9rUyi3XRAwGbD9IwBbHnC2riT8eJcRUMQqDe5amrI2E3_JvBBF22fFKCUOabc3Z77h9TJe-bl1lOrr0bo81uANBrPe5YN4k8LDnOl1BmJC_jJUNmS-duulCbRM2Q-tOzpMprElSatLNd5HSPzNsnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJAOkGQHq2Hpwwodk9E7jnh6qElXTwetzLq5CURApXMtzUBsaI4iNgScE6aKKa2e2eNt6DpcCtI2TEdMhv_Mpw8z9Pj--3aaCqcNFijCx8tp-HiUgasd1nD3h4CrThoa9vg5uhppAy-KOKz89gI3i5vspQGyKMOi2yrou5spNVZ8GwBaPnTO0Jz5Ym4If56O_Tv-PfrHH_aXj3xr1HfF5VVLQ1kqVtdqiRx3TIM1npdDtMHhR4gflD-Spq9yRAlpsYfB8r9houds6ZlYJA3Dnik_cyCU-mVFpUBIdg7J-HrFc2Zvaow8uXUaO6vrZ5U-yjbc2MIxU6FHEfdhKYGLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOLE8gsr_hgfRJoXArFJf0DoElGFwRlc1xL7Sd2q81vYbXnb4gVZgVAQPvOvtrT_QunZ0jMOc8UvG5Oz9s9UaSwUk9lsdAS2TuHtz9tdb5f5ewyvNYLcPifFaJTzz5Df34siEihR6roLt-u6c8B_wcSNrIikjUB-VBNz8zKKnsF_RLItrFykz98qTRfJVxjZ-OTqEOFMU5q1RF6FHgBSfhKsZIGH0otYJgtKaO7E-SzYSJ6TNHoWZIS9ODc7VX001HQrodZEA1_Fo5liJqIJcfZViUKtUh2zpTel74BmwVCU9VTYcmEk7UPsHRMnfE2kwwXtc2gP87dTlHo5WMtOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDS5ujLRDFYzBXijKkjLL_vxu1S3aU0iBswqpEJnvdnaVyi4GI6wEP6mrXsgSnCvtoGHYB4ey_eVJutpwXpW-GnC6AqNOw8yhADc0Bieoz23eS5QvzfO0t5578pZPC16peIB4TMkC18SLEsyq4HyyABAyQ6U0uD0vKIT80Qt_oSk1NB_6u14r106GOt06VmYYf0s0OtS8mNInX-hSbHJuHzr12ACVnMfpbHpUwiR6E8UnCE4DKoh8aQO22eoZhEkG2Nr70iKJVc045qnHVBt64F-wasaJhRKTczwFb7ev3j-ZHXmspQ2h6SU3BCD4YoFX22vmfTOgC8ntX61tQEiVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JN6CV65cA0BvpJK9NPIodSMwpRQccZFSyK5d-46CzPAgtGPCG2HAVnnlVnftPnfBmlHXozaQLtsOcxLeu9x1ZWbmQPC61nPewMRzXAW4sRX2wWqfmf8dkQ1oAFMbDgXzAvTCmhrWEKVWmG06zTbFrwFpyN_632KiFi8Y74BUWb9yk0f31Zh5Iy80IY2cuFdf40nUqSQBhB1MZWbbDlf1-f9f9jeUegL5vAgVzofzqaYIJ_Sb_VJ6Lsmb6JZ0xV_z7C9invgkZMgd0oZ0xlA75DeVg60IShBkDdFc7t4yvru3fGIz9QHCmbwQgUEtYcJHOPvtAMiDmXbJTPzNURtlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4xdD34AaTn8A-B6_bxG90gA2HMGGrEn5RBjtuRlS8GPZIkr0QWl9sYkzh7pEl2otCl9T-o2e3RP0EH7oO5H-DNDisbgb_lAxIVf6qABcWUKCjJpEqOav_LfxVcUR3k37Z7gywixt42MnOzwJA9mlzn8mPLmMJ1UweQrMr2s-s2CTi9u4WLDW3lUb3OECq96oFY6p9HTAM9dcsVbS8Uifgaer9FeFWpoCufSgeU-X33Rd73yIuRLw6BtVTEIYR1KNUkoxDEFMsXnhrWq7Qqp5ibgcDJsAHzL4Y8g7-vg0YAi_-4xPdhGktfzXCM47RGR5AqRa-tzfhvgvlTAJvc2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlzKBPTd6FgZMuWBMlDKoRE9GGhYOF3HAPV7KapuQqII5pl1C7HNCtB_oDV2Cce92opkjY9ap0f9uOTWjgdtcOhqtQ38yRUFm841nHAo8E56-8sG4IIY7P04rYjHtEQCoDFGR6JuFnqooKkGWa5277V0kUGZrppibNx6GXVdin_nYppYkFRjW02Skx5FcKP7cxyMY0hPo2FldtuynLwyUNy4T2Sn1oYwyLDgjGlstVTaTSycxf4TaFInuZRg9WhtLK44cGpSbVWVkDcKXf0UT8X8CBA6zKklfkfBr3d3AovaKjWsfKcmbemKXCvrZ_y3MoOAdQBnf9-Yv5hhxV--9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار حدادعادل با خانواده شهیدان خاجی و صاحبدل از همراهان دیرین رهبر شهید انقلاب
🔹
غلامعلی حدادعادل، حسن خجسته، اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب همراه با جمعی از اهالی و اصحاب رسانه با حضور در منزل شهیدان سعید صاحبدل و اکبر خاجی یاران و همراهان دیرین رهبر شهید انقلاب به مقام این شهیدان والا مقام و خانواده معزز ایشان ادای احترام کردند.
🔸
شهیدان سعید صاحبدل و اکبرخاجی همراه با رهبر شهید انقلاب، در اولین روز جنگ رمضان در اثر حمله آمریکایی صهیونیستی به شهادت رسیدند.
🔸
پویش «اول خانواده شهدا» به دعوت رهبر انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای، با هدف دیدار و تکریم خانواده‌های معظم شهدا شکل گرفته است. ایشان در پیام نوروزی سال ۱۴۰۵ تأکید کردند: «مردم هر محله، دیدارهای سال نو خود را با تکریم شهدای همان محل آغاز کنند.»
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/440062" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
منبع ایرانی: ادعای العربیه دربارهٔ موافقت تهران با انتقال ذخایر اورانیوم به کشور ثالث صحت ندارد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کنندهٔ ایران روز جمعه گزارش رسانهٔ‌ سعودی مبنی‌بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به یک کشور ثالث را رد کرد و آن را نادرست خواند.
🔹
شبکهٔ العربیه پیش‌تر گزارش داده بود که ایران به‌طور رسمی با انتقال بخشی از ذخایر اورانیوم خود به کشوری ثالث که مورد توافق طرفین باشد، موافقت کرده است.
🔹
این منبع به خبرنگار سیاسی خبرگزاری فارس گفت: موضوعات مرتبط با پروندهٔ هسته‌ای در مرحلهٔ کنونی مذاکرات مطرح نیست و بررسی آنها به مراحل بعدی گفت‌وگوها موکول شده است.
🔹
وی افزود: «موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد و ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و دربارهٔ برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
🔹
این منبع تأکید کرد که گزارش منتشرشده دربارهٔ موافقت ایران با انتقال بخشی از ذخایر اورانیوم به یک کشور ثالث «نادرست» است.
🔸
مذاکرات میان ایران و آمریکا با هدف رسیدن به یک تفاهمنامهٔ ترک تخاصم و آغاز مذاکرات ۶۰ روزه، پس از حملات آمریکا به چند کشتی‌ تجاری در جنوب ایران و تهاجم ارتش رژیم صهیونیستی به جنوب لبنان متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440060" target="_blank">📅 14:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0679961e.mp4?token=i1liEqKLdDH3FuNCSfhcxZTrL6XSxzi0TVYH3J11y8PS4HoAaoXMsNGn4iGeLGJKKB7KhOLiMTssgIgggQDKj6EVwFiJUhdr7wFKcNSsep2CqXYb-10b_KCwVctO_YfKXsr1KIbERgVqzt5k6Vzh6VO-GfJd0s8FZl2pZBgF9VlAPEQN5LRZq1lbHet3dslcAw8jKU9jiXTn2n5GpELS1YOVVA_ICBbWNhBSiAz-xg0BAlLSyFTaqEVpVlWgrLoukKQLI6LT47qvjENiU4ETNjY7ZxrolSU6b8o12JHaNfZc4SFTaWmzvLeSKkObmX7W-9Frqozdh89teLFLt_Q0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0679961e.mp4?token=i1liEqKLdDH3FuNCSfhcxZTrL6XSxzi0TVYH3J11y8PS4HoAaoXMsNGn4iGeLGJKKB7KhOLiMTssgIgggQDKj6EVwFiJUhdr7wFKcNSsep2CqXYb-10b_KCwVctO_YfKXsr1KIbERgVqzt5k6Vzh6VO-GfJd0s8FZl2pZBgF9VlAPEQN5LRZq1lbHet3dslcAw8jKU9jiXTn2n5GpELS1YOVVA_ICBbWNhBSiAz-xg0BAlLSyFTaqEVpVlWgrLoukKQLI6LT47qvjENiU4ETNjY7ZxrolSU6b8o12JHaNfZc4SFTaWmzvLeSKkObmX7W-9Frqozdh89teLFLt_Q0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران و وزش باد شدید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440059" target="_blank">📅 14:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e0870945.mp4?token=Sttt-4AaVEox3oOTSXkg5oLV-fe-T8pLTTzjkEiZlUFIz_D-XGGV1YjJasmXFtC-RWGEnEZ0JWbLlUkTjI_mAj9L7OZP25sXzUtm1KSXeBtlUX2bzjrcaXtyJGM6oD_46KbzC99dZMv1rvfb3idasaPGBT7r7g-6ew7w2AMl0qyTfNOpXYoRxfrBbk8SGzwbmtDOvzQHye4t9wuOgoZYxmNz_YG5KPncgxwzpN9EvRg9Mh87p8b3kqg38Cb56AVswayUxwpJSVVELOYWezIk_K5THAc_PfZj-qjMu9lgj9af2iAH7woYxVezqaKGE9yI8wfGhdqbaYuPkDFB095J2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e0870945.mp4?token=Sttt-4AaVEox3oOTSXkg5oLV-fe-T8pLTTzjkEiZlUFIz_D-XGGV1YjJasmXFtC-RWGEnEZ0JWbLlUkTjI_mAj9L7OZP25sXzUtm1KSXeBtlUX2bzjrcaXtyJGM6oD_46KbzC99dZMv1rvfb3idasaPGBT7r7g-6ew7w2AMl0qyTfNOpXYoRxfrBbk8SGzwbmtDOvzQHye4t9wuOgoZYxmNz_YG5KPncgxwzpN9EvRg9Mh87p8b3kqg38Cb56AVswayUxwpJSVVELOYWezIk_K5THAc_PfZj-qjMu9lgj9af2iAH7woYxVezqaKGE9yI8wfGhdqbaYuPkDFB095J2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع خودروهای نظامی رژیم صهیونی هدف حملات حزب‌الله شد
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440058" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv5qs89MaDBv1Nbc4HZhmwxF44F_TtFPdyPmOqwOPgjoYhY-ORceTT8npwv7ooRVLIZ4xiabKPiTxrByhF3peISnhtkaJRu4suXW6z6s_7pZ97DYmMy8DYTNw5h4ytpzfK-s83Z796G7A3f9zv9kC5GKp7QrAWTwvxmHGP1rWGJgTp0F39iRa2PJ-rArl2zMr-bkQI_eYWnR69ku5_byAa9kN39CzIDghW65IfsoJqH89SK0CPKf_IIsuMoA3NlksZWshM50PZoANMtYI0tsFjrkbGDgCXuRjBy5UyL1jfOu6TpZUzS7UWpXPB3hpoBlpFDlDBx9l0E-vzAVlpsB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل: جنگ علیه ایران میلیون‌ها نفر را در
معرض گرسنگی حاد قرار داده است
🔹
برنامه جهانی غذا: پیامدهای جنگ علیه ایران بر امنیت غذایی جهان در حال نمایان‌شدن است و میلیون‌ها نفر در کشورهای آسیب‌پذیر برای تأمین نیازهای اولیه غذایی خود با مشکل روبه‌رو شده‌اند.
🔹
در صورت ادامهٔ درگیری‌ها در خاورمیانه و افزایش قیمت نفت درپی وضعیت تنگهٔ هرمز، ۴۵ میلیون نفر ممکن است با ناامنی حاد غذایی روبه‌رو شوند.
🔹
پیش‌بینی می‌شود حتی اگر بحران در خاورمیانه فروکش کند، پیامدهای مخرب و زنجیره‌ای جنگ در ماه‌های آینده تشدید شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440057" target="_blank">📅 14:31 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
