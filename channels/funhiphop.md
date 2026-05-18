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
<img src="https://cdn4.telesco.pe/file/Nln8KtexIZnlWl7nW0vlgJ580O3tZ2xxMB0gTGWXtR9s1FxC0S1_3KWXqyV1WAfnydY8eqGiBRWs0qYU9sETNYIfKEemdNU3OUtEj1wdCegSnOUlBEIxqrhqgJixSfCMgmvRKX3NswJEUh6BiTJJQ2TS49wKXYiXrXPCwfdtjyQkfREidCG_7yGpA4UUHT9Dq6j7pMzqrEDWYjpoNAL44A-wLU8-H37uO49QryaL7QZJCNmbWfHTSwYMXHp0YDS944NSDZ6wBKfH2xSUEDHIoLW4U7CfDwSWiU1fl4x9crCFL0S9xdxzsFBxgUMZ9ra-QUvBWouXTjg02XG0Up76JQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 152K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 23:41:53</div>
<hr>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBGIwVxQojR2xmHQQndKF7p1P03pteC3U-Kwc0Q-menOg3fHMCoJpVm2Wlo47zBfb1ziohT4qiDXJG7XczTeZIAHCTtKIh2SIJeyra5CzYXZTef8s-k_G-1LjIGjqifrNITKzDf0JHRUeE40z-2o2FiegBuvIWXjo3PTI6ALJ3VBz4fJZNzYtTNjpV4woU1UMWJ1xXkV3yXU_lhLrPhw_HqWry0iVRev2OpW4vV_O5yHQpFmlYEDl_EBaVj_hD0QSLUmJMcCzKWPBjD4boeeLRvXKOGEhrRXhmADzvaQHlwcbi7bTxnwm2eDUgDjpOdT8HdQfAiqWvfXkRXsVg_i7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
فیلد مارشال رضایی
برای حمله نظامی ضرب‌الاجل تعیین می‌کند و سپس خودش آن را لغو می‌کند!
با این امید واهی که ملت و مسئولان ایرانی را تسلیم کند!
مشت آهنین نیروهای مسلح قدرتمند و ملت بزرگ ایران آنها را مجبور به
عقب‌نشینی و تسلیم
خواهد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/75312" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فوری: پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 95 · <a href="https://t.me/funhiphop/75311" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">با رفتن پپ از لیگ انگلیس، دوران پادشاهی آرسنال با رهبری آرتتا رسما شروع میشه و تا سالها هیچکس نمیتونه جلوی این تیم رو بگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/funhiphop/75310" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فوری:
پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/funhiphop/75309" target="_blank">📅 23:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">باز حداقل الان ۱۰۰٪ سهام کمپانی های خودرو سازی داخلی دست خودمونه
نه که ۲۰ درصد بنز دست ما باشه نصفیش دست اجنبی‌ها
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/funhiphop/75308" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZyKskRAtu8gZRAVy8QkIUxhu1LLjQsvEOme97L__x0OO4UGJcpPyh0MpXZXb7RfZLcVAfz6XFuxa6xmPxHEMRf7S8xkGGFxhhSL5z-6byhGYfTUS-xlYHtWAA-Gf84K1wonenRZQrY7T1KfvH0An7GXUWHeJpA6u6dT6YQCfAZu_ligw3PpmQXr8NRb6yEjYkU7LjtLZ7Iw3kX7L84cXCucrbXwQQjOPiCG0QUwE-qqheHqTgKH0gc_mYchH20UU-lZ99m0YirmNT4kNIc7K7mLpxCnhFEsuPkSdlvU9jSPIp_4JeV7w0_dNPQkXyOg4FjZChVg3DAjMYpeiGlo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/funhiphop/75307" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUZxRsLae9hIW2cItF-8WNr65PQa614O8MmKNSRkQqcab-cV6-y13eBOeZ4rvB_SvvOeEsVoYHnP0nnBuToE0IFTjjABpsATV4brIzRKI_p2N-sf3Jo7OYxz7ewB7qgxuWPjH-DYvLXixggPwrAcfHq2nSNyuu3Ox-EqA0r6ULE3YE8tzvxTJo6T265DhmskOSMThsYeranx_x0g_mKnd5aeTwB8dMW1TZwlPdmsKqcyqtHngclyaybg1RB94afhXh01X4L1-8dXqEEpv6z6Pg44qmeRr23xsQCQsX8M67mqxaW1xxPDb1L7pI0QRvIFySwpiHjBGRisYqH1pGu08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم. به امید توافقی که خواهد شد که برای ایالات متحده آمریکا و همچنین تمامی کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
مهمتر از همه، این توافق شامل عدم وجود سلاح هسته ای برای ایران خواهد بود! با توجه به احترامی که به رهبران فوق الذکر دارم، به وزیر جنگ، پیت هگزث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین و ارتش ایالات متحده دستور داده ام که فردا حمله برنامه ریزی شده به ایران را انجام نخواهیم داد، بلکه به آنها دستور داده ام که  در صورت به توافق نرسیدن آماده باشند تا با یک حمله قابل قبول و در مقیاس بزرگ و کامل علیه ایران آماده باشند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/funhiphop/75306" target="_blank">📅 22:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرگزاری مهر:
فعالیت پدافند قشم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/75305" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بچه ها اگه کانفیگ میخوایید تهیه کنید میتونید از ایشون تهیه کنید، ۲۰ روزی هست باهاشون کار میکنیم کارشون درسته
قیمت: گیگی ۱۹۹
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/funhiphop/75304" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الان یادم اومد ک تتلو راجب ممه های گلشیفته آهنگ خونده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/funhiphop/75303" target="_blank">📅 22:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZChh6MAUkC7aeRs3lR4eN5mbxPoXmrjsYkFfSGtd2_Vem_xRCzV0JVk8SYsupqHTya2jc_Q2USkbctnrIinhRqjqX1eXpue19Z54rs1mtE99S6AN6ZnfrA6FMLPEyE0c8Uflx0ZBFQjLWxtZQ_tUhPBe3O-euuSXUvugTIf0cHZEf6iUTVZKDPdugdw7htS5pdsV2_f7wnJkjH6UhUtAytQDtGjxd-WqTPFWIn9-2kRFYDNpy2d5-tHeL_YB638nO-oR2wc8IhaTghaKq7uEEHt1-gnx9PM7TvxyF8WdazcujXvAZn6rmTC3QjqpeOgVSyTtXT3GGVguQeNKjlSeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/75302" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✈️
واشنگتن پست
اسرائیل برای آغاز دوباره عملیات علیه ایران آمادگی کامل دارد و اکنون منتظر تایید و چراغ سبز نهایی از سوی آمریکا است.
😶
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75301" target="_blank">📅 20:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: از آنها کاملا ناامید نشده‌ام و می‌توانم به شما بگویم که آنها بیش از هر زمان دیگری می‌خواهند معامله‌ای انجام دهند، چون می‌دانند که به زودی چه اتفاقی خواهد افتاد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/funhiphop/75299" target="_blank">📅 20:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وقتی نیویورک پست درباره اظهارات قبلی ترامپ که می‌گفت ممکن است یک توقف ۲۰ ساله در غنی‌سازی اورانیوم ایران را بپذیرد، از ترامپ سوال کرد، ترامپ گفت:  الان به هیچ چیزی تمایل ندارم. در حالی که از ارائه جزئیات بیشتر خودداری کرد. ترامپ در ادامه: واقعاً نمی‌توانم…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/75298" target="_blank">📅 20:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به نیویورک پست:  من پیشنهاد ایران را قبول نمی‌کنم. ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم. ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/funhiphop/75297" target="_blank">📅 20:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به نیویورک پست:
من پیشنهاد ایران را قبول نمی‌کنم.
ایران باید بداند که در این مذاکرات من حاضر به دادن امتیاز به ایران نیستم.
ایران خواهد دانست که «به زودی چه اتفاقی خواهد افتاد» پس از دیدار من با تیم امنیت ملی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/funhiphop/75296" target="_blank">📅 20:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الان وقتشه مکرون از گلشیفته به شیما کاتوزیان مووآن کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/funhiphop/75295" target="_blank">📅 20:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به العربیه:  ما کار بزرگی انجام میدیم و نصرمن‌الله و فتح الغریب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/funhiphop/75294" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdHSINLq42Ik7nfoC_nq_pT9oJ-e_4FMsbZvwyzcmdwjIVbWLUwDGAkMP_vHLdWu9BBMmppv4SYjC3DHXBrpciyv4Hl-UYvT4Za5hE790HbxZHzlQGR3cJ0IpWZ6-huBDTs1jn-bvJEfygU1UmopA5Iu4Ss8WQOUUOiKM_Bqdxikc6Is0mi2GeDOxQ6PFWhIeiFBKdurjM7oMTKNh4wI-2xkVqXiYHZ0zTKhVL6lJUnp2D-QC_GuTTDSzgRIJdPDETqOt1REmOxTYDJRUxkth-TyzQ7dwvfy5itXgMRfRLaYJaGmYWkaKu90gmQbR3SZZCCRGxRkBahf5MQ0lcKBVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا ارزش خرید داره، هر بازی بیشتر از پنج گل میبینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/75293" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">——• 4KNET •——
🔥
تخفیف ویژه سرویس V2ray
🔥
10GB 2500 —> 1900  •پایداری تا بیشترین حدممکن
⚡️
•متصل برای تمامی اپراتور ها
💯
•مدت زمان 30روزه
⏳
•بدون محدودیت کاربر
♾️
•لینک ساب برای مدیریت حجم
🧮
–کمترین مقدار حجم 1GB  برای دیدن لیست قیمت ها و خرید به چنل مراجعه کنید:…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/75292" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1G98u6IniXNBV4AcxDy9Da2jLUJoSu7D_odGU43vCQhIPux9Ba2i5Y3y8h79nqsgQ2IBbaYOUJCcnWi_rF_HlQz6wVDTj06YYC3lP5Zx7x-tmN1hCo3AoTCq7JXKbMuAtMfq3aQY6gd1ExXdAfXasfMdcOrhoXol2CzpnQMo4eruzFij-n1a7VrzJ9YA4bOIiE6lOYYzhEA-ffy1OMzmfhZUAd83aas46c6poezH07UbTWr35XpRRoiKmzCom1QjEadZmPZo4iE7GWhJtskq2VH_b6KHKC4ZZjGRBnWxDWbw0OU-_OuTGkLvpMQyEPXEvGBMirfY7puVr0dOUolNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">——•
4KNET
•——
🔥
تخفیف ویژه سرویس V2ray
🔥
10GB
2500
—>
1900
•پایداری
تا بیشترین حدممکن
⚡️
•
متصل برای
تمامی
اپراتور ها
💯
•
مدت زمان
30روزه
⏳
•بدون محدودیت
کاربر
♾️
•
لینک
ساب
برای مدیریت حجم
🧮
–کمترین مقدار حجم 1GB
برای دیدن لیست قیمت ها و خرید به چنل مراجعه کنید:
——•
4KNET
•——
پشتیبانی :
@SUP4KNET</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75291" target="_blank">📅 19:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آکسیوس: یک مقام ارشد آمریکایی گفت پیشنهاد اخیر ایران برای توافق ناکافی است و هشدار داد در صورت عدم پیشرفت در مذاکرات، احتمال از سرگیری اقدامات نظامی وجود دارد. انتظار می‌رود ترامپ روز سه‌شنبه با مقامات ارشد امنیت ملی دیدار کند تا گزینه‌های نظامی ممکن را بررسی…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/75290" target="_blank">📅 18:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✈️
آکسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/funhiphop/75289" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✈️
آ
کسیوس
👾
کاخ سفید پیشنهاد به‌روزشده ایران را بسیار کمتر از آنچه برای توافق لازم است می‌داند.
🔜
یک مقام ارشد آمریکایی آن را تنها شامل بهبودهای نمادین توصیف کرد، با زبان قوی‌تر درباره تعهد ایران به دنبال نکردن سلاح‌های هسته‌ای اما بدون تعهدات دقیق درباره تعلیق غنی‌سازی اورانیوم یا انتقال ذخیره موجود اورانیوم بسیار غنی‌شده خود.
🔜
این مقام هشدار داد که اگر ایران از موضع خود کوتاه نیاید، آمریکا مجبور خواهد بود مذاکرات را «
از طریق بمب‌ها
» ادامه دهد و افزود: «
ما امروز در موقعیت بسیار جدی هستیم. فشار بر آنهاست که به شیوه درست پاسخگو باشند.
»
🔜
هیچ تسهیلات تحریمی بدون اقدام متقابل از سوی ایران اعطا نخواهد شد، این مقام افزود و گزارش‌های رسانه‌های دولتی ایران مبنی بر موافقت آمریکا با لغو تحریم‌های نفتی را رد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/75288" target="_blank">📅 18:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بمب پشت بمب: آمریکایی‌ها باید دریابند که ایران به هیچ وجه با اینکه پایان جنگ در گرو تعهدات هسته‌ای باشد، موافقت نخواهد کرد. ایران درباره ضرورت پرداخت غرامت توسط آمریکاییها به دلیل تجاوز نظامی به ایران، بسیار جدی است.  اما آمریکایی‌ها با وجود سخن از چیزی به…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/75287" target="_blank">📅 18:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌شان از بین رفته و در ته دریا است، و نیروی هوایی‌شان دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود.
دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند.
آنها کاملاً دیوانه شده‌اند!!!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75286" target="_blank">📅 18:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کان نیوز:
نتانیاهو امروز جلسه امنیتی محدودی با مقامات ارشد دفاعی و چند وزیر درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/funhiphop/75282" target="_blank">📅 18:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بمب جدید تسنیم: اختلافات اصلی ایران و آمریکا همچنان حل نشده باقی مانده است؛ منابع می‌گویند آمریکا هنوز خواسته‌های غیرواقعی دارد. یک منبع نزدیک به مذاکرات به تسنیم گفت ایران در پایان دادن به درگیری، بازگرداندن کامل دارایی‌های مسدود شده ایرانی و درخواست غرامت…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/75280" target="_blank">📅 18:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/75279" target="_blank">📅 17:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">العربیه: ایران در این پیشنهاد جدید خود خواستار آتش‌بس چندمرحله‌ای و بلندمدت است و همزمان بر بازگشایی تدریجی و ایمن تنگه هرمز تأکید دارد.  در این طرح همچنین از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/75277" target="_blank">📅 17:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:  آمریکا در مذاکرات نشان داده است که در برخی موارد انعطاف‌پذیری دارد، از جمله در محدودیت‌های مربوط به برنامه هسته‌ای ایران. با این حال، آمریکا تنها موافقت کرده است که ۲۵٪ از دارایی‌های مسدود شده ایران را در یک بازه زمانی مشخص…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/75276" target="_blank">📅 17:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDon Quixotet</strong></div>
<div class="tg-text">رویترز فیکه بخدا</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/funhiphop/75275" target="_blank">📅 17:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:  صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در رابطه با ایران در حال تمام شدن است. رئیس‌جمهور ترامپ تمایل دارد اقدام نظامی انجام دهد مگر اینکه ظرف چند روز چیزی از ایران دریافت کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/funhiphop/75274" target="_blank">📅 17:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:
صبر رئیس‌جمهور ترامپ به دلیل عدم پیشرفت در رابطه با ایران در حال تمام شدن است.
رئیس‌جمهور ترامپ تمایل دارد اقدام نظامی انجام دهد مگر اینکه ظرف چند روز چیزی از ایران دریافت کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/funhiphop/75273" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAKkHq843aQMXdK3h0kDBLVV2E8Ua8znym0v5_ilJRoAgsif8E3Qxy2BE0Lo2fpD9it0y_SgmV75qwBsPrJjisj46IrV4PsrE18GAY2tZaK3hzedFvkIw5sin7gErSGDFm0w6gadwA3Nw_m_cc4qAniUSokZ2rGbGIs6cSREApF-CLNd-rpprZEZ1n9lXNJEC0u9ZfW_6EB9hY_y-oulvoa6Gi9ClyKEDqYTfzgmNvGM0Dnv2LcOKRTN7Ev3c-kBOdQoOWHqWoziAjRUEcKHfC9TO6snUA51eXfpGrCPZ6BquGF3rS5hxCYoECjr7zFOeT2tkCOAYufdi099EV0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/75272" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw--TwXPesRp4lvJiB2k0MwiP7tfP7L986isaR0GQSF4-Y2dE3h0uVTRBzD2UAUZnnRs0obnKP6UqTyKD6cVC0_FmHIJ38sE8lm-BoxVbp5wd8x-0AGvCCTwC7hcQdWLtH7GgjsjHC8trhe6agewLUWg7ReFFY24KkSvYJRN2MaTBXPhfS0gFwrwT4JvEyn2YJyL-NPCkjOMX4pSyUJWDUFZ1btG2NlBMnOmBXubDPtxLysIMEhGMa-tiwD55K741OE5c0GVQfBeAJUlqnmgz3r6V49KScWejUim1cc-dc9CE_iALkaSD3gy58FJZ6CwSaewb6Y8mYvabW8eGK7osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بد واس رئالی ها فعلا قرار نیست جام ببرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/75271" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الحمدالله اقا سالم هست
توضیحات مدیر روابط عمومی وزارت بهداشت راجب زخمی شدن مجتبی خامنه‌ای تو روز اول جنگ:
۱۰ صبح روز ۹ اسفندماه در وزارت بهداشت بودیم که تماس گرفتند و به ما گفتند که حوالی پاستور بمباران شده و جنگ رسما شروع شده است.
دکتر ظفرقندی، وزیر بهداشت همان لحظه تماس گرفتند و جویا شدند که آیا مجروحی یا مصدومی را آورده‌اند و بنده گفتم که تا این لحظه خیر.
آقای ظفرقندی با موتور راه افتادند و به سمت بیمارستان سینا رفتند.
حدود ساعت ۱۲ بود گفتند که آقای سیدمجتبی خامنه‌ای را به بیمارستان سینا می‌آورند.
خوشبختانه اتفاق خاصی برای رهبر انقلاب نیفتاده بود. فردی که در محل چنین حادثه‌ای باشد، طبیعتا چندین زخم بر روی بدن خود خواهد داشت.
این زخم‌ها نیز زخم‌هایی نبود که بخواهد چهره رهبر انقلاب را مخدوش کند یا اینکه همانند امام شهید ما جانبازی بگیرند یا قطع عضو داشته باشند. اصلا اینگونه نیست.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/75270" target="_blank">📅 16:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI9s-aXNIdBcYq17H6C4qP7tcJaSOthOFC0b4uAEbybxCWZCRH3AIawsOG1yKdXAl9c72dAn6WbLoCE_HPSR8FZ27p99EbZomHvNq5xdquzPGE2m4L9RZtMw_A5J5vSBGZcBWiMKf-9TI8PWKLpCYuBAlxasD-8Gwj7ajk7o45WMOQslfvQiMyOMHvrSluUDuDw6149EyHeXjxf4uobvN83qQakpdyWHzOXLz2NUyPT90Rn-elCpKPmcSheB4yF2cUp3kGg2yhiDnHUsRVGG48gWadvE4OCPipGm7IwKXn8G_z5HL60VRcO2aG0H_uZt6Kph3M9kXgObeefiyt10Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات کی برگزار میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/75269" target="_blank">📅 15:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNCQLlOdlUd-MdjB9sAXwdauW85LlTYmyn0xNiy1JhZXZYiORtMO5i-gDeIf-7DmmKaRZZfPJKzH1ubI6IqRiibKQ-Dj-w9tp6CJBELdAl-7-LrubxUYTFDv-dgErExnBqhc6t7eXq-v6dE8wkc7WkkLNl87H4W90lBHq1DquQN0V427NmDFLYbtkr_WcoT3kuSIPylynVnBfEwexTwIpAyyOQdjN4O5lg0Z0chyPiqwLi2D2HktG3o_06pgSmk_qRA0k4GnVwddVBZWWK35i9I1hHKWU4y07dauqI9az2jIdKP3v7hfTC12MDluEVn7BOxeOww7NzIvtf_gBf_yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید   این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست  بنظرم این شرایط باعث میشه که جمهوری…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/funhiphop/75268" target="_blank">📅 15:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید
این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم
خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست
بنظرم این شرایط باعث میشه که جمهوری اسلامی قبل از شروع حمله دوباره یک پیشنهاد طولانی به آمریکا بده و باز از برخی از مواضع خودش کوتاه بیاد تا ترامپ رو متقاعد کنه که دستور حمله رو صادر نکنه
ولی این پیشنهاد هم مثل همیشه توسط ترامپ رد خواهد شد و دور بعدی حملات شروع میشه
هدف اصلی حملات حذف یک لایه دیگر از مقامات جمهوری اسلامی هست که به شدت مخالف توافق هستند
تنها چیزی که مشخص هست اینه که ترامپ خیلی زود تصمیم نهایی رو میگیره چون باید قبل از انتخابات کنگره کار رو تموم کنه وگرنه انتخابات رو میبازه و منافع زیادی رو از دست میده
تا برنامه های مفید و جذاب دیگر خدانگهدار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/75266" target="_blank">📅 14:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfgpdGDizzezjy18xKq3bo4LV48LVbz6SFiu8IdC7p2-3i-vUX26qLrCf38mdO5NJcGTYmb3RssM9wj34BTgmmZO3lsXi78O8asjZW0x947UyYuK2yKv9loIFiOKzxpWHsdgu0mZQ2Qj4vvbMtniCRCkx_lkJA7omzoNmPF7Pz713oS3_GMFWIipL2LAxset443nsg1K5lP3r_RDPtamO7kSVf9np10FLWbSHdZcwbBLKl8znrZg2v5ZKlF3QV7B-xSNLJJ1ediqX-ALVCfIhAJrEyqDaynuP-UTfFlhmgi5FReJuXIsdhNgkt7_NXkUOsuYqtz9EDu9tX0Hk7q0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی فعال رسانه ای :
علت اصلی آموزش‌های نظامی این چند روزه در رسانه‌ها و تجمعاتِ میادین، توصیه‌ی یکی از «مقاماتِ مهم» برای آمادگی بابتت فازهایِ جدید جنگ بوده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/75265" target="_blank">📅 13:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وضعیت شغلاتون چطوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75260" target="_blank">📅 13:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان من شوخی میکنم با رضا پهلوی چون فامیلیم پ داره نزدیکم بهش
شماها بی جا میکنید</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75259" target="_blank">📅 12:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مهدی قائدی پیج رضا پهلوی رو فالو کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75258" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYC7GEwqlFQHPMBaLccHY-DNZkr1R1prAkn9O2k9Q-kRr_SjbR0F8DANF2RD9S_WQG69xD1AHnWklpB13E98U2RmW-UnTCSm-8qU-jrr2GIU7NHEFuyMT26JLxEzU7cXQAmX_gVE8tyD8ZxwSQLnP8OqlAN6m5V6m2Zg1V3kuz6glbminEFnEHP5W38cn7QsWB4WW-VOzfn8ziz3oqBaXCAiYX8FCJLcekj4DBVd3OPrSuD9XsSeePpoyLJoaH29PPlE_wIBzGev9bnTX9y4n6D11yd_LMLp_w1SqoX20qp4PWNMpLxrmeQAJ9J38mnBwLh17sTJpGoCc_gzZvZwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سردار  به خط خوردن از تیم ملی:
پاک کردن پروفایل با لباس تیم ملی ایران و آنفالوی پیج های تیم ملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75256" target="_blank">📅 12:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انتخاب مورینیو هوشمندانه ترین تصمیم پرز در ۵ سال اخیر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75255" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوری از فرید رومانو: مورینیو سرمربی رئال شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75254" target="_blank">📅 12:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کوروش با آهنگ علی سورنا پست حمایتی از جاوید شاه گذاشته.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75252" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✈️
وزیر امور خارجه کوبا
دولت آمریکا بدون هیچ بهانه مشروعی، روز به روز پرونده‌ای ساختگی برای توجیه جنگ اقتصادی بی‌رحمانه خود علیه مردم کوبا و در نهایت تجاوز نظامی می‌سازد.
برخی رسانه‌ها در دستان آن‌ها بازی می‌کنند، تهمت می‌پراکنند و اتهاماتی را که خود دولت آمریکا مطرح کرده، منتشر می‌کنند.
کوبا نه تهدید می‌کند و نه خواهان جنگ است.
کوبا از صلح دفاع می‌کند و آماده و مهیا برای مقابله با تجاوز خارجی در چارچوب حق دفاع مشروع است که توسط منشور سازمان ملل به رسمیت شناخته شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/75251" target="_blank">📅 06:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0m7_25x9o515TTlzYggsd-Tq2JTkf6CILl0R5K9x0PRO_HN-C1xGXqcDh18BWZXGEFU47Bc-Yy9LYXABS0kiHfAO0UFKP7FRti6EG14m94buMPwcfK_Fq3iRD71Fq249f4gTlVaRdXI113Wo9FXpU_bJ2mRmFmJ2EO1a5226WWDjT6IOOTAfrhIGYOy5X-BpJAlfxttkMtwlSUpVckaLtTPzL16D7jvWdHARXxE9iUuKazvMXGm_UKROV4SfGsWpAZXdj-SXYg-BkL5D2qvkWsy0uTSSCWjiBo43mlWK3bkm3rsrfYZtpzd_oG2TxKVrH9-182TMqc-HKSRcURWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
تا یادم نرفته اینو بگم؛ مارکت حدود یک ساعت پیش باز شد و تا الان بیش از 500 میلیون دلار پوزیشن لانگ لیکویید شد و قیمت کوین ها دارن به سمت پایین حرکت می‌کنن.
🤩
ترس توی بازارهای ریسکی داره بیشتر میشه و از اون طرف قیمت نفت هم روند صعودی گرفته.
🥵
مجموع این اتفاقات نشون میده بازار فعلاً داره احتمال تنش و خبرهای مرتبط با جنگ رو قیمت‌گذاری می‌کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/75250" target="_blank">📅 04:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEURrXNWtDsej2FZMfJH4LYm8TaAhZTPEpZs7_jZLWD5_KXv0I4asgAsZkmAmAEYn1PR5miudLysrlAyx56U5iotnAEbbU2qMPjw2nL5Kartpw-R5M1GTx_x7576TxTtOrZoL_EifCJCugmRm_NBmCLnTkpoFfUDzRer7JIXgEvdqj5bHnKYDmNT-1Piv3e51zFWJuTasZJeQJMRIso2kDqsHGKymdL-r2v6GiLkGD1EGeqA0ygPmMsuWxbC4IElVFKE8dULzwJDxHIJS_FjyIS_DZOvI2q78Ec_RDatGSGrclmC4utD0QkX9Dknt2ZJicumQO2TAidSKSyinW5jdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک راه اتصال رایگان که این روزا جوابگو بوده کلاینت (فاطمیون) هست و فقط برای اندروید هست
آموزش اتصال داخل اندروید
لیست ای پی های جدید</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/75218" target="_blank">📅 02:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl_mi1GSwqSwZba57SWKB0dt2Icyok4ufh9lOnsnCfwspZgbVCiE2-CGg7V7Yg5O7DHbo5ZFw_mReQa96qYIy1AyNB-YCFZ3imsENin_eToapxOoFJHJfEreW-hvzOlYzD7UySvJzb1mYNEsEU4b1xNpR6BimS5VhweFT6ua7zO04fLfyVfuJyn58JOW3PvXMoRhZsklAwsnxRLsJcc3lOIC9-RAMD47MLuQWtTNXKTbITftSB2lsasBKAzt4duMdABLaj2I1N1lrN_He2oXxRnQiik3yXYEetmKxVzCw5v4-RswZc5-xC_LneEQ4AH6d4Do-XI_ah_Ehua6-sM3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/75217" target="_blank">📅 02:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/75216" target="_blank">📅 01:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لبنان MTV
مسئول جهاد فلسطین، وائل عبدالحلیم به همراه دختر ۱۷ ساله‌اش در دوریس در دره بقاع، شرق لبنان توسط ارتش دفاعی اسرائیل ترور شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75215" target="_blank">📅 01:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS0ulf_2xtkUw439Xidq1QP30cbkLzfM7THhPQF7fUQ8cqaTNCoEswWi8m32dHce_79hTNFSklduVECayyncrur_CYoL2OENJo1GlmNVeul_yv3wmX0oQ2uyWMI3LXgDFUO9enVCSNqso8d3IsMV4Rp0AnYcR5nuC1F_HBcyfHOlQ0MgtnNYL5gS247fCB9EVYLD_FnM2NAi6Qjr0Il5CoFga9cgEB5pUrf6YHEix3PDHQpqKEUDYP8seehZZkuKtkixOO4joCp4qGYJGRor9VJmuk_ywChHYxA0D-nSxJeWO83B1NVOBUvjriXAVrIfnd6rDn5_aDpNu-hmCI00Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه ترامپ این عکس و توییت کرد  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/75213" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk-s9rRdd8yQyS2Wh18sNQKHl4M4w61wM0b6k0iNKbaIZVoaKBCeUGyx-lvc_lnH-rF6tE_XmkMEjPwxRub9wwfK0E0OjK7c7It1S3aubgU_BG4jJErhxSNmkTqsYRqNfGy1_9jpmAaADTBpuqAKH7HitBPxNISjQLUkJOUp8h62U29hkHikBcCZnOyPYhoxwLnR8ZnIBboI1IqcttauO8WSr7AWViToJiKkFIrm_tqO4HtOvBwlmBRQLODwp1HBI4qx0R8glrPmE6dha1HNYmuKewstn9jBczb4lYlXibo_M3gM8CEvjkPhuHZpX5671J9P0HSpAPb4so5xry3p-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو بکن تو 2026 پست های خیلی مفهومی املاکی و مشاهده میکنیم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75212" target="_blank">📅 00:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جدی پستایی که راجب ترامپ پوشش میدیم بدجور ریکشن خورش کم شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75211" target="_blank">📅 00:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال 13 اسرائیل
ترامپ در مصاحبه با کانال 13 اسرائیل گفت فکر میکنم ایرانی ها باید از آنچه الان درجریان است بترسند.
آنها باید مراقب باشند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75210" target="_blank">📅 00:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwmE__nTMycbp-dW9CY3si5W-sWS-H2130gmgsvFYFEgvVsRZHTS1WYssjTHXN5P8rZtrp86Wmg9PSF2HXV2XffM8Ym7Tv99cVacWRBm64L1dj2wXA11wrFedciVU4MggVK6CrP89fXB5bcFU873_ta3TZwi6r6u9XFQF5xFZIORMVBOZbyVdakGXLt2vY302A-fCHYDf-ig1SSCyJWpmty5JMKn2Wb_Jiig_xWtUjo5BZ5DQM4UYSBLSBFA2-8y9EJ6SY_iWT3KIgHVMpFplEUd016WnSR7U2McOUXiSe5xiXVuWE3VwyyJMNEMChzW9gUcT8NFTWsn770vfgku-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوبه خودتم می‌دونی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/75208" target="_blank">📅 00:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhoQp1EUzdWTw_COu9Ip9QG1MM3wz2lWWztuzTb_8h22JtMMISkLgfuowycmMivqZTSHge2N6cCUI4v-jawqqN_JxoIvdYV1WXvtk1F_9sreJXW2R6p75dWs9cV7MvNY7O897ZF9HUoR03sPBqPrVLO0tVzxj13yUgNV7v-jL-IY_kqybgLfsNDfgovPjfbnSwNC21dJPDhyN_6037Wg1BsnuIIvDxi4TARgReumhW49kt5ldamwEPssgJG1FufmDVqmMOnmdWkjOWtlliJfrHFVGN7x0ckKGmRiKjSrsISJ1ZrCTV7QXTYY6sDnng-ByElcttOOAcZ89m1PwiQLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiUDVG8BicPWKx1N9QWgKI1lwoWkp7iZgRBgTavQyisOjvoax54xybamtqqNyTNYP93uGkK89mxtHePTYaQOR9Ak8dX-oHL08Vq6T-vhTd-m9vXKsCSNJRKt6rbyWUazGb7ruOa5_xZ0sfplrK3an7p38iaosG3cO0CArMPg0zdpjq3PEwEOqOgBL-2W_FgQhP5llIMnaOaEeCm9UXXvss85DMX7Va1ehuET38UMJEm6SqA267gqDtGvvXiaNdGxtXKdq-l8Z3mGmFlotEZtZm2HsMslprjJTA810VkBvt_h1nZFHPfq9Bj0dTBGbnNS6uomYeqclZ3fUiOxBkxT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvdvvwXpwqmBfmRAjxCTJvJpKeFz25Y0ot4SaizMRELZYEvBKsBVzRF8E6rUjrze87L0bqfmRqZg3wGMHMFwayQlqSQpVqHEpNd6oUFVOvh4A-ylmRHBwwpwfc92FfP4bZDNQczleUpWIVo5sDNr4nivj7rZIrF-WOt2lYIzqaeGcpcSWbBxMARdrEIg6EP6zZimFV6OBDHJ87mHBDqQTqJB-oZJxnvXa-4IeN7TLARvpkTsItSfMPd_j95mWHH2xttIfPCRLkwbTJXHTodPyRVRftTQoFNRfdDl3tX671Q-6SJ2sshNCXemcWrQLtHiZzpB8NR-qoA3EjyHefwOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSLy0mnvnOtmovwMRK5HQ2xtnS8tPiYaCModnsCPEoUkyApcOBHW6hMlDZOcz3EUBIPve4gORCWgS3pVk3annFnYPEy--gYsXIG-p9AAsgJMhIBcLp1mM2m-TxhIKyLTAUOFgWYq9mjDJ8BhyWL0ahYIXTqHKtQOs-QcCTeFDYnqJqx9XuKZEEUV_fOHPuBu6i0alAEPCAClmq5vw8iXPVbnY2AQTxEqoeeCX8M0TUVsUS2NSHeGBJNkUozY3MT2diOT0pEpco8z-sW2rKmt7oj1mqt_OwsJVUqq6it3VIh_iiEN9CNWVebMcnW_OZ-XSpzEStVvh0D7cA6WDetFTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکرشو بکن تو 2026
پست های خیلی مفهومی املاکی و مشاهده میکنیم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75204" target="_blank">📅 00:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRmYAQqyvthOhrEUbtMcVuZLvoepUus1EhQfQGKjRwrrNMD9qDB447gi2J7-8yoDhXM4GeHH7k_bfyYuVJaX2YMop3KS865gUAJfbxCUi7LSVR7MuneuecdW_zZ5TNOIOB8_itx_jwatP8fO3bdTbjQZBCpj4ezt628-GhEkUU7N-CQ34-AXBsQTCv-nHSuLMQ_VEi83Kr7yiuPnOvQnRlBbalrHYOYiEcuCIbfEPImhNEG7aO6h-suUxjplENTRuYdKcYYjy45A31GWXDel_ZJkw6MGS01I36xi8US6og1ydlhplpG4AYu2Ahx0dl7bk3OnzYPy1ud1L0OiXXsDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75203" target="_blank">📅 00:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👻
ویتالیک بوترین
ببین آقا یا خانم باهوش هیتلر حتی کسایی که معلولیت ذهنی و جسمی داشتنو هم اعدام میکرد و میگفت برای جامعه مضر هستن.
🤬
خوب حالا یه چیز جالب میخوام بهت بگم
بعد ساتوشی (سازنده بیتکوین) یک شخص هست بنام
ویتالیک بوترین که سازنده اتریوم هست و ویتالیک داستان ما اوتیسم داره.
🤩
عملا فنای هیتلر مخالف زنده موندن چنین اشخاصی هستن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75202" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=OIue_Cr9icSLBDPWnHxBX1Yuh1V1mP4scD1t4JZ36-vZFsPvVOXMh37MwXvo2iaF3vTdhbLYbijWuO6Ax_WT2CjToaIsim3M3Y-gYlLgA6332YDZOy3wi8MsFiOu-pTlRA6D9nRXFgLE06EMjwv3Vf48kEnjjNM9iXmiQt5yV7p39nG96IqbtUknehuPprPks9lAdAxITT25wmGkdglh5hkEAGr8B-7gPxeJW2Gwjs0Zhnz6hB8bUI-9AMj9V4F7w-a55L3t9MJzimaM2bhRD_J4N4lNIpjyqSXZl_7EzcjshHf-wEe28LYQUhHYd0g_LznKl7Rzbiwl_ALbGpbCwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=OIue_Cr9icSLBDPWnHxBX1Yuh1V1mP4scD1t4JZ36-vZFsPvVOXMh37MwXvo2iaF3vTdhbLYbijWuO6Ax_WT2CjToaIsim3M3Y-gYlLgA6332YDZOy3wi8MsFiOu-pTlRA6D9nRXFgLE06EMjwv3Vf48kEnjjNM9iXmiQt5yV7p39nG96IqbtUknehuPprPks9lAdAxITT25wmGkdglh5hkEAGr8B-7gPxeJW2Gwjs0Zhnz6hB8bUI-9AMj9V4F7w-a55L3t9MJzimaM2bhRD_J4N4lNIpjyqSXZl_7EzcjshHf-wEe28LYQUhHYd0g_LznKl7Rzbiwl_ALbGpbCwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/75201" target="_blank">📅 00:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فعالیت پدافند در اهواز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75199" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">محسن رضایی:
ابوظبی به عربستان تعلق دارد؛ امارات ابوظبی را به عربستان تحویل دهد!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/75193" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کی بود میگفت اروپا اینترنت وصله؟ اونم بزودی قطع میکنیم
خبر مهم شبکه CNN درمورد ایران
:
تهران قصد دارد شرکت‌های بزرگ فناوری مانند «گوگل»، «مایکروسافت»، «متا» و «آمازون» را مجبور کند از قوانینش پیروی کنند و از شرکت‌های کابل‌های زیردریایی حق‌الامتیاز دریافت کند.
همچنین، اپراتورهای بین‌المللی به دلیل نگرانی‌های امنیتی تلاش کرده‌اند کابل‌های اینترنتی را در بخش عمانی تنگه هرمز متمرکز کنند، اما مؤسسه تحقیقاتی «تیلی‌جئوگرافی» تأکید می‌کند که دو کابل اصلی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/75191" target="_blank">📅 22:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🤡
د فیلد مارشال ماحسن رضایی
آمریکا یا شرایط مارا میپذیرد یا با موشک مورد استقبال قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75189" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ گفت من یه پیشنهاد دیگه دوست دارم از ایران دریافت کنم که حمله رو انجام ندم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75185" target="_blank">📅 21:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75184">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید  هرکی درست بگه یه جایزه پیش من داره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/75184" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75183">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید
هرکی درست بگه یه جایزه پیش من داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/75183" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک فروند هواپیمای ترابری VIP C-37A نیروی هوایی ایالات متحده که حامل مقامات ارشد نظامی/دولتی ناشناس بود، حدود ۴۵ دقیقه پیش در پایگاه نیروی هوایی مک‌دیل، مقر فرماندهی مرکزی آمریکا فرود آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/75182" target="_blank">📅 21:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aApkdjPVr3wC7COZPcTgQ8RMkWQCByuABqIbHyOIc5ILiaTEBvEqJDo9edIMYEiM_FdmHmALpjt0ny8MhL19M5biVPdyP8VXNQt2tXz5zISzVJILSSMhXtQYD4z-n6PUuLjM-ITPmYAzlFk5qPmW6xqqfuMI9H4b-g0q2eP6xyBQyWmdEN5b1eADR0dTbRZom4N5xKxT01ygSm1PC5Ryt3LFkaHdnxV8ivM1Oz0FrDswM85Ovj3izPSJMhvgE-Fk-LBCBl1NpAsbD_016c6u8HnIdfblzCrJUqEG3F5GWXDMfyrkNM5ODXrm-P5zXYCfbq_HzbwUzSZbPjY7djtyzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=aApkdjPVr3wC7COZPcTgQ8RMkWQCByuABqIbHyOIc5ILiaTEBvEqJDo9edIMYEiM_FdmHmALpjt0ny8MhL19M5biVPdyP8VXNQt2tXz5zISzVJILSSMhXtQYD4z-n6PUuLjM-ITPmYAzlFk5qPmW6xqqfuMI9H4b-g0q2eP6xyBQyWmdEN5b1eADR0dTbRZom4N5xKxT01ygSm1PC5Ryt3LFkaHdnxV8ivM1Oz0FrDswM85Ovj3izPSJMhvgE-Fk-LBCBl1NpAsbD_016c6u8HnIdfblzCrJUqEG3F5GWXDMfyrkNM5ODXrm-P5zXYCfbq_HzbwUzSZbPjY7djtyzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/75181" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آکسیوس به نقل از منابع خبری در دولت آمریکا:
نشست روز گذشته تیم امنیت ملی آمریکا با حضور ونس، ویتکاف، روبیو و رئیس سازمان سیا برگزار شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/funhiphop/75180" target="_blank">📅 21:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnZRBhhQWQxeziI-OI1sHY3K0hZpkoLiuvpq4SaTTkj2tw-VMXrroqTM6V0dthnNCmnzixNNvltEub0xVCLMsMsYGtHU9AJR0FHAMigVyNyN_Ne9Pvo-u4xWNj0vzdUL4EOYdSUWIH6MNOfy5VOp_8l1dNcQMIkM3orVv2_ZutQl-17dAd-kVM7X2oy0Mthyb3tCZFlT22Kx686tPz4hWuicm9lEPfVA4Ay11q_BUduDyGqYABdNvZxPWXBw2cmQ_p--brN4ecz2mqbTXOpua66fWl5qnpYw1R_GH5SBLYGjNlNeSrVPzV1Ps_guXF84p0DDt1HV2m0--_y4cpfv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47 دیشب : آموزش کار با pkm امشب به حول و قوه الهی: آموزش لانچ موشک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/75178" target="_blank">📅 21:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx4hMZRb8134X_vdLsEl4b3u4P4j4KNX4QwRJNm4LIgHIw3xuLCzF2vYkImGj_BANtAmPDk4Gh6Qr3D085MQpE2QYz9UVEysuAOUzdaLv_A41O8ca_BIrmEFwK4QTZ2G23H4iYwC8upxKsNoqEhdzFPTEokQfVooA5p6G2LId2ajGsS1PpZ9LNHbqviXb1GamHjzRI23jCNtfj1Sv7u2KKzUICtPR9wiSH_MyKauHMuYJMEiEZJokETir6nuaEdBYFoLTOCXJfEFOK8mJn0AL9jgq6qhXQM6l2gj0m108OJP1Gdga3K2loAwsgpSyyNas1BRxNj2VTxNJj9oLGxUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/funhiphop/75176" target="_blank">📅 21:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی: انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/75175" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی:
انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/75174" target="_blank">📅 20:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک سری رسانه عبری:
ایالات متحده و اسرائیل سطح هشدار را برای احتمال از سرگیری درگیری‌ها در ایران به شدت افزایش داده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75173" target="_blank">📅 20:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران باید از من بترسد و مراقب باشد.
ما منتظر پیشنهاد ایران هستیم، اگر ایران پیشنهاد خوبی ارائه ندهد، ما به آنها به‌گونه‌ای حمله خواهیم کرد که تا کنون هرگز نکرده‌ایم.
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/75172" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx-YsoaJqD6C-85S6dScnkuEwKjG1mGwhTJ6ub1TpOAD3XuTffEvd15siL8-XBdTx1QSwnEvrsl4ZXdWapOWoTqRGRxJvsZBi1BMVSmbGUr8G5TCXEpiroXMh0fhLRHvuSr7J_vWOV8cIeJAHcvpMpgP_u0c-c02LCrm0in0aSMMp9XXzimNatiTssUax54_B8xyTB4KqPUI57FhsMJZ2Q5CG-X386OMUVO6IK0IBBOXxnTBmSeqwiEWZsv4S1QtHogC2OkZxSqGPYDv0Qocp6jTjjsR06GRt2DhmhIJGievNDRcPBPnGKZhcCOB5v9QVLlDQjSqV22jeGUk6xGEnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ساعت برای ایران در حال تیک‌تاک است، و بهتر است خیلی سریع شروع به حرکت کنند، وگرنه هیچ چیزی از آن‌ها باقی نخواهد ماند. زمان یک عامل حیاتی است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/75171" target="_blank">📅 20:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE5SMovGqd0x9DltPDMSXqkppgdB5AfRukwYJPE-UByX4OmD9loIObpEkVt1DsEv3p81TNHWe9QJHvR1Pm0iPC2P0HM0Etkf2pxlDiq7elGu4jsdS_6lLHSfdDIRpZBEy2y1NPlOoHSbTEK8epS5A-6v1blnCzr4Cx4NSMyY3TKNvam7rSBurSVBRFIf4owSL6wevLAeXgKUcOeHdksh0i1Oi0ZSMj1RUPvI8qY-F3tu6DplAfkng7tY580FJ7zU87JJLIX-66POcHbzEvk0vaQFBU5tBn6yXAhXv0ywsRpeBgFy0hJaNZQZ5OPbCt4IYNu297syuTI_g6UDZppLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکه خدا لعنتت کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/75170" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اکسیوس:
ترامپ و نتانیاهو راجب ایران گفتگو کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/75168" target="_blank">📅 19:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75167">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر کشور پاکستان:
پاکستانی‌ها شبانه‌روز برای موفقیت دولت و ملت ایران دعا می‌کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/75167" target="_blank">📅 19:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ulcA5ru00gr3Tqtjpx7OivuyWDAQlgw3_80aVZPeHexoLaT9zcftNBcJ-l9T530ioMUCGzFqxEwFo79l75GudupoAdosWcmGd-QSrpMGY1dz91wOJ_btkAHgCv5CMZYW2XYN6zmmcDks373kTMXa4mP9_YRFt3wDyx8nq1N8Ob4Ou8CGqsOF73dAQMRahy9qQd1T8W1hF0RVyjqZyTy-h2Kp6yfHxKfkvAQhgoU0zwP6-szO4_wTN8YKaUauQomluPxGdnDW3F8PAaCfHx-4dSCgKiGpxCn4FX_--F7Kvo26TH-3qsg1BWPgHn_lV2b5f7lZgvXbUaGkBt_1CEEBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYJHq1c3hODGkDtk8JLGA7vnqgb1FzfxbcKmAiNrCBH-Yw5zoUUh4VNfdM-3TNTDHOvPx91hDPXM2kvRF4X-poXTQgZOKa90OfCnCr0k0VkoqXskSVIxvBALrQMAAF-_pn74RoSA2TcDgmlEaYrjLFdpI9l04vJJulCXujsTRf5joc4NC-sMGh7i76XyvRpOfYHkuONK87KcCCte6C21EouyiVqpdO1SnhljYYIOKVUtB5Ot5gEtePzLOHFN9toT7_bfiiTA63lOwedWi6z3tJxUEe29SSs2rZ-gYWl29zFAysM5jyLMslly-TuYcC-7DRvMjmkQ4o1zXzyAVoVxmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آنالیز تصاویر ماهواره ای نشان می دهد ناو هواپیمابر آبراهام لینکلن در فاصله ۲۴۵ کیلومتری از ساحل ایران مستقر شده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/75165" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=V3ozmswwK0AxGG6329N6NGMEVE7KDfks5ovKM-ALqS-yBOXvUv7lE3ZeWBx0aH3ppLUdvwoDINPp9QdYclC_yQKYhAQztzs4DnYbZSa2nfj5vtrfNWvkz7iHb-7saAJZi8CJbFJAyyYi7ltSaQZhwplJMNokp5A58mJBWc03sy31DdTmtXPAzkYj4AxxqAFWszO8U83T32u1grbCMnw5_0U4om7s1P7AzKGb_fQj5vOCLvfiAqw-SeFaUYzV3PkklcO6FdFCJ0DU63BupsVKyTe71IOzUxmgrL7vQAt4inlskldEnTC5wXp7NDIeJiYw9_6tcNsV920JA8iC2BU5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=V3ozmswwK0AxGG6329N6NGMEVE7KDfks5ovKM-ALqS-yBOXvUv7lE3ZeWBx0aH3ppLUdvwoDINPp9QdYclC_yQKYhAQztzs4DnYbZSa2nfj5vtrfNWvkz7iHb-7saAJZi8CJbFJAyyYi7ltSaQZhwplJMNokp5A58mJBWc03sy31DdTmtXPAzkYj4AxxqAFWszO8U83T32u1grbCMnw5_0U4om7s1P7AzKGb_fQj5vOCLvfiAqw-SeFaUYzV3PkklcO6FdFCJ0DU63BupsVKyTe71IOzUxmgrL7vQAt4inlskldEnTC5wXp7NDIeJiYw9_6tcNsV920JA8iC2BU5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75164" target="_blank">📅 17:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75163">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJIooaQX1Lh9uc9RHiyucjm7_aEuQyorkWHwBGWQWk-2_BL-EHqWPx-E6A02q5vvfhF-HK6MOulv87gXSGaDbZyvDqrrH1OBQXRY_mDo1uOFCY34cwMU4JxqgIpc2LdIURLwE1j22CaBhLSMBETeZR8iyh-SV6fq1MZ_oYjkuELL5w4xP_bc5LXgr4OLwub_XC-mY8vfQbjpEQgavrbK-LNiLeGnR45eR2qb_mYnHym2TlfouXOQhmI1YQ0sH_NuvN3QrRBCwraMCv0l2-2N7W74N6vlDcdMGR14GOCC4KK1Z4Z4-2d5zQO72vW1UFbxBifYG1O7rgGUg0b3vTUxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75163" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75162">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این بدبختای فلک زده رو کی میزنه؟
وزارت دفاع امارات:
ما مورد حملات با ۳ پهپاد که از سمت مرز غربی وارد شدند، قرار گرفتیم.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75162" target="_blank">📅 17:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پشمام معین قراره برای آلبوم جدید دریک آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75161" target="_blank">📅 16:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری فارس: وقوع چند انفجار در امارات برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/75160" target="_blank">📅 13:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری فارس:
وقوع چند انفجار در امارات
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/75159" target="_blank">📅 13:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فارس: آمریکا هم در پیشنهادات خود علاوه بر رد شروط ایرانی، پنج شرط اصلی هم برای مذاکرات گذاشته بود: عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران عدم پرداخت…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/75158" target="_blank">📅 13:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/funhiphop/75157" target="_blank">📅 13:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عباس عراقچی در کانال تلگرامی خودش اعلام کرد که کتاب ‘قدرت مذاکره’ به چاپ پنجم رسیده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/funhiphop/75156" target="_blank">📅 12:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ژابی بنده خدا رفت چلسی
از اونور رئال و بارسا میخوان چلسیو لخت کنن</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/75155" target="_blank">📅 12:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75154">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMi04jEi0j_E5EBJ20zHttnDtMSGOTFUJjgqqK5tN36DmCsr0n7LncYHmD1k3P2J_xNwhnAapqDqRkxOLvU3ikeJJa3mrZsnwAVZEPdc2MJhfZ2UA0sluhvIkhcLkNOVjVMZWY8Q2ym_ul0kzttJMk0zxCLIKGd8QQvR3a8hJEUJbxiR-kPG7cheMhcD5WJyWIKTawcOYLrAuUuL8SagBlULkOwFZwbjkVxDUDz724x9t4bMsVUI3vZgNjEOEXaZe6tQTBsqed8W8qkfR_LMukVk0AXJUOLZdTpUXmWqH7bBZ1pORDiZyMY862_Y1zCpvp76YQKbavM6y52Z8Amkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😵
نت بلاکس
آمارها نشون میدن که قطعی اینترنت ایران حالا وارد
روز هفتاد و نهم شده و دوازده هفته‌ست که ادامه داره.
☠️
🤬
این محدودیت گسترده اینترنت باعث شده مردم کمتر بتونن آزادانه حرف بزنن،
اخبار دنبال کنن یا توی اتفاقات جامعه نقش داشته باشن. انگار مردم فقط دارن اتفاقات کشورشون رو تماشا می‌کنن، بدون اینکه واقعاً بتونن تأثیری روی اون داشته باشن.
☹️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/75154" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">😂
معاون سازمان بورس
بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها در روز سه شنبه بازگشایی خواهد شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75153" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWUS4iJPUs1NcTx8CZcx1N4xGaWL8gm8yX4YdkfprXxB6GC8iSsmmamQWe9MCD5SHhZwybflPcfc6pJqhJqlmAAnp4oQ3eUZItsGVeWQxfjJvWAJG0O5eW6utXYkhc2E45h15FDQ2kZKZfIOAlwz12Ael9mm8wFFifIf3OFXDQA_X8fBzQzxfUYTsMnTu0H6Bn5C8Ju7gfK6prPVLU5-d6VqZa7zv1HyfA0w0q2U_CS2CWcV3tWLmqZ5OFmO9RG80LAnJKmZtZKU9GlaycBIoAQ45B7NUP0T8b8UP7xZ2D4ZFC6XFiG6tVDdi59VXgkVALU5BGAJBQIurf-ODJJeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ روسیه در آژانس بین‌المللی انرژی اتمی:
کارشناسان غربی معتقدند که ایالات متحده و اسرائیل ممکن است در روزهای آینده، اگر نه در ساعات آینده، حملات نظامی علیه ایران را از سر بگیرند.
اگر این درست باشد، به این معناست که آمریکا و اسرائیل از اشتباهات راهبردی گذشته خود درس نگرفته‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75152" target="_blank">📅 10:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH1m40Mir9XeBUbmfTgszTojZ2TJ9GoMUpqe21LvIb9lhAD5cjksuUmGYHpQTMXj7mW2yGg-lJKQGVjeu8DEtjttEETL4YSGLX__AP7YmrQGtTLnGNB-8AJgBW9At7HXrgRMrARZISMsomcGNh9jelHDSwv0Jy8mj0Lwy6KhWTKBflPJ9glsmrgCNFbGS6VuGMLoiWd-LwXPtPeXUMWIyzyypQVYwqcK1YJbK0hq83XTu07D_Rn_2YOABLOEqkrK1GwTimi2vDbCdqtEvpw4oViCqmf0ABh0cA6q8F11vgjnwLLFZBL9UZg191DJkummFE6hjp82PkdRGMZpH-nm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید کاخ سفید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75151" target="_blank">📅 09:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCumKSYCcUWq6Kp4kCgqBMto1nlRpD_hd4pXifixo3S1_4o0-HfnhiUS9MM4xo9E_uv4G_JqnFstd9pnaPFLvuwhimIBrhRRAZNVYqEGNvKUj3fv-Wa8FanKUMu86NlOvOm_MBzkb3qk-yySsEajWFUPy5lfgEWcyUFW1UNFlv8cfnoWMRt8WAKRRymYlEaluT-AM3XV5bwpopAIrHjNrMWsTl1KBqMvU-TCB8zO1OevDXlcgtKradqiNLVdpH3WIhohDe6ht2RDrFvfptNXslH9ZOgb8WpL_bxC5d3ZpUg-M0rd6dh8lOQty-O-WMkcl1EgupP0UCIjg_nsMGWzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47
دیشب : آموزش کار با pkm
امشب به حول و قوه الهی: آموزش لانچ موشک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75150" target="_blank">📅 09:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری‌های عبری:  یک انفجار در کارخانه شرکت تامر روی داده است. این شرکت در حال توسعه و تولید موتورهای موشکی سبک و سنگین، از جمله موتورهای پیشران موشک‌های آرو ۲ و آرو ۳، موتور موشک سیلور انکور که هدف‌گذاری شده است، موتورهای ماهواره‌های صنعتی هورایزن و موتورهای…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75149" target="_blank">📅 06:04 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
