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
<img src="https://cdn1.telesco.pe/file/eAM6DklpOCM8PPFt5g9z-ovhvFPsz9x1zeUtH3Xbu_EJOzcV8h1Y4abSFtEw6nJMUFxtbFsk6BxCZsw6P87DV5TgGzkRqhZ7P9cTGCDDp2zVKV7jxVFiAZVSYpXWBO896czBBzcejhnzgecWYvStr_o7qDBTtwXBrDYCdymLBL332jlEk-F3Gbm20sXUlk0H-cwzIFBIUMqqoqbHAoxRXvoOqpu95I-1pK5j_Trvinxz68QVHGxetsIuFO4KftlgGGfcMkjJQi8SKsJ4hc7tR5_YV4ktV62fDrToMDqjOd0vF-lspGwmKkYjpo-tp3D9E1Wxb5o4VWd0NJQFdSZoRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfJXSxA9dZfjeTEZJmOQgwqTQawlm_Nng6qcj9mj12HIOEdQlO62EQaCE1mayLw4y4F4nZZ6tB5Kuf_F_-oGQ6mV79L7XHXXAlXmpfS7nKKfngddAzJZuwC5jVh6k0lra65bMLuH9ePfjvWvXcaBnjvRj-DwhdXhp-lf77HqS0Mq97BUZMVDs3aXcTFvoo6lkb0L8vfTKhJ0DE3MJw23KCk1UDgNNNmwtwPuNVfE7DujQteu5TZqmRKx0ygh6tLqP2UlsQgi9HL1QBtkzuU0ERW1tpb5qhHAsmsutApxA5jKWO8p5jyfysHlQA9LafcrdIQQnUl7VHjVv0h79djc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fU7-dagNe5g1QqsHoJdWNZGEo3_zaZ4_1acBqQ3IRVaQuHP69x3lSGrGQz5LE-D-hgZYys7dF3eFLRtfoRd2s22Bi_UXxNftj_J0wP_u74FhnSWexjhf55I3Tqz3ePH66zw5257hndZFRpqkUS3gdtNV2M3y2n0ftZjG9VSW9JZugxLRpuVzmuR5wZ8YkzHWNxb53-_9SVOdJB0u8TpeLsF_3XEuTDI0TQL47h4b75ZZGez0QvLoDw92IDwVuUXYO54Gs6OV4ADpg2LILmOt9bAZCf11mXazmULTF9XJuhCTOsY2-EphcoJ4u_0b8Lb0Astg-TqClxaieWm4l63GLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=vPN25wCEuFccXDd4r821UUAt-eTxA2Awv5pfEMiS2UPXdGAgRg-muCGyGvQy23Ln4Pvu_F2KrXsLJAo7XooKaRyOKnvBQv-WcKCmCTQvkw2wT1xzqXODhMwKBFJe-8uSouiHDaaRc76_aPgJbKmgpP1u6O1E3ovKkSI1Vm1PsUJnSjmEyGazgB120pVNe3gwgZcZLcQ7iuOJ2IZia-PP-2GHThgGIMxY3tVFOnCUhvytOarQs1w1PJ7WGpU2pV56xgAdY3yWreocgh5zelamzOEi_BIj3kOVZdE6azdRpBOlcCW7YcJbbdwq0mV122FS6EYPZLx0iHdIKMRU-v5F5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=vPN25wCEuFccXDd4r821UUAt-eTxA2Awv5pfEMiS2UPXdGAgRg-muCGyGvQy23Ln4Pvu_F2KrXsLJAo7XooKaRyOKnvBQv-WcKCmCTQvkw2wT1xzqXODhMwKBFJe-8uSouiHDaaRc76_aPgJbKmgpP1u6O1E3ovKkSI1Vm1PsUJnSjmEyGazgB120pVNe3gwgZcZLcQ7iuOJ2IZia-PP-2GHThgGIMxY3tVFOnCUhvytOarQs1w1PJ7WGpU2pV56xgAdY3yWreocgh5zelamzOEi_BIj3kOVZdE6azdRpBOlcCW7YcJbbdwq0mV122FS6EYPZLx0iHdIKMRU-v5F5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVcHMMoNiC0m_-cuZ8B071jq6YRt_Tq8UvbL-ZA1ZURDOGDYJPO6Tjk29DKAHgoSrgiLbQPfMYqIjV7M-dGw2_JlcPWO6NPysqOKDwG3mgiGm22wfAd3WkML3YQPvFeIIqFvYhQi6yyW87ylUM4kf5bHgameYcnvyW9GiexO2qLk2v69aUYrvgqnG9UZMHss5ASh0DRBDX3m88CRX4X0cvYtJhVuh--8X4zElBdv0y9j1Ie2xHXZh88FK8lS2fW1ODaRsF2K3BJVXijm_z67s7f6X5DUYi2RdWbu1jksiAX_4D4jGpsNPMiQ-OVI2NwT0piaKiXEWnjICKXybGYWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J3dj77td7xKW30ZV_33DTMBEeVrFHbn4io7wWBDP5e1TdXxNI8qDfOnTRM6hjE8U5A4kFPr5fs4_kRK-gkQUFgrQxjgux6M_JxC6SLl-0PjXum9bXVv1h3AQpbIXeUnNN6Mf8sUee-gu6dNNuUgQvYIU_mb-2k4zR5Z3RvYQdkgTvHFw_G44o1U7G-JlqPLQN473dIici91szOV3pwHFEV4_jogmfd0j1gyMzhO66jH67bQwGwLi-gVq4KtkzdokqbUxmbbAEbCScOGOGWhokYBD6DUw9RvuGz0TW562h-ixk3jYou5avrmHtYd1pkZdw_bDRqjKtHRkgRYtmuBr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4X6BwDLbDPz5E4TMr3-DSNwq_eFhv7hgMhnLBdSg2wAXxdPVGevrf9mmnmtAUiNPNiie9ZNZca76zajtXn9yAfjnO8JjZd05zXyt_1yiKo6urbkKhfJusLLfixwW6K1ArZkp_LqG6jioX008Ru8bPS0Lz9TnCihu_oemTr_ApZpmBIDrvMlj8OaC6A-nKN4VGA374vPvLkOfXsFhy2bKJ9AkyM5Ugw1_LI5PKpOp_9C74VFws_i6u_o1MXYi9OCCEkQNmg2wyuk938rWPG3rhbPfN1I1is3uuVnt632Wk3kdPo0XFJiQTVilgEFPauYUBqytAFgWJB7_-49Yoq2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL4pCmEY8SoiQMGL1Ws2OxvOFWfMh7Vub2DCYXJqDOF-ZqeUHS_TBdHfSDfwrq12dt58ehM0EVeCFdMlMWuYRq1pe7_dlIgxWEGfjpoORjfuCSChugVrfQmheRFynEewvFW2_9Mg9ENEX7KJnBSl07RLkIw8QtLKYVvhvFKCOA0ORBqIy_hPwE1VuVSuj_YYLilyc8zo1Omd7182WspXeoG6RB_cfLRZDRwfkV7oZ0gS0Ucd7-LrQI8JDlPiVJVxGuiPM2cjolClxWmcUDG4U7lCQ_m3e72dxSIRy-_IgfrEoA_vuO8cjwFBy8TLGyk1IKGZPNUDxsVRQYU37zrgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h7djfNHhwUqMEXQkJCyYxlJueAa-oaVmZAeD10jGUp3O1c_piScZrpWwSWskxky19MVlftNm0ZsJpMfPyIxsEjHbShZKtNhY3uP6Dbz-2blHj4fgPw2bWnWnRJKQYjnQuy-pZlB8O7CtBsb_tJXOyy5_kKjvOLUsvM__DWxYwXifRpsH1QTMQKk3PCLhoQho3JnKTaOim2XmWeQN2lR5qAqpLJMkHm336efVYXQAFmwqUhiGEmtqMHQ7r8r85K48posBMemZkmh4xwOQ7ykSEB6orXu5TcfOF_HcTTP83l-7B_oHRP34RHZ0ABUvC3CQ5q9zzhKHjao3_zg-XWg8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g-UqcMZgWv9iERenASzxRkHaqYb8MPaor5y3pP9mdkK3ik04vbMB-Y12dhY7wCMemVnXt4x2j0_StVy-bQYGfp8aggeyYW_1Em1IrHQcVMwOMqv07CiDjxlsW-JVz2_XTT9TqlLqzUCMv_9Csd_y4JjgwSBwZJnnlE-sC1b9Y5P75NzgtvJc1Ru35HN1nUUaJTQB732fcDJbqJG2ac2BQli-PBaAhpRlighs3KhKpxBi2AkezDataAVOLM1L7Mp9mR4zTdGQHSspSlfqU5XbelbLhNjtRBZ8ojIHrA4g9zgafhg7P4bbrXhK8sCzmppmxxVq33ugzRtkAQZv2pyNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKiN3zHrDrsdwxNZ_Ue6Lol8IQxZZQRgjnmoETx91RJ8bIrmIYWsSPN3uI9UYerUlmeHbp-WUgDSNDZmZw3gR2WOdluC0waXp6yKA6oanjNNl1FcTiPoiPR12ztg597hS8IX8XVZG7LB2kswqEzfcJIrlC60QYv0C-7STAcJj12KI_TQ8A9EYVzU0BQdVhyxAh4ArZShVQ320Xa5H1jBHJ_ikULZdhJi0EXuzZe9SfIrPIg4RQxcF5sblzlr7u2aB38ZVDaECRbsKYiOPzBkXtuRMcJC49kEXVizPts7ZR1dY7rcn9tb_7bg_wVNG5Rspwy8Er6cRPhcI0FY2RF1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NC1eqACPYL2PVgcrVVKyWTLZVpNbLxM_BLqgM6cj8sTUxaFBRlXfWetQi_bir21r_N7zwPW0nL1YAAHpkTd9gL7h3gAX_861OUXTHuMDM6cCyBOw3DSCIBkmRUg28Xwpmj0B440KKeDI_wUeAFA3lIWm8PSNxuWvct68VkwrJWeRvoS7zOYfolenSERE8HuGgyGnCpY4rQULKvYqaSupYu3siS42ZL2GbXfd6hCScDdmSjdqfXshz1IDLsplct6eeW1xkibD2MRpiN7xE32Iw_bOxYVL-WAwomQEpb6RDbWUcqBA8RnQir8_NE-gPorLhdI21Z93SPLXn_TbDD146A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmp-i2r0I50tAOy9FFigjtWybH2oyp6m7dDrjb1-TiWT8uLuH9MC77d4SXO1JFNBi6RcDBDUVCbEt7HyroozdxeIJUyPzeYXA44V88mAWCUJkslRq1hQAhNUPKcxci386AsFAop2tJpEBZkBciRUm5jvjCno5ABqKVH1kt84YYjIsXEHFeQKK8ygl21BPgqQFFwjLJf-P0GsfzSO7hlWWRYqY2dIWverziYPJ-EsuklPi1BILkgpiOZ1aiY88SC4x4_YO-EZr3IY1VV3rrro5B96Od_tyoHr5GhQF3wcQyxavClCk_9_BtuxXxnwG_fBJ1U1i6_ZYRXkJLFj68hncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/atgCqAOt-9K5H1N6rRPd-lPfSyXL90hIDGtQ6qD-jizTcc-6g-ABFL268_9FdTYP2PCHQdk8HCQiezltUgf6h37fW8GIz03CjYYhDw_uOAwuoOOVG2mlkyy9lBSSHAJLWnPHLeOb8Q-NdzNkego4zDKEQ1QONdDcx-vRa-bmOvPVhNgbhdnQx-GxDD0plnAmSj9gZcexRm3N2pLPF1WClCECrPkmaBuFOSNd5EADWAHl6S9ahQY2V79tiPIibbe7dYcrbeFQ_Siv0BB_kMPKyBuFpc-naWwusiwi4U7cWwLTwbwtqL8Piv34VilQVYc5c_Zm-ZP2TTUgrBxtaxqTaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICP49KkqafFH6OAiQ0NR9nriC4Z8z0DLZ6cnxbF__ycoXlX2w7CRdh0-GwIWQLC5PnkzDwIvg4bvJLg_iiMODu2GH5o0oRhaZSx45D8KhvA7mA7fd2To3yp3Ft9c5YuuyiuGVbEHulSc_eEg5i7lepAHW4P9V9Jk8Argt_8VQPiAhTc_e4Hq_QUdl8g20SuoQpTSGOVCsVBDuTAxU-PWZiCvX-YfxOuO6n-NrYpqJ-1jTyMepp-HJzaBF-hTyg7j1xtXbHy1kRBVdO75dWYWayLwrarDBhF7W_WElsnGtslNr_7npuz_VMxdVHK422PL7dKSN-9LqM5k-eIo0WuIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=TRGquyDmpIph6ZhUF9E_ZMMa-5EX1e1ud_9qL2fcF7uZcwDIXNNloFkcOoFOqH4P_u4bb9ITnl-nEoEDHeoFJmpM_kv1ga3201JGH3PlvRs7fLssyalwCvrhXY0IyWDesw6NfQoEbdzlclu3RiPrnZk8VhM76X3jeX5xGSUxRAEgiHzIU51ywtLcXjChBb73HgJExAHgF1Bedd4zydpX9LUXetYOMh7PKJLJVpYI5cXwvG2zIEj36P-YL5LL7GchtvHK-zr8Y0pnrbSRSw6H0YrB6BgFjCPCLXGbLjH24mmQVEF14F5_1tvlDuGq0bQ0TUoCT9p9_4RKQ-6Ba4Ri3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=TRGquyDmpIph6ZhUF9E_ZMMa-5EX1e1ud_9qL2fcF7uZcwDIXNNloFkcOoFOqH4P_u4bb9ITnl-nEoEDHeoFJmpM_kv1ga3201JGH3PlvRs7fLssyalwCvrhXY0IyWDesw6NfQoEbdzlclu3RiPrnZk8VhM76X3jeX5xGSUxRAEgiHzIU51ywtLcXjChBb73HgJExAHgF1Bedd4zydpX9LUXetYOMh7PKJLJVpYI5cXwvG2zIEj36P-YL5LL7GchtvHK-zr8Y0pnrbSRSw6H0YrB6BgFjCPCLXGbLjH24mmQVEF14F5_1tvlDuGq0bQ0TUoCT9p9_4RKQ-6Ba4Ri3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDJikx5xuDV6xT8AKOZf58AEzNO0Db4CkAbfYqbMJnQtAXwK5DrLSil4cIgs4UicJzj1wX0ntnB0egUQAHyAgBoR5xJD2rRB63-dFbb_nHNEDVyfQ1OcAf96NDEf6gGHYIGTcITBKVruB3dHd3JU4QMzMOx5e8VN6IDv4AT9aZMqkOtI9VxTuoyZqBwp6UtI_uw5ILUD07impeiMUlPPmZ_PHqb7wYULmz7vT96LvvtsFTv1mkdOeCZHd97gVJond9dbaJXuVrby812uMmWDqLcj24Ku51g7FxSdE9EQwMEN93Da4lQda0OPBE7PSein7u-lFdAb_6b8J_drLI9Zvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUDRHrlvL4l16v7BcC1MwbbOFL39AT_1yR3P6tVUlrgSvsYICYn_jZI-PohXZ7ALZuUpA7bv0yHcI2AS1la4ruBcXUVSkfCd-Nsz11Hx74lWNXaadoejEVWxtdDV5jFkDuqcPJzCQXmtDQr5gyuO0GJMfpJWjG65m_sgAcOufwtvE9YfnPZyjGzgKC86eYANulSiGHealYSzkxI_LGpJh0R-LEQNHafx2R8ng2YU2hvm3dJTXECaESAKuv9iNLMmc6SI5mp1wCdcoE4asImv-Xvyp9yonfF9qpwkwNvyfsZD6ON5yprIVYfIFkQyWZcjuUaOasprxIfqomPhGReLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSd0mAbovJ5u96RF0yzV7lahqxUECTTEopVZtDuiKYa7Kw0Apv_YVH2rONERVndvDCxRGTo8_Nf_eJMaVJjicnnAo1VXNgaIiJ5QrJEOEsz6cl8vh5NMFyNMK8t6Blh5ApvI5o28RYvLxQU5uUlAI7TkTyzy7NduY3Pepf5-d18_Q2vXjLdn8kjsVPcjTFsn4LK8X9UknqjpaoNbna-s2sr-beJp6MxkPS2TXb24CxKv8YAIL4M1ihnzHBnHMj_fvUgB61spNyZ1pUCTHinXoZC9QF1ovmJ4uKKQf6S8dohJNIFdd-tRjCOsw8nUAcHlcbmp2lvb5QUgVdMk3wOZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUVHgztmjJSmbeAL6n07tnrDlH2qKSRxD_XAWkYrFvnxBPp7OJXQRhc-j1rMdzbRW0dLgf8Vdo1oahrMVNZVCsnCTbBv2TFJZzyee5YFqUv9TtVMpiJLY0z36i0mdgAODD9bMtSnauBr163vswbZ3YJhYR8p3-APEWT1k-QNocloWJQLmPYhbUl7ii4-ptUBxkK6WlOUky_9Wx61vVr4buTJjocK7hZGSVp0Xj2Au196o4TWC8RHm69NNdsT_tK8YngF1x6dUn0PlNoP_Hb_b3cQNIFrhKWUJBOo8SaeYaul7gdSEDCMAi2nG94sprskK7rNgADZ46HuCAy1YvTMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nves8kfRY0p2Y-vy8Km__Apki9caHpYD-pTYyq6FehlfW9xqKLoBLruJYvo350KMvi6cgYsBK200FuS4koUCAbzRjX2-S3z2fQWQnMi5Vkt7X-mdmSadikqjt4WbfYxZ4D-o5f-IgtBrGx7wCMuUvtzI2D-R1v6r0UMXKY2QqpG6Uv0N9JwLwybhx1EYdzCpITxvef_vn2VIlH7JeCWP_864avsKLFrXVTHqBbpXApMiuyL-DFl-n4hlBYbk3TQgjSAlfUECULOJhnV1NGXxsOBnSCMHtTgIWequNe2NgV_X6wXratoQGlLo-65WkrPcZ76FvaAPxk6VfrJbm4BCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QChVfxIeusJRzfcsHDWsMUAYHyRKdG1v6Q_91egbrC8XF1q_6eZqoyJ2rUXn_mIYmLtyynqqsyXwRf2os05ZcBtXm7ZCDPfWEMV_j392aaPsqyWCrrM3F4eyVBHG47DjHr9NDvnIpuHg6gYPsS38so5q5COqOH7oFUZWfvfErditaEmmyvAXDgq0V5sykZtrsnogfeHlnxe3bgQ2ADdXd7ijWWh5QnEqYUqtc9XSrOWaSq9c3nRTjfRflF9ExQEMhPpZ8fOtLHjX47rdYnjXXEaskbX1cayRCdGgSWfV-991xHucjo7fXY44bLVUnun5r2FXgLwufDOjAvDq0GZlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfQBqYMDymORuCjQZxUSZjuLsmjeMgue0fXiHyll55q7Y2kgXkMzz6fwaJIeEtcsRYgPD8_Kf5tUb8WfQ9jegtYCUd1QTeWJFWNklPH97IAXrXSUvAbhWYIZ8DDB0Cj4ntvJPFi-2slTj6_x0fUeEB_0jbBtNwVEzrje0f_a9iChk4hp2e-dFCfTPzSa6cOL4hNqVIc0vM1nfoN0qv691Hw_uaex6CgMBWxLy533lPb3R-O3DF4rujusCoBOaKnH8ZJWeWyNPCtkKpt9jlz3hYPPTDQPJao-Qpy44BUYtNtZPrEn4YmUUoPu7Ht4t931wlYH8Buabymk7F3mMSHIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A8n7vZyU0c8-2NKBWj6cM_xPDSTkQzhoABVtJNcLTQmmTrHglr6nwRtWbnnbaifHb0u1edAjkJYYVWPQSu1vejnYCkJj2HJxbIGwubJddtXlcqpa7IGQ0T4xd59386qg_R3vzQ8EtyHnIQ1jvbCr_Y8sJmzApWFrl8GkWi4C3E6enn67_yB1qtWt7DcO7i1ALSxphkq5qu_ex1j10zHkzBVJm8mKhHjXWnONlmZ2A3AVWX9lzEQmCLA5CuWUqonmQdgmGnoiU1wfPIG-d4J2xUdJX3f5S3d1D8tyLTYOrXo1eg4eVKuz5nYgZILvxw9L5kv16q465I1Ae7qTvO-rkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HNfmeiSpyHECB8itvTzcgsco-dLmsGEBxuL1Z59bnXNL6WM3UbOj5ilQGvBvt7bexj9xMhIjRU_3f98h_gQtHoFbnRigeu24wpk1Heic8H-P4v1u7ahCFn4CXKNPdy7A2QNaTb_D5jilSQwhEJEI7MmaV5EWsVxUSW6dZ7sGhZHYi3RkSZa0LAIYE0UrjmTqPvjyl_ifbcx1H8AfDgQhv7EecPc0iS8JiRLDCWoZ7C-fqjVdioTJiSY29NfTqRZ7Gfl6h6PusQD7Hew_YuZsATQ52J9HCr6sSszRxClYX0n1wvdwBlSVI4NzSnv_Plo9wxm5xM8i6iz4YgOfh_qzLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u05Iwca0LeJRwcHUojzlYaYCW_Q3ZIwdppfNKpC_VKAol6xmoLq2mvf4SN6ipIUAhhpsOD0GMftic_PoHOrfkv7T3r77c7Q7VPgZCriOEcTFlPKqkn86MKBBKbxWA1vTw_xrLPGovRaSzRF7GcVr6CTEXskvbvjzpff4N-vLeBexSVl-jHcvgdIi0acu0HKaAs_s9qnjL8gl2uNGIR-CZgu7A30LvEcI0mUS6qXhxQywSApU2R65cJVmMkLz4HUfuusO0Vdof6Ev7KX_wYU13kOs-RTgLJwbqiM-O1HYE7ioQnVF10BMVOeSwOFGLF9QBJ6Ql6KUVnzSbDJiOQy-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EXqT3mUHMt0NN1ERVgIbcM8pMCcsV9qDhm2068Lk72pnSk6NooP22HIW5lzPnEEpa2MEczJ5CMON_NyyM4NdpF_mCUj8Tzc1TbxsJdeHyJ4yLumK-aKxY_U6SDCR4H-VG2yVzuvFhF8j1OgU62dEAtleDNQ2GJU7yTEm0Rrm7u8jZMoBgr1ENjDWr1XIJEJnyFm2GplLXNAmfeSAnjxMcCWsjGgCGdGGviwym07_UTq1PbhjLItOwb3iCbFlYk2RQbFLJePnidb3tjI-4Vgjsk-3zL5OAK_QVOoX_900d8bS9v1YzEclQ2CCCm-7ZdRjY87T1g4Iomq4sb-47BoiDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRUWvjMBZ9jX2eOPQJeHf68xPHbp1Tdj8Tz-Rrmx_i3-gilyx85gOsNLnXedk3CspIaIOfvet2T5NI7UYzSPVdSkHlDy8G_seVba8mjs4I8LlskYIJL8P54UBmkgVpsTWWcmmt8xFjTgsqHnsOwl0IRx2vkmkFf5L-IxpQwadGQP9SGQYaii8OlznrhPcN3pfTHkDQzhh2ayDQhC5z5dyqNEBGccVvSRqA8TFm3tTAOjM0SXPgkUaSQYGHG9yo1vG0hXV3jvyHYyZ-WDtN8vR7--qfuy9RK4IWtpCrfi3eD0Hgoff80ffV0-AKgdGr8rIi7vUD2hewMUXmoiBISb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKKD-OuEV-KtL1akp5GROnIazxyPuEdG3qkkSPke9ekUh_2_ZKwIpRENWU9Qt8ZpnGl78u1eAH_7bTHMFGFqP5JiO3fPVDtEyN6JD_S6Vp-E7kA0pZrg0DbNIetZtileHYMVYMB4RdgkUpxRQW2L6b704vcTd2KwEfYB73NF6ftxM8WK7D9kohCBkirMO9jPZ9nWnE5nY1dHmJEWiD12lbTbIHj-O3SRfHk5dubNcCA8L9U6sEBFFPqK1bVMBDEYfbRlEJc4UBEGVc9J_ZUdGJFHi-N7PSeNwbscKu6JzfInysHMWAMGyfhqL7WIQ96LMX8ikTV3LZOOElJ40_I0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVQfAlbfpAxiFE1ZELU6V4KkFZHOrInwpHgp6M9ev2hxwhwjyPjnVXCLwC8-uxSaOFvcq84nCOws_u3XfX3cSBPawQtHiMo5uKA69beV6ZrmYu_V5xz7VrOdtp8SwwXm6j2tPVZ685HYXfLoaGt01ryl59uM5eEscm0y_iJ95GEwn0Id6YvmvDLYpDj_mLYrN7Sic8DJFgbt9RoDel1NUxFtbgHdzhB8NC1VXClK0_pLhUkk483F37NSNY2mktqbYMN6gdi-3zoz4PLjLgTYgKC-U-wp-Ysi9dKtYKPBbM-WHcqCNImxBf9jOXdw4Ft-wkPiiRl_tKslo9hZviTPUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BkS8euWoxmZaD5R9uFkrDoEU4TSEd2Ov_I_kLSi7N5V7PdxADEpiOtxHSM3Nwsvwx7Dxt8ez8OOa-417eZTJh47tpz2T2PpYc53TmoAajeuXchKatgc5AWW4SdSJLnPWtFiDJ0-gM2OjkLwcyF2MIjIh6J4_5y2Z4qFmSvGUnKVAcTnBMS__ZgwmK3sq4aUXPrJ276833XnzufkIxgeyBQqmVMMIByYSmOhb_znCOQefb_NB5K09hau12kjOHDLDsMwz9DDe9tGuRZ1yGTCiWHrH5SJRrW4rmeXN-f6XGdBbBQgnq-I3tb_nb_XH5OkdZ9jMdljmi7NJQTVJ9DLezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jSPZvB4Ix44xxa13ar1NvbXTqkjhymir_2Q1bSybzhxd-WNUJkPxcfW8Nhl7kXO6_TVV__ozfYZWi9KtsW2hJ_QWgskSQSS7bOxpL6XHNkS8ys-kL8mtgi1WPEP170-hi8JcaSFxLmplAFe-11fAcx51Lbx05RH-dYMRz7i-Dov-opHTZ_9-oZ92OoL6D-5oZXWqJNYm4IwRhKcHLReku_rYUmO4N25usVVhZnP8K29BJzmPK6Oe4gvtWB1IOXnj4LIFZbA7NSIHbvyv8DBraoS5cb0pHyEjiCitBvfRTbgjRoWKWdc1u6NoxFqzW_qlCX_h5L3fCsi-dc6qWd8i9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B494MdsyRBCimvN11EGfXFGNKhGgOMc_Z3efBuSM0ZUnFtsd4QNdwuQ6AL8KGc8CBsAy3MRGeSDzjL9YklwNN2MEsQ3LEdoc9F3Vl8C0FxS-CGd8NUaWralRD8XvxYzIK7p6-N8MXXeNI2PlV_eS08Ahyq-v7G5t-pF7A5imdhkJdRWqAWwlacsngwIczwM09hcnEgtJzh64kESO4tTnK_hPBB_RpZojp8gdSge42eTMRSAUN6LJ6X8VN3lSJsGqZVRfJNh7P1C7g9VgWgJcGT3BkQYZGKtxXDRkG0vu4bJIDXtIAv_Ik1OuOcVWuXrgvhMHl--90kHcBVjMllgmOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1XaAXJ6Ck-1zzJxUmxu-3f9RiShe6R04aLRHaUiVEWPepnEpnUYSFdxIzrbp2fxzHfGtllCfslgrtXQxso5IgLDnf9Vg_CTzMUr-f9Mt4eS5QDrTy4LGDF1pjIhfN2D4NmKOPk6O41H1VlGyy3QIKCqJHEc8bpYSB6kkNOgLf5-7iK0pxLMTalM8F4IUhpwbJu6_B_VfrqMUobxwsw128hDSLWQmErwK8K2udvDOjch8WqHHXI4emQUCeZpedjBfuFeqtRWUjIeWh4ftDwq9wpQROBPn8R1bTxScpQPgJa7lHKlC5jO01GLfg3TIdV_XP6E-76Ysu06H7_MVUo25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBPIb7pKxaZ_v3NHTF2rGPLbkbB2h2RvqtcT6GN6DyEgWJN0RcLV_xSiOYGIylBsRyuWAWRMRh2Ef_qgUwgIsSP9Usw0phR7RCug2RFlqge_nF13syyezTGtXRbo4XjjZhADqRnlTwFulsnGvvnGja4vbzswrLYR3yAI4VKLYlk2H19bD-DuFTQK4J_q-m9sffHOpb0ciwYRQhAgy23CyX_Z37SOGLkvH60hHMov3KpkeT0m55fhnn1yLTCNmWdoZpkwvrry3AyLoZ57mZgDM8BtQ4s2lKMyylkUOzj-khmEgvBjvEGXguWDxEAE50VN8AryZQALV8D_Mpslr_reJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQjVX9v7WoZo_DkX-oYeKX7QDyoTyWRPMIx7MufIVByBdzS_91Zc-PwGY7CoO7R9lvY7dSLte3Nr65HvHoXWUSWBvR1p1Pg8h-v2ROB1xXAYPCPfxlrToaK1JXXRpP5YWKwfdo-fxb8yblJtA_AqEBd3SylOH7iIrPDOTcZI6XzRUlejQcYtLOoxVXvUUQl0hZq0GMXtAoQsAmoXWpL1KHYUavMmZjTQhdi7RxpTSZSIWMFxgPgJfG82CUEKreR6drg8xsNTX6-OuH33sIhuCE9Rhp1tFKwGyKpmI1sbaCPH9JY88HOXHMlsIQWJ4hoXyPtZwrEm_d2Xc6UK43rnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G-4A21u-445vCKUVpen2Jw1QxMjwBAKq5MhRheMfbHSpG1X_yg9IGwG-e8mvlHBrZfuRci247JH_GIox5dwnTs5HgbJOlmYJVYgrt5wF1raxggYqxk5y_BDU0DPjZURQODOlhHlkow-RuxyNDKB8SBrZM2hurLXnjJojWoQBEhXvnXzPFpbDri6umX-ZOopCjahe6UKlE7RfBWH8mPZuGqAqzG00mp5g7XF5dHyFgnsIHih25JLxCY0Kj4seFn49Dr1WYEj4l7coTVpReQYxVRVfsvgDuRFS98JZeBtT7BYerHX_fsZOjkpkfqFe_TLhYdzZcWNmGkkd64BOF9fRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pfvw8Q63obSNjmfJucZH41LR9HkNdiLQJG4Nbv45p-gkFiwEbvvAT4_1jELxx2N68H8L8Q9CRKNaNxEtiEIsoWQUJvGdfqJPTHC4EFa-MfBAhitFbLvrb9oQztH5BtZ7AH0to2A4BvXSJ8eRaDh9JCmZ0Iw5I0YB2xVd8TuAigskCtWKYWhc91SJcE33xQpa-w36ecQaFS8_LZhZQoxPzYr3t3y3Ok9Vrfg18W0OgaCr9YRNdvVu4boqmfkt7HWArX6m1MkunqJGEPulGcuQmsWsRcOBWlWykklj84g83UFwbg4nWZnWivmLPOE1eR8mK7KcfV2YQXGqv65f93Po1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aWhcrE7bcFhDgdFjosDtw3HgbheReueog-B46M4by-4ePmp-Zuj6FQwED2Cdmee6qcTPLTElPOdEt2V0uFAFQVzyTeVXTW2gshazCxGIxh7BVEgml4yS9Y_17CewKKcD_QcerghRjEJh3hdUX7Iqt_euayQElK_nsDgmrOW2kX1B0Nj0m4H326eJWGx54YYDKGhRerwKwccOcblXHg9-4bBQV_BcDYAHJMC88kpCOjHhTv65kuzut7ZgLXv4YJ8KW8c9JOVyFAaIVWjm1AmzkP_nOjv_B7hCxFY3wHd2RapAymxNDdncrE0crga6bgF3ygJWpjYTFTSHk4gzmIj1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nSDpxv0-0UlBxiE_sNEX0bFLxtEx0NaiU-sQ8Aawj-72NVcrtkUj4KnPikCUuToiY81Z6MhZgWBZcnQ6Ak8uFlwoODGYUQmI-eJHreHxOePEXYc4pgvt7U2S9lk2aAJpYW8fGHV-NohlUZgdqk7E7sXcx1ze75-VyJ97tcgCb55s60LJaubLy4XmA5IdG6fgUQwqntuyp7kqdLtWd6T_IvJmWOstPClo_e7XNVUj4XIIG35BE9pJ1wWOVycy-QW74yYNc0Y5BhjErFM-xO3YQf3pGmUVb3oi_jV8AEDxNPspaTX4xey-nUwKaHpaH29dV4FlvMNrG1c2WkCY8KPaoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7_zvnlodUW7UH-ehKCCx5ZwBop32qGjppA75P0SlYYvHS8bTCxTgtiUpqOLBCa2WjPSecLKm5bgCSUCyZJASnVzT3ycFgchryiYPl1tiubgEGlFofIcjHCuznuCi_prcpLZOIontJ2Hga0EWdOqvnu2UMgQGEi0Q_m9vVE76JXegGaR-7kpVUPvrzvdCgQ7H1mi3miMhU02XevnGWHlygPazODGHhOkgeNhZiicZurljQefPzBLOO5Q5dfi5geCqkUKjEg8gOej7ArteQjpwpoaXRqmIzVMiAePUxin_qsZJ1pr6nWHQsd-1JK_LD8u2ogXuyw-kToLmnR0EpSiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U7PLfJ4QnDXv3UZsf-9GtJRs7vlhP944mPEo3g-flovpaQh0Yk-P3FStltW4IjvTN8aM71wjoUm6JaSUpgyqhs31mMhQNd9-E_DEAtlg5daQJRxqNdc-4InY5Vd69piDY98968g0YxY4uI5eyjqYemo9o4PPJNpJzpSA3lq8LB3gYUN8_ctRa8JmP3B1Bc2ia_IrfK0yjuBQ6kDxob2G9MYzghF8yRG76UNOB1bPLtS6T7VvCrDwxiZh1a8IdP6_2ALMlav9dkFIiq9bQrf9Ex-zWsB129JJxzneckzrAMTbWgKhKwRqohv7eyh8B23zfn3oQDiC1eGevFFlQSE1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IT02nqZhjkUXS-tP3jCHZPyHtOZbkSg1zhKkvcqXqgXsYeFCTb0RvHPCDdb7C0hnmBI0Wp_LqLkgoZ8j-07u3NQO0kqo50p3h_jTMxLGbmiF1mQifl6Oysui5Rf5hFyq7P3pV8kYqwZQ9d5eBip5hCOpN8R-VStHRzMX6Z6OZu1cK-CnjPL6lHn-Fgyq4FG-YcghY-RvxDiEYjw4VRiiDyeWx-NnAER5GimackudFzYeFc_cvdEkntetn6wVAhTS9sq7RX62wJkJO6elK58qxIkFSAEsTvrtq_ktJ0pYovsTcyH7oHtffnBamyCq7pZzIOwBvN2ImQSgv_7WMRbTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RY_zCFeynIwcXiNjbNDrkC5wfOa5Yy4TWGvfqKIKL9XGLM7IhMgI7oDucr2eMcG2uZXmdW60oIrPw1eLyz2ovegY8BWRkJFZmypVBYDdl2AptSc36V7A9-TfZJXSdLwPwqT7PQ2gcTVErdxEdbRCJRh6jqvbLMtMrO-OU88VcnDJu6AklwBcSvJjMZbsuCFT3lSHJonjt77NYKRmh4P5JjXZcNPQYo8jyOXefoiESHcve58pJttiDBHIjuCGNqMqVlOrVqlRlNdh6z39kwOKWNh0oqd16-U9PamBXJQODlqCwVLYvj7Kr-8Hf1HmSL0lCmgNiPoVKrwwd_Bx7EUM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XuW_rFZwx8lUX1yS-F4FRArJYpS5-lmGwt4WDqd-q2ROOVAHIz-fU1lLzx569JjiDbWg9g9IPC7Y6eBRFAcmoYQyDz8aas9RabD1JiJFqI-Pf7DTbwbJcJowx9XKHt5WQ6aGPPa9zfwBt1CpIhPdZ3Tej25mRJj3wsmYOqmqqr96bdXf0NKldjnJoxB941eSkwz9AaaF-xjQWqCOa754nF3OPEhsv6bV0cn0rv1kdE2j1hpPN2Ng7OEkpegWWwV2eXZWDIk6W7SM3g1E6N-nhbjfN6rxNFOHPu90Qz2kI5W3UU1GiufDXboh16lOfQwXugDNUVoKyrja1euBVOePiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mD2COnNsMPQox-v4oDNkcMg37YNFG8sHaBOcdpfQ4ClqgbavQxIcXTltQyIW2Eju6I53fJKMy6t0QTAekTFxMjDNIZxFdBJqFvDIMHDT1bWmx356QWavWtuhBvLtJAZxd2OA0pRr3iauj88T4jFYSurKUSInmnIgFXSSIyR3r3Ei4xBFBSWWnPwJBw3mui9ZSNG1zLgR5KCiwYonNV54BzggM4btmYhVFp_B5O6V4uTw7SrOPV1Z_lg_HQY09LOFZsWDJXce33OJex4Jp1OsW-q3Tpuw8X9ekaBgp2jgFJVt6i6sEBOAEEVXovY2-3RybMq8pwPtDVkoZRhNfdG4sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bLnOGjJ6VoT6swvOGnLukUwYuEFimdw1vp65NR8HhT3eFukMOKa1ixBSEmidoR85NpMWX_72vVdJFT9MqsWERbPL5fBXbPMed7XwKGfZGkLQAD-wjdogwsBi_g-JFh06X3nea1xw_T6tXWC_LZ6AADRBItx62A6xolmsK4YYH8VNFzr0ODKcgVECbkdaC4M5Y9V-XRbkdUITaxCbvZiW211EcPlWwYJ0U4-5XZv3Y_EJDPjzgvmznnSjcOtBtQK1dActk_A6UZua7sF1MD_elLuwSrCUg_jaJPHB7SpGmXy5xWBivciUtTb4y4L_2KetwB41MNEOsZjQSWVjk715FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR957jTG7SVzSMaSpxT2ZPrSJWGoFcVAQPLydhA1srZhV4xL9KEvYezSrn-r4JvNPw9ZHE9GKxfZJIdZKO7dj8qRsipHeJLAqTkPtOIB_Hpzus6WB_uOX06zV2nAblBmXp4e9_CCR0Zhb6ILQGsPnIahE8MW6wKvVsnx_jxfrIievewPjdC8XoDGl42MGhZQjgQuHuJLt-35KN2iQsDS4li-4c8zygCgo7hOPNQY4sbON3tF5aVAxeoDpYvru4IheZmLMu3Q9dLwy2X1tW5LW9jIJcb5QJe68kK-e9kAfQqPkxg1qnza1lgFLAEctmkq4jkLM7r0dv_Uugsepi9VQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg0pYOl3-_wzJDtB1_6c-eJkyjoYt4jsvQRMJ4JbNbHJpDWpswY6vlDlN2ZeiQGduOM2rW3aVpNQerFhyhWv8_BC6JejNGP8X14DFx6mywPsCyfEShAV63Qmd-ANmiLOyvb1JnFOkZ3qWFxxtFOyDv3hNqUMtn52r42Z6UecO0e3xX8yKagTXCsFy6kGMbHv06p-T3N62Ux5GugfIOt7mGsjAiOpCXqsufgRJeMYYf62XEUbHTm9ZVRL4NG3Q40g4hVXZPBI7N1lzp87DvBXRV8kIXvuvruxFcpPlfFk2UGRTKc1Tt_uS5iObxbogdtlznJ2QV1yEB6lMYU6XcQhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5B79A3_J1FXGCM7x-d18xQf9pHz5Qakx_O2E6d9suXuiYSKt5EsAEpyclnFn-h_myCYyE8KfG_U_zxxmivngiuCY1I7ixcgfM8HKjMid2oaEBgJ2MV6_7C4S6V8Zos_K48c8jq7N8kR5xG--OGs48V15Xb2FoQi4RYP5nKFPqb_1ckqz-53YnkvpQnk-urTDWo2BMC0eEp9J38YGRHy52Jd-ZijSrYzhRJq8HL2D-v7LgYIWhTvKjEmIhcm09pv0Bks-1ASmcHSItkoBMwkm30fFixai95c2n_1GnE8T48QBsK36BoP9CNo9C_oeXaPjIo05D4B5v7k74XIxDAxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbpa3U5qvk-4hVr266BbmllZgVZz6W8tdF5ZtSFro5FWjkgOvdKnrQb-PTQScSv5pZ43sxN71Fm4b4VOxONQVbthXmuoglv0rHt0_IwKnmipABJ13rYkkIoAl4WxemZBXtKL48joeLkpfMaIDmpoykjDfrBNMQCHHssJ-U5amiC5eB7jXYq91LAZ-MeiRZA-EczJpIkZvzaF6K3TPTnQL4QtKF1TvxMyGiGE_yjLEhrvq1lp6eMa1TgpFkY7-ad_39DQ7NqELOHs95I37hrAwfWL2Egz4lXmSfajtn43hTRFpXyysFbQD053tlvqg_iCMvZMbRTeJ3FLhOGE9i7Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/io6LmLw5iI7lqB2na73ZBrRFkFK3YFJodwQgYvxQyKDau1NVt7D8vJq4BLmHuRutbjCKUQrOx35vG-z1GZEbJ4rcoBTXyljYqJ1kR3TYoje4NsM8uy4bhnQag3ZJHJfbPR4rOfeElzp33RYebHI9I6uAPGT7GxQKXefG157TGZCN7lGe7ToxW5e0YxY6jnT-6ZO_Zop0fKcz3R_4uVWzMHBQRP8s1rN03ruJ-BV8fU4UB5j_lGmRji8qJE5D9TQ2VdpE-l5yel1cgD31TzBcXAK27af3Nyzum5DG8Kr7puaF1IX6pJTwf6bN0TrvZZnqzJGhasIDIYKtPjSJ1BS40g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uV-4Sct2FOkBSTI_jsBh1Ekr6hLw08_UfCI8D6BQ8mULUC6eHmbULdSM4BrmmiBr5zuWUaXALecLJ1g0robtmUlJIZirHcVg6focKIPoMxlzaKnnmtQGM4m6WrObaUbbTjHPQ333KlR9CJ5-78ujvsPYOgkzgz9VJemDOhq7u9mZgvZDP9acz3DykvcU1-9o_9KEnUj77ilXAS3b9bP9xBrTfaA-5FOXTlgXOdowtjTC6IkrdxGpLR6wzhGjfdMpIPdGO6Fg4L_0MD_Rv1pSCM9Dm0mKH6ZhvRDqdfup9WVCfjWjgvFGEldB0w9HmUh5PK0cSPXq_UTalbc2I2IuyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bAKaj2M3nW2B2_4VKSeh3XWUuPvMHZrbZgviUNrjqtY-PUPrRYp0SEzLO6ox5Ai5Op9E8NNo9C9TESHbpCU3bEkDAy4FFqSQthHMrNUIEsXZFaChr-SpQ-SmN22Bnrv66iRdQBmZw61hDDxupBB2MghOHfSKCJbt7989Q4DwIWcyvliMdzOJRbmeWWt5OuLsCaQixOxmEbUEwZ5vcxNabmnDzKau9xrwB-k0IRbH_NmtLMM8q8akwom0QRDUSlLcO4L-e-nqBovMUELsZKJqRCyHbAn0P-Tv_HIoV56HHUF41Eula3S9vkUwPu4xDQ5CN-sDHsyOz4qqXCIupkQxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iIzUadDPfjecly9Xeox1EQkSjVa9s4kpr6nW-DGi23_7JZl8X-rnKXr9yDfKydpIrA_Qi59O3nzIXlJFZdblS5YwudaFztKiUHmAu4VcZqp0jmreZDBDjwaLsusPBv8gaIDJcdGfnjcD9HoQNYU20nCnARsJxTcpKuwPeQ2Lv0BkGPgF5lESrL01-lsUGN2dgn4TAVvwl4AHLy6oZinEqw7l73CbvRD5yJ7fIZqJHYWdLPpSVx0NLIEc7tK-4mRtYfzY5ahvMWqHZBSdCBn1xW2YWluCzLuhGrNroekY0g69punU6Fy8tlisnU_SKfWc4K-W5Mi0F8sI_IdMOOOmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdC26G4Pm1vr5iudjcvsNuHblaYVn1d-MJZqOanD_Mzkq0jr-1UldJuTAPtFHQcqJSqUdlyutIHxQ8b7pb_ADFGfEOhgGFKnwSMd-CEB2e3690bGX8WH0QrDB3bR2BphTRpwasMiiJip8wLCTEMRWkFXwoivPukmm90ydRAi6AQdPc544M0G_oNCiqxA120eFqOhM4auTlY3Bjxb-c0IRU_PxG9FxYXhVu2mibVxLNwrimB86Y5-kFeCOAGG2ErYLPX2qTa7fA7HSZctcCojRXv_i_x-hwo2gk9q2tkf3ZlgsGVRsHEn8PQTZlOCDrdEl2Ia1CGVbMwUcdW5oSyuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YMkGiphA9H8iob63vfmgnOj3kf-_LWBnWgiVmeRsto2PGob57klUPofooPDLN6_asz7jAIpqf8p-Es_cukivRPZZ0WDg8oVaJ-lDfzfmPAGk2EY69p2jynzJLxGFJSyVQsnzilLy7TZ5m3_9BYcLY6-L_he1MTr41jTMeToeBCbdZrpDfYD9i4Ik8jzoALuSM1sbY8tX8JG2YW1ZscCdglil-SYZ58u08wjMIR8ZeJ-11v3Lic_bV6iKMFpE6QjRih56cI0htXKcAO0Y1fIxWxqrKbZHxIJLBgijptkFX26eKiHolZIcQDenoivwdftrGdv9vfvMRc8JSV2Jpnmx8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGZL5osxCT4TCowrwFNzm78i8QdrSMmxQT8bXrJZ3SmAunxek9Ei4i2u19S5YfA6bpi_xdVsL8d-25kmo7xUgb74N1YGI6cjdsW5RcFKPvR6G1ToPNUKJOKQ1Sy5i1PpU2lzhfJ3wbG1t8GUcAJOMqGfmwm8yeVpitCZq0pBtpxaB-WsruYWAz5M03tSYf6XEdQLhtaxa4arw9bes5VEloxCiwa7b8nGQexFNBsB8_FbjrtE8Wu49VlaFww27gfDq_ma8HmIslfRyyT957Ng4bmadGmRLbYbmo1C-fZJip4UufiQ0F3F2DJBZzzE14TdCjna3mbyRGHD5whWkB3efg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aw9nTaL_Q5iwoQ6VgHcz0OzWSDCBnvyGAIV8c075CHzYRv-NxxanH95N0jc-_z5aBzUqj5EP7nuz_3JAupe5w-ZbzqQqcpHo8lhnhsV0kxT3mKtQpOlCY_dM5fQsUwd6sM-TD7skrbUdnNWO9yGnsni5SHIiyC5XvGfHFQWdA2ZbvyfehYtn8SgHJ89LyQ3fImqN3gUGhSgGZ_ePzFj89v2uSKO9B4UzL8fYNympPk2bSrpihI-ix5RIauIyhrGrgC8TjitCfEF3WJ39A974I_stQVWe_3qQSWOL3lVDGibXmpt4TeGqgzWA6g53oZC7bgrVVVyojdHhHc97u93H9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TqaCVBnWyKy7-h9Dm7BgffmLw4Zk52tTxV-j2vY8RpBsTkeEGWTOwMvAfdeYdBwVSWnrj590kX2W9vC9EY2Jf0Y0dRJHIafWSoJnIiKyxoN5aJyPb3HrHE2GCZCoa0zeo-ZFaGcVh6bFdFN6uBUOT2baxKFQ3lS_pwn932jJU4VoAn41k-9Ivx7wJ815UFP1B0EPADSkCfIfjLgrmcR364BUegl5hddGdM3c5KmTbwvKLRo-xy4D2zsBwm_fEEDnXAHEERgsRZIcCTLsTjcJEMyYNB3u7gRI_3__VcKPjN6_rJcV6j8EZmPqmzYqAXVQWxrLpt2vOaVCfY1qrQSGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juXuq7GKnBoVuqvFwXCKLP505ZSF5AZdPK1VYVAbz6EHuKGPCeBbQiMHLVrfZWgEK6pUdTqFmCXgR21stW5UeeFRkTVLE7RmYAKNUkEbEdXHzTE2y13Xon-4Hujnib04LEIePRWcaLfpr25aN2-rEktHjaOQ9I-kKu9xInsacwnz3npsn2sZQzKGdTv-4oUQpAwGDjhVHtWmAJX7GoYg1MHASmm-7E7WU_SflqBAxHqYVW8N0a3DMSTJ2FuOr5SVEiRFuMeti4bmuVwbfeaQ0qUadoOyLWpNeu4RqMwd8x8El5PXGECnJGQVmuIawpJdFgKcdC4aA8ua76c4f32QOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FT665bH4bwF7ojP3jZMvWloGCCmLRMwDW7rn5Gl66Qlr7sMTuWkWYVV_n9asNm3NakqjPSbCt35g448DBw53YMaQfwa3ze84NtZ6IpovBgKSBEHtzAlyxG7ZwxLSJs7ftiLnk9lKKu8hRooo0Ip538uS444i-jr6XQOtxqtdalkl3chZFozbyBrHk6PM1d1SZraziN6yMK9nn-4KGrD3dTZZpKAcaDe26_XVQduk2ahsSQft6nuf05W9-iSJholwxudi3Kzfr91HKkO2mjfnz4PP0Jj9ysI0lrdI8zPe8MhrPFzh2m3-SuIojs3vz44a-9dFmv8pZGgjOCWelNMlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LM95uSOhYtdnEk3pKwBACi9bVfZAFGtQRwsQEOPSEpO4S5IikPmohNGACPNj8C7k--nwb79nZVz3i9rhxP6ldkUwZqLYOu_zaNsPB94CSXlc6wxXUmyjKgeAv-oeZQxmMsEHwiNY1R3q6KRp_8_alnAOJafXEH4wpAxGWMAWE48r0QuBnUmrNOxyaYsXw2lreivOV8VTuoce2cwSCO_7Zx4M11LYlocerNvI65_1GoONKLUvxf4pfW4ViTj_0sdPJ4SHEVWGiEcoF0HNUFexIgY6qG3ZDdaxspakS1gZqcV3lnPxHWT-ION_OSoUeW2_yFJ1630dn1OKbYinr5AzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A8VT7qHTw_I5Hn50IiP0Bvbsd6NdYQC9qLDVjKCM_pR4b-FzKwKHloJNZDsYqY9Ox2h-DKo37Oy8suarDQ0X37NKKqXlakxaNvOVnh0g7gz5F_Evq9SgTSQLwTAxgMZ9zPI9ljxqGckiWiQzhsnfTPdSWinl25eAgvKei9wjrXyVCybgEKyON72fIguqrpslhH9yIEEii8c5OaPBGaO2kstpJenYW0IbcBxlRhdW_XaYB3_esWhsQRbE2inYCS28QnYgnXWDz66L7OpQ9ssqvkNMrk2aoy4uASDZtMCViYE89l3-cEtMdHIaKLMmKRHFCLY1DslVAe1QxPvdIERfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZBD-ICTF-5BeOXGJWv-x7K9rbjlZ5zmsFtgENdhbdlKx_GwrDppolyforRiM9wrK9kChI5CnrK_u_WSKhKMz995Dk-sbkwSnj2ojaLCE3kDPux6z7lhARvz5ko4jPWCchvhlejq44SAvRpJfInusUt9tJd7uQd-FQuqwVztyFdudYcDW4m4-M3MEw1sJBCeRkztXFpPxObFp-mbqGMDq0xvFmiVuKNvCKzdghLzxUICsdzkgBZJ-_hlTRKpa261GqmihKQknrGvNRhj8qPbg_5p7d_3McGGAb058lgOGXCul4uftHf4_25wEYIiMK9AKyiS9OpnkoWffQQJcx-cElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VlxB2WJzSqUVmpK1Bnwo0EPVBZzsaalNPk8T9cOA82Wx2xhcjpubqhLsHeOxj7u3yd0Jrf7wpJO29yhboQIAUME-0In5M-76XIwJVofECxyOG5SNpT9Ofp_KccJHQ0WJTs9_icfhtYQkV2DTx6fZlKDRQlI7Fq63I8WQ0Jhw5cX0nh0UF_pCx7Se6EtJTwprXaWG2rD1CDxLgB-MrPd0vJc3SquabXOGk9x74PaaJ8-OOgvB7iSQmgfGmZo6Dza8V8ziCAVkZ8CCWpGmGdVIVxzJHzJHHhFCM-ft-oJckHGT9oWaSY9tWyeq4xVuR0RG1e5eDjYexhAZchvzG9h0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
