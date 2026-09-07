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
<img src="https://cdn4.telesco.pe/file/L0Q1rnirt1lR6QEbjfZjDCq9aA1iQFD32S75Hd2uGRId5ri0zxgRpfd4QuOoePyZ1amM6EEuz8mkmNt0Ket1bd4p_yapk-oU0kqjirMF-ak4U0soLBPM3STg7ip0PyM7SI8rmoiZMGRf0dcSPxEweIMlrSZed4A6ht3YokSKFoerWD79Ix_UWngkVVJAZhtYrYNgqVGbqjEU3ZssIfGO1UOhI7-64eqqMDZOrtfNdthEa8RoErk5IxxjyPzu6QjcOXX5zbJqYXx8LI2XqoGek0lDZNMc9zAA34HYJvbs61xafctF5DcA_DpG0Vz9kKOhpxOW85d1Yh2I9ELeCwgEMQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 449K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 04:01:21</div>
<hr>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwyEGws-I_YBvl8nGt4pqydLwq3uO1iCeiKPQOckavTeNGqtwiQ9_9LkWl4ZP034IXQxMUUAtl9_O-lHofx25MjzN2Vta2l42A75qx_-BpKC3Bov8gSYYL3O7embtukV7H2VOgzWNKZOpf68mbKF7UYFZhv39aUrZSy6Jb9rdJ_m0OG1ZkK4o0-PZD4IL-3faTqwNWIwrUD771BAmXspdskniCVR5Mfuj-fyMrjbiZDgeitd3UT88l1uQTNBd-L3FWNzlKrMi2wwbqMaTAmbIiq_qhD1tbZHklgS90unuBwGbHEIEcwClSXomzFih4ecoS2f9qayCGyxj2vJrkxB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Par4ylA6ye7ufnIAVYRJia7fWj8qghg8AkBMVWE5P278WikpOYpxPW-BR7hjfNfqol2ByhxsA4T-JPF_Ho1I4KVDq7TZqxp6nI9ORy27kyaut89wEKhOVAXKcn4ISro3mrAWvqJ5EjFS7_Nn5i2plpe7j69CyTzY5XMWFWbvSQdrI9ABdxtETwJWnBqKl8pRyo1JkIWE7TMQSMOqHkdsT_Bx3H-Wi_5uUqhjC4qtzw17zxyCIHokGRslQE6Ar3eQRYLAGyhCRYz4Qa4cWYhcVCqRhTztBXq1R0pZn8wRKxwYaPUaDKJEI3xrKQwI643WQl6uDRT43wqLyqod1hyIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmqwiC85n7mC6abyubUSUl5gDtZQho7KInC1k4GQTpMuyvLXlaAtHQyi5TGzHkVmnOzE_k8VNgdMPy1p-VB4gmcAemCkx9jGwTZCJiIGGUXBdwO6tpPXSn_OzivcNWy3pi_nfQX18baaxPp_CCG8PoXqyRueKodPeHmfw-2U_KSURrYo9qeXEbAm22G1_5PCxFt3Nj0VcoOci4QrHeYIuqBI-94tIOLUaiw4EyU5LFDxM0FpMNN4DdgUDNZ4WELxzUQO9VhGSh0wmk7I9wvolIoRch0hAiP_hifZH-O6m0xaey1UlD9DWuNT0mJVg9DMeXZSWwe_ThNOjtH8KD80Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNef0cW43_j6Ipy97MHRLls_CGAPgn8Ch-dbFgjN811Lfztp1JV5xb-LEVauWfZM3FqyHO8g7xqbf6xvli6oshoOfy7YJRmybhLWiAFfPEnkMPhE76cv9651vWKNoU9oBoSc9p7WAez8svdzcnJg13_7PfnLuWlycCOGJJOKz_9NuTfRhPdtdlw4KKOV4HtSJ39Wr3ci-Db8kcIxXNBF41Be98Dfr_EDL_WgnmgfgHXgSSWj5S1zQN56TjgltIOhLWvLD984XOjs8kFpRmoyoL8zQ1WHzIvfBshqXDQzMvylrxw7bHPrgTBOQXD93QUkx_JeYm8AL04gEiqkmyawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFkRWg0XGdLYLhrWMKjP-L-azzUI_TVeIwVyGzzDuwVzZpyM8T_FSy0mCepOK1On5sGPB9X8tHrfu5H1UFhGd2xS3w3Djrttq12VO1AlmBnbBdoTOmmc6UqlsBB3K5j5-FxicPgb-62nQr3JgB8Uz38zYQKt9oAGOdqdwAL5RegX7k4ofLg5YaDsdoYvchA031OIW9HdUzHRH1gUJcQHjh6YN0bW0lHdcEgCyFvYqI3cFmJgimBdYAOs_yJ091ZLrAqySNoSWkHqdnCfw9yVjR012QAfKhPg_x-Wx6CtV8gRxMPBxJBfGZc_elxQlxRh6NI5axYQvS87jQtRqTo4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9usKgzmjgW0nTqdl_7vr4abKbnqGQTn2MLPXvaO4LNOz_-BEuH6oBdbtIN4jr7RUW-rtQl0DMJo5zGnz8lIOb3DptdxD5MU77gR8tXYmOE-Ctycod8g56mfIjlBeXVh-KkMzyHKgHpDHGDXFPuuEr1DcXReRp38zAigSLfn9NvdMs9ZVuNB-EXN4CfmQ6EeIxtovHmHwQE4cjhBxK1TYfVQtzsTH23uK8HAv5NSbKWHESkj2jdga0ZyLdbFAp46YrASAky4vBoRopghumwfruPQIX0_IPzEkIKY1YwDUhyfC-mjNfzJq-clrAD7UpFpEcMiRTPleTpESEgtsvLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : کابوس برایشان بساز
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22464" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHffedJDodpmEGGaTk2XImh6B24rpnDvVwLonAzeUde0aq9uzIBc2SgqrMdP1LZwKqUC7IM5F8MKhxQfxRLrWevHjZ9jwxLiO--00XKouyKotZtXflxV52nxHfkJtw8mmlUV2Qmf3iWRarTVIVvqCm0VC8oeO8hzpzTsrFpt5y450jCK1CyXChdgEmqgOji62V-QNCOASXlvK4RpCzB9QtL61jAEscZTQVb4J-r8x1gnSn70tNs4cxQnR1yVECTTEBdtuwohveFFMDe0zV62M52NFQysCjDDOOU5AtVSdfUS2oWZpWAa8BOyxKtX2__KM0fln9zSU7au5JJ5vnOhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : صادرات نفت ایران در حال سقوط است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22463" target="_blank">📅 22:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLa3yDy0jc8Fy7HX3YMt3Z7sIxsW1wJWHeUclGxOPC728nXM55hDFyIP3g879PDU9B0gjxT85LQtHay3dUcNnD1Hro84apl6VVj9H_TrjZ_Eu11t4lRMgruNrWlC8LKzvG6InqAcqGGIyWoZNGekSRBimDFobnPhqMtd8I3ChSgiFJ2jqNt4XRJZNvrIP06Pv4tA_ImfaA6GQegXDU8PuR9Zao6ktblBEOeguRbQH05XE633r_In6OKJONHRjpWTUeKB0rePNrEZ0myt2m0IItUGVZ0RxW2oNiZxNJosHWKJrXJF7W1G3truy9UMiqJy1GiNozut-Zc65ZSTroq2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
ایران دچار ابرتورم است
پول ایران نابود شد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22462" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQdomFCwF6wYmos_sf0Sr8BGm5IhU9g-Va8i5Vbcz_Hk4nag1WYHAGwrKNsu2ZUAChuFTBIWbE7gSUPboZ1aZ5649IlRMuR7aYmq-GK322v9e6PyrBVx5egqLARPUhqVgrSvR9CR4AjrtbTVNfCkekOhQg72juDjnZOwI1Ho447YhphkRzwE8bAtV8fCs8hDUh4WotWTm5d7IaHSXdgwA0rbjOI3VRLB4M3TzK3hjZcfcGoDn8-G6KzT4rDEGZwgOphUQf2IbLZcyyp3zrS0ju02Z86PJg5vvCcurc-VpRrDI1errNdNyZGJUwsluNYzYrocdw8YGc9B-2q99BMhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22461" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ارتش اسرائیل پس از شلیک دو پهپاد انفجاری حزب‌الله به سمت نیروهایش در ارتفاعات علی‌الطاهر، موج تازه‌ای از حملات را در جنوب لبنان آغاز کرد. اسرائیل اعلام کرده
انبارهای تسلیحاتی، مراکز فرماندهی و زیرساخت‌های زیرزمینی حزب‌الله
را هدف قرار داده و برای انهدام دو مسیر زیرزمینی در زیر ارتفاعات علی‌الطاهر نیز آماده می‌شود. همزمان گزارش‌ها از
انفجارهای شدید و درگیری‌های سنگین در منطقه نباطیه و اطراف علی‌الطاهر
حکایت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22460" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUZ3mQQ4cyOIbx5xYAcEZNQhpkliqPWpYD4M0et_tzFvjEmXjlY3L3OkBIG6Gw6GhDx9IQ2rU8jlAHtLwVGxtIOOg86J_WmfsI1HDr7LdIkdyiBZIRoQohbwCt834Po75k6UDr5ZcfCqsR4u9x7i5l9oMI4LAKaSX13yIuXIuOXycizyalaVWuQbycg6ExPK6sjsF3yJvx4I8NcqiL5V7h3ux34UvoEFLAlWhbHi5_hV-Mt3XDLwxIqQLJ-RHmmr-NNMQ3OmfTrKqXFqm3v9f5yruBw0kp6P6nzZwQPzotA0_4B4lqFefLDWMmyL7fo7ghGKkSbzniDeaJWFHvuIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: نقشه ایران رو برعکس کنید میشه تصویر من
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22459" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22458" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رژیم:نرخ سوم بنزین تغییر کرد/ سهمیه اول و دوم بدون تغییر
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند. افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22457" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کان نیوز:
ارتش اسرائیل قصد دارد
شبکه تونل‌ها و زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی الطاهر در جنوب لبنان را به‌طور کامل منفجر کند
و بر اساس گزارش‌های اسرائیلی،
در انتظار تأیید مقامات سیاسی برای اجرای این عملیات است.
گزارش‌های پیشین نیز از آماده‌سازی مواد منفجره در این منطقه خبر داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22456" target="_blank">📅 21:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22455" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22454" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22453" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو: ما مصمم هستیم که مأموریت سرنگونی رژیم ایران را به پایان برسانیم.
پایان جمهوری اسلامی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22452" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TzVaruC1fB4WU3l_pVbgPP65YxwCehptmgmExlUfttRoX5NDCCfAgZXTqVozmVLcKpGPK0ry4QwXXVOIsWfHq6gxbt4APRQZkXodJ1Z-Zd9z1aBq9K-FlcGbuMhG0ccc5xlW46qF9pQzfrr8GBEVmO19VksCN927rMOc1FkNN3d74nAw4fsFDCxNBB5FQjKKtc5MnqerKlLfwY3s1Cs7TGa9GMe85ISKRHimYAtGvFxbqF1LMA1BaYqBf4hUK-BLsC4kA2AcSUfZxxc9yxc92vXENevgE28V-4fVX2zu6Z-i9pYDZ6BzF-qIIY2YhwZdwkcvwiTtGfcA2IySLccpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=TzVaruC1fB4WU3l_pVbgPP65YxwCehptmgmExlUfttRoX5NDCCfAgZXTqVozmVLcKpGPK0ry4QwXXVOIsWfHq6gxbt4APRQZkXodJ1Z-Zd9z1aBq9K-FlcGbuMhG0ccc5xlW46qF9pQzfrr8GBEVmO19VksCN927rMOc1FkNN3d74nAw4fsFDCxNBB5FQjKKtc5MnqerKlLfwY3s1Cs7TGa9GMe85ISKRHimYAtGvFxbqF1LMA1BaYqBf4hUK-BLsC4kA2AcSUfZxxc9yxc92vXENevgE28V-4fVX2zu6Z-i9pYDZ6BzF-qIIY2YhwZdwkcvwiTtGfcA2IySLccpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جرد کوشنر: در دنیا چیزی به نام دشمنی ابدی یا دوستی ابدی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22451" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، در مصاحبه با
مارتا رادزاتز، خبرنگار ارشد ABC News
در برنامه
This Week
درباره ادامه جنگ و سیاست آمریکا در قبال برنامه هسته‌ای ایران گفت:
ممکن است دولت ترامپ به توافق هسته‌ای با ایران دست پیدا نکند و در عوض، توانایی تهران برای دستیابی به سلاح هسته‌ای را از بین ببرد.
رایت تأکید کرد هدف اصلی آمریکا جلوگیری از هسته‌ای شدن ایران و کاهش توانایی این کشور برای تهدید منطقه است و گفت
اگر توافقی حاصل نشود، گزینه نظامی برای نابود کردن این توانایی همچنان روی میز خواهد بود.
او همچنین گفت آمریکا در حال وارد کردن
«درد کوتاه‌مدت»
به اقتصاد و بازار انرژی است تا به گفته او به وضعیت بلندمدت بهتری برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22450" target="_blank">📅 20:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22449" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f35315292.mp4?token=HEq55Rxqvjb-OqmN0D5SWE2c4ClD2iccWGPKUE3mYiT8Ud6bmbxVDSuM9doOvNOBHjEAXM2lzCRsKZ5ApyRcT4th7aH8NW9-hVPhnmkjfRZ0olti-fG1VKBunYZuCxDrP9R6m77SwNzyg8e2H0uvUUXtV-hrX0Ly3p8aD_1gb-fz9_3grkiwWfdt4GH0sq9OYR1wpW8c-d9XMpT4HRCwgPDDBT4c8b5klRM2KO2Rk2xFHWBwwtrIjHu5Qy_g8ml_JtqR3Fd0P2OxD99pkF9FSB1pT_au0IzRJSQiVWufisbaLr3DTcN2h3Pfj-QF1OsQaSdpTL2jzCF2jzb6IHNq7EJHI6izfD3AmH0I35zEmzmNAGeqLpXEF6M-OGEdV6np0dmC1qMEVxR_y4h-Cc4ukvqfF5s4cMuD2qnlz9tjBEO412vNJ_ZbJ6floKm59P4REx3-9Iz63OuhQGpR_y7oz0pTOrnivWyAm20b8KzXt4f0Y2rrBAMS_L_s5ulJML7bexC893iSdW82D3BiQ9w4XL6pNWx1V-Q1rQ6Yol4TYHlofWa4y_9oarGBAcIFZuv7Gq1TBZRZmVjW2-zLyHg90AIGDt0lf9xuejDg_BV3uwBU7rnuDvEeYvjzjPBtIl2KzPZoNSnEV7iF00olSQzhBP4w2M8NlzL5vN7QZOHZQfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f35315292.mp4?token=HEq55Rxqvjb-OqmN0D5SWE2c4ClD2iccWGPKUE3mYiT8Ud6bmbxVDSuM9doOvNOBHjEAXM2lzCRsKZ5ApyRcT4th7aH8NW9-hVPhnmkjfRZ0olti-fG1VKBunYZuCxDrP9R6m77SwNzyg8e2H0uvUUXtV-hrX0Ly3p8aD_1gb-fz9_3grkiwWfdt4GH0sq9OYR1wpW8c-d9XMpT4HRCwgPDDBT4c8b5klRM2KO2Rk2xFHWBwwtrIjHu5Qy_g8ml_JtqR3Fd0P2OxD99pkF9FSB1pT_au0IzRJSQiVWufisbaLr3DTcN2h3Pfj-QF1OsQaSdpTL2jzCF2jzb6IHNq7EJHI6izfD3AmH0I35zEmzmNAGeqLpXEF6M-OGEdV6np0dmC1qMEVxR_y4h-Cc4ukvqfF5s4cMuD2qnlz9tjBEO412vNJ_ZbJ6floKm59P4REx3-9Iz63OuhQGpR_y7oz0pTOrnivWyAm20b8KzXt4f0Y2rrBAMS_L_s5ulJML7bexC893iSdW82D3BiQ9w4XL6pNWx1V-Q1rQ6Yol4TYHlofWa4y_9oarGBAcIFZuv7Gq1TBZRZmVjW2-zLyHg90AIGDt0lf9xuejDg_BV3uwBU7rnuDvEeYvjzjPBtIl2KzPZoNSnEV7iF00olSQzhBP4w2M8NlzL5vN7QZOHZQfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی، رئیس جمهور اوکراین: در طول یک سال گذشته، فکر می‌کنم ما قوی‌تر شده‌ایم. افراد ما کار بزرگی انجام می‌دهند و به دیپلماسی فرصت می‌دهند. بدون یک موضع قوی در میدان نبرد، یک موضع قوی اوکراینی، فقط اولتیماتوم وجود خواهد داشت. اما امروز، دیپلماسی امکان‌پذیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22448" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dc505262.mp4?token=IZIuPsFVEvm-p9qaZdhtzKtkWs-ciaoPzZSjnOKlnZzcw5OdtjBTHNtLPvYeb8fOaYx32dU-6hjiwPVzrMcn_63RaZ49jCTxIDm6qK4ZwL3mNbulRMWm81wg1of6yeQaNncYh3EjM7W17w89yQDiUznRuETw0IPLnh1hWT3m5FIxC-hDyeH-FG6o0QGPG9roTjQtl4T-bSq70ZbCdPwSMuOq6jr5XqZ0Ux79WRdeXN65UuPiqZ_O9RaPlRPw1hwpiAQwTSLtIhYhMX-vMOc1Dvw7be8VLNWN2M6KTKRevsN93m-FhieCRG0GfCbCFiVjVqQ_PUluOC8y1KqjGJnCtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dc505262.mp4?token=IZIuPsFVEvm-p9qaZdhtzKtkWs-ciaoPzZSjnOKlnZzcw5OdtjBTHNtLPvYeb8fOaYx32dU-6hjiwPVzrMcn_63RaZ49jCTxIDm6qK4ZwL3mNbulRMWm81wg1of6yeQaNncYh3EjM7W17w89yQDiUznRuETw0IPLnh1hWT3m5FIxC-hDyeH-FG6o0QGPG9roTjQtl4T-bSq70ZbCdPwSMuOq6jr5XqZ0Ux79WRdeXN65UuPiqZ_O9RaPlRPw1hwpiAQwTSLtIhYhMX-vMOc1Dvw7be8VLNWN2M6KTKRevsN93m-FhieCRG0GfCbCFiVjVqQ_PUluOC8y1KqjGJnCtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است. این رژیم در ایران به پایان آن نزدیک است. آن ضعیف است، برای بقای خود می‌جنگد، لنگ‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم. این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/22447" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/22446" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم. روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/22445" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پرواز پهپادهای ایرانی بر فراز تنگه هرمز!
سازمان دریایی بریتانیا (UKMTO) اعلام کرد که پهپادهای متعلق به نیروی دریایی سپاه ، در حال پرواز بر فراز کشتی‌های تجاری در تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22444" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=EuySIRUdeJhvDtBPzqQpGBfKcticPIk8Csj4G7S_EhzVY-oPP1aUB9Ik0C_ykXah2FooCi7nRpfYasMnq9abTflnmnXQuVDcSzVtOE5djhIpl0n0jdYGIwMupRUTJEAvjVDwoxmFU2QSKitSqJDScoJFFM3ZqTnz7S74115XmZH7MvUeQOSMzMdv56NhB1N5zjxOvLDs53AU6p3ldBgfJQRaZKeiyeyFsLCc3QhUTZYFKnytAdGLcNH4tvAJnbCu9qHEiBclfY56mdrCBoEYVd0ZnGQOaRln1l2eU9CsbyCEm--Ovvy3igeMsgoxL7ymk7cTq1YoWpH1eXZi9zDRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=EuySIRUdeJhvDtBPzqQpGBfKcticPIk8Csj4G7S_EhzVY-oPP1aUB9Ik0C_ykXah2FooCi7nRpfYasMnq9abTflnmnXQuVDcSzVtOE5djhIpl0n0jdYGIwMupRUTJEAvjVDwoxmFU2QSKitSqJDScoJFFM3ZqTnz7S74115XmZH7MvUeQOSMzMdv56NhB1N5zjxOvLDs53AU6p3ldBgfJQRaZKeiyeyFsLCc3QhUTZYFKnytAdGLcNH4tvAJnbCu9qHEiBclfY56mdrCBoEYVd0ZnGQOaRln1l2eU9CsbyCEm--Ovvy3igeMsgoxL7ymk7cTq1YoWpH1eXZi9zDRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، نخست وزیر اسرائیل، درباره ایران:
آنها به ما حمله نمی‌کنند. ایران از این کار اجتناب می‌کند و دلیلش را هم می‌داند: چون اگر این اشتباه را مرتکب شوند و به ما حمله کنند، ضربه‌ای خواهند خورد که حتی تصورش را هم نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22443" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqrMNJLF7vbbMM75w-jtH6q_M_La8Qv7tHrevQwrtws_GGfyst6vEZo8MUU6YUc4_gX4iv1jWfu2R9MEPhT0s0CHNMx2gLia61o24Vgl5sULotZoo--7prFl4bgB0u8oTPDWCSpoMMdwz1W39OAQegmv8t2pqrYFqKHRy2gHu0xmSdqaCR3gno22CQcJfX27jHIuQ0pAOvb0N6FMkBBMvJ99a7wxKxIhM46jyUYjHVSyMX3QtEPZp0pT6PkQbjdTdb9TjjjZBMOwJe7T44DW2ar5JfB72jxDAJDubERQFMWoTgV_EO4B1L8g9fVq1Pt6qov0-Pjq0OH5hgzNIqLTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خطاب به رابرت دنیرو : حتی این احمق هم داره متوجه میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22442" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6cgg03XjhMgh_xIkU6humCNhFX0ug9CQEJ-R063kl71hi6u25H1OLc5NGtjuGk5QPi5vvG2KOZeTy8MfwyOppzOyrRXpBeg587-EHENbbad0lbHsNn9yLFqiNiYrcUSbCK8vAbrSCBiMeqjFfXGj5SthdvWgOflUeap8BZoxZRWy0F7q87N9KycZbTJYCN8fCFzHfAQrGKb8yswWoXvTlAzb6Yc-FqVszO2cq1J9nfDRIuol1rxyvqoZkhhSGCTaQb5IWwU7cp1K-a8W5UnaTWBta6t5MWOdRCdoTMs3mUVk2dUbh7VPC2BUYaWWT1Ixw1ol3rbDS4vTm8BC6P6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22441" target="_blank">📅 18:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N10PLqhuJSZ_ZwYxwOk-Fn3RZ43Cnr0xXCM3MlcmrzMwP45Og6LjV5lE4qNzwljvulis3uJ9ICmjyY5S2-C9bYjy5HzmYUn57hdGcxUPSvbUKm2ln1mipNq6hko5xw1bWLG5Z0HpibraHNbsNxpOjTQQnk9YG4Oqn38NlELX5DaGOjnlaxjtrJQgBfWq-xhKrGILrREAn3wHJPwQ6Q3FYU8GI6Q-WUs9bLcAsHJCENB6zi9-SamVybL3jT-er9HJCXx1AN3V4MY_77z8q7qSdRJIuZcySY31aDoFdiR_f6dhzYCwkYwmbVYncBcqiQbFcN47mYmVlkfU6Oi7jQE8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رنگ موهاشو تیره تر کرد
@WarRoom
😁</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22440" target="_blank">📅 18:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وال استریت ژورنال :
سالانه میلیاردها دلار از منابع مالی ایران
با وجود تحریم‌ها، از طریق حساب‌های تسویه بانک‌های آمریکایی و بانک‌های خارجی دارای روابط کارگزاری با آمریکا جابه‌جا می‌شود. در سال ۲۰۲۴ حدود
۹ میلیارد دلار منابع مرتبط با ایران
از مسیر بانک‌های آمریکایی عبور کرده است. شرکت‌های پوششی و شبکه‌های پیچیده انتقال پول، شناسایی این تراکنش‌ها را دشوار کرده‌اند. مقام‌های آمریکایی با یک دوراهی روبه‌رو هستند؛
سخت‌گیری بیشتر ممکن است به جایگاه دلار آسیب بزند و تساهل بیشتر، مسیر انتقال پول ایران را بازتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22439" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تلگراف: لیبی کلاینر، همسر یکی از سربازانی که پس از سرنگون شدن هواپیمایشان در غرب عراق کشته شدند، در یک پست در شبکه‌های اجتماعی نوشت که دولت ترامپ او را برای دریافت غرامت‌های مالی واجد شرایط ندانسته است، زیرا کنگره به طور رسمی جنگی را علیه ایران اعلام نکرده است.
تلگراف هم گفت پنتاگون از پرداخت غرامت به خانواده‌هایی که توسط ایران در خاورمیانه کشته شده‌اند، خودداری می‌کند، "زیرا آن را جنگ رسمی نمی‌داند."
اما نکته مهم این است که
پنتاگون در نهایت غرامتِ مرگ را کلاً قطع نکرده است.
پرونده‌ای که خبر از آن شروع شد، مربوط به بیوه یک افسر نیروی هوایی،
الکس کلینر
، بود. به او گفته شده بود فقط برخی مزایای مرتبط با منطقه جنگی، از جمله
combat pay
و معافیت مالیاتی، به دلیل اینکه «جنگ رسمی نیست» شامل حال خانواده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22438" target="_blank">📅 18:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ9-k29K6PVHyYQMIPm5WSCvXsaP1-EWEdtUEQe20UOR-ZMJ1RTyO4mHogBCYNeFHYEC2BAgM7_dw8xAIYKt0-dp7velvkzuuWDPwRFznUJ_AW0aeJDzCckLX9xdBwOJSC_8Hc2T3KGvfjcQFma7J-HXoV5t5yvmx0Q1ImOZsWP1vfJd0ttddaX9Axe7DzcXFuLVmvyIjO_Lnam36aPxOWRE-ULEClYxPUqLHIrm2-bG8cqk5Q_l7CadudDucBbr9OdNBWJ2O8bJdZ_uvFvXcx8u6d8lIe31KQQSC1CaMqedbVfm2qPrce8yc_8lH9IfkV0ceN1WRWks7s1qcLreUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ گز لا (Kuh-e Kolang Gaz La / Pickaxe Mountain)
در شهرستان نطنزِ استان اصفهان و حدود
۱.۵ تا ۲.۵ کیلومتر جنوب مجموعه هسته‌ای نطنز
قرار دارد. مختصات ثبت‌شده‌اش حدود
33.7051, 51.7081
است.
@WarRoom
https://maps.app.goo.gl/LJq8rZ2kNdve6xiVA?g_st=ic</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22437" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارشهای بسیار از شنیده شدن صدای انفجاری مهیب در اراک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22435" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : با تماسی‌که با منابع داشتم نفتکش هایی که دیروز که آمریکا هدف قرار داد ۱ عدد با مالکیت ایران بوده ولی ۲ عدد آنها فقط در اجاره ایران بوده که حتمأ بیمه هم داشته اند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22434" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYsbHREOQdFTnsb4Xpa4lt5HKFltLSIfKyVnqvFhfziCTeAg8W-fhkDj51379jAKF-08ndLLXsPAcq-LDhG3awywMA26LJi6gm0KmRSBU3UysUqsNRaSo_xl1QRwVimcLHn2T_uovVWCkd8wCiw7jN4r0y7MaYHzJALVkFBPm6CYx_rZqd5Jn7UEWyBDITUhw9wi-_stj4-XpLdbpQI8r7Tjyi4w81jDQoiLIHMpWFILwXi7iXdX8DnUziWzNs2iQIOpERbIIz9tsc1Tod8n-47tsXqN1DMztIJ80m7aX1XIb8TbBRNwftbVxTZO63T4zUu3xCcop_UjgcXsp1knng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار  @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22433" target="_blank">📅 17:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=XGmNeK-cSfWlHLyP83zvgbxfeYGcxxby-FJa_HDizyY0DJdqtB65T8WLb1Cwdg5zesOB0yc_hC5P1ZziZXM4RCQEyie017uAQ1C7mfTcKvp02n3wUgRPtFSdWlNNgE5ac2HubxvlNV_6ar39jBK3JGM1GMOQJ8zXG4hPFbjcHT3RjjcqjgSFnL-AbEyhAZpwjsCUtaYDUE4MFgxUrvJFkmT8zcxF7JdsbjW1eKEOYsA_OetepvZFEMXeEyY9uk1V6LQKUIBQrIcauQvUiRlDjPBRjNtNnq5sqB8UO7oNgBqsiHYY6e2n2X-147vPd8rHyKL-1E5ybiYBuDMQudCGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=XGmNeK-cSfWlHLyP83zvgbxfeYGcxxby-FJa_HDizyY0DJdqtB65T8WLb1Cwdg5zesOB0yc_hC5P1ZziZXM4RCQEyie017uAQ1C7mfTcKvp02n3wUgRPtFSdWlNNgE5ac2HubxvlNV_6ar39jBK3JGM1GMOQJ8zXG4hPFbjcHT3RjjcqjgSFnL-AbEyhAZpwjsCUtaYDUE4MFgxUrvJFkmT8zcxF7JdsbjW1eKEOYsA_OetepvZFEMXeEyY9uk1V6LQKUIBQrIcauQvUiRlDjPBRjNtNnq5sqB8UO7oNgBqsiHYY6e2n2X-147vPd8rHyKL-1E5ybiYBuDMQudCGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22432" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=C-l2YuohKZJ1iatKuMdMe_wbBZb5VRxP173km97rBT_kTdutinsuE4MMg-TvvGMwmIhyTT5EV4sXfx31GR0OMWG2ZGigMPXrfW4jCGBsSE30t6py2qB5sD00utGNX9sHMdZrnBnT0KiyKGs1E8xfa5V7EHJdKfdT3ySrFiXLbEppwt7rGZAaei_qO4-_b2UjjAssidYFwttygJOo8v_3zQDCVfI69Lu0BQ4ux01wZD_ZhjpvmwAl_ivMXN5X5To0FrBX_G7P3-S3BU1mimhL4YgD8NBU8PjaPgRhac7AVtINTcWpUsP_5gCoi5_mfUqUA3zlXDwr2XwChNFlb5t5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=C-l2YuohKZJ1iatKuMdMe_wbBZb5VRxP173km97rBT_kTdutinsuE4MMg-TvvGMwmIhyTT5EV4sXfx31GR0OMWG2ZGigMPXrfW4jCGBsSE30t6py2qB5sD00utGNX9sHMdZrnBnT0KiyKGs1E8xfa5V7EHJdKfdT3ySrFiXLbEppwt7rGZAaei_qO4-_b2UjjAssidYFwttygJOo8v_3zQDCVfI69Lu0BQ4ux01wZD_ZhjpvmwAl_ivMXN5X5To0FrBX_G7P3-S3BU1mimhL4YgD8NBU8PjaPgRhac7AVtINTcWpUsP_5gCoi5_mfUqUA3zlXDwr2XwChNFlb5t5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از موشک‌های هواپرتاب بالستیک Blue Sparrow استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به ۲ تن که از جنگنده شلیک…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22431" target="_blank">📅 17:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw0uYdHfUmIEvLojvGlI-C6oddbZacWPBFI4-FOv4rKfhhfcXRI3g5uoNu1auLZieTc37DHdZFhxEnuhcgwd-7E8sgMBihgP_v2t73aARfGN1es4nQtVTVl5HhK6IkZkeaiZ5nfhgPuNo9etvdHc3UaQpvyYNSvXw2w6lTiGsC17V2-SU9k1lqIx8IwVF-NfU7KIZTeguDIlrZYKjjY77-2qgPOFkbw4aIlOw0Uw5Rx5T_a-zTvv9Q_mCQIFrMWWWSg0TfeJVW-tnzZNEwPt1BEIi1mpFwjcSkJSdjvdAY3A_CyMqM__Te4ajv8dtSEGY0Pyykg5DVUQV-JixGwYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد
روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از
موشک‌های هواپرتاب بالستیک Blue Sparrow
استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به
۲ تن
که از جنگنده شلیک می‌شوند و پس از رسیدن به ارتفاع بالا با سرعت بسیار زیاد به سمت هدف شیرجه می‌روند.
گزارش‌های اولیه از پرتاب حدود
۳۰ بمب
به این مجتمع خبر داده بودند، اما گزارش‌های بعدی استفاده از موشک‌های Blue Sparrow را مطرح کردند. با این حال، مدل دقیق تمام مهمات استفاده‌شده هنوز به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22430" target="_blank">📅 17:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روزهای بسیار حساس در انتظار پرونده هسته‌ای ایران
؛ نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از فردا با حضور نمایندگان ۳۵ کشور برگزار می‌شود و پرونده هسته‌ای ایران یکی از محورهای اصلی آن خواهد بود. آمریکا و سه کشور اروپایی در این نشست چندروزه به دنبال تصویب قطعنامه‌ای برای ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، به دلیل عدم پایبندی تهران به تعهدات پادمانی خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای هستند
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22429" target="_blank">📅 16:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22428" target="_blank">📅 15:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nguGJjayuI_y0S1UO1ASmUjKNfGU6GquzCrDI-sVSJOfemtGOnxLRJWZnau2_IOab3WxHbNb187OPDebaushMi-oEPHckBGg3k3y9FnHrVVOqpHQXVBCtSl04W_UloIt2TV4RRyDuvYjIZ1N_M2E443Gm07ECRtmCnVqO63rCllIEw1iy9PgMgJJhOO1HxCIxH1DrPSpRTcSpXb5gHhVGuD5mRin0VqPTOkVVvQKNrp2wUIwKOf7a2X8K9OKnr4Vhl10CV12EEqBy29BgNLee5HEkF6F50vSPqGADkWzj4JP0Ydu_-uLT3gnZKmDGWoMtOvBd2W5xi-t3tQd9j3VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جوری شده که حتی اوستاد هم نمیتونه تحلیلش کنه
😂
خدایاااا بسته دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22427" target="_blank">📅 15:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS9rrTZMFA5MLk6AgaanHJXCVzHSDqIiuIZzhzorElR3g31TZZ_4odAcMWm0GfFJI_MDZKTto5N-kN1FVOyrnnBKBoA4JBeNVUAQUEhTJ6-WurmyMk1JIzTSPdv1ri5auNOCJCCSN7OI2n_alwX7RM8bYufK6TruFXcvfIbTY_lJJeLWMxEquAeAOppE3lQZzkau6tLhkZhp2XHLKJh9qEKK8BPVrTyx1m99L4WQYp931f4Ovpxg21HJgERBdH3ypf0y3pPpLCD7WVczEahb6eX0mjoQy6WNqrZJXLWxEXc9lZx_52JN2P2El2BVKTWCmbLE1hkXyGJUfW6o0KUe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در حالی که نیروهای سنتکام همچنان به اجرای
محاصره دریایی علیه ایران ادامه می‌دهند
، بر فراز آب‌های منطقه‌ای گشت‌زنی می‌کند. تا امروز ۱۵ شهریور، نیروهای آمریکایی 92 کشتی تجاری را تغییر مسیر داده‌اند، 3 کشتی را غیرفعال کرده و 2 کشتی را توقیف کرده‌اند تا از رعایت دقیق این قوانین اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22426" target="_blank">📅 15:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منچ‌ اوسینت : از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در مسیر جنوبی تنگه هرمز، پس از شلیک هشدار نیروی دریایی سپاه، تغییر مسیر داده و برگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22425" target="_blank">📅 15:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رویترز:
اوپک‌پلاس امروز در حال بررسی حفظ سیاست فعلی تولید نفت برای ماه اکتبر است و انتظار می‌رود افزایش بیشتر تولید پس از ماه سپتامبر متوقف شود. رویترز می‌گوید
جنگ ایران و اختلال در صادرات نفت از تنگه هرمز
یکی از عوامل مهم این تصمیم است؛ در عین حال اعضای اوپک‌پلاس همچنان پایین‌تر از سهمیه‌های تعیین‌شده تولید می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22424" target="_blank">📅 14:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری i24:
ارتش اسرائیل امروز یک رزمایش ناگهانی و چندجبهه‌ای با نام
«Breaking Dawn 2.0»
آغاز کرد. این رزمایش به دستور رئیس ستاد ارتش اسرائیل انجام می‌شود و هدف آن سنجش آمادگی نیروها برای سناریوهای همزمان در چند جبهه و تقویت توان ارتش برای مقابله با تهدیدهای ایران عنوان شده است. پیشتر افشا شد که
ایران در حال آماده‌سازی یک حمله هماهنگ و چندجبهه‌ای علیه اسرائیل
است که از نظر ابعاد و هماهنگی، با حمله ۷ اکتبر مقایسه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22423" target="_blank">📅 14:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=RB2OOQ51UCZ2Deyg0oG01mFX9oIQlWfUaG0l9jjSHMNuVnTFeAYNJzSdv4czkfuGiMgIxKpy6Bms4odzxWmV3G2pLcWf1ovINJRJkt_1FdgnyXOLzT-jmO2N2OgChFxyxrVE0vaB8yGCJNDssl9oTJLzGtnCGVydVMiXimYTsyrm9VikiPMbYBtwsy3H9sUexBgx5jZr6x2Kz08vg1z6TLZbttAgWtASXPothKbdxZNDgWNSSxgumvUZbEbTLk7L725ft-VjpysZOiFBbqzgYueJryMt0SQ7FAPCBtXE31wh9gUbPQhVijZJsui4bi-VHDnnW6ycBvVSCTvgpSSA7ZRb-I4vm67Y4ya8clh0PgpRew8w7Up7zuco1lgvxI8S22zZ0GzsfFLrr8gUp4L4SM9Ng9Tk67czfMyH5-sKNhXhjflCAcOfxWcR4LIoGA2x7Zi7Wilm3bYP-s-HSZfnJM8iSop0M4ke4c1VA8Z6BEQAI1h9I8E9ZS1ahqMjd8ynGWJYv2BY9xvV-_sYXrVvmHCc13IU7tfeSof7HgncHbm-PikiLwOj3kbs8Sb8h272IM8CjvidMU_tdk8xemuJufr8bB0Znwra6WVA5hiOsqEbum4Lmg8Fz6ysa5GbZhN4dWxHis-8GHpJspQTP2eO6v4OlmtwadB5q-DPo9CB9co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=RB2OOQ51UCZ2Deyg0oG01mFX9oIQlWfUaG0l9jjSHMNuVnTFeAYNJzSdv4czkfuGiMgIxKpy6Bms4odzxWmV3G2pLcWf1ovINJRJkt_1FdgnyXOLzT-jmO2N2OgChFxyxrVE0vaB8yGCJNDssl9oTJLzGtnCGVydVMiXimYTsyrm9VikiPMbYBtwsy3H9sUexBgx5jZr6x2Kz08vg1z6TLZbttAgWtASXPothKbdxZNDgWNSSxgumvUZbEbTLk7L725ft-VjpysZOiFBbqzgYueJryMt0SQ7FAPCBtXE31wh9gUbPQhVijZJsui4bi-VHDnnW6ycBvVSCTvgpSSA7ZRb-I4vm67Y4ya8clh0PgpRew8w7Up7zuco1lgvxI8S22zZ0GzsfFLrr8gUp4L4SM9Ng9Tk67czfMyH5-sKNhXhjflCAcOfxWcR4LIoGA2x7Zi7Wilm3bYP-s-HSZfnJM8iSop0M4ke4c1VA8Z6BEQAI1h9I8E9ZS1ahqMjd8ynGWJYv2BY9xvV-_sYXrVvmHCc13IU7tfeSof7HgncHbm-PikiLwOj3kbs8Sb8h272IM8CjvidMU_tdk8xemuJufr8bB0Znwra6WVA5hiOsqEbum4Lmg8Fz6ysa5GbZhN4dWxHis-8GHpJspQTP2eO6v4OlmtwadB5q-DPo9CB9co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولودیمیر زلنسکی : «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22422" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گاردین:
لئون پانه‌تا، وزیر دفاع پیشین آمریکا، امروز هشدار داده جنگ ایران ممکن است
شش ماه دیگر نیز ادامه پیدا کند
. او سه مسیر احتمالی برای ترامپ مطرح کرده: عقب‌نشینی، ادامه جنگ فرسایشی و حملات مقطعی، یا تلاش برای به‌دست گرفتن کنترل تنگه هرمز.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22421" target="_blank">📅 14:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=UmAgEoiFk22qQ1bIouowO3o1_URPtSpvkur10QVp3ZsUZH0YaaKcpl6-7LuULbrkhrErPlhYJzIgpoGY5bN3-ppmYC6rCmqcAAJQ5rqQHpXnNtazwyKawd-cYA5eP52LtNTfmXHwUSEH-jDc8_FDzdMeclsFPucbTvGVyMKbgnMq2EDXBNtvJREmQxcTC0k9_4vkuKdlzCMSg4SkCpgIXNjBgRfxFogBlrIL9EBiIV0ebMWHrpr45pVG1Ol-mvXh4W8BsOrqpIG0ItgO69yDy3Rq6Dq13rJQrAl-rPnuWKNe4OfmZmh_qqauv4SyGZEclKh-O7K2bInYB7r86IRy3oUfBbBRdd9eL_qPei9b0bMoJ6RlSewk-8GOKZ_vKlpDXcWUq6lR1XR3ubYv06KgIyL5dSCY1jpAvwmhwJS4rCl9OJJHsssDUnTq-tOLtD6CnowmyBxi6n_Vd83NL39qcInPB0moN0fGmK4IhO0NZLysa0KYbXXqy6TnfW_0dxJzMkVemNfyeRh9gCjYoVgDJA8EfTjmyxjZGiQ7djJmyLyD_rt5W9KJ4Hc9e7iXPhtfNbZglr3FlW04b3RJbFWYpammHGo0BkFbQ5_FNSEPMdyrlxqaic65uyizYq9bRinNaIdfsw5Xx8IxSk4_80vhaiYUStQ1YXk4OVfHhCz-pG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e392ac131d.mp4?token=UmAgEoiFk22qQ1bIouowO3o1_URPtSpvkur10QVp3ZsUZH0YaaKcpl6-7LuULbrkhrErPlhYJzIgpoGY5bN3-ppmYC6rCmqcAAJQ5rqQHpXnNtazwyKawd-cYA5eP52LtNTfmXHwUSEH-jDc8_FDzdMeclsFPucbTvGVyMKbgnMq2EDXBNtvJREmQxcTC0k9_4vkuKdlzCMSg4SkCpgIXNjBgRfxFogBlrIL9EBiIV0ebMWHrpr45pVG1Ol-mvXh4W8BsOrqpIG0ItgO69yDy3Rq6Dq13rJQrAl-rPnuWKNe4OfmZmh_qqauv4SyGZEclKh-O7K2bInYB7r86IRy3oUfBbBRdd9eL_qPei9b0bMoJ6RlSewk-8GOKZ_vKlpDXcWUq6lR1XR3ubYv06KgIyL5dSCY1jpAvwmhwJS4rCl9OJJHsssDUnTq-tOLtD6CnowmyBxi6n_Vd83NL39qcInPB0moN0fGmK4IhO0NZLysa0KYbXXqy6TnfW_0dxJzMkVemNfyeRh9gCjYoVgDJA8EfTjmyxjZGiQ7djJmyLyD_rt5W9KJ4Hc9e7iXPhtfNbZglr3FlW04b3RJbFWYpammHGo0BkFbQ5_FNSEPMdyrlxqaic65uyizYq9bRinNaIdfsw5Xx8IxSk4_80vhaiYUStQ1YXk4OVfHhCz-pG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22420" target="_blank">📅 14:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فایننشال تایمز:
آمریکا طی چهار ماه گذشته یک عملیات پرخطر و محرمانه برای مین‌روبی تنگه هرمز انجام داده؛ این عملیات با مشارکت نیروهای ویژه، قایق‌های رباتیک و زیردریایی‌های مجهز به سونار انجام شده است. با وجود اعلام ترامپ درباره پاک‌سازی تنگه، کارشناسان هنوز درباره ایمنی کامل مسیر تردید دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22419" target="_blank">📅 14:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز:
ایران اعلام کرده نیروهایش یک شناور بدون‌سرنشین آمریکایی را هنگام تلاش برای ورود به تنگه هرمز هدف قرار داده‌اند. آمریکا هنوز این ادعا را تأیید نکرده است. این اتفاق یک روز پس از حمله آمریکا به سه نفتکش ایرانی رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22418" target="_blank">📅 14:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">افزایش ۲۰ هزار تومانی نرخ دلار  دولتی:
۱۰۰۰ دلار با کارت ملی نرخ ۲۲۰ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22417" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UamrzULNGPv9FfbHX3L81FibtONUCSa7o2TBO1IkXwdrZuZ_BfkOHw0PXQUru5f0yRHHs8hbDB02amQT5LgHMXfCBCH9J4M5m4ZJRu2_s9MJYAtTEUyNJFRkFSTl8HlMV_DCRLexbnloDySYAXL5DGqGmzwjUJAqilQw80krICAoMQi_GgQLmPqWyJGtoVH5K4NchpbHD7piuy6Onp1RKJQEzyJre2KnoZzOBuHo98jFEohqpcoK_oh12CPco35FrBcDAqZ8dVxUevDHjbFSMwOtejsFd6-mrfYtfz-WQPuL70Ahb8WK4si1_nY5QzSOUF4AnfUOEbEXcJfb4oKSS0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025828335d.mp4?token=rTB-OzzHHNZqJuT0CqtJWk0rnIZkq7maWIhhm_qyzS3iEJ0ytZX8R1tdsvY2ExAEwkXW3aMFJ_uF0gl_PMrWJ-OUZ3PIrtio9fZk9yNKz3bT-SXHMEC9jhj4cQorYW7A80xFVbDlhbvdj99Ent_IaspNm0qn_eEiYE3a6ibgyZG9HtitN18GDa9IOggUm_F6X334H9q92gM4A97YIN3S7aSMJBZpjqvdBvsUgYVJjL7Q84HY5Wu7LbVuLR0TJTOt4aBaSr6t5QOurULZ3UAvFBGuJ4c-sXVGg_Cj_o5V2x5ISXY3I7EGpwcAxqfq_2lwI9ESPmdiVqeI9-Z0m3E7UamrzULNGPv9FfbHX3L81FibtONUCSa7o2TBO1IkXwdrZuZ_BfkOHw0PXQUru5f0yRHHs8hbDB02amQT5LgHMXfCBCH9J4M5m4ZJRu2_s9MJYAtTEUyNJFRkFSTl8HlMV_DCRLexbnloDySYAXL5DGqGmzwjUJAqilQw80krICAoMQi_GgQLmPqWyJGtoVH5K4NchpbHD7piuy6Onp1RKJQEzyJre2KnoZzOBuHo98jFEohqpcoK_oh12CPco35FrBcDAqZ8dVxUevDHjbFSMwOtejsFd6-mrfYtfz-WQPuL70Ahb8WK4si1_nY5QzSOUF4AnfUOEbEXcJfb4oKSS0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگران تایلندی لایه‌هایی از جلبک را از ناو هواپیمابر آبراهام لینکلن پاک کردند این ناو هواپیمابر پس از استقرار طولانی در خاورمیانه، به طور کامل تمیز شد و بازدید خود از بندر لائم چابانگ تایلند را به پایان رساند و به جنوب چین باز میگردد تا در مسیر خود به سمت سن دیگو بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22416" target="_blank">📅 13:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال استریت ژورنال : ‏
در نبرد محاصره، زمان دیگر به نفع جمهوری اسلامی نیست
.‏ ایالات متحده به کشورهای خلیج فارس کمک می‌کند تا مقادیر قابل توجهی نفت را از منطقه خارج کنند و در عین حال مانع از انتقال محموله‌های تهران می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22415" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قشقاوی در گفتگو با الجزیره: جنگ فعلی برای ایران یک جنگ موجودیتی است. ایران درخصوص پاسخ به حملات آمریکا به نفتکش های ایرانی ذره‌ای تردید نخواهد کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22414" target="_blank">📅 12:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک‌تایمز: دولت ترامپ در حال بررسی طرحی است که بر اساس آن،
خانواده‌های متأهل با یک والد خانه‌دار
نیز بتوانند از یارانه فدرال مراقبت از کودکان استفاده کنند.
این کمک‌هزینه حدود
۹ هزار دلار به ازای هر کودک در سال
خواهد بود و از یک صندوق فدرال
۱۲ میلیارد دلاری
تأمین می‌شود که در حال حاضر عمدتاً برای کمک به والدین کم‌درآمد جهت کار یا تحصیل استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22413" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22412" target="_blank">📅 12:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22411" target="_blank">📅 11:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود و دیگر نفتی نیست که چین بخواهد بخرد @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22410" target="_blank">📅 10:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بسنت: محاصره و تحریم‌ها قدرتمندترین فشار اقتصادی تاریخ علیه ایران است
تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز آن را خریداری نکرده، این مقدار به زودی تمام می‌شود
و دیگر نفتی نیست که چین بخواهد بخرد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22409" target="_blank">📅 10:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmp6rpeDSJwRnFBmhSppCkRJF8JtR6MOIj6VImuceA-uV2Ed1_GqXzaK54Qkyl1Ci5lIVOe_kiv7Jq5I6TxQwZB3-VvQapNL9ag4PWF8OCCmwLc3vOy4tBMLoM-LoQCDetS5G_g4pLWakDLpgijsor-HVm5wGnk1CUyYibFNIuoTA_P8VsEiEac_8RCO4IFxe3-E4X3-ECgtF_rD6JzIoiu9vsor5cRU1i3ctX9HDO4zHvdCrvaB6PXfW1P_rXASvbQzD9DBp_jsjrWoyfSOW-VUVXCLdfWtTBxjkDBRgTllQFN2zqbfjH6gtIpjOw52E5Akpj8B0DR4I0qX2lCiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بسیار تأسف‌بار است آنچه در اسپانیا در حال رخ دادن است؛ کشوری که
ه
یچ کنترلی بر
مرزهای
خود ندارد. واو!
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22408" target="_blank">📅 10:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دنیس راس، مذاکره‌کننده و فرستاده پیشین آمریکا در خاورمیانه، هشدار داده است که
احتمال دارد تنش‌ها در خاورمیانه به‌زودی تشدید شود
.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22407" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مارک لوین در واکنشه حمله آمریکا به نفتکش در جزیره خارگ : «در حال نزدیک شدن به مهم‌ترین هدف اقتصادی در ایران؛ منبع مادر ثروت.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22406" target="_blank">📅 07:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیویورک‌پست:ارزیابی‌های اطلاعاتی اسرائیل حاکی است ایران با هماهنگی حزب‌الله، حوثی‌ها و شبه‌نظامیان عراقی در حال تدارک حمله‌ای چندجبهه‌ای و مشابه ۷ اکتبر علیه اسرائیل است. به‌گفته جروزالم‌پست، سپاه پاسداران رزمایش مشترک با نیروهای نیابتی و تولید پهپاد و موشک را افزایش داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22405" target="_blank">📅 06:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مقام اسرائیلی : برای تحویل جسد اعضای حزب الله در تپه علی الطاهر، حزب‌الله باید پول موشک های شلیک شده را بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22404" target="_blank">📅 06:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آکسیوس: سپاه پاسداران در حملات اخیر خود در مجموع ۶ کشتی را هدف قرار داده است
؛ سه نفتکش و سه کشتی. بر اساس گزارش آکسیوس، سه نفتکش در حال عبور از مسیرهای غیرمجاز یا خارج از مسیر تعیین‌شده در تنگه هرمز هدف حملات موشکی قرار گرفتند و سه شناور آمریکایی نیز هدف حملات ایران قرار گرفتند. در آخرین مورد، ایران موشک‌های بالستیک به سمت دو ناو نیروی دریایی آمریکا شلیک کرد که به گفته سنتکام، یک ناو هواپیمابر و یک ناوشکن مجهز به موشک‌های هدایت‌شونده توانستند از این حملات عبور کنند و آسیبی به نیروهای آمریکایی وارد نشد. در واکنش، نیروهای آمریکایی سه نفتکش ایرانی را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22403" target="_blank">📅 06:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هم اکنون ۲ پرتاب از سیریک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22402" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=TAcZ8w1855aLtFAj-MZEqxUr23VLo0JEWME1fcilzE306IZN_KmH5qdAXqLESKdi-X-KEjO8cCXEmjcyhRR1VSlfpIPwFs4s_0OTLOrvxluwMpqE5OGTtqzwGmXFL-0xkfHhfaag8vFbHJmjz4X30Xy6ChYZFUXht4Ws7i6GolhBL9V-OrOLiDwKF7esso9z3IYictY89oixf7sTIulavzdYgXXQrCn_6JNl9bLqB31qFzmDuZWy9E9n3taf-R4vwqmJ60AeXlgedGwcfJt8b17SCZjvG2ShdxPB7RdQMWBx-Zrx8fXpnRFhnk-1uSkgY6kceBlAOqKQOpMRE6TeIVNp6g1FuXrQeVE0LFatwlgTuiUflU9xLtfPdyBzuVf62aQXoIvXmaX6F-Hm9ZowlhUNSemvJnqVgVdvllEEIhVWzyQoZ7Q4T2TbpNzxteAql0sdpYkTHKOpByHuFMzm30o1puHXaEmWSxNK5YkpXN9gerxg1bP8gBdM23uWnk4pXhcqBrpK-CXfPW2B91dPQTvU4jzQiz7ZnW0pt_RciydfQNxsM3JeAT47YOdnC-x6f5YRDKc-aXCjRev9GVm46vYjd4QqGI3QoEK_qR9o-biI4JSDibhejGEIEyOUJnRwNlZnpQYzK5L4vmssZ3JJai0u4FALckFSR2U-onZnSi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ecaf8975.mp4?token=TAcZ8w1855aLtFAj-MZEqxUr23VLo0JEWME1fcilzE306IZN_KmH5qdAXqLESKdi-X-KEjO8cCXEmjcyhRR1VSlfpIPwFs4s_0OTLOrvxluwMpqE5OGTtqzwGmXFL-0xkfHhfaag8vFbHJmjz4X30Xy6ChYZFUXht4Ws7i6GolhBL9V-OrOLiDwKF7esso9z3IYictY89oixf7sTIulavzdYgXXQrCn_6JNl9bLqB31qFzmDuZWy9E9n3taf-R4vwqmJ60AeXlgedGwcfJt8b17SCZjvG2ShdxPB7RdQMWBx-Zrx8fXpnRFhnk-1uSkgY6kceBlAOqKQOpMRE6TeIVNp6g1FuXrQeVE0LFatwlgTuiUflU9xLtfPdyBzuVf62aQXoIvXmaX6F-Hm9ZowlhUNSemvJnqVgVdvllEEIhVWzyQoZ7Q4T2TbpNzxteAql0sdpYkTHKOpByHuFMzm30o1puHXaEmWSxNK5YkpXN9gerxg1bP8gBdM23uWnk4pXhcqBrpK-CXfPW2B91dPQTvU4jzQiz7ZnW0pt_RciydfQNxsM3JeAT47YOdnC-x6f5YRDKc-aXCjRev9GVm46vYjd4QqGI3QoEK_qR9o-biI4JSDibhejGEIEyOUJnRwNlZnpQYzK5L4vmssZ3JJai0u4FALckFSR2U-onZnSi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه پا : آبرومون امروز رفت فعلا این
تصاویر منتشر نشده از رصد و اقدام علیه شناور های متخلف
رو ببینید
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22401" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=vrvXMo92pc0ypzmRYbWCtIOAwlfTvcYGtN3aM3qRCco2oNGSCcIKN4MOM_xt52G74-rOFopEZlmWsfwNBw5FYZjCsEE3O2FWJ4ctSsgFtrhEzutjR7nAlM2ySTmMb3ryAoT5oIcyAU_rU27munY_dHY_fAvBD3EVPVvXldgbukd6UXRH5MTknMapO7uiK-_ImWXw39V_LBJ7BbF-g19Hn1O9S3Akzy5AGLgMEpX-uzAkQbTuaKVEsWNYnVpA30NAnaaHdQwTTLEVs3SlZkK1qPooAeXFWiR3FNR5TWwmzvUwqJqajw2_8CMB0LHfEL9VSDGGXDyjNNjHHNdoGCGCMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec62b949f8.mp4?token=vrvXMo92pc0ypzmRYbWCtIOAwlfTvcYGtN3aM3qRCco2oNGSCcIKN4MOM_xt52G74-rOFopEZlmWsfwNBw5FYZjCsEE3O2FWJ4ctSsgFtrhEzutjR7nAlM2ySTmMb3ryAoT5oIcyAU_rU27munY_dHY_fAvBD3EVPVvXldgbukd6UXRH5MTknMapO7uiK-_ImWXw39V_LBJ7BbF-g19Hn1O9S3Akzy5AGLgMEpX-uzAkQbTuaKVEsWNYnVpA30NAnaaHdQwTTLEVs3SlZkK1qPooAeXFWiR3FNR5TWwmzvUwqJqajw2_8CMB0LHfEL9VSDGGXDyjNNjHHNdoGCGCMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیران آمریکایی، ویتکاف و کوشنر، پس از سه ساعت مذاکره با پوتین، کاخ کرملین را ترک کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/22400" target="_blank">📅 00:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه های رژیم : تمامی افرادی که در کلیپ رژه طرفداران سازمان تروریستی مجاهدین خلق در کوچه پس کوچه های‌کرج، حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شدند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22399" target="_blank">📅 00:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس اداره اخبار مجلس:
۵۰ روز است که یه بشکه نفت هم نفروختیم.
هیچ کالایی هم از جنوب وارد کشور نشده‌. محاصره اقتصادی بدجور دستمونو بسته.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22398" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زاکانی: وصیت نامه آقا با خودش تو بمبارون از بین رفته
@WarRoom
😁</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22397" target="_blank">📅 23:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: «اگر ما علیه ایران اقدام نمی‌کردیم، ایران امروز بمب‌های اتمی داشت که قصد نابودی ما را داشتند.
حالا آنها دوباره تلاش خواهند کرد. آنها دوباره تلاش می‌کنند و دوباره تلاش خواهند کرد تا محوری را که ما شکستیم، بازسازی کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/22396" target="_blank">📅 23:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قالیباف : بستن تنگه هرمز به ضرر ایران شد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/22395" target="_blank">📅 23:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پرتاب۳ موشک از سیریک سمت تنگه ( رادار ندارن موش کور شدن ول میدن )
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22394" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدای انفجار از تنگه ، امشب تنگه گیسو گیس کشیه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/22393" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : آنچه سنتکام امروز ، تأیید کرده این است که سپاه پاسداران به سمت
دو ناو آمریکایی
موشک بالستیک شلیک کرده و سنتکام هم می‌گوید
ناو هواپیمابر و یک ناوشکن
موشک‌ها را جاخالی داده‌اند و هیچ نیروی آمریکایی آسیب ندیده است. در واکنش، آمریکا به سه نفتکش ایرانی حمله کرده است. بنابراین رسانه های زرد که به دروغ نوشته‌اند
«جورج واشنگتن به‌دلیل موشک‌های ایرانی عقب‌نشینی کرد»
، اصلا در خبر رسمی
نیامده
کدام ناو بوش یا واشنگتن
وبعد هم اگر
تغییر موقعیت عملیاتی یا دور شدن تاکتیکی ناو از محدوده خطر
انجام شود هم نرمال است ولی سنتکام چیزی‌نگفته است که ناو منطقه را ترک کرده یا به‌دلیل اصابت/ترس از موشک‌ها عقب‌نشینی کرده باشد !!!
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/22392" target="_blank">📅 22:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عضو هیئت‌رئیسه مجلس : هم اکنون احتمال حمله به اسرائیل هم وجود دارد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/22391" target="_blank">📅 22:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22390" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار با افتخار عرزشی سوز ترین چنل تلگرام
🙌🏾
😁
💥
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/22389" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromUTA</strong></div>
<div class="tg-text">یاشار  ناموسا سگ میرینه بهت؟</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22388" target="_blank">📅 21:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=ikIE396l2RLeLUlIILw5A1IjplLKlcjp0_L_1FWihQ99yiXsOPoDP6eLYSfeE3wYQGQ1s5MXFSep3DM6MjOlzfXophsxxltirWFLqdpO_YAjyGO9FaZfz7SsIZKVSlE8NJukcofreoW9WPl4vhhWrrjQX6ukLraQm70X6z4_nLUZXkO8OB8OZB_qc4TOAXhZmq8M-R4dqcngnY42xQgqablWssb3TWQpnZRmCzepYD8sADXRew70iSZRJfD-J7DtxtBDMLduTBCBsb2PIRrbg3oe0mJiFeo6nyfJQMfECrSyTmMKFj_zKdg3cKuHlcanbyMfSdTGY7KGAAeLVPd4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df0e56e21.mp4?token=ikIE396l2RLeLUlIILw5A1IjplLKlcjp0_L_1FWihQ99yiXsOPoDP6eLYSfeE3wYQGQ1s5MXFSep3DM6MjOlzfXophsxxltirWFLqdpO_YAjyGO9FaZfz7SsIZKVSlE8NJukcofreoW9WPl4vhhWrrjQX6ukLraQm70X6z4_nLUZXkO8OB8OZB_qc4TOAXhZmq8M-R4dqcngnY42xQgqablWssb3TWQpnZRmCzepYD8sADXRew70iSZRJfD-J7DtxtBDMLduTBCBsb2PIRrbg3oe0mJiFeo6nyfJQMfECrSyTmMKFj_zKdg3cKuHlcanbyMfSdTGY7KGAAeLVPd4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
تنبیه</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/22387" target="_blank">📅 21:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸ @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22386" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قرارگاه خاتم‌ :جون مادرتون نزنین
قرارگاه مرکزی خاتم‌الانبیا: به ارتش آمریکا هشدار داده می‌شود که در صورت ادامه اقدامات خصمانه، ایجاد ناامنی، مزاحمت برای کشتی‌های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی علیه شناورهای نظامی آمریکا در منطقه شدیدتر از گذشته خواهد بود و امکان گسترش دامنه آن نیز وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22385" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=sDcna_qtk5eE28oVH6xfyYJ1KglobwxioXhActvE9C7l_0E29_vYK3Jc_fu2ort0Esb2uI85OGgeLx8AK2v8RI1xeNzwoxzKTfsUK4kiOcC-2ZQ-kEi7Yk-Vu-7fOtUjCf8fVeRj0xV809_GmwiCp-M1sZuJ0y390tIEG5vVcpiDDGSHzPWaQNPXdUO-Zq4H3vMwTy89Z8bZlcfq8MSNKMM-zpoMrymjLJQglYOn3MVi6se6A74v1omsdP8ZjhM1gC_rimqlTUozQGkG6thWnc2zfhwfGIm5UKnwn5N9Fnfd8fOzMBtLevTBkGF05pZmC2ykh-WTxuQ0nxLvJF6JKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d6f60dbf.mp4?token=sDcna_qtk5eE28oVH6xfyYJ1KglobwxioXhActvE9C7l_0E29_vYK3Jc_fu2ort0Esb2uI85OGgeLx8AK2v8RI1xeNzwoxzKTfsUK4kiOcC-2ZQ-kEi7Yk-Vu-7fOtUjCf8fVeRj0xV809_GmwiCp-M1sZuJ0y390tIEG5vVcpiDDGSHzPWaQNPXdUO-Zq4H3vMwTy89Z8bZlcfq8MSNKMM-zpoMrymjLJQglYOn3MVi6se6A74v1omsdP8ZjhM1gC_rimqlTUozQGkG6thWnc2zfhwfGIm5UKnwn5N9Fnfd8fOzMBtLevTBkGF05pZmC2ykh-WTxuQ0nxLvJF6JKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین، نشست خود را با ویتکوف و کوشنر، نماینده ویژه ایالات متحده، آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22384" target="_blank">📅 20:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUD69BgQCA49XuP61cAGyBc0WQlI-I_RdIUd9C05P3N_AKiZCmOwk_I-1MdqgbicHsgHgBjxm6cn7h5YRZSlTsOZrIdJlyek8pE8FC-dh_JoEjHSii_TM5_-LKqS9Sa2-92VHSb0JRSf1wWx4nTixb28IM90D0nYGEYbUpgXXvaDK0n6BhZFucx2EUj2Krww1FHsYZ8o56gd5WCg10PR-J0GMC3vngkfBFvqOFdx1B4M5LejfInOCV6jWZuJhT7UZFQ53oBeEE7o7G2tb4qJ-XTgHvzls9BUj4a3etLvzesAb4GUmP7KBgwMe83q3FAqL5_MTM_BVFXDbVRqQZyG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=FPYb_Uir_KNxgeajpqVUnS4TxCnJN_CzuXq7GvWl7bbsp5kJvX50DE7Z4jWIJzRkR_zIXQpIjI8O4_zwxi5T_MMEP5x0LYCjffvdnNbVGniqtiPK9TX2DwBrKEJte4NLlYI1UxpgB-pAL8i-5Qa4i0DasE7vuwW5--PUKfFysODnj8qs55a0AhnkgU14b14O7MBfdBagf_aF694GTAMIA98029hz7w6gl41uj3N0Ws1leEKr8q2Tpyad5ZhaoCL86ZbdkVw7DkZtt2l1-Ca5wykMbkZyEL_CsAqKAJiFQ03O2owwzyH9Wl0iUTrnrjS1_wTfloUP3d9znfyawZjWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78ca28583e.mp4?token=FPYb_Uir_KNxgeajpqVUnS4TxCnJN_CzuXq7GvWl7bbsp5kJvX50DE7Z4jWIJzRkR_zIXQpIjI8O4_zwxi5T_MMEP5x0LYCjffvdnNbVGniqtiPK9TX2DwBrKEJte4NLlYI1UxpgB-pAL8i-5Qa4i0DasE7vuwW5--PUKfFysODnj8qs55a0AhnkgU14b14O7MBfdBagf_aF694GTAMIA98029hz7w6gl41uj3N0Ws1leEKr8q2Tpyad5ZhaoCL86ZbdkVw7DkZtt2l1-Ca5wykMbkZyEL_CsAqKAJiFQ03O2owwzyH9Wl0iUTrnrjS1_wTfloUP3d9znfyawZjWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7 نفر زنده زنده سوختن و جونشون رو از دست دادن...
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22382" target="_blank">📅 20:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش صدای دو انفجار قشم از سمت تنگه ، ۲۰:۰۷ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22381" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با یاشار : با وجود ادامه درگیری ایران و آمریکا ولی هم‌زمانی با
مذاکرات صلح روسیه و اوکراین و آتش‌بس سه‌روزه میان دو طرف، بیت‌کوین هم‌اکنون از ۸۰ هزار دلار عبور کرده است.
در صورت موفقیت مذاکرات و اعلام پایان جنگ روسیه و اوکراین، کاهش ریسک‌های ژئوپلیتیکی و افزایش اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک می‌تواند موج تازه‌ای در بازار ایجاد کند؛ به‌گونه‌ای که
عبور بیت‌کوین از ۱۰۰ هزار دلار نیز می‌تواند به یکی از سناریوهای جدی بازار تبدیل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22380" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=SGGHrc_WfDhbpD28oRiUt2ddL8x2HpquXnXhXSfL7Ygk_HfFeaOZmjFO44HBui6WOUkXJpALUQ9pwtnjR3Jufkj4K3M_LYzVApcusddklRFHi3__rtrqmxNt2AldogA0iSNnoRLLnVPP_iLf7ITS60I4lMRJFS8WDVT0PIeytaQE5nGaj62GkCrOkLTBJA3kRa7euHNjylI69cOnkB7QT4l_h4vUHqfAsrqF7y7YGLeP7o5SLomeVNWMT1GJEoMrByv9JLr8fzLvdPGfPu6UUdS8m4HEhbsVCwZgOy1503rKYEgfztfuGhc-OhhP7IvP7b5H_q7yMjVjnH_ZPcoON5jZnu7R3juinSyBagBmemQMLODRMLCV4p2VnjeW2A3pOqxAGP3Pm34Fcf8GkNJzGQdgPRYzLDn-PdEw4F185JeO9xfD8ezy43z2m8sBz9So736tPpYi8-B9TAZEri24ZrCvu5QSg8nS6NVxUC7x0up7bDU8L4jtheATQH6xyrY8nav7LdG6VJ05c-nFWw_Y1MSMRpT6NQDs7aVLZyO8fMVHp2FEiS99cgd5BUvnNpa6QgcVVr14Y_JT6WedWF0fVlLgsp-ek24cm8zBrrqIcf8qR3gPuza5JleHAtbz0oOP4DSlCo42ATmsHO10ArBRAPKhV_yOzFaoysjwbq9rkA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83eb31b467.mp4?token=SGGHrc_WfDhbpD28oRiUt2ddL8x2HpquXnXhXSfL7Ygk_HfFeaOZmjFO44HBui6WOUkXJpALUQ9pwtnjR3Jufkj4K3M_LYzVApcusddklRFHi3__rtrqmxNt2AldogA0iSNnoRLLnVPP_iLf7ITS60I4lMRJFS8WDVT0PIeytaQE5nGaj62GkCrOkLTBJA3kRa7euHNjylI69cOnkB7QT4l_h4vUHqfAsrqF7y7YGLeP7o5SLomeVNWMT1GJEoMrByv9JLr8fzLvdPGfPu6UUdS8m4HEhbsVCwZgOy1503rKYEgfztfuGhc-OhhP7IvP7b5H_q7yMjVjnH_ZPcoON5jZnu7R3juinSyBagBmemQMLODRMLCV4p2VnjeW2A3pOqxAGP3Pm34Fcf8GkNJzGQdgPRYzLDn-PdEw4F185JeO9xfD8ezy43z2m8sBz9So736tPpYi8-B9TAZEri24ZrCvu5QSg8nS6NVxUC7x0up7bDU8L4jtheATQH6xyrY8nav7LdG6VJ05c-nFWw_Y1MSMRpT6NQDs7aVLZyO8fMVHp2FEiS99cgd5BUvnNpa6QgcVVr14Y_JT6WedWF0fVlLgsp-ek24cm8zBrrqIcf8qR3gPuza5JleHAtbz0oOP4DSlCo42ATmsHO10ArBRAPKhV_yOzFaoysjwbq9rkA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ویدیویی که امروز از بنیامین نتانیاهو در شبکه‌های اجتماعی منتشر شده، در واقع مربوط به
سال ۲۰۲۰ و دوران کرونا
است. نتانیاهو در این موزیک‌ویدیو در کنار
عدن بن زِکِن (Eden Ben Zaken)
، خواننده مشهور اسرائیلی، آهنگ
«یش بی آهاوا» (Yesh Bi Ahava)
را اجرا می‌کند. این ویدیو با هدف
جمع‌آوری کمک برای سالمندان نیازمند و مقابله با تنهایی آنها در دوران قرنطینه کرونا
منتشر شده بود.
@WarRoom
😁
یاشار : باید یه فیت باهاش بدم بعد از جنگ</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22379" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش ۲ انفجار جدید جاسک رأس ساعت ۸
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22378" target="_blank">📅 20:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22377" target="_blank">📅 20:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سخنگوی سابق مجلس: پیش نویس قطعنامه جدید آژانس، کد رمز برای حمله مجدد به مراکز هسته ای ایران است. ترامپ اعلام کرد ممکن است خیلی زود به کوه کلنگ حمله کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22376" target="_blank">📅 19:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزیر جنگ آمریکا: اگر ایران به کشتی‌های آمریکایی شلیک کند، ما ناوگان حامل نفت ایران را که فاقد تجهیزات دفاعی است، نابود خواهیم کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22375" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIkri_t6z9Htupkk99_AgC2l1xYmbecAy_Ks4dMvGU-HysNCImH2DTIF6GMczq1gxAskGPkVNwuJgFsp8zF1i8yLvRppf_Ew_TGd6cWN9qpEru8Q7H8QqOe3k9XtG__r9s_iCUaL2bbwG-q-JyXj9sDDPJaahKtj-AxqNG-NIzTyckbSLNmqTFfZAP9fbKhK2UM8DtjCDVRaph06Kx3BvNHP2HohXkC4e4ildVmvXCOAGMMqiBt-GNsIUA9h8VgWjb9ZNc5JvL7cTK-gAFDJlIugPfGF_GhZwoL10w1ihkI5Amvnnii5E1wwY7q3yo1L0ArKTvJipyWy3VL-NDamkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22374" target="_blank">📅 19:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : در عملیات‌های طولانی بر فراز خلیج فارس، به‌ویژه در مأموریت‌های مرتبط با ایران، استفاده از هواپیماهای سوخت‌رسان اهمیت زیادی دارد؛ زیرا جنگنده‌ها می‌توانند بدون بازگشت به پایگاه، با
سوخت‌گیری هوایی ساعت‌ها در منطقه عملیاتی باقی بمانند
. این روش علاوه بر افزایش زمان ماندگاری در آسمان، نیاز به فرود و برخاست مجدد را کاهش می‌دهد؛ چرخه‌هایی که فشار قابل‌توجهی بر سازه و ارابه فرود هواپیما وارد می‌کنند. همچنین بازگشت مکرر به پایگاه‌های منطقه‌ای می‌تواند زمان‌بر و پرریسک باشد؛ به‌ویژه در شرایطی که
موقعیت پایگاه‌های مورد استفاده افشا شود و این پایگاه‌ها در معرض حملات موشکی و پهپادی قرار بگیرند
. از طرفی، جنگنده با سوخت‌گیری هوایی وابستگی کمتری به یک پایگاه مشخص دارد و می‌تواند
مسیر و مدت مأموریت خود را با توجه به شرایط لحظه‌ای تغییر دهد
. به همین دلیل، تانکرهای سوخت‌رسان نقش مهمی در حفظ
حضور مستمر، انعطاف‌پذیر و ایمن‌تر جنگنده‌ها در منطقه
دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22373" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروهای سنتکام نفتکش M/T Downy در نزدیکی جزیره خارگ و نفتکش M/T Stark 1 در نزدیکی جاسک را به‌طور دائمی از کار انداختند. همچنین نیروهای آمریکایی نفتکش خالی M/T Kylo، معروف به «Noxen»، را در دریای عمان به‌طور کامل منهدم کردند؛ این نفتکش پس از آن هدف قرار گرفت…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22372" target="_blank">📅 18:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22371">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyftcaYrdZi7hMiaQhovBhK9haHZaHVYgXdLJGVfx6Wu2-8mRmGDj9bCn5vVstV0LLkYO74a7cfo-7oD-SfPU6wN7aW0O9ULA70i16g5BkPP4h7aWwgyRNTEY0fv1nlJXsdAuq7CNoy4MbH8Mm-ZzSJK4iZ7PMzMpbp5DI3W8CyiTk1fUSzAI6Ym3KL9TI5HcemzbLij2v8DGUfUWlUW2mVzLo53iysJRuWkQ-7XukzRgQWysmxmKHkE2f02HJkDyHWof9p0fLQmygR8Z9Sp2proU5-RUZDPZ-fFhXoTOzcMBC1QnKXGbevhbick0YK5jdcvCI3TY95olwVEBzZS2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم ! @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22371" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ززززدن گزارش های زیاد از صدای انفجار جدید از خارگ و جاسک
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22370" target="_blank">📅 18:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیدبان اتاق جنگ با یاشار از جنوب خلیج فارس نزدیک تنگه : در همین لحظه سوخترسان آمریکای در حال سوخترسانی‌به دو جنگنده آمریکایی ، چیزی که ما در صفحه مانیتور نمیبینیم !
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22369" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
