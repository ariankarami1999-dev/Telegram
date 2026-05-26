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
<img src="https://cdn1.telesco.pe/file/FQc_MCQh0cJHCwADiEEiVxkmktjsUUP5BeKWA2Ko2PbTO_SoiiGjoerUlzKHqSp1mDOF3bOjxwGXR8nFbMBbvi9-cohea8rS0fHwDM9OtZFLVUqPBMAoUfn0Y3P1WWLt-ug9T_T59jeTZzdC4zrLmQv7qH-5Ar8RN0G6wxj6eFXpfle7qqjkfAkhStEt2pIWM35mOxye-WuL-HfIhDb9VoFei0PxdvrPf0lJy7mykHWcln7S6tLxja-EDFfIKN6G1HACJolswIyp5tPAf5G8HsgUd91V00h_hGBOgU1Gx-gaBMczRgYVg8aHwZlb6nP5DDz4_5c5bxdVABICWctDSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vivr5NQVqYWt_-k091a-7Kd1vsUkhl1_ROW6vzOZDs9kocczxtMJ8vs_EZlCJAzKUezfljfFPWd_JQxB-MX2iBvPFuf82ra7axqRoAGG-lrJK4TR1FKKkHG4aIGZwZDf0UR77aOYG6cKwAGp6R3ZOeQftpEcuyxHuBVPYerycWHj1TaRbAncRkgmJJ4OXthkH1meyDu9NvAxOnqcvq21C0p7tTzn5YeY7sfMYxyCwny5iy9Pd73oC-VW61JoW6zLTHLzZDiUndBuBG5m-Bj8WUhrE7T4zaLzKRRJiV4bXJQcygg1TxBJUBvxeEtku4yOgKaneMmA-jZ9tZ6x0j5K_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، قرار است روز چهارشنبه نشستی کم‌سابقه با اعضای کابینه خود در اقامتگاه ریاست‌جمهوری کمپ دیوید برگزار کند؛ نشستی که به گفته یک مقام کاخ سفید، همزمان با نزدیک شدن مذاکرات مربوط به ایران به مرحله‌ای حساس برگزار می‌شود.
خبرگزاری فرانسه با انتشار این خبر نوشت که انتخاب کمپ دیوید، اقامتگاهی دورافتاده در کوهستان‌های مریلند که ترامپ برخلاف بسیاری از رؤسای‌جمهور پیشین کمتر به آن رفت‌وآمد داشته، نشان‌دهنده حساسیت گفت‌وگوهای پیش رو ارزیابی شده است.
روزنامه نیویورک‌پست گزارش داده که موضوع ایران محور اصلی این نشست خواهد بود و همه اعضای کابینه  [
از جمله
تولسی گابارد، مدیر مستعفی اطلاعات ملی] در آن حضور خواهند داشت. بر اساس این گزارش، مسائل اقتصادی نیز در دستور کار قرار دارد.
کمپ دیوید در گذشته صحنه چند تحول مهم دیپلماتیک به رهبری آمریکا بوده، از جمله توافق‌های سال ۱۹۷۸ میان اسرائیل و مصر در دوره جیمی کارتر و نشست ناکام اسرائیلی‌ـفلسطینی در سال ۲۰۰۰ در دوره بیل کلینتون.
این دومین سفر ترامپ به کمپ دیوید در دوره دوم ریاست‌جمهوری او خواهد بود؛ نخستین بار چند روز پیش از حملات آمریکا به برنامه هسته‌ای ایران در خرداد ۱۴۰۴ بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/VahidOnline/75738" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxmKHmOx_jSiGUj1ychutybcIuYy26xsUe7Xkwx4r_t2U5Uo_9Aimi8rZp_471q9O8zv0X5R1I2Bl_sU-B5bWxdJpMaG6vr7mLul9CI0-bfUgGqAYKk4oR-eNUmQfLY-9R23rWd5DOlHGxCxomDJP22HBPGK-Bd_ctBrPxlNkqx80dUH7lFplSg1FoTW9VltGAgPIT5Wep3P2Zm2Mp7gAFCUt7Mb93lUe3SbnTPiSO2sOCfb4EPC-nCZvKCvPneneB-bnpeKaIW5CKOpwn2WNO9KwD8w1zVaE4OSIw6UXUOWevC0WI-wlppF3szs7NnxKZ0NK4ClJSdZXGnHMLD5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش فارس، خبرگزاری وابسته به سپاه، محمدباقر قالیباف، رئیس هیات مذاکره‌کننده جمهوری اسلامی ایران که روز دوشنبه در راس هیاتی با همراهی عباس عراقچی، وزیر امور خارجه و عبدالناصر همتی، رئیس بانک مرکزی، برای رایزنی با مقامات قطری به دوحه سفر کرده بود، عصر سه‌شنبه، پنجم خردادماه، به ایران بازگشت. بر اساس این گزارش، محور اصلی گفتگوهای میان مقامات عالی تهران و دوحه در این سفر، رایزنی درباره بازگشت پول‌های مسدودشده ایران بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/75737" target="_blank">📅 18:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O46EHopApYe82-yYQIDrd-RU0J-bi-IGaEIikH-BNXBk5qxfxDy6ryqHq_ak-xBouGKyzCoH4LOAB8XaIl54pCl2U0t5sTCb2PSmOwxpFoZHTR8zAfRaXJc8reX5BLutgJahN1V-4KNrqxUFKeDeryghUpdj0afZVCV8q3ZRmqVxMlj6K5YCvT5vUkyCnc1DOSK1MEYEerRIR4TeY0DLmn17R_Tvzi8spTOeVkjWoEecSkx51qrxVG7bIL7A4oX0CAeUVoH6E0ZA2MWv2-RIqN6fww0nInbot0xodYdyopzRdeL50Dg1C845ziWQJE3z6mjTKjtIH3ASCboRw5RUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز سه‌شنبه، به نقل از منابع خود مدعی شد که طبق متن ۱۴ ماده‌ای یادداشت تفاهم بین ایران و آمریکا، منابع بلوکه‌شده ایران، به میزان ۲۴ میلیارد دلار باید در طول مذاکرات آزاد شود.
آنطور که این رسانه نزدیک به سپاه پاسداران از قول « یک منبع آگاه نزدیک به تیم مذاکره‌کننده» گزارش داده، ایران تأکید دارد که نصف این مبلغ باید با شروع مذاکرات، در دسترس قرار گیرد، و بقیه در طول ۶۰ روز منتقل شود.
این گزارش می‌گوید که سفر اخیر عباس عراقچی و محمدباقر قالیباف به قطر هم برای تفاهم دربارهٔ اجرایی‌سازی این مطالبه، و نحوه دسترسی به ۱۲ میلیارد دلار در گام اول و رفع موانع بوده است.
همزمان، احمد بخشایش اردستانی، عضو کمیسیون امنیت ملی مجلس، مدعی شد که چند روز پیش، قرار بود ۱۲ میلیارد دلار از منابع مسدودشده ایران، از طریق روسیه وارد شود، ولی آمریکایی‌ها مانع این انتقال شدند.
هنوز هیچ مقام رسمی در دولت آمریکا، این ادعاها را تأیید نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/VahidOnline/75736" target="_blank">📅 18:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U1wYYEc9PO5mn8cbvorpUmdw3we9g1-2gk60wydIbfDGmNjK2TQRe0dqSYo74ZLBbXszQ3_g2T7Uf2zl8qHTgbEHUlaDDY54X88n6tDW6NliDMhbaCJ6cDSYyeX0SZeVczYlWkNHaYcVTNFdYcHdYAmOsPobUPghM_2B-YnQ59Gd3ketGA2zsRis_7TyCR_CRPqCNftVXHRPeQWpsqWRvrmS5ScHJrk6GCStHxILfuQtqq6DX44ffw-L2CWC-ypCR8fUpOb9cBDX59MCPZSH-AXwmFmks7T466U9VtAPG0lrIE4_r-Eggdk3tXJLxGAwYgT3sg3YeljObbYtsBjzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rf6YExlJBtCToVkmveZ-Lvd91nbLVMohqMvVkBlMx6BSDPVR5dF8Dr-AyIsB8iw7K2IKaFgv6HhQtEcTQrLtMbsQJ6yc42jEnXRzpOIqbK3P-HioWfuO50MjL-H6uuu7uIfJzyTl4TNUfMNakw7UjWjrrRHfajXqBPFTKIMwRpSVSoSQOR81gHn9dD6w1_u9ormnx4MUSXT41I0rA-irO45msLtJVhR_OnAFdJVH6WXB3Jb4TJse-7JbELCJKH4yWV-njdKDHV-I-F1qioeMR2zDkm77PVlIfytN0U858QsnQwdwdRk8xRpF90AyzNBVXfhmb_Dt227mFPW5P2g8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mfW7sQh8faAHzNCRg_6z2sfSzzgtGDp9lO5PXxFfxhlVd-L-0fNczMZdnmPIlQfONKPGmTeSrAwG1R_Vtq2K8UJAXwIbiAQmI5ntsZb7BLFfQb0ruujJmyf5FeifOLsJbywFXN1nDGXNvLOyQCztW1b0UGhbhKtTs32Yf4dNcQWxH05cYI4E8ByjOWddkJrxacQiYKgSTCnOWE-VXKLOKhCAdcyf-0uOV5xGlbpyzReSvFmGPg5BrZpsqj8Kz1rV6iORvBeTRojxJefCTtn0iReHMh8U8EMm3gWCZDdorUGdRVZz-jsGUEJ9UDQtWXte92WbUTnpjX1VHLMdeH5QeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hnmPSu-o5PQylhhiuYOJqETbjVNYH9QEADyEMaRR5pKxcBjn74vC2lQqxCp2QCsoOPwIXaqGgSXcC_v2UkzH_LDNwJH47_--rHz2LswOfc4q5z745-QbqvrkeOR8DtFg2M-hT4PgC_B9k2Y7Qw6-FCLPKSSE1N6Lna61MMQ-4JJHNdsNZl03Nwcbr5LnjdXjt7eCdQVMVo8tZNeux3fmoobluKZOUCE7qtiCE5Cb_2oNd_TLBr5GhcPUcCVbDZSe-A2vsULc5oHD-tRuXnTfB9w9mjxxDJgoHhhZPYO_nRU3Dykosjo8oCX9krr2Vi57WJHftCR2TiVhG47W2kF6Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد پایش وضعیت اینترنت در جهان، اعلام کرد داده‌های زنده این مجموعه نشان می‌دهد اتصال اینترنت در ایران در هشتاد و هشتمین روز قطعی گسترده، به صورت نسبی در حال بازگشت است؛ هرچند هنوز مشخص نیست این وضعیت پایدار خواهد ماند یا نه.
@
VahidHeadline
ساعاتی پیش از این واقعه اخبار دیگری منتشر شده بود:
در حالی که مقام‌های دولت مسعود پزشکیان از آغاز روند اتصال کامل به اینترنت تا ۲۴ ساعت آینده خبر می‌دادند، دیوان عدالت اداری اعلام کرد دستور توقف اجرای مصوبه تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» را صادر کرده است.
این دیوان ظهر سه‌شنبه پنجم خرداد اعلام کرد «به‌دنبال طرح شکایاتی، دستور به توقف مصوبهٔ ایجاد «ستاد ویژهٔ ساماندهی و راهبری فضای مجازی کشور» داده است» و افزود: «تا زمان رسیدگی نهایی به شکایات مطروحه، مصوبات و تصمیمات این ستاد قابل ترتیب اثر نخواهد بود.»
مرکز رسانه قوه قضاییه نیز اعلام کرد دستورات و مصوبات ستاد ویژه «به دلیل بررسی غیرقانونی بودن ساختار ستاد، تا زمان رسیدگی قانونی قابل اجرا نیست».
@
VahidHeadline
بعدش:
همزمان با اعلام دیوان عدالت اداری مبنی بر صدور دستور توقف بازگشت اینترنت، ایسنا به نقل از «یک منبع مطلع»، روز سه‌شنبه، پنجم خردادماه، گزارش داد که با صدور دستور اتصال اینترنت از وزیر ارتباطات و فناوری اطلاعات فرآیند اتصال در حال انجام است و طی ۲۴ ساعت این امکان برای همه فراهم خواهد شد.
این درحالی اتفاق افتاد که تنها یک روز پس از مصوبه «ستاد ویژه ساماندهی فضای مجازی» برای «بازگشت اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴»، دیوان عدالت اداری با صدور دستور موقت، «اجرای مصوبه ایجاد ستاد ویژه ساماندهی فضای مجاری» را متوقف و مصوبات این ستاد را تا زمان رسیدگی نهایی، غیرقابل اجرا اعلام کرد.
همزمان، انتخاب نوشت که کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری تحت راهبری یک مقام ابقا شده دولت ابراهیم رئیسی، «شاکی قضایی» اتصال اینترنت بین‌الملل هستند.
ایران از زمان آغاز جنگ در نهم اسفند، به مدت ۸۸ روز، در خاموشی دیجیتال به سر می‌برد.
@
VahidOOnLine
محمدرضا عارف، معاون اول پزشکیان، در شبکه ایکس نوشت پیرو دستور پزشکیان «گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد.»
او افزود: «با بازگشایی اینترنت، خدمات هوشمند هموار و مطالبات مردمی که این‌چنین پای کار نظام و ایران ایستادند محقق و موانع توسعه دانش‌بنیان و مرجعیت علمی برداشته می‌شود.»
عارف در متن خود درباره «گام نخست» و وصل شدن اینترنت برای شهروندان توضیحی ارائه نداد.
این در حالی است که پیش‌تر فارس، رسانه وابسته به سپاه نوشت دیوان عدالت اداری اعلام کرد که در پی طرح شکایاتی درباره ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور»، هیات تخصصی صنایع و بازرگانی این دیوان، با احراز ضرورت و فوریت موضوع، دستور توقف اجرای این مصوبه را تا زمان رسیدگی به شکایت صادر کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/VahidOnline/75732" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8pRPGgBhRAIJL2Jn5mKlTrjTFHcRF1tcfKa5xC1Nk0WXlBHNmZPEQBj1I58yBqFHSHp0R0bVJkYJ-afd9mFX9h3qQ2BqV4I1Q6U2SdSkq7u8lEkOIis5oRcytEk9pFneyoz4Ree4-E-S-FPtozoks6C-AcuhmD_GmgmsKdYWv_s7HdMrTa4X6VkJPJpDc67GDoblnKHU3zaCCC1hPUn87z38rYavS6BYOdypLRj36Taf6T_QVJuU7ozYs41NEfqbbnJmPhtbZtWHIIO-yelnqkJ5w2H6DFs3UQCZv3VkRJs0I7Ix5ix-II20ttsOgCJ6rmeYNaUWIYyAiPms1jomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/75731" target="_blank">📅 17:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h-FD530lSP-IHGEloFJh1kbT0-_OTFQI2uxCw9xCXthssXR0vD36NwJ-8P5tekIAKfQL7yGUNskEmbk-bbSEh7kqQNpYmKBTDpJTSawuwTGbpVi8_baQRS-oNICKCkTVeORyJ68sb4rSWbwYFGwnQ2GDzmQAxsd9D5iI7F4wj4iFxqBRA2yDspiMis3PLkDWSyeM-XTeGi1zMmEDVoibBAIF7u14X-jsC7JTpDrefshwe-iFLois3j1YmB1KNSGceJ10mOmODYzXxy3GKA5Y180UaJdu208vOyQAnfFQlXCdhGNl7_oLeMsqjYtYv0VAk9DBp4hol5Ez6Kf_zMAX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nRnU2uhOl3CwpsXmBsk9zj8LPhdk19TF2-AW5XdXgEFU_5lNU3lJLEg0SOOrh-orpZMZkDcwyoefQo_cZGTOmzQq5NFEJJheIzkpiQnlGDsGA4YRZejbTVomrk-E8wn6_bEnV84byYNKfGJf72peTmDGFpkD2lQ34_H0qauRZKYvqec8ukrcEWeZX76CifOWVQSQQACPfEk-RG2bjwTDIDcqCRN0FkEUdWhrGqHl4RLAsWJs8MYMCp51HvnBfrFHDgJGmnheUUvMFt5FPGlXb3RtX_QX2p4_qFiaYkzRqimLcm7dagtgwAka9VGRP3ivHjOyY5KnJP4NMzL5H1FGZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران روز سه‌شنبه پنجم خرداد پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را به‌مناسبت برگزاری مراسم حج منتشر کردند که در آن می‌گوید آمریکا از این پس «نقطه امنی برای استقرار پایگاه نظامی در منطقه نخواهد داشت».
او در این پیام توضیحی دربارهٔ پایگاه‌های آمریکایی مستقر در کشورهای خلیج فارس نکرد اما هشدار داد که «سرزمین‌های منطقه دیگر سپر پایگاه‌های آمریکایی نخواهد بود».
مجتبی خامنه‌ای همچنین با یادآوری ادعای ۱۰ سال پیش پدرش علی خامنه‌ای درباره اسرائیل، مدعی شد این کشور نیز «به مراحل پایانی عمر» خود نزدیک شده و «۲۵ سال بعد از آن تاریخ را نخواهد دید».
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی را از او منتشر می‌کنند.
@
VahidHeadline
در پیام منتسب به مجتبی خامنه‌ای با اشاره به گفته‌های ۱۰ سال پیش علی خامنه‌ای، رهبر کشته شده جمهوری اسلامی، اسرائیل «رژیم متزلزل صهیونی و غده سرطانی» توصیف شده و آمده است: «اسرائیل به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگرِ ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله‌نفسه‌الزکیه، ۲۵ سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله.»
این سخنان در حالی عنوان می‌شود که اسرائیل و آمریکا در یک سال گذشته در جریان دو جنگ، مقام‌های عالی‌رتبه  سیاسی و نظامی حکومت ازجمله علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، را کشتند، بخش بزرگی از برنامه هسته‌ای جمهوری اسلامی را نابود و تاسیسات و زیرساخت‌های نظامی و اقتصادی ایران را به‌شدت تضعیف کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/VahidOnline/75729" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzA1a3w6X8t8ijDYNPGBVHOj0FnT3xyH2sRmb6vAqweKuaDavt-bzGbUvxKnxN_umSxrU4SOeUKLRP_v-seZ2jvvjRphg4H06EFxF7ijh06Kd-ErbTdZifRf_aUxrNZvfdWcCN1ZbsxoskNXX2rafSH--G69YowpYLH52sVyuaHOL1bXDLdxn1Ui05hS5zz5SPF22dznxPNij9l4yd4hDlIf8pYIcMk9l9aaQZ2vVE1ogSBjg5sUECv9FSB-nCa2vLe_J4vbRpT5NVuk-aZfF5RztfJnuTTQdYz9ZbrrHPDz_a3nGWWrOAULpWUvGU2eS3VpeQFL5_PGblpAXH8OKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر می‌گوید گزارش‌هایی که ادعا می‌کنند دولت این کشور برای تضمین نهایی‌شدن توافق با ایران، ۱۲ میلیارد دلار به جمهوری اسلامی «پیشنهاد» داده، «کاملاً بی‌اساس» است.
ماجد الانصاری سه‌شنبه پنجم خرداد در شبکه ایکس نوشته که این گزارش‌ها «توسط طرف‌هایی منتشر می‌شوند که به دنبال برهم زدن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش‌ها و تقویت ثبات در منطقه‌اند.»
او افزوده که تلاش‌های دیپلماتیک قطر که با «هماهنگی» شرکای منطقه‌ای انجام می‌شود، «شناخته‌شده و شفاف است».
ماجد الانصاری انتشار این دست روایت‌ها را «تلاش‌های مذبوحانه برای خدشه‌دار کردن اعتبار» دولت قطر نامیده که به گفته او به‌عنوان «یک بازیگر بین‌المللی قابل اعتماد در مسیر دستیابی به صلح» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/VahidOnline/75728" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8mcNsVHxYtWY2xOcG-n_-Uau8bcAT2BwM1PfmJKz2V87_KEhy4TPbmS7bpbsKuBmsjmdTtxbgHWIUwckoYDPGzlooilqs5GEkfheOekW_iUV-w43z5UJDL-hhhsWD9xHvLRzklcg606R6j853tlww3Y0oRSeCxbwBTSLOL-d-YeDTAuEDkyFSjvBjPcl_rk7_jkzDTyb8gu55wddvTBZOF4CH5i6VLH_wo6RmcH6nWPBF0c4YYmIutDbTknJPKGY877kCJj3l5NdPUz3Z9xdcuM01Q7NT4iVoaZ0oJe389DY5HTICYLyb_FrUMcf2uv0vepWGdPGj9IDkPAfN77uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mTWj0hivoNb64xupOwG9MXxCCkulR3i-4FnC13BwnOx3YkvAfSPulHD2MWLEEHBzl_t9XdgYZXMojj0bbdyGmk91J4DYwp5kstX978jcu7VFNaUP_xzV1jPfBTThsXuhWAuOuTl15ue5g3ICrya1yItD-vDv7oCNY3bHI4xqovj1AtHxjy3N_z9hJcucniX4HZruPxZq7JqH52JN-hqB59Vbrbcpr2N2-YcFO5gX6CLGc_8GJlmk__aHbZipbr1jt45UpM-I4Gz3bI-2IleG3pNIz0r7AVH5uv7eSLw4-X6p3QzqNc9uKrYAu4oIeD8__Qfyc9n65h2LoZWoifPSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BTG81QprhZOMWlbXU-LZRmibiyyZpCxUKQkmf0oUJuFH3JWxsjv5r3MY44dcMvb2hsfnIvilAQIO-jeL1bRSnARcB5y1zbCZzlZgaxOPZ3TL7BlnzF0J6RQt3J9fad2gBDgdbDvQaUDHpTZmsqjI__i20PgOe4891G6cqhueSpXozcfVyka6iNgVxNzpoqgRx6ArnKkrBw3mRoSl_kYCbfuiFDpMHhHw6_6DdCrGNUt99ZWuZgnXBdc3A_g9fu_pGHZ_xgPdRj7Jdbd0eu2WH2XnlS8A5JWvC_kaZbgqiLnk_TyWs0YRtqhhVyIAqHgeOaRwhWb4bfqwWgOdKs0aaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه، اعلام کرد غلامرضا خانی‌شکرآب به اتهام «همکاری اطلاعاتی و جاسوسی به نفع اسرائیل» اعدام شده است.
میزان مدعی شده او «سرشبکه عملیاتی موساد» بوده و پس از تأیید حکم در دیوان عالی کشور اعدام شده است.
در روایت قوه‌قضائیه، اتهام‌های سنگینی به او نسبت داده شده است؛ از جمله جذب افراد برای عملیات خرابکارانه، دریافت پول نقد و ارز دیجیتال، تعرض و اسیدپاشی به خودروهای افراد مورد نظر موساد، آتش‌زدن اموال عمومی، تهیه بمب و ارسال آن به تهران، تصویربرداری از نقاط هدف و حتی مأموریت برای فراهم‌کردن مقدمات ترور یک خاخام یهودی در یکی از کشورهای منطقه.
ابهام اصلی پرونده، نحوه انتقال خانی‌شکرآب به ایران است. میزان نوشته او در خارج از کشور شناسایی و با «فریب اطلاعاتی» به داخل کشور هدایت و بازداشت شد.
@
VahidHeadline
میزان نوشته است: بر اساس اعترافات متهم، یکی از مهم‌ترین مأموریت‌هایی که سرویس موساد برای وی طراحی کرده بود، اعزام او به یکی از کشورهای منطقه با هدف شناسایی و فراهم‌سازی مقدمات ترور یک خاخام یهودی بوده است.
@
VahidHeadline
گزارش دستگاه قضایی اشاره‌ای به تاریخ بازداشت و محاکمهٔ متهم نکرده و در عین حال وی را «از اراذل و اوباش یکی از استان‌های کشور و دارای سوابق نزاع و شرارت» خوانده و ادعا کرده است که او «به دنبال جذب افراد و به‌کارگیری آن‌ها در داخل کشور برای اجرای اقدامات ضد امنیتی بوده است».
از روند محاکمه این متهم گزارشی منتشر نشده و گزارش قوه قضاییه نیز مدارک و مستنداتی از اتهامات ارائه نداده است.
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/75723" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sw-l4B2xOyNCGRx-kp9ZluCJkmquSQi8NV6fuAyd07qEH_leNHHJ_s8D9Bk9EqUFVxdL1u7RiBtVUPE4VYAS5_uJZQmvQ8_3Beio33-23I17Ohn3A7kO8-IkWfs6rwtEjiQsT7OXsHwVjBnbRUD_n8TA6Mv5tt08X9pvJNMF8YDiNaGA2hRwTBhnAo5mx9HlwSCzRVVyoLtF3NbLLZRlbK9TtrDJSC-BPwgzQJCYgoDwGvxdw2Er6Lq2X4OT9wdILbqH8-0Ed611fb65bw60oN46vUurgCdAZxcPiTHOdy1I_oi6E-bC1-u-fsRLbazOglDKVSo8Ss6AJwUlv-kKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/akP109IR2WKqFOKLKwsJ9MSqsATwQ3wx9e5Sr5RlpRSHoC5RTCrESh1HYzloux2XWI84Cbsx9SkYzaE-aPnwkVoRzRw8nv4w38EdAETD-gv8mInZM9c4Ab_ro9jj5JKPaHAB6CI5X-eSqgAlP3vhbjTnicIfhabAap8J9iSB-AdetJQPuqmy-ufZhzYChDWvpm3QrWPKQCW3P2LYKaZSd9nvfEZww01dR5dcbuIDSBZlfp-bInk-mq3zhb1DN2d1EYA-U-oSuvzxNClLEULIuEbmMUWGMWIK_62HDwucVWPDXt10zE_doUG_nvXnWs33aAas_D07Z3kvcNySD9s_TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با وجود حملات اخیر آمریکا به سامانه‌های موشکی و قایق‌های ایران در خلیج فارس که وضعیت آتش‌بس شکننده را متزلزل‌تر کرده است،‌ مارکو روبیو، وزیر خارجه آمریکا روز سه‌شنبه گفت که توافق با ایران «همچنان امکان‌پذیر است.»
او در هند به خبرنگاران گفت: «امروز مذاکراتی در قطر در جریان بود،‌ و باید دید آیا می‌توانیم شاهد پیشرفتی باشیم یا خیر. فکر می‌کنم بخش زیادی از زمان صرف دقت در کلمات و واژه‌های به کار گرفته در متن اسناد می‌شود، بنابراین چند روز طول خواهد کشید.»
آقای روبیو افزود: «رئیس‌جمهور تمایل خود را برای انجام این کار ابراز کرده است. او یا به یک توافق خوب دست خواهد یافت یا هیچ توافقی نخواهد کرد.»
آقای روبیو به خبرنگاران گفت که تنگه هرمز باید باز باشد.
او گفت که آنها به هر حال این مسیر را باز خواهند کرد و افزود: «آنچه در آنجا اتفاق میافتد،‌ غیرقانونی است و باعث بی‌ثباتی برای جهان و غیرقابل قبول است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75721" target="_blank">📅 07:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAQ0Z-dDS0yH5XaSMNBprqo48aE4WrZwkfqVSl5FYWmCiDuab91lsU3KqEQTTBOz1dIP9bzbXn-sizhVw1vYQgb8GuBhRjcfN-5YZai24sEKotaLg1-DviXa-2oG7yX4HO8QjMy6n46s1VamGTuR2f16oYpKbh9W5MiS7SJUsXXbNrsSjwnwWI6-dyBk19kPwI1io1qrgu-CvA5LMmBBO6PnRuY1ecCn2evq-mOnXGmHVrHKWOa37uST9Hc4qJs6T14HXCBoS2T1z5WymEy2k1mPYoyn7-cZb425aHc-bHc-ZbBNSz_NqImIV9pBi-0H8AwZAU2o-WqnSkOxghlP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اواخر دوشنبه به وقت واشنگتن گفت مارکو روبیو وزیر امور خارجه، به در خواست همتای روس خود سرگئی لاوروف، با او صحبت کرد. در این تماس تلفنی، دو وزیر درباره جنگ روسیه و اوکراین، روابط دوجانبه و اوضاع ایران صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75720" target="_blank">📅 06:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPOGwHwcBospZQqFZhcQNPezO8rSlEUKASP55zUNurtURNh_nyJnFi3Z1rJ-LdkXVB1tpuDho_y-Vr7XrFCoLO7iCqI8bPlO34nZ-TAoPVp8acmpc4QSh-NIbZIrc8CDbrrz3yLLDfhB_TaAa9kFi2YYtnbJmGhQoZQ9fztQ11OQDTIAM898I8kp1LoR39MRvody7TrNBzVpw_JhKiiL4BU7RIQcbM9-amZxnMsTtruFP3l5ZiAFbvlhvKsJIHnxNP0uj5hZT6-w4s6Y82tMzq8RsWVSzoGQnl7mvuT2zHthDSBKu0a5KAh2oQDz0aut3XXHZgVqBtTrwxJG6G220Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75719" target="_blank">📅 05:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwv4A4kAJAAJ2_rTOqVZNPTkU4GXmwebeIYiAxTVvw7MtSkltoIINqs0IaTRW0wpqpbzSj5AulolZNm2rcUDENxd3zQK2SjLW5SOgQGIanGJAPP9akHZYCTWToPyTyg6YBXDizq1ClIsQWQJSFZnCwvgAUz_mdcn0DqTbLyrftr3KvfqdCrrFwFn-1npUpHm6ZRWWl08CgQA3kc5VjyTA4JOBVfs3-arEaOlPF1yfrIB0oOeUgB-ROETND39xWqV5OLFhpMW0ECVUklMeTd_JtML3OoCBBkPWK8hwdFDkxd1SGVP97N7satSOvtUzhHyZqGZXK-tBXaovnkxVoCyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رماندهی مرکزی نیروهای آمریکا - سنتکام - در بیانیه‌ای اعلام کرده است: «نیروهای آمریکا امروز (دوشنبه) در جنوب ایران حملات دفاعی از خود انجام دادند تا از نیروهای ما در برابر تهدیدهای ناشی از نیروهای ایرانی محافظت شود»
در بیانیه سنتکام آمده: «اهداف این حملات شامل سایت های پرتاب موشک و قایق های ایرانی بود که تلاش می‌کردند مین‌گذاری کنند. فرماندهی مرکزی آمریکا ضمن خویشتن‌داری در طول آتش بس جاری، همچنان به دفاع از نیروهای خود ادامه می‌دهد.»
ایران هنوز واکنشی رسمی به این گزارش نشان نداده است، اما برخی از سایت‌های ایرانی از هدف قرار گرفتن دو قایق تندرو سپاه در نزدیکی سواحل خلیج فارس و کشته شدن چند نفر از سرنشینان این قایق‌ها خبر دادند.
نیمه شب دوشنبه به وقت ایران،‌ برخی از ساکنان بندرعباس و شهرهای حاشیه خلیج فارس، از شنیده شدن چند انفجار و فعالیت پدافند ضدهوایی خبر داده بودند.
رسانه‌های رسمی هم این گزارش‌ها را تایید کردند اما اعلام کرده بودند که علت این انفجارها مشخص نیست.
@
VahidHeadline
درباره همون وقایع ۲۴ ساعت پیشه که اخبارش تازه داره منتشر میشه ولی بسیاری از منابع جوری جلوه میدن انگار مربوط به ساعت‌های الانه.
احتمالا
اون پست ترامپ
هم که تصویری از قایق‌های مهندم شده با پرچم جمهوری اسلامی گذاشته بود و نوشته بود «خداحافظ»، در اشاره به همین واقعه همون موقع بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75718" target="_blank">📅 02:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lQmVVuO1QHQ-79RwaABTjeBYi3JDKN3zYqgza-dAfLfVZBJu3CMO7kPrHmIneJLq8nMGJ5b0SxU0BiBuK6m8vN7tCBdmh6ekGlJDQq9oD9WvEiKgY2fZl-bGWPMvVoF-rwAFqQJ6KyoL2d9BV7P-S6BbCK6__rqF9xSB7YTn2nQBLJfevKKmABwWEb9lTLQ30jGHZLMMNIHd7rWkGulB0i1k8dd9Smi7o24E6xpJmAiAvaA6r-DvYFitjW7i7n7cvY2dVR0gXPgYrpOr8DBLiYRnagkH2nCRW-l9omh7sVyZWIPJB4ZnrBjJQo_KfARp7LyOx7zCs4weEQl0m2ADFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EfHCfQAdNnvWcJ_3H5orjBqzao2H2PyWt0kc4RUMtuGhVBaS3cbEiTQ7c4LOnjCvh-DYX_vDIsJ7nPDjcWvxSOpSFS0ndSpYlWK8lAFbmsK5DMnWIHV8vv8VW5A9AC6tBCBSyyns3mK5lPt1clihwq2Iqzsa-pC0pSIamnME371VjLQLbU4ZBBtOpquTSiPNP3dtOfgTob95ELK75hKoG5PHoCYNxuQ5HZhLDQJOACLT7ECRuSl9wMrxxgB3bFtHnnXs15WXcUt4Qv9jyrIole9LQzekenVDnMIAPHdaVJC67KIbrfi-LkqHwyXl6sWVRsB5vCp1xRGhvY4BTzd0TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری دانشجو گزارش داد که در ["حمله سحرگاه شب گذشته ۴ خرداد"] در جنوب جزیره لارکآمریکا و اسرائیل به جنوب جزیره لارک، عباس اسلامی، قدرت زرنگاری و عبدالرضا گلزاری، نیروهای سپاه پاسداران کشته شدند.
براساس این گزارش «تعداد دقیق کشته‌شدگان هنوز مشخص نشده است».
@
VahidOOnLine
گویا این واقعه مربوط به اولین ساعت‌های دوشنبه است. یعنی حدود ۲۴ ساعت قبل
ولی به نظر می‌رسه اون دسته از منابع جمهوری اسلامی که این خبر رو پخش کردند عمدا طوری گمراه‌کننده نوشتند که مربوط به صداهای شنیده شده الان به نظر بیاد.
ولی این توییت مربوط به ساعت ۷ شب دوشنبه است که درباره همین خبر به نظر می‌رسه:
دیشب یه قایق سپاه در حال مین ریزی در تنگه هرمز مورد اصابت یک جنگده که از خاک امارات بلند شده بود قرار میگیره و چهار نفر از نیروهای سپاه کشته میشن
YourAnon_Zeus
حالا این خبر درسته یا نه نمی‌دونم ولی مربوط به
صداهای شنیده شده ساعتی پیش
نیست. من هم ساعت سه چهار صبح دوشنبه پیام‌هایی داشتم از شنیده شدن صدا در قشم و بندرعباس
آپدیت:
پست بعدی: آمریکا اعلام کرد که ما بودیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75716" target="_blank">📅 01:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LX6-FqjvTlzQul_98IDgeuvmtTyAKSAOOfcVaR32HCZ5IUZ5DKmvEGo6F0XiLcFhG-ioImuQAV_28Q9ReSFcWPf0bxjyzMcP0wUoBOo6ftfmSZNLoZ1VroNsMSiOmJC2go1N86OY48xRnTQRw00YKUOnxws3Z1hVWGpikxFuPBKdxHjRrVLildb4RCochY-w93gxwtMD3D3_01nS4VKICUJcBdL6v4_LRu-7oxlsy8VzNS_FpmqmdcqvA0DLBhFUeTMGTOg_ONfRiptRvjdpyy7p1f2RcO3Pdriyg2n_zqmrQTTzSdtEhOCeBQUmMQ-MlmzzGrCIfDrkLDhwtes-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اورانیوم می‌تواند در همان محل یا جای دیگری نابود شود
ترجمه ماشین:
غبار هسته‌ای، یعنی اورانیوم غنی‌شده، یا باید فوراً به ایالات متحده تحویل داده شود تا به کشورمان منتقل و نابود شود، یا ترجیحاً، در همکاری و هماهنگی با جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری نابود شود؛ در حالی که کمیسیون انرژی اتمی، یا نهاد معادل آن، شاهد این روند و رویداد باشد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75715" target="_blank">📅 01:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">#بندرعباس
پیام‌های دریافتی درباره صدای شنیده شدن صدای انفجار:
بندرعباس سه بار صدای شدید اومد الان
صدای بمب میاد.
بندرعباس ساعت ۲۳:۴۰
همین الان ساعت ۲۳:۴۰ صدای سه تا انفجار شدید توو بندرعباس اومد. نزدیک پایگاه شکاری یا همون فرودگاه بود به نظرم
سلام وحید جان
بندر عباس صدای آزاد سازی پول های بلوکه شده میاد
بندرعباس ۲۳:۴۰ سه تا انفجار شدید
حاجی۲۳/۴۰ سه تا انفجار شدید شرق بندرعباس
دقیقا صدای انفجار ۴۰روز جنگ بود
سلام همین الان بندرعباس صدای دوتا انفجار اومد
بندرعباس حدود ۲۳:۴۰ دقیقه سمت فرودگاه صدای سه انفجار اومد.
درود وحید جان
بندر عباس ۱۱:۴۲ سه تا صدای زدن اومد
بندرعباس، ساعت 11.40
صدای شدید انفجار و لرزش
سه تا صدای انفجار پشت هم شنیدیم بندرعباس
بندرعباس 11:40  شب 4 خرداد صدای انفجار
بندرعباس ۵ بار صدای انفجار
ما سمت پایگاه هوایی هستیم نسبتا شدید بود
پدافند سمت فرودگاه بندرعباس فعال شده ساعت ۲۳:۴۵
آپدیت:
رسانه‌های ایران شامگاه دوشنبه از شنیده‌شدن صداهای انفجار در بندرعباس و همزمان در خلیج فارس حوالی سیریک و جاسک خبر دادند.
معاون استاندار هرمزگان اعلام کرد منشا صدای انفجار در حال بررسی است.
@
VahidOOnLine
آپدیت:
کانال‌هایی غیررسمی نوشتند که به فرودگاه بندرعباس و اسکله باهنر حمله شده. منابعی مطرح هم با تاکید روی غیرقابل تایید بودنش نقل کردند ولی منابع رسمی چیزی ننوشتند که لابد مذاکره و توافق به خطر نیفته. تکذیب هم نکردند. حتی منابعی هم مدعی شدند حملاتی از سمت اسرائیل یا امارات بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/75714" target="_blank">📅 23:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=T2OmIR4OSRfxoApcf6YRSoptynVn2NbR6BO0DCzQwj2nOkzDBIGcxQ4tWPstdrk1C3ixGjrXe4tS38ImGuEhRjZMga1xYKX7dAwUOYuTVJM-ioO3RFi73Rvmdy3tuSaqRDYylHQtDNnc0q2saexiUAdVad1FbPXnZOcskpMupd8uAkZLynHPssOFe4Xj6KBv2JGYhBCqXNcz4txCuoTi9YqKjRWmdOtKudLePPjzXq2dw64yyUCIx9AqCkA6Zif0E0CW4229NdDm24FrubjiqMjcUfq8n0TFS1gf1vowsOlf96nQNvBaoCzmiLF8pNjCmv9zI1CnhuolexfHP9Xi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6990989c0.mp4?token=T2OmIR4OSRfxoApcf6YRSoptynVn2NbR6BO0DCzQwj2nOkzDBIGcxQ4tWPstdrk1C3ixGjrXe4tS38ImGuEhRjZMga1xYKX7dAwUOYuTVJM-ioO3RFi73Rvmdy3tuSaqRDYylHQtDNnc0q2saexiUAdVad1FbPXnZOcskpMupd8uAkZLynHPssOFe4Xj6KBv2JGYhBCqXNcz4txCuoTi9YqKjRWmdOtKudLePPjzXq2dw64yyUCIx9AqCkA6Zif0E0CW4229NdDm24FrubjiqMjcUfq8n0TFS1gf1vowsOlf96nQNvBaoCzmiLF8pNjCmv9zI1CnhuolexfHP9Xi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه خبر داد که دستور حملات تازه به جنوب لبنان در تلاش برای «خرد کردن» گروه حزب‌الله را صادر کرده است.
ساعتی بعد خبرگزاری‌ها از چند حمله شدید اسرائیل به این منطقه خبر دادند.
نتانیاهو در ویدئویی که در شبکه تلگرام منتشر شد خبر داد که خواستار «سرعت بیشتر دادن» به حملات ارتش اسرائیل شده است.
او همچنین حزب‌الله را متهم کرد که با پهپاد نیروهای اسرائیلی را هدف گرفته است.
صدور دستور حمله بیشتر به لبنان، همزمان است با خواسته دو وزیر افراطی در کابینه اسرائیل که در همین روز خواستار تشدید حملات به جنوب لبنان و همین طور پایتخت، بیروت، شده بودند.
حمله اسرائیل به این منطقه در حالی رخ می‌دهد که در سوی دیگر تهران و واشینگتن از جمله درباره پایان جنگ در لبنان مذاکره می‌کنند.
حکومت ایران در هر دور از مذاکرات اخیر خود با آمریکا، پایان جنگ در لبنان را نیز خواستار شده است.
حملات متقابل اسرائیل و حزب‌الله در حالی رخ می‌دهد که دو طرف بیش از یک ماه است که به طور اسمی در آتش‌بس به سر می‌برند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75713" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nDk-jYbmRVddMb1BP8JJfzLM-WxhRvtFcqBJk9KNrZhJOwjk-GWlw7S6Rk933CpMLk0XTS_np9R-cTd03DwDWgytgGo0vQz-sEbP9Ql15ovUQnVhxkHm6FDFGmAUIlaGV6yQSM6TUC19N3n6BOYnFnCisjLnWNCLk-m0ui5TsMQpaJPeSkzUm4DgoJsGWnEeasr0kGYDWC9GowR8zAReuM3ZmpOvuNHYydQDkaNuN1S84u4ny5RPYxaDBauqM0PVDfLEs2_hjQzP5Mo1Xs8Q3JvNH4L7bp1mmFpoXE0w6WUbxmguZbkc3ZO4sewm_FTu284yJgnCg1NCyshi-3PpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره به نقل از یک منبع آگاه
گزارش
داد میانجی‌گری قطر به دستیابی به تفاهمی میان آمریکا و جمهوری اسلامی درباره دارایی‌های مسدودشده ایران منجر شده است.
این منبع افزود با توجه به اهمیت بالای این موضوع برای ایران، احتمال زیادی وجود دارد توافق میان آمریکا و جمهوری اسلامی فردا اعلام شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75712" target="_blank">📅 23:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdEKhL0_4xOE3aUlG-DdD83KLczlW7t2z4MFQLsL9LwioJFFiu6IiPQUNxlowMJp-mF4OK4MRUlAzKzKtnSkcvR2ZQKUV7e8FxzF5XreChwad-RVLRCEYxx1QmxvZz_HmHoiJIyzO8EU9XYzcx9cu9AkKz6fPHI1wr9Wf11Wa_hHXUKCwKN25u_45JZ-BiMbOCe3F_Gc5C2KQduyl-4yKcNYA9Q4kQ37bM8gOjSpnizSSGa1mE1fcXeGqVXLRLq7rYUgVvIm96utV8queHLq7s_jYqIT8v3xxAYVLmDZ7tYnjjEnZV1qaWIkB1s6AGu8BMSdkNYxPJzRUG1R3NF3Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پس از انتشار خبر تصویب تصمیم بازگشت اینترنت به خانه‌های مردم، چند رسانه در داخل کشور می‌گویند که مسعود پزشکیان، رئیس جمهور، این مصوبه را به طور رسمی ابلاغ کرده است.
رسانه‌ها در ایران روز دوشنبه از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌ بودند، مصوبه‌ای که برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، بود.
به گزارش سیتنا، پایگاه خبری فناوری اطلاعات، بر اساس این مصوبه، اینترنت عمومی باید «به وضعیت قبل از دی‌ماه ۱۴۰۴» بازگردد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75710" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hz3ZIZZm25T28zGPT-E3FpSFc2tFBaiPCuPasYx96b6yHpaqSIAki8OfuJXQ9bpQhSNeHU4PO-Fh2vsOUzpb8QsspnSYO0rwWX-zdYFDrJPO1QrgPCKOjoqPWDdTyICukEcbnrsfZlfCNvmZQJob3kFWB8-wmBY-MGf_OuSD1Sz-ZLHgDdvo1WOTqGU0GgxuoWFTp0B3rsm_UvVAAreVUus03QOS6QXJXRjsDkdqdtCVW4GveCtz-jnGPLjON1iQenz7kwP4PdkjwmUlrNmu6rmOUUhtg_tlOH3uFKzC4_9FLlY7eQAuJ1ugdZhHA_abTxHk2VwEfoD4tgsO9HfONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از منابع آگاه گزارش داد پیش‌نویس یک یادداشت تفاهم اولیه و نهایی میان آمریکا و جمهوری اسلامی در حال بررسی است؛ تفاهمی که شامل بازگشایی تنگه هرمز، تمدید آتش‌بس و کاهش برخی محدودیت‌ها علیه ایران می‌شود.
بر اساس گزارش العربیه، در پیش‌نویس این تفاهم‌نامه آمده است تنگه هرمز بدون دریافت هزینه از کشتی‌ها بازگشایی خواهد شد و عملیات پاکسازی مین‌ها نیز انجام می‌شود.
این گزارش همچنین می‌گوید در چارچوب این تفاهم، به جمهوری اسلامی اجازه فروش و صادرات نفت داده خواهد شد.
العربیه افزود پیش‌نویس توافق شامل تمدید ۶۰ روزه آتش‌بس است و امکان تمدید دوباره آن نیز وجود دارد.
بر اساس این گزارش، آمریکا همچنین متعهد شده محدودیت‌ها علیه بنادر جنوب ایران را کاهش دهد.
منابع العربیه گفته‌اند بخشی از دارایی‌های مسدودشده ایران نیز بر اساس سازوکاری مشخص آزاد خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75709" target="_blank">📅 20:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GDR2I24NuyWlGUAeh1YeFOFFD9rWfLWzQMjTIvT-9Gwz-eHxdhfWQiRE_AqmKD9zEiHRHPYKtl6I-_sjrjA4MEBM6Y2gSqVrd6o6u3u9wqw_IkqRMnnZu10PALcTuzFetMHIGOkABpVjhEgWOiiml8RegoJcui1rNTrTiQEAokRmApjQbOjJGBUakITZ83dhd4X7nkII1b6UtUPSiSM-skYSCL_uqs0lkQgz-nRkl-sLBywkWcOLDtpvAXmNwqIVsFpOyo-5z2RBT9AfgGF8bbJoMEz8UP7Zxs6jApNdUJZyicQM-ntYbf-Ho1pRtUaG9h_0PNIttFAnhzRYK7uV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avnrvHzybtnUtp5rQLWRg-b0h27gRN8WF96DQJa1CzbzX8sZKBpvSJXz7ziTAarYUYrt1TFG0jC33QCtRo9NL3-FhE6HPtQOH0OllfVYC5sg7mVdp8TMtKcjmA9qpO0n3rRUMEyWlwY48G5204psiOhDo_jsdwMESiPvIUTBS-s6REqP0kbnq_kdTOjxeJJoDT75RDL4DpBvs4F_QZT0CFa8pOl1rDp5CDjR80RcwVNqLmSK7WSXgnyq7N7D8_G_4DonyPrauPKSQj7JshjzA0GK_J8dJP_mbqXW1CH7R5E-Hlcexl83HcKCTJPHE-WFskzLVKVvSLfQN2xRegb6BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی، در پیامی با اشاره به «میدان نظامی، میدان دیپلماسی و مردم مبعوث‌شده حاضر در خیابان» نوشت: عقب‌نشینی در کار نخواهد بود.
او تاکید کرد: بیش از هر زمان دیگری به وحدت و انسجام نیاز داریم تا آمریکایی‌ها و اسرائیلی‌ها مایوس شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75707" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oda1hd8kbyTFaPRrV-8B6phFQ8pAeCj2Iz3TrDlzHu4IsiTF1ZiSn4jeCHCl_E9lD0ntgJUzx4fCDKKk1ZrbsbSMmHFFthrL892iB-miyqMi3xQpI0KHiEh9B9v4w6C4IdVDNMctC8R9JPTOVJGFSKWvZKnw2OK_j2fM6_06iN3-np7YyUXFW70AxWxiqnmns1-h_8lGlOnHGx_-09mG5nmt5VKrNTLdKd4aC_3q8JaS75qZvxVhlBJAhFEHbQVUSOPIDWG-s0xturORVrVJFrsKChSdFZgf9nOEefal4cd3NrOmySf3TqeNhhUaerfctbrXngCAUvJND5NL5AOYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IJcYcO2YiCsM-Xti96CZmiAzcX668EU0p1oOC1c0fHNNK844zAWrflWoACKwJe6Y1fwni3y4m6q6_J2OQTBJK9UWn8zWqmRJSGSNfYIeMnk0N5WvEMKPiGYbv4LwgbgKREEeI0-4NSOYtHonpt7D7XyUc-w1PMwNmk3G6sndNMq3AqmnefIrpPUUfFWp8QazoyAQdRc5tPINwPUA2eaGFfTDqZ47DK2Ta9oYVGMhRxy_f53kRzB6Fjfv_kFpV9UPtel-jAZqKF4Vr2i9HctuuOSAlz7saXsIN5iQGRUPyWFUulmjRjtaTZxtZQP0fg0E5erXgVtcV-qn4hmzQCZkDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ از اکانت بقیه بازنشر کرده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75705" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DTgXMIXUI4wiQTRSyf9ArrAhcjX05lNAqs_KqDtOV9Bk2QioWj_e_rL_5og17LAGWCvVqn7OfKc7795dgUcoLtnVE7YmoSx463OnYfI9bNQ02VFenaVYRnteinzKassQpuMeUQ0PfZvtjTTperwRaAyJntSWPp-JlZkLREb_fWjCe4xg-8Nd0GhTDaPPOioMg-ipcAmwICL9a8c3buznKP6LVbpEaHstpWk1PqSC3Wu3-YrBJxSYEwsVxvmJ4jhY9VzWiT9DOCCE4NiRe6X8Hw9-XzAhFnWJiV9u98s_rUcJiUaMuXVOyMPwI0bRyD-JBVhAQ-k0gM6HIymiyv85kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mb1rkoI8xtklyHDuzzMPltxjLEc8puNXrGFF_RFCSSx90QnQSg6O8ShSroIbLbA8JiJSfdjm53DxcQD7S-LIJYRgyLGjJZgc75Y9dKrXT5NK4SKiog_spaU0cjC9TdghXGVVDbX79R8HaWvrXq6rajSb-044WJOskh-SCK2lYeP7mnPWW28WUTogcgey3XuxxtIUNN3RRus61aOfu-5Tt08eyTiyjoyHKAmIE94-KeRRBGcDoLRmhXUosaKfWws7G0yhstS65xWe1nwABCaDmm-LLuY9bqTGjpa1ZtZg-nVaRsMYImKMEnnooSM86_YyKbPf4bjRPQggioPEuLR1sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه در تازه‌ترین پیام خود در شبکه اجتماعی‌اش ضمن خبر دادن از پیشرفت «خوب» در مذاکره با ایران، از تمام کشورهای دخیل در این مذاکرات خواست پس از حصول توافق با ایران، بلافاصله به پیمان‌های ابراهیم بپیوندند.
پیمان یا پیمان‌های ابراهیم طرحی بود که دونالد ترامپ در دوره اول خود برای تلاش در راه عادی‌سازی روابط میان اعراب و اسرائیل آغاز کرد و موفق شد تا چندین کشور از جمله بحرین و امارات متحده عربی را هم به این کار ترغیب کند.
حال رئیس جمهور آمریکا روند توافق با جمهوری اسلامی را به این طرح پیوند زده و به گفته خود این «خواسته اجباری» را با دیگر کشورهای عرب خلیج فارس و همین طور ترکیه مطرح کرده که به‌فوریت و همزمان به پیمان ابراهیم بپیوندند.
@
VahidHeadline
دونالد ترامپ در شبکه تروث سوشال نوشت که پیوستن جمهوری اسلامی به پیمان ابراهیم، می‌تواند به «اتفاقی تاریخی» تبدیل شود.
او افزود که در گفت‌وگو با سران عربستان سعودی، امارات متحده عربی، قطر، ترکیه، مصر، اردن و بحرین، تاکید کرده لازم است همه این کشورها به‌طور هم‌زمان پیمان ابراهیم را برای عادی‌سازی روابط با اسرائیل امضا کنند.
ترامپ نوشت: ««کشورهایی که درباره آن‌ها صحبت شد عبارت‌اند از عربستان سعودی، امارات متحده عربی (که هم‌اکنون عضو است)، قطر، پاکستان، ترکیه، مصر، اردن و بحرین (که هم‌اکنون عضو است). ممکن است یکی دو کشور دلیلی برای انجام ندادن این کار داشته باشند و این پذیرفته خواهد شد، اما بیشتر آن‌ها باید آماده، مایل و قادر باشند که این توافق با ایران را به رویدادی بسیار تاریخی‌تر از آنچه در غیر این صورت می‌بود تبدیل کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75703" target="_blank">📅 18:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GDpTMnX1n-xnPIFSyGYJqOEb6z36nQuMbnRa1KRq20TS0oM2Wm64TyDQE_i0nHXJkAWaYyqv84G9AxaDav_NbWvoH-Ih8CoCY0M92sGRpe_Hiync5QCK0kdJFdY213x2DkVeutEM9jtvpxlvEt9RhheDvipjitaLwiWdI1WUAKrveOziKpao7W3hUeraf0ZKtC3LhWnSGnKRie-BvFKIdvUeiuUmw0nLj_CHKX9tXroTlCSdQ98aG4WxLGKUpHuRIUj52DEa04GriSb1zKr3hoUUZfzRYeF35wrVDNSJOpRZeCFC30e_Zqt-ximJpofznL1A8rutzt6aX0XA4CFKmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SQF4pg8cSin4OwPLNT-IWQ_P-QlNSduiknKm_iR2ilG4aF1PcHekAlcvyNNHBbGmGl8YYFj5hotPVpzuZBEDS0XUt_4FD1fSXeUe91tjgA1KT6Y8m9wZLgIiJ_dMvs5DDD-Zs4s-TurduDq3O_v2Xx5LlnpA_QDCD_TBDVhxjSMZwmQAUlmpjwZFC-h-O4ibYw0LzGkCdM5iW1ppp2Ugmd0aJORtLWIPj97odh_-Vy8nSJmyH5tBz_9pZapG8rrZqNiUnzzLzSDXJt6c89XqSrpp4g8W06YkiMaB9lGkrYrVFQr8D69TjULj1peUHepMpZCQui7MNKwfPITrQAGT7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری‌های رویترز و فرانسه به نقل از یک مقام آگاه، از سفر غیر‌منتظره محمد باقر قالیباف و عباس عراقچی، مذاکره‌کنندگان ارشد ایران، به دوحه خبر داده‌اند.
بر اساس این گزارش‌ها، رئیس مجلس و وزیر خارجه ایران برای گفت‌وگو با نخست‌وزیر قطر به دوحه سفر کرده‌اند.
رویترز نوشت که این گفت‌و‌گوها عمدتا درباره «تنگه هرمز و ذخایر اورانیوم غنی‌شده» ایران است.
رسانه‌های ایران گزارش داده بودند که عبدالناصر همتی، رئیس کل بانک مرکزی ایران، برای «بررسی آزادسازی اموال بلوکه‌شده و در راستای کمیسیون اقتصادی مذاکرات» به قطر سفر کرده است.
هیئتی از قطر هفته پیش به ایران سفر کرده بود.
یکی از خواسته‌های ایران در مذاکره با آمریکا آزاد شدن منابع مالی مسدودشده‌اش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75701" target="_blank">📅 18:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvDSbii0CAf9l_0uTPDts2rNEy7hZ4lOuZbLwqhA-BeI-Ut0YCoapD3sPFjTMZ2XfId0F3XoLJefRoeBIS1PGtTKSl5Mu0fPyw5we4uwqW82rExUyyfhByaz0rLL89GRx8kZUtmjHO3bIiQsn6GN7MsrXYcOZPgsjmXAQpkZDdA9NjPFkb6-gG1MGz5u4tSa1AHbNS85PnGMKDLWIMKn9EE7U-bHsoFalgI39xRbTZnAXxx4OUkC_87J2_YvsRjr1kq89-Qtoq3-1XujCyvDnawQi4o4asO8I1ezYjleqI20vJjubxBoU8fjU81AcCLrIvqIbKH6Tv4kt-2Il3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پیامی در شبکه اجتماعی تروث سوشال گفت توافق احتمالی با ایران یا «عالی و معنادار» خواهد بود یا اساساً توافقی در کار نخواهد بود.
آقای ترامپ در این پیام، منتقدان خود در میان دموکرات‌ها و برخی جمهوری‌خواهان را به باد انتقاد گرفت و گفت آنان «هیچ چیز» دربارهٔ توافق احتمالی او با ایران نمی‌دانند و حتی دربارهٔ موضوعاتی اظهار نظر می‌کنند که به گفتهٔ او «هنوز مذاکره نشده‌اند».
ترامپ تأکید کرد توافق مورد نظر او با ایران «دقیقاً نقطهٔ مقابل» توافق هسته‌ای برجام خواهد بود؛ توافقی که او بار دیگر آن را «فاجعه» خواند و دولت باراک اوباما را به گشودن «مسیر مستقیم و آشکار» ایران به سوی جنگ‌افزار هسته‌ای متهم کرد.
او در پایان پیام خود نوشت: «من چنین توافق‌هایی نمی‌کنم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75700" target="_blank">📅 18:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbcCX26k82dq07qmQ6wo8O7ZLVTkfliu0rqkwxu6Xl13NkaIgtkOE0J5jPA3erTRtd7Uh7G5LnT6t_Wy67XZRf014UdCYa9jQVvjZBiyllVwOwBLUb1UYlmERbgpM_aLIeZd4qbZqcGlyxVova3slZMl_5X15WhciJKZHIPkILhZKuTLpVNtqWS4M43TGLqhmNKlFrWq8GgrbuFpRgN6Xadzk5BgPN6ueGAs1FD3Tg-FeqwXgOAwSdI2ZXW9JYzmfZ3DjyXPph628p6bGEFrxvlxNsv8DICVkc9cR5UcCbpAcqdKSAW7IzNjR-Kfe_MXW8U8tYlyxR_0al1y5YU7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از تصویب مصوبه‌ای «جدید و مهم» دربارهٔ اتصال دوباره اینترنت کشور به اینترنت بین‌الملل در «ستاد ویژه ساماندهی فضای مجازی» خبر داده‌اند؛ مصوبه‌ای که هنوز برای اجرا نیازمند تأیید نهایی مسعود پزشکیان، رئیس‌جمهور ایران، است.
خبرگزاری فارس روز دوشنبه چهارم خرداد گزارش داد چهارمین جلسه این ستاد به ریاست محمدرضا عارف، معاون اول رئیس‌جمهور، برگزار شد و در آن «مصوبات مهمی» دربارهٔ اتصال به اینترنت بین‌الملل به تصویب رسید.
فارس به نقل از یک منبع نوشت که «برقراری اتصال اینترنت بین‌الملل» با ۹ رأی موافق و سه رأی مخالف تصویب شده و برای تأیید به دفتر رئیس‌جمهور ارسال شده است.
خبرگزاری تسنیم نیز با انتشار گزارشی مشابه نوشت مصوبات این جلسه پس از تأیید نهایی رئیس‌جمهور، برای اجرا به وزارت ارتباطات و فناوری اطلاعات ابلاغ خواهد شد.
در همین حال، سیتنا، رسانه تخصصی حوزه ارتباطات و فناوری اطلاعات، به نقل از «یک منبع آگاه» گزارش داد که در جلسه صبح دوشنبه «بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴» مصوب شده و در صورت تأیید مسعود پزشکیان، جهت اجرا به وزارت ارتباطات ابلاغ خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75699" target="_blank">📅 18:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOz-DwNhdcMd34a5NenCyr2Ie4HVRXLa_hs-OcygQKdFnyxe_KiaIbkIk3_m6cffmQh3T4cMxV74yPC4tBSbRMf7L4s9NttEaC9Rv8xbmqflElyOOpkLo7OT4GMqBgVqB-h1kYwX4n3gAyrNygn-kW7Uf47J8m2DggHDNNu1fq9yLnhVPNxW0lM9-zY1Kjs77b-JDZ9qy03-aYLq9m4rEZs_DUIw6bUFFCYm2qJtC-FI3usMKjReXtOOE9JV5f0LOEh5S09RSfre7-bBqvptisSLglgGAHEAbfFn8GQU9L7TApnO0fxpej_tKERop7_qYBYyK1uYOGEvTy-tIgc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از «حسین کرمانپور»، رییس مرکز روابط عمومی وزارت بهداشت، گزارش دادند که جراحت‌های وارد شده به «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، در جریان حملات اخیر «سطحی» بوده و مشکل جدی برای او ایجاد نکرده است.
کرمانپور گفت رهبر جمهوری اسلامی تنها از ناحیه صورت، سر و پاها دچار جراحت شده و این آسیب‌ها «منجر به قطع عضو یا ناراحتی خاصی نشده است.»او همچنین مدعی شد که هنگام انتقال خامنه‌ای به بیمارستان، پزشکان از او خواسته‌اند روزه خود را بشکند، اما او تا زمان افطار روزه‌اش را ادامه داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/75698" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdKWQD6vB3lFE_cFmrWGHd3KOj1_U5MFHfeBvUoxyo61WfNFm_GRkph9C5DBthQEuHJlOHiKqcKVQZL9o46csU1y9cc8qQXujWl-gZ2enzJL-V5r4CQVs1ZlY7H5CM9TZY2TcMoCAx6q_OmULyP9ACckU3JcteIQj-hb9KrGxrCmyPnkTJRp-LjJ-r2pNEObNVIcMKzgvkdPYc5_627-SHxeD7xEYkhK0vfwxW4rqsIhHpEGxZhBJCHpFnokn_W4VwQq6mNh3TBYOaEO3VOwUkA5pNaHdORQ0Sh_L5t3XhZJeGJl6qxN6WQ-162nkGdWbRqElZMz6ZHBuECqdsgOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید که سفر وزیر خارجه به نیویورک برای شرکت در نشست شورای امنیت «منتفی» شده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران، دلیل انجام نشدن سفر عباس عراقچی را «مشکل روادید» عنوان کرد.
آقای بقایی چهارشنبه هفته پیش درمورد حضور آقای عراقچی در این نشست گفته بود: «این سفر به نیویورک احتمال دارد انجام شود و البته ممکن هم هست انجام نشود، چون هنوز قطعی نیست. دلیلش هم این است که هم باید روادید صادر شود و هم ممکن است اولویت‌های دیگری داشته باشیم.»
چین به‌عنوان رئیس دوره‌ای شورای امنیت، سه‌شنبه ۲۶ مه یک بحث آزاد در سطح بالا با موضوع «حفظ اهداف و اصول منشور سازمان ملل و تقویت نظام بین‌المللی متمرکز بر سازمان ملل» برگزار خواهد کرد.
این جلسه به ریاست وانگ یی، عضو دفتر سیاسی کمیته مرکزی حزب کمونیست و وزیر امور خارجه چین، برگزار می‌شود.
چین این نشست را «فرصتی» برای همبستگی و اجماع کشورهای عضو توصیف کرد تا «تعهد راسخ خود را به حفظ اهداف و اصول منشور سازمان ملل متحد مجددا تصریح و نقش محوری این سازمان را در نظام بین‌المللی احیا کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75697" target="_blank">📅 18:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrJVqjXu1w1r3jb7JHjUE55HIeNqrDB9ZQ7drYrmfz0tauVcQORMjz0v9jVsP86a7AlK2yYEC7CWUAKRauLyVdPaiQl6SbCFN3No0BH1BMwgDveVNeTP7xtAyLAz7nki4JWQSU6F0kUO04YiGvQfG0YqUhlkG4PTt8e0aPJip8t3Jl6DjRTEE_dfBy1purZNB48uHRhm0QQC6lIpUaxW_3wGebPJmxaWWwvRVD7l0n2xC7IWRos41WQIgJknQ_9BkXPnX2CjZ1qhc_3AoiY6tMlOYwN12D1AomiQxWptBsFNs0rnJEonloE2H1rZQIjSiEjkPhjnKLiF-bpwnCbyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۲۶ اردیبهشت‌ماه ۱۴۰۵، «جانا سعدوئی»، زن ۱۹ ساله، مادر دو کودک و اهل روستای تاریمیش از توابع بخش قطور شهرستان خوی، به دست همسر خود به قتل رسیده است.
به گفته منابع آگاه، همسر این زن پس از وارد کردن ضربات مرگبار، تلاش کرده است ماجرا را به‌عنوان «خودکشی» جلوه دهد.
با این حال، نتایج بررسی‌های پزشکی قانونی و تناقض‌های موجود در روایت‌ها و اظهارات مطرح‌شده، ابعاد این قتل و تلاش برای صحنه‌سازی را آشکار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75696" target="_blank">📅 18:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_LGAFIpxrnzD0tDaGeufLR9hZooWhCLS3YLcioWR-4DcduDVg0784_HZ9CNFiIXTJaK2iu-IzQHYKgbUkwwcVvKtpspq_2GpXQRqlOlZJi6pdlD2o-GMijveSFHSjnYwex5xyGsUhhJTcGoH0mh6zcvuuxyCVaG79jrRiNAV-IneXnuRh8CzxWjZc9lWKia-9eZMisApmNABw3W-nlkA2A4iMmv10BT3dQX1PF8rbm7G7CylyGaIrJ4goIMciuHIBtwm0khzdKIKmX3dFKsup-flqeXkYfu2nM8_fBwK-CpIPMgJVtt1SkNIRJBSQHlc_zY1jCahXk7z85a6ub9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ایالات متحده، روز دوشنبه چهارم خرداد گفت که واشینگتن در مذاکرات جاری خود با ایران، «هر فرصتی برای موفقیت» به دیپلماسی خواهد داد.
مارکو روبیو که اکنون در هند به‌سر می‌برد در جمع خبرنگاران گفت که مذاکرات با ایران همچنان «در حال پیشرفت» است و خوش‌بینی محتاطانه‌ای نسبت به توافق احتمالی برای بازگشایی مسیرهای کلیدی کشتیرانی و از سرگیری مذاکرات هسته‌ای ابراز کرد.
او که روز گذشته از احتمال توافق با ایران تا پایان روز یک‌شنبه خبر داده بود، گفت: «همه ما باید مطمئن باشیم که یا به یک توافق خوب خواهیم رسید، یا مجبور می‌شویم به شکل دیگری با این مسئله برخورد کنیم. ترجیح ما این است که یک توافق خوب داشته باشیم.»
دونالد ترامپ، رئیس‌جمهور آمریکا نیز شامگاه یک‌شنبه در دومین پیام خود درباره روند مذاکرات با ایران اطمینان داد که توافق احتمالی با ایران «خوب و درست» خواهد بود اما هیچ کس درباره محتوای آن اطلاع ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75695" target="_blank">📅 09:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXgbYbcHsIBKU1VHqkSpY9tvq84k4rjObtPJh-AoEbc3IS211dnUqW72N-uHiblEauO2D43-cBHZPCX9Y9qF4rNS-cj5bbEdTtnfEKF1gq24LvOFMmtGNI3t0VwHifSdEt63xr6fle3jAjnINGPg2VWH67522_rTxpL7GUtERjYRL-LV64YikGvyyYY1UFzx4z_VL9BEmwJFyfxEEF01NqrWUnq5mFF2Y3_Wylst48BJjPhkKGO82eavlX6H2bDDek4ffeD_32l1_p-TFyODs5m74Voam7Ht_K-Ex52OCYGuotbt1ZMK1UqttkfrbSAh58NnImwEvqVvFIvuS6VjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه قوه قضاییه جمهوری اسلامی اعلام کرد حکم اعدام «عباس اکبری فیض‌آبادی»، از متهمان پرونده اعتراضات دی‌۱۴۰۴ در شهرستان «نایین» اصفهان، صبح روز دوشنبه ۴خرداد۱۴۰۵ اجرا شده است.
«میزان» مدعی شده که عباس اکبری از «لیدرهای مسلح» اعتراضات در نایین بوده و در جریان حمله به فرمانداری این شهر و برخی مراکز حکومتی، به سوی ماموران امنیتی تیراندازی کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75694" target="_blank">📅 09:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbZC-4mMHMl-4niJUu7LUkfGNG95X-ftSNiZjT1A03D0UGcIuNPuwGkgUgGxi7jV9cpYnNwcFZYxIqWrBrBUUc8nGMNvPez0KgVCIlUCA1MJ05xxo_BRzeY1Dwic18LNPAGC6lktfmRwrf79TKGSHDvctZINijzlf7P4Fwv66G0m4ND00H4T4F_Uwl8tQX_uR5gvpotAzQzH3CxZiLMpQzQdqHXSULoa1JR_oxdzPjqK6Q2np4B0Xj0eP_sg8VFsXb6jsjxZq_b4wNcPk8m_QhsQvforK-G0k1a6x_wKiUM5OGM8VFNvtgscNWzYekUT3E5TBs8ELJ5ggjgYQiLEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس: مجتبی خامنه‌ای در مکانی نامعلوم با دسترسی کم به دنیای خارج پنهان شده است.
ترجمه ماشین:
اطلاعات نهادهای امنیتی آمریکا نشان می‌دهد که رهبر عالی ایران عملاً در مکانی نامعلوم پنهان شده، دسترسی محدودی به جهان خارج دارد و ارتباط با او تنها از طریق شبکه‌ای پیچیده از پیک‌ها امکان‌پذیر است؛ این را مقام‌های آمریکایی آگاه از موضوع گفته‌اند.
به گفته این منابع، مقام‌های ایرانی که مجوز همکاری با دولت ترامپ را دارند، برای برقراری ارتباط در داخل ساختار حکومتی خودشان با دشواری روبه‌رو بوده‌اند؛ مسئله‌ای که یکی از دلایل اصلی تأخیر در روشن شدن جزئیات توافق احتمالی با ایران و توافق‌های قبلی بوده است.
دو مقام آمریکایی گفتند وقتی آمریکا جزئیات پیشنهادی را ارسال می‌کند، دشواری دسترسی به رهبر عالی باعث می‌شود گاهی پیش از دریافت پاسخ از سوی آمریکا، تأخیری طولانی رخ دهد.
سخنگوی کاخ سفید از اظهارنظر درباره اطلاعات مربوط به محل حضور رهبر عالی یا روش‌های ارتباطی ایران خودداری کرد.
یک مقام ارشد دولت روز یکشنبه گفت رهبر عالی با چارچوب کلی پیش‌نویس توافق فعلی موافقت کرده و دونالد ترامپ، رئیس‌جمهوری آمریکا، در تروث‌سوشال نوشت که انتظار دارد ظرف چند روز آینده پاسخ نهایی اعلام شود.
مجتبی خامنه‌ای، رهبر عالی ایران، که در حملات آمریکا و اسرائیل در عملیات «خشم حماسی» زخمی شده بود، برای جلوگیری از حملاتی مشابه حملاتی که به کشته شدن پدرش، آیت‌الله علی خامنه‌ای، منجر شد، تدابیر بسیار شدیدی اتخاذ کرده است. علی خامنه‌ای از سال ۱۹۸۹ تا ۲۸ فوریه بر ایران حکومت می‌کرد. مجتبی خامنه‌ای از پیش از آغاز جنگ تاکنون به‌طور رسمی در انظار عمومی دیده یا شنیده نشده است.
یکی از مقام‌ها گفت اطلاعات به‌دست‌آمده توسط نهادهای اطلاعاتی آمریکا و اسرائیل از داخل حکومت ایران، امکان شناسایی و حذف بخش بزرگی از رهبری ارشد ایران در جریان جنگ را فراهم کرده است.
منابع گفتند در حال حاضر بیشتر رهبران ایران نور روز را نمی‌بینند، هفته‌ها در پناهگاه‌های به‌شدت مستحکم می‌مانند و جز در موارد کاملاً ضروری از صحبت با یکدیگر خودداری می‌کنند.
یکی از مقام‌ها گفت: «تماشای تلاش آن‌ها برای فهمیدن این‌که چطور با هم حرف بزنند، تقریباً مثل تماشای یک سیتکام است. آن‌ها کاملاً به ستوه آمده‌اند.»
شدیدترین تدابیر احتیاطی از سوی رهبر عالی اتخاذ شده است.
بر اساس طراحی این سازوکار، حتی مقام‌های عالی‌رتبه حکومت ایران هم نمی‌دانند او کجاست و هیچ راهی برای تماس مستقیم با او ندارند.
در عوض، پیام‌ها از طریق شبکه‌ای از پیک‌ها منتقل می‌شود که با هدف پنهان نگه داشتن محل حضور رهبر عالی ایجاد شده است.
یکی از مقام‌ها گفت: «به همین دلیل است که می‌بینید برخی می‌گویند: "رهبر عالی با چارچوب موافقت کرده" یا "منتظر پاسخ درباره نکات نهایی توافق هستیم." هر اطلاعاتی که به او می‌رسد، از پیش قدیمی شده و پاسخ‌های او با تأخیر زیادی همراه است.»
رهبر عالی در قالب کلیات با زیردستان خود ارتباط برقرار کرده و به آن‌ها جهت داده است که درباره چه موضوعاتی می‌توانند مذاکره کنند و چه موضوعاتی نباید مطرح شود.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75693" target="_blank">📅 03:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yd4b0zAjQO7yf8wm-BQzf9dJc_0mq1PSmpkgyG8_Kt6xmC-uxx0KoVCiW9hcHw4OSZlOzK1kmPiR8ArPIH6lvaXVnKCQNdywP_cFYNy6wqkwM7aNW8IaXVLIbj4mYz_9vSRCv6m2NcCKVX-HMlOjYJnGxyZP-h3a_EZTUUix5-PuM6ZHBr3YvTM6sckWZXP9ZwOQZCGoYmhXVjaRIYLAGE0_uerHwB5TuQlePxViXdo2jf9DfoCKi32URxubKZHWXG4LcaJ5a7kmHzGe0q8vw9THxc6eFmZwB2zUinEAGFIrx7eQnIjTnnEeEeTPYzDtr3D5vzMKHKuQ1z_j6OqJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I2JdVn_hv-_S43tJVxHG4lb4UxXT_JQKXGEt4ux2svaw9G8u13Lev3Vmus_rxu3IhfirKPtZdewHIUZhDLswgnBqmac_Os19IY0WuOPPVufi1XuZP6iiJHutE5JL_F4QPpVeGdmwcbbAlxAn0BvzoeowmieD5_jldLAbHB81BuapCna1vcHA0j2h7OT5BiLZiHjndtI6Ofh0HQ5ZnjxohVeVdkupySSVB1o8N0JcIZ9v-N77isBj9WLzwah0Ts_na06EeycbqiQBVMemiX2_f2xEYKMLH6kO2LFJ2AGpiKkyaXYGNZVCrdFpCBPAbVGvvbd6LO7qj99Xr5ULc_UzKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با شبکه «فاکس‌نیوز» اعلام کرد که واشنگتن هنوز به توافق نهایی با تهران دست نیافته است و هیچ توافقی امروز یا فردا امضا نخواهد شد؛ این مقام مسئول با تاکید بر این‌که آمریکا تسلیم خواسته‌های طرف مقابل نخواهد شد، افزود که تمایل و تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، این است که یک فرصت ۵ تا ۷ روزه دیگر به مذاکره‌کنندگان بدهد تا توافق را به مرحله نهایی برسانند.
بر اساس این گزارش، یک توافق چارچوبی با ایران تا روز یکشنبه تا ۹۵ درصد پیشرفت داشته است و اگرچه دو طرف بر سر کلیات مربوط به ذخایر هسته‌ای تهران و بازگشایی تنگه هرمز به توافق رسیده‌اند، اما چانه‌زنی مذاکره‌کنندگان بر سر جزئیات و «ادبیات دقیق» متن این تفاهم‌نامه همچنان ادامه دارد.
@
VahidOOnLine
تسنیم، خبرگزاری وابسته به سپاه پاسداران، روز یکشنبه به نقل از «یک مقام مطلع» گزارش داد: «هیچگونه خوش‌بینی به آمریکا ندارد و رد و بدل پیامها از طریق میانجی پاکستانی نیز دائماً با در نظر گرفتن بدبینی به دولت آمریکا صورت می‌گیرد».
تسنیم به نقل از این منبع در ادامه نوشت: «تا این لحظه تفاهم نهایی حاصل نشده و چالش در بعضی بندها ادامه دارد، اما حتی اگر تفاهم اولیه‌ای نیز صورت بگیرد، به معنای تغییر نگاه ایران به آمریکا و اطمینان از اجرای تعهدات این دولت نیست. آمریکایی‌ها سابقه بسیار بدی در مذاکرات دارند که بدبینی ها را تقویت و تثبیت می‌کند. پس حتی اگر تفاهمی نیز صورت بگیرد ایران در طول روند پس از اعلام تفاهم، اقدامات آمریکا را زیر نظر خواهد گرفت و در صورتی که آمریکا در آن مرحله نقض عهد کند، ایران اهرم‌های خود برای مواجهه با آن را حفظ خواهد کرد».
تسنیم پیش از این نیز از «کارشکنی‌های آمریکا» در بندهای تفاهم از جمله در آزادسازی اموال بلوکه شده ایران گزارش داده و نوشته بود: «همچنان امکان منتفی شدن تفاهم وجود دارد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75691" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnadlp-glmC76PS6Q7ZyeW1Vkb7YQuJnMS3jta5THLEToktRYLkOQ_2YPQhHlNKChtBhbaoxfOcKC3zDSvl1jeJiZJsH8kw8svgF0X0_C8AB6b9od2qDwQEYWp8S6Z1HD65I6krwiJBAjnQvwzj4b0jLuKHeAD9CcdoWkqt3lgZ2yiITSsfa4aKkvifCVn5zVY8hk-3KDsxajVErNl5__qA7ap8W2XlzC5oBlI9ktwcmDgNtF4nIZAyB_75AT_MDJ7FJMY8XQWlv4-e-aqKxa8XLXvKe5XhOZgwZuok2c9ip4eoPymcbEKIOyB6zxgGM70HBsTsdw9t8G_Z7kNsMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری حکومتی تسنیم، شامگاه یکشنبه سوم خرداد ماه، به نقل از دادگاه انقلاب تهران اعلام کرد، رای اولیه پرونده موسوم به «بچه‌های اکباتان» صادر شده و طی آن چهار نفر از «متهمان اصلی» به اتهام «افساد فی‌الارض» به اعدام محکوم شده‌اند.
به گزارش تسنیم،  اتهامات ۹ نفر از متهمان این پرونده که به دلیل کشته شدن «آرمان علی‌وردی» بسیجی حامی حکومت زندانی شده‌اند مواردی چون  «وارد کردن ضربات چاقو،اخلال در نظم عمومی، اخلال گسترده در امنیت کشور، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور، توزیع کوکتل مولوتف، وارد کردن ضربات سنگ به آرمان علی وردی، ضرب و شتم آرمان علی‌وردی و فعالیت تبلیغی علیه نظام» عنوان شده است.
بر اساس این گزارش، دادگاه انقلاب تهران متهمان ردیف اول تا چهارم پرونده را به اتهام «افساد فی‌الارض» به اعدام محکوم کرد و متهمان ردیف پنجم تا نهم نیز به حبس از یک تا پنج سال و مجازات‌های تکمیلی محکوم شدند.
@
VahidOOnLine
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی چهار تن از متهمان پرونده «شهرک اکباتان» را به اتهام «افسادفی‌الارض» به اعدام محکوم کرد؛ این در حالی است که دادگاه کیفری پیش‌تر اعلام کرده بود انتساب قتل به متهمان به‌صورت قطعی ثابت نشده و امکان صدور حکم قصاص وجود ندارد.
خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، روز یکشنبه در گزارشی تلاش کرد صدور این حکم را توجیه کند.
بر اساس این گزارش، رسیدگی به پرونده در دو مرجع موازی انجام شده؛ دادگاه کیفری به اتهام قتل رسیدگی کرد و دادگاه انقلاب به اتهامات امنیتی از جمله افساد فی‌الارض.
میزان مدعی شد که پس از آن‌که کمیسیون پزشکی قانونی و اداره آگاهی هر دو اعلام کردند تعیین فرد وارد کننده ضربه مرگبار به آرمان علی‌وردی ممکن نیست، دادگاه کیفری سه تن از متهمان را از اتهام مشارکت در قتل تبرئه و سه تن دیگر را به پرداخت دیه و حبس محکوم کرد. اما در مسیر موازی، دادگاه انقلاب همان متهمان را به اتهام افساد فی‌الارض به اعدام محکوم کرد.
به گزارش خبرگزاری هرانا، میلاد آرمون، نوید نجاران، مهدی ایمانی و سید محمدمهدی حسینی چهار نفری هستند که حکم اعدام برای آن‌ها صادر شده است.
چهار متهم دیگر این پرونده یعنی امیرمحمد خوش‌اقبال، علیرضا برمرزپورناک، علیرضا کفایی و حسین نعمتی نیز هر کدام به پنج سال زندان، دو سال حبس به اتهام تبلیغ علیه نظام، دو سال منع فعالیت در فضای مجازی و دو سال منع اسکان در تهران و البرز محکوم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75690" target="_blank">📅 00:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hbsMZTNV4isyCBR8zHIYlnKecivhE_BTtg56dc2QZlduasRKw9m1a-wV4qgods6cg0NUohGFbdTj9j6L4q3wG7WdoI2kxmbVc8hm4cELepWWUXvNgjFgwYngg_XlWmWfjNj3FBkgF1DLjw_BFVO5dfyrtbRF-mVHlXN0rXNHgSOXNbQYGVhpRK_wi5Sck6uHMx9P7ARJzMXZMDstjKBg8roxqm3TORnYxJwa0AYtDaR_sSMSRldQC7Xat-qI0dHuEW_HEqlVMOUtx04FrxUELPWD_ogqn6mPHr5Zw8JvqYz9YRTVS-_g39-pTnwm8dn3NMi5S_OADbkHtmG4zBB_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ
روی تصویر بمب نوشته: از توجه شما به این موضوع سپاسگزارم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75689" target="_blank">📅 23:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWUJEfawyVqrFLxIA5rsIt-kNrcQTmMv63u3rhthX6DIqnB-i5eDPhnPOg8eJMD_sgS2r15eFR7njH6j78V0sCIV5xvTRs6gdHRRWZSrJ4JpaUeI8aEI-8yto8htIlnGF3DtLOLSY41syqr8edVLbHLL3BIaz5eNN4jzIraKqf6nAPfhw5YVrPl9TmdzTEuWNlOLrhgwrs8lhD3TspNdMMXOgvkKP6WRC9HKnSVARiL7iXrXGLAv1lJrkHpg7n-G8EnIViGC2n_UnBF2FfNWIuXTF0yCi8Ae7Dbi-2OpaMkjWdHH9gqQENX1HwPEc5r-unbUTqTW91JjdCr6UWB35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در گفت‌وگویی کوتاه با نیویورک تایمز گفت: «ما موضوع را به بعد موکول نمی‌کنیم. مذاکرات هسته‌ای مسائل بسیار فنی هستند. شما نمی‌توانید یک موضوع هسته‌ای را در ۷۲ ساعت و روی یک دستمال کاغذی حل کنید.»
او افزود: «در حال حاضر، هفت یا هشت کشور منطقه از این رویکرد حمایت می‌کنند و ما آماده‌ایم این مسیر را ادامه دهیم.»
این در حالی است که آقای روبیو ساعاتی پیش گفته بود که ممکن است تا شامگاه یک‌شنبه خبری دربارهٔ توافقی با ایران اعلام شود که می‌تواند به‌طور رسمی به جنگ خاورمیانه پایان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75688" target="_blank">📅 22:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFv_3SGTLFVLyYxX9J0D_Joo-DSITy2JS3IK6kbcctQ3GMh1XtyhmwPKXgY3tCeZ_UQSmDJg3sJ1DnYcuOKr14cxsuGiu8VwPf71qdVue5lmZszOrnO75-cH7GMC4_l1_jJ-2n6Fuo3A-OYaO4lcXuNnZFU9jslvV8jk8TyyDJi4MBPydmuATWMpQ5inNlohpekqO0pu1KePGGATNw-9ceB7DzkJQc4CfaZD4M1bB33J5mtvFCKks1JnJQUHsr8qAXyNGwWpiNI-vTsxaB_he5QLTT78kxKNZLoF1yCiYIjr1QhKZKHlfXvtEpvD1Hm-BI_-IfjJrOXkycxNr7St-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر توافق کنم توافقی خوب خواهد بود
ترجمه ماشین:
اگر با ایران توافقی انجام بدهم، توافقی خوب و درست خواهد بود؛ نه مثل توافقی که اوباما انجام داد و مبالغ عظیمی پول نقد به ایران داد و مسیری روشن و باز به سوی سلاح هسته‌ای پیش پای ایران گذاشت.
توافق ما دقیقا برعکس آن است، اما هیچ‌کس آن را ندیده و نمی‌داند چیست.
حتی هنوز به‌طور کامل هم مذاکره و نهایی نشده است.
بنابراین به بازنده‌هایی که درباره چیزی انتقاد می‌کنند که هیچ اطلاعی از آن ندارند گوش نکنید.
برخلاف کسانی که پیش از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بد انجام نمی‌دهم!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75687" target="_blank">📅 22:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viN7RFb3JWGQ42PKOUkk-VmKMTZrOaRJ-TtbLrDnNd33B29o0-4gmo_5Xx4V1-ErsU8NXM1t6RrDCLQMRABLxg8AwvVl-Enra4ljAB_MzV86j-YoX_-cvnFk1ASq3TnLZ4R-ghS95vnT01rUCKaKOUCr03oCdEH_tP2YF4gE_xaA4D-Muvf5rjSFt3Pvi5j20-__gde52MCllAsxtyH-dGow8L946KaBWCRppDR_H_JGOfw8T_O5cBsPp9HvWv8SPaDFFIP8jln992pLILlGuaS-Wba6lVRhK3sSYHvRLtDcgv7GgxRR2k77kXMenCT9lOk0z6mk3ssER13Tnnr7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه آکسیوس، روز یکشنبه سوم خرداد ماه، به نقل از یک مقام ارشد دولت دونالد ترامپ گزارش داد، «چند مورد جزئیات حل‌نشده» میان تهران و واشنگتن باقی‌مانده است و به همین دلیل توافق میان ایران و آمریکا احتمالا امروز امضا نخواهد شد.
این مقام آمریکایی به آکسیوس گفت هنوز بر سر برخی بخش‌های توافق «رفت‌وبرگشت» وجود دارد و اختلاف‌ها بیشتر بر سر عباراتی است که برای هر یک از دو طرف اهمیت دارد: «برخی کلمات برای ما مهم هستند و برخی کلمات برای آن‌ها.»
آکسیوس به نقل از این مقام ارشد کاخ سفید نوشت، ساختار تصمیم‌گیری در جمهوری اسلامی «سریع عمل نمی‌کند» و روند دریافت همه تاییدیه‌های لازم چند روز زمان خواهد برد.
به گفته این مقام، ارزیابی واشنگتن این است که «مجتبی خامنه‌ای»، رهبر جمهوری اسلامی، چارچوب کلی توافق را تایید کرده، اما اینکه این روند به توافق نهایی منجر شود، «همچنان یک سوال باز» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75686" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzlAQc21_7agT9XhXZtdudgg2cJ-OTRx0pPVS-WZw64aHCKYYf3cfbhAjkTT8J5sLXg3nDUOxB8dhpbxphL-hej_pI-rTvrFi1_voVp2Oi3oKwMmRlT-eoSSLLiP9kIjtTX7fH9KTX0Pz9bP_riQ4LkbYaLkaspVs0pjIFBXzqUbnFuHoIAfpUP0sQq99teo6jRAN_M0NamldI3k4IqgU8Kz8LZLXjg0di_o_wYLt9xWTKuqNmDQN41fMUQCGTG1TrD9rwSpgTjzpcxBkjix5Jz-Bt1RGCs4d3yh6X3NUvZ6y5MPyU-t5AM62laSmI9f_qxYc3sLKmM8SJYiQD9Olw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او و دونالد ترامپ توافق دارند هرگونه توافق نهایی با جمهوری اسلامی باید به‌طور کامل تهدید هسته‌ای را برطرف کند.
او گفت این به معنای برچیدن تاسیسات غنی‌سازی ایران و خارج کردن مواد هسته‌ای غنی‌شده از خاک این کشور است.
نتانیاهو افزود ترامپ بار دیگر بر حق اسرائیل برای دفاع از خود در برابر تهدیدها در همه جبهه‌ها، از جمله لبنان، تاکید کرده است.
او همچنین گفت سیاست او، همانند سیاست ترامپ، همچنان ثابت است؛ ایران نباید به سلاح هسته‌ای دست یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75685" target="_blank">📅 18:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_8j2MGYIFfmr4LhBgD4THrNxHsy9ZDuG0SBgt-V7Nn80e1n7rYbjFUG8iWCoKLVGyjgset3xszyCa4LOyZyfVrm4NbV1fUQUePlwxCHxqP6jxwQMzMH6GaYqX2YBlRXOmzHy5lQ0GAZO-XB_P6c3COmCOCGdY-0HzFwebxlqWLPTC766saHRQNLan_6qATX-W_bLPS8QHDuqk0SxGSbTSlbgkVsRduLFyC0YAVppYWoS-l4_LtU_paKzLung9K2Lb6zBjASoM6BSOGWY65XpuMGgYcuK7k4pzdy_CapJ3TEPt89DvkXLQWdxLgEn524xe6lE4NPeX4m-IWooJ-qPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ سخنان پزشکیان را نشان داد: آماده‌ایم به جهان اطمینان بدهیم
ترامپ اسکرین‌شاتی از
توییت
خبرنگار فاکس‌نیوز رو پست کرده که نوشته بود:
مسعود پزشکیان، رئیس‌جمهور ایران: ما آماده‌ایم به جهان اطمینان بدهیم که به‌دنبال سلاح هسته‌ای نیستیم. ما به‌دنبال بی‌ثباتی در منطقه نیستیم.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75684" target="_blank">📅 18:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tpd9sIpMpyaalS36zRrlPy7iEG5Pq9aS2dyqcncwBS_IrY1TzRjDFCKnos7czl6gJMM-PqhCHP9hN5SQfxYfsaBCj7iOiIT1QbmNtpQI0d0paf5iK4W4Wz5WNRUqwfdpmm4kBjMZQS3j41S9wK0_kR5T1_QjX5-VoXMLpg_Wy6RnlGSrClEjSlch2Zn1nFf4MIa75a0bWh1n5IKHwIQglIeIWbAhCURx_shDpvxLOGDr5BaILCw7CKfp6GXTPvZTvtbFB3T2v5iMQaXxIUeaMCj0IrD-Sw6GWPqy_H40S-5g1J1cO3gm82OXuJ41W_vEu7zpc4OfB5ohiMBMukzdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uY0OSMr5qCVhosXqQ7nFAzLbpcj_4yiwP99RN1bn1zk6krbyJP7n4O63I7fITMV7unWKeP_wuXNv6OXUEFaVQ2CM9i9oPHqOVQ8tJ6Hx6PqxXMIKpbRgVJp7SsAKp9mWA7UPZJYGeF-CWQX3wJzB3rFEWbCy0m40A0l7Y4uGb9vDKC6kY69Ey5tN-b66KHHbl3ckkxu958ip8lH9R1NWLXy17aEDSJuPpeMDSVM8HTXP6jWGrJknO5J2qzkp1-ccugRzjw8xnaE2mLIyPfabiTfKjMaVIeNzkpfqCcCny0u_O8ziNBnDQrv-lFgxWRkfPgupN4aCEeZ9VsFIe1YiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCU08u4_hvzUiE8p_kqRrvhNY6hHdRgxprEwsv5fn85Az7IojztDRD0-2UKkVeahZfjkvTkpJsW7Fh7Wu_MP-OAY9LVOEr9t3sVi5vHJHrNSjFIMKo3VZnP3npkE9o1SyoF5nGxyXcfbvKh3Y8_oWy3Sdut2etzkZIXb73QQFSCrcH2QM2FMeaMjFbvVMqvYQurdEfn0P3tG43pRhOH2-ST4nwwd4Jp3YIx5X5VHh3fsvph_r-yJoS_NVZym46WCVNl4FzofcXhRSUa23ILJqPmpLWGLDy0wDdp6RzU5wOJFn0ZN9m1GLePDB6ufQMYXnSrSa6nJLd9w0NBlP_wnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORYATR-mmtN8TuaJLxzUpze26MBMHyHm3OPRDGp4YSuk_xs2S-wXxX6me_Vz9HT2O0JSNl91vOBaE8BzpTht0deKZw0X3XBCwaHs1fogiDsTTb4N2JWpp1C2vqApB-zwNtdRiPygzteVdVFuFj-1_C4vpRAmUxFynpKOqdb-3knqx-dv7dGAjY41WZ4BGbtvI6NNt-ZVdUNLKTdREDLo6q1qu0tGVdRjGmZIwjCGrJAJm8C1koLcyTwyh5_01xwHYkJgz8qmKzrM5ydSbf6181uV4lV0VgfUWRlLwKJCuxeKp_K46jqqNNn9PlRkJ_5qf0_wU3HNipw1cpKfBW1mlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5gfdNJittiErEvSKmodnbuHSwlCPMws8MbTIQuFrJ7bBjAKh1zXdgdiyCXj0wDNmpapVsQSuOMswA_gIyiUdybwoQ7BhEW3Ol6rbI6GgzK-XdFFEFE_b3CvA2rsT75IM_Kc7KNBl2TROOQMB-tKK6DpQq3Cb3qyDcH_bJRS3J2rrykz2UNK5mFpKwhL2iDGLcjYAxN--M0vS7Y4vJcGD84evLOEM-JAfItBPBEeadW16gL9hE0ILh_ip_TuwbcXLdm0f7CMiFnpD0FbaKE0iQ1TmnhWR8WBvVtNygv2LLxZpZXvtloFpm1ZSpjeuoE61iFUQBnQ-PPh75A_dw-oxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران روز یکشنبه سوم خرداد با اشاره به توافق احتمالی میان جمهوری اسلامی و آمریکا، نوشت:  در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی درباره «تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامه هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.»
فارس در ادامه تاکید کرده است که «ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.»
این در حالیست که نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت که شنیده‌ها از جزییات تفاهم اولیه «احتمالی»، حاکی است که واشینگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط درآورد و جمهوری اسلامی در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است.
این گزارش افزود در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده حکومت ایران باید در گام اول آزاد شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75679" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vcfEowzDS6Tu7zaTXS1xxlwq-Ddx5NYxZxysmrgVF3QEJa1Js254-SlSbqSa-Z1G-s6nZIt81zt8Idhe6qosv3BBFNL_rpbEtPkob5pUdaetNZ67fU4QP61QaDSVpa2aLdCM3qXQmFans_uuZPUKUPDOgyYvo9MZKAAgEGAVq2DC3OTF_DHVZk07NKDNbx1YJH49wZjlnM3v38okNWaN-hkBo4BkIoShOlDZbFV49Rr5KrICG0n1sR92J9ytKfg8gfpLqdXI1L5K3Bf-s3XMHoX-Vd91cBb5aB75YrA-31zomi_O9_wIHDdh5ETayn8rCJXxEKtNKmJJd32qpwaSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=qVR647590wL39u4hS7oiJJ_xdkQK3m-JHsu_ykOMB2rbJWVIdbVhDR_No29g4qeePncig4y0rgzwPd4J7cqtjcmY3zECEDDQFMdJAK1AB8h1ooD0HMMPFna2WDPLC-uv5oVBIrik3hj0r7PHDnahVUdf0EfmDM08DfHqGluGflDbDMlPCnY_rxwwQuHWy4e7wAq2Sx8r4TCjNqWFXLVhUvk2lD9Fwd42_VJaw8OgIqooAirugn0vPUrsnANRkzZlZZuVMPoMDDeONp4BGSPeEW4-2FL-lUpDAnprglw9Aw-ba4jEsxC7PCY8koy6JLQBw-wmbXvrYSSmJE56EuQgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=qVR647590wL39u4hS7oiJJ_xdkQK3m-JHsu_ykOMB2rbJWVIdbVhDR_No29g4qeePncig4y0rgzwPd4J7cqtjcmY3zECEDDQFMdJAK1AB8h1ooD0HMMPFna2WDPLC-uv5oVBIrik3hj0r7PHDnahVUdf0EfmDM08DfHqGluGflDbDMlPCnY_rxwwQuHWy4e7wAq2Sx8r4TCjNqWFXLVhUvk2lD9Fwd42_VJaw8OgIqooAirugn0vPUrsnANRkzZlZZuVMPoMDDeONp4BGSPeEW4-2FL-lUpDAnprglw9Aw-ba4jEsxC7PCY8koy6JLQBw-wmbXvrYSSmJE56EuQgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه در جریان نشست خبری مشترک با سابرامانیام جایشانکار، وزیر خارجه هند، در دهلی‌نو اعلام کرد که طی ۴۸ ساعت گذشته «پیشرفت قابل‌توجهی» در مذاکرات و رایزنی‌های مرتبط با بحران تنگه هرمز و پرونده ایران حاصل شده و احتمال دارد تا ساعاتی دیگر اخبار مهم‌تری در این زمینه منتشر شود.
او بدون ارائه جزئیات کامل، گفت هنوز توافق نهایی شکل نگرفته اما مسیر مذاکرات نسبت به روزهای گذشته امیدوارکننده‌تر شده است.
روبیو با تاکید بر اینکه دولت آمریکا همچنان راه‌حل دیپلماتیک را ترجیح می‌دهد، اظهار داشت دونالد ترامپ تمایل دارد بحران ایران از طریق وزارت خارجه و مذاکره حل شود، نه از مسیر درگیری نظامی.
با این حال او هشدار داد که واشنگتن در هر شرایطی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و این موضوع «خط قرمز» دولت آمریکاست.
به گفته او، رئیس‌جمهوری آمریکا بارها تاکید کرده که ایران هرگز نباید به توانایی ساخت سلاح هسته‌ای برسد و دولت ترامپ در این زمینه از همه دولت‌های پیشین آمریکا سخت‌گیرتر عمل کرده است.
وزیر خارجه آمریکا در بخش دیگری از سخنانش به وضعیت تنگه هرمز پرداخت و گفت این آبراه، یک مسیر بین‌المللی است و هیچ کشوری حق ندارد عبور و مرور آزاد کشتی‌های تجاری را تهدید کند. او اقدامات اخیر ایران در قبال کشتی‌های عبوری را مغایر قوانین بین‌المللی دانست و هشدار داد اگر جامعه جهانی در برابر چنین اقداماتی سکوت کند، یک «وضعیت خطرناک و غیرقابل‌قبول» به رویه‌ای عادی در جهان تبدیل خواهد شد، موضوعی که می‌تواند در مناطق دیگر دنیا نیز تکرار شود.
روبیو همچنین اعلام کرد آمریکا طی دو روز گذشته همراه با شرکای خود در منطقه خلیج فارس روی چارچوبی کار کرده که هدف آن باز نگه داشتن کامل تنگه هرمز، جلوگیری از اخذ عوارض یا محدودیت برای عبور کشتی‌ها و همچنین رسیدگی به نگرانی‌های مرتبط با برنامه هسته‌ای ایران است.
او توضیح داد که در صورت موفقیت این روند، نه‌تنها امنیت کشتیرانی و تجارت جهانی حفظ خواهد شد، بلکه نگرانی‌ها درباره برنامه هسته‌ای ایران نیز تا حد زیادی کاهش پیدا می‌کند.
روبیو در ادامه گفت هرگونه توافق احتمالی نیازمند پذیرش کامل ایران و اجرای عملی تعهدات خواهد بود و مذاکرات درباره جزئیات فنی برنامه هسته‌ای، روندی پیچیده و زمان‌بر دارد.
او افزود هنوز نمی‌توان درباره موفقیت نهایی مذاکرات با قطعیت صحبت کرد، اما «نشانه‌هایی از پیشرفت واقعی» دیده می‌شود و ممکن است جهان در ساعات آینده خبرهای مثبتی درباره تنگه هرمز و روند مذاکرات دریافت کند.
@
VahidOOnLine
روبیو گفت: «هدف نهایی این است که ایران هرگز نتواند به سلاح هسته‌ای دست یابد. ایران هرگز نباید مالک سلاح هسته‌ای شود.»
او تاکید کرد دونالد ترامپ، رئیس‌جمهوری آمریکا، در این زمینه موضعی «کاملا روشن» داشته و گفته است ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
وزیر خارجه آمریکا افزود: «قطعا تا زمانی که دونالد ترامپ رئیس‌جمهور است، این اتفاق نخواهد افتاد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75676" target="_blank">📅 18:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E1KhzcRLf7EkyyVwOlja3tgY6_ELwtOlC2Clko2MOTcLF2GwWhb5SwJfzYCE_vo7T8pq4eroI_W9NMKx-mzJz7XBFilSwJVf27cq2ywiZ0pM7_n0piqF4SJroYKNs1RWvJ5qEmE0zP0MOuN1yfVohBFwa1qcgsSGmONW-TYR4eQtzXDSvzs2JMoSnBIQDFDSVPf4J-ywEkjPY3vGO07ub0npcak51CGYZIpRuotWQEfUYhfH3Ki2W85Qlagd7Qg6nEb63H_BGKKd28FSTuu1-9FBWy20HcdYUSrFuF4g3FuvHlr4XqWuyqa-KEmlWHi_Ne1IquiSoGcWDNaZYy2GHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد سرافراز، رئیس پیشین سازمان صداوسیما و عضو کنونی شورای عالی فضای مجازی، می‌گوید بخشی از حاکمیت ایران با الهام از الگوی چین به‌دنبال محدود کردن اینترنت جهانی برای عموم مردم و ارائهٔ آن فقط به گروهی خاص و کنترل‌شده است.
او روز یک‌شنبه سوم خرداد در گفت‌وگو با روزنامه اینترنتی فراز گفت جمهوری اسلامی تجهیزات لازم برای «قطع دائمی اینترنت» را از چین خریداری و وارد کرده است.
محمد سرافراز توضیح داد که در چین اینترنت جهانی برای عموم مردم قطع است و فقط به‌صورت محدود در اختیار گروه‌هایی خاص قرار می‌گیرد. سرافراز با اشاره به الگویی که آن را «سامانه نیکان» در چین خواند، گفت هدف چنین سازوکاری این است که «روایت حکومت» بر کشور حاکم باشد.
او همچنین اپراتورهای عضو شورای عالی فضای مجازی را از عوامل پشت پردهٔ تصویب طرح موسوم به «اینترنت پرو» دانست و گفت ذی‌نفعان قطع اینترنت «یک روز فیلترشکن می‌فروشند و یک روز اینترنت پرو».
@
VahidHeadline
پس از ۲۰۴۰ ساعت قطعی اینترنت در ایران، نت‌بلاکس نوشت در حالی که دسترسی به اینترنت جهانی در طول مذاکرات صلح تا حد زیادی قطع است، کاربران منتخب در لیست سفید، تصویری مصنوعی از زندگی ایرانیان را به جهان خارج ارائه می‌دهند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/75675" target="_blank">📅 17:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=ijgZdmiGYlfK6JVEUYgyK3nj2QvTtIkbSeywzhjienyclWMAUA9Be3GRIJY8O3SWIPgkw_lAI6HBSt2tKFgxcGTjGCsrSzTG4xy701xCO9M8Z84fSh-5G5dXLHOgS_0fGavsIZCQeJoG-mR3kWwk8tb-EInclR6tEUZhIL_uMqf7imyHJJnMbymGnh-3RNqR_JlEJKDfvncosjyIVz8J0UgJh3BUI1hu7j4eLHdLID7Fnajz5vlSwT1J3ZxU7H4F_VLfhS0PGA65d2l_GLDk7ZrIF394igpaV6VDz44mzEWC5BJg4I7SmkUtsw4XgDxcvvRVbCPaelid8g_JGM7Gvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=ijgZdmiGYlfK6JVEUYgyK3nj2QvTtIkbSeywzhjienyclWMAUA9Be3GRIJY8O3SWIPgkw_lAI6HBSt2tKFgxcGTjGCsrSzTG4xy701xCO9M8Z84fSh-5G5dXLHOgS_0fGavsIZCQeJoG-mR3kWwk8tb-EInclR6tEUZhIL_uMqf7imyHJJnMbymGnh-3RNqR_JlEJKDfvncosjyIVz8J0UgJh3BUI1hu7j4eLHdLID7Fnajz5vlSwT1J3ZxU7H4F_VLfhS0PGA65d2l_GLDk7ZrIF394igpaV6VDz44mzEWC5BJg4I7SmkUtsw4XgDxcvvRVbCPaelid8g_JGM7Gvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری بزرگ در نزدیکی یک قطار که از گذرگاه چمن در شهر کویته در ایالت بلوچستان پاکستان عبور می‌کرد، تعداد زیادی کشته و ده‌ها نفر زخمی برجا گذاشت.
یک مقام ارشد پلیس بلوچستان و یکی از مسئولان این ایالت به محمد کاظم، خبرنگار بی‌بی‌سی اردو، گفت تاکنون کشته شدن ۲۰ نفر در این انفجار تأیید شده و دست‌کم ۷۰ نفر زخمی شده‌اند.
تصاویر منتشرشده پس از حادثه نشان می‌دهد که چندین خودرو در نزدیکی خط آهن آتش‌ گرفته‌اند و واگن‌های قطار نیز روی ریل واژگون شده‌اند.
گروه جدایی‌طلب «ارتش آزادیبخش بلوچ» مسئولیت این حمله را به عهده گرفته‌ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75674" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lx75PbwYS6Lvy7AiCxQUVLI41plF5JtZTHdQFuuk65E4hqgGLvkvdr3t5vf0FHMTpRHhKl6FCPieoW_2BsuGQgp-FWEyXumzo9jOIFs6L_hugoXE3Hez9OUqymsSaIuxb1SpdqFmujkHpcEaiqDPSI97OEOEk0xUBFgRCGc2BkLYTiDuhfhnWkVFAyYYxOK2rErhnPTRB8niuTq1i1y5BjQo_nefxf1N5tj8xJ9TEc-o2WX0KrbAtFHUWhxTMV-Gt5ijqAU9239QT36WpBJN5OmoarnDY62KjusddDz27WwPPrXJSfkAFu67cR2Oke7KGSB8ZbUm96HqMNmZtt2p4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه جمهوری اسلامی، اعلام کرد مجتبی کیان به اتهام ارسال اطلاعات مراکز تولید صنایع دفاعی به «دشمن آمریکایی ـ صهیونیستی» اعدام شده است.
قوه قضائیه مدعی شده کیان در جریان آنچه مقام‌های جمهوری اسلامی «جنگ رمضان» می‌نامند، اطلاعات و مختصات واحدهای مرتبط با تولید قطعات صنایع دفاعی را از طریق پیام به شبکه‌های وابسته به اسرائیل و آمریکا ارسال کرده بود.
میزان مدعی شده بررسی‌های فنی نشان داده سه روز پس از ارسال این اطلاعات، محل مورد اشاره هدف حمله قرار گرفته و به‌طور کامل تخریب شده است. قوه قضائیه گفته پرونده این متهم در دادگستری استان البرز رسیدگی شد و حکم او پس از تأیید دیوان عالی کشور اجرا شد.
بر اساس رأی دادگاه، مجتبی کیان به اعدام و مصادره کلیه اموال محکوم شده بود. میزان همچنین نوشت از زمان بازداشت تا اجرای حکم کمتر از ۵۰ روز زمان گذشته است؛ موضوعی که پرسش‌های جدی درباره سرعت رسیدگی، امکان دفاع مؤثر و فرصت اعتراض در پرونده‌ای با مجازات اعدام ایجاد می‌کند.
قوه قضائیه گفته دادگاه با حضور وکیل برگزار شده، اما روشن نیست این وکیل منتخب متهم بوده یا تسخیری، از چه زمانی به پرونده دسترسی داشته، آیا امکان ملاقات محرمانه و آماده‌سازی دفاع فراهم بوده و آیا متهم فرصت کافی برای اعتراض به ادله فنی، درخواست کارشناسی مستقل و پیگیری مؤثر در دیوان عالی کشور داشته است یا نه.
این پرونده در بستر موج گسترده‌تری از اعدام‌ها، احکام امنیتی، مصادره اموال و رسیدگی‌های شتاب‌زده پس از جنگ قرار می‌گیرد؛ روندی که منتقدان و سازمان‌های حقوق بشری آن را نشانه استفاده فزاینده جمهوری اسلامی از مجازات اعدام برای ایجاد بازدارندگی سیاسی و امنیتی می‌دانند.
@
VahidHeadline
خبرگزاری میزان هیچ اطلاعاتی درباره حرفه این فرد نداده و مشخص نیست که مجتبی کیان چگونه به «اطلاعات صنایع دفاعی» دسترسی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75673" target="_blank">📅 17:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cMnqthKUrnJmw2pqkQv2FjxYmJ2w0NHG9PyGZXBFVFIL_Bme_w0MdRKd4DPKBFOnyVfRfZQUnQ1oNhHwVpf5DiKr2TtJO-Uzjy1foQTGODZR4sto_DmMhg6-PizvtSnvjMYEm-uclf-QHSXEo66iaeu_zfwuZjGPAx8T_IYOkamuqEW9jWNhJC9ledv1l-ATgJ2nar9y4Ws1s1R9EvpQQVoemOsvjG0Z_QqqzgnE0AJ4JFylDvW2NayYXlQBe1Fm6YdWlLSH1xSg2NQqnfdiySEWuBirbyZEL0w_Uy-6z_HcckzBFr16Z8sLUFwKiZMoPDPcmf7LOfJlLgwXURBzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: جزئیات توافقی که ترامپ در آستانه امضای آن با ایران است
ترجمه ماشین:
توافقی که آمریکا و ایران در آستانه امضای آن هستند، شامل تمدید ۶۰ روزه آتش‌بس است؛ دوره‌ای که طی آن تنگه هرمز دوباره باز خواهد شد، ایران می‌تواند نفت خود را آزادانه بفروشد و مذاکراتی برای محدود کردن برنامه هسته‌ای ایران برگزار خواهد شد؛ این را یک مقام آمریکایی گفته است.
🔻
چرا مهم است: این توافق از تشدید جنگ جلوگیری می‌کند و فشار بر عرضه جهانی نفت را کاهش می‌دهد. با این حال روشن نیست که آیا به یک توافق صلح پایدار منجر خواهد شد یا نه؛ توافقی که هم‌زمان خواسته‌های هسته‌ای رئیس‌جمهور ترامپ را نیز پوشش دهد.
▪️
وضعیت فعلی: هم ترامپ و هم میانجی‌ها گفته‌اند ممکن است این توافق روز یکشنبه اعلام شود، هرچند هنوز نهایی نشده و همچنان ممکن است از هم بپاشد.
▪️
این مقام آمریکایی طرح کلی مفصلی از پیش‌نویس فعلی ارائه کرده که بخش عمده آن را منابع دیگر نزدیک به مذاکرات نیز تأیید کرده‌اند.
🔻
چه چیزهایی در توافق آمده است؟
دو طرف یک یادداشت تفاهم امضا خواهند کرد که ۶۰ روز اعتبار دارد و با رضایت متقابل قابل تمدید است.
▪️
در این دوره ۶۰ روزه، تنگه هرمز بدون عوارض باز خواهد بود و ایران موافقت می‌کند مین‌هایی را که در این تنگه کار گذاشته پاکسازی کند تا کشتی‌ها آزادانه عبور کنند.
▪️
در مقابل، آمریکا محاصره بنادر ایران را لغو می‌کند و برخی معافیت‌های تحریمی صادر خواهد کرد تا ایران بتواند نفت خود را آزادانه بفروشد.
▪️
این مقام آمریکایی اذعان کرد که این موضوع به سود اقتصاد ایران خواهد بود اما گفت در عین حال کمک قابل توجهی برای بازار جهانی نفت خواهد بود.
🔻
این مقام آمریکایی گفت هرچه ایرانی‌ها سریع‌تر مین‌ها را پاکسازی کنند و اجازه دهند کشتیرانی از سر گرفته شود، محاصره هم سریع‌تر لغو خواهد شد.
▪️
اصل کلیدی ترامپ در این توافق «امتیازدهی در برابر عملکرد» است.
▪️
طبق گفته این مقام، ایران خواستار آزادسازی فوری منابع مالی مسدودشده و لغو دائمی تحریم‌ها بود، اما طرف آمریکایی گفت این موارد فقط پس از ارائه امتیازهای ملموس اجرا خواهد شد.
🔻
مسائل هسته‌ای هنوز باید مذاکره شوند
▪️
به گفته مقام آمریکایی، پیش‌نویس یادداشت تفاهم شامل تعهد ایران به این است که هرگز به دنبال سلاح هسته‌ای نرود و درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالای خود مذاکره کند.
▪️
به گفته دو منبع مطلع، ایران از طریق میانجی‌ها تعهدات شفاهی درباره دامنه امتیازهایی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، به آمریکا ارائه کرده است.
▪️
آمریکا موافقت خواهد کرد که در دوره ۶۰ روزه درباره لغو تحریم‌ها و آزادسازی منابع مالی ایران مذاکره کند؛ هرچند این اقدامات فقط در چارچوب توافق نهایی و پس از اجرای قابل راستی‌آزمایی آن عملی خواهند شد.
▪️
نیروهای آمریکایی که در ماه‌های اخیر در منطقه مستقر شده‌اند، در دوره ۶۰ روزه در منطقه باقی خواهند ماند و فقط در صورتی خارج می‌شوند که توافق نهایی حاصل شود.
🔻
نکته قابل توجه: پیش‌نویس یادداشت تفاهم همچنین تصریح می‌کند که جنگ میان اسرائیل و حزب‌الله در لبنان پایان خواهد یافت.
▪️
یک مقام اسرائیلی گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس تلفنی روز شنبه با ترامپ درباره این شرط ابراز نگرانی کرد. او همچنین درباره جنبه‌های دیگر توافق نیز نگرانی‌هایی مطرح کرد، اما به گفته یک مقام آمریکایی، دیدگاه خود را با احترام و لحنی محتاطانه بیان کرد.
▪️
مقام آمریکایی گفت این یک «آتش‌بس یک‌طرفه» نخواهد بود و اگر حزب‌الله برای مسلح شدن دوباره یا تحریک حملات تلاش کند، اسرائیل اجازه خواهد داشت برای جلوگیری از آن اقدام کند.
...
🔻
چه باید دید: به گفته مقام آمریکایی، کاخ سفید امیدوار است اختلافات نهایی در ساعات آینده حل‌وفصل شود و توافق روز یکشنبه اعلام شود.
▪️
این مقام گفت ممکن است توافق حتی کل ۶۰ روز هم دوام نیاورد، اگر آمریکا به این نتیجه برسد که ایران درباره مذاکرات هسته‌ای جدی نیست. از سوی دیگر، آمریکا معتقد است فشار اقتصادی بر ایران انگیزه‌ای برای رسیدن به توافق کامل به‌منظور رفع تحریم‌ها و آزادسازی منابع مالی این کشور ایجاد می‌کند.
▪️
این مقام آمریکایی گفت: «دیدنی خواهد بود که ایران واقعا تا کجا حاضر است پیش برود؛ اما اگر آن‌ها توانایی و تمایل تغییر مسیر خود را داشته باشند، این مرحله بعدی آن‌ها را وادار خواهد کرد تصمیم‌های حیاتی درباره این بگیرند که می‌خواهند چه نوع کشوری باشند.»
▪️
مشاوران ترامپ می‌گویند اگر خواسته‌های او درباره برنامه هسته‌ای ایران برآورده شود، رئیس‌جمهور آماده است برای بازتنظیم روابط با ایران و دادن فرصت به این کشور برای دنبال کردن ظرفیت کامل اقتصادی‌اش، که به نظر ترامپ «عظیم» است، اقدامات بسیار گسترده‌ای انجام دهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75672" target="_blank">📅 07:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjxA-UZF1Mj6o-a56sgY_WFzF6f3GTZ70XTUb5zOMYbe2zj9wLmMUYP_qc5CHJ5YSU2rxZqExoI7unbBjupVfM75hI0Lx-uFw_fESEdoq_NHY7oBEQbfMwY867wytHhbbW0NJA_mRjKAK2wIWWsiTLAH65_7MQ_UYlOBTqPczRK-Gtdlm7YxC9xFHXqMiod55Kh9VFUD4-xmrqnmP-qb18asiJ5SMcub07bW4BUpauiy8ti3aJgNnV3PBde5MXvwS7-XKCSdQY_6QTy6Jjed-rB6duwtYO9SQsYseAUt7HIYs9nOkXX3dbfNErHSJ7SC3f4A-qO-tcBlD0Caabgvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG_QSMO4gLS8NIva1WF5W-iCezjdX9tm6CjBw_BIeeilEpo6mNMr0pzm_eQ-lMngSL8ZRKG2keNfF6-7ndKxUPFGRt-HvuPo-qhcNKY_EIcq2buTIAtlua4EWmzoEUUVzmlTRfyhxwSg8vF-n-IhaeRRe_Pq9-d7TP1fhSl9u51i4OS9kONY49Uxm0-qea9hX1F6vNdDUn3fHETHH3P3XEVtFFMEZ4eYO1dHr9IZcFUM73XD8Z9JN3uNv53iVZn07X5qUEpbXzIsVNJ6EcLVu_5FVXpLzStD75rLEaWjKZvfahABlConOJiMc1cy0TwPd2eoAJ6PFqQlDcAiEAL8Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی در شبکه اجتماعی ایکس با درج تصویر سنگ‌نگاره پیروزی شاپور اول ساسانی بر امپراتور روم، نوشت: «وقتی ایرانیان مهاجمان متوهم را ناکام گذاشتند.»
او در این پیام که کنایه‌ای است به محاصره دریایی بنادر ایران توسط آمریکا نوشت: «رومیان تصور می‌کردند که رم مرکز عالم است؛ اما ایرانیان این توهم را در هم شکستند.»
پیام آقای بقایی که به نحو گسترده‌ای در کانال‌های تلگرامی رسانه‌های حکومتی ایران بازنشر شده است به نظر می‌رسد که با استفاده از سنگ‌نگاره پیروزی شاپور بر امپراتوران روم در نقش رستم استان فارس بازنقش شده است.
آقای بقایی که اخیرا با حکم محمدباقر قالیباف به عنوان سخنگوی هیئت مذاکره‌کننده ایران هم منصوب شده است با اشاره به لشگرکشی مارکوس یولیوس فیلیپوس معروف به فیلیپ عرب، امپراتور روم، علیه امپراتوری ساسانیان، نوشت که لشگرکشی او «منجر به پیروزی رومیان نشد بلکه به صلحی با شروط شاپور اول ختم شد؛ امپراتور ناچار شد با واقعیت کنار بیاید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75670" target="_blank">📅 06:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hOPuvldnIAfqa-ckRkEwIJuG0Cy62klV18PsdqvnlCrm6amXtNuSJKvmPT4VJbaY4EraLkeQ3iFFRSv3q9gCRkGL4xBzi5Ai7yTWKjdjQjgcpfR2BtG1GKipEtNjan0uDFWmdewJtJKrasyuNkFs0XQu9yNBgouPx8ScLs5QyuGXDxYPzu3P-z9pxm26jsdw1SE7544I9fecGZF-BJMGU85A-NNpwaYpDtNOGOhqfG5br1kQ8iCrvVMC_cbYAY1jXRGZYnYbbDSgHnK8QEBppzUEy7oH50vsE7l2Pk8ifXrPp6J1Fdwd68Z_QHExyB55Fi4DNW9EA4kgGaZ4xSD6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است؛
مقامات آمریکایی تصریح کردند که این پیشنهاد هنوز جزئیات دقیق نحوه واگذاری این ذخایر را تعیین نکرده و حل این مسئله را به دور بعدی گفتگوها درباره برنامه هسته‌ای ایران موکول کرده است، اما یک بیانیه کلی که ایران را متعهد به این کار کند، که هدف دیرینه ایالات متحده بوده، برای توافق بسیار حیاتی است، به‌ویژه اگر این توافق کلی با بدبینی جمهوری‌خواهان در کنگره مواجه شود. تا این لحظه، ایران هیچ بیانیه‌ عمومی درباره توافقی که ترامپ اعلام کرده، صادر نکرده است.
تهران در ابتدا با گنجاندن هرگونه توافقی درباره ذخایر اورانیوم غنی‌شده خود در این مرحله اولیه مخالفت کرده و خواستار موکول شدن آن به مرحله دوم گفتگوها بود، اما مذاکره‌کنندگان آمریکایی از طریق واسطه‌ها به صراحت اعلام کردند که بدون دستیابی به توافقی بر سر این ذخایر در فاز اولیه، میز مذاکره را ترک کرده و کارزار نظامی خود را از سر خواهند گرفت.
براساس این گزارش، بخش دیگری از این توافق محتمل شامل آزادسازی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در خارج از کشور است؛ اما به گفته مقامات آمریکایی، ایران تنها زمانی به بخش عمده این دارایی‌ها که قرار است توسط ایالات متحده و متحدانش در یک صندوق بازسازی قرار گیرد دسترسی پیدا خواهد کرد که با یک توافق هسته‌ای نهایی موافقت کند؛ امری که انگیزه‌ای برای تهران ایجاد می‌کند تا پای میز مذاکره بماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75669" target="_blank">📅 05:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBsgG83L1c_QOlh3yGbtB94gwrUw1f0vHPCuCHxbDRrAVFZAbbEpepu2ZXNBsBgCOCGsbBEl3BEk62r81mT5nl_6IV51X05igjgU8ShVe9ZIhMZH5zyzLiD6eEi5oCETOyoRU2nFMaVCbYLcMZBOAvWlWLSaG3WGy-rtUXXDFeGrZHzZNk0j29UfHWr5tAB0OljekyOCit9uxkOD5OKRz8ycQCeKf5GSeWkeYDxaEo_SwetMqLPXtLKkBLdejSxK8Q0Pdu4pIC1xd6ZWzAMm_qaBk6bHI417-TuC8wpCeV1F-KhONsKZua5hrGK0P7r93nlkwcFz6vA2HG7yr4d5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، ابراز امیدواری کرد پاکستان به‌زودی میزبان دور بعدی گفت‌وگوهای تهران و واشینگتن باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75668" target="_blank">📅 05:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uaum5igoyWW3rbX6s0ZvjxUwhUIwVkjdfQMmTZuqGf8R2RvV1IHk-z9h1XheCG0K5BZ_W5-x9NsaLY6FUX-K66NwrYXhg9FVySi7C2L41nt9wxbcct35ucPkIAB2NsXTnEHhyO44bcqsbBYxoIhljrr3HGfhhCx-qRa348aE-VdpOg398ak8OhpnhlcFWx3aVbe3saHurmP0IKFTuVzrLZxkdOkSWwv01IqHyiEnte6Vym0yQ3TQbYfO_AhYGHLh_6lkxRfOCzVBYjgZvqrEi4oohFDHhLXVfxUDj1Bwnv3cTDcz1DcwrKc61P87Xlu2NzoBKIFxqa6IPzgXfeoMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z9-q1bvtWufQLilfKsRZU6U8pKq5nmC9bwpIw2SfstdSPF9PTMNogdgkvu3OmqPV9Kf6e2uMxPy0EhCZUa1HRW1fOcpvt0EDAlOFmHQlGJix_vsRijsaZza933KHIfZF5s8F-xOxwXeCOpEcIubNwL7B8TNOzqseB7MPNRGK2bD5E4sFnAvk3OV2jYxfYT2Kg7KjMtxFVotMBry61BAzbPgzUypLdmUWjojrhLbnlN2KEsbT4QZfrbujy91uOgdYFk96QPp8vqDV_zgWLa8sH9Z-r42R8mQ6bLe3pxWB1jTn3qmfID4OFG-22p7Iss1TCT8f4vjraKn0dTnIwd-CEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت‌های تد کروز و لیندسی گراهام در واکنش به اخبار منتشر شده درباره توافق احتمالی
tedcruz
,
LindseyGrahamSC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75666" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7119557db8.mp4?token=hxRp8KtA2wKcBhRNHgG2QI5IYvtY62n7OlkJRJYCEL0lb6C5xShe9ifqdylttuOrf85qBtpq32kyKmX9R1aSbIMCvlcR7at_M7wJG9UBilJPKvJtFYRQw1XzF1DDvojXrMeASnY7hjx5o4zPmCiuai86VEW2tsDbBDjKtTfLymbBY4JkB-1JC_nTARY4HTSIJs0OSe00X3Mg_MfxUXITI4a4_1VmB5l9Qpq8vmA2n9Kcol-zLbKsRk1E6KseC1lVMlhkhgRCuKUi-yuEeFPTnGg_bao_jKun7asl2a5YMF7uL0TnFcRvKA9URwfSttFozYy0c63IzvaYOXr3zcWnmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7119557db8.mp4?token=hxRp8KtA2wKcBhRNHgG2QI5IYvtY62n7OlkJRJYCEL0lb6C5xShe9ifqdylttuOrf85qBtpq32kyKmX9R1aSbIMCvlcR7at_M7wJG9UBilJPKvJtFYRQw1XzF1DDvojXrMeASnY7hjx5o4zPmCiuai86VEW2tsDbBDjKtTfLymbBY4JkB-1JC_nTARY4HTSIJs0OSe00X3Mg_MfxUXITI4a4_1VmB5l9Qpq8vmA2n9Kcol-zLbKsRk1E6KseC1lVMlhkhgRCuKUi-yuEeFPTnGg_bao_jKun7asl2a5YMF7uL0TnFcRvKA9URwfSttFozYy0c63IzvaYOXr3zcWnmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنبه عصر، یک تیراندازی در حوالی کاخ سفید خبر روی داد که طی آن دو نفر از جمله یک عابر و فرد مظنون تیر خوردند.
سرویس مخفی ایالات متحده، در گزارشی اعلام کرد که اندکی پس از ساعت ۶ عصر روز شنبه، فردی در محدوده خیابان ۱۷ و خیابان پنسیلوانیا، (شمال غربی) سلاحی را از کیف خود خارج کرد و شروع به تیراندازی کرد.
سرویس مخفی ایالات متحده افزود پلیس سرویس مخفی به تیرانازی او پاسخ داد و به مظنون شلیک کرد.
به گفته سرویس مخفی،‌مظنون به یک بیمارستان محلی منتقل شد، اما در آنجا اعلام شد که جان باخته است.
به گفته این نهاد امنیی، در جریان این تیراندازی، یک عابر نیز مورد اصابت گلوله قرار گرفت و هیچ‌یک از مأموران آسیب ندیدند.
سرویس مخفی که وظیفه حفاظت از رئیس‌جمهوری آمریکا را دارد افزود دونالد ترامپ، رئیس‌جمهوری آمریکا، در زمان حادثه در کاخ سفید حضور داشت.
@
VahidHeadline
آپدیت:
رسانه‌های آمریکایی هویت عامل تیراندازی عصر شنبه در مجاورت کاخ سفید را «نصیر بست»، جوان ۲۱ ساله اهل مریلند، معرفی کردند که به عنوان فردی با اختلالات روانی و عاطفی شدید برای ماموران امنیتی شناخته‌شده بوده است.
بر اساس گزارش‌ها، این فرد که پیش از این در ژوئن ۲۰۲۵ با ادعای این‌که «خدا» است یک مسیر ورودی کاخ سفید را مسدود کرده و پس از آن به یک مرکز روان‌پزشکی منتقل شده بود، به دلیل تلاش مجدد برای ورود به حریم کاخ سفید در ژوئیه همان سال، حکم دادگاه مبنی بر «ممنوعیت ورود و نزدیکی به این عمارت» را داشته است.
گزارش‌های تکمیلی نشان می‌دهد که «نصیر بست» دست‌کم در یک پست رسانه‌های اجتماعی تمایل خود را برای آسیب رساندن به دونالد ترامپ ابراز کرده بود؛ او سرانجام پس از نقض حکم دادگاه، نزدیک شدن به ایست بازرسی خیابان هفدهم و پنسیلوانیا و گشودن آتش به سمت ماموران، در تبادل آتش متقابل با نیروهای سرویس مخفی هدف قرار گرفت و در بیمارستان جان باخت.
📷
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/75665" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1m2uGG4gEUFOFDT7v0gbsPoX04ec6o4HOSB5a6BgbaL_HReWXIC8ujHT_1pzIp6AtcXH37puWzYKooVVFAiySrwTaFhu5ZByevAtiBa1c93VJm1GuYKu761ONQkixk1jvmRB4x8fHmHFgg8Si3VcWeJUHKxmmeZAy0ck8aFj7_NZMGTuH6ofHTGAw4WCqb6vMAhgfbnUZD8MKPBFBINTPSidWEzLGCMsnzVtSmStAwVghNbdorN1jQIbk2gadf-OyHc8Dehrajny8de4qVYBxU4w9tnEBg3xrWFVh7gBDwR-awH5or-KoqeC_Y3qtYiyyf9oFo0LSQdul7TAqBJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس، خبرگزاری وابسته به سپاه، در واکنش به پیام دونالد ترامپ، رئیس‌جمهوری آمریکا مبنی بر نزدیک شدن به توافق با ایران و بازگشایی تنگه هرمز نوشت: «این ادعا نیز با واقعیت‌ها فاصله دارد».
فارس در ادامه نوشت: «برخلاف ادعای لحظات قبل دونالد ترامپ در شبکه اجتماعی تروث سوشال مبنی بر بازگشت تنگه هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد که این ادعا نیز با واقعیت‌ها فاصله دارد؛ چرا که بر اساس آخرین متن ردوبدل‌شده، در صورت توافق احتمالی، تنگه هرمز کماکان تحت مدیریت ایران خواهد بود و اگرچه ایران موافقت کرده اجازه دهد تعداد کشتی‌های عبوری به میزان قبل از جنگ بازگردد، اما این به‌هیچ‌عنوان به معنای تردد آزاد به وضعیت قبل از جنگ نیست و مدیریت تنگه، تعیین مسیر، زمان، نحوه عبور و صدور مجوز، کماکان در انحصار و با تدبیر جمهوری اسلامی ایران خواهد بود.»
خبرگزاری سپاه در ادامه مدعی شد که برخلاف شروط پیشین ترامپ مبنی بر گنجاندن برنامه هسته‌ای در توافق، «هیچ تعهدی از سوی ایران داده نشده و پرونده هسته‌ای اساسا در این مرحله مورد بحث قرار نگرفته است.»
فارس همچنین ادعا کرد که «مقامات آمریکایی در پیغام‌های متعدد به ایران اذعان داشته‌اند که توییت‌های ترامپ عمدتا جنبه تبلیغاتی و مصرف رسانه‌ای در داخل آمریکا دارد و توصیه کرده‌اند که به این اظهارات توجهی نشود».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75664" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeMg0vKDXTd__swCR3hl6jF8nVcos29oTN-BOtpPQKS_Acuw8zfdY6WCgILbea-duL4SoxzHcUYl_SS--frauIeTcIlcmQww2HqiVbLxNMpxwhG5CiENBGSc0lLxArj17Ho2FjMGsyFk9bHT09Bb-TM914Agg6TVYdo1mh9RjJdMhsVS61MzmOPVDeOeu9KYX0--GmkbS6eiQAgLP4_ujvGnQ3uBq0Zx-DVWuA0fCfQufcnAPkRmlbKKbWzQTuiksiYoX5DqqaNCQ01E6ZFyweDLQwSpZcfN6XJ7doA0CaPI-DTwB00faDRctvJ9jaBcWBX74N0aH9NQk7PQzWQsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار الجزیره به نقل از «منابع خود»، مفاد کلیدی پیش‌نویس توافقی را که قرار است میان واشنگتن و تهران نهایی شود را اعلام کرد.
خبرنگار الجزیره مدعی شد، توافق پیشنهادی شامل «پایان جنگ در تمامی جبهه‌ها از جمله لبنان»، «آزادسازی چندین میلیارد دلار از دارایی‌های مسدودشده ایران»، «رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز» و همچنین «عقب‌نشینی نیروهای آمریکایی از مجاورت مرزهای ایران» است.
پس از اجرای این گام‌ها، طرفین یک مهلت ۳۰ روزه، که با توافق دوطرفه قابل تمدید است، خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند که در طول این مدت نیز تردد از تنگه هرمز تسهیل خواهد شد.
به گفته این خبرنگار، از نظر ایران، مدیریت تنگه هرمز یک موضوع دوجانبه میان تهران و مسقط تلقی می‌شود و گفتگوها در این زمینه با عمان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75663" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLoTPN6kxxgJS4kC-j3oukLDMAacfoNNf_2ba3vquVlRVgF06C_iUOVWRCYTR1jYZikK3Qc55wcs77Zf9ygp6uCfGlKts72O7WoyMMToCdmmCaGjigbFV_btZItkRjAyq1VnSNdH-WTZiWdZBPgXTd6vHW-prWHhVnKRhVi6SNy3Uik0BCL-cRjFOaUXIJCUU6QXE5S4pMd6Mw0QLsbLQ4N32Hw5a3s_ZKdreGq7HOwEqBaXaaHUTumom2Q1NEoBxtm3it7BqhUrgZ3sNCSe7Lo8cEYPf1_2bDcVhJUllTjTYTWQ87Cmo3HQpwCfQYfTIeNNDlT-UMLI228-bX0VNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یک منبع ارشد منطقه‌ای» از جزییات گفتگوی رهبران کشورهای عربی و مسلمان با دونالد ترامپ خبر داد.
خبرنگار آکسیوس نوشت: «یک منبع ارشد منطقه‌ای به من گفت که تمامی رهبران عرب و مسلمان حاضر در گفتگوی روز شنبه با ترامپ، از او خواسته‌اند تا برای پایان دادن به جنگ و مهار تنش‌ها در منطقه، توافق را پیش ببرد.»
این منبع تاکید کرده است که «پیام همه این بود: لطفا به خاطر کل منطقه، جنگ را متوقف کنید.»
به گفته این منبع، مذاکرات به خوبی در حال پیشرفت است و میانجی‌ها امیدوارند روز یکشنبه یک توافق چارچوب یک‌صفحه‌ای را منعقد و بلافاصله آن را اعلام کنند و پس از آن، قصد دارند ظرف چند روز مذاکرات را برای دستیابی به یک توافق دقیق و پرجزئیات آغاز کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75662" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RT0sJRpN7Wg9W3vhHbHdphsUos50KbdMvmJ_BlO2HXpeXm79bf_GYgm51NLX4OZnVbzcPLJJVQbHoSumxGpGuqDbwp5StyATkpcaG-F32v5ugR_mOHb8PRX9chQm0ZaVGtMggcbu4Lrm7pZCyg_SfMtYcJc1kMjYP_qO03sU5gVisihCRpPyjCzOx3WAs6l-nWeu93Mq1eWIrH3C1fb2-IQWJn6fUXPrjD-43-5wFi-pT_4Nyhpi32xYdNpQhpyxFv3CkQ14e1KOJkiTHNr3TG9U7Q2qrRfEZFt77Mr0V15RyCDAmeCsoj7CVsbPtY20pnsHI_RuiZQaipwzVLPAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: یک توافق تنظیم شده و اکنون در انتظار نهایی شدن است
پست ترامپ، ترجمه ماشین:
من در دفتر بیضیِ کاخ سفید هستم؛ جایی که همین حالا تماس بسیار خوبی با
▪️
پرزیدنت محمد بن سلمان آل سعود از عربستان سعودی،
▪️
محمد بن زاید آل نهیان از امارات متحده عربی،
▪️
امیر تمیم بن حمد بن خلیفه آل ثانی،
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی و وزیر علی الثوادی از قطر،
▪️
فیلد مارشال سید عاصم منیر احمد شاه از پاکستان،
▪️
رجب طیب اردوغان رئیس‌جمهور ترکیه،
▪️
عبدالفتاح السیسی رئیس‌جمهور مصر،
▪️
عبدالله دوم پادشاه اردن،
▪️
و حمد بن عیسی آل خلیفه پادشاه بحرین،
درباره جمهوری اسلامی ایران و همه مسائل مربوط به یادداشت تفاهمی در ارتباط با صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده و نهایی شدن آن منوط به جمع‌بندی میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگری است که نامشان ذکر شد.
▪️
جداگانه، با نخست‌وزیر بی‌بی نتانیاهو از اسرائیل نیز تماسی داشتم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به‌زودی اعلام خواهد شد. علاوه بر بسیاری دیگر از عناصر این توافق، تنگه هرمز باز خواهد شد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75660" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_ArDcoRH-gCKdASF4IPo5VRIWtvK9XOERF-Dg7KqxuL_FDU_JX39h3N0PSVM4AGUfxTGIpfT6qyVLnRWHEMqk050fBD8os6W8YgTbi_zM87yV8Y_82o1vCR_s4n0QLcqnrEk2LyTk_OsTAhRRHXKMA-DkeeByIhkS4sMsOO1KWxjHMqaxuOpKgOJ8fmaktkM0WUdkyg9Tdpz0Gyu3abHi8MMOz2OVmbG9zrzErwVvL-p-_NXr7Ril6-G9ATTgGnGB5fy44nqlTnOZACImenXSK2NK8tBNYVQo5TbtYe2sAdXXhXGqVq7cTmScdlXq6mHAwamDODJU2Hs4a2y1POUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز شنبه دوم خرداد ۱۴۰۵ در تماس‌هایی جداگانه با رهبران عربستان سعودی، امارات، قطر، مصر، ترکیه، پاکستان و فرانسه درباره توافق احتمالی برای پایان جنگ با جمهوری اسلامی گفت‌وگو کرد. همزمان یک مقام آمریکایی آگاه از روند مذاکرات گفت واشنگتن و تهران به دستیابی به توافق نزدیک شده‌اند و اختلاف‌های باقی‌مانده عمدتا بر سر نحوه نگارش برخی بندهای توافق است.
به گزارش اکسیوس، چند تن از رهبران حاضر در تماس با ترامپ از او خواسته‌اند مسیر دستیابی به توافق را دنبال کند. با این حال، این مقام آمریکایی تاکید کرده است که هنوز تصمیم نهایی از سوی رییس‌جمهوری آمریکا اتخاذ نشده و او همچنان می‌تواند توافق را رد کرده و دستور حملات جدید علیه ایران را صادر کند.
همزمان، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و پیت هگست، وزیر دفاع این کشور، برای شرکت در نشست ویژه بررسی توافق احتمالی به واشینگتن فراخوانده شدند. ترامپ پیش‌تر گفته بود پس از بررسی آخرین پیشنهاد ایران با تیم مذاکره‌کننده خود، احتمالا تا روز یکشنبه درباره ادامه مذاکرات یا ازسرگیری جنگ تصمیم خواهد گرفت.
به گفته منابع آگاه، پیش‌نویس جدیدی که قرار است ترامپ آن را بررسی کند، حاصل مذاکرات اخیر میان ایران و پاکستان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75659" target="_blank">📅 23:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hij14ooerVbZFDpGuWw6JHphq-ZGZO22J6gu-WXKc9pjSIYAGWXQauv8bAJGhH2cGe_Ijyjf7EYiDnl9mj9fGQ6iu6aeir8hEhdoXX66pj42YwDkheBdxyZkubV2v5euQKDACRTyjzqPmjRTY0OsVr10njYPTW8QBTASOaoOSpkyZZavkpDrz_lTnk9yIE-3YuOVVv4jmOj43zX9oFejPN8w05pzHptX4oJsJalEpm0asP559rrxGjXyQYWhvpn-Ysy2E4y-1LzrnnEKVrCQKp0_V3CjecKiu1M9BkBwgDf34qJvoMwssPqP-hzkSLSdEIJIpxEgJ7NC6F4GFSDQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ۱۳ اسرائیل در گزارشی از روند گفت‌وگوهای ایران و آمریکا گفت مقام‌های اسرائیلی معتقدند ایالات متحده و ایران به دستیابی به توافق احتمالی نزدیک‌تر شده‌اند و گزارش‌های اخیر و اطلاعاتی که دریافت می‌شود، «در اورشلیم به‌طور فزاینده‌ای معتبر تلقی می‌شود».
بر اساس گزارش این شبکه، مقام‌های ارشد اسرائیلی گفته‌اند پیشرفت در مذاکرات برای بخشی از نهاد امنیتی اسرائیل «بسیار ناامیدکننده» است، به‌ویژه در شرایطی که به نظر می‌رسد تلاش واشینگتن برای رسیدن به توافق در حال تشدید شدن است.
این مقام‌ها همچنین معتقدند فشار برخی مشاوران رئیس‌جمهور ترامپ در روزهای اخیر افزایش یافته و انتظار می‌رود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در پی این تحولات، نشست‌هایی مشورتی با وزیران ارشد و مقام‌های امنیتی برگزار کند.
نهادها و مقامات رسمی اسرائیل هنوز این گزارش را رد یا تأیید نکرده‌اند.
ارزیابی اسرائیل در دو هفتهٔ گذشته این بود که ترامپ خواهان توافق است، اما در نهایت به دلیل اختلاف بر سر مسائل کلیدی، موفق به دستیابی به آن نخواهد شد. با این حال، مقام‌های اسرائیلی اکنون معتقدند روند کنونی ظاهراً برخلاف چیزی است که اسرائیل در هفته‌های اخیر برای آن تلاش کرده بود.
این گزارش همچنین می‌گوید چارچوبی که دربارهٔ آن گفت‌وگو می‌شود، شامل یک توافق موقت ۶۰ روزه خواهد بود که ممکن است بعداً در حالی که مذاکرات درباره توافقی گسترده‌تر ادامه دارد، تمدید شود.
روز شنبه مقامات ایران و آمریکا و همچنین پاکستان که نقش میانجی را بین دو طرف بر عهده دارد، اعلام کردند که در مذاکرات برای پایان دادن به جنگ پیشرفت حاصل شده است.
روز شنبه، روزنامه اسرائیل هیوم نیز در گزارشی ادعا کرد پیش‌نویس توافقی که روی میز قرار دارد، شامل تعهد اولیه ایران به خودداری از توسعه سلاح هسته‌ای و تعلیق بلندمدت غنی‌سازی اورانیوم است و سایر مسائل، از جمله سرنوشت ذخایر کنونی اورانیوم غنی‌شده ایران، در مذاکرات بعدی در دورهٔ آتش‌بس بررسی خواهد شد.
این روزنامه همچنین به‌نقل از منابع آگاه که نام‌شان را نیاورده، ادعا کرد «رهبری سیاسی ایران پیش‌تر با تحویل اورانیوم غنی‌شده موافقت کرده بود، اما فرماندهان سپاه پاسداران با این اقدام مخالفت کردند و تصمیم‌گیری دربارهٔ این موضوع اکنون به تأیید رهبر جمهوری اسلامی بستگی دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75658" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/penQwkFVUBtjDLtX7kvZAuJYqtK-5KcoM1RCIFvQLLy7nxchADtGz8KhBtR5rlPKGhf4u8-XJmToGATWZNqrhsoF9-fv1xpM4wmLCBv57Fv5x8vJ2wKSQfPV2uLMxluMNmSRinOCOBH21kwDJ87vjbWWQ46YL88Lgj5mSXRdnmlkm6J5hGslGndK0BT_JxkFmo3YVeQPcG1YIu1fUATk8-puDY1Gt6rRS9RxNoV1f4KyIeEcR27BgAVbyjzDJMcn48UhVCG75jN_R3NYLNK5dLm7ZAZ3k2HdYrLx8QfSLu7KipLL5he6-x-W-7esvav7HZ0BysN3syT7FVuJ7-a5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه و نزدیک به تیم مذاکره‌کننده، با تاکید بر اینکه اگر آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد نوشت که موضوع هسته‌ای، پول‌های بلوکه‌شده و کنترل جمهوری اسلامی بر تنگه هرمز، سه موضوع اختلاف جدی در مذاکرات است.
فارس نوشت که تهران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
رسانه سپاه به نقل از این منبع نوشت: «پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود تهران به مذاکره این است که پول‌های بلوکه‌شده ابتدا واریز و آزاد شوند. بدون این اتفاق، اساسا وارد مذاکره نمی‌شویم.»
در ادامه آمده است: «اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگه هرمز است. آمریکا تاکید دارد که تنگه باید کاملا به شرایط پیشین بازگردد، اما تهران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که حکومت ایران با مدل خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75657" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZZgoILzjWHtqaTKg_Jcv3elgTjIpkWd_U3C0IhaZl70KUhCu5Slo33lzcFtYXUSVXGuV5Swde6RhJaxsHDZL89dQIeiRbDuNGn06gDNyvMHkGbxFlhkg33tyZPqNMIo2A9XAfC1L8d9tYLWHoFv3HbW7EabEzdOuKvot0WUBSvBdCoZYBkhMhYfDTjmZE0BuO-_fdAQFmlrjpr3CsTE9wblereJhD4EV4OkN_Dz_S00MRSYsmhuISqdokL-Vx-NRfcfEvCciahxgNqKs6IMrwTG1QghKqkwFFJjAX4-sfE8i31v5S7nijkfH9R2oVjoWL3m5-GSGNI6gxj99qMQeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به توافق بسیار نزدیک‌تر شده‌ایم
ترجمه ماشین:
پرزیدنت ترامپ به شبکه سی‌بی‌اس نیوز گفت مذاکره‌کنندگان ایالات متحده و ایران برای نهایی کردن توافقی که به جنگ میان دو کشور پایان دهد، «بسیار به هم نزدیک‌تر شده‌اند».
منابع آگاه از مذاکرات به سی‌بی‌اس نیوز گفتند تازه‌ترین پیشنهاد شامل روندی برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های ایران که در بانک‌های خارجی نگهداری می‌شود، و ادامه مذاکرات است.
آقای ترامپ از ارائه جزئیات درباره این توافق خودداری کرد، اما گفت که «هر روز بهتر و بهتر می‌شود.»
آقای ترامپ در یک مصاحبه تلفنی به سی‌بی‌اس نیوز گفت: «نمی‌توانم قبل از اینکه به خودشان بگویم، به شما بگویم، درست است؟»
👈
آقای ترامپ گفت معتقد است توافق نهایی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و افزود که در غیر این صورت «اصلاً درباره آن صحبت هم نمی‌کرد».
👈
او همچنین گفت این توافق باعث خواهد شد اورانیوم غنی‌شده ایران «به شکل رضایت‌بخشی مدیریت شود.»
👈
او گفت: «من فقط توافقی را امضا می‌کنم که در آن به هر چیزی که می‌خواهیم برسیم.»
منابع به سی‌بی‌اس نیوز گفتند آقای ترامپ هنوز در حال بررسی پیشنهادهاست و هنوز تصمیم نهایی خود را نگرفته است. این منابع گفتند او با مشاوران خود رایزنی می‌کند و با رهبران خارجی، از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس، گفت‌وگو دارد.
آقای ترامپ گفت اگر آمریکا و ایران به توافق نرسند، «با وضعیتی روبه‌رو خواهیم شد که هیچ کشوری هرگز به اندازه ضربه‌ای که آن‌ها در آستانه دریافتش هستند، ضربه نخورده باشد.»
آقای ترامپ پیش‌تر ایران را تهدید کرده بود؛ او پیش از آغاز آتش‌بسی که در ماه آوریل آغاز شد، گفته بود بدون توافق «یک تمدن کامل نابود خواهد شد» و اخیراً نیز به این کشور هشدار داده بود که «ساعت در حال تیک‌تاک است.»
مارکو روبیو، وزیر خارجه آمریکا، نیز روز شنبه گفت ممکن است «بعداً امروز خبری» درباره وضعیت مذاکرات میان ایران و آمریکا منتشر شود.
روبیو پیش از یک شام رسمی در سفارت آمریکا در دهلی‌نو، هند، گفت: «پیشرفت‌هایی حاصل شده، همین حالا هم که با شما صحبت می‌کنم، کارهایی در حال انجام است. این احتمال وجود دارد که چه بعداً امروز، چه فردا، چه ظرف چند روز آینده، چیزی برای گفتن داشته باشیم؛ اما همان‌طور که رئیس‌جمهور گفت، این موضوع باید به یک شکل یا شکل دیگر حل شود.»
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75656" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNENxJZ9Cy_PzEvfUk_l-iGzyA-t6nUyk8Q9S-2yzEaz0I_fHKB-tGVMt6VZ3khqXco_DuGlW_OiBWTnPmtPDaUfBQFzU09mbG657WjgTqXo4zMc5eV8p5t0u6aAcaB3TSY8XgDUKsSJ8nv4moXhm_AprdW7YVE3NWLHikN9sFLgaGoZ2e1vJcLnz23sX5amf6DOGuKESv0NWy-t86SprMhdJSSHJE3XyY30P7ulA8nttYMKAUX-MxaBNhg_SgMLWedg4hVnp5S10n5UY3-6HaP_AGIebCwU77SMBifRhSHIZ8DRgL4sWziHo9bZVWdidNoS-UfDrkObuD7NFBEjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز شنبه دوم خرداد در گفتگو با آکسیوس اعلام کرد که اواخر امروز با تیم مذاکره‌کننده خود دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند. او افزود که احتمالا تا روز یکشنبه درباره پذیرش توافق یا از سرگیری جنگ تصمیم‌گیری خواهد کرد.
ترامپ شانس دستیابی به یک توافق «خوب» یا در غیر این صورت، «نابود کردن کامل آن‌ها» را یک «۵۰-۵۰ محکم» توصیف کرد. به گفته او، قرار است اواخر روز شنبه نشستی با حضور استیو ویتکاف، جرد کوشنر و جی‌دی ونس، معاون رئیس‌جمهور، برای بررسی پاسخ اخیر جمهوری اسلامی برگزار شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75655" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYjHWZPi3AWA_msx7FrZQFyQCIPQTba3eVYXkdkEJMBixEgFAsGFjXzE1TlJ31USxou2cYrlDww5MEq_KI423OEqnfBFf-bqJGcvml85KoeQTp7Y1rUzoq_RHuOIBGxe5dAhFMmtMtYoyvGpTGDRXNfbfndQwBHJDyP0jnTrB0Q2HCTc-1HjoB3dmNjdC-8d__hkgW8c12YQ3Edidq6gLAWHGBVhgTRItwlXAxsXAkTqBWcEl9H1gQegwyLK-POJyjZ2jiE0X4-V9pSZ8XjwLYcBzdMoRvpL0kiGEOdcyyU59vOk_o_Eu3PIMV-SOg_LOEG7hsACpFT3jgrsPKBRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، رسانه وابسته به سپاه، درباره روند مذاکرات تهران و واشینگتن، با اشاره به اینکه هنوز اختلافات جدی در بعضی از حوزه‌ها مانند تعهد واقعی آمریکا به آزادسازی اموال و موضوع تنگه هرمز وجود دارد، نوشت: «با توجه به زیاده‌خواهی‌های آمریکا، احتمال عدم حل موضوعات بالاست.»
در این گزارش آمده که در صورت حل موارد اختلاف، احتمالا در گام اول یک تفاهم اولیه اعلام شود و سپس مهلت ۳۰ یا ۶۰ روزه برای گفتگو درباره موضوع هسته‌ای (بدون تعهد اولیه جمهوری اسلامی) اعلام شود.
تسنیم نوشت که آمریکایی‌ها در متون پیشین خود تاکید داشتند که تهران در همان گام نخست باید امتیازاتی در بحث هسته‌ای بدهد و موضوع تعطیلی تاسیسات هسته‌ای و تحویل مواد غنی‌شده به آمریکایی‌ها از جمله مباحثی است که مدام در متن‌های آمریکایی‌ها مورد درخواست قرار می‌گرفت اما حکومت ایران اساسا بحث درباره جزئیات هسته‌ای را در این مرحله رد می‌کند.
بر اساس این گزارش تهران بر ضرورت پایان جنگ و تهدید در همه جبهه‌ها از جمله لبنان تاکید دارد. و این موضوع باید مورد پذیرش طرف آمریکایی قرار گیرد اما آمریکایی‌ها در برخی از متن‌های پیشین خود با این موضوعات مخالفت کرده‌اند.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/75654" target="_blank">📅 19:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5cv4UNdgA2Ho2q_6IkzKVgm_k9lVFSLesJYeBN-9MljU4dZ3OJBZQz6sjHABGjLl2lHGgSa3BjjB_7aPWTCqIxkTZB1_wpD72TK29E2OglvqkyFvbVpanOBB3phhQUlzQayvzNOLYBoYfagCs1mfzWPjbfEFgtExDspzIcXv6YqUC4dJe9Ufn5NasU8eC2oSnPdbY0hG8MLRXNRGnYPKVivaVC5Omx88E6flMhbYgUguaSC7fIdQzO9ACMbH_ZlAJVnwj2oNbQJl572KLdAjPaPMPh7xETWkFVXuJ8lhDZB15kMseufKijL7RF_dlRRQDb-9Gv4jo8s8zJlEy8m9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخش رسانه‌ای ارتش پاکستان (ISPR) آخرین دور گفتگوها میان میانجی‌های قطری-پاکستانی و مقامات بلندپایه جمهوری اسلامی را «کوتاه اما بسیار پربار» توصیف کرد.
بر اساس بیانیه منتشر شده، این رایزنی‌های فشرده در ۲۴ ساعت گذشته در فضایی مثبت و سازنده برگزار شده و پیشرفت‌های دلگرم‌کننده‌ای را برای دستیابی به یک تفاهم نهایی جهت پایان دادن به جنگ ایجاد کرده است.
ارتش پاکستان جزئیات بیشتری از مفاد دقیق این مذاکرات ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/75653" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQEGD4uq5fqQHZFkIH7HKumRYmT05oT2jyxjdw-JTRPMV2L3eeIMzkJQbzi5ivUbGaCbdtOIcNuUBF4kLhIyefHMgkNdaXpdg6tYloVppAUc3uXXzdzjxU25xwMjjX4uX2FPNFrls6YpSxGt__QHYd4LgsrMrns4-i910pTNbWP89Q8tIh5pFXIuyOhX7wR1r39G4FPrAAiQLY9KgXOcKl6DDJ3TgOPrulReOwVY3wZ7m55i4HI8Qqpsad1bxgt9byWQtpKuk-MAidEwr3DpMlueCuNUN8AmK_lbe32-bKvrv2T238fEv2nz-o5SqPkLGidaUH9BqZQRLjHdYkumbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز گزارش داد که میانجی‌های جنگ ایران معتقدند در حال نزدیک شدن به توافقی هستند که آتش‌بس میان واشینگتن و تهران را به مدت ۶۰ روز تمدید و چارچوبی برای مذاکرات درباره برنامه هسته‌ای جمهوری اسلامی ایجاد کند.
بنا بر این گزارش، افرادی که در جریان این مذاکرات قرار دارند به این رسانه گفتند این توافق شامل بازگشایی تدریجی تنگه هرمز و همچنین تعهد به بررسی رقیق‌سازی یا واگذاری ذخایر اورانیوم با غنای بالا خواهد بود.
فایننشال تایمز افزود که آمریکا همچنین محاصره دریایی بنادر جنوب ایران را کاهش می‌دهد و با کاهش تحریم‌ها و همچنین آزادسازی مرحله‌ای دارایی‌های مسدودشده تهران در خارج از کشور موافقت خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75652" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=ZUmCJrlq38H4OBypdvRm6h9ykheOVS9g4YmIBRt-KQGaW3hUMlk2aiV620ir9443jF2_wsH0ZrpLeGvbL_GEChaRVeLYxe6F_33-5gkE9pOTat2B_8-_mAfjScbuV7lQA4qPoOgABP_6_R8l1cVCWVaYFwaZzeuz5v9opA6G8s-2YUEs-jL9ocWhm-GwRmjip1shVbBhDTcyD_7j3NWRs64nTQn6oWsP91KqPUZ4TRGcORrIgnyLN0OU1mT310APONob4GGe2UxlZ5vYbIvMej1LdG_ZPCenVfG9rdjFaCC-w7ePuMJv2DcyBv3BybIEBRPtsdDksmCb693l-WCv1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=ZUmCJrlq38H4OBypdvRm6h9ykheOVS9g4YmIBRt-KQGaW3hUMlk2aiV620ir9443jF2_wsH0ZrpLeGvbL_GEChaRVeLYxe6F_33-5gkE9pOTat2B_8-_mAfjScbuV7lQA4qPoOgABP_6_R8l1cVCWVaYFwaZzeuz5v9opA6G8s-2YUEs-jL9ocWhm-GwRmjip1shVbBhDTcyD_7j3NWRs64nTQn6oWsP91KqPUZ4TRGcORrIgnyLN0OU1mT310APONob4GGe2UxlZ5vYbIvMej1LdG_ZPCenVfG9rdjFaCC-w7ePuMJv2DcyBv3BybIEBRPtsdDksmCb693l-WCv1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‌ویدیوهایی از اعتراض دانش‌آموزان در شهرهای مختلف منتشر شده است. این دانش‌آموزان به حضوری شدن امتحاناتشان اعتراض دارند.
دانش‌آموزان در شهرهای خرم‌آباد، یاسوج و دورود مقابل ساختمان‌های آموزش و پرورش این شهرها تجمع کردند و با شعارهای مختلف اعتراض خودشان را نشان دادند.
در جریان اعتراضات سراسری در دی ماه ۱۴۰۴ که به کشتار بی‌سابقه معترضان انجامید در بعضی استان‌ها مدارس غیرحضوری شد.
با شروع جنگ آمریکا و اسرائیل با ایران، مدارس در ایران تعطیل شد و بعد از تعطیلات نوروز کلیه کلاس‌ها غیرحضوری برگزار شد.
چند روز پیش عبدالرضا فولادوند، سرپرست مرکز ارزشیابی آموزش و پرورش در یک مصاحبه تلویزیونی از احتمال برگزاری امتحانات به صورت حضوری خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75651" target="_blank">📅 19:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sRs7KCbZlK8iy0pVRIvUwTFyXnQp-2YwBtkCwRFNt5OK1nBWnSbKdty2ANCzcklH_2AKnc5IwAInrzO-wvbU_FRU2QWiS-WV4NdK5e9Ff4O81nT-altPkO_p632n0Q7a044eOi01WddiPuHIfVDtodT4sU5DmtrmuXdGkZmLjMEbkr0L70JesYz6uvRi288leQcio7TlclPFtnotST5hSi_j4nBybEgINrjUyD_dQ_1ls95g3pYfZfCQUanBOposlWRbTvNY8PCnPubkg25icHDvZS6itgxZHck-cB5TzrD5GbTrVxj_vbpYFk28QrsBOAuWRlsR1I9CYQFwK-0_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام جمهوری اسلامی روز شنبه دوم خرداد، در گفتگو با شبکه الجزیره اعلام کرد که تهران با میانجی‌گری پاکستان با یک تفاهم‌نامه موافقت کرده و اکنون در انتظار پاسخ ایالات متحده است.
به گفته این مقام، مفاد این تفاهم‌نامه شامل پایان دادن به جنگ، رفع کامل محاصره دریایی، بازگشایی تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
او تصریح کرد که به دلیل پیچیدگی موضوع هسته‌ای و نیاز به زمان بیشتر، این تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود؛ با این حال، پس از گذشت ۳۰ روز از اجرای این توافق، درب‌های مذاکرات هسته‌ای باز خواهد شد.
این منبع آگاه همچنین اشاره کرد که قرار بود فرمانده ارتش پاکستان این تفاهم‌نامه را در تهران اعلام کند، اما او جهت هماهنگی با واشنگتن، ایران را ترک کرده است.
او با تاکید بر نقش اساسی دولت قطر در تدوین این پیش‌نویس افزود که ایران هیچ امتیازی فراتر از آنچه در این تفاهم‌نامه قید شده، واگذار نخواهد کرد.
@
VahidOOnLine
همچنین بر اساس این گزارش، تهران پیشنهاد داده غنی‌سازی اورانیوم بالاتر از ۳.۶ درصد را به مدت ۱۰ سال به حالت تعلیق درآورد.
@
VahidOOnLine
🔄
آپدیت:
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75650" target="_blank">📅 17:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAdViiswen9WQB5Zzb4_NJ98LRYAonQM7WbEz8ya_5WC8TXCICr23cNoxipBcfLo9P2OLkHHFxl0JrAJMkoF_h5inlTjwq7AHF0lb03LEOk-KAICNpxnR7VMCRT0uW-4ilGiT--mzNopq_ABm1OLzCxEj4p3yboZnM7H-yJHf1B5kLRaDsgmKW60lH175qVJMxokzQpnterDEcyrAU3dUP3OUCSIlqJY1UzEb5Yo98gsaiSI2w2xrvaAy-9-DOkpGOCRWkpXzThnic5HLqtQ_--Gg4zX32xXXc4oFQ5bqBSEmf_1TGKrmkUWBdAbUA68ITKOBjWCMe5rLA98Y80J-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه گزارش داد جمهوری اسلامی دو پیشنهاد به میانجی پاکستانی ارائه کرده که بر اساس آن، در ازای پرداخت غرامت از سوی آمریکا، تنگه هرمز را باز کند و پیش از امضای هرگونه توافقی، پرونده تحریم‌ها و دارایی‌های مسدود شده مورد بحث قرار گیرد.
دونالد ترامپ، رییس‌جمهوری آمریکا، پیش‌تر گفته بود که حاضر به پرداخت غرامت به تهران نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75649" target="_blank">📅 17:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NkJ-Pdo-CGhuNFDwmQy1Ko-vwc7rnizxz2VLGMSYBErJv2kTPoS0cC03P2-qgd966xm_FmqWMshVXDKZVXPhzC9XRekIRAr8aIHaRxFiOwiVfrPbLEJkam2C6R5EW7qlQ2ze-ZxEiU0Jg_TtWhtz9YUSw7eLCv3smlc0YjoaGpvTWsx6N2qIS98fT9A7NKRk8z1qDX5_JVNsDPFi95yooOTN2JudcopHGYP4FgLy7gNwN5O3miIc1DyTm4jNoBH8AGJQoEC5jZKbwse8zzU4MlLU6dQZgpuh9vXe3p1SC9Q6lKWTnXdrjizfWYzhzIBOb9T-8fSZ5Egb1r2WNG4CWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری از نقشه ایران را که با پرچم آمریکا پوشانده شده، در شبکه اجتماعی تروث سوشال
منتشر کرد
. روی این نقشه نوشته شده است: «ایالات متحده خاورمیانه؟»
ترامپ توضیح بیشتری در این‌باره ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75648" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=qUwt3STXy62PwpmHyHNDW1-V0nv4-o2T3Ia20I04P6FTYVwyuObr14Lcyfm-VZMLtzDxhErXGHWySxNXC41DVFXCNL9CrkdUJJtN3IBtSGre2oNpX06odh3actxnXm8_IUkUfY0em4EH_-ZyA5ZvwTh5LOgmkB6EM1h-Vb8ko8lJr_-9S2eraWf-zMOC0oymDQVh-SuaMfzo0f4jfkjr8Kd8vp2Zm2U3KmtbOHA0N-g7bYzGeluyyAfSennTN4j42HQxUPd5RuGglesVBTdu_tgnyML5RkaIiZ5Qpol08YStMX9rHkRlJnLgxaJNu5Q4FYHKtVR0StMSGlz-G4Unsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=qUwt3STXy62PwpmHyHNDW1-V0nv4-o2T3Ia20I04P6FTYVwyuObr14Lcyfm-VZMLtzDxhErXGHWySxNXC41DVFXCNL9CrkdUJJtN3IBtSGre2oNpX06odh3actxnXm8_IUkUfY0em4EH_-ZyA5ZvwTh5LOgmkB6EM1h-Vb8ko8lJr_-9S2eraWf-zMOC0oymDQVh-SuaMfzo0f4jfkjr8Kd8vp2Zm2U3KmtbOHA0N-g7bYzGeluyyAfSennTN4j42HQxUPd5RuGglesVBTdu_tgnyML5RkaIiZ5Qpol08YStMX9rHkRlJnLgxaJNu5Q4FYHKtVR0StMSGlz-G4Unsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان مارکو روبیو در سفر هند در پاسخ به سوالی درباره مذاکرات با ایران
ترجمه ماشین:
ممکن است امروز کمی دیرتر خبری باشد. در همین لحظه خبری برای شما ندارم، اما ممکن است کمی دیرتر امروز خبری باشد. ممکن است هم نباشد. امیدوارم باشد، اما هنوز مطمئن نیستم.
سؤال در مورد موضوع ایران است و همان‌طور که گفتم، پیشرفت‌هایی صورت گرفته، پیشرفت‌هایی حاصل شده. حتی در حالی که الان با شما صحبت می‌کنم، کارهایی در حال انجام است.
امکان دارد که چه امروز کمی دیرتر، چه فردا یا چند روز آینده، چیزی برای گفتن داشته باشیم. اما این مسئله باید حل شود، همان‌طور که رئیس‌جمهور گفته، به یک شکل یا شکل دیگر.
ایران هرگز نباید سلاح هسته‌ای داشته باشد. تنگه‌ها باید بدون عوارض باز بمانند. آنها باید اورانیوم غنی‌شده خود را تحویل دهند، اورانیوم غنی‌شده با غنای بالا.
ما باید به آن مسئله رسیدگی کنیم. ما باید به مسئله غنی‌سازی رسیدگی کنیم.
این‌ها نقاط مورد نظر رئیس‌جمهور به طور مداوم است. و ترجیح او همیشه این است که آن را از راه دیپلماتیک حل کند. ترجیح او همیشه این است که مشکلاتی از این دست را از طریق راه‌حل دیپلماتیک مذاکره‌شده حل کند.
این چیزی است که الان روی آن کار می‌کنیم. اما این مشکل حل خواهد شد، همان‌طور که رئیس‌جمهور به وضوح گفته، به یک شکل یا شکل دیگر. امیدواریم از طریق مسیر دیپلماتیک انجام شود. این چیزی است که روی آن کار می‌کنیم. و شاید چیزی برای صحبت در مورد آن موضوع در حالی که اینجا هستم، در طی این بازدید در زمانی داشته باشیم.
EricLDaugh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/75647" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCyNoIopM4UCIjXN67xtv0dQzU7Joc2ars77urM3UW9uigKcqqoSAFVk4IG4LEVWlWQEWzs7AzAQHv5-i0EMIoKfwEWimuVauPTt2Vrk9IhTkhY83t6LF5oBC1MZw1cjxiXdk4MJOx1XBVkNGNaRAaFrNZjjPeb5lXMrfT3hPE0_10LNTLPIHB9DOuUjRvTDcF--YA68Wdb1LK_WLo519WQ9nkus_cDuJVznf6OD-CHDBnXlwdPCZKuj55Sc3I1RkVM2GQwMKD1v35iCn2QOqP3O0M9IcVrsNaIN7-10UuYWydZUDJ9PiIPMhHQAVAhRhHHd9j-c_jjckp5a3L5vKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «جمهوری اسلامی دست از حمایت حزب‌الله نخواهد کشید و همچنان از جنبش‌های مطالبه‌گر حق و آزادی پشتیبانی می‌کند. تهران پیوند آتش‌بس لبنان با هر توافق احتمالی را به‌عنوان شرط مطرح کرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75646" target="_blank">📅 17:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN7Tr2XmQPnAwY6mIe1O7NHOMT-bgZRGPen207ge6PviFs4ehcfKaUdN7zxPjS8i5mSjr_QKEr_8nF0Sdn0yQOROAeBy1BbSwF_G34FDJbX32yHEQs2lc9Sxx6H79Gf5WOxlE8Fg-iSeYgb4XcuB7noUJX8IvKoV6zE2rwYr56Rlfak2fMId91DEZG__4d-bzQkzvDHrlSViNa9TUBvOyeuN0Mg3ucmjFsDU3vPjvbF2pYzjVMh1wJSU0tv8ktdgcovwv1K7HP-r_ox6NYycpsW8LWucA5R-Xlqw1S_GFFAxR-HYiyWkTdNyzxFJtPYSrCM4hgEh_gK4u7jy9DRzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز قلیچ‌خانی، کاپیتان پیشین تیم ملی فوتبال ایران و فعال سیاسی چپگرا در ۸۱ سالگی درگذشت. او به آلزایمرمبتلا بود.
نجمه موسوی-پیمبری، «یار و همراه» پرویز قلیچ‌خانی به بی‌بی‌سی فارسی گفت: «قهرمان ملی و چهره همیشه زنده ایران در تاریخ بیست و سوم ماه مه ٢٠٢٦ مصادف با  دوم خرداد ١٤٠٥ در بیمارستانی در حومه پاریس درگذشت.»
آقای قلیچ‌خانی، پیش از انقلاب، علاوه بر تیم ملی، در باشگاه‌های تاج، پرسپولیس و پاس هم بازی کرد. او تنها بازیکنی است که با تیم ایران سه بار قهرمان جام ملت‌های آسیا شده است. پرویز قلیچ‌خانی بعد از انقلاب هم در خارج از کشور، مجله آرش را با گرایش سیاسی چپ اداره می‌کرد.
او فوتبال را از کوچه‌های محله صابون پزخانه میدان شوش تهران شروع کرد و بعد از مدتی کوتاه فوتبالیستی ماهر و بالاخره کاپیتان تیم ملی ایران شد.
ولی هنوز طعم قهرمانی فوتبال را درست نچشیده بود که توجهش به سیاست جلب شد و از پشت میله های زندان سر درآورد.
پس از انقلاب از فوتبالیست حرفه‌ای به فعال سیاسی و روزنامه‌نگار خارج‌نشین تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/75645" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RhB1CT5K0_4TneeAhcC67n6jMAT22hkhWc8zeINsKNvnLusXyDthqKAO3v6BaMx00nRIn_QKkbjc3wbrdh9MnMCL8sr3XWseRAgascPbAm2iFlOKCUCSaF422452tSATfOaXoQ3j5TwIZO7E7za0_idETF__AsK9c7CX1fe8cOidVfawJdk_P41WjEV09vHAtSlBvOblqc8Et5OyXRczGi6wouDRTsilOg0Y-4vQ5rnTSdv4rs9cGnZmeqMHYfFOHRnh5sNmhShvDkV9MHhqcxAYchZbfwVNNbqJLL8WodB8oooFkFuRgaT4MU_tAVxM2Xvn8DNh2FnH6PUbnrIX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/buMTaZhj2NGlY_rl3hyPOL8u2joc5THPUd-EshbKd28ce2TB8mS3zBZH7YH7DxHnsufUNR0TucThwf-OduciQOheBlQ9KCnOtSmGGR_kiIHox2wLe7xQn0vqZhAdbUriZjLVialODFJ0AImis8lXKvXsKqpelo8Zg9MU5N88o3QiF79-nkPp7gTErRp1Duvn45TkqFEMnuZHr8PedXEPIG4YAyvOrRH-Yg-5KzGAB53W2Csg-JHwNT4o0rBbuD0qHkndKGYI_QckSbkkDOKCFXxHIrB_oE6Yk7po9lqQKeYy7Wo3zw6S0xpaAlcZls2YebNyr_Pm-y39Enjy34jrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kaak-dl1-awWUnJbscl-epRj095xb9quuIQu1eUbciHgESDIXiLdzMiMmXL-GySok_fxcLsAPGPBUO99SDd6O_BhZfbMnbTE52Bq60fmzEjVg680lQIOXwbiKRyXd17TnxoBhW3BP1CU_P5PzMWpc-KnIPg6jEX52eK5-CX1B546zhjHmn64UBlLz9d_qN3OxDXQsjrfsquOx92xJB6ZnCKALo5I_eZE2zf4qoRuxvMxwdgHnQwAPS_K7pD1d6tHUE-0b2gFbHP9VwqogAuzsyZjVn4X-W6sA_HGjy4n705kP9EvhS8XDD-_DMoXbock2ydZAcDO9Oqg_YqWaOwQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCmUkFxQuUJhv716t9BhLx7txx-3HBN34-S5FUIKn0ZOz5y0c3aELLoEJVpzTqUQUwQcWH2JmQyKvGxKvfW9mHuso6kWTymKO8_z9en2UKpSLDua7c1hWURKPJ_EL9ZB0oAamwPBI07OPCgUmfDRbwnGzqi3TffcBKO-_AWU3rF-0ThpwnpPp21OXnsYaKjF-1ZU9OP-SOwryAMRNQEhscvbz8wxpWwaxMW6Ed1R6fN4d1bgC5dHBJQoNTUJMStw_5ZsEbXwXRHtBL5lV7lqbSBhviLU74-hJyyzJJh0d4WqKpdLwW015rheQPxpINT4PMoiyVwFxXTlSeY-nISm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E1I_ROMkEwdYg30_Cv6MfMY-yQn9V5qKW5cpelYu0gEOjc9wcGMXhyoU2kqtkb5v5Hm_AdE0zE2ZreOix-aZMS2qtabmZPe92Vk_eLQjbe0xjAEGrx3twNLTKG6mGONnC6sEEaq2sZgQv3YH-Pth21GdNR_0t_eZMJEdLSiVhfYa05jRMLQwBDkvJC3QvT1ZVUCeX0CbO2A9vWXSleycfy9htvcRSNSyKhQXx3RXKYnHRt98AWj7jxs3mlJjpx6OyKxWn5RXmENXWBud2Du4xlgIg4BkGePQkEuKr4UJeshxSHBoTstmmLIW436snf_dwYkqDJLx4DaVbHqGNTq0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kIUdvqWLKcQ-HIEM6X81xQYw-ghqqakr2pSTvoOqMu5cM18iSu5iI4_Krk1-dw-2uKB394Jbmcxl7-hdXOnb1tzBIG9R_gdPfFG3QBQkqbTvkeAIq4QmYXC7YBgrXIL-BeRFVsxCPGdjPXMbXfQBJ-70iEUwWU0WIqVcoUerU4eP4taISP8GuDElewRt9mStr6I9IaaEBVApHr1EQTL8G5rKp_CnKM4k5DbmI-Q0kKD3Z-r6xpqd6owTvukZOR5jzRk71DCcHR8YyMl2OG2f6a6Dbjr7B8srdji1Jxc0j3ht4R9_-DZP92WH9Oninbvjyql1AP8guslZPq5qotELew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B-lTGItcfL0zPH6cHqubzPEiZ_94DHuO6IVMAvSROHaamoah4YD68jmyXhDe75g8er8kVVunXE37sM0skqTV7IuOan-IElaRfK7oZY2L3WyU3meu1waTWkR7bjwkpIMElxzlp1Hdx4HTpjDQFB6rOV0VOqfExB4T8_kmb3YP5EocVFFcJZ2AnlYwacajKJ41cy0GLe7txptsWak9t7hIezVTGjOJw9S1hQaTtc-Pr2yIMwsRvdI_5d-FiGQmcD-p48xLK4O8i-1Lyw9W3OIXGqAdNFWbbanENuc3jRCUULV7Hkb0wJpB91McPspS7XtjoMvqrBwc6-kY9uFkrqc3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q0ZqS8odU_s8K4PfivZTBcdgzeU2_WLL44nFiG0xgLcieSo5ZSylO4sAIRaZQXMxG70z2hHucYR8nTzQ7qQ1kP-dSc-FxOiJNe8MxxIZ8OlTuQb0fuQ5pUBdHyr7YfGIy9Rb__S8MY0X1JJxkuPvQT9fUXsYqhxHzZR8t6l9KyD7EhXFAQPt_lR8XH0DLK8f7rIT2-l87miO6atFRu8-8iKiETCFP26-VUOucP0oJJuHUhI3nD0xn_L6xRgB9v6_SPiZY63CnwhVd_Yn4h8slzhRn_Gsesvnjki7J7CKRmly8L10WnygdvHhcQ3O7uoEmOUIZQX7BXH9EjKZS056gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJVUvKoNr4lyzq_cr4GfzSeQtw6tmY27JUmEw3cr6ZuYFLpH5wr7EG0CLi7IvpQxUDn8XDTjubtvo7jdM4O-VeA8GDVcptfvypgxCl1votIicyPNIlyMYWhMY2n4pWDseEv887sPn_PomPNeZgubb9lnyG9uSjHZnUTlcSe82CXirmha1Hc7JqifvxYN6QyhB0q2TZ2ISkVq-yoiGo3pdP0J7bR1PYsbQYUxPgDv6ciwNLwoCXtTaR1ZMhXgp6L70SuXfA-AMcs6o2EqzSysg-jY0aap1cwHHoIBMrQ8FEODkQSMsNpW8jC557C0XhGYCcmGI0QZ-olW8keGr63Y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gvcXpbokpQkJmA1VZPerbmL-X6OJ4DPRmjuUJezz0riHBK2x5YTHokmvBlonKZz0ez7sYHmnSDR-CL9t05UgvChK1qSAhtTzB2h-jBZ4nbL_aPtOvck0G8rHl7pJ8evU_8OFygh87lFYcibDJc6-xk3vl_YaPM4qEm0EFE-LxjyXErk9czxFgZKFO2Y_0_zK2JPgQCDGEhY5L6PHqU0qEsoHK5A_OB6i0KtXCqYTSUmlD_lXKuxKCkwbbV9euDO8cFtwghdQ_7MJGBwQOSAb0LXugmWcezKWaOK1_0fErLq1ulAbp33zp7z1Ob8MzpGwDyiQweTa3ctSVyn-EPf4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد عاصم منیر، رییس ستاد کل ارتش پاکستان، پیام‌های آمریکا را به تهران منتقل کرده است و بخشی از این پیام حاوی تهدید به ازسرگیری جنگ بوده است.
در این پیام‌ها همچنین تاکید شده در صورت موافقت جمهوری اسلامی با توافق، حل مسائل اختلافی در مرحله بعدی انجام خواهد شد.
به گفته این منابع، آمریکا در پیام‌های خود تصریح کرده است تهران باید اکنون با توافق موافقت کند یا با پیامدهای منفی روبه‌رو شود.
@
VahidOOnLine
شبکه العربیه،  روز شنبه دوم خرداد ماه، به نقل از «یک منبع بلندپایه ایرانی» گزارش داد پیشنهاد ارائه‌شده از سوی تهران تاکنون نتوانسته رضایت آمریکا را جلب کند و همچنان از دید واشنگتن «غیرقابل قبول» تلقی می‌شود.
@
VahidOOnLine
عاصم منیر، رییس ستاد کل ارتش پاکستان، پس از سفری یک روزه به تهران، ایران را ترک کرد.
به گزارش ایرنا، او به همراه محسن نقوی، وزیر کشور پاکستان که از هفته گذشته در تهران به سر می‌برد، پایتخت ایران را ترک کرده است.
عاصم منیر در جریان این سفر با محمدباقر قالیباف، رییس مجلس، مسعود پزشکیان، رییس‌جمهوری ایران و عباس عراقچی، وزیر امور خارجه دیدار و گفت‌وگو کرد.
@
VahidHeadline
محمدباقر قالیباف در دیدار با عاصم منیر گفت نیروهای مسلح جمهوری اسلامی در دوران آتش‌بس بازسازی شده‌اند و در صورت آغاز دوباره جنگ، واکنش ایران شدیدتر خواهد بود.
او گفت: «نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ‌تر از روز اول جنگ خواهند بود.»
قالیباف با اشاره به نقش پاکستان در میانجی‌گری افزود: «در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است.»
@
VahidOOnLine
شیخ تمیم بن حمد آل ثانی، امیر قطر، روز شنبه دوم خرداد ماه در تماس تلفنی با دونالد ترامپ، رئیس‌جمهوری آمریکا، آخرین تحولات و رویدادهای فوری منطقه را بررسی کرد.
بر اساس بیانیه رسمی دیوان امیری قطر، این گفتگو بر «تلاش‌های منطقه‌ای و بین‌المللی برای حفظ آرامش کنونی و کاهش تنش‌ها» متمرکز بوده است.
«امنیت دریانوردی، حفظ ایمنی آبراه‌های راهبردی و تضمین تداوم روان زنجیره‌های تامین جهانی و انتقال انرژی» از دیگر محورهای این گفتگو توصیف شده است.
به گزارش رسانه‌های قطری، امیر قطر در این تماس بر موضع ثابت دوحه در اولویت دادن به راه‌حل‌های مسالمت‌آمیز برای بحران‌ها تاکید و اعلام کرد قطر از همه ابتکارهایی که با هدف مهار بحران‌ها از طریق گفتگو و دیپلماسی انجام می‌شود، حمایت می‌کند.
این خبر در حالی منتشر می‌شود که رسانه‌ها از گفتگوی تلفنی وزیرامورخارجه قطر با عباس عراقچی خبر داده‌اند.
همزمان گزارش‌ها از رایزنی‌های گسترده کشورهای منطقه برای جلوگیری از حملات احتمالی آمریکا به ایران خبر می‌دهد.
این در حالیست که شبکه خبری العربیه پیشتر از هشدار واشنگتن به تهران مبنی بر از سرگیری حملات به ایران خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/VahidOnline/75635" target="_blank">📅 17:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slZM5eKFMKI6jotGwV6ny94r2srqv5364uvyyfdz5S_Q5DWby_xfEcJI5JkD3EaT7VqzbWX2HPHd1xyOeIdA3IFyFxAnapRCpFyNB_-DC_oa2zU41z1U9EkgLDj1B-bD7ITKY2xWLlS5lxUm2HzqeG5mkqCD5tpdenO_5mkwVr6o4u452ErdxZtj199EfBVhxixTPU3PPk3jUX0zZkIeyMLmpt4fn8faPIQkqpsjVSc9VKYwDokCO_4KHQNd0W-lT8Nv1hL-iXsNU7DtJZDm-7_DnydwlYuUPm4dUZ_BfQRQ0B0pzhIdg34DlEgqzlM3bsg9dxZzktFilNzvWlgnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان هواپیمایی ایران اعلام کرد این سازمان هیچ اطلاعیه رسمی هوانوردی جدیدی درباره اعمال محدودیت در آسمان کشور صادر نکرده است و شرایط پروازی عادی است.
او با تاکید بر تداوم وضعیت عادی پروازها گفت: «شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود.»
سخنگوی سازمان هواپیمایی بدون اشاره به جزئیات اطلاعیه هوانوردی (نوتام)، افزود: «نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.»
سازمان هواپیمایی کشوری ایران روز جمعه یکم خرداد در اطلاعیه‌ای اعلام کرده بود فعالیت فرودگاه‌های واقع در بخش غربی محدوده پروازی ایران، موسوم به «FIR تهران»، تا دوشنبه متوقف شده و تنها شمار محدودی از فرودگاه‌ها مجاز به فعالیت هستند.
بر اساس آن اطلاعیه، فرودگاه‌های ارومیه، کرمان، آبادان، شیراز، یزد، کرمانشاه، رشت و اهواز از این محدودیت مستثنی شده‌اند و فعالیت آنها نیز فقط از طلوع تا غروب آفتاب مجاز اعلام شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75634" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxO4De3iu2OzriNoB3Mg6c13kXzG5v9bcWt8cvHAupcT-PcoF1APrUS8ZVSa25RbUtL82zPFPnIcxs2FQ4UvLL23qDXtBghN1X1F_GrARmXwjN4z3haErhCXSoU6XKYAEggKAF_oEh-yxrKBjXGDr1EJUj2tQi1LPTr45JcE6mhRFiquktCLn72KAx2veqU4KC7XL82vWhqWsRydGFcxWQ1NWTSHu76JzpCOn-ZA4gfcetsImmA3GlENaCoux0DSgt4A_mrE8BID_Dbr5cM9D7lWWgNbmLgW3WFKc7-d5PJoq5tpQ0nL0AVMkFllO6oeHWiK2ZlEPGmV0CYw4gVmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از دیدار فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان با عباس عراقچی، وزیر امور خارجه ایران در شامگاه جمعه یکم خرداد خبر دادند.
بر اساس این خبر، دیدار این دو مقام تا پاسی از شب ادامه یافته و محور گفت‌وگوها «تلاش‌ها برای جلوگیری از تشدید تنش و خاتمه جنگ» و «راهکارهای تقویت صلح، ثبات و امنیت در منطقه غرب آسیا» بوده است.
جزئیات بیشتری از این دیدار منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75633" target="_blank">📅 08:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlUaOp3OUCk-6GZvJgoe9AutZEYSNu9iO4WpfuPkOGHbgOL52wOs2Lure6MsYIv_qoQQ6b7x8eW_TVq3ccVraTaAlp6uLcK_jQ4qpAu4MUAnEVIjQeZLt1BccALo4Nwm-J2HGMDc6ohZyraXMBK0IL6IOSERSkJIfnADB8yOO2ylGZIopr4K3tkwUU175R8N0LdG7psaKslR2T719Kv-6pnMSM5aOKHL7848B3LfJX8nrEzbXUTBmtKATX3aZSqfX-x4ZGLIWWZaF8m8dYVb2fXye-eUIemEqyygdepBbEIvMXiGyFKpwDMAyPSFPF3rrNjGdsoRP2tn2Me0y3ZKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ اعلام کرد که سیاست‌های مهاجرت به آمریکا تغییر می‌کند.
در یک تغییر اساسی در سیاست‌های مهاجرتی آمریکا، دولت این کشور اعلام کرد خارجی‌هایی که قصد دریافت اقامت دائم یا همان گرین کارت را دارند، باید خاک ایالات متحده را ترک و از طریق کنسولگری یا سفارت آمریکا اقدام نمایند.
زک کالر، سخنگوی دفتر مهاجرت دولت آمریکا، گفت که این سیاست «نیاز به یافتن و اخراج» کسانی را کاهش می‌دهد که درخواست اقامتشان رد شده است.
از سوی دیگر وکلای مهاجرت و گروه‌های امدادی می‌گویند که این تغییر احتمالا به «جدایی بیش‌ازپیش خانواده‌ها» منجر خواهد شد و قربانیان قاچاق انسان هم مجبور خواهند شد «به کشورهای خطرناکی بازگردند که از آن گریخته‌اند.»
این تغییر سیاست تازه‌ترین اقدام آقای ترامپ در محدود کرد مهاجرت به آمریکا است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75632" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m26U4S-unpJpF7yM-lwn2cwHYj_XDuW13OBwUANY9B-GeBRQ3rM8JcyYe1blSumcbHi5r9XflERkaYLsqNp7paO5VTjfRBUWWr3Y-MXCSdVyLUuUld5KQAQ7r5Xi_TAMvlC5iDONzykJaWUFuFadIvWUVEUoMv1kljRsRl2iR7Vrfh64tWYj-w4xBX_432hhOKkaI4SSMjeuNaaP3vIJZg8Sqehhw6dJ7a8m3iPshwUV5oetbc9uEkM8gCxGELht1-SUkFNPayAunLDU9COyMGD3GHF-eFf1kiMv0HvpkTFJcY2uXeJZvrOMNuzz-0e8hHZ94V_nB4deZlMQaiIUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «نیویورک‌پست» به نقل از منابع آگاه افشا کرد که ایوانکا ترامپ، دختر ۴۴ ساله دونالد ترامپ، هدف یک طرح ترور پیچیده از سوی یک تروریست تحت آموزش سپاه پاسداران انقلاب اسلامی قرار گرفته که با انگیزه انتقام‌جویی از کشته شدن قاسم سلیمانی طراحی شده بود.
بر اساس این گزارش، متهم که یک تبعه عراقی ۳۲ ساله به نام «محمد باقر سعد داوود الساعدی» است و به تازگی دستگیر شده، عهد کرده بود برای «به آتش کشیدن خانه ترامپ»، دختر رئیس‌جمهوری آمریکا را به قتل برساند.
منابع اطلاعاتی اعلام کرده‌اند که الساعدی حتی نقشه و جزئیات معماری عمارت ۲۴ میلیون دلاری ایوانکا ترامپ و همسرش جارد کوشنر در فلوریدا را در اختیار داشته و پیش از این با انتشار تصویری از موقعیت این خانه در شبکه اجتماعی اکس (توییتر سابق)، به زبان عربی تهدید کرده بود که «نه کاخ‌ها و نه سرویس مخفی آمریکا» نمی‌توانند از آن‌ها محافظت کنند و انتقام تنها مسئله زمان است.
وزارت دادگستری ایالات متحده اعلام کرده است که الساعدی از مهره‌های بلندپایه در حلقه‌های تروریستی وابسته به ایران و کتائب حزب‌الله عراق به شمار می‌رود که در تاریخ ۱۵ مه در ترکیه بازداشت و به آمریکا مسترد شد. او در ایالات متحده با اتهاماتی سنگین پیرامون هدایت و اجرای ۱۸ حمله و تلاش برای ترور در سراسر اروپا و آمریکا مواجه است؛ پرونده‌ای که شامل بمب‌گذاری در یک بانک در آمستردام، حمله با چاقو به دو شهروند یهودی در لندن، تیراندازی به ساختمان کنسولگری آمریکا در تورنتو و آتش‌سوزی عمدی در معابد یهودیان در بلژیک و هلند می‌شود.
این متهم که به دلیل وابستگی به قاسم سلیمانی او را مانند پدر خود می‌دانست، پس از کشته شدن سلیمانی در حمله پهپادی شش سال پیش آمریکا در بغداد، تحت آموزش‌های نظامی و اطلاعاتی ویژه سپاه پاسداران در تهران قرار گرفت و ارتباط نزدیکی نیز با جانشین او، سردار اسماعیل قاانی، برای تامین مالی شبکه‌های تروریستی خود داشته است.
اطلاعات فاش‌شده نشان می‌دهد الساعدی با وجود نقش برجسته‌اش در شبکه‌های تروریستی، حضور بسیار فعالی در شبکه‌های اجتماعی نظیر «اسنپ‌چت» و «اکس» داشته و تصاویری از رایزنی‌های نظامی خود با قاسم سلیمانی را نیز به اشتراک گذاشته بود.
او با تاسیس یک آژانس مسافرتی مذهبی و با سوءاستفاده از یک «گذرنامه خدمت عراقی» که سفر بدون تشریفات امنیتی و اخذ آسان ویزا را برای او ممکن می‌ساخت، به راحتی به کشورهای مختلف سفر کرده و با گروه‌های تروریستی ارتباط می‌گرفت.
الیزابت تسورکوف، پژوهشگر انستیتو «نیولینز» که خود ۹۰۳ روز در اسارت کتائب حزب‌الله بود، تایید کرده که روابط الساعدی با سلیمانی و قاانی فرصت بزرگی برای گروه‌های شبه‌نظامی عراقی ایجاد کرده بود. الساعدی که در زمان دستگیری در ترکیه در حال سفر به روسیه بود، هم‌اکنون در سلول انفرادی بازداشتگاه متروپولیتن بروکلین، در کنار دیگر زندانیان سرشناس نگهداری می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75631" target="_blank">📅 04:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9TqMfsgMHUnXMxPQYeUKNVtr1UewOPy5U6HeZd9DqLGYF3k7Dj0m99AMlRKndYwUo5ZujRUOwLafX-82qnEyaM9zlJrV-2oRYubMvG_1BWTaB-FZXQGyA7C-jK8ngEi2bfL-qf5jzSRli-PB8X1iVjpc_w3Rxqp8fimr13Nbhqd0WeA299WE5vQ13i4KMXEb-tNV8k-rgPxSEDhDe6sM27wVRFh7j1kUO9M062QAZaWN6_cIQezh3cnmmXIru9Q0PfdhsCPG9RwcVj0zxWOue7CdLHy8W_l90juiY-wagb_NlwYm-rx0v7EuzXnP75UqCglTtfMcEOwCqFTnP-0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس گزارش داد که آمریکا در حالی خود را برای دور تازه‌ای از حملات نظامی علیه ایران آماده می‌کند که تلاش‌های دیپلماتیک همچنان ادامه دارد.
به گزارش سی‌بی‌اس نیوز، منابعی که مستقیم در جریان برنامه‌ریزی‌ها قرار دارند می‌گویند که دولت ترامپ روز جمعه در حال آماده‌سازی برای حملات تازه بود هرچند تا عصر جمعه تصمیم نهایی گرفته نشد.
آقای ترامپ در پیامی در شبکه‌های اجتماعی اعلام کرد که «مسائل مربوط به دولت» مانع از حضور او در مراسم ازدواج پسرش، دونالد ترامپ جونیور در روز شنبه خواهد شد.
او قرار بود تعطیلات آخر هفته را در مجموعه گلف خود در ایالت نیوجرسی بگذراند، اما اکنون به کاخ سفید بازمی‌گردد.
چند منبع نیز گفته‌اند که برخی اعضای ارتش و جامعه اطلاعاتی آمریکا برنامه‌های تعطیلات خود را لغو کرده‌اند؛ اقدامی که در انتظار احتمال حملات تازه انجام شده است.
به گفته این منابع، مقام‌های دفاعی و اطلاعاتی آمریکا در حال به‌روزرسانی فهرست نیروهای آماده‌باش در پایگاه‌های خارج از کشور هستند؛ همزمان با خروج بخشی از نیروهای مستقر در خاورمیانه، در چارچوب تلاش برای کاهش حضور نظامی آمریکا در منطقه و نگرانی از واکنش احتمالی ایران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75630" target="_blank">📅 04:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgk3yIYrz6U-s4xHilckciWrx1GglvxijDvCngXe3g7zPuDPyXejXrSk4zWIVQJRjTGQTX-W5S9kJhYT-3zBDg9pY6XWD5dqGvq1dFVJaik-NPvXJTD4bubJ08p7HOu-8lruQoTQGCqi0qyFWwWQLV0PR4nBRrdFTAcopTHZwP5pyFHkugXcT26UqWhM4OmaaSRQy5cnXUr2EQYkNyJHa5Kh2wcUD90AicLz-WHzQrW1aA9s0zh0AArdsmNQBpzQneeraiujnQdc-Q62aHz_eWsq1ard-1HPR46Pj2r6rAGqq6zDIIWo6zfAPLcSiAzGvPOK7P9xVoDcA6h03wJlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه با تیم ارشد امنیت ملی خود در کاخ سفید دیدار کرد تا سناریوهای مختلف در صورت شکست مذاکرات و احتمال آغاز حملات جدید علیه ایران را بررسی کند.
در این نشست حساس که با حضور مقامات کلیدی از جمله جِی‌دی ونس، معاون رئیس‌جمهوری، پیت هگست، وزیر جنگ و جان راتکلیف، رئیس سی‌آی‌ای، برگزار شد، ترامپ در جریان آخرین وضعیت دیپلماسی قرار گرفت.
نشانه‌های جدی از تغییر برنامه آخر هفته رئیس‌جمهوری، از جمله لغو سفر به باشگاه گلف بدمینستر، بازگشت به واشنگتن و حتی عدم شرکت در مراسم عروسی پسرش، دونالد ترامپ جوان، نشان‌دهنده وضعیت اضطراری در کاخ سفید است.
منابع نزدیک به ترامپ می‌گویند او از روند کند مذاکرات ناامید شده و به سمت گزینه نظامی متمایل شده است، هرچند هنوز تصمیم قطعی برای از سرگیری جنگ اتخاذ نشده است.
در همین حال، تهران به کانون تلاش‌های دیپلماتیک «لحظه آخری» برای جلوگیری از شعله‌ور شدن دوباره جنگ تبدیل شده است.
عاصم منیر، فرمانده کل ارتش پاکستان، به عنوان میانجی اصلی، در سفری حساس وارد تهران شده و قرار است با احمد وحیدی، از فرماندهان کلیدی سپاه پاسداران دیدار کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75629" target="_blank">📅 00:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2W-IyBM_1Yw4UiHO7IMi-QE1r2mELCEZK2p6sDremfLtgIa0R2NZpXTewPlJE3o31hDTPHmrGq4gWoASJsLEqfMVlydQXYUpkue5e-TKQyGMXuotAPXbk_Z8A9VulyFpmWODW3XiqzBb4Se2lNrf6a8tvtvkU0ww-tO9oCq1zOlk4CkZxA12NfSnq-OT1spDLSG4D64rjQ6fj2PxztKEkRNq0jHsG7GiQ4dsDsB5adfD9skqHhpbLR02j3Vi3XUUydS_Mr-razNz6d_25W822pqDJwZIgYSQM4P3_xaNHnjAj_lc55GIS6jyJTLKlI4PqJhQAxKO2ETosuKOJwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع نزدیک به ترامپ نوشت که رییس‌جمهوری آمریکا در روزهای اخیر به‌طور فزاینده‌ای کلافه شده و احتمال انجام یک عملیات نظامی نهایی و گسترده را مطرح کرده است؛ عملیاتی که پس از آن بتواند اعلام پیروزی کرده و به جنگ پایان دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75628" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuNsq8O9g73Q-CGS0G3LZl6l0hAkcwI1_f4JGm5WNmblMh3bjOaJGI4YOmwtNdw3jdm6d4yHDKT9mjQiMN8qOJP8AaMvl9Zn-QL6GhiO9CGbzuVVDvALLjYiVsGOMyzJXAonkscHTBVvnDi0wZv2t0voyq-y-d64rmhNpUOsFeR0eIy59ZrW6oNCOZA2X-FKP4a4foEaV4i5NKYzzqytPK3nxB6RqKjsM_5-nA_3iH_muQwZqNTsGG7xqPaxiXSyADWCAgU9q1uokHeUEATvikp-xjFCkdEtSAZYdjQiUFLVB3cdVcV74YBW3sDYLs4B6NcthGcXZoeEeaf0FfOkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت مذاکره‌کننده ایران با آمریکا روز جمعه گفت که موضوع پرونده هسته‌ای ایران در این مرحله مورد مذاکره نیست و از اختلاف نظر عمیق با آمریکا خبر داد.
اسماعیل بقائی گفت: «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
او گزارش‌ها درباره قریب‌الوقوع بودن توافق با آمریکا را رد کرد و اعلام کرد: «نمی‌توانیم بگوییم ضرورتاً به جایی رسیده‌ایم که توافق نزدیک است.»
بقائی بار دیگر موضع جمهوری اسلامی درباره برنامه هسته‌ای و اورانیوم غنی‌شده را تکرار کرد و گفت مواضع ایران قبلاً اعلام شده است.
@
VahidHeadline
سخنگوی وزارت خارجه ایران حضور هیئتی از قطر را در تهران تایید کرد
اسماعیل بقایی،‌ سخنگوی وزارت خارجه ایران تایید کرد که یک هیئت از قطر روز جمعه در تهران بودند و با عباس عراقچی وزیر خارجه ایران گفت‌وگو کردند.
او بدون ارائه جزئیات گفت که کشورهای مختلفی طی روزهای اخیر با وزیر خارجه گفتوگو کردند اما تاکید کرد که میانجی اصلی میان ایران و آمریکا همان کشور پاکستان است.
پیشتر رویترز به نقل از یک منبع آگاه گزارش داد که هیئتی از قطر در هماهنگی با آمریکا وارد تهران شده است.
قطر و امارات و عربستان سعودی سه کشوری بودند که آقای ترامپ روز دوشنبه گفت که به درخواست آنها فعلا حمله مجدد به ایران را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75627" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEOTVpjjIBiIS029a89Emzm2SqDWolDBzIGXxsvTcXMnvapoaVpoDAdM7-agJQrYD8ppNafJ9AaLNHXhMjthx_ySz796LkxhQ5OGNMt6mvk7W6TweR22b_GxBCTgb2hPHzS_2bZKYa_oAHEZpetq7RVRsBvhzna0aJK4f9PD8zetP761Fn9r-fp2nBAdM-zDBgYQUKiAoINH9dcz5jpnkFLRPCMYBpx-WE0Xh9lZSYbtgoFEaNx6auQvl0DzhfG-OeS5avut_jzP2KchvfnPjCRrJKHEGyhtDEh4pMsHViHIwafxHllQgoxoUIZ514fUQfqj2LvpN6UR-7L9-UfH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از عاصم منیر، فرمانده ارتش پاکستان که امروز جمعه یکم خرداد۱۴۰۵ وارد تهران شد و مورد استقبال اسکندر مومنی وزیر کشور قرار گرفت. خبرگزاری آسوشیتدپرس پاکستان نیز به نقل از منابع امنیتی اعلام کرده‌اند که عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75626" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1vVxbRbRh--TMhGblvYd-b61LXKW0528wwJ3xkjUzRmHKTZKQrJ7MWu9nmEiPE-PwtkkA5n2z8hSJ_leW-GD3vflzsOCFvxXXWfK6yUD2taGWURVQOn7HQ9KMeqQnOLzy1xgwXqKv9gH8kbPBbs_MvN6hXoHkLCKBdezpFgCPzKKEA6Y6IHQmKPmlsgLmZGf5nFcNE5JFiz0Dj8dPCzPIMGI_wg7sHwSBOTy3VHwjhVj8g2b3JJW498CXHiNws0iwxMo9FDdmqs-S3Akc4sMQxqHEzDQfMAoLub48E9ueExF2sYVAK2Dk55DdSP2ADvzVfn9PKiF9Zi4jmp42qyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فاکس نیوز»: تولسی گابارد از پست خود به عنوان مدیر اطلاعات ملی آمریکا استعفا کرد.
AlArabiya_Fa
پست ترامپ، ترجمه ماشین:
متأسفانه تولسی گبرد، پس از آنکه عملکردی بسیار خوب داشت، روز ۳۰ ژوئن دولت را ترک خواهد کرد. همسر فوق‌العاده او، آبراهام، به‌تازگی به نوعی نادر از سرطان استخوان مبتلا شده و او، به‌درستی، می‌خواهد در کنار همسرش باشد و در حالی که این نبرد دشوار را با هم پشت سر می‌گذارند، به بازگشت او به سلامتی کمک کند. تردیدی ندارم که او به‌زودی بهتر از همیشه خواهد شد.
تولسی کار فوق‌العاده‌ای انجام داده و دلمان برای او تنگ خواهد شد. معاون اصلی و بسیار محترم او در دفتر مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی خدمت خواهد کرد.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
از سوی دیگر رویترز به نقل از یک منبع آگاه از موضوع، نوشته که او ادعا کرده کاخ سفید خانم گابارد را برای کناره‌گیری «تحت فشار» قرار داده بود.
پیشتر اختلاف دیدگاه‌هایی بین رئیس‌جمهور ایالات متحده و مدیر امنیت ملی‌اش، بخصوص در قبال ایران بروز کرده بود. دونالد ترامپ در فروردین‌ماه هم اشاره کرده بود که از نظر او، تولسی گابارد در قبال برچیده‌شدن بلندپروازی‌های هسته‌ای ایران، «موضع نرم‌تری» دارد.
خانم گابارد بیش از یک سال پیش، پنجم فروردین‌ماه ۱۴۰۴ به کنگره گفته بود که ایران در حال ساخت سلاح هسته‌ای نیست.
مدیر اطلاعات ملی آمریکا که برای ارائۀ گزارش سالانۀ نهادهای اطلاعاتی ایالات متحده به همراه رئیس سی‌آی‌ای و مدیر اف‌بی‌آی در جلسه استماع سنا حاضر شده بود، تأکید کرد که بر اساس ارزیابی نهادهای اطلاعاتی، علی خامنه‌ای رهبر وقت جمهوری اسلامی، درباره تعلیق برنامهٔ تسلیحات هسته‌ای ایران، که در سال ۱۳۸۲ فرمان آن‌را صادر کرده بود، تجدیدنظر نکرده است.
با این حال خانم گابارد بعد از مدتی، موضع‌گیری خود در این زمینه را تغییر داد.
تولسی گابارد که مسیر سیاسی پرفراز و نشیبی داشته، پیش از پیوستن به حزب جمهوری‌خواه و ورود به دولت دوم دونالد ترامپ، عضو حزب دموکرات و نمایندۀ هاوایی در مجلس نمایندگان بود.
او هفت سال پیش، زمانی که خود را برای رقابت به‌عنوان نامزد حزب دموکرات در انتخابات رباست جمهوری آماده می‌کرد، گفت که در صورت پیروزی در این انتخابات، ایالات متحده را به توافق هسته‌ای با ایران باز خواهد گرداند.
خانم گابارد در آن زمان در گفت‌وگو با شبکه تلویزیونی فاکس‌نیوز هشدار داده بود که ایالات متحده در آستانه جنگ با ایران قرار دارد.
تولسی گابارد نخستین و تنها مقام ارشد امنیتی یا نظامی دولت دونالد ترامپ نیست که کناره‌گیری کرده یا وادار به کناره‌گیری شده است.
در آخرین روزهای سال ۱۴۰۴، جوزف کنت مدیر وقت مرکز ضد تروریسم آژانس امنیت ملی آمریکا، که مستقیماً از سوی دونالد ترامپ منصوب شده بود و زیر نظر تولسی گابارد انجام وظیفه می‌کرد، در مخالفت آشکار با جنگ ایران، کناره‌گیری کرد.
@
VahidHeadline
خبر یک ماه و نیم پیش:
ترامپ قصد داشت گابارد را اخراج کند
به گزارش وب‌سایت آکسیوس، دونالد ترامپ تا آستانه اخراج تولسی گابارد، مدیر اطلاعات ملی آمریکا، پیش رفته بود، اما مداخله لحظه آخری راجر استون، مشاور قدیمی و نزدیک او، مانع از این اتفاق شد.
دلیل خشم ترامپ به شهادت اخیر گابارد در کنگره بازمی‌گردد؛ جایی که او برخلاف انتظار، از جنگ با ایران حمایت تمام‌عیار نکرد.
طبق گفته منابع آگاه، ترامپ از اینکه گابارد در اظهاراتش اعلام کرده بود برنامه هسته‌ای ایران پیش از آغاز جنگ «منهدم» شده بود (موضعی که توجیهات ترامپ برای حمله را تضعیف می‌کرد)، به شدت ناراضی بود.
همچنین استعفای اعتراضی جو کنت، دستیار گابارد که جنگ را غیرضروری خوانده بود، بر آتش خشم ترامپ افزود.
در حالی که ترامپ در حال نظرسنجی از مشاورانش برای جایگزینی گابارد بود و وفاداری او را زیر سؤال می‌برد، راجر استون در تماسی تلفنی از او دفاع کرد. یک منبع نزدیک به آکسیوس گفت: «راجر معامله را جوش داد و تولسی را نجات داد.»
استون نیز بعدا در شبکه اجتماعی ایکس تایید کرد: «خوشبختانه به موقع اقدام کردم.» با این میانجی‌گری، گبرد فعلا در سمت خود ابقا شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75625" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HSkGNru4veCP6MhT5DXXKBWF8_goxnDVZTgEqXem2a33M4eoGn3wr2zpzhgdmcBqboPsOYrInSfnXncIs0_iQeEuVkcMpSaG_Uh_AP9EG6R7oLZlfZHh61Pd3BW4gec1sP45QXuPvn8ZllItcqrf4JScp2kRe5vcU5p4BrKDTI_bN49cSU-qVSxdSqvXmxTvPdDHIYRTr37NIU42lglZeTeSz6OnI_QwA-Yol4yyEMBe18nPxLdfGXh1B89mnWGsxf6iP0qGZDsdFHS0MXqBcwEEhVGgNxikOy1ZrjmTplicbsxUheDY6KzWuZTMadO3-zWBfAfn43-svirW2wx8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست
ترامپ درباره شرکت نکردن در مراسم ازدواج پسرش
ترجمه ماشین:
با اینکه بسیار دوست داشتم کنار پسرم، دان جونیور، و جدیدترین عضو خانواده ترامپ، همسر آینده‌اش بتینا باشم، شرایط مربوط به دولت و عشق من به ایالات متحده آمریکا اجازه چنین کاری را به من نمی‌دهد.
احساس می‌کنم مهم است که در این دوره مهم زمانی، در واشینگتن دی‌سی و در کاخ سفید بمانم.
به دان و بتینا تبریک می‌گویم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز:
ترامپ با اشاره به مشغله‌های شدید خود گفت: «به پسرم گفتم الآن زمان‌بندی خوبی برای من نیست؛ موضوعی به نام ایران و مسائل دیگر را در دست دارم. این از آن مواردی است که اگر در عروسی شرکت کنم، توسط رسانه‌های اخبار جعلی سلاخی می‌شوم و اگر شرکت نکنم هم باز من را می‌کشند!»
@
VahidOOnLine
رسانه‌های امریکایی نوشته‌اند که دونالد ترامپ جونیور، ۴۸ ساله، قرار است در پایان هفته جاری با بتینا اندرسون، مدل و چهره اجتماعی ۳۹ ساله در یک جزیره خصوصی در باهاما ازدواج کند.
بر اساس گزارش‌ها، این زوج در ابتدا به برگزاری مراسم عروسی در کاخ سفید فکر کرده بودند، اما بعداً تصمیم گرفتند مراسم کوچک‌تری برگزار کنند. دلیل این تغییر، نگرانی از واکنش عمومی به برگزاری یک مراسم پرزرق‌وبرق در زمانی خوانده شده که امریکا با تنش‌های مربوط به ایران روبه‌رو است.
afintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/75624" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx_FC8EMWUndQov1dLCMUHBxB0D6HEnWn3PeriW66v5q_FDCtsuXpVAOPL1669SKu86XabxsTg386QoCOm5v9RxFzcYqDupZIAI_QN1lbO-TIZbJ2lyogfnY-k5hvlK13iIEBC4q465kG-ucqXnXHy4P7hA8-pywMXpLF-GPCmEA3v6S0tNIM0A0IgwSxirmrOiEcS16W--Hi23FCf0KP3nuPLBud1VbBXPk_q6SCzigAELzsp8zrgb1pvcRpoq95_srIGM0x7r0H-VL41WJslGOxBhCq2pzqv20or1m1QYgZNoZO25QCsDI03209Ii6newM-WPIZgVTpHbtwznxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4XyqZvyYBmQWnKHwWTq8-FczhlVSqSzj1KH5Y7ZiYkFCaa4NiHV5y4BCbPkxeykX7pWI0O3AJpDVq_GMTFonK6KE-121KBIoaz74w0xoGndrYhxmc5rgAzaDkONXiukbUPHtYTjRdH0zzVvOLAtoYyRm2UydgS5GBc-M0Itzn9RszF_5FYVdOn-nmgqc6ygf1RhkWfZUjGIysjawQcGBFJALn_TE_tkFddPnE5laPmuALgLFZH1Bn9KEpQjvkVuIoToBGtnTXI-RWOalcU-gQfn-bxkEBnbgMk7JX4OCtKk-dNv0KoGZdO6Weu-PATWh8yLG4ones8JJCKtY6rk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pb_D_JowomUSK88n39ZDlIuUkFZVwPCN342Z-xxXAnq5Yl611riUVOGLq7oI-XvOzlECmspJ_GVQIXCsFdZVMCHR6i9sG4O084ymQrONQLqBEOstHCpfW0ohM9Y5KWmcIzNU8-U3SjLgqUXFU8SyqYsBO9Zcf05MQaYMhEA7yGe0KitdPuuu95GtmKP96Hm5lyVXoUM--rldAaC6fJRwCMrisAIfpV1ULQzhtSYqcF75QXblI_n3skAa6rr1-xIbmYRCfabYNETys7uqZ8Sjv_WBUZycJYlrK01PlgkrXhzxPHUROHBLxrBaMBzqLT1u8KUjr4TSWS7RWAzNiu8sVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند تا کنون ۶۵۵ مورد اعدام را در سال ۲۰۲۶  ثبت کرده است، که ۳۴ مورد که از آغاز ماه می تاکنون اجرا شده است.. آمار واقعی احتمالاً بسیار بیشتر از این رقم است. جمهوری اسلامی در حالی این اعدام‌ها را پشت درهای بسته اجرا می‌کند که  ۸۳ روزه است که اینترنت کشور قطع شده است. حاکمیت با قطع ارتباط جامعه از ۹ اسفند ۱۴۰۴  صدای زندانیان، خانواده‌ها و شاهدان عینی را به شدت سرکوب کرده و نظارت مستقل بر وضعیت حقوق بشر را به‌طور خاص دشوار ساخته است.
🔸
از آنجا که دستگاه قضایی همواره تنها بخش کوچکی از احکام مرگ خود را به‌طور رسمی اعلام می‌کند، قطع اینترنت داده‌های فعلی را به شدت محدود به منابع دولتی ایران کرده است. بنابراین کاهش در آمارهای ثبت‌شده، تنها نشان‌دهنده خفقان اطلاعاتی است، نه کاهش کشتار.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75621" target="_blank">📅 18:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIcNtFkrGSAobzG9edK8vnm-SlTgYlGfAcP2I-VqHhxSwyUibxtJLe958ErqWiPkAXYzvwqfw4gZOzM1arFKJQn_mvMVEz9Om-UZSQyjKdeq40cugxeL8h9cqh5d1IlMn-_Nro5ZJHn-NG4tIchTGWfLU_8mCxaJXWnY3yLs3M63AX_7MuOg4_qRu_K_nVt7OUV99GAIE7b4SmWdbUBnD-JDqP7vfKdSEJWzRj2ZPdlPusqg5yL30YSxTGRp0-Z6Tjn5pM0ntFNNav9cpj-jkiprD477aO4gmEeXEwJNzZKbcQdGJlW33IDF-NK2-jgAoUebnnUOW4HARrklFitP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر حسین ناصری:
MNaseri23595
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75620" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD8K8Gx0PX0ykpvG5eB3hvbtJasQ4bm52d7M2MwC-OeSb8R3cgrKgi7mbu-W8fHT4DxJrAZ2D8n1ImuVwkfzcMEO9kMqCcQ08hHCHZgUflOnLIRaCqA76-q2kr3w3yUd2q9KWIYmq72EgBQN03CJoMxKAvuNxEUsbQpO7YxIfcZ8NjSLKiOzuEKZiG4pe2Qp4mkjgesZOXumNdd9BPs_Ly4PtQClWOaZSJyiVQ_PHOkmBEyB4DK7AX7gb8We-DZuVB_uBbGfIj299wTbJzcXYzZbH6k6Vy6l8Ccloft_xalOX5DFwD-UTYLx67dhoyZAa-QBneFyGKvZlvzt4r2aKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های دولتی پاکستان، فیلد مارشال عاصم منیر،‌ فرمانده ارتش این کشور راهی تهران شده است.
خبرگزاری اسوشیتد پرس پاکستان به نقل از منابع امنیتی گزارش داده است که فیلد مارشال عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
فرمانده ارتش پاکستان چهل روز پیش هم در تهران بود و با محمدباقر قالیباف و اعضای تیم مذاکره‌ ایران و آمریکا دیدار و گفت‌وگو کرده بود.
این در حالی است که وزیر کشور پاکستان هم برای دومین بار طی هفته اخیر به تهران رفته و در حال گفت‌وگو با مقامات ایرانی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75619" target="_blank">📅 17:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fqT54uHqve4xiPDthH3Mf6GkAxFPhSqqx23FkEZHzo3qR8UieeQewopuBi9Xx6_Z0d9J2loNxDyg26-C9Z_6jsYzPw-3LpT2Fe5LeX9oF9SikvIMBTrBON_zPVqfEGKY9Fba3fYHrRyILd0wlBQxrTYyW8s_abArfLuhGSmD0SisWy5423H1-FMqQ-e5tTpf-CdX6fXclAiMEA-SDVU4hYwSaYd_e4rlljGqwf-kG05znrzEgUW7z-70eqvyiDzS8SBfsbr2PD7l5eIMuQGrtDMjjf_Z9bottIFV7AczhtzrrEOndN5JZxantqF0ODFhGw6am7bke2t8j5uqQTGLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvVi5eDJY7CoD5NWbxO-WthiJjL14FeFjSr0xrw8_3GW-NdJNg0wZk6-SfplsnbTY6ipoueOvSenLeoevo2hP5YYdJSyZQSUJVpH-TN9tx_z8uoq4kspMkgA68ieO7O63PPSK6TSf1A7HLUaK8gGsMU2p98uLu5YSLcgHyvyJ-Qj38llD_x0SM6EQUqTd4YxKTtJTtBF3l7U4o_kQ_DMyD28mCO2pynQP0APSB705tRAidmQjIRYHRkjnOcVY_U8Y_ggPTTzdsSlM_RUmwYpBRYZYafF-xS6LyRi7U6HjRjrnqRQJWLg57uUrL0OJs9sI8yKTmnXon7UviBH2WnUaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=UZT-E9rfdolDsVnef0Jydxd5UuDhSpxW1eUPX7fm65l67hD9ZWLnZQnn7TDB-uZPkGzMLregb-VGLV5PwW3pWgEEJ8wR1kV_WfWSYrqlum1njMOgUYklqAWlmMXipmugIrJ1YWy4mQxvrgICm47p7iym-ootRZ26rMrFQZkILCw8RGV5Mg9o8WZprQDkMWFQUPgLqk4eXUYdzJLSNwHCUnGUC24k1uIXzXX3LMYh5W06g7tmhBGbbidbivxv3WjexPCrtKQp4aNC3E60xkUwjmKdTVwPmvtHbKYXtK8JPjPHMWFc7ANd3NUXURYj5TEAE22ItfH01j0lkYvRvTN1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=UZT-E9rfdolDsVnef0Jydxd5UuDhSpxW1eUPX7fm65l67hD9ZWLnZQnn7TDB-uZPkGzMLregb-VGLV5PwW3pWgEEJ8wR1kV_WfWSYrqlum1njMOgUYklqAWlmMXipmugIrJ1YWy4mQxvrgICm47p7iym-ootRZ26rMrFQZkILCw8RGV5Mg9o8WZprQDkMWFQUPgLqk4eXUYdzJLSNwHCUnGUC24k1uIXzXX3LMYh5W06g7tmhBGbbidbivxv3WjexPCrtKQp4aNC3E60xkUwjmKdTVwPmvtHbKYXtK8JPjPHMWFc7ANd3NUXURYj5TEAE22ItfH01j0lkYvRvTN1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در حاشیه نشست ناتو درباره مذاکرات جاری با جمهوری اسلامی گفت که واشینگتن در انتظار نتایج گفت‌وگوهای در حال انجام است؛ گفت‌وگوهایی که به گفته او نشانه‌هایی از پیشرفت داشته‌اند.
او افزود: «ما در انتظار نتایج این گفت‌وگوها هستیم که نشانه‌هایی از پیشرفت دارد. نمی‌خواهم در این باره اغراق کنم؛ تحرک محدودی صورت گرفته و این مثبت است، اما اصول اساسی تغییری نکرده است.»
وزیر خارجه آمریکا تاکید کرد که حکومت ایران هرگز نباید به سلاح هسته‌ای دست یابد و گفت: «برای تحقق این هدف، باید به مسئله غنی‌سازی و نیز موضوع اورانیوم با غنای بالا رسیدگی کنیم و افزون بر آن، موضوع تنگه هرمز را نیز مد نظر قرار دهیم.»
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، جمعه یکم خرداد در حاشیه نشست ناتو گفت جمهوری اسلامی در پی ایجاد نظامی اختصاصی برای اخذ عوارض در یک آبراه بین‌المللی است و تلاش می‌کند عمان را نیز به پیوستن به این سازوکار متقاعد کند. روبیو تاکید کرد که این اقدام «غیرقابل قبول» است.
او افزود: «هیچ کشوری در جهان نباید چنین چیزی را بپذیرد. من کشوری را نمی‌شناسم که جز ایران از آن حمایت کند.»
روبیو با اشاره به تحرکات دیپلماتیک در سازمان ملل متحد گفت قطعنامه‌ای با پیشنهاد بحرین در شورای امنیت مطرح شده که آمریکا در آن نقش فعالی داشته و به گفته او، بیشترین تعداد هم‌پیشنهاددهنده را در تاریخ شورای امنیت دارد. او هشدار داد چند کشور در حال بررسی وتوی این قطعنامه هستند و افزود: «این مایه تاسف خواهد بود.»
وزیر خارجه آمریکا تاکید کرد واشینگتن برای دستیابی به اجماع جهانی جهت جلوگیری از اجرای چنین طرحی تلاش می‌کند و گفت: «باید دید آیا سازمان ملل همچنان کارآمد است یا نه. ما می‌کوشیم از این مسیر به نتیجه برسیم.»
او تصریح کرد اگر اخذ عوارض در تنگه هرمز اجرایی شود، ممکن است در دیگر آبراه‌های مهم جهان نیز تکرار شود و افزود: «این قابل قبول نیست و نمی‌تواند رخ دهد.»
روبیو با اشاره به اهمیت تنگه هرمز گفت این آبراه برای کشورهای حاضر در نشست و نیز برای دیگر کشورها، به‌ویژه در منطقه هند-آرام، حیاتی است.
او در پایان با ابراز امیدواری نسبت به نتایج نشست ناتو گفت این دیدار زمینه را برای نشست رهبران در حدود شش هفته آینده فراهم خواهد کرد و افزود که تا آن زمان کارهای زیادی پیش رو است.
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست ناتو در سوئد درباره مذاکرات با تهران گفت: «همه ما دوست داریم توافقی با ایران شکل بگیرد که در آن تنگه‌ها باز باشند و ایران از جاه‌طلبی‌های هسته‌ای خود دست بردارد.»
او افزود: «این چیزی است که همه ما امیدواریم و همچنان برایش تلاش خواهیم کرد و همین حالا هم که با شما صحبت می‌کنم، کار و مذاکرات در این زمینه ادامه دارد.»
وزیر خارجه آمریکا با اشاره به این که باید یک «برنامه جایگزین» هم وجود داشته باشد، گفت که برنامه جایگزین در صورتی باید عملی شود که حکومت ایران از باز کردن تنگه‌ هرمز خودداری کند.
او گفت: «پس باید از الان درباره‌اش فکر کنیم. من امروز این موضوع را مطرح کردم. واکنش‌های تاییدآمیز زیادی دیدم. اما هنوز چیزی برای اعلام رسمی درباره اقدام مشخصی که در حال انجام باشد نداریم.»
وزیر خارجه آمریکا درباره برنامه جایگزین در صورت امتناع جمهوری اسلامی از بازگشایی تنگه هرمز افزود: «نمی‌دانم لزوما این می‌تواند ماموریت ناتو باشد یا نه، اما قطعا کشور‌های عضو ناتو می‌توانند در آن مشارکت کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75614" target="_blank">📅 17:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jy-Pd0i9zWe8y4R0FUnDGgv5gWv5Hovr0Xy3ioyUHS19aOFkaIKh19cyrAaaOYsdNdelVJMuX5OO7OjcyEKhBxDXKoIrf1ZZ3e9Sa2glZVywiLDp7ufYPhna62_9OM2ISJrVR0Oe1XCMhDVo2b-8Rtq4125fUfog7_hTKLkEPBLnbqm36TPCWy9WwUQ2FIh3vofgoLC_K89LRI9tEgkUgDlv2toMP4t4VcI4yeE6OHmnLDoQkcmdq_uhfoAr1E3TRLhDG73Y0HM7Y5ILx8jscyTBfKHXhf2rmsIDpfy9-aQT0LqFQ_roqHkcVfZ80jPLvQLGMD28gBkOeco1Ua2V-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bD62NjPfpuJXTZXZmKpHn9fyJJRtyhM7j8k-alw2klo_2sUsoMoJ_uSTU74TzYTfeEs-st4S0EkuiPE5P7zzqK5o7nn_hZGSP_jqxTMtmdTzNzhrgT6Uo39qyh7y-LiSSPF-gRC75bg3MDvtZMqjxAmpj3MAZWOCyl2zo_gtOFEoRDRccWNM94h0k_2EP1A9RQmTTo0VDvrDi3S_AnfYcarNCK2xMKbLm_OMfxFU_A1qhJx0QOp3q9U2_EnlrqPXe4tnsCh1vZOy3VPQn_fR_HLnNTacEmC0Q_VKNeYJzJN4WmCkEhNiZzEci0ViuMyj4oVSPnVTuL4hqRc5VebSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HidqdjA8h38wHfsIpAs_OeUOsW5_E3mCfJDzQkuzFGTqbY6R9Vax2LObFSvRA2Ig6mB864p3_YGCuNUE-_mnActsmVxGGhVX5LpnFdg0mK5d5uPurWZuKUvTaveNOo3h6JN9vDcW8vrBmIign5ws2WtD2Z4x4VuKi0knB9v281FQSAan3peHgHjKasDL_7dAcYURNti10iXe1VwIKl6yraDBSDz2fJmMSosd9YNB_PIjg8dUSHCp9nRizRi-xyLAsEOW4OTysXRV9bkeEqGibd5xFUSvhGo7ouglVoVeXHtIlehTvkhPoBH7m6-2k2lsxdOmkp_HjvifMpIeOtjvrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاعیه منوتو درباره پایان پخش برنامه‌ها
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75611" target="_blank">📅 17:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uAvpV8FEeU0XOL5HoP8CI0jHT4Wbxu9Ea9cIUQQnghjkSB2CZ8O53rtX61QZf7AuKs18Rsxr1ocb7D7YysixlAL35vfnT3Uq1uiJgDE5xov0LvwCGmqqJT32Kw29Cphp3OZZMj8GK64DdfsU-pTL-g4v7WxHAphZ6PrAFotcoRKzGYvTBdZ_1oL7tQOs3b9xqv2KLIE7J3wzNT95l5dwC3zh4cMqY3HfmRdw1IzzuG1A8YzwCEhPgJW5AhUJ6ItYnoSwzkW6dn7LeU_bBVm29wAXuVjYrHFQxfdivdF78x5iQP6hPsLffpCg-BpEY-Q-3x7kkuhFYBlVlNQ4bt6E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PZ3BdSz7Pz7TUOdtFxUFrG6ppxkzRDUzcZgKEDMypfRSO018MIQp3Z3ACRcV0EIO6bXlEdJupOPXx2RjOYDEc_Vg4yuNlUd55J8vj42x8GlzybAhPehfxtoOVB0_vq63blDJVerQYrRmmzH-J5tiACXFDc06ote-Dw9fuM2CSMTmtyzhm6UWF9n0fGOi4lz7CytCz0ejUeUk3Jtx7NM-rXoUZmg5fSmbc_6MoU-ogDsyYoLhg_ZWRfYyEHEG28SHY0pdy2dz2Rt-qgamYt3EpqhmebdYyKrVjiRh5FZV7GmmJIQXn41gcUXYSobcNg69MxEgvtB9ULnfQ-40_5utog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dULenNyiDU8TixrjCbvYN00FaM9tmKW8K_4Vp20zxizuc9dvjtifIpKu6bfLVLZF5I_rNG6Zxra5wwFEkvAUrZ5Gy2uEFt8DMEfLvIMirGszemt-jLXSbBbc-FQKyZwaRl4wAhDvvW5Gs7RfWwGMJB-yrIS3NpqH_DZ8G7toZS1l7lUDIfoSE4-nvWD95QPAbNKALLkblNwWmEGsL1HcAQffS4KKqFzTYlQdHxTpzAKWEfDBYkap_e9gNCL5BzASteXKDlaYr3mcvVf8yxlpXL3TBnOcXqERIMbP8WWnLcvio3Fp0bW2I0qqd4qovd0K33TQ9-NlbAReuqgvqoUFnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=jGnmQh3G57Zf9m0d-AgzaY04jwJnAI2mFdGZKePAEepANBpluAnp5xQoWDKuyRL_r8D0RIjCLxOcYXP-9tHsHN4YLwJczL7PHdxrSeNuaja1MJKLGrZRUJhvgL_gpT2SVdyWuF-ieCTS6tlJqpX69deCgjtLIsfPMmlX-wQvdXaMjM-QS-hTnbFsijpS4s-nps9kJK-9irwludrdmf29rXNKMncRkR6OAY_ODc4lI5AXBnPeddnHVFHinSOO0GzXhHTUtrO5xpwi-3YBDCrMgWAJD1ykXhHn2u-QO9h60-RPMB6BqLQB5e626w8mDj2gmeOHJQBEcZg_ObTE_whGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=jGnmQh3G57Zf9m0d-AgzaY04jwJnAI2mFdGZKePAEepANBpluAnp5xQoWDKuyRL_r8D0RIjCLxOcYXP-9tHsHN4YLwJczL7PHdxrSeNuaja1MJKLGrZRUJhvgL_gpT2SVdyWuF-ieCTS6tlJqpX69deCgjtLIsfPMmlX-wQvdXaMjM-QS-hTnbFsijpS4s-nps9kJK-9irwludrdmf29rXNKMncRkR6OAY_ODc4lI5AXBnPeddnHVFHinSOO0GzXhHTUtrO5xpwi-3YBDCrMgWAJD1ykXhHn2u-QO9h60-RPMB6BqLQB5e626w8mDj2gmeOHJQBEcZg_ObTE_whGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم مستند «تمرین‌هایی برای یک انقلاب»، ساخته پگاه آهنگرانی جایزه «چشم طلایی» هفتاد و نهمین جشنواره فیلم کن را از آن خود کرد.
«لوئی دور» یا چشم طلایی، مهم‌ترین جایزه بخش مستند جشنواره فیلم کن است.
پگاه آهنگرانی جایزه‌اش را به مردم ایران تقدیم کرد و گفت: «(مردم ایران) با وجود تمام سرکوب‌هایی که در طول این سال‌ها تحمل کرده‌اند، هرگز از تلاش برای حقوقشان، آزادی‌شان و آرزوهایشان دست نکشیده‌‌اند و مطمئنم که آنها هرگز تسلیم نخواهند شد. مطمئنم و یک آرزو دارم که می‌خواهم اینجا بگویم: این‌که روزی دختر کوچکم لی‌لی و همه بچه‌های ایران در آینده‌ای نزدیک در ایرانی آزاد و دموکراتیک زندگی کنند.»
به گفته خانم آهنگرانی او با استفاده از آرشیوهای شخصی، ویدئوهای خانگی، تصاویر اعتراضات خیابانی، روزنامه‌ها و صداهای ضبط‌ شده، بیش از ۴۰ سال از تاریخ ایران را بازخوانی ‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75607" target="_blank">📅 17:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhf3xXKp0B_LpSrWFVMxZMFVA_ExpPOSKS396snHZCXj0UaJZxHXIi5OSZkz0MBwCJybEIJy9Zuomc9sx_7WedNImVbFDW8nlMuvSPTO-UbK_tqUKxxMdvcP1syEoOBXq_GCdAWjo9vvKMzWhwJv38CiVYkwILelQWLL32Ss4tyg32hIUnJz3-6tnkI3Ydn-egDCgRaWhP6ED5hEnPgA0QlzoWtt4AtLDG1AaU0y9gLn7pKn9bDq2fuxIR28z64ZNBVGHZUFxIzz1sYk9nPOh-eVTToSL8zEQqnpHdaVcOXP47Ga-eoImMuYWVqi6CbQtTdIUDLKyb4c0j371I87oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عرب حوزه خلیج فارس از جامعه جهانی خواستند که طرح جمهوری اسلامی برای مدیریت تنگه هرمز را رد کنند.
به گزارش بلومبرگ، در میانه مذاکرات دیپلماتیک سازمان بین‌المللی دریانوردی با ایران و عمان پیرامون بازگرداندن آزادی تردد و امنیت کامل کشتیرانی در این آبراه راهبردی، کشورهای عرب حوزه خلیج فارس طی نامه‌های به اعضای این نهاد زیرمجموعه سازمان ملل، نسبت به طرح جمهوری اسلامی موسوم به «نهاد مدیریت آبراه خلیج فارس» هشدار دادند.
پنج کشور عربستان، امارات، بحرین، کویت و قطر در نامه خود گفته‌اند که به رسمیت شناختن مسیر پیشنهادی جمهوری اسلامی می‌تواند یک «سابقه خطرناک» ایجاد کند.
سفیر ایران در فرانسه روز گذشته تأیید کرد که تهران با عمان درباره اعمال دائمی عوارض عبور در حال مذاکره است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75606" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoZuIW5vSNpxf60g1qpFl6QJeKLLl4X0IQj21gpPVRZd-JQ945wnXB8_r7ozrhK0ejvsOZxHGkAxKTQDjfsRsJrNJisc6Hk5oIiUYDIw8Gs4a15U8-tog50SQpbIEup_kRRgF4zGD3t_A-KRHhfA5aEs5_WcTEyo2wyUidq0N9D1SBUeTE2lGY4FyfoFgBAvRPb8A179EU-9G5RP-OlVaGf2ZbKthRcFXUcg0I2mjFGpG681nuELLCa1iiop8rEU5Wlu4Pv4-_zCNJX1PAEEexH5miycbupssO7Yhihn5_LVS4dbSgqgdtLK9NAtHCaPf2u8V-rSRP042th70dtqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد بین‌المللی ناظر بر وضعیت اینترنت، نت‌بلاکس، صبح جمعه اول خرداد اعلام کرد قطع گسترده اینترنت در ایران وارد هشتاد‌وچهارمین روز خود شده و بیش از هزار و ۹۹۲ ساعت است که دسترسی کاربران در ایران به شبکه‌های بین‌المللی همچنان قطع است.
این نهاد ناظر بر اینترنت نوشت با ادامه این وضعیت، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شود و هر ساعت از قطع اینترنت، ارتباط با جهان خارج را بیش از پیش به جایگاه، همراهی با حکومت و برخورداری از امتیاز وابسته می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/75605" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwLjEmZcMQt3EPBw1RI7q91L61VXbHT2rAz3hwhSzBoqDcDuRuOE6IimcF9fCNT1Zp0teIQO8zHEWAR5V6QOF-EpRcpX5a2ca1JtmGFVHh4vxy_lzZBLnObvPD6-D9KPXh0YB-zL7xrWM6Xe3oh2XctBc6HGF0_GCka_pJo_CvthCJHXirLZe0Yz0elybcvd7ol8ofo181c2qHGADWgYWT4iII3qlIfSkQoMtUptl6vUwgANKaqWqM2aI_SA475mrOzTq_xq-sqwuI7_O6Im3LpBzOU4CWsawQrOen8F_OSV4ouqDsZuMcgeXCbpnz9paPaOajZ4tSa2ZmOgI7twYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور احکام اعدام محمدرضا مجیدی‌اصل و همسرش بیتا همتی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، را نقض کرد.
هرانا خبر داد که پرونده این دو متهم برای رسیدگی مجدد به شعبه هم‌عرض ارجاع شده است.
این دو پیش‌تر به همراه بهروز زمانی‌نژاد و کوروش زمانی‌نژاد با حکم صادرشده از سوی قاضی ایمان افشاری، رئیس شعبه ۲۶ دادگاه انقلاب تهران، از بابت اتهام «اقدام عملیاتی برای دولت متخاصم ایالات متحده و گروه‌های متخاصم» به اعدام محکوم شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75604" target="_blank">📅 17:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=bZ0sSIukdGbyX8bOEJYZdmHEQSFxvZVuZX5E49wcOp4XPGTbk-9L1WTP9JvtZhhfirwO6WwSV3XHJj66e2ZbQ0_RrInySOUEXUwsiiDLdaA7UQFMLksSDdrXgzI03mCU_TxSn0wxTWruDcZptbJFgOv8hc-GeRUrJ2Ods0iIEThkayqb8uut0-R2SD5n-QE3MEkHyPf5WVBFKIewsxtKWjfQMlqxVdNuNjP_KQFIJbRB0sUVUexiY52JmMvaRehyn8-WO_pS_vfWiBtrqvrm7T4CllWoNWJ28wf9TEblUmteeVtbJk4vZojXzBiHf5qzSYOew8cBcmRRITwle_EEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=bZ0sSIukdGbyX8bOEJYZdmHEQSFxvZVuZX5E49wcOp4XPGTbk-9L1WTP9JvtZhhfirwO6WwSV3XHJj66e2ZbQ0_RrInySOUEXUwsiiDLdaA7UQFMLksSDdrXgzI03mCU_TxSn0wxTWruDcZptbJFgOv8hc-GeRUrJ2Ods0iIEThkayqb8uut0-R2SD5n-QE3MEkHyPf5WVBFKIewsxtKWjfQMlqxVdNuNjP_KQFIJbRB0sUVUexiY52JmMvaRehyn8-WO_pS_vfWiBtrqvrm7T4CllWoNWJ28wf9TEblUmteeVtbJk4vZojXzBiHf5qzSYOew8cBcmRRITwle_EEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویرسازی از مجتبی خامنه‌ای
وزارت جنگ آمریکا روز پنجشنبه ۳۱ اردیبهشت، با انتشار
ویدیویی
بر ضرورت افزایش بودجه دفاعی کشور تاکید کرد.
در این ویدیو که ترکیبی از صحنه‌های واقعی، گفته‌های پیت هگست، وزیر جنگ آمریکا و تصاویر کارتونی است، تصویری از مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی نیز در کنار یک سامانه موشکی دیده می‌آشود در حالی که یک پایش قطع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75603" target="_blank">📅 02:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSDAYnb-QaRZHOsaFe0CrnVhruQ_RhiVzjbBsX70LRDFn-hyDS52gnSPbqbCL_j5GdSLrEtrCn3Ba79pfQinxO_57ZLTKPFBw8YEElByAmWfOiWDNFtZGBCx4U-4kVVd77KARN6vAk9eiBfYCqRy39L9s9Ks2g-5v6MCGUbWFG26cRAJsevxn1AIywqtLu1-fsVdtgEtfUsZYJ6RlVJm2SnB3zwuE-UYW4lY-SieCoh6nLU_srLsjO_SDdZPBKBr2TUMIcbqC5Nkd4TTOn_hYwyRphqI_R_Hsd0bfUihfdMUDMu467NJCNFeFkak2B639pU-pnAcKeA32swkpH5eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
در تازه‌ترین تحولات بحران ایران و مذاکرات جاری، یک منبع بلندپایه به «العربیه» گفت که فرمانده ارتش پاکستان امشب راهی تهران نخواهد شد؛ این در حالی است که پیش‌تر گزارش‌هایی درباره احتمال سفر او در چارچوب میانجی‌گری‌های منطقه‌ای منتشر شده بود.
قرار بود عاصم منیر، رئیس ستاد ارتش پاکستان، امروز پنج‌شنبه در سفری رسمی وارد تهران شود؛ هم‌زمان با انتظارها برای تحویل پاسخ ایران به تازه‌ترین پیشنهاد آمریکا برای توقف جنگ و دستیابی به توافق میان ایران و ایالات متحده.
alarabiya
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/75602" target="_blank">📅 23:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=DUb_mXKJ1h0h2WGrormfbKMPvlXD3H4XjvDi_IJgq0S3DRLRuJW1GLRuH5E1tavWy3I5r2UARGclVa1RfZRO_hBvAaFJSCSpglVizNCcRl7VnB5OaFtgels2o1Z5dADAxet8UbgoIgIhHM9EKUNRssiFlGlwlXMr3WvKcrpbUFSP0SGm7O2X5Ky5hAq1Wk4cA1b6zpVhdr74Xxh2mlcoYegecCNxPUuXsWh1wlEpndV46fC4Dv1Aoz5ZreEH7cio9areRvKBO0jqAYANtDN5Sl4Z6KlHKQxfkMvW9LiDLHgEE4ZoF8CRgGMEaP74I8b2GNISoQY83HYzilCtp0U--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=DUb_mXKJ1h0h2WGrormfbKMPvlXD3H4XjvDi_IJgq0S3DRLRuJW1GLRuH5E1tavWy3I5r2UARGclVa1RfZRO_hBvAaFJSCSpglVizNCcRl7VnB5OaFtgels2o1Z5dADAxet8UbgoIgIhHM9EKUNRssiFlGlwlXMr3WvKcrpbUFSP0SGm7O2X5Ky5hAq1Wk4cA1b6zpVhdr74Xxh2mlcoYegecCNxPUuXsWh1wlEpndV46fC4Dv1Aoz5ZreEH7cio9areRvKBO0jqAYANtDN5Sl4Z6KlHKQxfkMvW9LiDLHgEE4ZoF8CRgGMEaP74I8b2GNISoQY83HYzilCtp0U--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفتگو با خبرنگاران در کاخ سفید تاکید کرد که هیچ کشتی‌ای بدون تایید ایالات متحده اجازه ورود به ایران یا خروج از آن را ندارد و نیروی دریایی آمریکا در این زمینه عملکرد فوق‌العاده‌ای داشته است.
ترامپ با اشاره به خسارت‌های سنگین مالی جمهوری اسلامی در پی این اقدامات گفت: «بر اساس پیش‌بینی‌ها، آن‌ها روزانه ۵۰۰ میلیون دلار ضرر می‌کنند؛ رقم بسیار زیادی است و چه ۲۰۰، ۳۰۰ یا ۵۰۰ میلیون دلار باشد، آن‌ها در حال از دست دادن پول گزافی هستند.»
رئیس‌جمهوری آمریکا با تاکید بر لزوم آزادی کشتیرانی افزود: «خواسته ما این است که این آبراه بین‌المللی، باز و آزاد باشد. تنگه هرمز یک مسیر دریایی بین‌المللی است، هیچ‌کس نباید در آن عوارض وضع کند و ما اجازه چنین کاری را نخواهیم داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75601" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/011b067e31.mp4?token=dX8qICj33TGgV8uPpAYd2g9dlT9BNSXNsTubibYEXQfvYHbfU10hExeaQxL6r62DGP4UooU2CaeIust7WfDC-NxAAR0yXdQlfKUicmarV1qp-d1-5oqW-nJ6z6VW40q-c-xrrhQBofTfHcAJZdLjIRUK2MPfZN1mIWrrzNtrLJKW8RSYS_JKvfHigdzsLozu3MUh-vZECiGZfAlSrvI79Qi_0FtybLQ0IGim0mgLZ_UYnaoLo9BnZY60BXcikojopeDAERO8loQn0B-KKJaHYwy9g7vOUJGNUaqgUePNfR5xnj4eDfrV5UKuewWRAvrO8pK60B_C8BtAzA6Tjxd5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/011b067e31.mp4?token=dX8qICj33TGgV8uPpAYd2g9dlT9BNSXNsTubibYEXQfvYHbfU10hExeaQxL6r62DGP4UooU2CaeIust7WfDC-NxAAR0yXdQlfKUicmarV1qp-d1-5oqW-nJ6z6VW40q-c-xrrhQBofTfHcAJZdLjIRUK2MPfZN1mIWrrzNtrLJKW8RSYS_JKvfHigdzsLozu3MUh-vZECiGZfAlSrvI79Qi_0FtybLQ0IGim0mgLZ_UYnaoLo9BnZY60BXcikojopeDAERO8loQn0B-KKJaHYwy9g7vOUJGNUaqgUePNfR5xnj4eDfrV5UKuewWRAvrO8pK60B_C8BtAzA6Tjxd5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی هم تلویحا وجود یا عاملیت داشتن مجتبی خامنه‌ای در تصمیم‌گیری‌ها رو زیر سوال برد.
بعد از شعار جماعت در لحظه 01:48 ، یک بچه میگه: مرگ بر دیکتاتور!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75600" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=PUGbrzZGetjj-JE2fl_hWtr-2vIzFjjQOCDf_oqkxQ7OR3KPI0mA_CoT8BrUph6IEl8z46vLxU49VOqlZaROI2qT_QhoBhB3vmdDx1pW4LJssVqOkB5-npwpzOZdLgay73ymUCEfJ89-q6GRmKnmnhMtB0C06bhua23KRbgiI4ZQO2wsd7ai5sW1_ah0E0fHgnQmltp__19QN_W92AhllGzz4WPUnIYeeWXOewt1gw6cE2caiR-GIGa_GYdCwz4E4YuBuQvpZ9H5wnhp8BP82RR35xrKVgjXPW_q_hByyyLh_dPpmqHzea7xrNneJQafKgKXoNGPIp702_rmr7K2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=PUGbrzZGetjj-JE2fl_hWtr-2vIzFjjQOCDf_oqkxQ7OR3KPI0mA_CoT8BrUph6IEl8z46vLxU49VOqlZaROI2qT_QhoBhB3vmdDx1pW4LJssVqOkB5-npwpzOZdLgay73ymUCEfJ89-q6GRmKnmnhMtB0C06bhua23KRbgiI4ZQO2wsd7ai5sW1_ah0E0fHgnQmltp__19QN_W92AhllGzz4WPUnIYeeWXOewt1gw6cE2caiR-GIGa_GYdCwz4E4YuBuQvpZ9H5wnhp8BP82RR35xrKVgjXPW_q_hByyyLh_dPpmqHzea7xrNneJQafKgKXoNGPIp702_rmr7K2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، در کاخ سفید گفت: «جمهوری اسلامی قرار نیست سلاح هسته‌ای داشته باشد. ما نمی‌توانیم اجازه بدهیم.»
او افزود که در صورت دستیابی جمهوری اسلامی به سلاح اتمی، «در خاورمیانه جنگ هسته‌ای به راه خواهد افتاد، و آن جنگ به اینجا خواهد رسید، آن جنگ به اروپا خواهد رفت.»
رییس‌جمهور آمریکا تاکید کرد: «ما نمی‌توانیم اجازه دهیم چنین اتفاقی بیفتد، و چنین اتفاقی هم نخواهد افتاد. قرار نیست اتفاق بیفتد.»
ترامپ درباره محاصره‌ بنادر جنوبی ایران از سوی آمریکا نیز گفت: «کنترل کامل تنگه هرمز را در دست داریم. این محاصره ۱۰۰ درصد موثر بوده است. هیچ‌کس نتوانسته عبور کند. مثل یک دیوار فولادی است.»
او افزود: «هیچ کشتی‌ای نتوانسته بدون تایید ما عبور کند. و نیروی دریایی کار فوق‌العاده‌ای انجام داده است. و هیچ کشتی بدون تایید ما به ایران نمی‌رود یا از ایران خارج نمی‌شود.»
ترامپ درباره اورانیوم غنی‌شده ایران نیز گفت: «ما اورانیوم بسیار غنی‌شده را می‌گیریم. ما به آن نیاز نداریم. احتمالا بعد از اینکه آن را بگیریم نابودش می‌کنیم، اما اجازه نخواهیم داد آن‌ها (مقامات جمهوری اسلامی) آن را داشته باشند.»
دونالد ترامپ، رییس‌جمهور آمریکا پنج‌شنبه در کاخ سفید به خبرنگاران گفت که ایالات متحده خواهان دریافت عوارض در تنگه هرمز نیست.
پیشتر مارکو روبیو، وزیر خارجه آمریکا اعلام کرد که اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75599" target="_blank">📅 20:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=UpCvrcTzgqRQW4XrWrotOLFAjh9gfHLdPCq9Pmo6QRJW3UK0b3D5zwyyb9eXKd-9-lLqWHvfFtTK0pKNjN3R5n4Mc_aWbdPI5xl5Kagv1pT67N6fg6PkbrFarOysXlg3JIAUW5mCI9FeVJ-CYztt-YPZOXd8u_Eay2O5Zg8oRZA0PMNgk7RyYTQuCNSKARNaS8wjzA1RRe6o6d0Mupwamux9EXaXX7VaBuvi_HMQQebAmdi2KfjPK1eSA1q-QE023rE54QZf58V2GgtgYODDw4s2fzIwj-91RuRuYZ4ArKUiJPb7EVb7y_WaRUPiKy-io8B4vJD5GGsep1rtmIFk1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=UpCvrcTzgqRQW4XrWrotOLFAjh9gfHLdPCq9Pmo6QRJW3UK0b3D5zwyyb9eXKd-9-lLqWHvfFtTK0pKNjN3R5n4Mc_aWbdPI5xl5Kagv1pT67N6fg6PkbrFarOysXlg3JIAUW5mCI9FeVJ-CYztt-YPZOXd8u_Eay2O5Zg8oRZA0PMNgk7RyYTQuCNSKARNaS8wjzA1RRe6o6d0Mupwamux9EXaXX7VaBuvi_HMQQebAmdi2KfjPK1eSA1q-QE023rE54QZf58V2GgtgYODDw4s2fzIwj-91RuRuYZ4ArKUiJPb7EVb7y_WaRUPiKy-io8B4vJD5GGsep1rtmIFk1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز پنج‌شنبه اعلام کرد اگر تهران طرح دریافت عوارض برای عبور از تنگه هرمز را اجرا کند، رسیدن به یک توافق دیپلماتیک میان ایالات متحده و ایران غیرممکن خواهد شد.
او در گفت‌وگو با خبرنگاران گفت: «هیچ‌کس در جهان از سیستم عوارض‌گیری حمایت نمی‌کند. چنین چیزی نمی‌تواند اتفاق بیفتد. غیرقابل قبول خواهد بود. اگر آنها همچنان دنبال اجرای آن باشند، رسیدن به یک توافق دیپلماتیک غیرممکن می‌شود. بنابراین اگر بخواهند چنین کاری انجام دهند، این تهدیدی برای جهان است و کاملاً غیرقانونی است.»
او همچنین خبر داد که در مذاکرات با تهران برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «پیشرفت‌هایی» حاصل شده است و به گفته او «نشانه‌های خوبی وجود دارد»، اما واشینگتن با «سیستمی روبه‌روست که خودش تا حدی دچار شکاف و چنددستگی است.»
وزیر خارجه ایالات متحده با اشاره به این که مقام‌های ارشد پاکستان به عنوان میانجی مذاکرات امروز به تهران سفر خواهند کند، گفت: «ترجیح رئیس‌جمهور آمریکا این است که یک توافق خوب حاصل شود... من اینجا نیستم که بگویم حتماً چنین اتفاقی خواهد افتاد، اما اینجا هستم که بگویم ما هر کاری بتوانیم انجام می‌دهیم تا ببینیم آیا می‌توانیم به توافق برسیم یا نه.»
او در عین حال افزود که اگر یک توافق خوب حاصل نشود، دونالد ترامپ «به‌روشنی گفته است گزینه‌های دیگری هم دارد.»
پیش از این گزارش‌هایی درباره سفر روز پنجشنبه فیلد مارشال عاصم منیر، رئیس ستاد ارتش پاکستان، به تهران منتشر شده است. خبرگزاری‌های رسمی ایران این خبر را یک روز پس از آن منتشر کردند که وزیر کشور پاکستان، برای دومین‌ بار طی هفته جاری وارد تهران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75597" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RD4teq7kz9dguVV7arjUCbmlk183A6BNvvo9EEwh53TBfxPeGXslP_iN5NgPEqBDRX9ulNpcPdObFcSMjEqhK5IdAYvD-59Mb-9C69M6SHZ5ij46GcWcuWt6gzWl4uvjoBeV8GALWmvd0YEL-nBXhNRy1msJmCR9zRTsa2TE7pPy3cvfUQefmBByJ0jO-RuMCGRZsY107lGJx0crca95-VQLeOwTiYqZ8hDzf-_SNQRxOsM75ottKCn6jzwREF91uBtW9jbqN5zFU5XxDr2IWczJqQi60qtpcETfKJsCx_WVkHpVo2NZBLMTlmhD1orDgtuX-_4Ur8kBf0iXzBf6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس نیوز به نقل از یک منبع آگاه از روند مذاکرات خبر داد که کاخ سفید گزارش خبرگزاری رویترز مبنی بر این‌که مجتبی خامنه‌ای دستور داده اورانیوم با غنای بالا در ایران باقی بماند را رد کرده و آن را نادرست دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/75596" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
