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
<img src="https://cdn1.telesco.pe/file/U2lV65bWuMaB1lgVmqzdT_99XtcRzHdSeA80e4PTJZXQiiHCwOB0Z41vMhG1lE0hSdxdrdcfGHNZ0xU6EmOuTML6l4AqZFTy0bSFwrAInPWvt9MTfXoNE8D_K8AJwY70yE6lZDvP66fdrK9UAGHdCM8xuxD4fJwXCAkAv9AtXWhoBNq2LPMfrBRNv_NwIpWBWWWtMIX4UGimvf4Ai9qN6cfnOs_Qga02F81LfThzlj-JI4mxXDLyOT3K-h_8EqQ_T9zhKWp-hcbxSF8ScZyBQ-eSvGSQhCaSFYt8K9mbtVSHXCSS5EkdZf_CcKO7QkCAVmbYTCjwwYKlqR7geeHcqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-78628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLlEQY_6PCajquStLnFGKKKEFHS1nZDkBVCIdaiSxhyEFW7Tp1JRiDnQH6GZfDjI7rT34L5MfYKmnbR1rypEoMzorEAVGu0AOWwBEm0vBwP2ry8ax_X2ATeYVEh0o7IUL2tmNFHHgr7PJlsWSNuO0DSNjUEjjkDPJWSxGLVz3fOnSq_lY00ZUx8NRxG7TVBynz6Vvkz91Ke8WquOOnqBsE2-2ct5FyVXPAPpy9iB-j2QXsV9wHLNtZN536TY6Ug7ILNmhRX1xPymq7kqiKosWE2kj7rVDZmvCMlLA8bYpMV40PMDceE-L2FvaW5WO1DWjjLh-nAMh2L6fgYd17ZPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید آنچه باعث افزایش قیمت گازوئیل شده دیگر ربطی به تنگهٔ هرمز ندارد، چرا که به گفتهٔ او، اکنون مقادیر بی‌سابقه‌ای نفت تقریباً به‌صورت روزانه از این آبراه خارج می‌شود.
دونالد ترامپ روز دوشنبه ۱۳ مهر با انتشار پیامی در شبکه اجتماعی خود، تروث‌سوشال، افزایش قیمت گازوئیل را به «پالایشگاه‌ها» مرتبط دانست و نوشت: «پالایشگاه‌های روسیه توسط اوکراین هدف قرار می‌گیرند و پالایشگاه‌های ما که در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط "دمکرات‌های احمق" تعطیل می‌شوند».
اشاره رئیس‌جمهور آمریکا به گزارش‌هایی است که در روزهای اخیر از افزایش میزان خروج نفت از تنگهٔ هرمز منتشر شده است.
شرکت کپلر، ناظر بر کشتیرانی جهانی، روز ۱۳ مهر گفت که داده‌هایش نشان می‌دهد صادرات نفت خاورمیانه، بدون احتساب ایران، طی هفته گذشته، با وجود حملات به کشتی‌ها در تنگهٔ هرمز، از سطح پیش از جنگ فراتر رفته است.
با وجود افزایش میزان خروج نفت از تنگهٔ هرمز، قیمت جهانی نفت در محدوده ۱۰۰ دلار در هر بشکه باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/VahidOnline/78628" target="_blank">📅 21:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) روز دوشنبه ۱۳ مهر، با انتشار اطلاعیه‌های رسمی، وقوع سه حادثه امنیتی جداگانه را در آب‌های تنگه هرمز و در تاریخ‌های ۱۱ و ۱۲ مهر تایید کرد. پیشتر خبرگزاریهای فارس از هدف قرار گرفتن یک نفتکش در روز شنبه خبر داده بود و روز یکشنبه نیز ایرنا از شنیده شدن صدای انفجار در حوالی جزیره قشم خبر داده و احتمال هدف قرار دادن «شناورهای متخلف» را مطرح کرده بود.
بر اساس هشدارهای رسمی UKMTO، روز شنبه یک نفتکش حامل نفت خام حین تردد در تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است. روز یکشنبه نیز دو شناور شامل یک نفتکش حمل گاز مایع (LPG) و یک نفتکش دیگر حامل نفت خام که از سمت خلیج فارس وارد شده و در حال گذر از تنگه هرمز بودند، توسط پرتابه‌های ناشناس مورد اصابت قرار گرفتند.
سازمان UKMTO ضمن آغاز تحقیقات رسمی درباره این حملات، به تمامی شناورهای تجاری و نفتکش‌ها توصیه کرده است با احتیاط کامل از این منطقه راهبردی عبور کرده و هرگونه فعالیت مشکوک را فورا گزارش دهند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/78626" target="_blank">📅 17:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gg0OQh9GY6P82NxZ-I03jEiZXX2aTNhbPt_77YPyB597UcTbPYEgCTYVIKlNLOBjjHXNyi6eKP03I9gOacByDLj53iXDvNcpO5Bu1THG9XY8dbGaSKfk0mQhvyTVf19XN5nm3Y2Pcy4fqNb-hMly5D7Dz4ymUpE_HIl990CyvOfLtHKPkbBsI8NhxO37UMLoLeggfTSj34p_Icp8Xj98ZmET6WoqRN0z4cD6Ab_3qpNlFOejKylDeovIGGuVSdiMjSnbquW78BMlxu0cG2hGdyCs1zdz--xBjJxwiyUmCfHoqFNRS37rZZaq3HiZyEq5gReE5lL01_bKQWOcBwZPkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78625" target="_blank">📅 16:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnbpM0zK_qLyQ6EW0NjFv0a7KN1xOLofm8arNaMBVUN3lSJk7MWnjKD5ioa63ntZKyb03fh-dhzzJ6ZmFdGgIa-866_X1DolzzN_loEG-QD4BOfOmpTzE1a1Qzok8JMvZ6N9upPJ62zp58gYmHNHJ-gxbMMgb8LqIN3IjsxLZRXl_iwtqioJMXDfhN2aFz8ksdeFE8zKzHPlVbYiwqI3XZ-hb_Ut1nRVdOjJCBN1S7f0jHyxi_pDAkuJDStPq98mZKrf1Ud_hnOgINwsjN81xyjU8DneTvCEplKJt8duBN2KK3CLSCi62m_cE7WHrA5SRX41xwtjReY9jh7FmZkKqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/78624" target="_blank">📅 16:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ethW8rgU3wUACLWb_ohuq0bQC_y8nGVdAnvxhDjM2JYjUKCdo9EaPDr_eO6-H6cpU3_CEMUPoGQri11se9lyKCnSn_gQvkdf0-IRKjmQJZGg9xClSMXgHedd1FR892nBDzGHr6hZil5IjnGysYiypk2D1NI8J0u2Fc1Wuko4dRVb3u3hU7JaxqhRdZw9cN3L3hTnyoLr8lbawafoMAqlq4VwU2q2I0sv31i53ejEimmlxBeFTtlfEC2gyaBhdBa4ZzbwvX3anWbiT3j_mGwcMj2ZH_NVIfVO8pX1_YhqNE1U6TtdG2pkb7Wbth5hTO6m_HQYHwmNCd8mZCP0C8U_yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZPBRJVxM9e-lYgWNL9m-aKkMwAUUJySXwd7vJZI6Cs4JJfclrd8-G_ehG2RQmX9EexX02Yr_m0ENJ3xmx9hvoA3PRp49p0ki-tlZxXSIOmWIraTqZfvNeCJV_7UvEYehXNKMcQqR4lY8105Qq4OMmwp7gCeXfYsr-rQCx82l3625VkZPxdzONn4JDtDTRDdqmaZ033eq0CG83GZOL9s7ZGCxGQamrIzBavWDhY0EUNZbA2skuTK5_JD5VLIGQ1VLwvitmWSWvGUWp0joRa0WvT0ao_ZRf9uygkcMe-pqfE8BySMHc5EfJa7pyWbqrF2ByY4R7ETYd4HkmZHP8KVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPWZbkoro6Rb23I-vYaGUNI-VlV_46Glx-0yevRJ1U0FcVGrRJBWUQUXGAj-wVW1xYQCl2SOtxETnDQizSg9Mmk3jU695k_cuLihDxgiF8pv4fzU3NWWL4a0L9p4T1uTSwt9_CRQ5mHYGIHjNLD7CAlo4ADg2k23e21N-GyZSP5XPxu4eotO-pESeuNHhdaJbeloY5gui-vDXFc8UjTJ7H4Mqi5GSelV8AYqivvyLxj8Jlq4uoSZNs03lk7Pg1ZHfpG5QdVAxg7WyIEH8L_4dS0ROe0MCWVlGCA2wp3TliuXdcjzTNC1_DHJbbC7XEC8epIf2Xx3ERNsTFlMxvLI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ac_JYQDCgiKD26vg1167gvWWJCiQooQp9MJ9agDa4_sOlU6KSVq--Cq5ShXiG1ZRtc9uENbn0SpZXUOtrayC8lFPAmpK0L8wSRhXmGSOfMSnyuXfz5Amg8gUeZUsYMX5s2fRIszBSGidXMgyxJs4vBSXZ_DiIriCmSMg26ny-b2DrPFNZi_HeEF3kbOY3rMjqe5qqIqmaeZamEOW0KuWnJSBqPdXT7tnltDA6P3wvadruPqZvcb7MeFusKNiH4AN2Pjedh_aSdIByh9z1CThvTrstuvjaK0_Wx9qoevSpSWovr5mHC2fhaNPIMPZTkSbTWJKFhBi-vhIb7jRuJcAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=b_hu_UUBz4PRMP1UQmlW1HBAUB1L3s5tQHacROsIfessHxWqbDsTpIvvt4b2_nm-aYKwaqFl7zOg9-BcPeXJtv5s0pTz6t8l1dWMhCfI1tKBE7wzzgapG-zmdJo0Rymf2Ciy8L7MhOuo_G1aLLeMjIkhlfRp_gSA5GmH9UOEDmF0PWf9B6Q9n2IogxPxo4Ieos79NoFIouisheA1S59dVsYFeggY6lLjn-sLD7q-8jIrwefRV_8zdnE3zC4wnvkRx2uuG_CZM0C2hH0IWKijWb6Con2ABGvtyJf6os8ydVAXTNr0fQZbSnPMoPykLwT9yA7ttIbkMGeQUpwW-ye1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=b_hu_UUBz4PRMP1UQmlW1HBAUB1L3s5tQHacROsIfessHxWqbDsTpIvvt4b2_nm-aYKwaqFl7zOg9-BcPeXJtv5s0pTz6t8l1dWMhCfI1tKBE7wzzgapG-zmdJo0Rymf2Ciy8L7MhOuo_G1aLLeMjIkhlfRp_gSA5GmH9UOEDmF0PWf9B6Q9n2IogxPxo4Ieos79NoFIouisheA1S59dVsYFeggY6lLjn-sLD7q-8jIrwefRV_8zdnE3zC4wnvkRx2uuG_CZM0C2hH0IWKijWb6Con2ABGvtyJf6os8ydVAXTNr0fQZbSnPMoPykLwT9yA7ttIbkMGeQUpwW-ye1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3Hgphe6hf1mEAyMkeHK21Eggxx-sk0ciHFcns0mUw43MxoDDq_-88R-nKNr00jO0mTF6wx_J8hI6eZWdsHePq836RrA3-z4onwz-cHJ8oHqHriwcnwh5VDF1HpQuAt5TbW39pyBUZmm2liJ0MKgrB85hTJkQ7FeJrd2b8oLPTdc7XkJLSbVkXDnNN5032MDeS8_q76YJxThJNBJDF9NJ8F8t4kPmkbmfMMEYmam3whj2xy2P9TBXT_ZX2o00VykP3df_54H8h4H2YJul62cuD0wSaKhxHcqQgMgliqsScpvTFTofrPbylaFAkPp2c7FGa9G2OI8QfxGOu-_Zznf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6uFP3YzhlK8o9Mu3VUIumhY24i-hVL6jyeYgk5yrG0b9U2KuHNQgGf-1TILN04n9H7bETbXEH3rCwE169MH4kkG9tVZXL3ZFDtgthQvS96VrUKdQpuj0Ig9ZhBWgjq8RyR5vGRiHUOS_6K-H5twyqZIo_-eKV8b_BvspAl7r3B3rs79MYu6En7XXazSJjdXbYE08EcQBQG64q3UqUNQO4C99QlQ7m7cB8FSZBiW6V9Qq7uCngfbIbYmwz1uLAxu0GQaUSveWCW7NkxHBELHyB4_LebyAoO9QrH2biiXvRftRltB9KSqOm9-7DrpgKTlXqgXDd-tXzjB3Q_9DdgDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWQRMIGVhY0-098DnuYbK837Ho3mIbDUjpY9NWnZHumKw_iT2lE8v2zF6aiXmlnfRvNIDlhY2Z1XcjvCHhWqR1KW3YnpG5sEQhmqGZVAP-bhfqH77CbH9ATVM3zE8e9e0900vW0aN2Vj109GQIzYnBy-Pd0RVPgKAFxmrfVTa9gjyCZpbDpTK6wV5weCnfGBkD7xX8lsa83ZI8Tiel5P1Q2Tb5RcpN6OSVM5gmnVhberIFE-_BQIWbIpwkPc87FzQ0dIX4HwwDfGMKiucEi7mlCaXZU6d6AllgrNAAqGWGSpWxhumOUM2XdN5K3GoHyvWa4NCIVSULgMrhvHQErJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2DjJBClPiYe4c_HvRvBywiO98yA2O0yIALaT-3CyXIWfItRTqfYpfhWaOz8Oke9Y3RBsEvGBmrxm4Ye2ZNZUrK0mEp2Ouyjd1K_UAXiAwJn5vX5Rux_bqIlGK2HpXwRgFutY_63qc-lQMmTaAR2AlozmwQRujyhbxtU-AizzPJWW4d5vQcJ8PIxnTSsgkvzbYTo4hEAX1gpgvKQVqCVTcdiW9pSADTN9O_2HgFuEqAfdSfugBdNhcKzZrct-fuWa7nDXb0T0hkafBC1wUDQXUzApDdampbJJfpZxblTH8S5YXLwtw5ZLLuQ5IJ3B95XrxpznfJltADakOokZjNIVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYyckf5RHxS5U71DHg7aDue2XGQLTF7P8zPeTG0xL5I_ydbiYDq_gXZAjJLaQ90aIZbyCrkwZ-lLONShR55AVkIq02BikEb55rfuvWKtuun5r4MxgRVeIhgjf8hJXrkT1CB0WP3n2Hbcnzzh4F9-J3Rq8p6iY1bk26wpbHGkqjzj-VCwLfGaiW9ZC5vzU98NQZtt_NuSL8S67xGHNSUq03ZpKlc5Q_qmvhjurJiiDD5sEPZH8SLoo88vX-VyO163vC4rneKsQNytXswYjJukNE-MFKC7yOjbWH8bXzcEyo4wcq7GhI7JXMGqDSIQ8IzWvmL0ktx1SwhL_dPhRISXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niTqqXuTPteoM_eiN7RJMm7Rm7kYKNF7SS9CYLRQPDDqh8FnsqHgNxarLn9_1SZCNQuSBbHFWxzK0sSHB5y6zF6IuNpvVaMZ10NkxnNeKoJam3w0x8T7LEBlTcngZneT3h8Lsavuq6tIS0q8D3m8X1seeQbSmiOmHf89Kgg-MV_3fIlKXk-gPakunEBayXnSQ3A6FD2mNp-MPq8EDadOsJKrq5_uUCtR56Ks7RAOMdmj23eTBVFenSZGNLIXWZ3V9HKLRb9Zb-V5EtIT3crfBAVewa6XPV-SqqEZ7hhHJknxal6OjrcNri6SphONeJrKtuXK0mm48TmhqS94uGN6xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qy8yWmuRhhw-kfI3X_yqqt32wTyHEpuaPVnwFonf05WS45fMBJdAP-RS0Xd4BfbjJ9okDJ1VVdWG3vG4dwqAGj3oZXj-R_RwRHgbcHGcW-LNspTSE-SgQPexwyOXV0a_pMKuXxfgrXeDYlLYy3rq5v5bfLQDQOj56xWY5weVDVbBVceMOZCOiiSvddCHpqQSPmHOiqes7cmvqKk7ucH7_jO1Ai9T1fapHegDHSqjEBV6N3npRmBSLbPXEuszrQsD9InDhKC9qVzfyUTqZv2ajYEAsntPsPGjIiL0JAwEZEnV1-Nsd7Y5nc3Kc-nDLnInQNkvvuu2hHtEoaPKl8IXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR1zzAhFO4_x85rJ91DwhMftmdGqH5kiMzA8hnqVq88NrhWZ6LwdcNDdB2dPp8mjrI3LM7p6tzh4hJQKRL2rBPe1GOd5OjEZaROEuzZv7rLcESWbS8SXk78hkLnR2j1rp_MTLpCU3hVxSaCq0nB7gNS71bxtDXMaoeKvLpW2vTb_kBu9yV4rox5nN8NOPx3jiYmhh-mYp_RZC1JRbKR3AOgxwsh2_WOOr2OFCNl_ef-6ugb2ZHwNAYAtybZujLigIgrBWJJlfb7a0wj33Bxfh2yNXPUmtK7qYjeDXaC4fpKxXVVMfa-I9JM8TWODPZqk0QeXws6wgBEadOKq2TCgpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNIkLK3XZUgiRRC20DUNreEkXF1dBkdO4-LJgtusmK1e5QD3SNIa4jEJqTvK5NvauodQLTaAhX1McEYW4J57UDJz6zsxZpldFvDPmw9WMlsJPdxPbWF4ej-z2nzMkGTPrR7CWlXWkQi2fHBPf613FYHRLz6E9kImxOuhV7wrmkuY4hRzKjXx5S7YmeIFe8MnvtavVvWK65qsZt5Ss8sHjcWPl0exSkOLQj2A10bNqf98EVg6cVylRR8AKsK_122ve6sXnFhhqejaGCJqjJuK4XRbLpTZUoiA0FcOOjnB0riknBkyjcJ2ewHsZxpMHVWOqMLdy9r3qIiTQI6QoSexxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opYl565vLZzSq28kXnZmIFWHnC9mX_EiPiTzO0bLFhASIiOnOJ_ZNoeFRdxK9E9HITYbZ1_-3cXLBDe0fqVAOkDDN1NNsRoYcipCvdeNV-PVrEjBEf4VUfmwT0tIxdS4wAYf0fMJ0am3L0qAy04M_Ut5c8OoZudTBXO14Q4uZTPmDy2mgdLXusMijgrxox4zgQeIHJrt2pkZTE4d2CR-6WZCElThB5LduVKNPiSL6zPFgaafwaws4jphjyfRZGg1sXeCPZH84VI-PFXtlu5zPdjo233-KX__6pgpRBXZ2d-JPFCWWRMKAPQLV5LLfBH1ppaJ2oQbiApUL7ceLHL0VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OEd6B76B0nlJnEU1gl54FOSGzyfU8OpVIIl6L4vgc1T3u6v40hFQlanqkQqFo9Oti8IJApAuXaQHlR0MGzFRBcA6BESvRtJlqcdmz4NQS7q1sTUMLNkjTavYqM-J82fhRsw7m-HgWGFAYmf5_NIgUvSUS5I6XzNnzBLKay_CaDRFn7iKw6LWnlp_CnMflH7FTRMoNtspTW-PNbJbarVE3jNer0Th7OCBZHWVSfVJl66nCuWIQd5wxqk4Hzcm31yDq1vcDjIfG-VgnaD7UrdXVqq362OYvfGMuUVMOSgfZBZwQ406vQOutb6L53Phtm77Ga-atE_anTHYjtNvYbNv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fM61AUmPkpPya199QU0lEU7kIeY_9BmROdX2LE0Q8aUCeDHhPInadlAAtAfxffMitf7pwkT8cPMArpm6Q8qkjRusP24pD6FuKspcNV_zRcpbv8RUKaElz4cCYiWXn9yZTOpj6lk2ZGcA6by_Ni8ZmabnY_Gbd2-BruE6rUMqQkXFls3Z0KhpiLBKyjvFWg7n-G88a7DCGWicW4LqmXEQ1F1W8LIHmUIP9BqbroCiv5NVDE2BI7BP2DA8p4NfqeR3nCUvUAx0KOenltmRRzneefP9EIwcpM6WN6AqJPDr2cvWz_yJYPSDEy-GOiVdiwvsMFROcUA3mYDTFqPeHK9VDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVqdbYzlEAB1ORig88WnyDnv_E5iN9uezZdsX3SNc1xe0Gbe-QSVEM0wPrAxaMb11QTrvXJNyKVKV7r1J-kxADq-hfh0p7BaRSDRc9bMhb58zHl1qOFLTfvPod0eH6B2smhJFD4SorZaOSKUX7uSjbCQJymAtIc7rx9cllb0JGD74jOwvap8rcshe6sqOXv-tJOmBIc0sD9xUPmIVfL-wowbHC8jG6JYJPcu3VroW96W6dztiDOdu9WGOTmxPM8bXTKTpS1Wp5GrmEUZRviUVVi7enHR60Tc-MgDgIof7KlvYJsAk2Pmw9dg0XJsjYBxfwgp7EvYvTsYcThQ-0CJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3zX7dI6ZDnx_OY326CkHdFvBvjDouqB3P_ORa-DhLsoVE_rDIobDYPIOFL9VLjtj6wl54Ag7A7k5P0frrlrn7RK0dZM2BBLQCImuHiRj7hDJypdIoHFVQMIaw_NjdcsSpVZiwB-esP8fz996c5E1Xke4y5U94XTJUOcOsOKnGNGJsBmIE2VfUu8KETu4RdFQd3h6jL0ZEjCrw_3hYrANGFa5pz2fr7h901d8lKkIDZh6nBRng1Tc4BBOeVX7t4m0mozvqCsRoMMMdoEvtLGa1_jG75NS5HPHWsX7z7ZDTmIauvsozVIS0xv_jOczo_gK8zcTTOrmf-736zVdVR07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jHzZcJDKF9ZBYdhDGhQUL34KzB50HS5rR-_9HBmsPAYH80fgepdSFtRnZTbX7SiczTkA_fRBIKpu9HCun3KP-ei7m6U_9ynNQRPfFKzJKdSClau4wrBsve9XFGFVm8fXSbXIscAGOzH_iWdv5vAWx92i6EkuEE1IZOQpTWSSlvjwcoGRv2khEpZmmu2eCx8uPVoMNxSGXtW5LHn18ATrC4lgJv-B608-OrJ1cmRs4AaMH6shnt-KYc1Y0aznOliSohYw27KAvtyWq7mqs2-5wH1-W0b7DYAY3A9UKdf_Rg2pU2_CPxCpHo1-xQWlBeiG5TOfOFVdUp1GSkdM8DWwlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=rM7teubLrKGVEHpQPnJG-E2ktqWjBaRBikURdZe4XECV4KyR-852sMhlrOkhrnoGC-Stc8o3QaAXCwMMDu_2EJPI0M25P74W7UL1JPvi_Y6jMnicdWHbFym2sg2toXjUPR3CdlIsH5t3tvbBkOUciHgN9wtIKGGbK_Ydm141pIJRHFtrIxnQ3eyBKVc0_vT1RhWQADy_YKiMzquoqpc3asn8jaylYP67YaKZ_HHC9viHfPFZoTVdnjqw7Wx47bp2iw8rxsJd6mOCUrvu1dx45_lbAJP-a_mKWaKypn33t3bzXwDeg2lzn6Tfn-Kr7lAzdU7LGWfmuajvMr9zhz6KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=rM7teubLrKGVEHpQPnJG-E2ktqWjBaRBikURdZe4XECV4KyR-852sMhlrOkhrnoGC-Stc8o3QaAXCwMMDu_2EJPI0M25P74W7UL1JPvi_Y6jMnicdWHbFym2sg2toXjUPR3CdlIsH5t3tvbBkOUciHgN9wtIKGGbK_Ydm141pIJRHFtrIxnQ3eyBKVc0_vT1RhWQADy_YKiMzquoqpc3asn8jaylYP67YaKZ_HHC9viHfPFZoTVdnjqw7Wx47bp2iw8rxsJd6mOCUrvu1dx45_lbAJP-a_mKWaKypn33t3bzXwDeg2lzn6Tfn-Kr7lAzdU7LGWfmuajvMr9zhz6KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DHa-G1qImPpFRf1MGo2ZCnSplvkqyQvqCxl7hxFNi_UL02Amu1YS4ZZq2n2Quz83ofVDJWLCmFvuwvpyJ-lRlOmuiw_zBpKLoKcyCsuzODsWW8yAMea12RKHvaHvY7cJpTmK2DVn1XNqSTY5Uz5lZROAyxbFvJfTesGDZ7whzpcTUCRvSz1IoRG4ThdKb93FNLE3ySayuP5a6rvh1GdcKPjeJjuFW0rshKUnK4xAhBDhmnbJg7IjaiZr_2fGa8Gdk2P-I-4r-awMyUMQrMHBwiVrNNEyFHmrmgxRMzcQ8YDWOOek_Ag40L0Fc_t6E9h4kpg1v7m9pv73Sr9ScX-V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GM4YcZoxqDo9VSi5l1nXg4R3XaSOnrxDgSYP6P0LlUqa1-dl3eW8a1M1jr_3zJOCQRWXzfRSZkugyckb5AP9HTex7eUdMTDzY-iAMLvj3fPBUCP3sHeUd9Jf16pIe7VVYwkFgjkyW8fJz8T6RP9F1Hupm4wNd7SKi0T4hqDNvfb_nyK_YA2y-DL-neL3HtM_dRfLXZ514WnX1xE2HGMLpvtoQJpu3PNKK-fbG92t5rFo5v-7Q8rynLWqXrlWo2oyU81p8PYHOfa-FOBwIhwXUgLoM6H5qps-Wi7mELgkf-Nukq3H-y3n42VNT1vWRRGA_xc4yJiUji_KNSDxJ9Z-gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=VGUem0Qi8UxQlEOzm_ACSTmkiGrE_gMkJsPspky6Rp32dIhsHx18USzLULPJaxwWS0VZe80IDpQJ8szRhjl6nsn5kDpF95EX2fom5JIkMc_JJ28ppEGGhIkX4UHJQQYuupwuOVblgQMav26VEZ-e_En8Fp_Q9n3c9thjABmub6enHU82FKIwqIQO0Rn_RVyQDWdY65t9EiLLPda_OIVwnPXfyFTA-62dQiqbby2ZbZ6TUC96VLWxpAgDxr0nQ884IEtAbeI1n7tvgcq5EVPqtmxoyXQAZAtR1fbUAAlrF_mzr77ZifV7s-iScwTzajKAOo7EKvbqn0AT6Nsxt33uyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=VGUem0Qi8UxQlEOzm_ACSTmkiGrE_gMkJsPspky6Rp32dIhsHx18USzLULPJaxwWS0VZe80IDpQJ8szRhjl6nsn5kDpF95EX2fom5JIkMc_JJ28ppEGGhIkX4UHJQQYuupwuOVblgQMav26VEZ-e_En8Fp_Q9n3c9thjABmub6enHU82FKIwqIQO0Rn_RVyQDWdY65t9EiLLPda_OIVwnPXfyFTA-62dQiqbby2ZbZ6TUC96VLWxpAgDxr0nQ884IEtAbeI1n7tvgcq5EVPqtmxoyXQAZAtR1fbUAAlrF_mzr77ZifV7s-iScwTzajKAOo7EKvbqn0AT6Nsxt33uyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxiT7YAhHQxqOloVshdQ35tgyqGNvPEdvOoC6a6W1kZTw-83sWctSFeHA9NnhRK6bR6lN_kA6VZWyboKlYgASuePn3GTAbsQLVFuy3gO0NbrtWezYoq_OF-dLHCd0sV4tE6UXp_XFIsOfbPJ0T9Xs7LF7nGxn9GQmbvZZblKwa5i87irm1i_per1TF-ZYRqvafiKIDhdSLVKEMsndH1DTqwv2bzXK24cBxf4_QIBMNvXkMNFt8CIPeSy7wN8BlJGnh1kt7Z1nHqLx-bkLlChAzcmZgQlFN0BwIbq5_7p6fG1x0Cg1rl9jsjSw0EWcoFA16iZj8IZLAG8kTIlvyuazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9ATvB8slfTjCczt2uh-OJngOz6geZ1QMstZ7unvXl4OpHflJK8beJ1iWblqUgpUCc1jDPV8ITqZMs-HqMP9c56qMtx1VLYRX_RHIq28oRaBam6HrOvyB59F1Z4kBJZxc1ADm1SNh-44bmY15rwBGCayFHCMN9GklLsuQxTkCQmeBmte88PBchFNj7oKTpaDtE6uDwxXsG5GsRNt4RZ8DkAEQdt71jQKwVoMUoZTx2qp1xJAF2W4d7y5UWDWn1wqtya2wGBoBCcf8yHPDVPxiVVi4NRKAlPh7U-kJ1iMNspB2e8F0aDpZsEBh_2FWpi1PVDATxBw3sFUILVFDeqaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4dDHVkehwTQ0QFOwK_3gBox26vo1VG9kiTH0hm2111xoR42cSuIQ8s8ulULe4GAoBWfMwZE8pv8LPpDJ74RPPxA3CyfjUBenUgptvcp_a6kNAmMEsQMgBbsEidLZpwZgYjkhLbw504d0k5BAXU2eZdsxfh_u2ArUq0CIm6Fq7Q7FyvbJ0toECibvYMpeD-r6ykSKaEGcLdJ6ONWpk--mV3mEUa0C9rPcWvvvXbuNoX1WjoT7fra-r6TqUVxLJG0EBgsv7oG38iNKECrAz5e-sxttCbQ67xH5z_Y6SEk1KP9vr61d4FLIWkg_8H_2cHwNcHmstbHNYDThl0NtUrQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJKw_cs3u_cjxSu5SWFFj5OuLAjjE4MVb7V4I8XvMfxVyZPetkip65K3P1d9EBfD2uFIsBwWr4yS3_8_1kCE82xtCtK2UW7vu2o0Z6MZm0vbq58WFDtWffUKmhR0mDO3J0Cy54s3swpn6U9uYwxONMYAX1t6brFBdkWc80ecRpXgsRxANOUvXFvK92XcQN7uiq36OZ4dCweEj-ckKX9Q8LDCanhUwh1xWba8pma9Xv0imCPECbrW9SqV7uZ9wMDqTu7ehQ8-CZ5ZlYYkFSDPpnubAojtGktyhK1_SeAQJm0Fl5fd7Od7JWA1ORevvdBqCwc1ulnYJPla1eII0-kDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDLi3V5iM2mTSwkMP5O9j-mkHMpNuCMMTbxQ6YZpS-P6nBjVtVJGqJIcRzZ0CI4JLKFIVy_8O0sgRuqfTgk31OrPBPLTC6g9FPAIb3n5dXIrvK3akN9pd-Z_IEwSwGzMk0PgKTZPM1n-_HX6HqTWpwuPijiRq6aTyilV1qRjQU-VuigkYXDEbhS3uMTKb1INRsW42pKmqow1zuMG1jngJj2zX7Z8Q6-1S3wsbAE4EOfXA9gRPYUEJAjct9GXRI4X2-w9X2VlUSbFjDvtd1VMV7PTkwCI3aXt1QTfXODayfVupJMKssVC1z4OIrrVC8KSEp6Rk11lgJjlGChBlSFuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPyWdYOYyLAa1DEWKoBDIgufvjTwqQRo--5543-FQ7aGOLlcvGK50R6ZClfYYnR_BxZf1Qh6TNBcmwztUMlDr1fqibml-uqHU-qjiM1MuhEMXYVoatzg9bNgT1rsEYRFGG16gQ8uq6yALHmqzrh7rbHy7lXgw9zswpm9CYbdwuFcitOiTHxWYAYyIjYTyqe6Ey2EZwOi9Fr5PW1pL3KT2issoCbhMmgKkhp_OESMko22sH8qrD-5C7YFH2v-Ee5d-YrretSSzwYwiJxAveVTK__R1Wu8d7m3MW4D0HV1uzfzQ3vjTQ6iAlRq_Hle-A6GDW0XoIRUp9S_Q6r-16Zi6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r436FY1u5Oud0ZgtHOFvcTXWwcBIUlcjsxGGdBMisBTiH25vchbkiablfIXI_36INH2qYXvC7FTdi74ZoFWlBIz5YO4opTtHEszSr9jJt_6QyyXgcNjuKDCSp6ARXzmvhtoev3RYvvED7iZCKXe2yYHD1pHkZSHd0lWOfWVUrNKUCeOgzzieV1or364UUaQpEqxs82YvOUUhhvkctwJKQbXGjUs2q0Q0fDA03hgoCUeGvdHWS2Uz3YTiC-dM21rPaxu_WNVkcRuqwZsSjL9MsdmTQO9M8JHVNG69C03UNV0gfjaGPwn7JPRt733XB1pYAq1Bv60-P-d9x7SxOxdLMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD93rOIQlln9plDMnnJMY-FxoxJJCZgUT1mYu0E19QN8SX0AXM6PMX5lM_hlRHm5GxgD7qQPcXRxMymXQ2sOM3fnt887Bhx3XvvYGEfB0rZ-i1k9YNWtU0zTxp6MVubMqMI0t9ELWrHDVQgOJ7Dpy1zhdfs4ydresWc0ZQTaT4MJdgMyNcH3FCx3AtLGn949miovflgBShtss4j42Wqo8ZwR5tlnQ0M5AXnV8YyIeWXEetZ1A-Jk-cPHLdMu7xVe_b1V5x5YJxLhtBQQnD3IO-1Mer-_zbd4Kkr3hbRFET6b_w-mB-UJt5XzjG7CePn6vcsfizL6lv8MHbNhirB-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSAqEi89Rns2WMVfVSdy_lZQR0et4EAPHeq-0K7nZC-dxQDJogrWs9uHVX5as28i8Ox-CkFPTsF3fpX7JWWksjSqWB-NLZpPS10PlNdlqUDK5YvZE98mJVrjxJyPVcYTdqjtxl5OmYHoM4ckX41HZJyzNgD4qYU_QDBPPVQkyFP06aCfWb9zS9Rappu1q9HwJ21I1s9Fojk6-CY88atksZrvXrC1Q1YG-WrpgONmbWqZFhJ1yLjhm1oRMwZ2gyfOHjalncQcfeQlFMlK_Bc_5l_OBwzSjEhI453Z2zrteBBsWEMDeTkUERx3f9KWfwr0CfMNeZBIUqjLj0xkOp81eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TpOL6JqDNVVf_kYG3r6tDc0HKIsoiBLZ5b8e4tmp2AJ9OU7wxwK1lWiwaTOzJT-JgY5hKyBDGQxXN0WaiXpxPM6Y4ys2wW1E5HHbNmpKW7e1_6nMD6_jXmYw2XSofsAaEb3YgF5Seg64sXtsfQJZd0JyOwHIJqeCBrEyDA3HAJnKpGzDly-5rxiyWap6pmJ7H9PrD_3PYtC8xoiuDns3bntYe6mK4Tcrgc8ofmNZS9DIsk5_WNmp0CH29Ghqu2VWGxZiAuI9I39-9Yb4Tx1bGNEmHO_yUPqr_L4HwtIhAwsIv6eEb3onHdVBwR_9Lkg_iy5BXzGSxmghOShIYl7rPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mp_pXbaKj_nwAXp5-4l1RV8CnczoVA_2cogP41H9VNsFcywdvoTdd_FUfOpu8ZmzgIrIrAhnVHXRpcbrqlko_HNCln8vNiiVt3gkckIfZBLhxTamKUnSYUjfjKPvHZE8A6eCO3L7n1ZYb6BYn7-RESgZsQ8FFf3P-pGXvnGkxTaBOobrwlhXA1ZzTxmFcYJKkYwAuIqHJksqWI9rDIA6bK9UCvGYRuJIu5_sQUbAN9e4fof2gqwJSAD6yXMZu2kpZfTximBGrlJvFqPqRi6Oc1YKGUryUn3MJFVZp5scAudlhbmwkyWS551EyxOUkf7qaal8r-kn-U32XZzXKzMk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imZ4Gzu_Cwa6vqCRMbX5rhkyBz6_1lcJ0urbpWAd6wnsq8HYY7qT5DMEClA18TuW189ZnOLZv9PDiBBiEIi59dDWLyhyqcu8pnuEaiVfstpfNeHdwIjOd_B39hM3BpaGrj1ftc-z40x8Pm5G3xwc4oGjrhYX0Lx3b_tgq3RDonEgEXZceMdD0d5atJ3WjrjJ7rNVgOXRh2UUh2RlKw-7Xmo_gai5BYtewcHo-7z6xpAzg6EzGi9-RNJ8JV3t8KiHgcdPlENwtIw6RNl2EZdz2ZrmRP7l_UtrBTKS8vrvYU1jjg1cmcbngMes2iHgWq-BrmFFvHSnsB0vlxsN65D1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cSwWR4jq7xBLCO_wZO8i9GUTPfLwcfOF4i5qvwzrHYRbfYrposiDhOrBcI37fS41sWB8C_CH8ELDTeXig4E91UYis_yJN4MylGxv-MsbhGzkWTPyqZx3kZCBNeCkMbIdQW6ECLAjqjUIkomyiWeUK0Sp3vi6hJpbTaHrKsLMdtA3I0SsCfRBZIbA4Ao4UZasKPbAGDs8UIY9oTS67GzVwRwjpzQEHleXbsFcXPBnWTZBUyKfLpujOYgjO_pBN8Et_iE2_-B_OpvkfintJucm8kSHaT6ldkgB6JthCvt83VldfgnaCxdc_1oYYwTdPV4qJVqVoxUHfV5R9_0V-UisJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=rnh2904LuiexsLblgi2vQziEW80CDFvL6TPfnqj200_uS6poorXp5R64xfUy_YkFuRIrshDgfmolkKBtaXJ8rYzuoiHrWeXZ7G_zygsN6i47svhE78SPNz1zxQc3WdaKn6Rmxhoi_5SeKShoBkVUz73jSxX-33bJ-EgmsEnC2aAf9dN2B5JiLynVCpifXKhTaK0q3DnxKNWMKSe4wOjxuLxLHyALlUT15_MseWgwVOL1BGD-NO8O-y2GK9axV4Qq8U6mprWX-2-V7AcJEpO6AbqNoIQxPqz_MHm75cThDLj2du1nlpX5kp-KIIc81XHrvtWfoAbtluXi-cXb6mGMXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=rnh2904LuiexsLblgi2vQziEW80CDFvL6TPfnqj200_uS6poorXp5R64xfUy_YkFuRIrshDgfmolkKBtaXJ8rYzuoiHrWeXZ7G_zygsN6i47svhE78SPNz1zxQc3WdaKn6Rmxhoi_5SeKShoBkVUz73jSxX-33bJ-EgmsEnC2aAf9dN2B5JiLynVCpifXKhTaK0q3DnxKNWMKSe4wOjxuLxLHyALlUT15_MseWgwVOL1BGD-NO8O-y2GK9axV4Qq8U6mprWX-2-V7AcJEpO6AbqNoIQxPqz_MHm75cThDLj2du1nlpX5kp-KIIc81XHrvtWfoAbtluXi-cXb6mGMXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tr_1lQOARWgSJgdO4AG1Iz54l1oT-2j2gDzC7nVSpHaGF9ISWA6vxDNiBFAE0-dkyzlPcmKSquUllnit7rsKwzG69-8b4Hp99KdWxAhMKjve1UcJq1jtQYk1dXZJhtH8SWt20ju7hbsVwc6NTZBkV0i0dh1tMaPcgKCpmpDSlzQ3QZeVzWQ40e6I9ReXxYzOgEJtCzU3bjnLToFRz4j19yUHq6J97Q9fT2b2dQGr6EmbgxpZiTQspfWYyilB_pKOjiLN44nWdur6QabhAmui2S4_jW3F67XhfPZiXGm20QT9yPx7Ec6OuujmWX8wYIoHatSTQgUKWeA6OVHpFA0iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdb0dxu-vFur7lacHUqYzojdMxWXbcFj1JYIzIn-ZIcN-eTUSTy8DuLqi24yyR-r9OjDOiHlQKg72I6JTagFRZ0KOlKbv3aU-j0RXkAit1WU4r0ZWhOyPf-GmEepSqF6mRoGrmS5KlIvgfXt8mA-_TdyqoCAROrUpClr4FxL4iRJwje5L1pBedqkdCjE0tb1Mky5Ax9bCLswWbNa5msBv-E-naUQ5jILleKH4DzFLHEWcAmBpt7QPBrzJRIJRyGLPC8ptWbV4Hjr1SwF3PIOmD2UZZkioEHvJ2uUuczMGVAkH-J1zziCBLLxrN2bkBj_poXT4Q1nsCZBAMLdwLtxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه، چهارشنبه هشتم مهر گزارش داد صرافی‌های رمزارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کرده‌اند.
بر اساس این گزارش، این محدودیت از امروز ساعت ۲۱ تا یکشنبه ۱۲ مهرماه اعمال می‌شود و سقف خرید روزانه برای هر کاربر دو هزار تتر تعیین شده است.
این اقدام در پی افزایش پرشتاب قیمت ارزهای خارجی و سقوط ارزش ریال انجام شده است.
عصر چهارشنبه قیمت دلار در بازار آزاد ایران از ۲۵۵ هزار تومان عبور کرد و هر تتر نیز حدود ۲۵۵ هزار تومان معامله شد.
پیش از این بانک مرکزی جمهوری اسلامی نیز اعلام کرده بود اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXflBFApQwadq4gJLTeZjoHGDCJpr_0K1OORmcCEuhfEzTHbvSfGMNs9oTGofk_0EZtLKmutazFtPJstSmJNrtTXFMF3muRi1Kz1vmyG6iDQfcTCbyp0_DGGtNbzTr5mrl-dKhNbebFzbUdGPDxpgzbc-0GWrw5Z_Xzx3sm8vzPAVgHuSl9Kk4vwXqSma3k7H-55j6fGNK3miPzdPXbP0GzdVKgu1sngcp-3Z6wS-3hMNCta3LJehSVRqKwJo6Lek2Q-AQjmLdyMwB-OBfliU9FbGy_gYNtVznH8fOu7AmX3_-5giKCavfWAEVPeQsS1KExIEqKX8SPZZLGWJXIAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fFMRfTbABjmlXXi7buPzv_JQoBrR2CE3taX3CMUHlt1LzseqZC7MHaGKNT1DHUJkTXEtuzDBh5j-BP8axBbrg7MC3wq6rF9lY8ZUEshPNlayd9blQ6rkX6Zc6MYRseQWIfdCwOu5uS-FLg9E9LenPpWTKvS4ibmsCdWJHWezwmk1fvzVwds2PRn5crnl6E_iYKZ6xl5rRW1jV2XY3XEL9AlfxKgNkau3SgKrfdlYnQrLuk9rkhkjcECx_gX4wlTBRD3F15mF6nQP31KuoCzg6ASBmLvC5P4jsIg0yfANJ-o087bPn3T7CcX3mNLUATA1vpssMpM4B89KqQqrpRXsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=JQSXn-3yc9oeD5Iaf_B2Mvvxg1ts1oWJcsa2bm40mH7iJm4VTUfK4_33EYjeMLLamSfEDmy2SOO3rZHw-b3Af9i_UapKNvQjnfXM7ZFvJdEwSChMH-VYRRvckneW5jwobyc8ySaCcev9mtxJjC_HaVCb4QGxjM2CASjFT8kUV9q12AKycWxakAUKnPn5oMOdSTgb5yXlDjC5ScvSIMtH_fwS2dnn66h_a5qLvBK3r6LpsQiDerbb2_ENlL-vsPsmT_5NQ04mkgmkrP9o0nGN8WBiIwV8_YXNEyb8L7vm1-1nEH-Qgy4zJxJ7L10H1_MI7oVhRz4_1PTWbkRw_1vomw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=JQSXn-3yc9oeD5Iaf_B2Mvvxg1ts1oWJcsa2bm40mH7iJm4VTUfK4_33EYjeMLLamSfEDmy2SOO3rZHw-b3Af9i_UapKNvQjnfXM7ZFvJdEwSChMH-VYRRvckneW5jwobyc8ySaCcev9mtxJjC_HaVCb4QGxjM2CASjFT8kUV9q12AKycWxakAUKnPn5oMOdSTgb5yXlDjC5ScvSIMtH_fwS2dnn66h_a5qLvBK3r6LpsQiDerbb2_ENlL-vsPsmT_5NQ04mkgmkrP9o0nGN8WBiIwV8_YXNEyb8L7vm1-1nEH-Qgy4zJxJ7L10H1_MI7oVhRz4_1PTWbkRw_1vomw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UW0ebZjLI0JVDmWnbcWAnuN0atPSVtchRrJHFSo3_GYCrcvmU9qsnXsCRVqzHREnMbKgZvG7wSzDkT48Rg9prNP5ll_W2EtKvqzBRmXU7d_ahEiURX7AI3Hk1MYU5g34e-xzxY2DSiK2gCioOa0AVy4xrvSb23eoByJlS-wrFuNM2T4llUa6ji-H5gox5bRMZQXl8HIH4SVPeLeiaNkxpuRnNXGfFrQX4_FQCYbtUbipEkGZDOYlCKmyJxKKaXEkaRMQ72vZMieFaf9lhWeeMvY742wfYe84PapZ0C18I430V2ueatXM5ZIuk8q--UiS3S0R9oDaZ3AKTSBEz1TxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/op2BdSurfwnUUQHGWnO82-Stq0Kh1a2NKuN4e2dLYh8Qy1uC0haxukCNzUI2lBweoKy0GxOhSTdDRt5yd7Mz7-t4DU0jTqQLauf7ozR6FgvE2_EzsDWnYy3xqCBZfPyJIfgop9RueXGrzFHjlVYi16XjfrVAqPMkQKiPht2z5oru3-6KBlNjw1XHO5R4aIW1uPNxxyE6W4ACuF_CGWU0txHUIdZZx7AZDblmFAtHE_bPWzZa-9Ae72jADduinkRWczj64oyxZPxcBUk3XMkuXt3EFMB2VDBf_pvffop64b8pvOuaoAV3hVuukg1zlrckMxNabWbAr0vAT5rlS9KwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjQKpRHeU70e-CV0HQJXSBxkwLu_UcKTN763TfeZGkiGpFK4R3TCm2NoHfxRCnLylZtuMCMJP11f8hX4Ujco94UKEWB-S_OZ7K4fH0rZVRpnT_sAwlC6wdjcoE-1vgysGndHNBzbLWO5yFG4JqjiZz2PP1gxBmAk31bHS2TaBYaH1fPHglxP-CdWdhoSYxKtJnMfBnLuVrGaxXsmDoeFmigpuJ4YqdVdnszyE75PVW7Lsq14oNia_kRCv1uNWwKZcIdKnBTIHHt9nGwa4_oPijsmFBH0MdLhF5zsSIKE8Bs0Ue4RzcMMw848Mm2Xdmey2BXFpOhgZyiAbGR8oUxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q18ODfcDC9aup1cBfM18-xYgIQBX1heutnim39ObTMUlt4b0u2-htAYvLwq8SkjglL2aYnLawHztvnIOE3i-5hxtzrNtnbVf-rsktr5mjKgAzdVvRigW-jXEAshQlb0hsJL2GJnXlT9dkVFpDAG35Tc34m328BJ1suVgyGSQ_EX0arezSNDVnAT6Vf04PL8HzCS4Jk44wr83gKFYCeNl6eVVpw-WeMHQNN0Btha_4kncwujtTSQwQH9kOiwSgj4AisaDgt6R6l0bBkEYStMkzhD5TiCUffEsCyd525J3RF9Pwc1iDfhtcw5YTlIfzejbLYiHZf9llKMh9qFoFSAvcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgOKjjEC4_YqWdNahOYyPwkA4PHBLLGGTpIZ_KniNIbEzgPlmAAE1DaGR6PFGmMiVgBI4r2X-h8yWc9RQLGYDXRinv6l5LjbIqVux7YkNx4rT4TFjFMjeRTzifzbquwFvrATJRN9jhRKU7UcxQV89U2AjATEcwQx4YnOh1cZMHYxu-7BT-TMQZRkV2AiXVNaBIEW9yt2aogSrl7krGRiIQP02zLj5CwFVGQ9m6ZRD6vYpkNxHfwuntL1jAMK2WAcNg98PgNAYQjtjo3FZeS7e6XNumGuCf3IWIAYgq3iHMvHDZZozAjL6r4RDgKC46GNz_VMGKvRAdXrmu0XbaVuUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pfILlJXgjZiPl3N31iJQuhn-01nVvx3Ir0-ugsJL0YZLzAscNbCn6xwKfyxfSYBcoxEI6ntumiMU5deBzPcgFC4JJicerCbQth7qkJp8iLExge8Fh6CMyD60Zs5MJ2i6tX1uTfHCf02vcHN2WP8Luj0stZzCV5TKwws1x8Xx7mKLCghv0m5hdVfhElA-c7jkTG0croFZUZH6xlxqDo1ieCq7a2L6tia3BLhA6Av2hTwuFcUU5cF5xvbNMGvGf8443oGVhmYt9xfNkZcf4k50JN4WJ2uCzo0xCblznEY87YF2-EvpJq0FxCQAWgUt_ArBmzPIC8QFSkOvOAARlXOm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kWHHu2-7IqFvd0aQUX_BQKsIzIQJbVgR765OOhigN2_cl3AwDFX7QpdMk98weH8b7lOog0gsP8gYOeZOg4VHnFbCHBgYrf9ZA2kmdDYvdq_nPgwCTHin4KEWX8KLFL8-njsdSMU29jO5prVnXQXMp7Jmm81LCCckW5jjX-4JvMJZ9r1QhUZu5UJmuk0Ujlcz6Pn3BSGV0Hn27Ivt-GaE46eW996444t6_2mJDIA6Ys7mf19UQ8DvLx1Tpv6vBl3q1TAi4OHP2ZZJMLoYs8lc1w4triQJCdYR2rq2ASI33KlKaFUCVpsclYVNLqDE_Q3zyt_NQsgHNqSXOCsNMcJAXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=JQQQTO460vEVDM6JGGm5z14D59UnMGe5V7386wRU0_eEJwMBWm0PxnsPlTJftGT9_bU411oGt8JP46nfnd145n1XO23rawbT8xPP_09jzTBUhGZHY3XuwdQUTqHxM69rOjku9El3Y9bqYRwpn_DuGOuGjio6pOLS6OcZdog8xvYub5V8ScOYuoy9ELMCoDoWLV_PjgKCM4_z5ppI6gHUm2zwdl4wEkLkZzflQI-iXtcVUMXgwl0kWBUXPag2I98ImTbxWMu-Tvm_lIS1qBsh5NWWCu0p5AZ8vMQOZyYPhdnJDuyMxYtIKn7niWqzCO5a66dXRsz8ThvJ9YzZacJlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=JQQQTO460vEVDM6JGGm5z14D59UnMGe5V7386wRU0_eEJwMBWm0PxnsPlTJftGT9_bU411oGt8JP46nfnd145n1XO23rawbT8xPP_09jzTBUhGZHY3XuwdQUTqHxM69rOjku9El3Y9bqYRwpn_DuGOuGjio6pOLS6OcZdog8xvYub5V8ScOYuoy9ELMCoDoWLV_PjgKCM4_z5ppI6gHUm2zwdl4wEkLkZzflQI-iXtcVUMXgwl0kWBUXPag2I98ImTbxWMu-Tvm_lIS1qBsh5NWWCu0p5AZ8vMQOZyYPhdnJDuyMxYtIKn7niWqzCO5a66dXRsz8ThvJ9YzZacJlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHVag5GHXL6xPDWx1bxotZ587FOe9wAjTPCukV7tV1ZjM0zyt3A__ERRP-MqHK0g3pebXv6YSuzvWdbuDeGKlkxVjzN1aq50c5d-stE9Pz1kBhLwLUQbLvneGMPSw6vn21B7N1rSmDgObSTneb9D2XZcs29vMTuxvhv9r2gHvzk6tSV0UcKjpRMI8fFygtGZL1zm1AUVGw6E_f6-VZA1b8sLFiUC0rDsEg4SiFLCHZcZhGuOlVQHC4fdEjt9lcBmLl9EQFLmakPrSFfDlwpJaYEmJLnYmmwb6O-XwCmvpD1Q57MaBr1RzASF4ja5UQb83nZvu2hd8Sx2vux-MDNlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W0B58qyLHzFf0GS5CVR5k6jgVRhIZxnC3Zzme8DX8aMHmIgGl4u2B1ooD7bjEbGEdoLv5cEuIimNSuk5ov8wvyXuLQpF--3PykwSnmOGDeUp5JyWWw32EOXB_f-RtZZwRlIUsl8lADAIUC9sX2fotvtm2D8PRuTzVEu0st5erOU59fk3OppytWzZKWO-D9vfwfwrJiZzhF1T0ezmUrPEpF0meiSzcbee2g3YY-fxsbVnezcrUctHLyzvuvKhUtqhrdnDoUR6OCe_yriDIN-FB3_ZlF_eZauwvfJAhn68k1vTI6pzanQ5t4qNcJXq42w3IjRELr_zA6n5NYF3hqSvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COrB5VrQO0yEOPjqeMoQzH1cwiI-p-jH84hGMq5gs-flcdkdltSGPwE9gkVbxZ7P0-RsLAJyrsfpA_4Hs1c3iqHVIiXYOhpysJ6OhTn6q5q_NtNchIqyiSy9kzUai_cAty_isYp_wjeVeVX6jzwGO8JiYdhxiatD5vIjxughHr1TBscgCPDdsWPEiReikDK20Jm8r40YV9xmg-Rirlczwn6B5apRxDhsFoh4bCpCbTZs4Fqo-QjV-Lv8ZOT6KSOaVXP1OofaRJHS3bA6YJ1LEYiGIxDCN5YuGY9p0pG6GXAxqQXPOrxMLKwI41JGLjtJNhz-dloOH2tOWFg6SOVnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nimk6hIOsguxoo_Fb8b6qtiP87yxmq8Nk6uHIZt9UyBkNZl3KHL6uwlh1aT_rNegQbHmAKcC_6I_PFoyeWB-ag7giyG3BGqie_k8gLC3LCsbFrE0kBasNdIQBE41aZB60B8zIAKu9_WKihsbP3Z-k64SZFh1s6p5lNoR_O_ttyyPrhq3wMFgGnnR13va4yM_l5yB3I32Y4htwqrhAoqajcNof68JwRG6n_2M07D4L8jAVqdPkO0DSbyTAsnDbDXVUSwGmpu3t5HUGatro_Mp9iz-4wMG2L5AhYQo5MxcyVBhLbk3kTLAz_Z3BnKC6soq4OKtzdM-scSDLOMYZsXGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pT1hwGRwUjjww3kUWi2c0w6wM-8_f_fb4dqHnN8ujhMZhG4ZwTEKi5Bt6SvT-glupwm_kdgleT75OZ_b-BMLHcqHByoU89Ov8YAkMuMSAyqdKWhhJ2hGaurR5nMMWzNvsuW4xFBtfA0AfaNR_Z0bY1G8kPSVhB9JoYb_GEOX-f0UWeG4WMFJdc4bqP4QssUsCwQuLwT-vg72o4iMEeB8rbg7_dA5bs_sLUYwwq6Id1HyiXZ21Eyyw0uWB2JeJOeY1E3Q2PmJtMbCXQu98qQog0CgPKb-54HbhSDZYHifrscIwMPKsJa-lsbz5bsdFefuAD4skWgPzPUcAR7KJdequQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ac_iTu-pJDXWIEPayWWIJ_k8hWKpAJqjp1o2G7ZMKLNy6AO-w971DjsSZRU2EvgL9d0lAzBF5tqVgY8EM2QpznQ90_PhrDxMnPxhL698iUUT8ywbtG2YQlyAU7faKKlAB12neyFUY1SpCvfXsShA8jMlzBTtr1WorwOAnkFsJqlJ9ah9ee4vg-fhvyiU4fVbpKWBYl0Be7WSGHPKk_hjbJywQJnAgGgs2GIjHKqqBOF2gyrF90C3IQ5Rv48lNR-43MdQWmH711Ymg-ciFwGatgv1WNmk0ueZWOUDs-SkceXkvJCmipjj7dXSHS9fGwWR0Qx4Dr2kBNq3PEKW4sZ4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GTms1AaFjuj8-XIzV8hD1tqYfnmmcKTHebHsLkZDixYSq6Ap0cztt1FFVaHv_JY7I9gsvPtBS_ck7T6yhXqSSJCXJ1JPH97nF_eb40ip7snOmR713oRqVIJwqf6BOZ7MzaYfMj9SbCF1rAZAI-LTHkZyRpKzUsY1A5sfq3TqsrKlRePUajpUDEmPn3wWf7YCjneRlOvf7nkGZsoqMUGt8He83eLhqjQzuTZ5rJXP1hWMAZEK0cpbtlE2SvvV59o0wS4t4tu-XB0mh2w8-ODmSIWleL3GgHREpBbMANJNmrqM97FSZqH6CJJEyDwFbCP-8YxqV4duH_WFFQmESMuldg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=tUZWZvU2Dmw_AqxAxos4U_t5iD2OU9bAZYULjkjUvua3ZnjzTzhw0CDd2fUSv0rrOb7UT0WfdiXFTInYhfmYdJaQsu60kLSrqq4HumCmcnkT5wGORUT8e6RfPe4Puz1G904AXi4ad2n2L1k7Y0CWVErjuIrM3jEs5QIjdRKFdD3CS1zqCuGpmlMI9S6T3uqGoACNqt7u9jKd-Y-ofgBX8MDRtoCa7T3h1rBr_ZiEf_dbFgIWxbEAxtKtyQ4-9NnX_EO6VeO96NFqUJEaxasZ5e58ZjJvy0CX8OANwWmylwFnRcvEDxIfGrJxAUtXots3Id1yV9CT7JjQ1wBCf2M9-Vu-zvgCEokN7oKSCyRXNfSFrgMailoiu7127fx19vSzARtcycTimMb3tYOhdq6nLGqfMJ8PCrPuiZx6DdrZFhuC_13uWNRR5Zmu6mnzW8-oyyw6xAcRENKeecVGOUOgFs5pQ1jq5NOYLStXuHMqNc7TU8E7dbX20xNbuj24eJ8GU7r9fg6t3cfeySC7JmhMvqPndnC661Av8QRnePqQWrb0KOYLP86KeCUUsA_Je-EdgFLkAMMI4FrCB4qGeWexrBSfcMTJhXC7m6geDWi31wS-gjbYc7kXPtOPXH-tFVr6yuLUb19Fp7tfy8r3CsyjNXpubNW18BgXgkDMzDARMVU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=tUZWZvU2Dmw_AqxAxos4U_t5iD2OU9bAZYULjkjUvua3ZnjzTzhw0CDd2fUSv0rrOb7UT0WfdiXFTInYhfmYdJaQsu60kLSrqq4HumCmcnkT5wGORUT8e6RfPe4Puz1G904AXi4ad2n2L1k7Y0CWVErjuIrM3jEs5QIjdRKFdD3CS1zqCuGpmlMI9S6T3uqGoACNqt7u9jKd-Y-ofgBX8MDRtoCa7T3h1rBr_ZiEf_dbFgIWxbEAxtKtyQ4-9NnX_EO6VeO96NFqUJEaxasZ5e58ZjJvy0CX8OANwWmylwFnRcvEDxIfGrJxAUtXots3Id1yV9CT7JjQ1wBCf2M9-Vu-zvgCEokN7oKSCyRXNfSFrgMailoiu7127fx19vSzARtcycTimMb3tYOhdq6nLGqfMJ8PCrPuiZx6DdrZFhuC_13uWNRR5Zmu6mnzW8-oyyw6xAcRENKeecVGOUOgFs5pQ1jq5NOYLStXuHMqNc7TU8E7dbX20xNbuj24eJ8GU7r9fg6t3cfeySC7JmhMvqPndnC661Av8QRnePqQWrb0KOYLP86KeCUUsA_Je-EdgFLkAMMI4FrCB4qGeWexrBSfcMTJhXC7m6geDWi31wS-gjbYc7kXPtOPXH-tFVr6yuLUb19Fp7tfy8r3CsyjNXpubNW18BgXgkDMzDARMVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSS5LboxZ3w1IWluNsaOaxMzM01-w2ZIN9xkueJwmppaS8M4R1UDwuorgr-KdaDf3iOXpqAhYG3yvRkwXf7zwjyFZkoRBqXiW7cZtxvBugLvZ52dKUEfWBNRBwCBwawkmKW3jmG6bRnrP8Jgy33OFdP7uAXg9Cxk24zwhzdI8Oh0Nt_hpxoRBGdIlFBBrEZ6Y6dA-0OuLx0PK1Ueim5XxwgWv2SegbeSfB-keH98RmimyIJaWu4WduQbXoDO_UjLAfpG6JG1eQwjOUBXo1Q_qVskknSQyvabZuLQN1Md9mjyLhOaehdwgrhrrHa3XkxtVWaq54FCIsTj-Gys8JrlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U2dxrK4GXBEhU9b-JHl2M3lwdVMWpGH7l9qrSclY9MShkKCB9lAG7ttuCsH9dDcC-4Y54ET49YV-yM8Fsf7KUXNe59Xg5YDHOmbPRtQYu5NpsDToODbyFs_EITXfAxb4iRsn4cyFqx0_-bXg0CpoR2k36SoGbpdQ6YMG9PkW00n886puZNLfsfyR7qpqU4q_CNp9aGr8ZyDpgO0bzQh7xDcI_ykFGo9ipo_zrx7_L37brGWGy9Uur8Xc-a0WSLlmUoeYR95hBX4NDxaJBkUrT3AVUjBEAaQTXd1CxTANnERtI3s76Kn5EC1pmTo8Gq6SKovaC9W_f0vJpDMIcwt19w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/srvlxv5AUW70pV5Dno4ryFlhBrlp3ObNz-6WNWvOqXIdZFkNSPqt2lgzMv7IamBen_vTdQ_OG8g8soe1itIakz3T_tON0dY2pzI-lABoiYdlTwWFemCrEMoKddEWbcrZCeX6xil8CbYpIQT1AKTRlYI5Qs6RGTh0Ke1JdYrVVcwSIvXP-Q2IhjaMRSI2YOnVJbt2TIkVSKl2CchMI5suJcvFt0-Ytt7p-q3iJPVgWiglxVw05mFWtBByB1hOGDmNO9BGyEwqH8Zl01ddaMuUQGK4F7Mvkul9NtasRpqRwerte_20GuP42pP2U-HX9lSFQ9W1GYCaNRibasM-1cLt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=P8_saluDLl0qFPazg8-6nR8p5Kvjt0lwXd_iU0uYmgUL4HB23oqmakfTrZFvYyKPxPqELyv3M-lNWT0Mh5SnkB290HSqLviOfEm2RFbeOACLjJpPnQoX9CEZSXocucV2ItQXttGXgxOPXwQrRPq_82sZV0QDHmZ2WdrClMvK0Ws8EVcI49j1JfAfb2UQtCJX0W44ixqYztDcm17Pd_hK-cpN0ZJB2daavcnoUVur9QUORuLrSTcRseV_9oqzMyinPzKIxXVmD49UcFWsnY4yPycdxcGSmUn-5WqYizBKPBoxrS2r7MVRoK78px6bB2mrzDYQGrsIUwMHu-nrC9l6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=P8_saluDLl0qFPazg8-6nR8p5Kvjt0lwXd_iU0uYmgUL4HB23oqmakfTrZFvYyKPxPqELyv3M-lNWT0Mh5SnkB290HSqLviOfEm2RFbeOACLjJpPnQoX9CEZSXocucV2ItQXttGXgxOPXwQrRPq_82sZV0QDHmZ2WdrClMvK0Ws8EVcI49j1JfAfb2UQtCJX0W44ixqYztDcm17Pd_hK-cpN0ZJB2daavcnoUVur9QUORuLrSTcRseV_9oqzMyinPzKIxXVmD49UcFWsnY4yPycdxcGSmUn-5WqYizBKPBoxrS2r7MVRoK78px6bB2mrzDYQGrsIUwMHu-nrC9l6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=TMATCJnqYehot6E9VnGE21Ov8VsDOJv4r2SKLuQWAcyhQpBx-N9rrXU3fqtsKxkkf2Oy-IMb8i3MGBeP2OHNX21WnQAWh1n1AHwwHYtwgI4UgIpgGOVwfi4YkeUDYRVAVrVbSpHcrym6bJQGwpPsBI3WDvkgBP2x1oI0igHAR1hR9dDJtS2T95tZqxNJzG6VMAKVe5r-dCSxPZb-b21VMRT9UkmKuhAS-fDv92mz7ziyw_NviFNjCuqLGlnQRLJVEEm52-wLTSW8SExk84KrC465gsGRATszPw3EOcC2mfLY7r5jSsU1rN_GVZ9BjkrB1YYIJ9ViwbHJKh_hCI355A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=TMATCJnqYehot6E9VnGE21Ov8VsDOJv4r2SKLuQWAcyhQpBx-N9rrXU3fqtsKxkkf2Oy-IMb8i3MGBeP2OHNX21WnQAWh1n1AHwwHYtwgI4UgIpgGOVwfi4YkeUDYRVAVrVbSpHcrym6bJQGwpPsBI3WDvkgBP2x1oI0igHAR1hR9dDJtS2T95tZqxNJzG6VMAKVe5r-dCSxPZb-b21VMRT9UkmKuhAS-fDv92mz7ziyw_NviFNjCuqLGlnQRLJVEEm52-wLTSW8SExk84KrC465gsGRATszPw3EOcC2mfLY7r5jSsU1rN_GVZ9BjkrB1YYIJ9ViwbHJKh_hCI355A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6zmLfIM4sNHSlivfk0x0Pw3g-7MSSe7czxGb4W-h32FpUjDNKmULjKbRlahFDkOKsuFH2sCVl0SMbIzHzMTPk160A_3_P9Y8jxMC-dnf1p5yPk-1DSWRc0KqwhgQEQouwX0Y9TOwPnnWlADHT6uQa-6a-nAxO6vWJlRRzomrXm7lF6pbjqLEIWnqg7cQq0Tl84RTBASSVuZFWMjN1LEKO9uSqE_UyTIFjWHz0yWHQW1NWraCsBQNahWi1_ZpKb1WAFH_ysdK2Bvjp7mjf7MCbTL_2U0t7X6BLkbU6S5mH8W6v5nlubtsWCcbk2M4b8WWtQSdZxnvSWEBIGIW1bI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dSbvD1SmXJCS8vJnjjnpoqIQBqeIbPC3bG8iMYnGvsQ4s3hdf1FVQ6HmeuVE_nYtuhvcMINK9Lgx940LuqvoZKH8Uvbb9qfHKPsV3v3ubIm2S_nIysu6Uq-seV7v_lpsLO3E_YDWYkz-bvRYIcwJvekjJWSUZsiJJUok6te4fE5HSGRfgnh49yzWOmTEudX5qfS6BRqpHtJKnbSrhGKKYHKFBHf9rYzt-Cu4HVAMRgXCHQPd9oT17Twa-AgGrlWhhpoGh4ImA9jML2CivhdVs2hCK4bqL9SZXP7ePAXpU9rlTak8nmSKNZbxYT0y5UajZuYfybLKFGtQ9D9SDDekxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHpCj0OxeImyeQTWDYuYC-sfdrvKy0kUeKJR8UM1_JD1VzlSc1j8fnswD6QS_LMVclI9YkofOMxp_BIcYMk9Y3WpnaBxCUPMUN7SlGoSWkv5dceum7W57nMfJ71ITa0LJOcLCo8cny3DFdL17v-_xOpdjewljtg5ydn049l0M0u75M-Q3RxdG-CIGgQn14OQw1jyZl3KodLRKWsfLVr7uv5V0cd0CCgKyPc4siqU2cj3SEWaQXt6934KD0GB2o2dgXOV9VuIggnyvF_iWp6eNV_5PIHgDZL582u6HddLyR0Buaiuol0qnFZadVVKb1Ez8TvX8mzEi1EPnQ1Z6tICCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=XFP24r9bJdeaEnQaT8ixAE8zGf4mFiRmHvjfK1dL1FWqyxKVZJ30ADgTBRtnVwYkLvv_F0mNhW6UM1HWu-W8HQF_09lV6uBEoXaUOAW_TCZ1K2JevNllzOnK2x0-BbU2xQ42Kq1S7mx4V1MfMl14okOCGAD1TGCNSSz2R2AO27ZJT5ZUKvE_Cf2NPBkK2K10F8LFVeDNHhTNRFpOEc3aqBBvbWRp-vhiay50X5s6eEEFqiG7VuDKW4BtDSbK_eNN9ruJwnYo8aNYTiB-JrvsShg2G2clar5JueuT9H0b0QJX1yumy9QO2Oeh0wuhR9YoFJuEI2H4qyl90L_kogXhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=XFP24r9bJdeaEnQaT8ixAE8zGf4mFiRmHvjfK1dL1FWqyxKVZJ30ADgTBRtnVwYkLvv_F0mNhW6UM1HWu-W8HQF_09lV6uBEoXaUOAW_TCZ1K2JevNllzOnK2x0-BbU2xQ42Kq1S7mx4V1MfMl14okOCGAD1TGCNSSz2R2AO27ZJT5ZUKvE_Cf2NPBkK2K10F8LFVeDNHhTNRFpOEc3aqBBvbWRp-vhiay50X5s6eEEFqiG7VuDKW4BtDSbK_eNN9ruJwnYo8aNYTiB-JrvsShg2G2clar5JueuT9H0b0QJX1yumy9QO2Oeh0wuhR9YoFJuEI2H4qyl90L_kogXhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4qgua4E8JsvhX5A_qnpcUlwKPknIqQM36Qu6iA7Axf2z-Izz4rLuuOoJuzEu_tmHEiBSPpF3dl2A7nq8m9a2StK2B4-le1r4JyymAEQR7aIpshI6-K4vVcKhTTwecbWT3AiaQtc2WJ4C0X7pBdlNzEyGk7I4FXQQbT3Q1GRzwOgzCK6PSH44UFcYzyRwFIIaFY4JOH61aVu9y9N3eP6i_rpHNK6BxKJ486znO0PVkEv0kB9_ThmHv6ZYZMXKbL9EuTcsGOavICaaZ5jnsm8763H88dJqRUnI3Wf495MxA7GdKCZq9v1agKC7AdZZidBevyQ6gbxAR9kTuxjCr-ObA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FJ9hQmee3EPcK7dXo6sqAkCnzaqhYa2KwoEweGgPgr41lb5a9p6qgbYHlCZAlaA-O0QVIPN66eL-3dXuPnMlfofVmf0iAt5fMIsxLAnM6kOHhc7wQ7cFiDDYKXnY6WQxkv8cC234tn6sx1qykCx6fV3iUP3vhTY1LkQP5I6e0FkOJjXUI7HCTN7PiPWu470LtExxk8PkGwKTgjKebl4ICytpZplT5vnpEAFi-KPbgGHGRpSvIkslhc97rld5K5CSBrx5yoBUPk-JgwcE-MC5P1Ixamjw_l_1Phe_P2OMQeQgSfvSPo8GvATyfKkvUOTs3MRGPeLBD8sY_8w6-DA2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U78bJ1xpqHRusEu3jv02qG5BDdJHb9xjz_8PYT1FeTd3FCFDFGCzsahXoQVUjrzf6hbxDF0FK5f5h1TUFLkB9OnWhvT1zxSTFIfaedx_mVrbkt4D7ed4kGp1IgOtdIo3SuEdbUpgzgg6AJp22gXs_GRoVH2CYs280ZDWOfHsKyOILyFnwsy2ful-Eov753OXFBSb-L6i1WxBPciTUbuUroU1E4fx7wv1viZSaAsuPc_gwT3e4QldluZdlkL9CW2a6NBTgACzTR1vQSVeLPLQNVvRWDh4Llo1fTVYzRvyVStGK7rXjTYGDr_Fu7tsAiveD852-irPy4fvWGQDUIBT2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=rtZy-lH6GeY2_4QVTCMnofHVRfRnoS7BMJa5K_eUD8RmMYCZ3iALmGKDDZu-L7Ouxqvpp6jI7pgjPhePmY0v1Sy-5D_dgFZkQeB7sKlv_zftmL3eZpkwewA2KCnTIrNZQ-mSRShu-EqkJeufqfZB32CocfDDRLwBqKF_3S6QOKhC5d-wcO28UjNn8hqWg_E6euCtx-BVxFn44FM_JXa2nHphnDDSwE0WtLI6rNyDKWgOrnaYg_ymwjK8X3b31G326fRMUw2m9vabgyLnaWhXA6wlSkAhABGWAai7EXp2jBR-fHw3ujcXP6mDtUzRMeuDGgOXrNVZoxhLfqR8UGzBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=rtZy-lH6GeY2_4QVTCMnofHVRfRnoS7BMJa5K_eUD8RmMYCZ3iALmGKDDZu-L7Ouxqvpp6jI7pgjPhePmY0v1Sy-5D_dgFZkQeB7sKlv_zftmL3eZpkwewA2KCnTIrNZQ-mSRShu-EqkJeufqfZB32CocfDDRLwBqKF_3S6QOKhC5d-wcO28UjNn8hqWg_E6euCtx-BVxFn44FM_JXa2nHphnDDSwE0WtLI6rNyDKWgOrnaYg_ymwjK8X3b31G326fRMUw2m9vabgyLnaWhXA6wlSkAhABGWAai7EXp2jBR-fHw3ujcXP6mDtUzRMeuDGgOXrNVZoxhLfqR8UGzBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OF7nH3l5qsTrb_qMiLs7lD2c_rVk7bnb_LdJTqpwlMUaKCt3-A8ak7rIRNZtXUzHRzRSiXdmdaDtqYrA1yxEnB7X0BsPCr6lfYNiWFBeA6v1YlS6TfzLT7sRyb3ihHIw8J6RclB7PmF7s1uOWhlJPRLeKOHtuSogNvd3yXOabLy-0WsvPblRGNQK8G9bqiQq05MDsjtsuaowePAhDDM5LEX0UTvs2Gclj5JGaR-Dk10sD_eq3D6zquZfKubmXMFkXmmQMQTodANuzQauqey8hFpz5XzkFYCCdVkBpAxRuxhtZTq6EB7NZjdru9FzUUtR6YYYb04oLPHUdSYA3-G4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KauRkzHGMH1YVVCc07LBNwTmnoAovXiVMIyacbNc67dQEvAwHbXrIwtoU9-cTz_V1B4frrBXQZgsiMLh3CO7HL2b82jL_R59uUpoCEyZx2nkTc3KN4XZxr2B5lzt_-azGgpgt9Cw5f4FOTl_U0alwSMwwkQPTZ2m4R5DEMlpJ5bd95G7Q9nmGEpQouIIwP5PKD6edGUso7pNC_5UcXH70a56q7O_Ti5mlz2QsLfB95XYoHD-8OFMQjTMaaCSu6Fk2gbmRbFeF7QRccNmoKpyrBETa5fH01RaQn6QjsTcblrIZvgDW4h5QMiOEunf-6MvCRahMBaP4Mgxljb2D5fK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OD5YxZ1uyjJykc8IdkUxDurexuJ8cse-kS_1WhZawiuaXLgY0suV7iR1X-5Na09lE9QLGliRT5NWu5PRckxu5Pvxu0L2BGsVeJX-t4qDLKxAqY1i2EYzYoRTjo8nROT-00vcb7A8nfvSLJr8lzm04UsJ562inSsfTj76esxja9Si72OlX0EhDIt-L3uc0KbhVxSC09dDa7zcq7twHZYgZPhdnFQgC3ioYDW951hXSiJIdbVJbqzsKmYxktrMCJMG0g5t7U-lLJ8HtDRnBA7PZeSLGO6Mr-6aJZMoZHAERZCq8bgTo7nbQJOFKqFeE7akazH33JK-jMchaIdmK6_nWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO5t1dhvtIzJ3GJp1QRq8uhBX4WOL2TKDJpPy8BwoKuOiSufEjG8GwWl2N1RceIe2Y35SW99JmqiqmnsBghsqzAMfQ9zmE5uyv8b8A0MsrxJF8yIi-gd3cPXESA4TW-Xaeij8VLlucs6cQPWuWv5yh1X90wurToAMPvIYG0zV3HUqS0xP5VXIUoWumUq-bi5U6CHyZ6K2q3Ry9hqJxAVFdHSBFU8ilDtoC5BGt8_D8TV4nlIXzNzz0cxnp9geuBrVENmBSniqfI_E9PMSXhNJbfkkFQIaoZiCd94EPxUwA3U8P6R78ROIQEXxZrI3WCng-eMXBWWtNOjEivW_0nJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1khIzRFaqFpJ1uEUybjvWBNYU7kiAll_W77NBmTGI8yrDtbj4BUPfDnZeEFECBsriqF6micPbLTzuL_NMBZZ4EndniPaUnoDpVSXObZwRY2hWICvG9PqWsfN5bySHHkaBUQh2gp1koHKv-iAOOmGpQ9BiXNPI_jZ75alopdy3o141OP7s2nfw20qLweMnLoqwEdL_sGFZeXhi93c-ySJo5iRjBrzzAV6syUwZH8qc9et4-XVJZQsvBve4zY431tctXcF8sD-LuD6ZNjeTtxtp0p5D6LUcbhyvBLqK_GgWt1P16LYP5lout-qKwpWQoIRYLQY7bzsGJgoUIY1ig_Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=es3otfXqV9XUXeyIbimtmlGQSEHypnZTHqSCwNFplHs2xZfAKKrZ_EuG76SKBJLvqTPE_fKnTzRcE8pcAClunGn4FsSwrHE9L90bG7NooeRZkDbWgJAp3z0JlYtuJyI87xCYKHOZM9G8TUCDWNEFRSezd-DTR-wr0_D0D1SE4cReT6xUaH1TOtl0r16z0TVq6X1G2CX9SczNtRmlrH-EQ7SbHkTHM_uHIyAUoJnOfQ_DOgD8eRnGHkmQteKQEnbA8iCzf6PQlt1bXuLrJTFkExCphRQn_SJdx4ayrNVRjrMFl3uiFYl7Hi-cw5zwPIZr5F5HMPSkrwjjY5qiAwzmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=es3otfXqV9XUXeyIbimtmlGQSEHypnZTHqSCwNFplHs2xZfAKKrZ_EuG76SKBJLvqTPE_fKnTzRcE8pcAClunGn4FsSwrHE9L90bG7NooeRZkDbWgJAp3z0JlYtuJyI87xCYKHOZM9G8TUCDWNEFRSezd-DTR-wr0_D0D1SE4cReT6xUaH1TOtl0r16z0TVq6X1G2CX9SczNtRmlrH-EQ7SbHkTHM_uHIyAUoJnOfQ_DOgD8eRnGHkmQteKQEnbA8iCzf6PQlt1bXuLrJTFkExCphRQn_SJdx4ayrNVRjrMFl3uiFYl7Hi-cw5zwPIZr5F5HMPSkrwjjY5qiAwzmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PcJimkMZ5HzhpMIQntjgWavxFW2dgmo8zqfsKpiTXJL0j5nsrZqxSs4GxtWrlRsS6FurX9uJNCXX9AHfhQd3hxZSfcMGYEHwtRktP_xdnBs6iAt_d5STw2P6L3WZ6IoWYh4ri5fAnxac9aFLyI-Dt76DdpnpnUWyFWve_wppdhOfVwoXiFhuRMecdq0_4zLA0E04PhjI0ry-VLZvXkKhCmM9-VjtzxLAJMwTs9AkJkEtCuKOOeW1NLquyKKLwo-Cwc3rSsSbs6Hu1VcNAx9omf5uLgkTkEq44ML7Y-RKxLGDOWR17KN7_olw8jbAznMMlYIsvQ5Y_ipaDc54dqsXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pzt9x5FvARYToWTF3a8iX_JrydQyHA7_klXOxhaTZEZ4VXNfCOI04go1whSd81Fy8HX1lClokPBFiVv-9DK1_F6G5RWzsEumtSUegy2CezFyEitEXBb16mtLNmYPTktxkxJhJKbfVZRdVhGPRnYdg5JTpomR4uLjjgbm6uBgiBzNg5h9wOVTe-MiukFuYZJRTBgP5-xF7vuTT2LTRxug7tneUuKX_NotX_VH1VdHRsv2hGnkjKKhCf4_M-6Fxx95SBmWm0mHruFl81PgvVlOcbZKJ7RtSueVXa5-zppTjtfHAA7UTzdWODNAozDShnHrvRqy7HfIXD1IVeKRv3U5BA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pzt9x5FvARYToWTF3a8iX_JrydQyHA7_klXOxhaTZEZ4VXNfCOI04go1whSd81Fy8HX1lClokPBFiVv-9DK1_F6G5RWzsEumtSUegy2CezFyEitEXBb16mtLNmYPTktxkxJhJKbfVZRdVhGPRnYdg5JTpomR4uLjjgbm6uBgiBzNg5h9wOVTe-MiukFuYZJRTBgP5-xF7vuTT2LTRxug7tneUuKX_NotX_VH1VdHRsv2hGnkjKKhCf4_M-6Fxx95SBmWm0mHruFl81PgvVlOcbZKJ7RtSueVXa5-zppTjtfHAA7UTzdWODNAozDShnHrvRqy7HfIXD1IVeKRv3U5BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8wMW8hyYXc3e9-INxT16VOMV43tN8WKt27qzhopvX-Gm4c6f3rE-BrrT_HEhKA2aUzp_t95l4n43pIyG2_Ck6sacmcsx_rNXO7MzChAFSSjEJA1hYMi7iVFuJgPZO45znaMGpb0gEGkZwN502E4b8UlSG8kyTrB6-_VFTRH-5XSpaKXU6RfwJI_Ko6S-YSLt3jRSqjCyIsRbDMQcGXjB1QTnySdxdz1hREBqpajgyagMiu59fmCpBcGd7mWRcuUMQb3Gfq8CaMI0rKSsM0wQDRJlA_y1FFU4nF5e0vx_EJ_sTJT6X8ECL_5U9pz1k40MoA1VGZxna03kAV1fLZhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFVqsvcBhyzpDyBP29ADJUW3DgGsV18z5iImz0ck1e3zOHSJzFbqrbo7AhUsc2LeQcC2A5kl7Y6Tf9MDIFnc1jggcSRAcUZRbvXDhghvaczEyMhtDrc4Z6z-6Ust6Cp0mTEs9SCtBoSRHloKJXuUi_QCpXR0obxtGp8ct3jgYGHEEePWkLsp1zbF2eCsqKYOs_AiZVePlejtgRBESee3e5CHgkeEE9RazJngSULeGIwa-TjKS-mSpgycZ7Xmi666rVDQc5xhext11k0LgvoQf1zD8OLLnPk-NmeHLR1ArqFRJxNnx3sketrBDhRlkxeA_LhmSHPhah39UWmJQWjpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4jJgdNzYBrqAerKemgZ17-D3zUSsNr4OQreAeWWJeZKIdbzMt_CP7I28lpPJG8pyL8eB2J34kBOYOltaokaixzh4PHkWSuOuAv2eLkvkH8FffyT7dgjYaTUKn1r17wNqbyZIEVbVDDY33p7vPx3sNMOH7TaDJooQ5qq-YpsWtheeP1qgptpr9-s_w1fpE8Pwm9wHHZzgJca110XyPRkjyJS1A6roi8GJiBQ75-uZ2o9cdy-rx4sbvJvC9XkeHNiCKMUU6b5HLtpTCivLD4r0uw_IJk7Np6Ze1MVEXuvVzXKgBdKcTNe8BMOow1RVdc9hYeR7j4Zbyt8NdH7bu2GVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=vxbyV-2_5MlyDOScWwiBNRcjTlR5FBnB2_Y_GyDlIaKdWYoxglZuS4FM8uVq-ENzQySxPfY82Zea5guPw-n_OBB1cDTxB1ST0FwpjYkfkBftD3StnXkXQ3URMw412-8eXL-381rIlB-XO20PyHaMh3ZesBrlpaBTdrtV63kHCexrZhGS5TyRy7iReoDL38rTcFxy2DYjKzcj8Pt0Ne3u5WxT_-jUPllXfJyNcTT29wZd96mjbHCRn4rBwTanP2zY3QuVeQUqhUv9eZ4jWUvA2XdgX7z0zdELE3DGQK5d_BXZY8xK32H2uIPuO6PzKEf8ZCudD16rqh1U3RCPpaAloA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=vxbyV-2_5MlyDOScWwiBNRcjTlR5FBnB2_Y_GyDlIaKdWYoxglZuS4FM8uVq-ENzQySxPfY82Zea5guPw-n_OBB1cDTxB1ST0FwpjYkfkBftD3StnXkXQ3URMw412-8eXL-381rIlB-XO20PyHaMh3ZesBrlpaBTdrtV63kHCexrZhGS5TyRy7iReoDL38rTcFxy2DYjKzcj8Pt0Ne3u5WxT_-jUPllXfJyNcTT29wZd96mjbHCRn4rBwTanP2zY3QuVeQUqhUv9eZ4jWUvA2XdgX7z0zdELE3DGQK5d_BXZY8xK32H2uIPuO6PzKEf8ZCudD16rqh1U3RCPpaAloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjddk_5Cn7Xs_t2Wbe_ViJ-qteIRvxLlHKl7-wyML4eGsUQG2tLYCfSP-YWsvlx6UzoqnfHAggRBDb0KZ4mi5o9a7bSm77NUZ08RHfDbiYfpLqNxfU9Jy4qZaBgSL4SiNe-CXe337-NmH499IWReYou_94bs0S5h78fQbIWFlvJY6rId_PtgVqiQijQFRw8nwq9FNTvfApAdmiThESOcbpUZeBiguhWa7ho1z6E-RX-waS6wA6lys2gsIKR5KJaVI3Bp6Z79JKse171hp5Ey2oEszMJfoyvG00wjacrePJG_QNwRSski-cQjopxP6022B-xclPIgDTyZkbQMxavkSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-6i55o98D91eyemMs1pdr65kk6UJSxICgS0f3gYxo0e9SpeB2amXGCJV8-P4ccFgs2Ne5WSq6YP6FWcfm75Bgyog7RCLn3FIJd6f15h1kL8Ksg1Phv-iSdXqakrrCZ0l0DieqnR-v10Ah7IpcBBszyFMBDR74iBCG2QMD03jIbQPXvJOOvMzSp6dgfmYeeaIW8Q1xLcoFZNFU7mXHEI13Rn5mbeiRuFqbYuX7ueufI7S1796Bzx59FlkTDQ9788qOmBsGINyNG8e7dX4c3ftZUlYoUIKn3TaIBmWd8fp25C0e0-IPnLy2X0oFPVORwaaGViGZIo2woSY4ZnkD4C2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK4QTNvFAaD2KP4LtV-2lLnJf2HtUL48qxaNMhigON4vIRhpSZhRKVD41yPexaSrbGpwWUwL3B0GQE8SZPhLmkjsDP2M93l8hdkdS3Ews9amViajJjtobRAoPfV1QxIxFAUIuCXVfSqyoOG2TUkcWKW8BjdddNeNCMCN9-k_DhgziNLCh4rnZmFi6mBBYiXapDygTKvtyF3cbNG7Y8x3DO_mP12-D2-tPd9CnF1r1BCeW6oN4sxppRfYkC6cFJEqidyoc5Otw0XHVVxxZUuURhXHldv28ia0ThWLvq0wsPnqEdjES54qsVx2Cd-VsMzTOTig8MuPZmUk4UC62B_KCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuE7iw4_LAtftfzKNHWK44w5F7EiVOCC953b_uLk96dNJrfOm_z3NhCDJW6C2zkgZzIIis8SyMgWL3YDA231wnPyKwannpewKikC8ywS3xiko9iAGI8XUb5bSYd82tTEA0iL0B5BG6EWDU9LucNeds0y1i0jh9zzSbSI5kLpKAfDXjKZ5GVYFKvA51xAZSujG7aqp3al1ERdlYFIIfY9ZLtpeNfCLMwgN2CYNdSBgm4sMKNrI0PoeVv15zbrsBZTZ6QOHdeFw-X8ZtB55s-PbULoAQzLoQllxqJJLB2sbbhoSS7nWhoNSq0PjIHcQnHmA64NhERkuGrYnsNZfKi82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnFF9b6NPtlfRmcPxL8_j2TE3xYhh5tLoC9WOBMAFoROMSnkLhD1_elDqmThxveWSZhfm3P4ocgT2a5DVK4dL_NxWl0HpYwI2oYE-jVxmoSTpNZMW3YcYk_AJp8p9dNYQXk23FU3lzo-XLqEXrSUg9EDMBeZlmKM5OM7iLnhPlPr5-UKzlS5EOn0YJb_q9mbmvl06ExrERTJvzhzl-yURKGMWwx86nnjjKYbWhUPybNnlfsd8vi8nViacRyuhFZT5dKnzenAgDeq-YNmK8rOceeJp_esbv40jDZQU6EYv0NJWHYrWE11InWEjUkd_dDJxLd1j8bm5q-zgube8bPFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c38VupMklgjSUtgc89dJEnOTBgXeffpD4TTpuRluwI4E8-PKUWG8WFLF7DV4l3VrWNke39F982--jVqCwy2sYQkeSum8eKWsl9kvlHT1pJsbhGBhqCQEyvql1u72GopIZouPoSxQaAj2GrZtKHvShUwG1g2tIHULrdKV6Uldf-JWpTzd-GQ5yUtJFytrq2Pi_AC2LvMez_gwd0f7X5fcCtfDIYOdcccPNH2w12zc_5Qxro15X-OwtaT-Us8OV9j8BYoZB7chzsWx8CtOLitBy7yjkLoUhsUAEbIrGhC89XUUkI-FlNhhZquBT-nFfmKli3JcgZjo4a9-_Ui4CVueug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwoVFY4dauBzJgUiHG9kLL3hNwI6udqXSOo4sTvyK8iwaALz8atK6QmoqLoYDKXKFm2afmA2KTsfAfZoe7RBL4SOEeHtHNes9mNvjXYkWYVBtBWd4vg0nKE-nt4hsCRTUVS4Feo99NXCvYVh-zMi677mYVR6rC0yiX3gXUXqPO2O05uDrVQAC6oeWRci-y7B330U0qhBZCO4bIDM3N4K8P_5Ffw2Jm3tzk1I3qG7Kq89PQBNUcNmHL6cHM2iXrJemORWy90QYwYDUJJK0-LGVtqG-vjFFIxPqZQe73L3KOBhpZ67WXaLESyFKOoSZdZS5XfO4iQke0fW6CX-Qggwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Msj0R6X7f6Ti2LE6j67eDGJekNAJWWwPxBTAs4I5tVT3HPXOjzw7RmwhhB-IHKjSiDH7jpzHxWlGhwDW5eWTVhlWLp5GG20xNAEHBQnc3MFH3Tvs3KTe8_8Mnk7BGXxiLURQOEewCke2Sner6QopRZ7GIDmmjwQnemHgLsSuEe3tO9NJ3MaQwWTzgVzjbC2bU4Qs1t5N_HUaUWdHnwuUDbsTTXfdLDDx_HsCOGptDUvTDSoMgW4j7fpRkQild-Jp8x_3_awX6D5lJABst4p-wlTUQPxuNX-QbxztG1X4XOOnwzz9vSzHaAAAXtVgxOifE7F2xuyU_JCSqpvX8-F5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nt1LQF3Slajh2Lv0hIqOyC0p4oVD1G595_8VAkKdygTzI8vods3Kq5rF7Swo41Knyd80KBnJDtOKUARi4QBifBGiFDPWA7ePbkU9KOpz9I-c7B2wv6PZPAu-izaqznRt-SqarZbzK_O6GZpRAJJexa4q4ifnYHEv0qEnJZtrD3mjdz10t2B3s9DM4QnjiOqEY-k3oC_yl046wc7-O1s6j9kH59B1x_Xrj3_Ed_iG4uvOgbp2S4GG9YWgzNmofCT0V5_0Qls4srFAPjjNOWB6wmE8diQyxIVsbz2rH4GiteJMj67DtPubQZQUSECNqg_PzAAh1AzS05GN_MrCrbp8PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFAO0ALIMzsljbJPIIYobzl1Q_YxwlqXsf_qEYTSZPF2g4jLU4l6kXX9aqWpAvYy86XRnMj-J9wJ1PHYxmxKGHWU9fm6SGstXlITy60ve9h0TbZnKHn4yBrE74b86BaFjEx_hEhnIKFMv5YhEOw2vw-dknHGhDz6ypAmznt3jf3MyeXJIUt-_g1u6K87898MH1gJ_k05ZS0-CuLeopQ6BZynI78TumhHnFMbpex2a7e2aRsgTIbe9T-d50u4vQ2rRQj6QEbg6GpQ7DQYfQcftHLxXOaDaYGfmnIPud1h23JBTd2EeNH60wGSL7T9evCFeyt3O3xztkJbL9XOwS2b9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=IG9igUwzeHUi39ljNr0sxV3U3kKydfCU5PkZVUu7T-hUcGwWy1DNPuKwS84MYTnc6Fd2_Y97Iv2xKEcbi2sWbQk5vooR0_s5WRcxLCF9Vl8DomqaBTXOu4XfD-l5FJrl5VZ2RFePW48G4g4ZHak2lO0aIwRTLrXA02rUyk5J5dSPolSe5L5XdxvKdVQnaaHvDyV9g4VlNGB0i7HbgfH7FrjNbusbDmdGzaOaNvZ0MoRB9LHVYafnrNa9xhNuSVVUP11EG04elBr0B4gWRaj9QsE07lkqiK_dyqFt0671ajJdJYYnhkCvJp82RqTeIZCTEvhrVRP54NeyTmTJScn5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=IG9igUwzeHUi39ljNr0sxV3U3kKydfCU5PkZVUu7T-hUcGwWy1DNPuKwS84MYTnc6Fd2_Y97Iv2xKEcbi2sWbQk5vooR0_s5WRcxLCF9Vl8DomqaBTXOu4XfD-l5FJrl5VZ2RFePW48G4g4ZHak2lO0aIwRTLrXA02rUyk5J5dSPolSe5L5XdxvKdVQnaaHvDyV9g4VlNGB0i7HbgfH7FrjNbusbDmdGzaOaNvZ0MoRB9LHVYafnrNa9xhNuSVVUP11EG04elBr0B4gWRaj9QsE07lkqiK_dyqFt0671ajJdJYYnhkCvJp82RqTeIZCTEvhrVRP54NeyTmTJScn5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyHGnXMeUl4B8W9Fo8QIRrZakwDOAzm5S5bBIt6tKQI1O4Q4rbRrWB-Cexj1pyHqb0NfBlGxl4fzy1l86mf0D0N60BS81B_w59NpgRWepslfYWx9agoKDl6Xix1IDgmrcSU1ji0WyXLeC8EdHtbtoNl99v2f66Cyh7h6EjTueEhpdxcP6W98GUKDBgnXkqyPd1RzYxma3qvbM_A4Lk7SkOWydwGoz6Q1iuJw0P1j2hCgvWr80ajBxVCVcva0zFpt8mGiQBhFdyO3tEO5ZMfpjdXyjXZA6md6-gXHr9GKn1SKGTs9dmFysftN6FGjx0W34ruKIRDfABd6fyEqx44aqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=UDMKM8Y5gA1efXpx19-8Fp65PWN3phvDPE9hOTfq0MLeqArat8PD967tQKBOpTn3-DriisV2HhZIMRG5bquWIhVaz7RZd4d7rNYm4_KK34Gv4_vALjTPBg6FtMpFoZwN5JkACceVxGXl0-RXommGrkSFXlyR0FE1kJC7OSLk65hPrJiH69aU294A-ZxOTQQD8-W98io16lFLgEJR8KTXOAE7Zb32G_HrKqGNbQ5Zyu-TVRs-61X1MGGt0dBtsxRMT86Y15lJYqIGbvjf7cHoi7SeOSatcQ8xKsYTelZT_gEXrWKK22Yfi828mnVdXthOwkUWpsAwfxfPyGTwu0WXew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=UDMKM8Y5gA1efXpx19-8Fp65PWN3phvDPE9hOTfq0MLeqArat8PD967tQKBOpTn3-DriisV2HhZIMRG5bquWIhVaz7RZd4d7rNYm4_KK34Gv4_vALjTPBg6FtMpFoZwN5JkACceVxGXl0-RXommGrkSFXlyR0FE1kJC7OSLk65hPrJiH69aU294A-ZxOTQQD8-W98io16lFLgEJR8KTXOAE7Zb32G_HrKqGNbQ5Zyu-TVRs-61X1MGGt0dBtsxRMT86Y15lJYqIGbvjf7cHoi7SeOSatcQ8xKsYTelZT_gEXrWKK22Yfi828mnVdXthOwkUWpsAwfxfPyGTwu0WXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=QxDoMEakfFqwL46wbkeAVorJkf1F8hXYsfAUB8MkLe6jTkWPBT1wt5s_mJrud_tn1L88MKqMtfruvnlR2Ej6Sd9gqnzTqPVSHjnu_kcTsMbd8_jHf4kHy9QuzKyQDr1rgt2_lQyPTa1mTf9nLxawaOO8GBiVdAB7f6A1vlbF6BltMw8I0FsjK3rHjcAcW-qPrDZhzVNx90DBWlMQsll3IlsVc6LXsxTDq1tjnKJ2jRlIij_p2ZJjmJQkUBowbSsV2aL7fONvd3qbqcnTIJl598TrBjq_62v5DxeRz_wLI34eLtgpaGFPoTpUc6UQVMAGAunxGIQiq89fNcAwfVX46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=QxDoMEakfFqwL46wbkeAVorJkf1F8hXYsfAUB8MkLe6jTkWPBT1wt5s_mJrud_tn1L88MKqMtfruvnlR2Ej6Sd9gqnzTqPVSHjnu_kcTsMbd8_jHf4kHy9QuzKyQDr1rgt2_lQyPTa1mTf9nLxawaOO8GBiVdAB7f6A1vlbF6BltMw8I0FsjK3rHjcAcW-qPrDZhzVNx90DBWlMQsll3IlsVc6LXsxTDq1tjnKJ2jRlIij_p2ZJjmJQkUBowbSsV2aL7fONvd3qbqcnTIJl598TrBjq_62v5DxeRz_wLI34eLtgpaGFPoTpUc6UQVMAGAunxGIQiq89fNcAwfVX46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=gK3xixMp4tXrZH-KGdVlgZTU1PV-POjYWAPBSlDhfRCx1qxqnlev4BovxRU_2_QgSkWH_swIij3PTVHG7wF6nub5UueuGhHlcN9PiciYLYnlmxIehjxEi-HEso5rvZTqLZe-PaOQaHA-PLzk3FcrfhhghlnqV1LoZeTu8W8K8VXbPoc3rHeAR8HtwHh6JSl7GFQh2TF1i3vxKaDkNPODf_DT6DHi4Nr-BldhEjdu-OycOVJJ_umkHga4qdBWWvfMiX6A7w2z_FGrw5h2c05rWKf7Bjbjye4Q4WHLbM5sEZvwiSPxao24f84wWG9nT-WJ4jW1vDRASNufv7uwCNRaprQEVT0vJq3JhRj9cpRObUPlhfnirVpB8aHchf6KKgwQcs3BymHtPWRKxVa6fQMt0BNCJNY0XDVYMfG2Da42tqjpfW-8JjaRw9rEGTi5ZqDgKO8slNQ9Encl5Y9WDAITB-zvOnlLnffBkhhdqoQqbiAzHe49Xvig07MkYIGMcbXCypv3ikBIGyM8nZLEjREkiIj6sbgVHKqJuiOH95hSZ7kqOOMhDWXPs8OjoCoxqGRf9Xpd2JCokRiYEF_urlDohmmKXWV4GD9UTrDXkLPL4CjOXGrTSHL9e0MOVeEa7sA_dPxCfNtpLgiQL4-ZvrdnCxO-KXBCsSjjTP3iJTzUQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=gK3xixMp4tXrZH-KGdVlgZTU1PV-POjYWAPBSlDhfRCx1qxqnlev4BovxRU_2_QgSkWH_swIij3PTVHG7wF6nub5UueuGhHlcN9PiciYLYnlmxIehjxEi-HEso5rvZTqLZe-PaOQaHA-PLzk3FcrfhhghlnqV1LoZeTu8W8K8VXbPoc3rHeAR8HtwHh6JSl7GFQh2TF1i3vxKaDkNPODf_DT6DHi4Nr-BldhEjdu-OycOVJJ_umkHga4qdBWWvfMiX6A7w2z_FGrw5h2c05rWKf7Bjbjye4Q4WHLbM5sEZvwiSPxao24f84wWG9nT-WJ4jW1vDRASNufv7uwCNRaprQEVT0vJq3JhRj9cpRObUPlhfnirVpB8aHchf6KKgwQcs3BymHtPWRKxVa6fQMt0BNCJNY0XDVYMfG2Da42tqjpfW-8JjaRw9rEGTi5ZqDgKO8slNQ9Encl5Y9WDAITB-zvOnlLnffBkhhdqoQqbiAzHe49Xvig07MkYIGMcbXCypv3ikBIGyM8nZLEjREkiIj6sbgVHKqJuiOH95hSZ7kqOOMhDWXPs8OjoCoxqGRf9Xpd2JCokRiYEF_urlDohmmKXWV4GD9UTrDXkLPL4CjOXGrTSHL9e0MOVeEa7sA_dPxCfNtpLgiQL4-ZvrdnCxO-KXBCsSjjTP3iJTzUQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdviLkLRGUifSDmcCYmetOnSfKTaLbRItGGXG8pPxGoRuSwhfAwmq3wTwrjiR0Fwi2K5gUBxnKVKpf1WCFDcw_XWMz1V4fMtcfn6ohizNc_880OlHjremFuxGFCpPw9NQ1KyIcKXvimQ6P__BijLjpZ4AGjx7ozlfdC7n1FRE_3hdhFvqXk61qQO-1BAwhm2xna9k__vtvbJ6k8ctcONLdVzj6eAq4-gRIVmy4iatJsmfVwDXW_8dxVc5LL0VsyvxTHQykZ64q0aKPMHSar5I8BxqaHDt9RIN1rvQr9phohmSUGq4IAQqSfaVR566wvz2Dvq-sApumj6I-ATOjztiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVOu1DWBmiUViqDA01I3_8Q9bGoF80hVR99DiqFkOa6cqf1t0GGDfKa9Qac1pj_UBBHZGICnNCJdMrhJtFpb03Z6XxBe8Ebd7Z5CwCp6ov_0KQpyz7Q0qjdFXudcZtlyQDgOMxAgRfUONzCZq0RWxclVRQiFqCnWTg-qEtmQZbGQ9RQ6n-4wsdhb_7DNUbDfk1A2Flmpmc78i0rySOB7Da0TDmu5qaR2d2wq3XTP5fqeMdt9FnhqxlpTo-slyJnU0ez2ghS5ONdgwJE4wFlUSdRm_LpOHuxlXy76_1cUa1Uo6FnNaEiJ16mofSKIqsC51knm1-de084hNgMMeep6qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwrrapNI-BP74zTAHzNePj2WxbV4tNQ7dCxpMSd9GxXBt4-TRhqZHCRpPcTyTxKtb6iPPhDCmB_LbzAZ9Vtdg6UwiWkQpizmHhVlXJ7XrUAfNwF14N_jyszSyxpV-LkClV_Fu4ZdzEAbpTCRb2QJGtgju2s4YqQ5dyAxvq1kTTldoeG_xSH2tq3wmVkbBtyG27K2wnVzlDBw9w9Iy1oJ6pXt1w-vAs5aK_2pdWXsj-hxQ8SLXFX5Tvds79PRFj2dEtk0VQMqumTbJfO7WIZ_4eW9U9tMudylx7e39NgDejNB8JSiA-bGi7-D5Fr2eRQ-xrEhJbc3JdVZNOmM09whBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMkadJ6ZDIx4RHXV1q1mnv2RGsM04T7t8qifrY8qEEbQHPg8TtAOt8vhbcW-88ANccJjySFmT9cbLCCAtP7cZEYkgCQ2bYNf-k2khXDd4ZptcI_474IW7nseVPG0HXtljkFbyl3LGL1LosR1an3gCD04QKmOjh1GdavzZfBeN4ly50_9VQff27Q4jM1LN3kN0TXVPrcSOYbfqlwH9wdCAs7hD-pvWhS0T5Ou4QeFObnSV1g_TxE5gOKkhzMGGLxmcItsXjCqwJ_RDAF0tZX31ZFYCY-MTrTfjLK-BIhl-xK0EPZLKztI43XOv1Mizjl0mzWCIkgVOMPuZGusUExnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oR-XeDGTGMdtahcCAKOvMUXQubBWCGBU8uUPVsiEVB0QYFKUskW2USeiYlXXnSW-BSuJ0DImPunDyI_uUKsukPGEsBECtnyTuR0NIxnvnawfPQjs8h8cQ-IGCvRno5C1sKFokDjlcL9bV7PLz-t-ZaezqtHY_WonuHHKKDJ5JjS2Tf_MiM6xTSCvbw_CMutcKm3A9G3lCicIjI1L-QXWq6QK-rcu_2eG3Ob0jlxDb4TeWToUMktPNdZNjnvmLgTg1Wtld121DzcrHIE0AQLCL1FEGrrNmi6NGmz-1e4Il77jIeqKf4VEAzVclBM4OO4_-PYdd-tkxRVdZbLErWXIdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj_lOmlIZxf75S8nOkgo06SSoVRvTJ43LTOmSUQN0szUHZvZhKDkzX_nWVoXI5agAAdnqnZBMQLLaW07UFSOu4j0FetAnZpZDhTiOqeGJ_6co7GJPiy6D1C3aBoavITidATpvWmvy-e4W9QvIdaugEuFVTFLFQtrfVC2r0wmYob9hJSkOr7h9OQyJGKd0yfoZiV3mWa04yturCvMNfFugpb49sMn14n0Mh4rVBdQAOsEEGHe1lHmKf0tCmvAdqDeW7onIGmTQ0mFJVxYTRglR4tqTeGRjrzuCJ83qEUJIVSYcbmv2bFhBlf4AeXHr0T1LS7MA90WWhSUFPRYlowhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4qfkMyx5dSwQVpX_lnjHq-eLFKiyvj8m_GMORTRQSQhy4cepW6GGDyIInvLvKttL9dORrsF9fMwIPcDb4YqKc9CyMlF16x6PBAyA4zD2RlMbD24ZME9EZDNYHRXLcRGl2Bt7ETsZ7fIyD_6VwXBSP_axQtcM_Cc9voos-SMlmyGSlQCbot3V18h5gK76TkpRFQc9mbjOV6pt5fEPUvOlBRl28APf-cTzVonW_Xj4FSOFpsQrIRtN7sImyEgogIA0CjUMjR1-0G68_RlPpA4vnh-f0etLsn2D3oA3N-B8BVHKPWrD066HTvN0iCVcW8U7ExyoDGGfeYNQ6KEdvnUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=ShTOZhnXBek7YsUvIdvo5-CeCD0w_612VyqxB7bOqfqPandUSVy12SpAx7ANFzDZNwmbT3ZsluMa8QpM0xkgBST2KPWo8TBSJOZc-zymHM4uf_Z7O13muNakJD858cwEk9CdIdBB1bIu-QFjb7r5MUV1Asc1jAEix4wLYobTMAeV77x73wns6zIEvuBJIj_47uKusrfkvExoEEq1ccOl_I8qEmIWaKCDCnZVHmvXbfVPgzuSwp0OAlikFn1yk04g5CWVhELU3x-NAMHVqydrgnzDrjzOFNYZh4p7xGgxiLJ7K22jwkdMxJJib_kbbzsj0q7j-dRThSkWtGuhYLptOA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=ShTOZhnXBek7YsUvIdvo5-CeCD0w_612VyqxB7bOqfqPandUSVy12SpAx7ANFzDZNwmbT3ZsluMa8QpM0xkgBST2KPWo8TBSJOZc-zymHM4uf_Z7O13muNakJD858cwEk9CdIdBB1bIu-QFjb7r5MUV1Asc1jAEix4wLYobTMAeV77x73wns6zIEvuBJIj_47uKusrfkvExoEEq1ccOl_I8qEmIWaKCDCnZVHmvXbfVPgzuSwp0OAlikFn1yk04g5CWVhELU3x-NAMHVqydrgnzDrjzOFNYZh4p7xGgxiLJ7K22jwkdMxJJib_kbbzsj0q7j-dRThSkWtGuhYLptOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
