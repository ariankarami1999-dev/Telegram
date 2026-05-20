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
<img src="https://cdn1.telesco.pe/file/rtQ1nEIPJAnNmVLHEVpherRLbKJByjjDUTuW-zR1sugCd2uqu0GquMdTF8UMgdV4nSb6Jurs4rCLmyhzrhB4-pU5w4jyD9GhvdPmT6-NUCO6YVLW80DDSsTuWc8lUyIw_Irrbbwe-hK4ylBmW29MSwybbJ7LRx8IJKImyeVbItTRn7JXGxftEu5Rwfd8NnyQPaGMrDmwZKB0EBURx5y0lXrkFyC9U8W53_f66fJg3ec5sSXE0Hi4V-Kdemd_RPPxzWA95ytb9A6h1QCJefkT0l63hWVmnZ2drVZCIRdV6XSBERXZZ4zrdHPF0__BIrOB8tL6A63S_Y25IZ9JdQ1_Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=g0iu6PY0qkK6UP3LM4Vvq7ZicqCsjeFwb_u_1tlXXcGt0nXkDZRFMWPi1392Dsd9mEggRzP21LYCG_OJRDMGbm_cset_jAYO63B0kggDq7ldoACW7XvFvISaV6-Ibhkg5PjhR6eWZ2GrEAMvRjt2rbyC94WnzzYfzx1Pou15liuUJ9DGB88N1q00YwdLGBqMdjJ72bRdQDft3Sdf4VVDhFp0WgWjWU7XIIpHOkfkvwnguljNYbS-LX2n4mibolxrY6qNsn_B24lKf9GRoykSdpNWpr4pLt5wSADc2m2c75gF5Q7nKrPNa1DRXmdfXDbq1Wmf6atK1_6yDS_M8_18Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=g0iu6PY0qkK6UP3LM4Vvq7ZicqCsjeFwb_u_1tlXXcGt0nXkDZRFMWPi1392Dsd9mEggRzP21LYCG_OJRDMGbm_cset_jAYO63B0kggDq7ldoACW7XvFvISaV6-Ibhkg5PjhR6eWZ2GrEAMvRjt2rbyC94WnzzYfzx1Pou15liuUJ9DGB88N1q00YwdLGBqMdjJ72bRdQDft3Sdf4VVDhFp0WgWjWU7XIIpHOkfkvwnguljNYbS-LX2n4mibolxrY6qNsn_B24lKf9GRoykSdpNWpr4pLt5wSADc2m2c75gF5Q7nKrPNa1DRXmdfXDbq1Wmf6atK1_6yDS_M8_18Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین هم به خدمت شی رسید.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75566" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SCtxp76U_kZviqPs9KcTIjopJcD4cg-AYZoWjUIeJTxKJA5YNTbvawYo83UfUOdeWhQALAgGJJBS3qlcKP6reUKCWZ45Gh48MGoDelbmiZbAVdV9bi7mHUQhd7lnADzFQmw5TzRAdctNQnvovXwzInJi7Fo1aWtIJ6aOmVcZQwJIF7G8roeE8qQ7R_9BdM6RFkBeP0eWyfv3lvyGms8wvTn7tIZXocg4puSx36uBy2hwnA8c2g5lZ2_UO7nG0q7peYkUDb96MVd78AI1C8v60pV7CfeXKC8uFsn6vs692ZrDNixV5_LdWUizK5JDamHPVsLvU2tga3VkpTsmrfgaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین
تیتر نیویورک‌تایمز: هدف اولیه جنگ، روی کار آوردن رئیس‌جمهور تندروی پیشین به عنوان رهبر ایران بود
بخش‌های خبری مطلب:
به گفته مقامات آمریکایی، حمله اسرائیل که با هدف آزادی محمود احمدی‌نژاد از حبس خانگی در تهران طراحی شده بود، بخشی از تلاش‌ها برای تغییر رژیم و به قدرت رساندن او بود.
چند روز پس از آنکه حملات اسرائیل در آغازین روزهای جنگ، رهبر ایران و سایر مقامات ارشد را به قتل رساند، پرزیدنت ترامپ علناً اظهار داشت که بهتر است «شخصی از درون» ایران کنترل کشور را به دست بگیرد.
اکنون مشخص شده است که ایالات متحده و اسرائیل با در نظر داشتن شخصیتی خاص و بسیار غافلگیرکننده وارد این درگیری شدند: محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران که به دلیل دیدگاه‌های تندرو، ضداسرائیلی و ضدآمریکایی‌اش شناخته می‌شود.
اما بر اساس گفته‌های مقامات آمریکاییِ مطلع از این موضوع، این طرح جسورانه که توسط اسرائیلی‌ها تدوین شده بود و با آقای احمدی‌نژاد نیز درباره آن مشورت شده بود، به سرعت با شکست مواجه شد.
مقامات آمریکایی و یکی از نزدیکان آقای احمدی‌نژاد اعلام کردند که او در روز اول جنگ بر اثر حمله اسرائیل به خانه‌اش در تهران - که برای رهایی او از حصر خانگی طراحی شده بود - مجروح شد. آن‌ها گفتند که او از این حمله جان سالم به در برد، اما پس از این خطر جانی، نسبت به طرح تغییر رژیم دلسرد و ناامید شد.
او از آن زمان تاکنون در انظار عمومی دیده نشده است و مکان و وضعیت فعلی او نامشخص است.
...
اینکه آقای احمدی‌نژاد چگونه برای مشارکت در این طرح به کار گرفته شد، هنوز در هاله‌ای از ابهام قرار دارد.
...
سخنگوی موساد، سازمان اطلاعات خارجی اسرائیل، از اظهارنظر در این باره خودداری کرد.
...
مقامات آمریکایی گفتند که این حمله - که توسط نیروی هوایی اسرائیل انجام شد - به منظور کشتن نگهبانان مراقب آقای احمدی‌نژاد و به عنوان بخشی از طرحی برای رهایی او از حبس خانگی صورت گرفت.
این حمله آسیب چندانی به خانه آقای احمدی‌نژاد که در انتهای یک کوچه بن‌بست قرار داشت، وارد نکرد. اما پاسگاه امنیتی در ورودی کوچه مورد اصابت قرار گرفت. تصاویر ماهواره‌ای نشان می‌دهد که آن ساختمان ویران شده است.
در روزهای پس از آن، خبرگزاری‌های رسمی روشن کردند که او جان سالم به در برده است، اما «محافظان» او - که در واقع اعضای سپاه پاسداران انقلاب اسلامی بودند و همزمان وظیفه محافظت و نگهداری او در حبس خانگی را بر عهده داشتند - کشته شده‌اند.
مقاله‌ای در نشریه آتلانتیک در ماه مارس، با استناد به منابع ناشناس نزدیک به آقای احمدی‌نژاد، نوشت که رئیس‌جمهور پیشین پس از حمله به خانه‌اش از حصر دولتی آزاد شده است؛ این مقاله آن رویداد را «در عمل یک عملیات فرار از زندان» توصیف کرد.
پس از انتشار آن مقاله، یکی از نزدیکان آقای احمدی‌نژاد در گفتگو با نیویورک تایمز تأیید کرد که آقای احمدی‌نژاد این حمله را به عنوان تلاشی برای آزادی خود تلقی کرده است. این فرد مطلع گفت که آمریکایی‌ها آقای احمدی‌نژاد را شخصی می‌دانستند که می‌تواند ایران را رهبری کند و توانایی مدیریت «وضعیت سیاسی، اجتماعی و نظامی ایران» را دارد.
این فرد مطلع اظهار داشت که آقای احمدی‌نژاد می‌توانست در آینده نزدیک «نقش بسیار مهمی» در ایران ایفا کند و اشاره کرد که ایالات متحده او را شبیه به دلسی رودریگز می‌دید؛ کسی که پس از دستگیری آقای مادورو توسط نیروهای آمریکایی در ونزوئلا قدرت را به دست گرفت و از آن زمان همکاری نزدیکی با دولت ترامپ داشته است.
...
در چند سال گذشته آقای احمدی‌نژاد سفرهایی به خارج از ایران داشته است که به گمانه‌زنی‌ها دامن زده است.
به گزارش مجله نیولاینز، او در سال ۲۰۲۳ به گواتمالا و در سال‌های ۲۰۲۴ و ۲۰۲۵ به مجارستان سفر کرد. هر دو کشور روابط نزدیکی با اسرائیل دارند.
ویکتور اوربان، نخست‌وزیر مجارستان در آن زمان، روابط نزدیکی با آقای نتانیاهو دارد. در طول این سفرها به مجارستان، آقای احمدی‌نژاد در دانشگاهی مرتبط با آقای اوربان سخنرانی کرد.
او تنها چند روز قبل از آغاز حملات اسرائیل به ایران در ژوئن گذشته از بوداپست بازگشت. زمانی که آن جنگ درگرفت، او حضور علنی کمرنگی داشت و تنها چند بیانیه در شبکه‌های اجتماعی منتشر کرد. سکوت نسبی او در مورد جنگ با کشوری که آقای احمدی‌نژاد مدت‌ها آن را دشمن اصلی ایران می‌دانست، مورد توجه بسیاری در شبکه‌های اجتماعی ایران قرار گرفت.
...
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75565" target="_blank">📅 06:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dLKsHee9i_guOs9R_agROIQ6EJGxfzcobphm_JH4aK0c8ElyUKRcy9LEZr-WO2YPFV5E7-cvSap7vAvAZAzVoN9ntN6ANF0L460XEshcr4AK8SyfiWGXAXtSp4CYiwPlJNGzViIksPv7YjPSzAK9ChTW-jGS1aE1Jn5I0AXA2AhTrvnB59nH55Aoxjp34GjrScT78oP-ON_AE2Pi-RuCaKm0HPB9g0QNV3gwbTIVoNQ0NqFxyYmuiBvFpM2yKg7OqHg680Zt9EGWHVjXkSFP5iAjhSMwTq65kXDvBZuQX8YvpewhH_BaC-m_CaoNo4Dy7r8Mveq4CTVmynF14Ll09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در یک سخنرانی در کاخ سفید گفت  ایران قرار نیست به سلاح هسته‌ای دست پیدا کند. نمی‌توانند سلاح هسته‌ای داشته باشند. ما نمی‌توانیم چنین چیزی را تحمل کنیم و آن را تحمل نخواهیم کرد.
او گفت ما نیروی دریایی آن‌ها را نابود کردیم. نیروی هوایی آنها از بین رفته است. سامانه‌های پدافند هوایی آنها از بین رفته است. تمام تجهیزاتی که برای جنگ استفاده می‌کردند از بین رفته است. تقریبا همه چیز از بین رفته است.
ترامپ افزود: نمی‌خواهم بگویم رهبران آنها از بین رفته‌اند، چون بیان آن چندان خوشایند نیست، اما واقعیت همین است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75564" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UDl-I0Dfi9lhKPiyM7aJ7oznlS-J9lBSTKl6bVZ6b7ySusTOTSWEwiMyqeoC8iq_o5k7etMJfJnweqndHK1-hKo_B_eyQWDnbaIw6RO-icO_hV8wHHGV33UJqlrTuM7dTUiIPknmWgSe0qjdaMxXpXgzEw9hdFAjqu5cGxRQlaI9wgR1cQyKWAUklBWfN7efTwo0Iccw4oD7oaPh_PgJDfcWDWBI3B65nv27L2fbDh1v1VU_0CAZH0ui00P7J8w9Ik_cY7eXpxiYbOzO0Q7oaE_mTu_Mi-lV5zH8uSghuuxB5Fi9gfvP8tHVem6_WVRTd2tZjj6wFgz-KEf62itCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه در قشم
آپدیت:‌
تصویر بالا:
#زلزله
به بزرگی ۴٫۷ در عمق ۲۰ کیلومتری بندر لافت در جزیره قشم هرمزگان
پیام‌های دریافتی:
سلام وحید دو زلزله شدید بندرعباس رو لرزاند
ساعت ۳:۱۱ دقیقه بندرعباس زلزله اومد
همین الان ساعت ۳:۱۲ دوبار به مدت ۱۵ ثانیه وحشتناک بندرعباس لرزید
من بندرعباس هستم دو بار لرزید
زلزله اومده خیلی بد بود
زمین لرزه نسبتا شدید ساعت ٣:١٠ بامداد بندرعباس
بندرعباس هستم فکر کردیم باز زدن دقیقا ۲۰ ثانیه همه جا میلرزید
چند دقیقه پیش زمین لرزه نسبتا شدید اومد دوبار تو فاصله خیلی کم بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75563" target="_blank">📅 03:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cfBT_dCmmR1bhL09pBkLfRUm2hpaZnZGdhKdrrEZYGehIYLBhM3E_dTWVlF7zIQtshoc-wDlDRkrtQ1tLe9NJiYxzw_3p6d5W_3ZV-aa7POM7s3skk9OY7IlbLOn9PNswX4wPSrhJXQ7ixTYi8U-qhYTU8q6PPJq8__3wSwhrIC_36pCGJilw0KEx222sFF3JM5ZlWpdMTmDEZHyX0_JlHQQIeO0K6lHH8QypJ0sxP8yCmmqc2HrHhTUnQ658u6eUHASkSko-IyeuUwED-71MS6t7ZiALqMbxv88fQQTyvmp7Dqb4tLQSaadGOztTxqZwz4Pqp2BbX1_sWbs478ANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا روز سه‌شنبه قطعنامه‌ای را برای توقف اقدام نظامی در ایران پیش برد.
پیش بردن این قطعنامه پس از آن صورت گرفت که سناتور جمهوری‌خواه، بیل کسیدی از لوئیزیانا، به آن رای مثبت داد. کسیدی چند روز پیش، در رقابت‌های درون حزبی ایالتی برای ادامه حضورش در سنا، به نامزدی که از حمایت ترامپ برخوردار بود، باخت.
به گزارش سی‌ان‌بی‌سی، با وجود اینکه قطعنامه اختیارات جنگی با نتیجه ۵۰ به ۴۷ به تصویب رسید، اما هنوز احتمال کمی برای تبدیل شدن به قانون دارد. این قطعنامه باید ابتدا در سنا به تصویب نهایی برسد، سپس مجلس نمایندگان به رای بدهد و سپس نیز، دونالد ترامپ به احتمال قریب به یقین، آن را وتو خواهد کرد.
@
VahidHeadline
چهار جمهوری‌خواه هم‌حزبی ترامپ همراه با همه دموکرات‌ها به جز یک نفر، به آن رای مثبت دادند. سه سناتور جمهوری‌خواه نیز در رای‌گیری غایب بودند.
باوجود تصویب این آیین‌نامه، حتی اگر قطعنامه‌ای در سنا با ۱۰۰ عضو هم به تایید برسد، کار دشواری در مجلس نمایندگان خواهد داشت که تحت کنترل جمهوری‌خواهان است و پس از آن نیز باید دو‌سوم رای کنگره و سنا را داشته باشد تا بتواند گزینه وتوی احتمالی رئیس‌جمهور را دور بزند.
طبق قانون اختیارات جنگی آمریکا مصوب ۱۹۷۳ که در واکنش به جنگ ویتنام تصویب شد، رئیس‌جمهور آمریکا تنها ۶۰ روز می‌تواند بدون مجوز کنگره عملیات نظامی انجام دهد و پس از آن باید یا جنگ را متوقف کند، یا از کنگره مجوز بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75562" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPoNMZGvY6kPvEjbEr_2z17If7JYBQhhyyv_26Pre3QB_NIKlJpIvKWa9pANaX2dyaQgmXgHBOVcr0UXmxSrhyH5ef8tt-BMn4Y1GG_qI6pWkFAkZTpRTHs785HuTKgDNSbe0sNEEZrcfOaQtwH9B0QOSbPv5M11dKC0svcaawXZfZ6nYdagYrWMuaw4-nm72XE4V88SthGQ_JyjajAQT9OYlZjhY_0BovaMALW9ZxZ-cDBNVYw0_Ke8zE5wGXumcRLyJHzO3PQSyRLPpcYeG61vgBwHBizMW05hyxBl7XpdrCz8YqQV8MIgAawHYLkSoPhX14HzVGHukTvQ84DDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/URAZ5VNRY91kd--LHiy_fXYF0Em45v6emGARq7xTb1NdlIfsBnpo-6EImj9CaSkwY2KPcl6MQothVTvoiukaGAM1Z1qpnitZCea2wMxidmqiZu-9ogEdvrSWI5q85Z3dxePPQzPV0JVtpJKsLyY_DzcHXdS4Kl9XNYYlr_6bKNC6Xt1S7_p_IU_mGB1RgU_hjmidusZZtnqxT7KzAz5OxjTMwSQqgD-RzsHQ96AqObS4GfqLXHK9eVJrraOu3Hd1bmV08aqFxZZM6Bf7gCzpniBcT-2bOpzKZEAonj1FRAiopNpz4K0BxIN5VLLH4-YrpSNaN4ar5n816umNU9YzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s97Ldlpow-_9g2jfUp4RhICw4VTe0O4HOkDj6nJ4FztXqe1ZZDV4u4r__3m8qx8artGABJzdzAluBDe9o_INXesB64KTkQTJ07HToA09L0JPSK-l4abFh4QfjWia3XeRt7lAlZxJdp_rDY8DMyI-FchIbkt6YS-J0FdV97MDARB3nVAdo8IGF4JG85GFWxjfON_1Fbi6MmcPiXxnq2XasBHIRCN7Lyq0gsThlYdJ8iolyum2NI2Qaz9jpkRwRkfQcGprO0Uk2Sd0sCHbLHXo5ENbomkBJUnSj4XpUU0AMLIlpJ6SkFnU8FYBOxI-JSfxre2GiLkcc4l4YjICIFxQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WI8H9ZDZ-zdyhhFxtqp0Jl_AA3yHHM3LaflD3EIitg94GnNqhPoFYzEh0K5VDbZ21mx42ZGiIY8It5lxnMQ0ARRiAD8GevC_FlrEokeiojGDjjB7J94DVGRGmmy1X4WBR5bE6BvjfhYlw4GAsw4BcBpipsFB04EAOvhTZ5tui-xv2BvcXMOIkhbJbo7K7TkoIx4RewNVdBpfdCdqw8XTvIqnVyvBHApIR5j7WD7eUKa2AmPcrp_q9zoOY5Q7aO6ZwRZtvRWztK7AGkt6fmyHnwJnDuYB1dgAhdnvQo-_fAVq-tpzs7sQSykOhmZzNOB56wrsGJwBPKIP2of1JNW5IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=ePkz07rnDSH7c9QUiSYLQLc5VTDMDlMdmhHFEQ7VaGds0AEUJApop3h8VQ_P5Kjf_7_8fWphSCxtnMYQ96x7h_FpUiVXfXdhMn5pGtJqFJAyF0bbrpFNLa02HqyRqZyvhpgglmRhLPp8VeyK7SKftbjVSsp7pqtLKOBzzfdpqMVXtp9sAcgGkfnuMl2Ki3vSD99QvEoSRvwWeYG7UiVDHZ8Bu3CW7PgEj-FInoRaL6sgfN0WAnlrHI5nH8_6PqIBpYgAet66DUs3eylj14ZFcoHhV_noxT9rl8DkRN59KhofodT04zrbW4Rl3C5vnYfs_eTduAidk4ppMk7mSYQQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=ePkz07rnDSH7c9QUiSYLQLc5VTDMDlMdmhHFEQ7VaGds0AEUJApop3h8VQ_P5Kjf_7_8fWphSCxtnMYQ96x7h_FpUiVXfXdhMn5pGtJqFJAyF0bbrpFNLa02HqyRqZyvhpgglmRhLPp8VeyK7SKftbjVSsp7pqtLKOBzzfdpqMVXtp9sAcgGkfnuMl2Ki3vSD99QvEoSRvwWeYG7UiVDHZ8Bu3CW7PgEj-FInoRaL6sgfN0WAnlrHI5nH8_6PqIBpYgAet66DUs3eylj14ZFcoHhV_noxT9rl8DkRN59KhofodT04zrbW4Rl3C5vnYfs_eTduAidk4ppMk7mSYQQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهور آمریکا، گفت واشینگتن و تهران پیشرفت زیادی در گفت‌وگوهای خود داشته‌اند و هیچ‌یک از دو طرف خواهان ازسرگیری کارزار نظامی نیستند.
ونس افزود: «ما فکر می‌کنیم پیشرفت زیادی داشته‌ایم. تصور می‌کنیم مقام‌های تهران نیز می‌خواهند به توافق برسند.»
او گفت آمریکا می‌تواند کارزار نظامی را از سر بگیرد، اما «این چیزی نیست که ترامپ یا ایران می‌خواهند.»
ونس همچنین گفت: «فکر می‌کنم جمهوری اسلامی می‌خواهد توافق کند، اما تا زمانی که توافق امضا نشود، نخواهیم دانست.»
@
VahidOOnLine
جی‌دی ونس اعلام کرد که دولت ترامپ برای دستیابی به توافقی جهت پایان دادن به جنگ تلاش می‌کند، اما او همچنان شاهد وجود شکاف و گسست در میان سران ایران است و موضع مذاکراتی تهران شفاف نیست.
معاون رییس‌جمهور آمریکا گفت: «خودِ ایرانی‌ها هم دقیقا مطمئن نیستند که می‌خواهند در چه مسیری حرکت کنند؛ آن‌ها در حال حاضر کشوری چندپارچه و دارای شکاف هستند.»
او در ادامه افزود: «در ساختار حاکمیتی این کشور، رهبر وجود دارد و در رده‌های پایین‌تر از او نیز مقامات زیادی هستند که بر روند مذاکرات نفوذ دارند. به همین دلیل، گاهی اوقات اصلا مشخص نیست که موضع واقعی تیم مذاکره‌کننده چیست.»
ونس  با اشاره به اینکه هنوز روشن نیست این تشتت آرا ناشی از ضعف در هماهنگی است یا سوءنیت، تاکید کرد که نتیجه این وضعیت، ایجاد فرآیندی مبهم و سردرگم‌کننده بوده است. ونس در پایان گفت: «با اطمینان می‌گویم که گاهی درک این نکته که ایرانی‌ها دقیقا می‌خواهند از این مذاکرات به چه هدفی دست یابند، بسیار دشوار است.»
@
VahidOOnLine
جی‌دی ونس گفت اعضای تیم مذاکره‌کننده جمهوری اسلامی برخی ویژگی‌های ایرانیان، از جمله «هوش و سختکوشی» را دارند، اما همزمان مواضع «بسیار تندروانه» نیز در میان آن‌ها دیده می‌شود.
معاون رئیس‌جمهوری آمریکا با توصیف ایران به‌عنوان «تمدنی بزرگ و پرافتخار» گفت مردم ایران «شگفت‌انگیز» هستند و جامعه ایرانی-آمریکایی در ایالات متحده نیز نمونه‌ای از این ویژگی‌ها را نشان می‌دهد.
او در عین حال افزود گاهی مشخص نیست تهران دقیقا چه هدفی را از مذاکرات دنبال می‌کند و ساختار تصمیم‌گیری در جمهوری اسلامی را «چندپاره» توصیف کرد.
ونس همچنین بار دیگر تاکید کرد واشنگتن اجازه نخواهد داد جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند و هدف مذاکرات، جلوگیری بلندمدت از بازسازی توان هسته‌ای جمهوری اسلامی است.
@
VahidOOnLine
جی‌دی ونس اعلام کرد: «فکر می‌کنم ما در حال حاضر فرصتی داریم تا رابطه‌ای را که طی ۴۷ سال گذشته بین ایران و ایالات متحده وجود داشته است، بازتنظیم کنیم.»
معاون رئیس‌جمهوری آمریکا که در نبود کارولین لویت، سخنگوی کاخ سفید، مسئولیت نشست خبری روزانه را بر عهده داشت، در ادامه افزود: «این همان چیزی است که رئیس‌جمهوری از ما خواسته و ما به تلاش در این مسیر ادامه خواهیم داد. اما برای این کار، همراهی هر دو طرف لازم است (یک دست صدا ندارد).»
ونس با تبیین خطوط قرمز واشنگتن تاکید کرد: «ما به توافقی که به ایرانی‌ها اجازه دسترسی به سلاح هسته‌ای را بدهد، تن نخواهیم داد. بنابراین، همان‌طور که رئیس‌جمهوری ترامپ به من گفت، ما در حالت آماده‌باش کامل نظامی هستیم. ما تمایلی به پیمودن این مسیر [از سرگیری جنگ] نداریم، اما اگر مجبور شویم، رئیس‌جمهوری آمادگی و توانایی پیشبرد آن را دارد.»
@
VahidOOnLine
ونس افزود که به‌تازگی با آقای ترامپ صحبت کرده و رئیس‌جمهور آمریکا تأکید کرده است که مسئله اصلی برای آمریکا این است که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند.
ونس یادآوری کرد که اگر چنین اتفاقی بیفتد، کشورهای حاشیه خلیج فارس نیز به‌دنبال سلاح هسته‌ای خواهند رفت و سپس کشورهای دیگر جهان هم همین مسیر را دنبال خواهند کرد.
او گفت: «ما می‌خواهیم تعداد کشورهایی که سلاح هسته‌ای دارند محدود باقی بماند، و به همین دلیل ایران نمی‌تواند سلاح هسته‌ای داشته باشد.»
وقتی از ونس پرسیده شد که آیا ممکن است روسیه مالکیت اورانیوم غنی‌شده ایران را در اختیار بگیرد، او پاسخ داد: «این در حال حاضر برنامه دولت ایالات متحده نیست. ایرانی‌ها هم چنین موضوعی را مطرح نکرده‌اند.»
@
VahidHeadline
جی‌دی ونس همچنین گفت واشینگتن می‌خواهد جمهوری اسلامی فرایندی را بپذیرد که تضمین کند ایران حتی سال‌ها بعد از دوران ریاست‌جمهوری ترامپ هم نتواند توان هسته‌ای خود را بازسازی کند.
او گفت: «ما می‌خواهیم نه فقط تعهد به عدم دستیابی به سلاح هسته‌ای را ببینیم، بلکه می‌خواهیم تعهدی برای همکاری در یک فرایند ببینیم تا اطمینان حاصل شود که نه فقط اکنون، نه فقط وقتی دونالد ترامپ رئیس‌جمهور است، بلکه سال‌ها بعد هم ایرانی‌ها به دنبال بازسازی توان هسته‌ای خود نباشند.»
او افزود: «این چیزی است که ما در مذاکرات در تلاش برای رسیدن به آن هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vgn3MTkSmg6_LfanmOk4XVqqX7KcVofo1lrWN3DwHT_syZT_LYnRxoMB-CWm4xRZtpF0Kxy4xnXkfrFImAOrEvyojY9A1gsg4TpamrhbTBjwDy2-lWCJC0yfdBFwAE3OydvKp2M-TWDFqC6uwF2Sq_kJx31O8fLMeCMRwVbYrqEsx2ePb0NcJikAJqeALOsIjsBRO59Kc6h8xpiLvv8Uys9u-gy_3U7_mZR_dpZhSsx1N3-6_rMgdegXoBircTm26AlTdORDx3JHawTv0Y6y1WrxnoFqBhdhFX1yvjl67hyMtcVQYEjpxm-zqQMXNfYG2MAd67eWLRutmodoWITTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vgn3MTkSmg6_LfanmOk4XVqqX7KcVofo1lrWN3DwHT_syZT_LYnRxoMB-CWm4xRZtpF0Kxy4xnXkfrFImAOrEvyojY9A1gsg4TpamrhbTBjwDy2-lWCJC0yfdBFwAE3OydvKp2M-TWDFqC6uwF2Sq_kJx31O8fLMeCMRwVbYrqEsx2ePb0NcJikAJqeALOsIjsBRO59Kc6h8xpiLvv8Uys9u-gy_3U7_mZR_dpZhSsx1N3-6_rMgdegXoBircTm26AlTdORDx3JHawTv0Y6y1WrxnoFqBhdhFX1yvjl67hyMtcVQYEjpxm-zqQMXNfYG2MAd67eWLRutmodoWITTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا سه‌شنبه به خبرنگاران در کاخ سفید گفت ممکن است مجبور شویم دوباره به  ایران ضربه بزنیم، مطمئن نیستم.
او گفت منظورم این است که دو یا سه روز، شاید جمعه، شنبه، یکشنبه، چیزی در این حدود، شاید اوایل هفته آینده؛ یک بازه زمانی محدود، چون نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای جدید داشته باشند.
رییس‌جمهور آمریکا ادامه داد که او دوشنبه تنها یک ساعت با تصمیم‌گیری برای انجام یک حمله فاصله داشت، اما این حمله را به تعویق انداخت.
او افزود جمهوری اسلامی برای رسیدن به توافق التماس می‌کند.
ترامپ درباره جنگ گفت: «همه به من می‌گویند این کار محبوب نیست، اما من فکر می‌کنم خیلی محبوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=AkjdTON-aS6MtzdorhxkH9ufDZy2rrlfSbir13oLLY-P9NM3c877MWPK_z7uZl2GU1YxR12gDX58RWcguDDeb1IpR_OwW9-vStPJa63rf1-2PyEm5VOjlThqbheRttM_jJTEbD5wuj4fQi-XB2J0FYFpjJcN-cRY7qzwxNYA8xU1HnM8QmDYEgWgYsts6INYcplul5Cgbl160bLvQoaFbPDA4amGN1Pz1ixWaJSN00GQxp5_Ldx8yWkNM4GK_gEcvnU7ZLAunB16a-HQhrxhbFvrkbWP8X46So3JXku8xZTi9eZLxivFAaYWqZ3fyaNvfmtU3MchFi9qFnnQtFpmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=AkjdTON-aS6MtzdorhxkH9ufDZy2rrlfSbir13oLLY-P9NM3c877MWPK_z7uZl2GU1YxR12gDX58RWcguDDeb1IpR_OwW9-vStPJa63rf1-2PyEm5VOjlThqbheRttM_jJTEbD5wuj4fQi-XB2J0FYFpjJcN-cRY7qzwxNYA8xU1HnM8QmDYEgWgYsts6INYcplul5Cgbl160bLvQoaFbPDA4amGN1Pz1ixWaJSN00GQxp5_Ldx8yWkNM4GK_gEcvnU7ZLAunB16a-HQhrxhbFvrkbWP8X46So3JXku8xZTi9eZLxivFAaYWqZ3fyaNvfmtU3MchFi9qFnnQtFpmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی کارزار ایران‌اینترنشنال برای یافتن هویت پیکر جاویدنامان در بیمارستان الغدیر تهران، ویدیویی از لحظه قتل جاویدنام آیدا عقیلی به دست ما رسیده است.
آیدا عقیلی، ۳۴ ساله، شامگاه ۱۸ دی ۱۴۰۴ در شرق تهران با شلیک دو گلوله ماموران به سرش کشته شد که پیکر او را پیچیده در پتویی چهارخانه در حیاط پشتی بیمارستان الغدیر یافتند.
@
VahidOOnLine
مربوط به این تصاویر تکان‌دهنده: @
VahidOnline
این ویدیوی دلخراش: @
VahidOnline
اعتراض‌های چهارشنبه ۱۷ دی:@
VahidOnline
#بیمارستان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5uNM7K9Zt6cFuP3B3X3ZS1TCe_OH3LjmFbrBRRdZjweRtSzn1Uvfe9mx8TTpiqUPfLXU3tGhPIPB4NXJLN5lWMxj4nxLfS3doffTuh1bk-dW2BR4vVhAtnGENP2UwKzdh1RaC3wbEfNzumXVW7ZEMr-ou0TVQiEzd0-d__cdx74w0MNmyld0rPMNo_0UnSp4ZIqON4jZPKDSWsqUxJe_-PcExlVhCAKTPtoerGhcxyHc8XOejwwh4RlRoDTl1lZTk4nrTTTTR4QSkV_1Ed1_3hlEc2sDGRhtuZ4eYbNdvtpD6JiTACOMPtavEmtqZzY_keHSTTOoaMFrMzOg074wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnE_czF4QWekatwX7DSxQFmhBzgDR_l8pNHq6fSIGJlYT2vghzJgTNWwPx8GJq-tMaOLR7iY2BZ5XWHCrZqaQ1ZU-KeEWktA5AwBUpEsHde1FRQMROYT3mRu-ZZXAz-N3ssC6KlvqpXTwPxyl8mJ2yvFYhAK5VqAdq1OFTtW6-MgoQ9Z3f6d9dNkuCuydNB0KXU7TI6ShTh9xUPI7nNj0toZgAgtMib-WY8YxHYAcXITemKby8I2v_QYcMHOMJhy_LOwdkjj5M3eL5CfItDmSWiEJ_9IFS8WlixcZVRMoVW2OlyHE3CA9HDO2zvYPpGvHEKMOtt_I5MIrnLt5wyJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
آپدیت:
گویا نوزاد بازمانده جنگ هم نبود و تکذیب شد و مسائلی دیگر:
beehnam
،
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHadRDKUKiXmKd0gdgrq5p1HQFjoql0Ap2byNMs-I1R0ISy12y_-i0ZG-CKFCibP2oXwr-3JGuvmoDmAMPkSzTDrtWBoBS8N5cXsfu1t9sgMdAQBuGPEqN_G922vaBN2-fCo3LJFbHegdMFWll_ah2gFfF_csKAx6ngeGeDSepQAfhmo2xpY7of8YcdVtR_kbaHAOwWQrInYk8OD5X04Z6UvIOp0dPz0sWyoyd7mu_jHDDlBKHUooA0c4SlaNZU0uOVZUE6dGfsg2JSQ39by1gt76AZgkqUrt5pu9QyJb7_iaLqNW23mwy5KE0xIQJvuAq1nwqxXRx1GFn29DXLOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XABr-IAJSBh5dRkdPq1Wl7jlDLXHuULorbWwYeTAGdyq0td1XNfnaQeIK0DzMRX_4upB47IFYT5kyQaVr99_NrNE2vjRXmjgFCNeCNTgF04iATNbE94GsO8tF04pPBLf7ddIj_bvvYkSXtjtZnN0AbU1PME9bAHycGv2f48JqSG0pj48PIpPiRJ_U5pBTZ3jXwSCnBaRyhcqKYXRMYA0xU7tblVUsBV6Q4q9N0qUcs7D7RxOaGuoYOWK4ze2-m30d613JtNh6pXdRijsVyF56dSQwCL12NBqtyvbI5mvZD08a7HRSZGriVa_CPQ78Ot00M7NhMpbQRbjOOJlZfVTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RGngNAQ5HaV07RDO618f78-ps-Ep9uPEHjYwdFd4o42UA8z7iRax3EMSDiIgmq11gZyDWJDTQAU0JAhXX5xkwm9Ryeb4_Wumv9VDHcdqJLWfslO0L89QjB7128DHqIdKLTXBFF8KXDHiz-4u-W-m8r4ZgvI6LFhuAIbha-ZQnRWQ12rCXIIX6-AXwjBEYkzde0wAtU96-hDXNrDj8QPNRZEBd6_XrYq4_7MQxIWBFt7svrfxta8_kUTYm40RVgoMskvu-cyXIoVqKRqq3KrtPZnfysSKlgsdcfmHjaQt_zyKyMa6eh56UQI100LyELhajC04y_k2VmUJOHht-bWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khDTLk2hD93vfjIeu58V30Nfry9QO08HEsLgHwhH-4jJyG4EA1re46Xi7MKAY1ODa4GlgQ3ukKSpwJsKuPjHsPwqKKNtRg70ial63BxUHssH9ShHs7wBdtgPxsW6Sorcuqg1W_6JHfKLf8YffL9szJzO8pMgakE1OHCtq72v7ZdnXKYd3lxa5qGktCtRU4uc7Q8bU5nMvcf2Y3T1v7rDKSfnvquvrG3qSHTmn0SWcoT_Z5iqYFnSkavcKbJDXsbP_qs5jrFbH0MmDwAeyvbSaVUQc93cW1bjvGRAARlN0N4baDCBVnZx28Zc_83YxM0Iz9E37lNHoacxWVJzfiJy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOyYoX7nXjydM1lK2HXU8aTgduI_FFrcurlqhvPjfMU3ad62_1BFTPXZeWdMERZT0_4wAsBNnk19FRZzDd3ey8JfAWsfeHW7KpmJDGaLe--zFI8sURRgyPCAR0FrI3s7PXvY85dxuFclLoSan0fe_tp5jnJ86LwhtId27HxhIFeeoxM8jpRhpknwfpInAjoTzr9rLR2vheCMz6ChRFvNE4Lb0GjL8mekILpUt8kDbZcinp5t4nVbwY8DKUG_oZnVZy2daX5GOiAQrEkcPJmQkGkgRnSRaXfNPBzzvXNOhmnAxtddRMHdPZiw1--GQBNURh1ow7kuy7FOGs2FKb106w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQZA1IoOxbmV5c6EG7rTn__d7DXJodjoE-bsKIdakVCy-oeigdbZ5H5cfzqnQ2qAihevUXfRCiQfe8AZRYwdtIZ9N9aSFQJnV6HCuBpC_DldDeTsJe5RSoo1AXeX0jJaqsK0cmNXr1GEyPfAYY24AAjOWWNwl72OpZLJ4RxxqtUv2xH4piI6eoNT1Nq48eoBFExjBbxNJFPcLWfh0ZN-kiuIrWJi1AJs9mJwSI81OXuH0OurBy5P9wOIrjYckAj1VoR-_ENWpIG-rDK9AHiiS4k0HBBYurFs1vQ-d-_OnHIa-I8atzG35ez_oLfP3CqCR4L95a8g9m49tEZsqASr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله فردا را به تعویق انداختم
پست ترامپ ترجمه ماشین:
از سوی امیر قطر تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی  محمد بن سلمان آل سعود و رئیس امارات متحده عربی محمد بن زاید آل نهیان، از من خواسته شده است حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛
زیرا مذاکرات جدی اکنون در جریان است
و
به باور آن‌ها، به‌عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
این توافق، نکته مهمی را در بر خواهد داشت: هیچ سلاح هسته‌ای برای ایران!
بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دانیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده فردا به ایران را انجام ندهیم؛ اما همچنین به آن‌ها دستور داده‌ام که آماده باشند، در صورت حاصل نشدن یک توافق قابل قبول، در یک لحظه و بدون درنگ، حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75545" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uylluMRRAzBvrNZ-YqtKq4dXa9Eapr2yeIZ93LtbJC-A_v_PpDVASRC9_W0YqGE0BU8_RbQhvkJur2L09v4Rl4WVOfRn-7EiatrJDrCQB4g_0UrGb08va_JdGKHNoKghcpOlx1dG9bjL3ZDrPsh_jOh9_p4nHwATYMA7CHXAO4BPbzDmgjtKiFZZHgOzHBGMJUs3LzRSiYBr-XNw4eIUHd-wJwx74j7UY44GgqEnwkfwpZkumCV1cYf8OmFR-RuV3ZCwtbwnJwPPd2GSxvrZ3TToS6uhKyw2wNluf9zawO4gVDsn1Lq1jSNvfZjgO7msn5XhsUqe3THnEBlT8-7SDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز دوشنبه در گفتگو با نیویورک پست اعلام کرد که پس از دریافت آخرین پاسخ ناامیدکننده تهران در مذاکرات توافق صلح، «به هیچ وجه حاضر به دادن امتیاز» به ایران نیست.
ترامپ در مصاحبه تلفنی کوتاه، ضمن ابراز نارضایتی از آخرین پیشنهاد تهران گفت ایران می‌داند «به‌زودی چه اتفاقی خواهد افتاد».
به گزارش نیویورک پست، وقتی از ترامپ درباره اظهارنظر روز جمعه‌اش مبنی بر اینکه مایل به پذیرش تعلیق ۲۰ ساله غنی‌سازی اورانیوم ایران است سوال شد، جواب داد: «در حال حاضر به هیچ وجه آماده دادن امتیاز نیستم».
ترامپ ادامه داد: «من واقعا نمی‌توانم در این مورد با شما صحبت کنم. چیزهای بسیار زیادی در حال رخ دادن است».
رئیس جمهوری آمریکا همچنین گفت از تهران «ناامید یا کلافه» نشده، اما هم‌زمان تأکید کرد ایران به‌خوبی آگاه است که ایالات متحده می‌تواند فشار بیشتری وارد کند.
ترامپ گفت: «می‌توانم به شما بگویم آن‌ها بیش از هر زمان دیگری خواستار توافق هستند، زیرا آن‌ها می‌دانند ما...به‌زودی چه اتفاقی قرار است بیفتد».
وقتی درباره ادعاهای منابع منطقه‌ای مبنی بر اینکه ایران تلاش می‌کند در قبال هر دو مسئله هسته‌ای و بازگشایی تنگه هرمز در برابر واشنگتن «سیاست صبر و انتظار» پیش بگیرد، سوال شد، ترامپ گفت «چنین چیزی نشنیده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75544" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-dD4O__LjwWIBSxFyomf9liL7-g41TEWiLx_GLew5Y-BxWH7wJolVGLv2fEJjgcpf1SvDCQ4d1wdCvAcBEES_29H4J61zKO2RjTKqQUlkr9sX4v6Uu9SkrDr_5hgwrfixC5PYuUDTdv6wQHz9dItTuntiP2sB7nHFeA3LpKPNnTAXbWQGl7hBEQUjNkTzqDKA8H4d5MvLw_WIXsvlFhfz6JyV_yCXjnt81fcgykgOJj529X8Rw-ybkas5iuDwspO5IEMrGDPMgSDBxf72rW_JoUSrrjSFqbtMZ5m8KL30Z8-v8-YY27OGgRr6gWnt7Sn9ZtDTZhYbx3L9C-FdpuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، دوشنبه گفت که آمریکا در حال صدور یک مجوز عمومی ۳۰ روزه برای فراهم کردن دسترسی موقت به آن بخش از نفت روسیه‌ است که در دریا سرگردان مانده است.
بسنت در شبکه ایکس نوشت: «این تمدید، انعطاف‌پذیری بیشتری فراهم خواهد کرد و ما با این کشورها همکاری خواهیم کرد تا در صورت نیاز، مجوزهای مشخص صادر کنیم.»
او افزود: «این مجوز عمومی به ثبات بازار فیزیکی نفت خام کمک خواهد کرد و اطمینان می‌دهد که نفت به آسیب‌پذیرترین کشورهای از نظر انرژی برسد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75543" target="_blank">📅 21:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cMwYsemP93JJCFip5hSbMUP2u0jvNQhU72rY5eM8OHrkaW0vW0dH21G-3XVRX7bqDLDxn7jorbzThW0juAMwr04k8Ime2MVF1p63U1C2ioM-s2ZMx3iBiBii2dJ6Rnj6RZfh7crYWNew5UH6oGCGH4lqze3YJB86oiONcb5KckHV3vkO5qcJ3uyxugPsiJeae_gPDNm4adbmQVE0SVg2tGc-ELxT8-JUHC7JyzhpvalxDJ4bPRI1yBfw1o2K82HvmhcrP7zQrg0n5MnF0Rz6_GwkwvfMTZIsZfRibzUm5k6J2NbjBmMIOD5QzvvZqb8nV0Jb9HGG8Pe2qhHz7StrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/me4dkpq3G8Ew2Va4aYQwNjMQPCVxPaDRDJVF12wKs_QptTb-mMiixjqXK9_WLZUut0G0i3MlAnndtq67z6lsFsZb_XsMThH3jMrfbQeFNlHIEuUNl8dDpJ6ZCgvr6ritH1TgIsPN65NEa2J6Mr-2TJZdYyWWjzAnR8IcLf-RsOHsLdpjyy1S9K3VYD6AxT1kCtqQSXz6Xm2OdZj5651KQOAWtIu1Ceeo8D3l1Few9EuSFxOC-Pbxx8p3teQ2B6_TtZBbcVvYRzxSt_fP5-d5MM7vFfXi3SobUiOcX980_BHZQamqbIxjHCas6ISHpCP1sbvQ5sHFtBQnZa5ifTn-Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس، روز دوشنبه ۲۸ اردیبهشت ۱۴۰۵ به نقل از یک مقام ارشد آمریکایی و یک منبع آگاه گزارش داد که تهران پیشنهاد تازه‌ای برای توافق ارایه کرده، اما کاخ سفید آن را «پیشرفت معنادار» ندانسته و برای دستیابی به توافق کافی نمی‌داند.
به گفته مقام ارشد آمریکایی، اگر ایران موضع خود را تغییر ندهد، مذاکرات «از طریق بمب‌ها» ادامه خواهد یافت.
بر اساس  گزارش اکسیوس، مقام‌های آمریکایی می‌گویند دونالد ترامپ خواهان دستیابی به توافقی برای پایان جنگ است، اما هم‌زمان به دلیل رد بسیاری از خواسته‌های واشنگتن از سوی ایران و خودداری تهران از ارایه امتیازهای قابل‌توجه در برنامه هسته‌ای، گزینه ازسرگیری حملات را نیز بررسی می‌کند.
دو مقام آمریکایی گفته‌اند ترامپ قرار است روز سه‌شنبه نشست تیم ارشد امنیت ملی خود را در اتاق وضعیت کاخ سفید برگزار کند تا گزینه‌های نظامی را بررسی کند.
آکسیوس گزارش داده پیشنهاد تازه ایران که شامگاه یک‌شنبه از طریق میانجی‌گران پاکستانی به آمریکا منتقل شده، تنها تغییرات محدودی نسبت به نسخه قبلی دارد.
بر اساس این گزارش، در پیشنهاد جدید، توضیحات بیشتری درباره تعهد ایران به نساختن سلاح هسته‌ای آمده، اما هیچ تعهد مشخصی درباره توقف غنی‌سازی اورانیوم یا تحویل ذخایر اورانیوم با غنای بالا ارایه نشده است.
در حالی که رسانه‌های دولتی ایران گزارش داده بودند آمریکا در جریان مذاکرات با لغو برخی تحریم‌های نفتی موافقت کرده، مقام آمریکایی به آکسیوس گفته است هیچ کاهش تحریمی «رایگان» و بدون اقدام متقابل از سوی ایران انجام نخواهد شد.
این مقام آمریکایی همچنین گفته است: «ما واقعا پیشرفت زیادی نداشته‌ایم. اکنون در نقطه بسیار حساسی قرار داریم و فشار بر ایران است تا به شکل درستی پاسخ دهد.»
او افزوده است: «زمان آن رسیده که ایرانی‌ها امتیاز واقعی بدهند. ما به گفت‌وگوهای جدی، دقیق و جزیی درباره برنامه هسته‌ای نیاز داریم. اگر این اتفاق رخ ندهد، گفت‌وگو از طریق بمب‌ها انجام خواهد شد و این مایه تاسف است.»
در ادامه این گزارش آمده است که ایران و آمریکا هنوز مذاکرات مستقیم درباره جزییات توافق ندارند و گفت‌وگوها به‌صورت غیرمستقیم برای رسیدن به چارچوبی مشترک ادامه دارد.
این مقام آمریکایی مدعی شده که ارایه پیشنهاد تازه از سوی ایران، با وجود تغییرات اندک، نشان می‌دهد تهران نگران اقدام نظامی بیشتر آمریکا است.
در مقابل، مقام‌های ایرانی همواره تاکید کرده‌اند که این ترامپ است که برای دستیابی به توافق عجله دارد و زمان به سود ایران پیش می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75541" target="_blank">📅 20:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MREcMBRfVYpKpAdzmhITixdxZZSfaNzcb_g25EnwE7P3nJyzVLY34662FFAbXAll0h0hNSWGk3YIKV0tJpFaCno5EXF_H4DbLlbPJORYYVltBsIQBk6Y-Ykj-0jNlFBuwhkvscCXhhcB34N1SRoSFPpT4CyDlYGhe9YwsqM9AbPK5cNUNQeCiB8oYAHWe4zQJAYgTjHGT_5kvOSAZHfyKhXm5Kf_YSF4Xl4Vqe7JMUG1YizB47JDmiyyZsezD_ovfUzHd4hKNT1ndoWUE0-csENCpKfFK282f5VaIcM8TGx4SozKFmDi9z-w43T0RJ5UxGq21EFgr3-_2znE8ZiRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEfl4IRQ-uNdyDPp-jLxNxQ11vJR3JcJ41TOfR4h2j-JGSAy018W5brj-s7PX4up4YEX5JWAKdYmGnrpwKdkGgNlTsXSURUAnNi3uhNcQHZF8D-FKbTErPcU21qOltsT8Kv_GKmVd1VJBbpTJez-FZ6-yvApNjkTKL_0P9h10hGoM5K82lnqDLvpyUpm_J1Tu0xWjc4g6NncoztFj4FmGuZkjetC7lI5M1IOhCMnVvk1k-g2Y4aUt-Kd1UfjnI3uct6i9F07jkBNxmau7qVltHbHV1KBgSRu2v0hwFsMavEq51V-aeiplLU_5SzI3efoVOeWtLZQdrNBwy-q_AM7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTFmGHUDwvQqq1l2JAWlAXJf7K-O8O8KnTLZB5koL1iWmvYfSvaUedpSd4Np0EDum7MdzsEkoXSTqJCS_1kp8U3Wq5G05SmbHdn5FFZvSNWEblsQs3GXrOe31tnHHFF6rsy6hK06WPiWvHYoGaIDdTi0Eq7Ia3vqhz2UrctscTBDOlZpdLrgTyrO29GquK2WvdMbVkH8YqZXVeFX3_11CzlSRKOmZQ5Lcxm2c2k2XIW3Ywk0BnnIIFn9DAKL8de573Z4NI1zH-iMtPA5H1IuhTNI_9LF2yyBhYlEWRW9Q4D8d6HhsbolQFFZsQFyUrKtKdUw9dGx_BdrzQSwbsFIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vcvR0VKakNsmzJQKtWIIQOGk3sg0kEHeOf4k6sbcOQNX9naEoBKcw4iPLvP0kuYSgq8eHyUT2bgYHXDFCOyUu-FLx2RWii9F3pRLX_SIfpMxsrDm8AvHN1RYL1bXR0y0HSR92EwVpPKbpC-GxDpMzTnshcs8Qs4phU4p7UFVsZ0RRaNemvZQNw0JO4oTHTjZoq3YmfY5372eA4GSAGWZPjeAgqN_7l9Tr3vMvfccRYJUlnsfA7Qz5BQwlM_3Dgw-TvOM4qDQ2anwu7P8YFPycyRjZW7JXBkmtYXxdjTVe4GCA-KCBVfGNK-xeFbZXXw6DQ0_q3qnQkVwPkgPUOW8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OAd-4HKQuWPKdXt-VjZMOUgz27W749cP9S264KkOBCQtVa-UyhuyKqTzSI1_tzw91tYv1cN6Ez76Q8ovZBFgDktropOTJx3TYG6-aIrj-YKjDBUjjmvgSgJo1hNSjp6pJkz0YgmQItpgTV2fPIK-KWtDij0KqEoICump14we5TBBPmELdVIjv8DoK-gDIejbZtReMk_j9ltMrTaOkST2qyRSgfraWH9wMvYXANQEHsGqwejoDZr887B0gOktCsMfIAkvBUfGG5KAPi1Vim8uWr-3kZ0Nw6A7eyB-VJbSVp7V30Syv7NGjF40hx7VmTmfbaTUEW7KOv7SjhGlP3hefg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت ماه به نقل از «یک منبع نزدیک به تیم مذاکره‌کننده» جمهوری اسلامی نوشت که تهران «جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.»
ساعتی پیش از انتشار این خبر رویترز به نقل از یک مقام پاکستانی گزارش کرده بود که اسلام‌آباد یکشنبه شب طرح پیشنهادی اصلاح‌شده جمهوری اسلامی ایران را به واشنگتن تحویل داده است.
@
VahidOOnLine
خبرگزاری العربیه، روز دوشنبه ۲۸ اردیبهشت ماه، بر اساس «جزئیات درزکرده» از آخرین نسخه پیشنهادی ایران به آمریکا، از مجموعه‌ای از خواسته‌ها و پیشنهادهای تازه تهران که بر آتش‌بس، تنگه هرمز و پرونده هسته‌ای تمرکز دارد، خبر داد.
طبق این گزارش، ایران خواستار یک آتش‌بس طولانی‌مدت و چندمرحله‌ای شده و همچنین درخواست کرده بازگشایی تنگه هرمز به‌صورت تدریجی و با تضمین‌های امنیتی انجام شود.
بر پایه این اطلاعات، تهران به‌جای برچیدن کامل برنامه هسته‌ای، با یک توقف طولانی‌مدت فعالیت‌های هسته‌ای موافقت کرده است. همچنین پیشنهاد شده انتقال ذخایر اورانیوم غنی‌شده به‌جای آمریکا، به‌صورت مشروط به روسیه انجام شود.
العربیه همچنین گزارش داده ایران از مطالبه دریافت غرامت عقب‌نشینی کرده، اما به‌جای آن خواستار تسهیلات و امتیازات اقتصادی شده است.
بر اساس این گزارش، ایران همچنین خواهان دریافت چندین تضمین بین‌المللی برای هرگونه توافق احتمالی است و تلاش دارد پرونده دریایی و موضوع تنگه هرمز را از پیچیدگی‌های مربوط به مذاکرات هسته‌ای جدا کند.
در بخش دیگری از این گزارش آمده است تهران خواستار نقش‌آفرینی پاکستان و عمان در مدیریت هرگونه تنش یا اصطکاک احتمالی در تنگه هرمز شده و همچنین بر استفاده از ادبیات و چارچوب سیاسی‌ای تاکید دارد که امکان «حفظ وجهه سیاسی جمهوری اسلامی» را فراهم کند
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iruZmqkMZu3O31RLg-u-_fFHIEQYCkXwMBW7xNTU08J4Q9UHYvTM9tGeXbWvEoIYcP7JbQ-Jaw0wYSkvE1-1ULiC3x5VOeJfB8FXDsq7jl66dL4y8rjebOkTixbi9jQ6nLJLBESKoCECsExjqiDsvLtoxefiLPIVNJNmiJ7H1JtMncK6VRFqAsKvkyRJPw7WCnFx_eMUXmKW0MyMX8bMaRcdfKO4yMiQQuZNy4YK6A4tO8DVQ4vb2qcaTYN6nmJ0r4ukPJbeuq3bu-oF_M5n1GNrgkhu3IZRW4MDmLszl4ArnHtLMm17ghEEGZYsuO4cWeUKvnCyOq2sp02rlxZdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHZOT9cuzoc-5sSPXASgevO5N35VOWdZuBgGbVlcZZnd3vOHWL-fBXv9xLDdS1DcTiF0dg36lMDzVYc8lwK2x7LJRIit2omNXwATpf1POKPA8lTwSl7IVsMAWKTJDfjv-BaZIRIdwprmuH0N9eDzqtc99VLmzAU87wktJk6R8U9wy5svvN1miDw5b6JFnp7pUXZejDU0tfhWRq4qw2Z8ruZRWLHErrtHOCfttaETJQybnOdGhc5NY7nsI44UwcMi7pPi5K8dk8DwMiKM5wMkD5ZWQVxKnNXXLM60SuW9us24RWWCuDDkBnFtOs9KpIqcw_fPaaZM__w5jvAGR5kr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjB57m2ymUqHq-svXfzvRvDy2CT6nqANcD0_VWfnl1hPv5fUoIpaH4rZiUOHELLONuOxE5qXfthFNfblOM0AWiAXCHzE9DJ0I3g5UFflKw91Wu22NeQ35RGE22LEGIzLXLdEwVXZb0Rv0E2OJyXLBQs5qNWY3-tSSJTdbre1xKoxHRNIvv-d05oKx02YJWdFQj6fXZCmEsWBf2q5vCXnX_rXUJNRuV-mmWISN0ZHhPxaW2Ds8YYD0JpPjrRVJL9D3K1yllMqVt28WFu41L4i1KHCSm-l7xv5JDDOvLkzTt3fd8dBnXyBkIm0nXzVsq7mzK5Asb-CqVQdULnCMZ756Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6KKzLF6mpuXLvar7B_K90Vqk9bwW-lkGwkrrWW7zK1qAdNEPt4IEsjT5xvCbq67CrC1-VhPZO1Coe11nrE68uOSMRgZ27jqhbLguCF7NF6w_KLk0MXFrnr_oCxq8eM9weSjyD6ExdGnzbDpBbe5eBgIoCZ3nSXLtBYfYj8zw4l9Pm3ZkJVFFeE4Ljxb8CQElhJ1NFJf73zmKqfYjEddiAS7POK2dNkDeBuSkwcRwEt0Nu7bA7HNyIJkoyqRuKO4GASsVjnENdhb5aWa4NxFVYLqlk_WzNuHLDfp_-la6uWOboKCQglMK5wgttViIWHjqUumTGdTYs1aqJRNwposxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rV-ZpHAYe4cLDKAmqwBb6YcdnxnnaEvYIM_JDotMGnKWmjnaPxPzoBtcJf3jKm7YqRMwywy7ATU9QCHmGRdzVVt66rBe1DV9PKzTrDnYSH-qAcB7joszMqsJ_v6fP5YfCggPIDcW9mJnx9qW_klRdn3UrCnqdIDSlqTXPV9y5l-X8z-JNMI1YxzNC5XWf4kRE9cyAsQ-OjBmg5F8BkQXrv4xS9K2nXae2mJG7efNNnMZ4hcklxrXCNKLhcNxQ-LG6_j2CT8R-EmQPw9fHCBx_2EuASpGm0--qw3OLI5sROffZDgnOFyBLrOnPSdQK7tMN_JJDTkHiZYXypi0_AlV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bG71cichYw_gpa-drQml6W9zuvp7LDSi99BFetrHqkI5iSG70T3K2xo3pKORIN2uSO_IG4SmCVGcTt1lDsBEcolL_ZnD28dcsMKr9-wGHG4zLR1iB6GNGXtT_fSMbvVrrCGU_cic4kwEVQhE5wVPD30en5GrLDuG6z8cwvKDHNmdaYMtHHQPYT65ZOp9fbXXo71_mdJSoWI8VACLc9GsXUFSun9EkvJ-H3gIsv1gcXj6DZ3x4XsZ7Pm1bb5uL-Blm7AzBdM1z4KRaWOlgN2ypGPuN7IPipGZub3X6prPtroITsOU1Tu3mnISrLGBYO0-0KsifM8QyIhFdxvyehHGhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران می‌گوید روند مذاکرات تهران و واشینگتن، «ادامه‌دار» است و حکومت ایران از ایالات متحده، «اصلاحاتی» در پاسخ به طرح پیشنهادی خود دریافت کرده است.
اسماعیل بقائی در نشست خبری روز دوشنبه ۲۸ اردیبهشت گفت: هفته گذشته، علی‌رغم این‌که طرف‌های آمریکایی به‌صورت علنی اعلام کردند طرح پیشنهادی ایران مردود است «اما ما از طرف میانجی پاکستانی مجموعه نکات و ملاحظات اصلاحی را از نظر آن‌ها دریافت کردیم».
او افزود ایران بعد از این‌که طرح ۱۴ بندی خود را ارائه کرد، «طرف آمریکایی ملاحظاتش را مطرح کرد. متقابلاً ما نیز ملاحظات خود را مطرح کردیم. از روز بعد از ارسال نقطه‌نظر آمریکایی از طرف پاکستان، ما با مجموعه‌ای از پیشنهادات طرف مقابل مواجه شدیم که در این چند روز بررسی شد».
سخنگوی وزارت خارجه ایران به‌دلیل آنچه تبادل «نقطه‌نظرات متقابل» طرفین به یکدیگر نامیده، تأکید کرد که «بنابراین، روند [مذاکرات ]از طریق پاکستان ادامه دارد».
بقائی جزئیاتی در مورد اصلاحات مدنظر ایالات متحده ارائه نکرد.
@
VahidHeadline
او همچنین آمریکا را به «خیانت به دیپلماسی» متهم کرد و گفت واشینگتن دیگر «به‌عنوان یک طرف معتبر» در عرصه بین‌المللی تلقی نمی‌شود.
سخنگوی وزارت خارجه جمهوری اسلامی تاکید کرد تهران در مذاکرات با آمریکا همچنان خواهان آزادسازی دارایی‌های بلوکه‌شده ایران و دریافت غرامت جنگی است و این مطالبات را «حق ایران» توصیف کرد.
بقایی همچنین درباره تردد کشتی‌ها در تنگه هرمز گفت موضوع ترتیبات جدید امنیتی در این آبراه صرفا «مالی» نیست و هدف اصلی، حفظ امنیت تردد دریایی و صیانت از «حاکمیت ملی ایران» است.
او همچنین در واکنش به گزارش حمله به یک کشتی کره جنوبی در تنگه هرمز، بدون اشاره مستقیم به عامل حمله گفت «نباید عملیات‌های پرچم دروغین را دست‌کم گرفت» و مدعی شد هنوز مشخص نیست این حادثه توسط چه بازیگری در منطقه انجام شده است.
@
VahidHeadline
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، در پاسخ به پرسشی درباره گزارش‌ها از قصد امارات متحده عربی برای حمله به جمهوری اسلامی و سفر مقام‌های اسرائیلی به این کشور گفت: «ما قرار نیست با گزارش‌ها این واقعیت را از یاد ببریم که تهدید اصلی کدام طرف است.»
بقایی با تهدید کشورهای منطقه از جمله امارات متحده عربی گفت: « اماراتی‌ها از اتفاقاتی که در دو سه ماه اخیر افتاد باید درس بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPIaqVMfcJ0Sw0gBarccUleiW9Ijunrb9c6wBf2AS6P2A0RSXBYHiWZ4g9oYfVG9giFgLB3NgBhZ3-i8ZxSQFTtHjHwdFvXNFLKiOOZCz4jY-ZaZLpc018fkya8S8CsA4mkrn_90vBB4jt8YX_s4qu8c89T4EcZuUdCbmuNgePLPsowIk1Y1yR2gD3Dh7c2diEESfFht2kmvYvvhK2Yz5sahMZTqYfuxhU3Mfpz_EJQ429lolcCs1jHnwab3vu6qoknwQslqh7-XExHcJNWBoZX9p-lEkhN-zfu6No6qkEwCRa3BFq8XOlsZOsA8kuH-d7S5vwMAybr6xtx498m45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/akDcg0nmUi-Q32oeuZ_IbKBvpiU8X9CgWNFtjry7u-4PWgsRmf9UA1VJ5NXJrSRbFqjED3vYQIKf44s-ZxqbpWQDpYkI1DL3FWeQxBHTt9xWPIsyTizXqHajhD6sTK0SHvrXwMC-dk5vFaHw8-UAL1vc9_G_MsyaO8hVsdnroHuE9-Juq9RPTc5x9kB5zAMyhczLiESK-st-HRQicbujxJdTNlkWVuKZSNHG8igi8nCq7gM9XwvIe-1r_cev7kojuilopGJQZUIR--6gOoS6k75T2I3ot97wfMQ6628MMtSSoekKxRp2e446Te_8PIy_hXSaLt1BiNyWXqW4ORVdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل روز دوشنبه ۲۸ اردیبهشت گزارش داد که ایران در سال ۲۰۲۵ تعداد «بی‌سابقه» دو هزار و ۱۵۹ نفر را اعدام کرده است؛ رقمی که باعث افزایش آمار جهانی تا بالاترین سطح از سال ۱۹۸۱ به این سو شده است.
این سازمان مستقر در لندن اعلام کرد که در سال ۲۰۲۵ دست‌کم دو هزار و ۷۰۷ نفر در سراسر جهان اعدام شده‌اند، هرچند اعدام‌های انجام‌شده در چین در این آمار لحاظ نشده است.
عفو بین‌الملل گفت «هزاران اعدام» در چین، که بیشترین استفاده را از مجازات اعدام در جهان دارد، انجام شده، اما جزئیات به‌دلیل «محرمانه بودن داده‌های دولتی» در این کشور کمونیستی نامشخص است.
این سازمان افزود که آمار جهانی سال ۲۰۲۵، شامل اعدام‌ها در عربستان سعودی، کویت، مصر، یمن، سنگاپور و ایالات متحده، نسبت به مجموع سال ۲۰۲۴ بیش از دو سوم افزایش داشته است.
در این گزارش آمده است: «این روند بیشترین شدت را در کشورهایی داشته که مقامات در آن‌ها با محدود کردن فضای مدنی، خاموش کردن صداهای مخالف و بی‌اعتنایی به حمایت‌های مقرر در قوانین و استانداردهای بین‌المللی حقوق بشر، کنترل خود بر قدرت را تشدید کرده‌اند».
به نوشته عفو بین‌الملل، «افزایش بی‌سابقه اعدام‌های ثبت‌شده در ایران» در حالی رخ داده که مقام‌های جمهوری اسلامی، به‌ویژه پس از جنگ ۱۲ روزه تابستان پارسال با اسرائیل، «استفاده از مجازات اعدام را به‌عنوان ابزاری برای سرکوب و کنترل سیاسی تشدید کرده‌اند».
عفو بین‌الملل و دیگر گروه‌های حقوق بشری گفته‌اند که پس از اعتراضات گسترده ضدحکومتی در دی‌ماه پارسال و همچنین پس از آغاز جنگ با اسرائیل و ایالات متحده در اسفندماه، استفاده از مجازات اعدام در ایران افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv6YvT7wzWtsShztYN3YDOIMaQQmW9QNa1-7MZDGBv_AbEvdsuyW5YcoG4SI24Ro4GPL74nHWMmlAVDRepG4tkFEYS6LT2GIS96DU7qDEsXEW1QDsdP9LJoUqD_oJLRQfOmT--VE34LvXkFMLy1b6oByHuz0XCosID1dVR6oUR0qqzjW2i4C5ONxaDbdGtP_YOtd7q747tFmZEF718GPnProXIt4mI9Dfzd4rZtDUmS_s3juJ5bhDNRBpzdyvfGMhJt0EsxS1DE9k6YH2WTEWZmD3IjIAqQ4lDoZHYNo1i9mfLrLbAMw7ROUCt8t4Xa-QX7wIGioYJjLrIp5X-FL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACk1j814gkY3amXP8Y-gULxC5lLYO_bhBDX9ogoKvMlK-9w-PU7rXgIfN9AVPJPkhF6bTu2vj9t9V2lDdFIrq1r5d_wowaJlysvpJJWHKmFRY-S176-lJF1s7JXWGn0hlFsBOrXJJ-CzSrhQREtH4Fjy8ZgORk33BJwdIUNiH7BQDxSAhgqcyQ6TFFL224ERoTNu0oT3pyxz5ujedipUb7XjIG0zyE_l_yeHXrK_q6LNvR7lPjJShtz719OQU6JJA9L6mOj_2GSdJCvSKN-qK3yNdwabFeanMGVAUK5a_uOlYocBL0fNVD9RpzKAE-e3JcpZpvh0aDi_DP0lUgiLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mdZRKmaZwSQDlPdpaVnneZhG_n-EPMvM9PpmKIHK3FobpXuJkFJQauwCFtz4OOXUV1Xb2yghEcqXUwq1TBpXTh6hcOj9PyGLfmlsMYKplixh82TWdqAGkVyQLiGL7r1sa8FTUsVOD_9uIwa5MYVKts043RoUSmTPFRbiWr7VrcgohbY9V1Zc-7LZ83uHgc1tS0sZJgHDD5LyA5r17dah5mHzVPMXjDLafkWMcShkkitRaqWI9O1GpG8e26y_AWM71XbgfF75uBnrfpaYQNw2soAN1_pYB2gAm7ytYX4UF8KTMBPwVgMejomtdcitFKFxX23zdWdJgd3WSFl5DkJzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ترامپ به فاصله چند دقیقه‌ چندین تصویر مرتبط با ایران را در تروث‌سوشال بازنشر کرد.
ترامپ همچنین یک تصویر جدید از پرچم آمریکا را منتشر کرد که در پس‌زمینه آن نقشه خاورمیانه به مرکزیت ایران قرار دارد و از همه کشورهای همسایه فِلِش‌هایی به سمت ایران نشان داده شده است.
او همچنین چند تصویر و پویانما را بازنشر کرد که ناوها و پهپادهای آمریکایی را در حال هدف قرار دادن پهپادها و قایق‌های تندرو جمهوری اسلامی نشان می‌دهد.
@
VahidOOnLine
طرحی که سه‌شنبه از قایق‌های جمهوری اسلامی
پست کرده
بود رو
دوباره
منتشر کرد. ساعتی پیش‌تر اون
انیمیشن دیروزی
رو هم
دوباره
پست کرده بود. تصویر ساختگی یا طرح گرافیکی دیگری هم
منتشر کرده
با عنوان اینکه نفتکش‌های خالی برای خرید نفت به آمریکا می‌آیند.
اون پستش
علیه اوباما و بایدن با طرح گرافیکی قایق‌هایی با پرچم جمهوری اسلامی در کف دریا رو هم دوباره
منتشر کرده
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqSwM9BxlGw_vea962PEqETXqIRYvDsvl179N_dUUBOG7VREbpa0QtSl8OEfI9IQn_D9DNMqMoWGbVwxFqG6ySMQBjv4LaQTxY40giLe2EvXp0zd8yPfcXvkMBRBbVV2ZlWYrMdXewN2T00meJ9oYDkeFWGam60GkV0RiHmPvIN8hKkfl0I9Z5XypaSNLPLaj-4UIrn8sWxiya6PIuMvcd_Qmw2tXUq-Z_0sT60sHyQjUDQWYz4GxP_STNijgY90BjkSxIQs6nK8euF-vwMT8I6MoWk0DYnYB9JtpYaq1BZnH8Zd1nAK7ci3lOOqpxCrfLkx8CUDmG-S5Mzevx93IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vehTAlhMtVQbSe3i6mWwHLy_NmI81TPeN5LM8lN0bVm5jddsteHMWSFjzPe1WuPa1IMTXKxHIrWbnnzyP-ASQSOiAYZEIMW7BaxRZgx4VBtGOSjDpoE2BFa1gxdmejlA6YcpwYc7jhtO6dxgKePO06K1-Kl5SNdZtcN-ZdMr6PNeYwRCmvJcyTWBInzg4MhVZzLsFc4uYclParf0MPucKcd9TXEoDGdy4qj4uvnUxpaTvuZZPbfYECnNS3fBkxxLOqk6wFnM24FVd-uesDy_D7b47BqJdeP5w8ilKb7wgfqhe28aI_NVctsj121SmXcuM1YydCXbwBWONl5BVEhWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MegRGBJ6MFBYQHRJBBlRkUshOd5NAR8MujD8maNxThF74dK_I1zRFAUrRIuXjrv4RPBa_EfT6Dvisk1i6BbM92zLlou9Zjoy87J0RKlZVzXh3450A-AuJN9cPOpwcbPVBYXe8jdnJtTqq6Hgtg4CXXIrnjUWlQmX5CkeX0naYE7Cznltoxq90wiSLemmpYmQ0K2mGay6n1LYlk-1wJy7gYEuCUlph9Xx4Jy5jxbf-cFQ_9C6R2OaDSN1XMGJIz0yKZucH72HgjIi-Nq5J3QDaG449BAw66WSoV-Dg4v0CBSQdnzbNnLbIHSD3gq75tcss9wBz0wPqwuMjfdy7Z18Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMtXiPly6N1U7dmXT7TJ-Q2uSbqEeV2ZcS_ElaXW1bsVMefIyp8yr9L3iGYPO8ICyhHsYpYYCWFDHznwqDeCVMPUUI0EERvG8YE9sLnWYzht2ODAWO1KlSWAuCx-S269MRUCZOgiyQqIzptK5ScAB10FWBA7MdgqBcPtfNqs7eZi6AxVlpP6NKQeKVz_6duSv4icWa3xA4PrAbK53Iu8Efo4bUFWyZtkzpawKkEy6zMWj2n_zdceR3HtoQ5eMUilkSUEWugLZ-zWLm6HrpKCmcr5IXXwc-eQz_uqMO8C4Dygn1BXalKml_ptxxpihrVoQy2rtegUAwayz9a4mLqzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AQua48E476j8n-dptWwFfN8d9Rf7l0AQ-LangQntn1jiW4chQ8T0HudDFuFfRrAtxSYd7l0Kut8bWbq-uEZnobggTY8JzJ6e-x-dT3M5UBkywDoch0f7ZYym6R_k6KzaIUVRGqlGjoescNcY3UtlEWxac8StEmbqsztSD5kQrSr4ITqINha1RuN1kx1tRWQ4UumpWhf_ojbFcRzFy0hoVv55NiQ17r6TSTcUntlzfGzxxCKWuXeqrPkfsfbCkG0v8_v59QrwzxCoYz4J47XPFCq7fqvHXOKSLuW3ENe-ftMTD6NvTP0Tzo9JBP7JhADhvbjwIaGljdyXrKgpfiS-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WTuacxSbaIES2FQMfoXLi0vhWxO2bYItkEaOcJ_sS11MMH5juV6nP6j_sHwG-Z7roX5B4KAmsnvgW5oxnS2gLnscURrGxy4616WE2-uNKGAiTxh8JD28QWGUHpLhlUNwYaxWDhcPVd93xWkE2Cr2KqoPUMimAbfPvZHfzIFlKK1seJ6Buru0y-6gvqN7Vm016xTBxcXz9Tyftw5nvLgPcV13AhaGJoZ-D9Mjm2GhV5PAzK_lGBFmQXRIaXZTgx_YPepoDjniZXlH1vKdw_OaccFtpEzMJvKCLbMsof1G0nadzGknrzb4qtDTqsPZk6ueezQ08Q9-XBYlk6wExk0Xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOSumR0hDWmfBzjwQbJDLLTN-zCNOWLEQDqp9PwuvSyQnv7irm7-D_MUqT_TDias7h0gVTvYSK15ioNPoSgG3I-flPJnJoYtcMN9U2x3-xdA6eQVzMtMazbXeCQWDejLJAJYxbFVzF0I8fUUM32Ttd_Uh_OLrtgx2X9E65h-1927RO-LiIbahllC170xl65EPys25Mo2gSMzEEIsAhR-5DVBmn5fcZ48msKg4o07VfN7za_8Au9S9Cv8TgGCbQ6Xt4a59xfnYzrkSvyRyCvPEGEAI3qMlIPlN7zgfeBnNN0YP3I-0bZb0U2UqR_0g7ykqLS7N6InG7rCmMVc7PEy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pz5UyTFblaPGxavH8fuq3IWGc5LIdlYyQpsCKYuhKcT4B7mlqYiW_i46anvyi8V0h59-Z6VHwBhSD9jUpXVmsf8n_-6IVsJCZVrimUpZR2JbppWPkzF7yR7slqd1IEkrXWVeiSKRkXn95H-5fNNsg5owmjJFRUc8Fjzb3pZ5RD_CI4z3CRlvfuEtLEqhXJlQ801MQMHQCM6xKelLdb311kJvfqmxJvhyoASkCqrEFSYsFv6AjwBSu4eUBqNrCuv3Se3o5eJ0wis6oUfbmV97Cbv9jumCimGGOsu-uz72lzn7XJi74DZ6uUemgAVuikygYx2VwmbNcPBpMP4LSUb7gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZAE_-yH1wGIwS_dmpdACntjnLgsWRGm7cF4F9dFIDgvMaYRF9SFw3dZY2HiWCyMa4snB79dwnTj7mfLmWwErrEPuAJ5ye4nhY6pgsvMS24UOpBKiJQEzc2pkf36UxJz6GolxImIxonUVq9NVHA_2fcmCBKMOsrJ-3ee7yAiez2E7K1I9ovnwQtb8RTT5FUhUpdhgiQDioeVsNtokaCrGaLwY2rqnijYLhdGBjBUwbY3NTeSpg8ukVvTtXiHFM2Tl2hpAqTRnqYpZHf5f_hAVN7YbZsDbxM6ZaN6ikzEDt1mqSXWQTd49qRi5n2Pu04Xi4gMi_M7aouk8Yg3y1xbguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HMwnL9LlyWCYML7-kHBe2iNE4N5RkVvGa-Fn8XSB_ZJQWi-xukIW5kitMcV8aleN8ZkENoUz5E2TbMsZpgFDvi2f9mQv3yZVFvtyGee-ufYZ6ksCsiD4dyZ8TCaAfkdV_awNbUNs6wXKTmuRTcvOQJsXzo9-vLqsFZaRrAd4Ig5-gghJAE_ihwWSPJZFPZqhCnUvQN15cOb0kHLL37OUn6FwkvmIFWfh7N10BqwRYwrbR4PUTWZ3XuqG3zYa6Q3X1A4Mt3L2Fj6Gw3_IakoetR2PuaQC-oGqbG0orOTORGgSsCytmtSflBwXoYFK9FJO4WK1GO13280GXb-Zxh11vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxFLp0J4RyP8XFccFTxV9zY2l-t8lCtN1msRYbSyiPU6ClhEYVqvxt_p9mu-aD9XPGJX-tC7oCGz5PZraf8eQ9X_xpKty4HTMpK15l4CKCiyjZVL9o-oxE9yG5CvKbseoVNhy4-9_6oG9849q8OSX234UiI96my-nCRI9Phim2HKy3Ul9fOUXFLeA89QzWlHp5xlfCmcP7sOkHE9GZkxOmW8BT6tnD4_nqT7KMESwMeCJFa7hsmpZ9qXrVIdES8jC1GP_SeXZ5VAscT1LTBbO22OHIZ56Hpw0lGw8slZTbLzGM9m3KZk7inOLL8SfZ2I8tq6VF4B53cpSF9XIXvllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BypYPjiAia3B1do8UDjW7Itd0UOLHjX6uzh0eq8_qJxhLM2iXRhFz4O_05R0lSw5wRsYBnXdGP_iKNqhlSE4ANWn5jDwED9kfFyarQNoKvIEVsYcOrXzNtjEOwAxBbjkqjZo-aHhBWhpcILBku0nsS3qjJHzneCj2Z0dsPZ-jn6jN5FsfANynUoP7BVC8yQ_5vvH-hh98Afl9wwJPGW17BAQ_I7s4X01NGQahPWu10phqGF7oudRVecx5meq-yF3obqV5niZYnUY72iHTEsHPo5_sbd4aRTIfeBgGbysbGcnx5ozg_ip1cGyH13Da5BnWGsa4dhq7_iYouYUbIq_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYzaHArYWwdY0V7VPkVSL419xMoNmFu0oJoNatZlo9Jpv8HuGj8u015Jih3EALkO0aQqVOZGzj5q0_l40DyARxT2DSebcfVG3jFUhC5GoRJPJ4dy90Kiw8RmkF17RZdPzszSwbAikT9u-dOciYI9-yx8wOf4rXgzquXJ9ilRyCwrx27on7k7YF92amVY8oiU4Gj5h38S6Q2tifoVdiCKeWyYyefsLame1kMQgqOlki21FScNdmXRMHRDnp5B863iUf4JvQMWSejW_d6_gwvkYxMJe7du-KBvdjEuvbbqbSRLAv3yJw22fRYrg_IC5Zc0CEdelvN8s2SfBQvbULgrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKpVAyihUK5pPoZUfm1QBgVGmuU4yrsxPCu8gds7isc4KvkpC7rns0OuGBZb1Apvv6mWqqGn33mtMBO2cX7cO4mciGcixcvbr51tA8D-BiY6iKbLwZeNB5vdpJoJN5kvgc1J2yuDP-pbdyEYdwWX3if8J7BL2tl53uqOIAbwq5FJBqcyagdKdUkU4gNc1AS_pBRkrRE0HGrwW1E84xRZNhYKTcxtF12kAY1c1GPtVuIRzKpiJ3xD2YgCLTmpPDqAQIOwi9zfKqYTRw3rspTBT2tAinKhXm0-sD5tx_4eT6SCc5TE0GDg_N4i1H43SZWz3nn-iQJ0l_3Aw2GPRHW4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VvaQShUKb5MZjWETEmMeaqFmm5qskrv3xd4h8BoPIjxAsGQAUTFX37YZdc0g8l-zyxw2CvjQ_EfEwxdQ-To6GIlvWmO847j-mPSmXhOfrhejyFMHaOgtzUrNKEyAb5m5opfh5o61KYCRirVdUdDfBEEWuyrw41ioiN8cF8NODUc7_BxexR6kjxvCwWza2eXN8TvIGrCB5Rb6_wBLe6zIpkegPoC1wLw-Z5-K1pyXBU5r10F-9DXeLKHydCnrpiqjhK9lacUxi9zrSZVT42oz175jFUu9pFbE-dHjWqMexnozFr2NhYyUTMyVB94Yv4B6i1BnVLnuypzD4dOGF4HKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IBIpoBDxofdednS4cgQhEJYpIrw8AOn1WxC4xSnKvXQ_RhWgVvjL-lpwZ0Wst3zqTGw7Mqs8BPwzaTVZJn8soP8GjpxWb43hzaGbWD92Ch8kRU2_cC6ABJvYMb83lBSW5aiSZRg_yYwPFq1kLL1pCbp5zztG9-MIY3u40KG8SpZ_Xv7JbIsXytZiPGwz1KaqMpAwEMzY15APcE8kthYOTEdl3QSMztd4Ueq0C2PzgzYPnbfRW_GrdHFLdsKMBjKnhGXjqROhT-Wwx1Xf1SrqE33rpllBQp3zBC2VmgmB74rKD9PoNyZqyCA0-U0BMNKKoDaZdv93XwjqBg59GKX_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=oMxq-qM_DueQ7CaryujBRGpcpUY5RxaT_sHcNLJ8PB_2ctHZjBBA9MAsW3Fk-KqGbyGClu9lYVbaX2R1hS6XJx9hkt8C_adFS8nGmjNR9tQ15FBRHU6BC7QfygdcBxi6HHMCtfFe87DTOCj1qYSMVEHDP-HKjW5XsXFT9_apn5KzGQUJ26lj0qDMSc_nxDSsGz34cFKJRHJnI-8Zw0CzFCw7CGVE49er4ON10gFW-iodORJJYPHdnMoqhWHIueg8n6UmH2fzPTBggA1UGmUFzUKljMgXxNascum_iz7p9q_Ox4gwzbyDY8CT41oAKaVOyXJHCS46HE8QvF8Jpgqcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=oMxq-qM_DueQ7CaryujBRGpcpUY5RxaT_sHcNLJ8PB_2ctHZjBBA9MAsW3Fk-KqGbyGClu9lYVbaX2R1hS6XJx9hkt8C_adFS8nGmjNR9tQ15FBRHU6BC7QfygdcBxi6HHMCtfFe87DTOCj1qYSMVEHDP-HKjW5XsXFT9_apn5KzGQUJ26lj0qDMSc_nxDSsGz34cFKJRHJnI-8Zw0CzFCw7CGVE49er4ON10gFW-iodORJJYPHdnMoqhWHIueg8n6UmH2fzPTBggA1UGmUFzUKljMgXxNascum_iz7p9q_Ox4gwzbyDY8CT41oAKaVOyXJHCS46HE8QvF8Jpgqcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7nagdxCRbqms9JUvi1_t1Fv-YKi2L694oI4Hz-nV5IVYxhwXDdnRoVG66rUwqRVPgoPJjxHNEaLYjQ1aNPW2al_gCvWMp7cdg9k7ks4eBLC6QvPqB733X-S0pshjRV--2QMMwifRhv1zeRxSbOmTw8WiCDkRTEhAQLvD5aMNCnSYTELBHvlcXjh9gD3JDjh1HR6Ju7nfWZKx_t0nAIUBmbCbe4peeylDhB3IRetf_1briXjceuOy5ewLQA5UGAu55pK34gfdymStn_Zppsht4hTE0Rv2p1KbAb963Nb_Tvah6QgfJ9byN6gc6nzCxO7jloz_kW9T55235jow46ggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJf670i0jG_I3EN-7M6VTQtSxWxIvedfaL9AWnrSpw3yxPzC93AliWIUgST0k7vBrXvuvN5oup9eT1mm4XRjUWwdWVYLu7ABOqRyILRaSuGhbp4IOPnpsc76xALP618n5MdsssibhK0TlGuNdjC44_kWNdRrhC9chNqWPRGUvhMVdj0Q_eKoCk5XXo2OJMCJHM255C7gvEDNu0XxsfY02wFX_6fGBZnTQN6qnVXGke5avsJxSCOjok-4XUcarHo0JJTuWdOTfLUWd1hP9yCjWfBfHCODrfLF9vaMP-EgAuOqrhZCOQdwRzj_THg8_0RU3bSAfke6qn01neXBm9OlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mCYR_ny9MaqNuqWx1eouBTYDd7GOKHQIK-Pz-DQWojljdJ3triaLp-t8lgFdzR1opnjqCZOPun92ClCCkvgGfkeIYtlJyH-p89VCesvRBZj0aKIvNaHY-mYj99oOr8ZClIX7vpAjZB40ezK0Ojy1vJs05W3_rcsBGJcCkzfyHVWwUDGnRpxOvIHU857agpK4NvJECtawLlZanocnsEcvhuvxs-Gw01RPKPpnbKEgRpb0ndv3AOdNEcsQxNsPCpXTuGLJSWoAH00gdgwCcTsY8uH6ezA2jlANvuc6PSgtopoIdR5D8SLBvjI1ejMf08J8RxS8dIGEY5jsGuYr6KNFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y2HW83CKGxnDz5Zy4dBiNQhk389rhTpSldoAE-4EZpnF2QnUTKulloIwmSPwvzOke8Z0E_8VndTXbBGldtIMYDu33pZvhxFXwRG78jfJbETkF6xWRY0_A03eWdp8FXl6GH_Ita5loYT_v0pyVjRikK8PZPLdEakdcxVwmTzav_6h3RWgeAFiuAQv3H18APserlD8psE1T3odaA4xGE6f_5iTAxOyAiXFqkBw_PzMFNy34vBL4AiOAxe1mTuaLll13-LVQcsE7LdbdCSabtsBGlSsvFh-WHlGWgvchbc05APmFL8cAgpkSrvmvuZna7jFVPQiRPXOOfhhDBwNFhVsnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=rghO_kb8m0vEBe5ieuCxXLOrqEP0b35Eah5GhrMPTLnlsNM_UlrpjQ_namxgn7K4bMxKt3te-Yd3i2gO2CeHnqwRZjQ1iJXcf9S0aXlYUDFPA7t3DpfzUmN1Tj4nJcG-TxWXB2ucCC76j4GHXQg4GC7-6yDkDkW17k6bG1AVLpDhncCs5ofUIaUugrMUWVwrrob87uJfdM6Q-u53c4s0ZmBTQRbYv-ArBYRYqEd8LkSYO8JfhIRWSzMt5YgW_5ZhV4fHG9lBB7T4URsu6cbGamjfDtX47Kv7Qm4z84c4zz2KHRc8IgMpYWo7S6lzQvAc6mlD9NWZKx8Pyp4qGluEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=rghO_kb8m0vEBe5ieuCxXLOrqEP0b35Eah5GhrMPTLnlsNM_UlrpjQ_namxgn7K4bMxKt3te-Yd3i2gO2CeHnqwRZjQ1iJXcf9S0aXlYUDFPA7t3DpfzUmN1Tj4nJcG-TxWXB2ucCC76j4GHXQg4GC7-6yDkDkW17k6bG1AVLpDhncCs5ofUIaUugrMUWVwrrob87uJfdM6Q-u53c4s0ZmBTQRbYv-ArBYRYqEd8LkSYO8JfhIRWSzMt5YgW_5ZhV4fHG9lBB7T4URsu6cbGamjfDtX47Kv7Qm4z84c4zz2KHRc8IgMpYWo7S6lzQvAc6mlD9NWZKx8Pyp4qGluEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=skUuYmgpM45nat5j_RXJA6vYhIH0To6h5nAUzCRVYyM9LlYnPsXppF6TapXClCJM8IexEUO-vQrK7X9ghaVBtrODfP0JKVTr1ajaGnTlg1PD9DNQn4YwWHEsHJiKZR2pCZYkokw6V6YLirM1_CfqEQTzd7al_R6AkTVW9vYC4EdWQoKTJCKSSfrXng5--pPRRsfj5EPdDBBUl7TOPRdJcMPky0d1VK5MIchUqqqr8n266XkFfnr2FniYDGBWCw3cfjBPNd-sagP3tC07VqEv6e7-w4geIqdNUW8-UBEbvlk88v90RHa3sUT7J-U_dLoaCiM4_FMyKDjH0YHxtpU9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=skUuYmgpM45nat5j_RXJA6vYhIH0To6h5nAUzCRVYyM9LlYnPsXppF6TapXClCJM8IexEUO-vQrK7X9ghaVBtrODfP0JKVTr1ajaGnTlg1PD9DNQn4YwWHEsHJiKZR2pCZYkokw6V6YLirM1_CfqEQTzd7al_R6AkTVW9vYC4EdWQoKTJCKSSfrXng5--pPRRsfj5EPdDBBUl7TOPRdJcMPky0d1VK5MIchUqqqr8n266XkFfnr2FniYDGBWCw3cfjBPNd-sagP3tC07VqEv6e7-w4geIqdNUW8-UBEbvlk88v90RHa3sUT7J-U_dLoaCiM4_FMyKDjH0YHxtpU9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uRqoY6zHPFwW9aqbMhKQhvc3vZQvjla7Hhtg371NbeUgFFqrFDKRNq-txwmleG2vmR25upvEsrrDwPMKbQ0V_T_-70xl9bncPqiFvBh6SHnZVu3pb19x3PAuC1jnIFHWzLxv8ch0rj2WnBK7t4ZbhQ92a5YlCyvmlN_dvoM1nmkqhHYtx5txI9PUjhdiHDlI3884JALk-22nta07tdcaK1ThPhk3b4s43bdFriaHK7LsPTfnc-bIEt10GDi14DbxhZ-XtDzzi_l_-qBIALKr83knxGwWnApltULTvAD12gSgLZ1zU93SHU8plGuOZzGKi4GzK1tA0m7RWK1n6EtwIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=uRqoY6zHPFwW9aqbMhKQhvc3vZQvjla7Hhtg371NbeUgFFqrFDKRNq-txwmleG2vmR25upvEsrrDwPMKbQ0V_T_-70xl9bncPqiFvBh6SHnZVu3pb19x3PAuC1jnIFHWzLxv8ch0rj2WnBK7t4ZbhQ92a5YlCyvmlN_dvoM1nmkqhHYtx5txI9PUjhdiHDlI3884JALk-22nta07tdcaK1ThPhk3b4s43bdFriaHK7LsPTfnc-bIEt10GDi14DbxhZ-XtDzzi_l_-qBIALKr83knxGwWnApltULTvAD12gSgLZ1zU93SHU8plGuOZzGKi4GzK1tA0m7RWK1n6EtwIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H98c7W1JVkeFXh3z3u8L29WUtf-V66ySjjuKlUq-z2CBUfuYaFfAcmibBeb9L6rhftjjNINL9pZ9h-ih8qfhHr0HvGvtBHEx1ImpexU5thXTVAdwYrJ90RJDTBve7vm64JkAypYplRP_mhY5oLU6nCaI3eMXKryH9mNi8x-t9jvFHA-NVCtWfURgj6TSpex6Xx1JcKdLK3ul4TcZd3ui8Q_SgEspyovpzsd3FKALwvk4kUmyRF_mdOu_3diznVoMq3nLzyh7JID0cMc_Pe8icFCY4LA7CE4cnJegdvcc5Y53IiDKEueNXGNuJG1UBjrFhwAdiGQy4_lK8rJjVomjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JhcCteY_i8TBL2P7j0AVJgsFqC_Xj9FLZEy3YiOSml_00GCV9jwhgbDEVjWGcazs-54h3qpxlraLeFwhXXDohYbB3Tpe4MQuaLcFzzmBSeqh0s82t5XQm4yeooW1mj5qkwcSB7YVwO0XVXMoxQcF7NBFHPm37V6MDgEVwGbeUZ0Xn88K9f5noPRVJ_-oMQgUWHoRuAAGLooG18-3fgNSb-0Zu_WMqkbKPCo6EdhEPA8bpcSje8UIBuFF1rzT7cnu7KPKydPdJQ6PcIlbAbZzZtcsqCBPtETZAT361-tCHIN8Fce0P7rueoKbmAEzEI8JI1VQ34eBnGff1LFfqQSjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eja2EYuCC2Abg34ebpIQv8GT48u0WTgjCX6pkLChhsZroQwls3StjXFpGy1UYhd4nyGffjppQfsL0TJcW5cMhenju0GSP4WkMh5FFfyFrfDZV42KWMkcUsSAquoNpU8NB3QysS2knyZgP6kvTQ_YiidGwfVpAzhKYQO6VxsQfD8aNrHuXsNFe9-i9S4gpPCy8_xU8THj53o3fheD3W3ryyd6CO7Iul_HaWPtyOOYYFFHArBOVBYY5iBZ6Spo8TCC_7rH4fq8Q2S2z9HsRh9u6qv0eReckadSdYGJvGY51BbrssxvPvZDYYKDrdpitiQQNyp-KvkDYPUnV8YUiIn4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D53glEsNeqW8mtof4hT3G6sU1HWh7li3nxwIUU-opARqJLEDfcNwNUYOx8xZPGw1BHkwaZSVBFHuOyO4OQL2j68-Qmzm70esOTYbQdqsc9E-IkgPJTdElzIygbqN2OMKrMtJAO4RIIFuxkyGS1Xkmy_nH_nfHq7ZWIW7DtQPYphl2rL2UReGBZrKOiuZlkd_yVjkeKk38akLhMh9ExewpJ5jU7ZvZn-vtf6dktHPpyFsLMx5QhQdp6kU01ANjLkDupD6S9RK40101XBjv3T4JEeT12xld6HuyUwmmzE5izxBFROBQS7P36IkQIHZAGorDKBFojvck4P3SaN_IUbY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tyOaIEolDZKKtoepN5X7FnEonaR99_SBc9QVk7QmzVYlXhkqYpNhcKF4iQQu9MSMQBywepgWGL8GmxCp4wFrszzQKHwdeFWQTRbhy-CrMflndyBtPPgt51DWdjUNm-JzCHHNL_kLWh78F0hWY1cQd7MsM7hDfeEdJEWAe18JYP2X19V3CtfqcrIW_Xd5VN_iAomg0rNkTnKLJXws20Olh2kld5No6xDF_DFy4_vdDQCbD62OPFLiQ882GSDIiwMM8p15tkk8EBIsso19wQldLnrr_3bhr3ywTolQy5U48c2p2E3yyPXZIqd-dWpk3GV8jvlIc5AJmMdS4d2Fi_wvQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keZA_nDmUF_inAmSAeziWGRMUQBltX7ZFzY4Dh5XxPxVIIlbPWZ015R82ze-11HMN3cR1pAuuYqgHHPkMkKmn-GazHEJwbnAqek_M5L8KAPx0WIBDhhwscFNp16LM4-8033bZO3KSTZ0RVg9XlhqAloMmgv0bd0fTlbwnN7pqXDZSXWodPcNRImSBP_AyPBKAHHH0Wij62I9IVMa8YXkKAYcwo7btHX3VcGBVtkS5MJEweo9lY7GecExb3z1fHSQujC8mB0EnR_pZnNwpRlFBiDiMlqDPnOZ_j6zZd-LrOUAbj5rruCGP0HPIjv_dokNKCOaOl9zNRhKSqHbLpmSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-x1u_LbtNfu2q5hPnfDuDD8Ag3ghSxCIxqAAwxjeP6actT8-msHTQeoqiC1kjWJo2jMUz_ejTed2uKqhNrUoMB93G7Swo95VdurLYcG9NC3loFlrDQVTy9mPBuAk2RZnLFFcfDPjbBR_u_YmRZwMmVuYO_YLOEcjWjxAHN0dITXSh5ZZpjkENAs6OyB1K85NmWWkr0zumIO2CzjOiXH5_um4Dtoiji2_9DW-Ag5W2Z1YrSFNID4WvEgPaArkShWqm3AK6YCBalvDM7x3LBdus-xIFiDtjGW3f3W78kIBnglkHM7qUPdi5NARr7KbhWmFBH6xD8UFSsugVLC1UJoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQkd_9DDupJuCD47_Zbu_CaygSLHjAM-HvVkPhJIHKxV51KZOXpH6UBNybtwnEva3exY-vmzfp-lcbdIKRo4A1t_osgm4TfOsuwwQ9zb_hSyxg0mXnhA5Xi1wiiPgDYmBxxbTOEMRF3xQMP1W_QALqPO2212YNRQnoHnENULgVduBtN0sJf52uC41jEwGdygcBcEiFhxRsfUPbX028EnfCCHEE39pedNGdx7Ldc2L4uPWgPZXysDplo-S_DUzLGBiP6gz44BzZDWyndePVruaz-0qf3NT_3514Szw1dximGMqbwM3Xls0p1Bm7XR_Nf7NsWCXDQfiQ1hyqH0x0VAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uub44hcpfaMhL9IWhDoIZXPbPOGBvhUZjvnh23IeERKcuMw5MYktoe4nTyIL-1fYTg3jmU_Ti63vfqoRpxiFwAdhxRdvjMybDkkT0YRfwnPzGSaGbtu8UkRtCmwlGj57bh46vNEwvL__qFC8NXOaMsCyHSMBTws3HhjbudUZBA58JLIe2D23NhbJz0olwbpnNgZwmX7i-F50z5e6WZRg7WN80GYVeAsQsV9gV_LlANWtmvMvn-QijYCI_4Zbo5uhI29W233UD72niiyKGEkRmTvRI5UoWxYr185Gb-BBHUYo7ZuxlpYn8RGZ8MNtXyCWRGhpAKHIFGI9q-qterO3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=mnFYeyeNM2b1HuY7vrIfl4FKdkmAyjIlXfScWepuJKKm1gSzypGl-MTPtsYwSG6jV7CJ_ICKFhRSEWlEqUKTPeUsCzAT3Wintbo8pDfzoEMM24nJ2n2Pv5exIxZVzRrWJ2obFnYCEopVeb2BPSS4o5goNCw_hbaZ15ntjmrc0g-G4easE0mFJ-ZcrE1e2on9aU8vpAR-dLwCpZslpN9KDVbtH_-bfv8NfqbgdjtHucWPgjzNLKrTVfy5ZZB45yMjBPOH7bUqVhpU1wmXBiZYJZLt8xaK0ENqGrZt_MMAmX3FcXLxdDQZYT2NGUQpoLNuwFGBiaEsW8vh3CYVM0IA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=mnFYeyeNM2b1HuY7vrIfl4FKdkmAyjIlXfScWepuJKKm1gSzypGl-MTPtsYwSG6jV7CJ_ICKFhRSEWlEqUKTPeUsCzAT3Wintbo8pDfzoEMM24nJ2n2Pv5exIxZVzRrWJ2obFnYCEopVeb2BPSS4o5goNCw_hbaZ15ntjmrc0g-G4easE0mFJ-ZcrE1e2on9aU8vpAR-dLwCpZslpN9KDVbtH_-bfv8NfqbgdjtHucWPgjzNLKrTVfy5ZZB45yMjBPOH7bUqVhpU1wmXBiZYJZLt8xaK0ENqGrZt_MMAmX3FcXLxdDQZYT2NGUQpoLNuwFGBiaEsW8vh3CYVM0IA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInOzy4xNBPRXqP9WevZqag1-6J_DHGjy-rgJBk9Eo6zlloHf75vEoJ5fDAga1HhpeW4_tam0KM0M-OxMwv0YIgujBkbV0QzfZzW9K7ZtI1MUDGCz0vXW3uzh6yj_5RvTuOkAcnoCNrvNnFjUXuvXaIitGeGNwpLlsxEOKHS6V2EGBEWPkn2O766uMo50C6_X-bO16ZMqvwxC_G8V2Iv9yolcn6uSSsdOm7qkXwgRO3ePRWQ0fevaPJaFFtvkC62mfkQRQwpKfJisnpKwG7mnmFHbZKMNGREH08lnnXWHakQv35lH6KMXHoWlY_MPrSXJFsVROU_Vc1aKW_zea7kHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=gMVsQ8Mv48srrQnJB5Q8Xeto_WIBiGgSegNHQOXdBhu3fo1IRWAyfCxwAZkOOBYMUzO75GLlrlIdh42PwLiTSW1y-awnkb7YgXfTf34LooGiQ82ylIEpdsvle3EPYxYKraSkDZ_EuFgDYdVhn_R_bENJVpJpATfXiUGfQYUaUMQfHH1qsQ2mgS69oFkJDvzYV3wydecmACWSceGWDdoqP1-uExzlyZ-r6aMqG75a88kDoS5rCB62G3EPdIn0QX1ymMMYsALfjlU76B6kUP3cTD3WcA1PMe2uoidhSlfn2HPlX7300Y-6CPIstMR-cwmi6BRufv85fLv2e91UoiLWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=gMVsQ8Mv48srrQnJB5Q8Xeto_WIBiGgSegNHQOXdBhu3fo1IRWAyfCxwAZkOOBYMUzO75GLlrlIdh42PwLiTSW1y-awnkb7YgXfTf34LooGiQ82ylIEpdsvle3EPYxYKraSkDZ_EuFgDYdVhn_R_bENJVpJpATfXiUGfQYUaUMQfHH1qsQ2mgS69oFkJDvzYV3wydecmACWSceGWDdoqP1-uExzlyZ-r6aMqG75a88kDoS5rCB62G3EPdIn0QX1ymMMYsALfjlU76B6kUP3cTD3WcA1PMe2uoidhSlfn2HPlX7300Y-6CPIstMR-cwmi6BRufv85fLv2e91UoiLWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3P_QjRbPgq8PTzbF9eCbhf11lf-LMFsdzS18R_exrtFSl2uEO2OsUsRiiIf-13Z3XOEUHcv0EhE_HOZVfB8sK9tLrK60B5VCCy0o7fr8zGTrYiqXwyKBMR7KafbsJDJ1p80Ik0F25fUk6vK_Wj2NbKmm0c_ohLCq_kkHm5JxglNpoXpo8WiwrKyA8wa6FrJMJP3vAufOljj995ftkKWI3V7iE_r4_6wcrzqpWFGrFh4paUF5IEzwk2qwuj6dd4l8aWFGb97COxSSIwnz4FpaKwmLa6y48GFj9DnML9xCZ7Q2M77H2snikB9mP2YAZVpWt03NqfRCDBOcnawU1rXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QifGwDGPemyFLE3u1cwQoPSJgNjSRuxQzh68JmrO6jEVmI6b5IhNQmOuFyVQ-HKVTJJY-S-bufipLpS9QKzs2u6Opgq8z2Qc8ZT4K7qzhVpbM-CUSIrt4kLfl3KKl-1mEEhi2K1TlFro3alf5BQsZk1A8x0dzqfOALioH_x43Lf7QFjwvpe-aEJUNZeg0fnNGiTSyUXdW5OA0KaT1-V-Nennb9W3Xauj2T1TcqJ-r4GL69z0cjslf6Kci4Y95l5BXGocGFHyZ2vtgKKk7inGQKaHDerc1ZyG7g0H8cB_T40VhP0rXEIGI8iq3PKnrn4EDVB1hcCTOg6WNKZPEiCqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UxZcMxKFLuwPn_hqShOrM-yJvekuHfz2lspGcXpLE7MgdLnkkjmCBKCjdfz85V2_TwfS7j3V6I9E4aeKpYzlNJRQcEQoWS7fr0m3DSW-dTgP_7UR9xsruZocO_qoKccYCuPYV0ArS5gCWtxxX0-Uzdv8xWSeZ29CBZEoslJ1CaSfkSukKSClVNuDdgjppUQtWFIC0hbh-dfxex_ngh8jVgZGtChgMzpUrH8TEfEVhpSv0vyybtQQPkCrpSCEtonQ-wIEh_7wI2BZnZd-UoQExh7uBHza83ygP96rBj-z7kQACpCLevS0x1wJvZznHUkh7eV8Wk3Kr8PxV4rwNM0t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a7eQu_TQ5VoHl6kTUtKU_v5SQxWD56cZTLSLuQEHqI2EKvINgRV0pMHfyN2j6AQyjTWglIFSgFrNrWQPRTZPhn5p9VH890hN2IRUv8C6g8BWNMowvNKSaTIil25C0Bh_u9S6DVTr9Z-Dth7PdwZJsXwWn-jvxXYCs2Heac_gqnjPTBBHE-RJk4rROYYu3-t6hAocTz6_qlAgLt6Ny_7G47acpP_pIKr4PAYFwK1k75Wr2eJQfLNQq5T2Pcb1-0JPB5Tjx_JbaBoZdKoIPDrQ33VSGV87AItXCc9hj5z8Phn-cLyi8BDM1jCn0Lvw6PcCaSOzWPWhlMc33N9caMNN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/swUNEmxsIjAiSeDyJS8SRLqhDzhhnkqNyXSgzoISwgfhCLm6IxkCF8vofkF_gSYdc65QSOu3XTSC9a27KFHyZGurTzFMHUe3K1XrdOpqHV1ei3eEEXM92qTrn9i8rOkcaNzf-_K2yHsj2DAlQLkBZZvCruOB2lW9F4zwh6HbsNfqzclT9iaix_Nb6OwB5S5PM4RESEfSRkWAseXBjQwqjy02ubDGMqu9om7Gs4xNSaMB8LBSQsV8TcHfnyb8E2gL37htht1dwxOIpNicrW6ZVGmaGaEIA7FXmXWg1-xGTjllvT0cA-8qJaLAvPeY2Vhte2KVZdkRhlHIVW8Quxy-Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=W2s8p_hPOuVi5X5CUmsdybZ39Cr8zhMcfsofA6KWSqKLh5JrUR54njrwJ3X3WUo5Khx_N10Z8jzdMIDB0pYFxu0GSY6eBftDIXEuYk0ENXewqw_c7NxtVrM8Jo61JTKNIJe9IqmEZx0GVZ7fSgwYg3rjaVCwHbEWI2GRWGIyKCAOUyMQHFVT5etKGZDB4Ar_xgwbnYTzT0qXFGbOGSeiF6PxmY8I_hkvsWXQtb8DB42HNFtdp3NX_z7MljbE4Vcl5p2ghY9khtvjctc9RFU7hR8g4H88sDxedYXxYjlyffZJX40CSYSwUhMOOmLtttWt0ueyEZbL7kaIzSjFmhYUeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=W2s8p_hPOuVi5X5CUmsdybZ39Cr8zhMcfsofA6KWSqKLh5JrUR54njrwJ3X3WUo5Khx_N10Z8jzdMIDB0pYFxu0GSY6eBftDIXEuYk0ENXewqw_c7NxtVrM8Jo61JTKNIJe9IqmEZx0GVZ7fSgwYg3rjaVCwHbEWI2GRWGIyKCAOUyMQHFVT5etKGZDB4Ar_xgwbnYTzT0qXFGbOGSeiF6PxmY8I_hkvsWXQtb8DB42HNFtdp3NX_z7MljbE4Vcl5p2ghY9khtvjctc9RFU7hR8g4H88sDxedYXxYjlyffZJX40CSYSwUhMOOmLtttWt0ueyEZbL7kaIzSjFmhYUeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHGpd0xword28J41WQ3DPwxgfMDkZ0DD_x37E1TththPY586iKB2usmzkD9gnSjsTwS2nJFfRSgHoby73drFlvO2pdXaxY0-9gS4O0UyfQciHe7KzkNFY_oqcNHeVcDRdGNrorkUeGDNbqqOeczCVY41S0LGhsQBNntCZC4HfV9Er44wkk3VcK4SWcCz93Hdt9njPIm6EB8VliueRitfyAPf0MUBk4ha4132R-7AYAPiz2f0RrDPmSUgNegF-u1EX4WgIc6MHiF10XgWZmY-gP4Kx3u-Kj0SeisE1LqC2OmwzeMloXaaoZyV-6JPgqjOYkCY03w9XXFsA9eaS1DKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orc09UopqqJKc2BBhb4SG2SJOJdrGremPskYAKtCd0GlMK4K0aXswt0XFd-YEFDiVVh1wfhKFBbiteF0qYwnPFtd1sXtr4NbOP5VbLisE7-kU9U0LpPQE8iWmztMS5ThqrkC98-5nsNDqFksrsKY9jvKvEwa7CF5Csi2G8BZ0zfE5CGUTPWPdHK1KU1OeH00tJmm7towd1Ayb2gpIghJdZds50oF3bSXhPMARX5VBmQPpk9fxLdCSteuI8C9SFJc2RePfzGyLnl93y3h5M8Hu21X-EggIHDZUCw1A6dGOv7WkDA7DXlZIavDsj04tkZy0aoQ9iVAsSkKxPUIpNKDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RJcSbETjWvC015G8D0oId3r6HumdF5uB9N7i50J4bRoEI3uF7NVfPamY6eQlKMDQAhdofXK0rxuDmWqdNoFprCy56ozwc1TuojAK4XE-F6mvNImXHHHimRQ3TulBv7gM0kUSbnTVuxwISYVFNiQS-GAP2wk2Wgn6G8Kxz42wNSknDnTPAbuoZHWltv4z-XkqjXAV-tvXJxgIBn4Y8h3_VRMQ9Kwo1LOA2l9rUImbe7ZVfLPidOiwAkuXbK7njRjkLyzJ_kgRStyXzyiSHPkc4NVkR3EXJNXpAng7o3sAMTKyvj-OqvARXDnhx7Ialz5upeAM8NYNGwFmDvhR-cAMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g2VFyKs4_M98Zo7UrGw_sXjudAiIwWheCS8s5prUrl2tf2lrEw6JhG66VDama3ydxFoxDb4-4cMSgz05NztliMEpZak-IO7zBmyJCkM4nZ99X1w830kXdZbabsCu6JvFw_tMjKhDDQA3s2KY4X_B_slttmA_MnL7-eioCsR1lS9X4f4-aVGs3pXvzpRyqT4oyxF7E43_8v-v8J13ClIHJF9YAfv4CiULx2g7G_g_9YP1cRZIVXtkxedEiWCUFNoQfg2LCB7rb5nGsB_KOwssHGLRhpdFQcLu3GRQiR8ZLayufkIs_Udj57nENZm9bqZ5dWhA_VlR74RCkXsPK1bmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iS8q8yvYHK3l-jo5u5RjaDRW_hmRbDDxhtbYvxT_FbrXBPbhFT4CnsmUDVcpksXkctYlSUTOfCq6ioUVVdBBVbUSy7hugCGriz04g-LJ_mRG8_mnxEWZePEUkbc2Xrw8YSFL6mHtMebyoLfoJKhOY_ebtMAEhLPd6kRyiEL9zUv4nHRmWm46YzYZAbFAUnShtn4xILS8dRtJrvFbiOoERirgylxhe7sUu44Wjc45rDEebLWcCwN7qHrxvvR05mgoxdGSf__na1RFGNPgzf8oLkwYS3L5pyfVq5U6yWpHxyY8vDzeElGJJVyjtLkT1UyY7kkKOD4JrcxVy_0giVxRLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e523XDbGQlHvmvtLf-HOTGJIwLv22npTzQUFS-cUnR9dPOnfiZ6VDgZbvEHIPEZLA-eQOQ83Lt_ylulpHTDcbJw2nL7i6UL66wWLBwXvBPPFNWgfNhht9pQFh8iw28InjlcT3tp1QPmO4A9OuKCCMpgwIDiYN0S__pjepRyB-FJ2rguEkHXybjOcCxp6mTsEZ06jU2e2AnKAW_lkEoz9Sa9PEWTHZpLNZKU_0v5ciK3Mfn4FYQ2xxWz5qDvwKDgY6FRJZTR6DVFJnSC5J1z5W8GEesSBYz1sUEjexUWqiMOGigiSLdBqYvHpnowNZ6k8ihi8MYu7ipxtvx93C_1LQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MWdTWXUeYsc9_G6T3XUCTufMoFghYGcnAJd8dP2fhl_SpfXa7ZCWDFjc7IkgteodBzRULRGCWr64Zq0IAfj8YMPUOM6H3SrhqQJJ42Kg2nbGSJ86st9HfpTEitJQEpOXe07NAKBguz6gQkghOBbjlQqGdrR-N7YzLTq3IRBizOaKwloTJSKLkaCmhU4sXVQjBjYbn2f7V8nHGMS9SA3KcFLRqcKng2l2bxd5HQFl089t1m4G4SWANplDmmdMXfIgi80QuasOECSmJ4_wthjhIDpajdMKyOfGNVrSgg9SxS1FibCDd7NAxOIXqs2GZtXIEPL6a-X2_4hEtpFjHUC_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M_QyybBh_QdjGbCRsu88fn8nKo4wQH8JudDoa_1FeCE421kv1nELWn36jxVP3FqZRunOKGPBNgwvwB7J1Lp3oFQMQmPxxY18BXfubKVc_sH7jrAMIBYYSxsNhLSaZSq2FrAnwwldjsQTMA9i3sjScbjDaSXAggDVx_qWuDezVChGZostMJaRbzDSHQLJ8DuNoiszA4EREC3wbmtwVk4hRaF8qAmXtDrOXkJCSF1jvnk3rOXzhV_s7H655wzTzknKPabZybDoTCC_dhybZPvVbd32t-tRoeuAlHQARSB3jfkeK1eaUCdS4cyHEg3b0QTZzmK1nSDB6C8QH2zFypA1yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mV2uzxTmUFIH9iBi1hiHwBugGiA8RenC4U2W4ZSjeLK8I2MyQtefFiUlIrTTQTqU4E0cVsJa8hjny11wMloTNDOE4iA5-QrN0dSpwM6mTX1_cFPGVN-0SsH34-BNovc709R1HCCUDRX3wafoq4SHWAbweQQsNzT3OmaJEARcEX8lvBIvV7Nxj7jyRdXZgUv_GsnHNofcnDccziwR9bO4MzspvS6hc1SvjKbHj7-yAh_HhbroycgI6UZ6zQZVVL6SqyAkmvf8_1-UbDm_CDnNsf1N3Lwhqj4hHX7cr3mkn6UHvJFT3bDeYMUjEn-6rrMcpdZwZSx7v6GtqkKDM2VgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR7GawGhjxz51H6SlFUFTcVEItjD1-btin5cPt1D5kZEt5BDDbcGQduYpijIxRZwqcNuVJSeLLMTfiuImMDbPql-dSZ-4m-mfYHmL-MFU_tUILpI-CmD4d4h7_6JTYAECcdrP6lSZJB5tPwdWBtT8yUgrSeT83BDgbGrO7OvBLwIsILCUXzUIrkRcBwPD8QAhRon9-b0Sy1AWbYXSIN_xmcaEdsPomWdNNhdGh9Q1O8dSCXMYk3EqTIgrQs-QPRJvEv_vN9ItIfbroLj3t4DnnMZS7VVwr9lXmLk5P8_4aM5VdbHyZDx-WziYbitfqLmgocd8Dwm-WjewfeOmLM9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSii5GqVbRyEuWPl5XihdZ_Rg6kzFvs2ZICxSEG1aXA5naeZTLK1nVsy-LAtNjVULiy6iO_XpzZOhQIw-eMznprM8XErV-7y0iSpBsK7Gldk9BmjIBpkPhckVYEdoVvsscKQUDjBhFT6eqJLM7IMRR2V2A9J-l1Xhw0bd2TCIiL_9yANJf2osh4wwMxoEwo6daw0md44uvshvaoNkJRG8umCPZwTZjA-ahJfwIBp1m1luqSI6qwEKVAcaf2MB0sx9o21kTWTiwXjsy3SUrCh9dIxVFVRlzm9iLVFlVPC87KqizpbJ8CqK9RJ1Os6FkNSOhHNOlbdaIBrxj9eijoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsOi6s1DaH0qENpYrAgrwkj0niSKY2-bR1Ef6zJwVkUuVQNRShL-XX_dro-Bkrfsna5de9NXyq-s_jt-F1fsi9ic8yntRHRhAyHLpNkTiZaxAMD6ZYYkFdtY2v6DNi0nerbarLi7tXO3v-kvFz4t9Wr2gUpSE6hk1MHl1nhXRt1kMHE_gnhtbD5fQg1y0lx0XaYYM4bdOvykF98cAdDDaSutGoChsPHncyu0mlS1I6N3q_PI-17LD9uXs4864LePsON7UmRcp6n3k_3NPC2OuxB0IJQFpKZp443b9Tnoz46bf_TaaWuFIGwcbJcJZomJUyPzVT1YhjC7-XTaJqAVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw9_nkadIOYDO6Iqy6gPnKxQ22PQAs52z_eGQ5z_a9wzLf6ZzhPe5JDAb8BKEQRSWqbCYyDDOBWGnXteqvWyrNGXurrFwlwiG3yebMzrF9sejqNKgTw1RIedJToWM6XKHimUKMSDSIU1RCKwSJfk64D6uiVxDqWrW5QUqwViL-TGRiBhzxFeDJhZjitXtlm8ZdJd1xTmJaE9-e24yIo-ZYk2aWXoTV33mCU4AGOR_Fj3VQQ-iIYnGd-up0gFDLDavvIEtJotRVeNRmMVJc8-z9o-AAoONATX24LC_-NHKNTUP_JqDup-xqDEuE-p6JuccChQdYwGc2Xr5e_sm1hPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2OABgyRj6g5yep504jXGw6ZDgrE0TrPpnUffWWmFcoEZTsn6sju4tZs1yz5dEN52vKcB9jhpKqIAPAjta9arzMba1DQzjHXSndpq2yc5qPhU6D-dP8Q_fBXsfCoP-KGchKrcz9fJMugW9N6XNdRuf9McuFYIfNAV_E-4niFhhuyQJ0FAlLju4fmv-5GY3TFh46mX2yKonD0FKrCwJITzx83BQsJDqq4kmUukJsg-ddkXMMH-1dBn3wDizx2s6U_UkKStoJ0gwZPkHuTdA0_fILgFuYuWHcypAPEiNmMwj9-LOn0tF_b1YND5_VlZchfknmT3Zi-YRh52-lpMWa3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWE3ppX4zyjnqaLq45Ehdu_qulfmlaOgyZTIOWExH1HV-lCFtKIFe1Mkmiv2fvsMjJl_EnmSx4GHjAntQOAFShvZV-1GP-MjTbiOWDkp5J1XEg2nTsEddese806rZzT7POlySc3AYeAqi5XE-rDLDiw1e4CR-Bx86XuHXDCBsf5n2jvJJij1ioLt8noMXQzVl8U9gcpZS9oxu5_vdmwQcLqNc0Nz7bpzT8EoODFyjpJ8Xh_LN2_GIsoAlOaa5_5yaq-K1mMHxW2Qu_rkbReL-TNY5cadSVMplT4rbpMm-Wnh1euCzRibuhgsG1m0H6xn1xz6XMXh5llyLmYsPiehLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdZrK_k01WcK_HAoy7Gdcuo7vXiMntfp-cY5dpCHftFLDRzaPXFJlxGLRcOV3m2vc6dk1KmUIv1U0GgNe3fih1ZcrHPEAwsePnMyVSJWkRa9RD4gOpsb7zfyKbq-LwUEl0XICqP78nvmBo1u18lzBpwCf0ezlZoqQfVG2EPHEzMWAm1YM2duqrvKCbEylW7qEA4xFW62HpT3buJQIOMc4swSqnEjKm2KLoEIvhdpG_P-ZD839ZiF9LzwHfvefA0PwnpnY6h47gNDgmFTHpX-hlfLaXvQGHfP459AL8acu-YxNc8k3v88AUJOfXYncQ__9NoEbh8wVLPcoWBPV8h3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwIQdsghNCdoGri9YQMDZ-o66IlGItPiT9G6w92X2e_t48iwJq_1F802_T8a7Q8ePm82q9mBirAOZvTzx9iCiEQmRxXev2gbMv7He8lDw1HdpikpfsO16zXrF8CQGu2HAGFE1c9kB8Txy7DJBmtG1MuLC1wGicF4lsk301pv6FtSICpTBtck8Ci4lg-qA2Qtr-7EV7b5bdjcHJCmL7mtZk2oCpPrtSaqsHfi9rC8gArHA4J_239VWDCevGTg4hFPK-LzveEyFMspR-amrdS8wHd3tFrJ78Z3lVo_7B64oo-Jl4aLaXPhDdop2W2vgBp6qsGHUnbnuxEgeK65P4VnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVpZKJLm1jKZuVNNqesKUYAEc-CQ7kVHGNBstsZ__PZaQCj07wGhY11DSBg1o8lWbBjuTdONJJ8b8kNL8ETmRNrVWv2yBmwPSTl44o0gZDLq1Jv8SSYHjm7VL_f_dxJ2QDkdPbplGeMoEWmVufnxqf9NG_QBZNAKBLE48wB4oSyPvhLbE6drLnMNXEd6RezTXtRBOClgEDH2imbkcA7nwD3j2S_F2gqz1QE6PhJdew1Ekv-QWw8T5nR3rePdKwYK-BR921oswA11ziEhk6ypb-0hl8ga7Tpwj3SUQU9VnksC6A3dO8QrX3nHdIbYMzQ6742ZrrYJXxdyoF0Mse0_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9XeGKKogaqclBzXBEUVx9hJQQvikQ3hQIli-kSKhTEWjg6Id6utfwRgOk8KnoWjm5EwnF9awRE8GviIS7uewdVKiaixjnobWnJkCNC8_WMChvg24azxKcn_c_BNOVVLxNM54LrKfW9oaYHtxbjKCToYwHnDGRGrr_Dkek1zAC_B3F1t5zLxZAQPg4mvjMQaT05EVZiG0b9OuY872vzWQSbvSU_kDk-yoRbPjXFXuKmvp9ybG_pi_0B8Kd9lBcI7aIcHG9wdjXUnSg8jZhbJzuzqNmsBulGXgmCtVU3BOz8rSiBDZB7-vINC9hgenIogd_dJRSoMetj3xKfnCvgl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9ASUrcvCziKEP9opOHMqBYgJI_BOab_aOa-ptKyDySIdmHWjD81Jps0qBAO-CXsMq6RAa1ucg-Q4AzyaXcjPU0Y7YB2QIDEirqcJYPwBF2ZbTsEV8QWCkiooxiPpvwVONiWafXIBRWWuMrjgFCe1xgaDkpJj23M7mhsw-dK8reQUTZGTfjYsdmkkOiDUCpLdZd_tJTSRBvvTmKPmZhFHu-sgjZnAIc4D1PoXRt3P9MbcQB0oDa3g4DXG5kDi-dSzdgccKxClwhssoyvzEsnG87HtkxAHHLuC_bhK9k29meOOjTYRTOb3f3ROpq--7Z1YxBeSvV-myetVY5b6_w6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q3Bboi-aB6ZvP78LG6QqAowq8BWdefkwvO8xz_tloFn39YYF8qpcSjH7Ik357stHyYDk2rw70sDGjs8-pKAaAFUEuee-07_3_52V71umZ_tmL6yS48NxI7hIZtU1Pgo7uN2JcoRtvLAWInM7JMQybjQ_VoLP0L0tRindFfELkIXLM4dDVZzXMrqeCn1qv2hJGpy-LPZ95ibDo0kR7EYeTMNIalxN-ngmY2qPj-tfdAfMaKKc1oNlrU-U_rC0w9ZpKNDc2HN8SK3X395mGKEQBXSQbgtlKGUEbAXvQ8P01bsjwmHUbDBE34FMqncdi3X35v6UjGZHdj-v16dANj5U8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d1blqFugwRY34sfKRsO2OiPwKD2kVzSG_8z_ayw1cSZ7reGALdbWQ5sHZqNoe7nDngn38dzQaNpscNV8P8CsGs3xT7ZSMWL28skGHWcRBY-Q1VipwoaQWQtdd0u8IaqxVNrSz9aGbUZ6QFVtwYGsenwhuPVoq7lhSxi9Nl8W5opcchEtBXncc-CaEM-Qw3Dey_XCExt1m-0cl_KHiZdDMKDl-xWyFBl-OzhKWdiXpz1zNog3u6ARyjTT16IM4mgRFNp2Yjcd-iHqCF3_I4r46kYK_lAM8LzJcAx96li6uTBXMBmINHczukr5VSyh8FVIrp9HI5yODGjTIwiF5yY5zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyDTOEtF3Cr3sBSmJLa76E_MqNWd98rGD8YaOVqXcAPqFN6AWu0_FFZwEVpElDnXXLgk4-zl9Ml2BFa3NNOOKiqAeHfN-Gm4Ygm1BpFmX74CwrkkkJE3AaO7-DohHH1nItNxaYDieZhkjjEyxOOyoujCCuFepZr4Kx-9LYnS5p_eaKOYj0Zxqbh_O0nbdrGjHv9Kem0xNZ5AoDQgCSadC6a8oUr41oYvvkw-U_KRb9Vr79G2ddJXxdVocnBlQXChJk9f8NGVLpJmzEFkeLGmxD-_vj42qV0lnHfEWOAaeJPNOGFNkkSwtWXG11acFnd_0jFkWDV0ssqTgOF1CMvt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=RHTQfNIHSA21wh2Tv9ZbhXdvVEsIZ7hw3hdYa6PqcHrHGmMZ-9WhvtoT4a7lew6Tj2ypsc-8Y34EUyJP2bLuvFbXjcH1bTFN6yft4WLcIA8XGPItVVP7yvqv6HX-sK_Ms8KKDGmSt0vGhAGCOANWzsW8bwCg8weupFlTdVvnHvJ79IOLDhqJ7rl_AoDCPbdfQLGQllotoTcYvMTm0d5RrV-lwCadtkvHc5d8DihmI-fCEozBxnp0hwzYnksWRik0En80Z-wb09M2hDIlUFk_IsnPE4_oZ7a42XirX1MmNMbI13YrTxPlhJnAcHJ3JmtjHtHyOgb2_lUFYTYNv7dSqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=RHTQfNIHSA21wh2Tv9ZbhXdvVEsIZ7hw3hdYa6PqcHrHGmMZ-9WhvtoT4a7lew6Tj2ypsc-8Y34EUyJP2bLuvFbXjcH1bTFN6yft4WLcIA8XGPItVVP7yvqv6HX-sK_Ms8KKDGmSt0vGhAGCOANWzsW8bwCg8weupFlTdVvnHvJ79IOLDhqJ7rl_AoDCPbdfQLGQllotoTcYvMTm0d5RrV-lwCadtkvHc5d8DihmI-fCEozBxnp0hwzYnksWRik0En80Z-wb09M2hDIlUFk_IsnPE4_oZ7a42XirX1MmNMbI13YrTxPlhJnAcHJ3JmtjHtHyOgb2_lUFYTYNv7dSqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qU2l3LHD_flEtF4SqaNT3Ip22pyc9KKiXGyK9h_pJIjfC2xqChqI5tFO_lCWvILIJxrP33VFEhrL7AQAdAspgy69wRUaZZX9mX7JVugkiPtacpivfKHCCIeUhGNZ8gxTOkv8VkBH9wQytCHvuV26pPScOrnmzNJVcb1Qs_JwensiYUWo_MZPVdTyBJxmWJMhlix7w1E01XOpkWTyJFGUFUg8OeR4by3Bm9T9yubLVyoFhAdqLD-Nwl9mL_cS52XVx1w4Pby35vqASc2deQUYT9kp3jhCer4nQRJqPwu0N-GXD4Q-drZbPKadXAd5-vzzPkxEYlXjey7_94mnJrwyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLlSbuu-cDHuHxatUqosSv_saw_c64kYQujIWzC55LbXuBjVoC2PgXpZEGiyv9UlcENDWP-JW9zml1hHG30Zqxz3pS3V6RJ5vE0bTDycZNHnE71NofX59xy5vxJIme0JYSd64UwJENeSKBL7146MTrdsvgv4ggjPgO77PWt7SVxmLyqgtT_4iTRIkZdoMOhieHQHeneqxEBf7ml8XnTKMjx3uCUX0bNXZ8w3GLW3N8msmbktuUIWSbOoFelXRNpfbLhOgkyj2Sq5mytI9IAphJF9eHfhXwHtByj3NaOPMclismGTbKGq2KeN-eXSGNPt_KZMRp_A36ErE8i8-DZq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkw03A7V74nTdzpNkGuApz9Iswwkt0x7MwCNqD7Qepo--ayfZkenlLAjwWA3YGuE4XnfGgUr3LpHQdkfIRcbdWCkJ0dehVGaJuqplE-mIjpwohwOvpHPPKfWYXFzjhVE4Ad5bT2xOQh_tQB5UdbqQNqVwAW_yhaYzMgbx55G22nAzyUNK4SxeVwFICDMyzIx1YJtpWGfD6euyzuF-DSOpZscAR2mgfAk0qB5vqMVoxbK2hJLHuj-6WSAEeZWXufxs01oq__QBt0m1-EWUSirKfvME4C-d6yPvRQG-Fqh0SFgGHiENphbW44GlD1k2QSpaPPTYc3UfdS7DnvetAIGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXXq8jUsKT1dV7yfQ2_BOwFJq9y3XraklSDXhcK-5GJAK80AukHCf60RMm1FAdWGKrgPjYt2RdJKDPnghDMb3-XIWi2BYEKOj-XIAWI-u7FdFxR3ldvldnhIPQ7G1oxwKKXcR1YoUrznoghI5ajR5rDVHIbBGX_zOaRdlF6bNlSXN3yIJXBCCSeVa3d8JbBqLwQUIfJb2YZzbdrbgcXL6siSD3bFqVI_MUDu4LzhvaAFJmU5L5Z_67friF0Z43B-Z6ObezkfZCnpd_T3JFL0APrbbVFdHSxBKIgaFpULv2uMBRhgTsXS9Fqo3Cnfxyi3XYZE_lTJknSTTidUwUKCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvSYiHLUJyh6_XXHGoCUBkR0GyT0BryEqGs8RFgriSpP3zFsgKaPMIUjkJELROk-m0d_fS_g0jnRr77OfTjivZPFD5pnO9NKKCroK8g9RH19ADF9eZaLfGHDaQME8aml9Xv2GnTRjjBrenhQe40vOp2vcOKgLUNOakMGIubgFJU2SQkkytO4AAu3i5ajAJUur6oQn1vgJ2Aj7LSt4R_kHqVGM9U3OeTlDhJ7JKsrwVXCuNLHYZJ9DPAjBxkbG4RhkhxqKwrH-H4yMMXvhNXak9AApVpVgaUZTuIrlEExNtEZpb640xxdeNap0bR8j3zqeZ5pj3ApjYyQOwWxFyFbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=mA2fDiJkkpAJj5ho5tafEFCDEVfo-oPCJ3Lm6dU4oSUU6q6YpbZKWhYCB26EPCnlYnSCkKyYzAfxXbMLsUAvtO-HpxYdo3GF3a3jUWX6BgaegHK44algNDdryYIqHk_DkyNCa6XbBI3TSH2muirG2uoGve3-aJwR0RGJS9pn1xkDKyosS4aR8UohOJ5ay6gPToP9XKxa1aIRV0k0CeR4fF5eAqTn3j9GG_A0y16CbE2IZwtm4nDKgUGYntGQyfjBglgikmUfisSGnZ-Ru0s3OjufySXzLgVz0cvXqhk7Vx086QBz0vAXkqW7Otz05nI11_aLFsr47riiQ2hP5qenRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=mA2fDiJkkpAJj5ho5tafEFCDEVfo-oPCJ3Lm6dU4oSUU6q6YpbZKWhYCB26EPCnlYnSCkKyYzAfxXbMLsUAvtO-HpxYdo3GF3a3jUWX6BgaegHK44algNDdryYIqHk_DkyNCa6XbBI3TSH2muirG2uoGve3-aJwR0RGJS9pn1xkDKyosS4aR8UohOJ5ay6gPToP9XKxa1aIRV0k0CeR4fF5eAqTn3j9GG_A0y16CbE2IZwtm4nDKgUGYntGQyfjBglgikmUfisSGnZ-Ru0s3OjufySXzLgVz0cvXqhk7Vx086QBz0vAXkqW7Otz05nI11_aLFsr47riiQ2hP5qenRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmlQMhphecqNiC7nZep72d7kdQMcmzZExQWEPrzS0uhnIXIxTiI6n5h8TabpODcVhei0tYgvxVr_SOfahbQwGk5Hvav3kzHZ0jFCNIoV72AZQXen8FkWbFiScml7rDvmW3R4p7wJweLyMmxNBxdkgADEAbAxWf5ekI-MtYEQ_BNVVcKLa3ZT0wTfmbcAaOC67mAhss2wy0POs_0lx29NlsyCMaVAJyS59gbDN1Ssz7bBw0i_g0BAQN-gprOtyckfwLaEymuJfPKeOI5NHeJ90IaxoE7wuT2sX7qtKe-nkTZGy5mtmndWrARBvxDXVOvmNsIveglSlXEg-xOKIlOlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqdrJUpJSHxTB2KQFAPnQLKzaXw8nZJ9544DHFRSMZx9opBImOR0eEo_pDIi6wpywh6vvo26cshEtAP50cuIm2RU3q3l6HEEy9Y5hiZa9DZ5k8bZ6jvm81sTYLVr2frbWgSN0I8JU2D7NA0CdqXEvGAgl7qmjQ_runPu4MriqN-_3_PocUGtTE8D1292H7L2QTaKIsT9oFW8h0tpJ7rDRAYPVBnXxd7gCqLIGt7T2sbkFrnKyvo_MyBzkWTjY6xQQr0dwDOTuttOoDc84OZw00MGsmjgYFkQF3pZ0gi8plUPvPke0rdHGtKRwAMB3mTieMs83SuuJ76nn9VYxEwy4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MM13GpNR43AQpik8hkPp_s6D7SKCNm62Ey85E3Zf6fNGlN8roeZP8wC7UmfnYqYhLEcSGyCOr4O3KNYVJRoqDkzWdGbK0_0qEAC7yDMrnEjWmmswZRC0fblLGco0w_qIzEQWYyL71vlokOxDbthEKjrMynHanXN4UIXLuhCd_eyvgmhGcR6Dqlv4SkETI0eCmoXBk2kjEGA2a5HLW-QBdLG4q-n6bqGYqckXAcYWKpiGv8BrTovzDbd3RfQpXsOzIrz9YS0wVCcK0BoRwb1Q3OB_JeRHSzNzv9qr7BLPsb7WwJczQO83PRqO7NjIaW5wXVG_lqMJRwjSArcPL9bGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVcU-YMIivq9zlKoqnaqy4eMp1WBlWo5L4o_vcVNIcFNhpYyey6oDy156HW4ANQF_4YEtxMQoXXavcZba52EAxw0VKRMRh4_tTnCBjNqlq_r67n3pBSlCdG3eegpaqjAsA0RFbYQ7VXJx5oCkVxF0sLbkSO8MGr-acH8R_jxmIQuZO_FSjlL-YzqGE1T7_34rwMsIvnboJjF0Rt6X1-qQ20x8El4zMyWc4rOb47sWqNDIqeTY8IFM5Al7YyaAq2QZDceuLjVkAMWrVzxSLtpKLBpgWEU5SEZbjkUURBgLhrTqkva0zTbJoHjKN-_59jEdnC3ksd_RoMCVRBPN0TcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLvIlJMLqEm6FjB2w3gufnETLqgZEOgwJvB8QPengDkyanMCvwa7cirFvjxDyTkxgG_92KPEIK60o3r3GY2Uf35Xt8s_Mqcxj1WrMoLVP-oC8ksZ8fUvo3awLyPu5TLzGOB-PsQT3Rnsd2ttIdbQX52t85pYEK17jTc6UwI5BbNW4VcNReZY-nFE4ZuxHRtvIK1jeQzo86iY22KhOUB0Z1iGcB0l6sC2EIV39vkHHDu_RaoH7bhfk1aVgfHaxriNyfe0hYhhsMk1bfoib113PjdqJcxBV4fReFozl8qpvNmubynV8GBjCNWv4mo3X_GUInziHxY5BSwQCMQIN7dJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jgN1wvsVYp280R4zxgbnAt1-eqTVOvjtX_cD3KTv0dLvDS9PWWDk7LD7mXtQOKbVF29R0kC1pVLoTT0WlKvNwQOIysLh1QDTgpenRibBbGSxbbCc6JyOnmd8WskXe7Ldq6_wFnda04p3mQIegAgqz3SMiCl_sdeiYv9BiFfoyG7DIK3qihpMT7Ps2E4oJrjT3nkT0_xygyzwzxDUNE7ckqLFaXJVfdTBKnXPurgPe2iitNrVmY8-XjypVw9esN6xmQWX39eW5guHqQ9lopGBJiJ4I1m3J6WSV-SrMIhY9FLmj_82A5omvQ2blsNvZq-4vlC4H0MI9PLbGXh3rIS17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FkVDmXUk59aG-50AnddpYoGvmDDXf5C2wLXQg34hE1mBCNzWQtBENjqyDwmeycnDZDShOgFqxr4SP5klkb1uU9gzbBPIMlz_vwjwpf7wZD0rOK6tc--5ahhw4uw_ZGHWWgZCdwXSzRXM1vsKlsZ5c8GUK6WzRpNlKZdxcOT56z_9K7safvTJg8bjHIGZLZyWMotPzuo16JYkA6V0uEjAQZjV8UJlAeBEfwNvOwV4YOHIMi6nAJtQ8Hd8e0kPp6XtskD8J2kupr3Hv6cek4WW-0bLQhAEpUBKYE90x2DD8vyz4qCSGift_AfHhnJuc1D4lMeL9U0K6lSVg6AjeL--wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/keNSEDztMu3jcsPagfkVeKFXeZG4IPa4a3YnpOmY6VRlLJ4fNpm996rYhNssw-5uB1D-CLtFpAgKNY5LtIZa9SwtGSZo5fI_LEd2xk2HMmkMlvqt9ceR1kLGUJxqtb6CwQZJPlXmYnN60S8S02PMwnA8X-4SLdcqaQU5BjJDlyhVS8oIkYIX8wUWT7zJ7qXhkVAglywJxX7JsV-sSkIxUS31yeNcfStse9Xupy9qLdf8H14hBsnEEu-VVOpAc3r5ePx_2gLWdUfL5i3lxar8mHG5mH4tun0PIukTkcuD1vCldrTQwiM_IhTMJ5qdKJjEyFCi5SadexmOA9FrvQlxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oXkk5lUrhWhWfu5KE1-wp8exQbWMLGLgaR4h0Kjww8wVB8QtowJ39sImxQYKHLLs7T752Y7AbsJXS2HQXsmmQuFJa5NRlSyVbAL2qsTisUynWnK4DtlRxPmZkSvHS4zAiBWUqMqI_dKKcHK-zcjTdJE5azufo73_M6eObQBoXp3irxVpMKC4mLpk2a-hLz_T1Kdx912wN_giaqVOpP6y1LDYXo9lgIEPplejfycLF8EgsTwKXYoapux-4EryJdysFQLUeazcnrUX7jxq_ePWikfQorGw-lmI-gJI7T2TT9ufEXTAmWgiRLcw7SMLVm-ApLLQOzGg-FXkhso5M-LRig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuZ9zytqjkF4jJL71axB2b6MqEmDgc_cA_2OHHvlEeem_B7izVIJ3nkUEhu7UPHcVsWALaTjKhXvtfuHY_P6u0JWLmwQHYm0joI8W9TCUGutP9oIvlNjUViyPCY5FXO4EaNSMtb-Krne-DY4bh3Y8HbOne8ILdSqJgXS4Gcmo9WbzEHz7q7riCkchah2jAnAdfZserO34Tw_5rLtjXILa4F3ziDWrBq29sXdtSnVcgktQFi-NHx-VdxQt6GlYxDOfXoqlAishBPfPyQ5RnBKTSIo1KYiID4BTl0edlS_epDpzivSIa9RUDX7pJxGek1rQ-EclJ17bCevzRX68_903w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZxfCtKqvw477b2PpaGO3vw2-L2O3yAmiHMdXNejMOUP_8XRToufnmlCMHJAXsZ8NxUr_llaQvBA2sfixKg8Mlm0fXd5c1jhRz4gtMRkI5WCHV4dU6f3M3icGLusJFdlCBrg0eaDCp6VD2T-LxxWQRS5klkcPIKekJdU0J5a8Lx1vQtDUun62HxaaaKom6Q3wxgyt9n7VKJVbEAuGXSWZ6Qn4zn6JjR5vU24ttKKu_Vtq9YETPjTrlh3ziCozcwvw_ZpDQb8Qj6rNeToxTiqa5QbY3ZvWzN3FXTQ-kLgqhnel3JcR20Ca5o0aXPmPqDkUeHsT7ox1K_6I6tb078JrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HtsbOVNQWXFSiZ1x6_TeJqjgMR0q4purjNgFHb5NWE5P67U5DByX4O9jTe59kCkKy1mLaNQiWNlDJB0g5R8O7TpbkD7Fh6ziSLtOAAuUuojxxFp92U8v9X4b-MfUTSz27Io-SshJajspneEZw_bDpbfzNAM3rL-qW9lG9NFEXTs1UtaiRa6WyW0VHUJIR2uO6v2_wcHjk9Aw9oHVzTMKNyq8fOueR9OxGF19ayBBvninkKwCbFLEfBP-TmhMs5vaqmHd0o96V-i8rLuHjIgYPny84xWjQ6DQQogq0ZZXxDQQSr_PV13rpqMayCMmNgbQDqfEgAksKDS_K36oy8qPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=TotWHdikyPxjiDffC7bG-wpzEq8wm3PJHFjKHCNXhkUel3652raalX2ZoAHQzI7FoHb-xVpHGTqCFB8KiYRrhMVSM9yns1QQze1InXSG5yW-xPu-jRLGXOA5MJGU--nSny5oQRNyXHSBSzbLGqeOvFzLz-s5U-50dkhOP_STo388OFTbgUT6jT0EO4Sk-Y9TObIew_rRJsxI19euRL544xljD3AnfgDggMgRxruv0K6Ift0Jju_WEq5fi025gh_5u6VKTgbk3nUWOK5cvWCtI6pDUT7epIJLnMzY6VH8J1z9ajClzFBsWFaVnSO-Qxen4bezNqoLiw9YUfVf96qvHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=TotWHdikyPxjiDffC7bG-wpzEq8wm3PJHFjKHCNXhkUel3652raalX2ZoAHQzI7FoHb-xVpHGTqCFB8KiYRrhMVSM9yns1QQze1InXSG5yW-xPu-jRLGXOA5MJGU--nSny5oQRNyXHSBSzbLGqeOvFzLz-s5U-50dkhOP_STo388OFTbgUT6jT0EO4Sk-Y9TObIew_rRJsxI19euRL544xljD3AnfgDggMgRxruv0K6Ift0Jju_WEq5fi025gh_5u6VKTgbk3nUWOK5cvWCtI6pDUT7epIJLnMzY6VH8J1z9ajClzFBsWFaVnSO-Qxen4bezNqoLiw9YUfVf96qvHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pjnLAJivIjqtaiXkUy9_T0YQtq5sxZruzCmhNOgfdLyEeegMcArbqg7QfSdOn20bkld1exRoYOcG0lsNdB8-AlEE4v3VHxaqBLwhKkKiVJZngRRa7ZRW4IOL7_WFj1cUTKxDCutxLPkDjceWjeEmQlkrwBJqIbbSUNYfMKgWuFX1NmKU4-0mGe0aOTZ1Kf3ADov0EiB9Ozr2OtEEQthirp3gseIxIpRq-YyPVRxPV9ljzonnzV8l7V0Ch_U9rmcxyUqfJMdvXI9vm2YleDtI3Jukwsh8xtImwV90fMwQiLm0ZVUpPCxKrHb_qSAO5TvKErp2A3YGi9RQONlTdo6gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdDjoGjxGQ91KxyC1VE5iPN9Ld9GhfBmA-o4nm_lnKDGLqouBhVZmKQOAdTNW0Hv5-qbvOMHlwti9JUBlylZa3wS8RAHkSo4G-9PkG_jt0M-zCO_UbT1rXR--cAggxCBBuBca7DB7_4UUtLTe3zEiKgb9Az3SPgfcVfRcr-zuz3zpVKaJP_xgx6JVnYuE7dS3yr1ltXS5Q8DTteTLv7s6DkGgmakg5ORhBO2WcWkI-IkzUOjkd98UHxfi8mgXWiMVYDRgL-zCHCUwtfz5lXAQ4eUQrSD0nGbinV2uIVTStDg_jB98-E2NaTq0vEHrF-5YpP1-Dj_7zLHb1FK8l0cUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXHxKToCj-CLY4j149JMmn29l8dDUoNojlI-3PQQ876U59S9hgLNxnOp5VDUg3Z36-lrrci_H88dEMFw7fuYOCCpn3Buq9YUuj6gVOxCa0Nu9-cTOWXBT9QvUvJXrKHSsLlqZshNKgsqrP-4H9-FikWOAnMEf63fGyvb9F-dLqH4smx7Op8Gvc14RAsBTCrNnOvdpz3KQ0vQp-i8T-asFg5IMrToFdVEHx_2pjwvMURXCkdRDXqaNaW67M9l6GMjyB-So0m_u82N700zR7mRDBmZG7pER3tpU19LI5kUKZFTHox9ly4vYxQ5HJ4rHgdAp84oYIOVdjuVgtzbjpJ6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=jiOF7gfLqFsGTK7EAUjOMEflSRGOtm0oeyBhXudd8NdCAbxAB-AvXB8zjgCvHu6CGQAhIu92t1fw8oytCLI5xwms1KNdDtwA7-iVvm1LP-lorKoFKZ1LkrS_YIJGYIne6s3-iUwAq2qxDWQR2t8Y-FRU4BiCKkixkk_iDhqca3I1EJM06Fm19vBGQ4h4gq5Pc-TW8wIRN-g9mumGm81ho0_11qbl32AvF9cV0X7dZrIYRuHZOVS99RoUCDtsHFv7yD7bFS_IZDXJy8tyKeARW3RSpvSm6SzN6LaFQ-CacG6UcwN8FMEtLQnA_D_fbvt1oboBH0LdNvfC7N1Yxmne4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=jiOF7gfLqFsGTK7EAUjOMEflSRGOtm0oeyBhXudd8NdCAbxAB-AvXB8zjgCvHu6CGQAhIu92t1fw8oytCLI5xwms1KNdDtwA7-iVvm1LP-lorKoFKZ1LkrS_YIJGYIne6s3-iUwAq2qxDWQR2t8Y-FRU4BiCKkixkk_iDhqca3I1EJM06Fm19vBGQ4h4gq5Pc-TW8wIRN-g9mumGm81ho0_11qbl32AvF9cV0X7dZrIYRuHZOVS99RoUCDtsHFv7yD7bFS_IZDXJy8tyKeARW3RSpvSm6SzN6LaFQ-CacG6UcwN8FMEtLQnA_D_fbvt1oboBH0LdNvfC7N1Yxmne4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2TpQk_x_Z6bbSW8WR2iVJN8B5PVNVhFoa8irRs1XlO3WYg34L9Ldc45dvsZxmV1VRN3e9hZtlwzqij-wbkJiKJBzS-7zrM4Hk0eNIuhYez9D-NTumKMHTWuSpGXVqtMev1tcy9nDmi8zaSQnt-WUYXNZfeQyxjU3z4wAe_KKB5iIapt5y_twEYoJ_ZoKRhX6endQ9HH_8BYzL5hlql3n9Hi9IBHsHin-rOPc27QUSPQWKqENyQhtFnjytjB-5lqjcGfhZ5KQYsk5EeMsLEJCFDLziokwFkMfVOXIobgr1-CKBUr_phCgUwDdz5wmRQQ7-F5syKtl6Ax4x_6cQVpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
