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
<img src="https://cdn1.telesco.pe/file/WZHPX27eVxxiIlsyrV7s09kaP_IWUZ1oWn49j3Q3wrtfrCQycV7VhZIA5tENk1-FrHeyqS4dIjZ0ZajroUb27FcUWo9XX51KiTex0hnkhIxU9l53Hog-S7git2qoKkm5bPJFSW853rxPjhz79qi3ZN4VjViK46RoVMaumoqsRqgWPixGGfuZXc_-5oT_bhlVqpnnVAd42nIIIPZcTfLHPuDjYm5nw3pSuuDLfyZIGeLNgdwdhwiRxUPxAdlBPT4YdvQqvrZJtnnbd3TeSwm0wkyYAnzusRlutpXp5KtE1BHAgt_UoHPgNRUJseoFtpSVVBMQyHchfZjhu9tqlPKtCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 16:38:18</div>
<hr>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=I28CyVRpUgn-mYtxy3tLZYop1NL-zAwj4wR-xVryOr7EtvjPy7UYX571KBWmzDhFsu_TXZpTi-OUZw_B9uFG4NlzMLMsyTmqsmhuCBo4kJcQbUqnm5bz8Tn8_3Y6YjW7Jgby5RiFfRqjtenfVW8_7gKhsjPtLmoU9X7ga_A2S6cp_35_YWx0S8GwCEqnzef61hox3m-pBvZaLpEQ7TJcoRX51HphAiflevMeSYAFkCQVia5yN_KklnFbGE_vaLvkTv3pqe3_urjTy_U1EmTMrYIzEoIq5gweeOyePenF69kBrHZfmM9GCM5qGdhJY4jOPqMfu73KwoqhTOuMmhLj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=I28CyVRpUgn-mYtxy3tLZYop1NL-zAwj4wR-xVryOr7EtvjPy7UYX571KBWmzDhFsu_TXZpTi-OUZw_B9uFG4NlzMLMsyTmqsmhuCBo4kJcQbUqnm5bz8Tn8_3Y6YjW7Jgby5RiFfRqjtenfVW8_7gKhsjPtLmoU9X7ga_A2S6cp_35_YWx0S8GwCEqnzef61hox3m-pBvZaLpEQ7TJcoRX51HphAiflevMeSYAFkCQVia5yN_KklnFbGE_vaLvkTv3pqe3_urjTy_U1EmTMrYIzEoIq5gweeOyePenF69kBrHZfmM9GCM5qGdhJY4jOPqMfu73KwoqhTOuMmhLj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TEUOQw9623iX80fXtrKrzpipRC1gbdalB1lVKo80UHAdWDnCezYHavAh_-lgJtzLor9VRwEb8UuZlRri5PNXMe1FwYHr9nOVenxis4OCty_EC5VFDniyUELon3iblZJWWBl2Y4RDD9a1MrEuPPTVbVaC96nOvYHZZz3Y2uUgallitnojWel0TaKh3scSXK-6H2qW-qKaSZaEHmF1Zn9m5BjGFK6Pzpk9tb7YNlOZ7RyrZNBbGND-9RUbSv4URJ3pOjO-WoNzS453MH2kI6RW9JfBC515xd6QlWumqOoY1xYj9XxM7OHLmdcqmr1-5IYLvIZ8xJHbDYUM-CmvkeVsaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0Y9InhWIXvDUdNoDqFPbcN3XFhZwTI1auSe-xXaE12ZPBct5Wx8p9bLiqhYzByTdnMT56qsCV-w5wlKehDR-3AmqAItNDnHaVH1jLsix8MniH1Cm0IIoXUOVJvnz-SjLXYoAJYepwJz4p6HGO7m-e45Gy5zoGoSPja570aCakn6ckmWqbZ0kyADMjk9cBDLb3LYjoHWjstkE0L1N7ej6x9GtjawXSq5Jt4CjlLxfjDCnYrAbKEFSM_NN5nOWkMpX1pRDSFa69D3BeUdLpGrlnyJZi-Pc56_rtEjDjjA9qWA1Dl1Uqdgb6dOqELdBMHeI8pjQlb3CtZDNsNICs9moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sy1FnLaBlVNT9WxXsaIy03a7YHbf4KKEwZEX2H9qSUifp87D9H7Gg-wBf08t27uO84pQdBwrswg76ks3EZKT8SD-LFi7Wteg6vVetYANjKAyvWPjQQ2n9KHL-a_bBtv7r15RbmWnS2JsOaD3heGZ5ar0zzPv6jwMvtgELMe-3MCcMYJTjtD4-lyVyI25-XluBrXYsI952SJB9-TrMparDpGWIXTUE6JnyuKvONlEiZXyZZX7YKZ0cQinp0cSUsipRuvh03P38jXXPldR3VK-hNkutAaYf-fpgGodwBotQHAMC9sSknw3s1pebpvJ3I8ge3qiJgLiCizZAaECRLUnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnXom66ld4Tyg3liZTSns62E4ufeEwC_MFNFCY_GkjRB251Bao4eDKmNRlaXAUL0aMqeNqcMX3kJPSy-E9xWGVgT0AHopvtcwaTFIzHDDvXX4JELJHYy1lp90OjxSEv1ExZ0LX7HA1PSiLZH8oZFzwKEcqFMLiv15JLeCSfpWf6oFCp26rAahhuys75jZ1Re0xr_c9T-c9SFVR4n1DJJNTaPCfjyGxq_dA2Tp-lgne2QhXGK4Sfgy8BUcYrgp5DBsdPOTGb_REpYgnE8msJ2mkYNREcbTrMyEnTsdIQpi7f3jwaPmGUU0XLP57E7qJsd9U6-KfiAzcr87PsYK-41EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/andVAH1dtI5Kd5z_kvRJtzdFzVDKW8158-BVFmeUacGDQ2J8phSYf2qSNjFV_dKDT9AwX1PIlNNrDVMr4QvD4-_zv-W9WAOmVQPOWdF2ox1AH9L-uB1GHH9Z9UI8rT1oWdrb786dUrm3EYJJTvrhhKAIEcZf4JsvRHTL4LWjVuzLwxiNJrYVL4S4sZCb4wq1FENfeggQU2FIGSRbdp1pndCmHHyOxzcHZ7xgmdbLYt1Lo9Aij3vaCHNd-uj71m4fF7Lxoh8xJFrR3Dyeo5Ev6rO1aoyDK_L-9pvBgGA48H1i2zv5ye8KWBTeDywUM32Dcyti6T4xOD11Sb0qTJ6jOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkcRbc-2hum3EdHY0KiqHUltPFTDrOjidKbegDn9HvtWKwalhE32yNKgcb0kyJvFSntxnvTa3V6y5PzuCb0YwcyKoq1zkBaE4wWRlTRoaj_jApgX6R-J7dUQSIBIApL4Lzpdhqyj2L02WjhII9-1Ijm-w2VJDkStnCNd1aPcL9-z2P1chNYUmAvRc3uSuFr6GC-7e0lo6hJpaXTDUwk9b_Fjg-7ytfxwxx5AUvojTxZLsipPv4wP0GRy6CcKyHXMt9feCsJ5cKXHL4X7bW1knZwco56FVh0gOdqbeDHpgZULd8gYgqOslOm_g5S9pmgNH2G_29iJFp8d0EBCyNHRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gMMZbZkcpcjmo-kcEMTAs4bqUXMd7tgtO-CT8C-ZMbPU0Iz8ti93gD3AawWn_5U9NlDeIDJyENxuUv6UIIZf3bolVDcOo67zftXssAR5D-OTi0E5vTGe-8uvvpAOC_8eMwQEjXvvJeCeWBabC6l2dgmFvTck6n5cxz_M5Gu5ZO3J-069fJtPIAvuoF5l09H8Wypjwls7M21EelxDS_hughpq0WPds8Q0ygGGzMI8F77ma4Q7RqJPyT0DfWXE6aklLQPeX8eG2FSGyFayO2tdqbRJpPd3pEsCp8q4PzKpfZxTbi9hsx2pjOON_RhdLtrn9-d9eyKKRA_MqG2byHxT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kpXTXwqQ-P1j6Cx9_0BEvNiowrlP1cCoqMdm6u7TTt0YsAd7oNMKSvP8TlrjinNAxuT95zYqk-aXZ2NMmdbhN-lruwIals8aHWCAxHoYqFQuaAZfFElqnE6hEwttNJ_tpDxvAHeAV_q2P49ta66ABJkkbw2mtOoPrIplHGN6DFJFWKnVYaK-bemdn52J83cyxK7rpTPb84Hv2Z9ty_cvaQhBNvtrQ9eUrbi_zpLqv9B2KuWLYEH64phvWpM9Z7t5GMeXlYSzIoAlIPFjNQrRyg6McJe8bpkmcSAEhPq13AlXnjZUNCvd7lUlRlnoags9p21S2kvaNyVYI3rcotIfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cmrQybTpSDaiqogEhOy_6Ryj1sGxCp7qh5MIO8j15T2fmMZ4MUbIJJSs5S4QmTNw_ZymOqYUffIMlkc5O9BaFDJT6xsz3v953QWxQ5ctu8KJHKvCwCOQsFIAyr71ou8WgOIMX58-NuCxhxxBvjCdW1Su7qYLPpCbVA4qc7B5Wp9w0eQt9z90yViqXSGpadbzo0GWg-jOXIlvQh45EB7TY-D2HEcHL07bHGZeSVw_VVHRzCuScRgypNQnl-ZDYnAZFNbJDLQhVJ_ryKF3Ylp0mvC8J7wrhnaBZ7OJAKcpCv61WOsQB1nWQclFAHGd4pR5_VHhRxJd5CB_SFBYDz4Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u5Iuvk2HglNW-bOS4ktS2c0d0GMO1ehXWkrX3Js3staLOkjtcppdLYuDEZt0QlTX3YTKCWeKav3PUlinbIMvLVMNbKcyyxjijkux_-gdzzIG7go7mQ7-RY84owh5_r7HLgdwe2d5B63x35A3omJH7vb8OMH6m7_ZO8LfoOxk34PyqqOhOSsq1kbb3wD-WlKa1kVPXYa6wDr2xtqgAIx8Zo_XBQ8WauRWslL5xKqxwXFOy1CxI-9Z3WvEJT5DN-Zg-C1bCChqgoRaoPmF-R25vTG0-VyJ_UBuGjpNgOHiXyDIw5Fy71Z7Dwo3CocuY3wjRgmGL-8D_R11vX3P3Bk9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G6leBWylAQecFto1iM6mBOZcXEVs-4_x2i64ARXjSjlTDyJQYsUPAtLOc-7TKuFB1GlBnsKgXRGzL8gxmwbT_ZSTjrGBQ56vfhwPO9xFIaSD_AeSrJoJbowmYHVVvUnN29Y5m8YcUB7pHUlXQcf6Op_q30XuJ5CiSyelGGIOHrjQnfEG4z4SODQHJ1W_HIL-8XF6i0YhnqAEvwM389GehFxYY-DUSdct8gox1teUIHyE_XcZnoS0aPZMq_XJW7B-OS4cCtyY0Jtk2KUjc_W8Wvnl9M6qWvWA5s3Lz98TZVm_9G-E2CnPq8Vo-xKiSNOjoy1vQL2GK5-W8JtGra6a1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=eSRSJLn9pGX1PBTv5ruPBdPvHSgd6XQDg8SyR8dHOgVauG0m9pXlAx5V32TuoYugb18qrGa3hHu4zQc5WP5_GhT7Nd0-XEsGyUlHiEicwzGAf0wlv7QzbCZV0dpW8kv1SGDN4OeNBUMVI3VSrvmRQ1UC-x6SrcfOJh28IleiEoikFQ1LyC71fS4bMGMSNdunq8OWrUd6bXaNpXOdCcddebL_5vgcZeGVyIkLoumSs0Gk-r9BRoDodRgQfXCM1cMtU7QTbJkiBg1GNPa44Bx1m05JODTQMuSi2hhUh89Vnihq_K9laWi5A0WlqaJQMeMGzEnYHM_aNrJkiCtSeTza8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=eSRSJLn9pGX1PBTv5ruPBdPvHSgd6XQDg8SyR8dHOgVauG0m9pXlAx5V32TuoYugb18qrGa3hHu4zQc5WP5_GhT7Nd0-XEsGyUlHiEicwzGAf0wlv7QzbCZV0dpW8kv1SGDN4OeNBUMVI3VSrvmRQ1UC-x6SrcfOJh28IleiEoikFQ1LyC71fS4bMGMSNdunq8OWrUd6bXaNpXOdCcddebL_5vgcZeGVyIkLoumSs0Gk-r9BRoDodRgQfXCM1cMtU7QTbJkiBg1GNPa44Bx1m05JODTQMuSi2hhUh89Vnihq_K9laWi5A0WlqaJQMeMGzEnYHM_aNrJkiCtSeTza8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=tru6WMEb-_llDrwr19RMwLoXu-7bhznasCAMxw8qfPacAz5ffvm5D-prm9FWPzybq9O7nRGUx23Je5TLnhkcN6FJErOOpLgbn1gnBfHDQWQzHAGcRIVMBajKtqzfdghFLaSdYlPAGYRv6sIRntEYqBBfECMwX1HPuuRv7HPbiRmUDgQUwQ_M390DWdAFzMIEnTrIVsGOq6Rt3gyREr14W2xMObH6I-dOpv9FQWd8UYYQQnCf8F16Eb_sriqxoYsBaun4KkjEZ8VMvE_8D1MJLlgLjLdwM6ohYE7G6kMyJ1V1k6iqAA5q-RRQTsWTZuItptdS1jbJ5NJhdW9Nb-YPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=tru6WMEb-_llDrwr19RMwLoXu-7bhznasCAMxw8qfPacAz5ffvm5D-prm9FWPzybq9O7nRGUx23Je5TLnhkcN6FJErOOpLgbn1gnBfHDQWQzHAGcRIVMBajKtqzfdghFLaSdYlPAGYRv6sIRntEYqBBfECMwX1HPuuRv7HPbiRmUDgQUwQ_M390DWdAFzMIEnTrIVsGOq6Rt3gyREr14W2xMObH6I-dOpv9FQWd8UYYQQnCf8F16Eb_sriqxoYsBaun4KkjEZ8VMvE_8D1MJLlgLjLdwM6ohYE7G6kMyJ1V1k6iqAA5q-RRQTsWTZuItptdS1jbJ5NJhdW9Nb-YPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NWHLmwdFh6_h6191KNlX504PFv63No6hC_jl9Gkh_WnsfwtoFx3xYq5jsDuWV2ubHIO9UKtBJrokTZjOAreHMVfK7Lwt755opwNImRS1JhkPO7l0HVx4Xxm7LRJFG8WvvHN68DtZKRiWma9-Ldy0gSJmJyi-ZYaXKZ8ltC9sNNBqrfDuy9DVouYgEiiVi9SLd1TdI_QxEv8bK-gPjLlpM8pGjWiIc7t74AKLPH_jPhaGcaFxT-mBKMLQ-15CQTN2UszWzqm2oh3F7twwCBFks4ab4g1BApceORZuSsdE04tX1nyGL-q5VzHOy467boKDJKKwN67ztUz7V49HbGSkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pyj73qjkTbh6SGaWg3foZRJWth-6TfcuqzI-RJM0bKVI3lA_5YuUdK-LbGL_kn_tL2v3XguqVJLJlQaItEr1oPWssY0WZtESlVZd81PZGLGLnmI6spOdV_22LyFfKdfJx5vKhrsxqWPMb7EKguT0TQnURiiwi-NdgFmK-ARN0DF_tiwgJF7oQXyCRo5HStN7w05HsqIhItZwP-oA1CkjmxIsedyvxAq-RkuMYiQD9OmV0XSHHiv7v7YtgmuByJHRbsGqputNuik9BZ1exVov8qPjppUXriuhokeGi-oxXzyMp4fATo-s24YkJsu-nSveQ3WPM6ZUWmjVWIV7kdjFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FddQ80NT6N00J_qcuJF5R6O4VNBYNMm_JtgixG3r4A_tQJnA6YMgsmm25xEvqoG14-CexaNXfJV8FY8Dzd13PaqyayfA_rHkTB2zgahZBQHkZk9z7gI6Oz-SxMXQNi0ss0vGfmUAlRZrPWjERVo6ZyaiC_KWlNDBgt71lgX6DA3wz2040oDvv1mza7UHuSAeOQQSvcy07X1P6uw_X_3NCzEMVhpeHv7XmtZmW1fafxtruSA3pSP6Az34yKPJuRK-TSCp_EuNK_zEnIQdMBNnqdZDbXaDARAODqQRS8ulbYk0oyT2fkKmw6qCez2nVILhci6dLy4d7CxAnGsMaWG0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=dtYAM6bLA1cQ1PRTKYw9_VKeaRP0yBNPTT3NitOnqG1FPn4Wbrzfzf_HT4PJPGdAcLfEQXnw-Mdst9deD5pPLenamwvGsW814hy7TfsOX0LKXSsMfru_W1ncK-fXktX9XhJlY7wctGujikFPoWhKZANK6P_LIBTuw8ncQjzqcl4AkzB6-eCqF83YbmLMoO3CTa-yn-2c-46XU03HSqJsJWExvQCN9d4VBSzf2w5CNEz8DtEGKbPecRp2m4AM3eHuD0371UMm2wp5lJTIS94AFQ4qoe6DUDNo4W2NqF0oWbCUJnH8JwxWkP3heSvaz_CVJpt2ta1gviyVDDQG3luJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=dtYAM6bLA1cQ1PRTKYw9_VKeaRP0yBNPTT3NitOnqG1FPn4Wbrzfzf_HT4PJPGdAcLfEQXnw-Mdst9deD5pPLenamwvGsW814hy7TfsOX0LKXSsMfru_W1ncK-fXktX9XhJlY7wctGujikFPoWhKZANK6P_LIBTuw8ncQjzqcl4AkzB6-eCqF83YbmLMoO3CTa-yn-2c-46XU03HSqJsJWExvQCN9d4VBSzf2w5CNEz8DtEGKbPecRp2m4AM3eHuD0371UMm2wp5lJTIS94AFQ4qoe6DUDNo4W2NqF0oWbCUJnH8JwxWkP3heSvaz_CVJpt2ta1gviyVDDQG3luJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B10Acayb73tGL3Cr1E53dPwG8Co0tnj8jWE79-Z_GGp8bWO_tED15M-J5htJLWFb4vjwEs1VZ5d0-CCz0y15VuAdo-KrrF7D0hmLa4DEf7ypIKIVK4Kl2F0109UZrZBR1xdnKK8CwKJEQFkH5ce2L9y6TR9hDVnCSLZvlrIAWRjiZNM4lp5QdWlb3EudQ1KlSwFJeJjeiWYZcYA89EigjvFUqfH9FGu5K3v4-eFDdayA0oE7Pfn89G4Sl7s22xrPl-yvje7TOEx5KeqZNPtI0xla6OkzhgP_v7MevhwQ-MyIGAhV9iUJDOON3EyhX_dvBy-QDXaSq6iTzRzMETvMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hGFbpeT-0fkqY-jOhbg4WD9zYDdgRHnhxksnA11Ykc91rjAa2Iwhn1KBtDoKk_W9B0HwIFgkc4nSvTQKOhyH5Iam34xbcW87b008kmsA_P29khI-9Y1BgFbwSkaYCAAtqAQZfNkVJj54L-H-IuB09hgf1yNkplXR6sgfVG1fVMVeg-3NpGph0en34rJG35XQKm8Ea329ZHDMrg6N3PUKhrdqmiu4dPFwmwR2vuueC8vWstrX9dZ7I_xvp5pL13rmPLgW-4f20dmDngNUCLXzVqToun-gTrncMUhPygkUj-qGMlQz_6T6ZIM_f8sXO0CGGpNyJVm4dAcAxjseRbbuTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrXVcUJgnpA9UxNSrzDHXG3vdfQKvN8ExoGfUOVj9V6OefA0FxUIi5UvHHAanOV5RoLSv6mAd7IKeC5t08fCpKOpi0L5YwMnZ19Lle2p9RQZX7UL_jsqpq72UuU1G6Xw8OTYO13LvOlieE_lhuiaDHHWpKzEnSNzNdbas93i4DLBWVDDXChdkd7qzOC7n--grjOvCSde5dprGyt6t08t9BMWAbZray3W2JheZy8NXH7cEuFJc9ZlOp9_rBRbGqI1tLrelDyQhTHXKOJsqMKSSgHhyUwg3sW4FtwmpP3EgzH68kJzUylmJvoRfezduIFjJ-QTJ8budsxlR6J_jjZlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=h2DnTkYkyXLJxPBzV9MPTgo40XXfYnzv_1Z2YSTLxT-XM9rigEoj8MzmBb-QWHgYQZjvThpFzpIS3lIXMEpXsweAQycvvm-QyeQnPQ1a_PbX7kLEY4C7tCNvAPb3Xf6IP8_SjaYgREdpsuGtVyb-41xIDEihf1WOVd7i9RvSyWy8zTEAxnEnQotUGGo2o8NCT4lpavfKC8WognxbO9eOPGMHLQmeH2esCXzxDgn_9tJNPwXO-Vju_WznP5KRww8iB_vQiEVkXUhPbtuDktlvUe3ABUueaPpzxt6QeIWT5eJbPWsgitrvd6HrFK7A3gJKQnhOkTs89jI4TCsYxdKNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=h2DnTkYkyXLJxPBzV9MPTgo40XXfYnzv_1Z2YSTLxT-XM9rigEoj8MzmBb-QWHgYQZjvThpFzpIS3lIXMEpXsweAQycvvm-QyeQnPQ1a_PbX7kLEY4C7tCNvAPb3Xf6IP8_SjaYgREdpsuGtVyb-41xIDEihf1WOVd7i9RvSyWy8zTEAxnEnQotUGGo2o8NCT4lpavfKC8WognxbO9eOPGMHLQmeH2esCXzxDgn_9tJNPwXO-Vju_WznP5KRww8iB_vQiEVkXUhPbtuDktlvUe3ABUueaPpzxt6QeIWT5eJbPWsgitrvd6HrFK7A3gJKQnhOkTs89jI4TCsYxdKNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tNaWYLguwU-9JLyOti_jb7Qd_Gn1z3mMl9b3jg_cZNSjMgm6vIFSW_5rrDmuXQnYqjbWFasn453AF6yUJHdD3Ysdb6PuQSliz91B4_2aGjZU1M4HedqsJdK2dhkUks0igTVtG0qGVnvBZGFQD3UzmhK6YglFGuYnaAkQkQOf6V64Qbe37j1h1Hx7gQJ3PkS85y2oq8oHctIb8PVAYGSX1s1pmV1sjQV27XZAalydnXNYb0dwzNbkOHO-7HOdw-qWr3L9qL-uUJDHw02l2ZBwpO0CF9LGvn9WgnRqtPL7dqTx2O6Wa95UZO3eUqgElkughp25yIF988IZFz9Wby5fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7k6rLaMnzK19bfqGDcB8Cm3xVxYtBOURjske0Z78T79VpqlV_2n0ioS7wKNfphNhx_cJ3msgjrl_ernaj4E9R-5G14dTkJfWKYVFJXih_H_8Kh4x05cMK2YuWh5Zy5_AqHpD_gvwfl76FxEihOx0QQuFcQ_MK8baDSW-w10gMBmqG_Z167o7zJaHXEohGkAXp1dhZo6_C7cg_eXysUf6D5ejtO64SV-r_PE1cFHAnye_poY2C122X7avrTZMmZPICR4D60govchFW2ifji-TkM-MJSThokYPkpAIxis9eghEWPOTI9SEXwOuqVWUKUEOQlN8MMBzTHawgd2loWOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=NkUTKffYzrW-pMAzwGZ2ChW2NEDzMtIKqyDyMSQ4CM2eB6MW7GOREEILHcdi93lfcbrAeCHfgCKER6uxDiMD7BkHdYhC72nGuS3wPE2VaC0mgLH0hTRxbQYJcFTTmUIt6A-UdZPoNlLp6GSPdAAcuYP0qkGcRx57RvrO9-hBGTb6zpPPXL0g5U9wJmfZh0-Nr8fZn5XqOp-yEi-hUXVHh_shFvLeQ7udTfiqL7-fAoxMxhVld3DqhvpL3kFsuXsuddRG4nKcs87FkY53gXDZ1PENhshJbtDmIl9edFZoijsMzZLHYQbxCL8LUyB0NiD4Jmi0A73IXccQ6qKy-g-UFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=NkUTKffYzrW-pMAzwGZ2ChW2NEDzMtIKqyDyMSQ4CM2eB6MW7GOREEILHcdi93lfcbrAeCHfgCKER6uxDiMD7BkHdYhC72nGuS3wPE2VaC0mgLH0hTRxbQYJcFTTmUIt6A-UdZPoNlLp6GSPdAAcuYP0qkGcRx57RvrO9-hBGTb6zpPPXL0g5U9wJmfZh0-Nr8fZn5XqOp-yEi-hUXVHh_shFvLeQ7udTfiqL7-fAoxMxhVld3DqhvpL3kFsuXsuddRG4nKcs87FkY53gXDZ1PENhshJbtDmIl9edFZoijsMzZLHYQbxCL8LUyB0NiD4Jmi0A73IXccQ6qKy-g-UFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lyR9Zw1VceVA82CYf4lL6gCbRup4g3u7hjWu1jY84YNnm2LQJspRA-nYxRzdxjWaA-iF-BSvcAa5MrDS4HkC1IQeKpB8VXa8jURbNo4V_sRsH6jA4j8VYCcpqTzAXCNP5RNRol3wlM4N3ETHZMrEoEjiBp0HTBoZ9YDoDLrBXP1zNtGCs4Qqw-w0XWos2iKktwJOS4rklwK6sIK-wbhZLDriBfGg6pReC0AYjTIS4g0jWumb7GG_6eci7OEejk6eJH1htA4WK8c9RXCB3ymtIiaUdxPk-4GH5SJAL8MMeUwsX7BH2PsI6JUlliOD8VU2Bld1zqRYxWixBCLGhyieOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfsKOJ7-BgAexhMCtZDYDrjkx74o0reahYlkXKkLT5OocpMIrhjqyDWH4206yuqEW-aQlmyesbJ4gKtibx8NRmCygyCsiV9byblQYih25oXNa1-TYOXF_T6zowY8GlI7A_fyH_zczDbk5AWrFc3-DBIXjPf1HQFNF68-WERdPsQGk9GATielI1yeSCPpzKbv1alx4kcrkY_V5AdXKz0eRtxK_BbZrud6jSJb2s3ZFqvXJABY5-h_eQ19vFX24ZR7enXXc_DIGAr64gA40CiSbKcjJJ-DELTjjIZtcV8vkbQq_Da3eg7m6D6Iq66DrWEWqGyQWgoaldISC_YA-8qY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/imjAe_kWOB4JS9ZeCjNXai6C5cAkwSUHWbLqcRqSOiRjuDPu1_6kaWzN65svAKFQm2ETlIC1bluMbBVQIDiPYb0uoJVvxXWhxyIj6Ypa-lOQ3jlqcfqhNR_U0YBxDKifNiToan4fxkmt3DSbbe3T0Wx0kqW8UoOsVYTsgUVdHQy2pImxds4Vl4ACbnTjbqN4Ni9GRpYUwP3CdrpjfdbADm38i5Z__SqkhoYXppve1Sdx4V8MRPZNpUlvuozV2VfAH0pqwY3gs_g9mO80rbh48XimvBSSEt-ip6Wt2O4qom2hqpRemSRi97VLW57S4E2BKmk6arUCunyNIuxPknUcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eJLIUaxPBYAALRVdYOinWNw6HmY0ff5xWe3zifb-SkZjlFPYclFyF1FO8sgQnIIbRIqzPh8kUihuv9X-u9Wm1-kFeXG3XTk2vSzliXPm7gUL5iinbw2cyjMNryNzwbEm4qnznZZvt-v3WUXAOwa-MGYDsOlsieMqvkAoFsubtwp1udmVMi4KY-ZmLg7Jpq1iiOBqY7MXBew71M29NrNp4_DkgS5DIYm-ZEbLNEifEpqCyIv70G3CHxqeDz74FpIAnWOJ0xtjzPTeuAsezvwboOUIpYtseuy4sSbTYs__JJsF5MViv-GGz4R9xD238l3rglSXY2ypZxwjZBG35KFedQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SE2GI732qJ0S0gpZ64Xn16F0CrB3-bJqRUIrLOSctuUtnltyLRR3YfWHTf8mYwDVjHEbOj87ddeXH2Mt3-Vw_c-dDdg5Mj8t05GF16T0arF3-C15AH6usDXyAiK0EW0UOTs6rqGLMoNv8c4odpQQVRo8ywkFziWON4fHEUTej4ILP2nzqQkDbFDPrwL_P0FJxlgZP2qPpDLa7DHUbqoHcVXhkCtt8khx1n1-M8Gf51ga1tfxvunU1Zqv4z0CzoOJJMVAIawiohakc1jg1YcZHha7AYnS_rCgf_fnWMUrKb9QvwzGdZmU5_v59gjYzOXOuSgefQK6kId_lRY8lfoU1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/duebvPO0gwxUwhWkZ32Em0JlUiOu8Celbuu3M68YeaHW9AeNVHhQ2R5eslkr1P8nzgilBCrYDnyDeCaFGIG7Jplql_o0ndyQl3CjYts-85pRru-wlFHfvQmzzSCJy9xjAxi8C7XvM-05z-bRVDZ7FDL0qGjjPfaHtqhKq3LCuSLR15giULvsDV8zwYsrk0l929qjWVWOyS7UBRrB-WMOFZRv9s-Oc4lX6iZE-IwtJ4k6cRcjLtvfD2yBgox1PYVzlYtO1Qi2mNeDB78MIXvctzqHQtwRP8_ZlC0eP5hBn7CU2aZMAjqeoqBBpRASfDEuK3FrzzOLHoRRZ6zxZYVRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E9lXEtNCyzF-lYqKCYgr3jqec6s8Ryq3DvOq64_M_7WQoglJnWeKwcRufevkP2zH8eeHVRSDMe4WVGshDN9zEQfa8ASnOwL5mhva9esoZFsdZSTukguGKbA0wU8WhTVm_xcQ5aJQrdlTLvnfjB0opnCD06I362Modj9d2V0smKkrBh6Fb6l1R2qA3Ic-7YKMRP51Oc7S3ouQRnnUIIUG3NM15amaJuDHKKJzQqz4NUXR2Uy001jMmM1_bt2yOH-TuHJuOyHKbR1wTx0Qcax4miWuOOw4TFy7sLg_peZfRj_Q2hy7D6wDWswVt3TV7M1wx3LWy7Cgv9LGCtHYKpyZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l9quLdHleipq6LjYq7AFS3lpD8kWtJc_1UuU4oQ93pXY_nzlOMOjul2Skd2GvGoDsiN7aRnTJJHHjFjGQBWnfRjb6u_cv8GWCy7ON8KXkaNSPIJOMBjVIxZFC9mgZuGLEJf6kfy8aLmvxcUOpPPZ6fl01FOfbzVN6B71bTwJldNdTqlzLCTWZszp1MjiEn_o-lHIcbOBsZhzVmMO43plXKv5IpEklR1xim1MuEWKmRHhiHm1BUsFXqBRbJh_CzTQNZPpGQAukN6djntA1bEez_iZAUp5NJIFpftNsbCJga-C48I0Q9RSBqbwtwJhVhXOuNScLvGrxpEPLHPfSpoztQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=Mc7JxT-_8Jai0h9Kr7HigG2ktWYGnPXywk9r0oY7QFOgDiMOAufd1oLXubEjupzEmn_qJYo338F6NIK95WylpBKoBd7EXz0Izrz9z4Y8SwZxMQ5rQdO06xX4R_oDhB5PP5_-vS5Bb21nWe0of2--RREeZdpQ4La6QoPPt5jnPs6akPks50v5Te6TKiXu4gFXCucvqWJUN4vtp9-KS54YXYI9hVKU5kx0UwukMcklVLsYjZ_tGjSNAo1aLakVH6_p-m7GXbiYR0Ftyp4qjJaWEi2d8gtKPXYlhZF3IAa4wuDxGHE8h9-hp0GUHVfcNz4r72ugYdp3-9LA9-rclFdJ-UENGFnZF7ZjnnVMuHp8DVlY3w3TpxdjMbL8vsimRTL26EnTodghMapYOY29z2hHgd1VulHM9Pk0vRXVTksGrpEYMkWJ18aoymAstv7WdrhNafxaEwVZTZA3uAyN9fBNWLQ-R5-9PXCCKZbUD7YD9OLnqsPnOihaX2TgWRYFfnERjpg89Sj5_gkZsb3ZT0ffZ9dfvKwbBIYSX_pwoMVAPbDNzSolpDIIsIS_yV5BDt5SQmYSBk_pVZCloXMBXneSsrQjLdLX34vNE-VrpXykGlW5N5eOwVOg1c7tosOET33yKmSRUOX-Hud5UG5l-cty-2lWyrNdRjYN1tA_ADkKPug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=Mc7JxT-_8Jai0h9Kr7HigG2ktWYGnPXywk9r0oY7QFOgDiMOAufd1oLXubEjupzEmn_qJYo338F6NIK95WylpBKoBd7EXz0Izrz9z4Y8SwZxMQ5rQdO06xX4R_oDhB5PP5_-vS5Bb21nWe0of2--RREeZdpQ4La6QoPPt5jnPs6akPks50v5Te6TKiXu4gFXCucvqWJUN4vtp9-KS54YXYI9hVKU5kx0UwukMcklVLsYjZ_tGjSNAo1aLakVH6_p-m7GXbiYR0Ftyp4qjJaWEi2d8gtKPXYlhZF3IAa4wuDxGHE8h9-hp0GUHVfcNz4r72ugYdp3-9LA9-rclFdJ-UENGFnZF7ZjnnVMuHp8DVlY3w3TpxdjMbL8vsimRTL26EnTodghMapYOY29z2hHgd1VulHM9Pk0vRXVTksGrpEYMkWJ18aoymAstv7WdrhNafxaEwVZTZA3uAyN9fBNWLQ-R5-9PXCCKZbUD7YD9OLnqsPnOihaX2TgWRYFfnERjpg89Sj5_gkZsb3ZT0ffZ9dfvKwbBIYSX_pwoMVAPbDNzSolpDIIsIS_yV5BDt5SQmYSBk_pVZCloXMBXneSsrQjLdLX34vNE-VrpXykGlW5N5eOwVOg1c7tosOET33yKmSRUOX-Hud5UG5l-cty-2lWyrNdRjYN1tA_ADkKPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M_wOpUEGeKa3ujSDQdjxYGOHRAC5qECVsS-6VYuVTjRAFn11i-OmNDGFzISTX8r4Tadh7CH_V8EbK82wL1-g1WkxGwxxr2SmTqsAx-v1h2H9RlyZXRVM_hot7ZzIsYeGxLJMb4zYPIwSBUC80oeBTJNTdjHAx75x_P_FWllLtzVkdyofiOUZvwmUHHnNqSOQGVl-GRm5lC_pedIgHOcbuw-_M2yAYCzsF45IZyUpdru7_Kqy5nih4Xr6a7jpASDYzLXRLa4EePUKE3f2VqghTX-nnFNZAGjM74Xv1oYnQJ7i2OsqTqw-87wRpn_RluiGY9B1glPIvIMuB6XB3SIsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YesjX590h_aKIfKjp0bmw4jA6OhBdy_fysGW7S69f13jYt437-0w0_bHQQP1uozwPXMEnvMV9TRHk3JI-Xb9yvNtS92ArcG-4Jg4djXt5a-mopygtBN7HgikILongozeDg5B6LlI9lmxTfB0mvUYCn2v2KwKfhHU4GVZ7jHo90LCIpZIkfFhKoSy3f7gUf37Y2kfCYENe7qqStaQX7DLvmhKQv3FnlUMTuTyR83N2zw0EcHXKxWvdLH70DkKqvjUrkCHPjlsiM5gxaZUQ2B9DLIR1ePV6GcXOw0uRUGD2E05WbCUgfZie5_r000Ky6eW6fmcr6YwhGRczd4fyZeufQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=raLfXW2KJJ6fAvwRV0n4fKZiwCb8U3Nk9nJXcXo1HvqvtNgYyRemMbhZOrcmEbHaZPh2034jXjudrl4MkXwbQ6WuY7NYMt4rideBm-ZZ9TFI2bPWO3dZWYodyVHpuiawns2uMYExfhaQcHaGaq7GOB8MHeCllUfaOzRlIPw9wuiYw0TwtxHCK0vYKB56JP0yViwKDvFP_-5FGuVPrQ97ZTKFSKQluMI9EtH7EKrSqfIC5WWwSHISQkDZStu2ki8RjShCisb1fSkGzJM5gdnB2Zdf03sIMs_nUYLkCu6_a96kKqcDHqThVA79MWLAxiQndtzktALNn5ayhrUYRWnf4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=raLfXW2KJJ6fAvwRV0n4fKZiwCb8U3Nk9nJXcXo1HvqvtNgYyRemMbhZOrcmEbHaZPh2034jXjudrl4MkXwbQ6WuY7NYMt4rideBm-ZZ9TFI2bPWO3dZWYodyVHpuiawns2uMYExfhaQcHaGaq7GOB8MHeCllUfaOzRlIPw9wuiYw0TwtxHCK0vYKB56JP0yViwKDvFP_-5FGuVPrQ97ZTKFSKQluMI9EtH7EKrSqfIC5WWwSHISQkDZStu2ki8RjShCisb1fSkGzJM5gdnB2Zdf03sIMs_nUYLkCu6_a96kKqcDHqThVA79MWLAxiQndtzktALNn5ayhrUYRWnf4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WLW3TBdteFlqo_VRIkxDduIf0RQ6W9IWPjXKK2miP8rm7OzGCfKQb5D6b1uBsTTVv65k1EEmvpuhbV6FAjSSI4zLbgbZgAqt3KYf4KGn4VkLegvP7maFCh4Bpl8Vzc2Evh8ABwicfsBfNy7szFk4buPZRoI_RICQIRxKZ5BCNJUNgBMyVGx0FGBwiA8aGJal_Ag_lb76FefmdltkHF06CdgFr7NCf3s3Xwq2N8s_TTmfFTEe0egUiikEqChZ1DsU7RWS2XjGekbFh9_BlBqInWvdbW-zOf-ptyDWGhLzj_L0814yORfIhSaBuwxn5GjKmCZK_PDi-EjDZ8y_fRyVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4VI2xgirkSRtjZGOIP_Usr7obS57CJBttQaV4abFLmWkZHoR5IuSG24EPR79hvNohQEOZpnvCO3C8R0wZNV4PLVAmGrx9ZRBJI5zPFZ9Z4FvdVoF5oFe_j0AgYAAdOLgwBl899cf5X0R52EWX1noIkxLj-R15H1Y9D4SA4UYIiWOpkWjIHpdTNcGUKLi1w7CAmtLP1Jui3pVLwXl4mZQHGw-aGX7QYdLbpXa25YnU0d9jHWzjWSVjb9ekjJnfeHicTHC_QstWRC9D7Tlp0XFAvLF6WAgCA0CgPFRuxxPFapHWU6rrSvzp0FP088U0EdNeH-xbMZSDZZOIHEO7CfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p3n6TiNWORaPscliuwB_WUdqO9R2uUzkpl6f4dvN3YJkDC3KGB966QiZZde5a2J9sWDkyjRjGdeQiMd1EkFKzmJYMsc0cmLA0Zloa-q-F2GLvCC9stF5xBybTyjtjUZLl9Dul72vsiT6ccQ9x30fAiA3QxiLN6dbiC2iFHYbadbbLX7uyL22pQKoExnAHAmEbOdE_X6VRqD6-LlmwY4VdHMW5zrjgMZfKzwPNQ0iKTwSev8xoSxfPazwMiwIBz2U7c5y_o5_a-76JlAvpHM1eLx6Z4ElxyS05NXyo6EG5uRqhUgp5zuZ_CDgawPyl810qh4XLqcWK-do501TNmgOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=GYg0K5I7y0feVrHyop4H4qEpTAXemrzRPDU-cA_5ORVUCryZVWKd70upx-gW3y6Y5idifdRnfghYTB6N_gjPr7m9yw3bdGXDzZIuAS3ewAjYG5y2AnTr6PyxtfNHGAKoON4SoZPRyx3-q5_HRGva4o4OUmNOzJ_IPEXVB7i0pkY2ARR_B3mm5vAK63LiLE0JsADwe3n6-eivuFbeNS79Mg_p-dDr5U7qrr4xyUj8xvsAixDh-XCdxR60A5QBSIsY7xAAL5v6Ko0fUtyZ0w5RLXYttW8F7TMjmticwSjU2R-7FWlS1rkc79tGar5IWtZTnBFzm_HMdI7djCuB8OWuoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=GYg0K5I7y0feVrHyop4H4qEpTAXemrzRPDU-cA_5ORVUCryZVWKd70upx-gW3y6Y5idifdRnfghYTB6N_gjPr7m9yw3bdGXDzZIuAS3ewAjYG5y2AnTr6PyxtfNHGAKoON4SoZPRyx3-q5_HRGva4o4OUmNOzJ_IPEXVB7i0pkY2ARR_B3mm5vAK63LiLE0JsADwe3n6-eivuFbeNS79Mg_p-dDr5U7qrr4xyUj8xvsAixDh-XCdxR60A5QBSIsY7xAAL5v6Ko0fUtyZ0w5RLXYttW8F7TMjmticwSjU2R-7FWlS1rkc79tGar5IWtZTnBFzm_HMdI7djCuB8OWuoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZUDAmd0k7glCFRRcyjCbyiHY9ln7pbzWFC4ttp_FrdcePdYZuFvhNaft80u4FMKrWLlygnZ0n-CA7GjsroE8NBdE1zd_oT4UyNTMNqvDlc5_kSsjRCVIozUGC2q63l5cy-XDfRbWx3nGZ9qr9EcYCItFR6G6gEZDnWpZaZBBloNllNljz24ogMTmEDCzJm9wlwOYzSsCD4zwyliA9Wdme9iOCzKx4a_hgam0_fmJknnqh9i0xQwpSTCPxx9bkSpKm0om2yjW6ueGv-GGWZVOPlQ7UitU2EuvWZqGaARt9NV3BLX5DAUHt2U8HQzYeObUQ8ZfwS9BCQfwRzwzzgz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=SHlV3yf2UujVZrAhkFf_W-LoUR5H1GaK0huVDQhfdF2cscd9dD9MCSj3U1gQTrcmPpyTC0Mg7scaDHt1kKRrRVbUE_BbVFeskPaZ_ZRUc7lk0m2mTH15N8tJgH_A-jI163zEtUNi_PNyIyN8TA0c9m4H4su7diWhCle3XkKAbhroVOEPNhnacvqaft8FhhGAOBnjTTwLbp3Sl83y8_T_6r4jumLot0KdvJ3wlE4haqgrF9dmVsSNBdRcNamquo3qCi9DSNWmLWKQ-Wymh6JKX5mvolVoTNoErbI0T0eIH3aYJGYKes4bQ74QJzcvWQSJmh9Zp79oN62YlxwAtURwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=SHlV3yf2UujVZrAhkFf_W-LoUR5H1GaK0huVDQhfdF2cscd9dD9MCSj3U1gQTrcmPpyTC0Mg7scaDHt1kKRrRVbUE_BbVFeskPaZ_ZRUc7lk0m2mTH15N8tJgH_A-jI163zEtUNi_PNyIyN8TA0c9m4H4su7diWhCle3XkKAbhroVOEPNhnacvqaft8FhhGAOBnjTTwLbp3Sl83y8_T_6r4jumLot0KdvJ3wlE4haqgrF9dmVsSNBdRcNamquo3qCi9DSNWmLWKQ-Wymh6JKX5mvolVoTNoErbI0T0eIH3aYJGYKes4bQ74QJzcvWQSJmh9Zp79oN62YlxwAtURwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LZ-fFJbpnv4n398jDEULUT36uiQDWxy14I6DArQ_vvUE3voIVQTG3Eaf0bKfp21lMLz3cPo7yLCsDrPF2IDtnxYeOXg9r1qGMGxYLj8cXKOrW9_LCA9Oamc5Z2U2ALmK0wf60Uyh5zekCrrMYfB5AaZDZluyoLxhcJFRYoxD6AX6Ff9UQJg8n3oZhfutTohxXbER8g0Taitu0zrjDqXTqgKeaIdJD8ADj9c442BHz6thb42G0kqpO9iPsSlEqMInVc6u7ODABVaDYKIQ29lThZ8-zffClHAPgGaidi-3Mx8bFz9-KgBHJFGPXOj2HVwUvt36G0szhLl7guc--EVQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OQVej8A0M3MSZPdNiEE9QVfJKYfF5riuBBqNI5WF6JH1uTkGfjtpnoUK-x2r0ooS1En__NGDPvzc_9nNZ4kjqesz1WL39vqbQx_aK42VcYjTUKXlzftsxVc1wv0QF5nhs1iiDp7rcjCpq1A5lyiUoLSxEdu6P0tZhB8dbcIri-M3VXMHDJHcgj9L4tCj2BcMuFT-lW5y-XWBvIW2fz8oHk-RZ3Y0rA8wgDWm0u7h_9OM3OVS-jddCaGfHqEftuuqKJVQZ7YKUXX4IG6pulMLEUKtUJovgjp9UjN7OWat80f3zDVqObmwCPsIiwEiUtRD7S6zQx4GstRxY5NYlEY-Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P9kdHEwaBiqtvuePfcPl0e3cB3zBaA8MmBQXkvTCcoCRz238wulw5-ZQoNZJVEvoVIWTC7apgUAT-d2F01VNwahDFBNdq6DOrkBqnMwz5Sm60M4TcUfBmK9LVlyZexgJbCWUFfWrBKMjRSsov7QbBtsLQWR_V-tjOhl2WPJKqxsZnv8j4kS_W6SDPIKbfRexm4PvUqOeKZ8itYRf6wSH-XBePNm4wlmbYqNnc7jtkMxiVbBjb9e7anojEbG2wZn6-1GKOn_RKy58ACZH-Hk4nCvaKNfol78wrQdzHYmYPD98gM5EHhUB8PhfTfi23Cuk17BcH5RBJhBWoWrkrXwh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PDT6r0vcpQE7QsQDRFHR4F_fuBGVU6uJV_bTXdh6LunIfpcV8XwwX3ieu9pHAVW1rJQ9vgy1W8xEql3pfhmjcEqykxVxF5jGjxTsUESeb4yCH24gTeG89ciQS1H3AQR3fQPPGezMdvvHuZVZD1mtTF6ZYL3QalZ75n2aleyZr5-Nh3ExrMbDv6agvTm1Kpid4zfclfFtTGKnS4OkjQeLKJYjeRrcKd5Xsm0hkWoWyaYRyQDdQ9Pc4KuJ_e3s2pr5cf9MrRa9MQyoBFCMvRfEgQXYaT-syqyoMLm3XH4f1nLXgbalniePqGIHBjNfErD3os91ESd2IhCvKWRAWW_B5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWXa7fkGSrDsMh-SkvBiICaont8WCx3TK_Hi7sRdMZ8QyfnY4mOsXPReuA24tDfaOEW-eZoXrnDAeAkKPcUZKa2iOQlJQ0ZkfH6jtF-_kmMalTLanPEf4I6X3yK7vAlm-J57yROiTh8jK-dtjQ_byvkdEyHjgPskj4ZqBPEQXcEDck1nlbz8ecRI_cZZ-h0Z4dIK6FY4FV7Qd4bMUGAqn2XA9mu6JO8sfBV3fo3nDP6DESJT6UT0qQ-YE_UV1Mg24CT3BY_Bm4yZZHddYUT4TOt0UTTfCjPBVH2GlxOZedWLBsTmfaRqqy658mR5IcfaHSNPl94TWXM71J018UW1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQot24FpEJYFlR7-7wuFb5SkVr8JqGHYfJxWkO-ZOrtPbCdBb-KfO6cg6mBEECF_w9D3-QylovGe02bhm8dFTjGb_2IQSJpHnK8qrtRwl1cFpLaxOYjUrVkAkxmwWP5YG6h3jADoX8dlmxeqjUcTvjivvtFdmoJ7N4UWaT9YSHxXND2rWmGOIrAl6vMxfMSyYaWT4mLXvOkKy0vbvdGQsI2aWo7hGMb01jeVwr2Ksp8q7JQ0fLfr4L0B3ylWzIar0KfdmvFZxxqrS1OGiF7Qy3Tg4Zjlcak2V9759HBcu0RWmj5qZzcqQQOQHxzxp5neclT6HR1DZD9kDm3JH1ttug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AH08ZlQSf_rcAt5YTag-Hdy_YQNhV-LGoOlwEowwRdEq2Hq6iNqypfHhP6ui27ZB9rcf0p2vsvvbK0iBHpvKPyJPKtXduqW4RVNoRTA-aefpyk-KCrt2FDgHJJII-NHsJLVdDIhnzxLkRnfL2jBPt9fknA99QU9SeOLWYcorER6zbbtTXezJnqxkFpI37gfHOAj1To57T5QnIBDMCBMhA6lpkYtAxgxlv8TbPEhri4g8bw3-L-h6O6wuo1VVJyymMBDYSHbriLCh2-9zqyCDqDh_JRac-YouGKOIIY1BIDgK9XPhPvGH8vYjQ85stWLP68jj8S3PYz8X41nXpLkaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcWXQ9MGL0QUxQpcRY219Er9EbTZ77Kt-aVnWZJqR1cYeTOhzFlp0hL1PSYSgHA6Yr6CRoBGX1SFYcU9CRG3BzejXw8lJ1gO7mvnnvLKGxWTtsKE2v9QCNZ1rF6SD492SBJ-o6NCHgLsNIUU9kjJo6ut472skcabhvOruz6Vj8EDoJz6iwCsCfcT8S3QM-YQvrhz7ZbzQI-jZC_7McFd3rtT-ZLBTIQc1vR5aDLj_8ZHVa1np8R-HR_XCG25JqyoLvFj1bH7Fg8MG1BnFq4ktsABKoP7LScgitKRryc2ED9lcLkZ4uRBXnYCHo6NMEQrYANB4jZAjR8jm7bAmTHBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=CISAY1H-XnoKr32blbKTT9aKXO-H8qVD61HBwSORQOlsmD0s-DHZ3JnpH0trNbStF_13aXUTJiTcRCK6xgqi68PQNZWZFx3gxufCw19JVF-oGEC5kNuJX8JYqLKoOMbHQBvQ4WQR1r5Fqyi-oYCKxSRo91iWevJ_wwZrbytp9O0HrY25zvYJntxyzRgHViEcnTaCBLSUYeamMpMArnSSvD0KwpOuZmz90Wt_zvyxU8uyv_9UddeFzsHWwkJ-4EGgLUnPAyhPrR3gtyQRfoa8_IIXgdMEJ8phbAEZ-nz4laP8OjBKmclHOw7hxakoaGm-Sx4qE0IwwGmD9xKAQBNQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=CISAY1H-XnoKr32blbKTT9aKXO-H8qVD61HBwSORQOlsmD0s-DHZ3JnpH0trNbStF_13aXUTJiTcRCK6xgqi68PQNZWZFx3gxufCw19JVF-oGEC5kNuJX8JYqLKoOMbHQBvQ4WQR1r5Fqyi-oYCKxSRo91iWevJ_wwZrbytp9O0HrY25zvYJntxyzRgHViEcnTaCBLSUYeamMpMArnSSvD0KwpOuZmz90Wt_zvyxU8uyv_9UddeFzsHWwkJ-4EGgLUnPAyhPrR3gtyQRfoa8_IIXgdMEJ8phbAEZ-nz4laP8OjBKmclHOw7hxakoaGm-Sx4qE0IwwGmD9xKAQBNQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1LQW_qMydJAMbckxEfqz9OJf7rlCVrLDRz4LrbOCKdnHmUq-W9oDorliIE1Qtc74cV5tUyRMjPuRwMdfdtuHxonvzINlZ67pBl4G3G4jkJfefo6H_tvRIRQfkJdzoLI44ZQWV8ea8laV46sAfASXH-zNomzyg2VSPQmUspm5cgXGPtfuGQAWUHIcIfRbvMIl4PBadeoda-MAf9c4IXXZYp0b3M3x6OKZqFDZJcgyJEhTJ3z0FJsCC5ItNbCCX0sljaBTGYKQjV-1Jm-2R7lrEUk80-njgPAnrSKO6QfDytTQV7TLTjJ4ZeU_Q75HM9ze_cMkcURHKSGRiSY1JTIZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BaWgLwxaR9mRDX0DzwN0HEsqoui_2LnfRcn6ty7elP4FgyO22JxOEaeG-4srr4WFNp4rEGIrkYOInQyPS-WVeOxZbNYdyVR2c94KzhuFuusGu2s1UB8IyS0_ZtjXy7AwuXjhNOuph_6VTUmEOGSrP3_VoV7zkLenIfTuhDC6y-61S9U4nWPZD_JM9Q2Dktw8RTnJlu9vb68sFpDfQEcjAaws7yV6w-KcMYgkCEABZ-lJbgpuzRyz17fwCDez210xKnsZ_-bDRjoCmfJQewfc_p6CH-mb6YyFzLabn7CRWRlWfqp-mOhIT0QynH-iOajhCbNptfGYxe7gsB_WiyXsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PKOrJxUvHY7wqxr782NJxaieew04gN1jGVSQF1GQiqMenuXdTivApT0IYyzsLJ78SaQlYLahTEvJ3Y7ri4-ftYOXIs6SkVU2HkRq1dpx-KcPntv4fYpNxYeHSItiQy2dJyzuGauNw8jJRke0PLxJYC6EM6vyT6HDyN-YThvIZ7AbDY1V-HAjjPy4O5XRE9vEO3vtqjfsqsP0DTL23hsD4DW9qOblwuHFeMoxnp8sP4FyUX6GHTOGzwkYub6Pq8z_H0aW93vRqOGpdXzCC2j6edINJ7o1ZIdpVCqdlCit_drQ2fXUExf4DVbB9CN2aDjUa_zzy2-6iGYDc2YdjHJlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sp8ll2t9aRZ2PjclUlyVht7Gg84Zz84f2RwqOn5xp7htzXih18EwglWfVbHB9Hw88AYtWB_mAIvFFSEBLzwyRbRnfKqLIQs9pzh6Dfxj5RSg3TjE7x6jKJBfnvMwcWLDmW7sskYWRwlN-EZMFY_XCuGATaRGDId2AMfW-eJq9PgJD9gg8yzitTw7q5OiisUHi-g1uYed4T4lPq2Okmt8DCroIoLy61UtJ46MLxtgENZYgUINLbVa4XxwJaYeckHEoIPsSOX7S4EsHjpDTf3BEgrQ6bXi_dMy02wu-c_qQbb_-fc7hIrfHI_sdsx_OImTXQYyuK6o44IG8TPwS5Yqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cMS50F9Ll-CRAJt04DQ4FZbWXqDISYS9kXGY8ITaTx8J8dkOKsn35TUdetdVE_uerKCJK5mXEacz2v8Mmq_avqxYMguao3QmO_yUUPEfDQ-sXjyUnOj7ZbpEI78nbZctMofnLLxUqGJZz79-SUXilbestrAeJ8MloNGQVB2ai8Ma0hxW9jQ137b6VPgE254chuku4Zpb2fjMhkIhbdlIJRSvLJE34ukJPnIeCKUc7on5edImPrPVFzqdaUqIAKRfWCMTvs6N392nPIPHJwKx4QhND-UI8Foy7mpQHgBdGP7lp6tznu4hFJLMXedcGK6ZuCm5wZ0d2ParpgJ4NyT6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nW1NYp0WVpVaPQOpTJSij2qvNz1P3F1LLCkG03WWM_Q_8czzf_7rTEkj8_h1TgBd5GxcQ13VqMUpc6lMUKtrVWjCRkH1jxZjnjAUOI94UpJcLbtJkhnR5avEtWqS7dZu2znVFVkeYCN--m1s3V6J3W4L0PX-T6qD02hS7V7-sVpxHHFm7LJUtAZuUSvaaM6dJYf2DCvVYa9MpIYheta7I0Jd6UdoFFPo0PEBD5WHwut2a3Pu6_cxoX3qJwfk-Ad8jkpuTYKlBSRK9ZgNkG9zc5LmrTLig1w0vxAxVga7ZWFp3hwb7etwfJGAdFrZ8XORc5aEaU31DpENK7DNE-sThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX7Ii_k3FONLly7mBZsBkepJYiH7Tayuiw9I3W0Q0A_JFJjHlenEsqz_MtHTzNsPTdcXls0p05VovnYUVkj1zBZOh9U2zb0soTiQK5Saf9gmifPVlALXAzkbGbKqLiRa04gsJup2zRokE--NhUkP6LoNEJEaVr6vHle9M0MU7K9dUFOqqBODgb2JeqehGgA_fATiihMW22HvJN9CO3Pc_0-o6wTProseDgGO8Aqvh-9k25i5qtglNCtkxAY_GdEhs71WMFGnBlK9v9GWObD17wMC2F7dvTjU5NwdFZO_nA5KkMAaFFbGNSxI2-ts06dZQMKt1YLWe528GghYA8WgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qKHM9PFSzfkZXpy0ihnu_Lwe2XCVM5HQc3AwfBaEClaWmK8jXPKZlyqFXXnNlbQlFQ23eDmWNvGdwI1rlVXtIDpzphUgYEHCkSRmvhSkkXnb2niAt9G_OBRxpIdYzQLtREC1C69bTTp2NrCiKf6r3IDtjmBbbjvAmSlewKr97PCSQpkgQH1-8Ac1pp2g1G8AlfCxMEz8wLK3S0nLrfoEutBRT8JbpWot5JqLKN6Yd-btBfCALNs19t04snHHId05KjFcHWdThVIbwckxRD-DVeFbBG9KJ24JSXIvQrfPNJBRb1DUKzwqOcEej4prVkNnJjeKMjsYecslQQp7RRarbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUmcz8-3stxlcQPf3k_SPwSjV2vFoL-Oip4meu29PJsClRaoS-KHjFEncrpwHaxwwBsVf6-pTTVygNOKZ7wkwlnlunrABq9x5I9azXRTNkcSYKGZrKARj2xwFEQW9eRdqcnNZhF3WzF0kIMnTz2R9SLl1x674GqoAvuRWHIyyljb-1vr4IsIRqfov4tfIs1HvIfFmRS4DTjzjrn0_Y62z6_L5pMPraF51pGtQ-g5M_is9qMHkx1vhmkVdj0g-tkuT1P5ae5eeXigsznI8kraPAfe0pg4AOfWGvZvWVure-xXmxT_ehaTo38NBEN3vuDFKIbVNyMUD24B9thMnTPAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RDldBQlK1fAhlP1NxtySXii5F3rQYVq7PLc1w-dXIZF2A6Oo_vreRzwsA8FjDh3HpDmViNS35F3_ce0DrfGSJscWg9lPz5gLybA9QJ2SVrxtE4iKW_ZGNf3ZdWaFTJJRDa5kECfN0f2_b5faGWKyf4nv_QvwgcL9_wVrak5UHJnhwCGR3TQjng9DwgEcwSdEUPsUvcttYwCMopl3jD30A_Gx7Mz20NcCS3XmOkba93Pn-ivKO1S70kpRywvchQObjtfo7qrR4NqbDJfSakKUKFzF-vcaEuw-OHzPdSZShgUhNjtlkwKQwwPOXtxf8aRCHDE1PyshAtYPPMT89BOlrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=kfblHR3hp2-93MgmNjDX4cnPFKSe1Urzv_CqsxDNqPuR0Lee943ub-ZB5fMfTnsKug9qSsQ5VEb6b3RBuZk-hMkxVJWwdIGZV7kRksAL8iT1O4HByUIDKCcAuN1y2HpVRKm3czcvbvpUPqUnucNu28W_H34OopCjLq62KSGeDfSI1TxSGY3BP2G2UtgG1CZyXAMhkTzqAAuFVjoZR8BnjEbwT9zOHiNnMP3Cv8rzoWeWzrXTnrobZypCNvvNbpb4yBhk9FweTSLLNyqUCFa5Tn81309yzUHBal7GWTNYL-rGTQcDIzWQBgeMUahhAhN7UrB4EHOodJsR0mJdr3im0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=kfblHR3hp2-93MgmNjDX4cnPFKSe1Urzv_CqsxDNqPuR0Lee943ub-ZB5fMfTnsKug9qSsQ5VEb6b3RBuZk-hMkxVJWwdIGZV7kRksAL8iT1O4HByUIDKCcAuN1y2HpVRKm3czcvbvpUPqUnucNu28W_H34OopCjLq62KSGeDfSI1TxSGY3BP2G2UtgG1CZyXAMhkTzqAAuFVjoZR8BnjEbwT9zOHiNnMP3Cv8rzoWeWzrXTnrobZypCNvvNbpb4yBhk9FweTSLLNyqUCFa5Tn81309yzUHBal7GWTNYL-rGTQcDIzWQBgeMUahhAhN7UrB4EHOodJsR0mJdr3im0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4VSXaIKGJ7Akwc0KGZeHkhUhyyX2AR1lKpd6wRzuCbv8PKq2exvywNu4PecNqgvgrzHI5gx12TIiew5b6TkCXxG7xSX_iAIhIHXcFBfhbpoxtowjJfjBkihQrqNIZ2wpK3xGOTto8CetHIanR43C9Ai6C_F1-aOXTSUZRFvJu4uN_f7WH05-HusnCx5lIxNrSNxWW-gszABGfd7oJL5PqL4lIkf-KnybxtvG1eovSjFctlN9paLziLhFiadC7gfIskP_giBnz7I7vxhvUgJPfh__lLzIPRrlW3e3AKC-rolCfyH1mpEjLEbPPAPvpCD-rAUcWkh98_WwW8QUjb-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=cYR4YmF--VaowYNNS-qEfs5DFVjD6SDC-v1Ilxsrv3Xexc7jFOCb97qv7td50zav4_O7fwSR8dbM6Ppc2n1oenwMHI709n2KAjegMhi5sgapV3GNw5a27GHDRBFSmczgo5rv4_HljDUjCIZ-UhxE_hn_2OQQJ9jUBhhr5H8JDxpCPSR1O7ZYylfOj0FPSF37ZbLQ2p95WuozhqgufUOFN3jQB2iIC0yapxeWbZKk1uKmvLX74fb-MLFSV2aJ9_06eCowfD9Fgl4h9LUSKY_STVlRTIZTfL2iIF-EUyUN058rXi_-wK0t-jo9R-XnORUAjoivOr9GyKVOnHleUZ4v6g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=cYR4YmF--VaowYNNS-qEfs5DFVjD6SDC-v1Ilxsrv3Xexc7jFOCb97qv7td50zav4_O7fwSR8dbM6Ppc2n1oenwMHI709n2KAjegMhi5sgapV3GNw5a27GHDRBFSmczgo5rv4_HljDUjCIZ-UhxE_hn_2OQQJ9jUBhhr5H8JDxpCPSR1O7ZYylfOj0FPSF37ZbLQ2p95WuozhqgufUOFN3jQB2iIC0yapxeWbZKk1uKmvLX74fb-MLFSV2aJ9_06eCowfD9Fgl4h9LUSKY_STVlRTIZTfL2iIF-EUyUN058rXi_-wK0t-jo9R-XnORUAjoivOr9GyKVOnHleUZ4v6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ltqsy5Mj80MKOsh8RNRsoEIwLnZsICYKj9O4gjq-Xdyh_XGQCYAk5wwFLvACD4-9u4HWXdbG-U1jBmbX8qUYVYRUd0WERMxyE5d-C0M19xVVxdZ16ZPzZhs5JW_4HMPErMfaIE8x5r6wx47coNlwR1v_qVH7t4tsahu1Ky1DNygNn6G14KbMGT8wrFjOwoebhHfNU61SLHunaQUQJ1qV7lZ1yUuEbSA9wDb_LNRAwCGqVYpIPKQ2hKeelBJn_EhJ4w4kUpXy8p194eD5MDCO--LiJTfRPvVr5DGv0b06jnMDqrNQzKqDnjRe7unBlmwonjxjHzKGqQeW2ntiqjokYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pgz9xyhpEm_-4IEak_GeU35-h2Vy816CnF7A_H-JIYu-vGQIHmEfP-tovOqcQfPWDnefte4JTTni3Zi8exwYYYYql18WngXLDEqHAME3jVu8yCCkUOCwiiEZHU8lcpOfrMeS--yGQ6uXThB8gUFgRiC50QDG9cYg1iFvIhrX4U8J2DGfXcsa2xXWZKv-pnnXUS0FQSiT7cuJuuHwT6myI66RZO4udD0lQ4oFD5pRILJELlZpfo5eKSEvAOwumJY6iqgRJDI3FftlEtKTinr7zNvm5M7-3tbPRSOuxoSZhu3FuMwYKd_O_lxSOKXm2PAxppdIl0Nj7EjFa_mzXhbepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okgBhGHF3Rdmoix8-biEAknIwpgGc4QSGNTEIQ9_rVQt-XVCenh9-AZNRfc7TkpjKtSV_dOBnamQHqdqQCrX2WzlWDY6Z-mmtyWMLiFe8HRD7t1mYjomyHewCPjfyLEDvByIavPoZTGQbb7FaoKo9k0J0I9HWoybEfMht7_nXbp39pe-P6F2M5sUHe2a8i0erRuipFCXItezQuKcMi21_ek9SAD8RxvHbcd_BoItMOmbqRSjKcrHlSu2EkP-zgnoDzbArLgk9-PChea8VFb-3mbBQOyNWW1LjWa3tHnPvydPsAVl6gF_alQUKS9Ozdrk9w6rZIkkuf_QspezHhv4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-XR8ytqzIPYijD8OJxXHz74G9gkL6ZC4PBHDHdTMGLFcrgrIjdQjXy0HRh-SfbMA21QJPe3bxWuhQ1EDjrSt_2C5y9NNZJ3K87Svkh2xev72hOsiUPVr00j05WAc59queK_a_JNwbo0guWk5DhhY_Awb65ocrePSr2MssMq64-nl89K1EbHWnxaLQoHYauttpdxXWNb4Tr8lEIuqlt7EhkVWjAfxoPc90Odt_T6WJsoSH_Qwkly2eJ7hf7HLsyPbMFrdvxg2kdK_cvZNX-8sOPO3R5kq_SwAPGWw9T929438XxS5c5fgaIaXUURl76frOEMo82atON1H1ztIMgIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=Ef0kPK1_6HbgLGop9qA0-IW2KCoVg-8M7xH-a-Vq4hKvGlDoSZ2jCHhRg2ac1N_jA6vtQmSHk4iUdEHWaTOGG6bNklik-dYCnvPl8JPp0tAlSXe1RQPVqMvMfUx-ojOkDLFdGUCND2DXcK7hHSfa-xM7EtlATrHUceoeOzZNIySBtl4_nx9vHCOp_5WpOFYZG7wXaQenWgSSvgF4fQaK1Gd3XCeeKZtY5RyLrCtuKvvheuM8hmHMVlY8SJdRNOod82PNHVWagUPOkbUhAvLhYdhBje2lRg_mKJ0SS-VTuV6WZqwoyTVssPZxF4LW8uEsYLSLRuJf0WwnDcb3MGLvxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=Ef0kPK1_6HbgLGop9qA0-IW2KCoVg-8M7xH-a-Vq4hKvGlDoSZ2jCHhRg2ac1N_jA6vtQmSHk4iUdEHWaTOGG6bNklik-dYCnvPl8JPp0tAlSXe1RQPVqMvMfUx-ojOkDLFdGUCND2DXcK7hHSfa-xM7EtlATrHUceoeOzZNIySBtl4_nx9vHCOp_5WpOFYZG7wXaQenWgSSvgF4fQaK1Gd3XCeeKZtY5RyLrCtuKvvheuM8hmHMVlY8SJdRNOod82PNHVWagUPOkbUhAvLhYdhBje2lRg_mKJ0SS-VTuV6WZqwoyTVssPZxF4LW8uEsYLSLRuJf0WwnDcb3MGLvxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qh6azyiG9T8XvpKptts9ak1UgzALEqZ1zKiRfutn9V72AKhlEyQuuaDZrpRFOMvj4iJjKM_yqzwyRbDIarB4FCaACmy8ZBJG7Jwd-R_m2Y3KuwyY4EPSsMh-kDUeHKdtR6YSnQApiKfJNonUV8ZyI5oucgLp3Lobhyc_uA_0TldwAoThuZgeYxLwwU1BoywcmYzUrEValyaKbU46vb0Jc_cjXPocRONct_4qsFJQ1PPCyiHP3v4Q0snFXvCDLPNSHLUMpDPfd7Pi5SqrWyzSbQhCB2wtvL5eQK0fHWoq1TY5LYKz8xvjtcZw9Fg6P4kI_H0YDFykfOAOV6VohfuWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=XGqkXBPjpO9r1cnAjT55xrPSaQ_AkQApoAXDbL1JbhV8ITGmdEtd311FXKrA97UOOwbdF0UPFRaKhFXfxHOh_K4Bv-lFpFpsGR7sG7QgJm20MyyvunFF2OUD_8vp2DUXCEtdRbZpduzQjveKvzHHD6DcRwTz2VhnAxY5GdP5Lj6V7tYS9hIQNU9OXZmZB3y0eG6ymNODaaqpgic1QP_eAi9dtHiud_9epioHQTfQCqpAnIBb1OLxMwaRBZ3ahUgGNtGColzNllxL8XkOngMjIpG6hgWE-UUoxhufiORRzju7NLmCPioCvscg2tT0NURWmWHQqcXPhPXsPKqmcbxEMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=XGqkXBPjpO9r1cnAjT55xrPSaQ_AkQApoAXDbL1JbhV8ITGmdEtd311FXKrA97UOOwbdF0UPFRaKhFXfxHOh_K4Bv-lFpFpsGR7sG7QgJm20MyyvunFF2OUD_8vp2DUXCEtdRbZpduzQjveKvzHHD6DcRwTz2VhnAxY5GdP5Lj6V7tYS9hIQNU9OXZmZB3y0eG6ymNODaaqpgic1QP_eAi9dtHiud_9epioHQTfQCqpAnIBb1OLxMwaRBZ3ahUgGNtGColzNllxL8XkOngMjIpG6hgWE-UUoxhufiORRzju7NLmCPioCvscg2tT0NURWmWHQqcXPhPXsPKqmcbxEMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYo1aQT8oAIUJE5d6Rkiarz6JludNSroEuYD_4tW2WAV2ITZY8RqfVpb1ULDubEpXVkUUfVPN20tnUZfVjHuD7pYG6RyMxL19vGjoa2boOVmDZA3HMGJJQhC3EBzgmBLDPpKlh9tErsF2fQ21M3u9Txi_pGJ4Xj3GJs6K2l9J8-U33-Xm0VoFFYVopJgATEZ4LzJ47OcO9eUX7jRJpfgxOf-asDSThlkvHdexOhzZY2pG8UKDgoarMVEBK_Dzoo7oO6C8KniZ22qqgvOlSf-T3cH5Wdbj990w-fDuD62McGOCjTF7BJuv6fi16L3nTx1cUh0Q7-mahcU25sUuXgVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=gl-IuzlM9KQzAIIIR7xl9uVp3DBN-sWZYY_ljiEZhcfzJvO_dcDBClBZW1WP-FWrN7mLQPSOUWMqNnlzVvjBUvxNpIrf21iGR7eo8Sh2aS7lJ0l55765ojbln1XunWm3vq-SRNCikyOE7Zm6d9P4CFA24UnVu1-72kfRYvhPAFv6cZWJyobMuHGQ1tcJUV06Y225Saqt82yxF9ircMW_zTGEXfjxs0aGkVUsRhYLiYa8Jq9eMcfuekmj5LeUy8kQ6hr1bzVskV1MLq3IWsrjk87Z4zUePEw0sO_XcLm5jAvjhs_TLS7KnbgLTGhX87uiU-7__QXpqbF9zd0o9WVTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=gl-IuzlM9KQzAIIIR7xl9uVp3DBN-sWZYY_ljiEZhcfzJvO_dcDBClBZW1WP-FWrN7mLQPSOUWMqNnlzVvjBUvxNpIrf21iGR7eo8Sh2aS7lJ0l55765ojbln1XunWm3vq-SRNCikyOE7Zm6d9P4CFA24UnVu1-72kfRYvhPAFv6cZWJyobMuHGQ1tcJUV06Y225Saqt82yxF9ircMW_zTGEXfjxs0aGkVUsRhYLiYa8Jq9eMcfuekmj5LeUy8kQ6hr1bzVskV1MLq3IWsrjk87Z4zUePEw0sO_XcLm5jAvjhs_TLS7KnbgLTGhX87uiU-7__QXpqbF9zd0o9WVTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gj4Aa_ZKHQSV_ffkvVH6cymKqkGoiizvWIKaejyu7a5lt_wIH_AnrT7eIQSS2pyqIqFqfeIdtnPNduBTy0iHtB1WYKdj_7HLZLPOz9rHxN82w4v6iQIqLfDrfgGjfiC8yb3AZi83pH3fnG89X6fjS5yidhrdkbCmOAuhfcTxzrKgq91WzCyBNWecfCyKxIOOasQxeEclOZTtApP-FmGiy5OgZ2-LTRvVE8uKsIVPxFwJ2_-V4czKtv-N4d9cinvfDdKpIJqkogRA6bOAEAVldOLWwtybIYUPMWpvEfKZtC2bhv-Kzi7rXXd-kOhg9yccbv8jCTPnEauSfir0oqb7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UWfc-Y8r2oa3sDuE7o218USKSxo8S1o5sptArqlUnxo6Zx-7U_WhUcEHSRfiExzuxKm2_HOfm35Z8Y8ISvV-_YquJukIXY7YRwwInVWyf8Bja1wG9kyRIqtWdCJqR5_YJeyR0laFFNnMhS5aB0V55mtTRBe7AsTNH-VpY62T1_elvN9z1iOwjlIgQDAMg3suqrYWLcWobOCNEuYX1aMLWPBSnVwzfv4rsW_K22hMTuLZ_fFdF69YSoe6uChmAbV2jrPgWYzM7nyxtz99H-f5gtiEqJdCbIt1zppxmYZe3pH848wMGtgQ6ejNR-fxuN_wW9gNW6SHdho2rqHlf_YwTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IHLzsyCM9LLCZgf1aSu_pFQI8SLXmkBp6vwksDAJiUwJ5ACxBi-usJgwl8GgM9xaZwMHjPbZ3S8A7E8eEQoKXvhYnDK0WMRp95kFxMKeq_WHfAa_XBciPqRNgN33_7aF22SDKsqQ5l7v2VA0vE0dPV7yi2JRNeU7xgNRZ3zcEO_-eaarxCPhkBFEjlFMyzTci-Jcv0X7AK4lFmCdtgyxn-9PKtHijOmHLVrElbpcg10WCATBcYu1HvigDPNN8xHnW2dl5uhF7pl9aYBcEvoERa2LDrfD_nLwXDVUt6qnlO1An1D5ST1vBUZjs4BQLwODFDbSHtyJx1CdKsFB4ZA-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=mvlw3-m01MWngNac9N24TBCyotU-Z198gKTXcte3BMKrIAKk1c3dZKLAYEGHtEaItWM43VjolV5C9wXscfbsQFnyT2TDceFXHq6HHOa4gTqxz2aR_yhx4-WylrUtdBSpb_XDWdgvaGFW_lvV3_gpD2BQVDqpFxPWixrMwfyvFEoaXP2fI7zfqh6oMe-Rfe4i4muwVcaeRV120m-N3R-G3BVa_QJz0vz8RgcC33dwtcYbgoCBrmfonHgubaXhoET_UTW2U1igTMHisH3Wc9l-SM1rwfraqaUbilEIM_-qPYT4Oq1JizAP-K3FvTPpqG3Cslf7-TWQUf0keiL02CMKow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=mvlw3-m01MWngNac9N24TBCyotU-Z198gKTXcte3BMKrIAKk1c3dZKLAYEGHtEaItWM43VjolV5C9wXscfbsQFnyT2TDceFXHq6HHOa4gTqxz2aR_yhx4-WylrUtdBSpb_XDWdgvaGFW_lvV3_gpD2BQVDqpFxPWixrMwfyvFEoaXP2fI7zfqh6oMe-Rfe4i4muwVcaeRV120m-N3R-G3BVa_QJz0vz8RgcC33dwtcYbgoCBrmfonHgubaXhoET_UTW2U1igTMHisH3Wc9l-SM1rwfraqaUbilEIM_-qPYT4Oq1JizAP-K3FvTPpqG3Cslf7-TWQUf0keiL02CMKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/suw5QNvhqnIffS869Irt9xjyN5gb1oTnR1u4C3MIWTiNOSUKjlQsDT_PdNeyWypXS-jBv_T2sZBUAme3j_6BTiZ1UFC-LeAShmKPS0Oe3eYwN3Cthg9imrx9nuJj7XGVlW8cRYbXVX0xwcICX5Km7IdVofctmiJCyaQ51ZkIuHjpV-5EZXCFtSzELlTPLNs_OwdoHsOnoz4NfConsM04m5PhAwk4MoWyu7ggrQRytMRxfs5rTbcJYgPyw5OIwb6A3WLA8OhMYB0BtzOmJ3LybeePAe2RNl3iWOozvDaS2uw4LKLwNRDkmsjNASYH1xUH0f0_kElDyn2czrjP_QKkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aCEQpYumHM14sOkSsjRYimXvstypOiTR5Bk63xWKZx56UaCx_Y6mZv7yLRdMSWLVe0Aib8E5_LIATGeedD_7fRO2HWKBIT5paevhszX9_OaxSmHv4Tj7SIFjCFCcvrPGhmbm3xIq1N_GaSvht3a7c46Ma-HcPPDASLquDFyVoZzO_hIILjYzMYVL4JwRDswdQCjbzJnuMfxyfNsbho3myoj47LP57OApfdxLqiGB-iTZy2l9KESGRCFffQuQ-MBu8-4T4hcl_G14zfKOZIBl2otGdrr8m9rJGLo0mdpzKkN5ZKUoCqwglTgcm3k3VaQobgo7_HzUkWOu-Bl1GfmCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=sfIgCVQHr8P877fp-9pEV4h0tDrgMiCSmfMv5Rmtxm0yTSldw6pZDuYp1-ndPyUr9PiwiQPsPkgSuaW2TbyHM6oDW2OweLMMb8d6X7aTfmqy46ML1G0ecBIjq9Spu4GA63KitASAdce_Jyo6TX95ajtpplpW12KYDapsNBsGeyPPkNUE6eHxNzO6qoZVxMuKVVM_m0wec8erBrXLRhN_isD67PdKiiyE42yhyUReh37keHR5bgQfzUqRBgZoixmhsHwLSrFWEkU5BK1ma4T5PxZsFWXbVRoib_Q2yTrPe_8VZORtU3OR42kXO53whC4rsJcMFXfT0n54UdMuFqPjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=sfIgCVQHr8P877fp-9pEV4h0tDrgMiCSmfMv5Rmtxm0yTSldw6pZDuYp1-ndPyUr9PiwiQPsPkgSuaW2TbyHM6oDW2OweLMMb8d6X7aTfmqy46ML1G0ecBIjq9Spu4GA63KitASAdce_Jyo6TX95ajtpplpW12KYDapsNBsGeyPPkNUE6eHxNzO6qoZVxMuKVVM_m0wec8erBrXLRhN_isD67PdKiiyE42yhyUReh37keHR5bgQfzUqRBgZoixmhsHwLSrFWEkU5BK1ma4T5PxZsFWXbVRoib_Q2yTrPe_8VZORtU3OR42kXO53whC4rsJcMFXfT0n54UdMuFqPjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=iBqrFD7WJE0oVE8_UXK72-k0KRolZgST45gDJ_cx465FpuXWNK4L7z8FAFIMDApXQzYFmHqtMl_yhGrBUnWC-R5PwEKKtQPElb7eSR3CuQubUzp3xWgf9U_lh_c8jo8oVefB3XTaCMSTM4BiQRI0OyVSlt8TaKUgSiVxs75b76ggAZx-vQr9RjVKatpeutuU7Xc4FPsyp4ndexeEJaRe6koG4l6dPwMdJr4iXrxO4gDfEhmyFgAnK9QjjnT9YZ6zr0QVPNZnDou18_ZfmWfBYh8I3qJjdpuKwyp3aFr20f0wfCpX1K4Q_v-mD9GbybGVYGKQEbnadC_yHY4adwV6VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=iBqrFD7WJE0oVE8_UXK72-k0KRolZgST45gDJ_cx465FpuXWNK4L7z8FAFIMDApXQzYFmHqtMl_yhGrBUnWC-R5PwEKKtQPElb7eSR3CuQubUzp3xWgf9U_lh_c8jo8oVefB3XTaCMSTM4BiQRI0OyVSlt8TaKUgSiVxs75b76ggAZx-vQr9RjVKatpeutuU7Xc4FPsyp4ndexeEJaRe6koG4l6dPwMdJr4iXrxO4gDfEhmyFgAnK9QjjnT9YZ6zr0QVPNZnDou18_ZfmWfBYh8I3qJjdpuKwyp3aFr20f0wfCpX1K4Q_v-mD9GbybGVYGKQEbnadC_yHY4adwV6VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=ImNJpG7fzHrOvo1IL7pfShDSWNsd-fPJVpvaTrwU3_kHizVVukhO8R6f5g1Yk9KQR_PPcVH__Wih9Mn9naDfMRWq9I44URDeJkeVPqtooMp_lRHydgpKQG9DaZp0uZ4ZQxeyRDjdaZj5gozBjUGaJKtWnTwgt4rqSyi4huSImfrGqAnBNiPAgfZHfMwrjGCVYEAs00NPyq-6TxAH3umzH8CRMzuoezIbSrlnnqi3xr5qJlcSeqQhafx3M0GOLbIo6P8_L2K2dHf2LUqsPGoZ5oOkMT9yrTWIHJxFysG95w4UWE5yW0VbFfurdC4kF7Qstw48n40fyfExq684iwIxqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=ImNJpG7fzHrOvo1IL7pfShDSWNsd-fPJVpvaTrwU3_kHizVVukhO8R6f5g1Yk9KQR_PPcVH__Wih9Mn9naDfMRWq9I44URDeJkeVPqtooMp_lRHydgpKQG9DaZp0uZ4ZQxeyRDjdaZj5gozBjUGaJKtWnTwgt4rqSyi4huSImfrGqAnBNiPAgfZHfMwrjGCVYEAs00NPyq-6TxAH3umzH8CRMzuoezIbSrlnnqi3xr5qJlcSeqQhafx3M0GOLbIo6P8_L2K2dHf2LUqsPGoZ5oOkMT9yrTWIHJxFysG95w4UWE5yW0VbFfurdC4kF7Qstw48n40fyfExq684iwIxqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5zaQl5owP7yA3sR9feUYjt2br58JH8gW-PKkTXiqkt9QU01JcM37116QDUaJbKByI0Ru2NHl-U7Cpj3-0H8pMVaFjRSgQBL_Tsxv36j2nHddLLZvOdEODKv_rkhAmNKXe9GnyTnIye-KyOC5SFE2vPncfU3eyLJ0lLwzyjAncWZV_VWQUbeMCY9Wur9lvo5_zEmu_Cy1rVEbi01N-3hHtZEYC3OZC4eS04vPwUIenRFlK3WZwUrAI15-hft3RRF2E0uieVw6tf6hYSS4fXlBjpQF7WFh6pmnShoaw3AkLIuycPzKv9y67VrR3W1SS49c02JntEKAAJ-6ZkmIvMT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgROUmOy6LuTYp4sPgribONGLoIzzRQKMH-PPYy48D3H1e01q-KDwxWNvl_xfWY2WfoH1bQA3fcijAOCnZAr_SfgwKtb0CNSd-72C2B1XgiEIwzhJbeN0AIswzRTSIUe4FXiX4XW2rs3KU5iLebQZbdd2jfO2D2cDEyAJJ541jXaa9ZM5K7ZgAfEpQQ5g1XDSq57j67Fu6-7I04RkZ-WKrHldG3dUVVtvU9-0ha4EIEbGgx7255eLkxm3zsrNrrqh5Hm-6buBVPHKreyPJlZ53tSn4ToTfYtpt8Ym-B-hmnNniKnVeYDCl7uY2rRc_U19e9WKM0IdgyiAkxBvjFj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLZOyEQOFPtmyAlF4RNHGEK9teoIiPJTfSFUb2lKEMJtcGMEMKCPkmZk_CiCVQXRZlsRkUUZvEjBUpP1ohDyon_-9M6N41jgYjDYBOB3BI4bXhL2_0u6QBJgxn_THNnc7JZ7me_QwtJAw0Vq71mk3yYK3TnCRw8R8UuZtU5KQqCmb0ZPLnkrJo7sBvLFvEtdOGfDAIlSoTXxkqfXyAOqQmXmqSyHe_0z3bC2C5JgYbwNO8cZv4-_S84MUslmhEfi9KfhWadX4I5_UmURyFlEnQC9K8ogyVVg9slzjm_vekeFXiB70AUcACk9fvHUbYC1J0zsKgnH3v3S2aHJAza5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiAsdvNmWfYeMUDhvEL4QrDXry6xHla7qzVSi77njTZH2YGzC9trrK61q_WbafbM-_oAFjRT5DdQ4RFFK3MaoEwC-aAwarr2pP8zdIfiiWi8VB8u_Ap8Ngk5U0Yq-_9ducA7w9Rkm0i6YMMeewUMfCapqsEssrgJ-u8MxX1l0ABYRHXtkzccVXHmvbTnnvykxSqiSKRLhdy_LyQ4HGcISdUuNiwa2XArK90aStNBY11Dw9y23xmkiI0PGmg4xpEM_eyVcRAoujT5amNKNYdCW86BgPo_FTqWxQ9FQPhhHoyj8P7uxXLEM65hGWz_C8z4gvEExWrZDkn_Mw_QTrKuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZn3A1bamyDkT6dUlHFEE-9M7EZIW4zB7ryd-Q_niALE6Mkuxdc4LwjZicKuxhQ59Rp96tbfEM8R8WGAYyRIBnMTHKStn-5dBWfJkd-NAJvDNGEZiXCd_toDuG3oDAsguavLOG-iwBXPjeyRG-2EX1q-fu_pzJPSp6m3wUTPkip-JbzSANLimqdvuzpD0yQ4Dyf8SiOxJKReL6WSU9tL4vOqXTNJVKQLDZvPWpddPocnBQCy_ZlAo8lk1sYajM9HwtMQUOOkCdDWyDidgPlTVkm2B57_kSYdQ7B6pJUXRWHCl036CDuwIc_AfKQp91K3Dlfskz_7y9SvlR7Lqds4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W25to7GTDGzED3jLVYF6xe9NVpACxsgDLvI4EUse6fn8w8OarvbMLVCtHkrn3ZTnUVkCQvGyIiN6-XqHIfTYM5nRfLCbJGSfD3OMTom9uBjjKM5CR4ZPXk18OOCEVDiOylL9jnjBmHyyNhIMdW1ULLMIwsCu7MSK82RH7SjYH8aC-S3Wz8jwVoGUYlMO1r6ogX_yz-9rQ9F2hVgyoMvhAE2dpVXkLNsfXeJwNw5ZIauGZd2uoTnATe2rfDPn6Qo8KHaBdXc95_yswJDZNeZ_AniLOU2Q9YCLnIPCIP61Lh_bsN4lSgcHHRv-X6v8OH7wwvyK-aaGKD7Y13FsnbOGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neeaw9XsVeUdkAlS7YKme9m7j_goeb4ip4LnDHYE3hthxwgFgUA7C2ZvlSl3dAclvDWf3k82ktP7BgD4jR-fiOkunuJ4kf2Q3CJCPr8SqDKyHVhNNZNwFEE7AMj1FE5n0kGxs2CtcHeOJdjYMn22XH5xI8IqfF2rhg8-jYEOT8qX60VYFv37AaQ0LRJmWo_Bzr0CNVEFS1w0nGVuwc-M21pKWvugw5DuHS01Aj4-taQGidXMTVu4WjbqvPLUYF8NTcWAn_QwnltpMxcfOOsyfeqQ4-ZSptDW41N0S598yCH3idye3J_bZTNcWzyaHdlztsyzhzAml7IK4T2bRf90Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=O8sg4joCh4zJ45tF9QSXbrxL9KqcF_NmUvPTJoUwMNCoyAZ0LacLhCyl6WEJ-Wo1-XmOsrMD0fNPtIYudt079nrrPYyuphoeDB2FrvLPhSRS2BpqUvkOcj-E4sdcNHuo0_iSctIOvsGRi_2L_oKy3n__AmZvcUstqjqDegpLFId1IIpgNPb5RGTct-TsykfjrutO43PAOR6Wt1-CgVWZREbril78n0jOJq_5ro5LBzeDf7dGB_WqcIj528PfO1LJtEerikwf9dnrIFWp5gV-o6ouK7G_zZt4EwatPL6xMMUWNwh8un4rRROOeb9gNOjfN1EaXwljZ6Vvw6CcPAznmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=O8sg4joCh4zJ45tF9QSXbrxL9KqcF_NmUvPTJoUwMNCoyAZ0LacLhCyl6WEJ-Wo1-XmOsrMD0fNPtIYudt079nrrPYyuphoeDB2FrvLPhSRS2BpqUvkOcj-E4sdcNHuo0_iSctIOvsGRi_2L_oKy3n__AmZvcUstqjqDegpLFId1IIpgNPb5RGTct-TsykfjrutO43PAOR6Wt1-CgVWZREbril78n0jOJq_5ro5LBzeDf7dGB_WqcIj528PfO1LJtEerikwf9dnrIFWp5gV-o6ouK7G_zZt4EwatPL6xMMUWNwh8un4rRROOeb9gNOjfN1EaXwljZ6Vvw6CcPAznmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XiA5HORaInG8_Fb47SdxC9yOwA8iBvckTwY-TLrowpBJKQbRdB3FiZYysU6BoCn1KrMJXITvry0A_zyAIXtd2wdUtSkgL7JpJb_Y8moPpeN9fNwb7KTgqUes2ODXTiH32fjV9ZE9VeIM3Qp44OYPG-DczvXhU9LVETOlHkc6mmTIxoYfo_f_TvxQC4lafqSIegxhdef2iTYaa1m3AoCDOt9AcurLUP3PP7_ZxN8BQojJ6cysK6lbgrAzG-y9wv-tFFFCO8n-DNzc8vXg3VDItBIfPZ60pHE0xxEv5rDakOZJe11DVfGwUqZfkNhd0HREk657blU78fPfRZBkTDnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6K2DZAKPft_x1q5HaK4sSiZGgZqFIkM5j9rrNWie0eB_Yng3tC7bSNlLahYbLLcX59cZCXqZff1W29KNmVirO2IWE_5cwWNvaZaBF-ntop919LiMh9iGY53vfvcoaK7yzNExsBVoO3we7OUtdVXRuvlB8ICe_ky2JTEMfTdnXpU65cC9kOyZNxva3Ou9l_zd64urzOoDwDHxomoDwYk6cqGUssyiLRyjtArKbxBWWLLxHU50owdER8P529hPgCnqxlKaTQbr9BviiB55F-jcnwVNjO_rbUZtmOdAhB-p82-WQFlpANgKoai9kU81qRkk1bXZ1ISqJ9Yt5VScDpQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nynsc5Zzk71jkkqsXpWZ7SILX7mUmmjix4eXEr4iRTSz2EhIRwZbRBuwWX88XTOCVwkVq7NtcFsGn7zvS80yhdArn0RD9-imqBmnzdlutovuDt1g9zC2dbxlXjQJhoS0cnLJM1M2_G0iWKDdkh7gg9QXT52p1_95ZJsDSyTRhEx90wEx18fj_KGAhuUmjkvfvTAs8etiJIglVuhgKmC9K_BlmqFBkKwGcQIQpjsAXZ6iCfHVGFPlZA-vqQ-0X_dbOHkx5KBPQeCE3KMrleSRuerGURWQY1OtIoxGR8-KFhuD8Gc1MLQhAYVKndGIAWhn-RdcI71WmTv1xofhtXOLEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=VD1FreYIwCXN3BweKh6tH1l5-fjcIXHrBudsVOnLs0VTHGG0QzI1_lgfiAQgExfWYzRNd2rtTP7y3IwuLp6lQGgWu23VGetEy0FaFzDGng_IWz9tWko3Wtggv9awtwM9pLzkx6mWHD0D3oPvfSvTb5pncfQXG8fY3GHAtzkgG-ZzcEGRqL6fHWVmVdHx2DkgzvTHH9RWm06lDt9nVot5cK-XVIf3ycq3IjEiTHkUq8E_cxOkCHUxM2isfT9GWVIYiBYsvjj0u0_0Zdy20qlI79_iHFbhCXdUci5a3wwfEQw_O-0WnnFuKKoA0sseS6WeLs5XNpI5W5wwsSUzkoK04g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=VD1FreYIwCXN3BweKh6tH1l5-fjcIXHrBudsVOnLs0VTHGG0QzI1_lgfiAQgExfWYzRNd2rtTP7y3IwuLp6lQGgWu23VGetEy0FaFzDGng_IWz9tWko3Wtggv9awtwM9pLzkx6mWHD0D3oPvfSvTb5pncfQXG8fY3GHAtzkgG-ZzcEGRqL6fHWVmVdHx2DkgzvTHH9RWm06lDt9nVot5cK-XVIf3ycq3IjEiTHkUq8E_cxOkCHUxM2isfT9GWVIYiBYsvjj0u0_0Zdy20qlI79_iHFbhCXdUci5a3wwfEQw_O-0WnnFuKKoA0sseS6WeLs5XNpI5W5wwsSUzkoK04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gO8D_0qhUlsSBLK7TvtlYNQ5yVImVdL1HKHlM6go_X1wwIZs5eq_sdaVmD-9Stn86hTl9IhgJjbkjs2Wt2wQhaULxSAhAy14OQrEivEx37_ObSNC2n8rdEKoi_PsDfXtN3quT5Bv5Lhyv9AHA6oYb4ABZCm3dD0OYjnEqxH98IfTe1eu_QJ6WBxLHOOCmApHZA0YZ_Eg4iq32swsfqpcasNxC0pLfqIqMp89XueM639cNpgsVdpGnfD1cRo5u2Mb2su4eEtLml7W3HsdxIqfhCbeXNLMmR8N4iP9kIaNG0aB7ROZOzKL-KGSPocvMik8_qbnGtnedgZ4pCz3wnbXzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X6fwx2whTxtU7TK3MK8b82e-hPDnMvEgYEJIVac0xdxMee-FBna8K1obG9Q5wQtZsz_6Uhk24kzKfdLLUF-9-CcsW8SEE69umWidWMePnr4EUNZ4ZSEuIRwpH_0kN8ROaREouDwvVvXforYPikP-8Ii7C4NfGqUNW6g3h4wc1aVli5VQP-WwMBHKauK_IFOhbtn0ZGLRzUbVCY765w2D35uGPCHZtPDWawO5Amc3ERUMX5JKxlJpC8s8Zkno3yLMcfAbZnQxIWyRTG0uBw_DyYNNhdwuRmNl9tJuFHhuanEVAjuqRVECo93nWe1ni495sBMVgXHX9HDgBhqKlhTQIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aJglGPs1L3wMZ8OMKAAYUt9FiSU6BVq48Z4YMcHBEx0mkQYPAID5a7_3kAsZpzIt_3_i4OQJfOvk4f5bPnJCp3iOaDvwbjqVWzXv_1bzUS_9lpxqRVBA6eZcA6BVlNydBIxbAYbIs0wB4o4Ya0ZAGoa7acfOm9bvmH6Dl-vA6mRs7Y6n8N2RqvOBvBt6rY3yjHnoFsPgM-bSvnf-UTolQCwY4aUQxTBFZJcxxXKVMh_PKNkYkcpXLPk-w6hKJULWprcb81JtbRjzioekfpHTRLnS34_ay8so9SlyzC5OYvrw-6sRs2A_HT3yNA7EWztaiQpjlFGRresWoWZnwcFyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VGj43iOhCCGxci8jfCSNDhrQS46Ox9zQ1L2EAZRSkHddaqu08FXxoTZOq6pPXtflFULZSQr6iM6nZXl_4mLIx6_vR2p2QMLal16ZlJ5WuWAuTJa3mppOPUrs5vmKUEYDg6N-F5u0UK9h95lGSbX9hG3wHYv2IXjtEynfnZ71booOGvv5SXPuc-qeZ7kanHcGw_clIg7PJDiZMl1ADhmnxyiaf--_7hTGKRePTtdmOmAs050MFvLPl_vZNq10Et2MEPMuzg8GPX-lZU4hXXELGHHSnjGwM11maNVQJsspbGQnBv4dp1MpofU-Qm2yIYK9txatEBFd6W_zpH0KcUt4Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=r8SZcgmM0eF1c8GxYPxhdijRIVcPsLgNUh8tDqt_if7QmFlsA6Ryi9FmC3xiI_HoiHV4jhFj4V3HUWwxdHudY0Yf6CzhqYu_E05DbLAa2CCVCm35fyFQMQgX7MSYk3GhOdt0heycIw6f263WbrI5wETvMrgsmcTzzV4R7KOJYuglA5xx0nuxGqlx_RELY5Emfq-XCB7ExCwC2DU02oTzQAAYgSgtnBeY4BV4xPiIkWjxh7SeZ2EgEfYpzdGN1bLj4KY7jWNbyffAx4fq5-bIC3ap0YeEI2LqMrOyLmdqRHfdiwe_qnuY5niPZT48Y9ph343qO2ZnD2dUSBjo64ncZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=r8SZcgmM0eF1c8GxYPxhdijRIVcPsLgNUh8tDqt_if7QmFlsA6Ryi9FmC3xiI_HoiHV4jhFj4V3HUWwxdHudY0Yf6CzhqYu_E05DbLAa2CCVCm35fyFQMQgX7MSYk3GhOdt0heycIw6f263WbrI5wETvMrgsmcTzzV4R7KOJYuglA5xx0nuxGqlx_RELY5Emfq-XCB7ExCwC2DU02oTzQAAYgSgtnBeY4BV4xPiIkWjxh7SeZ2EgEfYpzdGN1bLj4KY7jWNbyffAx4fq5-bIC3ap0YeEI2LqMrOyLmdqRHfdiwe_qnuY5niPZT48Y9ph343qO2ZnD2dUSBjo64ncZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LPY8grOa2EXDSK96Z0-jy82Ic2f99XpFArjoPOZOs4vDWvT0z-xSP5KOOi-1XrJgcYicZdXs8w4JrD0mrm5otAb-iR-5ppqLBmLap-0Ygz41ZQssbfCh5EezhoWqA7lSYXjUouGbyt4JRfA-EZXl209xNY_58UBK5HGQM0cW9sKvR3pGJO7PohoJlfWce95SOXzEFA6m16ARApYdmPMVJ77zcrF1B02lm9sWXXbNeT7E6Pv8Im_Hv9HBxYQIpxSaagZhyDeS_TnocvwZjvBHWkaoTkoMiYAXQlQjg0V5Lfb4wJ1FMdjpvxepkU5XQyjb-MSw6FrmmFSNkmz_fSuNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aj9Tx-zrtNXtOa7PzrkguL3tdONgA6z4po-_z8PJhQ5st2RBpkhVzSFzBUNOs18CVoj3Q_oczPF5aE_Qb9EH6OGykQSxW6X5vTbUylSl1uzOrBy40gEg-uPxXmS5ToOe9zCbaEITAerxOlvfvo5rXPsEvG6gOPIrjcedG6y9b8IG3Ds5b9F4pBVYGwXIeA_NkINsSfcnXU1KT3FKrQE51AtAiGDHkyvTogs2-zm_AOVJwTjBr9y6ekpRki-YfR-IXrKP1fZ25avwfdTip8hQROZz-9cjyx-JxAgL3w_1PuylOe1rWjhBge-FEVScoAb-eelfnD3yDkFpnF5NWGWwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XKt8cv1_VhRlbKzPpguIgHsgka8vRSpX2U56LOFAwzy-zJ_4-Qr9Wi_wG7GbXvl3DUOBApLKDbDVmnlv5JdN6scABnRuM5i-SSVoxBzREAtLVlY1fCwVu-pjXjiHwzPUFd7onnYOSOXITnTreXtwyWDWvnlG3aY8tJR6PH6uJhGUOw9f88TozV5kofteJceHN2n-U_VVCRejCqYPjO1NCBHJo6OQj4E8XEte9gFC2hyj0mLbkEE8rNKbdI3W-ePaVVeePwdC44EjhVPwTzGK3xkSKFsmnrgtKQof-ug464zxfKM7qs_vkxm7Svl_5SEFcfY-6Uu8GZ4DQP-qQ3GhcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NhPwcHPmjwgFhP697Cu_Nwv_aRrmXVrR5nwdY_9UsRSTxvuZmOBSJiOssGVEoFTDWK_3xDswwoy3x4fQiUFkScorMfY7WiPDOfJuofosueIOkpS8d9VCUDMQXKmcDeci85ZD6cnSL7InSmi47grpYf0CM4T8BWcuqErEVUj9z65DZVgiPdndeyljHYmqxUWEB4g6OGNNKoibBCYx9XTEF3KdF6NjpCA1mdi6owWvmxzZJEelsCJo0IX5ZfkmG-Mz_SEq9azOF_OBSDW-vvT1DuQY4QKLSk6EnODbuuXCkEQgCaPvwCNsuJf0m6KAB7DlXV0hxL3X-IQQgT5iHE-dsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LvFuM_HAhdp-rv7XHBQx75lbph2taqi2m5JPwqcXIaKWiw3Pgs76F_hi_1lyIoKaeEtk82VB8dcMbA0sYw3-1UeMdwP6jyGjlxTjzaNyTV_dbthSuzXflQMBWP7Xzkl3U5hdhVqsWC12bPHwkz8qd5p9hmo8UY3FBI5q2qEsCrVb42hqy3n0roL7Wf5vdEPERPRoEiCDhZkg-MFyc_QybnO_zw1iFRQDhp7ZHeuUGy8Pkam_GLe5MfZRvWs5GZj8hQDUyvygERrktofSvKPvNlnLVMRcJ5u0CePTlSG30cYhJ1EDR8npk5hbOhL4CN4Vvd8ovNK8QPxbcRRqOef2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TtdF08tnMHJr-1OoUowTfIgBj0woeS2zrk8IRn0O1bR1yFNVcWdbP8pyeljQHHL9-xDYMruU2-0HpbPfKoNDkjPEvU0hVgxP-_uGZrQqrx4lKYpnch0E1nDPEJk603SmOSzgID1hylcFISYAsabkKLUJkMHiMdC_1auS7QSgtbfZv2e60TW8kemZALkNU39zTjmW8vkJSGbafkHvHS785ntLKWY3uLNVijARSU-lAopjfPEH4lW04xDzBcndH4qtdbtqTaJF_7r2rno-uXsEWm9puugmtjmF5bYbNcCe4Y1V5f_dKYz1y-DfIzXsk-1sNEVv3sxraBpYlXErfYlong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KDrk0FMt48blxeaYlEhzOmulNwF9s-Semck68eQqS4bAsHwG8wvScAfoCFFOGxY4gZVyzTk4nxImNyMtHcqxz_Jl7u3KYx_l3egPHCHn8W7_sZ-3s1ZNj-Y2pw9pxUU7PtDxrP6J8K1lZnc3-BEZVXbfQiloRZ_TmBOEVtgWRSHF8q0CzDGg1WLjEI3CBhD4-oQWq5pfUT5sHWY5Te3xZDjQE_zv6x4K5UoQnwehVtSTcQlm7QauWMQzF6EIdT0IKtF6imJVtBTAQZC4Fiu7v4RV7-bmquVtX-gzFJAe9-5RheCQaqdo4J-bXeTOxTxfHT563y1hKxrWwgrcnNk2DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kt_VeNEXPiTvsirijHTMEfmd1WjS5E9wGzNfdS38zWjtsKcIKjVLykjDKxnVCNLaZsvAU5tNp1Qf-xXz19xzFx0LS8DaAVSvA_WT9FsyXmPP_C77uCF8pqyNRk7KPsYzWXkOhbVNgUeGiF_L4yrmuyRmRRbsGV9csE7e51-YQHQlnRwknnp4MQzOXkwegnLUhgLbxSdWF8OmJnxdQsOg2eUGgkO5jyeuE4U_VZqbpoy3aBLx5Mn8hrMVArjVtNn89ROKMZqBtdSzepmIHr3-hcn18Jd_fZxe8KyQVk28r0tMB7sscGKclZB1VoQYSa1V_KqYNK4KN8l-31va-VBn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j80b5NFOwswf6xWt3pT6T4-xFYwtuo617ML2sZQkrtwmIbjSJcdxYz-rlxozv6QkbSIXpaHr7GRW4-j_64sdFeQ-cC7mMCmmL6n3Rac1njI2KTvpOZeRDW7QqpDfJaJQmORkbLf1pYJ0k29hmfRWI32sRol96HvSm5lqOemt240SJYj_m8wFG3oExurQbDT8F_QMhF-EtDfyapy-xxVBY2Ec3Io7cjuA6dtW4bACL5qhP6Ra_ITjohr5_lPfLq5h5_8cNFOepbnZEbqzUG9NW4qTA3EbaAcLJa8KY8nDjrUQgTLmsiPflxOQU43dfjpBgH5klZDK9tEtv7y72wzLbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HSTjyMunnAmUJLXwSfwRarJb0YRofqFhKWH9uHT0JbmOL5JW9Ey263XkOdeRsfE3b05vlNppeeH7QOVDcpgKbW8kzdIC3-kWVkDJFLCxRBrjkA4JVg63_WSGDFw3NSmpWCHFqNtBrCjTtF91tqRG3wkGucB0ZEwmqvCN7Zcdm6zcbjT49e_eAMM5TpSa62ipjjOqhpxWS75ZUa98RpCkB3ro0WfHbTWF12xd-HOashSZdMeyKnUpD8iP3voiaRYK_cJODmHX-BNyTLYll5r-yySLFs0eLuoregx4vmKH_PMOaUmTQ4SmN2e_9DQTnyE1KTNl903y0uay4iaMehMFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AJxt4uCtE_vAWvIEA0qQ7bW4BD_BaKrYxgFIowkHisTPZGoSwU3DwLQI8mLf88PecnyBFMBKMUGcEEy8QmHEG_zjIr7bB0i1iHRdG9TtA2OR_P-vNnRB4ss1k_yGYd8tOPQFLz6n28ri7tHuagjHLJI3IkriDvwKW59PNuL6gYjlCn6_2jZV06vPTv-0IEJThENPf-O28-A_hJtEHxDdf3YqYafoo83Pt3N0EDD4uu29_B2lDwcldUG6O8YY1lAFWLtomX56N8SL50xZrdI8ucD8rh6dbucZWvUuL6FPceT6wH9XYMZt5PhbhsfWv0533SahDAVMkbduqCp9OZpzFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=akUW5yvSlvY8S4KMthEAx6x1UVx6v2OKgO5ZLvVwbWa2UReFpswRvm4L-uZRjRSuMdoAZDySLH3Je5dRUpGxgMprRzSBPOjGhi4h0ZSPIDPhPFAzl5D7gv80WH1o5sUWcq6pm69cT3NFV0g18U7Gq9mei060Nq_KSH5QmZYdXgGLcVh5gWFurKsmyVwSjRGAvDBXGPq8Wgb2d82-L3RBikP4bxY6wod4cFMwALrwFlxgntSMpR51zflWTGfJOoMj5oPN3TnM51L4O1VkwYkkwHeCVnmYc0ILmgL06a2wD55Y6kj7PGD_3bWQJX6ocLnEzzcZSim58ZxC2k4sgb53Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=akUW5yvSlvY8S4KMthEAx6x1UVx6v2OKgO5ZLvVwbWa2UReFpswRvm4L-uZRjRSuMdoAZDySLH3Je5dRUpGxgMprRzSBPOjGhi4h0ZSPIDPhPFAzl5D7gv80WH1o5sUWcq6pm69cT3NFV0g18U7Gq9mei060Nq_KSH5QmZYdXgGLcVh5gWFurKsmyVwSjRGAvDBXGPq8Wgb2d82-L3RBikP4bxY6wod4cFMwALrwFlxgntSMpR51zflWTGfJOoMj5oPN3TnM51L4O1VkwYkkwHeCVnmYc0ILmgL06a2wD55Y6kj7PGD_3bWQJX6ocLnEzzcZSim58ZxC2k4sgb53Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AwIZe4TCUybgLxlOKHmw8acaV_TJx1B3mXqHczzXueD0Xv0Ye7Z5CYBKZvn0aZ8NRAfRKtPVWahLc2jq-oR1I_s6XQDlN7iwKYVnwrzboL3fzXEFP4mKmrQf4Jx49-FTBxdnTK5EMf5A75rkj9W7qBOfz4oOMeD0FXDzNGD_ejWDq1fSmTlvrMApt7VEwA2VSO6VV9cizaOPmPAxzRFdeP27REA1HfD1kuqWQ88z6Qhcfn5YUViHG6VhuKjzIRjDIxFTZNzoBFhW9a-un1hg4PrI_7Ol9S2tRqaY9gSnlgBs3prCk2moNwKa2OIUmb9EQdtocvFT9vuGsF7axUS0-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_CsOGSIIwJM4qXWEx4X5DC9ouFPHPIpJozeFXmSWjma4J_U_fO5-ha_a5PqkDOICx2kogjV_VMPOY2QchnQdZmCvFhOPkadQJnYHCJbCoYRSG-dXV3BoQp18pW3u1RAVjOFW22-QgfaUXtSmVVBWoK4iRAYGZojYDdI1L1-3AMjJ_LWrZJTVYDQU0NBZ4qn7KRL0hSUX1sLkAJdeoLRMkpVtIrhAdqFQZOH0f6qJYmTSQhI2qh-ajdJPt4YGlqaIxQx9VL_twvBeWEeBIsydYvger0kmd1Pz9rElJwWTGcYcef_JkOovLs2Iug_4_8SYYs1ycf1udepdlDCHDuJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOlWOwfd1LsP41n91XgPjY0kDdW79bYkYdfxBdsGb3Rx1oiuoUaJq4vYjwIyB3Q57Sx3hpBJHwI-fPMbZLi2wW2H8pp0MtAXEwqXvXjbBkNUVWW3MUjddMCIlZDonX06EJ9vvKWhGftJuE-w1STE5FojW6DcN8QLaLowAosMe1qAP2ptvOPikqmorOPa-LHOgoXzNUmtvVvypAuXTwDpkQUlLOyUqR_GhwSA2HorNLKRmjTa_Zm0nrIOaziCGUJ7cMGCd0Wpvx3D06nvUDTCM77n7BgJYlIgWGw0bc_2pEVeZ4pcHjxs9tYcSErt8I7lM4r47igiWpyLtNFWOKLNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=iTyYzaM3kg607A5xu7psX6nE1vc8kbyTJIbFKBYKnlDauNlrATek7IMxLLTwkUB5abFkKqYUkoVRHpwD9GYX9ZMppEYx2oYgqDXtxTgAZ6-nLwzMqU7ing7W8eUP9MX-gJlfJWVrKfr0radqlrLC9qLh5soQXnKrwYobwgAG4YiUgidLc8QdaTnfyL8fuHEhFqezBeI9szcGVhPPvaMQ2wKGyPLr_s8QlHckdVOB_JmQmwgClCilz88o1Fuyrt2koLfLNHOc4bqgYa3GbHtSQViSmkh6XL46JjSTQ5NF0ZwN31jPBWCeUjgJP7Dg1h7JqDftk-JFA241OxxIuT1c3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=iTyYzaM3kg607A5xu7psX6nE1vc8kbyTJIbFKBYKnlDauNlrATek7IMxLLTwkUB5abFkKqYUkoVRHpwD9GYX9ZMppEYx2oYgqDXtxTgAZ6-nLwzMqU7ing7W8eUP9MX-gJlfJWVrKfr0radqlrLC9qLh5soQXnKrwYobwgAG4YiUgidLc8QdaTnfyL8fuHEhFqezBeI9szcGVhPPvaMQ2wKGyPLr_s8QlHckdVOB_JmQmwgClCilz88o1Fuyrt2koLfLNHOc4bqgYa3GbHtSQViSmkh6XL46JjSTQ5NF0ZwN31jPBWCeUjgJP7Dg1h7JqDftk-JFA241OxxIuT1c3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=uy50AvGFnVTQbfQMB2DxgusPNn3UVD97zEAx3Euq8NkXpemqlMzWu_PrakytFx_VW1xnrAymzoi6bZfvV7Ceq2CDEb5evmkU_GRRvPPJ_X4BeiBsK2Y0FZ_VejKB90IDE2TMm66TGbCeeQklp97WcarZX9pFTS9DUyI_dmtUOP7BFPXZ3kQoZoCD4pY4KLRUdCVpupKfblZGCXDmc-wzDgSJghtDeyFMAgxusTxWzdE9d0LL6KObEGIVfVYt3OLaVEysx3MPul-1an4RfDkjhhDmHEhObxb_h3JXrIojkoU3I_07ZDT7BCi6Vs10y9IJRE96oOEodQhEmdlxw34Lmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=uy50AvGFnVTQbfQMB2DxgusPNn3UVD97zEAx3Euq8NkXpemqlMzWu_PrakytFx_VW1xnrAymzoi6bZfvV7Ceq2CDEb5evmkU_GRRvPPJ_X4BeiBsK2Y0FZ_VejKB90IDE2TMm66TGbCeeQklp97WcarZX9pFTS9DUyI_dmtUOP7BFPXZ3kQoZoCD4pY4KLRUdCVpupKfblZGCXDmc-wzDgSJghtDeyFMAgxusTxWzdE9d0LL6KObEGIVfVYt3OLaVEysx3MPul-1an4RfDkjhhDmHEhObxb_h3JXrIojkoU3I_07ZDT7BCi6Vs10y9IJRE96oOEodQhEmdlxw34Lmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpYAWKiRKyC5wM5mZJN_zvGOgMRYzBHpIsnZ1eDcJboFyxFXNaB3gHeRzH5OWFblSjDRPO0ZynVqBriRp7B_FdEY67sH_t3dLb4t6Rr9aHx36_e7zg0IyDfWVix78rt_UhdUpgAC57xgBkV1NJA3wmaE8f1MpN7Ro5mmz06pyx8fCvRjM_Azg37lpqkP-vdR4zUpPi-npMbM5nKj-XdX4xFuhWfWAcZLojT78o_1MqFC2GUHuBtZ-1yb9IgvhBGEz3Kth-xq000apFTsGQKoaSsCLtJCEuViZPnueAx8zl7Y2DxK1IDo5vA679bbKU_Y96OAkC-DyyedlBc1cxg6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOrxNc1yHbqJLuoSzZa-hw6kwufHGLgyNM0MaFi41lpHKm-AnQHcsLGQRAnhag_20MayMvV_tZ1HRTIxHTjL2v842arLuGl88e1pSiYrPHtZPh_DNpprqSjuBDTuMLIpF3exb8YwOeniGcE3kz8CUR1eTO7G-y9fY6vFtrhppPdVR6bmVVRqnT4F83kGtVdmD-5uZ3DyF4zB3InInusFav-oVUywFUlWDEYG0bjgMIvdWTXsxZEOL7lWfE41TshYPv8e3lPe-ScYWAPJlaGDsn3R5N_B9NGXUeeOfmK5wbEDICXyW6AS2XZQM-oWTY1d_0nTXpRH5BlGkrRfji-f8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=LHCZa0v8eAhaWZnP3U5dmNqZBspDo39NOuhliELfpOjUwV9HaKn607b4YS01Z-vkd_Xq2Avc-0dRea-yxRd4CZS-X2INfvvwwsMAml39zGKrC1Qln3rXxMwvE4NTTmICB8YzMS2aK47KMivvsXr4rNoVrOhiTktB3Q9yhqPpHsuHCeJ-n5liXP5u6cFGc4l1fQZSP8AjMmd_Ah68J3Qnggevj8CQy3o2p9hCOTD5k11fevMmR18LTO2Vk-nbBkR7xs5d5-nw2oG1pOtx6W7MIVj7hnC0Rnu90_le8lRj2k2alv5YgOi9GPlbDGg2RyyucZSbOHgXNoc4No6graY1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=LHCZa0v8eAhaWZnP3U5dmNqZBspDo39NOuhliELfpOjUwV9HaKn607b4YS01Z-vkd_Xq2Avc-0dRea-yxRd4CZS-X2INfvvwwsMAml39zGKrC1Qln3rXxMwvE4NTTmICB8YzMS2aK47KMivvsXr4rNoVrOhiTktB3Q9yhqPpHsuHCeJ-n5liXP5u6cFGc4l1fQZSP8AjMmd_Ah68J3Qnggevj8CQy3o2p9hCOTD5k11fevMmR18LTO2Vk-nbBkR7xs5d5-nw2oG1pOtx6W7MIVj7hnC0Rnu90_le8lRj2k2alv5YgOi9GPlbDGg2RyyucZSbOHgXNoc4No6graY1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=U2Re0oZeTcgs4sEf3tF-nGCPdzLugxyjN0opQ_omBbP-f1IIp07xNBmCa1xnZXw9ZRIKqlY7Jbxr29VO16uDDbA-FaJC-wJBmlyIiliPk3lKdVga7cFxfY3IerZ53Y4bSf49PfFRSTtEdFWv6s2UHa5-XLNnJHHARtq7uWSl5AMJ5E8NhxsgD0U5sdY8Z4j8dakeYU-xopZapp0UKApYeCIOzGJl_cnhfOiv0gub4q-aZ8xyQ92o0VUKYT5MdAnPSCQmST8p3atBxNTr8HS79ezQYOdKlMv9dOqGcsamZyKsUSBWNSU1IHUtsaEUc0WdwHI_Gw4cZtWGuOV_Cha20g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=U2Re0oZeTcgs4sEf3tF-nGCPdzLugxyjN0opQ_omBbP-f1IIp07xNBmCa1xnZXw9ZRIKqlY7Jbxr29VO16uDDbA-FaJC-wJBmlyIiliPk3lKdVga7cFxfY3IerZ53Y4bSf49PfFRSTtEdFWv6s2UHa5-XLNnJHHARtq7uWSl5AMJ5E8NhxsgD0U5sdY8Z4j8dakeYU-xopZapp0UKApYeCIOzGJl_cnhfOiv0gub4q-aZ8xyQ92o0VUKYT5MdAnPSCQmST8p3atBxNTr8HS79ezQYOdKlMv9dOqGcsamZyKsUSBWNSU1IHUtsaEUc0WdwHI_Gw4cZtWGuOV_Cha20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=ESAuYIZCJMh2BZz7v5epvnxM3ts-kryBkCAlgchxPvBhq0nLJifgON-02svKQepXbDxSCaa5rJebJjo6a70auYSwRktW1rd10ho5XGxPUfSqnT09eKRyNklGMLl5q8budoJhG06Dvnf8Tx0c-8zpJJvHT5l3MQDhoPLfE7SXTpAaLk0JETQmJw9R7pagbnLRSNN6VXtLHVNJcoHzzOmwl4DGr0T4HJ9aaEkdKjmhsQAThRPQG9Pw24U_ANdab9Fbv4i-yIjbMVQOjuEV5C8L5sTnrsDTLOtqFWHBXUzoDMmlQmRwukllLI65A3gghWCoKWtjeHBL__16Lj7K29MY0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=ESAuYIZCJMh2BZz7v5epvnxM3ts-kryBkCAlgchxPvBhq0nLJifgON-02svKQepXbDxSCaa5rJebJjo6a70auYSwRktW1rd10ho5XGxPUfSqnT09eKRyNklGMLl5q8budoJhG06Dvnf8Tx0c-8zpJJvHT5l3MQDhoPLfE7SXTpAaLk0JETQmJw9R7pagbnLRSNN6VXtLHVNJcoHzzOmwl4DGr0T4HJ9aaEkdKjmhsQAThRPQG9Pw24U_ANdab9Fbv4i-yIjbMVQOjuEV5C8L5sTnrsDTLOtqFWHBXUzoDMmlQmRwukllLI65A3gghWCoKWtjeHBL__16Lj7K29MY0oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Et49nILsOdsizceVetVQ8f6BUc7BYE-vjA7typCw9-KrCgB3aPdMwOO3Upg85Wysj0hwe6kuHKkE61KKlWGJuQta_PWbY8TCaSQ0Vf4QBpaxI_3uhX4wyP4OH08lMRLpAAeiILCpf6gcX4WP0WN2SZIkCfjXgusiVBbHjM9uQ9VZ1HvI9hRXXiv8biAFSv0zlnrV5l-N4cTdUTuoNYto-cocLP5HeEvKAnRSuvei-BrwlIk-UAyfnLweoY7EQ7v4Tga-TaMO9HGgL-qWVOkyZ13VA6RIew01kDDj4fsB027KgsA57gDc-eWotxSyOK0F3L2WK3BvtH9NizLRWvAtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMjEoIPlqUCVhz98Pkxkif-InaKJflkuQL5-_bL9sLTjCLBS_0RzMSjy5wnSEhD8VSGBx3QLEqawM_kO-f0XzauI2FN8DMpNd2ktactRDMEn2YHpSCcs3wZO7XOKT2MOzDTvpdh3CMglvdK_5wARvs2elks68waxQd1OwMrzysodItqLLYIIZdlAIG1l5ab0NCWEr_mOYRE_giNVlCW7PVXlPfoCaoAzM2AFGDWu4R5ZOHCJei8aKPgCQo1SqoBoONyeT0MTTt09fXniMkh_zB1p-KHJYP1KvPF2aI4TV7A_A897qgo5FuvTzvgspJ9zhDFzMxvkYjY_ZrkXkMF0DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=Pbuq1tcUd8__E2wPqpSKx4KAEH7TLAdrikoXsJsWIyx99AUYz1i0RvrDxpooqauWqikhFWqIV6ijVnMX4LkuSf3zojnP91QjeRCBq2FQy3meVtkrgi0z3gyU_ukMKYuiG0j8d1CsTIMAx7NcvoHOjKKh1urFfl0vthqY1-_U3zZYmYknT8JZhJvQg-6P5xuLIqwFthWyMIBJytzyQI3EnJ03UZBWrGlIzzn2Oymrp0Vw-q3RZhnaLuX-o4oX3sd36XixuyaA7GdANrmA9M9vu2gaSYttb0l20c-zbv4pcjoE8Wl9TtbjDCvKQSQ2rP0cqJgGx2yvWVTndAUcple5hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=Pbuq1tcUd8__E2wPqpSKx4KAEH7TLAdrikoXsJsWIyx99AUYz1i0RvrDxpooqauWqikhFWqIV6ijVnMX4LkuSf3zojnP91QjeRCBq2FQy3meVtkrgi0z3gyU_ukMKYuiG0j8d1CsTIMAx7NcvoHOjKKh1urFfl0vthqY1-_U3zZYmYknT8JZhJvQg-6P5xuLIqwFthWyMIBJytzyQI3EnJ03UZBWrGlIzzn2Oymrp0Vw-q3RZhnaLuX-o4oX3sd36XixuyaA7GdANrmA9M9vu2gaSYttb0l20c-zbv4pcjoE8Wl9TtbjDCvKQSQ2rP0cqJgGx2yvWVTndAUcple5hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TwAaEgLOWrvIXDzskM7IqBhkY3Viq_Ph13imnfpGHqMq5KH1DI_dbO7mAnJQg3FzeRUVGzmuE9lHEV3hL1Szi5k2YvQL4KbhbcXunEoz6ahymcMFaI55eFujLrsZFtSiKpIUxYAstwHiF3El7smKfD1ukqLkHKsfneZcdDYrcNHF0RoQuio8NlFGnAsWxg65zwvQeGcoic58ZKNSutQFgQa2_0j8mWN16WPWT5ddaC0Rq3fVAfdyxZQJmI87qQd0Kdgz-Ol0LrKg86VrFDdFJAyWyn3A7IUr3Jnt8AiHhwXYffC3yjyIcgwpyAX7lA7zvBBU73rxD8erfXIM6Ldi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QbAgbLA2Kim2OfgU0-2swNNQOS6j6kYOGmIoohlvS7zjWuhZrjZR8MC6vGdqryZpozFC9_s7RVcQhraaEunJJs_XdR2h2henx2Dx719oKZokCgPhmWXY-FoDJ7OgAEhYlpPoq1R0nFy_odF1ikiO4C0TG9cfDYoAcpKJ-TpxsmVWKo9KZVVRwJQ0PzcM4vizOj1EDenzM2kyTdOcNk6ZiHyNpbIRy2B3aLKGq8pR5Ed52uEQOkLmEbUtpEKiu5i8xY6kHNgcpqE1aK1k0nBdBemxcD3pgYfIk99JmRwUZAuaz-_15eDqTVUroFrZJ87IDAPjOtb_bAXZg2j81rscJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLY62LuUsQnwAqeEL6CaUYtJ6_wPHA3LNiDybZVTG8GoXPgFwRjfewfIr2MTSdjozQgUzDJFBVKbti9K2a2uTNRJ58RuUSLoUBgdGnxx9PLHajg5lNEx3tj86S8xJFryJQwiH_SPkkeLB9PjitCvNx33i2GqkVQTdo_zBF2qlpUQM3Cqipb_P--LWU9VCRZ8WZLO1T9aW8ZXzGAjcZ5X-8HrpqTzue9qftDptS0ZHPUIkXAJdfxLz3OmSxMnVsM9h2rWaaxWD-DNSVvBJCbm1ebWGA-Dd9swKnMzH8N5sAgE5qF1gpdmKPFG6RFzzV-X3q94n8wuDk2t1iTDMy56-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DLxd-6ae2m1RsO_f-ip4NP7A1aPNh2OetsWrYBzZYtI8K-MU5F2o5d6KHJhv52NeXsd_9rSx6SLk1dLm3ekhitiiblKoBAO_j95pHZqisO8JYyT259XDX-AEy_lJLyYUpg8jjgg04DQSRPi8Os3UJfESz_ACi4KqQSJbdEJjMcEU2YwU7-UlT9rOosGEXbSiAQAjJw0fFRXTxywHmyrDRXhQ_4p9K0SbZlXT7YuXL_kAOZqt2zYcv8ielcNRaA_sa9SgEyFwK8S-EVm5Vh1KZdC1w153iQkvahyBLAdGfAmkFC6JFrBfxNzIL2c28fDjNx4oJEmXhmn3GSG6evbVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z3_VDGEjjN-9PY0zicoZN0iNRGoD-e-aAYTHkRFIroVkNs9hON4ZbK9IkIYizGhFkXjQdlkyIfyJV9ak0SekYGz_mv3m6UsJTSxDYslVq0-osmYdwaWPWIO0cMxkSx3uYBQsTzWQ-YsqTE6isJah-yABbQDFqiUoHwSmgE7_yM6dRuTghMEZiotA9Nv8h6pxHDvsUxY3Zg9-DoIdLA8XV54dzZELxIqtjvxA2Yyc9qDon7AYUF3mCw64TxfTRK0G4v_523kgibT4Urko9cTKbpmeq-19hmBswkFsyM9cg0hhkfs98FW2_YpqFaMpmfFxBVZvRrT8KyZRv7qEZyJ5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-XF3A-UbsgyU2HTHkSazXnGRCN3s9jroZbY_EMiQxCFu5zkHdrobwQH9AvMOcFsZvX8H1AHNRpG2gENXqx5moCYUyZUzpGggRxHqAayumelPa_zTa3bSrIJJoRvbAx3JcBSZeorD6PyZ-9gWm_rYxNuHZJ14KiiLfw2BtQLfCsCvzdCqA1crbpwdpDwINblbdHGtK_sFSX_QLY2a1aRExQtKdpBI9fsDMk1C_UK8HVFyA9HfeiZcZqHCMhLCORw8GBRHuQJGzxZI6MYKGItysCc8nUoqXbB5h3ryWqj5J2CFEfflDfbU53UXSwv8znlbZz2AduSkpScgsBhiU-AsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z1EA3j5LmiirhdxJ1qa6Tth8djiJjpcnF2jE2xBkmZYNk2rNfJaGrOiLmNpx00MBJVQcfJRANU_drX0Kwc5_isTw3L5OrCVzLNzHlDDqlrQgLAlJtc-BV1wE77GFC_jMQ6XsSKpAuFtqg8dHIjjRcjykbnsor_g83bDh5zshOurxOsa8uXHf4BRTAfhvt7X59SRBNnJf6V4MZbyn61kzro1lLTqJg3zMzWp8Bsst8hJPvEkLlS9TuJmz0gqvLcnQ8JoK7ThUkTAN2PhYJnBy511XE_OQ0gnkK5iq7AXeIo0mkqlzMFur0MZ95chDWNWrb33Emmx06-5UvOnKM08ngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ewlhg1szcXpEX8l-t89Q4O_xXkRttwXz9QqpKBKXibS1kD1Z-VQLQHZhEAO2YDyXh4Uo3Uc_azol8RFgNrP2GTZfD3-vwsJiZYpvzH5QqSRnABhPwQg-lDujPctQ_mkov0-W5cBN2DQxq2rOpfNBQdSvood84dopiGw2HvHFesMzatbUlDFhgaAjg2CuWLv3sqoxbNUpMRzqsSoPY6H7b2LAhKnfER8L9xfBIG1gex3sEJ297bk0BYcFi_TmgtSw9zPYeqUNj2JLeTijCg0LfQQ1zPLJBMAuLGmtSOZ8uXk7p_FR7L7WedwHyr2HGlIGpg-g-dwVyDyJgoEAnLDQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SHyZyNZ9FEqnTw7S8eTpUoLq5wczipVFzCbK8tNLLPeUmcmqMDcDvPOLPUi9M-xJuRNCizcZd00B3gMX7hCtgq-6XEFcedmtWUe5s4B7QEUwrU2lpVdBGD78tsdGVXYR7Yg2OfrHLDnY2wdlHenG0Tpg074E7QiXWjZFINRLJLTyr64kM_LV8ERKexRJ6aqbaV8NG0mumOXODeWmVG6ZRkcwqBbtpB_qX0s0UjPjWF-nsMxobeU28MBgQjnSEztJIRwNmUa9aEKDuioOlzfTVgFd8rxOaCi2o_pWcWS88KMALGehdDsWaFfMwNNhsP_6Iq-_2TnhuzL73b-IQ1XQZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jn7SdEfRp796LCjLKVSSnDqdSV7LkekxE6UgZl-5pFGEQuSeRyx4SZniW9dpv30kp1GfmiD8-yi513dKwIE1XGRQD84g2UEQ_mDxU6t_DKeViPyOFH_Qa7pBuXMtYhICu0BBR3LbYyq0MH6NuHpLNutOp5ycVTMzyjIcGDI72e2lFR7M3VaSweHM-YP-Db5tzf1ayu0gIsqgAtcyixNViugq25gh09whFSNOEtTaFBOOjhPCyfSRgKZYmyVi3Z9qQ_dnIhM5sGb221YwQn_AtOFZs5i3nWc2oza1b9cpLp4-NA2vrMK-CaF1ZkZ2UAEwhxudckmvx_t1VF7j-cWrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Aaceynz02yagN-K82Tg-dIEDiP68hVBB88jd1TeElRj7jrXwkw9tRuI2otfjf5DJE8qBRHd7nu6fq0J2ZH0QHwtBeb3D6Tjo8KCib9poFQBjpXxTKRQRBgjaYGiJ-9rtv5RaNyGm8YlV7g7yHjFHf_hIagJB3vHH7B5v-Q_6_EOYSmh3ruZKzUWwJEQYrNqNDa5yvOXhy6JblUKLE_3pqPVp2u4nUS-wr87tyFuaDPHIpZ4cKKw6cYqsFEbwkNWTYbQG3Bg26XldDBMXLqoWBfXeligBEqfX_ooVVZwlX-Mtst57KI5O63eIAicL4c0LDwLeDi8sAmvkCktjiUrN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Aaceynz02yagN-K82Tg-dIEDiP68hVBB88jd1TeElRj7jrXwkw9tRuI2otfjf5DJE8qBRHd7nu6fq0J2ZH0QHwtBeb3D6Tjo8KCib9poFQBjpXxTKRQRBgjaYGiJ-9rtv5RaNyGm8YlV7g7yHjFHf_hIagJB3vHH7B5v-Q_6_EOYSmh3ruZKzUWwJEQYrNqNDa5yvOXhy6JblUKLE_3pqPVp2u4nUS-wr87tyFuaDPHIpZ4cKKw6cYqsFEbwkNWTYbQG3Bg26XldDBMXLqoWBfXeligBEqfX_ooVVZwlX-Mtst57KI5O63eIAicL4c0LDwLeDi8sAmvkCktjiUrN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YfYn_iXpXtQBKJOcjnQ04oYBeLHnnM-iJ8xmb7-9VODW4cYw2WdWuKXNl6tamRgSedpWIGlDdYN8uXSLzKvYLFQy_GaJtURp6UXJCh_ERApiY7oQ5lVxRh4oQrZDha6D_0h9Bv_2cWYs0VQEXvpLRZsgNqUtb63Ktaf65cUi6LE6uXOegaKQHtJdoAzlCkIEEagjI5qiCin67AnhTcY4pSjWNg4TA9l_hkiZBwABkOaoq9XX27Lc7_wwvM5cTT1SPuydIKmRiAMpATp534CFB7e512n_Lrf2o90ItcBsPtwgC25FoKF5NQm_evO0rCfbmkNA1KLlqhkM0xipjMRpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
