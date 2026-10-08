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
<img src="https://cdn1.telesco.pe/file/fgcviQhJkbm9Sr9yuNHqLy1x78LfSbm8kK1MEO1IMul5D_A66EfEIhbMNyMCP-YBXSG9QEkzaRiw30Jz5NZGXHv6dQ8Be2tRKB-3in6SGKXXqJbQT60dfamWxZumd8jWmP-plZcKglHT0ivXDYoJYv4Lx8B55204B7ddOwpN9B71lOYSCrzRZ-_zQl_n-PDoxcf-FkLZMZDDwO_GPykb7bh3uvSyLcBnduMS_fWiP-nFWRSRj9l_8AN55H_RrGNfqcViIRe7kFos_3XGU1kONSArYBMGWq-SnsgYP50hzT0XyusbeMLewWMYKJYo3-f2jgD_kQPT3K8BvU8Z7ud3rA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی می‌گن. اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جوری که می‌خواستم به خودم نشون داده بشن می‌گذارم.ممنون از حمایت‌های ماهانهvhdo.nl/patreonیا گاهانهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQEJ-SSC1babn0Vgvzae04EgoqLSA8WKyrKl7x43wL8_-_Aow_1wFMO_fdH9M_7Sl7zy3n-_3ZKBflfweQHftwe-_gsfoY8mZxwc2oX90UVJnkUvD7LCIlC4yU7OW3a4el9eMcqROKrfUpA7AtdrItr5pmA-jYT9YDvhaMMxjyZLCEQmHzp_fn96Z10Rb60k03c6sHcGW0TTtJvIzV3bk9dCQ-TLvFyjb0Q141CVpftERO0U9uhGm3KFR2kgX9qb8Q8a3wazFtWhBicY4YSeh0omqfXt3nkQ-CflTN2_YeAoGf3F3R_rgS33rq0OGH62bc-QfaX19ABquA4-WsWCxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات در جریان است، پیش از انتخابات حمله نمی‌کنیم
ترجمه ماشین:
ما در حال انجام گفت‌وگوهای سازنده‌ای با جمهوری اسلامی ایران هستیم. می‌خواهم برای همه روشن کنم که اگرچه ایران هم از نظر اقتصادی و هم از نظر نظامی در وضعیت بسیار بدی قرار دارد و اگرچه محاصره همچنان با تمام قدرت برقرار خواهد ماند، در حالی که نفت با حجم بی‌سابقه‌ای از تنگه هرمز عبور می‌کند (تنها دیشب ۲۲ میلیون بشکه، بدون اینکه حتی یک بشکه از ایران آمده باشد یا به مقصد ایران برود!)، ما تا پیش از انتخابات میان‌دوره‌ای که قرار است روز ۳ نوامبر در ایالات متحده برگزار شود، در هیچ زمانی به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!
پرزیدنت دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/VahidOnline/78663" target="_blank">📅 20:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78662">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=TgghhF0en728mbSYhKpUs71id-A07UPP-fUxse7wX2uf0xlOX4vtmQ6mIEmalyNjcytDrMmyVuxWtnEdwehbI0oWGP21w5YC8IOp4-xb_HcDDVzmZPVPr1FYjQ-OZB3qa15wJR5TgOh7UxdobCqcRSqIdiPKxtrumZuHLfhmEEXUsg2ySt4LLWwrxJibj9alq3wNj7hpVPtF7lBpuotZLPn0dNPA778DSgXxP_dkrnZ6HF8UzeNAu2FQsMW-VsXt7dzWpy3Pib-_HGdEu_qC4Vc1XHKVBI35rybKOv6xJ0yOckqmxUJwtYWGBrQh1Hk0DCo0iIpQvVOpqRe7lOWUdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b534ce975d.mp4?token=TgghhF0en728mbSYhKpUs71id-A07UPP-fUxse7wX2uf0xlOX4vtmQ6mIEmalyNjcytDrMmyVuxWtnEdwehbI0oWGP21w5YC8IOp4-xb_HcDDVzmZPVPr1FYjQ-OZB3qa15wJR5TgOh7UxdobCqcRSqIdiPKxtrumZuHLfhmEEXUsg2ySt4LLWwrxJibj9alq3wNj7hpVPtF7lBpuotZLPn0dNPA778DSgXxP_dkrnZ6HF8UzeNAu2FQsMW-VsXt7dzWpy3Pib-_HGdEu_qC4Vc1XHKVBI35rybKOv6xJ0yOckqmxUJwtYWGBrQh1Hk0DCo0iIpQvVOpqRe7lOWUdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ گفت: «من باید در مورد ایران اقدام می‌کردم، چون آنها به سلاح هسته‌ای دست پیدا می‌کردند و آن وقت می‌فهمیدید مشکل یعنی چه.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به احتمال حمله موشکی ایران به شهرهای آمریکا گفت: «ببینیم اگر آنها روزی به لس‌آنجلس یا سن‌دیگو حمله می‌کردند، چه اتفاقی می‌افتاد. این دو شهر به دلیل موقعیت جغرافیایی‌شان بیشتر مطرح هستند و منظور من حمله موشکی است.»
ترامپ افزود: «اگر چنین اتفاقی می‌افتاد، وحشتناک بود. بگذارید لس‌آنجلس یا شهری مانند سن‌دیگو را هدف قرار دهند. بگذارید یکی از شهرهای بزرگ ما را هدف حمله قرار دهند. آن وقت است که می‌فهمید مشکل واقعی چیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/VahidOnline/78662" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78661">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osE0eWshEnHRGVb5DwjJTJIYtQMr_zJT77OnL6MwcTkfr5HJh88VfMi7UgsRiEiHpNR-etmAMJbfxLHNNYtd6mvjOeJHOiEhsAcLuQfbrRqe63b85-C9ubYBIwC3kUXTgQ39u7ryvpEk5HqDZVOoRh4WQyM9bXEEGQ5HVnU0tM4n5kMmuSFBEAsbaR89pjvMKCykuboiwshYUsLbjX-DROR4gk_A_a1pjjPRxNEpicab5g2c8KnjeNzAqla-fNvMQD5XrEgGBoiKAbz2klbI2jkHb19HuE-6Cazw5IHg88ZoSunkuduyv8Ffeg49MzM3QSnWdqe0DiVlDPOJU2tRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز پنج‌شنبه ۱۶ مهر گزارش داد شرکت هواپیمایی لوفت‌هانزای آلمان پروازهای خود به ریاض را تا ۲۴ مهر و ایر ایندیا پروازهای خود به مقصد و از مبدا پایتخت عربستان سعودی را تا ۱۸ مهر لغو کرده‌اند.
این تصمیم همزمان با تشدید حملات حوثی‌های یمن مورد حمایت جمهوری اسلامی به فرودگاه‌ها و زیرساخت‌های عربستان سعودی اعلام شد.
حوثی‌ها اعلام کردند فرودگاه بین‌المللی ملک خالد در ریاض را با موشک بالستیک هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/VahidOnline/78661" target="_blank">📅 19:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lyco_gh-hUD3QHy6JpVFkdbn-44nQqhMBDoIJAeYw2sILbWKo7aublsOk0Si4jLD-VhwEqZb2ZzDiOjlz0clK7m3Jh84UkaQn6ivQp1zIYXss5K7_nfIGeOeuK08wR3qjo7snXFTLyAYa8tkxzJcSO7x-AOCT09r3TWXiiqGRQKhZwQGtEpguQtU09e-iYSROiI_FVwxzcpJ5F1ePGLvxJZQc5Z35p-2zckwO33iRh9b_oSriiyhFzgfLRDgp6eUptjJGziYqYW7SXdOJpdXbYz7qDNFauWsm9KpkPZws2tQqvVi6xsqO0PUsPCZ6mrzuOclhXlGUmudCc3if-kRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارگارت همیلتون، دانشمند آمریکایی و از پیشگامان مهندسی نرم‌افزار که نقش مهمی در فرود نخستین فضانوردان آمریکایی بر سطح ماه داشت، در ۹۰ سالگی درگذشت. او رهبری گروهی از متخصصان را بر عهده داشت که نرم‌افزارهای مورد استفاده در ماموریت‌های فضایی آپولوی ناسا را طراحی و توسعه دادند.
موسسه فناوری ماساچوست (MIT) با تایید درگذشت همیلتون اعلام کرد که او روز چهارشنبه هشتم مهرماه ۱۴۰۵، برابر با ۳۰ سپتامبر ۲۰۲۶، از دنیا رفته است. این موسسه در بیانیه‌ای، همیلتون را از پیشگامان علوم کامپیوتر توصیف کرد که پیش از فراگیر شدن حرفه مهندسی نرم‌افزار، در توسعه این حوزه نقش مهمی داشت.
همیلتون از سال ۱۹۵۹ تا اواسط دهه ۱۹۷۰ در موسسه فناوری ماساچوست فعالیت می‌کرد و مدیریت بخش مهندسی نرم‌افزار را بر عهده داشت. گروه تحت مدیریت او نرم‌افزارهای هدایت و کنترل فضاپیمای آپولو ۱۱ را طراحی کرد که در فرود تاریخی نیل آرمسترانگ و باز آلدرین بر ماه در سال ۱۹۶۹ نقش تعیین‌کننده‌ای داشتند.
در جریان این ماموریت، رایانه فضاپیما لحظاتی پیش از فرود با مشکل پردازش بیش از ظرفیت روبه‌رو شد، اما نرم‌افزار طراحی‌شده توسط گروه همیلتون توانست با اولویت‌بندی وظایف، عملیات فرود را ادامه دهد.
باراک اوباما، رئیس‌جمهوری پیشین آمریکا، در سال ۲۰۱۶ به پاس دستاوردهای علمی همیلتون و نقش او در پیشرفت فناوری فضایی، نشان آزادی ریاست‌جمهوری را به او اهدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/VahidOnline/78660" target="_blank">📅 19:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLjfZoDIE1qSPosh89KPRFKnsrM7gaeU2ALlEW5ewDJPaqmBnVRdOj7SrNG8tv9hXB1mIHO1RzErwQlKNmfjsVMRNaCRMcASvvIWrxwPVo2asG7LeEM-TPDSaon-LrrdzDU94cwwuIpb7o2sF9DgYrjH1h_mnzL0NLqR73k5CfBRZTmVY1SARDriXh7CxOGiy1i-3n9DkEZlzs58wv5ZS8c490QHee5xrSylkBcZ230SX2YPYRL01MxgQ1A4_3nbYuGOk8CY8YMqXhofw9fUi5NaZphof9DCo-kCfMBFeMfEi-FQLjBifGI6rnQ13rDWuEWzBWK-KGNblBYS7LCEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی در چارچوب طرحی به ارزش حدود ۲۱ میلیارد دلار، توسعه میدان نفتی مرجان را برای افزایش ظرفیت تولید نفت و فرآوری گاز دنبال می‌کند؛ میدانی مشترک با ایران که بخش ایرانی آن «فروزان» نام دارد. براساس گزارش مرکز داده‌های باز ایران، عربستان روزانه حدود ۷۳ میلیون مترمکعب گاز از این میدان برداشت می‌کند، در حالی که ایران از بخش خود گازی تولید نمی‌کند.
در تازه‌ترین مرحله توسعه مرجان، شرکت نفت عربستان، آرامکو، قراردادی با شرکت آمریکایی «کی‌بی‌آر» برای نوسازی تاسیسات این میدان امضا کرده است. کی‌بی‌آر روز سه‌شنبه ۱۴ مهر ۱۴۰۵ اعلام کرد خدمات مهندسی و اجرای پروژه را برای تاسیسات فرآوری، فشرده‌سازی گاز و زیرساخت‌های برق مرجان ارائه خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/78659" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78658">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFNJsfOI_Kym-691s-kVu9z3II90ALxJ1u1Cf2XR1vThyDgsviL3SyJxVlc64KdVPUjBRMp7m5Fu4H6Yf1t9tOH9aKKuwNviguDpz9ht0WB7FAiHXtH5BdmF6ar07irTd0KpOIB2Q0li22bd3Y1Doz9QDL6eSFHv1GwEPtVgLU2GootyjRFu3zBEQBxItsUnfHGJmOYVubfnNiecfhnqeqNiDtJk9nVSss4wgaYiG8tpsbcX0RgOqQRyfqru58ZM3XQUsNu1cnpwiM-TtoUfNn6qNli0FO0F3-hu99nqLhH_9Gt4F-F-2R0kcDFsxMKTmhs1lDPdfR8-KD0VKEWmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز، روز پنجشنبه ۱۶ مهر ماه، گزارش داد شمار کشتی‌هایی که از تنگه هرمز عبور می‌کنند، پس از افزایش حملات به نفتکش‌ها در هفته گذشته، به پایین‌ترین سطح در بیش از دو ماه گذشته رسیده است.
رویترز بر اساس داده‌ها و تحلیل‌های شرکت تحلیل کپلر گزارش کرد، روز سه‌شنبه فقط ۷ کشتی تجاری از تنگه هرمز عبور کردند که پایین‌ترین رقم از اول مردادماه تاکنون محسوب می‌شود.
عبور نفت خام از این تنگه نیز با کاهش ۲۷ درصدی نسبت به بالاترین سطح زمان جنگ در هفته قبل، به دست‌کم ۱۰.۱ میلیون بشکه در روز رسید که معادل ۷۴ درصد سطح پیش از جنگ است.
به گفته تحلیلگران کپلر، بخش عمده این کاهش به انتقال محموله‌ها از کشتی به کشتی در دریای عمان مربوط می‌شود.
به گزارش رویترز، با این حال، صادرات از سواحل دریای عمان و دریای سرخ به ۶.۷ میلیون بشکه در روز افزایش یافت، رقمی بیش از دو برابر سطح پیش از جنگ که به جبران کاهش عرضه از طریق تنگه هرمز کمک کرد.
داده‌های کپلر نشان می‌دهد تعداد کشتی‌های عبوری روز چهارشنبه به ۱۰ عدد افزایش یافت، اما همچنان بسیار کمتر از بیش از ۲۰ کشتی در روزهای یکشنبه و دوشنبه بود.
این گزارش پس از آن منتشر می‌شود که حملات به نفتکش‌های عبوری از تنگه هرمز در هفته گذشته به بالاترین میزان هفتگی از زمان آغاز جنگ ایران رسید. پیش از آغاز جنگ در نهم اسفند سال گذشته، روزانه حدود ۱۲۵ کشتی تجاری بزرگ شامل نفتکش‌ها، کشتی‌های حامل گاز، کشتی‌های فله‌بر و کشتی‌های کانتینری از تنگه هرمز عبور می‌کردند.
همزمان، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنحشنبه نموداری در شبکه اجتماعی تروث سوشال منتشر کرد که نشان می‌دهد سطح تردد نفت از تنگه هرمز به میزان پیش از جنگ آمریکا و اسرائیل علیه ایران بازگشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/VahidOnline/78658" target="_blank">📅 15:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78657">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVZXoKs24ATUsPC4O60rtkgSfoyus5qkRoCVVfYM-bTOCcU4W0A-NL68pMTJe2hXwWJpx13Et69NMss9LE9QYzma3HAW6MQj9gXZa_Stkg2w4Z_v8xYelTWfJLbstKKgHkgczlEskb8eiTgiitTdpsDn6CQB_29hnapMa3NA1rF9ELLGMNt944mHc8tTgJLTgXKyK2tW8NrXSb8jbIKc6BCnOshJEGK3sYcid-7eVlqHBZ6gz-SUfFUvMlARSAYe7dKRrfqY8EQKofhExnGwfe1ur6RjmdJPzUSpnZdPMkng7rr4gVIvWXulYSyM8ejwjPxvuI56-I2gZYcjAHLukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حمله افراد مسلح ناشناس به ستاد فرماندهی انتظامی شهرستان گلشن در سیستان‌وبلوچستان، نیروی انتظامی وقوع انفجار و تیراندازی در این منطقه را تایید کرد. هم‌زمان، ارتش جمهوری اسلامی از کشته‌شدن یک نفر و زخمی‌شدن سه نفر دیگر در حمله‌ای جداگانه به مینی‌بوس حامل کارکنان ارتش در زاهدان خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/VahidOnline/78657" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VDkYhl5bnxwHi3g6LmeCMhbj310AcyLVVSsjnjmE5rTcXjR6NrtXaMutHekzd_VuD5qqca_zcZwqQmjV-UuSXfLwdYqueB9-r6jybYPkgTxrd77D98ZrZAv5OxhwnSSDHwMwjFOQOduo8OUEwPDhKhrO5B3nRoKUBwd7wQqufF994kW3wAWtMWy-nr_Cc_uq2-4-sBnafivY1HKko1z2DDwwNnoh-1vZ2ln3Nr-zaPec7EfcE5cE2huvltKXAN0w3aup0VZ4OJtQBA7NfWghV3lz2H7zrOjn2C_9cvJz_fdLH_ZygPGz7jA98pmPtaAtW9utSXaNfb8HbHhEgVgWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز
پنج‌شنبه ۱۶ مهر در گزارشی تحقیقی بر اساس گفت‌وگو با بیش از ۷۵ کارشناس حقوق بشر، وکیل و شهروند ایرانی نوشت ایران پس از اعتراضات دی‌ماه شاهد شدیدترین سرکوب چند دهه اخیر از سوی جمهوری اسلامی است.
به نوشته رویترز، دستگاه‌های امنیتی و قضایی جمهوری اسلامی با همکاری صداوسیمای حکومتی، از طریق اعدام‌های شتاب‌زده، محاکمه‌های غیرعلنی، پیگردهای قضایی گسترده و انتشار اعترافات اجباری، در پی ایجاد فضای ترس و خاموش کردن مخالفان هستند.
بر اساس این گزارش، از ۲۸ اسفند ۱۴۰۴ تاکنون دست‌کم ۳۴ نفر از افرادی که در ارتباط با اعتراضات دی‌ماه بازداشت شده بودند، اعدام شده‌اند. پنج نفر از آن‌ها تنها در ۱۰ روز گذشته اعدام شدند. در مقابل، طی چهار سال پس از اعتراضات ۱۴۰۱، در مجموع ۱۵ نفر در ارتباط با آن اعتراضات اعدام شدند.
رویترز همچنین گزارش داد مقام‌های امنیتی ارمنستان در ماه مه به گروهی از معترضان ایرانی درباره تهدیدهای جدی علیه جانشان هشدار دادند و از آن‌ها خواستند برای حفظ امنیت خود و خانواده‌هایشان این کشور را ترک کنند.
اشکان، معترض ایرانی ۳۰ ساله که در جلسه با مقام‌های امنیتی ارمنستان حضور داشت، گفت به آن‌ها هشدار داده شد افرادی احتمالا برای ربودن، ترور یا آسیب رساندن به آن‌ها اعزام شده‌اند. رویترز نوشت روایت او را با گفته‌های معترض دیگری که در همان جلسه حضور داشت و فایل صوتی آن جلسه تطبیق داده است.
رویترز همچنین نوشت نهادهای امنیتی جمهوری اسلامی با تهدید خانواده‌های مخالفان ساکن خارج از کشور در داخل ایران، لغو گذرنامه‌ها و خودداری از ارائه خدمات کنسولی، فشار بر منتقدان را به خارج از مرزهای ایران گسترش داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/VahidOnline/78656" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Oc53gayna9Wh7ZUqcEG0z-GlyA9DgR3yfv7XkzQ-vzDTtWgPBtyy_s274C6au3nTdm1qsw7MvAvdMZMIAWT01DDxChfLc_plPPCmgeJm7X1QT-bd55n5lz8BdDnj_CnFXwKjbxj-lPp28fWzrAjsXjVEfYj7oyiqeaWTkSYK9gmCc18pA0_-p24l5vwnrWoUjtQEdvnF_irzDTElGOIjWegY65M1BgKJWtVnPEL_tTUENI8cxhXSI8_SRDTnPakKlQRUX67AdKkkOZmFoCj8fZSv88metFBDxuX_Pa_G8snxGHBZ8ZOIz4D1Keev52g4kDLKvj3SlXTjOkweS1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، بامداد پنجشنبه ۱۶ مهر در سخنرانی در ایالت تگزاس درباره جنگ با ایران گفت این جنگ «خیلی زود» پایان خواهد یافت و ایران را «کشوری شکست‌خورده» توصیف کرد.
ترامپ گفت: «وقتی این جنگ تمام شود که خیلی زود خواهد بود، آن‌ها یک کشور شکست‌خورده‌اند، کمی رمق برایشان مانده، اما نه زیاد.»
او همچنین با اشاره به نفت عبوری از تنگه هرمز گفت این نفت در سراسر جهان توزیع می‌شود و بار دیگر بر نقش آمریکا در انتقال نفت از این مسیر تاکید کرد.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا در جریان یک گردهمایی انتخاباتی در تگزاس گفت «ما به زودی از ایران خارج می‌شویم و قیمت نفت هم مثل سنگ پایین می‌آید.»
او گفت افزایش بهای نفت ارزش جلوگیری از دستیابی ایران به سلاح هسته‌ای را دارد.
رئیس‌جمهور آمریکا همچنین در مورد احتمال دستیابی به یک توافق با ایران گفت: فکر می‌کنم این توافق واقعاً چیزی است که می‌خواهم انجام دهم، اما آیا آن‌ها حاضرند برای متوقف کردن برنامه هسته‌ایشان چیزی به ما پیشنهاد دهند؟ و ما قطعاً هرگز اجازه نخواهیم داد ایران سلاح هسته‌ای داشته باشد.
آقای ترامپ همچنین با تکرار سخنان جنجالی چند روز گذشته‌اش در مورد حمله فرضی ایران به لس‌انجلس و سن‌دیگو گفت: «همین چند روز پیش گفتم: بگذارید موشکی به سن‌دیگو یا لس‌آنجلس اصابت کند... بگذارید به سن‌دیگو یا لس‌آنجلس حمله کنند تا شاهد اتفاقات ناگوار باشید... ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما از شهرهایمان محافظت می‌کنیم. ما از کشورمان محافظت می‌کنیم. ما اجازه نمی‌دهیم چنین چیزی رخ دهد.»
این سومین سفر دونالد ترامپ در طول یک ماه گذشته به تگزاس برای تبلیغ نامزدهای جمهوری‌خواه محسوب می‌شود؛ نامزدهایی که در تلاش برای حفظ کنترل کنگره، اکنون با رقابت‌های انتخاباتی میان‌دوره‌ایِ به‌طور غیرمنتظره‌ای فشرده روبرو هستند.
ترامپ در ورزشگاهی مملو از جمعیت در سن‌آنتونیو سخنرانی کرد تا از کن پکستون، نامزد جمهوری‌خواه سنا در این ایالت حمایت کند که در رقابتی تنگاتنگ با جیمز تالاریکو، رقیب دموکرات خود، قرار دارد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78655" target="_blank">📅 05:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhRvtc40gmRe43LoovpxkfbX4SMElgoNBgqpsl3me0BuU1ya7jSTyxddP6kGqdHL6UhXhswNaCA8SwKcx9OeBQvZeefw3GxF0Ohy31h3DThSRse1c6XG9A-7dJfXxQaeA7-eHH-6SMCFVc6Y2_r7VYOgagRXZLhpAtjVDVwJEuOGkRj2sNeqyTQlkh3wVZ7rSiDq2fm_5vgRXkQc-1XqqYBBJ-gvpjqlDP5fQFSjcRhnPhFIh5khr--weA3eRettxlQFSWBJs5VxNRkzKQa1GG6zx1ouj-ukRzou14lTovNZRmLlscOXUYb-M5D0ZRPKVDfcRhCg1krh3y4iyMA4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو رسانه آمریکایی گزارش کرده‌اند که پنتاگون برای حمله احتمالی مجدد به ایران طی روزهای آتی آماده می‌شود.
سایت خبری اکسیوس به نقل از مقام‌های آمریکایی گزارش کرده طی روزهای اخیر پنتاگون با صدور دستورالعملی از سنتکام (فرماندهی مرکزی آمریکا در منطقه خاورمیانه) خواسته روند آمادگی خود را برای از سرگیری عملیات رزمی عمده علیه ایران تکمیل کند.
همچنین مجله آتلانتیک هم در گزارشی اختصاصی به نقل از دو مقام آمریکایی نوشته کاخ سفید از پنتاگون خواسته است تا گزینه‌هایی برای حمله به اهداف ایرانی تدوین کند که امکان اجرای آن‌ها پیش از انتخابات میان‌دوره‌ای وجود داشته باشد.
به گزارش آتلانتیک، دونالد ترامپ مشتاق است پیش از انتخابات، قیمت بنزین را کاهش دهد و به پیشرفتی عمده در مناقشه با ایران برسد.
به گزارش اکسیوس، دستورالعمل پنتاگون شامل تاریخ مشخصی برای آغاز حملات نبود و دونالد ترامپ هنوز تصمیم نهایی را اتخاذ نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78654" target="_blank">📅 05:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78653">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJtVD_a40ryKpogiGcCpyOqxxn8quFGgN8cMY6WJEdW4vFxbsHVDcGwoyyaQeNntRcDnn2RlOCxRRP0H-ogsowv-VnnEga46fu-T3jqe8b0ia8SgDXBpG7MOapyX53CzyvmBct1PmWK2SDpxNQSFuj0f48y34Qenl7HjhltGp4E5HMLMoXkyx4GYS42G3LJGetQvjVfxYQM80TWsHO2_xe48-NggKGlaz9hAKboWXtV41B3eg9swVELwopPaoSGvauCxgYTJslBFFs1GCquSpBAATwzd5jEvz0TKvF4vdRDtN6OjRer_G59jj9FqPpMV44px5wH4FJ34bM7B-XchSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش آمریکا، سنتکام، بامداد پنجشنبه ۱۶ مهر با انتشار پیامی در اکس، اظهارات یکی از فرماندهان سپاه پاسداران درباره بسته بودن تنگه هرمز و کنترل کامل ایران بر آن را «نادرست» خواند.
سنتکام اعلام کرد تردد کشتی‌های حامل کالاهای تجاری و محموله‌های انرژی، از جمله ۲۰ میلیون بشکه نفت خام، در تنگه هرمز جریان دارد و افزود: «ایالات متحده و شرکای منطقه‌ای به‌وضوح کنترل تنگه را در اختیار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78653" target="_blank">📅 02:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-hZJGH1eE580cb-HzgvYm8xu6tdDnLJbi_Q3u_dD8Fh_DehMnUf5oV_sSFARr1tmZbBIIgrqwhnsgf_oyPODCoFW8_Zr6b87WdA2UTGvFeuG9bXgNalOrUAxbFFOw4GfbuW1DwKTv3MpDVEum7DbSAH5Yj8hRdVMyDTOIl-E6ptZTjItPn3ls52zxgs4UlGs0jY0zebAn3jHdmOs_nlxJ-HSmuO2_O4drF6_7D9eFNERAYANgRty0pzyBpVTSg0vqIhwOxx23eGF_CWhn-QOBgCD5r69_tRdjtFxJAq571KpzO1Jm2_Qz8fZIZHL94u5S0MRbrP3k42CjZu7G8zOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات تجارت دریایی بریتانیا: در حمله به یک نفتکش در شمال قطر خسارت جانی گزارش شده است
سازمان عملیات تجارت دریایی بریتانیا شامگاه چهارشنبه ۱۵ مهر اعلام کرد یک نفتکش در آب‌های شمال قطر، در ۵۱ مایلی مدینه‌الشمال، با چند پرتابه هدف قرار گرفت.
بر اساس اعلام این سازمان، در این حمله تلفات جانی گزارش شده، اما هنوز جزییاتی درباره شمار کشته‌ها یا مجروحان منتشر نشده است. مقام‌ها در حال بررسی حادثه‌اند و از کشتی‌های منطقه خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را گزارش کنند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78652" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBySNYbAxA2hNE1xty40adM60rGDV-xwH9On13Yht6bHo1i6sz-YrjtPDX5cGMelVpHGoFAxuHjkpxsmb6t9XKI8oWCemQBQAWSRwmJE8214T8SVtcwIHnm_YqPsMyA4Q-yUtXqYuiFapiJNz9Eb6JAvwJ8OI-2fJ6F60j54QJpKZRNttGXQnB-_t8imW7thwcfuBMK6A0mvtCft1KYtBQXrAuI7ayHGcn5-PfaoYwHoYnfhvZ8sBp74boA1kfTac9nqjLXwQ0gkjcHADGPaT89XCwvd-KjlBfDTFRXBxKnMcT8nZgaGx4ungviqvjIUqU1Qx7ZgjMff4aoCCYvPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو منبع مطلع به خبرگزاری رویترز گفته‌اند جمهوری اسلامی ماه گذشته ۲۰۰ میلیون دلار در اختیار حزب‌الله لبنان قرار داده است تا این گروه به خانواده‌های لبنانی آواره‌شده در جنگ امسال با اسراییل کمک مالی کند.
بر اساس اطلاعات منابع رویترز، حزب‌الله قصد دارد در مرحله نخست به هر خانواده حدود سه هزار دلار کمک کند. اولویت با خانواده‌هایی خواهد بود که روستاهایشان ویران شده یا به دلیل حضور نیروهای اسراییلی در مناطق جنوبی لبنان امکان بازگشت به محل زندگی خود را ندارند.
یکی از منابع شمار این خانواده‌ها را حدود ۵۰ هزار خانواده اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78651" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noWK-_4-8qIrvm4jY7uCeapVykOmxOC8b9zNIY9kLderznXlM_Qi_S1KhUJ_YeSSQykQf91EPeKdNrQjDCg2xitfje6mZfgTDMR8xQF7CcveDas-aiimaGVw8aJ9Lt1c5VL5jFyw117_vsNHsBa82LXoSkq32WYTZ2Ja_WAVEfbXUNsCzkMY__c887ev_9Hg_9fva52NelED7zhxIfa3MQq5N9SQlhTqAjqp0zZI2yBHbqhbaHpXA1s4jRe1MFJB_aWPiyAeAZ3sT0R7uyp5BaRLpl6jXfa93rGqCmm6wM8Nd4oCU5a5XMpdgSzAGFrlgUVBt3J0O0lEuMi1YujnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهاره آقایی، وکیل دادگستری محبوس در زندان قرچک ورامین، به ۲۰ سال حبس محکوم شده است.
کانال تلگرامی شیرین عبادی
با اعلام این خبر، حمایت از معترضان دی‌ماه، حضور در مراسم چهلم سپهر شکری و کمک حقوقی به خانواده‌های دادخواه را از موارد مطرح‌شده در پرونده او عنوان کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78650" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMaJ6XX2OF6qXDEB9p_VcBkxagTI_9V8_sPsOaJDFBuOPR95NLufDivRyD9kvN8grodEflGejrbJpESPIqDTk6piFkdGg-A2REKXCocklEeDyUxat_ahR2N4hP1G55O9csMjJriE-ulNEgLDUiR-fYwxzmjepHwCt0jOccOfSzlBxtgSKtosFYmzOWzrgWOZylCy6ICHytm07oIUW5D71_jRM9n-jnT_UTHEXJTX5LREN8WTOGBm6lBjWroYScjK6rKBxymAYLmZYbJOMFS8od5Qpp-bCZzBVIs0D4_KvF7uIsjHm1sqRBT62NgE45num91ND8d3Q4vGNdivrSYoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده آمریکا، با انتشار پیامی در اکس و با لحنی کنایه‌آمیز نسبت به استعفای محسن پاک‌نژاد، وزیر نفت ایران نوشت: «ایران وزیر نفت جدیدی دارد. با توجه به اینکه از ۲۵ اوت تاکنون حتی یک بشکه نفت خام نیز توسط ایران بر روی هیچ شناوری بارگیری نشده است، این وزیر نفت دقیقا چه چیزی را مدیریت می‌کند؟» پیش از این، مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر ریاست جمهوری ایران اعلام کرد، پزشکیان پس از موافقیت با استعفای وزیر نفت، طی حکمی حمید بورد، مدیرعامل شرکت ملی نفت ایران را به عنوان سرپرست وزارت نفت منصوب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78649" target="_blank">📅 17:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgApYPpX2rbazAim5In38DUeIDtGOMwQ9XaGScgfe1qBtBYSEgYvn4k6YiZgE3Z9fyXGVzqyf1bcp62c7vfTgZCqZ1udbWDW2EYevvuxNcjziUWIG4FXb9OHHa2DPo2_pFZ0dTVAGH9bDdUtlu8MKnOWEAtoJHSmIzKLxcf4M9_JfpHVHjeZIF5_wr41eMdqe9_xAuobnYaV56dAGvvdU6t32VHPW-iWDYDuPvOLXIcNInRKdgqMCrr77W5dqEtOaFEBiAxTJgGDyQO0GUEN-pPkkVTHqBPcUBa77MNEJI8RZQAEh2PevfTKAfy7v1TbX8BD4y2rVQTJ9eLQqO-Pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، معترض ۳۷ ساله، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ و محبوس در زندان چوبیندر قزوین، در مرحله تجدیدنظر تایید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78648" target="_blank">📅 17:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1p4ozC1OUQ3hzXfeUAXlF64HxTMrcHABO6DShLsf1Vbsa__UZNR0Rm56NKG_UOGhu0cpxpNr9d5BLd93n91i1NlsCV6hvpv0SffoRnGZ0RFXdyBOx7Qx-p-ONAFgJv6bB8nTglNp0weE9U-ne3xTnco6RbQigaCIelxVDiPhyrm1rryE8Jj6OaVxx-U2_olvI-wFV3XmnDUXkkhL8b3ia8KDl5V0MMbU-KjotT_RMOh6P_1W8SRBdkVFAjv4_Q9S2BvB8tSz1G55ZHHi_Dexe8ylQ1dH_DWc9gDwEGh2aJFGJptqHxE6HP6GkZh-cUVajFZ9lWLX9pgthczHzWrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=nUwmtTa9WuNuh5S1n2yWslDqoliCfmS5c8Tyd9Nb5fOXxfvPTekB6N8Sk4XSPrjZpJuAU5bgRcAXJmXQi9bT15buBKEr4bWQSxlWCsgmG3lrAxtZSXbFTO8zGl5d9GOhjVFFxwPkbxW-ie294xWGyGerXrvEfR2OBIAQgvjes9SXEiUJZsDU2mEdvNp9Ea4Wi0A2kSM7bZuuTpqjxbKPD6KEwLis1ripjNiqBhXy7d1mSgl0qeVH_A7dn3ea-asHtbJYMU4GqOOjjE3H-Sev1GWt4DTf1TCi7ELWL8Y5GKI0Kf4C02I71bYwTtdovptZW2GyT22I1rhKuJvGtdh34w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20e0cac582.mp4?token=nUwmtTa9WuNuh5S1n2yWslDqoliCfmS5c8Tyd9Nb5fOXxfvPTekB6N8Sk4XSPrjZpJuAU5bgRcAXJmXQi9bT15buBKEr4bWQSxlWCsgmG3lrAxtZSXbFTO8zGl5d9GOhjVFFxwPkbxW-ie294xWGyGerXrvEfR2OBIAQgvjes9SXEiUJZsDU2mEdvNp9Ea4Wi0A2kSM7bZuuTpqjxbKPD6KEwLis1ripjNiqBhXy7d1mSgl0qeVH_A7dn3ea-asHtbJYMU4GqOOjjE3H-Sev1GWt4DTf1TCi7ELWL8Y5GKI0Kf4C02I71bYwTtdovptZW2GyT22I1rhKuJvGtdh34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید ایران فرصت‌های متعددی را برای دستیابی به توافقی دربارهٔ برنامه هسته‌ای خود با ایالات متحده از دست داده است.
او روز چهارشنبه ۱۵ مهر در یک نشست خبری مشترک با همتای یونانی خود در آتن گفت: «ایران فرصت‌های متعددی را برای رسیدن به توافق هسته‌ای با آمریکا از دست داده و همچنان مبالغ هنگفتی را صرف تروریسم، تسلیحات و حزب‌الله می‌کند.»
روبیو همچنین گفت ایران اکنون با اقتصادی رو به فروپاشی و تحریم‌های تازه روبه‌رو است و مسئولیت این وضعیت را متوجه «روحانیون تندرو شیعه حاکم بر ایران» دانست.
او گفت: «اقتصاد ایران در آستانهٔ رسیدن به وضعیتی است که از نظر وخامت، کمتر کشوری در جهان آن را تجربه کرده است و همهٔ این‌ها نتیجهٔ عملکرد روحانیون تندروی شیعه‌ای است که در آن کشور تصمیم‌گیری می‌کنند. آن‌ها هستند که مردم محروم ایران را به چنین وضعیتی دچار کرده‌اند.»
وزیر خارجه آمریکا همچنین با تکرار موضع واشینگتن دربارهٔ جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت دونالد ترامپ توان نظامی و بخش بزرگی از ظرفیت صنایع نظامی ایران را از میان برده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/78646" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTPhnDgCRxG2_p29DSX5S5XQV71ZZEAZiqaLfT8TOxnAstUocdeRkcSXw1G2rlwI-wcayILyFNKO6z7mwHc46_VIltKTA9byVLQS0VRgJW6gxvWG1LQHxLyfRgksVPL5bZxu-LQoyzqgngz7AuvK9aj3pHdWQVV-VHex-pTtQhsIO2lD7VhzztAzp9OaZ6xTwz3QMfUGAZB2_38btV7KYJGlnohhJIM-npLLJJ_mfjwsO86LcUCk7yq6XTirMxyua-gGSvPD5ghexqeysPpWjeYT7FZpqQa-Hv_Un0Vj6FC-BtsCEDT2bRmSqUbX_pQYDXARTnsIhPxUqhG8VnGXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه خراسان نوشت که نجمه امینی، دختر ۲۳ ساله، به اتهام «سب‌النبی و توهین به ائمه معصومین» در فضای مجازی، از سوی شعبه ششم دادگاه کیفری یک خراسان رضوی به اعدام محکوم شده است.
امینی پیش‌تر در یک فایل صوتی از زندان وکیل‌آباد مشهد از صدور حکم اعدام برای خود خبر داده بود.
پس از انتشار این فایل صوتی، خبرگزاری فارس، وابسته به سپاه پاسداران، اعلام کرد که هنوز هیچ حکم قطعی برای نجمه امینی صادر نشده و دیوان نیز درباره پرونده او اعلام نظر نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78645" target="_blank">📅 16:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rkPG6LUqWYogSutwe0lGah-tSUYCRKX-hf2G-lMrBwSzeoIraKG1nc9XXrM-4YXxtKb5_mKhMD6fYanzHiRjYzq2_muKJ_IJrGf4j759LrQIIyhgzHKlrp29l01jbOobvwjQUh6KNb_ASaE076Fmwm_W7ik3OUhUGdDVE37ogGpRd29vkiKU5UTS6ZeZeJD1RkFHWq6Eu3d-dwtBkxz5jY7HqFej_T7gcfZesM3GjhJhCduQVWKxHPsd3iap3vtzx22bUUxQYFFA4ZRtR_4ugY5e_OJc5S67OtwToquuFeBSXE1Z5W95b2BlHqrklw-Sq9rwGhw57yFxBxYUqaubdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران باید غنی‌سازی را عملاً کاهش دهد؛ میزان اختیارات پزشکیان و عراقچی روشن نیست
🔸
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، می‌گوید حکومت ایران برای پایان یافتن جنگ باید ظرفیت غنی‌سازی اورانیوم خود را به‌طور «معناداری» کاهش دهد و ایالات متحده در مذاکرات با جمهوری اسلامی، به وعده‌های لفظی بسنده نخواهد کرد و خواهان اقدام عملی تهران است.
🔸
آقای ونس در گفت‌وگو با خبرگزاری رویترز که بامداد چهارشنبه ۱۵ مهر منتشر شد، همچنین گفت ایالات متحده با مسعود پزشکیان، رئیس‌جمهور ایران، و عباس عراقچی، وزیر خارجه، در تماس و مذاکره است، اما برای واشینگتن روشن نیست این دو مقام تا چه اندازه در ساختار فعلی قدرت ایران اختیار تصمیم‌گیری دارند.
🔸
اظهارات او در حالی مطرح می‌شود که تهران و واشینگتن طی هفته‌های اخیر پیشنهادهایی را برای پایان دادن به جنگ و بازگشایی کامل تنگه هرمز ردوبدل کرده‌اند، اما دو طرف همچنان بر سر دامنهٔ مذاکرات و مسئله هسته‌ای اختلاف اساسی دارند.
🔸
معاون رئیس‌جمهور آمریکا در پاسخ به پرسش رویترز دربارهٔ شرایط واشینگتن، خطاب به مقامات جمهوری اسلامی گفت: «اگر سلاح هسته‌ای نمی‌خواهید، پس چرا به سوخت غنی‌شدهٔ ۶۰ درصدی نیاز دارید؟ و اگر می‌خواهید تعهد خود را به نساختن سلاح هسته‌ای نشان دهید، سوخت با غنای بالا تولید نکنید. این یک مسئله بسیار پایه‌ای و تعیین‌کننده است.»
🔸
او افزود: «فکر می‌کنم اگر آن‌ها بخواهند تعهد خود را به نساختن سلاح هسته‌ای نشان دهند، باید در زمینهٔ ظرفیت غنی‌سازی خود اقدامی معنادار انجام دهند.»
🔸
آقای ونس در عین حال تأکید کرد که آمریکا همچنان برای رسیدن به توافق آمادگی دارد، اما چنین توافقی باید شامل امتیازهای مشخص و عملی از سوی ایران در زمینه برنامه هسته‌ای باشد.
🔸
او گفت: «ما قرار نیست حرف را با عمل معاوضه کنیم.»
🔸
این موضع با مواضعی که مقام‌های جمهوری اسلامی در روزهای اخیر اعلام کرده‌اند فاصلهٔ زیادی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78644" target="_blank">📅 02:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=nKSSig5nDGDFrDhLL4JWoaFT7bniFq5JYuVaxKbqYu1g98Hwg_i90qNK_uXlmSJ53ZE5MbuzNCsYqihEdcCX3S9PsQnHwoqMprF-Ylb8vmqRlHBBhjcPwDvfnr-6C4JWTPq0p2lG70EkjuzqxTwqgXCtvSWdz6Euc62prn0Ki_joKOb2pO3Wg56_KEmtWvjzLX-d6ADs9Fc94wlxbxVks5urz8jF-6GJMnHfiosWLSP-0mzNjLh2mKK9hzInljgtezUFVcjlFLwdqybnD7H29QsvnTDRfErlfpzObPKPBpDBJQ031LSex8QditGRYEJkQqqZqHTf4RNCpThjkbXhfXOeIH5-bWb5YVJpBjCT13lzlIdn6Ed0EfGMVd57Nz3PdrIcDMxQOulmYqTJBD9M_31y-s0jxNRmpkwWJnhQ5TsXDnr1fzd7IRCFiTLEtgQZNVp_Fkf6yY57k1QnMjvu2NwxopqLeCbF0ULkdS5aa_pRI7Odrl63DhHllIFnUhIo-0Gts3PzDw2_dJ4rf-sLwR_IJMJbSQoVSDaDgG23Kfde0FDTm8icKUhjzXorhpmOxD_rPwHS75c7KRVHwiqF5r0Li0eB7vol9S1KXfV0WsACikL3RDHB0YhC0mlZGMFJv365e-vRyFDfZm-eJc0K3xTQSxdcq2JK-I8zupO7aQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ccbd7257.mp4?token=nKSSig5nDGDFrDhLL4JWoaFT7bniFq5JYuVaxKbqYu1g98Hwg_i90qNK_uXlmSJ53ZE5MbuzNCsYqihEdcCX3S9PsQnHwoqMprF-Ylb8vmqRlHBBhjcPwDvfnr-6C4JWTPq0p2lG70EkjuzqxTwqgXCtvSWdz6Euc62prn0Ki_joKOb2pO3Wg56_KEmtWvjzLX-d6ADs9Fc94wlxbxVks5urz8jF-6GJMnHfiosWLSP-0mzNjLh2mKK9hzInljgtezUFVcjlFLwdqybnD7H29QsvnTDRfErlfpzObPKPBpDBJQ031LSex8QditGRYEJkQqqZqHTf4RNCpThjkbXhfXOeIH5-bWb5YVJpBjCT13lzlIdn6Ed0EfGMVd57Nz3PdrIcDMxQOulmYqTJBD9M_31y-s0jxNRmpkwWJnhQ5TsXDnr1fzd7IRCFiTLEtgQZNVp_Fkf6yY57k1QnMjvu2NwxopqLeCbF0ULkdS5aa_pRI7Odrl63DhHllIFnUhIo-0Gts3PzDw2_dJ4rf-sLwR_IJMJbSQoVSDaDgG23Kfde0FDTm8icKUhjzXorhpmOxD_rPwHS75c7KRVHwiqF5r0Li0eB7vol9S1KXfV0WsACikL3RDHB0YhC0mlZGMFJv365e-vRyFDfZm-eJc0K3xTQSxdcq2JK-I8zupO7aQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مربوط به ایران در سخنرانی ترامپ، به تشخیص و ترجمه ماشین:
ما در جمهوری اسلامی ایران خیلی خوب پیش می‌رویم؛ خیلی خوب. آن‌ها دیگر نیروی نظامی ندارند؛ نابود شده. همه‌چیزشان نابود شده و آن‌ها همان طرف شرور بودند؛ قلدر خاورمیانه بودند و دیگر چندان قلدر نیستند. اما هنوز باید کار را تمام کنیم و فقط مسئله این است که به کدام روش. می‌خواهیم این کار را به روش خوب انجام بدهیم یا به روش نه‌چندان خوب؟ خیلی زود خواهید فهمید.
وقتی به «دیوار فولادی» نگاه می‌کنم، همان کاری که ما انجام داده‌ایم و آن‌ها اسمش را محاصره گذاشته‌اند؛ من اسمش را «دیوار فولادی» می‌گذارم. حتی یک کشتی هم نتوانسته به ایران برسد. تنها کشتی‌هایی که عبور می‌کنند همان‌هایی هستند که ما اجازه عبورشان را می‌دهیم و این تأثیر بسیار بزرگی داشته است.
برای همین کشورشان از نظر مالی شکست خورده است. یک کشور شکست‌خورده‌اند؛ همه دارند کنار می‌کشند، همه دارند می‌روند. به نیروهای نظامی‌شان حقوق نمی‌دهند، به پلیس‌شان حقوق نمی‌دهند، به هیچ‌کس پول نمی‌دهند؛ اوضاعشان به‌هم‌ریخته است. اما هنوز باید کار را تمام کنیم.
نیروی دریایی ما پیشتاز است تا تضمین کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. و این همان چیزی است که همیشه گفته‌ایم: هرگز اتفاق نخواهد افتاد. هرگز اتفاق نخواهد افتاد. این دیگر یک امر انجام‌شده است.
ملوانان و هوانوردان دریایی بزرگ ما قهرمانانه جنگیده‌اند تا ارتش آن‌ها را نابود کنند. آن‌ها دیگر نیروی هوایی ندارند. نیروی هوایی‌شان از بین رفته است. نیروی دریایی‌شان از بین رفته است. آن‌ها ۱۵۹ کشتی دارند؛ همه‌شان همین حالا در اعماق دریا هستند، کف دریا افتاده‌اند. رادارشان از بین رفته است. تمام تجهیزات ضدهوایی‌شان از بین رفته است. ظرفیت تولید موشک و پهپاد آن‌ها به‌شدت کاهش یافته است. به‌زودی آن هم از بین می‌رود. دقیقاً می‌دانیم بقیه‌اش کجاست.
اقتصادشان ویران شده است. تورمی دارند که هیچ کشور دیگری در جهان ندارد. و آن مردی که چند روز پیش رفت، گفت: «من می‌روم چون کشورمان تمام شده.» این را گفت. نمی‌دانم. من هیچ‌چیز را قطعی فرض نمی‌کنم، اما اوضاعشان خوب نیست.
و به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها تن از رهبران تروریست ایران از صحنه روزگار محو شده‌اند و مستقیم به دروازه‌های جهنم فرستاده شده‌اند. همان‌طور که می‌دانید، رهبرانشان رفته‌اند. گروه دوم رهبرانشان هم رفته‌اند. و بزرگ‌ترین مشکل من این است که هیچ‌کس نمی‌داند واقعاً چه کسی کشور را اداره می‌کند. هیچ‌کس نمی‌داند؛ شاید هم این چیز خوبی باشد. اما خامنه‌ای را یادتان هست؛ همه‌شان رفته‌اند و حالا ما اینجاییم.
ما داریم کارهایی انجام می‌دهیم که هیچ‌کس قبلاً انجام نداده است. مثلاً تکلیف این کشور باید خیلی وقت پیش روشن می‌شد. حالا ۵۱ سال است. قلدر خاورمیانه. این کار باید خیلی پیش به دست رؤسای جمهور یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم. همیشه ما هستیم. کشورهای دیگر باید خیلی وقت پیش این کار را می‌کردند، چون با گذشت زمان فقط بدتر شد.
اما ما کار را انجام دادیم و راستش مدام از رهبران جهان تماس دارم که خیلی از من تشکر می‌کنند. می‌گویم: «خب، کی می‌خواهید هزینه‌اش را بدهید؟» می‌گویند: «آقا، بابت این کار خوبی که کردید ممنونیم.» و من به آن‌ها می‌گویم: «عالی است. می‌خواهید چند کشتی بفرستید؟» می‌گویند: «آقا، ترجیح می‌دهم درگیر نشوم.» آن‌ها هیچ کشتی‌ای ندارند.
واقعاً داریم بار تمام دنیا را به دوش می‌کشیم. روی دوش ماست. و به یک معنا دوست داریم این کار را انجام بدهیم، چون خودمان قوی‌تر شده‌ایم و دیگران ضعیف‌تر شده‌اند. آن‌ها فقط ضعیف و ناکارآمد شده‌اند و ما کارهایی انجام می‌دهیم که هیچ‌کس دیگر، هیچ کشوری، هرگز نمی‌توانست انجام دهد.
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78643" target="_blank">📅 00:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/141ace0942.mp4?token=khxV1F6l77J2gYdILMc88NjyGTDuO1303ULRzfva2lK5mx2LKrICxuOkM4guKUuru1xVod2FXqPJ5KWhJLc0BXn_2QfP-eRUsTWpJjmxqwGUUvgRWoE3B4EFHuV6vE9OCJESBKl6PxVCd3_0Q5uiNV4yI3lSh4NV72PlmixWJ2ywA4KFAyCiEdY5Pb77rlpDPi72OZWiHJUx4mwrCRN20UrmJjV0_dDlADxstnKPHldTPwh6blXcd4yVE5mWk-V__AOGHjv53cP2igzKwPa3q7Nac2MfEAO8W_ULdJZJdLSSMtuSy_BR3kO7DpA33_hzsBAalqSoadK8Uyvcm2yT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/141ace0942.mp4?token=khxV1F6l77J2gYdILMc88NjyGTDuO1303ULRzfva2lK5mx2LKrICxuOkM4guKUuru1xVod2FXqPJ5KWhJLc0BXn_2QfP-eRUsTWpJjmxqwGUUvgRWoE3B4EFHuV6vE9OCJESBKl6PxVCd3_0Q5uiNV4yI3lSh4NV72PlmixWJ2ywA4KFAyCiEdY5Pb77rlpDPi72OZWiHJUx4mwrCRN20UrmJjV0_dDlADxstnKPHldTPwh6blXcd4yVE5mWk-V__AOGHjv53cP2igzKwPa3q7Nac2MfEAO8W_ULdJZJdLSSMtuSy_BR3kO7DpA33_hzsBAalqSoadK8Uyvcm2yT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرگ یک کارمند ۲۸ ساله موسسه تحقیقات ضدطاعون در سیبری پس از ابتلا به بیماری که گمان می‌رود طاعون ریوی بوده باشد، موجب نگرانی‌هایی شده است.
بر اساس این گزارش‌ها، داریا شیپیلووای ۲۸ ساله در ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) به بیمارستانی در شهر شلخوف در منطقه ایرکوتسک منتقل شد و دو روز بعد درگذشت.
ده‌ها نفر که با این زن در تماس بوده‌اند قرنطینه شده و تحت نظر پزشکان قرار گرفته‌اند، اما مقام‌های روسیه می‌گویند تاکنون هیچ مدرکی پیدا نشده که نشان دهد مرگ او با عوامل بیماری‌زایی که در محل کارش با آنها سروکار داشته، مرتبط بوده است.
مقام‌های روسیه می‌گویند وضعیت تحت کنترل است و تاکنون مورد جدیدی از بیماری‌های عفونی مرتبط با این حادثه گزارش نشده است. با این حال، گزارش‌های تاییدنشده درباره احتمال ابتلای این زن به طاعون ریوی در شبکه‌های اجتماعی منتشر شده است.
مارکو روبیو، وزیر خارجه آمریکا، گفته است واشنگتن این موضوع را از نزدیک زیر نظر دارد اما در حال حاضر دلیلی برای نگرانی نمی‌بیند. دونالد ترامپ، رئیس‌جمهور آمریکا هم اعلام کرده که آماده کمک به روسیه است.
@
VahidHeadline
, @
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78641" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9M9waxVCMsTL_UZOHqGi9m3_gB48HLcyniA9FaDhviQhhLh1mBjtPd-NmnrD2q6HuRAzhcquXbX2O08TD5typXoxY53ffptBs8T1RwlQ-eIxLK-O7To88PqG-J5ni42GvLaHHPRpPYWYxz84GZsmAdk3yFij5x9RCzcnrqv7u_fE8tOn-bPgsb906A1FgRy6oia5tpNQ4VtbswHjUrRD8Qyr1q3z3pQTdCxN6zfqupuvc6d5LnswFqpHeKkcGE5uQ2s8DjsrCN0k4VNv1MUkFovILsfKvjCH8IIpszZ0J6NJxRlaKZHIl-TfGkDnHdMetjjwoSMejBqtmlFL7H7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران گزارش‌های نادرستی را منتشر کرده‌اند مبنی بر اینکه یک بالگرد MH-60R نیروی دریایی آمریکا، پس از اعلام وضعیت اضطراری در شب گذشته، در دریای سرخ سقوط کرده است.
✅
واقعیت: گزارش‌ها درباره سقوط یک بالگرد نیروی دریایی آمریکا در دریای سرخ صحت ندارند. همه هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه در امنیت هستند و وضعیت همه آن‌ها مشخص است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78640" target="_blank">📅 16:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/edGAa9JQYd4ibPcc-TjzcfH4zB0XPOdA7sj0jxGQCfNi_VNS1woSETVjBAz7j-OFKgxkFZH_VtY1soccXFVvUoeaVvSm8DBbOoYL8Sbqy560CUuEIbRNYI-m3YjPdgaeWIldwa18IUJi7Grrlvgv989KiyWLQIUFEdC1qkbT8z1G8kLAiSi-KCDwOm6NGYaGfjfK4I16hicGiI8Qhtha7YqLVrIipPFT8Iy22ZVb1g3fPuDFxWrAXo_KeydA-omFuEwxkhGZxLqTPohWrHjF1u4knGX5ZFhg2my7Nr36tRl1bzN9IVuhgFIjkEPAsUaDvGv4I-uxddFbH2nj4E06JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا بعدازظهر سه‌شنبه ۱۴ مهر اعلام کرد گزارشی با تاخیر درباره حادثه‌ای در تنگه هرمز در ۱۳ مهر دریافت کرده است.
بر اساس گزارش یک «منبع تاییدشده»، یک نفتکش هنگام خروج از تنگه هرمز هدف حمله قرار گرفت.
در این اطلاعیه به هویت نفتکش، عامل حمله یا میزان خسارت احتمالی اشاره‌ای نشده و سازمان عملیات تجارت دریایی بریتانیا اعلام کرده است مقام‌ها در حال بررسی این حادثه‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78639" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioFbitxtZW2ppHSDOOe6Ls6MrMV9nEHrYtLFfsm3Y2sQ6IhLl5-XvsK1h_lR_YllsxTNoEbY1Qxj20F3i0t-TsyItWtMXH-axhCL9eL2lnJ30B5CNo11kqizHrF6x1NORT5W_rhT0WO2yOq9gy994qcYlqBg5SLEnSd-ePZW9oQg_Q1zti1fXU0UNS8PV-NYtYxO7L4S1MWje0ugkDQ3S6kE4d_pNZtGcjadauP8ozac1e6hm93tRdajCIaxvH8KO5ENUy6fqEmlihz-wAudYXj5hoBcSQrMyiKOYJ5w6X3Z0OdS30ZwWnb9_C5OfAniaN97FbBeCgEOSDDGH2WeYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواپیمایی کشوری عربستان سعودی روز سه‌شنبه ۱۴ مهرماه اعلام کرد شامگاه دوشنبه، فرودگاه بین‌المللی ملک عبدالله بن عبدالعزیز در جازان و فرودگاه بین‌المللی نجران هدف حمله قرار گرفتند.
براساس این بیانیه، این حملات منجر به جراحت جزئی سه نفر و بروز خسارات مادی به فرودگاه‌ها شد.
شورشیان حوثی مورد حمایت جمهوری اسلامی دوشنبه از حمله به فرودگاه‌های عربستان سعودی خبر داده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78638" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9P2hVsBLq3Dihlbi6RGigJQ1jAS9xJmxawSHZaHLJnXIL5ansXVdK2TQzSTsZdCuJkrtcDWk0ELiHiyR9kHv0j6gYePNi4JTawnUhc9dML_nckCRrxvlDHZn0j42ohoBSGuvQkX3LY9_fSapILFCCDBLwxoVsYiGxLeknOcVWWzz_H_xM3HACmy-wPUi5BJXAWyGadN-XAqygInHMwHDee6zjuxbq9PyGwwwstnh3M_eu1qZU9tNB7RrTZoNKaOxP4_BWKqoX4_aptTd0nrQ_DsTXS7rUHRdTKKvwotghzRE4Nl5ozTcUv166lrwA4k5_dyCWA26h5IcHl3bdGr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ کشور قاره آمریکا در بیانیه‌ای که روز دوشنبه، ۱۳ مهرماه، منتشر شد «اقدامات تروریستی» جمهوری اسلامی و نیروهای نیابتی‌اش در نیمکره غربی را محکوم کردند.
در این بیانیه به «تلاش‌های خصمانه ایران و نیروهای نیابتی‌اش از جمله نقشه‌های مرگبار، تأمین غیرقانونی پول، مداخله سیاسی و فعالیت برای نفوذ خارجی» اشاره شده است.
این بیانیه اشاره می‌کند که هدف از این گونه اقدامات «تقویت شبکه‌های تروریستی، تضعیف فرایندهای قانونی یا دولتی و ضربه زدن به امنیت منطقه‌ای» است.
ایالات متحده، آرژانتین، کانادا، کلمبیا،‌ کستاریکا، جمهوری دومینیکن، گویان، پاراگوئه،‌ پرو، و ترینیداد و توباگو امضاکنندگان این بیانیه هستند.
این بیانیه پس از آن منتشر می‌شود که آمریکا و پاراگوئه در ماه سپتامبر گذشته به طور مشترک «نشست مقابله با تروریسم فراملی» را با هدف همکاری در نیمکره غربی علیه «فعالیت تروریستی» تهران برگزار کردند.
سال گذشته اکوادور که متحد آمریکا است سپاه پاسداران، حماس و حزب‌الله را سازمان‌های تروریستی اعلام کرد و آرژانتین نیز در بهمن‌ماه ۱۴۰۴ نیروی قدس سپاه پاسداران را در فهرست تروریستی قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78637" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmUD0wl23AE040peeCuJ-IBgcCLxBTDAnshUg2s8aYzanR-iNwjZQprGVRNMhZRmWVqdABSXTso8rLFsnAfCTjYzYlW5IfSma5_FdtFBfmUjvDLo3FZhi9bF0WmTqCDqeREV8ZRALiQ81hWpJWGXa6dvsvsmv7dpZC5ytJOGWcRztN-oNu7lpCX5SDZZtU-C6deJY86Ai5iRhEsYYAQ-HLZSoTQkCVFx22WDfiIxkrD1V9Umaj2xfYQGlloFEoBKtTfHC45rrytExJ7fWDZgwdPC6tuBnsaQmwpMb334E5NA0R7_DawpbUqYMrKGz7U1Fhn26Niuxv67lFV4HpZxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی عباسیان، ۳۸ ساله و ساکن شیروان، از سوی دادگاه انقلاب بجنورد به اعدام محکوم شده است.
یک منبع مطلع به ایران‌اینترنشنال گفت حکم اعدام عباسیان یکشنبه ۱۳ مهر در زندان شیروان به او ابلاغ شد.
هادی عباسیان در جریان اعتراضات دی ماه با انتشار ویدیوهایی از مردم خواسته بود در اعتراضات شرکت کنند.
تاکنون اتهام دقیق منجر به صدور حکم اعدام و مستندات دادگاه علیه عباسیان مشخص نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78636" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpiHQAqv8CFoKcgSADQJmZ_oupbbHPlK64hNB992DcLZ2y_xjl76p8UiJwcVZeUAsnrXJRAU92oiSeMqyz2L1MgNT-MIbcuOguGLi85te10L7nq50FDMdYK0Spc1de_nOODsgkX_CbRtoQSX3BoiJiGmI8xbUBqwX1nYaw8XD9245ICm0WxZKVGeOqL4Hz7xw-TlhcNqY0Og5eXP2WviXTWjiOvEAmS6VT0XaoyLL3d5QSrLAFhEw8qm6q2nFarTFSo6iL6sJONVZkfHemjAzm-m3OlV3wdksQqPjfOPAVsi_PrqMwRNQgWHwtMja6im6zleL4zBahqDITfl31nfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر ایران از اجرای مخفیانه حکم اعدام «تورات محمدی»، شهروند ۴۲ ساله افغانستان، در زندان مرکزی کرج خبر داده است. او با اتهام «جاسوسی» به اعدام محکوم شده بود، اما مشخص نیست دستگاه قضایی جمهوری اسلامی او را به جاسوسی برای کدام کشور یا نهاد متهم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78635" target="_blank">📅 16:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78633">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ch3w3KIzBoOPptCOqYDDoD5FhT0A8fS6FAbV6x-4NmhTffL8Zme0NihGG5kOFq3KdLGDzY7ng2WiXcu9c4mjITmXP-wz3MIk7F6GhhDR6s7YgAnkH3JQXkcUkMyG66k7zZ3L4IHB_lUPE2YIqZBjsE9zU_pSGalIxBdD3lXn0ZZ28Yryvw1cUp68rMgMjvcbqk7MgcWTAKcN3lDfj6TcY9RPSlb744HGDqspiRustvwtXqkQhRyeDqPLxwzxc5o9wJEU3E9mIKI8089QTZPanfbt-Id-odXkxKGREYyQtf7NxySKFKgHQH-2GTIlgcXQyiN-y-GLp-XfpqJ6hqXc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QtK-f3PUbZXi_BJZTN0u45cOv0-JsQq8vt8eTgZb2v3_sxs7yhkqfY7oSzto40IQ2TWT-ruSC_e7w4tnoTxCZYNGuif80Y28roHgYQuWStk7GDhL871xKhyOmwYfv0h6RfG8kDKM3pLby4YiCfC0Q_ZLqRKnYmRi0N9WBFJiZHJDjuOC0pPbmlrALhjtxpx9e-Y08vtTidrVDHY2bx-_Ywio8W3teex9F-u7uwjQQ5M5qf_Pc8XrJ0sU-W0olVatR3cHZ4vwrAAyMm0SwSgQGMOkaX4uEq1LuGTrVuqDL5m6QeOxaHOF7-GQvpBYD-9dkrRMLAognjiND4Qbw1aCAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد ارتش ایالات متحده در پی دریافت اطلاعاتی درباره احتمال حمله پهپادی جمهوری اسلامی، ۱۲ فروند بمب‌افکن بی‌۱ را از پایگاه هوایی فرفورد، متعلق به نیروی هوایی سلطنتی بریتانیا، خارج کرد.
وال‌استریت ژورنال علت خروج این بمب‌افکن‌ها را «نگرانی‌های امنیتی درباره طرح‌های احتمالی حمله به پایگاه» عنوان کرده بود.
دونالد ترامپ، رییس‌جمهوری آمریکا، دوشنبه تایید کرد بمب‌افکن‌ها به دلیل تهدید امنیتی جمهوری اسلامی از این پایگاه خارج شدند.
این در حالی است که مارکو روبیو، وزیر خارجه آمریکا، ساعاتی پیش‌تر این انتقال را بخشی از جابه‌جایی‌های معمول نیروی هوایی توصیف کرده و گفته بود ارتباط مستقیمی با تهدید ایران نداشته است.
@
VahidOOnLine
روزنامه نیویورک تایمز در گزارشی اختصاصی به نقل از مقام‌های آمریکایی و بریتانیایی نوشته است که آمریکا پس از دریافت اطلاعات جدید درباره احتمال حمله پهپادی که گفته می‌شود سپاه پاسداران آن را طراحی کرده بود، به‌طور ناگهانی هر ۱۲ فروند بمب‌افکن بی-۱ نیروی هوایی آمریکا را از پایگاه هوایی «آرای‌اف فیرفورد» در جنوب انگلیس خارج کرد.
نیویورک تایمز به نقل از این مقام ها که درخواست کرده اند ناشناس باقی بمانند نوشته:‌ «حمله احتمالی بخشی از یک طرح پیچیده و چندمرحله‌ای ایران برای هدف قرار دادن هواپیماهای آمریکایی و کشتن شماری از چندصد نیروی آمریکایی مستقر در این پایگاه بوده است. به گفته آنها، تمام بمب‌افکن‌های آمریکایی در آخر هفته از پایگاه خارج شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78633" target="_blank">📅 08:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R96TJbywIpHeI1ee8TxYvMHJNTSL1iHz4nqddPTk-GSZYFrh9DY5rbfU-I3HiERtQ5UwpA2qZmCv66QbV4wVE0g382YG60DeCR5CYHoTm8_gEU2Ll-vtlK5_560TFrNexWo0oBtog7f72I885lg8y4-7tdppQdl0ipXIppPahWOaYtlqEA1CUkfCoE4Vkjuda-zxY7_oXF9tWihH5LBcIQbqiyD0bR9hMgXd6NhaUP60jM-JGHP51mJqYIsbmiQs9EMeJYVkTMspWUVgzuF70ByEY_hxMqHQB6HFe7XK916AeFHq5LvfcLcjQW2A16UDieoFUPMtQ6iqd4zNoDleJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lCWW2HNlmieWZ8-bI58qpt48gcClGYKSkRhTGEi4fnnNBKtdJvUi4B3QrhN5ektKDP6HXlO6U6H5dQD8vVpqU3tv4JCf5guFOh_1WsQMdz_rKsv_ir53pjLUqVKyBntgPtXC9dqFCoS3tr81eCsaxADgmzxtwNydT68nhQjQBkRlvoqPS9OnOCzHOYO3zMUZbqOl-hJlm1asENYF_0uAKglV8e0wvtn19rlZtDnl24bxUSeDfhoFU-SjgbfxGcCZYH7Hmt-EQ4n4bTq77FZ3d7MB9WdjmyH70UXcWgtj0pjmiXGc5f0UBb_zoaA7zryzDXfMT79pQWmZ43BEqGQJug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به سوال خبرنگاران درباره حادثه امنیتی در نزدیکی پایگاه هوایی فرفورد بریتانیا اعلام کرد که ایران با این پرونده مرتبط است.
ترامپ درباره دلیل خروج هواپیماهای این کشور از پایگاه فرفورد گفت: «ما با یک تهدید مواجه بودیم و اگر قرار باشد ما را تهدید کنند، هواپیماها را جابه‌جا می‌کنیم. این اقدام تا حدی مشکل را برطرف می‌کند.»
رییس‌جمهوری آمریکا تاکید کرد: «ما افرادی را که این تهدید را طراحی کرده‌اند می‌شناسیم و آنها خودشان را با دردسر بزرگی روبه‌رو کرده‌اند.»
@
VahidOOnLine
ترامپ روز دوشنبه ۱۳ مهر در کاخ سفید و در پاسخ به این پرسش که آیا احتمال می‌دهد ایران پهپادهای رزمی را به بریتانیا منتقل کرده باشد، گفت: «نمی‌توانم این را به شما بگویم، اما اگر چنین کرده باشند، بهای سنگینی خواهند پرداخت.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78631" target="_blank">📅 00:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=tKS-s0cjyXSIYwXUt-MQlOgTFTPJiRXwhnOb-gtktaUGePLyzSgyXJUpFAR5_6A_C71olN5slPddlMaIdM0nrGqnQXI6jCyJQhKExotZW6TFyaxj15VDyKegILog1uuwZ3GNqjv5RQvI3F9iy3U2-eCyu3OiVAdHAQRM7Wi5m9QPTLqL1wvFhqbsIwBlndjbDJ8enhU0p8NQ-i635UlBuLc3qScBP27EV_TGDEvgBnwYtRqQ2DCHyVtmBOH-OGG8STryn3OwsPPY2UjGGoVBy0Sppru7VFT_IeeprDXBsniT5ywmgFz6G1N7jG-Y4ZYEpBljeGdFY2VMjPbxJ0ge7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668a44a1f7.mp4?token=tKS-s0cjyXSIYwXUt-MQlOgTFTPJiRXwhnOb-gtktaUGePLyzSgyXJUpFAR5_6A_C71olN5slPddlMaIdM0nrGqnQXI6jCyJQhKExotZW6TFyaxj15VDyKegILog1uuwZ3GNqjv5RQvI3F9iy3U2-eCyu3OiVAdHAQRM7Wi5m9QPTLqL1wvFhqbsIwBlndjbDJ8enhU0p8NQ-i635UlBuLc3qScBP27EV_TGDEvgBnwYtRqQ2DCHyVtmBOH-OGG8STryn3OwsPPY2UjGGoVBy0Sppru7VFT_IeeprDXBsniT5ywmgFz6G1N7jG-Y4ZYEpBljeGdFY2VMjPbxJ0ge7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ترک کاخ سفید، در پاسخ به سوال خبرنگار فاکس‌نیوز گفت: «شخصا باور دارم که ایران مسئول حمله تروریستی فلای‌دبی بوده است».
این اظهارات در حالی مطرح شد که جی‌دی ونس، معاون رئیس‌جمهوری آمریکا در همین روز به خبرنگاران گفت که هنوز مدرک مستدلی بر دخالت جمهوری اسلامی ایران در این حمله دریافت نکرده است.
در پرواز دبی به تل‌آویو که روز چهارشنبه انجام شد، کمک‌خلبان با حمله به خلبان اصلی تلاش کرد که هواپیما را با تمام سرنشینان که اکثریت آن‌ها اسرائیلی بودند، ساقط کند. این اقدام با واکنش به‌موقع خلبان و مسافران، خنثی شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78629" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjVTHgTpEA7CMoRXlfW0GT0__y2aPu-RAUvuOD8xKh5QuskT86T1bRI9vdJ7QhFZIcdUP25HuIoT9CxsMb7nMSy64i27x2vhsbTxwAycTQIK5vGwOtMcvMM2z5rmlvQW7MSyqOpwFzKVG9e1CsfZvDXrsk5DxWZ1nCGqiCGxIUfcHYioCwnpKHO9YNBvPwM47hVRjwtPjkaN7O98RzyzF_xRpGQq_1IDOFoelIWQ9lglHYSRQoY8BrT4qUpEPFEKiBSOnjWj3gDxEKWNVKAFweX_VM1gmq2r4NZqB-qoMR2Vw7W95YFX6AkiBaLiP2d8sw-jcH-w8XUPtVz650NgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد روز دوشنبه ۱۳ مهر یک پ نفتکش در حال گذر از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است.
بر اساس این گزارش، این حمله موجب بروز آتش‌سوزی در موتورخانه کشتی شده که خدمه در حال اطفای آن بوده‌اند. با این حال، سازمان تجارت دریایی بریتانیا تایید کرد که تا کنون هیچ‌گونه تلفات جانی یا خسارت زیست‌محیطی گزارش نشده است. تحقیقات در این زمینه ادامه دارد و به سایر شناورهای عبوری توصیه شده است با احتیاط کامل در منطقه تردد کنند.
@
VahidOOnLine
پیش‌تر:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hjDDLvQansVlFpdbEQxePU1TapTovmird6aX9pM_vq2-7Jm28v2QAihh49WdWDnQajCpkaGXaJd_7Q0aFPomanR72nC9SSRVUYZ1F1ldrVOwn4Rbq5NF0MvAtr3nPxe6efjKIL6ZZTe-1p3CC9N4dEqU6snKi7oVAOPA103sq58RwMf2Hk3Xj6zbF7n_JUK2bMXyWLi3nDaq_19oNuzbWByxzLDhE7a8SvACl4echpfrBCzwE9rf-BXfplIYz2p-6jfD0O7HIofz91YRu7sMflgsk-7oW_VOnSRJz-X8DS7-TNxfaNbB6JesnMMAg2g2Zkby2QozCan1Ay6xJf2DmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا رئیسی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴ را اعدام کرد
- علیرضا رئیسی سحرگاه روز دوشنبه ۱۳ مهرماه همراه با علیرضا سپاهی، از دیگر بازداشت‌شدگان اعتراضاتدی ۱۴۰۴، در زندان دستگرد اصفهان اعدام شد.
- روز گذشته برخی منابع خبری از فراخوانده شدن خانواده علیرضا رئیسی به زندان دستگرد اصفهان خبر داده و گفته بودند این زندانی سیاسی برای اجرای حکم اعدام به سلول انفرادی منتقل شده است.
- علیرضا رئیسی فرزند دختر عموی جاویدنام رامین رئیسی از کشته‌شدگان اعتراضات دی۴۰۴ است. رامین رئیسی ۱۹ دی‌ماه با شلیک مأموران حکومتی در جریان سرکوب اعتراضات کشته شد. پیکر وی را ۲۸ دی‌ماه به خانواده تحویل دادند که در «باغ رضوان» اصفهان به خاک سپرده شد.
- علیرضا رئیسی روز پس از خاکسپاری رامین رئیسی بازداشت شد. خانواده علیرضا تا ۲۰ روز پس از بازداشت فرزندشان هیچ خبری از او نداشتند. او طی آن سه هفته زیر شدیدترین شکنجه‌ها و فشارها برای اعتراف اجباری علیه خود قرار داشته و حتی تهدید به تزریق آمپول هوا شده بود.
- علیرضا رئیسی و علیرضا سپاهی از متهمان پرونده «میدان علیخانی» اصفهان هستند که به اعتراضات شامگاه ۱۸ دی مرتبط است و نهادهای امنیتی مدعی کشته شدن چهار بسیجی و مأمور یگان ویژه در جریان این اعتراضات شدند.
- در پرونده «میدان علیخانی» ۱۲ شهروند به اعدام محکوم شدند. با اعدام علیرضا رئیسی و علیرضا سپاهی، شمار اعدام‌شدگان متهمان پرونده «میدان علیخانی» به هفت تن رسیده است.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P5CS4Z3NEsYInUS0GMIGpxmEP5-yMK2Gx-Mx1lTofeiw8F2RFmZ10SQEFW3eHNQF-O6C3VVhEoM2KX5ZQ_qLNUbjF44jfnt-pjMlK2mMtVZhbdgeaX_2H6A5kaQ_J9I3HJX46maaaxienwKf-qW7MgJsqpoPA3PlRzWh8xlxDBQylFNJ8wZyjOdHxSuN7LOSRZCHTuRco0zbeGeasBfQUGJyR-_Wg9vISUHl8MWMO0VNI8fVtBa2y4HNka_pi-mpBlF3VhnpuslcvSA6aDBiew_QvZgaCnvXBvgKZ9OAycmLzheruUwGuXky53Ui0nse17uwl46ALHKMKD6_bV0jDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی علیرضا سپاهی از بازداشت‌شدگان اعتراضات دی ۱۴۰۴  را اعدام کرد
- خبرگزاری «میزان» وابسته به قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام علیرضا سپاهی بادجانی، معروف به علیرضا سپاهی، در سحرگاه روز دوشنبه ۱۳ مهرماه ۱۴۰۵ در زندان دستگرد اصفهان خبر داد.
- وکیل علیرضا سپاهی روز گذشته با اعلام خبر فراخوانده شدن خانواده علیرضا سپاهی برای ملاقات با او و انتقال این زندانی به سلول انفرادی، از خطر اجرای حکم اعدام وی خبر داده بود.
- علیرضا سپاهی پیش از اعدام و به صورت تلفنی با نامزدش عقد کرد. مهشاد کشانی، دانشجوی ۲۲ ساله ساکن اصفهان، نیز در اعتراضات دی۴۰۴ بازداشت و به پنج سال حبس تعزیری محکوم شده و در زندان زنان دولت آباد اصفهان محبوس است.
- علیرضا سپاهی قرار بود سحرگاه سه‌شنبه ششم امرداد ۱۴۰۵ به همراه ابوالفضل سپاهی بادجانی -پسرعمویش- و امیرحسین صفری حسین‌آبادی در ملک شهر اصفهان و در ملاء عام اعدام شود اما پیش از اجرای حکم به علت استرس دچار سکته قلبی شد و اجرای حکم اعدام او عقب افتاد.
+- علیرضا سپاهی چهارمین شهروند بازداشت‌شده در اعتراضات دی۴۰۴ است که طی هفته گذشته و پس از صدور بیانیه ۴۶ کشور در محکومیت اعدام‌ها در ایران، احکام اعدام آنها اجرا شده است. سیاوش جمشیدی خیرآبادی شنبه ۱۱ مهرماه در شهرکرد و علی همتی سیستانی و مجید نیک‌اندیش روز چهارشنبه هشتم مهرماه در مشهد اعدام شدند.
- پرونده معروف به پرونده «میدان علیخانی» به اعتراضات شامگاه ۱۸ دی ۱۴۰۴ مرتبط است که در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان رخ داد. نهادهای امنیتی جمهوری اسلامی مدعی شدند در جریان این اعتراضات چهار نیروی بسیج و یگان ویژه کشته شدند.
- با اعدام علیرضا سپاهی، شش متهم پرونده «میدان علیخانی» اعدام شدند. عرفان اسفندیاری و گل‌محمد محمدی ۲۸ تیرماه در زندان اعدام شدند. ابوالفضل سپاهی و امیرحسین صفری در تاریخ ششم امرداد در «میدان علیخانی» در ملاء عام به دار آویخته شدند و قائم حسینی نیز ۲۹ امرداد در زندان مرکزی اصفهان (دستگرد) اعدام شد.
KayhanLondon
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hchk544JW3sCmkrsASl8IIvoMD-lz0Vy54P0TOlwum_P7DtY7qvVPvqGTMnKYyuPf1UlznmM_JwZJIJ0fcrf2fcfNSTFoh-8Thl3_F9ZRvdV6dC-pdZZHjgs5AYfe0_5ok8TsM5g9IWF9w4j1ZMi1D7x_XDi9mTFbQaU54OweSzYxy2-3cJzQx0QAFEac0Zao6vcfATYQGtW8qd5d9QVgRZhJ1J-BccpJK5HM21REyD2R6dXaA79ZsXb_TnpZ2FBBPzXYP6liHi5xXmAFBjEJm492ITtAmhZKLQykshhEWKQ5iRVbzP7m3jxmgWmaK5L5tHABjbRsRRbhCFuLtoCZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnh8TCLdIpllSSzt-lvANSWxykD5UVKwPgaXqzqLohAR6f6hnLMrwVhTSMEZvOjdqSngxv4SYTRqdnCaiuF-USYrfPY4AZsXw5-aAf4FlhCt1Ugz2XSA8oZ_puZe0gSIsc6Jmt494byHWwMTlrBvBd-9UVsJjdZFEy9lMTErnGslg1w2FF4AFrDeabTh0JX1yHXjdvxKMTzJTrVTCY83LjF8HOWLh-v9TSm-jB71GkoIgp0RZ2a225-rlkzF74kR7GBpLCbp44r_buQVqHIgbfBoCUaFuZS7WQHEDvf0sQ0RHrCspN6zNLSYO12Jp2Ql0zAnX0aCCcdmtACqoqzyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9-4CHZQvVA0cRFmHy_6QLMJ1ucYb1HLbbJjghh2tPX2NJdCsXzl6zVae2Uq2oTLfmV6USWsByce5EW6pxYnoSrx-4DqFlNsyoTj_KTVPmrlC-jwv_LAARqjCurSKrgL63lQSH0wd7YkVHxt5msa4G4Z4uvl4LhhfHuBWbfTeXuUS-E4mBWW5nE4PZT03qKJUj806wr7T2WJX_1_L6aPM1y1yDNpqfSwiUy-GZYpkhSw2E8A72nB1BESAzCyA73u0Ab_HSk3DL3Tww8arAZkxqK97lEacMkOZe0DHmSA3sPXCccRW7A5sZhxtyMHSVX5GQyn4IBdulaFpWaE7REXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GB-bqKhIi4K4ykatXd8bZlRZXWTJC3NQW8YI5F0zEnDkqPGQj72cpaj57m1UBxxRmKl7IrhW4hDM9AYBqOfB5jJYXUH-iDG1dRA5inmTzf8ZabPeUH6YkwH_OIV8cK7Ud34P-yifI7WuBW73UHRF71A8BIKA8KQVN1p6BQV1-0Hl8nMgGD7Nw3owWMPlLbqjpayXgCcW5VHRnZ27J1VW8XcpDbFAOGMRyfUrYWye_-ioyU9sNPKI04-VR9BtV7NvzRjRhhq2WAVgkoPKmQiv4o7iB19Xqq9Q3AD4N9vjFlZ9McyHo59kSRmL02XdNYbm7F4yI_qt8t2szOXDeQ0LtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=o1KMa68hJCqNloveppDGSUtA0o3iCyNaz-bee2rhz_VG-zzOFfIvy0AMKnvq2sxetkZll4zeu7A1zkhK7noNMA9aDWJO9sY_aZgcvB5AyXEX6b7Cz7RxuYA3sYUzDc-LFNFbqEGTlFe9VNWYHpVqF10YM5mAQcLJ3quxdQaJZmq01sQXsYPo3qqOA0roAQ-5Lj387ve5UngfzyVgtg4xBfJadNjaA9PL6yI4jGxt-4yyLsf15zHHn-fuhYu1AorRbi2ju246_TfHLxZu2kCTDTiZ2rnE7IvqYqEZpWl-XJZEP78S7TZFmnQB8igKm8kXjRnPc38U7gKr1c5XO8zh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=o1KMa68hJCqNloveppDGSUtA0o3iCyNaz-bee2rhz_VG-zzOFfIvy0AMKnvq2sxetkZll4zeu7A1zkhK7noNMA9aDWJO9sY_aZgcvB5AyXEX6b7Cz7RxuYA3sYUzDc-LFNFbqEGTlFe9VNWYHpVqF10YM5mAQcLJ3quxdQaJZmq01sQXsYPo3qqOA0roAQ-5Lj387ve5UngfzyVgtg4xBfJadNjaA9PL6yI4jGxt-4yyLsf15zHHn-fuhYu1AorRbi2ju246_TfHLxZu2kCTDTiZ2rnE7IvqYqEZpWl-XJZEP78S7TZFmnQB8igKm8kXjRnPc38U7gKr1c5XO8zh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5TDcr21w6ldvFzRx-n57JOKnPcCeuMvJIB2xE123eo07k20ZaPMH6RPM306BOiFMKZPFDJv74NIyLp4-_QyqCeIPOi0q1rseH3YteXzYjZfEdhKlSIbFUiCL1iL-CLDXc-Ne1E3zxHJJYSWUNmPao-m7X5j3uPJOs9wBAOTxLXl_Un-VCJNKIdZWiGpZ-umKho4Zz7nuspiy-WFfLqyhHL6w5QjUvu4LwnqDWbLbgcffFhmrkdBo1bv8JjTvgDXx9PK6YonFYDzDanAqn9lmrunvuUGv7TA0wmNZmyPsKlXOLpTv7tkPW0AoFIo8cJEh7EXBVuyN3gd4ra8wd-QZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GteysYpEpFyzaxrjqJJvP3e6Et-2NZlL4Bem9g_X0DBX0W4lfybpox87JGjeMDWLDo83qo_Zxy35njFXD4UOLfi54xgA8PJh9Yfl8pGfgtHbbEmzfj8Y19bsoOxhebbd24ilDqibGVbiZS3BJhmddtvMgL8Dv_SMXQA32n-YlRfNro3iv1lwYHfwTzqFO0-L9MQIkVeqMp770HlWSIFurUytmpBKYFCJ85QrMpsp3XyKh8D6sq3Y9obBNI8R27iWdQUEwzo-AxrrVdgr94fEhnocob8W9vDJg4aO-5wl3ZX2ZUhjloOjGGrVOFW-X9W5zmFhKORMpO711PAJmrJ80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMwe1jVVtOpF7UYBi3drikAv1GDm0A3KQvTCcrBxPm5Z57njH_tbEWFoEelqhy2obtgN-zLx1RX2uE1TS9MaWSePkQ7NURkNHo9lfzZf0rSTKzPQ2SEdsJZbLBkNuTGUElbyseV3CFMOyQ-ztyC-VGpVsM-gKRrDv1Bl_1gMvSCsPPaDfWX4H_VVd9VZjrQbyJ-AGfKJO89ahoNG4vCXJ_20QXQx24XCzwB2DASP-aa8F79Kjiu50MCmrzNlu1PFsz0go4Pnu64INUXESoWwE3iuDVToEsOPmQDxUgh6jRbI1O-9zzv0e7NB4xhRgBdHhksC7EQS9-ERqfXhVh-xng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zdu5UnKBRoY3tspcpbzZnyoiC3BpFRnmBH3EW0RI12CIQkC32YJdQdWInCMQGokrPODAkBQQjClnSb9wpcPzGqLyNp1N3ZgvgHP-QKa5AZHneqvH_bzqUWvTmJRlf7ddNtsKhWjj2SY7_7Quffk_2t5pgq3fTWJQJIeYT5MJftZknbkWojYbLj7WXbOdJbgV8Qfrp2a5lFckbXdNzGOAg93QP2R3uVaD-5fDSoHdwMmJ6dhcTxANuXoGY_A_S6YVE1przAjHMqPeI_RMk1P4Rpj0UcvPVsbVodx7z2cuGqujw9iQRN7VKFB2rbz9RZMO2dGUQfFTzcX5pPuBZ6iIWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQNjjb4NnneZAN15cjfgeDUdQUHO2NZ7U2aGBUjxV6_EBwOxXP9vEVZP23wiCWkQhpbgfxTQjAWj_8zSsiD6yMzOQmsSH2ZjNKvvIhc9GJQlXY7EJqiR376q2R67ZcJWWWh7rqRg4x00tXYE8JBTdIBDksPkJPpVu7VwXCOgYN8U4rKJeSAFlJKwQwoYEt1r4JS1gUwx83JuLfAtIhS0pyexM1gG7bubZdpKTK6rzabEb2e0riNS6LIG5LjPEzkbRK6WfLkG6vz79dkGlFW8Fe4fEc-e9_gbr-twdsdHCPyJ3AFHBZfS9ljqKGzHOnhsH2ObeF4AsR1ivEIXeM9Fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTAzN3hdAHRUkqzj8HWQJvFq8dU_YWyCVog7yFmEvZeCM0haY0pe_nGRFMJDFQFNlUGUQ5SQd9lt4n09PtrDJ3eAql5hUOxFfG8PJbIUTZ8sOdx0agBIlLGSI9zilzI1sRPQHk8KWiA_8Ciw7uQs128s4OhMSfHRhCHYOh6Vu39Gs65Hw0wTPlmzOBu18CRk8qLJo04kqE2d2-WV3a7KJcUNd9djZFV7zJziNhuLc8g1NJHiOrCXOoB5vY1Z27wnXR_kQMvS9e6G5-NH0Dw0k5hDNjNrBWwXd2apcl39E9EgGpfy-VZNq7JODh5VpxhO6ksGXbVjjyLRF9KDsAheTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrkL3MmTVeZA4maPMoE50B0gkMGec2HlQCsikdVDC4gPWg79jMskHoTXma1cUvmSuiUd8IVAsaJbWWL6TfFB8JlDLUzjRGnpUhOWm4YF3GWTDs6oH2A3PKXryFqbCoeEJzN1gP_9ho7KhbpAiFLNMfly3rCaqWwoXxOhi2FFSifZlQKzZA8VVVtl7nG9BOShvaYmfXVsDpTcmamhaaIt01Tf98G-KQ7cysB0OfJ28qGiIT7AhE56bCilYLVKaJsVwyxuAS2MRC1WHv0kOaUpc-48fjKJct4FJdxEcFT95CcWHh3wdck3JHQmkcVTd5O7gwkj7v-U3hB_DXv4W2oqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3FsdZL6c7SFHkr6DBfJx6vjPXUHfA3NincTSejlcryC-qGoSbEHYQvcci6pg-A2JW0TH6pjVBg4-1YNw_YPoBGHI1knmFlidbmQH7GDGfyTL3xNmcO_KyX8b40VRRZ2niot27sgfxUasMYsDoCuODd8rOKsX2j1YF2VZsN8G64fmdnsEsJW8oTvCbo8ccSuk5mrHkoW0RlIwuygRP7JzO3vh5NX3yVkXWtJYqavlHOP1WdhN21Gm8UZHNTwbopu1RzA1YFvXbMwxnUWCUC5x7BgFvAZ1D96u1XkBpKsDS8YiS1IDjbSvkb6DdOLaY_zQCLQipGqRevajbSLe9ibDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeTobEpyMEFl0sDvf-5FUTkKMCtRzpMpy7EwqQxQgxSP58Gxhgr_xpPD0EnzDdjpwUZO9gS12RG61JHv-PPBnLhyvihrHD__zjJeINrnEi-0P6UZA19Zbm7TnlhewF2jJfN3tyPcmS3JWEtkVavHGfUDuUWkyPCRb0MonZPksPadwcevl2q-o2Mp1MCDaXX8qGjROGn3A1Y1L-1shfD4RDr7zqPG4-83sasm-sUo6r8P9YWZho07NlDtbASUkAf2M6p6BFLmkMTjmI-25hV4zMcwmd4kkbxnZnQayBBjNZyhzDUiJUAm_va9h_Ac7xrTS0fwza6FPi1X_dOFieqhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLz6T3D6wnWmziakNacZNkegacvtjMGQxLoPTeGj466nD5EM9fbAIkUPnApEIXzSphJIIKWNGp0joAD-JhRhyn1HBy2ZyDWw1rV1DWbfWmq7Lto5kz0AFFJHyDJKGEoX0YLhYqxIXkh_8l1OZFW3f5jXirQAviIX_ck3Qb37sHACOKEOUC4n-I9NVeRDCWIJvLHavdcO-qPn6k9VuLyzIEQQ3IFwmnjBBvPyDf72bPyNTcIDQtO21iPa5CH4EOVui_8mpPzw6Vu7_Ohhs3f0ASXGQ2YxMaLUqw5es7MiUT4KdYM_6tNkvx0hIj1gJeshs2f8qv423CpwMSS4VNEpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b74c0YoWU01Aqa2y8-Jt8Wm7WQ4zUVEEzanr0eesdSuhRa22k3vHL4fu0ablEptlCdHWtqOsciCSIuZ9do5t10dckLm2yAaNuGd6ZZFQ0Oel-L9gFjkFSakqq6Nfh6NLS4TrNFRCCJaBNevVbYpMO9yNEFg6Spa_gBjjI82mBTK53lY5bIym4THwIlAm9DN4gmvyocHpxf--0DnaFmtfRSjJzNeX5IFkibknCfyVZR-bTia-wEyYrlLwmlSvnrGNwgtrKzgeebb67W3yuyBHR7AmjGZfXnQcLgT2J78CbFvC1ZVzl-7l3jmg_VSk2yvNEbyW9Qequ1ic3RL2U6cKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BoWwviJkQchwfBUdz-XwmImGYG0pusjBthGAGrIbqRMQGZ-4BT9LwXUDZ4POQMUxT0_trosH1F8uThTCTVOcxg1eOUjvF7r2ZgpAd8soImBz-HXg1dX3A8CnCBk7dFn0BZBHtKdfy2qnB7XaiqN2R4URfdCuvL1AapyYFUy42E5JXkbRvQ9HqXrQfg1TXtUbGG2b26718SjI2-yvNaIWwNAUMeopeyDDisys7G8QYPU7AYLvRo1rAag3DVhYWnNLSVKTRgr7xj6-fQBtCU89dss3wNOjaw47vDxmpytwbF7UTy1fYkqZi-IK6UET7Px_fplLVRtZHCcHlVft2k2mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhqlrIelG7BToxGj5lDyyiAB8YKCCN-MZPdBoP_H_h8tpco0gB8-SS76CMbO8f6_5fBsHOlwUdYCoRsQ7FVjbtFcVj_p2W2sWR2oKV1i-vI_9GUbFhhR44vZEL5kKoSuitQB9fTDsfEPM7U-P0HN_n8dTIs8BdeyaZYJU99A0W9v5k4TB0qffLypGT5kgJfKSLXWgQv-6nz7QC0V3gaNfF8IyeYtx4Sg-svsgRinQ3GmIfwcPgYkeCHnhu_DjLwDIsupqTGNhFDIEHK3qFnjtKeFYXyFdbQeOOQTkhPIqPc1t9onmZzQI4h9sBETqLHsG6RrGZFu_r1QeIleAVndkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQtxL_nicG9U944JxF5eRTZTS97R1wA_wDkhX-fwwoHkR0TPCCd-13BljBaGGdHrVSIGxqLO3mj7pDBK6hoNalby2H5nXUJKByxQzd9OP4Hyxy0IPDie51djPtYjHGbOVzOs_VU5QwPAT-OpMdaAz7Yjxje7A8bT4H1n4Xhmsdz_DDYis7ZGIsZrwYfv2cZXjezoXlfKYtU49B3bNa67iBsGzh_iOOjydey1xMzTR6Cn0365nMPv3vbS8Ko5-kmhMgusnamCMX_L-kyERhGnsZBOhAKgpfHpKqUq2X20WpaBlB-qnQ2g2iRo54OAEtEuV0R1hHiAi0hlB5_G71YyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KEnZoy7PEQTkk4sg57nquPvt7wbo_ZT3jrNtjyYwe9UYDoXfe8MS3-ppW0q6gSHHix4lH53d9T_5OEQfc6pbYRL9hpU5v3ZrfoI2SO7tW5ccyk_zAJ8PCUN4S76oSLeXYDjAQ0B_tA6Crk2QbJNCWivaW5Oikr3qoWR5MyE3YjYQBUcnZ09agpsOreZJ9USnXALG8M3E-GenKMMFTS-RrUtKzfQoUhqHDGipm27uXzvnzkhvFoBTwBWbQnCn2IUNOi7809Hn387eL-v-YOGnOSE8oRIhFlfr39WCuVwtab2w4z4IVh-iS_F4xAzgH2Xdisq2QsVz_tlxQJE1A_BVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=YAr5oQ5PXrFRKujtpoH_GqtD8XuJ6FhzZt6RxSNPB90FNby4P-13Q_vRPfn6WtRD07KzuSZkkQ-9wh0GwwR3mel_9IIKNe5EAbX9c2sEgE9Yr-NADVkWnqN8JTyBxoQnYtHEKmAuh79kXFy_TYgjxrjRI9wbMwFka4hgJuR_3n9I5GS5nQ6ZZuVafcCKAuBJQmHGp-F3HRH8WvHzQyrVQbnQlBxWGNxoYDGNM2L6uIfJCfW8mrQPRJrEQVCraai-ZjE71b0_joWNZm0Ee5Lm1VkhIqwP0Ri1To8VgwBBGhkA6BpKnSAS1iIQZoXadqSpX-mdmEQDlnlQFWiI_pqKjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=YAr5oQ5PXrFRKujtpoH_GqtD8XuJ6FhzZt6RxSNPB90FNby4P-13Q_vRPfn6WtRD07KzuSZkkQ-9wh0GwwR3mel_9IIKNe5EAbX9c2sEgE9Yr-NADVkWnqN8JTyBxoQnYtHEKmAuh79kXFy_TYgjxrjRI9wbMwFka4hgJuR_3n9I5GS5nQ6ZZuVafcCKAuBJQmHGp-F3HRH8WvHzQyrVQbnQlBxWGNxoYDGNM2L6uIfJCfW8mrQPRJrEQVCraai-ZjE71b0_joWNZm0Ee5Lm1VkhIqwP0Ri1To8VgwBBGhkA6BpKnSAS1iIQZoXadqSpX-mdmEQDlnlQFWiI_pqKjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RTe9-UZ4c_0EuKw5XLbzZPIbuHidkdjdiqJYoyl0Mxx3t0SYpUCrXDIMP4MXLjZbJJI58FEtlBNLKSlpHInMOE9sC6NyWLdvhu3Gop5q1riyiEZ55PFah7unOjcpLe4g7yTQJTu-Jadmk335gFhz36t1_KbqWYjEzNvAEB7iOKKwL2M1QXIWiZqFk303Mz4iDnDiwNZ5VjXJIeSHSEXzcvNz_rq9834BmYpKI2vrmtRsMeOm84xjRwtvVFLBoX5rr5Tt4ptdV3ZuwN1SG2jY-5tKBSaVANyD5rh7iP9Bl6s0iohYVHhVc_LET6sEXMJsU3IVqyaWLKlD4kKWIvYuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KA_IsWEq_KwPNVeS3m7x8ef6TLSSYBie5xd7RxqDL_mlFRtb0eap5naMbYCvLz6OGbDd9jClN6kXucVFo4841vDlX6WjZfuuJXZy8VvQDu8t16ErcXrUdbvM_q4W4x-_fHthjXBXZVvq-77Z4c9kEcKRp6biuvDhGVg0w96WhoKDPRyoe88ArUBcJzpC5ptIyMVBHW1_bZaOop7F1WQO0bm5XzsxJjZ2cdqwdSFQhVBkutmTgFAngZ91TqLa5i0aOWFVDG3_l6M7X06-c8iEsNk1PhTSYqrfeIigz6MWUoHxpmK2FzTlvF2adb9xI6dStplQsYDwVjd_1DaX03uDWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=LQz2O05nH691kZS03RTkvKXafVdneAtvISzLqwYf8D40DB5JTKnp903pLNNeZQNgawcd_ebuvu-nQBXAHNivoWBTRSKeh0KXNVIYT0E4WTvyq6rmveVuUEhuzjKVPWrPBMYEFpJvDPzcGMqSS96wLXJT9vun8VzfGd8dtysbRsetBO7cJ4wtn9ErTOY2UaBHAQbJgovIyEt9woOn9SSxUy6_o-bGF-Lh841pMzKB3I6HyPRob2c2McpbGQVcaPxRS8eIxC4362GL1dmKurTJ8cPV90M8Cz6bzwiY8kOmFw3vU3SvdhB8SVSJ3tW8zz9DXjv21NOsK7zdwdvNmOaN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=LQz2O05nH691kZS03RTkvKXafVdneAtvISzLqwYf8D40DB5JTKnp903pLNNeZQNgawcd_ebuvu-nQBXAHNivoWBTRSKeh0KXNVIYT0E4WTvyq6rmveVuUEhuzjKVPWrPBMYEFpJvDPzcGMqSS96wLXJT9vun8VzfGd8dtysbRsetBO7cJ4wtn9ErTOY2UaBHAQbJgovIyEt9woOn9SSxUy6_o-bGF-Lh841pMzKB3I6HyPRob2c2McpbGQVcaPxRS8eIxC4362GL1dmKurTJ8cPV90M8Cz6bzwiY8kOmFw3vU3SvdhB8SVSJ3tW8zz9DXjv21NOsK7zdwdvNmOaN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvrHuRM-Gx1eLH2xUc9WG717I5AK0Vww-nneFVmOprmkKSUEdzS-Mn_hkBY1IwUwL2Zzxwrivcb1SF2R5IA_m_G_1s-s1I9NEkQxLN76LlofeecN70owPjgeByKDUSn586tWp4zCagmh193wwG4RujEV4Xa4pOTXTBIQm8cVJqrKPvNIkVRDK8SazbbXh8DoDOWP5K_d0-BswZ74j3NnDz_qvDxbENN_TXgWRPbU9ALCUswOZyruF24f8hCZVIQwT-m8AcEkh02TyKFJDrM01kicoxBjC_BY3izIzXlatfByJMZxuYjbGx7uArxN5wKnwJ0eubwsJUtFbCl1DEy35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bja4MXyIvyQdrP8BH7gw24s9xPBNuRA8M983j06TNsmiQRNb0otKaOtyPG7VY-mKZTKavk65DFzefcgcPVkC5LXGssx-ez203mhyOn9zH14Eioyd1FIY3j8bxftmETX--tb4BmSbjSeZ8Uf8-27PtBnaX44URIRDmvgeXMYbw7ebugz1_SGcE8diEMmq37eY9C8rNiEIrkeqC51Pp0qXKGKwMx5ao0uEt_2Yq6hxIIfmNfjwVNx14Jpq-UkhRGHvCFZvy404HGAVQRS22XAdQo748ZypvNbq7tNWtQESPUiMJC80xEz22KOhJ16lPRNp9bVEZ3foh2vvejmKXCgZWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP4ic6e5XFvxRdoLtO5Px5-kh7V-qqHTex6OF_iNpO7M9oUn0mRsxa9QA_Qiu5sCJuMgUuY3A5Dk4jLgboFIcQ9BhGb2ncR9QdwRyBbwMHE2Vxub9XBtz43U6E98RlGPmTyHoqf8prjigKCwI8A_fwzOspTm7n-U9oati84bsIrb3NZD7cKUyXMIFoGHMpRzXLbTznh4_UO9XuLxUaOETcj529Uw0apcY13AOgNCLJ91nGQt0C2XcOL7cWlqQbBIctIXrfEZgR2G0XVeGjgYHJgb-wzSFzSnKth33bixKZPk73bMlQUOI9DZ5328zvFeCDMaf-D4jGU1BAUlktisuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRb6sRiwe5xWy7Bx5IQPA7_rFDM-AP08JnU-kKyr79XOvfKGrb_8ONtJCLJnZDVcnPOun2-3KfL2WrPzIPZgg7LPqkpodlXm8okDinH0PilryqTrQpmp4lW1UFS-F5B39Egj9jscUEmjAkT05JQA7v6pk3EDq9p65uRFLkW-jJLym_HyXMy5cKwi_lGxSYVjIZXFENBQj7riELCN1T68S1CEUto7c9rsRv9LauQNUuguHOZNKukiasvepj-kn-JErVJ_cazWyNPq-p-Z7z495mqcJG5jNb2Gn2P5Z2rEgJAP6-m9N6uk3Ynl5PQ-rLYpCQINgeM24QEDVF2pU2ayMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OvK1FvQ5foJCRfPbnp2AHAfCnFvclZHHVc0-NrwMt2USPgrwf8eMdQD0z0B77snGk10-H6vNIG2cDKIdmMonFMBMV65cd68q-v96moEJaZIdApKpGIe8si8bWhLaLtadw8opouVQ9z3iOLcHibRgzbTrxh1CsYwnvxBqaN5uNdrAaWqvVv7I3G4RlE0Qis_RQ_XNraG3G5yC989RUWM6S-XGrbq90nKJjHWwGsNTuNbQVHlFDx7gIcPAq4VOB247Wnf4jqarEukG9vTMtiVvAInB1W02c8PIw7wedfO_xd4s4YkgGvTVayYaQ3GPeC--rmLIr5Fo9fM8d4RtraJgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d0qeXoBdHyNmk5f_Ss6S537YBqVdDmH8gkb8VT8bFT8ICWmusLYacw0qOTot7tDtxe3GDGzwppUgjO7vFFQPHgzTfpmAdqm7vClcMejzTXDBqgeuSPDvO31QfWIoa1H5TdQkJB4yv9g5eC6j2R41JTYb8PiaW1fmcIM4rDVaiohoOBzCAdLMHXchkOhsAqlAWbNAanQLQAV7VMZG9LcH9fCq5XglB9KcaINF6UgBs8c0f78JPU2qFsqe7gPhpcQEnyGPmKmFZlvcrhcBej-CjKtJmf-vWGxe6eloIRJO6uBftIZGuL8Wp8ERcGRgTrt-SePR3V9cTt_RdFca9coaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Grk8s3V0OivaGqHE1PNsxL7Oq-gXsH4hVNAWXx5oYqFCxzbVAbrvf-PssniCN_5R2QKsEVFN9x85Lguo9snnb3ZO9oUGibxSpW9w_NmgaEdKRsare30CMWHsgnuXxySEPAAB-_XDaSRjg9zNNSxUOLLA9Ya-8aJrVhnbxJqEdBm0Wppb6ge-AQfHdHscKf9TeAWyLR8yYIp2A9ScQs66E58c1yoA1KZA2b8ToWbANIYLefnSHQ5vnvYYxQcw2uS82eL3jseRBKmBMNvtyyUSJTSPxtfkFQUVItWdzqR7ZyfQsu_2hteaVpPypkCsLmZvYs5MoVOXF1Vy4WhQgh_O6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnApCNfgb3z2Sdi0P4dIsbnTEN7nsg4QGUv0zPa5qIxjk_IWMbAtji0b3qhJPJwTsLGFglibVuJmIvD-0j-LMwYBRz9Qouag6BWiIXqcgn2PJ1QrD9LvEj7d1yHwhMTIss4CwaxBbLddc1PVm5q4Dx1mbkaMyVL9kZ5qQkD72eurT2sKjickA6VOGT9qL2Ny44S386jNx5_qVVz4ywkFP0QpIxMGpi_Cxg4P3cXtyqZwAC-caPVFdVZxFbO8RnLl3H0hXmlZLH0mz_LXygNvKEfHTWLgC2kSbHPHv44Qjh7XtPNGiy9lEO0dwhmMxrzsLu8CnJg8hHdSV8j4r_9p0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CAqRtOt4zMKXsBRLlIoAqM1_86bGKKvwnDXJup9FST_HG2Qvc9IsqlUigaYGRebeDrUBfbhu8j7K0C5L8jzb183DjmFD8DdSmKYDjkeu1KPUDRMeJNyLgx8rr7hnMwuQBPTstFPrcC7msfKh_CDws5apDeqHIt24VtcudsfD2vHdaK7l8hC6FZbTchFSgE2hVEOp9wJBHbvSUItaL7-n6IM86_0Thum_Dks2zj4Xya4lXuAfocIQsP0psS2HVSNJAlfbDshBTW007jQGnps7XWg0sHEYGgKBtLCdRzAx0tNydar3wz9ogk1DSjRusWFalfTohAlTE7aRByh48SYp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rag9WrASAMBOFk75jBvArcEqVTQbDwe6TQtF4LWQwrIA1HABmYJFMxHTlrGNIrmupEHxprxj6mQGxyX4TWAdWU_sitQj5sqxAESivS9SFmpKZylp1isOxVJ3Gj-x7ErJxtTCfSlbRII3wmNVm4T4U20vNwxcESNfMp4BjdzPCjhIhlp2Z0kdjgQVXty5s9GpGbRyaTL9ILl2nfhiLD_2rmmbp7C6n2Zc3GOM4REphDUrU_D1SZA4YHvI_OxWZNtPbBTp6xOn_p5HASE-36V_6JPpDJClivPyEmTQbxJfuwDkzwzv-rqeMr9YeH_DMTtfgPmwYE_7XFRX0pq_TPBT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYW-dyJIobN_QfxTR1Gq3dPuBdUY1f061KcEjGAx2m1wZz1UuEltH1C6UHcMS8K_MqmJTi6IJtaUArGg4GfSJUerlH5noFmjppOhv4GXTFQxEGowSVeHoMpsS3UMy9zAQgMBcql8k9Fnxn1GK5Mo0J_8ZwymZ5DBJFJbdXCOFEntvlyYggWbCTrgTdFQD0btE6akBd3fYyRuqHumryep_GrBJWUujnGUDl0S3cr_l7uQhQWGeBBkL9eRirKTtYshZ29llVmf607PXv68daPBQ0agYfncujfvhgryipzunJUf7VKcuv5O2F-2MRW7MbiZZS6swy27-YTRxPiNoocaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY2lGJHZH0nM66U4-hK05rcV1j1on5y2PTDUjjRT6JgvQe-JPVv3j66pVFNwV6Jdbd9LRFq4-KCDmzaEXvGYplSz5mdGKsJVpP-PPxxMO6rPnBmauGtB1XHjD2AUGSMiPcITa7XcTqSur4mTPAmYOtSe-qp_UwGrq3XRf6WKlAfDgWY844Ldepj28c4MwoKuKk2a5e93IAUjIyffBvI4v0HPV1dZH6KkO4MFQoAdoYLNrQ485Xs7V2ffPIYvmthpVUlu_B4vnlpJiyxnT56aqLmCQipGa0cAcS4bj9boqSJbtIqpaTnNaYZljTKrv2lQchfpePFvIfOd04Jtl7UVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSOy1zaAKGD0PoKC0ruopJ4VbpyhjP_Izma9hYUdJv-Mr3G2Z1tx9tOqTtsVw4W6ZZuaTnvRA1vdY2CTK34nYSuihPoB_cMh1SXo-hECkjzTvLCiUSOqEBJjQTqNGk-vNF2w9gPWGkTo0UTqyZxFNuz59DBEycBAb37jQLaqCv_gvat6zjTthOoCwzY89L6HAtSi1qGDCVAgJvJ-ifyxE5hISldUQKhkQSZiCFxR2ukJxCRBwhh8s9MmIRRbHOHLE6cU9s-FhgLOtv9RGxk8cfJ3GpRKqijg5Yzbu6DmQnRWq7ItzSrA6_Ja_Nm2Y_tIramVKeniWbaocbaZRsgnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=dDOY7yDcTbUhGvecnnEGLJ3IaNXZ-yBbuCo4_-p8ZrambeXj79c5FUqZLTh4KBjAmH71dmnS_NRA937pU21TNCh_JPLgNbkjAoQugzK_hIwwJQVCE50vG07DMiVuAJA026cj6l-E6Jop1J2fTYhIrtefHyQZAit3ZsnbUCwMXlXLpMBXOJjuzVIPvdcqdqrwd14APAuGpLN0WW3WpfdaJsWx0IadMlAwpLRHIVhGQ8Et72LtIiijuyzzgDELOXSi102UySr3aeateAjfsuRQGxIoXBfQ4iymkQfPPwynYmLUA6jZPHI7icDt9lF77SNb4Mnr-lZD-tT3L5uSFA065w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=dDOY7yDcTbUhGvecnnEGLJ3IaNXZ-yBbuCo4_-p8ZrambeXj79c5FUqZLTh4KBjAmH71dmnS_NRA937pU21TNCh_JPLgNbkjAoQugzK_hIwwJQVCE50vG07DMiVuAJA026cj6l-E6Jop1J2fTYhIrtefHyQZAit3ZsnbUCwMXlXLpMBXOJjuzVIPvdcqdqrwd14APAuGpLN0WW3WpfdaJsWx0IadMlAwpLRHIVhGQ8Et72LtIiijuyzzgDELOXSi102UySr3aeateAjfsuRQGxIoXBfQ4iymkQfPPwynYmLUA6jZPHI7icDt9lF77SNb4Mnr-lZD-tT3L5uSFA065w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maP3LHA0aIcTQG8a0RKTqo106If6_Zn2XUjY_Dj4xkg4_TVLnYL8Pvczpm8RoKmwQFmL4j45O39oSRbyPR_eJdgG-_NAaYdww1VRuIu27PZdmDM_CnIJQJE50uyWzmtDrYC1eYS_px9RrfEImyLxjH6r49ONZfSwo2-QXcUVOp0HO7rs_tLHbR6p274ODYGwul6Mz0WzJ2f7Tc90uy4KAQ6BG2EnrgH9FKt2oSPSt8dwLR44L6HsKbWlAR42R0ekzBCFeRXju_-6RPfxrZSosyM6oKjG0i-jhjZoHXp0J7h3GCjjBvhUfEjxFmVQ4CVnwcJLfN3A-wR_CwlZGLe9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=e6bk2vF9CELeBY9v0iRw-PjHfy-diAVsZlI5eJBHvHoDkA6vKu5M1J5Y99kpwFBtz9Wjzu8zojlkrOCYMSW1W2FI4lsGjMBDcI13m06jKJeV2tFJRCdY5w9HAU77jmM6xVIP9ApmPDLk38AJRi9F0XA69PWrKqcqMt-TOGdUo48ma9W5AntHFZUl8pHNG4uQjeqANYVB4V_hO7uzzNbD371pCLSAxFJyhYGuYJHU3lJ-bGwG5OHTNbJgJa6vZjgelX5hLYx0IrUBfSjoGnCBLmutQFIdcLkbNnNMhpmhb8IuQRZ21ZMwiAZEm33OH-41CrROJ9U1tWokVov5ruayzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c6ec3cef6.mp4?token=e6bk2vF9CELeBY9v0iRw-PjHfy-diAVsZlI5eJBHvHoDkA6vKu5M1J5Y99kpwFBtz9Wjzu8zojlkrOCYMSW1W2FI4lsGjMBDcI13m06jKJeV2tFJRCdY5w9HAU77jmM6xVIP9ApmPDLk38AJRi9F0XA69PWrKqcqMt-TOGdUo48ma9W5AntHFZUl8pHNG4uQjeqANYVB4V_hO7uzzNbD371pCLSAxFJyhYGuYJHU3lJ-bGwG5OHTNbJgJa6vZjgelX5hLYx0IrUBfSjoGnCBLmutQFIdcLkbNnNMhpmhb8IuQRZ21ZMwiAZEm33OH-41CrROJ9U1tWokVov5ruayzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روزسه‌شنبه هفتم مهر در جریان ضیافت نهاری با حضور چهره‌های برجسته فناوری و مقامات ارشد دولت در کاخ سفید، اعلام کرد که واشنگتن رسماً عبارت Artificial Intelligence (AI) را به Super Intelligence (SI) (فراهوش یا هوش برتر) تغییر خواهد داد.
ترامپ با اشاره به امضای سند رسمی این تغییر نام گفت: «ما همگی هم‌نظر هستیم که این فناوری مصنوعی نیست؛ به همین دلیل امروز سندی را برای تغییر نام رسمی آن به فراهوش امضا می‌کنیم.»
این نشست مهم با حضور رهبران ارشد دنیای فناوری و غول‌های سیلیکون‌ولی از جمله ایلان ماسک، جف بیزوس، ساتیا نادلا (مدیرعامل مایکروسافت)، لیسا سو (مدیرعامل AMD) و مدیران عامل شرکت‌های متا، انویدیا، گوگل، پالانتیر و آنتروپیک برگزار شد. همچنین گرگ براکمن، رئیس OpenAI، به نمایندگی از این شرکت در جلسه حضور داشت.
در سمت دولتی نیز چهره‌هایی چون جی‌دی ونس، معاون رئیس‌جمهور، سوزی وایلز، رئیس دفتر کاخ سفید، اسکات بسنت، وزیر خزانه‌داری و هاوارد لوتنیک، وزیر بازرگانی، ترامپ را همراهی می‌کردند. این تصمیم در ادامه سیاست‌های جدید واشنگتن برای جایگزینی عنوان «فراهوش» در تمامی اسناد و مکاتبات رسمی دولت آمریکا اتخاذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNRn79bS_WDZJNSjtZ_MmO-ykT6Vwx1NUZvOK-sJRGRmUR_xX8vx1_xqbTZlUJk3JiKqjQac-fgnB0R2Z9W8ey7SfrMwWFleZpDZV1SzlS9Gp1RxYog3ju-KTliXUludMqap6xbV9FsjIHie7W774G25aRQ1HrGh7fgletri_VVjFnPwqqj6zZMmmx2v5aeVfJU60Z0DwopNro76yPxCfK-bLgKEel92PjoeqyR8wcrES8DI6_BfWx1gBGa0wS-x47gXOB-MdRzi5mXb7CZoHje8_qdFP5wfR648isID-pNwURUtXIystT1HZXUYSHaBqgQcENjWvVpgtYjMaeM-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JmUUP7qVivLiNz9AnnaG1JqN6RbdJWbvwlc8FJ8RJlNB0ByQFotMQnkeY04mtu6qNeZxcWaC2xxNd-VXSsECDWfJWGsq6kXXuIzBjdoSz8qXm8erjH0515tUODk-EFWGBYPOTACvTAm5xadFRdJjsz8q9F3iQ2aPghpnek-o4i1pA5HdVOhnhS83DxE_AGthVdPXIZkA79ylZeg93XgPOHGeaMHXyNvzCHusRbSQwcN4rP9bwPwrP4Vu_VzmEDDLWHlL9n6FjgUI7bnP6nJRhXgP91j8UkXM8DjmanymyQjJNbosQSbpSnwvMVsjiut11a1ILnNhtFCdi7zB67R4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=Y2br_XOqqqiEytnblHsi8vGMdwLl2a1Q3EwT-3xPGbmsDinqaAL9o-bnWeA-A2BkWaJR6LCsoh_kJOR_8N26Sojs5GNbo7F8ngA7AFdPRiiTllrvvm71WEOgrUDrQrRZ4ZR3_DozPOD0vspFChRjBRl8EptKPqPjcQFaXh8LOkF6wQZMYSK56HW9Q3eAql8saj9Uk69wQKj5VE3FKBol6pkC8UebxzvTB8CT65KmFKq_ZZEr1UfvcQm4XvAC3GcqogrNoYg6owe7qufMO5PKZ0iky1H3BrptuQqeezudtZ-_XFBeHkvzfJpSzUT6XuYfhXas5YkFvVr0bGYwZbb3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=Y2br_XOqqqiEytnblHsi8vGMdwLl2a1Q3EwT-3xPGbmsDinqaAL9o-bnWeA-A2BkWaJR6LCsoh_kJOR_8N26Sojs5GNbo7F8ngA7AFdPRiiTllrvvm71WEOgrUDrQrRZ4ZR3_DozPOD0vspFChRjBRl8EptKPqPjcQFaXh8LOkF6wQZMYSK56HW9Q3eAql8saj9Uk69wQKj5VE3FKBol6pkC8UebxzvTB8CT65KmFKq_ZZEr1UfvcQm4XvAC3GcqogrNoYg6owe7qufMO5PKZ0iky1H3BrptuQqeezudtZ-_XFBeHkvzfJpSzUT6XuYfhXas5YkFvVr0bGYwZbb3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0umHYZLJhCF--OpirAsSzkCg8mW-C_LhzBhoxmTG2gxXct8QheLciDQ4vWzU3qY5p4pENXOwAU0gC6YANkf0kEqlSF1rHskkfM2EpK6kb22aqM2h4nPzwUFidbgQ7r_81YHFjo4AZpdAn1I5jB9m7uQu1P7A8hmyOGeAoPPkAKub_IQ6-PFXNT2yb31UyO_PXldBYFK8hLt68txbrsHfGSgMfrRlrm7TfV2RlEIcIA7mNixROZUahArnWRVekHMUuEiNbyMC5t5OI7ssH4KzPwcy_Ku5FR6tT38gsci1dYQlwXmQitd0rHtIr5-Th4uVz1uqfXLnWMTteBeSKkArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPfClPKFaG0Vg1favSDtlyVcCXSSIhbNjh2dLBV4TtcHZGXsBxaR2sUWuQiLfAzbC-XwhwLzvjoTxu15sFZka0lA6b60omLnLmkYbozVJLGZV3GicoX1EAcODUuEKwcke1KjGKx_9dOJpDEN1MW2QW53lPuBopiBUCJvK6wKxbFQ2cNPpc6UQ-6yPzRgIFWrM43b5H_fjw2K_970qdje2rzt85mv50sdzJpErRNskH6fT0K6Z_cam-a8FMpy_tlM4Ye7Ajvu1_BZLnAzthtP0nNdo2otEUTiptOB8lHw1HAkw8znrctBYH448dbiPmjFXUoESWiCI3V7h3PWLfyEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Db1uDGtjzm2Pjm6Qp13DMb8Ztf84VLGU2Gawr1mfwl3NzVZ1h-Wk4LdsXzGrH5x3vasqeZPsRYFzCc1070lG92kW_Sx-E7oEag1p7WQKBRIlLAflpGlkyBj6p1oXd3zpD6FAEzTMm1X7jtFavCzcOtIsBYZNcs061M5x-n7ixQLyYi44S8Dvxt18C7xtWLG6nLDGtvoaI4cOETwKVYxyGNJk-D6YDE86C54s_jOXjWOzqgmKP4mNfJJ4yQtfJtJ-gccQMAO5vB8SQfE06Yrxc_t062FaItoq22_WKI4m1LRDm0zl4tk-lQWUzBjMNYXrVTb66juDT4twPJy8SwIdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5O3iESObdC7O269nGLW0bi7SkvsGgkdM8ZjHjqXQ6mLkVbBjOZsYv3oqz-Nx2A11PYQT5hyWfuLFCtBJ1m7hHZUUlWpvKbnLqGRIvjEEoNuA373Vow-0KjS3kcvOqQ-Pyz6SQXTt7d_JZI22zAvUULwQ4C7d0omBsz6azdL_bYgeYYwKeJDn8tQe6UE9UunPA-A6AWw-VO6shNrr4cXUpcdUSV2BkSRzlw8SHmWwIm4nK6H8bOjr4QklwnTxoAhHda4PI1b6Ldtx7T02D6Szuns_dxlsqDPNAm5N-17Ore9VOl_52sbzN52Xzf6dTX0o5n3BkINSxb0VXqCBodnrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwd3N3H41sNdtuvIvLauk18VI7Xg_a5zEwx-eLyRbbeiVMwVgU7SNRTxywhOW7yv8fDbgapzXEcZwfYjaaXgISbTP-Gsf88f30xRmFa2jm77kkPsGuHXcn1qILzQQCVwCHBjcEnnx34z7bsmZoyfm8ZRQdyRdWIWUogzozuVLxOX9SccF5-mdUNXVybthUiKDdoMMarLEcb-QMiGAuws1UVn2Cgs8zsnc7-f-LPlgBb9d_Y0fxCg4zebB5tmsH2mZRWowWJhZIFu38PZec5VeuEx1Wtm8Tp2xf1mfcjor9PkqYzJ-QOn5V1pu-EE4gduF7KYV5O0GdExFqx_FGiU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L1j3gO_yMzoHhebnbp8o8fvxkdT7XjBjcqLt1qzN2E_GV7pLazjjxGAOZPZyXNGLJvzJqOeb7We16B_yuGJORQ1uGko-1BVOZ3NUbusYG98dfLNL7OMsZnIA63pjmtl69N0WH7Hq6Wd5qEOsnBPtj1HK84cVx9n9CEtLgFj-1VCMK08dsgF9rdlK8Hc0eLDLqmQXqZoKPvtoCS239igh1sjvik0Gll0F5NwQtRrHflquKSYDgNdp84MraCijQQPpSMlqRQ7L3EUPHL1sv3RhwJSxyPsCMgehFLu_-yS1LGQJa7tdh7AEANgUvIB8pfzesuXhw19uI19kmslJ202t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OF0msLzdcg8bzPP6gqrwxJ8QDApimbp0eU0WRiY5AfzAvTzr7SzyA7lsjAknvw2Xp9tUDcFj24g1ErBw0agRuFbkJfT2dPskr3gr1YbAimouTrYTikRzYLUn0HdwI52TbRvEiUDm4oLE0XHtkwVVblGXm0bEzzqNd4ioE0NKiipmUaFGZATrwrujFq2iptfIAHQTrVNQphwhiuHZtfZlinIgDYja4Uqp8wvbFPxgT4bWjYV3B5J-U5ZValay5sacqj_P3kYL60e8jV65dn0Ew7EIAgudhlEH9fC2aNU02aOpZfLGcgkPDdRiLPAJ_5Nf74w6-mIGq1DG5IVKyJJCOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=io6OMMb18Dcda5IcB4PizuNTAWoQDUozTMqEWmsvHFO2UDFu0FQLUOIyYjrN7wKKapFrQtkQ5bdv9iUmAfIbyOBsuIKvSC3qRqn_KcXgGxcuuLNFEHUievjdPDvm_S1CYUObAC7rRSvN8dVKa_i7100yDtgdglr7t9Pq1juxjMk7ORSl3hpxAnL2kDpIfUQdAeKV2wnGeW4dNyVoYJr9X7TDYVCa9DnLj8r9WF4Yl5DK7cX2Uwq_0unm8Ab_at_YFkNaMNqjm-g8yTHAEs3Kph_lqrF4JWaCSMKBxcFUd8h5FH5OXOKSAcD_G4xEKpgXhlhZ8uLjDt_9dNZt4XlkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=io6OMMb18Dcda5IcB4PizuNTAWoQDUozTMqEWmsvHFO2UDFu0FQLUOIyYjrN7wKKapFrQtkQ5bdv9iUmAfIbyOBsuIKvSC3qRqn_KcXgGxcuuLNFEHUievjdPDvm_S1CYUObAC7rRSvN8dVKa_i7100yDtgdglr7t9Pq1juxjMk7ORSl3hpxAnL2kDpIfUQdAeKV2wnGeW4dNyVoYJr9X7TDYVCa9DnLj8r9WF4Yl5DK7cX2Uwq_0unm8Ab_at_YFkNaMNqjm-g8yTHAEs3Kph_lqrF4JWaCSMKBxcFUd8h5FH5OXOKSAcD_G4xEKpgXhlhZ8uLjDt_9dNZt4XlkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vt_xPmcPSj0gcGtJpOJQU1peASoF0AlNH3xjszS-10exSSgXkJyoltEROtqVmcM8ysrVZy0Up63zjsfrbSeU7DZBpHnIDZul7azreBUk6NZ5bDvXBEPf_EWlL_il9DyiQGP29Q6S-DqvIo392GfkwO63bqzH5wt5hFxlwaWsyBmaMa7JgRdmVGarFoOC3gW70kWWjgp-cs0y-0gs0GM3Hez0IGocOSAvbhTWKtSQ9KsWuAf5nc4TnDLp_11fZw1iaFEqy3uuJe1bcO83jWZ7w-awlWx4Q9-D-eKMDLYSgGxsxTAVj7Q1takvFq3e5M4mmIhQ4jSrhfNAZZ01CtYZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xw2qYuyNdkr-FjOZYpweWc6wcKiZNysgN48TEb1-cAj-TwOifbfDBQiJQSaQhYpWPY2jLltRcO1Dy64SgcYVhTFO8NY6xP104F0bmY8fePC-z2o0j0bONFcrjCEMUyK9LmNBFKv2tuu4sWWhvjoqZHWeozlBi19B0DB4WRaI3vbi0DDQkD4A39D5C8WmMGPBzvi9rRwsB2d23GwFAmtiro-fh3lal1EnDOy09jo15MxRLKKaIKoA2SJwmeobN1hLEwhnPNNFk0vx-0wEozwH-0PSHVGNbPjlVOobGs21D1p5cdksYIzZgwrowlYNNSmNo8XZvmJuoEkdl1XrqbfqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjMlrOfwi-Hepm_3rbLJB3AXZpUJgUVkipBGcIiIpIdEYASZFd1zdgCWgLKJMwCvaSnEp6GAkJTMlNS9Ko7Q-_HQKRS0H9fxPftOYEJ0cNasePD-nAPxHvh7BWraAOPwZc9zLr5zkAUMhYamzhwoA09Y4JYdefCJnFQRs4Q-qVWMzDh5enQaSLlNgHJIlZnH08V1hjsQiv5U4VAFVM9bXRNQXdyabmALBbwakW4QrE2LpKLseGyxT2HMTfI_b2DpOudztr5BOCP-OMPOHMpRycVh1UbVejrihTmS33vIc9UmdXJJV39V-JSb3xoqusjD_vXgD0Nd26hbSRXSL4pIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SSacxIb4ttcJV_xb-rHP_7z8caVboTfXtBbLjAOXTLjf339HUwRbukiXFUtOgCr3tZqwD-nFBNEKkNbeOiS9k_q2im_o3qNXWst2da8ATexM9qlxE9ZPP7uo30gr9OJpsqMKG0H224jd7jVOOkrlMCAowP2SS-7nMeXR3oOHxKDazg1Swqom88Aep4nauXX-gaUS8Xw_JWutXcBSnGq8zYqSDb35UUbrE85hLybQvJtae3NZCihCMEWXfgKj5bQO829FvI9rXF802PxGTcSlyPO9UrDtkKks43X4fYKNJ1Ew8dinHWXIad1pRCJYOqPLugInTVVlSyjR6YMKNiCuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6QL6m8aqMLn_gNob_sF5FZD8qvmiVMSn9YBliO6qbtT61ElX94UD9mS8O_hHTv2aYomk7C1Pp3WArIZNy-DQNuoFAOBjJlR-b8YwHSQsZ7czaKkES9huM_Q5EaXyuKDHC9_ZCacd1LEuQVAsftAorNjmerEwj7wdpWcEA11VpAopptShdge0ires6oBZOSiIaoDb0cSP98Km1ijhxxtWmMG4wKE-SM8oBD3x7hICS94D2Gg7s2pgiAG86auDL0zwkhMZSR9xAgBl0Etj1Top_NAnLrn28CCxri3yLmRbuy9HvIR1h7cTzBSwzG9OZN26R-ShegrSv7Tpdn2TgNLfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rsJ7FiLKHKXmGg5f7fr8gznor4skJqccV4k9uXviPfbjY46nZJCpsB63fgXSSKeYeGqYruiET5M3-R1EkuAvoxunS52XNLJ82JEAR0qJeYLI8e2_OF7tsL6Mgrsdhz0XncPIoxHuYSLzKi2yaxfzGTcjPTFShFyQc2tPTtD_YVXEOS-RqR3L8SwNw-BwFVaE0FD_B4XOgYA1oM3JRYLLWIJi0cA-SUedOsjBBpEzWIS6lbEUJMIenGdnSql9HpK5NOqZGqs9DvoRY5lTC4hoBG2nRM6bPMt44QpbHiX39NQsUj-RZCt1eimuIP7tgIckGLmUBjqsOXhPNrrq78CpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cn0Qqi91aJdlrWPqpeAhu6ZlmBCw14Y5-znBNKyOaTpkpxS1NFMwY0kIbzWCfSMIq83DHkNFCuorOg5eWUBZxjDKDaxnEMa39-FB2urPG7gL1MS_zF-p8YlwIxTfn05CKRnB6ceRTZTRt3UM2QNIY6eGSA5X-O404KuJdM0l3NsMRYtcvLdm-q2F4MuR4ck-vmHkuh74B2YTNl_9jixRiiBBeFnRZeAWRraFYYp3rReqFGjuxJMM-4xUj3_xjzsJyPsXQO2EXvVxQWN4g62R-rd85o1zbpN8FG07OlZ9avkcLiwzPsUC3bDcVvqGBufMvqNI7anOISLzV9MFH5YMxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=SY3yxOOUU3q2fPkItKXSRZTXCmPV7ptMQOYOsFNTtQmJkN_PEYP4-ateFTGEKQoLFfLke8VN3pseKCSR4zqjM_SGMcody1ALTkPzWMNJ7mCD2NNlpM-rGU8WieaRhkIFiYE9QQsBHeLeyJTh8l0tMsk8_z7fiQknVBIZeMfSL4IShYK4ZVld9NODhdUSj6p_n5eKWw8BaRf4Sl06nfhTmInGCO83RJ0LDsqH7B5-SPT8L3kXI8m_-HLoZwdUPNHEjOk6xoDVZlefzuF1VkcTZC7q_rtwZcH3E3Se2OG-M89mjF2CNSm7AFW4zT4SLxBt9YPfOa5GdjVkv7fpevDg6bjBql23vNlcs85llZIRpYdRYDdgELfzKUAfUCWPAZeShhHwGEobYeBkibru897ctxB5Mjzzdt_3QJkWRPlwVIXVXIaoPxaFNQKw6Jqg8oTfavkc5ZdFE_rEM2rjENs2xnBi_O4Lgy-Ufs657iZGsxEoGTg0_sPBPUTpNittaglCOQk3GhPzM--2eu5skx0a7diS0T0nl6oKr5KA4opdouzm8xaFVxJC_dzthVgn9mD9UsV-qSR542UiSelgmP8Q0VgnyXvxRbUS7qEI-J6e3DZ4NFXKT3tbkdqef0F84AquaKJKt0MH_hwdQZbS_eC3Yjhxr0DjKJT943ph6pGczug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=SY3yxOOUU3q2fPkItKXSRZTXCmPV7ptMQOYOsFNTtQmJkN_PEYP4-ateFTGEKQoLFfLke8VN3pseKCSR4zqjM_SGMcody1ALTkPzWMNJ7mCD2NNlpM-rGU8WieaRhkIFiYE9QQsBHeLeyJTh8l0tMsk8_z7fiQknVBIZeMfSL4IShYK4ZVld9NODhdUSj6p_n5eKWw8BaRf4Sl06nfhTmInGCO83RJ0LDsqH7B5-SPT8L3kXI8m_-HLoZwdUPNHEjOk6xoDVZlefzuF1VkcTZC7q_rtwZcH3E3Se2OG-M89mjF2CNSm7AFW4zT4SLxBt9YPfOa5GdjVkv7fpevDg6bjBql23vNlcs85llZIRpYdRYDdgELfzKUAfUCWPAZeShhHwGEobYeBkibru897ctxB5Mjzzdt_3QJkWRPlwVIXVXIaoPxaFNQKw6Jqg8oTfavkc5ZdFE_rEM2rjENs2xnBi_O4Lgy-Ufs657iZGsxEoGTg0_sPBPUTpNittaglCOQk3GhPzM--2eu5skx0a7diS0T0nl6oKr5KA4opdouzm8xaFVxJC_dzthVgn9mD9UsV-qSR542UiSelgmP8Q0VgnyXvxRbUS7qEI-J6e3DZ4NFXKT3tbkdqef0F84AquaKJKt0MH_hwdQZbS_eC3Yjhxr0DjKJT943ph6pGczug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vm5bexSh_aGvnE-W65ycdBwS-3LUZWy6T75Z1twqXmnj9vCxai-gLPA-gQYhUDkWtF40-2DXaDtHRPjus0zdv2FlPbljb1e8hGfxdo8V1vo5DEsDNTceZyc7Bu6RVSO7tYMUDv6HNAJF60452QElYC1HBF5GKn1tHdbr1xW_H9tIjKYHtNkwhP4hTKW1cgnJwJmoH3QM5XrZcX5mpQRdNo2eac45px_enbY3S0HyUC83Gvm2M6RzecyHNO_Yyd7njKqftEn8zzAdewUCJasJibCV0H6PXGKUG6YO497crbNFaDpPx_m0I0ccgilk8oMNDiVcw36eN20ZKKh-KI-dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbyRWRjDr0_mANu0NGmTXjcSobJuzB6o39mEbXV8KYIPZsAr7MTV_SB2dO4CKCD--_6VqdlSwH8_LFFbRdqGBvWCZTbZtXZXNnEeqSrWtloUkfEZKb2KCApdH-gpzpsUIiNB36rFdAepx2durdX68pkfFlt-tDEBDDNdTtaKGlclDL1qD_hWgC9M_L4foTVZ1SRpGAsaC8UIh5ri26yUjERkBm8XN_UmdVlL9HopRWQ06cKmig3V1Y16bjNXhGEtvV9NjDfFJrWK0yUa64uiX0h-tuT9cMS-Pct8RksogPj_hHttP2jg5fTlofSEIYk0k2whoAkiPL51y7ybjxPvjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O0_9MAXTY2uhBGRV1sS22PFddcHt4nXbwbUZlGAySSXbzWiVu1nOi1dYQwQ1j_ZjlJysWMt2mLmQe94v3U2FjzaZlqstL3KPKWaBGEbMMlj27nfSVr2deyuQufCpRBPf-JyVprr3MvO31PLZXw42XPiAjyzAH8A9mQH93CrelKLGKyyUjhNShh6j4frlBh4rNGhVia4vEDm1ATp7L2MEAtiPpdwwc-4bBBUX0PvLgNJtsWh2Mm9Ec914r1XInpobwHsroW0o5Hcq4PdnPU4mBXXAXMp9God0QmDXtT4jcTvWCdfiGS2k13JYN2Lg4B9TdXgxDua1f2NxXqvRy0E9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=kmpMaSgxMARSoT3Htsl9xphCA8lDOE2Z44RoSgb5yGY4Jt_4w40n1d_EmDHPADEL7zwZJSLKKHogUDAC8hS9bfNa22NqQL4xuIfE1WMsmU7jBvP9DwaARP72ybeIs9a8nrBcYr-wb1Osic1MezGbySGNPyInXNd-C6s0Iz2WNV97l_wEmsf_FWxH4SU4XAl-vtl3eZs6VkI7xSu3cJTszcnQcAfdLinsu3VY_2Xfe_IPmiRDax5LNUX_eCbjCV9nbsGCaZJR6Oh8nuHgMFSQEGYy0eR3z7YuaEH7WZW9gRkMvDCubW7B9JL1bDUHSHivr8xD45ETP6yNxYPrnFBFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=kmpMaSgxMARSoT3Htsl9xphCA8lDOE2Z44RoSgb5yGY4Jt_4w40n1d_EmDHPADEL7zwZJSLKKHogUDAC8hS9bfNa22NqQL4xuIfE1WMsmU7jBvP9DwaARP72ybeIs9a8nrBcYr-wb1Osic1MezGbySGNPyInXNd-C6s0Iz2WNV97l_wEmsf_FWxH4SU4XAl-vtl3eZs6VkI7xSu3cJTszcnQcAfdLinsu3VY_2Xfe_IPmiRDax5LNUX_eCbjCV9nbsGCaZJR6Oh8nuHgMFSQEGYy0eR3z7YuaEH7WZW9gRkMvDCubW7B9JL1bDUHSHivr8xD45ETP6yNxYPrnFBFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=KLC5WPCcEoLmqAOHN61RkA2uPf757unDYvh1o_8hRoYthRQFalGAvAp3jiV7Uj5_BlcEz9zHZXIFeGHYif-FAL9qbINkh9fA93B4El5DkiWF-NJyj-9r_gGztrzB_FLE-8uvay6lpgKRGNNIO46ZCuB8KMQ6KS-TnfTaKmlZ9tkvTKOq4ZbeCR98Y8zBFP78xnBGX_qEfDnC3UsOUxc2W6w1fV1BXwIYRnqehPPh1Vu56gOVQf5Nf4bmbpdFsWFs1RZb3rF_0srgOPWhqeovwYPqY5NxQPmymmJ3BonwpCmNUeuuJgdg3ntOUeMaamXBL-Dw837Q886N7Ui5-UDCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=KLC5WPCcEoLmqAOHN61RkA2uPf757unDYvh1o_8hRoYthRQFalGAvAp3jiV7Uj5_BlcEz9zHZXIFeGHYif-FAL9qbINkh9fA93B4El5DkiWF-NJyj-9r_gGztrzB_FLE-8uvay6lpgKRGNNIO46ZCuB8KMQ6KS-TnfTaKmlZ9tkvTKOq4ZbeCR98Y8zBFP78xnBGX_qEfDnC3UsOUxc2W6w1fV1BXwIYRnqehPPh1Vu56gOVQf5Nf4bmbpdFsWFs1RZb3rF_0srgOPWhqeovwYPqY5NxQPmymmJ3BonwpCmNUeuuJgdg3ntOUeMaamXBL-Dw837Q886N7Ui5-UDCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdUS-dEvWxzfJWeZY_JNk56fxyAIAvvcmzb__BZG4VSJQIEHaJpHY04V36R-ZK0JErPMD5RqUgTYuPbODQJLYsI2ZbLHJBFbppLigIdcBqTlLh2C84Re_stouOFuSajD6-WLYNOU84FxUTIJMudBhwZ3Yl2Xa80H-Sx-vNJOtuhrTRIlReGtnwajnzZdcM2QSr8KUcoRzi2A0Q8KPWRIkQbwgY2I5raJlRRbdJFhXh0pUAuJEUteWxEmEUDLMl_2LMNgTiBG5nF_98gdGDMepp-0CASaFUQuZ0YF9TkvKDQv_WrWd7Rp19rJEXL6bWtjACYBplV9eu-eY_7vL27Miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/easnAOFzNhQrMyBT9_nO9AbWecML_2ucUgrbaJ2hpsForsQ1TVhE2ZDGIJ_kj9qS37NTDo23-1wg7_uYbFljsWdzqDWKbEBAWcrHbLRjwtC_4N3Zmyq81jqzjUJoOniPJx_C2ibg4QbUmBB2mRhjbVGLvuRfxgPaHW5J5ka9aCiQlhal5b-iKHHWMfqwWoW7itKybzVmMafoYJcBtywEKySs-BPPKQv31xMQ6Z11zile28d7LcH1Gi_nVz2KRZk7KXw09sbh-xCPBY6fF6xlvdUKYMW7lx-XajkGR9iVFCwBf7EZoOBhoNv-AFgZOpEQvwB2XGXkpP_fpoLLUVjUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارز در بازار آزاد ایران روز دوشنبه ششم مهرماه تنها در چند ساعت بیش از ۶ هزار تومان افزایش یافت و دلار از ۲۳۶هزار تومان به ۲۴۲ هزار و ۵۰۰ تومان رسید.
سقوط آزاد ارزش پول ملی ایران، همزمان با تشدید تنش میان تهران و واشنگتن و در حالی که تحریم‌های همه‌جانبه و بی‌سابقه آمریکا علیه جمهوری اسلامی ایران ادامه دارد، وارد مرحله جدیدی شده است.
سایت‌ها و کانال‌های اعلام قیمت ارزهای خارجی گزارش می‌کنند که روز دوشنبه، یورو به مرز ۲۷۶ هزار تومان رسید و پوند بریتانیا هم رکورد ۳۱۸ هزار و ۶۰۰ تومان را شکست.
@
VahidOOnLine
قیمت دلار در بازار آزاد ایران ظهر امروز دوشنبه ۶مهر۱۴۰۵ از مرز ۲۴۳ هزار تومان عبور کرد و رکورد تازه‌ای بر جای گذاشت.
اما خبرگزاری «فارس»، وابسته به سپاه پاسداران، افزایش نرخ ارز را به اظهارات وزیر خزانه‌داری آمریکا، کانال‌های تلگرامی و فعالیت دلالان نسبت داده است.
دلار صبح دوشنبه از مرز ۲۴۰ هزار تومان گذشته و تا ۲۴۰ هزار و ۵۰۰ تومان افزایش یافته بود، اما تنها چند ساعت بعد قیمت آن از ۲۴۳ هزار تومان نیز فراتر رفت.
@
VahidHeadline
به نوشته هم‌میهن، قیمت سکه معروف به امامی نیز روز دوشنبه در کانال ۲۴۳ میلیون تومان قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpFHS2Kbm9_hsuyGTN3Zb-j3_k974b0oiD6WPyClT_fs59r0pJn39PPv9d3zSkOpGf9RK0Fz6M3Q2HYVoGapnWFiKPv_xGxYLIWEohJuMCVC7FuiLzMVoBj8rWe0mynTuBmSLjuy3IE33J5wQHsPJEAjk3PRZrAuruhRnrWgwmnuKs1YBVxaxABV_ny8T-EFB56dENWEEp1wd1cz7-8pYqywecMuesROlX1DHflvIBwYplGI46gjuvH5FxHLzoMRnfU023BjCDmCvmCuHH99S6cx-IsGZNFLQKVIuxjbj--Di2eGdmmf0nH9KGi2pa_CZ9qFauqrv-D1iqgxWPeyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=Tel_K0ODF_rc9QMZrTXzJ8T1QYw-FNcZh7uVvt6GSMMsMRpxVtPgcJmf9ypCvqOcBT5s9mL_rGiIAK8HebVNRKsUzX7SzDhmafCWIqp_2KBgb0x3C6hqe9PSZ-hQNtFN8bA5fV_yXXlvBrXsnJ2fnqmRxDB7FUut_wUWjslCrxHL2T9r2_nLIA-Gclqidch4aZIujTRbaZ47vl9TTi0VRsO32Z3Mi2_dGrdviEwYY0vDujy3nj2JG8rqw4ZE1BXaAMOhdNflH0xob4lWvSC5CsHNKktRyykkovCYD9R9PHnRHBo_o1g22TiYaix8RiL7osBgSzHMovwltfC5pcKwpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=Tel_K0ODF_rc9QMZrTXzJ8T1QYw-FNcZh7uVvt6GSMMsMRpxVtPgcJmf9ypCvqOcBT5s9mL_rGiIAK8HebVNRKsUzX7SzDhmafCWIqp_2KBgb0x3C6hqe9PSZ-hQNtFN8bA5fV_yXXlvBrXsnJ2fnqmRxDB7FUut_wUWjslCrxHL2T9r2_nLIA-Gclqidch4aZIujTRbaZ47vl9TTi0VRsO32Z3Mi2_dGrdviEwYY0vDujy3nj2JG8rqw4ZE1BXaAMOhdNflH0xob4lWvSC5CsHNKktRyykkovCYD9R9PHnRHBo_o1g22TiYaix8RiL7osBgSzHMovwltfC5pcKwpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YCPxEp5naVNK7IlOjAAVp5FMsjqh-gSzoY33688rJernd9PWKfSrO_gfzlA1sHxex-06X0D18o6cv6dSlaBj2NQr62v_p8oMbuD9r8Vw5s5BO-tlOhzj8LsyeInsKskcaH8teyNFL7B01BBkAoNcsmdrfcQBxzgUDazWz2HEOv_wY0fWYNpsSNliPVtQE9WOlBH_LGXL1Js7WSPbfTStO-pWBqKYj1dT3naEKqfLJL_6DVGbfyGRa3zBRtxFSi-L9ziQ6YlFdynBLUS4jboFrycMioPIlO490oFRlUox2jiMz0SQf3zyzXsBQ5pkJNXib3g24uFOfKicuTe8VrDpWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eOCJn4pwsS4XMm0clYc_QhGyoBywF8dEAkyS19hLg9NAOOq7c-RIYnFntQbNBGVMRcRnGelbk1qVbxqAKeQb5be2lQjmWVhlDZG-0hP-iQRKSGbODrWwHvFKCvfX7YqjQwbWCZv9NXYVtqN9lnhofVfRQ9laZCiarX_7OnVwybcJr8aKvfv3fKMWN4fpNMuafswigoFbTAqndRaE8dO7LeIT-aBdcd8xEfWK1iZonJ-G6Coz4lfr4F9HAFRMo52EL3doUY0Up4urPZMbOgy_pUL4FY_JBiVJ2wLdObteC3tq3qbnOvWtLBc65aQiKR59vgCP306-Qoo8pPK__FEprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rXzr5_p0K5O4Uhzwje7gO2fbwIuT46oIYRCNH2VI_GlrVB_fB725G1rsGjGEWDYBSNKcEVciMuvZaAkTXSFbCwUZaJFBwugpKt1j00PCQhrbc4F8B-1-dPDh3JAOCYrr0Ou8GOfOg-xANFZI4DwaRoBLmYP0NEhCKxV9eJDWG9rc9u0aHefNex5uYht-5fYFv0K6_QnfI9lASUIbn0_I6DK_9dC0yeojL5Gs_1SUyYfO8xlxldJvMMIRt3EpWeOQYSYRhbo2scuONakqilxg_2xkTtjINH7xBIGnlbmxncqYTZAAXFlMhxMRFVTkk-LmQOu5Mg9441-pbEv9poLlqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=u_hMksUiUHQx0jSqQm_GOQWkOQETfmGSFDI-YRcqkCs9IScNfFNEtJFbVx7bwKgqrzpGfdnsY06xH1kNfnwSEP5JmjNom9Z8u6WcA1uPoATZvAhqGMVzPdl_fHqlhZrVbZuREULGXFgGY8mPCNP8WiEdD0zWZ7pVee2mIFOJC_gnS5DomKFmMxRtjoxXy5kKMpvEYb1mgi0G_cvzRa1qhztWKHzy4sHCVGAA2Xqw5D7iX-g3AAlD2ImOKDESIbuweJw4C52wikZn0DaBdeaSkLL6eV-Cd2s9ug9JFHzVXv0YTHn7VFG_bJWy6GXZGPmx9GyXm3O6V44ryCwolZ1EZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=u_hMksUiUHQx0jSqQm_GOQWkOQETfmGSFDI-YRcqkCs9IScNfFNEtJFbVx7bwKgqrzpGfdnsY06xH1kNfnwSEP5JmjNom9Z8u6WcA1uPoATZvAhqGMVzPdl_fHqlhZrVbZuREULGXFgGY8mPCNP8WiEdD0zWZ7pVee2mIFOJC_gnS5DomKFmMxRtjoxXy5kKMpvEYb1mgi0G_cvzRa1qhztWKHzy4sHCVGAA2Xqw5D7iX-g3AAlD2ImOKDESIbuweJw4C52wikZn0DaBdeaSkLL6eV-Cd2s9ug9JFHzVXv0YTHn7VFG_bJWy6GXZGPmx9GyXm3O6V44ryCwolZ1EZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A04KGrRra1TRvfuaRq7VBiWsGYH2CfQAdM9I_L_pqwJhO6a6oq4YFZWyNFcysdTve3fFmdTHqJSt0Ta6AkgvqXET5xiKJwMlhlAYBFh7AHFKxRrYKQ01clBXDRPQTCutcR3DOZGgnKLXRCq7W5XtwSt9nl-Vp1G3-82TbqGMY_V6tjVjQd_1_SVoGdW-5bq6hh6qWGvK-FRHZg9WdOD6-M07ZhUhB9x2qbv228am9SprtNyi8jdyx8FGjGKCSj6-5HXwsDyRF97DR1yaOqUygb_-F_tMSoB5FQbsAEPDeXDjtZaDXKST-1RIdQrw_tGC3Jb8e-EZHJ-OpObxEClHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/li7UW_HY8ZmVZshtpIAfFZvq6GTK63NxFwj6o8NEzABtLG5pvH61-NMcsBvz9LHyV7sPYt6KMUImol8kFEReYvR3lPNHN4qtZ5RX7jq9jbfThlfeIrNsgWYWCG6b9LYVnD2LUjwy_avNrpg5Dfvq_AA3Qo0HN50bWjpE9SR1h5fyAKqpGgNGKesIGJFalTSrDCzR9jW66ZWkudgs-G5__d0mRcmh3OAlZ3ytgfnC6VuSu3Ny_61urj2oahjk03t5qXq4ufx87etgu29IXBsT2i0-uN9PXoEA4lkDjJ-0HHXgcNhFd-Matquyc6x1kXEnfUgwJ4VFEHkyewQ89OWJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CgckySyMpsxv1itpxl2BUSGk9HFheoL0vvtzOlWaNetV9tbJ4Q4zfsC6a7plaqtJ8qgjD9h3YUpoSU3fW9HQ6gLikcP2Xg06Xnx7kZOJGXGbaxdOFBOekBPkbnnOknHP1pNfNszBXbwunC4FSLBMyPZrhPmMuHsAYQ61lWM7kBd0RIgIZhj74Yjbux_Ky7fBMg73p0OrJyyXwwDyNw2dhRKB5iNPD-eiIqFtsSn5qrhL9RSzCNHOKKo9WiucgbqmV7AR8Ydcoqoi63PbZoE7OsUp-c7F3FI_x9M4MXhSN5CKgsacypJPzr6arKcs65fPe8jd4AaF3xRLYgRD8QXOXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRq0_syOHkqQ_CzkEIZBqkQMRNGfJ2cJ4ETZdL61decK8gmx3s26C2J8AoApcoX7nHw5A7oit9mgB-gyn4V4sQwp7KGLE2vpoeKvyiCzjYSiHuHT_FdPAHYNWwkyBNxPTNJ8YjIvmVrmCHgbfGJbLchckwdn-V7ZamAuPDeM5ardclnplbCSgcxdCgb1UedD8OOJtrtNYDZHDU4rPtCfwzgMclD999sVmlYqs8zrYBOq4X_Gc15TaQLVrE1y5SQt43Ds3JYM3_rxekTlnxiDDF-cuQbKeMBSKHLRtZ070AXQygTcSk6vFGXVShEB70RsirgbU9XLwwI2Sczx0GWaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_TCOB1mOYXaG8zkQuiODUJsJsyAf83knsGm6MMne9PSVSF65v1xAFVD0k6lhEpwBZ9PPAQn9tku79EgmIgFqRx8z_34AqpyZKzjxfJnnz49xdbwopVfJTpj4Q-IYBOvninGZoh5g3d6dcIETtp1_ljfSMDNV7Dd8enr5aOl96zBwW4u9lIispeGBMtMLVeWNFKyhscOV__ZVwP8k2bYdsL6sTFiKcrFXCLoGRJTbSv_1JfWvJozW7-ZLM736A1DCS5D0YkuV2oxEim-Uw44ps5GLNUNagyZ4j9nrvUDICHCCMHVthzV7_l5TWGwZNQRmpwuAhwK6s0bjLB1pwZl5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=EnoA0OXelYUwnJdpqIHbdSH-KhqPvvkfbNtopuYgXgpaSQukzeeEuLpFUTecvSRQIblmlW1EWw0BXWsZ7QOK6jM8-7O67xSs8-MooQyGvdKuANW7fa302KR0AvCP61IbQNzMyKFYGrghS6UhgjQIeBAVzdpPEGnrvY5ltaJVzZRLHIOpRNAaIbmb8JWjXZzRWDdaubu-7C45EJEfCL2JA-5_XQFv800ZgaE4C1-6wPbBDPqKe2ChcudjB8Bs_m6LriSCUGH8ZVMtH1RHLACTC3socdJX0WKxDNPNiJ8xFucA-Kj1Kjv2Ib60hnGYbmA81UXw7gNiHGVnlExxAfy-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=EnoA0OXelYUwnJdpqIHbdSH-KhqPvvkfbNtopuYgXgpaSQukzeeEuLpFUTecvSRQIblmlW1EWw0BXWsZ7QOK6jM8-7O67xSs8-MooQyGvdKuANW7fa302KR0AvCP61IbQNzMyKFYGrghS6UhgjQIeBAVzdpPEGnrvY5ltaJVzZRLHIOpRNAaIbmb8JWjXZzRWDdaubu-7C45EJEfCL2JA-5_XQFv800ZgaE4C1-6wPbBDPqKe2ChcudjB8Bs_m6LriSCUGH8ZVMtH1RHLACTC3socdJX0WKxDNPNiJ8xFucA-Kj1Kjv2Ib60hnGYbmA81UXw7gNiHGVnlExxAfy-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
