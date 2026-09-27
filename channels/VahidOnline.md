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
<img src="https://cdn1.telesco.pe/file/fWxurDQFGjcUfnbKY44hn0LMV9aH5yAsCzGtWs00ZhhlGDbRVwOL1rawaCbnNv-GtdPRP-Zj5JDyqMmVJikq2TipIopeyNJEL5DiShIMT9k9h7NQCwo3v__14dMFUhefVS6y20qmoRzGOC9aDNyPOmFdF2ScF1x02wyNnIbphR4k05n0ADVtw3qKpN8UuFJ4sbyZs1iCCyIQrpCDrnDRNycW9p32Wc2XA2TO25Y_G99uzepl5txug3X1wQ8b9EFdhzkE3PKN5jH8vXF5_2_iQHFsrnrmC6sZDWunw7OZzXen0f02sgksKP3JNz2Q10JYO8JpbW7tElluiEZx2q-jkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.4M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=D9G1tHXgiVSeVolLvzWGebc7BzFtLJd5Cyz-e87JNPzaff5PNxfeKqK9QupffWocXYQgnxZqS3WBVpwo62wwn9wq097z9Trb3SFPadtuCwAK0lL0Xfg6IvsCs7X9A0rwd878S9GTiQ54uHqdhHLnwc3wft7_UK4zDbHvah7DKfEQhr84cvlVVMw8ZnF67Y9fm1VIY_sqqXhLX7OVxQP6cAtz-cf3bP_44K3hpAtfP9o10bFgW-7Sk6RQ7dndtE9HV19lIj0qiF6A7QqqJtMkzfDvUTRDukrVyDiXw4AfPWxluwDm7xVnh_NadQXS8IVxntC6ECBhIvW4RywX1L6KLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=D9G1tHXgiVSeVolLvzWGebc7BzFtLJd5Cyz-e87JNPzaff5PNxfeKqK9QupffWocXYQgnxZqS3WBVpwo62wwn9wq097z9Trb3SFPadtuCwAK0lL0Xfg6IvsCs7X9A0rwd878S9GTiQ54uHqdhHLnwc3wft7_UK4zDbHvah7DKfEQhr84cvlVVMw8ZnF67Y9fm1VIY_sqqXhLX7OVxQP6cAtz-cf3bP_44K3hpAtfP9o10bFgW-7Sk6RQ7dndtE9HV19lIj0qiF6A7QqqJtMkzfDvUTRDukrVyDiXw4AfPWxluwDm7xVnh_NadQXS8IVxntC6ECBhIvW4RywX1L6KLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"از او بگو به دنیا.. از او که قصه ای داشت
او جشنِ زندگی بود.. سروی که قد برافراشت
از اُجرتِ گلوله .. از شر که می‌هراسد
از مادری که او را از خال می‌شناسد
از او بگو به دنیا.. ای شاهدِ غروبان!
این رقصِ بی‌سران است، این داغِ پایکوبان..
یاد آر اگر رگت را با مرگ می‌خراشی
تو بازمانده‌ای تا او را گواه باشی!
دیدی که بر مزارش، رقصِ پدر کدام است؟
این هلهله عزا نیست.. آئینِ انتقام است
از او بگو به دنیا.. از نغمه‌ای که سر داد
از او که نیمه جان بود در کیسه‌های اجساد…
از او بگو به دنیاااا"
monaborzouei
Lyrics: Mona Borzouei
Music & Arrangement: Reza Sadeghi
Producer & Concept: Sia Davarnia
Executive Producers: Mahshid Hamedi Boromand & Farshid Rafe Rafahi
Director: Carlito Brigante
Video Producer & Director of Photography: Avid Eghbali
Ebihamedi
📱
youtube
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdldvDWQklFnOhltF5VOHaRIfCifUF3s_wxxdvCyrcydLtD7ttvhGjXBRjTEj6Rquyuis6sBMDnsNPH2a9vx6gNtH8JMbd08oGl16oQyDkIr0Z8GmSx2k5ZayehL9d8UKpoOa_h0D1RnHCWDEriAm0uB9jhKUs_JoXEzc1NxUe9qyoplUqjIgjIVJfE-H2Ni0u82IsgFhY4e6xz7wRfV7VzkvTdEBzUsHwSmIfGP9OPfZt5725mdW4-F2zJOn3fZ5Y5MP7RukhRBHXL6PwTPB_iMW0Yk60irnR01onYOT71vjOFGmmhoZBio5IhVWYLqaMdfcsqIli_Q9eQkQgiOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز یکشنبه پنجم مهر ماه و یک روز پس از آنکه اعلام کرد پیشنهاد ایران برای پایان دادن به جنگ را رد کرده است، در گفتگویی تلفنی با آکسیوس گفت انتظار دارد مذاکره‌کنندگان آمریکایی این هفته مذاکرات بیشتری با ایران داشته باشند.
ترامپ گفت: «انتظار دارم این هفته مذاکرات بیشتری با ایران داشته باشیم. آنها می‌خواهند به توافق برسند، اما این توافقی نیست که من بخواهم به آن برسم. این همان چیزی است که شاید یک سال پیش با آن موافقت می‌کردیم. آنها بیش از حد روی مواضع خود پافشاری کردند.»
به گزارش آکسیوس دو منبع منطقه‌ای نیز اظهارات ترامپ درباره برگزاری مذاکرات بیشتر در این هفته را تایید کردند و گفتند انتظار دارند دور دیگری از گفتگوهای غیرمستقیم میان آمریکا و ایران از روز دوشنبه برگزار شود.
با این حال، آکسیوس گزارش داد مشخص نیست اختلافات میان دو طرف بر سر مسائل اصلی قابل حل باشد. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار تعهد ایران به امتیازهایی در پرونده هسته‌ای است.
@
VahidOOnLine
پیش‌‌تر:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه پنجم مهر در حاشیه حضو در مسابقات گلف جام رؤسای جمهوری در شیکاگو، از رکوردشکنی انتقال نفت از تنگه هرمز خبر داد و تاکید کرد به محض «تسلیم ایران» و پایان جنگ، قیمت نفت به‌شدت کاهش خواهد یافت.
ترامپ با اعلام آنکه شنبه شب «مقدار بی‌سابقه‌ای» نفت از تنگه هرمز منتقل شده، افزود این میزان حتی از مقدار نفت منتقل‌شده پیش از آغاز جنگ نیز بیشتر بوده است. او همچنین گفت قیمت نفت اکنون از دوران دولت جو بایدن پایین‌تر است.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/auUPbXrv3SQN5zQ-nDJKQbnnlyi8_9PRfqpLjCMUocjYpMu7zfVZc9ww-BVgUMRlkPPKjS71RcMIrs4jdw7_0Duwd846jyvvr8hA7lVgRSMPTAKZJwraoG62dSOud6gY-HsVM2FXcCpdP_Ew7pgtM20gAqQFrhaJPWxaG8yrs4Izgi2BjlCZnb-gV8sqxSafOOcq4jPuV_kXPUV9vCy34S-oZsQaA9S45SAxoNa3sw5A-wYXdhCNynV0GSxEuOMICkJZsAlD1hi0hMcRkDxQHiBhEqOJUeZGbP_S67odnQuR_mlJI7NR5lawExFdg36-b3XgcGf4LfQj8oGJHGGw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L4GvrIU8ehSI-Zi0uLKyue2Em2L_EZVgwlTKljMaRnfN01KukJQzEzGlOk0_qqoxxs06DA_gpLL6rz7kY_-_jbQ1Nqoo1JUxvZY3rMGCTEo6dkdYgF4oENKU8q6Hr_lNHFe7OlA9kdzo5o2RvUZq0a6yVyw0roAWiRVTKqnoSYuKm9Z34PfUKgpa0LNBdgdx5XsigXvedE_pamCy-fXMwB-a08VdY-MYj7KNWj4-O2jPbT7RVp9wujumyNqEjv7BWuJ2qjQmaLmKqgyv38TrjX0Cp0qsec2p1UY3RmitMFIfTNQpCBqtO703KCeM-cOKsFdvTHNJd7GmonrP_y9Plg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، می‌گوید با وجود اعلام علنی دونالد ترامپ درباره رد پیشنهاد هفت‌روزه تهران، هنوز پاسخ رسمی واشنگتن از طریق میانجی‌ها به جمهوری اسلامی منتقل نشده است.
او با اشاره به اظهارات متفاوت دونالد ترامپ در روزهای گذشته افزود: «متاسفانه از رییس‌جمهوری آمریکا حرف‌های ضدونقیض زیاد شنیده می‌شود.» عراقچی گفت تهران منتظر خواهد ماند تا واسطه‌ها «نظر قطعی» واشنگتن را اعلام کنند و سپس درباره گام‌های بعدی تصمیم خواهد گرفت.
@
VahidHeadline
عراقچی روز یکشنبه ۵مهر ۱۴۰۵، در گفت‌وگو با برنامه «میت دِ پرس» شبکه ان‌بی‌سی نیوز، در پاسخ به گزارشی درباره احتمال ازسرگیری حملات آمریکا پس از انتخابات میان‌دوره‌ای این کشور گفت: «ما کاملا برای ازسرگیری جنگ آماده‌ایم. در برابر هرگونه تجاوز جدید ایستادگی می‌کنیم، حتی اگر به جنگ آخرالزمانی منجر شود.»
او در عین حال افزود: «هم‌زمان آماده دیپلماسی هستیم. انتخاب با رییس‌جمهور ترامپ است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=YWQOFWXDLDVLl04SmlaLJ6kwxdpQkjen6m5wCRtEqyIqCC41v9iPpkDvUMtCzU2ZpjEBlskW8yGUZPx9dzHpYYJHTMFWfrNHOatEkrwK6cfB9ZIs9f9rhPtBFUS-CvRyybRUdut82FH6kaw43McZPTdEEITGABKu-cSNOgjZpVxWzTdrb4V_KVHqP1ZGcD6_jwXOGCYzkp1Pgsgqhiru0T7-7XDSQEBgEdSocp6QpAuPQiIgZ1pNAw4KOrLZAPIE6FCJQnFZdWWuSlxNrNXjFKCH02wqSPoQTGSVbIGIvgB0t6CjRHYjMAlHJyHWLDs5kBOXOjFRqJO3dZxYkwMu3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=YWQOFWXDLDVLl04SmlaLJ6kwxdpQkjen6m5wCRtEqyIqCC41v9iPpkDvUMtCzU2ZpjEBlskW8yGUZPx9dzHpYYJHTMFWfrNHOatEkrwK6cfB9ZIs9f9rhPtBFUS-CvRyybRUdut82FH6kaw43McZPTdEEITGABKu-cSNOgjZpVxWzTdrb4V_KVHqP1ZGcD6_jwXOGCYzkp1Pgsgqhiru0T7-7XDSQEBgEdSocp6QpAuPQiIgZ1pNAw4KOrLZAPIE6FCJQnFZdWWuSlxNrNXjFKCH02wqSPoQTGSVbIGIvgB0t6CjRHYjMAlHJyHWLDs5kBOXOjFRqJO3dZxYkwMu3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: دومین زیردریایی بدون‌سرنشین آمریکا را در تنگه هرمز به غنیمت گرفتیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی روز یکشنبه پنجم مهرماه با انتشار بیانیه‌ای مدعی شد که یک زیردریایی هدایت‌پذیر از راه دور بدون‌سرنشین (زهپاد) آمریکایی را در تنگه هرمز شناسایی و به غنیمت گرفته است.
در بیانیه سپاه آمده است که نیروهای نیروی دریایی این نهاد در یک «اقدام هماهنگ و پیچیده» و با استفاده از اشراف اطلاعاتی و جنگ الکترونیک، این وسیله زیرسطحی را که  «برای جاسوسی در تنگه هرمز» فعالیت می‌کرد، به دام انداخته‌اند.
سپاه این زیردریایی را REMUS 600 معرفی کرده و گفته است که آن را به غنیمت گرفته و اکنون در اختیار متخصصان نیروی دریایی سپاه قرار دارد تا اطلاعات آن بازیابی و بررسی شود.
رسانه‌های وابسته به جمهوری اسلامی نیز هم‌زمان ویدیویی از این وسیله زیرسطحی منتشر کرده‌اند و آن را به‌عنوان «دومین» زهپاد یا زیردریایی بدون‌سرنشین آمریکایی که در جریان درگیری‌های اخیر در تنگه هرمز به دست ایران افتاده است، معرفی کرده‌اند.
براساس گزارش رسانه‌های دولتی ایران، این زیردریایی یک وسیله نقلیه زیرسطحی خودران (UUV/AUV) است و برخلاف یک زیردریایی سرنشین‌دار، خدمه‌ای داخل آن حضور ندارند.
این خانواده از سامانه‌ها برای ماموریت‌هایی از جمله شناسایی و مقابله با مین‌های دریایی، نقشه‌برداری از بستر دریا، شناسایی و پایش زیرسطحی و جمع‌آوری اطلاعات دریایی استفاده می‌شود.
ادعای امروز سپاه در حالی مطرح می‌شود که پیش از این، در ۱۷ شهریورماه نیروی دریایی سپاه از توقیف یک وسیله زیرسطحی آمریکایی دیگر در نزدیکی ورودی تنگه هرمز خبر داده بود.
سنتکام در آن زمان اعلام کرد که آن زیردریایی به‌دلیل نقص فنی متوقف شده و «حاوی اطلاعات حساسی» نبوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hjvrxnjbVuhM4-uTIyyWl5lvFDiAzgNc9dYbAUJCixA7li544YDYTVqSY3lOa9o6tlqMkxzcpBQPpeqobxH_EgkM2Xjs1-Mz6d9hnU_y8fYVTV89ZuoNJx7q3mfwH_SxBPM1-yq0yjEOzpxzy5akeL6nQSAANprPA1teI2fLf7reni5tlAamzYySXcjR2IAeXbwHEnyolmfTtPYK4PO9LH3u6SE6xUFmhiPDGsvBFuWDAoqjixYaU_vpNhDWSnd8c_Z2Zl32VNI5AXNLgn1IQe79eLAa_GLskc_KKv_uJmepf2yRq87hWRQqlt3ZF701Ny2nRfYe4UPMuMSBoZYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HfQu_enYmfZFjGMWYNcfEIo3IUPSg8GWs2e5OepO79DVJfJ4eDbi6iS1q4-f6kP2q9mLSx0sT5l_zJnP80D_8X6mx4HEZwOXS9d_Mq_jb5GLHBgR0jSKJWYl0p4WbIg_ESI-1GieWsjJz3GPIIxOkrKMu8q7Z3yGnrLwWplIDIo59UmHwEpXpWoZiCyCk_P40KU14WIxQ-mo8JuCCK3QY9NbdQzslduhVizvW0RmxpMK7jGgtcOGjoxVPrKd-kKKG9d9KjXSC829T2up8yZI8eridfYYpFmtprpmYEA35zi58H4U3Kwu4jPu-R8U_B7etn8fMy60SjKggtDq1F3TEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GFqYBzpb_ZAjFauSrxOYVxViIOqt6Otdl6qXTev83Zl0EYHzxMRYD0vQ_dFMa7e0vanajonUZGsCiSMR20RZgfli04f30KRJD6YAbI3PCV7ptWiBtSleKb0LYOQTP_j7UThcG0hgK-a4mThltz6wPLDjaOyf7G8zRbXrxBYTUn2basrCNtRiFSGOJJbzuRDu8n5ik4eAbilNac5gHQa0tPSGB4cDsumDGjNCeiFzzHqfCtf1UG5TQQFxUf9zhhtTmm3IA2sDltIKHOTFmKNTfpX7dgKG-y0MXfIcKmdxKypyz9I6zzY-ZcFJNrB3o7KOX_G9AnqJpYPM_fd_D94ndw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمید رسایی در پرونده شکایت محمدباقر قالیباف به ۱۰ ماه حبس محکوم شد.
این نماینده مجلس شورای اسلامی گفته است که برای اجرای حکم خود را معرفی می‌کند.
دادگاه به استناد ماده ۶۹۸ قانون مجازات اسلامی، حمید رسایی را به «اعاده حیثیت و رفع اثر از ادعای نادرست از طریق انتشار تکذیبیه در صفحه اول نشریه ۹ دی» و ۱۰ ماه حبس تعزیری محکوم کرده است.
گفته شده است با توجه به اینکه این جرم قبل از دوره نمایندگی رخ داده، حمید رسایی مشمول مصونیت پارلمانی نیست و دادگاه او را برای اجرای احکام احضار کرده است.
@
VahidHeadline
عباس عبدی، روزنامه نگار و فعال سیاسی، به دلیل انتشار یادداشتی در روزنامه اعتماد به یک سال حبس تعزیری محکوم شد.
روزنامه اعتماد هم در این پرونده به دو ماه توقف فعالیت و انتشار محکوم شده است.
آقای عبدی در بخشی از این یادداشت که ۱۶ اردیبهشت ماه در روزنامه اعتماد چاپ شده بود نسبت به انتشار «اخبار جعلی» از سوی برخی از نمایندگان تندرو هشدار داده و گفته بود: «این افراد تحت نام نمایندگی هر چه بخواهند می‌گویند و کسی هم در مقام اصلاح آن‌ها برنمی‌آید.»
در پی انتشار این یادداشت، دادستانی تهران او و روزنامه اعتماد را به چند اتهام‌، از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» تحت پیگرد قرار داد.
@
VahidHeadline
صادق زیباکلام نیز در پی مصاحبه‌ای با خبرگزاری آنا به یک سال حبس تعزیری و از باب مجازات تکمیلی به منع هرگونه فعالیت رسانه‌ای، مصاحبه، یادداشت‌نویسی و انجام مصاحبه به مدت دو سال محکوم شده است.
@
VahidHeadline
حکم یک سال حبس در پرونده حشمت‌الله فلاحت‌پیشه نیز در دادگاه تجدیدنظر تأیید شده،‌ اما به مدت پنج سال به حال تعلیق درآمده است.
سیامک رحمانی، روزنامه‌نگار، نیز پس از تفهیم اتهام و صدور کیفرخواست با اتهام «فعالیت تبلیغی علیه نظام» به پرداخت جزای نقدی درجه شش به میزان ۸۰ میلیون تومان محکوم شده که این رأی قابل تجدیدنظر خواهی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdDEIecQwTcB0cNeaufmiHsPCliV_Rv-4xs0rXArjU0ZyFR5fS7QOexgXcTqqOuWffpKN8b1Yn1EYg053MpLfx5yUegn6KVr_lEX4sm3iehxl9eE9-vFoCUPKG-5xni8lJ6P8WwqMVqgYQdyLhJ1bzAbhd9bv-jBE4xinZx0DQ8ruKcSCCsHBtbNXZEs27TF31Ht44cSZ8jmM3imPjd5XLok7XqiCfDg04ydxUmxY1Nr_N3v38DN3vcCLqa-1HCdDYs7mhX5EZ8pNj_IXupZ0Q4SU2CYgfZOqDtvsgpUf0YrhFO1X3fSARy32EVue9SPRNLavKRQIW6Dh-_mLKFg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEvqj-HPZf1MRcqYkpKTNnu13TXok-Ggu-cP3e8I2uMEyFvcfooUNio19h5qZwwvReOmPCCm6MEP0aH4_ZX3kjoVcd1M2Xv1XpJ4WDXoRgP4LvYxde-8Al8nGyYJRssXPqjmsU-mAYBNpJdSnqt6qcrcGIjPtYq2js1iJahU10VG3RIjO5rmBezeL1ti66rJAqptymwt1z16DbgpePtFPqNvbnkHJFHsXb8XDEzQfk7_RDvaVGb0xiRuNFQ0PsvjATkdZrYFX3Zq_3hZHYXg2t7Y5l5O5E5WPtUmhomiQ0BTCScr64kBGa5tQA71CEaNYgqOgjCk4020Ck1kiZrnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت آکسیوس، روز ۴ مهر ۱۴۰۵، به نقل از یک منبع آگاه گزارش داد مذاکره‌کنندگان آمریکایی در جریان مذاکرات غیرمستقیم با عباس عراقچی، وزیر خارجه جمهوری اسلامی، به او اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند برای بازگشایی این آبراه شرط تعیین کند.
عراقچی در این مذاکرات شروط تهران برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای را به طرف آمریکایی ارایه کرده بود.
بر اساس پیشنهاد جمهوری اسلامی، تهران حاضر بود تنگه هرمز را بازگشایی و مذاکرات هسته‌ای را ظرف یک هفته از سر بگیرد، به شرط آنکه آمریکا محاصره دریایی بنادر ایران را لغو، تحریم‌های فروش نفت را رفع و آتش‌بس در سراسر منطقه را دوباره برقرار کند.
بر اساس گزارش آکسیوس، مذاکره‌کنندگان آمریکایی روز سه‌شنبه در جریان این گفت‌وگوها به طرف ایرانی اعلام کردند که جمهوری اسلامی کنترل تنگه هرمز را در اختیار ندارد و در نتیجه نمی‌تواند درباره بازگشایی آن شرط تعیین کند.
در حال حاضر ده‌ها نفتکش روزانه تحت حفاظت آمریکا از تنگه هرمز عبور می‌کنند و میلیون‌ها بشکه نفت را به بازارهای جهانی منتقل می‌کنند. با این حال، حجم انتقال نفت همچنان به‌مراتب کمتر از سطح پیش از جنگ است.
مسوولان آمریکایی می‌گویند طی ۷۲ ساعت گذشته حدود ۶۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل شده است.
در همین حال، قطر و دیگر میانجی‌های منطقه‌ای برای ازسرگیری مذاکرات میان تهران و واشینگتن تلاش می‌کنند، اما اختلاف دو طرف بر سر موضوعات اصلی همچنان گسترده است.
جمهوری اسلامی خواهان تمرکز مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا است، در حالی که دولت ترامپ بر دریافت امتیازهای هسته‌ای از تهران تاکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=I5BXLK8p3Fuwil5Fmssu6kfUwskpkL4ignW7uH2q4HbonYk1bBbkZWZoJRp_zeKt-qj4yK1pH-zCAHPdK-uxP9Dak4WxKmKQ5b9puXzUw6BCB7KNn5xHAB96L_Fkxy_mDzKa1HO84TRKYPpO6axrCUi6RgOzPHODR5PEv8VRCmmpObExuvwRYtg44hXf7rApJp3C7kaZQw9Jr28dyxPC4FKIA19jsQlv_kCYEKrFvA26FA3RLb1SKifiF-JNBf-M4yJPMTEjTmjw9B0bCWDgQhBR7e8U3KHkSL4GH9v8UL9CdaoOjZ_v8KRyRQzZxSsLZ4r3hvLXRyLxztarcB7MJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=I5BXLK8p3Fuwil5Fmssu6kfUwskpkL4ignW7uH2q4HbonYk1bBbkZWZoJRp_zeKt-qj4yK1pH-zCAHPdK-uxP9Dak4WxKmKQ5b9puXzUw6BCB7KNn5xHAB96L_Fkxy_mDzKa1HO84TRKYPpO6axrCUi6RgOzPHODR5PEv8VRCmmpObExuvwRYtg44hXf7rApJp3C7kaZQw9Jr28dyxPC4FKIA19jsQlv_kCYEKrFvA26FA3RLb1SKifiF-JNBf-M4yJPMTEjTmjw9B0bCWDgQhBR7e8U3KHkSL4GH9v8UL9CdaoOjZ_v8KRyRQzZxSsLZ4r3hvLXRyLxztarcB7MJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه چهارم مهر تأیید کرد که پیشنهاد جمهوری اسلامی ایران برای بازگشایی فوری تنگه هرمز را رد کرده است.
ترامپ پیش از ترک کاخ سفید در گفت‌وگو با خبرنگاران گفت: «من پیشنهاد آنها را رد کرده‌ام. آنها می‌خواهند توافقی انجام دهند که بر اساس آن تنگه را فوراً باز کنند، چون به‌شدت در حال شکست خوردن هستند.»
او افزود: «ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم و مقادیر عظیمی نفت از تنگه هرمز خارج می‌شود. دیشب ۲۹ کشتی از تنگه عبور کردند. آنها می‌خواهند توافق کنند و من هم با توافق مشکلی ندارم، اما آن توافق قابل قبول نخواهد بود.»
@
VahidHeadline
او بار دیگر گفت جمهوری اسلامی خواستار بازگشایی فوری تنگه هرمز است و افزود: «آنها هیچ پولی به دستشان نمی‌رسد، چون پولشان را از تنگه هرمز به دست می‌آورند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MffPtGz4Ll7_8scICcvFNOmojL-0vKqWqqb1Wbf5IN2g0hFHl0wWh1eXIpCJA8aqhfh8dFj7P56UuTKyzhFloHtfmTS-_CWiuSMIPhsYXP6-Nx6gr6lvsXfDhZLm-fVpi0wyFCLYIhqLGTt6w4v-m_PvsyWB1GNnOVamCvixkXiUSkOeAM8fWemUAsfQeGsv-LSrynb3N-mIxWt0_fcn5nBPd7k497tkY7LfufepynzvkZc9Ri1SCHhc7OMxCp94hTbUFfLf_rI67Y9G-zQRdPtHRkPBwRfQligrtnR-AOLmJyicW0EAlM3hIR5oyJbKbISKJsgacj9t6J6_YaoeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=dYEyCYCbuXvLwwAFSZwGZ6NoFpvwrqgEv7izcgEIpl_Xa2JQqYL95g0nawcEWLRbbmWkZuTK-mdLv1X0zJmMRNBPmlnkPyYQ27Zl5C7V3Jqxsts0WI9bvmHY5nSXYNPvX1zMFLEl4HpOjYVyNmfFn4_HFXxgDX8vL2bvCO2_mTiirRq2fwAA2qpIEyPUQCGY4jD1VVSlztwwakILCNNc1CnP8jBrO-XoHkISbPiVIg_coqHtai8ScUwUFmFKROgSdSzEcJtT0YnECt691PAzLnplhQg2LcCnzoPW_HqcwefCR39cp2o6JNSeBwbWTk5i7A8HZt0CjedNUl2PfQOZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=dYEyCYCbuXvLwwAFSZwGZ6NoFpvwrqgEv7izcgEIpl_Xa2JQqYL95g0nawcEWLRbbmWkZuTK-mdLv1X0zJmMRNBPmlnkPyYQ27Zl5C7V3Jqxsts0WI9bvmHY5nSXYNPvX1zMFLEl4HpOjYVyNmfFn4_HFXxgDX8vL2bvCO2_mTiirRq2fwAA2qpIEyPUQCGY4jD1VVSlztwwakILCNNc1CnP8jBrO-XoHkISbPiVIg_coqHtai8ScUwUFmFKROgSdSzEcJtT0YnECt691PAzLnplhQg2LcCnzoPW_HqcwefCR39cp2o6JNSeBwbWTk5i7A8HZt0CjedNUl2PfQOZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyu0IOvDpQ0o7yW7vncN1gKgiRfuFvG5TGHum-6aKNQgzYEaZaCZwiV83pI9RmscKh77606mNcg-tyj3G3uFsAzrn67yU20AJoJFer0umKh59PTFLHVrdJjnAEE0wmtc_EGdYqvbzmNb6nw3C7rjxIj-G-OKQH5bd9L6zceR_dCkP_VbRxRnzFffASUc-6P62B59X8hIeFMX4T8W-SDC-x_maGoj59gKaQOKRn_z9MIgiYLDwbRIAw1e_V7HYYU_1JpnfIn89lkhx2dD_RlP2SPynZzCGvdrB3rh-rr5cERf_Axk8Q7Olw1IsAuOCPLgDtTEFj2WlXKcOD3hR-IJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5aDZ1MsOTviW7gAuefZ6h9K8et1rhU2tt1J1UMUHISikcCWcCg3AWpMi5qsvXmXELRPujNhzAva2LtBLixvLP1LgXhuQhsQd6z1P-QUjBYek9VB9DiB1WUSnDt5R9-VCxARqqCdOF-8MV8Xb7h1_t04F2_jqqd7V6_XuLoO_AA2sWPHOqCkXSBuQ5CL5fUgjne43rfho1pIrGYiO8nujxtafmP7FGiVxtyI5TQ_j3PyaP8wzjyQcRQ2jyRBQ6nkfgxzi-ZzVl61rlelTbtgWLGe6Z07_kwFJ73TFDJNgFnto5TGpW1MVV6oT6fNq8ERwK9-x4k1yXUD_urrfzwAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edVVOgFnIv0PqKzK98GtWevAMzGeb5W8PsrDsSW2YrsBhGmcTvj1z_a5GqCSTQ3u99enJphNgE1XkzpKFu2I-Iy5JE0DT_GtHEkM9qw51uaGDAce5YDr9tlQJK9PHQqHXATz5sgphbxq9qOyujvjNGmksHPFUv8_f8UhA4Sb5yfNaScYszXjnPv8tZUV9syH20iXS8u327gSBICBCVhTSgg3md9OMT-U3q-31mNNLeMXecIYq-WE1njP_rMzgMtZl0IQvHnLDZVFa3vZAl8NiyXc2XGFTe48Dk308zGaY0rVflq67zBjK5ekghPXOX9TBdm25IpqdnWdGl3m0G2z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=aStEhpi0nEZUvKyYhPejUD2_Z5QnXg7VZVtcjILnV8fVCIfCPCKoFwUp0470OjRavJm3P_4YjTWdcI4qab_C1WNDS2yjS_BweVW_SWauoQDUpsaVAOylgGllryjRAzVxqCaiz82xeNw_WFcgjH6Zyy8clqZg9Ngr8R7kT_XvwfLB7KH7yMrnqG41GyfKyCPcgEGK3UpvZRZrfAhbC9FaH-iHWQHFtQJAFaXQ1QFo_i5ygtx336Z5UE6QU3pk0p_zPVSCqWxJwGV8EUwSMwm4rqZlMrN131nawYOJKCl_mA82eziy3NDtVdEbPQfq15UYc0Htt93reoNmVbl-KtuqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=aStEhpi0nEZUvKyYhPejUD2_Z5QnXg7VZVtcjILnV8fVCIfCPCKoFwUp0470OjRavJm3P_4YjTWdcI4qab_C1WNDS2yjS_BweVW_SWauoQDUpsaVAOylgGllryjRAzVxqCaiz82xeNw_WFcgjH6Zyy8clqZg9Ngr8R7kT_XvwfLB7KH7yMrnqG41GyfKyCPcgEGK3UpvZRZrfAhbC9FaH-iHWQHFtQJAFaXQ1QFo_i5ygtx336Z5UE6QU3pk0p_zPVSCqWxJwGV8EUwSMwm4rqZlMrN131nawYOJKCl_mA82eziy3NDtVdEbPQfq15UYc0Htt93reoNmVbl-KtuqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در  دو واقعه جداگانه دست‌کم ۲۰ نفر کشته شدند:
یک دستگاه اتوبوس مسافربری بامداد شنبه ۴ مهرماه در آزادراه همدان ـ ساوه واژگون شد و بر اساس گزارش مقام‌های امدادی، ۱۱ نفر از سرنشینان جان باختند و ۲۴ نفر دیگر مصدوم شدند.
@
VahidOOnLine
برخورد یک اتوبوس مسافربری با تریلی حامل میلگرد در محور بیرجند ـ قاین در استان خراسان جنوبی ۹ کشته و پنج مصدوم بر جا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2V61W2W-uduAIFZdoa5KaA9N0ftneAxXPZ2wOcx47_MjayusDHWOnsJRbTtrn_JzbFBZKFgHbJxtmtaa8J6KAbajRCQSCjINwD6d2_oyguUdRhzUdACPpWAGzQzI2NfzHns2RfB3ZAMhttn6iwweLRzG345MV8rh9R3mrfZ57D7Y-mXFKHjFdZxbV4ZfnZXoSTNGRxz7XMCEi822DK7LW_ISrLmzxrJBYk_vIrGw5BGvrNbEGWSHEjt5q2fdAu6B1fUt8Y0fk7MB-Q3CahruM5mlhELN3hUcEIMJt8UR73-k-Y0sjzlmaDnOKMJvLlrA0CGGOmeAfHG2yK1lropBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه تجدیدنظر استان قم حکم ۷۴ ضربه شلاق پرستو احمدی و هشت نفر دیگر از نوازندگان و عوامل «کنسرت کاروانسرا» را بدون تغییر تأیید کرد.
ابوذر زمان، وکیل دادگستری، روز جمعه در شبکه اجتماعی ایکس نوشت بر اساس رأی شعبه ۱۶ دادگاه تجدیدنظر قم، پرستو احمدی، چهار نوازنده و چهار نفر دیگر علاوه بر ۷۴ ضربه شلاق به دو سال ممنوعیت از فعالیت در امور سمعی و بصری و ممنوعیت از خروج از کشور محکوم شده‌اند.
دادگاه کیفری استان قم پیشتر این ۹ نفر را به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» محکوم کرده بود.
پرستو احمدی در آذر ۱۴۰۳ ویدیوی «کنسرت کاروانسرا» را که بدون حجاب اجباری و با همراهی احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا اجرا شده بود، در یوتیوب منتشر کرد.
قوه قضائیه پس از انتشار این اجرا علیه عوامل آن اعلام جرم کرد و احمدی و دو نوازنده همراه او نیز برای مدتی بازداشت شدند.
در رأی بدوی، دادگاه پوشش پرستو احمدی و همچنین تولید، تصویربرداری و انتشار عمومی این اجرا در فضای مجازی را از مبانی صدور حکم عنوان کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwDlrL3OMhEhf7QVdwt8rZ1AJfR_1lDiKAUSKtg6vKpjqTHBMy44cdy2UKbgfqtw2t9TY8lnmSxS7D8Wbh4XaqJDL-SY8FhKS37aXcRZrd7gOm9z4fE12BQm6DY7M7QDLfJpHitSWLMEeoc2HdKHwesBQO5K8o9YmpghG__zSYIz5f7B_ywc0UUtSVp20rEQqK8S2WX1PFQ9p5zEGX1JB8LurfT32gExkcyu-3QNcUWHusuH-QnlWSC9RaCv9sb41P_HGo5SNJplawkhq-yvu8QnpyAvpN5BoETnRL2eR3693aBnROiodhvVn3SxMwNlxm9TZqZnvuYF6bw7vUtYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDyE-YX7S2GaO--5Yf2AHNtT1l59LaxbpTU8pr7hubvDOlZQbUsegol7AIt9Lqb31gAQPodZv8Da8TGspES7DAZ7WDI56qqHNBN9wfXA1asVNELPz8HiK28x19SOYlp7nH-IHbgf-yQSCWET-al9D8FEvGG8y_kfqkdC2bAN6Ve9DwrUORviYSttElW9EXQm4ABGgEjVTOhZnB5o3W3ZFmnq5i92cQBd0pJ4ehyIx1m3IpeIk3U--FI5ymq2bluiHncHiM1ZrlgHJRX1i94oH-5FIr9OJhr-ggyQnOa-bxtPt4FtsY-mgZKOa-svH415UVgvDG5RdThi_cSbrqpQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrXpW1u0s8RTPZuUbWSJLNsuW8282cKLGg-UKf3L1QERPFISjZBSd2tDS0xlfSDYjqzn08u5KHmUHKpsYnbe9uEQU2HwawDaZy1RL_b72Avr3hVXo5KcTwQ0G_ZyidzIK4jz3SApxdD1Sd9L6hk0eGcIvkjXa7HM-QhmkMehi6epQ2b_Z8LSA7oKgFA5paF8dS3DVxhhhmpdP7rQKIK9MXFSMn_kcK0WrtzEDOSdsV3mBWR_45KxlF94SiSmX3pg8nuUahQ4Uhi7yPQA1Pa8TqNpZikkP-5fy3HSHtdJHLiI3SMmUbRj61huWf-ntCkv_nbqcHJT32Ow-vK_7IXPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vdg4jWRF3mEV14C-PhPnepcsZxxvVEK4LutlVFXWiUvym7tMV7txQ2p3qacEMQ7qCcS0Ek38flH88PRWzY5RwEXu5jtqaBXnuRxMFsq54Dk4C_k39y_643c-DeN0GKEd5qquRk9j695aObkqTff3ESqwRNu6862WzxuGO45d_ICwI7yW4tjb7iJWHhPRUZ8B13wfLlaEpQW9O65osMTY8eDK2_DCAo5aI3Frzi_Fp1-dVoefkdIgY0DX28UqC_hLfhVn9w8fgugM4iBAJr-8tGBOyYiDOYYGtr1edJ-yEhODxgA5mdyJBmeyVr34IEKNyp3CDD1TQqRONB3xoC9mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMB6uUwFSv7FXnYiBxldLyauDwdSuXXUuuM4yX3VtFSO08_oQnNdY7nlB25BviLNIrh5jpWrfv-utqnQnVwsGD4eaiutzvjT5dbJnMVFnbcq1Yai_O2B_LhuCQbs0nDq6sbQaTqzjnI_EszIeTnBcsBJt1TywVml2y_vXxebVcwl7DcucerTkVpS86HdvHrQtohSepp-lzXgfNO3jT5t8XiC4-Y-al-mBxi8jK-abPmqDrea4hG2LXT4o-A4FISHZp9vSDMwqmhQLoTo_PtqRfU0_eHXWDsZ8D02gFxkrA6abA82tNGfwGaMDRPHYirXfXLtRmrGX3zY9BwWpUAbeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE9FAMJl6fv1KgMnvKRHOCEIUXhMy8o4wVNfWC_e3r47MpWzRgfsltH9TYAtaJYrSuNXqpp-yebkvyCOjta9CVlwcKoQS0q_e2SbLSYvojkTkOqsyaBWA8EznA5m-bwqPId-PMUi8qtBOnMwn_HLNW2Ny8NxM8UCL7gvd0zxZLirVeL9v5w1bWk5S7z869uedB97eerVWoXV3oEbPCdDbFWy8xxaGGKgzny-85HcVHyY_AV8n8KxoMowyoX6U_P-9ANQOKgoFsVz2dSUhWxMU6pGTRWr91rJZ5Gev0uLwQ_f9vl7jsH-RxpDjcpQ93IZj70snt-WJYynkKTqNKedDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzBqfLM961BTCWTdML3QNrW_A0mf3RWoSSiRr8stE3GKn5kj6J2QWq3gM5BvKJr3GS8WQypxmEntjz_bqDYVKv5Vu3T5xZsd8e1lrJn51UnKoZ3bGkBPGTnoP09oS4Q0I1i7x6M4rVIYAIzNsxXKvC_fcAAOqPhfOJLnXAZ_C5XepoC66A-jNF0ypWOkimqD81zaIY-hQfukQaWyL2W3DqYNyXO2hTGXZA7lv5gOOkTb9rkhhFHs1i8GcW5wWzbl6dR2wH7pUSNQ3VaYGYYBj8SQo8mO8e0pGOOOD1r1Ien-asp8g6caEzhE7tJb2KTbiJ5120KMH-0c13sYIx_GCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEtCEYq5TGsBEgzi6CgU_JeS2vuOr24Q5oCFbzYPLhhH59j_WbqU7MlOB-jR6nj1wnerUNNXOcZEtpHzuD08-_2Ynv3cpxjtCvwX_lS6S6RjSDnqcmI46dD7Xqlk-lNQ0ml97fCNM8dMz56iQafGmasfUeGfIh109OSwmibiPNNbdy6AUcqaw3RiuSqURYsDzUzCdUlS6P6DaUPm1DJrgTZuISDyXwYHktaaqyyXrcEpTM5pF4FiNG-uAXWK4kcZRcgxwPNc4xf_5e8XfxI7Dm1lBuw2dRKzR75YTT5vAeC7Vmo0-PEGjoX1XrXzULYGj_zMvJ_57kxAtxLqbu3a1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK6_DdmD3VYuUxJiNOaNbgBmSFbDH8uEEHUEn0gNqqhu35kLfRaza56fAReIquz8eYxKAy7KaXOgHM4YdCqbb_dMjg9yjkd4TyxswUVJVfmwNdU6S4JQz5xggNtc2SR0LTCgm7EOe8v-ZKG-MMudq--yieVmKe_MAqNKDQDE12EIGJ0XWkR38vqE4H_47qD6HcKsLbtd7SO8172Q2YsCDQSqJ9sZCuHFmrqEyDI5Dk8WU-93MAZTY9LbS9b-9_tH71edoEhpYTZ66bK4u1sGdyhKGksinJbKUqBVyJ8Ra-b-7tpEefG8_anfGECWgHIyfzT9aZNrTHqpSA6EZvc1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=dI1tEXQKljUYK-wIA-De_iuMR6cnIV-216q3N4yXr9u63fF4sXhViVsJn_13rT-Jo_62B5XyzYQI18xpUWAmKP-ROQnvBJI2hHHxXs2jFVv06mORrXiVaAAuKIiMbwKdgma69lfoAX5rRExBPFBG2yrrSXaJqkDh8-ZAhnNkAg11odgF6oMVxZCLbEKWQclwXkn33akJusOaGe-2oqmLgxKVI2h5SxHhLvLTHSEt6fY-fXEI3yxc1Ra9IBOU-Uvu3lwiBCyNvTPp2v8pdObEKWfp_9nQ0wGWAhcXegvCki6R-uzI86D75ovG9ITi8OR4YczJ28mcHqd6J4hOi6L3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=dI1tEXQKljUYK-wIA-De_iuMR6cnIV-216q3N4yXr9u63fF4sXhViVsJn_13rT-Jo_62B5XyzYQI18xpUWAmKP-ROQnvBJI2hHHxXs2jFVv06mORrXiVaAAuKIiMbwKdgma69lfoAX5rRExBPFBG2yrrSXaJqkDh8-ZAhnNkAg11odgF6oMVxZCLbEKWQclwXkn33akJusOaGe-2oqmLgxKVI2h5SxHhLvLTHSEt6fY-fXEI3yxc1Ra9IBOU-Uvu3lwiBCyNvTPp2v8pdObEKWfp_9nQ0wGWAhcXegvCki6R-uzI86D75ovG9ITi8OR4YczJ28mcHqd6J4hOi6L3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYiJ2-AiFsJOCLER-zw7SqihMbZ3uam6uHvXKaxb8gtO6CL_EFuo3th_VhGNvNSO1vSyLnXZia6Yt0B9hvjHKjhG4RDJLUvpfyB6Bee-jOY3rCqY9PjPWeRSGFgKurKum7YE4nKGAOcFuNsK1zOVd3Nt9LC0gYLvIy5VT1chBaoFaYvxPxkjQUY_QgnkJF8nCVSgYEF6if4LyvV9IXBmspPxiZBw3fGAAYHqDmO2Anq4azYIa_xjQLkPTcThvlnveudd6LWmYTCzMMI_-L_yj_tkfRSTrH0EhEzkbij8sC2MXQWuNkZgTB-WrbUB8VXZ1KjNSAP6ui2kWw3xBK0KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Jvw0ioK-CHyWWkSpE8pC-e4blgPl-o99qTWbaEkGknJvs1vLOuHLe5pd5aZPkd-HSOhgeRD1MlaD9M5pCZXMkETgzXTfvC1ZCR0abSy-1HLzg79n-mMvqdY39p55yh9wt6-9mEU5yJyXc4PeYMaJLaZ7BKJndFfWHXCWQODdx8Tcz0CMFNynNlcAbyrQHi8Y01NESjjjBlEsb65Ux_n_cnRGheHI117O2faETYY6dbLa0E7QAavT2mY41v4vLZTygWKxhX_bgSxJ2DhtZmR7BO_W4vU_Fl6VtioBUSEk2MRd9-v433FaeOaPi89EIuq4bBqT2xwFCxYyH9RVgWAsKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Jvw0ioK-CHyWWkSpE8pC-e4blgPl-o99qTWbaEkGknJvs1vLOuHLe5pd5aZPkd-HSOhgeRD1MlaD9M5pCZXMkETgzXTfvC1ZCR0abSy-1HLzg79n-mMvqdY39p55yh9wt6-9mEU5yJyXc4PeYMaJLaZ7BKJndFfWHXCWQODdx8Tcz0CMFNynNlcAbyrQHi8Y01NESjjjBlEsb65Ux_n_cnRGheHI117O2faETYY6dbLa0E7QAavT2mY41v4vLZTygWKxhX_bgSxJ2DhtZmR7BO_W4vU_Fl6VtioBUSEk2MRd9-v433FaeOaPi89EIuq4bBqT2xwFCxYyH9RVgWAsKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبران دو اقتصاد بزرگ جهان روز پنج‌شنبه، دوم مهر، در کاخ سفید دیدار و دربارهٔ موضوعاتی از تجارت و تعرفه‌ها گرفته تا تایوان، هوش مصنوعی و جنگ ایران گفت‌وگو کردند.
در این دیدار که در کاخ سفید برگزار شد، شی جین‌پینگ از ایران و آمریکا خواست که در اسرع وقت مشکلاتشان را با گفت‌وگو حل‌وفصل کنند. رئیس‌جمهور چین همزمان از میزبان آمریکایی‌اش خواست که به‌سرعت و از طریق مذاکره، جنگ با ایران را پایان دهد.
رویترز به‌نقل از منابع آگاه گزارش کرده بود که چین در گفت‌وگوهای پیش از سفر شی جین‌پینگ، در مقابل امتیاز احتمالی آمریکا در زمینهٔ فروش تسلیحات به تایوان، پیشنهاد همکاری در اعمال فشار بر ایران را مطرح کرده است. این پیشنهاد به‌طور رسمی از سوی پکن تأیید نشده است.
تایوان از دیگر موضوعات حساس دیدار روز پنج‌شنبه بود. چین این جزیرهٔ دارای حکومت دموکراتیک را بخشی از قلمرو خود می‌داند و بارها با فروش تسلیحات آمریکا به تایوان مخالفت کرده است.
به گزارش خبرگزاری رسمی چین، شین‌هوا، آقای شی در کاخ سفید از دونالد ترامپ خواست که در قبال موضوع «استقلال» تایوان، با «دوراندیشی و احتیاط» رفتار کند.
این دومین دیدار ترامپ و شی در سال جاری میلادی و نخستین سفر رئیس‌جمهور چین به واشینگتن در بیش از یک دهه است.
شی جین‌پینگ عصر چهارشنبه به‌وقت محلی وارد آمریکا شد و دونالد ترامپ در پای هواپیمای او در پایگاه اندروز از وی استقبال کرد.
این نخستین بار در ۱۱ سال گذشته است که یک رئیس‌جمهور آمریکا برای استقبال از یک رهبر خارجی به این پایگاه می‌رود. آخرین بار باراک اوباما در سال ۲۰۱۵ در آن‌جا از پاپ فرانسیس استقبال کرده بود. موضوعی که نشانه‌ای از احترام ویژۀ دونالد ترامپ به همتای چینی‌اش به‌شمار می‌رود.
کاخ سفید همچنین برای پنجشنبه‌شب ضیافت رسمی شامی ترتیب داده که شماری از مدیران شرکت‌های بزرگ فناوری آمریکا از جمله اپل، آمازون، آلفابت، اوپن‌ای‌آی، تسلا و انویدیا به آن دعوت شده‌اند.
شی جین‌پینگ چهارشنبه‌شب در بدو ورود به آمریکا ابراز امیدواری کرد روابط پکن و واشینگتن باثبات‌تر شود و گفت دو کشور باید «شریک باشند، نه رقیب».
پیش از دیدار دو رئیس‌جمهور، مقام‌های ارشد اقتصادی دو کشور بر سر تمدید آتش‌بس تجاری به توافق رسیده‌ بودند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از گفت‌وگو با هه لی‌فنگ، معاون نخست‌وزیر چین، اعلام کرد توافقی که افزایش شدید تعرفه‌های متقابل را متوقف کرده بود، تا ۱۰ ژانویه تمدید خواهد شد. آتش‌بس تجاری فعلی قرار بود در ماه نوامبر به پایان برسد.
در جریان جنگ تجاری دو کشور، تعرفه‌های متقابل در مقطعی از ۱۰۰ درصد نیز فراتر رفته بود.
مقام‌های آمریکایی همچنین از احتمال اعلام توافق‌هایی در زمینهٔ کشاورزی و موانع غیرتعرفه‌ای خبر داده‌اند. آمریکا می‌گوید چین در اجرای تعهد خود برای خرید ۲۰۰ فروند هواپیمای بوئینگ نیز پیشرفت‌هایی داشته، هرچند هنوز سفارش تازه‌ای اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=DH8E4tiLXyB4a3SUC93Ad5E_L4009XtiJVpQz1XzKVuzqdBYAOJigBdwAIIH8sW0MnSgsVsnCM7H2PJQ_Rhv1dmornjKv8nYbVdoGkKPwfsBWV1TXq-CZTA0WkK8Ga0mZ4Ov1Tsdr9S2gPpccYcflkHgYx7I76uaSmzk4fyO2S0Mtp3cAyN9D2jjtX0RAJVSPWVS_fc8iDaYMRBv1JnVhrLaG5VIEUEoLOS7xsJbQVJv6gT2inEhl4XN_42N7r3T0xOwHWOxgg_0j8LTT2HenXMZztYr8jmRmZa05-rgUCvg2lXyTzOAPvwsaP_RANP_pBJXJ2mHRr0GaozfKqjjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=DH8E4tiLXyB4a3SUC93Ad5E_L4009XtiJVpQz1XzKVuzqdBYAOJigBdwAIIH8sW0MnSgsVsnCM7H2PJQ_Rhv1dmornjKv8nYbVdoGkKPwfsBWV1TXq-CZTA0WkK8Ga0mZ4Ov1Tsdr9S2gPpccYcflkHgYx7I76uaSmzk4fyO2S0Mtp3cAyN9D2jjtX0RAJVSPWVS_fc8iDaYMRBv1JnVhrLaG5VIEUEoLOS7xsJbQVJv6gT2inEhl4XN_42N7r3T0xOwHWOxgg_0j8LTT2HenXMZztYr8jmRmZa05-rgUCvg2lXyTzOAPvwsaP_RANP_pBJXJ2mHRr0GaozfKqjjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=bkbt-ctd8w9RV5nFr7kd5GE6fREKw1J3EH94wLF6VPj31AZorNV94iGfq9rvnFGyXO43S_8kzVueFL5bRhHnsDzW612TJw_J55IJPObWEjF9JU5tN9b2mSewfFHlWLKRIEUvmQzp8bXB9Vb_zs3IxC8YHf5Hy-NuaTHPiSkAFnRygVzVoQ7JpF3rGmo4XuHANNd4kehARRswZfjq1CglTLxWU3I-hQALBstBL-Ud4Ws7ot4H6RxUdTVq4uciducOiY5cjLLfvMn_vnUVdL6HqLSOsaqNyUwtazQ_Imnc-UFwiRcS9zsgcQQm6cTSgxLCvsfSYnqrM3n0nWjIQBRtaLV1Mt1_Z_7sJsjUQ2SBWiioC5G_jelV3nrtpW2VQmANvAOO3u7las8eYiSBH6JpIJs6rn9c2FFzOYlzaeCXcAjbzj2syo906oKHNTZKHgse8OKl9_FpCJaniO_wN_QnEiRKFtTgOp7iXkayrPqkgf20Dm2Oi6ZeBOBARcZyCwrknE8u0Glw6WbPTUhSXQpKfzGTxa2OhlqxEMkYrpsSH5l8stO005fFYvs-WabqeYnmAReUdWjXjs_Df4SUVYPQ2JDJkaIpdgfoZLdbQX4hcxTaxBfcI8GCYryeqFp7Ra3X49-f0XfXj4Zml0r5taCoObOQkrcwlT68Bwe1sxPcwPY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=bkbt-ctd8w9RV5nFr7kd5GE6fREKw1J3EH94wLF6VPj31AZorNV94iGfq9rvnFGyXO43S_8kzVueFL5bRhHnsDzW612TJw_J55IJPObWEjF9JU5tN9b2mSewfFHlWLKRIEUvmQzp8bXB9Vb_zs3IxC8YHf5Hy-NuaTHPiSkAFnRygVzVoQ7JpF3rGmo4XuHANNd4kehARRswZfjq1CglTLxWU3I-hQALBstBL-Ud4Ws7ot4H6RxUdTVq4uciducOiY5cjLLfvMn_vnUVdL6HqLSOsaqNyUwtazQ_Imnc-UFwiRcS9zsgcQQm6cTSgxLCvsfSYnqrM3n0nWjIQBRtaLV1Mt1_Z_7sJsjUQ2SBWiioC5G_jelV3nrtpW2VQmANvAOO3u7las8eYiSBH6JpIJs6rn9c2FFzOYlzaeCXcAjbzj2syo906oKHNTZKHgse8OKl9_FpCJaniO_wN_QnEiRKFtTgOp7iXkayrPqkgf20Dm2Oi6ZeBOBARcZyCwrknE8u0Glw6WbPTUhSXQpKfzGTxa2OhlqxEMkYrpsSH5l8stO005fFYvs-WabqeYnmAReUdWjXjs_Df4SUVYPQ2JDJkaIpdgfoZLdbQX4hcxTaxBfcI8GCYryeqFp7Ra3X49-f0XfXj4Zml0r5taCoObOQkrcwlT68Bwe1sxPcwPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی قلهکی، از منابع "نزدیک به حکومت"، با انتشار این ویدیو نوشته:
'''
اختصاصی: «تاجیکستان» و «جمهوری آذربایجان» آسمان خود را بر روی پروازهای «ایران» بستند
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه» _پایتخت تاجیکستان_ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🔻
پی‌نوشت: مسیر پرواز هواپیمایی وارش از سمتِ ایرانوبه مقصد «دوشنبه» _پایتخت تاجیکستان_، ورود به آسمان جمهوری آذربایجان و ترکمنستان بود که پیش‌تر آذربایجان و ترکمنستان آسمان خود را بر روی پروازهای ایرانی بستند و پرواز نتوانست وارد آسمان این دو کشور شود و بالاجبار به کشور بازگشت.
'''
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duyNm2dxMgMdfZxDl4FLRv1U9H-8E-a-2muDOiygj6QT6h1uJG-BM5GTAkSGlQXDk8qW97gHjS0djtXfX6OCiFvPc4lEaLacEVxmwtw8tMVayEU32-lSJzSWwVMpf3mNchieR-Tnqr_zkHkVc2beEgz4S6a3A8gxoCr_U_jcQtUnRC_dMVnO9270OsqT8d4cTwKMuKGDYUVp2aixR-q7uDfSn-dHFvmF2NJ0Q8LiOS0Jus086g4uMK1I-w22RSscHUpAGDSL568ChkuCKUisEwj0ZKyD7sRwJSMV95oe-Se94pgd8kPpI4WTOPi4VUXwW8mrzhTcT0VpkwSi4qL-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE11vxQHB9RGbTXYV-hdzZbgIQy80Pet_cnIxKkWewkNe2NwgXNKob7jBrZQoHdqovtkI3cM4gVe_HlGQbfopSMuwJpyc2ClADWddjoxzcMHyLFJCymHNVXqCkZ5n3WO5DleIwdpHI5q_eiKRvS6UiOWjDfW8qFuCxwuBsfWmrf3GDCgDu4k9M5hWMDPe6OlTAzR_F6KzIsMn72keOj4C5IsplUFhIv3i-i9nr9YupHADbJk8Ni4C1iq2-RD1aQtZujhEXX5xmqIujI7okV0QrY85PZQn9ukyQaznuf4RYetKn2FaKJEvF0lheJVC00aRVp9DQe4Ug9f98ZVbS62Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB2fZuIuZZHz_1P5eDOtaFx0lCbAROV75JR9D_IdlMg5ZsvptJ-te9E6Q-C1AfX6CZAjmPbW5_SzkC39QzHO0F8P52wwkK_PpKzEoosLyyRNHVoRQ9b0bcb2A-ni1SzUhfS6vS90ps-0Wx7iPjPpMr-VM2ulWpvBHhkN2GhTkJ1T6MAfiJtv8DlRQY5No068LFT824MYo6CqZ4rsHE3fu278igcZdi510jJK_baLGVZZz1Bw3ztNBk4blOvttKbqMATUfqT63iK4tVMq-CqzX_Nsje6VO71FcZnay0BGJ5Vd5EryItesccGsoBk64dMKNIGtYpuLBWdhO-6kCh7WGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkvfPz0x94dEH0l-wAS5YL2OwFYH94J4aYCIB4Ij8kIJpMX4OBD-t4HpFC6xF8F5HFGeDHc_O6FmRb9t1dZM9M4WB2ei4Qy7QWvMSXCiNqL2DapHRXNQODrE5u6fTdmYw575NN0smDoMW86f9cvJfiGGk7mq6dGBCM9gbkm8y2ujY3AjCcogKXMZLiyUqVl1kJojRrVMN55ii8-CAuh2dxIHdf5O856fdr-4MddtlSpBGva_M3jxaBg78GeB9tMyOO82EuJwEbaC-YeJyZ2xgs9FoO600GoEqCt7Dt7v5MSsj-r0UQ08qdx-trAlehEUWIwfDHXcjT07elTzvOZPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8RYNM4jBVQjYTF6XCStMAu_tDZiQu937HU68vU7uiXBSxfD6BJV2oNb80Z7ZcKvSuFZp4YJpBv81J0S1wqGi7_uPRI4mmAkwLdLJudcmoIgpzOmARuSovxrsqjEPjy0Zzt3GZqHudXqoYkNslfr48i1irIJNGlLoVEg63vFFv0mtl7GCc7z5c6J5vSwDk-hAB6IHZk4SPv_MugA4kS67R61xIdIgavfGeLCMDVXOO5j2CYE3uVdZuLHH-1eQluOepARNmPAe1G1Kxoio6lpiL3lmVTV6Cn3NXk5HJ0JeRP0_s2RjZGMHtiG9FzWiC88j_uVZ7HYv0WebKBT2KnNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D36IoNwU0T7VKOlMQxpQ6F3vKyCvPDCh8aoZy7BQ8TOqNl06gC2BnFlIr0d4nYSymYI6uRfi97lIsOkbncVE3k2MNiWVBTNTAFhoFUTeAYbpFLNmvtVuvJA9S5BohqR9SLQx7PcdHlqWjJla4sGaawAQ9p92JFLPEYA48myRjne23S-64NTO5ISdMJcpByAcL6gtkoEEc7oQZ_Ok4Ip3xIX6vYBL77OC8fsY30xRhCqlQBwj2xy2nLRIsIcrDmmJyA9gnpJEgnvXAIiWwV2uDNFJnb1SkzZDqZlr3h9h1rhnpak5eqzEo974yQehXL6LdgQlsCPUcyfTNO4rE4tJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gz8vh5_8-excTJoEsyH1qRN0Ryhd0qJxFL1uzxp5QATON3GNCASp5by08Y5x6P78GXUAM4fHnr9IDcpNyj4J5JvM3pmoIDwezjfHol40xQEoMrh027BhqXZR-vzT74VIPxXFUimRa4TvApzolGs4BEp2IpJ3KDZNUqwNER4T1zXeoVxQswA_hKCTnFkkdXu85z0vlKLonOz6YlKRx1avALIa6pyGX5l-feaS8UTTpyKk8meprgc4ZROVcpm7fLimr6MNGKqzs9_jU_L7rzSvV8IoaJ1ltP2HNK52fVna-RgiOz1Jx4_cA082t74lkTDm-bNiNSckhlYmlN8qNG9q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=sopV2nJE7XY4sxfDWxAX8jEp3vlcZvejhtET8E5jznDFmuyrembzlHgvodByz-iuEyv3OZWS3v4XF-3rl5P7bByV-Jjq3Jy7pICaKztdAQFSwBnzZRfPvA7sIDmyIq-UhiS5N3XMhqNojLm0me7Ydo-cI3UBljiZc-YxxxijYrGgY1JPKpQ8_CYj4ORBnN0EtqDa77EtNSg_WxwdykGIOYoCphIQp67lbQQtC6phkXa4D0XFEqEC2cFm9T9ZMYB4rXqh3_CI9PY__Bs8ieQdJZbwBb_CiSGdSWDb1ae7I94hvrpVyvLhS9-4fWeYlikBE9iuGSTnfQQnp_YT_wvyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=sopV2nJE7XY4sxfDWxAX8jEp3vlcZvejhtET8E5jznDFmuyrembzlHgvodByz-iuEyv3OZWS3v4XF-3rl5P7bByV-Jjq3Jy7pICaKztdAQFSwBnzZRfPvA7sIDmyIq-UhiS5N3XMhqNojLm0me7Ydo-cI3UBljiZc-YxxxijYrGgY1JPKpQ8_CYj4ORBnN0EtqDa77EtNSg_WxwdykGIOYoCphIQp67lbQQtC6phkXa4D0XFEqEC2cFm9T9ZMYB4rXqh3_CI9PY__Bs8ieQdJZbwBb_CiSGdSWDb1ae7I94hvrpVyvLhS9-4fWeYlikBE9iuGSTnfQQnp_YT_wvyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y43WjXgHsVsovGSuX-oA5fOSxwxHRewHUJtSjIPnydz484WO4AetsW_CjjdJNsgQk9Xp5dTVBLHJjHkVOjidmnUO-x0JL5vzZsS7YwlNzuOfbHzDjRlHsWp-Cq3jyCvP17jjTN8nNTk8ojnYzDBrRVJ8oarcP3x0k02REpU6cYJ_b_BeikDPVLFg7KPqautqAj5tMGRPzYlyqEuFci0dO88VBtCO1R5dF9Ud60mQ1DSr6lrbL9qu7PecobyTNg-kLVQXI7GN895FN8Rcm3lKf1mIhSnwYTKOl6A-WCnrBQRApRiVKG6PBQUo150JECSfZd2vz9eOlhDVRpRq-N7jxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=CP4nHi2KU2RcfSqS8teBsbbd5WCyJYdGWGf4EAztGLqcaEXGRLYqHoZkoW72WDzqsp8tVevDjFrm0UTAr0Q6huHqV015SgvygAlC3aYdZbtbt8522RrqA2jVvGOe4vDWbwEJ0VJc1Vt0ZEaDjMvpXiuWvCAVX91l-MbooyOJz2Wa_TCg-ULn1nIhIbmzHHwp_j-LQ5MuwIwbL0j9yhloORTVvpRSTB1_aXmu-BvxcL-rVQnoyJbH6PRSzFjBUo2x71GbN148qAVJqs3sMUeMGE2037OsskkfrQ4hPxVD8l_JE1fpbCyMjCRoMcLNP8PtDMaMU9_TUoCEuRH6hV0llg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=CP4nHi2KU2RcfSqS8teBsbbd5WCyJYdGWGf4EAztGLqcaEXGRLYqHoZkoW72WDzqsp8tVevDjFrm0UTAr0Q6huHqV015SgvygAlC3aYdZbtbt8522RrqA2jVvGOe4vDWbwEJ0VJc1Vt0ZEaDjMvpXiuWvCAVX91l-MbooyOJz2Wa_TCg-ULn1nIhIbmzHHwp_j-LQ5MuwIwbL0j9yhloORTVvpRSTB1_aXmu-BvxcL-rVQnoyJbH6PRSzFjBUo2x71GbN148qAVJqs3sMUeMGE2037OsskkfrQ4hPxVD8l_JE1fpbCyMjCRoMcLNP8PtDMaMU9_TUoCEuRH6hV0llg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=kwrw3r7y5VgRI2hOqRI6G5yid5UX7PLFdgyoLXdZbQkzK9q6yRQ_WUxJC3UU5TdzcBxjFebD-a2vSsJrLuhSYDO2GyUlzdOeysUSj8sY1juILIDqr2xjgu4eh8iJVPYwDrMxVsk4Gxtb8xRlCjE4_j3XTgKuhaLnmFkH3hpNaq-M59kMOunB8uxSougbozKfDNXMoG_Gm-40GDMXuLNcAnIvrHYGLXgB2-l252JBKdqDgNfEzBIrN9JBKlaHLZ-CkFHXOTygQhj26mpwi-Nl7oOHMTjEwSj-g-1qn0r7HfqqEy6UfQF4ofKetE3KjqNQVgm3y-n2Fu8qLcR9oKohwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=kwrw3r7y5VgRI2hOqRI6G5yid5UX7PLFdgyoLXdZbQkzK9q6yRQ_WUxJC3UU5TdzcBxjFebD-a2vSsJrLuhSYDO2GyUlzdOeysUSj8sY1juILIDqr2xjgu4eh8iJVPYwDrMxVsk4Gxtb8xRlCjE4_j3XTgKuhaLnmFkH3hpNaq-M59kMOunB8uxSougbozKfDNXMoG_Gm-40GDMXuLNcAnIvrHYGLXgB2-l252JBKdqDgNfEzBIrN9JBKlaHLZ-CkFHXOTygQhj26mpwi-Nl7oOHMTjEwSj-g-1qn0r7HfqqEy6UfQF4ofKetE3KjqNQVgm3y-n2Fu8qLcR9oKohwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_8Je6EHmkp-t1OC4uFT_A-G1pDCupHa37eWYpmBtkCU6paoKpgAo9LsAFwhSFHRpd2rMXCYAOffV2cSmer7dflp74CmOHPSfgddqlZCSQ3hh4Q1YTvrmMBRubHfpVQD8FORWWp-kZQe6IS2ktr99jH_7SL4PJm-oNLpesyEB4u5TVsWE00eKCNGXh0Ud4_3XQbIm80tor50weE63U9MiPxpHMt-CaS3iHzHIPRzBPnc8KuXu7Pp44Rhg8faf8ktsPPiwbL9lEYN9koTXvqqwjJWsGr7dGXorrkjTg3X5oywyll6ayQHmWbU7D30I0gmYz-6CHs5dhrJZ5G7H5WkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=FhhdPCiR7e8fcxaXqJsoQuIOWOiQH4JQsLLtCsOtm2F-lx9uSItDreUqEcObNQ4ngepz6yV6EU-yBQb-FFOe6LkUV2PssAsLBQswO092kFRR_oQh0VmST08mUrDMZda-Xd90EOrnpmk2MixQpwBQS27V8BUS13TV6UHnLaoXh1w2UdgEcU8DVtPbWmBaw-4g8Li1OZTLdI0BkYXIg7siGzdCIjUw2a4pKlOhaY7TWOUteKcaqS0IcacVJTdstgtREMio-8V6bdboD9clZVZcGEnDvgbCjieCpNwBKsmGYN3Yv63CMXTDiuAZ4_xDwwHdc6xUNb9gzGsKxrkkIp3Ifw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=FhhdPCiR7e8fcxaXqJsoQuIOWOiQH4JQsLLtCsOtm2F-lx9uSItDreUqEcObNQ4ngepz6yV6EU-yBQb-FFOe6LkUV2PssAsLBQswO092kFRR_oQh0VmST08mUrDMZda-Xd90EOrnpmk2MixQpwBQS27V8BUS13TV6UHnLaoXh1w2UdgEcU8DVtPbWmBaw-4g8Li1OZTLdI0BkYXIg7siGzdCIjUw2a4pKlOhaY7TWOUteKcaqS0IcacVJTdstgtREMio-8V6bdboD9clZVZcGEnDvgbCjieCpNwBKsmGYN3Yv63CMXTDiuAZ4_xDwwHdc6xUNb9gzGsKxrkkIp3Ifw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLW_qlJLt1ZR26acnoP05WaCRtD9x0m_vjxQl_x-ZGzc4zlCFY1EbDHBxFrnECsc5O2_Ur_zLMxLDt8LicLVYooFTkVzqs2j7eNAqum-vNmXa995XyZM5HRtpazPMP6M2myzt7TtARVmgZ-UX5-HP29MFXp7-hAEaGB_gcUoxv3YYGTjvKCpDw6hpIBGxwFMa-Li9T-X5K_b2g-saeRWnwxVwtoDRcoy09N-amI5HEuza-WoTHVyRab-Zben9bcRiqlN_q4dtyGVSDzVijETSFrXlw_tNkRz7qYOtDHj_nKx7tkcjhMVWZL7G-3ZEaKPodn4lQmuSvP6hVvJsa2y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=THGKZNmzBCtXF9J6WkgDr-A3shF7kGHdxytzQ7oRH6NiBwFO-8bbhdC6g3I5Ces_Lg48t_LdrruaH5IbxJCGqJy5bIsHJHFd06WZKJOVCwk4M9CzPalfqQxgXypp6hlh5c8tyoqK9zFZ4JXxjGEyCJyTUACCC7c9yzyirLJRDKR4lWP-owrh5NGNK_arHJkDyUXr4pK6IISqTJIOEtIqmPpRLIJXmqMGHwel7kE8rNh3bF6w2Jph3dM4-PdtXs_N-GEuk7VB0tmxlQlFCUSI9O4GSEPDybDWF0yZhiiCFxgebznYYwsHDhvzirRq6GQrBSBffVyeEmdIyHnwVdpJNDVhMpX0ziKWDYmd5P-s5Zw3opUrlkSP4kZo5aGKPlFGc8jiQ0yUtYYGfqyLQYj_JhL86T57TFSbgU6u5DcKJMFZ6usLeMisjjppvZQDrpMQTWk5NqnKlatyL4wdZiFBMlHlljk991clgp2nGBElT5UKwphxRiqknz3VhkQNeYhp4KwBM-b8dDwaeQPNgnpLl5gfmRnfjA3Ppa8kjPUSWfKDC7Z9IxoE7jzqRCa6pZxDTuuZVk6r9mRTzNj4ckxQYOZ5PQXfEItp7LT8MxRPoajzG-iVy5Xr3d2DVPieYd99SoXHLkKfIVSD2zLqOsAnfFhCtlyh3-ofcCTTtMJjrh8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=THGKZNmzBCtXF9J6WkgDr-A3shF7kGHdxytzQ7oRH6NiBwFO-8bbhdC6g3I5Ces_Lg48t_LdrruaH5IbxJCGqJy5bIsHJHFd06WZKJOVCwk4M9CzPalfqQxgXypp6hlh5c8tyoqK9zFZ4JXxjGEyCJyTUACCC7c9yzyirLJRDKR4lWP-owrh5NGNK_arHJkDyUXr4pK6IISqTJIOEtIqmPpRLIJXmqMGHwel7kE8rNh3bF6w2Jph3dM4-PdtXs_N-GEuk7VB0tmxlQlFCUSI9O4GSEPDybDWF0yZhiiCFxgebznYYwsHDhvzirRq6GQrBSBffVyeEmdIyHnwVdpJNDVhMpX0ziKWDYmd5P-s5Zw3opUrlkSP4kZo5aGKPlFGc8jiQ0yUtYYGfqyLQYj_JhL86T57TFSbgU6u5DcKJMFZ6usLeMisjjppvZQDrpMQTWk5NqnKlatyL4wdZiFBMlHlljk991clgp2nGBElT5UKwphxRiqknz3VhkQNeYhp4KwBM-b8dDwaeQPNgnpLl5gfmRnfjA3Ppa8kjPUSWfKDC7Z9IxoE7jzqRCa6pZxDTuuZVk6r9mRTzNj4ckxQYOZ5PQXfEItp7LT8MxRPoajzG-iVy5Xr3d2DVPieYd99SoXHLkKfIVSD2zLqOsAnfFhCtlyh3-ofcCTTtMJjrh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REVFBawnLZx66HTvrO8sHZbxmCDDO_MlEeW3T_jKnN5icy7Ia9B1ytKDUzROMVXL67oxy2KxDDZgrBhYcIho8TucMgS33MmXpKo_wPSaOE-GbXGx7KRoB-NINAOf9RPqVzLTN7edOFbE6XoHgSJ2zM_tyFisx8h8yMspy1yP8jMF5noRDjD0suhgHuQ7MaNZ1xleuZa_jo-6DwT0-3YJiEQ8S1PL8vBh4kSK9p20YZv-unF-SzUzDnYy_VnEdigIM2JidpQ6UkavYm2uzMxPrH_iEgqY93VX2Kx0-rKydRWnZfNRAnouQDxN6BcjgrwiE1ZjgslAjnWXXk1ncgqH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=RyqdggDiHFXc5J0ZqA_mByYu77V7b7faXJUeHOqFrzrbdK0uTIPt9A5CG6Lu2T3zo69IXkgqQiV5zrxHbXQzZegnVaiMgVkDVRC4no4D0xv7biJCWMBO2f_T7XJn1z3HtFO97SiWRouO44qD4hfjra00Z5FMakLIMHRtMfD8p1uhd6r8-x0Yt0lWvs9ceP1YkJj2Lty138X1twLBkGJAlEqvRXakPPJGSjlWHRG0lJEksZboFVaEZ4BdcMASFhaCjQFvF7HqG-HjytGs3Wa_S3TsGnyzqdhf2ksNf49r-Z6BWs18xZhZulXkmUDbrPhpYtuqwrbSzSS-Y4-U1f2kzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=RyqdggDiHFXc5J0ZqA_mByYu77V7b7faXJUeHOqFrzrbdK0uTIPt9A5CG6Lu2T3zo69IXkgqQiV5zrxHbXQzZegnVaiMgVkDVRC4no4D0xv7biJCWMBO2f_T7XJn1z3HtFO97SiWRouO44qD4hfjra00Z5FMakLIMHRtMfD8p1uhd6r8-x0Yt0lWvs9ceP1YkJj2Lty138X1twLBkGJAlEqvRXakPPJGSjlWHRG0lJEksZboFVaEZ4BdcMASFhaCjQFvF7HqG-HjytGs3Wa_S3TsGnyzqdhf2ksNf49r-Z6BWs18xZhZulXkmUDbrPhpYtuqwrbSzSS-Y4-U1f2kzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78494">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afEnC2q5ff_kSEBny58mb5Cc_ufGS3Ylja9Ft3UjHXvJSg4xiWjZRE7h5nn0AyhYBo5UYXR8AfVVXHKXyA8IggMWlBG2L_t_VoN_Hr2pDunD1iPbpiQRzZpNikUutFI1O_uuKk3W_9dLWweZ0a_RlkPKkv7UpHvzdbYYbIMbAd41y9Jdsfe-NdxHr6F1JsR24-IEl_9UcAUJy0UjUcth3ibegEbIJG-57LSegIydjGcBzlXE6gvpf6sUo1lnfaI5vgvtog4LmxqEUoxVrqTKHffg2tYlKKxAkES7vGrcQOLgEishZ89v4wwBIkh3ugrZ672G4tEP3Vl15BYJq6vsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه ۳۱ شهریور اعلام کرد استیو ویتکاف، فرستاده ویژه آمریکا، و جرد کوشنر، داماد او، ساعاتی پیش در حاشیه نشست مجمع عمومی سازمان ملل به مدت سه ساعت با اعضای هیات جمهوری اسلامی دیدار کرده‌اند.
ترامپ که در دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با خبرنگاران صحبت می‌کرد، گفت این دیدار «خیلی خوب پیش رفت» و افزود نشست دیگری میان دو طرف در «آینده بسیار نزدیک» برگزار خواهد شد.
ترامپ درباره احتمال توافق با جمهوری اسلامی گفت: «نمی‌توانم تصور کنم چرا آنها نخواهند توافق کنند. انتخاب آنها یا رسیدن به عظمت بالقوه است یا نابودی.»
استیو ویتکاف نیز در پاسخ به پرسشی درباره ارزیابی خود از این دیدار، ابتدا از اظهارنظر خودداری کرد اما سپس گفت: «در حال حاضر احساس خیلی خوبی دارم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78494" target="_blank">📅 22:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WsplGp8ez2YsvGv-4ePINlTk7H7UvVozUZx4rPqLygSB1QGQS7uoOq3LPjrkrqLQt3weqKhhvIKb3sK9O-TOxnFV49Z-yDIi8bhQSgFfVjCKEiF-dQHND7YJJ63RlqTOvruLEdh-TRJhK97fFq9Y1E_-qiYRT2hZKqIYuflv5-yk6myOY7rB1HbIyGM1eyLFGDNhCgjHz_Ns1wBtjvFTiP1Ai5i-leMyLL-0QqbJKhH_VOJqsOxkCAafHPhLROYAp0CFGMg1TgTX2F1qkZCiel1uX8o5MPAvu5R1BFdLFP3Bgy0HtluRtdiT4LFsYYbFrCdlcUbFM8Q39eD7GKs1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از بیش از هفت ماه غیبت کامل از انظار عمومی و در حالی‌که هنوز هیچ صدا و تصویری از مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی منتشر نشده، روز سه‌شنبه ۳۱ شهریور، دست‌نوشته‌ای منتسب به او در رسانه‌های جمهوری اسلامی منتشر شد.
بر اساس تاریخی که زیر امضای این نوشته وجود دارد، متن مورد نظر در دهم مردادماه، یعنی بیش از ۵۰ روز پیش نوشته شده است.
در این متن که خطاب به مجید موسوی، فرمانده هوافضای سپاه پاسداران نوشته شده، نویسنده از او بابت گزارشی که محتوای آن مشخص نیست، قدردانی کرده و خواسته است که تلاش‌ها در زمینه زنجیره تامین ادامه یافته و گزارش آن مرتبا به او ارائه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78493" target="_blank">📅 20:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEhww3sPUDAtT7U9tJfjXY7ElZwhY_gUa_q5twp8keCUDGZk-ulBVk5YH4x3kcaM7f86Qfa3Exylax73w1k7P_qjJgwBeODCTgYfcw1lCPpxkFg47QxphGNxqRxrsuDNfN9_Vt-kdl50aP8iyli0iTkYvr9RFWGfAhh-2CO5HmKjLN56jtqo6qHb4GryrPyQiWvM7bo82VSf3dzIhv06pMSJKVieJGuyyCdMw8CfF942wA5fzwE0iV7zeMkFhgPTyDV-QFzIFQKxpESxjgI0i_027J8HXBxseizJYwG9maNtkGbpiCmoO9CdmGBeYU6KSZ7gJlch55SZxF4WJlE1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در دیدار با اندی برنهام، نخست‌وزیر بریتانیا، در سازمان ملل در نیویورک گفت تهران و واشینگتن روز سه‌شنبه نیز در حال گفت‌وگو بوده‌اند و افزود: «فکر می‌کنم توافقی حاصل خواهد شد.»
ترامپ گفت: «ما مانع دستیابی آنها به سلاح هسته‌ای شدیم. واقعا جلوی آنها را گرفتیم. آنها سلاح هسته‌ای نخواهند داشت و خواهیم دید چه اتفاقی می‌افتد.»
برنهام نیز گفت در نخستین دیدار خود با ترامپ «ارتباط خوبی» با او برقرار کرده و دو طرف درباره خاورمیانه، جزایر فالکلند و مسائل تجاری گفت‌وگو کرده‌اند.
او خطاب به ترامپ گفت بریتانیا آماده است نقش خود را در خاورمیانه ایفا کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78492" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yj9eE6k8Ld5at6Wqa-rnjEhH9s9H1M6ml_D5w2mCx5iERqqRGscS22OaMhIq08UzoJH9hEjco2oyI-Hw0gPZo1cPCGWXkAJEJQpaBdSol89ksQU00O-gQdXFtu2nrsGZ3EvtWk_DKAvTGXw_0AU17E8sPb4bkW54ju_cyLA8nVS7ZWkjcSWBC9aOCWJaUZN65Y3u5YJcUwT5k89Zn6hdJef-e00VBC_UfurU8EX1v4N3HTYJ_065_3jMz8ZOHGQgnXBTBTa1uPboQ3R6MM7Zh41IcbSTMGFxgyIkXWo9lAK2Ns3KzkjNrzzzz7d0ueoI0rNF7mtNFSQ7xooTPpY4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه ۳۱ شهریور در جریان سخنرانی در مجمع عمومی سازمان ملل متحد، با اشاره به درگیری‌های جاری، وضعیت کنونی منطقه خلیج فارس را «یکی از خطرناک‌ترین مراحل» تاریخ این منطقه توصیف کرد.
وی ابراز تاسف کرد که بسته شدن یک آبراه بین‌المللی حیاتی که نزدیک به یک‌چهارم تجارت انرژی جهان از آن می‌گذرد، ممکن شده و شریان‌های اقتصاد جهانی به ابزاری برای فشار و چانه‌زنی تبدیل شده‌اند؛ موضوعی که هزینه آن را مردم سراسر جهان می‌پردازند.
امیر قطر با اشاره به اینکه این بحران قیمت مواد غذایی و دارو را افزایش داده و معیشت مردمان بی‌ارتباط با جنگ آمریکا و اسرائیل علیه جمهوری اسلامی ایران را تحت تاثیر قرار داده، تاکید کرد که دوحه همچنان بر حل دیپلماتیک این بحران پافشاری می‌کند.
وی خواستار بازگشایی تنگه هرمز به روی کشتیرانی تجاری و بازگشت به میز مذاکره شد تا از گسترش جنگ جلوگیری شده و زمینه برای رسیدن به یک راهکار پایدار جهت تضمین امنیت و ثبات کل منطقه، از جمله ایران، فراهم گردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78491" target="_blank">📅 20:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGypgdQN3K768yVNq9mEWdOaAHizASpAzhZqRVO6pnOwfVNv84cKpGLrhahh0B0ADyPeo_eKtihV8xscZditIE22YBBD4S5_qrxKMwMk6q2Oe0hyVbxXHsbPzOUF2oNxTjYgxvaVQpCt9U7H-ZGvDdnn2bD2_JxfRckTiwn2sxdzFIMel7E4vaaYXN1WCiQ6He_zxE5EJfRjWwpQfrExBhxAFevNA3f8bZAWW7zU-XlIQw5y3bTFNXwaxfYfXnbSL-Qd_TnSYEfuled19o00IMBpeT8C9PM9Ix5emUFUa67yAn05FUNcaPL92BO1lOb76w9BVR2PeLPf-M5t0piCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه خبری اکسیوس، روز سه‌شنبه ۳۱ شهریور ۱۴۰۵، گزارش داد چند کشور عربی که میان آمریکا و جمهوری اسلامی میانجی‌گری می‌کنند، در حال رایزنی با دو طرف برای برگزاری یک دیدار در سطح بالا در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک هستند.
بر اساس گزارش اکسیوس ، کشورهای عربی تلاش می‌کنند از حضور مقام‌های ارشد دو طرف در نیویورک برای شکستن بن‌بست در جنگ میان آمریکا و جمهوری اسلامی استفاده کنند.
مارکو روبیو، وزیر خارجه آمریکا، روز سه‌شنبه به شبکه ان‌بی‌سی گفت دونالد ترامپ برای دیدار با مقام‌های جمهوری اسلامی در نیویورک آمادگی دارد، زیرا به گفته او، گفت‌وگو با طرف‌های درگیر برای حل مشکلات اهمیت دارد. روبیو در عین حال گفت هنوز چنین دیداری برنامه‌ریزی نشده است.
ترامپ قرار است روز سه‌شنبه با نمایندگان ۹ کشور عربی درباره جنگ دیدار و گفت‌وگو کند. منابع منطقه‌ای گفته‌اند شماری از این کشورها از ترامپ خواهند خواست از تشدید تنش با جمهوری اسلامی جلوگیری کند و برای دستیابی به توافق تلاش کند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز صبح سه‌شنبه در نیویورک با محمد بن عبدالرحمن آل‌ثانی، نخست‌وزیر قطر، دیدار کرد. قطر یکی از میانجی‌های اصلی میان تهران و واشنگتن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78490" target="_blank">📅 20:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=eMkXElxdaXLeN1N-m8XY2wC-QaY1TZLZ-7SIA69er-Phyg489pCTkCWVCZU-ZWNlxOpy7oDa5F2PNpFo5baJIOJKxQTiG-sZQVHlTv3rTP2wedCYPeSjXUMLqH5tBVAtF_29Fck0txyGL6GKuX3_DMIFdV0r7QondoElDfF6zKwpVd0lEA1APh1N_e42g8g-bGD2byu1DwuRqX7qcXDzNYo4BsXJ9Z9OBT5PIpo3SLmLFfiBbOBP4OEfHFAyUaQ5OfIcB0RwfXvTwqr4iWo_nvhzIKXdPImeT8q7YNLvQgaOUu3Od1nlcaGM8Gc2fYxQBwmX71JnR7Tkrqz1qHI1slZe1WojztroOs8nV9s3Q_1evkAe8aU_PoaAMEzeS2G0vdLWq_w4NCJq_QS-VUrLPidR9YMtt9Rp0JLi4vk8KW9UGGRk1kmakrHe5pwIwEt07HKjjZOiAEqjODh1IkEolZjMRTTW4NtNSzcmjVyVBlElgKaqj24rV0rR2ERSHoyhTkAa2TMK2oDYgElu2HK8JfrhC7C0WzE2BMV-78BdbarzBGDhgISgJrmDLEe73RFeI21VgCV2_rhvLLMmvxBuhHbSjOj68FrBwoR9IKKT-rrBfyG17qqT_lPzq9PUP_NSvA3ni3XLZG-V4grteXiQAb-7-igt5Eu8beADEPn2oNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c36a3ad0f.mp4?token=eMkXElxdaXLeN1N-m8XY2wC-QaY1TZLZ-7SIA69er-Phyg489pCTkCWVCZU-ZWNlxOpy7oDa5F2PNpFo5baJIOJKxQTiG-sZQVHlTv3rTP2wedCYPeSjXUMLqH5tBVAtF_29Fck0txyGL6GKuX3_DMIFdV0r7QondoElDfF6zKwpVd0lEA1APh1N_e42g8g-bGD2byu1DwuRqX7qcXDzNYo4BsXJ9Z9OBT5PIpo3SLmLFfiBbOBP4OEfHFAyUaQ5OfIcB0RwfXvTwqr4iWo_nvhzIKXdPImeT8q7YNLvQgaOUu3Od1nlcaGM8Gc2fYxQBwmX71JnR7Tkrqz1qHI1slZe1WojztroOs8nV9s3Q_1evkAe8aU_PoaAMEzeS2G0vdLWq_w4NCJq_QS-VUrLPidR9YMtt9Rp0JLi4vk8KW9UGGRk1kmakrHe5pwIwEt07HKjjZOiAEqjODh1IkEolZjMRTTW4NtNSzcmjVyVBlElgKaqj24rV0rR2ERSHoyhTkAa2TMK2oDYgElu2HK8JfrhC7C0WzE2BMV-78BdbarzBGDhgISgJrmDLEe73RFeI21VgCV2_rhvLLMmvxBuhHbSjOj68FrBwoR9IKKT-rrBfyG17qqT_lPzq9PUP_NSvA3ni3XLZG-V4grteXiQAb-7-igt5Eu8beADEPn2oNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ در سازمان ملل
با تشخیص و ترجمه ماشین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78489" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c08589429.mp4?token=u13-JmNiQdCjPr-4kGbJkLTj_EYtnLASjL8BoiQBXhC0UCgacPVLpNOOA8Uy8lax_A0RHPw5kd6OM7-je0O9GVsk-cfo2Mp-nS-n5_Nxd6cGF_c1Dh0p6CjHugMoaeI8UWHUIntz31xoJl0gc9Cb66GmHHbROVa5oHlLWG0V4gotfPtGLxtWY9rZ0i6YmTZMhFVs7tTqG1Y-eiA6KZw1n8LyI2BsCPRLkBOU9K-Aow-YiUn0wCVBbca8c94cgnYvrxsLfZFhqy72ShNeluoHKveTXOeKq9cYiJ4HKsBZwSIXoUYtyDf3BCVmg_VIC1aJwbLAb-p88itP2_VAs7faog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c08589429.mp4?token=u13-JmNiQdCjPr-4kGbJkLTj_EYtnLASjL8BoiQBXhC0UCgacPVLpNOOA8Uy8lax_A0RHPw5kd6OM7-je0O9GVsk-cfo2Mp-nS-n5_Nxd6cGF_c1Dh0p6CjHugMoaeI8UWHUIntz31xoJl0gc9Cb66GmHHbROVa5oHlLWG0V4gotfPtGLxtWY9rZ0i6YmTZMhFVs7tTqG1Y-eiA6KZw1n8LyI2BsCPRLkBOU9K-Aow-YiUn0wCVBbca8c94cgnYvrxsLfZFhqy72ShNeluoHKveTXOeKq9cYiJ4HKsBZwSIXoUYtyDf3BCVmg_VIC1aJwbLAb-p88itP2_VAs7faog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"جمعیت ایرانیان برای رد شدن از مرز زمینی رازی."
شهرستان خوی- مرز زمینی بین ایران - ترکیه. میرن اونجا شهر "وان" فرودگاه
.
Sam1Kia
پیام دریافتی: ابی در وان ترکیه کنسرت داره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/78488" target="_blank">📅 18:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
ترامپ: ایران در پی ساخت موشکی بود که می‌توانست اروپا را هدف قرار دهد
▪️
رئیس‌جمهور آمریکا در سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران به ساخت ذخایر گسترده موشکی و پهپادی ادامه داده و مدعی شد تهران موشکی ساخته بود که توان هدف قرار دادن اروپا را داشت. او گفت هدف ایران این بود که در پوشش چنین توان موشکی‌ای، به سوی ساخت سلاح هسته‌ای حرکت کند.
▪️
ترامپ همچنین با اشاره به حمله هفتم اکتبر گفت عاملان این حمله از سوی ایران تامین مالی شده بودند و افزود حکومت ایران «چنین خشونتی را جشن گرفت». او سپس حکومت ایران را به کشتار گسترده شهروندان خود متهم کرد و گفت چنین حکومتی نباید امکان فعالیت «در پشت سپر هسته‌ای» را پیدا کند.
@
VahidOnLive
🔻
ترامپ: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند
▪️
︎ دونالد ترامپ در سخنرانی خود در مجمع عمومی سازمان ملل، جمهوری اسلامی ایران را «بزرگ‌ترین حامی تروریسم» خواند و گفت که حکومت ایران سال‌ها در خاورمیانه «مرگ، ویرانی و هرج‌ومرج» گسترش داده است.
▪️
︎ او گفت: «هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست پیدا کند» و افزود پس از آغاز دوره ریاست‌جمهوری‌اش، مذاکراتی را با ایران آغاز کرد و در مقابل پایان برنامه هسته‌ای و حمایت از تروریسم، پیشنهاد همکاری اقتصادی کامل داد، اما به گفته او ایران این پیشنهاد را رد کرد.
▪️
︎ ترامپ همچنین گفت که ارتش آمریکا در عملیات «چکش نیمه‌شب» برنامه هسته‌ای ایران را هدف قرار داد و پس از آن نیز از تهران خواست توافق کند، اما ایران بار دیگر نپذیرفت. او سپس ایران را به ادامه انباشت موشک‌ها و پهپادهایی متهم کرد که به گفته او امنیت نیروهای آمریکایی و دیگر کشورهای منطقه را تهدید می‌کرد.
@
VahidOnLive
🔻
دونالد ترامپ: تصور کنید حکومت پلید ایران پشت سپر هسته‌ای حملات تروریستی انجام دهد
▪️
︎ دونالد ترامپ گفت: «فقط تصور کنید اگر چنین حکومت پلیدی روزی قادر می‌شد در پناه یک سپر هسته‌ای حملات تروریستی گسترده انجام دهد. این واقعیتی بود که باید با آن روبه‌رو می‌شدیم؛ واقعیتی که افراد بسیار زیادی ترجیح دادند آن را نادیده بگیرند.»
▪️
︎ او افزود: «در حالی که دیگران حرف زده‌اند، من عمل کرده‌ام. در حالی که دیگران از صلح سخن گفته‌اند، من آن را برقرار کرده‌ام. در حالی که دیگران تهدیدها را نادیده گرفته‌اند، من با آنها مقابله کرده‌ام.»
▪️
︎ ترامپ گفت: «من از آن برای تبدیل آمریکا به قدرتمندترین کشور جهان استفاده کرده‌ام.»
@
VahidOnLive
🔻
ترامپ: امیدوارم پس از انتخابات با ایران به توافق برسیم
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت که آمریکا باید فشار بر ایران را حفظ کند و افزود نیروی دریایی آمریکا تاکنون بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت کرده است. او گفت اکنون نفت بیشتری نسبت به هر زمان دیگری از آغاز جنگ از این مسیر عبور می‌کند.
▪️
︎ ترامپ سپس گفت که در برابر ایران با یک «تصمیم بزرگ» روبه‌روست: یا توافقی حاصل شود که به گفته او به ایران امکان بازسازی و تبدیل شدن به کشوری «بسیار بزرگ‌تر» را بدهد، یا آمریکا مسیر نظامی را در پیش بگیرد. او در عین حال گفت: «فکر می‌کنم درست بعد از انتخابات به توافق خواهیم رسید، چون منطقی نیست که آنها توافق نکنند.»
@
VahidOnLive
🔻
ترامپ: نیروی دریایی و نیروی هوایی ایران از بین رفته‌اند
@
VahidOnLive
🔻
ترامپ: انتخابات در تصمیم من درباره ایران تاثیری ندارد
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل گفت ایران ممکن است منتظر نتیجه انتخابات میان‌دوره‌ای آمریکا باشد، اما تاکید کرد این انتخابات در تصمیم او درباره ایران «اصلاً وارد محاسباتش نمی‌شود.» او گفت: «تنها چیزی که اهمیت دارد این است که ایران هرگز سلاح هسته‌ای نخواهد داشت.»
▪️
︎ ترامپ همچنین گفت برخلاف ادعاهایی که به گفته او مطرح می‌شود، آمریکا با کمبود مهمات روبه‌رو نیست و ذخایر تسلیحاتی این کشور با سرعتی بی‌سابقه در حال افزایش است.
VahidOnLive
🔻
ترامپ: اگر توافق نشود، جمهوری اسلامی ایران را نابود می‌کنم
▪️
︎ دونالد ترامپ در مجمع عمومی سازمان ملل گفت باید تصمیم بزرگی بگیرد که اگر توافقی حاصل نشود جمهوری اسلامی ایران را نابود خواهد کرد. او گفت فکر می‌کند ایران بعد از انتخابات میان دوره‌ای با آمریکا توافق خواهد کرد.
▪️
︎ او بار دیگر گفت جمهوری اسلامی ایران بزرگترین حامی تروریسم در دنیاست اما اکنون دیگر تهدیدی نیست چون آمریکا برنامه هسته‌ایش را نابود کرده است.
▪️
︎ رئیس‌جمهور آمریکا بار دیگر گفت اخیرا ده‌ها هزار معترض اخیرا در ایران کشته شده‌اند.
▪️
︎ او از اروپا انتقاد کرد که متوجه تهدید موشکی ایران نبوده است.
▪️
︎ آقای ترامپ بار دیگر گفت تمام قوای نظامی و اقتصاد ایران نابود شده است.
▪️
︎ او همچنین گفت دولتش در ۱۲ ماه گذشته بیش از هر دوره‌ای در تاریخ آمریکا در زمینه نظامی سرمایه‌گذاری کرده است.
@
VahidOnLive
🔻
ترامپ از همه کشورها خواست ایران را «به‌طور کامل از نظر اقتصادی منزوی کنند»
▪️
︎ دونالد ترامپ در ادامه سخنرانی خود در مجمع عمومی سازمان ملل از همه کشورها خواست به آمریکا بپیوندند و «انزوای کامل اقتصادی ایران» را اعمال کنند؛ تا زمانی که به گفته او تهران حملات به کشتی‌های تجاری را متوقف کند، از «جاه‌طلبی‌های هسته‌ای» خود دست بکشد و حمایت از تروریسم را پایان دهد.
▪️
︎ او حکومت ایران را «ضعیف و مستأصل» توصیف کرد و گفت اگر کشورها متحد بمانند، به گفته او «تهدید ۵۱ساله تروریسم ایران» پایان خواهد یافت و قیمت نفت نیز کاهش پیدا خواهد کرد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78487" target="_blank">📅 17:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjOiR9MJeVnwNg2RMJv-IWu3QWVdVOas52O6CxIEZjh-61Dmnbm6ellgt8TjjDTJiawdgD5QFpV7DDL2gb9Z9IaAqz6wLUQ9pL09vXBZrjnUAG1kT1MLL0Ke4AqZZMskwQCv_-hA3S2-14HwM8ad0Wqrp45O5HBbIZwbboqz6jLb6Zd7NBJyyyEE_F6LUh16AwUzZop45uTVr9leP8uR7Qpd8_M7Wop-nkdD7fnwJdseLPY5DldweNDwuQGsaBPmVz5cAUlyyKvzuCAYDQSAmpebWEuV96gzANYjd23NwMYnhwtFPPQW69chjjL3omUY_HNqjwVoNdvgYIBkNzYAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد جمهوری اسلامی گفته است تهران پیشنهاد کرده در صورت کاهش فشار نظامی آمریکا و برداشتن گام‌های اولیه برای پایان محاصره بنادر ایران، تنگه هرمز را ظرف هفت روز بازگشایی کند و به مذاکرات با واشنگتن بازگردد.
خبرگزاری «کیودو» روز سه‌شنبه۳۱شهریور۱۴۰۵ به نقل از این مقام، که نامش اعلام نشده، گزارش داد این پیشنهاد از طریق میانجی‌ها به دولت آمریکا منتقل شده و بخشی از تلاش تازه تهران برای احیای مذاکرات با واشنگتن است.
براساس این پیشنهاد، جمهوری اسلامی خواهان ازسرگیری مذاکرات با هدف رسیدن به توافقی برای «پایان دائمی مخاصمه» میان ایران و آمریکا است.
این مقام گفته است تهران در مرحله نخست انتظار دارد واشنگتن نشانه‌هایی از آمادگی برای بازگشت به مذاکرات نشان دهد و اقداماتی را برای پایان محاصره نظامی بنادر ایران و توقف عملیات نظامی مرتبط با تنگه هرمز آغاز کند.
در صورت برداشته‌شدن این گام‌ها، جمهوری اسلامی آماده است ظرف هفت روز مسیر عبور کشتی‌ها از تنگه هرمز را باز کند و به میز مذاکره بازگردد. این مقام تاکید کرده است آمریکا برای پیشرفت دیپلماسی باید «جدیت و تعهد» خود را نشان دهد.
کیودو نوشته است پیشنهاد تازه تهران به تایید «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، و شورای عالی امنیت ملی رسیده است. مقام ایرانی مشخص نکرده که آیا این پیشنهاد به معنای عقب‌نشینی تهران از بخشی از هفت شرطی است که پیش‌تر برای مذاکره و بازگشایی تنگه هرمز مطرح شده بود یا خیر.
براساس گزارش کیودو، شورای عالی امنیت ملی ۲۵مرداد تصمیم گرفته بود اگر آمریکا ظرف ۴۵ روز محاصره بنادر ایران را پایان ندهد، جمهوری اسلامی گزینه حمله دوباره به نیروهای آمریکایی را برای خود محفوظ نگه دارد. این مهلت اکنون به پایان خود نزدیک می‌شود.
هم‌زمان، یک مقام ارشد ایرانی به «رویترز» گفته است هیات جمهوری اسلامی در مجمع عمومی سازمان ملل در نیویورک اختیار کامل برای احیای گفت‌وگوهای دیپلماتیک با آمریکا دارد و جزییات توافق احتمالی می‌تواند از طریق کشورهای میانجی در نیویورک بررسی شود.
مقام ایرانی احتمال دیدار «مسعود پزشکیان» و «دونالد ترامپ» در حاشیه مجمع عمومی را رد کرده، اما گفته است همچنان «امکان حرکت به‌سوی توافق» وجود دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78486" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQCOb9VCGyQskbeTNiY2I-zqizFwaJIPdUWQRUDNZSUgfeX_eD4Vqa4LgfklPzaF1-5HUHGc7mLeh3AH7nsWyVEaP5FmUz8nV42YkDSTYGmYkYlJI-XCAR0cHEAP6Ccn0RmaCIJCDk924w2GKHKHODKidWPNCYZTBBwKPVcxg_zcv85Yv1dg6SoasgzgfilrkOPsj4n0izxmZzhvs5PSASOsXNEWRs2jEAYkumDg0fnR3-HGGxmVMDQVskHfq7aO_8GEGgClQUcmGla6LXvuUtJvC-d4p65uD-Wadsm0-1o_TQlFHYKZltFoQ9xkJ49E7fnz-pakb7Vp0V8ZwYNDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدرضا رادان، فرمانده کل انتظامی جمهوری اسلامی، با اشاره به حملات آمریکا گفت که جمهوری اسلامی بر دشمن پیروز خواهد شد. رادان گفت: «به اذن خدای متعال، صبح قطعی پیروزی نزدیک است و ما حتما بر دشمن پیروز خواهیم شد.»
او همچنین از اقدامات حوثی‌های یمن علیه عربستان سعودی تقدیر کرد و گفت: «امروز اراده یمنی‌ها موجب شد تا رزمندگان انصارالله هزاران کیلومتر پیشروی کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/78485" target="_blank">📅 17:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tVnOjqpgRm9QiDpZ7ni-5Tf9SIjSkpn9UoKjOuTXTG6B9RrGc_X86zGP2P6AbjN8woTbi_CkiBF_A__xGveqhWsE-HSLr8oxoP0wrYUldpwsClnqgmFlazq6FV_4QDlznZe6pUgVVk-hZY7yTwR2Pp8SqXF2s3Cufhj-XWuEupAn-mkWRa0lzkws0J-kBuQqiqxJFv9THQnpK4caEemapJMNfJjD3_LZ0-1XYLdwFJcoStS4KRIdsGP2K7H7ueruIpPDinXnMmoH4VLSiqwblZDFs2nuydmkOVcDDWLT34QDV0t0-UQMPIsk5BGfbM3tsEetL0b4igH94OQNYUKMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران روز سه‌شنبه با نزدیک یک درصد افزایش نسبت به روز گذشته به ۲۳۳ هزار تومان رسید.
بر پایه داده‌های شبکه اطلاع‌رسانی طلا و ارز دلار روز دوشنبه ۲۳۰ هزار و ۸۰۰ تومان بسته شده بود. بهای دلار در ساعات نخست معاملات امروز تا ۲۳۵ هزار تومان نیز بالا رفته بود.
یورو ۲۶۷ هزار و ۴۴۰ تومان، پوند بریتانیا ۳۱۱ هزار و ۴۳۰ تومان و درهم امارات ۶۳ هزار و ۴۷۱ تومان معامله شد.
در بازار سکه، سکه امامی با یک و نیم درصد افزایش به ۲۳۸ میلیون و ۴۸۰ هزار تومان رسید و سکه بهار آزادی با یک و هفت دهم درصد افزایش ۲۳۴ میلیون و ۶۷۰ هزار تومان قیمت خورد.
نیم‌سکه با هشت دهم درصد افزایش ۱۲۱ میلیون و ۴۰۰ هزار تومان معامله شد. ربع‌سکه ۶۳ میلیون و ۸۰۰ هزار تومان و سکه گرمی ۳۳ میلیون و ۲۰۰ هزار تومان بدون تغییر ماندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78484" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evc3hJSrEwzFwm5-Ly-Dxu5fEzqLFKQsfBGjLXA5-xQEWoAS_2vGG28MpeDvGKZ7JPxod8J270X0uwEpOcaU6Tk5gGOR2B3DsACKqW5RO9aJdLLBN6JvnEi9k0K2cyPc3Nqqum4yYyGyJ-XmMQ_GiK9CDEsjQN1cnMNfhh-mm8jSSgxDsL4czQj269wWa2znMX37fwAc67K0wgrTD8-R8wQG2fhii70i2mjHXAQWm2jzZyjWxYX0Jg5YD3cmZiHl4avToP4CFEtfSW8MQ_kuC3XLtSZ3EGZ_e47nTMHGpVOgG5T4YkCh7TKC9MsI6-A5MVoRQk-TURa4EC9JVp9aig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهور آمریکا می‌گوید این کشور «بیش از آنچه حتی بتوانیم برای استفاده تصور کنیم مهمات» دارد و به گفته او «اکنون نیز در حال افزایش ذخایر مهمات خود در سطوحی هستیم که تاکنون هرگز شاهد آن نبوده‌ایم.»
دونالد ترامپ روز سه شنبه، ۳۱ شهریور در پیامی در شبکه اجتماعی تروث‌سوشال با رد وجود کمبود مهمات در ارتش آمریکا از کسانی که آنها را «بزدلان و خائنان» نامید نوشت آنها دوست دارند بگویند که ایالات متحده با کمبود مهمات مواجه است. این درست نیست.
نوشته رئیس جمهور آمریکا می‌تواند واکنشی به گزارش رسانه‌های مختلف درباره کمبود مهمات در ارتش آمریکا به‌ویژه پس از جنگ اخیر با ایران باشد. در این گزارش‌ها به‌ویژه از کاهش ذخایر موشک‌های رهگیر سامانه‌های پدافند هوایی خبر داده شده بود.
این در حالی است که شرکت لاکهید مارتین روز ۲۴ شهریور اعلام کرده بود که نخستین محموله از قطعات حیاتی موشک‌های رهگیر «پاتریوت» را از شرکت «جنرال موتورز» دریافت کرده است؛ این تحویل کمتر از یک ماه پس از امضای توافق‌نامه تولید میان دو شرکت صورت می‌گیرد، آن هم در شرایطی که پنتاگون بر تسریع روند تولید تسلیحات تأکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/78483" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5VeVat7hFODEy_uE5dRn7-ejRKZkP3nvmR0OwFZJR2X_z1ux7q4cAeZ8ZizxQN_jzeaOQPeoD7acT5CBUcNJTNPkoAqQpja2ZwyUye7Dqzt8bwVbzqZ6Gwrf3OWbqSNW7Ixei9SylLICPzFCszMsR0nZMBT-ScXxaCHDSbSdJi5ePme1MkXVWZxpOd8tata4g5K3_t5E3rspinG-J7gMyoduMVcMbpbytJFk1I5RD6BzsQSHg3jrkSOxyMaSbVvx2Q7HPJz246vChBfB6abRK2LNCLekqfc0MSx_j42fRfPSTFAOYddbkSSIBH-62Rn6CUU7oMl60t4d__Ab1ii6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو گفت آماده ملاقات با مقام‌های ایران در حاشیه نشست مجمع عمومی سازمان ملل در نیویورک است.
وزیر خارجه آمریکا گفت: «فکر نمی‌کنم در حال حاضر چیزی برنامه‌ریزی شده باشد، اما قطعاً برای چنین دیداری آمادگی داریم، به‌ویژه اگر چشم‌انداز آن نتیجه‌ای مثبت و در نهایت تحقق هدف اصلی باشد.»
آقای روبیو گفت منظور او از چنین چشم اندازی این است که «ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد.»
عباس عراقچی، وزیر خارجه ایران از دوشنبه در نیویورک است و مسعود پزشکان هم عازم این شهر شده است تا در مجمع عمومی سخنرانی کند.
دونالد ترامپ دو روز پیش به شبکه فاکس گفته بود که آماده دیدار با مسعود پزشکیان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78482" target="_blank">📅 17:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJyuu-iKU_McES9JgWOpmMaw1pKQkJSv7xVmmm9vhir3QjTDB_400kvMqehsKF21nrWt7it5ioTvvdKj0vbTTUY-7AG47nwzhyCRXEjuiLJOcbCfF2JjsiKKYG2MIDvtS4x8tmgvT3PytC0i0j8_m9oZOZ_lNRlZuB9wJeKh3YA4TxHQAo_gdpuQZBQugjW5TpEknM8NS__tUGLOL1MJnB8dj0XSyRjpnL5H1-sVwmztzRG1s4suatJHi7yojWeCPWZOvLvMNUUuI8Aj6LZoziZbADMQAyKix6EvZXuxzT1OTsWTqDNy-CCbxmscrXjoRk5WJTlBqb214fI8Kcooiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه چین روز سه‌شنبه، ۳۱ شهریورماه، رسما اعلام کرد که با تحریم «یک‌جانبه» خطوط هوایی ایران توسط واشینگتن مخالف است.
گوئو جیاکون، سخنگوی وزارت خارجه چین، در نشستی خبری گفت که پکن این گونه تحریم‌های آمریکا را «غیرقانونی» می‌داند و با اعمال آنها مخالف است.
این موضع‌گیری یک روز پس از آن رخ می‌دهد که اسکات بِسِنت، وزیر خزانه‌داری آمریکا، روز دوشنبه گفت که تمام شرکت‌های هواپیمایی ایران از تاریخ ۲۳ سپتامبر (اول مهر) «در سراسر جهان تعطیل خواهند شد».
او در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «وقتی هواپیماهای ایرانی در فرودگاهی فرود می‌آیند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛ در غیر این صورت از سیستم دلاری کنار گذاشته خواهید شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78481" target="_blank">📅 17:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpY3W16vdhJiMheOnhE7RVsKAmsOOA4ZjJuvvW6W_IoU3sWUSCcdZJcFFPgFjXldKsh-btvR6BMtVIk9exhh-N-11Lc5fPr8EotpzwBMC-fdQxs79Jl6rNLwEnDWcwWBUJPl069v6Q3qhtIQWzEaT9roFOxjTMjxkwEiT4PLR2ezLUZflibk8Iqm0B9pWmMTceP5OQ7BIx-4P-yvSJ1l5xjc7bY4CJcDPhl8a7muwqbwKkSRO_OH-cSDzG73Abw0P4tiSRISYjbEyvdLuNPVj7TTIqqAygfSj01WZOarmVi2AtH7-rmGU1FDUJxbf1B1hcdH6UEUo-i2rgPkZLtmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسبت نمونه‌های مثبت کووید-۱۹ در ایران برای پنجمین هفته پیاپی بالا رفت و به ۱۷ درصد رسید.
به گزارش مرکز مدیریت بیماری‌های واگیر وزارت بهداشت درباره هفته منتهی به ۲۷ شهریور، این نسبت در هفته مشابه سال گذشته هشت و نه دهم درصد بود. نسبت نمونه‌های مثبت کرونا هفته پیش از آستانه هشدار بالا گذشته بود.
وزارت بهداشت بر ضرورت تشدید مراقبت از عفونت‌های حاد تنفسی تأکید کرد.
این هشدار در حالی است که نگرانی‌ها از شیوع همزمان کرونا و آنفلوانزا تشدید شده است.
از طرفی واکسن آنفلوانزا با وجود نزدیک شدن فصل سرما هنوز در داروخانه‌های ایران توزیع نشده است. به گزارش روزنامه شرق، سازمان غذا و دارو از تأمین محموله‌هایی از چین، روسیه و برخی کشورهای اروپایی خبر داده، اما داروخانه‌داران می‌گویند خبری از توزیع نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78480" target="_blank">📅 17:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDe9Vh9jqr2SFfra3nUzxObwgYMONcnsnUc-ysyJVDENJ5iioedG_4-Y0e2lQyFPDgZezYazM-dhib46JvYKBEQyLHqxLGJI5104lQvrRWhhZC4MT2mIKoFfmFDNnTJiDOrDKYUjbQDHTWH1XiI0Z5rRof8TVEbdHZ_wldf8kSdNidHgzOswqPrIJLvTxYz57hpEEkxdo8gs_GT_C8VhroGoBlk5PucMADY12SjWX7wZWBIxb3t3-exkO2_MlDSbsJM14RZoFIo3NsErHmEmMdpH-KfwU19d5VZ5Ez0JH77pz4b5gFTmTZ6kkFzewuBpAEk5Rxpz29RCmiqw2UbBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر بریتانیا، می‌گوید با ارائه «پشتیبانی دفاعی و سوخت‌رسانی هوایی» به عربستان سعودی در برابر حملات حوثی‌ها موافقت کرده است.
اندی برنام روز دوشنبه ۳۰ شهریور گفت که این اقدام در پی درخواست عربستان سعودی برای دریافت «حمایت نظامی» صورت می‌گیرد.
دولت بریتانیا اعلام کرده است که زمان این طرح «محدود» است و براساس آن قرار است نیروی هوایی سلطنتی بریتانیا به جنگنده‌های نیروی هوایی عربستان در سرنگونی موشک‌ها و پهپادهای حوثی‌ها کمک کند.
برای ارائه این پشتیبانی، بریتانیا طی روزهای آینده یک فروند هواپیمای سوخت‌رسان «وویجر» را به منطقه اعزام خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78479" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwzbwL1FNG_r19u5fmczwkQN63TacatvQjQfB0aOn3-nUUImtm6GBAGnxmogDsRGX5uKqZ_mc710j4TR23JXzQritpPY5ZLYyQH4T6OMwd3HBigVAViaJEG6i-R1zicXvaUYjpW4FhDt1oSVJ2Lz55Ddh1Sgo69Ufac94NV2sFFFN7KejWj-E-5vgT8eYv-S9K9JNYruduf8Q87gxarjEfSicnMjqzCodyoN8I4emHblEH3Y1zsvGnS20YM22wXrQuFQNrw5sZQ-7TqdslAnseOUJxr7E6SqSm-FBKubGWKYpSkw8qx-Bp_PGw6uNAf4Kq1qwkqu8UwOpTQlF83L4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهوری فرانسه، روز دوشنبه، با انتشار تصویری از دیدار خود با دونالد ترامپ در اکس، از توافق پاریس و واشنگتن برای اقدام مشترک در زمینه امنیت انرژی و بحران‌های بین‌المللی خبر داد. مکرون در این پیام نوشت: «به محض ورودم به نیویورک با ترامپ دیدار کردم. ما تصمیم گرفتیم با همکاری یکدیگر برای کاهش تنش‌ها در بازارهای انرژی، از طریق حفاظت از زیرساخت‌های حیاتی در خاورمیانه و تضمین آزادی دریانوردی در تنگه هرمز، اقدام کنیم.»
رئیس‌جمهوری فرانسه همچنین با تاکید بر تحولات جنگ اوکراین افزود: «ما تلاش‌های خود را مشترکا به کار خواهیم گرفت تا توقفی در حملات علیه زیرساخت‌های انرژی و تاسیسات غیرنظامی اوکراین به دست آید. جمعیت غیرنظامی باید محافظت شوند و ما باید هرچه سریع‌تر مذاکراتی جدی درباره شرایط صلح میان روسیه و اوکراین را آغاز کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78478" target="_blank">📅 05:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m715MoWFWKM63Y6vNJQL8qf5partNOdAHxnHVUnok9NJFn7-sNFWiOuIqGngRs6pdEO4jUEfQIAJBIZdbZOhBB1eG4K6XauRGMhvnKylxQ25XixLYVHQ-HYpXe0oYtsIcxYAO5vYB3d1uDA_32AP2w_ZN0J_KFqvNUIvA6g42xxCZWGwj6AVURfjbvwnj7vCOV-S5WXXSi3iTO0f11I32ZK5tUb31R-jpRgdzgYlIc6J9Om_6GGygyUfGjmvuy9locv1xOTC-pqRKE_npWT9R541aE4srcMO_P2EdQxPqplAZ5AchtFygEK5defBYbk0x5GPbEbtHs2MSO96ZcUhXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع دولتی عراق به خبرگزاری فرانسه گفتند بغداد در پی اعلام وزیر خزانه‌داری آمریکا مبنی بر اینکه شرکت‌های تحریم‌شده ایرانی ظرف دو روز در سراسر جهان «تعطیل خواهند شد»، پروازهای شرکت‌های هواپیمایی ایران را متوقف خواهد کرد.
یکی از مقام‌های عراقی گفت: «عراق از بامداد سه‌شنبه، مطابق با تصمیم وزارت خزانه‌داری آمریکا، ممنوعیت فعالیت شرکت‌های هواپیمایی ایران را اجرا خواهد کرد.»
منبع دولتی دیگر نیز این اظهارات را تأیید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78477" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiAFkJvLzTRshEhQThHFWoSj-kj-QYVTGx1iyUIqUMjBbDCAJVv4tOiCYeSBJ80M8IV9r-CLTNoPf34Twyj94V6Ab4CJ1WKmsC9NYTgpXbYpwDf33FKrTm6HVqJrF-1DIqmV7HRtkDlHbqIqHOwYTRJjYJhFgti2vxlS0ElG3towGCHoXD0vbibAud1b0Z6H_MztmarnuRqvG0t9puyfCjqwGdQlVpZv5x_FJblNDYCIVx5eZj362p1Rp4tdCRyHAN-g0Wpb1idsqX3IZdrn_nBKnUC7JKnjCturqkfnPuqD8bIWlfF5laTvQMiPhxwWwIUB9V2Svrvq827HV5nufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس نیوز، روز دوشنبه ۳۰ شهریور به نقل از منابع آگاه گزارش داد که دونالد ترامپ، رئیس‌جمهوری آمریکا، آخر هفته گذشته حمله به شبه‌نظامیان حوثی وابسته به جمهوری اسلامی ایران در یمن را بررسی کرده بود، اما در نهایت اواخر روز شنبه از اقدام نظامی منصرف شد.
بر اساس این گزارش، ترامپ ابتدا در جلسات چهارشنبه با مشاوران امنیت ملی متمایل به اقدام نکردن بود، اما پس از تماس تلفنی شاهزاده محمد بن سلمان، ولیعهد عربستان سعودی، در روز پنجشنبه به پنتاگون دستور داد برای حملات هوایی آماده شود. با این حال، با اکراه کاخ سفید از گسترش میدان نبرد در مقطع کنونی، تصمیم بر آن شد که فعلا از اقدام نظامی آمریکا خودداری شود.
رویترز نیز گزارش داد که ترامپ روز دوشنبه با رشاد العلیمی، رئیس شورای رهبری ریاست‌جمهوری یمن گفتگو کرده است. حوثی‌ها طی هفته‌های گذشته و در جریان تشدید درگیری‌ها، توانسته‌اند مناطق راهبردی مهمی به‌ویژه در امتداد ساحل دریای سرخ را از دولت یمن تصرف کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78476" target="_blank">📅 20:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=IJlwR0j0_x9-EnKfAMrVlN1Piygm-zUFd2bPTzGikHl_ZO4LAqEtTvy67FycLGkD6kKLtioWTL7E7AmqahPISw0Vm48cKm6KEvPnnf2JMC4Vhx_P3jGQh3xu0s7US4K6wrkCVqC4PiVW6S1_u7Ol_3J943UupYUqiktBRPSQVqmmaegmGBDjSgD7s9czMhdkRwhO4kV0TEdzQ_U2fynSoLePJLS_t0iK0ASjclknZcy4nBTu9vOr9M72kLn6Ol9VHv4SBFI6OM7ZLV93THgULtbqaY_8XXz7QeJGcpQx0S0hSup0uQhEsUQSj-UK366d4n7oCSUJSwmeXOlwOU3-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5ae0dfc58.mp4?token=IJlwR0j0_x9-EnKfAMrVlN1Piygm-zUFd2bPTzGikHl_ZO4LAqEtTvy67FycLGkD6kKLtioWTL7E7AmqahPISw0Vm48cKm6KEvPnnf2JMC4Vhx_P3jGQh3xu0s7US4K6wrkCVqC4PiVW6S1_u7Ol_3J943UupYUqiktBRPSQVqmmaegmGBDjSgD7s9czMhdkRwhO4kV0TEdzQ_U2fynSoLePJLS_t0iK0ASjclknZcy4nBTu9vOr9M72kLn6Ol9VHv4SBFI6OM7ZLV93THgULtbqaY_8XXz7QeJGcpQx0S0hSup0uQhEsUQSj-UK366d4n7oCSUJSwmeXOlwOU3-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره جنگ ایران گفت: به دلیل اینکه ایرانی‌ها در حال ایجاد رعب و وحشت در کشتیرانی بین‌المللی هستند، قیمت انرژی افزایش یافته است. ما هم، طبیعتا، تلاش خواهیم کرد در برابر این اقدامات مقابله کنیم.
معاون ترامپ افزود: وقتی ما برای اطمینان از اینکه ایران سلاح هسته‌ای نخواهد داشت اقدام کردیم، آنها در واکنش، با ایجاد اختلال در کشتیرانی بین‌المللی، به این اقدام پاسخ دادند.
ونس افزود: ما، البته، تا حد امکان تلاش خواهیم کرد از جریان آزاد تجارت محافظت کنیم. این همان کاری است که نیروی دریایی ایالات متحده انجام داده است.
معاون ریاست‌جمهوری ترامپ گفت: ما همچنان شاهد عبور حجم قابل‌توجهی از نفت و گاز از تنگه هرمز هستیم، با وجود اینکه ایرانی‌ها هر روز و به‌طور مداوم برای کشتی‌ها ایجاد مزاحمت می‌کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/78475" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MMMgQMEJdFWhViZr3_aip7Im0j9uQss1FPWPp6lOa3b3zE7LH553sCGYTNj8DfsBg2xKLoyCeBYQBwpaCDm8iuu2j6U8LJSJ4nWINTV6pkNR76i7dkMt2wmezjLBIXE7uR0Ci7faPENoUcjJ2d1TBowq9uH1iDkH6JxIDtbL2SSZNQjk7rLqKvFDqbvusywZkyGcXdo2Hv5EwrjWiSSoGboRdg93z-Z8DLDzYqJ5Sv2CgiiOZr5Wc_kZ6PeiJVvSEqsJukCrFnZk2H8EtNlHO3zlUmIjcZqyl5touMVPNogjzdkXJOnf6fiyAwZ5DlaZ9qXUxaEjtPA3Q118r9XTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HZtF0jfJLBoj9EadrLopxM8ijKEhU0hzt5cj8yzi0GHj9X_FYb2TnvHGuDOIx3N5UiGppcvdaJTMfpnYuvHu6Nn2sN5UcnvhxcZYuKtOG1-HmQnALxSb9JbSbiLiKwbbzO7BgylGlVK0bK-HMHoIfj88OHXx_Rb6BWb-lvjF1lgBQJtJBsUF8qQXj_9-hLewy_mG5-HSje06lwh2j9O1fs-0iwzNtMgEelj1uxO2x9GeVpgfi7qVPqpErxbrTLh8dzkt3nPXzfZ4FIV4l8lrljvQi2XyLztHtRKyPmWiKNvToQ7rVOO7niWRW7nAgXi_-JsUoKKWR7tEfGsu0tqtsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TYeDUzZw9h97WM7kwvk75WKcdfcSQ17vQ3cK1U2vQ9nNwYpJ8wqYCBzrfYH1TjgPeaNbKkskU1VDP2wfzYPbrJamHkZ_r8ho7bHjU1SY2Au7pNOdhn9xI4TBFKjMefNeFUNmOJ_O01CYDrSeA0sQlgTMDK58Ok16bLcB_yvsRJ_sQfFyvSC1G8lpmUHOC6IDt1VGp3s1OWMJjT9YSDfxvkDZliJtpl4RhBzObePG4VMSxrABSiCDGO1IMFGhoJ2Jssdbhhi-ZIS3Dfgj_gEH2vnSfasnkW8UGSKvK7kWiTcPzIG01Nn0ZyjniMpr9QDdOL-c0KJUCP-YktuuXUFyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftggU--a5_8P0yljRLTtK0Pu3mxXaPZ-IA7HRXiE7UR8GFZ6xFkx-toYHqUmFyTPb-_6JyHqxW-7twuJr98vSI-zM6v_kPQIdTI332wIqzFUQLfRCTWMpn5SjAPGXAfGi-nnh8CT0PKASPQggEOSwPekZTy8Oa9GKW3YAS9VZIKkcsmncHRMdxzHMy1C8Npa1Kn4NvQp61yq6Z_iv225Zub-prIQ7PPbSokdGS68jlqswe9HXIhwHoLof3oQ1x3P6lO1LYD4I65y15ickdGtFKkzbeHQ5JnbCCqCHMEvnh3dxK2fUNDrrHmSJqFkekcDomAuuWew4wtC8Q96lQbwfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواگردی که توسط ارتش جمهوری اسلامی ایران در نزدیکی تنگه هرمز ساقط شده بود یک موشک فریب آمریکایی ADM-160 بوده است که به اشتباه پهپاد اوربیتر تصور شده بود.
آمریکا با استفاده از موشک MALD به دنبال شناسایی موقعیت سامانه های پدافندی ایرانی است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78471" target="_blank">📅 18:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eee6Pp_aZjVDwQ5DG83aycnOmFbe-C6ll5XpHZV4qUubYIaS3nlDtWJyv6D4eiDa2NBEAkC184gA3Z7p0RBh6G5HSNtPpir2G1iBh-jRO6dvt36HADF2plJkzbwbJAsFHHRJ_-KOJHYSVg-NO3ZJunRCRudL9RXCC7hzS31zE6ozroNUkc3Gv-cAUIkblD0493f-SpUbsh2TkMZoPZ0fMi1i1qVZUl-5BJFKCysJBx_XP_enc29mj4xGuqwCQSW0g47WfWnQfWgdnoO2HfJ7Qb9selZrBTQrMOzbBiEv2pR2UqECMYuK3_KeYFP1sdvce2n6BOYYHjznfAcTKZiJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز دوشنبه ۳۰ شهریور، در گفتگو با شبکه خبری «سی‌ان‌بی‌سی» اعلام کرد که فشارها بر جمهوری اسلامی به بالاترین سطح رسیده است و از ۲۳ سپتامبر (اول مهر)، تمامی خطوط هواپیمایی ایران در سراسر جهان متوقف خواهند شد.
بسنت با اشاره به اقدامات جدید وزارت خزانه‌داری از جمله در حوزه‌های هواپیمایی، دریایی، ارزهای دیجیتال و طلا، تصریح کرد که طبق این تصمیم، در صورت نشستن هواپیماهای ایرانی، ارائه سوخت، خدمات فرودگاهی و فروش بلیت به آن‌ها ممنوع خواهد شد و هر نهادی که این مقررات را نقض کند، از سیستم دلاری آمریکا خارج خواهد شد.
او همچنین از برخورد با حامیان مالی و «تسهیل‌گران» منطقه‌ای و بین‌المللی این رژیم خبر داد و افزود که سه بانک از جمله دومین بانک بزرگ مصر (شعبه دبی)، سی‌امین بانک بزرگ ترکیه و دومین بانک بزرگ روسیه به دلیل انتقال میلیاردها دلار به نفع حکومت ایران تحریم شده و فعالیتشان متوقف خواهد شد.
وزیر خزانه‌داری آمریکا تاکید کرد که دولت این کشور با تمام توان در حال بستن منافذ اقتصادی حامی تهران است.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا همچنین گفت مقام‌های چین در گفت‌وگوها درباره کارزار فشار اقتصادی علیه جمهوری اسلامی حضور فعال داشته‌اند.
به گفته او، آمریکا مذاکرات مثبتی با مقام‌های مالی چین درباره رعایت تحریم‌ها علیه جمهوری اسلامی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78470" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCPbgB9K6AweTq9LAGdPck5jIOp3piUoT7FI-oeAXQrICDev1cnj3TD5QdatVsCUWZvG6aRD3DkNs59eQualzj6r1TAEsS8iS8FXdveGJMWaIPL3bKNdwu1VVI3yPqnER0vWiIoBTz3U6yDQRH9Sd_MiJfRxHXVafr992cxE6HcqJHbbx9us3KlcRNLcta9AGz9mhmOGDm74BlBhrb2o_Lmz3gS-SUlZUGKLwi5fgnHMmpxjvZ36ZUGauV0A2S2ZIm0dwXTIHRbO0XvwTT4w3lMgJGUX_DtSP7ygaNboqPrmGuhXygJ6UoTwQhQx4SUVH9w_jcwOYRpPsS2wU7HjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه اعلام کرد در واکنش به اقدام حکومت ایران در پلمب یک مرکز آموزش زبان فرانسه که به سفارت این کشور در تهران وابسته بود، سفیر ایران را احضار می‌کند و «اقدامات مقتضی» را انجام خواهد داد.
پاسکال کُنفاورو، سخنگوی وزارت خارجه فرانسه، روز یکشنبه، ۲۹ شهریور، در بیانیه‌ای گفت: «این حمله جدید علیه حضور فرهنگی فرانسه در ایران، پس از تعرض به دو کارمند سفارت فرانسه در ژوئیه گذشته، غیرقابل توجیه و غیرقابل قبول است.»
خبرگزاری نیمه‌رسمی تسنیم روز یکشنبه، ۲۹ شهریور گزارش داد که مقام‌های ایرانی این مرکز آموزش زبان فرانسه را بر اساس دستور قضایی دادستانی تهران تعطیل کرده‌اند.
مقام‌های ایرانی مدعی هستند که این مرکز، با وجود هشدارهای مکرر برای دریافت مجوز، سال‌ها بدون مجوز و تحت پوشش آموزش زبان‌های خارجی فعالیت می‌کرد.
روابط میان دو کشور طی سال‌های گذشته بر سر برنامه هسته‌ای ایران و بازداشت چند شهروند فرانسوی توسط جمهوری اسلامی پرتنش بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78469" target="_blank">📅 17:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCOu51aOWfdQqM9vOIEBfb2j155hQL-8yv6P5wh65rjt2i2VTKioqxF7nA3RtLqFoW17VtkrZZ7yfsoHWx3L4BvX62DgdE3p74K-I-MNGCZOSCRqYka5B8hG4HuFlb6a2s5ByiAp2h3AYyl0ZvCsA2e9Pm6sPv8IFh_tdIx2ZEpHXZPjIM6IwLiWaTMFf1Z7z8f-JGedDaiaKc2aZ3ofNytSknJL0I0LJpeB0UhnnLVhv9FDqDcHWe-kxdFF4GamM4JzdxWob6tYchcMwfdWHp7WXq1FN4lSRjSNuy2Du1CaRqoCvBhNXCyXLzmMA3ZyTfGMuXalsuE2wrkTuS4-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «تسنیم»، وابسته به سپاه پاسداران، گزارش داده است سفر «محسن نقوی»، وزیر کشور پاکستان، به تهران ارتباطی با انتقال پیام یا میانجی‌گری میان جمهوری اسلامی و آمریکا ندارد؛ روایتی که با گزارش شبکه «الجزیره» درباره هدف این سفر متفاوت است.
تسنیم امروز دوشنبه ۳۰شهریور۱۴۰۵ به نقل از یک منبع مطلع نوشته است که سفر محسن نقوی به ایران در چارچوب همکاری‌های دوجانبه تهران و اسلام‌آباد انجام می‌شود و ارتباطی با مسائل میان جمهوری اسلامی و آمریکا ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78468" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v61gAsJGaGz0396AtJI0oJKL8lDzIy2cmQnEpXGCiFJ97ANBr3SZzs3K_azLMRHt0gtmtC9hXQX2F4W6DjyUaR8S7eIaWeyQZaYvMDW00qTHiD5BmNLbODp2bo4XQ_ST_uNrMGktOi63nWFS-FZsgSagkbyoD_UaeLlLAQDV3MiUW7opnD_63_fiwgfmQwYt30Zic7igtx2d8pPhr4QXD5BN7_QxubSmFFeb15I5aKrNXDaO_pEvSYh4SXHK-fylDQpATs-AQOUJW-VlJGbgr6w0H9WfmaZocIURMhayZlJt9QtpLftAAT9jzWQydVt-QlNaA4xyhdNpHwQWNW0rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌های منتشر شده، امروز دوشنبه ۳۰شهریور۱۴۰۵ یک نفتکش هنگام ورود به تنگه هرمز هدف یک پرتابه ناشناس قرار گرفت و دو نفر از خدمه آن زخمی شدند.
«آسوشیتدپرس» به نقل از ارتش بریتانیا گزارش داده که این نفتکش هنگام ورود به تنگه هرمز هدف قرار گرفته و دو خدمه آن جراحات سطحی برداشته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78467" target="_blank">📅 17:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d05laHZmW7tCXok90gQ_jfF94PRdVHMD2nIE7M_Q4sFF6T9vFSHtIa3LBInhMgPJI1Wf2aelTdoE7hrGqHvCc33lQyyuUMZcYmeBPpanJT70zbmFjEaxv_qHL83JrBVLwUCvE1VhDkJYqzZycxmsks3vDLOIHUENBbJKJKNLCKw0ml5vonXfn0pu3-U1bhrZfQFMo60-3JCY31VccnQA0Uc7-79q7MNcay9MwQmsCZOPk57POOi9229sNrY-qemR15oSlXvTiIu_a6UHL6Lez-u6nGs0QS8x1xx3n7LITDffOza0a-0FqECkPraABfYRv__ks-W-xlhWAYPySt_L7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jH0cCP9e_lDtUUsYH0HjH6t7vzRF41RWdimVnRPjJGDdJXsMg5lOWJNgix49diLW2WB_RwBxifUrBKAFWx2IXul8rTGwCQ7mxJQn6uBN6NuXlQhcO1Vg_bnZfNFqRi8QlMaOuOgT-ubMG1A02f3AMH-O2_7C4791bgj1jMk6AZ9rBvjUJkCaLQSSQfwkPzigoPGTakGDHPPNKa6BMdFsidlHOZ92J3wJIiVcBmnwDozyaVO--5g1fuvCTiiZKti4zbsu4fkeb28DFYnrFRlvOzvUGXlDpgEimHbOI1NVASF3DdVY1xGKSnZT6ZKe7nYb3vPSAH5wlmfCgd3M4cJlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5yVGohwUMXD_0PY-tejYBOc1oKMIXG1ti5XNK-iT0hxUcxbxbXTr8Qc78HCGLURFaL4HqctP0u-61EmgXM50NfLNTxT2NKw9Rhq7wTJQQ5k2i4sOKsxFNiNmd7KmEWJQmgsjJqGC16SIpGWQnacsvnlmvDIlJjNNHs2CRlc20SIdj6CW1Wiz6GyDGuPmXdntbmE0zpEdZMxhu6THfxWe86s-hCevF9MSToeJ4ukHP3xGKCt3yXwYJk5e2ytGH0ZYrYuGOLKWa3RveVOvytjUFrOtOGZaqtaOdBEavP9SCceQYJPlzNqdfBJLhBBGtgXdeYXfGxrtlm4kn8noaWK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSpzINCWolzvifmMCqxWBbN_Y5WQZ0rxZZPwNjokdrObbKJ3U9j3HaHt9GorsM-Y6pK_NG5XyKnGW2Ym4hQoQKhIWy9EbyeLLOOaBEckLXkIyqVD3OFTFgdLGHKPezu0tIbK9Qg2wp_GOy5uWuTq9_jXRtnqFudm24eH0VA4f5T2pXtjIr96NrAQ873AL_kGh2gswHQmNowucjcsA3vTZj1IWgNqoIVPMSZb5mRjOihPgn42XknZBSq4imYC9CHd1OG5eCRktSIQPAf2ROhXvprFOdB25MHwvrVknfz7nLGgknPcRTkVClMg9kMa4Z-FcQCAtyS1Z3hFrrw36WDAuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
پدر و پسری که قربانی قتل‌های زنجیره‌ای شدند.
🔸
آقای حمید حاجی‌زاده و پسر ۹ ساله‌اش کارون، نیمه شب ۳۱ شهریور ۱۳۷۷ در منزل خود در گلدشت کرمان، به اتفاق با ضربات متعدد چاقو به طرز وحشیانه‌ای به قتل رسیدند. آقای حاجی پور با ۲۷ ضربه چاقو و فرزندش کارون با ۱۰ ضربه چاقو کشته شدند.
🔸
خانواده حاجی‌زاده در تمام این سال‌ها برای روشن شدن حقیقت و پاسخگو کردن عاملان قتل حمید و کارون تلاش کرده‌اند؛ پرونده‌ای که با گذشت نزدیک به سه دهه، همچنان بدون پاسخگویی و اجرای عدالت باقی مانده است.
🔸
سرگذشت کامل حمید حاجی‌زاده و کارون را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-7014/hamid-hajizadeh-pur-hajizadeh
https://www.iranrights.org/fa/memorial/story/-7010/karun-hajizadeh-pur-hajizadeh
@IranRights</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78463" target="_blank">📅 17:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrzntaFh8q8R9kTH6G4dvvL69WyoLm3bbemWr8A7XCD4c8Vv8m9cpwbSG7JRdmBIdBdW6Apkh2xeNFXGLoSYqi9dXAjoFxT34H97AZf5z8vXj3DDoZke8uZ-kG27qhMQK8Oe1_r56hGRwEw6pVIui8loVHJeIVtOguCe7kTKqH6i7UimsT-WmZb0F12eM_6JIR4wvJKVpj2ii28ViXk9JzyUwmQf-AJ8fXKRzChLO0o3ncapdKZP-1Ppnz-YDt25Mjec1WwSHWjrJQjLjJpogk2oqCzXQyDv0N-C8OoJT4DBg0wTyivT79W6CdnsTPl_2Y1eCFsXQFpKtJ6HVHWtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار ایران روز یکشنبه ۲۹ شهریور نرخ رشد اقتصادی سه ماه ابتدایی سال جاری را منفی ۱۰.۱ درصد اعلام کرد.
بر اساس گزارش این مرکز که در خبرگزاری جمهوری اسلامی، ایرنا، بازتاب یافته است، تولید ناخالص داخلی کشور در این سه ماه ۲۱ هزار و ۷۹۵ میلیارد ریال بوده که نسبت به مدت مشابه سال قبل که ۲۴ هزار و ۲۵۵ میلیارد ریال بوده، بیش از ده درصد کمتر شده است.
کاهش قابل توجه رشد اقتصادی ایران در حالی است که نرخ رشد تورم در کشور نیز به شدت افزایش یافته و بر اساس آخرین آمار اعلام‌شده به حدود ۸۰ درصد رسیده است.
از سوی دیگر ارزش پول ملی ایران نیز در شهریور ماه به شکل مداوم کم شد و قیمت دلار آمریکا رکوردهای تازه‌ای را ثبت کرد و از سوی دیگر مقام‌های ارشد دولت نیز از محدودیت شدید در صادرات و واردت و کسری انرژی خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78462" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIuZiVzpjHuPFTYurDrfmBN3mwN1ixAsNmOQBQHnVGPRQ8gUD33lCZn_OsMrZLpa_Fq0eIMY1UdjVfSBQS6gB-QFx1t1zCWT-6cMBRtg2_wE03V98z5Kon7xZ84MNfUHo708dcRgddBap0andhC4W4LD9sgocTu6qC6KI2edVf1ghGPiCWkSy5dHBciEd7HJ-sukmeL87ekHYr3nRR-Ne0-lcpigQjWy4wx0vU-hrjvp0D2TY3bC9slzi87aalYAUhv87_3bw8d3sbDldFyYk5nZqd_ybNm_j7CLaVRWJQNHB-irQtKo9TWc5GPR7FNewHnDY7-PfSY_AzVNPahw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید موسی شبیری زنجانی، از مراجع تقلید شیعه، یک‌شنبه ۳۰ شهریور در قم درگذشت. خبرگزاری فارس گزارش داد او از روز جمعه به دلیل خون‌ریزی معده و عارضه ریوی در بیمارستان بستری بود.
شبیری زنجانی متولد ۱۱ اسفند ۱۳۰۶ بود و در سال ۱۳۷۳، پس از درگذشت محمدعلی اراکی، از سوی جامعه مدرسین حوزه علمیه قم به عنوان یکی از هفت مرجع تقلید مورد تایید حکومت معرفی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78461" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=VAgFSO00nZaDSdvVnW3IyoC5PAtqqXuaFcsOjxzyTPFW8KX6dI8oqdVcOuC45gdMiYEgu2Ya9j2ouTVJ_Ip5sBi9Zua8JtvwqQ-WoDWcs-r9E_SdMPXeXfTPz1EVoCPrpKB0s9QkcMJInWqOuxtM89v8FeIAceaOiYkjTmnFslY6ivvCtxhiyjbC9NDKLKRisl-ex2QLyk2khJai8ImZW_QYt2PPMqf6SzB5zitbzCbr2Pu7otYdMsdn0AUftvSnbc1f0_uJWKJ7QO5CGBV1olGnuYtFMzsBEuMvMP4Km-mBwPuCrBJztbNwrdLt-_PCQ32kZQ9kCZLXbTqGv8RuPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90b38e08b9.mov?token=VAgFSO00nZaDSdvVnW3IyoC5PAtqqXuaFcsOjxzyTPFW8KX6dI8oqdVcOuC45gdMiYEgu2Ya9j2ouTVJ_Ip5sBi9Zua8JtvwqQ-WoDWcs-r9E_SdMPXeXfTPz1EVoCPrpKB0s9QkcMJInWqOuxtM89v8FeIAceaOiYkjTmnFslY6ivvCtxhiyjbC9NDKLKRisl-ex2QLyk2khJai8ImZW_QYt2PPMqf6SzB5zitbzCbr2Pu7otYdMsdn0AUftvSnbc1f0_uJWKJ7QO5CGBV1olGnuYtFMzsBEuMvMP4Km-mBwPuCrBJztbNwrdLt-_PCQ32kZQ9kCZLXbTqGv8RuPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: ۲۹ شهریور، ساعت ۱۷:۳۰، اربیل عراق
هم‌زمان:
رویترز به نقل از منابع امنیتی عراق اعلام کرد که سیستم پدافند هوایی، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل در اقلیم کردستان عراق رهگیری و سرنگون کرده است.
@
VahidOnLive
آپدیت:
نیروهای ضدتروریسم اقلیم کردستان می‌گویند که صدای انفجار شنیده شده در نزدیکی فرودگاه اربیل ناشی از «تمرینات نظامی و فعالیت‌های امنیتی» بود و «هیچ خطری ایجاد نمی‌کنند.»
این فرودگاه میزبان نیروهای ائتلاف به رهبری آمریکا در اقلیم کردستان عراق است.
رسانه‌های محلی کرد گزارش دادند که ائتلاف به رهبری آمریکا مهماتی را در این منطقه منهدم کرده است.
یکی از خبرنگاران خبرگزاری فرانسه گزارش داد که شاهد برخاستن دودی خاکستری از نزدیکی فرودگاه بوده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/78460" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv_XD8Usvju_YjSmdcoeeJ7k8O_ifdONG5fKjEXVdjRiLgbnEmUYdiPT_UvMt6uWPpaDKquVRjHVOVnLpyHKz481nzDoAfEnxpFPk0RXtAPABDrak27ae1HSf9ujQwEOTLtYdX-ct_wlo1_zSGwI2rzRX-BVaXSjskS8_48JW8EzrUuYc6BEvhRZC2a9qAynlJguKdG07-RttLygkk43LTPUpw5tymkce1sw1B2h1gBDgGtEaKP8LFibQCTiYsRfkkpLvDtScnsuMnNPKldKo9ASi7B0PwcOfltj_gbGOmTwgSizvRvkCDWhB62kRWNJ1DkoySqz0zS4lr0h0NCCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز یکشنبه ۲۹ شهریور ماه در گفت‌وگو با شبکه خبری فاکس اعلام کرد که در حال تصمیم‌گیری درباره ایران است و «در آینده نزدیک اتفاقات بسیار بزرگی» درباره ایران رخ خواهد داد.
ترامپ گفت گزینه‌های فعلی روی میز شامل «محو کردن ایران»، «رها کردن آن برای فرسایش اقتصادی» یا «رسیدن به یک توافق» است.
رئیس‌جمهوری آمریکا همچنین گفت: «سؤال من این است که چه زمانی و آیا قرار است کل ایران را منفجر کنم» و افزود: «بهتر است آنها رفتار خود را اصلاح کنند.»
ترامپ گفت برای دیدار با مسعود پزشکیان در حاشیه نشست مجمع عمومی سازمان ملل متحد در این هفته نیز آمادگی دارد.
او در ادامه گفت برخی مقام‌های ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به دستیابی به توافق باشند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78459" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcXd8a7ICMDiIEap0Gu6vXQAgDwMGrdmn9gR8p5nXtU4xNhJf0TRQm9n3K3xWZIMhTXNgSeRc9LN75z2ccR2sY2cBLj_X7k4fc2UDVs7OKh-y2_k38XWmHrSN_3aMcx9e-vH-guvs4oUl2NH9-zk93TQVmONpU8r0EbiLfouusmoZn0o0ABdc4RVOmABHj7ovZZKLKp2_Um8XGr-1JGqUzpxe33uktiFPgR5Gm6xgSbKeV6o7TeihG1GiQyU4vQ67We94gzh0x8TBbstFHKIrF-CLb15eifZnvqOtNw8euXbi5AEGHUdRonq8nzfeNGCt9DyrGIyeSic--z-7ldWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا با انتشار بیانیه‌ای نوشت به اطلاعاتی دست یافته که با آمریکا با حمایت برخی کشورهای منطقه، برای ازسرگیری حمله به ایران آماده می‌شود.
در این بیانیه آمده است: «براساس اطلاعات دریافتی، آمریکا بار دیگر تصمیم گرفته با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران را از سر بگیرد.»
قرارگاه خاتم اطلاعات بیشتری درباره شرکت‌کنندگان و یا کشور اروپایی میزبان ارائه نکرده است.
این نهاد عالی نظامی به کشورهای منطقه هشدار داد که اگر با حمله آمریکا «همسو» شوند، «همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.»
قرارگاه مرکزی خاتم‌الانبیا همچنین به آمریکا هشدار داد در صورت حمله، «تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78458" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClPgv6-l-TcFtPPH2kFQ0J_YXIJCzNTbeqoxyHCbN1w6PgGSiNC_UcUpsxu-pMFvXWnMU8k-fZs1hQDTMLPQ0cGAsoD7lQw8ICmW5WWntCKrUYTyKmaKwqsPyRjCpJ9tYoUPMT6AyZZKB9afhgp0UYbjUcq9nq4Jv66fmz8F6AnVPuWZxfANt0RRtEVwXJ5TWW7bT8ut2QYN-Az1e6JGgvdkSnr7psGgP9u2y61Gm0w-N0jljnm9UHBaSFVdSn1oo_4V8nGgsIn7Cfg0m_S1miRTBHiLAjgMMPzgpu-q0jfLarq2S_Vf4YojV7HcwTNAFHEMlJ-czW5I-HzusKBXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی از جریان‌هایی انتقاد کرده است که با رد هرگونه تعامل و دیپلماسی، ایران را به‌سوی «فرسایش و جنگ بی‌پایان» می‌برند. او هم‌زمان تایید کرد که تهران شروط و پیام‌های خود را از طریق میانجی‌ها به آمریکا منتقل کرده است.
@
VahidHeadline
محمدباقر قالیباف روز یک‌شنبه، ۲۹ شهریورماه در نطق پیش از دستور خود گفت: «انتقال پیام‌ها و تبیین شروط ما از طریق میانجی‌ها با صراحت به طرف مقابل انجام شده... و تا زمانی که این شروط محقق نشده و حقوق حقه‌ ملت ایران به رسمیت شناخته نشود و تعهدات آمریکایی‌ها اجرا نشود، هیچ روزنه‌ای برای بازگشت به شرایط پیشین مذاکره و باز شدن تنگه‌ هرمز وجود نخواهد داشت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78457" target="_blank">📅 16:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtQxKaS11osGw4AwygkaZruRWJbLOJ7J9GAa7hOihrnJsRQzc7HiaDp969Ddk7np0lR0u2aYE7nDLxyrL2b0T_gMDeHXHm3fVwn_r1Rf6PLQ9WuXExiRuDkz2SKBlQMuTwpmhJILpdjHiBAt315F2gGTCUltCMtZEkzkk9FR9Mb_UfMSCgqKCQWnJL94SNWFVxDnk4cXyMcyJByo-OOVZG2tQH5Tfsj3GOABCk1XX2F3ieZ--l652uh1Ppu5KUkjwmqbArTElpXTORxIuJLmIJY85rQN2vO-3w_qbq90HpYzg-WILDfu_W7r8SyVIX2ESZOLMGRdj46kxTXckzdCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه یک دادگاه تجدیدنظر استان البرز حکم مجموعا ۱۸ سال زندان «منوچهر بختیاری»، پدر دادخواه پویا بختیاری، از جان‌باختگان اعتراضات آبان ۱۳۹۸، را تایید کرده است.
براساس رای صادرشده، بختیاری با اتهام «تشکیل و اداره گروه در فضای مجازی با هدف برهم‌زدن امنیت کشور» به ۱۰ سال زندان، با اتهام «اجتماع و تبانی برای ارتکاب جرایم علیه امنیت کشور از طریق همکاری با یکی از گروه‌های مخالف نظام» به پنج سال زندان، با اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به دو سال و با اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم شده است.
تایید این حکم کمتر از سه هفته پس از آن صورت می‌گیرد که شعبه اول دادگاه انقلاب بندرعباس، منوچهر بختیاری را در پرونده‌ای جداگانه به ۱۰ سال زندان دیگر محکوم کرد.
در پرونده بندرعباس، او‌ با اتهام‌هایی از جمله «فعالیت تبلیغی علیه نظام»، «تحریک مردم به جنگ و کشتار» و «ارسال فیلم به شبکه‌های مجازی بیگانه» روبه‌رو شده است. این پرونده با شکایت دادستان بندرعباس تشکیل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78456" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=l001yO58f8nc7KPYvwVaHjg4pMof0CD_aBOumAwH9t3cLAoXx4jds8o2jr3-3JP-WSM-a6X9nxdVi7ZDU8eVRkHY8eJgB9x5yv30SqcSaEsRktdCSXEbznIr77TNNMI4Wjim2Uxoti2AwNorSkEip6DBPmfo3uez-UONc3gM580GAON03QHbA2-V5JH_zdQatv4l2JHvcMJbEMEYe_oaiEzA0-mc2a15XCFDZzCyFh1K6Sz3ph6vqxQz0AFdo00DOfPH3Of22X5xDkkakUjzEj35cmS7Es5vy2eYzyV7bUY47P1LFBx0z2gqCR6ZrVJldnQVLiEHSYYi_z5nQp75Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b5d4ff9bb.mp4?token=l001yO58f8nc7KPYvwVaHjg4pMof0CD_aBOumAwH9t3cLAoXx4jds8o2jr3-3JP-WSM-a6X9nxdVi7ZDU8eVRkHY8eJgB9x5yv30SqcSaEsRktdCSXEbznIr77TNNMI4Wjim2Uxoti2AwNorSkEip6DBPmfo3uez-UONc3gM580GAON03QHbA2-V5JH_zdQatv4l2JHvcMJbEMEYe_oaiEzA0-mc2a15XCFDZzCyFh1K6Sz3ph6vqxQz0AFdo00DOfPH3Of22X5xDkkakUjzEj35cmS7Es5vy2eYzyV7bUY47P1LFBx0z2gqCR6ZrVJldnQVLiEHSYYi_z5nQp75Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نجمه امینی»، دانشجوی حسابداری و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در پیامی صوتی از زندان وکیل‌آباد مشهد اعلام کرده است که دادگاه انقلاب  روز ۲۵ شهریور برای او حکم اعدام صادر کرده است.
او از سازمان ملل متحد، وکلا، فعالان مدنی و نهادهای حقوق‌بشری خواسته است پرونده‌اش را بررسی کنند و برای برخورداری او از حق دادرسی عادلانه اقدام کنند.
هرانا پیش‌تر نوشته بود که او با اتهام‌های «اجتماع و تبانی» و «توهین به مقدسات و ائمه» محاکمه شده است.
نجمه امینی روز ۱۱ بهمن ۱۴۰۴، هم‌زمان با اعتراضات سراسری دی‌ماه، در پاساژ فردوسی مشهد بازداشت شد.
امینی ۲۳ ساله، دانشجوی رشته حسابداری و ساکن مشهد است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78455" target="_blank">📅 15:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5tfe-QhL0RlD_kY6f_y4l8Mz-ud6Ha6kI0b5S9meMi6D3r2tFDJ04YjUtoaNWSyxZI39ouL8IUK7-FxyWE6XvuWnqW96p7Fiq4U5iBpxlo6YpMPqDU9VVZUATqfIoLJzEFwRN5XMQRI5AX_vTAH9PBOU_TIi5vvepKYuJa1Jqy5C7Exc_00NkCLJY7kMZLKDCiALODvbpgmhNDHc27R8YEg_nUrCVreuqWyO6TJplSKF0gVMi0VDd9cH-hpgKnSNCgEO1isvGrIjfBkXmv1ST4iqzGSzEbitUdYRu2MDgyKUvcZuMqfGR1YbjsXGnfIRFWjRGPjMF1aHWFpyt5nIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی جمهوری اسلامی، شامگاه شنبه ۲۸ شهریورماه در شبکه اجتماعی ایکس نوشت ۷ شرط ایران برای آغاز «هر مذاکره‌ای» به دولت آمریکا اعلام شده است.
رضایی در این پیام نوشت: «پیام تهران روشن و بدون ابهام است؛ اگر واشنگتن می‌خواهد از مخمصه‌ای که خود ساخته خارج شود و بیش از این در آن گرفتار نشود، راهی جز پذیرش حقوق و شروط ایران ندارد.»
ساعاتی پیش از انتشار این پیام، رسانه‌های دولتی ایران به نقل از گفتگوی محسن رضایی با شبکه الجزیر گزارش کردند، ارتباط میان تهران و واشنگتن به وسیله میانجی‌گران قطری و پاکستانی ادامه دارد و شروط تهران برای بازگشت به مذاکرات به کاخ سفید اعلام شده است.
رضایی با اعلام آنکه تهران منتظر پاسخ واشنگتن است گفته بود، پایان دادن به جنگ در همه جبهه‌ها، آزادسازی دارایی‌های مسدود شده ایران و پایان محاصره دریایی شروط ایران برای آمریکا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78454" target="_blank">📅 23:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SWevTEi4l1QlwjV2kHRX4kDcKZnYP4tDBt0DFewETS8uUkd9mg8z1VSWjiPwl78o5mpLry79cczAKksRTjgqIyaPrtWxHg-wZV8R-UNpjYxvbgbZLbTfkw6CXgJHeuTWogCWsiN-RzVyqogQy2ExmwkTuS5Dazu8N43YGefMqEk4dUuuSqd-V_pqtlh6SQsQVNpskZkiyzdfS6x2JGwzL8Z3g4cZrJae7rvQcacwU1K_tg2rkLlemBItB_4wSfSi7oaGoTjkImA1C1Z4Bhb9pjuJR3m-2algurruCHCPT1oBt32GQCcyuEb-8ydqWpiyEBwDhs-1TeaYzZFUb2fX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هاکان فیدان، وزیر خارجه ترکیه، گفت در پی حملات حوثی‌ها، عربستان سعودی ممکن است در برخی زمینه‌های فنی نیازهای نظامی داشته باشد و ترکیه برای پاسخ به این نیازها در چارچوب «ائتلاف دفاعی مکه» با عربستان سعودی و پاکستان مشکلی ندارد.
فیدان شنبه ۲۸ شهریور در گفت‌وگو با شبکه «ان‌تی‌وی ترکیه» گفت حملات به تمامیت ارضی و حاکمیت عربستان سعودی جدی است و ترکیه در چارچوب توافق میان سه کشور در کنار عربستان سعودی قرار دارد.
او همچنین گفت عربستان سعودی تمایلی به ورود به جنگ آمریکا و جمهوری اسلامی ندارد و کشاندن این کشور به این درگیری «غیرقابل قبول» است.
فیدان در پاسخ به پرسشی درباره ارزیابی برخی منابع اسرائیلی و ایرانی مبنی بر اینکه «ائتلاف مکه» تنها روی کاغذ است، گفت: «ما به این حرف‌ها می‌خندیم. ائتلاف مکه به یک سازوکار بسیار تاثیرگذار و تغییردهنده معادلات تبدیل خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78453" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/205953bb15.mp4?token=k0AfULM9kzMTIT3YT8U0iPTlaRCmlp6LYJ2lXjgnYQGrI_j3yUTnFQDRbU4nSr31-3eKRtAKlnzoAV0HtSbpFPV-RnCLfYkolJTXssj5k03OQXXjngxafMbVVALNs_QwXX_e4njwUNocfG6l1T7dAo2iB49c4Z8ZYFfeTk78I0eO9ZVBZbW7T-pWZy2Z4ukVvLvr5j2CcSu82ULq650dlSgesyrJXu3r7pd3O-DTuC-37HfN9AruOHECYpCeRf-25VzsTOrrWCcfu1LjK8qUaZ8kJhjlMkE9-csf6YEQID__nalBjMkOfOY0AqVF9b1iXYnwma4FxT76UOOChtH8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/205953bb15.mp4?token=k0AfULM9kzMTIT3YT8U0iPTlaRCmlp6LYJ2lXjgnYQGrI_j3yUTnFQDRbU4nSr31-3eKRtAKlnzoAV0HtSbpFPV-RnCLfYkolJTXssj5k03OQXXjngxafMbVVALNs_QwXX_e4njwUNocfG6l1T7dAo2iB49c4Z8ZYFfeTk78I0eO9ZVBZbW7T-pWZy2Z4ukVvLvr5j2CcSu82ULq650dlSgesyrJXu3r7pd3O-DTuC-37HfN9AruOHECYpCeRf-25VzsTOrrWCcfu1LjK8qUaZ8kJhjlMkE9-csf6YEQID__nalBjMkOfOY0AqVF9b1iXYnwma4FxT76UOOChtH8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، روز شنبه ۲۸ شهریور، در پیامی ویدیویی خطاب به شرکت‌کنندگان در «مجمع گفتگوی جهانی ۲۰۲۶» به میزبانی انجمن سیاست خارجی اندونزی، با انتقاد از رویکردهای مداخله‌جویانه در خاورمیانه تاکید کرد که دهه‌ها حضور و فشار نظامی نه‌تنها کمکی به ثبات نکرده، بلکه چرخه‌ای بی‌پایان از تنش را رقم زده است.
عراقچی گفت، ریشه بحران‌های منطقه را باید در یک حقیقت تلخ جست‌وجو کرد؛ چرا که سال‌ها مداخله خارجی، فشارهای همه‌جانبه نظامی و درگیری‌های پی‌درپی اثبات کرده است که مداخله نظامی امنیت نمی‌آفریند و اعمال فشار و زورگویی هرگز به صلح ختم نمی‌شود.
عراقچی در ادامه این سخنرانی ویدیویی خاطرنشان کرد که در شرایط کنونی، جنگ به‌جای آنکه آخرین راه‌حل باشد، عملا به ابزاری معمول در روابط بین‌الملل تبدیل شده است. رویکردی که نتیجه‌ای جز عادی‌سازی خشونت و تداوم الگوی درگیری و تقابل دائمی در منطقه به همراه نداشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78452" target="_blank">📅 16:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVNA5tffYoHKTQrQoeZzoVIPec8ItzP0zs1tBzSIg31zZQV37WUK9vX6-937cCqOV8_G5A6pNRymZb8KWSa6XT03suSMIHc0R92yDwDtbZ43Po7fZroBxk5GYSYegACQSfqE2UPNBl_0Wl03CUtpq8lNyxej-a2DsVXvHL8eRyfwGhz0uWHzmxY39W95qU1jem4omUTbWB_WxwBIlp2jMLRHVXmezVqRDwO2JXitfRiPLXIJJ-OyPxdVq2ryt-qSn91uQwBwzVc8OrExW4wQXn_D4NaTHZVRBE3MbY2f4Gb9yif49HOc6mkDPMVqCkBv30CExsEPGE6OSuAHMzYW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادستانی تهران اعلام کرد علیه عوامل و دست‌اندرکاران برگزاری مسابقه دو در بوستان ولایت اعلام جرم کرده و پرونده قضایی تشکیل داده است. دادستانی مدعی است که در این رقابت «موازین قانونی و شرعی رعایت نشده بود».
مسابقه دو ۱۰ کیلومتری بامداد جمعه ۲۷ شهریور با حضور زنان و مردان برگزار شد. انتشار تصاویر شماری از شرکت‌کنندگان زن بدون حجاب، رقابت را به موضوع بحث در شبکه‌های اجتماعی تبدیل کرد.
بنابر گزارش خبرگزاری فارس، برگزارکنندگان اعلام کرده‌اند مسابقه با مجوز وزارت کشور و هیئت دوومیدانی استان تهران انجام شده است.
هیئت دوومیدانی تهران گفته پیش از آغاز رقابت از شرکت‌کنندگان تعهد کتبی برای رعایت «حجاب و شئونات اسلامی» گرفته شده بود.
حبیب ستوده‌نژاد، مدیرکل ورزش استان تهران، به خبرگزاری تسنیم گفت مجوز رویداد از شورای تأمین استان صادر شده بود و با ورزشکارانی که «خاطی» شناخته شوند برخورد قانونی و انضباطی می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78451" target="_blank">📅 16:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azv36I-NnbVxiFig9Ktpz7hIbYw9OFjoq0kyaZ72b-fpAmrx7agUt1Xa1lY3yWaCd3gXDlKvEuJ5CGp45B_86wCPr80t5XR7kmd0yGe-tVR73ZsS4KnO85cDHexCqXxhp1nBKQo5mT9-GT7Mw8_KueyuFS83o0YHWIr1warGkYS8d2bQiGR93-USsVevHa1zqD90fW1IrxHO1Et7ntD1uvR1NYjfoPiIKOwGu7M7JwkMuQtIUoeyBnO9YZ1o13800mMd4GcFsU3LXCk4zSGwio_L_cldj71AnR5h9EbiZnkv4ESbOg-jnQcsckjWXs_SM15_RFbLpUB9FdjkND397g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد تنظیم مقررات و نظارت بانکی ترکیه مجوز فعالیت شعبه «بانک ملت» ایران در استانبول را لغو کرده است؛ تصمیمی که پس از توقف پروازهای شرکت هواپیمایی ماهان میان ایران و ترکیه و مداخله نهاد ناظر در مدیریت یک بانک تحریم‌شده دیگر اتخاذ می‌شود.
براساس اطلاعیه منتشر شده در روزنامه رسمی ترکیه، هیات نظارت بانکی این کشور روز جمعه ۲۷ شهریور ۱۴۰۵ لغو مجوز «شعبه مرکزی ترکیه بانک ملت مستقر در استانبول» را تصویب کرده است. این تصمیم روز شنبه ۲۸ شهریور در روزنامه رسمی ترکیه منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78450" target="_blank">📅 16:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZClGJvy2vOrqyYHMpax6tagibecrQSepbeXISgQWLO3_VYztchKkbfXZsm2QbzQNiTDpeaODNG3bWE75u-xufR9LPwEnckPUrGXIkxfn2eBjT4AplriGmUF0ymhSqOhVeezOHxgP1KsJzU_Xo1kBjolRVmUtssalFj-XErer81g3ZZlnHPdQn6GD3eb4evM4i2npnhtkkhmrkZicGRPVOWOnlRT-9asUSAS1P1CvqjjxWe8HmHZq9BWH8INDIgD-ZEUq_CDxlrp_uoeiLbzOARmkSPIseyhkFDkYqeugy80ZgrJpa99iyOVVWFVE1qAE9vVZ78mLt3wAQhCtB2U3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز جمعه ۲۷ شهریور و اندکی پس از تایید کنگره در هفته جاری، لایحه‌ای را امضا کرد که مجوز اعمال تحریم‌های جدیدی را برای تحت فشار قرار دادن روسیه بر سر جنگ در اوکراین صادر می‌کند.
این قانون همچنین تحریم‌های مرتبط با ایران را نیز تمدید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78449" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4ie8Erz5LRxdhvafQN54PjbLlxAvxETqsDMymqbdL2XZkFdDXa0qg5GFZd5-pPsNwnkf0TUG5TFY3IvkNBwMJHoyPmz8C-WUIacXssp9dw12391H6bWJcfer_nzoqFa0wjQScF5k7_PSDcQjEr4eKMm9vq8ZMrcKtCxwUWjpWlOkjDhlCAOgy45RSYb1hwzLmscG03IVEINfer3tnEGuA8tmPCBeOaFvGDBxc2FuVn4VOsUCK-fsQ46CesjfRPCBXhWf4bsv_JQFfMDmbfckqQiJrwlZZmP_KGQJpTnqbPBFtucjVdtHpwwTRjnN1Wssf_CQOZ5A5W0qLCd-U4yng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اعدام «حسین پدران» با اتهام «جاسوسی و همکاری اطلاعاتی به نفع اسرائیل» خبر داده است.
براساس گزارش رسانه‌های حکومتی در روز شنبه ۲۸ شهریور ۱۴۰۵، حکم اعدام پدران پس از رد فرجام‌خواهی و تایید در دیوان عالی کشور اجرا شده است. محل و زمان دقیق اجرای حکم اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78448" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt4gqQxq__so5MxV3xBPykcYwu0NIvdgRwAAqqtBfJOywPgG8LBmUfMi0Q9Drky8NVJwTFB8F1bW2STINCMWHt4cGOVWyxku9jSdQCq4gPDrMKIR_HDyiqWYnh7le_lMLFvgFoNVOgCSYXFubeL58IoWA9rtQRKVGpzvesnRZ7vvSRjJjTxaE8sDDWAAS54jxe4Wn7w8dM-rYIX-ExTlA_EY19gv0PBYtC7BNtce3FRDc8WYhYPFvZh659vJHIxDeQ7NgvpMuucBMLKpXqkKeXen_Drkbd8fUUKe55hTjWGWLQ4syJzzI1CJ_boEDQSedA9MbLNHDVTPl2A4qpH4RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌سوشال اعلام کرد آمریکا با دانمارک و گرینلند به توافقی دست یافته است که کنترل دایمی امنیت و تمامی نیازهای دیگر در گرینلند را در اختیار آمریکا قرار می‌دهد و به تمامی نگرانی‌های متعدد ایالات‌متحده رسیدگی می‌کند. او گفت این توافق هیچ هزینه‌ای برای آمریکا نخواهد داشت.
دفتر نخست‌وزیری دانمارک نیز اعلام کرد انتظار می‌رود که گرینلند، دانمارک و آمریکا هفته آینده توافقی را برای تقویت امنیت در منطقه قطب شمال و اقیانوس اطلس شمالی امضا کنند.
ترامپ گفت: «از این پس هیچ دشمنی از سوی آمریکا نمی‌تواند بدون تایید کتبی صریح ما در گرینلند پایگاه ایجاد کند، حضور نظامی داشته باشد یا سرمایه‌گذاری‌های حساس انجام دهد.»
پیت هگست، وزیر جنگ آمریکا، نیز گفت: «ما بلافاصله روند حضور نظامی گسترده در بخش مناسبی از گرینلند را آغاز خواهیم کرد؛ بخش‌های مناسب زیادی برای این منظور وجود دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78447" target="_blank">📅 04:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=SsiH4OYjVSUwb80IzJMZnSgRo_kCWLaBLRmR7VXercbGVfTX6Wj65BllEMgzKgSqdoeJaXLmFsY2WQ2NiVqYIEqD19Z5RH_zG0CAFFxA8dca57AJZONJAk-2hnAtKKgmVDp9N57CC3RlLTmZ3YbITgxHNKvys2hkwRU4OOoHbflp7kbxy0M4g3zcjzCeYDnEuw5T7IP5n2_ZMb0cyz67hawaChruhFWgu3-7Xiq6E7e4v1BJbFTmfo6n-xRVgBqtrWklnwH-Nmc5lNplU72ICygjAO1E0wk-Ru-cLo-ju2QNwQcYo4dKfSszld0uXGvf62AE1_sk3aE003sGKSJDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da1aa0c490.mp4?token=SsiH4OYjVSUwb80IzJMZnSgRo_kCWLaBLRmR7VXercbGVfTX6Wj65BllEMgzKgSqdoeJaXLmFsY2WQ2NiVqYIEqD19Z5RH_zG0CAFFxA8dca57AJZONJAk-2hnAtKKgmVDp9N57CC3RlLTmZ3YbITgxHNKvys2hkwRU4OOoHbflp7kbxy0M4g3zcjzCeYDnEuw5T7IP5n2_ZMb0cyz67hawaChruhFWgu3-7Xiq6E7e4v1BJbFTmfo6n-xRVgBqtrWklnwH-Nmc5lNplU72ICygjAO1E0wk-Ru-cLo-ju2QNwQcYo4dKfSszld0uXGvf62AE1_sk3aE003sGKSJDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه ۲۷ شهریور در گفتگو با خبرنگاران در کاخ سفید گفت جلوگیری از دستیابی ایران به سلاح هسته‌ای موضوعی است که به آن «بسیار افتخار» می‌کند و ایران دیگر سلاح هسته‌ای نخواهد داشت.
ترامپ با اشاره به افزایش هزینه سوخت گفت تحقق این هدف ممکن است مستلزم آن باشد که مردم برای مدتی هزینه بیشتری بپردازند.
او افزود: «اگر مردم می‌توانستند بین قیمت پایین‌تر بنزین و اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی بدهند، فکر می‌کنم نتیجه با اختلاف بسیار زیادی روشن بود. مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.»
رئیس‌جمهوری آمریکا همچنین گفت انتظار دارد جنگ با ایران «به‌زودی» پایان یابد و پیش‌بینی کرد پس از پایان جنگ، قیمت بنزین به سطح پیش از درگیری بازگردد و «شاید حتی پایین‌تر» برود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78446" target="_blank">📅 04:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=D1pF5C1XrdFss1Nz8KVjyYSVTddYMWHQdFjQkpQtpbOOdSZ6lNA6hDuTp2ygiUWAm_HDFU2J_eFcYzofwqvrvLXuTdPt20eTwv1J2zJE2evbbQ6dAbjTHk1Z4ZTkc6u1cA6UJzDGg2UCLvd7tAkgCxODUkI7EJf0qB2_URUPHWH6g6Q9VdYkm2dzMTLNjxcQvU5RQmvrTo_8c6GHXNq6_PUlYg4GGWM9SbJBeHnNpwCYyKPPhJrKN4FN4f5Zu92adwBC2amcf-5fKSTHEf-_s4PEqLiFVR-fED5Y1NooG9O3i4dfVkChy3GcJE2FEG9Mwn1nDMyVxDL5T2Wjo_7O_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29e74749d1.mp4?token=D1pF5C1XrdFss1Nz8KVjyYSVTddYMWHQdFjQkpQtpbOOdSZ6lNA6hDuTp2ygiUWAm_HDFU2J_eFcYzofwqvrvLXuTdPt20eTwv1J2zJE2evbbQ6dAbjTHk1Z4ZTkc6u1cA6UJzDGg2UCLvd7tAkgCxODUkI7EJf0qB2_URUPHWH6g6Q9VdYkm2dzMTLNjxcQvU5RQmvrTo_8c6GHXNq6_PUlYg4GGWM9SbJBeHnNpwCYyKPPhJrKN4FN4f5Zu92adwBC2amcf-5fKSTHEf-_s4PEqLiFVR-fED5Y1NooG9O3i4dfVkChy3GcJE2FEG9Mwn1nDMyVxDL5T2Wjo_7O_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با برگزاری
رزمایش "جان‌فدایان"
تصاویر بالا رو هم تولید کردند:
مسابقه دوی ۱۰ کیلومتر تهران روز جمعه ۲۷ شهریور با حضور گسترده زنان برگزار شد.
در تصاویر منتشرشده از این رویداد، زنان با پوشش‌های متنوع و اختیاری[تر از قبل] دیده می‌شوند.
رقابت امروز در «بوستان ولایت» و در دو بخش جداگان زنان و مردان انجام شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78444" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OajmzUOrWLr0DkWOpOV66Ra-hrjCLHPzWZeXtj1StMcnpFlLdpYLlaurmt9gnrr75vGD20-ek_RBJOvBWV3XslX3BldYRigydwy-VuPR6b-2XhoNBgYy04brptLfKth4ZPxSKFTXcys9FvfotThPyM48tz90QLij91hMGa34WNDqnFFosAGwFvP5CU2WYde885sTWRf7vc0X7hrG_NIRx5_ekjWyTNUtK76Yz583VAeFDFMkA71VD1FtnfsJOQEttOWAygi69GF-VVetUImFpEUsr8p_igfA8zBy6pHYtlWo3pFKCs6Jj53o4EpsgCzBsewL7hN8VXMQoepNlP9lZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TAWHwx4D34E78D8dUpQMAXFALR5czyB-Cr7YcTiw_CnUfp1cqJnxWaKyPcSuPKMRTq2eJdjvHY6h0EHJQYklYmCQlflURnZ4PY5NJ_mMW89zCBYeJuJJrW8dRRXk_jcFQQ_hYHvswJDR0xVXti11XVlus1QGOu5cGnFU_ZbGSABnANC7B6DEwoYrrlHx3y2ZiLqySYBB4npAzG7zUGf5v_tFuh3nccGFCZFPzRJHeFgAyiLPm4AwUosiRbP9HEdo0RKKH5YbOI8xNglNAazM8WCngKK43PIsvBJrhypykb4b_y1fA3rzfYWbVRrzEYF5RmWbTjXeLlhnBGvP-F1bYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O5mfqR9qP6XtDdTW9VHphaIsR-qizFNfoXMdGvMO5vlJN0b1eDCqwO5YGT_z6dQutvcUbMUNJvYBzzqam3U_dXi3YW8xJG2kBYn_0YyTAwjuyYr-RyIA2_yP-S-ZTLDFrF2py9hnFlptBUVSnE6AA1-YLqb_HdR4AFjHHJWXG4ThNrOgGnkng8gsflxSi4lHdghcmwQmyn0_uRxUcze5qKQJDYwaYDWR5Pd_uwtQuZJ_VVd8JY-ATkVjL9052t6KBUCUC7K1yYY1eR4kzYZq_iPduBPn-Rjs6pKRlpz_Zjvgw8EaaHbPq4Fo95OxHeQKUrCYeIBnT3O2IW2zk507TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SNolH7ESpwQAieBAufRupxEo-aQLEHVEbq9FBmpNcWfB-C8S6dQ367qvVnGBE31j5Qd1tynR9GsM18Qu51m2JfrG1-GDtPld_HwVIfHzjFIzN6RKF4xNTNM7so_jExp7-7HZkEyJ_xXy59XL6ntaCKsRmOUSW1iQaMA_RGr3L_eu9wDpV2HgbQb8IXR6ohSeY5QNVk9VxagIa2S0f_gefSc-gw1ROQCrrVWhzIn_J47OHP1s9EcjK7V5-IyUWZaSo_4yXfk0hcVflJ8WJJQWLqHSsX0pGzZbQPE3V4AqnFY5A_oSk3pcqMQaLjF-ptamH2N35uNegEZWNn_0T9NZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fvie31Fp45dyVtRfHzbuByKBDeQSgChsJdAKLfh0MPhfP6RUoJHfQO8AqLL6u9mVFYBWqwouFPWCDf0Ft8vD5HLu8Xvk3Ui9frz-V0XwLRFdog67-HR87NVR9ylfpJEvQ3JVVgEYIiU2HVqaJgMgnNr5onBz9thg2peJ5rbyWIFLrR_usSGBjt8mBKp0r_ELfqkRFXUOCltoyG-gGvVZrT2pZUCYzGO-DVI7wO4rZOR6HvRDIocaywjEcN7TR1jPWIAeZ9E8qR29E_ziPBQVgFhYkbgdxhtcT8WpKu15d4b1laCxgDD5-auVaxzb6aSm5UtIa2a6ON0JBCmWJFLHHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=j4K-4jw-gWGrpK491BNVGsioW_Pc1Yo92nMrO1oAfdYBwAx-6YqFmBxDLFSQkIahNHr2Lv5MouzEi8AIFLs1wIDyQrQsE04uZ8xj8x8on__52Me1PwzehSosmHnxfPTk54TfWiEqT_PFxoRC0Lar_dWg267pDTk1Ef1-VtjnnhnPpun0wThwGxr9V5Mdfq6mPzpdNCm63-RMy1Mmt7jDTFxYS99o5Vuda8UyQ2D0rE6OWLZLbsvRXJFGE59awqVMGo_BZ4f_3dxir12anABiy4lD0EeOmGeVp16xSmw9MUlmJUIErcUlYLEIekz2iSywvjZZ46akueQfHmmVOuEcRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e40dc6c35c.mp4?token=j4K-4jw-gWGrpK491BNVGsioW_Pc1Yo92nMrO1oAfdYBwAx-6YqFmBxDLFSQkIahNHr2Lv5MouzEi8AIFLs1wIDyQrQsE04uZ8xj8x8on__52Me1PwzehSosmHnxfPTk54TfWiEqT_PFxoRC0Lar_dWg267pDTk1Ef1-VtjnnhnPpun0wThwGxr9V5Mdfq6mPzpdNCm63-RMy1Mmt7jDTFxYS99o5Vuda8UyQ2D0rE6OWLZLbsvRXJFGE59awqVMGo_BZ4f_3dxir12anABiy4lD0EeOmGeVp16xSmw9MUlmJUIErcUlYLEIekz2iSywvjZZ46akueQfHmmVOuEcRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین طائب، رئیس سازمان بسیج مستضعفین، اعلام کرد صدها هزار نفر از ثبت‌نام‌کنندگان پویش حکومتی «جان‌فدا» در تهران سازماندهی شده‌اند و روند الحاق آنها به گردان‌ها و یگان‌های دفاعی جمهوری اسلامی آغاز شده است.
طائب روز جمعه ۲۷ شهریور در جریان رزمایش موسوم به «۳۱۳ هزار نفری جان‌فدایان ایران» در تهران گفت برای این افراد دوره‌های آموزشی مقدماتی و تکمیلی در حوزه‌های زمینی، هوایی و دریایی در نظر گرفته شده است.
این رزمایش از صبح جمعه در مسیر میدان امام حسین تا میدان انقلاب تهران برگزار شد.
@
VahidHeadline
حسین طائب، رییس سازمان بسیج، جمعه ۲۷ شهریور در همایش «جانفدایان ایران» اعلام کرد نیروهای آمریکایی «به‌زودی با شکست از منطقه خارج خواهند شد.»
رییس سازمان بسیج گفت: «جمهوری اسلامی از تمام ظرفیت‌های راهبردی و تنگه‌های دفاعی خود، از جمله تنگه هرمز، با قاطعیت حراست کرده و دشمن را وادار به تسلیم خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78434" target="_blank">📅 16:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EatA4ZU0fVIKXPbPbnJvmBZktIiIOmcgmUe3Eu_xsrp-Seeun7bswEjEsfVst7wbUQb0SuTcD-lTRNAQS2hx5sut9RasZcj8E-eBSjJtho7DGWT45McP2Dhix7U2L5ffQEr7Vk1uayWv7Ey-IWxc33dLpGG5jPW6qHzVm7elOyuXdyp3qqgGE8XwXCeyu2lSDaDEkHLhJBV-z5dn6qvCQdzdNScO4Q3Cg7E_YWKugRMeZ_bRj3dUXHtPToxMBORb43k2kThMFzMbmXWplVgcDS4DqDOegGNIdMPNu6dxU2u7QENxlw722F07FZpZP_V24pxSPhL4lFUQ8HYeTRTHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور کره جنوبی اعزام نیرو یا تجهیزات نظامی به خاورمیانه را در صورتی که به مشارکت سئول در جنگ منجر شود رد کرد، اما گفت کشورش ممکن است برای حفاظت از کشتیرانی تجاری و انتقال نفت در منطقه نقش بیشتری بر عهده بگیرد.
لی جائه میونگ روز جمعه ۲۷ شهریور در یک نشست خبری گفت: «هیچ اعزامی که به ورود یا مشارکت در جنگ منجر شود، انجام نخواهد شد.» او تأکید کرد کره جنوبی برای چنین هدفی «به هیچ شکلی» تجهیزات نظامی اعزام نخواهد کرد.
او در عین حال گفت سئول باید مانند دیگر کشورها «حداقل اقدامات لازم» را برای حفاظت از کشتی‌های تجاری، انتقال نفت خام و امنیت شهروندان خود انجام دهد.
دولت کره جنوبی در هفته‌های اخیر در حال بررسی احتمال اعزام نیرو یا تجهیزات نظامی برای کمک به تأمین امنیت کشتیرانی در تنگه هرمز بود.
دونالد ترامپ، رئیس‌جمهور آمریکا، از سئول به دلیل آنچه حمایت ناکافی از تلاش‌های آمریکا در ارتباط با جنگ ایران خوانده، انتقاد کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78433" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XtW6u7dLQWKzY2i6fiTZGeuZbYd2Ba929jJ0PB0guM8g5l7H_2RHnpLTgeRLjAJ3dB0iPzsSEMlEsvldgsc8kv1cl1PB1YNKOhu8aKH3fMyvCC4hzwxZp1AiC4fSXIL_iUhNS6h6GMsughNIixTmrayItwCrvzGJcUicGW_O-FGhPNPx1OrXEiyFtLZFiUsw3U0lIfCZcWTyPn_3MG6P4NHh1RcVCV9Rx7vZ3g4Zr5J1Aky1TBANENYbZa8Z2ej7TXZng9FLHpdxlkgVquD9ohsObqHUfKn4Y-YNeSpfB9_-dANPKf8WQYCC_71OCmTJJnUmoIBHTRhREyNdxthk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد یک نفتکش با پرچم توگو را هنگام عبور از تنگه هرمز هدف قرار داده و مدعی شد این شناور پس از اصابت و آتش‌سوزی متوقف شده است.
@
VahidHeadline
UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی درباره وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت (CSO) یک شناور گزارش داده است که یک نفتکش با پرتابه‌ای ناشناس مورد اصابت قرار گرفته و این برخورد باعث آتش‌سوزی در عرشه شده که اکنون مهار و خاموش شده است.
گزارش شده که همه خدمه در سلامت هستند و در حال حاضر تأثیرات زیست‌محیطی این حادثه تأیید نشده است.
UK_MTO
در گزارشی دیگر نوشتند:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) یک گزارش تأییدشده اما با تأخیر زمانی درباره حادثه‌ای دریافت کرده است که در ۱۶ سپتامبر ۲۰۲۶ رخ داده و طی آن یک نفتکش هنگام خروج از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
گزارش شده که خدمه در سلامت هستند. گزارشی درباره ارزیابی خسارات و تأثیرات زیست‌محیطی منتشر نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78432" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTnpCKL_XMZXVNZ889GoK_QW8_x5be1d9coN6kbL83XwKkq1GhYwinxNcHDpJj2kN8qIWCd8_40L8391BVv51HKRFDS-bCUG8-tGwkrC6MBnvDJX4EakzQa52YSH3CuoulxVhOt1p_keimk9CuJ03YSdue_viHTinz8swKOQNqhmBydzdmYdCYih1lrxL93W7f62thAwCDrKssODnP9gnQcOzme9rjScfyRUFXDLa50KM7sL9AvuvmVw8uTilvcnXtezoxuX3eWC_zS-xUGqqc4VvV3x1RR3zk4I5iy9VA_AVw87ybimtFFK4cK4N02Gjo3REJ_MnyxqoPm9CPPMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد کرمی‌اسد، جانشین پلیس راهور فراجا از جان‌باختن بیش از ۱۶۰۹ نفر در تصادفات جاده‌های برون‌شهری در شهریورماه خبر داد.
به گفته این مقام فراجا، این آمار به‌طور میانگین به بیش از ۵۰ نفر در روز می‌رسد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78431" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dMnlloczH2cbVKtU4QIclq6RGm2hBJGkoyN7yCag9Mk5PWvjO4lP-d6XAH1gTU4TvPDxOr0QN1Fxv6FtXh2NvH8rf9DmCYHaHCjNAKXzDYnu2kwyU0GRt9K2j27Tc5wmZx_Ih77PMlm7IEgOWjT8xFyYmaB3mopHyA7ck0KyjojLnJaVjAYfirUQM0murHlpT7t26aheYSFukgWzFnvqGrGKfRn8jXwy_BrFK9vHav78mZVcyRI5VImfPTIhuE1zMXKjc21eVetVNumazYfQP8FQQgbpqtB9Y-Wh4323ODc9hM5xNtneO_BJp5eM8tfYU_XLAgiehZkwj9ytOxLtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Wx-PgrIcByJy7gyzlFlO72_eR381_vdFTGaJpUsIaCB0MAS0Y9EE_jn5G2VutaUETPhfCVE6pfXtr7DsR1Eyn7S1S3uOOiwLh7I4BaXdz4ZMljodD7SQSKWeKHqP3CQGJPNVf54Iz_KMAKKhq0s_PTQALBtBYXApy6Z--9ISF1_nF-Ho-x5RtTxwgHAm6o27uqTNwDm8wHzGdR2toXPX7nezkIFc7K_Ez2SWJ8a2FFLg1qRyzTkDVJuAnkPjyBAMPXaiDr28NFQfnKsLSPiyTCHXKSu7t8wOQGTAo4mScgdNR_iblOIKbdGM822a8u5My5eO0-lwpHZNEWh0KvMX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e616598ff4.mp4?token=Wx-PgrIcByJy7gyzlFlO72_eR381_vdFTGaJpUsIaCB0MAS0Y9EE_jn5G2VutaUETPhfCVE6pfXtr7DsR1Eyn7S1S3uOOiwLh7I4BaXdz4ZMljodD7SQSKWeKHqP3CQGJPNVf54Iz_KMAKKhq0s_PTQALBtBYXApy6Z--9ISF1_nF-Ho-x5RtTxwgHAm6o27uqTNwDm8wHzGdR2toXPX7nezkIFc7K_Ez2SWJ8a2FFLg1qRyzTkDVJuAnkPjyBAMPXaiDr28NFQfnKsLSPiyTCHXKSu7t8wOQGTAo4mScgdNR_iblOIKbdGM822a8u5My5eO0-lwpHZNEWh0KvMX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با انتشار ویدئوها و تصاویر مختلفی در شبکه‌های اجتماعی از وقوع درگیری مسلحانه در بامداد جمعه ۲۷ شهریور در شهر زاهدان، خبرگزاری برنا از کشته شدن یک مأمور نیروی انتظامی در این درگیری خبر داد.
ساعتی بعد خبرگزاری فارس اعلام کرد که در جریان این درگیری دو نفر از مهاجمان کشته شدند و یک نفر از آن‌ها دستگیر شده است.
وب‌سایت «حال‌وش» هم که اخبار سیستان و بلوچستان را منتشر می‌کند، می‌گوید از حوالی ساعت ۳۰ دقیقه بامداد جمعه در محدوده خیابان دانشگاه و اطراف خیابان دانشجو زاهدان به مدت دو ساعت تیراندازی رگباری رخ داد و سرنشینان یک خودرو پژو ۴۰۵ هدف حمله قرار گرفتند.
این رسانه به نقل از منابع خود همچنین افزود در این درگیری «یک فرد مسلح، سه نیروی نظامی و دو زن رهگذر مجروح شدند و چندین آمبولانس به محدوده خیابان دانشگاه و اطراف خیابان دانشجو اعزام و در برخی خیابان‌ها ایست‌های بازرسی برپا شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78426" target="_blank">📅 06:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRife-tdep1Rq5OK8s4IabVqZzcbtad3IvCiuOj5igSJfTnNyUc_57Vd5vhp6jAkiRYuHlF_YYG2GukS8VDS8UD2IuvnU-qk5W5-eh8xNw7UsLvQvCWiXy3VMxKJH_kzVIoUc8jazfL9YR-77nAbuAasRNCJPCnbmIylQyYHFrB0GVvu6CvHSUhzrgPXnpZLcEzBfcxw0qzvFUGvHwu3oujSvYTUPkBklxCk5_PGETocUizRw4Zgi4jqfMx1foTIgeP9Hi4baNp15EpAc-KVOxB2TKgXSH1Ak_6qTBnzF_36NTO1IVb7VQwEO-SmvVhVNkvHCH-dskr891KX3EFbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران بامداد جمعه ۲۷ شهریور در بیانیه‌ای اعلام کرد نفتکش «ترند» با پرچم کشور توگو، شب گذشته هنگام تلاش برای عبور از تنگه هرمز هدف قرار گرفته و پس از آتش‌سوزی متوقف شده است.
سپاه پاسداران در این بیانیه گفت که این نفتکش قصد «عبور غیرقانونی» از این آبراه بین‌المللی را داشته و هشدار داده است شناورهایی که به این شکل عبور کنند، با «نابودی» روبه‌رو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78425" target="_blank">📅 02:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uU7Fubyz7O100G_Ckol_RlmMOXvoSID2VzGaQ5Ep2gq7NZKwS3v6RnLLugh_RlcqCMFESMosPhnlO1ITH0Fyg5LoqN8ZR-MEAKi3NS1uRzKVwAB4yrYeONGHFRJZEstrNcPNCmKfTDZIFpOh9zxeMcibbdpSQXzJw_p9BSnnCrgrg6SkkOgmyWjdHRbpVD00IbOCKqPn_2mT9yIXh1x8QzrUf-S5XeRaX5XRdoTjw6nYqfATWDu4OLp2D8MHGvFzHpYCkJjs73TSwpQ7Qyb4orB6MmeAP3nXRTEaAURqrZDcrgOyt_R2W8cYUvQ61ZFlLsinzry4p5PqTtYntjsCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصبِ عمان، دریافت کرده است. گزارش شده که خدمه در سلامت هستند. تا زمان انتشار این گزارش، هیچ پیامد زیست‌محیطی تأیید نشده است. مقامات در حال تحقیق هستند.
به شناورها توصیه می‌شود با احتیاط تردد کنند و هرگونه فعالیت مشکوک را به UKMTO گزارش دهند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78424" target="_blank">📅 23:18 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
