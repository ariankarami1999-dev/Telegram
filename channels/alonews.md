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
<img src="https://cdn4.telesco.pe/file/UfOLw8wz2SSj1zYvy0gstIFzHjBkCcvlDGj3L1masitDbd7J3ajmiFJ9hKQVKpy1XMA44f5zTcPf_9aCNIoAo7b-l2ueCFqDGs9ssh3Dn6DZJYO2p9ckuhHbZNwSs94PxgvA71v9oz7rI0ntw653Jr7eI0yw95oD4ikMBTnu1zt_YIIViPixudNxbaE3OB8kx2BwVGR3wNtWH-gHVKwYsHFX9JcnS_8Cpkpb0JVmQxBxL4TO-pLtWVqu1Xw42aIBR7ISmY01vvffA5JW_5AgB9X6OofU7B-YrRAB_1L85mlWAX6ZmKb3H8feLxm5OO3DEVMQ3EiU-9udfEqbqcru3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای احیای مذاکرات میان ایالات متحده و ایران به کار می‌گیرد. گفت‌وگو بین تهران و واشنگتن در مورد وضعیت تنگه هرمز و کاهش تنش ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/138621" target="_blank">📅 10:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
دقایقی قبل، زمین لرزه‌ای به بزرگی ۳.۴ ریشتر لالی در استان خوزستان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/alonews/138620" target="_blank">📅 10:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47170f0680.mp4?token=eB_oQyrbLJrLvmKkfevIj-8KvwYU5-Ha2msL2DkZWlbd3QfiSElYdUb6bMWWcYX3U8FzS9hxj0RPekfNsdVVplphGwlNQJYxetNVunwHBaaCuDXmf-QzUm8prYxe__IMmx6pjyXyHvf0SqeuVHPXzQWdKOpqQtoJiAnq9rxShgp-r2rgukVVJ08s1GRM6jWXYOSkjaU98Xl-o2dsabc7ti3B59kK0Gzt99WkYvSWL5qEW2OnboW3JWhcD3sxn7kYvYFLH-UZZVll0-RF71BSTbhpL6_uOh3QmSvSPLpuuHdpUL7XM3HsR4TdmGvRolWuRCYrW7Iu7HPXlIr9-9dyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47170f0680.mp4?token=eB_oQyrbLJrLvmKkfevIj-8KvwYU5-Ha2msL2DkZWlbd3QfiSElYdUb6bMWWcYX3U8FzS9hxj0RPekfNsdVVplphGwlNQJYxetNVunwHBaaCuDXmf-QzUm8prYxe__IMmx6pjyXyHvf0SqeuVHPXzQWdKOpqQtoJiAnq9rxShgp-r2rgukVVJ08s1GRM6jWXYOSkjaU98Xl-o2dsabc7ti3B59kK0Gzt99WkYvSWL5qEW2OnboW3JWhcD3sxn7kYvYFLH-UZZVll0-RF71BSTbhpL6_uOh3QmSvSPLpuuHdpUL7XM3HsR4TdmGvRolWuRCYrW7Iu7HPXlIr9-9dyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله ارتش آمریکا به یک دهانه پرتاب در نزدیک بندرعباس
🔴
سنتکام اعلام کرده است که جمهوری اسلامی موشک های کروز ضدکشتی را از این حفره ها به سمت تنگه هرمز شلیک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138619" target="_blank">📅 10:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=sfctjZpeeoQcmCRP2ZNqtc3Lb2a2vLsgcBPc7l5eN0HAHg2WSHgtObspwETRSXYfdzY8mTI4_OXv5zUH5bgSZq3tmhjLbJHHFEgjOIScg-bNphZP7TlME4tIgqCdMSj6yaKQSScPvyxiPQVrpKpGnfUZ3BxAvRzmli_8Pdv-mTK-KwH-ybmI3YzUUuzc3YoUOVqmIGmr2yXt6X4eY3lBpiOg3VyO739EBpo8MVKw5Vd2fhe2TGb5CSHeYSFXmCf--FPEnfXnAaHoWzo7IsXJPqzYSdODW1M8nn_edqzQsCL5bsqu5Mk2HxSRAV-w4BYV1Fp8_a6L0UBXqgJ9JBjrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=sfctjZpeeoQcmCRP2ZNqtc3Lb2a2vLsgcBPc7l5eN0HAHg2WSHgtObspwETRSXYfdzY8mTI4_OXv5zUH5bgSZq3tmhjLbJHHFEgjOIScg-bNphZP7TlME4tIgqCdMSj6yaKQSScPvyxiPQVrpKpGnfUZ3BxAvRzmli_8Pdv-mTK-KwH-ybmI3YzUUuzc3YoUOVqmIGmr2yXt6X4eY3lBpiOg3VyO739EBpo8MVKw5Vd2fhe2TGb5CSHeYSFXmCf--FPEnfXnAaHoWzo7IsXJPqzYSdODW1M8nn_edqzQsCL5bsqu5Mk2HxSRAV-w4BYV1Fp8_a6L0UBXqgJ9JBjrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در اهواز  پی حمله آمریکا به این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138618" target="_blank">📅 10:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwCWl9Qg9wBNzyHsR6-QwsCbTgl7p1BitqFymwuhE77PiAtOuY4eqHDjtitC-ZrVhXDOzYs3W3fnj56zXayGBceojUTT1C_q2bXZQwxqJnZ5U1BJSzpiF3lQxuD6F2y1GqIugAEQxbd6vbrkezXw1l12wy9YOzFuNXqI9bh_jP2OfJ8am2TZNy9g2OMiHQjik-GvbVSY9XS0U0E2cC1PomnHIKkJ3B08q9gp2q2eVzONGiSsgDY65Fa5z6CspQQbhpD7uuuRX7HoNeo70WwskSTj-xM7OlMxrLglA_p4VCHemYP_df_cPo1WOrk_zzeJtZywdkCqAbp6JX9aUEgZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: در صورت دستگیری من در کشورهای اروپایی، نیروهای ویژه اسرائیل برای نجاتم مداخله خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138617" target="_blank">📅 10:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aixey4sdpRrp4OyDV9ZJnQJbhnxWt25KRUPEaExu4pYwHuCXw1oAfK9DkygjxJH13Ah0Rkj3qRaja-dAXJF94SvQQGr3FkospaWhjzfyNouJ3nz241OIiKk4fOeDeP9Q7MPiUTh6uBBxk3lPieApymhx0Z3YlMoCC7vbo548kkCCgvAQXEDJcPeQ_soqARMztlnp8clfB0aY3rlu_amJVo9wGksdk1JTnnRr42F6thHYZZTn5KBLIu7hGM-h1PHeCMOj_RNO1NRyS9Ooa6v3Q2V6ZKT5JTlFO_1ET8Tc_qalQfgFGdAUnx78pAyopeg1tOvrpbqjaODFA-JF_2vxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138616" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbbZro87JIwbCwiPNvpmzavbVwBnorxh1vR0TILqwMCclpe14_QEQIcGYqsibzpNoCWKuO_pHEcqRrxKy3ogniDsseG-gwYyaKKoXSwWBNe0C2BXrf5PcokFTktKqQHTub5K02rON3kvx5LjfeS6-2X_KlaHhAwU-5uC-WS8CEl4f35QyZ0GpzvCW_SNCy43CkOkJ3EzhqtBa--X1QPfGfLbmDHkHIik0upsfYIf2mHlZcNbYKqYreRfUtwBKIh294nqDEjiVFJlbFqNBl_hPUoI2OfpZID5zPijXH9ZARO6QBullTESPm9MWqLgL7k5NRde27NmgXdvP0d5vBlR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نایا: اعزام هواپیماهای نظامی آلمانی و فرانسوی به اردن برای کمک به نیروهای آمریکایی در رهگیری حملات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/138615" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
زلنسکی رئیس جمهور اوکراین اعلام کرد که در حمله موشکی گسترده روسیه به چندین استان اوکراین، هشت نفر کشته و ده‌ها نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138614" target="_blank">📅 10:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
👈
شهرهای مورد حمله قرار گرفته از ساعت ۳:۳۰ بامداد
‏
🔴
قشم
‏
🔴
اهواز
‏
🔴
بندرعباس
‏
🔴
آبادان
‏
🔴
اروندکنار
‏
🔴
شادگان
‏
🔴
فراشبند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138613" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3gclmx5EnOcDtWpdcKBbEVGXMcYrD524tERtj3klnYte198pSAvg5dh6qOyFSQM6SYI84RNBd_Q_07q3dGznGlSkVLqeA_9wqGd9JJY5LUeR19YXmiU_PHUdr9wbYTSIRulDOnO3Wsh7VXHuLNPtwo71UypO9hLc4I_opmv3ObNHu-ipQYpcxsU5Y1Pb7j4lqxcQkSXWaXKait6QTzHPXnIe4TbPkCMuLu7ns2Q4pI8sJnBMsFWaXQHOuGeCJKu7fFnwLahnFTYmX_vuObLT0rO_NDzGHh_5_AXUe14Ku9LCBO0h9TIkrizqJYOqOC1zdyISL9hTW-sATrqrbaGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138612" target="_blank">📅 10:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ای‌بی‌سی به نقل از نتانیاهو: من در دیدارم با ترامپ، سعی نکردم او را به ازسرگیری حملات علیه ایران ترغیب کنم
🔴
گزینه‌های گوناگونی را درباره ایران با ترامپ بررسی کردم، از جمله مذاکره با آن برای دستیابی به توافقی گسترده‌تر.
🔴
از جمله گزینه‌هایی که با ترامپ بررسی کردم، ادامه محاصره تنگه هرمز یا انجام اقدامات نظامی است.
🔴
من کسی را گمراه نکرده‌ام و هیچکس به ترامپ دیکته نمی‌کند که چه کاری انجام دهد.
🔴
قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تجارت از طریق تنگه هرمز را به اهرم فشار یا سلاحی تبدیل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138611" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
منابع آگاه به وال استریت ژورنال : ژنرال براد کوپر، فرمانده سنتکام، یک طرح عملیاتی گسترده را برای ایران آماده کرده است که مدتی بین 10 تا 14 روز طول خواهد کشید و شامل حملات شدیدی است که هدف آن مختل کردن توانمندی‌های موشکی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138610" target="_blank">📅 09:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اولین محموله LNG قطر پس از ۳ هفته  از تنگه هرمز عبور کرد.
🔴
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگه هرمز را متوقف به تأیید ایران کرد‌.
🔴
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138609" target="_blank">📅 09:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVfnn5PShqEDT_rWlKAwUHt4ini94RCtXX1bIeuaQM6hdsxDcSXCVBIDfFLlJor-HlufZXR66gOf7aZrPhFrhTtUxefrORzC-zvGh5WEcKOlWf78WvGcG2xOZQpCAZALInFecynB-TyJoFqOSbO0TJe_1Dxu4GDFz-Uftl__Nwbz-azsle8FWeGGuzUAsHtw2e4MPPaQ7fzNIh75QhM6phDNelZXlosav6lUtYPUwP18wXY4rnUa1FNWDe6h-Vc9MFfUfYLYwbqGqrnoF1kGc-93Ifi1VeecmnyMOq4dqYaQM9TyRiM1ejlTYgX4wSEHjddMn4s7Xiwao2JV-yB1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین در پی گسترش تنش‌ها در دریای سرخ،«مذاکرات مستقیمی» با انصارالله یمن داشته تا نفتکش‌های چینی بتوانند با امنیت کامل از دریای سرخ عبور کنند.
🔴
اقدامی که با هدف حفظ جریان صادرات نفت عربستان و جبران اختلال ناشی از بسته شدن مؤثر تنگه هرمز صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138608" target="_blank">📅 09:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: پس از پایان این جنگ، فکر نمی‌کنم تنگه‌ها دیگر این‌قدر قدرت چانه‌زنی داشته باشند، چون مردم خطوط لوله انرژی را از تنگه‌ها خارج کرده و به دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138607" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTKkVf7bQc7a2vsEiFigRPNNXbgU0euaxuZGtzINSLHhG_gzbf4_KCiXGa4wJTkOUmonqUzxIHvHMw-8dIDRl4bltUZjkhbPWwV-hL-7h7VX7dfKVSIy8NKJXZmbUFhYp92YYCIr0-b5cAADHh-SFn10SKD4ANGzH06fD0rkqmwImuVtJ0epsblLCa3jFNJ7Z81ttKBADQ5s72d-ZbEhvHnlYuZPz7TjXa8xr8JnhPNTvlBC_UB08wrVdLVK1YgiJInFxIfKRhDYSPoypbBlOAWLlnVogeP9DXTxE0Pry3qyOBmtLQRwbbtLUjKDHnVPL9086Uy56ZmnJEEJ3TMvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMt_vFvNxnWmgu_-oBKPeCJv11rybETeA2pgjL-Sz8X7k6u4KnFZCPtN2Vvrlv8kgNV68SaXSZa5hAAGBEdhdM0IHMaozU3bjgRFjpCcFoQKXdSuf1fO3HzCWS4TZhyP6ydlkR5I0EaCJC0xKAiWKZMie8YlhHFh96jt0eqMyVJFXRG6MLNiOpfNxkLSpyYlshSnBI9ln_DVwIkwwysh7GWfIMSgZHjmnIcmPb911mnkMSRhVnqvl7Ib5T8CwVPSzB0QNrRyPkyQBZaQhg81s5uz4Ui_Qy9tuBkCLJAGGa-SXw6ihsF9Na8_4e8Hn0bZcXmNOLTT87AhSaxjHjkDBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وضعیت قشم بعد از حمله دیشب آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138605" target="_blank">📅 09:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی، دیدار کرد
🔴
این دیدار پس از آن به برنامهٔ سفر وزیر سعودی اضافه شد که او با معاون رئیس‌جمهور، جی‌دی ونس، ملاقات کرد و به او گفت که عربستان خواهان کاهش تنش با ایران است، با وجود حملات مشترک آمریکا و عربستان در این هفته به شبه‌نظامیان طرفدار ایران در عراق.
🔴
منبع آگاه گفت هدف این دیدارها، انتقال پیامی از سوی محمد بن سلمان، ولی‌عهد عربستان، دربارهٔ جنگ با ایران و اوضاع منطقه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138604" target="_blank">📅 09:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الکسی چیپا، نایب اول کمیته امور بین‌الملل دومای دولتی روسیه در گفتگو با ریانووستی گفت که با سفر همزمان بنیامین نتانیاهو، نخست‌وزیر اسرائیل و ولودیمیر زلنسکی به واشنگتن، هدف حمله کی‌یف به کشتی‌ ایرانی در دریای خزر کاملا روشن شد: هدف آن پیوند دادن دو درگیری و تبدیل آنها به یک جبهه گسترده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138603" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از بقایای موشک‌های رهگیر که برای دفع موشک‌های ایرانی در آسمان اردن شلیک شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138602" target="_blank">📅 09:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: اگر ایران به اسرائیل حمله کند، چه پاسخی خواهید داد؟
🔴
نتانیاهو: فکر می‌کنم آنها اشتباه فاحشی مرتکب می‌شوند و ما خیلی خیلی قاطعانه پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/138601" target="_blank">📅 08:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز درحین مراسم ختم مرحوم اکبر عبدی، عادل فردوسی‌پور دست‌ سید عباس صالحی، وزیر فرهنگ و ارشاد رو بوسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138600" target="_blank">📅 08:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که پنج یا شیش موشک بالستیک ایرانی که به سمت اردن شلیک شده بودند، رهگیری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138599" target="_blank">📅 08:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138598" target="_blank">📅 08:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwEX3BvCfLhEtpsix_w-2yvMTtEJP11AeR_Vb7hndUstVco4YIGCErbhdoBJVEQ6r2stzh79ZplEBU6U06ug-Z0a77EB9OpTArWS4G728ILuId4cnv0Qdm01NW4A5ajJoHOcw32Gd3hBEucsmplWSEKHIB3kHA3gYFGCEXFiweVrMUhq94GKuhiw2xKgQjdQ-MvWqsy_6dh51qvsvkJjF2EXqUOo59dxzaRLThAZEFT2ZJT5DBFm-BpGe5zKEvrUumL8HZa6YotzK-P9FpwjCIKecGHN-YTZV0sFZQacXBcJEp6zmUqOIM7s8rhCWwAEmZd_YfAYTZhh4avbiZBneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنت‌کام): ساعت ۱۰ شب به وقت شرق آمریکا در ۲۹ ژوئیه، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
🔴
دارایی‌های فرماندهی مرکزی ایالات متحده (CENTCOM) ده‌ها هدف سپاه پاسداران انقلاب اسلامی (IRGC) در ایران، از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های نظارت و دفاع ساحلی و قابلیت‌های دریایی را مورد حمله قرار دادند. هدف از این حملات، کاهش بیشتر تهدیدات ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه خلیج فارس بود.
🔴
در ۲۸ ژوئیه، نیروهای سپاه پاسداران در یک حمله غافلگیرانه، چندین موشک بالستیک را از ایران به سمت نیروهای آمریکایی مستقر در خاورمیانه شلیک کردند. همه موشک‌های ایرانی با موفقیت رهگیری شدند.
🔴
بیش از ۵۰۰۰۰ نفر از نیروهای نظامی ایالات متحده در حال حاضر در خاورمیانه مستقر هستند و بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138597" target="_blank">📅 08:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnOnBDz3hgSglpn9iLfJZZTBM_QdOFOQapW91jGAjWpZK5z-TiKgzhXH5Wmh_PhYnOPuTwWIu4bbRZHIbeAvuRN21LlvPTwWEGgLqczn7pxnHtlgIbe0dtt3zAxoihMZMeThR2B3h3hle9fRRNarYgm2E5oBtqoqOhua7e6eCvE05p16g58Es3dnAuoqwzVKS3FTL9ZVbRNakzm6GUlFjtyXD4J7m90fOYtBP7Q-S8LOdlaeTYfwOCxoGJCbPE8wtHvoKZvh8wYP1DBK6TaDkRgCpCSQiGtT0hrOcHJGXG80BwnmSdmYWybLK_26TtuChiTQRK_229qrZwwjiu8xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: استانهای دونتسک، لوهانسک، زاپوریژیا و خرسون و نیز کریمه را به عنوان خاک روسیه به رسمیت بشناسیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138596" target="_blank">📅 08:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=lF7-h2rvIn2oiNiCrrx2jBkVNrFtZwVV__4_bZNwD0LqEtzCpis3UqUqDfEIUbH6e4AJeEfbu_-1iRxhLXajM3jJayfGrie7v4DTPd8fHH-T6Ff00ZWDncR9hgXEVxX9zglQrH_9Dktlp8SOvtay9O33kcJuXixl9o_3zTL4cE5G7EBWmwZ1kVJEk-yKR7xUMQfZn8Bl2CxlkhmApugp0G3WBq-0b58quq1QYjIezzCMtRpCptZ4dA1SRJs0DWwJPXULs9DXHlEs3Qzpou-L2fg4gF5m_CWiV4Sy7zxcFzgwY7Y8j1NU-PpqwlNZOob4AGVOa10pCUleHaygGTl6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=lF7-h2rvIn2oiNiCrrx2jBkVNrFtZwVV__4_bZNwD0LqEtzCpis3UqUqDfEIUbH6e4AJeEfbu_-1iRxhLXajM3jJayfGrie7v4DTPd8fHH-T6Ff00ZWDncR9hgXEVxX9zglQrH_9Dktlp8SOvtay9O33kcJuXixl9o_3zTL4cE5G7EBWmwZ1kVJEk-yKR7xUMQfZn8Bl2CxlkhmApugp0G3WBq-0b58quq1QYjIezzCMtRpCptZ4dA1SRJs0DWwJPXULs9DXHlEs3Qzpou-L2fg4gF5m_CWiV4Sy7zxcFzgwY7Y8j1NU-PpqwlNZOob4AGVOa10pCUleHaygGTl6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی:
اکثر مردم دوست دارن جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/138595" target="_blank">📅 03:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بندر کنگان رو زدن</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/138594" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جروزالم‌پست: جمهوری اسلامی ایران به منظور بازسازی نیروی نظامی خود، موشک‌های دفاع هوایی دوش‌پرتاب چینی خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/138593" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سیریک رو زدن</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/138592" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اهواز رو زدن</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/138591" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIWcjlX8XuJg6VXAGqLCE31hlosqfJDXoM2AIZtF7bBP3qX6He4lcOGhYhwW3Fum-neuH3Tw2erExKgW-v2QMP1QDZ793upB1hOZYMTW2LABTyIe9jy5f0knlLu9FVV_76aGpyg_PqZOVvL91TEuskZyWxzFwfkT2Wt0LSWAassDcpiwMDkGuN2vveRrrXqQ85owiFWCXII7FVHb1Y8OBPB7qnZP4xIli6LZqU1VyHdINn2fx7ui46gTijlnNo-rSzornLj-LtxmM54xc8l79qTgGmYSRk3R9FrTDiKBMv1J6n1ZEIEXGqtw5tp5iPrwSRlFkle8q2UJ5U2dyh4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/باراک راوید: حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/138590" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش برخی کاربران از شنیده شدن صدای انفجار در فریدون کنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/138589" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارش های محلی از وقوع انفجار های مهیب در نور آباد، فارس.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/138588" target="_blank">📅 02:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال استریت ژورنال: دریادار برد کوپر، فرمانده فرماندهی مرکزی آمریکا، گزینه انجام یک حمله هوایی شدید علیه ایران را طراحی کرده که ممکن است تا دو هفته به طول انجامد و هدف آن فلج کردن توانمندی‌های موشکی ایران باشد، در حالی که ترامپ در حال بررسی میزان تشدید تنش پس از حمله موشکی غافلگیرکننده ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/alonews/138587" target="_blank">📅 02:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زائر اربعین:
پشمام اولین باره میبینم یه آخوند داره کار میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/138586" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=nzcp8Yu0ZxRyeq1zafoFY41CsiOzXNU-EMrOfyMHoMlyVVmg2cm9jCy6TXLU4NVNcImIk540IKSizE7WAjbPLrjk7yaP-XkmV9OhQAwsP8rFCDRBJZm5dmTFKdeyrzgkuIB4yWJHXZz8HdJzLonYC49qm438UBQuGuaJuDfu1NXPke8qtE2Ed43gE5JyTAmfuBUVJW-E6f7ppuxxt701BpRWKYiyrcL7gj-SUEuFlySr1SnQ1SjzBKTtnAa3L7zGFOqiHHnsI3mMusQMvzBzxMJYhSOfeqLU3YFXi-9GPq3CWCjFdOoXr4yJvh_IbWXtekgBJdABGO647F8WbTUqFA7B-xcBHK_NIcgm7OQGMr5b8WTOH6E0tObjT-03FuqitBAXOP7SaCu3wgbml7rbPPbHlo_8AHtZBCiIdoyE4qRwIKXKSyHD29f8VtGQ9nhYrMhbEBOpxhmLecJZ4yQvqiAH9G0nMpjC5TSxS9zWgOSiSgEFS83Xc7FtxFWgpkhs8H77sYFWTqTfiDfq_TSYbcRdBsh6sLuTicUHW1X-h5mj4ednqUHZUcdr4egqeQh6vB1az-lv-_ztGBonNvshNMizpWRzT93DzioVgrMENFSIRgc6EFl6gB9yj90LOoorSLSMpT1_Oilr8Fs74szW4rrLpZZUnR_UcK67MjUCq1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=nzcp8Yu0ZxRyeq1zafoFY41CsiOzXNU-EMrOfyMHoMlyVVmg2cm9jCy6TXLU4NVNcImIk540IKSizE7WAjbPLrjk7yaP-XkmV9OhQAwsP8rFCDRBJZm5dmTFKdeyrzgkuIB4yWJHXZz8HdJzLonYC49qm438UBQuGuaJuDfu1NXPke8qtE2Ed43gE5JyTAmfuBUVJW-E6f7ppuxxt701BpRWKYiyrcL7gj-SUEuFlySr1SnQ1SjzBKTtnAa3L7zGFOqiHHnsI3mMusQMvzBzxMJYhSOfeqLU3YFXi-9GPq3CWCjFdOoXr4yJvh_IbWXtekgBJdABGO647F8WbTUqFA7B-xcBHK_NIcgm7OQGMr5b8WTOH6E0tObjT-03FuqitBAXOP7SaCu3wgbml7rbPPbHlo_8AHtZBCiIdoyE4qRwIKXKSyHD29f8VtGQ9nhYrMhbEBOpxhmLecJZ4yQvqiAH9G0nMpjC5TSxS9zWgOSiSgEFS83Xc7FtxFWgpkhs8H77sYFWTqTfiDfq_TSYbcRdBsh6sLuTicUHW1X-h5mj4ednqUHZUcdr4egqeQh6vB1az-lv-_ztGBonNvshNMizpWRzT93DzioVgrMENFSIRgc6EFl6gB9yj90LOoorSLSMpT1_Oilr8Fs74szW4rrLpZZUnR_UcK67MjUCq1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی بعد ۱۵۰شب کصخولت در میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/138585" target="_blank">📅 02:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار را به لاکهید مارتین اعطا کرد که بزرگترین قرارداد تاریخ برای موشک‌های دفاع هوایی پاتریوت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/138584" target="_blank">📅 01:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روسیه چهار موشک بالستیک ایسکندر-ام به سمت کیف شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/138582" target="_blank">📅 01:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آسوشیتدپرس: ایالات متحده تمام مذاکرات را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/138581" target="_blank">📅 01:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مقام ارشد آمریکایی رو رویترز:
دولت آمریکا فعلا به دنبال ادامه مذاکرات با ایران نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/138580" target="_blank">📅 01:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش کاربران از صدای انفجار در بوکان
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/138579" target="_blank">📅 01:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه خبرگزاری خارجی: رضا پهلوی این هفته تو واشنگتن با نتانیاهو دیدار خواهد داشت  @TitrDaily</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/138578" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
رسانه‌های داخلی فعلا انفجارها تکذیب کردن اما کاربران زیادی گزارش شنیده شدن صدای انفجار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/138577" target="_blank">📅 01:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=ZWrD6Xw4wcJGeaoz-Bzg4-hJhfcDPY_tHStSkG3GniMx1RraOyg4O59qApFcQcuQ4Qf-IOm_5heLujjFOCrutqDLY2-lL6raIItBM8YLt6KVgU9wA9Zblqh0Sq21PZmQ4-Tn2NnY896dmuLPZIHcoW9_WEpb1P8li2KuA0qqNAytzR7-lBVd6szUifiWyNvJ2t1b8JdmJdmh_m3QeQ28PMmGX8yjj-SNv3NpkRe1mI7IMAlznqd5ys1Xjp0VetZ02flsYvK49eMLiiYIJZs4DLNP8I3qLmfas6cU-Hf5lLzq2OWSbP-YszMjwPUt_c4uh2-uNEQqveC3dwBCp4WrFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=ZWrD6Xw4wcJGeaoz-Bzg4-hJhfcDPY_tHStSkG3GniMx1RraOyg4O59qApFcQcuQ4Qf-IOm_5heLujjFOCrutqDLY2-lL6raIItBM8YLt6KVgU9wA9Zblqh0Sq21PZmQ4-Tn2NnY896dmuLPZIHcoW9_WEpb1P8li2KuA0qqNAytzR7-lBVd6szUifiWyNvJ2t1b8JdmJdmh_m3QeQ28PMmGX8yjj-SNv3NpkRe1mI7IMAlznqd5ys1Xjp0VetZ02flsYvK49eMLiiYIJZs4DLNP8I3qLmfas6cU-Hf5lLzq2OWSbP-YszMjwPUt_c4uh2-uNEQqveC3dwBCp4WrFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز تو مراسم ختم اکبر عبدی، عادل فردوسی‌پور خم شد و دست‌های عباس صالحی، وزیر فرهنگ و ارشاد رو بوسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/138576" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش کاربران از انفجار در ارومیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/138575" target="_blank">📅 01:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138573">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/138573" target="_blank">📅 01:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138572">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/گزارشات از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/138572" target="_blank">📅 01:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138571">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab42f37f.mp4?token=R8rtksZw0FSjzvrun2wKvwsiMcE4sVt-4INhHQN0JQqKlD6mmKsRdmiBI4wt6zvyeRYBtuseP9Gt92ylFpudZKQ4EMP1JY5Fvl9F6eywHCgu4RxkOAkOkhOOa2REqKkT-VS1M7ZzGfcU8HMwP3x6nxUk9nJotpwwiZ2ohztr4KEMFPKuM3xPQmEayoJWC230DlJ9xbSe5PHDs6fApPJT2GJRp-fkRwUcKSKhhkLlhzy6JHPN1i197WOX8Nyk0dWBbOpjOqXV0m-FK44zqeNWaild1A5K3VRvfTo_oJ53sb6BnpanwWJv243ggQp7m0M6f6iqXG8j_T9Xl0akbOmCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab42f37f.mp4?token=R8rtksZw0FSjzvrun2wKvwsiMcE4sVt-4INhHQN0JQqKlD6mmKsRdmiBI4wt6zvyeRYBtuseP9Gt92ylFpudZKQ4EMP1JY5Fvl9F6eywHCgu4RxkOAkOkhOOa2REqKkT-VS1M7ZzGfcU8HMwP3x6nxUk9nJotpwwiZ2ohztr4KEMFPKuM3xPQmEayoJWC230DlJ9xbSe5PHDs6fApPJT2GJRp-fkRwUcKSKhhkLlhzy6JHPN1i197WOX8Nyk0dWBbOpjOqXV0m-FK44zqeNWaild1A5K3VRvfTo_oJ53sb6BnpanwWJv243ggQp7m0M6f6iqXG8j_T9Xl0akbOmCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب عروس و داماد جلوی مهمان‌ها در یک عروسی در نیاوران تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/138571" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کارشناس صدا و سیما: الان چند ماهه انتقام خون آقا رو هوا هست، لطفا انتقام بگیرید دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/138570" target="_blank">📅 01:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">کاش اینقدر که برای مجازات جوان ایرانی قانون دارید برای آینده‌اش هم برنامه داشتید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/138569" target="_blank">📅 01:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55b2320513.mp4?token=tvBAtGeK7CKOskDrFLoAn_jrlkWDKYdJQLXEnpggH-lYnpi0YdhidmnLR33EtspZHg6JxO73Mj0KvTfLEAqdGWl3HvnI90yHhhScMdNYXAU6S08mav_bMCWJ8CD_iXL1uxNTVgvWsAB1iLXVFUf5C1RDNhfhNLH1QypuQ9ZRyGQivqBDpkkm9cPlvDLE8j4XJ6fSyffbIPh0-4witBlkdKK9gpgmP-XzKd0EgtC50fXG1TdBMO7JTFJdGpJBYaN5MzApOglwRbdca5YXOpqJkfbeS2eEW1I8vvzGjWJ6tdHFrKEm6d1PElw-yHAkBnacqR8U0aZzD8v1gb05STcVQ0sO4Aci5WvSkPl8v5IOUm9ZWXG4Y9_nczgollYCdtaok1u_ZMXRj7RwHW3w63WUtxd_hIsRX4zyngwKAo71xD-PL_tdbOz8-09WrdHdrVWb4OPBfakcBCX9mXr1J88G67Z4yQfYrHS0e2Z7W985371OyTUpCS0tNq953vhPTWEtWXbCBPreEuj4tuPL3byC94vhQVzR-Bk-CUWYfkTFu9BHv8gjQqnSLMwmWsHj2dOTeNlngg3W54HYMEYQaIk3VzcIWGJCJUP_OAPJ-po9NeuoPg_TPo26imdACya721wO948Z-3ZjwGmhl4NdghCLMIYdyj6qwp87HH4z-Gek6mU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55b2320513.mp4?token=tvBAtGeK7CKOskDrFLoAn_jrlkWDKYdJQLXEnpggH-lYnpi0YdhidmnLR33EtspZHg6JxO73Mj0KvTfLEAqdGWl3HvnI90yHhhScMdNYXAU6S08mav_bMCWJ8CD_iXL1uxNTVgvWsAB1iLXVFUf5C1RDNhfhNLH1QypuQ9ZRyGQivqBDpkkm9cPlvDLE8j4XJ6fSyffbIPh0-4witBlkdKK9gpgmP-XzKd0EgtC50fXG1TdBMO7JTFJdGpJBYaN5MzApOglwRbdca5YXOpqJkfbeS2eEW1I8vvzGjWJ6tdHFrKEm6d1PElw-yHAkBnacqR8U0aZzD8v1gb05STcVQ0sO4Aci5WvSkPl8v5IOUm9ZWXG4Y9_nczgollYCdtaok1u_ZMXRj7RwHW3w63WUtxd_hIsRX4zyngwKAo71xD-PL_tdbOz8-09WrdHdrVWb4OPBfakcBCX9mXr1J88G67Z4yQfYrHS0e2Z7W985371OyTUpCS0tNq953vhPTWEtWXbCBPreEuj4tuPL3byC94vhQVzR-Bk-CUWYfkTFu9BHv8gjQqnSLMwmWsHj2dOTeNlngg3W54HYMEYQaIk3VzcIWGJCJUP_OAPJ-po9NeuoPg_TPo26imdACya721wO948Z-3ZjwGmhl4NdghCLMIYdyj6qwp87HH4z-Gek6mU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمادالدین باقی: چطور میشه برای یک جوان ۲۰ساله یه روزه حکم اعدام صادر بشه؟ ظلم‌نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/138568" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u7yqM4mb4BhNl6VjMCndSFnCBskd-9Abr2GdOevQlwUCo-trwg6zSFnaVi70JcceevYPrMXbsVFIexHpB8Jn6SR_FJ2IX14SsTvIhCOegcTpIiq8t3j5cXkJ4MoQ7QzEKRTlFbMhiuYUSnDaGO7tvgJ888hq9VIT89JuD8ImiLRuDsfdbCc5y25DjRdMZb2bKDWR7XEr2e_jmnTjzaZ1V2FeQ9qCvfCbmhiR1D2ffy4NMiXTKaSz0UH0Gi7Ua7vF3Z44o5h1_R0X6wDD0M33hC06Y2pfJqAWHdEeB1_9SySzuLxHzFDNZrWivmgAJCJH5eVWIP5UhbHN6_OLXT0FyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u7yqM4mb4BhNl6VjMCndSFnCBskd-9Abr2GdOevQlwUCo-trwg6zSFnaVi70JcceevYPrMXbsVFIexHpB8Jn6SR_FJ2IX14SsTvIhCOegcTpIiq8t3j5cXkJ4MoQ7QzEKRTlFbMhiuYUSnDaGO7tvgJ888hq9VIT89JuD8ImiLRuDsfdbCc5y25DjRdMZb2bKDWR7XEr2e_jmnTjzaZ1V2FeQ9qCvfCbmhiR1D2ffy4NMiXTKaSz0UH0Gi7Ua7vF3Z44o5h1_R0X6wDD0M33hC06Y2pfJqAWHdEeB1_9SySzuLxHzFDNZrWivmgAJCJH5eVWIP5UhbHN6_OLXT0FyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید جلیلی: نفس دشمن به شماره افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/138567" target="_blank">📅 00:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/رویترز: نتانیاهو پیشنهاد ترور فرماندهان سپاه و ارتش را به ترامپ ارئه داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/138566" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
هم اکنون پرواز تعداد زیادی سوخت رسان ارتش ایالات متحده در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/138565" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138564" target="_blank">📅 00:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/138563" target="_blank">📅 00:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانال 15 عبری:
آمادگی‌های آمریکا نشان می‌دهد که طرحی برای یک اقدام گسترده علیه ایران وجود دارد، و نه صرفاً یک واکنش جداگانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/138562" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsheMIND0zHj7sF49KnJiZXOrVgcwt-wyEB-c1RjLPuxSxAJUfHzHgoz7tLQZDeF_oOH7hhW1ms8hqutB0Rk0ipJDChq7Wld55e9diVltLCbaXac9K7ijDpNNOpKF9JMRhwen35gfDzqp-PJRvw_jPgpE9inFQ7J1I-yqAq9h1fZw2bYan7E369dKNDYVWdvOKihlgh0ammhk20SuJVtk5awvia34EL0ix6VH5CHQ2jzHAwrH3q5Vm6rR62IywxVzltjYxJUFzQ28-AXsHswKnMYHfEGmEhtfioicLgVXd5WortsvP4rsOi3C5-uTVkn4gnt39n9XYRD1F0MwzmmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مجری: عموی عزیزم‌ محسنی اژه‌ای بابت اعدام‌ها دمت گرم
🔴
پ.ن: جواب با شما  #عموی_سوباسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/138561" target="_blank">📅 00:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/138560" target="_blank">📅 00:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6LNXkO-6ytxYWmfdesJ9HBvbvjLcHUBcbYaXATcbFd12nSYuMUMaNWi8Ns3iHEjkWO8r9hVPZkvDTyQczOiASMpUzdERyHDKjXrjcv3Du0hK6QtgRdTaoJrBi1NPW0XrOeXOYy5Ker-_bWKr_5st28Ahl2sLGzkKXILJ0VIqMXkSuSfC3dJ79NHugdACdYbtwElnzXgFSqxd4G_CgYmxEiD040x_Gep-SjkCfSd7R2PRdK3plrh5pp2xDRx35C4VpIauDj92GYn2iAt26lsowpp1Kup7qEWKyiD3IsdjFCfwcaegczGmn27EM-fBafEWllPvH5oJ6r4nTS3hQrqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال محسن رضایی: برآوردها حاکی از درگیری شدید و قطعی در آینده نزدیک است
‌
🔴
جغرافیای جنگ از همین حالا در حال گسترش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/138559" target="_blank">📅 00:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0JsU9OFdyLwK1NR1mPN7uRysoaMgKfsHE5TEPYtpAtvZgQ1XPyXi9oO0o6FF-jrYZpR9lo5QcdrvaMKMEf9c_F_JHS5u0N4EJvdyokyX1pHNRGexbRpNQZ36eYNeolzr-OwmGcAf_1XmNHpPzWeKybLWmvmFUwUI56ySJ0iotwlcYWUG2isuQGhcnndi2PlHlk0ALzS5IxY6Y0Na_Ob0pR7EO55Ksgbg4fB3WLzVb5wR59Xd9ehgdM0F645E8lc0yAapMKUgf70lj1Vg-UrDlSQPWYTjCp6Pq2_epbePcjZNVQ8gJ3gBdfBgh1HYdZEtXOphCoWg--j4TGBjot77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود سنگین کشتی باری در مازندران؛ مدیرکل بنادر هرگونه انفجار را رد کرد/دود شدید مشاهده‌شده، صرفاً ناشی از راه‌اندازی اولیه موتور این شناور بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/138558" target="_blank">📅 00:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شنیده ها حاکی از این است که علت احتمالی عملیات غافلگیرانه شب گذشته هوافضای سپاه علیه اردن، تلاش برای هدف قراردادن ژنرال دن‌کین، رییس ستاد مشترک ارتش ایالات متحده آمریکا بوده که با توجه به حجم انبوه شلیک پاتریوت جهت رهگیری، می‌تواند حقیقت داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/138557" target="_blank">📅 00:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138556">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxETp9npNd7Q5A7-M86TIHWdpUYmVhTdnRJZQTxJATUS4V3VizJ2TYW2WJQOyDaGjphayJI-o8mFEs7blsEDEXESS9l2nV2wGKUgx26b79ivPl1qqZTHFcUg07Sxah9Nlc-I_KB_Y43E08gHOGMi0lX3jE_vYBIyZLln_YL5OCx3U1gLz3D5FL67VEY4CIdkqg39_-PCOuoLKVZJv0z-SsEW83zvLEgd6teW2WVHeXCmh9XxsitGkJ_8WUaWz-PumQgvy7SbrZKUk9O20_8QD5psoIeXQQ89QjTSQt1bqkORCY4n8vuvt5QfqDJ_KytDX1Nb4U7QdE54f65snEvQlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت تعدادِ بالای سوخت‌رسان تو منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/138556" target="_blank">📅 23:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138555">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری / رسانه کان: حملات احتمالی آمریکا دیگر تلافی جویانه نیست و گسترده خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/138555" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138554">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
حساب کاربری روابط عمومی سپاه در تلگرام بسته شد!
🔴
سپاه در پاسخ: بستن حساب کاربری روابط عمومی سپاه در تلگرام، نشانه‌ وحشت از داده‌های دقیق ملت‌های آزادی‌خواه منطقه از مواضع آمریکایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/138554" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138553">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آی ۲۴ نیوز به نقل از منابع آگاه:
اسرائیل فشار قابل توجهی بر دولت آمریکا وارد کرده تا «عادی‌سازی روابط تل‌آویو و ریاض»، به بخشی از توافقات برنامه هسته‌ای عربستان تبدیل شود
🔴
نتانیاهو می‌گوید می‌خواهد پیش از انتخابات، به «دستاورد بزرگ بعدی» دست یابد؛ یعنی عادی‌سازی روابط با عربستان
🔴
ترامپ هم در این مورد گفته «این اتفاق مثبتی است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/138553" target="_blank">📅 23:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKzqkbSvRmJ6y_eSMGzXHhup9a6Z7EFXCa9OLSq9ZEdw1PjAbSZhQ5WUaJvzc-K4QZbgPni0NEq2B8tuQyrYF_F1sGLrNYTzAnuyG-CYNOMQKbaQCzVWstaBpwIpmGxur_DuF3ALjZV02tAqSR4SsOKJ_uUmPS3K1sJYi4EE4PlTYO7FGfP0LZ8wSSYaAZ1l9lo3Z8ZWnX7qaSd60Ac7SQH6J6l8xl8KffEm7jPWjbdRo0cSVD7NRSCsuJct-aZlMZi5O22Byp9qJvny0SH8Y4YOW0e5oUvAe_Xa9s7i0mcfhX72JEwojLoPWt4O9CUPrRH6myAc90kP83fgHdDOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🔥
مسابقه بزرگ شهر هوشمند
🥇
نفر اول 500 دلار
🥈
نفر دوم 250 دلار
🥉
نفر سوم 200 دلار
🆓
نفر چهارم وپنجم هم 100 دلار جایزه
به هم پوک بزنید فالو کنید
پوینت کسب کنید
◀️
لینک مستقیم بات
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/138552" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک منبع غربی: منابع آگاه از مذاکرات می‌گویند عربستان در حال تشکیل ائتلاف بین‌المللی با هدف حفاظت از مسیرهای کشتیرانی دریای سرخ در برابر حملات حوثی‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/138551" target="_blank">📅 23:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nanyAbRuwctYLa4H-bpGOI3jI4GcTFpSOtkNDvI1-lLiQ3i2XqLu1AAIdm4cy0rUopjDXRsdQ5tiVRXd0iZbUFzhfz0D3_iyDOkAq9JCP9_AJ3liH71KFZ--i4Vx9h1iTn6ItJmw9oC5uiYzdFA6BDwox5ELVsnBoVxCqQvHZYDLzu_f1L1qFoAGVLJBIfbhl6ptIX3FmGtTS47VoV5Bf72bVXpnJ0zEpWE2D6uiPz0EELCvxUxksE4jpL7Gy4bd7oLe8xGWwxis1zcuHRYZjJ4Tki-7U-HS2ItgO25hnt6KCrATFoG8d5Y5pI1pl-CsdcRIRN-ReTEQclAIe7DSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / العربیه : ایران برای ادامه‌ی مذاکرات تو ژنو یا دوحه، به پاکستان اعلام آمادگی کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/138550" target="_blank">📅 23:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138548">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flqLSmv3Ou_dWKtZaRySJbmicRBYk1qbzBm16K0SvOCwIUAWGzc7fGJtnC_-IgVMANwRi346rybO9lqDA5M7FGEOY9rJlyIbLjIuiYu-Yrv1m8ywqfp-yfjZI7uIF9d33l3zG0um9N3vCZtiWV38xrmIbBT-Jzrh7DE0rnaamq-aCMf-8ZJXre2_MWEqvEjbgBUzLxoVtkzYO3kt5GbJ6quPE-k7ruA9cgu8jG4uP8GQ-dwx6X1sE9p7KmF_sc29XpdrWE3cZ40coBNaKM1s14ggwQ44M8Ji1YHf4PVpfaT4p5Zgv7AII6g-ssJyAAOpxtnElqbRkdzz8b2N6HyLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1_LblII0e3QKlNQfFMILFtgM5jsLNf4L5kxfBO1Fi13SFxmL0452AV8ljXgMwpZkdJw5BzOk1XGitH7Q1YcULqhIkAV1GJlzwclaOlJ46BURKIcLPrNRCyNWSKBwt2c1nY7NskW2Yxsaa7x_zUtEpMzb3GpQ-OuD-SrUuPTButt-PhK-Pjv7uqz-U7Eku2SBop0bx67VUq1PgYQa7lYN1W_EbcudVzPZgauuve1BX7FMinXd_gjUUX7Tpydz-jNXxDe4pzcwh0XJ1SI6AYh77mvey-Tb2mYhjpeLfVrMIYs97UXOjivzF7TtyyLbh8SjYqCDR2rFSxsKTrcUapYKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسانی آمریکایی از پایگاه هوایی شاهزاده سلطان در عربستان سعودی به پرواز در می‌آیند و سایر هواپیماهای سوخت‌رسانی بر فراز خلیج عمان فعالیت می‌کنند، در حالی که هواپیماهای بیشتری از تل‌آویو به پرواز در می‌آیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/138548" target="_blank">📅 23:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138547">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9b9b5a89.mp4?token=omNhJ8jf2qaNRZroDjsdD0DNxpOyerHj2CxFxeUsbOyC9XwGmzZB5-MxZvyIe796Vc3B3HSgQFkXpnlSBzmA3NcpACWgWWARbeC0XaTD1y0DCpioLA-s7Zu_p8FBtuqoMhn8yDa0WqgeA-Jd0ejq-rq_B2apFlTqfIy18KXBm4iGEdhX7BYXDdwMKeWBzWIEQHVOcOenR-WiDWEoF_9ptqFlK0Zv0uxfGbST2D5Y_QaNhxUKGI-lVm41GrY9VfxaMuRq81suoWs7tSFxs5v2xpqXz76kMmWjasX8_Fgqs6_KtCIcqmyIpZqzgJagU8BaiYMv2ie2SDjPB81QDMod_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9b9b5a89.mp4?token=omNhJ8jf2qaNRZroDjsdD0DNxpOyerHj2CxFxeUsbOyC9XwGmzZB5-MxZvyIe796Vc3B3HSgQFkXpnlSBzmA3NcpACWgWWARbeC0XaTD1y0DCpioLA-s7Zu_p8FBtuqoMhn8yDa0WqgeA-Jd0ejq-rq_B2apFlTqfIy18KXBm4iGEdhX7BYXDdwMKeWBzWIEQHVOcOenR-WiDWEoF_9ptqFlK0Zv0uxfGbST2D5Y_QaNhxUKGI-lVm41GrY9VfxaMuRq81suoWs7tSFxs5v2xpqXz76kMmWjasX8_Fgqs6_KtCIcqmyIpZqzgJagU8BaiYMv2ie2SDjPB81QDMod_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا شما می‌خواهید که مجلس نمایندگان قبل از ۳۱ اوت برای بررسی و تصویب طرح تحریم‌های روسیه و ایران تشکیل جلسه دهد؟
🔴
ترامپ: به طور خلاصه، این نباید ضروری باشد، اما اگر ضروری باشد، من مایلم که آنها ایران را نیز به فهرست تعرفه‌ها اضافه کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/138547" target="_blank">📅 23:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138546">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104ed50ea0.mp4?token=VqNaxYv9kVpjWhGD_s06yxOoygGgYMai0vT9SBUX_uF6xlHqxqU8CKh8bFsv2slHYLcWe6Lbrj_HRJ2suSiSK-67X6Lv9nF2patNfhU2gKQnmTF5QycAuv5ZUHqh-Ix_ps5X_U_BCxIZI-4bnJgE8dl7IH01HhqtVDxCFihp4mYwvCnPqbyG3jimvsZpxNBYbJfOWwpeEZdSaGsll2f1hDI8mw5qEijT_rul4tM41PbDrFpp2jfoGrmFOq8UenTLpBef_OwmNjSvclYQ4qQ2h2yiZ_4IhrBdK7nf7IMWbgX8-PdlEhm6ZqUh7XgFHG7iCzvDMoTICYH6uSPyEId5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104ed50ea0.mp4?token=VqNaxYv9kVpjWhGD_s06yxOoygGgYMai0vT9SBUX_uF6xlHqxqU8CKh8bFsv2slHYLcWe6Lbrj_HRJ2suSiSK-67X6Lv9nF2patNfhU2gKQnmTF5QycAuv5ZUHqh-Ix_ps5X_U_BCxIZI-4bnJgE8dl7IH01HhqtVDxCFihp4mYwvCnPqbyG3jimvsZpxNBYbJfOWwpeEZdSaGsll2f1hDI8mw5qEijT_rul4tM41PbDrFpp2jfoGrmFOq8UenTLpBef_OwmNjSvclYQ4qQ2h2yiZ_4IhrBdK7nf7IMWbgX8-PdlEhm6ZqUh7XgFHG7iCzvDMoTICYH6uSPyEId5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اما گزارش جدیدی می‌گوید ایران قرار است ۴۰۰ پرتابگر راکتی از چین دریافت کند.
🔴
ترامپ: اگر چنین باشد، برایم تعجب‌آور خواهد بود. او به من گفته بود که در این موضوع مشارکت نخواهد کرد.
🔴
او می‌داند که اگر این اتفاق بیفتد، من به‌شدت ناامید خواهم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/138546" target="_blank">📅 23:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138545">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56586855d6.mp4?token=Z0dJBogQ1tp3xNeeAF6A9RqVitSUzUJD9frSEV_f7kE385_zFf6EK_PwaK7rSXLfwNb703IVE8MEG6mlfRx4_4mjEC5-3ma9kkQkHGLMj-P6neSjhEmk1UI5biNdybGCZNLhoCEK0f2WFrWsTxBQpNl19pZGFtHfyFUJuOKzcYWF3K-lSSbjgtQsdR2qk1m5zBZefEgesKD7c9pTa6N7Sh3N6EYH7o2_y7oVIEN97bTzXlQiQfyuOv4OtXAPj4ND588hjiX0gvY3X-yPE0uXaPO7W_J6t_iSRXy4YMKoXdOArvQv6MklDdYgf3-jhmobaxYl5I2ajb0t5O0Jtfuq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56586855d6.mp4?token=Z0dJBogQ1tp3xNeeAF6A9RqVitSUzUJD9frSEV_f7kE385_zFf6EK_PwaK7rSXLfwNb703IVE8MEG6mlfRx4_4mjEC5-3ma9kkQkHGLMj-P6neSjhEmk1UI5biNdybGCZNLhoCEK0f2WFrWsTxBQpNl19pZGFtHfyFUJuOKzcYWF3K-lSSbjgtQsdR2qk1m5zBZefEgesKD7c9pTa6N7Sh3N6EYH7o2_y7oVIEN97bTzXlQiQfyuOv4OtXAPj4ND588hjiX0gvY3X-yPE0uXaPO7W_J6t_iSRXy4YMKoXdOArvQv6MklDdYgf3-jhmobaxYl5I2ajb0t5O0Jtfuq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من مایلم تعرفه‌هایی علیه ایران اعمال شود.
🔴
لیندسی این را می‌خواست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138545" target="_blank">📅 23:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138544">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813e2cc66.mp4?token=Eke-idtElPVdJeZzL0MGDTz8OMqiXY8ojkhMS-by--BxZkmjswQNuQTMLoXbjVsjzXhSz1-n_VSTiPbTJUBpJWvU_K7uFQBcl8pbpAXnk16TtPbOigVJm8AKMHR8lhcgRUSBmay_PWM123Mholnfcj_LN0yWllmo0XqjUBwj6JdO6SF6kUqMylgcPeGFG-fyJPFT9Al-IUqmG_FhHRRjyaQ72sj_2C7met6NWO1LxwjtVP7IkiTsKW_2YADJhjvCu77XuBQK8Zm_VjAVIHHoOhLiX39RETh5brt8bqzkcKbpWk-FGKkNU44Up8_gBYzgH7sdCqUwG20sIWV7nUxNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813e2cc66.mp4?token=Eke-idtElPVdJeZzL0MGDTz8OMqiXY8ojkhMS-by--BxZkmjswQNuQTMLoXbjVsjzXhSz1-n_VSTiPbTJUBpJWvU_K7uFQBcl8pbpAXnk16TtPbOigVJm8AKMHR8lhcgRUSBmay_PWM123Mholnfcj_LN0yWllmo0XqjUBwj6JdO6SF6kUqMylgcPeGFG-fyJPFT9Al-IUqmG_FhHRRjyaQ72sj_2C7met6NWO1LxwjtVP7IkiTsKW_2YADJhjvCu77XuBQK8Zm_VjAVIHHoOhLiX39RETh5brt8bqzkcKbpWk-FGKkNU44Up8_gBYzgH7sdCqUwG20sIWV7nUxNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
🔴
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138544" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138543">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d931d8c3.mp4?token=k_B-2mSFMXWn78YadHvkyPrezXoHy8bNfqIchzuqbmNOlH0awVVfo14eNjy4PB6xXSHHg83nAb710J_eX-NDYGp5-gvnvGpKTr3KSXJvEL0Frqs_BoyLNLYExV41nMc4B91mqbH2RqrK8U_HPJhO4qANkOHFatIvJlLDnQH6e-SsJ1pOWiKFEHZgOB9U9PILNmLzAsTYRFEcVegTNRhDhkhIDLdSR70nci7033GMxmI3HI9poW6p9feczto3OSWS-PjKozYEGoMdIbmtUPqNEFHZoqHjEMiBbCbECmsIBE9PY5TqLOKb5Wkrn4kAvfuEeNsom6-Jl6Ipl9y9j61m_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d931d8c3.mp4?token=k_B-2mSFMXWn78YadHvkyPrezXoHy8bNfqIchzuqbmNOlH0awVVfo14eNjy4PB6xXSHHg83nAb710J_eX-NDYGp5-gvnvGpKTr3KSXJvEL0Frqs_BoyLNLYExV41nMc4B91mqbH2RqrK8U_HPJhO4qANkOHFatIvJlLDnQH6e-SsJ1pOWiKFEHZgOB9U9PILNmLzAsTYRFEcVegTNRhDhkhIDLdSR70nci7033GMxmI3HI9poW6p9feczto3OSWS-PjKozYEGoMdIbmtUPqNEFHZoqHjEMiBbCbECmsIBE9PY5TqLOKb5Wkrn4kAvfuEeNsom6-Jl6Ipl9y9j61m_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال هجوم به اروپا هستند.
🔴
این یک تهاجم است و بریتانیا یکی از اهداف اصلی آن به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138543" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138542">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چون آن‌ها عملاً کار زیادی برای مقابله با آن نمی‌توانند انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138542" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138541">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عارف: پس‌از ۲ جنگ تحمیلی اخیر ایران‌هراسی شکست خورده و اکنون فرصت طلایی برای گسترش روابط، به‌ویژه با کشورهای آفریقایی فراهم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138541" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: اندی برنهام باید درباره مهاجرت صحبت کند، چون مهاجرت در حال نابود کردن بریتانیاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/138540" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0225a170.mp4?token=tdr7QJocGV_NRs-SW31Ct08rHNiAPtbcvbqaXSvtQQuJSIw7aocj2fHbB4RBB3x0fh5p2C4PYtjPw9aclJ4C0LKnn92ZV_oXy6-M96Jt9WgZhlwWWFdmqab4tx35QW1eOlLZa5lfEBJS7hI3gIB9Tae9w8n7QiA66wPT-x30ocTJ-Y8FiKL48ZfyLidNBIqqjyPyFbiyPlPqc0yO8ui7Zz2kIrhWJ0JvusBJCNUdB__8u4HOipWPvo9PHtJJRceF67Ge63zNTy6LQaOrfWIb7FFNcu2uBATJv9dI_Pcd_rASGvL4A7TbMbgY6MbmXTqUFmZtDsCl3bc5zN8nniY1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0225a170.mp4?token=tdr7QJocGV_NRs-SW31Ct08rHNiAPtbcvbqaXSvtQQuJSIw7aocj2fHbB4RBB3x0fh5p2C4PYtjPw9aclJ4C0LKnn92ZV_oXy6-M96Jt9WgZhlwWWFdmqab4tx35QW1eOlLZa5lfEBJS7hI3gIB9Tae9w8n7QiA66wPT-x30ocTJ-Y8FiKL48ZfyLidNBIqqjyPyFbiyPlPqc0yO8ui7Zz2kIrhWJ0JvusBJCNUdB__8u4HOipWPvo9PHtJJRceF67Ge63zNTy6LQaOrfWIb7FFNcu2uBATJv9dI_Pcd_rASGvL4A7TbMbgY6MbmXTqUFmZtDsCl3bc5zN8nniY1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
هر زمان که آسیاب‌های بادی را می‌بینید، یعنی با یک کشور رو به افول روبه‌رو هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138539" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9dd98031e.mp4?token=kV7uo_DpjvzMLbH9Kaz2Xez3F6Uq1g2YrrcAQNhiWQq44uEiP4lTcQ3Q1tEn90u6bi-_-nwlf-Rxg1j8p6R2IfFoKL54_j1yHMyX7fTvNsh_NKzXVF-aB9Fu2sTlrCe2cA_UuwkjvB4kTRyQBcY7qrrHR2dM2RekO-HemmkLI49d3iKYkQ-U4fSIzeXZUbRwohHOBWwiXItB4LkmtcZdyP0cSiqHQdheRxKy510ztK9mg2gF25WEBTeLtZP1-CVGDBaqVns5qFCxS9nu9VQwI-bISg1IvM6iWdi94stZEmoamKIsT7oq52WMNlcO-Hx4mxNJaflWp1dSqJxbrQqn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9dd98031e.mp4?token=kV7uo_DpjvzMLbH9Kaz2Xez3F6Uq1g2YrrcAQNhiWQq44uEiP4lTcQ3Q1tEn90u6bi-_-nwlf-Rxg1j8p6R2IfFoKL54_j1yHMyX7fTvNsh_NKzXVF-aB9Fu2sTlrCe2cA_UuwkjvB4kTRyQBcY7qrrHR2dM2RekO-HemmkLI49d3iKYkQ-U4fSIzeXZUbRwohHOBWwiXItB4LkmtcZdyP0cSiqHQdheRxKy510ztK9mg2gF25WEBTeLtZP1-CVGDBaqVns5qFCxS9nu9VQwI-bISg1IvM6iWdi94stZEmoamKIsT7oq52WMNlcO-Hx4mxNJaflWp1dSqJxbrQqn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ترامپ: آبردینِ اسکاتلند زمانی پایتخت نفت اروپا بود؛ در واقع، پایتخت اروپا محسوب می‌شد.
🔴
حالا دیگر آنجا نفت استخراج نمی‌کنند و هیچ‌کس هم نمی‌تواند بفهمد چرا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/138538" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ:خواهیم دید که آیا در نهایت به توافقی می‌رسیم یا خیر، اما ما قرار است به شدت به آن‌ها ضربه بزنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138537" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138536">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: تعداد افرادی که در دوران ریاست جمهوری بایدن بر اثر کووید جان باختند، بسیار بیشتر از تعداد افرادی بود که در دوران ریاست جمهوری ترامپ بر اثر کووید جان باختند.
🔴
کووید یک فاجعه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/138536" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138534">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87407dbb4d.mp4?token=c771Y2_xYSiPs-MWrrwYhM6ReyQXNTzqorHlSpYnrqU7dIfUNrrS_zhkCeOCVWz6oLavYuLu0pQfazNRV2qBKIhGe_3j-NQEIYin-RhwxeOWkBNQiauNdtp7XLwo6xtkqKMO8EwKyDJZhGg36X7zfYDyf98lsNbdTS25HnhR8Vo7nZTYajvJwJkjN6HOjPqF2xsxSw9rLGhHLos-u4HTe8uMiIMzLuol1LCZj7XCBvxPr_OYEPuTZf1S1KVKXSsQayGzsaX2H5inXP755LtdcYBjyaWpYf9KtQFXOmD1-Azvl1vJJ3LF-bgsEty_vazPodnW_7hMsP5dasaKQ1M_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87407dbb4d.mp4?token=c771Y2_xYSiPs-MWrrwYhM6ReyQXNTzqorHlSpYnrqU7dIfUNrrS_zhkCeOCVWz6oLavYuLu0pQfazNRV2qBKIhGe_3j-NQEIYin-RhwxeOWkBNQiauNdtp7XLwo6xtkqKMO8EwKyDJZhGg36X7zfYDyf98lsNbdTS25HnhR8Vo7nZTYajvJwJkjN6HOjPqF2xsxSw9rLGhHLos-u4HTe8uMiIMzLuol1LCZj7XCBvxPr_OYEPuTZf1S1KVKXSsQayGzsaX2H5inXP755LtdcYBjyaWpYf9KtQFXOmD1-Azvl1vJJ3LF-bgsEty_vazPodnW_7hMsP5dasaKQ1M_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا اندی برنهام همان فردی است که می‌تواند بریتانیا را به سوی شکوفایی هدایت کند؟
🔴
ترامپ: او یک حرف بسیار خوب زد؛ گفت که می‌خواهد استخراج نفت از دریای شمال را آزاد کند.
🔴
اگر این کار را انجام دهد، بریتانیا به کشوری ثروتمند تبدیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/138534" target="_blank">📅 23:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138533">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991ae12297.mp4?token=lq6LeKFs5ANaaR2J0f0HPzkYFZipAw-gePdQvdE0YuQVe-qE2yp43xwQa7mBT3oQKN-xg7F1rQcieknFhYAB6CtY8s0-f3C5RxHWHcRNVN6g4ZsbiM8fhOBR4L_nsO8xgPHssWVCFdWiDqvutOEj4ZK-U0cyUEwPODh_OeE7jHyKfnlK-5YIR3Bsw1RRRIW1qGr2Dwb-OLBz5LXXiVlv_FElUU7LYIjIqpD6UNo7lCTe4h94JoDjaq70vesBY5AtM1lnmo0xgbwhOJXnrEwGxQIWJ-zVFktQekCtt-NSaTZUCSlu7DBAYqaUTsDKYN87t6E25ZRDwoNTOcSUOszgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991ae12297.mp4?token=lq6LeKFs5ANaaR2J0f0HPzkYFZipAw-gePdQvdE0YuQVe-qE2yp43xwQa7mBT3oQKN-xg7F1rQcieknFhYAB6CtY8s0-f3C5RxHWHcRNVN6g4ZsbiM8fhOBR4L_nsO8xgPHssWVCFdWiDqvutOEj4ZK-U0cyUEwPODh_OeE7jHyKfnlK-5YIR3Bsw1RRRIW1qGr2Dwb-OLBz5LXXiVlv_FElUU7LYIjIqpD6UNo7lCTe4h94JoDjaq70vesBY5AtM1lnmo0xgbwhOJXnrEwGxQIWJ-zVFktQekCtt-NSaTZUCSlu7DBAYqaUTsDKYN87t6E25ZRDwoNTOcSUOszgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
🔴
پرزیدنت ترامپ
: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138533" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138532">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51700e6e1.mp4?token=LFl71bZYWM2GjMuftxCTjHMN_LJi3Lop7Ca6RSDy0r0DaJsdHMuSByj2Fx-CZjMIpw7Mtmi7AHFWiTViLUFu4_AjcZNGdjvS01K0i01orYlFUlX-_L47pGRFs5MQutHkYN-QipT-js4FdlJg2avH9Gvyjk9tCPDdjl7dpGXCPoc-O0glgTj0_hzLSNU1SydJTVkux7rgXS6fW-5xOhXfrbd8BHSzZFczSChqBPwW58rASVm6ns2QBl6j0HcygKvZWvK9N8FLj7OGPR9LbEeCjSnZf_brZBBw3C6ns0-rmzuYbsDpotbaXBO_dXkjVoukphcPzuSbuaH-Yt1C1d70kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51700e6e1.mp4?token=LFl71bZYWM2GjMuftxCTjHMN_LJi3Lop7Ca6RSDy0r0DaJsdHMuSByj2Fx-CZjMIpw7Mtmi7AHFWiTViLUFu4_AjcZNGdjvS01K0i01orYlFUlX-_L47pGRFs5MQutHkYN-QipT-js4FdlJg2avH9Gvyjk9tCPDdjl7dpGXCPoc-O0glgTj0_hzLSNU1SydJTVkux7rgXS6fW-5xOhXfrbd8BHSzZFczSChqBPwW58rASVm6ns2QBl6j0HcygKvZWvK9N8FLj7OGPR9LbEeCjSnZf_brZBBw3C6ns0-rmzuYbsDpotbaXBO_dXkjVoukphcPzuSbuaH-Yt1C1d70kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/138532" target="_blank">📅 22:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138530">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نیویورک‌تایمز: آمریکا تلاش‌های خود را برای یافتن کشور‌های سومی که مایل به پذیرش مهاجران اخراج شده از آمریکا باشند، گسترش داده
🔴
دولت ترامپ با اروگوئه درباره پذیرش اتباع کوبایی اخراجی از ایالات متحده، مذاکره می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/138530" target="_blank">📅 22:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138529">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گزارش ها از سفر ناگهانی وزیر دفاع عربستان سعودی به آمریکا درباره تشدید تنش قریب‌الوقوع در خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/138529" target="_blank">📅 22:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sjaLNkbR0saxU6TAS2YgNDCfvbU50cDlZC8__YuG88Qcua4hMcgtlPu_ZdNI9ZO9M6XofkojSaANAgnhQrbtWkGIuOGHJ19dEvzeFeMppe-KD6gXFUcN5HgHS-E43h9q-xcXwo8gJb_mV_rphvG5BkKPNWL0DeH7VPVLOnQu-jTZy-kdehJ6FBjWL4laaER_dzVErYS9KGO-MNduwEfZ1A0oLqFrun7Ow1ok5zRn0AeyjVpSobwZ3HhRkR39L0wb3F6S3KEoqU5gLCEJTHXP4o_8BGU7v-a5YcGX2SNMZEHZYN5qTBta_2fjHH8bIuF1gKY_4HegDcllYHDZFYmh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن چاووشی ۴۸ساله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/138528" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
تصویری از ماهرخ عشق ابدی تو خونه تتلو که....... خیلیا نمیدونستن اونه اما خودشه
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/138527" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
دادستان مشهد : افرادی که چند روز پیش تو بلوار سرافرازان مشهد 2 تا بسیجی رو با تیراندازی به قتل رسونده بودن، دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/138526" target="_blank">📅 22:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روایت اکسیوس از پشت پرده دیدار نتانیاهو و ترامپ
: ترامپ ۳ گزینه در قبال ایران در نظر دارد؛ توافق، محاصره و جنگ تمام عیار
🔴
نتانیاهو به ترامپ گفت «راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد»
🔴
ترامپ نگرانی خود را نسبت به تأثیر جنگ بر بازار‌های انرژی مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/138525" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار اجتماعی:
یه پسر ۳۹ ساله تو تهران که یه دوس دختر ۳۵ ساله داشت و ۱۶ سال باهم بودن و هر چقدر تلاش کردن به هم نرسیده بودن، در نهایت بالاخره پدر دختره راضی میشه و باهم نامزد میکنن و قرار بود این هفته عقد کنن که پسره دچار سکته قلبی میشه و جونشو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/138524" target="_blank">📅 22:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال ۱۴ (عبری):
تحقیق: کوه تبر؛ مهمترین دارایی استراتژیک ایران در برنامه هسته‌ای‌اش.
- این ویدئو به طور کامل از عبری ترجمه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/138523" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df71c5ea6d.mp4?token=BY3_m5NgZCDBsYCPXtaixmqU2hU5L8eMMcYv6XO2jP0it713xw4CLsL9n9ZUniFyqmKK1EFIeHIj9clTIUKach1eY5HrvuIi36YXvZtSey0Hr43hDMANpsYPJR0jEEgcDjtEZ5mH7MRvZP6wpWZHlnsdjrUO6CRPPSA01JTF1dxLgXsgib0AzrKYagM6teOk1Xy8h6ZOM7zG5fdcP1DxDP1w3Ev7aiSphTU7ttW2pffmZiIsLbLczvhO9XYqXvQfJ3BmFXNSePooCtgcaIFdfIJTBogeix-1yqXtcX0jxk7iKV0uP5TaupI21Q14rISPKPtH48Yoh08qUKR3TM_WeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df71c5ea6d.mp4?token=BY3_m5NgZCDBsYCPXtaixmqU2hU5L8eMMcYv6XO2jP0it713xw4CLsL9n9ZUniFyqmKK1EFIeHIj9clTIUKach1eY5HrvuIi36YXvZtSey0Hr43hDMANpsYPJR0jEEgcDjtEZ5mH7MRvZP6wpWZHlnsdjrUO6CRPPSA01JTF1dxLgXsgib0AzrKYagM6teOk1Xy8h6ZOM7zG5fdcP1DxDP1w3Ev7aiSphTU7ttW2pffmZiIsLbLczvhO9XYqXvQfJ3BmFXNSePooCtgcaIFdfIJTBogeix-1yqXtcX0jxk7iKV0uP5TaupI21Q14rISPKPtH48Yoh08qUKR3TM_WeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خفت کردن عجیب بازیگران در مراسم ختم اکبر عبدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/138522" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/138521" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
کانال اطلاع رسانی
📣
@safevpn_suportt
✅
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/138520" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فایننشال تایمز: ذخایر نفت آمریکا به سطحی "خطرناک" کاهش یافته است، زیرا جنگ ایران، عرضه نفت را مختل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/138519" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
دومین حمله پهپادی در دیماط مصر
🔴
شرکت امنیت دریایی امبری خبر داد که کشتی حمل گاز طبیعی مایع یونان حامل پرچم برمودا در دیماط مصر مورد حمله پهپادی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/138518" target="_blank">📅 21:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مجدداً چندین انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/138517" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رایزنی نخست‌ وزیر قطر و وزیر خارجه آلمان درباره کاهش تنش‌ها در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138516" target="_blank">📅 21:49 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
