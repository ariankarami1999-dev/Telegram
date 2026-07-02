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
<img src="https://cdn1.telesco.pe/file/UKeCgoiRJqCcI8bMYSNm32qT9oyJ9YrmWDUmt0hvQiRwqkNShIiJA4iHnDDFIREdBayNkf304GHlsiQx819_wXizybHpSrrk8fkySie8_9lTPKLsHNoinKZQQ7YRU7ghxXTuvhqTCjfyG_XcczPe3WlUghdCJ-ImMmIbEFP519PtmWEAw_zOnzlzEwjjL_KR_eUxWJIpbEBJQ5Ua5J9qWJ-E1DrsOr7Lbdf5LMw-XWs8pEYiEPfsOo8iuvY9gXrn3pRIT5VhMrlia_BvVMNeRoeVtv_Jc9SYLTjxkzhhinTeFAmFweMW1cO-2xLREJ_MXNrZDBm8dVd2tGnsG0dc2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 05:59:55</div>
<hr>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=hyiUCSy-xwJDDS3ZPVdexTDIbSyI1vyUkcc2wPrQQ8Kgy-0gzX3I7N9oiD_oG7AzzP663syVbllSUZsueRIc5LYdMGI9iU7Y6sP3ypWEBnUVqpTr_v_v4aAjEmglXmCkBbxOpvZu12I_gdphzemJyQY15K2igs7k_5r7IvIOD6zYK00GhfZthzGSqRCNFs-teyGxaSjMN3f3Tho6mIcnFxkdanKtHOk-66UsRIgYEkNIpltuX5fHLdmdWZ3_zzWphILLTP5O8Nxcdpnm6DBScOaqk8dIp3WUGVWIv-FDCWP3jNWqvA2EZIevAxzIaucXhrn9oXKZHJyd-mZtTZQHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=hyiUCSy-xwJDDS3ZPVdexTDIbSyI1vyUkcc2wPrQQ8Kgy-0gzX3I7N9oiD_oG7AzzP663syVbllSUZsueRIc5LYdMGI9iU7Y6sP3ypWEBnUVqpTr_v_v4aAjEmglXmCkBbxOpvZu12I_gdphzemJyQY15K2igs7k_5r7IvIOD6zYK00GhfZthzGSqRCNFs-teyGxaSjMN3f3Tho6mIcnFxkdanKtHOk-66UsRIgYEkNIpltuX5fHLdmdWZ3_zzWphILLTP5O8Nxcdpnm6DBScOaqk8dIp3WUGVWIv-FDCWP3jNWqvA2EZIevAxzIaucXhrn9oXKZHJyd-mZtTZQHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LC3NLMhyND90IFtHc2XLVzsAYog_5I_qVaouOT4t5WbIndUkN_Jl02h_P2XiPZyL0kxZKCNkzsCyyCO7P-UW_n9sjm0bhXMVcQjnz3vnU9bm3-hie0u9bRrWdiBniwT_VGlDN5cK6rZ57gNX_cHeduiKj0D6vQUlPNJgiFKEG-RBL5ES9d3BD1nWyQCYv93GONyI9hkwQ834mEmRT5wlWdL9a2xZlSCUuYza63OkNJYEebGaYXcoDLGIWvZg-9CnDmUntMTaNgEkD0PaSd3F82Khb_XVmbZqHIMQze1iH0vcWEANAKndAhK3DPo2g9C7kEa25P2MbbxdLda7MuWTaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dGb-4v5RNB4YjWcTm115xjFxHBy8Sf2ACg7jNBS2qSiCY58qvh27aP0CHyiK9iHFh9Q_MZ7eYNFeulEaTdGaZufwxtzbLDQYBFkbg0rNe9Xp1wuUlOlYg_pqfIPqcQvnPGl5n4QULK-o0MPZh1SHGeRwXd23ADi5llbopYQ2qEIawYKknRedZ7BcZfhGhYHVlH6vtJac6Km5EN_pxhs-rR4VaFqZ55UirNXkCWistc2pewCrfC6I5GdZ4OAy7oeTlAFvm7iEthflrNDHn8uSsqVj_m4EdP-C6rOyGm2QqhNQNAP-36u0quh4Lrw4aBpigxdb9f83kXkvYNk3kgFFMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aGBmWFlYsw_ghzH1TRpI5DaKV2VdzJPTZhzFhBPqZk3vPZN-9G4sANwzfsaSxG9mDxwWPJVKjlQ3CXw95sZ-EQ-fDLjflmuqly0TaAqxJdks5xyFATGsvXaMf9ksaDJSKzIzbD-VI77IT5Uh7F-CvHtH5JveZFYuBKr1ahC7HIGid7s-j4JLMWfdgjvHf9XA4Jbvx6sSecA0ooO2hZGPadT_RokgMO-UabNKOSxH5sevDrSdL91lDWEDJDpiIw7Fab3w9QhodQ8lZuXX3rPVwQOnAkvKU9YNUUbKjTzurBlmrzO3yhgd1LM9OWutXCgqJo0_NI-OpqDvpCTbtfPBPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZreLZIPbrSUbh1ltjfqJeI0mDMuWWdMQD5Mxj1KzASCYnnOYocqElsY_EKWjjwimll0ClXN6Ds76TwfjSii33vNOWhcdRDDZ4J2W5dWfh5Rj6Ag-kxGO_oiGYTzzD3WIMf-SZSDLPuH6ontflwqMCjo6WREjP1ncJnDBQ8xxxWn13rcuPomCF62AOy17J-gEUJ1xPNDuGAjfnougbJAxzIgnjdOgqGBMQrMBtJGI-8TrXLSOgvf2mCJhBW-OVXkLyoBzEPnM5vmT7SkoLwIgqscspcnLaLpx340ViRsZNV42IVcuusivdOANsA4NK27kAJXSJLPRtZZ2YqhhzgGn0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eYDANetlR4U0elQo5u_WamHzKsgL7gE1sVjrX9IlhO-8i6J51kMTTpgPEwmXCGuHtUDRGznn_ctYpxqj028JjahuMDzZpnbQPsMp02egQZVGusjrlF3A4EDSKXL4FWu9Nrh0yhdezYo5g6pugQSPLgigD0W5cRweWZuGEZXjrWrJTHZYKuF3HTwSMjy55B6Jt21jGlNfwuEiiWN1MR0REUqNZcMbnjo1vvh-e4sxidyWkj-DahCEOYKNEPgoAmHKR8UXX8ee0r4EuGEQCR5j6OVsBIl8WPYwUY76ZZWoyzgSNtdOtYDqH6AF3pLDYAH6LwkIPHzz0nPMWi4SYyultg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o_ygFBkQY-w_tYWBq9M3dGccCYZd2d_Xt_MZ5PmRt7hArBb--VnwYZKQBytc7TaE1k9A_PbUCeLSbptMsRinVpvCrEokK7PCqJ9Db-e7Bi6Q8S5FSuk5dvj6AnuwyQYphiXk4VjEr4BwTsgYzlxHH0jqJg0StLKJcea5nyGPmnCHCl3fiqZDP-BmLTZC6NObYPwBqU25vvh1oQ37N6GARiJbYKeoHPV1zBEk8924uSJ2-YHHAYD41Vdc77By5rQufrkFFSp_q5v8fbzwivq-_ur9TbJq_g1vW8uWr9uC7OSRvowmfLYTx1Bkhj6cR-Q4inlRkRAoYdx3elwCyyDO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=oRZrGmepw5m3DL0DqQTgH2arXkmFYCIRKSij8SJNRwOiYxW7K_5Gy3nMM3nhp8zZgFmbayYlFdbqp_TRjWgfCylfx5nSPpvY5AAV_ffXMiO3G6OrVOxZ2-iYkOxt_Nq-SbWLJj3fGIZNSYAVFrAhBhzJG3cQyTR2qu3nSSR8mbtleh3ulJjFi656Zu0y8_qG1ev6lI0biERJWbgQkNta9cMljRZNTWTCt1gw49YtcQOSUmLkJbHH6MzvV8lqwJZHhWGRKKVLxSx_qZBMYuy_mutdOofNV19SzCzUH0bo06fZa3f32Gpnqo1TYKXF3-m-LJPdsj_YCWP7OhEfBMigBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=oRZrGmepw5m3DL0DqQTgH2arXkmFYCIRKSij8SJNRwOiYxW7K_5Gy3nMM3nhp8zZgFmbayYlFdbqp_TRjWgfCylfx5nSPpvY5AAV_ffXMiO3G6OrVOxZ2-iYkOxt_Nq-SbWLJj3fGIZNSYAVFrAhBhzJG3cQyTR2qu3nSSR8mbtleh3ulJjFi656Zu0y8_qG1ev6lI0biERJWbgQkNta9cMljRZNTWTCt1gw49YtcQOSUmLkJbHH6MzvV8lqwJZHhWGRKKVLxSx_qZBMYuy_mutdOofNV19SzCzUH0bo06fZa3f32Gpnqo1TYKXF3-m-LJPdsj_YCWP7OhEfBMigBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoP-s1ERF5Bu1TBKJO9u2g0KFsjNFDxfFUe2ZwDu5zbiRIyLJ8y2HRFoYityIqMpJhrLlCrVILpJEAyXHxlreff2vF0IDfwsm29Kp3Q0KqWSdjzBEiLJz17xyxOP9XrCcZzWNiKX-zkt7huYRgerpFDxi0wwKu5SnAwF7_3-qDttpLVlskDE2pWjAsAzTytBw3E2zbs7KUnR-emzqciWM3P136UMbLUzJ1BtdBwpoJ8cNXilo-7XQHLBUfKFBYMCcrMrT5lVcLiAdR1fAOf2zTK011xkoweP1CPt9MlRAgnlNGGK8_EKC5Qn-IbBCQITgL2RTpLy0H_tZxfT0-aRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPHjzyu9JNBit9Q_E2NR4hljpT8muCSIcqj3UsjssroTjNiCCL_s3-VeP0aYl8wy-pcvJtXngFy2A2elyHFF4ZZ9X5_ILhjkc0h1D_Ypks93z4jL7LoGjhLw8lMSp_DV1w2R5v1j7KKC8lLIouZox62coYwu8XlF7aCk5uWomxEF3dxOnwtxwpPviJsywcYunyQn93ZPUmw7tGySQZN58r7jxwqyDwFksmW2c1-25BARH7arZJ-pxdaMCkvcL2diGJ4ttPODR2Q6fo1oovsNFX_eCZAWuF_Xsvj1O0cwV-juOb7YKcU9FxMQrnKbdHdbatmCDSjOhRos-leBSF-w5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiyxnPHVHUhJFCBeJDHPvcQ0KU4Wd2AIW2NI1FxZiOsARkqnXD1NFsjPoPeI_nj_xLYMReTSlUJ4YqTeL62Mxmp3yKNwGXV_p5LDFTndFxTGQA9kVp91ZuxpTTYOUXz3P61Q1JhuitSuPjl2xOacPhwzj9zFwxpNHgQx-32k87qj34OwrIP7RrN8B8qnGMwnVYSPbXLPMJ_TVQ3CbYIdP_usOl3zaYz8Rn1_-8vc0K361oqp3jy6r6D1BhdfTx_WWcBPwHs34ist6TvM6CkVp5nbymD8cIRDs-bzFGjPsP2U3RZn32ywqZGQSenFPWsxMYcZEO4t3hgvvDJGQ9bcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNFBkCngyHLqfHmCoWGMyROhL2q3TmGFAApEAfQMgNKloBDnaZs7EUeulAbqx7dF658NgsxZPNMCiv1Zu6MBDDIyTEpsvkWXFq6WFd2tq34A85vZTABaGhjLTDTnqQudfnjBKmpkGNhUaAlNSwGb3xEEex9xeNsKW_3aFlyu5AcG-FskD42qAbVbxUc0M2lt4RAI12oVA7oImMzIvz2GBQcPgU47WRe78ps2kj2T7rFuNhcfJ5sUeyjqFPfr6am0wRiWH_DDrMmEMc0XZq8zhbGPC2rVk1Y0hLnRVnP09I4L0LAljpYjYSfcfhndUlIGSGUv4Hd6GYHqkcZKVrlJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R-zoS8dkvviv4ptoqLVd2MaOEpzg1tePU1YOOwnJOQMlKA5BojhtR_qmKzypUD3irfjzp37pdZiMp3KcTdrmlm4PxVl6I8BgEh3ZGMNm6ueMgISJRvW6qvTSDkF4r_2aFD1mid5fvaLDQ1PeGGa8UdlG2ctEht6LL7T_fSUG2wPodlT13DI9tjO2r2nPGYSsZfAtFI-1OaHIjpV4nHIt4QondXg3S5rYkXSuk8o6QgO072h6lKe2vF1Ywj8PM5eLQMFYkcm-FAvt-5B8Lnf39DYYGx0LXv5Eo1Aa-kmXVnGiwkhR0SV1W3hLzOt8aqLauFjs7iuq9sg6A3ypYotF9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whjt8qDuUOubEl0AOHSYTr7qJj171XMq2G3QWjwnky_LG0rCWlX4O7OgOZ3_MQHoldvYhCx7dHGm6KOWmqv93wn0bHYYu8FpvsgKEcZS8qv7ngRVWmph4p45EHXidsvHCinq7NNagjyJM3wlfcfbIVRtVS-hNKRisjeR0kGEupl3dx0AT6vt-V79RO1awNP5onlMNiNHsKmMJPJUN1X0Q2nAuELFsl2Jgy0oR7QX1nNcsMftpivVx9LxCeehG7lnyJBiXHw8xl6QsaGjBptO5Q2Vf114hRtXOFewD8EXiQqkh19GeWsnAduSbmbVVpwjNdH1-RIt_hPN5jnFCsni0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2O7Zjq_jOzOKFw0sEwVbCdkWkJTOxFMdUh7QfDXPe8QgTINd_hvif4Dmm3P2fozSasZ5zqJHay0W9Fav-U3nvssEPcAMOlcy6GXpul8Avk3xysuJvpDTlSc-FN5KVac3t1me6f3BBaZ0AIQQ4UI_Xc8cu0JLux6JRpzMIuxovgHLSHrk22YY3q7UK7LvJbh2aeBkkDfSPIzfGFdhlvyWn6CLhn5SelOkWZ8dUDd5nrDCg6somaTSquRMW3eSev9vrIHYdwoU86suk1H5CUkeUi9MvhA-qicQj3C3ZCoYGWl2uMPt0NZHu4halPBg9rdWnkujS5DDCNwlk_uFDvAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6y_p2HmDNhVB4fP9mIGr2ARVYPgRNU3Tlq_WW5f0VB9s1k7K9hQ3OQ6lEsqxda-1Z334vqy7TXj4K93DPLdbz7ZcpCtczrVdiy_AX8vnTd_93_f6GmYFdWXW4jHI8W9pICxjP_1_ZbhLeWjeY44ijGMrtca-SrLz26cM0efp03zMxsIAAFNdKxXSABQBczgXD8ec7LtaznpWEXL9Wkzx-JfyhZEmwDFOZLKmmBLoaNmIlql9TimML83fZ2mw3XbZznlGN_MnILN3BhWCId6dZqIfxhu3J4WUhpSaHIHMIf2WVdrkKTY-90pOKg1DLHD0F4datCtjuEqzOoiL6lU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNjUcM7cen5gp2XgRTYIiFQYb5JYXVGm-_7OvAIqeOEQvmrDp2f8YafrUjbOwvXymoJEW4xT0LJx4wKWUHmaYP3FJVv_VDtpZyMTQK1ibRnTdbUVcvvt16KVWp3cbumrsV1AfzmmYx9oJJtnUh0Bn0IsEweFRZftz3Qz3vsSSrR1BL_yH-lJT5EUfGzwb_pnsMxMzuDI3f1CGdmOXCEOHmwgVmKRg4Z9JXz-z_9hu9p-jQAvTmWO0WpevFVaXJ0BkrwQWx_jGzqxzyjXEIPxFKwpKwvvD34uDGeixMiTZEEH9kBNsWkijRmJPFHKH8_Wk1EdpYAScpg7YNPCdh3YUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjLHVbN1NTKa6O13_fomdGY8HZmJhw_iX9G4CwNZ-BptkSaCjA6qtrzoZRRgmomEg1MqfKxPe9J9vRvSZcXXXZqAxjk1Kn2Ia31XnMYpN36v7gRRJe2pCkSAbBALa72a13oGRa0eWBj6aDqtDH3tcz_Tzlhg86_4x37A4jh8gL-TrMLDI0KJeA1LT_9zfIgS9_HxU8bwgTBzw92ffK27cBNorbWfx0rcVAA7E7MNmExBZ1ediTmsUPALXvYFhMMJSaDO4g_eBHw2HOoLkOuCjk44HqBpmFCWAPLEgFFx2hVQ5UAOp3QqQYPbK-Naub2uofYo0YNGiuH-al8wYPQESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxCAOmyyZ1NxFAMPYnxGuETaArIz-Fy6XfcNDxjDZx2-UF1qritviMObe1wW5EYdBvZAkjesm1FUtboKPzlTymXN5Obxl_LbveV5Id9OUgzy3dDbBbPNRJKo1yFt72ltShQwYMvPor4HAZ8fTtXfxSME5t0Io82pasSXC7iSwa4FftJ_XWLVMs9LRuSWXvWoppSzfB7P37MoqCzNihmFEKYbNg4e1cbRR4nzDBLoeTclbT3Hg_iCZh-TU9DOOa_qfrg2x4wJiRiCg8p6NdR565a-lcNjAeU-au7CfLxzl2irhHRT9UTDPgwwwDHaF4Nc6YB3VNw8qAbmbssYYEWRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzA0_v3QwOW9JFbfDSm-kjmTTMvpP6FvA2WY0TFdigXNYm_5epq--jzmVqsnugKP-hMfD7vpqSwdjaoHo_jiC9zaywbKABMb5fs8Y17dwe0MZ0aoyyTBJ0hqbRg1ymhhQS5GCjKuNo9Ouq0O1JPr2vzqEsCeZATB2T05canJwwLzAqpkQSjx3IZr6DvrxIAAy8vcA2J403xWYcghd5FeZCSh-PAqI04kJT5kpV87PpLyZAexfobS3S9si_vwzSzOFqA4iIVdGzuhON5crgkzAFfxTJlig0EvxrFk3AsXA32rC90aYQ_x8lFK_oJoos4Zhg10PyUR9_NO66rxe8MKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHDY5JjVgQCr3zvDBdjL2M7zKlxl-s9_NK3yHOwINoarlVgPJtMKd5LVj7QnEX11-DCRRyhjxje7KNz7NvshBObszPnadiKt9stu2NjELtzY7arj6INY9sahg0j4qtqFCCEum2Pp8vyxRVDBczqxwhLqNf4FNH9hgxUdfcNr5ACp0XCVflvBlNhwFK3t-KBn84ruW2cDcLKJCTbx1-XBXA-XSXWQpMfdaLIUUPG8Hk9RYrzhweQeweyppPVIO_weBu6HhMvVmp5exZW1nU3CIfowNEubbFDeq6wT6H2Uotzbqar5JBe6r9md3chiVvvaR6oZ4y-sniynojiTGWfF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rR1kD25YSv45_fPMdpJU_TKJIgno24dqsLAyIAm7p-RTd2uXqUwlCMyHcBmRXe_MzM_nr4dwKhst_IDI3gjaPOaNwCRZDCDcEI4Vjp0XWTfdj_L9IxaaaW9NpS7Mr9m76ZqnIpQuvHMc2iQKMZ780eUNIFN9-rp1kGR6hEKfL0JmN4BLxg3r6cXj_klZXiJCI4GAUy_8pxOu2wHueb24TI_PYZmuBfFGPoNOx1Ic8RHP2oSrCypftTmjelcr37iHjEnxzQAZwWqHc0ZAzaEnvhv-iE5E4AlQngTGPjnQwEfp9J7mup3ApY1qNEkTCk2edz3QKB0aPY8cCnwhGU7rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/atyqGIVNst7WUpA8dAXXSyqHdyjrycVFdjEtLRnlraObM8LPYIcNKfY3i0lKCMZ1Au6blvQpq-X4emoV1V8cModdeNWJ74lbieu-pJ_jzV5tnN3UMHgEVNMOrnlanDvzGJUKzw0AmDsI0yJTqOjdcYQDzoN6BWaYlt00pSr1p7fMPoHzSyd_vOeAwGWJjZknGy5k2Sl18vgk56b_6YhmeZiy4STFpbHYZtLw5HrQpgNUYohNX8tDvN09H8moIXMq6axzL3NPW57JzZfeuvlV4t-YvoD4SM3xQYYb-ukovUQcpUsVV5PQVIFmbbaE-AVTwdN5L3HmWZq1ruB6ozw0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tt3AbnzZdLjc0s6i7SMEjvOnevn6Jou3cK_pFKaow88TmgdBHPPV0sa0Nr9BSvBqc2PM0XNPpMK495xNKluAAkGvgu-Sfjpix-3fsbGnWvLMSInO3OBuAGGdJuz5NoPYKNbVHfp1hpGPxQdUvN7gN9dN1NXTjvsawIttkrr0dF6T2_J4JqzvxD32TR3wmUhEKpyucUEVI5mL87a08rotw311EPQeLWDE7OMk9652IdF5GiPRnT17YeaWS2ZeCI1hwfLn8-TiFtSvqWitHOQC234cyJJEke4osEmWt7jg5gqT2P0GBJcLhFUFl2nUWkhZNZVWrvVOIyKE5Nns6tgZ0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sSd_L8YnobkGcfHwLnH-woRDbvrTMo_sHCmkA84RQnzynPOdFesRXufiSKRBceM6b-McWabEfPHZEJ1BW_76Kab5CXOCE3GTMtjUZ9btGcbCh0p_R33gc4IR64wIhMwSihbWa9Kjb9bifUcZe4cnOaFnxcy9ccN0atahav62LMpTZYKREt4WqO725-E4Wc0unRzCiFNWxBhGKltMDcOKqVkRR2yIPaITvOJzvZFZ0ZAks_axMF09Nl3A2YOYHkK2WJ5l2TELZee2za4_VDnaZj4w_h9-wgfbdeKzd5uwESgiYDqD8uor3XCWghQiV5fZoF8XSiqHe4hDahfyqXOfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0cGq0sdqSSLo9n4e1fu3d3ZrjEL5IXigSU7E9Dc0_u6z1SqnBcS9mTzuesONzNal8vTeKgFnBLB3ahxssMTlvXNQVEQXMkYtd-HBX_BVFptrTHHxi6b14wlLVWpnLq2Z4UiGcz_09E3EqOwE5ufadyJQhEa39m9sfDMl0Mrx3AYLpV5HsUUXyk_KU7r7LOCzQh1c2nh1RlRkBPdl_YwifVFBnx82Kj9SYzZUcmGIkgNRO7GNenMslgAa9iFmxWW-qYwjH_kl1YAkl-_7F6zux6F3kFefaDndnvw5nXQY_74fkTZPDYwt1SCEUauzoNCe1enoIM-2GEItSrWHQ66bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-FmYRpq8rl5yKceGZ77_IWRTBbydrjNRm7S_PFtHrEovGaJynFROBBxwEfFqg7y3FZ6LJhT9Bu9KAGvyWDvV6NlLcskPeHqq0zvQ5FaiZTzFdxnuMLpOa0pDh54gq-fgSoEx50nm5svJyZqvAs8ChFUvV4MUUSq7AoXuQGrkbYxsTDYtj88geaSXTt4_-n0b0AgmBo2ZvhSoy-lGKCvr09AK2jBo5DR6hugFsHnb0tkx03FBxrRymFCLlFXSuxIotRX9wj7YUuj0BnS6qztIRjPHvvz3FvgAzT_8EF2LyDUhMJ5wVw2KoO4tYOyvRS7Xzj2QENIPWQpwHVYNhRz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB5Bhfm43cyRUQ-5AxjJtn2r_LwPT7FPwS75v3AY4AcRbvaQ1gsxTtmbT8curonW05on4YF64E_ks262DqSrqn_jIc8TyeiKEeqn9zT69UKNkmWYBj46MBK7j6a_PBsjcN_lC_x3q_ps0qC5GQtlu2AyjeAw8irDAzj1f3b5-rureuasGuJuobhAFsXvitoFNKF2cgAIgmR4ZlHxtiLgFSMTcoXgIa7PBarj0FZsL_fSjBqSqxOPstGA-psyfhAWyguSMuH6YW2yOarztaj6E5fCs42VAsc0mStQiHptzxL5IDrtktXSC0Gp8Aulu2POvxKlpui6Op0_UH91nIfa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuwfgwJVi3Qsna9EipChIjtSgesPxlGJbSi8Lm84Fu7pvubnejbejGwUgY5O7JVftniRmwLvdbpZK8IkmYtzCJ6QQMVKelByRtPtehjRsd8TRTeGaz4vQTw-l3AXFADBXX-u-PcpxbCcb_UGPy97F-SgPVDZThdYK9KWUPHqmFwrPIkJjRaZ6iPuS3kpfZf-icqe43weds22YDvvAdJHSxhH4OpyaXEJgy6Dq7L8XeJYGkmpDlGaosTAXy3NxDWQeOpze2NVN8Cj2uFlz3430dtXZUfLOkEh_yec_tKTqHwBjx8mz_f9PLSFPeGSmkY_ydXl9gth-K0VFwHRA0U9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJknfWIS87uBu47KkvHVNaTnyvJ8C0vO5ncDrjIQ6GFOE16mKBSvvbwcitXdCIEKA9Rn112lbvPNLayL-_2JS1EHoB5Iy0HliGXjdpOz1SprIgujguvStsKiQlOJV5I6ghfb0PYlFqJ1QT_wl76hxqTsawg-GnC-SndwZkR1g3_YUCGLljDIR30e2D1ZRtBxpnYRq08vqMTIbvsHkpvtScofw5Hp8F3SB6h0kuFdrHNxK0LUTR9PjdppbVvXyNGPoqo9xq_QEf3M1zZslWZEVysMAfqBiM8vm-gimIw-w_RNx6kL75wdkobTz-tfYi2CwrboSTCy_uQGO3bEv_uknA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=VHku0bQF445cVmV1BTeuJnsRLMoDqhU9wHQGJeI3HhmXinL8PRKrwyDjZfdwoPNUPC9POlPVqtemU6mjlh0vm0oDEReh-taZ74QJ6hbj1RYbZ_XVtw6IOHcsh3fUNcZ6itHnw5fsUYAAb6IzxifCXeGCO93rTEE0i4Cw5ZrJGryOePdH5bEHsUwKxcgwIkevmqJzUOyDuYJDaxbShFMxrRAgFxWkqLajuORw4nEgdmRmT4HzZfj6jlW4UvdIjyyZi-sqpGU2jglQAVp0LFWGekfFqUCkUVYVSU9lf0MgQl_RpCgnqILJ_GSBevIOcalCNXG1l2cun09i2PtwmturqqvSEVgDcyxHtuGXfM6sEhnY9MFdD_aC-uHyrT2y51gSFJ6oWToGIQxt0DWliMhvh5gCk1iw5lQbAx6_ZgFxXBUfuypsrtB1Mmu_JUFPew8jcuYlC02Ksy3O7Fn_SO2rHJrdAASYxP95I3Jsv_q2RUbVGnmJR01HG831-fkV-oBOxgKxAI78jSvivvpBxD-K76fWZGJnxiA6qJK4uhF8SgZO0BsPUFXZYmgvlnnVhSDtHC6O6DWtJ1d0Y84HLJ2g6YlKBQqaLgRWSn4v6MJDLDzMOxsalCtwQPaRSj33quh9r2lz79GugCvir47JAe7fgtT9XFcbMKT9UoMsG9j-uVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=VHku0bQF445cVmV1BTeuJnsRLMoDqhU9wHQGJeI3HhmXinL8PRKrwyDjZfdwoPNUPC9POlPVqtemU6mjlh0vm0oDEReh-taZ74QJ6hbj1RYbZ_XVtw6IOHcsh3fUNcZ6itHnw5fsUYAAb6IzxifCXeGCO93rTEE0i4Cw5ZrJGryOePdH5bEHsUwKxcgwIkevmqJzUOyDuYJDaxbShFMxrRAgFxWkqLajuORw4nEgdmRmT4HzZfj6jlW4UvdIjyyZi-sqpGU2jglQAVp0LFWGekfFqUCkUVYVSU9lf0MgQl_RpCgnqILJ_GSBevIOcalCNXG1l2cun09i2PtwmturqqvSEVgDcyxHtuGXfM6sEhnY9MFdD_aC-uHyrT2y51gSFJ6oWToGIQxt0DWliMhvh5gCk1iw5lQbAx6_ZgFxXBUfuypsrtB1Mmu_JUFPew8jcuYlC02Ksy3O7Fn_SO2rHJrdAASYxP95I3Jsv_q2RUbVGnmJR01HG831-fkV-oBOxgKxAI78jSvivvpBxD-K76fWZGJnxiA6qJK4uhF8SgZO0BsPUFXZYmgvlnnVhSDtHC6O6DWtJ1d0Y84HLJ2g6YlKBQqaLgRWSn4v6MJDLDzMOxsalCtwQPaRSj33quh9r2lz79GugCvir47JAe7fgtT9XFcbMKT9UoMsG9j-uVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=S1nlloR0EidEVYjP6yPL1a8CGcGu4XCASLBKKcjLg28xbu3ZHlujM64b2jm-xCs_GyUNu08c_EhPPhA4OPqc4S8Jv7bhCEbQCl6x2egh5WtdWXhUOn-FFNASsWPDuULv7j_eYv95GclR0ls--WdboBLCe12Ej01yTNVRfjtxViY4THo5_lhRn0tFx0etkmWfoHQ160Px7RbEC46P9VI-swove-q6OEL7FOI1s-ild_Tc9tLEw_d6QZ7XJHsaCMDVsjXJ7QgVz4WyXgw4vvnxt-OtqA0A9KwbV0KDqzRgS7MnB9p5VZje9ACkwCf_RN8DPk8zKHew3L3KjNu65CZv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=S1nlloR0EidEVYjP6yPL1a8CGcGu4XCASLBKKcjLg28xbu3ZHlujM64b2jm-xCs_GyUNu08c_EhPPhA4OPqc4S8Jv7bhCEbQCl6x2egh5WtdWXhUOn-FFNASsWPDuULv7j_eYv95GclR0ls--WdboBLCe12Ej01yTNVRfjtxViY4THo5_lhRn0tFx0etkmWfoHQ160Px7RbEC46P9VI-swove-q6OEL7FOI1s-ild_Tc9tLEw_d6QZ7XJHsaCMDVsjXJ7QgVz4WyXgw4vvnxt-OtqA0A9KwbV0KDqzRgS7MnB9p5VZje9ACkwCf_RN8DPk8zKHew3L3KjNu65CZv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tB2Def1CE0pSZqehZVrqZWP4vRK0gELPUJ7NAmaLpWFvve6Z_Yk73ofQJOBC17N0d999S9FIjvwv07NWIo20blu0P2E318tyvOs3IgbhClFaBCVZu9DG1qPuY179Xm6BeHvKaelwybZrJ9NOMuti6Oh9e3oPCIU6In2yPk2eiRFY8OcUh5PQZ5A6-Fetg5Ya_lpI0IwcbetVFepxpoqniqqBidl8iseD9HKFf1ADhP3BFbd0wF7ST-APUxwLG78XFubkzZuG9-hnTld8T1b3BslKg9gRSkRPkcIyO_SQMlhTGGlyFJHp-zl5-XE6pYhzqx1lXk9RCUnajw0kyFyHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAMVoN3a2Sj7bXjWSkB8JB652REe5b4LIrg0QKWoNpAURhzx6q_dh87Hn6Ex3Tb9KG2yg5StzcI0C0SQe-FTd2IxhlEtO062axgR7_LwR2RNJZBLRPvpZh0mS5fT6sA1LQ9YRKG7jO6eF6nV3mqnvCqHUye5b6i2TTl20sfHLTknH7SlE78kYH-hd0RL6pMunY2zOeLzjL72_v19ojQRrAhHmPe-22hWTmHJQ42fJ97IJgbRJtU47kUwwmVWtZT-uYKRLx4Huhgm76rAqFxwInQhJFZqIGmXkYBREXX-n4Nd0Chp4s7FoG2G23qser6kM2hMxfOvyWdoO2sLQGSEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dy2DimpJiEZJDiOYpZjDTUuEbjW8SbA3ukiV6qRc2svIh551loS6UqWSjDAAxqbw50exHLd9YEdK7oT0Oiu6BuSSyVTgUnEd3d7gLbZVxRzlTvK1ffhMxZDlo7Q1iK6QPB9OANjAXpuG5ZFMi2ft3cTXm21GfDyvr-mGKIwIDhw8LS-TH7hjyOAgo54U-5bpuyZ3ZyjaZldr5nP-5ygt_SRE9xo1g8yV3mJkc-juz_lcOktzCIYYMLqMrPRYfXjwYrCoJdgMnHRbtpp2qwxiNvKEIq8Vo436PyuCZjjKQ7_-Ojsg5wGGtf7XgwAUise-RpAjwPPvgzuDYFpTw0sipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BaiCn4FtY3lSHyCVYz-MIPaGl4Tpp3RH6gjw-TtNC4nYHXO9wunGIqBWjajwZFIFlFgYAL-Wo2EYjruv8vK5KNfdnrO_mjnjqdCMrCM2ri1zKu3FgVjaL1NFo8xiZM3THrQVbJE2Q5MtfjPb-C8Y-LjRU9z_b8hDHeaf3rG7x-LM7l_wrFr_v8ff2t7-_ny21jTejX_YYIJyGHrN_ukDrPgE2wENnwSvVxw1uR2sFvbQwLjM_pmfCsGJ9gVgeUXzQlc_OKv8gk0phMUv9g7Z38DA6E4P29PP-B7YiZR_zHS_ExBiXSQW59Y8XxWpIMnlBo228Jss2ZaKhwlomAyJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6KlALb7q36FtgcPx0x0ZBu-fndcQOTOAlQnfzKnagewnzqyBpshmzNSGj4lwTVsbs38QcjUv7WFtzQn1bgbDsnIJV_MNK9-8sG_SZn8egkP4uTpdUy1Q9owo9j-jMgm3EhcD2G7j3s6JXSpu3baerJm4vWMfRLT6prpJZGcLGvjgT1Uv244kPQlkWNATl_PrER6MR7G8wWuOyJAJhkHhHhjp1Fz9tGo9WEQnNh3XhGH4eEVF233a_YsCho1fOqsunGLQhzw5IMYl35vWf6JguzZa1we5pA5w0rZU2DY3gp16fvWOtg4CuBe0QNohSzmafjzRI6kdzPTl-O8DvW1cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z71AeU_ALs30oOUsfiw52SUK1rNfvmk-aKyVFkt6ehGmktFgPbS5H0tju97i59FTlqyX9arrZIdL_HeX5hiRL357Oh0MW56vr0ON7rfS47HF0mxlRVsP8bu7vZidnmhbfPg7aIkPHFrWwaa8fcHU-k6SGMhv8QeFUKBYdPGGeHwoULgw93Y2RjdrLCT8odeliWDuJvLYZxf2zt_hFVI8vbSE1pq7GDTU2TblqHzgzU4pGUKvtwllnl2NDRhZuhKW3xAPsbXR-0MADke9Sbv5VmKaKQf_-aq0-LVmnnVxXOxNR73Rhgpb4lt-LR0PCjl1Xe9EiPWyckOvNX4F-SromQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-yCh7ZRpF7qM6lu5xgbFz3wUhUcG7v8Ojd2EfMQQec3rv_pX0GTujqskL1AoWs5CIe-ZUNONcVU_v0irM17v8UHE3ypOUxFU58MlaIwrpnUJFHky1RbtnV8A-xko8_cnxlNwHqis4xzKHBbdi92hl_Hr4A2NAc1gP3x-pwz0XhSRxtgPcoebV8iZkVFcVyZTyDkW_49jYAosoTQIADiOERsHV1Or5nMvgFW4LESMTKJbg-6YLSmMtZoinvEDdomNdk0ANqD7ZMhyVWhX1ABpAkoz_SI_JdwPY-mVtZXPHzsF6ologLlN0lh_OBX0LzId8ya63DeHuMjajAaXHmC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=ooqqhHUXnIP4gpZmhiUpTOocR7XawjuzhctG8V5csiK_eWXa-KxgXVA18sT37bL7Z4zZUimmcc1kanGPm-fNxehUtu4nSGqVtefUmmtu_iwzKasYAOMU6e9AEbOjQHvWSOWzwfh54qVKlz7l6zvvxd5Jn-cdbGUH1XpXo_uOSBeLHOclr3-jtxOu-yFtTn590JF2fILHOHe9ttdlXsj6V5oVvXMFbjotDewc7tgtNyYcFXZdd78OMTjDYbGtP-GncEpUhDCs2jQq-6M5-tbtBNn3nXiHK3cA00RUiaaz82ApCGOhm_i6IIYLhPDm0QmH7RKNMzL91NlasnRKLxQqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=ooqqhHUXnIP4gpZmhiUpTOocR7XawjuzhctG8V5csiK_eWXa-KxgXVA18sT37bL7Z4zZUimmcc1kanGPm-fNxehUtu4nSGqVtefUmmtu_iwzKasYAOMU6e9AEbOjQHvWSOWzwfh54qVKlz7l6zvvxd5Jn-cdbGUH1XpXo_uOSBeLHOclr3-jtxOu-yFtTn590JF2fILHOHe9ttdlXsj6V5oVvXMFbjotDewc7tgtNyYcFXZdd78OMTjDYbGtP-GncEpUhDCs2jQq-6M5-tbtBNn3nXiHK3cA00RUiaaz82ApCGOhm_i6IIYLhPDm0QmH7RKNMzL91NlasnRKLxQqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbn8CtwZFVqFLoZXWosDD1Sslpd_TczOF4ypE9g23cRb09ZNpCQPxUUDDF9puoPazhd9y3Pwtc88BWwQjVeDjGdOnIU1f3N4q0uvR2K-Zmqs_Ys4a5nfafD1TXTXlUVJCX5ufAo8ODLEyOoD_Odkql1iQ188PnBkIdGOuVGlrYALEogfocfOTlGImxhbHkw4EM08G2D5hg5ep7dArQ5gpkyrUoc0hYU5us6wqTkilkkNZfE5aVmSFBFNVzAzMU9eYHfyz55i2Gpm5k9M3SJEhP9TcAD7BxbTASmTH9m001UQY7FEE05vYqmpUHx_lhgZLw7ywdX0zaTguOIbDM-isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R5QfBb1hmyi1dTAN0nqyrLPyquWzqPZCICYZxZP-kgo8LUn_P1sijoD1o0E28tISqK8LAETFDaCtsc8M-wKterE92j2SB6-0SeIQ2hhfkhO4jaTI3XZtwXZrFlBTsSjZVf4hr_PTitDyZSzXmV2VcBG3uNIjI2T4xPVdyS8_4TQWE_tah6ygOTEln7YnW7432_1ZKBX_z6095QhawAT-biP-xuedQ4Qch_pz6KkL5-EdSYDTcCWojPO1deZF2KfAfvaVXFRa68kRvwA469yrvOcwQrz1_lJwxWZApFsRpAlLbi2VHlnro45ZxsmNq_QwqWg4bo9637n0Aa4J6B9DAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VnsIQ8BbnV6QtOWDpsqv-i6qXzk7HgE6c3_8PlXV0kDYy2AV9xt_c887qIl26SoxNbilwrgTb0MuyqYPvIRvjBNMBQpdcv7FPyVwnUQLgMtRcKdYVyrmwon7ZOmBhOPbU0tFL-6BFKSsu7adOwN1H0PpDp1F6Z9aq-mIGRNw7oI8nenf6mSGCIFXl90W4iiM1c0UvJ7vD4UsYvWAv1rj1sBFg2IQChpvd7_OX22X8AJb7y0N_C8LyYouProoL6lntSVIn1XzSZ6aK2RJthha9G37b1nonD3g5PIuflWZLgst4i8jKtPLfUHOepAmyHp4QNP0EaRSMTTUxkz0VuMxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=IBiG1FxkQBNr8OzgnOe_vVkSjodPH5zsogMj35WRxgzajz2HRnnYh9ZDqSO3QSWiT-jGbnA--Turm-hRwEOHMTbL9tUosQFC2Xe2rrVY_llO6RnJLhdZYSL2D1gyO51QyBlg0RK6npAVHvXfeWdt1M2ym2fQcJdyb82H_a6anUdQ7bUZsVpK525Q2Fdb1JuxbFCMz-hjvXq_mxTLjcKZkIzJy5rYY_JwlfByTXr0oysNuYlAJV5NUsFIi8vJYEqiKtnmFHrq1nZBbv0Hhej7h2Kl_mnGQy_Nv_o010MSeLH8vDZhHxSubhW9Qc4S7YOEvHgIQC-A6c7FnEBTzfv8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=IBiG1FxkQBNr8OzgnOe_vVkSjodPH5zsogMj35WRxgzajz2HRnnYh9ZDqSO3QSWiT-jGbnA--Turm-hRwEOHMTbL9tUosQFC2Xe2rrVY_llO6RnJLhdZYSL2D1gyO51QyBlg0RK6npAVHvXfeWdt1M2ym2fQcJdyb82H_a6anUdQ7bUZsVpK525Q2Fdb1JuxbFCMz-hjvXq_mxTLjcKZkIzJy5rYY_JwlfByTXr0oysNuYlAJV5NUsFIi8vJYEqiKtnmFHrq1nZBbv0Hhej7h2Kl_mnGQy_Nv_o010MSeLH8vDZhHxSubhW9Qc4S7YOEvHgIQC-A6c7FnEBTzfv8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8NrqWep24SA3LUNCZB-BsLO7CtrIXtn8uHp-inFFuKIpGzFwuK-2FUY-mjDWN7RQ2nlDbSQ0Qms6zNgVl_YM6G1WpUd7uGfSeYVRE0QiajDs7-7r1mAAClZtij7qhdiMhrN7dGK-r8oXkEAU9_jnkmJk47ZUAvXZZgOTyig6cego_Gvh27EFz4yCxkmkePqcuAX36P0-0LT1xvmF8O7q84Ijlh4II9R1n0S8eVyWxmNdMaRQimi-Bvj3N84Htq3ZQoc3sw1hat1BTk8N3mBJAJodxy22axjhfz82EpKDkXkcWdJ2xiMnlwXOzYK5mMtuo5Xgg-QbC8bDQO1P-jzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HeToV0Jqw8vZTteNN8yp6tuo_C9aNb8UNkJo5U8NlrvmOS8iGaH-DVDeBDeq4WJgtnGDZWm1_7m7apkH2zOKZM11omS7MAJBA0DhP8dV6z5439MTsP9Zui6ab4jgRoXn107cFaRoL_lqtQBOydIzNYpB-KxESXudOwxKSrX5IwhM6cXjQrQ4rCCILbA2Pg9YN1Wo6lMzayHTOsAgcB6dEOllS9Ue9bC25ihTp77GsMumoEqi-27VGIJaOo9Gyv8Wd9TaeFkXlp9adMbgXnvyv6nh6Yc8W0dD19zUm6gQLcg-wlFn8JgmBfjkn1xV_ni5rvv_qDJ6cLHJVgM8F5DcoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlSF8DxQND0AfmnBEUjZHQKb-85NsXFifZmBHAtOTT5k765iUVuKttD9v3d5rdf36S8F1Jzx_lb09SDKQ23KRBrC4I4OVKpHci_2kbyxyUdDQKK-ld1KBvsoWpbolSVe3I1w7IxTVZQsZQL9aatr00eEbFIehJhOSLLcFe1FHcaY4PRSmbL4szYVGMS-QgQqddllzy4Vc0sNxkP9Z_RgJLMoW8EMiBNaiw0KHuTveUzWERDfJeuK7F4yahTdc5Yz3wJRZamUTbVG-PuLRzpRiQUGstDAJ3ldwk8GWLROoLAxe1ozXALT2K4CO6UbzJSDQkPz8JIBNThCJ3DO3NSzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=YxZ3pCenRRuh71UNzOkUdD5UyOf1vpUZlPkIrhhr8EQBWdsjVaYjTlRDob5ueCuHqphs22__LUmP48zvgd2TOd71VEQYAQGiZvHiji4nbgjy8PXNvItUoH1LZPqp_-f4nzgZ1_oflCZJskF1LTVRcQqJ635Kt91mOio_mmDBZFEIXs2FnLBF2NnN8MiWsC11CObVvmTGBXhU85sjLc7J4G6JiWmufqN_gDVMDx1WXG89oX-eNk1g9LdVniDSllXwEoSnoswexuCXkvPSW6yJOMz4NElH6b4zjMSTZDf0_KJhRcD1_RIHdIL56RgbcTGaVvntb1pig8bUYfnkEe2jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=YxZ3pCenRRuh71UNzOkUdD5UyOf1vpUZlPkIrhhr8EQBWdsjVaYjTlRDob5ueCuHqphs22__LUmP48zvgd2TOd71VEQYAQGiZvHiji4nbgjy8PXNvItUoH1LZPqp_-f4nzgZ1_oflCZJskF1LTVRcQqJ635Kt91mOio_mmDBZFEIXs2FnLBF2NnN8MiWsC11CObVvmTGBXhU85sjLc7J4G6JiWmufqN_gDVMDx1WXG89oX-eNk1g9LdVniDSllXwEoSnoswexuCXkvPSW6yJOMz4NElH6b4zjMSTZDf0_KJhRcD1_RIHdIL56RgbcTGaVvntb1pig8bUYfnkEe2jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=fF26w8Lj4yUz3zOo3EjNpi5IcgV1fB81CzMMQ-nXfm1Kn8vW5mWViObRr1DfCOalqZvnNel-I6iPyKH0WEV3tjLQv4JkpNV4zeqdYQlJL2brW-T-e6xHPjVfib7QPVKYT5N77NE2mUHrh0gYSa173Dts5mgnGaHETADUnzDAyA2Q7EwsFcW94uqNBJOmk9_hHwgNx3hn-kbhHVtQtxRZBx49oUXfzNA3FurvJbyFHAZ_IXoTFmI7633moQfsB-4Z_VtFQLQ7t9y0sw_qqbejEx1a-QNXx9QKqp7O6h_jaoncn5_WQ4uP0k0ZBzr5pcaG25jZr0RXbt8GHv6v_njv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=fF26w8Lj4yUz3zOo3EjNpi5IcgV1fB81CzMMQ-nXfm1Kn8vW5mWViObRr1DfCOalqZvnNel-I6iPyKH0WEV3tjLQv4JkpNV4zeqdYQlJL2brW-T-e6xHPjVfib7QPVKYT5N77NE2mUHrh0gYSa173Dts5mgnGaHETADUnzDAyA2Q7EwsFcW94uqNBJOmk9_hHwgNx3hn-kbhHVtQtxRZBx49oUXfzNA3FurvJbyFHAZ_IXoTFmI7633moQfsB-4Z_VtFQLQ7t9y0sw_qqbejEx1a-QNXx9QKqp7O6h_jaoncn5_WQ4uP0k0ZBzr5pcaG25jZr0RXbt8GHv6v_njv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t0SHvGkeI5FZ3QbCiF6tAvUwsR3lGQ_KuOOJdZZSoTySvZo50Yvq5Kq0W_lA2ZPgIrXwI1AROh6YEzcw0qGH9Kv6_Zb5eQQARvomZS38NE8BeRg486vu77f2qnBOLKI-97NhH4y5agjR5ymw5jkRA_tLVv9S11nU3t2qgPLsUVPWuQm8ZEzC9gIrWu_FozfWhnOZAhIQvyCySFHAvnZGjsk3w26IzDo_AWV-R2PZOFMyV3yAulv5ZwePC8sKu5EAvbPjl6piBe4lOOHIxOLjjRmZoz9MxpW2JQSmLC3Tuaqy480Z17kzxXwiEdcHroecPETSUidvyscSS8VmS0Wg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O2GSBp0p6VkbmWQCJ2E8pdrYAwyNz48ip0_r7Z6B1QKaNvMPRjpt5_UOvpyC1FTPisgNbuSfQ9wfRvQrN04EtgD6qNNESXhZAkQVMzmCBf81VvhGfsjr1vVIiqEVLZaQ_SpkSR8VIa9_XbaB_AiNs7qyt8-UFS4YB4RHpLLoN1jANfv0cNAiFlY7PZTy7NNN8samuKL0EiN5_xaLZkUeTDitkTK17JnN88Eu-_KCzKN6Q6Ajwtj1a0r_Ki6jH3pUKmdZLA9Uii2YNFV_Z5uY7VerX9hSkcb8CsIKWSahTeE4di81MPkvQ0DJ6MN7uzIprcHnDA3UG6gE33hiihWyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vi3mA7msXmVUrRu6EHqagPU_oWkrNF8TIKdz1kamPNE9BE4vedCSCmKmRcfACCKAcoE2Mize9SNbcCMkEjEUfqAAXoOPJuLgnEOLfd91uJjcGLfZUkDH6rhAvZM5Kq9L0eUZ5CdSd_18Hyz0ZU8oXmqlJ6ZOUxIvGUld3pdoyc0FMu2Da6j3xLKstClEEfiHF9dnsRc0G03pB8Y1gxAJAZYfXoFd1ZQr9mSVwMdhhbyEQFgxsC_sn1g8XBbLvzdHTR7Ei78PxGQqAMjaimtMz4mu058i0ZoDa8oYwf4kx4A2CxSvqWeNY7NPVGJP5Af-yz8tUsyTxuR_sbVT2F_nuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=JRYYQeUzcx7rKYv7MKfl6mvXha6SmWeZB6t-4XuHChGzb2zrtIxJt_Tjj069fAskY-kWM2NSBV0D3sVrkX2aCQJ26kvQmQDEXr7Olpoqj2Xg3na24Xjs1frbjiMP_NV4kvr65eYkl9Ca_42NJ5pTq5amvyRbtqHdZyLxuAdSmhCk2naAAHCxgHLqABoAOfzhUADxUvORuU5pwxQf1BLRAluYuAKHr_ymqZX7thmA9ZAVbDBRgJT4VJBZ7JZNksZur2-1roCH3oG-FmGEKJXx80QCWjTmlHgN4oq_wUdERd16odgD9tDEhD_xGwnX_bsfILmI5amHz02k792MxOR51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=JRYYQeUzcx7rKYv7MKfl6mvXha6SmWeZB6t-4XuHChGzb2zrtIxJt_Tjj069fAskY-kWM2NSBV0D3sVrkX2aCQJ26kvQmQDEXr7Olpoqj2Xg3na24Xjs1frbjiMP_NV4kvr65eYkl9Ca_42NJ5pTq5amvyRbtqHdZyLxuAdSmhCk2naAAHCxgHLqABoAOfzhUADxUvORuU5pwxQf1BLRAluYuAKHr_ymqZX7thmA9ZAVbDBRgJT4VJBZ7JZNksZur2-1roCH3oG-FmGEKJXx80QCWjTmlHgN4oq_wUdERd16odgD9tDEhD_xGwnX_bsfILmI5amHz02k792MxOR51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rfOAML70RPZ3Mgt10IrUPoJIxViLpLAxFbHRrJPKGmDRuA9FSecLYdoqGKzF3cnL86P-qKjM74m-jWSlAuYP-VW1AUkxlrNC8U4haBdeim0YG0Ui2aZ4BbivKpGo5neXM0_V1VWF9_rDGZ_68ni3Lb04hzfg0vE4pgyq2HZziCCldU4fhEzyKzFv42RmXMfmrXmhain4QD86_LYbhRSOY9mrBBYL-T4qnKdXgPEg2KmXwNJyZUIMknkJ-EPct-T2Cf1ga4Nfg0yUC_lmB0o2l_48AWTXRJqQJmbWlOndUGJMR-5DWup5LmM5Qlcfn6InmWuoRtPSgVwhIZrOFcxdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eackADJzF1hlZW2FKIfcNvJ2-LFALX3LnKZPTuI9wwnkXpd5Ha90-uZ7PNkW8li-NsyYoBqfD0Z6kBrKSkkXcV87FvxuhenHvrF9fOiQA46AFNMPYOFDt8qXT6aPCUEdyOELGSmKvD1HpexGGyuaZSxASFDvVXse2xZl18FKeNch4PEijJGcxuBpn6LxLvNOPf9MOsBKjzeS29sSoUkttDTPsYIJIuWE830A9sOndWKdOH7TgOjBhoXpi0NH39qpzXjV_D3LP9uyCuptVmdc9guynSuQgmcLt_cajEUj1KwS9cCu4yKYfaeijlJvwY_rfLiN9OxmugJbkA8Srce8rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPrCGZGdyr_j3wmVJbLbq7s3dWPDxjYE7ebL8NgkDIDYKTTV5DcN2ha4q-7BDRkAVTotDliWL5Qnp1251Fb5v__sZvTGIqLQ_AnJkPn5JdA6ymEXQvrd_hXHh6FrsHqXWKJdyMSz0V9lZRUkQ3dZtuHeTcnJdJvFtd_oah8WjS9-1pgA_CGB0G_j5Om3Qx5OoQouObGVC4lyR18TkV70YvZgvibiqiuquqXDeflSPR2f9Elc1rEdRYV3qOYOYESrfYCd2X18VotDQGJu2-3tMZoXbvBOH3Y3GGvJJlx3b_yCqX19NUe-_gIBKpmP4h-U8wbWQ3Wdgi6xqRPgtI8gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEnNd6Njl_mEBGsqUz3YNMSpxoLLwc3JBFFR1z2kPJpspUQz8z5jYUpL-wU_VmX_o7BkmHmvZW_O05wTpSIe_10b-8_vjif2gJuE6fbGc8Ge0tZxCD5-vuZdw78amGD6KaTTJPL6JmWLH_PSl8EuXqfqsKYSJfRiEs-vW132G5JIDGbgMp8Byz4vRDxiO-UZjYMSTwY3NbT4r5Uli_XRIfJcinyILk9kAcyyM0miNhORpexZ5fhT2NiqUep1zoB_CHMJ1N8q4-tiMybpSNdJJqXQ_nZESpmuz1yS1lbYsyxwCFz9PcvtvHEsRcZWxvQgBg1bNgjQXDnJDTagC2hNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kes5aBfcp5ghm8vaKcdJgciQYJxB_zJTtvE0Yf6Rb0knyTQraMe5wnTsXg1cKI35aNhQSm_jwczjnP71vuLfBajV_Grym_i7xeVCdhmj-pb-VJCWDv8JX3EwvXtrC_5INhaM2vqfUj7bwP_Pe1nwX0pVb9BhBkNdYDzCkls_xkUJbQA9Ib5569s2ke5ApBl8jkvGCjE4q64ahX9rZABU0DNJghesCB47fzGFn6Cd8koHwObHAzFTNkfZ0uqVje5Al3lL9jrQOhhrmqZ_E5qgtGA003M4GO0bHwM3kjvY9oMHoFJ6K26ysdfQ3ruKUEVI2O6-0qBpea9Vtqu_TT1pHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XSq1ObqxR6jLCgEXqnlqS0CQwHiJ155rixrfNUdBEravKiYmvc_tMlzwQc5qnPVAUV-K6-XgiJkHtzlO6POymJL_UoYQF0qTC2AW2XbtiYurwiJz_gggAMH30vWvCurDIpy0tBCXeDQyp0g5EZCnyWgCN9JZbTlEh9xvPapWZYX2mQtdqlfgvx7P_Mvyb1FHjWVzEQlOCHQj3M6gS_TOQxNjbJP46tzJGkLNGi-hUaoa_4EutTm4b02G9MnwvYvQ022r0jGNmEhmDGC572YFWjN3CxzdkuF4Glj-qxqyX3AUtNjdiSqaZySGP-2CKYIRYxXqpEUo7ARGf8v55ayskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCEoINIiNtntRzFlSNKHGJc6hUAe56hE-5-uegx06AKcYJcFPgAq-cej3STf2HSuNcSq6CJYAdufr-_srMJhiIj0QBprO4ZdP7lDUD0p7SrqJZrvAvlYhnW5jgQjyGliWlaGgQ-a7lAUr7SWzIeuYwCJm2qRp154yOvcL3H6RJVsAyxzOmfn2VzXxxYa05Llv8OVvDzaLteFSHwwfBbXNlsRBmoI8N7XidzHzqYiLI34ZJr6wd2hKHlPK329Hz9IdZM9WAL2Nk4uM3Y6Rz_C5fB5Zrx_3Gjlk6g1jY2_fCCHv0MPCQzKfyhOZNKRC45RbkyWBY9op3m-IS4d9H9KAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OLEJWeEkbbLrN31R3fNnO_lZ8Ex9aaXZVukvgI7M2LEY6EjyPD6a2peaOfzu8rHVeCmDKStZhzOzujsrC_SAuKa_nG2-WsstuUdd1RC0H-jkgFy9bZ7efjRLGIZU93g5q-4Sln8X2liC1fM27kR-42JMxgZeu-HSrJU1Q8brQGmF3-KtlQik3V647g-BKG_sln-D1NOuLrKPfjMYxfiLYf9KrFRA-7Pz-R-vmKZUw0ey6B5R1Dz9Cqz9dTXE-oeMIIZTsOV5ZwWyZFs3B92CXdCxonUL0lbfgDKfAbCrASHW5D0Z7IUgkig-aKZl4YQJtC4P9mnLNDm7Hs0eHvUAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=tG9PVOykbdYne3QD20gNfInwolBlFfmPJPb4y_jYNkZIfFgj4OyI6ZyIXqsqAF0x-4eDdN6HmCAr-Y6WRafIpiwM55Wb4IuK0O8vE40KZUEAQJgMOY7f9WHoT8UQVdpgzo7P_AMcNG5Il4fPmQ7xG8ngmQsvQtuOKB-UtasHYspViNGvmo9eVsnwdbd4e-lmTxVAC5LOUFYsAM8LllSW32Y4COei9b2ek64EAefHyNDVFpZ86mQy-M4ImMySXg_iIuQUG8iu_ZYQEUu4fehrZW6Nj6sVE9SBa7ZehcWGKHY93URHZCsuvoZ0oFDNMJwJc_ctA4Lr1amNhSyhV2H6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=tG9PVOykbdYne3QD20gNfInwolBlFfmPJPb4y_jYNkZIfFgj4OyI6ZyIXqsqAF0x-4eDdN6HmCAr-Y6WRafIpiwM55Wb4IuK0O8vE40KZUEAQJgMOY7f9WHoT8UQVdpgzo7P_AMcNG5Il4fPmQ7xG8ngmQsvQtuOKB-UtasHYspViNGvmo9eVsnwdbd4e-lmTxVAC5LOUFYsAM8LllSW32Y4COei9b2ek64EAefHyNDVFpZ86mQy-M4ImMySXg_iIuQUG8iu_ZYQEUu4fehrZW6Nj6sVE9SBa7ZehcWGKHY93URHZCsuvoZ0oFDNMJwJc_ctA4Lr1amNhSyhV2H6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD5f5GV6vFtnMQkUETUpTDJjIGuUNaiSqJ4lVLYrv_wqvCPDiZO_nryZM7X8keNmIWLlOrkpU2jBqe2DbRVvSry4sahqIJ4_mlnyavougPymMAlwwiZL5Trba9qfkaWVpoQExtJsuE-7f8Z55bOugUj3OJgyGBerXMI4O4l6hD4omB1keQ50XX2FN2f810gYYJ6KVuOAtY24ci-ZxO-D82UfH5-VVIKRz5B3tgx5qVL9C5YUAnoOHnDr6OX9qe72Ss66BuYgG5XNFf0tO9oPKwsrMbbcvojDTlDmdBWvmm8CD00NSkv07RPHBPLkcFymURNrpGJFe_m9QiO-xnJxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQ8RKgNeD_ERq6X7NKamKdjBwMQE2Q62IAkCIIOlz4Phd5YBOepXxuR_meuXWER7vqv-cqKoF5FEceC3s94YIlHBShsU7r1Jt28xdAYajbR_DL5NuI6IJ53nBwBgRFzrKlRQ4_3KQo_0ThPqOtaMonUwBs8Zczl4EnHC45S7yCm7Kii9iD3b8HuVP_6C5zYy9jYk7zFg2cT7JW6Yno2t6oZffc6HXrQwMXH7KoLrrK-6oNXDvwA9VTUpsdAJlcwiuewiL0KdrieBeXrVCdkIFI99RBDhgdwa6kyWcgSNgGHwMYFz6yNtEHaiX6-7v9JHNyA73lW3tRdm3Us5JrYsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-UH-ail4PeDEsq6rjcMlW7xRgwyglPkzxRdMjflfXv36f50kE3e2fqYMwk0Jzfmvqw0woxP3H7TOC17y4I91I3zpkW_ks5yJ0Wcs0XFgUJnTUrw47YAb3JYVGhVQHd444s4_N24TDWh_XrDBCFEPLEmncTXSAW22ui10Sljj19ON05GJWuNz-TRzv95mZdbpMnFxrY7xouCCK8g0zmZ1GUvFcLF8FSIcGdL8Q5hpRPjv4-QCJ-_xUkHvWQidVDY-hTxmi-zVcDLsrYtQFoyyAyP5ULjwhZ1BrtI89ejNWugnZ9ASsmCl2RTV2UOY4Jn67FxFifRMYW6d-L4bfJdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fm6VKLGAAWazN1kHIgaZSgBojM0R67msoNTTQuimyifztMPgp_n67Lzolo2x563E4Xd_pQl-ZBOVzo8uN5a7PZUgF5HyiOE4sgRU1pqb4iOm38xylnK_qT3rzns3xLPqROsJGZx4PcJlGzKBV-NKtlPTFWntjQ28LQ074Ul6Sxc2fpeU1fvE_Lg5mFlw1ci35ooisxyHqXgpHJl1FZX1yZIkY6baCvlgU0sew9xVSLlfLjvKa9ODqsHU0IS3a6hiRFawtCR5uUfpwE955gpgEVSAkBVN76vj2tJTT61MfVEGHzIjct4mTuig2Wa5yDElEz92CbW4i7hcaZC7-k5ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZCnRg4NU5PeJiQK7vCgvePD5XjgUG4Fp3U_Yb-MQMem74AN-ZTvmxVSbnZ9xF8SHmxcnXEQqJj4jxW6aAfwUoLVN3QsikgIVHnkpwcFB0uObtXbc1gtzjZkAg4mRKjDvEelUyQJ8aYzpSSWPc3_9W3IHRh2vdlfWBP5HzKYfTFuA_Bz3vEMjtsnFvYwOCFjWm7Cp8iFs78iDRig8k7oCPjoJWlQTkLWPJNgDOXgtcqtMt8iEFQEqG0brYT77XggVOINYh-ZcJ7dV6ULZTdKdcMDgHvlxnhtDoHVla9QzjnKKyOsiG0RHI7LUobd7r2cP3wqvuGiPQ7BURqiiabygYUk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=CsEIWJ7KZpaAf_XvSEH5tGGY4gBqyuJfEyARLIbkMMmOS8wOy5oEiorkJhSac2RbAjcBkNnutUbzlitMZaviFp7jld9NY1sV04qfSaj9Crpn2q6H4IXRNV1nuTt72AaZqx6OZx_7GgAxSOodNubVrJaCfKzfcZ7xK8j7_7YC_TnlBuQngv5Z3iov2XT-6LQpS5pMsehZAmnEXkF9s1B3ularIU2Whlm-47N9JTQHNH_KEloKqDUUZZ6r4rjNcydNoys59MGx1AypV-BiCLUA35wfdW-exvaZV_hZlBvcfNO6Y3PLPaWE6ZefvuojdxXy92QJdysrTVZRLrP0E8n9ZCnRg4NU5PeJiQK7vCgvePD5XjgUG4Fp3U_Yb-MQMem74AN-ZTvmxVSbnZ9xF8SHmxcnXEQqJj4jxW6aAfwUoLVN3QsikgIVHnkpwcFB0uObtXbc1gtzjZkAg4mRKjDvEelUyQJ8aYzpSSWPc3_9W3IHRh2vdlfWBP5HzKYfTFuA_Bz3vEMjtsnFvYwOCFjWm7Cp8iFs78iDRig8k7oCPjoJWlQTkLWPJNgDOXgtcqtMt8iEFQEqG0brYT77XggVOINYh-ZcJ7dV6ULZTdKdcMDgHvlxnhtDoHVla9QzjnKKyOsiG0RHI7LUobd7r2cP3wqvuGiPQ7BURqiiabygYUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hg7HhJsbyjrEikOOB5cZsHHJ-mbztzqDRevHlrMxPzesM4bFkxjvov3QFM2KfmaPbZfrR_AW4LDXxezSxkELDZFrmTBs7JvdLOD0PCzPOESsotRXHIe3-U1iRYY71ZGTlvdsGfD3O20qJ3BDAMCaEnKZ2t5zPQqZgSVLhkb4q7Rs1fFKR5My07iKc7sQ2j5DwmeImLJ1qgjrsk2iVQC5KWocDK09v-6b0DhdGykcAZI7Y0MvcUUu5wwgMo7P8IgGTh5SUrkFcZwenKEBVy_XafesQKSL5c8C15wRFBaZRTg34lUU2hki9r1CcKQR-_tQZ9uY8zet27XdOgQfvscOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c60MY6Nf2CPKlhoIC9eGm_YzPfRRqICTaCBKtlicAhKEQ84hEjfziNAjQrHt0jrGGej6fB2ftDbMAprXP1Nn6jrCOXqLROYRdRxa3b_m0eJ2fy-X5qTgzKTEfynyCkldfEB-rfWlL5KD9rDRvzjFbxzk7RTJuVAZUc_bSbRvLNbkpUiZWTovXLVjgsuPpf7gog1_UpbcayBh5-zADCjWGD7Ra6jC3b-c5pTHd_NQ6aXkSXJKEAeCo9axgfo-Yjw_nXrb6BWZKa4LZZhJdofKePuycAySc9MaIzl1wF6sdqbHqrMRp8AMVK0OP8kC7QoMJGIZHJAMrLkHbZyWnUGy7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=SrpUe8u-M6lnvxEp0Q1pp1tw3r2pYoQ5DqTLH5JBUDKtDu4ARb29YDA6wlYXzZJytWBTcs37LExtF1KLc2VKIdNv8lUxs7Lj0HHHokvW6nmdtFaqQTP1t5vZsMY-pyMMj3t3P_YoM_qN6oRjprK5Wk9seQuornm8k7qjZl-80qydyvIRyPiAhxiu1AM7lHETREljmoJxN5nFSn-1FZJLJeq0I6lfky8uybScY0VGNIaTz7SSWHjfXPvJZF7YN6vbeh6oKFLe7ctZD21ATzoO6akLsMy6eEo3rslSbAg0imkqtR7UDMnqRcKyJlAWsp9RUDmrbFPRYhFNbuu4DMFzUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=SrpUe8u-M6lnvxEp0Q1pp1tw3r2pYoQ5DqTLH5JBUDKtDu4ARb29YDA6wlYXzZJytWBTcs37LExtF1KLc2VKIdNv8lUxs7Lj0HHHokvW6nmdtFaqQTP1t5vZsMY-pyMMj3t3P_YoM_qN6oRjprK5Wk9seQuornm8k7qjZl-80qydyvIRyPiAhxiu1AM7lHETREljmoJxN5nFSn-1FZJLJeq0I6lfky8uybScY0VGNIaTz7SSWHjfXPvJZF7YN6vbeh6oKFLe7ctZD21ATzoO6akLsMy6eEo3rslSbAg0imkqtR7UDMnqRcKyJlAWsp9RUDmrbFPRYhFNbuu4DMFzUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=IboAxSPkF99X61lGOVjE4FjizfWeKsipr2g2zzdngXWplJVJ0IWtGmZ4arMulB_4GWxPPjaRjr9JOZoTIUc9bcZoauC9HR85jUXhmeb9mUA-qUyXRmVGMa56uFIdtDedFO9y4hCvjUlw2thNU8mgjdIMuIk5N1LuDcYR32mmkSVG-F3kUO19p4f1YZFSg3H1y4JaIAiqjqlPvImPcUa55a01pvV1-cDLCbHg4mC63zhYax2_VdIDRi-Ad7zQT_hZQvSQzCXY_tFobi2E_ZaTttpRSUTSzOVniRIbEo7K8CflCBAi2TPpNFnryIBRu4gGGkD8Bt_dDICYCS71u4ASSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=IboAxSPkF99X61lGOVjE4FjizfWeKsipr2g2zzdngXWplJVJ0IWtGmZ4arMulB_4GWxPPjaRjr9JOZoTIUc9bcZoauC9HR85jUXhmeb9mUA-qUyXRmVGMa56uFIdtDedFO9y4hCvjUlw2thNU8mgjdIMuIk5N1LuDcYR32mmkSVG-F3kUO19p4f1YZFSg3H1y4JaIAiqjqlPvImPcUa55a01pvV1-cDLCbHg4mC63zhYax2_VdIDRi-Ad7zQT_hZQvSQzCXY_tFobi2E_ZaTttpRSUTSzOVniRIbEo7K8CflCBAi2TPpNFnryIBRu4gGGkD8Bt_dDICYCS71u4ASSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=Wbwj9DbOwFhj4NzdTJlS-bcj2iY3oY93P_-qb_p1dRCgU-m1AONKC7eKHoPg6RrwGgw5k6z-6TaPUwssaENNGgP3YCbvAChkAYYd1dQg49CeH9fv4kIDLbCfvuP-f4SaGYfW3AWGyKwSoAVWiPoE8AdL-3KJ6lefbIRi1ofsiYlKo1sDZVTamHLFhlTZa7OLJo21SvrM6gF-ZryuRTe3WjQMKT5K3x8VoUW76L37L45t3m9mG6WcjfAJW_HdMGi_YrRnXGGWJw0jbmLHEemrue3tSXcN8synaqFSbqfJTNFCHtcY1NNf9-3q9ZkWbx5R7VLEEmdOtymhlexLK9Eo-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=Wbwj9DbOwFhj4NzdTJlS-bcj2iY3oY93P_-qb_p1dRCgU-m1AONKC7eKHoPg6RrwGgw5k6z-6TaPUwssaENNGgP3YCbvAChkAYYd1dQg49CeH9fv4kIDLbCfvuP-f4SaGYfW3AWGyKwSoAVWiPoE8AdL-3KJ6lefbIRi1ofsiYlKo1sDZVTamHLFhlTZa7OLJo21SvrM6gF-ZryuRTe3WjQMKT5K3x8VoUW76L37L45t3m9mG6WcjfAJW_HdMGi_YrRnXGGWJw0jbmLHEemrue3tSXcN8synaqFSbqfJTNFCHtcY1NNf9-3q9ZkWbx5R7VLEEmdOtymhlexLK9Eo-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8ticrqETMKQrIRVhVZq1wE0_smQ3OMi_H4qRKmHcWiCFJtbYoQA0k7gqVnneH48cLjSa8mJNgSAQrbB1spqKUSStMuCkgi2VOLd0OrDVCAm6Q58wGnVXTu-GuxOs0mW0I-q2DpDbkeBgc_EDDzCIywGniFaki6y8Hyz4OvgoIDVV8_UBAABBHwxfuTcof_D_iKJMoWDVsGBibYjVU0a0MTuCO3NyWedcZrBnDWr5j-Ep8ngdA2V37rmUXrc9prGUKutp1R9MrljJg9OJirYFRd002GVqFSJOFKJrayrEsk14ZwGF6kgpK1ABhMKja6z7PAdCQ2G-nM865howhnDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYqt4FqN9UFfTQnYfqxz-A71tcbxKw0wZfEOyIrc5hZFQT8cbChg_LmiaXbrW9BZKeo608LZGfeW2S9FZ3CYFZoUGoB-8QqYFpIRrWtEuuvEJLIf3Cp2N3WwcRTAXl1W7OcHef-fhexb5l5Dhch8ewd5cjKBU9KReF5BkhF9TVKO-RZDF5Mu9ktzyNM1rQ2SwMLPyB4e2qanjyoAXATyQ8EwY59p81mEtExhg3xyuk4mv4blLCJQolb3ps9TpqpGwGXrqly55FiHxG3SPKsBM2QC4c9Lh3rW9Y-IpGCzEz_GBxnts8dxjwn5FPXriYzEPCKlkmNrt-_xBLjT9LuZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcFmef-Vu2kJU6H6L5HHaJ-FhJlTyB5NHiPaLOoKvHeSJh6r2hTuESPqyIp8DzpkZmkAdiG1d_qIWh-Enb1lFZxf41deH-YkrC8xqoN3FX_xhRj6lwurBp7s0GVBrQGyHRXw03jhzZ_vKW5uUnSYwJ-9IMTr7kfbeTKY1Ne27tSQZM3N01tnm4mo2GkKlsm-fPXf0Z8ZIJKi8dsxTKcpIfUF9ZPOnhShKxHM-y0kluHGFNduUJp9vvkMY7P22PagbGzKrmrKqa_Mora3zLitCozhCFMr7jHi1hGBExFL23vyeHoVInQ4n-XA8shfYzcpP8g8w_C_fvOPv9hDlU5G-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FWetKNzgecKz2gmtNSRgIkTr4-dGMZfSBOyuRUxyUAOm-yf8VbBlhQHbQKdBc_c9ljAZM9qTU26NyTW2ga4J1_bdeXqaYKXP2222Mc8IQRJKKZ5gs3IxSebG1HZfHcEnkY7YMz8Jvws9dzhZ9i2oPhAg_20WiBTsx6X-fWk3_UgDy0CAAVJ2RRj8NNRn2hmMjOKxqrDw6mLyejNlG-NJXhLN9ThI0K2G0j-sL0tVKiSobv8WIcWks1fK5mWvQHNeMdWk88ry8NqcxzK7mH1FxTdIoGnTJHxQ4Cw7cVgepoDoyux40agR9NwvmZlSKOjD9CVmjj2hloezeZhE55sPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BliCZItKLB25KkcAl-BO_eeUNBiiHikd8OMU9opGNm-9WLUfUd0ya85_zRHHWK2GexDD94zWUVDGutKIgMpTsevK9TWF5SFvpfrIwLMdPIgop2NEiULy6gggjtzwjkbqozVPY9uo3kmLZ7otGqVC3JP9xSGm4qHQSOZDQ4taI3A7nQy0q0iHUdwRjdFCZAk9y_4ZYJr5EOv97nEL_1kATul3jB1Ml9cmQFmzbdjuFn6QakvMoyKPTpWvWiNfJVwNOn_D9vudcGCp5mogzrZh5jttQZfWUt4y1u1m5sDfbfmpnPQAHezsfLhGMOtIsbxekUPm4Cowrjbs7Q1fRuU7Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PkIoxiNNeRD927H7Ff8DOgtM6nVrwxnFv0UOjnMTr9UVyP1lgGj2k5bNNuL0qH5TqRlMoI4Hlx9k9WOgoJAEm9RApMlDSX8xh9zbzr6kxQ4ljiaCnB0o69sDTLnz_kWvFkKisKCqpWwdw_GKSe_UYLvG90B11lfqmeiyv1Z8yGK5vdMT413Doj_QVqbkJUbwmWHnSyJVR8Qx2LCKMiO7WI7FU9iTHuMDUVt7Pm8hfKC6Kp46ewjHAGrAICsuRCHTxl4giBqmckf8SOeq2JEXI4Om7Cr3erfFfeg_ZC7Pi_jo3LG8xrkPvrteWJujiSmVLc_dmHb6vEUqeLfxb3UxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jesvkvCzqtzwevP3CF29IaDSJUtGdLIp9__3fqVc8kUO48YpwWJDPwD4nm6OAfmCL0MOLoZi7eMUy8oFIpoOK1QK9BzzMaQoUvMaypS4SaqEnTlCtlm93n4EPjxfCzF_sm1SOs8Ho9GbfNeQbcFzRRbeaZC2tWopaVLlAWqg-EPDapuT0CGew9nf3Yef3YMw01Q4pj81uDbB3ANnJa4B8_2f4QExkRAeNpbncIlcbJp_rpqAdXsdDmhOI9LwG7jVANOUo_x7HhUVQhJlgogN12Bl4cr_WJ3P-MLNlevpwocu9jcHLAszRYQn5XruMyeF5ZsayXOn1ZTdyWMa7jAb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ei8XhG4ROTmOp6rry-rkwnDOAGdmbdjJuwGUkkvZvbYkA7StNZtCTDqPcbSeCFhFJr13HDIIUbhupTPf3ROvkfDZ6TkYSKcykdzIMKJvJLPr_-iOUOPiOHZonb3YOHTyZOweq8QJyTNeNdsTpzPK8y4Deqau4l-G913JJvBw3l5Hj7gP3bOTttCMM6kPVOybLFQSa-fBfNQ6CS5H5u-2L1W1LPZXOim7e6nh2Xx9v-zWQIYVcWmqTtABEnygFUFRcanqgp06tNfcR-3Qs6m2_d7m1YypfxR8VDZM0DHzTP02EhOAb1Q8KnDVPz1s6be3645UfupURzP72Rq1phVymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/slAgmBEbOeQQdz1u0rct_PiS3RDEiTh2_Dj7Lwfd5aabJ4m-rnmfy0gUPyJzziUoII7qodk4HZf0CsKHNEaw0A_9MkJZJZ252HzdYjrRix0XNWS8hBAzKNHOQeX9pNNnozfasnVkEgMzYJcZ7oIqFlVUUhxbQrXOcqhyFgBaeTY7E8gvtpy1gzTAeEI0oOR4XzRsa_oDgjncfonK6K7ywE13PIGQao1eQO0vfTYIAm4icr-0_Y5l37snQm6TRU_Q4bORPWJUPon5Q1Teu-aO42xnQ-hZ_j4DyXmtA8tty-0qJYLt8DIKJKhPnbuL9dQgftFeifKEW3YnSTQ3IB22Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cbbIr6hhVKAQfp2nFNhZDJed1oM_TL35FBkp1WUOWZWXsZfVgVuEyIcJ-9FvYbqAls3NCHUuAyQm4w4toLDnNtu0gVVxk7xvWy3hXCpbIv4dy8hdDJG96M9xNTC-Y2Nhf8Yd8gONKosJejGROeEUW4dgwN3P2pySyvzJ9W7F9A02Oe-wuM0Ribl0t8M0NTgHGaZ0BhselthwWbCKn286R8BGe1Akv6YLg2cRRRj5xdOyRUXv040AKSF7tqxCm3Pyu96cCzaYCp0FLjWfl86J5LULAbLde0G_-jNcTliIJGn8zTm0MT5yNLYyqjTA0mMUnRYO2lm_S2oD92CR6_EQUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mWFKsWfw0N4asmQ_Ba2h98vQAL_Y__TJcWWWQkWOLXwvBFbPuTd207AhDv8kFRGrO27UTlciYn2CIbvg8VkRmlC7VrcIJYAYIsmiXazeoAwoxnsuGGoDjSPXq-THhWebgqNbvdXJUVLv-B5yO3kcw8-YIJZwjFNYNZZ6Y7A4tFNuX2FEpmwos_4pDf7tECVLMa2srKjRw4Kn9Dv6yHSV0wGXBk3bBHVfa5S3_rp48siinx60h16SliILrHfZAdJGt0VxH_CTUhavoIsp6YCtMvqG517rp_DhcaexgpctTla5tAf-OZKmynOy59Z1erfjvs4e88yp_dWH1EkV9BIvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iJM4_PetcABIu_csq5dojYexaFEs5Oam0nJwhn8r3wAt-VWKUiWnGuZJdvHDHlAzhBw7u2AxNBHSe3-4fGQeIusLHTj-KLnLnoXk14ZnQvkdf7e6IJ60S4Otd8fkW1nnifT_liB1AiSucSYMDDmB4z4LDCnFg43UP6gcjnQTmi5K6YKQt3lIcImWf_yCLB7U6lSCsM4mZOC1U9Q1UJINJ9zhRL57jYNJz_Nj7IXpx_6Y6xRLqliWFBN7a9fFFqvULUELhJYBvwIxS6qtX1IibWnIX1waI7YcsyeyvyDJId-aeNoF9hoA-LEuZ-jL34GbYPf13uuDHGVV7QIZHtl4Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzWQttjoe_j-Gczgt4cCUPSZCt6W1sgys2Fi75JEbLVod-mBMhCXDIFYnXHrnMSutDKOnf0IsFr3jsm2mqA-TKpC3DBfhYNLGwwYT-EsPNuQQ-slFUo2gasXMIi8yUB2AyAL4Xh_ZrPJkmoNtI7pQDkFiWUGvOO_DPWWVZwdHA4yHwP_mcaW_ial2o5mCD1cyU5s7ecLdBEWMv7-BsnBUIU77vMxSHqdWmYoZQyLKQopczwAF7I9vYqLEjSAq48AFqPGW_UNlz_yxoUj0moBIYNOZO-iAx4B4WfxoWlsR4JtcnJXDIK_jvgEUc-tA-AGxLpTbvfOpcBECP6FEQjYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obrRV30hvrOQ6RzWSxJb21pgEVXamt9nGSmz0qeSr1IKTxfKZXm5OHGrWJWfnsV0KiqImkz2w2s8lQge8EfsLpll0CCk3qykHIywSa8HkwOgcTz8e5ztnWd5Wj4T-d45qW32c6H9Md4om1trSfjGcXpJPsphe6Ct7xqzG5UKftuH4jZSOpSlAlIzu-rKFOoakDYwQWwC-RHtUHzChlqjnecdrPYqNKrCZ59m_VpY6qNHZl2RuLmCK-4EOlsRj8SuwdAq756rB-GfQKLrn__C12SPlcGz_ca53H0yYjvsRfdEcCPCzr8Pv1f6gMBcIWmDNI5ssbdGNTGBhG1CZoTAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=V6yPCDx9AWjfl2evV3_LVX5Jg9q2XJHVqlwCEj9MSffgGPThg_4uJ_aQJ07nS2CNVhV_I7_qVkk6CUyTgG4pFGuU1dwgvTKr605JMPtNfzbwyRoYl4adkuzkzD4lW8w3KGtZjXFhwAGHABcItIZpqDHesJo-zu18ODVNdedAHwLxtoGIeuUoaV0T1PB_k-QlU3ReeorlZDgmf6BEiukUiy_YU_9ap3U1h6wglqTizz6GR6-iE8yVhIPOg9nC-6JnlxhEIDNxGjw71a5csn1WhCPbtE9stUpnMlSvq9SW_MzlIMGKcI1EBVshLuawFmujcCBcBXnWDpaov3rBIsnEPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=V6yPCDx9AWjfl2evV3_LVX5Jg9q2XJHVqlwCEj9MSffgGPThg_4uJ_aQJ07nS2CNVhV_I7_qVkk6CUyTgG4pFGuU1dwgvTKr605JMPtNfzbwyRoYl4adkuzkzD4lW8w3KGtZjXFhwAGHABcItIZpqDHesJo-zu18ODVNdedAHwLxtoGIeuUoaV0T1PB_k-QlU3ReeorlZDgmf6BEiukUiy_YU_9ap3U1h6wglqTizz6GR6-iE8yVhIPOg9nC-6JnlxhEIDNxGjw71a5csn1WhCPbtE9stUpnMlSvq9SW_MzlIMGKcI1EBVshLuawFmujcCBcBXnWDpaov3rBIsnEPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q019sXXJfLSR2MZMGckjqk65xbAxVZk5zrempsIuN05q7ZTZo0LVTSwyC-n2_Ch1fZQLSiJEuWVqgt4FwGjNgvFRa1bTTJW32ybgNyc5Cx3zawTlGlxFR0w1dKm8jyLkZBtQPc1ihId_Rmr-ON1MqYh9QhEJi-kNBm5yTgY1m4GN_gL7KHqLGWPNkqadUFCiYOBwLkJqtiIIAcjbin2vflo1qIC-ma1M-f9JysOx-5RdBo4wADOjyxy22XSL07c9qCs0DGJvKTGgym1rfEjZMt-Gg4zVVYNd0A9xK0RPm4ihzudXudZvho7khXrQNpKg5ssSBEaXZbAGBzHdVtlD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gGX-NwZW4Yd1pfQVX80AIKE87PFsIPgmd_pLN6kkc93CfI3UR3aVXznU9KuK-tcMLxUWfXuO0elYRLxXsCbJW9tDWSmAYEsE3HJTqy4MPUa6GZOV7lXdYWhG5wI0yBiLgEISDgNIDk_nouZnJux05So7hZUtdnK0iOQYxlt3KqOALf6vOFSkWnm9FfZPo8eSd5OEPEL6L_u3QQ7HFpEmun6Xs95nOU4jJb4COVD5IvsPdgPlFK35BHWE-v1PpZKvGu-RDGJr-JQofxTQOyujPi_d-1pqtc3Zc0vf_KUsZCdDBIkwt2pV2mbIvK7ruYwfWh9zJ4LUQG-MObnqgklnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SYiL5Wx98YQcAYYAYFlZkswba2hr9x0pujkyyrOlCZPwngSb655u8Sf74cPsmPYfLF2LkT4wCci-3muOZtmqfZoGdVUqxaL1ilAEL3RbkLkPDdjYBwoe7ZVg2V-Qt6KUUISuo_n8SRtpWGwboLyt48FXwNf1HYsDc51MWtOoELp9S4AgivlBK0tlZlSba8X2TOpBt_mvqlfE3-CZXt7R7ObDCKDc2zDAfJTJ3RpyuSNcWUs2EQJdzbENg1saMAVvKwcRWbU3WT9HCriWkAwpzNqRymmXTD3IOkPlEgDp7ItS-K3xEVknqCIEOZoApat3R7ZTT03u4Igxd7R32OK3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ukETW0_9I2vR0iTnAWa4M6AcntsKapXwFYcug-fFMdbZgr2Q1YinuM4_ReD3X7sZYoPHnxv0v0tePAL2NI1LBN9ZViYSacKJhLpwl7vHeXEttNcRhupC9E0nukyWbtgT2r8CSoiF48hGQb3IKbDELH0SC8PfsqpnYSM8rYpNwDka9_pHNCQklGNJp8-pRmn6Fnarz46piNJ6jApnlekAznhqQEPmd_OyW0TO5WPSI3s2uOnhz7Bqb3ROyu4MK9Z4TDeylRAGszO-7Wb3xZdi6fvQWLDBMq8wVmj35jYsOMtzhlmQUH7I2WgqUiHlytxATUx9wM0ZMR_Wzm01eZiC3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b7zxBM9urdaPBUzxS7rVnu0gneIaU-iw9vEPMz1b02ih29qO8ILLQq30c_qAcdfe5AubCDmIjWzpYrqBCYAvTvh7lXDpVtWcW-pC0Wc3yA3iXYZzMGJxEi1uS8aDlbJnQL_0FgDzWO99WlBQlMVsYZqRWuIB_uf9mr-S_iA_HD7QyoYoCXedhPIOonzLNNfQYVyVsyM2UmaHw7qwPXF8t3EsOKjciLuy4FMfqgPi_OTTJwWTerxIzWsD71yoDtUZi7fCvZk4GHs_8H9O9fx7U2r0LLhTACbIpkH3z4s5Ct_6wNhP1s5_bsCDfB60gxJQEfcNOTuflYwm-LLk_HLHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j70naKoXLBnqTpkO9NvxIo0jJDmO93eNSndSdFdpMFUm1PpgfK3m5dFPRqEvb_zY2ei7Eu-SvAfC6ZmzZVgF2HcZzBs7x0xk4iPyGuUUZMmzOqO7pK2sepReWwdJmgj10vP54qRIWmTET9Ep1bMNiHc3JECpHZQS2thlKXE4rMjErQt5NjPZCJF-Qeihz4huwpien3LATglUI34AMKYEgpVFaVsEu0UMqw5cUzG9n2gCYJ92S_4lf8R84dTVTg7Q8sm9vKbCgYSa4sHzty4cRchLK8b2JaFSv0ATpIibj3aSqdyPeFjZ0mx6iNbJmYnTOqf2pJyCD6xPs5GzJaktwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=FrJ8owXYuY2oHOORo2J0u2Ypuy6VHmInDbXZsyTOiuPvgaJeh2Hw8Zwrjj4ETbnM6SnwAtES5SMxgsisi9J2tZDEp2elt9yH78KqF0qjnSrEHlwGshIgVme8IOeiEVHYw_tTSBysFJRfrfJF4DZ8e07NkR6Wd9CPcEeoie8RNaXRzkLohHbBbdFU0WvbP0OX4UiW82GNNSu3kv3JiPw7T_0CJDiW4c4yS1hrqy6reiRy1KND8DJglQEoECA_1SBvyNGM4HXNLmxHNgDGINXBPjydbv4LaqgNIOGeR8kLhHM1yzGlBeWWLF9HNku2ZcmhHvvgYleYB_sjSrfaMHTGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=FrJ8owXYuY2oHOORo2J0u2Ypuy6VHmInDbXZsyTOiuPvgaJeh2Hw8Zwrjj4ETbnM6SnwAtES5SMxgsisi9J2tZDEp2elt9yH78KqF0qjnSrEHlwGshIgVme8IOeiEVHYw_tTSBysFJRfrfJF4DZ8e07NkR6Wd9CPcEeoie8RNaXRzkLohHbBbdFU0WvbP0OX4UiW82GNNSu3kv3JiPw7T_0CJDiW4c4yS1hrqy6reiRy1KND8DJglQEoECA_1SBvyNGM4HXNLmxHNgDGINXBPjydbv4LaqgNIOGeR8kLhHM1yzGlBeWWLF9HNku2ZcmhHvvgYleYB_sjSrfaMHTGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bqpjoVyZext4jQVFVjOEmXgjAMVZv72TIDY4D5LMnesXGr-ykq6IGsAuycf8xtx_bdcypGcOnLLgMKaapvVzOvVnQEc-yrQvfR-9sazOVeVDFzSawd-mr44bsZDMBmB6nhzRz20l_tKMTJk4Zp2IxYSFCB4ZUgnfwFwk1-NYF6fhBNmapanDkP9P1Te1AiJzLB4E_PudHbS64pKfZjV1IHOudj7UgY_Yv__Va5eDL06rq-qpYeMkYbm80uBUqyCvi7S474UMVNQxdhKVak0LFQS1qxhYuWVLcq7Hh_T_A0uBJy4qOnJBMgDifr3x9Q2DilWDhkGWfcWu-8yensb_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=DDEcIq2c99VzKiIosBjo40x5hJrOVZAyZjYAaOHZt6j0s3wwiyM5280HWkptmhS5sV9WjKHUqxTxaiGbwdeeqLdzhdzcyx26e6XRKfLaONea_Oc9atACKzhm8XE6l26SafgvcinIL3IdZwPvRaOvOFtl6lA2yAApmQP5FsVlEEpgZJdOg3tQE-CXibdeHplCfJxMxY7RiuO7vZPRkfiOOSig2-tVuT92DFpGbX0592YDSC9jAlcwYRtHNr-jPpwebkbmoBVTyXsX5uHqmYUQCNSUFkqEwFfC2YxYuS6GLq29SicfN3SYmJglWcBgBKbp4A9qfjdqmo02Uz-v1lpVEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=DDEcIq2c99VzKiIosBjo40x5hJrOVZAyZjYAaOHZt6j0s3wwiyM5280HWkptmhS5sV9WjKHUqxTxaiGbwdeeqLdzhdzcyx26e6XRKfLaONea_Oc9atACKzhm8XE6l26SafgvcinIL3IdZwPvRaOvOFtl6lA2yAApmQP5FsVlEEpgZJdOg3tQE-CXibdeHplCfJxMxY7RiuO7vZPRkfiOOSig2-tVuT92DFpGbX0592YDSC9jAlcwYRtHNr-jPpwebkbmoBVTyXsX5uHqmYUQCNSUFkqEwFfC2YxYuS6GLq29SicfN3SYmJglWcBgBKbp4A9qfjdqmo02Uz-v1lpVEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSnCALygpTJPyUikwG4cSp5ht-kDfEQZbgDUF3bfc_pSZRmPtj5yJJ-89cCRfujsD3zORVNHpJcMo353Wl5YuFsk5O8Rz_S6YhVG7tubd5VBhQ1PWV1eSbUXS2e6s_ydCX2X8TLFqHz2ueweCHgmW8iyIwtzdFwa6dQT69PXQ7msE3RrrU2cV3_rlU9IJaKZjswMg8x6xA824YqUkMNZ8GH5f9m2iPdN6mJWWlRajlasMz75H4SgSbh5IBuI7kKRw4Jhh1vRHpp7y3dJWqC6D8vsFQA6Sbziz3fehtJslT3XAR247h3kD14a-XJTZRt-JxWNSeaWfIXbnpSHCTChlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jdqVcx6peKlT3ak0BDvZBoMxGvqJbCX4ullszjTtCCAQaqOvvrOA7nMFTw3xMKRdRg3FovuX54_e7WgMMFTvRIafCa5xqUXRRF-8fQZQGEIb5PER1nU5mbxbs9Iis29Dq8gOSjhIByWqWOl4PPT-2epU2LGJoAjpGKCrQJSyvmceAttxqgaGQ9WKniY5Ywk-BU7wDB_tf83URxviAsb119KTvhR9roIG4fHAhvkI57fj3OUfXOP7L6vQThfJ1ss34gcK2EFrkEzMyDxwT5pDWFs4x6yR93i266pDsXqDBfzQ09OAK9NNflJj5FTnLMqBaV7CqU8iaguxq_3cTHMryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XebAPgvKG6G67cbQziKvRlQO58uBWq4aYt8oL1kSRAE5bxZ8EgHCYDl9aA5Awa3w70JmZQUjAH-m-oYS9ed_HGMpo-GDdJFPFSOKImRr-6Pgc_9g00uCRDmU_xhvFZpLOWEn01Mk4Rg5EanxQnuA4Y499EWRYoeX2H0ejfVYKzrnt1lp1TX6kEA0yHi4m-YfAEYGEkc9OerPO4lZi9FcJCd38JpgOYIO0LnVTWxfvo8odoyhL7lClE7uIDDEhT8aG2UEnJPAodqVpeKi_r0EQiNqOzBL5PtXpCjr9uVs1nipgDoEwFahq85cPYelgQQZy_nYmKKO8it-la8im95kIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwcfQGNhgKacryToWKXjZPo1l_cvBXi-oHYTCxmBn8p95WcT8AB7KYYUWbR5wQnS4l7qurbcLAOyiO0PCX5xaPVphtasx06K15AnS88lqz3bDoiqEgc1DGnxz-QBlYbRR4_jZ9EQ3o8kBwCAnBmk03GSZZB144xtoVrsdGjgXco8SQXonGAy3DDCb4tPcRbVYlp-Yg5HCAzJXNrjftmZlbT5F0T9r67ZZWDvkbAnTZXIZLY9ApbL5ei9q99sQqrCQJEY59KTyHFRjWd4OgDeelabT20RHs1QwqPnLbWtXb4ovQtR6hKcFnDtdjXCmuJBFxtioNbDsxbaVVmwOwtqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frgmRsFtV95hGPskYD5ukPJOkMWR2JHWmEMKDvLLT4fYjAWxMI4aePQXEIdOu5YkOyOwTcv_XYO1DzMP4FgqAbAIu7jnHaPpLB4M0cPDWTZPH3uTT5jX8Asy_5jvfxGLHYXb4U6x8py0roAP0l9L5D3dspURm1AlPFXqAKonrJiP4iGEq6IUHUu3kf-le1alRVNSchGY7ft8x-9Y7fN82m-BVIRBxf-zgfn54rM8L9T-sOCuQPq4KmB7FRlg6wEhwORp3hPN35rmhJUKag9SAc6bpGiQEop-KLDpd29rTlLPbzbY0B6Gv5KSWlAe_k0WgixSo5t3aFIXDcBfOp3Rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=uL1q2y_pFk5hEcOFUUYe-jCQTU0u4oHsXV1NHHTQQWqvCitBcrdoD6t_I-1ttkfqNXsvxRkiIDDGWdRVPxrYWMkdQjOTWHqkon8v7k5v6ZlEcJrwNlt0KnPEGN0howTQQ4K2Bs83bzeWuPb93mxRHImoyLxnlqroU2ICR2DRtldphVtG7QwFeiITfeijDmrDsxT6LXenAHd_RbRSpSjPbnOGPq0PGoDJ4I9HmMXSr0qkjwmTRQOh7xVbmksX-AR_PyYM0PJvw7q3ndnubV2tAvGd5DI0G19g69clC8w7pV7MxPbSdU36JEa8YGynKnXEVc6QK4T_MOTsehRr5YUtP55ZSo83WCHWsJQyObsxUIKoFy9bHRbAzcNIJk8SKRmUDf1n87mTHRjZqO_z7GoKBW2mFm7y71qBZ_m9BRHWCQyoZpohOXlaDmUTI_4dQb-9409OA5pAK4BSFrWZxYMoiefS0Y1LhDuUj3iODGI8-CWv1TSly_roZprC8ijKg2pnO7AZ09rOEujwUGGmYC42CCAWoQudIGqtLxriwKUDd1IjfmRCN2riesNCqUzkyXPc3dQjG-nVYbSYLNMOLu9GOy54twgCJ0C7rbEYFRBAywZfj2KSY_foh0uOWwAYUL7C96gMCx1KbSY6ovPxPNcACUkgbF7_XwOmH8FtFhG3p5I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=uL1q2y_pFk5hEcOFUUYe-jCQTU0u4oHsXV1NHHTQQWqvCitBcrdoD6t_I-1ttkfqNXsvxRkiIDDGWdRVPxrYWMkdQjOTWHqkon8v7k5v6ZlEcJrwNlt0KnPEGN0howTQQ4K2Bs83bzeWuPb93mxRHImoyLxnlqroU2ICR2DRtldphVtG7QwFeiITfeijDmrDsxT6LXenAHd_RbRSpSjPbnOGPq0PGoDJ4I9HmMXSr0qkjwmTRQOh7xVbmksX-AR_PyYM0PJvw7q3ndnubV2tAvGd5DI0G19g69clC8w7pV7MxPbSdU36JEa8YGynKnXEVc6QK4T_MOTsehRr5YUtP55ZSo83WCHWsJQyObsxUIKoFy9bHRbAzcNIJk8SKRmUDf1n87mTHRjZqO_z7GoKBW2mFm7y71qBZ_m9BRHWCQyoZpohOXlaDmUTI_4dQb-9409OA5pAK4BSFrWZxYMoiefS0Y1LhDuUj3iODGI8-CWv1TSly_roZprC8ijKg2pnO7AZ09rOEujwUGGmYC42CCAWoQudIGqtLxriwKUDd1IjfmRCN2riesNCqUzkyXPc3dQjG-nVYbSYLNMOLu9GOy54twgCJ0C7rbEYFRBAywZfj2KSY_foh0uOWwAYUL7C96gMCx1KbSY6ovPxPNcACUkgbF7_XwOmH8FtFhG3p5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLSe2eZduM90OQsbceVWBkYtzH2XIel1S8uIK8ArQnEwSZxGURSNUDO0heKiz40cQTPba9dKR-NQ2zY9aPbzWBcIIzO5fIdHB5qxSkZuwbV6mJordzX-iCn5LpzPZyOrZzIcve6y0iJsHwAJ8fe4jGFQTLlCGidE9x_dO7YBls5jhQWCxT1SB6m_2_8JXLkd6MqcR6GsO2oXfdmGGcetLLs4DUshg1oXT6VZ4WrujcaAZUGIWG7b5CL6FNgG9jwX6lS9yIzaKyJ7-Cxzs7NrmmN7HLC_7UL9y2ghgiCn0PJOSE5JvkybTq1pXKKah2MPSMk4yPX3bFt4Z0H6iAsVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=cE-k0HBXZ2ekGqz2pUxRKrfdTxM39TIbO2tNnvHbz_Sps4D3o60_937hueTqeVrO4Vi8VmOiuDhM9YIvwe3on3IWUMUsZb59zmMCX_dCibf7OZ77eXAekIgo8jzAdYdqQeQSs2EZDmZ_HscyuilZ2T-kLMVzqt34NWcmfzhTvcg1zeiuU93-yil29dYYZ24SAb4dRrfpJbjPqfauRU7pwAK4KLaG9-L3r5iYUAnM82rA6ahBP9u8GJL2f6ki0DJw7QrajPHU0jyQH8kGeSTdceP2JOXFnIHsEZh91VqNeocr_8YYOkCjJawrBdohvOSEvgVUfwHfekYRkdH6ubFnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=cE-k0HBXZ2ekGqz2pUxRKrfdTxM39TIbO2tNnvHbz_Sps4D3o60_937hueTqeVrO4Vi8VmOiuDhM9YIvwe3on3IWUMUsZb59zmMCX_dCibf7OZ77eXAekIgo8jzAdYdqQeQSs2EZDmZ_HscyuilZ2T-kLMVzqt34NWcmfzhTvcg1zeiuU93-yil29dYYZ24SAb4dRrfpJbjPqfauRU7pwAK4KLaG9-L3r5iYUAnM82rA6ahBP9u8GJL2f6ki0DJw7QrajPHU0jyQH8kGeSTdceP2JOXFnIHsEZh91VqNeocr_8YYOkCjJawrBdohvOSEvgVUfwHfekYRkdH6ubFnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=drVvolv6y5BUcG43r0ZPQAJhVXZK3FKTVNqkdXgm57INbw_FMOZuVjhSVD8U_wZvEFJ2x2vzl-y8DdpATLTizfV5sk_K3oKBxDkigpzZzty_rCoCRccVZO4cy3VfZjvcvCjByg4JUtAydls2dDIx6ZlA2x-5t5c0I5iEaOG96lx8J7Iq2YAeo7_IaXaCrRZQH6jcAR0YlbbAN4vOcsLqaH9jOgsgrIlKjMnwxeQEu1fRwbeRRB0udeQcUzmhmoc0v12-ru2zXys30jjXSVifp7nMv4rDdjbwWJ5fGSn2_1pxu94dIpS8mq0CVnoXknTroE29CmB9GX1YSkfxP6nh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=drVvolv6y5BUcG43r0ZPQAJhVXZK3FKTVNqkdXgm57INbw_FMOZuVjhSVD8U_wZvEFJ2x2vzl-y8DdpATLTizfV5sk_K3oKBxDkigpzZzty_rCoCRccVZO4cy3VfZjvcvCjByg4JUtAydls2dDIx6ZlA2x-5t5c0I5iEaOG96lx8J7Iq2YAeo7_IaXaCrRZQH6jcAR0YlbbAN4vOcsLqaH9jOgsgrIlKjMnwxeQEu1fRwbeRRB0udeQcUzmhmoc0v12-ru2zXys30jjXSVifp7nMv4rDdjbwWJ5fGSn2_1pxu94dIpS8mq0CVnoXknTroE29CmB9GX1YSkfxP6nh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=L9XLlcrgBmGcHrG0PYaEc29uGBhwiqFusQ48oUQ8PgPsxrb1cHPiuC4qPeH64qO6jCS5REFm7PDBts3SvUQuYzdsDLI3uZ4pVvyygqEYWp8aUTrDFC0sWAPfmWxDSG_KTx4mo7AhxWzUJ6yXdA5MOw_rQ9laJA47jU8U4eAZol-j-KQ79ftvnEAYxUtogho1uHXmLPUS3wNRsOrmZ00q1xMV86oQdxbrhamCnQZlYgTJuCN5gqZNWTk2nNMFa0aJi2G-5dCffdQmqpAuGIPkL5cvXLMl4OBVfwBVw9CremuOhPeVMsxGpU19I0LCwGwmL9zc7DpeTNnzfEFLGo2_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=L9XLlcrgBmGcHrG0PYaEc29uGBhwiqFusQ48oUQ8PgPsxrb1cHPiuC4qPeH64qO6jCS5REFm7PDBts3SvUQuYzdsDLI3uZ4pVvyygqEYWp8aUTrDFC0sWAPfmWxDSG_KTx4mo7AhxWzUJ6yXdA5MOw_rQ9laJA47jU8U4eAZol-j-KQ79ftvnEAYxUtogho1uHXmLPUS3wNRsOrmZ00q1xMV86oQdxbrhamCnQZlYgTJuCN5gqZNWTk2nNMFa0aJi2G-5dCffdQmqpAuGIPkL5cvXLMl4OBVfwBVw9CremuOhPeVMsxGpU19I0LCwGwmL9zc7DpeTNnzfEFLGo2_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=qGBQ9-DNY0GI9aY4d13RxE0CDhZy4x7Ts1eExOj-DATepFhVs_NxXBeVrQ-svniOXi_VAZTanNej2NiEBWtZO7C9vI7SpygQgf-my5t8Q1I5tQZnxlQuUQn-lq-ScC4UriRPAnuKOoNgITGVVCe-wXVP08oGkL4ZlrMA--C0hsMGVT48h0bCYWh_4HPqf-r4XJ9yYy7oyEWh4pBJB71aB85jFkWWY0pcQ41hJ0wxw07VuixS45rKduBgbyFnl9ViYZY5rSteFaj8Tta9NYBLRzlE-NOg9zAVMAaJOZbdiejG6PmVAThJhwvCbCRJBx8yOW_YdRT0MWiaa7iDTsYkaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=qGBQ9-DNY0GI9aY4d13RxE0CDhZy4x7Ts1eExOj-DATepFhVs_NxXBeVrQ-svniOXi_VAZTanNej2NiEBWtZO7C9vI7SpygQgf-my5t8Q1I5tQZnxlQuUQn-lq-ScC4UriRPAnuKOoNgITGVVCe-wXVP08oGkL4ZlrMA--C0hsMGVT48h0bCYWh_4HPqf-r4XJ9yYy7oyEWh4pBJB71aB85jFkWWY0pcQ41hJ0wxw07VuixS45rKduBgbyFnl9ViYZY5rSteFaj8Tta9NYBLRzlE-NOg9zAVMAaJOZbdiejG6PmVAThJhwvCbCRJBx8yOW_YdRT0MWiaa7iDTsYkaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZkUNRoq6nhhnXghmWey7tbpLDJPBM1nOrBuGZpPFwef99p0GyoyYo4qdHz09euWBLvbJaLzmfaYfFl47PDsk8VHnttZnoUcp7lu0mQbCDTJYu397g_oWjHUcgZyyP2INMcOWXAPiOPMpspJBoPQr79S_WA8e7UQq0ziVykgB25OqWn0UdT427xCpZXvlRXqmaIRd4z1Vtl6K_DJb4_reOGUkYl3Rk-24feFqWxy6kALU-Q0z0wOWkmPPDDB4rhh4RIzrJKwbVxH8PPJYz9uGEt4br6NexCpCbyau5i7cO0FFLxvvSgNuA0SBym3BQ5zEm1KjLhHRu__tJ_N9tsZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxJFZxM6z2Hx2m3Z5lYwDIATxRok5Xbg1QI4NFyiLoLZ-5cOXzQFxtuSnf3UgkCIJM2ynlywfTvdM0GJwci54Yqru7nlsAvgiLsoPPzfTL31TcfYB5iTlzqR5ydm77yMFMXHmIbK3xhKVp8MbEAy-vPaqrIDDMUsTY9oQIwn1OSlpFgU4e7jSN9gJB6DE14umBfyXC-SEjQs6ytj16zc1CJ-D-gxqaTxXMaR7PBZf-cPvvRclCoD5Lm_dVC9MS-wtmiqWg2mJFg4_Su0Oae6HODm1P6MyTiTUX9LcMJTv0pti2U3WwPSEeFxa3ibtI0sXhlvAEVm8cMs6FaKYDXRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5H9duurPSDCzHdepyyVmdyMoqWjvQ3_sRC-6YYEXfYHhp2pdEyXlWikKlVt3nPEQfofzNSrDkHkqE7buan3QUc31KTOJeUtvgh0-26aae1DxG3fmelEqDQNe9WG2sUUnPBmPk-Tm5-cSoN4tEiNQIVuAniKXtBEc-tKk-lKAfbtel1x6rwdngN2WwDXLi5qVWuatUB3NhddiMbfqZ6naJkMJWQ0hwsShXEgekmWCKf4QO0Y1G-lh7nbNonCiDecQt6fjkUbLMaD_BAoG4NIojHszU6gOvnYK9lRxAeNRmloHhpsvxvJLdwUgh4Plr2A5u8idG8AkPzVgiBJ446JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7UD-Azb37C5R5gSeRU1Kt9B8PTuVHoxKI-6Ou4KY1qxpYl_iclnTJf-qGg3R8VkHMoAGaUXf-FtH1U5lJSoyqQ8-hImvieFq7qLiRMpHyC-78MtJdhKW__MAqL0sNECpDfkAGcjWVNJu6L0Z7Nl1u9iTYSh9--j5e4b7MSAHLOjTKBqDYKw7Tc2tiLXkRDParf_eBXpWOQQH9ucNeircVn_m24b3BwBndS4fqmFgHouy5UybgpJ6_QxV_kXwlGJ2Dcsb53TI82O-kIkjuJZ99SW8oenPyfrz32KU3qLZnOxNDx_mnis_dIXbgaDOWidecwNjKNIq76zsFEv4BlL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M1G7eITswqYJ16WIJOJcdhoL3YWzz_QmUMdTvxQ2EJuiwtcBNAtLYkEMeVt6j6DebplEHf77xYS2cm0ppPKIn5HtP6ESkq9xxhah2dJdVIAtbgO-5h3vlaYBtkjl4Jb9hQQ2zYHf6eY8FtTONpsLdSHwBbSxQAM7hyNVCK0r6jcLjG7WjM9v373FhcWyY_M5hWyRXT3O3kZrZoBp5GbF_XjD67F2C2iqZdwtPJ4EEYpPZlaCOHO3FAbQwmjF73tt5SVUdIALfpSqOAazEbYTL6UG14HKbZxA0hrx2IHF93fGr-9kMMCmlclIJCgSRbN7LHMwlC57mbQGFqdr8zZZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AI1sy2-KfBHhxTarcp3aM5HEL0bgdTfW_QTuFDvl_P1nuEeK-SHk0XUafDALpqylY6vXDTfF2D7v1zQIo9S0rBdwmyVzqW8YPqy8K68KtZWVG0lk9qVSGFsiwIKjT5XikUonP3PC2tZCLvcxP67mKMgBK0eTOXTnqX9YtqWkVKzyoO6OgUiMzY7KyJ870moFvZ1dQPEiPsdCIXiBAvj3pJ1RW3LsiY8ZY5tMDYwC4K2UMw4bxpvTAICp3WID1La_B3cxu4djWbpHVgg3h--V-OiZlxS6hcgwqIKBBCAJMAAowm1IJTKJfRZHw_rbu6U7kxkTh-gdPeir3xs_oScxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGj7Skb8-XOvdfEW0nh4lS8Udhl4C4FgYVBZqDde_k64GmhseCNRb006bCA5XgbAc0LVqaMSOkamP8YoZ_zHB9yBxP2xHgAP69tYFf1aBcihw8ZGWerZfT8J_slHxCrruDyqTHylTfiXoAF4Zx0HHgwZzRqpiFAQ3INvayNwikrGtlrOtyRymEsoDWPZYIOiP0uwG6pRiFvupgrf-SL0s5WiOfgpL_4HoTUR6wxFp1IPuuQRnA0Zva3iGO8FrqqmfALW9jQnjfBuOuqETKo90kd1ejueXifpOdgiFngNCxtdhojktDiH2EZIlOew4-mcvJlRL6ixHHOIGOcZXcXDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFhY6S2KzPc5OKzRJ0b1InXs76Yjq-hfw0_vm8x5nQ1-p_ABuNBpY5bOeHSJaV4LGB7VQ3lvnWoTOBNbPDuelWwO4a5EHtJ5yBYTW02vwOYNLlhci2Rj4mO4iQiQVIAtCyzP3CK3lf0RVhxyZd4Mg34aiOBbPGxFrXWhVX6OZrrJwm1sLNQQq2zE1p11XoikDGa6TCntuLUdVjwKKAjIF3w5TupuLCcK7LYq7BPy-07cMG1b-Ty3Wy0Hds_GyRWymg__zBGskfEzPCU8AqO1J_RI-xF4pPFf-mK4i1UbmbhzetirV_5jCTOzN3ZRMdqn8tM6JRGCH52Ej-2uSSuIsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq27FTmdthA1NRRu3Xw8pGMH7EZBEG6_DPgmKKueRg5oL5JIh2GH3nCYdvx0k_xSQk1JzOxOw81AdWQFOc2zB87EzOKeNJuVXg7wvDakQcp3zgdhO5VcImeUntqJ7iPO0mCfW-eRT7gPvvrPNQXPLztNe0DT7bpRGiBcwVXMkomSxymNriL-lHS3MIHVJpFFSRL588eDkcpIFjJyHNjDzCzSAqpV0Vi8YLH-A1e6wRlJAZz6ncxAlGOFtF6kqMavk404NdvPcY4yjsIr1qiv_9h2BU5tO_QJfWcDze39W6QZO8dht7qQysMgf3Bzt41aP0A6MI88T3cwi10W8acE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuaUGCMJcr5QjGk_1Oir6N7bM1oGdyXgFLZfTSz96mX5nU5P9bYH5nIG5m7ImnIxr0WSWRXQftkPwftYR5BDrD2-inOmtDXFDgDzyM75hP75bKTRCWmLQ-zA335tUka8-z4V1UJiZLNox4KiftYjjRje0CCQhD-m6rgf82iKX6OykndP8yQegWWGL6pWMQYZLOrO2c5h0_V8DHcjKv6pEQMBvuiiwe93FtKDxpYc8Ry2sx_UTUFWv25zgHtwVhXxmkRuudkT4fw7aogdV2_BVnWEAhkfp6dsRi4wYvwsyssYUKCNC6eOaVoMNX6eGWzvjxTLgOrLC8ob4hn3y8r1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqlZNdV9mwXLl1ll0N2MgqzwkpfPWB95aQ735wpfLDfQis9HJVIdGZDFT3K6Y9BwbcIX3x-g_uRgs_3OmWWJNHuvR82dkIZLEYXsPKq0MIWdKp93hkkze9XLj2Pc5jrUtIeYJT6kP9pDU-RLF_ptwGuMM2wM88OpD26RUejPSmCPDAUjZNvxalsesMR3kLJ_kYY2z6KkBqeKmQNWJJDnSwp9IzHeUp1fFcqqcBQNXIvrMbvalkf51q-ptVKgp5q6qnzn0Bz5Kdct_EphAmcfTuriOq9xr4XDq7WPB6HacnZ_qb1FsmwTAttoLvnWK2j_1NPiG_JcYjPrtqOciJxIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5igwXoISozZzMR8_mh8rG3zowAOopR4kh1SLRCpM06Dw61Y5S4Wvyi_fmtNGDKsl-ZT6pVxFGwCZQTbzfP132VM7uGZz2dDr44AwCPYE4kYx9KpPwydwXj-m49vdhh83DYuDnip-StUBPAoDSMI2ZIQTvJOeQrMFl0VZ_gKw3NpRFsp4r5d-JxoE6Fo5tH5yPgoFMekVHxKUubiKpcGgN9Xewwc0sD6yxoRY4mkzRXcqXVL9-DZZsAAv84qmTBmfCwTxl2NZ3rc7SqO2KCe6Ofs7q3aRQ8st-zQPZJ1HjGtd_J2qI_OGaSI9dJ-BvK2gV9Xwf4RkC5PyTcvszrDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxQtquBYkhxre379-vxleBZM6yMm7qjXY8C0ga02Ngffe53lpwnnem-3RwyTDuZimgx_N4LK646ffNwIAXfPFqlHgvFAZyBlYaiUrdEMg4oiX-jNu7s4ejirgbiqdz2YoVecnJxA7Gz1Ft53dSQoukFU3wkcwmhN9FBpt3BoKGxyxWFMWdUUiQI7lYyx6NL71emfUOtLdrs3XA7E26lCRsY0YMQmxka03TaA5Z8dRdSsOeRddGAM_BIC5uLl5NjRGWzQ2jqdzbm3_U0NotMdugTwF5nc2-H2abqWfii0vwnzyXnyyIc7O1oQSAX1gfHwqs76CVj7l2YbCwNUCWjUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zq-XIdy4wnhhJhLGi24Jv9m1lGVbJqtTHk-TEiPZlhSoXjQBF3pcarktr0dMMQQn8EZ8hxmiAG1UJAVYfeWOytZOmNHAS4U8qprd04TsRlskVw0DTjG0B303Bt0QPloNJLQsn75VrC_bTVkECPNNEFNiBmIulVnpG8wJBjSqqNE5GoJjVa4n72I71aoZsFQYvGQc12etO9rStl4OR0g6JePWRrORD-B_8eQ_kmgYPhWe73YujiC-Y0u2c52D_ttOuFnKDPf28xWGa7Y_gXGuTV1CUgP-5-Z1moriLn5vSZF8C9q6bfUk1TDmXrxtadl6jDOjV6REvvyGciniL3nvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GcRI93EwHHMH5u164z9doL_Z8DVpnjxSysEFRLTZd0Bb0Hftp4CAkM504Vji8ZcBJuNd0RHDBk2q9ic9uOnTv5bxeqGvYNmBzImWwqmt9TYM4egOb2Ehp4Rl2k4BBo-8cb1zQFHRqDV7JBFKnoGZj0QBd6xBqhqN5wlEE1Ufepi8XSk3ejd73aFz7764npofvLADBaUJoEEjvzIJvWrt1qIQ1X-XbpofT-dmjekq6yG6a09nahFTTzt9Jc_p9xmjoY4-CDcfM7OW_rwvbZIpClSiAbHPyD-3_T2CNaivNqqIVGKZ32GsNGsh0G5msg1LWTzXG9afqQyhXNfKvn53tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=SMlgfKN1zB_c1d3X6jiIK3fHI1wt17oRyzo6VSw_PphM1r0sKuO99Na33mlbDkU6M-TjG11wbyEwCtCmmS6p8DtzeE5oMIFKu51ECK6hC10Yq1_CMGj1f4ms8M4CMQV7VrEh9HXvWEEgFtMVzn_IPLHr7scm8i4JvSLW0WsCDiExmFeHI1Ry5GoB2hQW_0QIy-BX_ofjzgrQN3vr9IXNUOee5WOV-4B4itr2xWO9GyE_1i9uKmhI-QuSIx0XjfiqbM-OZQPlQQ8r3MFyFgCoSlos0gLYH3Lqn89e_krAU4AxbSSk1q0VrL9rFUHG3GoAhzT-6fKMh3fzum9vv7ZF-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=SMlgfKN1zB_c1d3X6jiIK3fHI1wt17oRyzo6VSw_PphM1r0sKuO99Na33mlbDkU6M-TjG11wbyEwCtCmmS6p8DtzeE5oMIFKu51ECK6hC10Yq1_CMGj1f4ms8M4CMQV7VrEh9HXvWEEgFtMVzn_IPLHr7scm8i4JvSLW0WsCDiExmFeHI1Ry5GoB2hQW_0QIy-BX_ofjzgrQN3vr9IXNUOee5WOV-4B4itr2xWO9GyE_1i9uKmhI-QuSIx0XjfiqbM-OZQPlQQ8r3MFyFgCoSlos0gLYH3Lqn89e_krAU4AxbSSk1q0VrL9rFUHG3GoAhzT-6fKMh3fzum9vv7ZF-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8HOF9iHz0BGj_fQigNfFts6DnkDOMG1wH12U8yY5SU_lC_6evgeW9AUwkMvLcoTElquQ7dmM4VY_on4bc669d-URpht9xbYTev40AK50REtuyuT6IHNAM4zT8c9Afgrkfs60y5aqvJQA5jNubKIsArBw9F9fXoB4nj-lKx7jTdsMmXBijW0PkOkUKwbK5z4Jq7Sqf2qsM_Kup3bSEOx6fZ1zZ-Uz4xBjbjI60RFvudzEfziVsaOdPJwCpVmrfsBziuJVmVZwSIvKjc5pcFzquvo3-XN6Wblv3e_askXCrGTX9IHWVoX2gJfZ1T_ZfL4x1xcTifjPTpkhi6H5jgaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KoBoAAU39nEYycdy8bOmbSZtQ4rGyuIYQIcFDAkM4DfCexc7Dvjus0X6bwNXzWbxaMBkHHdBJykEk_RcvRvBe26En1q-KW9RGlDKt2ER0E9WaINRwEqZzTsFWoUFEwuHVdmEAHtrA4Ee_0p_XkAf2-KGqvYSeXFtjhhrUcRj3hyr-WM1fxJRwc-MwkMWSMcmoOZlnanZZYCI-lRMqN-IrRTa06lWUzWqXqw2nP0VitH40rxfYuOQs1qn08P-w4PeSCwXAIRWQBB-GvRoV8wNlwuuOOhdCj4yUqJtBBpThKYSgjcQP4Ya8BJopM5KsWQkKjUl7QQ9zLRUPaYyZQm3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=pUpzaQoi5wFP1c5gFe0UXLfkb2_AkIvVZV16RGWgBc72neUTWF_-fR2qQrNc9n3A0w97shs-6UTy7TgtUj3wmK_WWDkkJvr7IZfbk73-8yWaCAA7W-9JndIUOOoR1KBBjyrLkOrxCKg9yox_JXNiHOgCu9i7CD6bwcl_NtWZ59y63VXKRmxHdSJcnS1TPDdXrtUuRqqwkYtEVnbmY1hmcu24NCcE4LBg3y0HP3NJtjiadkqplpacKE6cRMK1dSgg9nvRlFn9CeqVZD-Toe_41c9d4ALrq7grjGhZuvjJvhyvdg6CIySk-l7-9gCVINljJ3AiBozgKCCK3xkZfRK7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=pUpzaQoi5wFP1c5gFe0UXLfkb2_AkIvVZV16RGWgBc72neUTWF_-fR2qQrNc9n3A0w97shs-6UTy7TgtUj3wmK_WWDkkJvr7IZfbk73-8yWaCAA7W-9JndIUOOoR1KBBjyrLkOrxCKg9yox_JXNiHOgCu9i7CD6bwcl_NtWZ59y63VXKRmxHdSJcnS1TPDdXrtUuRqqwkYtEVnbmY1hmcu24NCcE4LBg3y0HP3NJtjiadkqplpacKE6cRMK1dSgg9nvRlFn9CeqVZD-Toe_41c9d4ALrq7grjGhZuvjJvhyvdg6CIySk-l7-9gCVINljJ3AiBozgKCCK3xkZfRK7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=GBUVWi3ysA3Qhubr059pStgURshZn9dch2Zx_T7CzfVOkUny4V6k2--P9oZt4kQtL52WM7HQTL3oeKofQru_hfNDdhxg4YmOHF73Hmh3CLpGiNiXUi8xKPSIEzEVxK_wpnORmRj-y2fFWow84mws9daGxEORXu6kkOefXCwZQxokP8TyAISrJPreVK3c_V8kQ3RiSWjZDRC1QtZ4p5eiHVwzGV4aHhGlyFPz79EJDVtKbFu2PjMwRxcu6cKOAlJt30sIB1enEgtWQklsZ9G_LicTRqZd6bJBO5U8vCbJ4gT-atuiaiqhuI6G735dmh-C-wQ_5yFMDlPz7C4qG8RqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=GBUVWi3ysA3Qhubr059pStgURshZn9dch2Zx_T7CzfVOkUny4V6k2--P9oZt4kQtL52WM7HQTL3oeKofQru_hfNDdhxg4YmOHF73Hmh3CLpGiNiXUi8xKPSIEzEVxK_wpnORmRj-y2fFWow84mws9daGxEORXu6kkOefXCwZQxokP8TyAISrJPreVK3c_V8kQ3RiSWjZDRC1QtZ4p5eiHVwzGV4aHhGlyFPz79EJDVtKbFu2PjMwRxcu6cKOAlJt30sIB1enEgtWQklsZ9G_LicTRqZd6bJBO5U8vCbJ4gT-atuiaiqhuI6G735dmh-C-wQ_5yFMDlPz7C4qG8RqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw-_HNFoUKT2QiC4Tnj8GVJ1GTaUCIN3fNdaGRpiJ6LSIhdbqtVuPfy_Q8tC8Vj4-5qeqs1L72tOjySNLXPwcAINPx9dKwxlOzJW1hZA-ZfGDRpVYvid4lQElFWhAe8Mx5U5cWS3oOIbpnYRwsf_1_t5Dhqtdm4PVN4RGt6BgXc8O-ADXWSUKiQcx81Ix84UuSIolajOuKgVK0uuMLpTD1dAuJmoc6mXPXdvPSu6_UBofDsCKlR_idD8-GqDaNC_SXrIWIfdsFoCW4HftzFZusK_cKYyT5FglbZbl6cHLUPMmbRItodXjdv9lI67KYOwZgqGyoQP5LrIBGywACBajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=hWZz5uFbrzVmtmyUbhtpt1pEEe45aQ6A9qlpjRdw6p6TVAndvJygCDMdHk1D03opH7POntEOB38b-xUAVDeKAEhmkOowFaRGdzV6XXdZo4F53VaLTW0ff8v4HWH7IxqyVTFmNSSr3XIGFAY4fPwKAVHaho6xjYnCzI5U3oeWw3eR2X7K6uED_Zhz4A_gxGhqyFK7BEhOmQpky8nCwMwWfqW7VJ1rUkH3PGZiA5I7hu7HxAdHgAet82I5woyObB2C6OxEBR_pjLZ72X2qHRmzUUEK-kiKDbsKGcSn2Rvse9MvTqjsh6JOqGLhnEw9PHi58369RtHCpMsK8DShgc2NYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=hWZz5uFbrzVmtmyUbhtpt1pEEe45aQ6A9qlpjRdw6p6TVAndvJygCDMdHk1D03opH7POntEOB38b-xUAVDeKAEhmkOowFaRGdzV6XXdZo4F53VaLTW0ff8v4HWH7IxqyVTFmNSSr3XIGFAY4fPwKAVHaho6xjYnCzI5U3oeWw3eR2X7K6uED_Zhz4A_gxGhqyFK7BEhOmQpky8nCwMwWfqW7VJ1rUkH3PGZiA5I7hu7HxAdHgAet82I5woyObB2C6OxEBR_pjLZ72X2qHRmzUUEK-kiKDbsKGcSn2Rvse9MvTqjsh6JOqGLhnEw9PHi58369RtHCpMsK8DShgc2NYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
