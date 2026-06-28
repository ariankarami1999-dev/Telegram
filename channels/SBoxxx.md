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
<img src="https://cdn4.telesco.pe/file/EyvECTPmCiQCNQqT5mVNFW_ZH6HX-FF-Dc3bqDcQuU37IRoMUE8WnlkQGIV4T1TVBOKDKkPAVkhdP8ajb0xgP3wEzgcmwPTSEON2EOuotCoKmuOKUpGedLYGANf8yCPBWTtP6QayHk33P_dLrqb09e9gfjvAyOJy8c83jp5aemEETyDxGIxbYHdXc6tABbxSJYkDyCdz9uXJi1cmvTp1dELdEPgVE9Mme01HspdLKhPr75xUsVyLrkYhlZ1AZTvONdkt7YWvMw-jCe2ylAi_Jrhl1-Kgyh3_FCjQFCIewisChzJkwqE5gAr6wlqZu5AeM8NfMqsgpF7KnFI_px7WCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-18071">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/SBoxxx/18071" target="_blank">📅 10:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18070">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SBoxxx/18070" target="_blank">📅 08:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18069">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=EQLxsTszCEj4Tvd5XXys6qpOnSLZWWxBcNPGK5hRUEh5Hrr_pc9j5azWsggxmnMnsoRgqSMOMRw4WfK6j7PlNEHA0Sa1y0uCfWrM1mCPAz1dY_ejWYq7PScqSiHpYBdsHI-XS-uYm-pGKndBNk2W2WxpX0KkVd7hTdN2_1g4rqiEmLlcRdj37SZRvXIcQeCXhvzhoHLmWT5W3mGZEIKjnYGvZtzqZeN3M1HYt-XmsHHi0jVaF-hpemJ6SHzXsz279KlRMuL8Ax7ndONcg_ji4TLT3AB9OjkU6H-hMRTOFsjnZVyi7u7ujFFn_936SW6SNSeQNT9vzC7Ed8mhpJndpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5daefe620.mp4?token=EQLxsTszCEj4Tvd5XXys6qpOnSLZWWxBcNPGK5hRUEh5Hrr_pc9j5azWsggxmnMnsoRgqSMOMRw4WfK6j7PlNEHA0Sa1y0uCfWrM1mCPAz1dY_ejWYq7PScqSiHpYBdsHI-XS-uYm-pGKndBNk2W2WxpX0KkVd7hTdN2_1g4rqiEmLlcRdj37SZRvXIcQeCXhvzhoHLmWT5W3mGZEIKjnYGvZtzqZeN3M1HYt-XmsHHi0jVaF-hpemJ6SHzXsz279KlRMuL8Ax7ndONcg_ji4TLT3AB9OjkU6H-hMRTOFsjnZVyi7u7ujFFn_936SW6SNSeQNT9vzC7Ed8mhpJndpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/18069" target="_blank">📅 08:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18068">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارشگر صداوسیما یک دقیقه قبل از حذف ایران از جام جهانی:
یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/18068" target="_blank">📅 08:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18067">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه ۳ بعد فوتبال یک روحانی  را آورده او هم آفتابه را گرفته روی همتی که چرا گفتی از دشمن گندم وارد کنیم مگر گندم تراریخته نشنیدی!</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/18067" target="_blank">📅 07:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18066">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وقوع انفجارهای جدید در کویت و بحرین
هم‌زمان با انتشار گزارش‌هایی از وقوع انفجار در بحرین و کویت، وزارت کشور بحرین از فعال شدن آژیرهای هشدار و درخواست از شهروندان و ساکنان برای مراجعه به نزدیک‌ترین مکان امن خبر داد.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/18066" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18065">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عراق عملیات گسترده ای را علیه سیاستمداران عراقی وفادار به ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/18065" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18064">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تحلیل همین است.   این مواردی که خبرگزاری مهر گفته هنوز تایید نشده.  پاشنه آشیل توافق هم بند مربوط به لبنان است</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SBoxxx/18064" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18063">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ
:
هواپیما های ایالات متحده بار دیگر ایران را بمباران کردند چرا که بازهم آتش‌بس را نقض کرده بود.
احتمال دارد زمانی برسد که دیگر نتوانیم منطقی باشیم و مجبور باشیم آنچه به صورت بسیار موفق شروع کردیم به صورت نظامی به پایان برسانیم. در این صورت دیگر جمهوری اسلامی ایران وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/18063" target="_blank">📅 06:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18062">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
فرماندهی نیروی دریایی سپاه:
شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
‎</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/18062" target="_blank">📅 06:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18061">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گویا صدای انفجارهایی در بندر لنگه و قشم نیز شنیده شده</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/18061" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18060">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بیانیه سنتکام:
«پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی M/V Ever Lovely، به ایران فرصتی داده شد تا توافق آتش‌بس را رعایت کند، اما وقتی نیروهای آن در ساعت ۴:۳۰ صبح به وقت شرقی امروز با پرتاب یک پهپاد یک‌طرفه به کشتی M/T Kiku حمله کردند، این فرصت از میان رفت. این نفتکش پرچم پاناما در حال عبور از نزدیکی تنگه هرمز بود و بیش از ۲ میلیون بشکه نفت خام حمل می‌کرد.
نیروهای فرماندهی مرکزی امروز در پاسخ مستقیم به تداوم تهاجم ایران علیه کشتیرانی تجاری، حملاتی را آغاز کردند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپادها و قابلیت‌های مین‌گذاری را هدف قرار دادند».</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18060" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18059">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک منبع نظامی ایرانی به صداوسیما گفت:
«صداهای انفجار شنیده شده مربوط به برخورد چندین پرتابه به برج مخابراتی در سیرک است».</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/18059" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18058">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18058" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18057">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی به سمت کشتی‌های متخلف در تنگه هرمز تیرهای هشداردهنده شلیک کرد. صدای انفجارهای شنیده شده در شهرستان سیریک و جزیره قشم در استان هرمزگان به این علت بوده است.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/18057" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18056">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش‌های اولیه از حملات هوایی آمریکا به جنوب ایران.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18056" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18055">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مجلس خبرگان رهبری بیانیه داد:  باز کردن تنگه هرمز ممنوع است و هرکسی که به ترامپ و نتانیاهو دسترسی پیدا کند، بر او واجب است که آن‌ها را بکشد. ﻿حاکمیت ایران باید بر تنگه هرمز اعمال شده و از طریق آن عوارض دریافت شود تا خسارات وارده بر کشور بازسازی شوند. ﻿</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/18055" target="_blank">📅 23:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18054">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=YWQ0gorTcXMqW9lY72Vxp44xKcN7hvg7Z6S4qbQLaZidhyiREuRppZaANhTPAU4bZarau87ZabRBiOWAD6X7Sk31qzP822YdmpgP_ma48GDsisaqczRfPmvVH5DF9q3Vpcxwz4XnM2MLRqeNyxmuvWRT_Oi0WE0fAikR8XQc609nyO9TyH7QrQOC5VrNpGtT17TsD-l32y7QvRBX2Zi_6Uapiv8Wrd25XAoiSnLuY03puO-ER7thmiw38-KD8Krt5V1BaGszzBLBKgsm0bBNbRoOk5YmgBbj1PMG7gUSePK0PvH-FdqpstjOP6u5mF-s-oxSaCFmz6u_Ab6cIWGh3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39aee93e2.mp4?token=YWQ0gorTcXMqW9lY72Vxp44xKcN7hvg7Z6S4qbQLaZidhyiREuRppZaANhTPAU4bZarau87ZabRBiOWAD6X7Sk31qzP822YdmpgP_ma48GDsisaqczRfPmvVH5DF9q3Vpcxwz4XnM2MLRqeNyxmuvWRT_Oi0WE0fAikR8XQc609nyO9TyH7QrQOC5VrNpGtT17TsD-l32y7QvRBX2Zi_6Uapiv8Wrd25XAoiSnLuY03puO-ER7thmiw38-KD8Krt5V1BaGszzBLBKgsm0bBNbRoOk5YmgBbj1PMG7gUSePK0PvH-FdqpstjOP6u5mF-s-oxSaCFmz6u_Ab6cIWGh3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داشتم به این فکر می کردم که ویدیوی التماس جواد خیابانی به الجزایر برای مساوی نکردن با اتریش را دیدم!  یعنی هر چه شما می خواهید به خودتان بقبولانید که دیگر به نوک قله فلاکت رسیده ایم و دیگر  تپه ای برای ریدن نمانده یک دفعه می بینید یک کصخلی پیدا می شود تا به…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/18054" target="_blank">📅 23:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18053">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مدیرعامل شرکت خدمات انفورماتیک:   تلاش می‌کنیم اختلال بانک‌های ملی و صادرات تا پایان وقت امشب برطرف شود</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18053" target="_blank">📅 23:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18052">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت   اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.   دو بیانیه…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18052" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18051">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">به نظرم در شان ابرقدرت چهارم دنیا نیست که اینطور بانک هایش فلج باشند.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/18051" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هیچ حمله سایبری در کار نیست.  MV = PQ  وقتی M را با چاپ پول برده ای بالا و از آن سو Q هم اگر افتی نکرده باشد دستکم رشدی هم نکرده، قیمت ها یعنی P باید منفجر بشود. پس تنها راهی که داری این است که از سرعت گردش پول یعنی V بکاهی و آن را بندازی گردن اسراییل و نت…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18050" target="_blank">📅 22:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.
عین بلایی که سر ما تریدرها آورده شد که آخر هم نفهمیدم ترید فارکس قانونی است یا نه! عمداً فضا را خاکستری کردند — نه آزاد نه ممنوع — تا هر وقت بخواهند باج بگیرند و هر وقت خواستند رها کنند و هر وقت خواستند بزنند و ببندند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18049" target="_blank">📅 21:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الجزیره: اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/18048" target="_blank">📅 21:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18047" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWx8PF48JsGs2ghriHHSjgY9J06oK5ONGShzkKFFzIM6v3w6_rIuLO8OzzmCmRzZ-dh46MV44QksSgEv57W9VuRjdjqH6JLo-trmvq-GKN_U0-JaOQ1pkKSi5HIgF8i2fKDHcfdF1RtlyzlnZfHwMK-b5yq7-UKZE3NoDQ_7sQXZj6R2HlccUglC6CM0mJuOs1_MmuY6BgzoSfwLOzPhSRoDrztSHydMkfOcK_fSedK7YzPigWEk0hcvwur484uNtlPgsglvKGByB2XNl3Miey0fD95djIv9z17OIgbXi55B9bFuOL_0Tar8yAUgGQyGlVuKvQx4Gp4slbH8_UYx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!  مصر برای اینها چه کرده؟!   دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.  آن…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18046" target="_blank">📅 18:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=rv35K95AWV1Kz4HgN4a3QXtADHTQyr99460hkCNYCs3p-JkHj7GcVLdzpSg89mEH8Wo2Pqk-Jbvsm2O1P8gDBoPpAUHiD-Km2BIUTfahE3hjm0GEaN9ubKw9SeIhgTSw26s93z9L3S9X8w8Tb9ANJhlSUZQ039_aeIZ6dFDwnRvvyB0vjyPJDO_wJFg1aVnEP1eBpjN6zNPIR23Rg9-hCovDGP0yA5AC0FwKnT78lztKh0WF0kKjVD6mr30_aefiwu8qeBgXFrKg9Rskbi0BXhV7ETnbwCmtZeJFxaRbZWzWgFbPHdozxj6ewrgxW7T_WmxrL35_5noqpdLcpPze0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd3cf871.mp4?token=rv35K95AWV1Kz4HgN4a3QXtADHTQyr99460hkCNYCs3p-JkHj7GcVLdzpSg89mEH8Wo2Pqk-Jbvsm2O1P8gDBoPpAUHiD-Km2BIUTfahE3hjm0GEaN9ubKw9SeIhgTSw26s93z9L3S9X8w8Tb9ANJhlSUZQ039_aeIZ6dFDwnRvvyB0vjyPJDO_wJFg1aVnEP1eBpjN6zNPIR23Rg9-hCovDGP0yA5AC0FwKnT78lztKh0WF0kKjVD6mr30_aefiwu8qeBgXFrKg9Rskbi0BXhV7ETnbwCmtZeJFxaRbZWzWgFbPHdozxj6ewrgxW7T_WmxrL35_5noqpdLcpPze0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فلسطینی ها در غزه پس از گل مصر!
مصر برای اینها چه کرده؟!
دیوار کشیده تا از شهر موشها (غزه) به درون مصر سرازیر نشوند. یک بار هم ارتش مصر فاضلاب خود را به تونلهای حماس سرازیر کردند که باعث شد چند ده تن از اعضای حماس به دیدار خالد بن ولید بشتابند.
آن وقت هواداران جمهوری اسلامی، ژنده پارچه چرکین کشور خیالی فلسطین را با خود به ورزشگاه برده بودند و این هم جوابشان!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18045" target="_blank">📅 18:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">UKMTO:
گزارشی از یک حادثه در تنگه هرمز دریافت شده است.
کاپیتان نفتکش گزارش داده است که توسط یک پرتابه ناشناس مورد اصابت قرار گرفته است. این کشتی به پل فرماندهی خود آسیب دیده است؛ گزارش شده که همه خدمه سالم هستند. در حال حاضر هیچ خسارت زیست‌محیطی گزارش نشده است.
به کشتی‌ها توصیه می‌شود با احتیاط عبور کنند و هر فعالیت مشکوکی را به UKMTO گزارش دهند، مقامات در حال بررسی هستند».</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/18044" target="_blank">📅 13:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رودان هم جز میتوانست جزو گزینه ها باشد که ولی خب.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/18043" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/18042" target="_blank">📅 13:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سبحان الله! با Secret Box روزنامه فردا صبح را داشته باشید.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/18041" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18040" target="_blank">📅 12:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18039" target="_blank">📅 12:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjpmFuCC96a0YesW9hJLmoNO3bfCqc7V7-TLG-9ekDs28Vc5TzzBpArpb2zbHb7o33P2KeKYJdYtx11Lm0vlskJ7rNs_ixwgBSRuqmYgkiNyM0lv2Awgg0NE7L8NtPNS6AxFBkXMCdIDyipBgxpHQduHlPhFtRlIyICchKqOR8Apm1ZWeK4pUk1OIbbp-c0D9D4wVKtFPVtuFSOCIbIsbd-SMppuUdXDahndpZNw0zglKZyr5OojoQRtpOjhqhgk0CHrR2alTZng2uqK5NaEc9unVPJBJh_1LQq7nq-AYm7PM0FQ4kj_cypIIOjC-XT_aKrKBUUE1Q9KPJW4G6YGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفتی آمریکا و جنگ با ایران
آمریکا از ذخایر راهبردی نفت به‌عنوان ابزاری برای مدیریت شوک‌های بازار و کنترل فشار انرژی استفاده کرده و کاهش اخیر این ذخایر باعث شده بازسازی آن‌ها به یکی از اولویت‌های مهم واشنگتن تبدیل شود.
برخی تحلیلگران معتقدند کاهش تنش در خاورمیانه می‌تواند علاوه بر اهداف سیاسی و امنیتی، فرصتی برای افت قیمت نفت و خرید مجدد نفت در سطوح پایین‌تر جهت تقویت ذخایر راهبردی آمریکا فراهم کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/18038" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZ27rYz05lKuunCWNm-8y3wfM7TnEUMlBhvCkP7T-wI46j7yuAAKrPeDcw4ylcH9z5rOpojfS3QVbmIYsOgJvY8-0dkWRGny16JPe1ViNtDg_-O9MsJLoEykBPyAnVFwea75uNGyYv9_JAnDCBmUZW6k1AHo78SU9va_SviUa1ca5Aj58Fj3-cACKZL26X_z1IUaP0NO9321h7owLQFDvmJFgYPC5wzhJSNLcxdecBNfLznV5SAyiYqtrl9grpBfvy77-WmHQF_WGwgh6xHOSgsOrF1dJi15fnx68dEKcYtqQEzx9O2EC7k76eYyXV-DQ1WY56QzurgCspWpfpakdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه بازی</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18037" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSDDympHiiCvhoFSgK1Uk9jWn3Wt3s0yo9Z06x8iIiaJlRsxOHWAELqwsYFZT8B3Y1DfkVsxfIeO_ENTKPuNMmxbkYtwND17SlLyk8KdIZGoGlGo7Ffg-5iCfcoiRYhZM9DiXe3Vs4HXEFVLM9TWS54MaMVItrSD8GMm71tmjL_5jBe9jWoyFNRHy7K9c79lXcT7LB_SX3wYqyXWGJEm5-btvROIAaLvlM2PgphJVv744Ozy_FspGgQCWaZdC61llWHgm3eBsTr1KSLLEbTEU609q52MSxtOCoRyib1leeLF2gLMALxTZS9AZHwgaYN4bh5QI7_bYq8pLY5r9GrIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18036" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">الان تو زمین بگی محمد‌ حداقل بیست نفر تو زمین و ده هزارنفر نفر تو تماشاچی‌ها برمیگردن‌ میگن جانم؟
• میرزا •
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18035" target="_blank">📅 07:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18034" target="_blank">📅 02:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه‌های دولتی ایران: سپاه پاسداران چندین پایگاه ارتش آمریکا در منطقه را هدف قرار دادند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/18033" target="_blank">📅 02:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس ایران: ترامپ هیچ تعهدی به اصول مذاکره یا آتش‌بس نشان نداده است</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/18032" target="_blank">📅 01:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">متن اعلامیه سنتکام:
حملات ایالات متحده به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — به
عنوان پاسخی قوی به حمله دیروز به یک کشتی تجاری که در تنگه هرمز در حال عبور بود، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۲۶ ژوئن حملاتی را علیه ایران انجام دادند.
پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد حمله یک‌طرفه به کشتی M/V Ever Lovely حمله کرد، هواپیماهای آمریکایی به محل‌های ذخیره موشک و پهپادهای ایرانی و سایت‌های رادار ساحلی حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
این تجاوز بی‌دلیل علیه کشتی‌های تجاری توسط نیروهای ایرانی به وضوح آتش‌بس را نقض کرد. علاوه بر این، رفتار خطرناک ایران آزادی ناوبری را تضعیف کرد در حالی که تجارت به طور فزاینده‌ای از این گذرگاه حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM به ارائه هماهنگی و حمایت برای عبور ایمن کشتی‌های تجاری از تنگه ادامه می‌دهند. نیروهای نظامی ایالات متحده همچنان حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اطاعت و به طور کامل اجرا می‌شود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18031" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حملات تروریستی گروه های تجزیه طلب به ایستگاه های مرزی در بانه</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/18030" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سنتکام   به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18029" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEoIPQy7OcWFQoLUk2hEyq_qCkR3CF64LWi68QoPDSSbqyiegDwJtAwiAXlxubNoNxw4MIKoArY_Fqfh0JUU3a7s1R4OxUdkjITR7e4GGQZrx_HdYUK1DEoHhIO_cBdb3sv-3MstdhDj4UCTOp9tKgXopmNYHoJLDrIP2TFgLYaGCbmFiorYXkN-MBdrMPiAn4onVvKautPzFGP3NWQhIfWBt8d8zfdThkj9QFzfJaVPpVU5EZ1WAEadClLbG34THeew2jz2Pq8VjzPJ72sYE5215Z-Zp76qvd9YbwA0hklvp7Gu8joIeU10mWjRNoqpoOBdJ82LnIdwBAe9y8_72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مثل ما نفت را خریده.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/18028" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18027">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الان است که اربیل یا بحرین را بزنیم!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18027" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چادرملو! صد تبریک! / مردک نزن تو سیریک!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18026" target="_blank">📅 00:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فعال شدن پدافند قم!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18025" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان را آوردند که جنگ نشود؛ هر 36 ساعت یک بار جنگ داریم!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/18024" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">به نظرم بهترین پاسخ زدن رودان باشد؛
هم آتش بس نقض نمی شود هم به هر حال پاسخ داده ایم و هم دل جمع بزرگی از مالباختگان خنک خواهدشد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/18023" target="_blank">📅 23:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCHu-fWS8G2uXvH0fyuZ6yJujGyPrPRrn6tKCWU87mufVDeKdisDxm-fH1LfGnRnEluONDzfCy8CCUoaAX7EhwuFWbJxl9VWYVV6TFULBAd-g6Tby6B5RJrOnW01xDoef2P8HZoVJgZOtjBjrp8fVTd6JFy_2R4z6F6CBE60SimMT5a0jeZGseju1ktTlmdCijtZe8IcCPE-JzgrUkHzYZSVqX4LwzRVHTppdOBju_AJn7yv-I6ScFVGhzAfm72uzNHixi6CQQcJEq7Hw1rQZnome5bvdrQ9-nS7XahXul4LiuAe-5plF8DJDtIxX-PwxsU0fij2KISiM-2SsXsjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید حمله آمریکایی ها توسط یکی از همراهان باوفای Secret Box در بندرعباس!</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18022" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18021" target="_blank">📅 23:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام
به دستور دونالد ترامپ و در جواب شکست آتش بس توسط جمهوری اسلامی عملیات محدود ما در ایران آغاز شد</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18020" target="_blank">📅 23:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/18019" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ اشاره کرد که ارتش ایالات متحده ممکن است پس از نقض آتش بس توسط ایران با پرتاب پهپادهای تهاجمی به کشتی‌ها، با زور پاسخ دهد.  "خواهید فهمید! آیا من پاسخ خواهم داد؟ خواهید فهمید."</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/18018" target="_blank">📅 23:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18017" target="_blank">📅 23:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند  طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/18016" target="_blank">📅 22:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هیئت مذاکره‌کننده ایرانی قبل از مذاکرات، کتاب ترامپ را مطالعه کردند
طبق یک گزارش، مذاکره‌کنندگان ایرانی قبل از ورود به مذاکرات مستقیم با ایالات متحده، سبک مذاکره‌ای که دونالد ترامپ دنبال می‌کرد را از نزدیک بررسی کردند. این نه تنها شامل روانشناسان بود، بلکه آنها کتاب «هنر معامله» ترامپ را که در سال ۱۹۸۷ منتشر شد نیز مطالعه کردند.
این مرحله نشان می‌دهد که چگونه ارتباطات غیرمنتظره‌ای در مورد فعالیت‌های ترامپ در رسانه‌های اجتماعی در طول درگیری پدیدار شد. بنابراین، طرف ایرانی سعی کرد درک سیستماتیکی از الگوهای مذاکره او ایجاد کند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/18015" target="_blank">📅 22:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آمریکا، اسرائیل و لبنان یک توافقنامه چارچوبی امضا کردند که بر اساس آن اسرائیل یک منطقه امنیتی در لبنان را حفظ خواهد کرد.
ارتش اسرائیل نیز آزادی عمل خود را در این منطقه امنیتی حفظ خواهد کرد -</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18014" target="_blank">📅 21:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:
بنیان‌گذاران ما در اعلامیه استقلال چهار بار به خدا اشاره کردند. چهار بار.
من حتی یک بار هم ذکر نشدم. من بسیار ناراحت هستم. حتی یک بار.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18013" target="_blank">📅 21:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR_CtzbkMhXCO7rPOZ6bqTynQY16j9pFLE2GgZus6QljPVufI92akN_8N9Gkc-veAV8lfJLRk250gmt_58pIHlOm04HrSyINWNaPLDqjo47mHd93Tr4pKqFuEJEwf4OgHv0rf1Fm_4DQ7CEE8yCvl7CiCEgYOGrCVYQQfDS8cTjEGFqMNZJnYRrjluVDaFNnx0YvrDrK7dgQ_BMzsvDljlLjHkbFl2daFfzzN2Wu-N9KaeOkXesq5HeyczzRdet-wgxl43E1ytUsMakad9zwmD8YRvjq24ovBykm4u-dDTKcPXgsuK-2jzKwdyE3L_-MfuqfA65GkC1hqD6EaTc5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18012" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ ایران را به نقض آتش بس متهم کرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18011" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18010" target="_blank">📅 19:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLnjjUzhjmlnrCfwlAWiG7iPxk1yKwhfFJXhcvetu9qNDVBaBWjNyT2DZwMRzJkYqenD2yIFOA68CEqofYyOY1sPxX9sRtK0Oh8rF3aa2KYrmXQ6lbsc2PgfjxVirocw0UHmBZUXv1FhlBiHHpQ6c7-YmKb4moFVic0tGOub3sKtHUCH59IUvDNsoTYy3R0Gc6LH59DRpcgNf3VFgEKbH5xbCgankkswWNA0BxnfVvy6XbX5C_dxCPQKouealPEFK2rafCvQebPW6EacDX5RjLEGRwe_61e785qNpsmW_3OdcwlWCsqSbUc8W9eFz69od9-l4SvnaXFRlLwTJkwSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق کنید.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/18009" target="_blank">📅 18:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/18008" target="_blank">📅 18:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بانک ملی ایران در اطلاعیه ای از اخلال مجدد در خدمات کارتی این بانک خبر داد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18007" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسرائیل درصدد به‌رسمیت شناختن «کشتار ارامنه»  وزارت امور خارجه اسراییل پنجشنبه شب اعلام کرد که «گدعون ساعر» وزیر خارجه این رژیم روز یکشنبه آینده پیشنهاد به‌رسمیت شناختن «کشتار ارامنه» را در دولت مطرح خواهد کرد.  شبکه المیادین نوشت: بر اساس این گزارش، این اقدام…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18006" target="_blank">📅 18:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18005">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7CB-pUUDBA4L5lsPub2umw4Y87I2k9KV6Z2wnxmbb1lixi-wBfsbsNtm-yMdJbaZu3KMhajmkpkGhHAXZJY58TiTYNm9wu4EM5CR-QpMcDRQdGI3eFmCH_vNU43YSYhsz9MyZpY1y9go5pnJAC_7MR1OEEGzwKSPvxeUTI6goP8JjoppWmWPLX5O7I072HLXLIXn2z8NjKw7wVZ3p6e8IrORnExgCg-Ht4JiIzAKHkx9uO7VN8tTr2qgcWt0r93tfTfDojb8WV9ZzGQm4RT7P1CwoUWp20j-sn_Ij6p9Tbwg_LazbVhnNn_7O0FGjv_LdUZvovOhiU3NxrnzXi17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!  پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.  ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18005" target="_blank">📅 18:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMD-dwdylh99LaFtfL3OeHiKwq89Q0TZCKjYP8ovtJCBzA7Sv1OxXSaZE0_Ent_ccmm7tHXPk51MWvh4rwwHJpiZiXKzUP-NUwH4J1JXg5KUcXHigiA4QO1oTKD7iNzrmP-lrZMd9ZJ4dLJ4Zitw-0NQCVNCBQArtW8HoldftbDIjXAnUaRUyt54BV6NNuSUF2DgEXcvIR-ESpdcmnQvTsKKSOd7mqWt6FM6xMY2-cgSdIQf_IDhGUTYWmEk1i_3PqpYb1ua0R5GvgE2f1FEVT9RvCE81umkOFdSZiXadWjmfxKEP6c-1iGesF7YTvQm3EjunfN_U8Uh5Qkj_6Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاتز وزیردفاع اسرائیل ضمن تهدید فرمانده سپاه قدس، آمده عراقچی، پزشکیان و قالیباف را هم تگ کرده!
در یک لیگ دیگر است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/18004" target="_blank">📅 16:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18003">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prgFMEXXdNHwf_M6EmyU6aJ2vFnsJfEWJ7YU1UGIocscO5tHbm_eSWpnNBs42T6knw6KTsnJf-FIWLj_44qmjCKVwJpUbiEM3JstBM4NAnezzK_xV-eVc2lLqfBJ-RWMH0QkW2BklF55LCfDJwwqUL38Dk-WZUCUcBSUqAu0P4cW-FxfWiUnnm7yhCPsb3yrl8jsy41lry9d_fgeRirDEUGkSyCwKlWD7fD1_-usinQZmP2d42GThnmtyK0HPizCu44w_54PMyRk-YzARfVybMikW82Bi-Ak3RCFdj7LT9fi1iH4RvYwhumgE34I2I9cGTD0XqTOBHHdPLiHy1LhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/18003" target="_blank">📅 15:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18002">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرمان پوتین برای ساخت نیروگاه هسته‌ای در ماه تا سال ۲۰۳۶   این نیروگاه انرژی لازم برای زیرساخت‌های سطح ماه را تأمین خواهد کرد  پس از سال ۲۰۳۶، روس‌کاسموس قصد دارد خودروهای هسته‌ای را به فضا بفرستد</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/18002" target="_blank">📅 15:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18001">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.  پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/18001" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18000">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انتشار اخباری تاییدنشده از پیشروی نیروهای زرهی اسراییل در جنوب لبنان</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/18000" target="_blank">📅 15:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17999">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/17999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_تحلیل_روزانه
#اپیزود_394
🗓
june 26, 2026
✔️
تحلیل گزارش PCE آمریکا
✔️
بررسی تقویم اقتصادی روز
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17999" target="_blank">📅 12:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17997">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePKo6s7sw23HRmu_s7fSQtnZZtxAy568luvaa-07qhwAdxg7KeviCOC_qaq4YlebGoMyNLFzaa9psQP9GgDw2ksldVavtwmIOFDHaEC7kYGLRw98lER42uuJqUKYzMxWrZlGgGWewjOuMTg3EIuP18h5zrB_-9yGJeOHwqjN6r3UK3_jFubam498irsdIefAbvgYw4R7uME9leFvOr_q7vvBZiKrqC7DB4bu1X-Abbh98sHVcxQAvW6GsdRyneFwWS7PlWQfjxat3hy6DNBqWHqdx31JgA1Nxdf0W59J79D4ZYz55Q-4uhn_Mc3QfXkD3wSrKNAo7G24rayPToPTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8E7arQd0trCGxqUDzMvOHoz9kmoCxEBOjMj2i9__UnrTwM3xI7GycDyg4XTjmvHWds_qrQCZK_cN8jeNZhPj_aWibkX31I56Wm9V3CMnHo-ONMSjRKRTWUEg8UeoAYrv5e2zhO7dOVvvkDBJoYPAwf0VffFU_hTqlmcSPIWfi6Ihxa33DEXISwJ_dhNtQT_iz3HIVAOL_1EetIm-mtnS50klKc5ffZ7S_q8wWKddpexPNI_9o8GLxMtJ32AWEFr567PZVH8X90rcI30qRdIguzAQ_TlVx0G_C9y3n5yvxWh4VCkMEytuYWkF743E-D-swKvwhTgtM4SA2ACa7Dmdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه وزارت خارجه ضد مواضع مشترک آمریکا و کشورهای عرب خلیج فارس</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17997" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17996">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنتاگون در حال بازنگری در استقرار خلیج فارس است و جابجایی نیروها به اسرائیل را در نظر می‌گیرد
طبق گزارش‌های رسانه‌های آمریکایی بر اساس تصاویر ماهواره‌ای، ایالات متحده در حال بازنگری در وضعیت نظامی خود در خاورمیانه است و در پی آسیب‌های گسترده به پایگاه دریایی کلیدی بحرین، جابجایی برخی از پایگاه‌های خلیج فارس به اسرائیل را در نظر دارد</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17996" target="_blank">📅 11:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17995">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیانیه قرارگاه عملیات مرکزی خاتم‌ الانبیاء (ص) :
تحرکات و حضور جنگنده ها و هواگردهای ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران را اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17995" target="_blank">📅 10:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17994">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ حرامزاده تا کنون همه ملت ها و رهبرانشان را — از کانادا و مکزیک تا اروپایی ها و عرب ها — تحقیر کرده جز:
— چین
—ترکیه
اولی را به خاطر قدرت خودش و دومی را به دلیل مجیزگویی رهبرش
برو قوی شو اگر راحت جهان طلبی
که در نظام طبیعت ضعیف پامال است</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17994" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یونجه و سویا واسه من
تنگه و دریا مال تو</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17992" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بوی گندم مال من  هر چی كه دارم مال تو</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17991" target="_blank">📅 10:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#نمیپذیرم</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17990" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17989">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:   ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟  برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17989" target="_blank">📅 10:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17988">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ
:
ما یک بازار جدید داریم، نامش «کشور دوست‌داشتنی ایران» است. جای زیبایی‌ست. کسی دوست دارد برود؟
برای تهیه مواد غذا مشکل دارند، قرار است مقداری از پولشان را بگیریم و  گندم، سویا و ذرت، بدهیم.  به مقدار زیاد. روندش به زودی آغاز خواهد شد. معامله بزرگیست.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/17988" target="_blank">📅 09:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17987">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📡
ترامپ فرمان جدیدی برای ساخت کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ امضا کرد
دونالد ترامپ با امضای دو فرمان اجرایی جدید دستور داد تا تلاشها برای ساخت یک کامپیوتر کوانتومی قدرتمند تا سال ۲۰۲۸ سرعت بیشتری بگیرد
این اقدام با هدف تضمین پیشتازی ایالات متحده در رقابت با چین در حوزه های هوش مصنوعی علم مواد و شیمی صورت میگیرد
همچنین آژانسهای دولتی موظف شده اند تا سیستم های حساس خود را تا سال ۲۰۳۰ یا ۲۰۳۱ به رمزنگاری پساکوانتومی مجهز کنند تا در برابر حملات سایبری آینده ایمن بمانند</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17987" target="_blank">📅 01:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الهام فعلا استراتژی مالش را آغاز کرده تا مثلا خود را در دل آمریکایی‌ها جا کند، غافل از اینکه ارمنستان با چرخشی عظیم به سوی غرب، در دلبری از واشنگتن و تل آویو ، گوی سبقت از باکو خواهدربود.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17986" target="_blank">📅 00:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17985">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWZBg_BMDCvBC2h0C0bX_4_7JlujvRmLKayTzH-IUuF4KGz_C0cuNPcL8G5lBSpiy2XcGT-r7bNJeAO6JiQAr7IUo6Guu6GrtIiZiEMzmqIx-0jWNXJ1_CizdgRapX-qLn4i5QjRlNHOWV5vnYIkKct-byw7ggLAguLPo8H-1m3QmbfdFhDGsxWu5PTJfL_5jnWkvgbklfuZjDw2cvXcBmCCj2LR9pkws3-5lEnC6GotEFRVMq_f51G8gZFQez0Rj6j7yepGV3FBSZnanlQ2B8E-CBINhdAwt0M286lXBmcfeV3mmfoxEEgEkeugWTbk2DD7-f_q3CzPj42fQZJUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا پس از انتشار این گزارش، حساب بسیاری کاربران ایرانی مسدود شده است</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/17985" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.  @Milita_Camp</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17984" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17982" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVex0Gs2gQuA5jU9sR-nfDbnnQv8oq3w3xbGtCIOE-jZBJkuC-WMCTipLCE0mxOC1wNOLkrniZ6u72_dlCRVrX0Ppg9PQ6EUTRCeT6iGqwJ97YukZVUweORDYTcawShfZYjLPF0aqs9uE93Ezn-P0-MstS1hE-VowEzpYbUt0sOV5PUCFp_BIO7bMucjxTPdnIontKtDMXKeJFXrOBMbV-ac3xA0Jq9Vpa5lV4BHT3hNsX6qKQWNbU0duY1pkLWsaarTxuProYuyd9aEq1PtR8aEVVfofFKcNOzGrQ12ghceDBdCRdN7YYZGdY_PSoPMFVXLO12PPpITT8wCXrPCZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- نیروی دریایی سپاه پاسداران انقلاب اسلامی با یک کشتی در فاصله ۷.۵ مایل دریایی از سواحل عمان درگیر شد.   این کشتی تلاش کرد تا از تنگه هرمز از طریق مسیری غیرمجاز و بدون هماهنگی با اداره تنگه خلیج فارس عبور کند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/17981" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17980" target="_blank">📅 18:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li7H_W-bahW9SZOlFzzr5glkjzay-CTyLq7U4ks-pozWOyXhkB5fCC1BMdBirJeRqBlhpe_SUQHu_enhNk30tDad2Cb3shjbFfBNbIyCfy96PUh1RAuKka_XsHtwpZZRR1NVGBJchdmU2VQdZmmxNKVcSeVjIIe8WuLwB3_uThb9EBE0tcpPETbI3p50INmld7WhZuEviP_XwNbMKk8vJobcNpUsIL6so1wNAsgPGVPF9wDEUaIxLHGM0OghojUhp_Zhwk0i3DFi4Zwb3ttQAg_lUCPrFIWFDMJhx9dEpvjpS-9z3QSCHv3T6BCOhG-8gQ8d-9R52THZxutaT1RprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3Yog4YGHDB74hbbZng9tJSxntcasFP_4-QkU5zCX2Ls_7f4SlgH1IPTMDye6d7qP6cZ0Hmy19GihlQG2wRZfFfSChxwmDnPfVeB9A2QWhlHMpR7xdCCrGOWcgcPLtjsY3MiwHhtpwhnC6XfkeIE3qZJI3Sv8XAzDwQ2bRVCELaPj0j3nBKthLOllvAvMf8dPuFU31PR4ykY7QOOBL_T4_tL5CmtkkgFbqrYXLajxhJ1vhp7kRyBsfHUPGSh4MZ_0ji_fEyplKhTFhAwZdeKMWtStLZniE3b3SQoPd1EZL8KtxVj4C5H56VEMOv2eLekahCzlhSir7Xi0QS3v0Od3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔸
به اطلاع همه می‌رساند
تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد
، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔸
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و
با شناورهای متخلف برخورد خواهد شد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به
گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/17974" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/17973" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/17972" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=sZSeV8WthZx_8sSg2pVg0u_vOhTjTFvH3nkfVopR8zn7_TXNT9lsxRk-NgsZdjD_4v6gWOGUV2xU056wk82Nmgd8F7bg4OhIUnU7ysaZJTivjS3aFo30q5Hgq71JhaVaMObfXRJlr1Ie1Y71NV27ZR5xfBmTImMS6nHl92pTb5I83NtpZ5ZVIgS_8mi-da5B4AWuaaywFHMjyFGkNux_b2Toe-8wAr9BA9C2NmkQ7h7_KCJkSAw7PigoDsnpAVtfOTmjmCyKT5TKDDFNy5CRhjwarzQy2lAnZSoqVNSVKbcISYvOToO1t7i1RcpyUPKIZTiMM85GwmP3zB9LUJ3xUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=sZSeV8WthZx_8sSg2pVg0u_vOhTjTFvH3nkfVopR8zn7_TXNT9lsxRk-NgsZdjD_4v6gWOGUV2xU056wk82Nmgd8F7bg4OhIUnU7ysaZJTivjS3aFo30q5Hgq71JhaVaMObfXRJlr1Ie1Y71NV27ZR5xfBmTImMS6nHl92pTb5I83NtpZ5ZVIgS_8mi-da5B4AWuaaywFHMjyFGkNux_b2Toe-8wAr9BA9C2NmkQ7h7_KCJkSAw7PigoDsnpAVtfOTmjmCyKT5TKDDFNy5CRhjwarzQy2lAnZSoqVNSVKbcISYvOToO1t7i1RcpyUPKIZTiMM85GwmP3zB9LUJ3xUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
