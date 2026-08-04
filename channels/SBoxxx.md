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
<img src="https://cdn4.telesco.pe/file/WU6BpnzJYukzp2zzjJTQE0Pe3Lisl0capAPMOHOYSMzCXTWTgoCetx5HslCwz09o7BrpZlAtryWTwFuE4y5SaJVDHXfMNF6QwzfgDZeIcZ2fmBDJMnuG4KEn8OA7Ot-bNBTTcxHLCuElcVH1b1onk5w6_pgEJ-y-PPGKYBBMJhczm-kSvlPhTXhfgxf5xAVRur3-4att_Qa3JFs_7UzqnQAKQxYhKugbjLu3Qemon35ZQNB8-OSjztq3a4mo6TF4hWKqU9I6s9SCfUh-8J2ESqo5ZzAtHESXHO8Tp9gXyEVe8WmbRnbyhfbrUs8PW8rUSPhY7fw38lMDDia4t9xOXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 03:30:18</div>
<hr>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHt8aI8bPK94L5k3R7Ig8rQiz1J-ldOPhHdwHXL2CHcX-GStFSMUgiphCSRXXPYk8EQo3hyTxMd6m4rvginRzbM2tys3f4SLxLXB4rQna7mYI7329pM_csl2ORQ6zS32CgHHPIikDcQOOI1hkGlCWY0BQCstbFJ2tT6U00gcftu7CkWTMmsJyfiqEn8agsCaHh_aNg48g3YPtket6uEFlc6WFOOSEn7N2hiFQC7Zju9JSfTs9OJtbjI1yWokJBgrxltwYRtGqyDRbL5dL5vLOk7e4TwlulOG8q5vh_e11R3Q6Dz4Rv0TG-GRdTuGH5Jro83oErMXZkzcmaf-j-cNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SBoxxx/19640" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/19639" target="_blank">📅 00:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6ah04-KedZ0zdO7G35ZMBcLT4QoJN7B5Q-RxiWoSYVb5iLG_Zx1JKy0etF3rhap_lISk_XmMwfwFHGt2WRR77w-Yjlx32TSkDoImmhh9huwvRzaoMXz0W8GlGKi8rtmsJAWkLiT3p9UpqRWLXkRK7J4F-eHOkjdnMmQVdRTUbJ85cP_DDiJZGqT6FvRJL1PqihajK6RRPj4ps0NhgWPSXM2yToA9nxJEzquc7cDg3ZL8RgcR0CLMTX8TdTzeN2Xg4b-yyFAurcmBRaFhaO0svdcUWlSqGie0O3O17aLkb17bqRvzz4TrpxiFZtXHnIJnFog-82FokGTiVU4Th1sxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  به نظر تارگت 2 را می شود دستکم 120 درنظر گرفت.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/19638" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک منبع آگاه به خبرگزاری رویترز:
ایران در 24 ساعت گذشته حداقل 3 پهپاد به سمت کشتی‌ها در هرمز شلیک کرده است.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/19637" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در حال حاضر خورشیدگرفتگی روی نداده اما ماه کنار مریخ است.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/19636" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ژنرال محسن رضایی:
در حال حاضر، هیچ آتش‌بسی وجود ندارد. اما تمام عملیات‌های ما هدف مشخصی دارند.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/19635" target="_blank">📅 23:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برنامه داریم اسم جزیره قشم را بگذاریم آمریکا و آن را محاصره کنیم.</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/19634" target="_blank">📅 22:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏ژنرال  محسن رضایی:   اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.  ‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد. ‎</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19633" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
ژنرال
محسن رضایی:
اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.
‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد.
‎</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/19632" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ژنرال محسن رضایی:
آمریکا در طراحی چهارم خود علیه ایران تلاش دارد از داخل شورش‌هایی انجام دهند
کشورهای دیگر را هم می‌خواهند وارد جنگ با ایران کنند!</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SBoxxx/19631" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/19630" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:  من اجازه نخواهم داد که ایران این عوارض را دریافت کند.  اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.  ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/19629" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دونالد ترامپ در مورد چمن:
چمن مثل انسان‌هاست. آن هم زندگی دارد.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/19628" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:
من اجازه نخواهم داد که ایران این عوارض را دریافت کند.
اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.
ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/19627" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منظور کله زرد از «این» چیست؟! وقتی مذاکره ای صورت نمیگیرد</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/19626" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19625" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/19624" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سوئیس: ما در ارتباط با ایران و ایالات متحده در مورد مذاکرات احتمالی هستیم -
خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/19623" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVcEl-B6RtoGv_0HHXeOqyz0N-AJZxg8XsohRTGeVtl0u4EOoy7UQRRRr3o1oTxvZRSfHT-SFBW_4PoXN68J4x9f9iZO9wxhLDd7l0DYPQ3Ca7vxQXjbA0URhXEM5mROsfj48nJANADtKYI8VYlCPGRWm1p8EeNguz4hJn1sR2eyvX-64s8AhCUv7AdTqSRdcBXnbkmXKnCOnwpAv4cOvIL9JkaavHWbYa-IMP8DBzVKjVNW8zkwUgxr1wWeTqbn8IgjyKI5Y4wAervTczBCaUK047cLuXMSl92uqrYXugV863V8qW_qzLEOuhDzRSP4xT1LZldPzNAlzfWu78aMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19622" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان نیست، هیچ موضوعی مورد گفتگو قرار نمی‌گیرد، و آن‌ها فقط با "عمان" در ارتباط هستند.
سپس، آن‌ها به سخنان همیشگی خود ادامه می‌دهند و ادعا می‌کنند که تنگه هرمز به طور کامل توسط آن‌ها کنترل خواهد شد، در حالی که در حال حاضر، این تنگه به طور کامل تحت کنترل نیروی دریایی ایالات متحده و "محاصره" ما، یا همانطور که برخی می‌گویند، "دیوار فولادی ایالات متحده" است.
هیچ چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ چیز نخواهد رسید، مگر اینکه یک توافق حاصل شود، یا ایران به طور کامل تسلیم شود. چه ایران این را بپذیرد یا نه، در واقع، ما در حال بررسی راه حلی برای مشکلی هستیم که آن‌ها برای دهه‌ها ایجاد کرده‌اند.
این موضوع بسیار ساده است: ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19621" target="_blank">📅 19:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پاکستان وجود هر گونه مذاکره ای میان ایران و آمریکا را رد کرد.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/19620" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تصویر نگران‌کننده بازار کار ایران.
بر اساس تازه‌ترین نتایج طرح آمارگیری نیروی کار مرکز آمار ایران، اقتصاد کشور در بهار امسال حدود
۴۵۰ هزار شغل
را از دست داده است. همچنین
۶۲۹ هزار فرصت شغلی در بخش صنعت
حذف شده و شمار قابل‌توجهی به جمعیت بیکاران افزوده شده‌اند؛ آماری که از تشدید بحران در بازار کار حکایت دارد.
﻿
همچنین مرکز افکارسنجی دانشجویان ایران (وابسته به جهاد دانشگاهی) اعلام کرده است که
معیشت بیش از ۳۲ میلیون ایرانی
به‌صورت مستقیم یا غیرمستقیم به پایداری اینترنت وابسته است؛ موضوعی که اهمیت دسترسی پایدار به اینترنت را در اقتصاد و اشتغال کشور نشان می‌دهد</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19619" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو:
ما باید روابط خود را با متحدان بیشتری تقویت کنیم.
به همین دلیل است که من سرمایه‌گذاری زیادی در رابطه خود با هند انجام می‌دهم، با دوستم نارندرا، که یکی از بزرگترین دوستان ماست.
برخی می‌گویند اسرائیل منزوی است. اما حمایت‌هایی که اسرائیل – و من شخصاً – در هند دریافت می‌کنم، واقعاً شگفت‌انگیز است.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/19618" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو:
اکثریت قاطع مردم ایران، اسرائیل را تحسین می‌کنند.</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19617" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Geomarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">324.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 17</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19616" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجار در دوبی همراه با یک کشته و 5 زخمی</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19615" target="_blank">📅 17:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqQMrXVyHqp9Dww3TSfKv3TKYnR6s-r6zRHOmGzvCt9oA8Jcpu4f2WXJt6RbBqcb9F-r31gyK9lDM2cihXHvV9kVeAgvSlNEJtdxMlzthovF1N_e--N4Ji6NTD7a-YzOrs_mnJRv-QIoDFXBA3NBROpksj7AYSK2THRVgE-b9zVxS265JNr3D-PS0oC5-OAXVM-sRe9TUQMVqwBFwFVbtvyr_2kV9uXSZzuf3MrL7-qtztlgcK0f6GWnw3Ywi8_oTPczYncIxYi1oUJx6ADzuiZHb48A8Q394td1kEikCcFVs1ila59I9umn5FaBAw5QRnMzDkRr7B0mpD-zKe2srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا بسته‌شدن 20 درصد صادرات نفت جهانی منجر به افزایش 80 درصدی درصدی قیمت شد؟
بسته شدن تنگه هرمز فقط به معنای حذف ۲۰ درصد از عرضه نفت نیست؛ بلکه ظرفیت مازاد تولید جهان را نیز از بین می‌برد و با از بین رفتن انعطاف‌پذیری بازار، حتی یک شوک محدود می‌تواند جهش بزرگی در قیمت نفت ایجاد کند.
علاوه بر این، بازار نفت ریسک‌های آینده مانند گسترش جنگ، اختلال در تأمین نفت جایگزین، محدودیت اوپک‌پلاس، مشکلات پالایش نفت سنگین و معاملات اهرمی را نیز پیش‌خور می‌کند؛ عواملی که مجموعاً جهش شدید قیمت‌ها را رقم می‌زنند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/19614" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
مایک ویرث، رئیس هیئت مدیره و مدیر عامل شرکت شرون، همین‌اکنون در مصاحبه‌ای با ماریا بارتیرومو که فوق‌العاده است، تمام دلایل موفقیت شرکتش را بیان کرد.
تنها چیزی که او به‌طور مصلحت‌آمیز فراموش کرد ذکر کند این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و خود کشور ما مرده بود!
به عنوان مثال، آن‌ها مایک و شرون را از ونزوئلا بیرون انداختند، اما اکنون آن‌ها بازگشته‌اند، بسیار بزرگتر و قدرتمندتر از هر زمان پیشین، و انتظار دارند ثروتی عظیم کسب کنند!
این موضوع برای سایر شرکت‌های نفتی نیز صدق می‌کند... و همین حالا قیمت‌های مصرفی (خرده‌فروشی) نفت را پایین بیاورید!
بابت توجه شما به این موضوع سپاسگزارم.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19613" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">المیادین:
ایران پیشنهاد بازگشایی تنگه هرمز تا پایان کامل جنگ را رد کرد.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/19612" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گادی آیزنکوت در مورد ایران:  در مورد ایران، یک هدف برتر و دو هدف بسیار مهم دیگر وجود دارد. هدف برتر، حذف حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شده از ایران است.  اگر این کار انجام نشود، ایرانیان می‌توانند با تصمیم خود، به سمت سلاح هسته‌ای پیش بروند. این چه معنایی…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19611" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19610">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=tbfwYUBXvox-wsP_vFecLg96XXYx60nfnZ8FjshOApc76LetHUdXU1WgxmhOZ3-SF7UH9vuXmNVjsfcrVEHgsMTp3hTG_s9I1fEXvig3Yxt35dneX1g5BAwopGwZuP2yQZCB9p_qyeZ2VgAT1iQOBBaltNG2jPvhe0i1hHvNr5zEK-jOw9PycrFjgLaPHQSe8jVxOqNg1r1kwONfbMJrc0xbtszZYEn-xFp8XZgK5YtEyklF0QMI10LKbKrxLDG3k95JlW9VwkhGqiTn3Ix43tCJW0HlK12J1druptQTUIEBdswvl-1jMdM2bJ9bCYFctoCBH9S2_an3j_2EW8Hr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=tbfwYUBXvox-wsP_vFecLg96XXYx60nfnZ8FjshOApc76LetHUdXU1WgxmhOZ3-SF7UH9vuXmNVjsfcrVEHgsMTp3hTG_s9I1fEXvig3Yxt35dneX1g5BAwopGwZuP2yQZCB9p_qyeZ2VgAT1iQOBBaltNG2jPvhe0i1hHvNr5zEK-jOw9PycrFjgLaPHQSe8jVxOqNg1r1kwONfbMJrc0xbtszZYEn-xFp8XZgK5YtEyklF0QMI10LKbKrxLDG3k95JlW9VwkhGqiTn3Ix43tCJW0HlK12J1druptQTUIEBdswvl-1jMdM2bJ9bCYFctoCBH9S2_an3j_2EW8Hr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:  «ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19610" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19609">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6aAkB7lpWdfj8JAvzC8CqLFy9ePW5KJMWmg3qKg0NiZbi_hRAWXsNx3JwqyvA0Buc4nHIubIDilzQdZ2DpGpY19SopdmUY6TAs8bnaUSk9WjwAtPOp1SD1eyU9CDbgqiK165w7feaJJb9Lk_zBDs5AbL-on1bN3n1xsPXnx4X_P5UMYOMTw4mEi435rSwuK1LRT2FnT6Di2bL8vDOfiIdey0vBOzSGe56bPs6eGCF_eQbGDSnKK6h11w6xsmjCWIoxyiEfQ6CBj58MO991_sE0CaAXSj38vlXRZlPHQlw0kdqe7fp5616uGb0E1cT7uIIQKQlqg6kWZsVzr3128RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسناد فاش‌شده نشان می‌دهند که شرکت اسرائیلی "ال بیت سیستمز" (Elbit Systems)، فعال در زمینه تسلیحات، به دنبال انعقاد قراردادهای تسلیحاتی به ارزش تا 1.3 میلیارد دلار با امارات متحده عربی بوده است، که شامل پهپادهای پیشرفته "هرمس" و سیستم‌های اطلاعاتی می‌باشد.
منبع: هارتز (Haaretz)</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/19609" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:  در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.  گزینه‌های نظامی واقع‌بینانه در نظر گرفته…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19608" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:
در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.
گزینه‌های نظامی واقع‌بینانه در نظر گرفته نمی‌شدند. رویکرد غالب، آشتی با رژیم بود. اگرچه بسیاری از سیاستمداران ترکیه در کارآمدی آشتی تردید داشتند، اما این مسیر در حال پیگیری بود.
ترکها همچنین می‌ترسیدند که اگر یک تهاجم نظامی شکست بخورد، روسیه با حملات هوایی گسترده به مناطق تحت کنترل مخالفان پاسخ دهد و موج دیگری از پناهندگان را به ترکیه که خود با بحران پناهندگی روبرو بود، وارد کند.
حتی کشورهای عربی - به جز قطر - در حال پیگیری عادی‌سازی روابط با رژیم بودند. هدف تأیید آنچه اسد انجام داده بود نبود، بلکه دور کردن سوریه از نفوذ ایران و کاهش خسارتی بود که به منطقه وارد می‌کرد.
عملیات نظامی با وجود آن نگرانی‌ها آغاز شد. این کاملاً تصمیم خودمان بود.
منبع: الجزیره</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19607" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 17</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 17
دوشنبه 3 آگوست 2026</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19606" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIh6rHP5rCsBMgVjo8r6jSNKy2ucVLxpfKYFqqnnKLdkqUXRAzjg_OpWzYit5docyZcDzbtHDTTOJJBiX6WKA9Zf4k5ERd7_lk6Tf2RfrdsqNIffOV0jUnK1o4ml849q1IWmB2Ay8KUxurUAaXvetS3A36Z0VCmF_DK3xGETnagv0aZ0noTpZy5gg7k5pG-fL4IZNSRHmkqzkBiTkFfTuyHyetq2RRoy_t8woUFk6tT-cm6ma7IThePWP32EuPJECQdDp7p53xPraMWW8ipWY2eCqlI75qfu5xb--qwpPQB2MWeWIG397PC_XKnfu_fr1RVUPIhYp8gZnr98pc9cUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رنکینگ مسخره ضریب هوشی کشورهای جهان را ناموسا رها کنید!
اگر میانگین ضریب هوشی ما واقعا چهارم دنیا بود باید سطح رفاه و توسعه اقتصادی ما هم دستکم در ۱۰ کشور برتر جهان قرار میگرفت (کشورهای دیگر صدر جدول را بییینید) نه اینکه رییس جمهوری مثل پزشکیان داشته باشیم که سطح ادراکش از توسعه برق این است که برود آستین کوتاه بپوشد و یک لامپ خاموش کند!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19605" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/19604" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19603" target="_blank">📅 12:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:
«ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»
این اقدام نشان‌دهنده درک این موضوع است که گزینه‌های موجود در حال حاضر برای دولت ترامپ محدود هستند و ممکن است از نظر سیاسی یا نظامی قابل قبول نباشند، که این امر ضرورت بررسی راهبردهای جایگزین را ایجاد می‌کند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19601" target="_blank">📅 12:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRdjt7fylsIzb1SsgSSVpOgNKkUqxSngonHLogDnoYGXxWuQFwvUOIRRqTvDsz0z9VC12tZEckjOgQj9r7qgH_tYq93J_K4ZwWICGUUcUEherXfGdqpITs-dK7d04DgkEJGq0h48k90zL58cxK2sJvZmuNyLT0-WS8Om3ZyucJ2gPfMPD70DHHI3oO4NzbGgqM0Y8hEsokI4JFYsskV_5BqvOlCNKW43Yr_e8UXAdMAnA75g-n8yZDqFEsVt62nDbKMmSDhXG4HD0iYu2uKLQnVfw4V6EYZ5BehhNpC0etwMbnI-OXL2FRHMdyu_Vdf3ozSMFoKHpCX5QBKHG_Ur5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19600" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.  این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/19599" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.
این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.
منبع: i24</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19598" target="_blank">📅 10:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ ادعا می‌کند مذاکرات آمریکا-ایران روز دوشنبه آغاز می‌شود
او‌ گفت:
«خب، کاری که الان انجام می‌دهیم این است که در قالب مذاکره با آن‌ها صحبت می‌کنیم. این کار فردا بعدازظهر آغاز می‌شود و خواهیم دید که آیا این واقعیت دارد یا خیر. من عاشق انجام این کار هستم،»
ایران این ادعاها را رسماً تأیید نکرده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19597" target="_blank">📅 02:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19596" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19595" target="_blank">📅 01:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانید این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم (ایران) به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند رخ دهد.
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم. مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19594" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ می‌گوید عربستان سعودی، امارات متحده عربی، قطر و ایران همگی از او خواسته‌اند حملات را لغو کند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19593" target="_blank">📅 01:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19592" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کشته شدن مامور پلیس در درگیری با اشرار مسلح شادگان  ستوان‌سوم شهید «سینا سیاه‌نژاد»، از نیروهای حافظ نظم و امنیت، هشتم مرداد در جریان درگیری با اشرار مسلح و حادثه تروریستی در شهرستان شادگان استان خوزستان، حین انجام ماموریت به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19591" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام:
تا تاریخ 2 آگوست (و در راستای اعمال محاصره دریایی ایران)، فرماندهی مرکزی ایالات متحده (CENTCOM) مسیر 35 کشتی تجاری را تغییر داده است، 2 کشتی را غیرفعال کرده و 2 کشتی را بازرسی کرده است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19590" target="_blank">📅 22:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترکیه با پیش‌بینی تشدید تنش‌ها، اقدامات کنترل مرزی را تشدید کرده و  مرز خود با ایران را با دیوار فولادی تقویت می‌کند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19589" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:  مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.  در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است،…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19588" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:
مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.
در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است، حتی اگر ایالات متحده حمله نکند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19587" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فردا یک صوتی مفصل درباره این داستان قدرت نظامی اوکراین و بحث زیرساخت ها خواهم داد.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/19586" target="_blank">📅 19:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.  بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19585" target="_blank">📅 18:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.
بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19584" target="_blank">📅 18:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">با گند زدن عبدالصمد ونساوی در حوزه برخورد با جمهوری اسلامی، اکنون شانس روبیو برای پیروزی در رقابت های درونی نامزدی حزب جمهوریخواه برای انتخابات 2028 به 31% رسیده که بالاترین میزان تاریخی خود است.  در سوی مقابل شانس ونس ترنس به 39% سقوط کرده است.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19583" target="_blank">📅 17:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای اسرائیلی در حال هدف قرار دادن ارتفاعات علی الطاهر در جنوب لبنان با بمب‌های آتش‌زا هستند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19582" target="_blank">📅 17:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvZgDdSY2N2CwqmuGLszhi56vJa84jOHhYZVx8crqgP1ueb4dT_q5k8XcxTxpWRaNB2DC8uaujnyhQUYezgwnPhmBvKhTfyEBujGifK2BrwTagu6psIGekJlGlWs8y0GLY-mhogxfRLHUQWcpGS9KSekZ6Bcawt2cpfNwihi3G8cfawc31UIeBmQssG1_IkYu7nZQ8TT47DKoSMp56LaLFc0A25mazEzVuKcTrWkwIZL6V6VkNibi0m7Rv67gE2-hI-2_j-D9XzqyIGKtnnUFyKqvlB5KliGZPutYfEKGR2PCopkUNhy91uPHC4tFGidKfak1LVBC2WEUfVYQ6oi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19581" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بسیار بعید میدانم جمهوری اسلامی بدون لغو محاصره دریایی، تنگه هرمز را باز کند، حتی اگر ورودی تنگه هم در اختیارش باشد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19580" target="_blank">📅 13:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19579" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:
حکومت ایران در طول جنگ سقوط نخواهد کرد.
مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.
تأکید باید بر این باشد: اقتصاد، اقتصاد، اقتصاد، اقتصاد. این چیزی است که در نهایت حکومت را سرنگون خواهد کرد.
به نظر من حکومت می‌تواند به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی این اتفاق بیفتد، ترس دیگر مانعی نخواهد بود. آن‌ها بیرون خواهند آمد، قیام خواهند کرد و حکومت را سرنگون خواهند کرد.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19578" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baqbx7mFRejA4haRODkVJUASD8-_pHa5cRbfdBucfHLQG2s0rJLzV38tmk1XbHAxtrkSwakar5GYcTyog5hE_I6RqvUUdoio6PBxXIhCFHssTpdxrovFVt6PgYmDEb8t-FY8SoNpHKnPSI-OghTtnYuIGb7c77tBegciogBabmhMdlfcnCKJhVeZDsK3J4cawBzlPoqKe7QmO-Tgn-FGwPGsbLBT2onQt6uBuR512if73Ak0yiavRomafQay_y3mLxjj1Kg3qPvcE_fPXdNk1lYQpyc45xfmrQxicRunLyCTRfwSIbPPV0DxL6YP3kkdPN1tazl7DDIyPRYnkZkjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarket Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19577" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آکسیوس :    ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19576" target="_blank">📅 11:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19575">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یعنی موج 2 اینقدر کوتاه بود؟!  سبحان الله!   همه 5 سانت و 10 سانت و ....</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19575" target="_blank">📅 11:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروهای مقاومت بعد از اربعین پاسخ آمریکا را خواهند داد
علاءالدین بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس، با محکومیت شدید حملات بزدلانه ایالات متحده و عربستان سعودی به مواضع حشدالشعبی و موکب‌های عزاداری امام حسین(ع)، این اقدام را نشان از استیصال و ناتوانی نظامی دشمن دانست و گفت:
با وجود احترام به قداست ایام اربعین حسینی(ع)، پاسخ قاطع و متقابل به این جنایات در زمان مناسب و پس از پایان این مراسم مقدس، توسط نیروهای مقاومت انجام خواهد شد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19574" target="_blank">📅 11:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آکسیوس
:
ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19573" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19572" target="_blank">📅 09:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19571" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باراک راید از آکسیوس، با استناد به دو مقام آمریکایی و یک منبع دیگر، گزارش می‌دهد که محمد بن سلمان، ولیعهد عربستان سعودی، نگرانی‌های خود را نسبت به طرح دونالد ترامپ، رئیس‌جمهور ایالات متحده، برای انجام حملات گسترده علیه ایران ابراز کرده است.
بن سلمان در یک تماس تلفنی با ترامپ، درخواست جزئیات بیشتری درباره عملیات کرد و از او خواست که حملات را آغاز نکند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19570" target="_blank">📅 03:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حمله ایران به سلیمانیه و اربیل</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/19569" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این شرکت Fire Point، بجز موشکهای دوربرد فلامینگو، پهپادهای انتحاری دوربرد FP-1 را هم تولید می‌کند که اخیرا در حمله به تاسیسات نفتی روسیه عملکرد درخشانی داشته است.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19568" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/19567" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تهدید یک نظامی اوکراینی به حمله به ایران با موشک های کروز فلامینگو</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19566" target="_blank">📅 01:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19565" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8iFXyCU8f9e-qehvItQCnDMNPnQPi36e_4Voo_uG9sgP1ive_LoEIU69RmBBUQ9CbJBX7gHApluFKsGt4FS_9JNMvCI9FmTPXP4jWYc4y8Q3RxGSTSgkzZU9J99H9Ks0dQJiMpEf2XZyx4jirqkgNejCLFhGWB6UmL3jb1VPbCc6_ub1rcenVixBu5mRskjcSFakPlsSXTEztYkDqhc0ivAHcWiChW9dXCTPAcHxfIuWcrssKuR7ecXAJhAj8opdJtFmu4NiWi2NS-Iorie-M5Jvvp--G3k01AnOtr-tK6Iw_9HygMuMBTSGQ_syqw3drvyEZIt1K4KtzaRGfL71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت اتاق جنگ اسرائیل</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19564" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دکتر مرندی این بار دستور تخلیه کل خاورمیانه را صادر فرمودند.</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/19563" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf1ZZ0SHfVV5ruejy7DzMzUc_rTxsJmtzoxnFVQnNUSLtv6ZF1TjeBL5BHlEMDz424JIC941d0DAENkBgiWfoByH8ZpUOq7FTYr7ffmq7ZoDAW6yeC7XjdGrOqTsPsWFk9Hg49PR6XJ2BuNatteddixx4AtJvi_4JFiqZgrUyAvPHNUGsrtzzN_f4khhOp1ly29SJoOnOlP_UVxAQJ_OATrXDzNr1ThB9WdKxkmCP1D88EfLoKFBwwEaob7zx1UH0MJvVodYJ0bwCCz2KA7xRpVQGlBG0zyWHa8qEtlZddDdwXcn4cF5AtJEhceQtbyBSfOpSXDhQf7uQ3c1Ci9VIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/19562" target="_blank">📅 23:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک منبع از وزارت جنگ ایالات متحده به شبکه فاکس نیوز گفت:
«ما برای یک جنگ تمام‌عیار علیه ایران آماده هستیم.
در چند ساعت گذشته، رئیس‌جمهور ترامپ دستور انجام تعدادی از حملات مرگبار و خطرناک علیه نیروهای سپاه پاسداران انقلاب اسلامی را صادر کرده است.»</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SBoxxx/19561" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rikghzi3-XHvHMU2ElQr4ngMa4m8cQWOih-_7smhHR5sv8Rbv-gkGqN_ntq8yASDswgIcMZqCl44BxN6AIWCVxBC7exoc6_f1BHFyW4emIRfXWhPaDsvRxLBJOXkY-It78BHhvB4ifDYZXPNoMJ7ylqBpfB4wIOqmHn0XoXrIhZSYJaBFa6Dqgeel5yig-pjR2eiZjH0wzgbOsI6LEDEiVoZgBHbtTC2-W-JbnZvBroOegBj0tX60pwnzzEnomADonP6_UEQb8OYRPR7fWSi6qL867ZPecdqBcu4fYuqEqyVImWLzLDVyauAiWekpTvVg5vHKUk3w3cuNazzSjO3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ترامپ در حال نابودی ارز ایران است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19560" target="_blank">📅 21:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">برخی گزارشهای آمریکایی می‌گوید کشورهای خلیج فارس به رهبری قطر در تلاشند تا از جنگ مجدد آمریکا با ایران جلوگیری کنند.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/19559" target="_blank">📅 20:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">— مقامات آمریکایی در حال بررسی موجی از حملات سایبری علیه سیستم‌های آب در حداقل هفت ایالت هستند، با شواهد اولیه که به ایران اشاره دارد.
حملات برخی عملیات را مختل کردند اما آب آشامیدنی را آلوده نکردند و هیچ خطر شناخته‌شده‌ای برای سلامت عمومی ایجاد نکردند.
دونالد ترامپ نقش ایران را زیر سوال برد، در حالی که مقامات ایالتی و فدرال گفتند که ایران بر اساس اطلاعات موجود همچنان مظنون اصلی باقی می‌ماند.
متخصصان امنیت سایبری این کمپین را یک بی‌سابقه در هدف قرار دادن زیرساخت‌های آب ایالات متحده توصیف کردند که احتمالاً قصد بهره‌برداری از سیستم‌های آسیب‌پذیر را داشته است نه هدف قرار دادن جوامع خاص.
— نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/19558" target="_blank">📅 20:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مکن ای صبح طلوع …</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19557" target="_blank">📅 20:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMbmQzRNffybD07hX3RtDivRo91yc1xE0Jhvk7oYGYA4266w_JH2qspngqZrVUYrQ6mzZO345ArS61_lXmYyoENUGWiFhkkxjZ4g18hspGYIwaHizZqjvpTjc92HkxvK8bmHCWS933yFY7mngUgnPBEYJvd3Ze8x1lIdCWHj31SwtaEMPgdcNwmROWe9IWiSk7kjaxp5h1RNnS49ocdsvB8ybEEWEY8KbRM12EoDY8eKRZuIV20_RMWphLMZzNTyJXym2c0cE5hEFoHgUt4Awi826V_rs8kpIDjOcJxZIWHFqZyeQTe9zUFkCpk6ViTFOh22D0fWnew9feC2qjHRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SBoxxx/19556" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19555">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpOcBoBmMAeUQxUN1S1b6otV8Pxa0f8jJJ1GE9vsD7NXLRynwFbcj3nSamR6dQ75I2CSF2MNgvyIelD43oCdsJxS9u3c_eSZZEQx08B-dn6icSeTdwZ8IryuPK5AO7VdrbIw8rdqWcAVHd84BKdXRq1EiG9MoJ8iW7CxrqZ9LS3903pcruBFkQH8LVvJZsLFgxTS9VeUQOM-kQs-DoRBW-01NPRCbZPsBXg9rUzI2Cr-VKAnT5b37Aw2zADF_6INmP85T4cIhqpitFN2S7XuaLplezqOz8wzatjJsmcIbqlX89_90N3FXWxSlC0UxGNWIgPeOxRikDzfOcvkCgO9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه روسیه با پهپادهای ایرانی رقابت تسلیحاتی در حوزه پهپادها را تشدید می‌کند   رئیس‌جمهور اوکراین، ولودیمیر زلنسکی، ماه سپتامبر مجمع عمومی سازمان ملل هشدار داد که «ما اکنون در حال تجربه مخرب‌ترین رقابت تسلیحاتی تاریخ بشر هستیم»؛ اشاره او به بهره گیری روزافزون…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SBoxxx/19555" target="_blank">📅 15:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به جای جای ایران که مینگرید، نشانه های بازدارندگی قدرتمند جمهوری اسلامی را می‌توان دید</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/19554" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/19553" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/19552" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=T2mWvXGrDMufByIIokN9xr62alI-rCfjv8K9kMJsiXwGoA3IQz4RC056TBUktBLFWUyCYgXIojJNQ3Es6-9iiCMm4vzxzUuEcANeOfjWa7ud3JTkJvbYwqBYjQwhIfh3DVxXwz5BqXVgtI2ZZrur8RUr5t4AFonpK6taUfLHfl4zOl9sfx3jDjg000JczUwjP9ZrVvz2km94O1OOKuiSHGt6QZHoJ7eknMkB44XhocDonteeBR6FJVCvE5iOTw4fWFS0s4eFxrsdmUXx-Ly9jLfkC8vKQczjg1L4Rl-GmaVCTNYdS-9bZPdg3ZI4LG4Ozd_L86BA0xJCCLvDm_eOrSvUxhzuzv0y-NsL9JvRZYdhnz_S_wnBOOlHW4lFt4ABmCIt-_FFNpJZnJe9_V0tjBH3Gh6wPCFwt2UcEtK5YfoeeK9BVYT2-Kq0oJmPtwK_oH2KAIUqs7u7FhxhAZqq61i_9KxKD55S1ERDDT9DZxieB7N3qzDTatvavZdizQUJdI6ZbsXF9EVtWBuL1SaWYG3Ge7-DMqNbwQMo132pUrdmweeiQrf_x8vwew3CLgWejJmAWRLYZkXw88GNeyP9dI94cPGDmrk14S9ts-uC-TLj_WV-ZXviElo9nChQTMVeVFuu6GgmxraDBSuIysV8sNHCInjBQYKzLbHaDOONpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=T2mWvXGrDMufByIIokN9xr62alI-rCfjv8K9kMJsiXwGoA3IQz4RC056TBUktBLFWUyCYgXIojJNQ3Es6-9iiCMm4vzxzUuEcANeOfjWa7ud3JTkJvbYwqBYjQwhIfh3DVxXwz5BqXVgtI2ZZrur8RUr5t4AFonpK6taUfLHfl4zOl9sfx3jDjg000JczUwjP9ZrVvz2km94O1OOKuiSHGt6QZHoJ7eknMkB44XhocDonteeBR6FJVCvE5iOTw4fWFS0s4eFxrsdmUXx-Ly9jLfkC8vKQczjg1L4Rl-GmaVCTNYdS-9bZPdg3ZI4LG4Ozd_L86BA0xJCCLvDm_eOrSvUxhzuzv0y-NsL9JvRZYdhnz_S_wnBOOlHW4lFt4ABmCIt-_FFNpJZnJe9_V0tjBH3Gh6wPCFwt2UcEtK5YfoeeK9BVYT2-Kq0oJmPtwK_oH2KAIUqs7u7FhxhAZqq61i_9KxKD55S1ERDDT9DZxieB7N3qzDTatvavZdizQUJdI6ZbsXF9EVtWBuL1SaWYG3Ge7-DMqNbwQMo132pUrdmweeiQrf_x8vwew3CLgWejJmAWRLYZkXw88GNeyP9dI94cPGDmrk14S9ts-uC-TLj_WV-ZXviElo9nChQTMVeVFuu6GgmxraDBSuIysV8sNHCInjBQYKzLbHaDOONpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/19551" target="_blank">📅 12:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سفارت ایالات متحده در اردن :
«آمریکایی‌های حاضر در خاورمیانه باید احتیاط و هوشیاری بیشتری به خرج دهند و برای لغو پروازها، بسته‌های دوره‌ای فضای هوایی و اختلالات احتمالی سفر آماده باشند.»
«آمریکایی‌های حاضر در منطقه باید به ترک آن فکر کنند، یا در صورت تشدید درگیری‌ها برای ترک منطقه آماده باشند».</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/19550" target="_blank">📅 12:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ویدیویی بسیار جالب درباره روند ایجاد و تکامل ایده ساخت پهپاد لوکاس که مشابه شاهد-136 است اما مجهز به هوش مصنوعی و توان رهگیری بالاتر  https://www.msn.com/en-us/news/other/watch-how-the-us-turned-iran-s-drone-into-a-weapon-used-against-them/vi-AA20tLa9?oci…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/19549" target="_blank">📅 11:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش آمریکا یک یگان ویژه پهپادی در منطقه عملیاتی سنت کام (غرب آسیا) مستقر کرده که در آن از پهپادهای Lucas با طراحی تقلیدی از پهپاد شاهد-۱۳۶ خودمان استفاده می‌شود.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19548" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">افزایش اهمیت اهرم فشار چین
به گزارش رویترز، با تشدید دوباره جنگ ایران، کشورهای عرب حاشیه خلیج فارس به‌جای واشنگتن، به چین روی آورده‌اند تا از اهرم اقتصادی خود در برابر ایران برای بازگشایی تنگه هرمز و مسیر دریایی دریای سرخ استفاده کند. این وضعیت در واقع آزمونی است برای اینکه پکن تا چه اندازه توان و تمایل دارد تهران را تحت فشار قرار دهد.
منابع کشورهای خلیج فارس می‌گویند تلاش آنها برای ایفای نقش بزرگ‌تر چین، ناشی از افزایش نارضایتی است. جنگی که در ۲۸ فوریه با حملات آمریکا و اسرائیل به ایران آغاز شد، اگرچه به رقیب منطقه‌ای آنها آسیب زده، اما هم‌زمان صادرات حیاتی انرژی این کشورها را نیز محدود کرده و آنها را، با درجات مختلف، در معرض حملات قرار داده است.
سه منبع منطقه‌ای می‌گویند از آنجا که ایران و متحدانش هم‌زمان تنگه باب‌المندب در دریای سرخ و تنگه هرمز را تهدید می‌کنند، کشورهای خلیج فارس از چین درخواست کمک کرده‌اند؛ به‌ویژه با توجه به اینکه جنگ محدودیت‌های قدرت آمریکا را آشکار کرده است.
وانگ یی، وزیر خارجه چین، ده‌ها تماس تلفنی و دیدار با همتایان خود داشته و برای دستیابی به آتش‌بس جدید تلاش کرده است. همچنین ژای جون، فرستاده ویژه چین، با مقامات کشورهای عرب خلیج فارس و همچنین ایران مذاکراتی انجام داده است.
اما این دقیقاً چیزی است که وضعیت به آن نیاز ندارد! هیئت تحریریه وال‌استریت ژورنال هشدار می‌دهد که نتیجه جنگ ایران تا حدی به رفتار و عملکرد قدرت‌های محور مقابل آمریکا بستگی خواهد داشت.
این نشریه می‌پرسد:
«با وجود اینکه آمریکا بخش قابل توجهی از زرادخانه موشکی ایران را تضعیف کرده است، آیا چین به‌سرعت به بازسازی آن کمک خواهد کرد؟ آیا روسیه که به دلیل کمک‌های ایران در جنگ اوکراین به تهران بدهکار است، به احیای برنامه هسته‌ای ایران کمک خواهد کرد؟ آیا هر یک از این دو کشور، سامانه‌های پدافند هوایی پیشرفته‌تری در اختیار ایران قرار خواهند داد؟»
در واقع، نگرانی اصلی این است که چین و روسیه به‌جای ایفای نقش میانجی برای پایان دادن به جنگ، به بازسازی توان نظامی ایران کمک کنند. چنین سناریویی می‌تواند جنگ را طولانی‌تر کند، رقابت ژئوپلیتیکی میان آمریکا و چین را تشدید کند و هم‌زمان ریسک اختلال طولانی‌مدت در مسیرهای انرژی هرمز و باب‌المندب را افزایش دهد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19547" target="_blank">📅 10:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/19546" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هدف قرار گرفتن ۲ کشتی در نزدیکی سواحل عمان در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19545" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-puPMId6KzKv0V_A-cDr5Hrh-w1A5EfZWGG9P091Uy9LPSvAtaJvkzDWTINIyv9UbIo0RoYvwIV2-xswJTssLWjiaxZ57fgqcEld1pNxa2QwRoo9Fk8Zw3LI5avtpiUEw570RDGVhY8ixlKa_ClYqhKu8f6Tn0A-4fH2GlsmqQ50IxTt_Ri57jPAk6S6aWDrpa0cWS6xjjVI1mR3xwWHTHDso_p-PJR4oGF48EECBJAToeVxBqWJoR3JDVmhGZL41donXZZ-Xgmn3UrPMJqkwNRHmmBeHfk2pHLdQXw3dpHNT6yq1Xx1b7DAW2seJPPZVo_tmJ0x9wyMMaijvd8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.  روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/19544" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو خطاب به رئیس جمهور ترکیه:   اردوغان یک دیکتاتور یهودستیز است که مرتکب نسل‌کشی علیه کُردها می‌شود  او که از حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، آخرین کسی است که می‌تواند درس اخلاق بدهد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19543" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19542" target="_blank">📅 01:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مرندی:  رژیم مراکش صرفاً ابزاری دیگر برای نتانیاهو و ترامپ است. آن‌ها اسپانیا را به خاطر حمایت از فلسطین تنبیه می‌کنند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19541" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19540" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
