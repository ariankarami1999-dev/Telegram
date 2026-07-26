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
<img src="https://cdn4.telesco.pe/file/OX6DepYrEZtE4USHcYdSCC7rfBhVkMRR_uMs6kDD1_Tqd--MvFG5LGXQCOzLCcNHcnym2iAMSSCixByR2TOA1ocrIPqR0e0w9iMzfzWw4hzFnChi1vP7ZYkmtpF5J3jYkfin_TSBJychEPPEZ4HcfQMxx2l_19Yan4NRlY5MNHoGM5zkyF74X8LPf4I6DNixgsHcUuw7cUdLUicdnxAthAMk2ftJbltCBCoMnhClntKXnGmSgMYFFJBYdBYC6tsOCo3x-O1cBalAUsfDfu7mr_lEgnYa9FPt49Az6uR_JCz2AtJ1V08virF4d8XFxTG42GRur_OUiVvnioPi-yr41A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 08:22:00</div>
<hr>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=kH5vKw1OCBuOkkyBl4XvvI_S_xTMHcZC-CGCsGOyi6MjbD-_FIAu-vrH5Wc74c7YYU8dZQMWpUs5dM9A-licfrgNm_A3SiLyf0K-rnjY0VtykVW8ZxIMF2BS-03xtsO4ObhxWA2G_RsbfMDazdRI5LLXT-s6f0vMBeo_qYtjPhORkFqnKqBSb50xc4knpfj2UTsYDhJWVEQxPa5sGsPZy1a4qBLZrer5Om6buA-p3Ovdh2U_g06NxEC4x3CBIXvdJe1621xVlBWqIKD8WCtdRle2iIRslPEzd_MlND6Yk95gcPMXIVBz2uVNX7upXf1m5VaMIVGWnDakbl1sHjUYTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=kH5vKw1OCBuOkkyBl4XvvI_S_xTMHcZC-CGCsGOyi6MjbD-_FIAu-vrH5Wc74c7YYU8dZQMWpUs5dM9A-licfrgNm_A3SiLyf0K-rnjY0VtykVW8ZxIMF2BS-03xtsO4ObhxWA2G_RsbfMDazdRI5LLXT-s6f0vMBeo_qYtjPhORkFqnKqBSb50xc4knpfj2UTsYDhJWVEQxPa5sGsPZy1a4qBLZrer5Om6buA-p3Ovdh2U_g06NxEC4x3CBIXvdJe1621xVlBWqIKD8WCtdRle2iIRslPEzd_MlND6Yk95gcPMXIVBz2uVNX7upXf1m5VaMIVGWnDakbl1sHjUYTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=p3u3E_Bhq-T7rxZ90B8ro-toKqXAZ5LVngHFwm5rMu9IUYAOuR1UedIxjGLXsI77ZR3z_hioOcHaWLm7rr9VkBMl7ufEz0FVZKnQbdswi7zr4pV0FvarJtHseiG-3oQh-cIGlO0tZGymJotnrL_2TViMFS9vD4tBxywDddAaBNeLpfz-7hLmgWSDCSSx5kHCGbNz4g09XxkfM2PGfZHWsoCn72vfBB1ghuepBy2zF1rjUdBGY4y3xG3k_ewWNlBpKxMwhuVg7lcbe_tE7xuDU6NDOavPS7V0um_LO-W4hnqd1ShZeQjBeaKpZuLYWTDAnfuAPoj41z8hmxKR0GKGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=p3u3E_Bhq-T7rxZ90B8ro-toKqXAZ5LVngHFwm5rMu9IUYAOuR1UedIxjGLXsI77ZR3z_hioOcHaWLm7rr9VkBMl7ufEz0FVZKnQbdswi7zr4pV0FvarJtHseiG-3oQh-cIGlO0tZGymJotnrL_2TViMFS9vD4tBxywDddAaBNeLpfz-7hLmgWSDCSSx5kHCGbNz4g09XxkfM2PGfZHWsoCn72vfBB1ghuepBy2zF1rjUdBGY4y3xG3k_ewWNlBpKxMwhuVg7lcbe_tE7xuDU6NDOavPS7V0um_LO-W4hnqd1ShZeQjBeaKpZuLYWTDAnfuAPoj41z8hmxKR0GKGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=R3yKM9_BDlDY7Zd6JRN4t6zp29o1wTNfoe9NW4rJanPA5ZPSf-ZLwelX6NBW6yB7OniU6mBesHsWi47XnJcMUCz1LEa-jnpiLLYsgG4mr80fm0j4Y52AQroiNrSEcexDY2Y-FW5XpRaUsPX-oRRWavW2vMA4Xw00K_POKFhF44HlwlAxMEAXtioL9PxRqa4qZjnjAK44yBEnkURU2UfHV9yrY12kd8edsQPNkwi4sjuAhnqSLwbm8zbAOpGrbKK8NDazgZaAsfOwnqdzKOzuE85Bgi7be1BJ1f2SeraEi13g2OpWtR_1yvpvq1qWXh36ciJCq0OoS-qB2eyaOEvDNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=R3yKM9_BDlDY7Zd6JRN4t6zp29o1wTNfoe9NW4rJanPA5ZPSf-ZLwelX6NBW6yB7OniU6mBesHsWi47XnJcMUCz1LEa-jnpiLLYsgG4mr80fm0j4Y52AQroiNrSEcexDY2Y-FW5XpRaUsPX-oRRWavW2vMA4Xw00K_POKFhF44HlwlAxMEAXtioL9PxRqa4qZjnjAK44yBEnkURU2UfHV9yrY12kd8edsQPNkwi4sjuAhnqSLwbm8zbAOpGrbKK8NDazgZaAsfOwnqdzKOzuE85Bgi7be1BJ1f2SeraEi13g2OpWtR_1yvpvq1qWXh36ciJCq0OoS-qB2eyaOEvDNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqLZIw4aPszHN4hhN5JnJGr14vrVfmyBQakgtL-HqBEUUxIxXiIPSQHmCDcnOQdVm5PLK-EMCvtCu2Wye6o4zdO9Dw8do_O6VI7JAP_CUFHXCTyK8haa67rS39TaUGnRTWL9PCdnwjrn7IiQ31u4qJUbbT0PQTFRchyiRl8B3qh8H0yPqjQFpHzXrBg3cDsbLe2e2b7yT-hyg045AuUE2U5f5RkU1yYE-HDXnk-U3u0-hB8tv4cC_ahSfTXCQeuoDYzznQbZ4YPJxHpZyeJl7kaMiAzlRtclSgzBFqQMApvB7N2wbEcvFwxu3Ja0KH2IAi5En_H0x0kQQLPYRo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyz8KQgG8dyLlA-lOtBtmtNJ15sXU_F_w2osYaNOFrW4mr---7KH2WgfIq01i4mY1DZp_nM-268dGPWcAmlu_YsswMSS6wMNjkoxWPqHIsCQ3-ezMsnzK4KAe1CtCn3Qjjar9xJ7TIn5-KtdsjK2EDaruMjnuRlt-BScjzklI43Gn-WGgl_BiCkwC4b2R97KNbpYLoi9t-bK6Ic_nyj2BTUZkQg62TMP1bK-PqjraY8Y4yATIcoWOK93jIrGY61mTfI4iB2K7BQyRs3Qi6TEZxVs78JhyoUSZQpLrr0_GyACdOLUgFyl47EmEPRZi_FBgpvW9xzk1hp77osAQpd5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=spJIda_Vp38ADUMBdksliQqpfEEiN0ATNkEJZqn5KFeOPVmVFKKz_H64dMALhFjkyyNejlpllxfcukmyRpxlVLBWH3PWZv7FJ1pZB0a9QQuSOxe--zJi_sko5UD7Lnt53lD0wB5jyAg7mjA8ApeCN-CtKTBmgN4U6kKoQZoF5x1wlCJXIVXzQRJEa9bgYaGmcnVxclHkNhMwPRKnmxbLTD5RCOkDaTSwOZ9ww727YXBKgAKjPP6l6xhD1qo4CTXbPz3qNcaBatyr5d2Qos1bqc-pVMLEkvBkzjzXiLDk06varrX56bBQIbep38htWrCxZ8sqvG_imb0yh9DqQRIlfWpylCEeQVy-X-Ex221VXNUUCsqWoVtTpJ1XL6ScaKfYKByHOqATC81agkN5gHSSeJZkcDyJhrI-IfAp8naDhQFms9iOopQn2WsWb_RNpMh-m_oUSQzSlggbo4YIfRzT7LEq1wDVDavxh2b9e6s9t5LJ-BCCI2ajJh4yG90sKYoT1n2LicRsRWHdp3Lv4Ey2tYdlnwzMu8bQswAgcwZleEltDKaHxzz3onfGFvIk7hRAdZvCxcYpC30D15S7Fv0gMfWTBYv_FwLnXziDL_-tgQ-MZSs3m20vz0sK7g-CbDg9vfCOY8NTIxvaZSr4TCkCvg51XqMMt-USdVvfK8uY5do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=spJIda_Vp38ADUMBdksliQqpfEEiN0ATNkEJZqn5KFeOPVmVFKKz_H64dMALhFjkyyNejlpllxfcukmyRpxlVLBWH3PWZv7FJ1pZB0a9QQuSOxe--zJi_sko5UD7Lnt53lD0wB5jyAg7mjA8ApeCN-CtKTBmgN4U6kKoQZoF5x1wlCJXIVXzQRJEa9bgYaGmcnVxclHkNhMwPRKnmxbLTD5RCOkDaTSwOZ9ww727YXBKgAKjPP6l6xhD1qo4CTXbPz3qNcaBatyr5d2Qos1bqc-pVMLEkvBkzjzXiLDk06varrX56bBQIbep38htWrCxZ8sqvG_imb0yh9DqQRIlfWpylCEeQVy-X-Ex221VXNUUCsqWoVtTpJ1XL6ScaKfYKByHOqATC81agkN5gHSSeJZkcDyJhrI-IfAp8naDhQFms9iOopQn2WsWb_RNpMh-m_oUSQzSlggbo4YIfRzT7LEq1wDVDavxh2b9e6s9t5LJ-BCCI2ajJh4yG90sKYoT1n2LicRsRWHdp3Lv4Ey2tYdlnwzMu8bQswAgcwZleEltDKaHxzz3onfGFvIk7hRAdZvCxcYpC30D15S7Fv0gMfWTBYv_FwLnXziDL_-tgQ-MZSs3m20vz0sK7g-CbDg9vfCOY8NTIxvaZSr4TCkCvg51XqMMt-USdVvfK8uY5do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=aD1P5GTQElZgHtmA4fqSAW1aSSPCCAlvKvCSPd0ykOK75xqY7x_BFHSjV2uBd3XQOMIdpo-7r32pWAIT5GmLF_9Ae-SlCyiBqCIKd6ZKxpp-W-xfVzp2I1yPAebGLE-6ybOuYIQiQaDmylry7WOYkSiPIW4xXqXB5Tqv_45e2yY3AaKprCRty6h8JL9Bl543M582ReeP_YmG_wxamOWapZy7fTyZid5SPhnCIzBbEo1LZY2PFdeJDx5y0C_aK3qCspoVM9KyiohX-724_tlDBaU_WJ8JFdiOTUB-Rhs2JbRF7vy8zTE98gvGuagw_ZND1TcLf8jrhhn5RXOYcceWhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=aD1P5GTQElZgHtmA4fqSAW1aSSPCCAlvKvCSPd0ykOK75xqY7x_BFHSjV2uBd3XQOMIdpo-7r32pWAIT5GmLF_9Ae-SlCyiBqCIKd6ZKxpp-W-xfVzp2I1yPAebGLE-6ybOuYIQiQaDmylry7WOYkSiPIW4xXqXB5Tqv_45e2yY3AaKprCRty6h8JL9Bl543M582ReeP_YmG_wxamOWapZy7fTyZid5SPhnCIzBbEo1LZY2PFdeJDx5y0C_aK3qCspoVM9KyiohX-724_tlDBaU_WJ8JFdiOTUB-Rhs2JbRF7vy8zTE98gvGuagw_ZND1TcLf8jrhhn5RXOYcceWhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhUkePIIQi3ZP3LHcl4hVXd8WR2hXcZwEpquIINSvMW6KskkOTo9qgnt_krl3iwQwp21qRY0R6o-gZC92xdx5gel3LWYfCU8UrEQVlrEqHoSkfvI0nxqXAtgXejGfUA8JXReIX_B8k0h-OHuXbVF1t5sT1aNPlWQF3KdcXz0qDOijXIsummurvD_6QkpTL-kgTU0ID1WZj9D-KBZq9OIMVfkFS3UtIdYIFTcpONunxRdmIqwzSpXD0ektJ1a1UACN6MmHMLA5sqO-21UmXOf-zWKPw8miWf_uY6oUt9EEr5X6Udcuuekw2XiF9teqofjofc4DEts_NYLjGUeSD0TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=THx_DgDm8yWoQMVdO93HFAsBkdTAmRplib4FkFOm73wmZzbRp6T3Iwmx9fmjd3hppQV0duQEOE3N98idvL-p1t8HgdSe6qBy9SSvReDDmo_TolgoOZwbZvdGEUNQkGj71YaSSYJDQnBw5gsvs7M2fY52LP97lXpJvj0FGxPBMzB2A0lZ2E0e7yRhfeIeMG6QLwakN5Ast89jCdGina-dUNUbG5rdc4OfB0R1ZPMJFqsCenZlCR9kWoCRALQyGz7iR_0pMmeQPfx12KB_m3FwtHPp3ipkv07rvO14iSxQ1uZF2LP_hkxAw27tYIzgYyCy707e9AeqBJN6i7juWCVZBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=THx_DgDm8yWoQMVdO93HFAsBkdTAmRplib4FkFOm73wmZzbRp6T3Iwmx9fmjd3hppQV0duQEOE3N98idvL-p1t8HgdSe6qBy9SSvReDDmo_TolgoOZwbZvdGEUNQkGj71YaSSYJDQnBw5gsvs7M2fY52LP97lXpJvj0FGxPBMzB2A0lZ2E0e7yRhfeIeMG6QLwakN5Ast89jCdGina-dUNUbG5rdc4OfB0R1ZPMJFqsCenZlCR9kWoCRALQyGz7iR_0pMmeQPfx12KB_m3FwtHPp3ipkv07rvO14iSxQ1uZF2LP_hkxAw27tYIzgYyCy707e9AeqBJN6i7juWCVZBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJnCPX_5JLTYsSkHrsMkoB1cgGk_5SSpCXa6yE23DU2B5ZdYdTmXwEO1ossqPkHzG65qfxU7GrBZ5NKwJuLr1FwwLeyDtoqibQ5dWv0e7__xI1ggHvUq915nNt-Gp8TEnmwpIs7LEBKsj_OHdrYUmeLcXT_ujFtkfxR64VPv2twAb-jyGEO7aXtjgvCKnagIC3DwQyE6OiwlUTCfOgYbFqxpOWi7EBafhrwew5kH_DOnO8M1FPPQGmy_8fJh_ReFNgChWbUR8oxzc-PlIM7_yWyIjzsBd4ikpHvKFTQuaVCwXwFnZ01yO1TeDB0YJ0mkF16eKqTQiCHgH8-m90X1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLT5bDAAPFNH1sl5Vt2V92DOyBbMol6jgLxWky5D6fI8BCYzI7eL1rtW7zFcbPw3ri9cB5LIZnEEtD3IYN2iRZ68YthMzEGQks5ilT3PZLwFmXnmxeVX5HfBP-hWdaAKeLgsOZDW07pxTGb531ksNLxHDJ4LkSPacJ4DVhz6ECBiUSQ8HOkIIAaLwyk44hB47d8kfFhjcwQnRrcZwnMT5lEyEEy1w4FM_q9psfiDnSJD2zA56G-iSnjO-SqB2Px0SQoIMXGvjfgo6fXq6L7m27aN0Y9o4i5cNFiGPojou1QHiQc1_daHboZiw9QKvjKQI8JyJc61P4hYpibsag_SNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEAVzaEeQIf1ma0o7x9JPTU494Ge8TDxhpb2uAlhKXOIaflNGtqr_EEebgkhxJhNMbDaK9WlAKn2oJUkLPIrHEJNeCakjA4Uw7hYeLRlldpp-Psz_osFjHKftPaPxFgM3aFlq100LNmU_PR4KTN0m7jfhzG2BSQGyyPk8DUYanJahYIB3svdAdDXFCS-Ob4bOlPMDScqkT_It2ErMi0CzeRR1Lp-zhhqfUdJ0oC5REC2w1fJDDaQ_xWSCToWURDWPFYV2q_nkydDH50ag-IJgeOWppGgtldYvPVt_fvlRKsU-PKbNrK6Ggyd1rNl8N5ZsaXiEhzpGmkTzY_SDqyYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz58opoHkzQ-yYSUSiSe3M4zAyBAPPfVmiEhE5bwXeGmlfMxyswik1JyPfOdPyraJU6sE4lfFXytaNqzNBFS3ZQZ6tACYcc8d9Ev8_kxenXyregt_xZ3IzARp9Mrrx5gM-BIvXmlkgAE2K8L4QlxYNmvuhYXq9KqhjOomonCAdaUS5KWpGy4YYRxhEYZB6J3Vs7rfjjRboR-ooVKxEmsCVSchsXd27Vh3YIxwVsu3Dkdpd1vXmbbpcmPubFXSaJbPq5kgQOGuA4GNHlPsemNZ1rgyYvED_5yRCv33iz3yZra-WJBxeyJi5awydMve581jTGgHDa0gRSaVqaqEx_jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKtyuovE4UNF24nnnbDXCnUfbANCJLGRKALDcxYs0HXJKaensKLGyZgA7F04sasYSV8i8_bHJnrNpHo0fYBO_l8TIJYUoyCJt0xqMDKVfDgpL5sJi7BgL9KK52q2bD0zFinjcTEENXQ4CIL0um05uNHeCy5HZ1Clr6QwZIRU5D-ClT93gF0vtR85oNJkWXhmD8Z-LcPe2IuGL0Pgny7HlVnYN82ectyAr7hR1BKMV0ogmx_H1knYlr_hbIMIb088pOkxzCDZrjleP-gB7KtqXxdQH4cwmOof2wpubkmVgc8WCRn_skZtvgIjn_GbDfJ9oeFhSNG8mVk0lDNGrnqHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=WzdUGntk_pOPh95zbPLU2ni5Zp3fQmmL1aTJQlS6p-GPfwFQptwPu5sqOFFsr-CR2lKPPhnH979m0i4rmA3p-pdGIk1d4Z1JR5Oua2sZJKlRsmyVrubRzo6quiI-Zzsf3KD2ZcQkjSzZi_EzpPT-_nV0pU66TOLYglLajJItquK22oPfWm7rLnabCwhk5ZD7cl9uAJT38_tCayDhwXmfAgqVMDJcr5fgFnRPDdYG2t_TXCSlMNt52kv5-GQn90c7gqBAc_g2V4bB_UEMqFVh3klwG3WX3r2vFLYaN4qarUPcwdIEuwhLkNFIWWmWjSJKUS2SIQYHeOhyaKcv54pJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=WzdUGntk_pOPh95zbPLU2ni5Zp3fQmmL1aTJQlS6p-GPfwFQptwPu5sqOFFsr-CR2lKPPhnH979m0i4rmA3p-pdGIk1d4Z1JR5Oua2sZJKlRsmyVrubRzo6quiI-Zzsf3KD2ZcQkjSzZi_EzpPT-_nV0pU66TOLYglLajJItquK22oPfWm7rLnabCwhk5ZD7cl9uAJT38_tCayDhwXmfAgqVMDJcr5fgFnRPDdYG2t_TXCSlMNt52kv5-GQn90c7gqBAc_g2V4bB_UEMqFVh3klwG3WX3r2vFLYaN4qarUPcwdIEuwhLkNFIWWmWjSJKUS2SIQYHeOhyaKcv54pJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU9Kj_Hj1X6ZqTn4dC9pa-MwZoPY3s78MZY2W6btAECjCLJIlGVSDHYvPZxwwS8m4HqNoQBRFQ0zS65XwvFpTjN0XJ-zrvw2YBli5_tIgA_o1FAbUZKRiFan-84w8XjsupIbYcDpkNQUn6EzsZxqiJlVBbwjc1n5xCsz8v1un5Pewk47_rRc3_Wh7ToOk40Oewa4FYWW-_q6xhCdlKL__r23HUhJr0URuRQlxfpcM6Mz3a3f7ebWU_EVHPdOvpuIOOEUpkfwD65dXraBGxwT53B71Y_o5eFE2wTQnEZeXDO6Wb0kz6y9rxaHKWu5uDvMyYInCGCs_Xco1eesserhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHvs5du_WOyl8MVfinHA1zpVAgg9OM3q2vudw4-rEIApU6kl3bap6X6TNm6NvhXQOtWmbP7aYGzmfIJ7iw3bPMOuil69dF8oic6oc623Y4n6FWF-DcajwG59UySFAtt_J5JDyx9QXeUljSL-MhQwG9LsyVdSMTKqAnRUQBNr6dG-pZvDgYPEJYHRBP4UalFVaaP9SmcjFYWPoWSNVyAjA8wF9w15x55MWQ_MpQ6_aR6aIl0eZ89qm_gB5FuxUctdXn7IwT3X857FS7PSyYecDEKjkYF2CnLw0Tu1hfGNWgPmh6qqma8z-h5jQo9PH-jF8a7k3-nwA5g9uitGEDhZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gC08LVgormfdhURsd5FQv_mgDhxJVgS6zjao5iy_T4OhHTPP7XtZlFL4GduO2lrOLpj0fGub75zKBwqBg9rGmpyJGxCY8kAgACeEGjmpVRvgJttYailDfsHd3glKv6Ocz3zj-ZTq0_yFB7KrmnENQdTAHIWniZhm2mA2AQRstIhLnHqPN3mHf12zOXJkwOgZze3yPNsW005pKTQLMDdj0CwDa8Y7R7ja43GpYOK1NhTaF45Qv4ooyZbtweNqOcsyfSmrormPPyzR9rLBlv6TDkZNOyr_4swA7TdJpGYZSw7nF8ochY6D5bsvRijVzeqCRzUHukfACA_Pif5mekfzYRkWYBTh3JA0Wed0uImewUcRv5OD3Fc7ciqOJTUD2Z5X99D56j6eokF8rUG7ccO9HTT5kU9hqOmQFJFN93VTLcaAmGplQXCI7bITQg4HlGzYmUuAZMFH1UjfDo3P9FRXlP6jL5Yu7EKgVbf-pNkyupUDkSgsb9pdhSGdVu566tjczO9Cm6xrfKNJyoNSryGpRF-LAB_yS4AJ8O66Do2TWM2U0J9KYcOF0FsuJ2hIqNjbfzIOVUfLQ7jZGq4zaKU5NVCkt5GNSLABzThS14bfAShmTpbTrIRVRkGVQrZPgeMJSyAGxJu8NYJ-P2O9PQBwfH-XnoJqvt3oVsaUGyJ2_cM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=gC08LVgormfdhURsd5FQv_mgDhxJVgS6zjao5iy_T4OhHTPP7XtZlFL4GduO2lrOLpj0fGub75zKBwqBg9rGmpyJGxCY8kAgACeEGjmpVRvgJttYailDfsHd3glKv6Ocz3zj-ZTq0_yFB7KrmnENQdTAHIWniZhm2mA2AQRstIhLnHqPN3mHf12zOXJkwOgZze3yPNsW005pKTQLMDdj0CwDa8Y7R7ja43GpYOK1NhTaF45Qv4ooyZbtweNqOcsyfSmrormPPyzR9rLBlv6TDkZNOyr_4swA7TdJpGYZSw7nF8ochY6D5bsvRijVzeqCRzUHukfACA_Pif5mekfzYRkWYBTh3JA0Wed0uImewUcRv5OD3Fc7ciqOJTUD2Z5X99D56j6eokF8rUG7ccO9HTT5kU9hqOmQFJFN93VTLcaAmGplQXCI7bITQg4HlGzYmUuAZMFH1UjfDo3P9FRXlP6jL5Yu7EKgVbf-pNkyupUDkSgsb9pdhSGdVu566tjczO9Cm6xrfKNJyoNSryGpRF-LAB_yS4AJ8O66Do2TWM2U0J9KYcOF0FsuJ2hIqNjbfzIOVUfLQ7jZGq4zaKU5NVCkt5GNSLABzThS14bfAShmTpbTrIRVRkGVQrZPgeMJSyAGxJu8NYJ-P2O9PQBwfH-XnoJqvt3oVsaUGyJ2_cM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=nnvw2QECxJdaIKmUDi_P6vQJZA7tysKQqev8_R5it75U607QgVu90jT1I97LvUyMwTZRGJE_c4Qb5Uw6v2tcSXnIUErFRmewMpvcyj3b7_P2e7PE3rky0UExwNWPHoSNx8lIfMRdoN2WuiqYkADXFwPNSkwcQBzKH3-RIL4GGTY0934uUIyKyDFvCHu7UgdgKemR_kYIL6jHZex0xSUHh7blaPbFx5FLes3QR0FcdQPTEqpTwDdF9ac4yAlV8Mjy_tWcRJaNIrsNnO4A3aaj8T_XCZduVuGmw27R8hjykPQ1HfwWhEaciSrTTddiMKdQkg7F_ypF3byu4GjPoamedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=nnvw2QECxJdaIKmUDi_P6vQJZA7tysKQqev8_R5it75U607QgVu90jT1I97LvUyMwTZRGJE_c4Qb5Uw6v2tcSXnIUErFRmewMpvcyj3b7_P2e7PE3rky0UExwNWPHoSNx8lIfMRdoN2WuiqYkADXFwPNSkwcQBzKH3-RIL4GGTY0934uUIyKyDFvCHu7UgdgKemR_kYIL6jHZex0xSUHh7blaPbFx5FLes3QR0FcdQPTEqpTwDdF9ac4yAlV8Mjy_tWcRJaNIrsNnO4A3aaj8T_XCZduVuGmw27R8hjykPQ1HfwWhEaciSrTTddiMKdQkg7F_ypF3byu4GjPoamedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JInk6dY4m9DcCNELLu_NS-EW830s0GHPKDwM4Nra0OJotMC40kmNGk7kc_1KfL2AVNqqsJExwkqqiZ6CSQObAaXa-6TkJZorIB4IiF-dLktzv7BjxrDsEXgEeGjPlIh-l3ZF-IX32KOMsQlebx52_IluI5cRF9xKMeSLfVVaCS42spR-YHszRuPy8B3o8MX_N_7EqZSvEymJO6RM6SF_o5dd5kgX-lJ7GuFAB4Y5tr7A4-2F9p_f_qb0_NC_6-6WRysd-CO4oYsSLJnUl91u-Z_WdQPwN3JGL5_41ZsjkJoxb9bTUw5BJy7XVBoRMpya7wZppXkM-6agS61_9_O4ZI5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JInk6dY4m9DcCNELLu_NS-EW830s0GHPKDwM4Nra0OJotMC40kmNGk7kc_1KfL2AVNqqsJExwkqqiZ6CSQObAaXa-6TkJZorIB4IiF-dLktzv7BjxrDsEXgEeGjPlIh-l3ZF-IX32KOMsQlebx52_IluI5cRF9xKMeSLfVVaCS42spR-YHszRuPy8B3o8MX_N_7EqZSvEymJO6RM6SF_o5dd5kgX-lJ7GuFAB4Y5tr7A4-2F9p_f_qb0_NC_6-6WRysd-CO4oYsSLJnUl91u-Z_WdQPwN3JGL5_41ZsjkJoxb9bTUw5BJy7XVBoRMpya7wZppXkM-6agS61_9_O4ZI5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTJsCvjjpxdco2PgtZsIubnpSn7Ex72dXiiItR-Zeo7urSAYggeAxrS4nfAT-3TKC5w44qKLXfR14_l3nHp3NTuNfRyVWWL25iPEVK170dDdv1qR-CVgA4yAqTXli7Uevw_BD10mQjMySzyCOQFillExo06kQG7er-amG4DyWLXZlEveEeSlcto0mB9vLnlM0OcenfUbkcEB651NtLxCf4DVtTfbGe3WstbZSnhggncTfUgppaJ03dfDLRtlASu0Yw1HhiN6qCTUf8_P-DffoJBYZ-y4EgW5w_xDqme-Kv2wAMuRue3rW8iuYhp8DSYyYNF1qG9iyJi4ViJYIuzEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9-03EjLnyp3-gcaQ5vYfjiKqtzglpfzIdcP3nPpLoKiPhx1RibUQ0EwF7X1ge6O8prGAnHMxzG1-eJW6W8FA2sgvRYhrT_VUJjYI7cj34yY014BWbZscjlJZaLqgDcWdjobRyr15FjieZppjZkZMwS_NIjSnGqM5mYoG-Tcx4x4QsbhjSzmgt-rz9m-z6WIPFjcHaU44h5xCJpirWMoS4VzFOHtBGgfGYKbbutWJOUv6XW6GXyq0S0GTJCs1me6gL7golayXt1Xe4okbRQNaJLIaK2R0ftALTL3u5DBjdVFxWuYQTFjMaT-tkMe_x7Qu98srzc8AMr1pwGCFFKFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA84OcUi0tOCs4D31hB654Huxw_IxBuQO7z217LzFy8Aa3RBytPNe17JK0vpJu0eLICcqsfrWLq0uwYozmkk9XfMOUCthHuGr-J_Bwm00it6Z7NW7pkG_zJ0S9GJuztS-ejxSEN_ZNXdVMroIa_EoIouN8O3ytbrZb0pCqSqusPbIDG4XOa6WDyPd5lwyvJz0PIBMqa1ziPhmIlziM6HAZf1OYBajRgb75N2fXwJ-7hXN8SIiGY4yxEd48qb7e_c--JUYmqAykQDJi4ts7GViIqBLUD0_uqA7hN96xTmiNo4j4JWTsdBTFP3FHT077PFR6Y1LxuasccGk19YVoUgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=RscTwUCIp6a24o3KRsDP_2_ysCnnvYee2S41Tn9marGia-INip6qQ41WVafmtPGOKJIhxoOZeQVx9jv3jJqBVI2-eqa7UQmi1vzZXUrbZXoY_ZRpbmOulkP9AsJviqq9lyF25dG19TFwps6oRadMsQLJP42Xy65mnsTkJOQ90ScIaZ3JbGhpoZxunekk_cgNogS9lMjMOHbPk7H_EBKefFHvOIcVqPdOfB-gnZCm3HzaBtqiFQsO893cwIfZ3r5O5WDffuR0hrfGz3VjHDF7gq2ZlDa_zGd14H6tPHw9-lv61agcxHAa9WdZOnkLihz_FkvFbyHMDhV2m8A00NsN1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=RscTwUCIp6a24o3KRsDP_2_ysCnnvYee2S41Tn9marGia-INip6qQ41WVafmtPGOKJIhxoOZeQVx9jv3jJqBVI2-eqa7UQmi1vzZXUrbZXoY_ZRpbmOulkP9AsJviqq9lyF25dG19TFwps6oRadMsQLJP42Xy65mnsTkJOQ90ScIaZ3JbGhpoZxunekk_cgNogS9lMjMOHbPk7H_EBKefFHvOIcVqPdOfB-gnZCm3HzaBtqiFQsO893cwIfZ3r5O5WDffuR0hrfGz3VjHDF7gq2ZlDa_zGd14H6tPHw9-lv61agcxHAa9WdZOnkLihz_FkvFbyHMDhV2m8A00NsN1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so4TpRZmvon7VU_y-slZtghFkSKGqAaWc2bol2VsQ8hdKq69iX9WnrnJ_GkPyYg0_f_5xdjpmyy-zIWDIKCkjBp9I7rHt9qk4syirHC5WRGPNUluSoF-mcJsUoE5cgXrstjIDUvJK3gAdFVvpwtovzYQPwD65Q5Owe2Fdlm0jhVGv3hYZIWSaVzSvZWqkoVFK5pX3SVkSzv6ZAq6CQ4655Ufv0n4KQjQMeGhViiK72F5SMKeCqbTC0zCxM434dsHfnM6YVp12h7NkiSXtNaAMCVLe-jwHAXwZswSiYIYA2lTY-dQfNkkJPWXYlEG7UzXvpSHebRIpfd3m9tEgRfZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u814DjZm3P7m9h4lHWLRr6qdAdqqIWYAUy4xF9JwTKaGkN7RBQRN3ZaFyUWELSW5JQK-4NfRpi1E_OHtLgwLOXiaJUCyk6z0p2ijk3GqVRlh_ni1ZGZ9Vd0RGkFfF0glCQHmJvabJh3miYdAu-2x0FzE7ky7gaJF7gnGZV43fS7UZaKUD2-R4OMCDPGUZDLXFW6bE4QoJdZjZn4yCXizQFZvIw22u0LYtmLS7Gj5IPO1akx2sQtEu5g1F4uV38SHOBThZYDtz4Mwj7FNf91qU14k2fHcIQvro0MypSDQudchzu-nL0QCIkMWnHA1BEpsyv5JV1ORMte3G__hgAhSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4k3YLd7bdwj0_rV9yTmX7K6x2EVkH2BVoltCaJg3h99eJzx5eKiX_dZRMCbnN98auaugXL8V6NXrrtLHxAbHR6IlXKeR1a3xH8CTLLicJQzUo8FITnxMgjasfbpJjyGoylRmwGF6uKpECua43aTnne82T4REUMm_lHDORM-wsITne7UZ75JwGdglCIzUOh_NrvY20jxSJ0qPhyzBoG11FD_K_0F2SrW1fwduOinpx0cq84XYRYpIQvrw0s6XRpxGChoguBrBAi72iQDxLRwazgGP1xwfMvwLzChUoWSLPU8kir7sDnJLoZ13BqeXGHEiAaRd_HZjepAgycu8eva0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw5N6bC0KaLJO9bE0ZFQwXkxS98sJeTkver2sWertinzJNhNMF_F2EAMyMmgIkcCtrIDfZkbuXruptueydzcch11PsJsxYy8zh7j2E_FlPCZy-7AyuuOfT59ENXVJphsuT4ARQtdLTdP_yWHYOcA1AGUL33449cQDq4p1ISoDRJBEi1TnvNQMGZJWtZKPNNPCxk2OGN7CmweGdPADGAE4nnPKUQf3SueEfN8VAy-E9BjVyE2ASKOSp0nvmTB9T0Ncxf-RCaaJndh0viZA_jN3JA_E_j2ZddBKHl52lUnjzjZV1rohmAaQXJYPyhDZr1HlREJ3iWvYjP6DGPObup5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Ufkj3TnREjk0gWZhlEl5D1LZZRI99VnqpzkdQaQFi3lxkAZkssrazXNm7gEbun2KygYJ-cB66mkoeO5w4KoAdYc-pXYu5Dg4sP8CYfZCL6yDkaEe7VrcZP_3dOO8HzWbjSacJoG7e5giBZT18psOT1SNskYyAji6JdKy8ZjWCqL5KTgCY-TQomFxLQ-O6d0nAWxOipKqsUz2HuYSx5jXQ7bF7OOshcM1WCVR6aKRC5u6trPNXnzWzJtiJvI101EHh0jANDPs8OVKt4TNFe8mGvaokpWtKYEtURmZozvqdZBbQNU57UkM0krdH0H16tIKR4L8IIeqrTR41XW7MYg6MIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=Ufkj3TnREjk0gWZhlEl5D1LZZRI99VnqpzkdQaQFi3lxkAZkssrazXNm7gEbun2KygYJ-cB66mkoeO5w4KoAdYc-pXYu5Dg4sP8CYfZCL6yDkaEe7VrcZP_3dOO8HzWbjSacJoG7e5giBZT18psOT1SNskYyAji6JdKy8ZjWCqL5KTgCY-TQomFxLQ-O6d0nAWxOipKqsUz2HuYSx5jXQ7bF7OOshcM1WCVR6aKRC5u6trPNXnzWzJtiJvI101EHh0jANDPs8OVKt4TNFe8mGvaokpWtKYEtURmZozvqdZBbQNU57UkM0krdH0H16tIKR4L8IIeqrTR41XW7MYg6MIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ASfka0zBP4BWXreUikIW9uHrGfuTD06cK9puz4zN2cV7cIFJRNN3BbtXDw_4ZQ-GfdSfWLundGj6M9lG9EHPpRttgulq1r_cRulsg5XjKvWFBAj7eFGumy1BXR2oHfqFGyktuqk2JdBzDOTMj7pejJc-oRFTSNkkYdym0SPgbL9nPijZlzNnKFKjivjBeOwiXrV-3TAoxcTM4-KB8OOkks_YZh5wKcKKOZF21Gsk-1a9t5JBl5xm89LI_GjbeU-ctmUss3as9hbJnz62v_PEjv9naILw_leqeQw5uU1o7Aaf3acW-DjESE5u1phAx0SowORswti7YaSCcpVN5pKv_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=ASfka0zBP4BWXreUikIW9uHrGfuTD06cK9puz4zN2cV7cIFJRNN3BbtXDw_4ZQ-GfdSfWLundGj6M9lG9EHPpRttgulq1r_cRulsg5XjKvWFBAj7eFGumy1BXR2oHfqFGyktuqk2JdBzDOTMj7pejJc-oRFTSNkkYdym0SPgbL9nPijZlzNnKFKjivjBeOwiXrV-3TAoxcTM4-KB8OOkks_YZh5wKcKKOZF21Gsk-1a9t5JBl5xm89LI_GjbeU-ctmUss3as9hbJnz62v_PEjv9naILw_leqeQw5uU1o7Aaf3acW-DjESE5u1phAx0SowORswti7YaSCcpVN5pKv_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CxAucCUmQn4kEHTse5pS-WxehPSOCv7D6fJCtmpA8RqRLDlviHwi9Vz4E6B1VMJQ9E3gdvAPG17YuKSvViItS_XuxuU7HzvKlJoanv0amR9P028oNJVQenUe1O3GlfhMQXcncWlYR1CLP7ZwLcuN7_dbISK52ZCRWIYhbjg0djIJyNzto64h3ltHMDqzhwEeS_pr5DSacM8Sk7tbLfT_LJjtoT24ImMQrVA5SKY91TkvswNY8nrCPhtVhmm83Rbfttwu-wzo8ojL8nBt6x4ag9Rzr9FCm65yAg7_Sh6DR-T4srTf-3EhJyaHB4ZxWYjqp2eAXPeRvXW7cA6tA4BrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CxAucCUmQn4kEHTse5pS-WxehPSOCv7D6fJCtmpA8RqRLDlviHwi9Vz4E6B1VMJQ9E3gdvAPG17YuKSvViItS_XuxuU7HzvKlJoanv0amR9P028oNJVQenUe1O3GlfhMQXcncWlYR1CLP7ZwLcuN7_dbISK52ZCRWIYhbjg0djIJyNzto64h3ltHMDqzhwEeS_pr5DSacM8Sk7tbLfT_LJjtoT24ImMQrVA5SKY91TkvswNY8nrCPhtVhmm83Rbfttwu-wzo8ojL8nBt6x4ag9Rzr9FCm65yAg7_Sh6DR-T4srTf-3EhJyaHB4ZxWYjqp2eAXPeRvXW7cA6tA4BrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfoaaNDsGDZJtBCJMxC5YSSwBZzLj0BZl1h1jokKIBQdnMT-zuNBvYLc1RH2KMVYEulCflemVycjPBZaE-qqYiCoInjtH45fiDNm-1B_lwROE_0u5GjW9XQpT2c4_RT86NipBk1U6MDB28lnw_ijYJV5SxWAv5MmB7MWHw5wbBAUzEdBvjKTa97M422JVG5jXVR4SmTE21OKoVIeTmf-DaBsxX-MT9vNqn-_aITi0c2XOSv1_d6e1TwQv4DNFAFqRArtF_4djnj47a5F3eBOYPduQT6wWnmOADeB-QJoPAPoQIAouFqY2qox411PiX4TMavLjh8yh7whzEXRAoHblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=GocRZbierA1enocH8hpVdx6QzvCmksJWHP-g_j3UWFUshp2Ue2ll-oegRdxpn_GInqnJ_gP4HMg8rD_QKjQInT9w_Mpqj28FooqYz_JYNfe-Jal0iqMFDqWQ5qdPiwPtfDn_3JDP6JEE57A1gBlfvwM7VR5pQ9jzuDmIN-Yncnq0zP4zfFcxAUKggNFLTF4dkyNyCtIW7L3P9q1SQgSwyLfw-2_u3yvYyl3lE-YBs_hSJMAlD1L87WMLhDxrIxejG8ToKz1M5XLdCJsmiWZAfQ_w-DNcxVTwWZ5KELggwSyVT1qQ2h778bmZyUSBoUmVdm5gpcnKUQlnkj3Nqpl6XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=GocRZbierA1enocH8hpVdx6QzvCmksJWHP-g_j3UWFUshp2Ue2ll-oegRdxpn_GInqnJ_gP4HMg8rD_QKjQInT9w_Mpqj28FooqYz_JYNfe-Jal0iqMFDqWQ5qdPiwPtfDn_3JDP6JEE57A1gBlfvwM7VR5pQ9jzuDmIN-Yncnq0zP4zfFcxAUKggNFLTF4dkyNyCtIW7L3P9q1SQgSwyLfw-2_u3yvYyl3lE-YBs_hSJMAlD1L87WMLhDxrIxejG8ToKz1M5XLdCJsmiWZAfQ_w-DNcxVTwWZ5KELggwSyVT1qQ2h778bmZyUSBoUmVdm5gpcnKUQlnkj3Nqpl6XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Z1ClCg1Tg5hP3VEH8UJFQ7u78_gKn0kclWvoKuICHEV-t9fLiQt3llF3ngUDV5rr06mxnggFsSnoL1QbMOo4D4zLeELWNbcToz931LrSAsF8XDkXc58-Aful5fA9i0YhPUkKoPCFpf8AaeTeH9A_KjD7CYSbeyHcwtSmGUW6_mBB7qvPEWlJkp_3XFVDy8_xRAbVPNWbjd63MEnGGMJAUhodl0f4oIIdWopdVohdmeCLQZrMUoC0w8MP-lvYL5_sFajN0CwWusSHKnns7HjfxOrUxsOEgMBlWe3wMQInaCjG3-orn7Yxa5CpWd7hIxM1bWYO_X0FB1_jvHvC9r99XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=Z1ClCg1Tg5hP3VEH8UJFQ7u78_gKn0kclWvoKuICHEV-t9fLiQt3llF3ngUDV5rr06mxnggFsSnoL1QbMOo4D4zLeELWNbcToz931LrSAsF8XDkXc58-Aful5fA9i0YhPUkKoPCFpf8AaeTeH9A_KjD7CYSbeyHcwtSmGUW6_mBB7qvPEWlJkp_3XFVDy8_xRAbVPNWbjd63MEnGGMJAUhodl0f4oIIdWopdVohdmeCLQZrMUoC0w8MP-lvYL5_sFajN0CwWusSHKnns7HjfxOrUxsOEgMBlWe3wMQInaCjG3-orn7Yxa5CpWd7hIxM1bWYO_X0FB1_jvHvC9r99XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=taUTOl4b7LGgFLIT3uHBnjb49DV7PHrVKXswwGKE572nNoE7OZUhqz5_EFd-LwIQqSx-eRWy-OvTE3zrv5pgeplTd1wlh0rUM1zr0JjFbZcHP81F7Cqsbjs74msNjqN0xstVkls3xpvCeSaPr_vieYxqS_omMbrWQZZsT41pJBaEC2OYb3nQwxCdV7zbrW9HvqqcfX0zQypMhzfbrUIAPS1PFQN6zT-YehADOVhBgIB5upmAUYf9Akc6dmHB2QEA_uoQ9dojXn4rPSO9DhdFdJk5oBb9uvK7fMauHrHtw12WNawvJwbLwGiiBk374VV39Wg60kc9gVDq4v_QIdtLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=taUTOl4b7LGgFLIT3uHBnjb49DV7PHrVKXswwGKE572nNoE7OZUhqz5_EFd-LwIQqSx-eRWy-OvTE3zrv5pgeplTd1wlh0rUM1zr0JjFbZcHP81F7Cqsbjs74msNjqN0xstVkls3xpvCeSaPr_vieYxqS_omMbrWQZZsT41pJBaEC2OYb3nQwxCdV7zbrW9HvqqcfX0zQypMhzfbrUIAPS1PFQN6zT-YehADOVhBgIB5upmAUYf9Akc6dmHB2QEA_uoQ9dojXn4rPSO9DhdFdJk5oBb9uvK7fMauHrHtw12WNawvJwbLwGiiBk374VV39Wg60kc9gVDq4v_QIdtLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=huaF6vX5TIA-9_gMZaGdgfOtar3XfmGnVNIbjmURv0o2xlLRhB_A2CFAOKPPCpMZvr7m1Gr-AX2Dcfb1wGNH_vMKVtPBSUZrI8Zj4gKx9P3903FJKM2nTVH9o2tG--oEyLIeYkkTFzZ8aRWUm2F5KJopgNpNvbxdYjOCqvJygCotfNdy3LUS9SvUUNKa3ClOme3GL2-ovkXJ7R4lGtXEoue70Lb9QRkeB35NGSpoHKgrM6MgMuCKOgVV77bVQCSuNA7cX-vMQgpROejM4BGhZ4DlAYYP-ci7PrfmQzoIH4iWM4SasYSlMo071PYghuLFdl62CcfavHq8T6PSRRc_kYvY7drKlo65uAYiDGZ7gn8zGooho2u6drJawRCvnQrYROrQ8fqg4sY212P2rNh0RKAM8frZEnz6Gusvt06J5jb9sXr_ckFvkiUEh9nfHxNqZ1OlR8IeotxHmLAldjEE7_rHpncE2bx1m3HgsWhO7xKP1JGOoXUl_eNxXfNGefdBnEbnzvOfZHtyAYyl23JIizM6x6P0lXOw4p4bJ0E5sM4-sOeZH5Oj5cW9SUI1Abac4_DnwYOJ4bNBga-dMeTJGj150oCz1hDXbHfZL_M17xsHotYYb7PTNCps18g6gcIy2vutdT_OvNuH-FMQxpc32XnUwyoKjkYxhcc_xERBa4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=huaF6vX5TIA-9_gMZaGdgfOtar3XfmGnVNIbjmURv0o2xlLRhB_A2CFAOKPPCpMZvr7m1Gr-AX2Dcfb1wGNH_vMKVtPBSUZrI8Zj4gKx9P3903FJKM2nTVH9o2tG--oEyLIeYkkTFzZ8aRWUm2F5KJopgNpNvbxdYjOCqvJygCotfNdy3LUS9SvUUNKa3ClOme3GL2-ovkXJ7R4lGtXEoue70Lb9QRkeB35NGSpoHKgrM6MgMuCKOgVV77bVQCSuNA7cX-vMQgpROejM4BGhZ4DlAYYP-ci7PrfmQzoIH4iWM4SasYSlMo071PYghuLFdl62CcfavHq8T6PSRRc_kYvY7drKlo65uAYiDGZ7gn8zGooho2u6drJawRCvnQrYROrQ8fqg4sY212P2rNh0RKAM8frZEnz6Gusvt06J5jb9sXr_ckFvkiUEh9nfHxNqZ1OlR8IeotxHmLAldjEE7_rHpncE2bx1m3HgsWhO7xKP1JGOoXUl_eNxXfNGefdBnEbnzvOfZHtyAYyl23JIizM6x6P0lXOw4p4bJ0E5sM4-sOeZH5Oj5cW9SUI1Abac4_DnwYOJ4bNBga-dMeTJGj150oCz1hDXbHfZL_M17xsHotYYb7PTNCps18g6gcIy2vutdT_OvNuH-FMQxpc32XnUwyoKjkYxhcc_xERBa4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=chQFlF2lILSmV-awKDtHrWdT9b75ReAv06bnZio_pg8VRiKq7RjMl4xk3ralZndHXPHQ6IcFYy1ZecpYPrgnkPWZELG7PTMLkYv3EKSVFCFrLf-vdBEPOw1s4JWWtD4ane_gRx-Uta6AdpXEz6ojxCMZqC8ppVomny_1kV372jICm_bpw4mf1ZBx-vgCj3KiO_2P8OofVpyqVc6Rx3taQePUGp-kP01i469f8duCoioXCkcCByDGmfsOGHc9edLrF03QLo74VXyLm-IKB_opcQhWbI8E3LjQ5Hako8_fk5kqk8gBPJqusw-B9GFNxNKB7SCZ5aDi0puwqUr80BjROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=chQFlF2lILSmV-awKDtHrWdT9b75ReAv06bnZio_pg8VRiKq7RjMl4xk3ralZndHXPHQ6IcFYy1ZecpYPrgnkPWZELG7PTMLkYv3EKSVFCFrLf-vdBEPOw1s4JWWtD4ane_gRx-Uta6AdpXEz6ojxCMZqC8ppVomny_1kV372jICm_bpw4mf1ZBx-vgCj3KiO_2P8OofVpyqVc6Rx3taQePUGp-kP01i469f8duCoioXCkcCByDGmfsOGHc9edLrF03QLo74VXyLm-IKB_opcQhWbI8E3LjQ5Hako8_fk5kqk8gBPJqusw-B9GFNxNKB7SCZ5aDi0puwqUr80BjROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=hlYEThqKBwCnDPHqSuMvzPdupPDhUj5MqmNetjwvv-xnJ5Fh6EelUczBPpHrdpfOqdwvKWN0cqIxuYsrXGqWBfFwp7GxBeHL_gNFjfJmuwWy_l8RKJAO8pO9Zko-PkDOKZGKeqVDv4zdesxPk3Djgv1_h-yD-xxd5cL1sXgjtv5TEq2oCsuHhgVREYE3WJrfDz6wIcP8GGch8cndX33VxzphmyVkzeppTu_3a5914oSG3L4QCcGj2TeS4B7ZCx_TFAW3oCe2tHXdWWcAQ-D03XUvq0s6uc0mAiDYKmsDYrSxgL3gMfYVvOH33y4MQE2wLhyVuPgGgQRdg8bsXkQ8UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=hlYEThqKBwCnDPHqSuMvzPdupPDhUj5MqmNetjwvv-xnJ5Fh6EelUczBPpHrdpfOqdwvKWN0cqIxuYsrXGqWBfFwp7GxBeHL_gNFjfJmuwWy_l8RKJAO8pO9Zko-PkDOKZGKeqVDv4zdesxPk3Djgv1_h-yD-xxd5cL1sXgjtv5TEq2oCsuHhgVREYE3WJrfDz6wIcP8GGch8cndX33VxzphmyVkzeppTu_3a5914oSG3L4QCcGj2TeS4B7ZCx_TFAW3oCe2tHXdWWcAQ-D03XUvq0s6uc0mAiDYKmsDYrSxgL3gMfYVvOH33y4MQE2wLhyVuPgGgQRdg8bsXkQ8UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCcnbyLqYnwCho2Fts5n3mgoVZIFrmtPQky1R9KP9FTS18ECBLVOmEKeAbZ14AEQPMwje9PGxLxlDpQYI9xJ1PAkOdjXwt_-h6Jd_1bPVahHMafQmqB7SaH7MxaYqY9k0oYW-PZ6jsRNJq1sArH8o4yKhYkEf6oxM8IkFArVsEuMjY_ySjv7Wap3NoLrplSMJDSuUCnD9-ubXi-oRXNQlM5wp-DMeagQdbEX2SfnBM0hA_agiwn1pg8uzC0S_zZ3HmnoiY6Gsqn7ODnHu7EnTUiH2cdKYTZ5UHISD0kcbvJAaWYpRptdMW_JTP8h_NTaqut0I-enXqzKwe4A3Q1luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD9vVrbG9ALy20RWzsevUaBl-cLt0Ty3fBu76G4fkOkKuS_vzO8uVdqxTBBQbw0LLGozB2VjSf5oKcLa-hW7lOH3a6d7piO8cItdnpPG_-2drG6_CplTUMj6FrinI9fyIgHgu0luoz98mKIir9H4SZ0gfzSTIKldjgW_scZwKFrCmDfFNEK0_pxF5UTz17GfiNzaQAFxKQx_qMSShPv31gV_zlpUerYwvXXNo5UFim4Iqp0Swjgw48k6VBpF74xsm5-1SYqJHApM8bVecPGgDgkdNaMauZS8wzr1jEfRMR8q5C9kzhy4STaTTjjW7uOrhSguVnH5uPOK1fDEorQvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=f7jCFNXoF2qTZIVE_u1v31fDP2lZ5lNE6ui7_XhnEHH8KSsbgMFhYgAV1zFGW13cR9SqaUWRhO0_Gn0TFrw2FHYVyoqNijOm3zH18-k-KplHC93Js2guDXVhIQ6zKvcLgZc5d92UsvC1_SDh0n83xoMJrzuZ5kNdWIEx5VPmGYlte7l0DHjdMW61urVlcyyNynlk_LZaDaYVgQ4KwES3AIXsIiH04uY18GSC-vCNcNRYK5MRBqQsJA3mUO4SUWnFE0-HVFuz0cwZgEQBQ8pZ97Btn7STYJ7FNQY5EwywU7oJuH1ww7iFDZ7zOa0GK0mJPObMOJV7RXIkMvypLtkACBA9fHExUfKsSyAJd_oDtWRCsjkutWQU-qqUQVxfCWkDIN2OViLqqsPVrzqJPOp_yTZt0474UqjFSbqpJ3D0abwoAS3c5PIj-TrZ_87NDdyk5WEy7DtUdm5r2A19ECRbwqa5gyMHIrWbSWea6BUwtwLJM0ctmwp0m-yHXv_sMtpsvoQo_WKN6VnBkD0zP0poBc5MlLI3XcW5HKtLWpjdmfbFFEaNOZkDWaZ-5ubRB13vONUFfRLt0IW9pyQlWkVOXNnO5_2TnscrVzm-qhLLOCMool11S2ykZB8wsyYY3TGPR-rTs-H_6G6I8LTdebEx1GfwfLRMG6TOhB4nNAuwx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=f7jCFNXoF2qTZIVE_u1v31fDP2lZ5lNE6ui7_XhnEHH8KSsbgMFhYgAV1zFGW13cR9SqaUWRhO0_Gn0TFrw2FHYVyoqNijOm3zH18-k-KplHC93Js2guDXVhIQ6zKvcLgZc5d92UsvC1_SDh0n83xoMJrzuZ5kNdWIEx5VPmGYlte7l0DHjdMW61urVlcyyNynlk_LZaDaYVgQ4KwES3AIXsIiH04uY18GSC-vCNcNRYK5MRBqQsJA3mUO4SUWnFE0-HVFuz0cwZgEQBQ8pZ97Btn7STYJ7FNQY5EwywU7oJuH1ww7iFDZ7zOa0GK0mJPObMOJV7RXIkMvypLtkACBA9fHExUfKsSyAJd_oDtWRCsjkutWQU-qqUQVxfCWkDIN2OViLqqsPVrzqJPOp_yTZt0474UqjFSbqpJ3D0abwoAS3c5PIj-TrZ_87NDdyk5WEy7DtUdm5r2A19ECRbwqa5gyMHIrWbSWea6BUwtwLJM0ctmwp0m-yHXv_sMtpsvoQo_WKN6VnBkD0zP0poBc5MlLI3XcW5HKtLWpjdmfbFFEaNOZkDWaZ-5ubRB13vONUFfRLt0IW9pyQlWkVOXNnO5_2TnscrVzm-qhLLOCMool11S2ykZB8wsyYY3TGPR-rTs-H_6G6I8LTdebEx1GfwfLRMG6TOhB4nNAuwx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ML05MXdazjO1Mrf6VZ4KBLAIK5GHHE8fnHPgLHedGrD0rwtOu4sOjafkDdlROKQNXMbUwpeG6Yd03YBnyP_Vr7wjurv6kwLpldNP6axgzA1Ot1YmSFvhVLsItkR8GptsaNkxibpmdNeWlrI_jSPo2ToCmplyZI_v4z7hXdjPSjhabUz8c5E7CqCGHjOj3JDwoH4A2yknGofmYogs5DPWf7yY9LGJECqs6FnabYHz6LmP2P6anbmJhe2-0vMzeeVfSesJvnaH_hEw5Y36EAwZh23i6Q0CV_Dp6k-fr7zaEDqQ_L78YaoCtfJ_7L0YvzH3guW4wIUR89s6ZazL485yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlI337OrIJF0g3VC4zgUvClxfZG1J_jVfWsJate_tfRD-JRzJXK735rALRXKq2OXXDmJu22HTvUletl347Y7_JJb_S18zObeISA-v9mHkvH5hSu_gP_A4Rpfd_WYlCl4xxpVIijpQqcdErPYpGL-yW-a4wlTSt1AT9J06gYnJKniPfjvY4YiT_LG-izFIrEwNu5Gvj1rPDWaPtpj9z7j5jKwR5NZqC2XzD0fEKBTehNgG5CXVpE6LKV7sdM_n29HBVhTGh8vvifHkKw60SXFyWAnn8bn6qDq7HdXY3wfsJ_Ohfl4xbYxP5bnDr14lFDScyRliOBIxiJKiFIfITVO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWyX-_yY9TY0AtY97WKIJdkmvfR19lG-cakn52FYAIBAg6ebpSUkwb1vTX101-MkswVKCXNsMuWNZ-RHlKkT2bq2JSW87-A45vQYJWKJxrDTOUzebQh8Ev56-3Vvsn7SUqDY5ukTLwoE5kiYsPOyFqQk0_xrRPy7lW98nq3AkPCb10ToS7B6SDXZAuc_-yUUaC8RArAUnfiyjugQSicSkvW83GnEDe1S1EhwpP3R_Eq0qNMaRhLLCH-Z3Hcu8uIsRyx_tysTLUWtbvF6Q62VqBpPFixIxcqjcFYtP4S4qmlBFLy0MxywyoIlXsy8uDY91BjRpl_uFXl1wZwrDgQ-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWYfZc1Gd67PY304GsHi86_39Q6_6fhyxA7LVlXke8Z9Uj0oAdh4ghvAoFOxg2TZfYzriWLrXHeiRh6HhHnNZQ_QG15UIR2Tm_ToRh6Qm4KmoaXNTALF0vIfHIB83zVQttM6vkGXHSFUHpMZyE-FiNzznV_H2_1ktn34394SHJtS_I67D5fciQKN2JEbJN0G7hddThmzpEdMRa_OibZLgrpf_b99BjyRRgW-WDwnHrmNXBnQHcy6WKqi0UhXycj6xEiR9eMB5654vw_pUAOoO64zdoVK4Ti4rfHKJeQyZFyzvnQEt7avggPgtUIdChZJg6obXQAp64ostL8aGhNZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=f4umpHNPiHUulS4LqWZQJsy_oJ9E72AZw8QgrN3MjpSKaPWjlYHzL3t2je0EyQjPK3XshPZZjskNgJ_kFAwS7s8zI5iODcSj72nj24zAhQM7Vi2Im0uSCDfCDM3nblclUZ4VrdI103dGF4MZP6iDs3ZOEbwUTiJVhmY_8gYUjl6TEczBDqw747wTzonNVoGCLQmQyPVz_z_ONkvN2fWjzH7yIHO5FsfwqgrQaTtpC1_yG9JwOofCLyIcbBhWL0RNHCtWGogJR4X4sGsDldsn7islYjIhW5d_spnsAPaZ5Ln3SHVrkAXrtCO0qLeksvrVForic2YtCTnoxfaVD7FrqWT1SRCIdIWuFMIhD1IbTZdyxDAqNloDySXOyw-B1psTaWc-9lxp0HcM-SMHUICvOA3KbynwMrSNUGVP8YPuI9PF6108FSaKiXLMdbWsp-IuHnQKPAcykYFrtP8gHVg-5WtafRoZ8dOjzGv-De-pggiQAfG9vB82ZyQqZJRgJ_tVAF_4zIT_jIqq3FdMnbSC47jtDkXE7ezolUo18cWGmEfNWgUZbUaZwsX_bn_2iEJnsOwlD0Fz-7WdQM0wkro-v2xrnm_890wf70CxENEy3p1_8OrI6FVOWIO0o8kTHPNP5B7qXIlKPYxcrZK2HSFiiyRmoLS7c4TSkhe0b2hLlg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=f4umpHNPiHUulS4LqWZQJsy_oJ9E72AZw8QgrN3MjpSKaPWjlYHzL3t2je0EyQjPK3XshPZZjskNgJ_kFAwS7s8zI5iODcSj72nj24zAhQM7Vi2Im0uSCDfCDM3nblclUZ4VrdI103dGF4MZP6iDs3ZOEbwUTiJVhmY_8gYUjl6TEczBDqw747wTzonNVoGCLQmQyPVz_z_ONkvN2fWjzH7yIHO5FsfwqgrQaTtpC1_yG9JwOofCLyIcbBhWL0RNHCtWGogJR4X4sGsDldsn7islYjIhW5d_spnsAPaZ5Ln3SHVrkAXrtCO0qLeksvrVForic2YtCTnoxfaVD7FrqWT1SRCIdIWuFMIhD1IbTZdyxDAqNloDySXOyw-B1psTaWc-9lxp0HcM-SMHUICvOA3KbynwMrSNUGVP8YPuI9PF6108FSaKiXLMdbWsp-IuHnQKPAcykYFrtP8gHVg-5WtafRoZ8dOjzGv-De-pggiQAfG9vB82ZyQqZJRgJ_tVAF_4zIT_jIqq3FdMnbSC47jtDkXE7ezolUo18cWGmEfNWgUZbUaZwsX_bn_2iEJnsOwlD0Fz-7WdQM0wkro-v2xrnm_890wf70CxENEy3p1_8OrI6FVOWIO0o8kTHPNP5B7qXIlKPYxcrZK2HSFiiyRmoLS7c4TSkhe0b2hLlg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=EBjrscvAZicmBlgyu_lAndr06BpBS6HVc69R_0IQXR6CIpF-HB39t-8mntKUGzTJCAjxg1cIlYQTAqJGYbP084w_qiZrQAWbR079xwPKsNPGbunScyIXqfmbDIBi1AzihjzLi6qxSczLJ_vrE8GP1ZKbNODT_5rYWw70NlFcYjxO6_7Vb9el6QmiC1pEyFJkIXd7hNugvH0bJj3DphP_YovX_Jf6FLrNmIX-Czxrq0NOvmjJzv4_fq_F0cXG8f5tTUJDm04rqNZTt9x2PwQwpcrjQtuAzQWYLb1zegVlS1biBrHXOL4d0JXZjPH5YiFNEKSgA3P8HCrPcOJd69BgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=EBjrscvAZicmBlgyu_lAndr06BpBS6HVc69R_0IQXR6CIpF-HB39t-8mntKUGzTJCAjxg1cIlYQTAqJGYbP084w_qiZrQAWbR079xwPKsNPGbunScyIXqfmbDIBi1AzihjzLi6qxSczLJ_vrE8GP1ZKbNODT_5rYWw70NlFcYjxO6_7Vb9el6QmiC1pEyFJkIXd7hNugvH0bJj3DphP_YovX_Jf6FLrNmIX-Czxrq0NOvmjJzv4_fq_F0cXG8f5tTUJDm04rqNZTt9x2PwQwpcrjQtuAzQWYLb1zegVlS1biBrHXOL4d0JXZjPH5YiFNEKSgA3P8HCrPcOJd69BgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv22nvyyckHEKRaHiLguH_4l2_419u5lhGbGCgz9GE7KyoA1qZyOOXK1M9LfIF9K8Ob22Orkwf3G5EEAwCiMkx8lFQ5-ezVL0dtb61rHZsQNJkcCV44BhbQJQ9_E4CVxiC7zXH67EgRDjc69VawGxJXbTXAxKtmbbiOY90wE1uVRfLRXSL1QQSYY58uo1ZDR-8rutfMgzNz0WZrAM-KAznJwEumw1Vsad0AMWMDPOxS6m8KfZ98zM1fY5W2oPRbScx50QmHdB0QDCbcHVfJrF0ioRb5rpE3NPyUFaW_5pk-TsskaEa_mnXcdAtbgOQAyb-XZn4AC-PjH_oLVo-rFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzeW--E78eTa5Mf7GC1EfGH-gh8g4f-TkYreXQCkl-H3gioUld2lxRl-5MLY_tbfUVMcSUKnZkr5rYDzUPwl-I45hIZ3QFYtS4zKp3iqejSroIZ_Pv61UUyhiJJYw5fxn7lh49tvwEWHEkXCQICvy8FMiaYBmamQ9JDEN1JCsbavDKtlwqi7alah8n4J5k7o8VIxSWtStMioy8-mrrLEWGPBpe9g9XoX8r3EnxSvypN_15fQdXVxAu2TZiRdB_N7mbvInWHZ4YaEaUVRxuwRgE-cUMjFzJx5yffi0j9eOCJtyxUk1G9mhZGWBYU_E_c9FSMTbycqcTp-WX8faX5KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PghAVmYQop1ehyB37i0_M5AdGERdy4OqyLGGSnOfQjIEJcXOiSLYQifHpj50-ILQcr-aXyFKc8gGShFHbvFibglPrn9WOWFENhZ6z2cEvZ9yu4fgQRHS2FKfaf979pV9SU7jKBAKvabPX0oFwPw9ZVrL3aQsKoSwIxSup8bvl6MRjh0AtP3YVfgRyPniaOsfBrlj-cjJKTkUFr4xdt_T1kEFE6WJM6GDES_KA_wxnXI0a1BV9mQfts3JhfKlqgpTK96kcQiOABZIjmWqVLw1hwHHFrd1DllTXAzVJHvhUpstnp6QbYn3fRQDS_ankaxGSdcq9Sw6bTXK4RMVhqNjFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcszcTQja-R0IEn04Gcd6E7YYvAcpBOhPkyTWgy_oF_50rL6koGfZIA3ro9ZjDqnyrjBY70xmuK9dMsfae-_BgvEZ4aj1937G7v83ZfbD5kLXsqbTWsrZ9-i2tY-MDjAUyeLpCLRQr7WkPVX0BE7DIHCtczOwWRlC4D62HMwRNZ7YhTaY-VGsBe84_BFTlmCkUy3wknPx48hNB-MD_xy0bKDXO8KfMRCli18H6_AX7m7GoVJG4Y8ed-4dNOodT0rPOhJ8uoGYGQbIGKvSQRJPD5zzUdaNVS5iOrWa_3kf-xgnSWuZ6M6r_Xwkyav54yK3xIxelQrUbDuBbNDt8megQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3vWteEx_hTtsIopIjHnDKPwoFTKE8wVna3qu_gnG9UBYAMC-JdEhPS8v-vvDVyFiW1-2WNd_PS-xm3SUMIgA1-hlaWiIWHLHvwcB0sZzC9sIPGLWZYBjIPZutD3Pxl2X0GngYti3lpKvpybKbStiJhQE0ZJjJkLXAk79HoxSbBPxSucMy1dzyg6GYRbbYBCNqMkWGphwuZI0Vi51tkIfgs2uuEzj--J4YjWVjC2EanbIMlP9br8RjpWsfJnIoyzk_coVRp2-RsaqiLD_tbltBmkoG1TrklWVdlBGR9_rtzp0MCC_A1rD3GgJbSrmdlJFlP7xSHuSGl6OAE5oTPYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2JiQfNPmGd8ZX6upA96libE-KGRqMV_6qoF4amF_K8aO6HBnVCHhZ6BV9JfMLE3xJwcdmfRCmXv1CpppMzvVPy_uTHtVeGEEitfxvYouL3MZTd_EkTp0dzaSo_mhHLGOsG-RYVagOB1AS5Gw6lH96Mnjr79mwWIvWmMT7qqpLTlQnUGPk1qEsWWDb1Yiij6nTAd79gUoI3TLvMOMalpCRgd6k41tewmnmfSjT2BRpklSXCEtcIDYJFiaxZl8JfDQvKBgnCFSVICZtd8jFsP7Wr0O2AWSS3Po-nbrU51VhlF0ZNuQwkR6X8-ypEoB5kM7q-QJKhF4guRp33t9ItJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJME2F05mc1DjNzR7v9I-JfQuSEuMBs2hsbCKYfLqhqY1tL9EiCNKYzhWz__y7tscShDPPl_unBvl_d2PtDOs1AuDr4sp1_q99L30IZQmrU_as9i5DE3pHkXVCuBE1JbIJg17pQsZjx9GMpBS8w03ESdAXbOHsImcYZOSRFstlxgTHizwear8w4UaS6CgnhPcK1-CbrXA2jcbzcCOlBpo88PS6wfQpq6YffL5YfSW0T0TSTZ8s7y1TD25j-LGXni4DJ3HN-wHXbPTzBuGJe4QinCCKVzNYE7YNx_0UkMgDDhwmES3ypUInA1utQnYRmmUaaDmxZxHgGEVNZ5NUlBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=CgLsxWtMbTpAuHl-MFSd-XNe6B0JVnIlZWCslEHWNjhi5Mih0_bawECEW88ZHyf7Ys_YaIFfY0kdHdji--rekwbOftXpN2r_RaMhdYauw7-ebDnYNFM7g8J5BinyT7IoldH0X_3DI2u6yUu1UrRpQ0HkB_dif-EWcxD5wbfyaVZamk5H1j9b_jRdYINgIdDzeILXIwcvb_xCvb0OXE-FEefwKAju77caG7PnfPo7WYc26lc_VWen0BmlLJV0O4KLE156UdU8DysaogMgrSICH1Ju2EkyQ9J1053OiHupeqZz-Z1kv6LPhzPwDCxl7v6hsJxYJa4FMCCfHkn82M2KNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=CgLsxWtMbTpAuHl-MFSd-XNe6B0JVnIlZWCslEHWNjhi5Mih0_bawECEW88ZHyf7Ys_YaIFfY0kdHdji--rekwbOftXpN2r_RaMhdYauw7-ebDnYNFM7g8J5BinyT7IoldH0X_3DI2u6yUu1UrRpQ0HkB_dif-EWcxD5wbfyaVZamk5H1j9b_jRdYINgIdDzeILXIwcvb_xCvb0OXE-FEefwKAju77caG7PnfPo7WYc26lc_VWen0BmlLJV0O4KLE156UdU8DysaogMgrSICH1Ju2EkyQ9J1053OiHupeqZz-Z1kv6LPhzPwDCxl7v6hsJxYJa4FMCCfHkn82M2KNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpK0rYS3hdXCIDhAW_2Mn9umPUbWm_olLb9BUOHyFDnEqdjYrzgXv_3_PZR510Ff5rTQjPF3saiWrZxhbK6UDkgBRkdDsBBhJtgCzXaME1bi8DYuOmEPR3nYeqMhPA6l6vx9auUSezbsZtfPBr3S7jRX4uRIKN21Uc8GLXPEtuMppUJWpPBATmWzV-wMnlTB86qJBVe_GiOuW5rQYjwc1Ac9ZmLPZg56zJTKCv9iidOK3Bkbl21RcdS28BAfCAx0oLKBbtfaDLXMAu_21UKEPQJ52yYDzj5S1uY4QSnxcsmVgqbBagJA8Lr60CnpcVZjPBRx5EVJHiDw4bErnvXzsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=VEdvwRJeHR10-xZflAgRhPR89rRxJMI57H1n_ELYMta0cERK9aDq_XzUuyJlSHk_Ec5_BxBL4hZOEI5dj0g8SvZYz8lFS_oCAUR7x4bLhXzO2fj8Yy8CWAqN4-KDxPxShoZvRf-beGGXKlJ2gfJ1nSYBNVCh1rFBkpdneORAtUmGs9AO0A0aDexNyec7xhBrxp3Do3H5iDvF7yj0AZW5BC_wt1IvFroUvc8YY0ZCo0nnrb0yp3hHm1wbkc7gGMzzYhyN8Rm-YQj5Zb_C-_n7I07O2053cB2Ad-N5nu7lP5-JZHnYf91SxDZgdhhZJ18OBpJxnqPB5jCa3RvNlrYEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=VEdvwRJeHR10-xZflAgRhPR89rRxJMI57H1n_ELYMta0cERK9aDq_XzUuyJlSHk_Ec5_BxBL4hZOEI5dj0g8SvZYz8lFS_oCAUR7x4bLhXzO2fj8Yy8CWAqN4-KDxPxShoZvRf-beGGXKlJ2gfJ1nSYBNVCh1rFBkpdneORAtUmGs9AO0A0aDexNyec7xhBrxp3Do3H5iDvF7yj0AZW5BC_wt1IvFroUvc8YY0ZCo0nnrb0yp3hHm1wbkc7gGMzzYhyN8Rm-YQj5Zb_C-_n7I07O2053cB2Ad-N5nu7lP5-JZHnYf91SxDZgdhhZJ18OBpJxnqPB5jCa3RvNlrYEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqeF8eITGrn9ejB7SSclTisnJaDwWq0lSEyHKTiwvqRHTMPUqoMxix48z6psstp1EqD5rddRwMUjjN_SFAXfaCBXAdfk5yCSDF7FpfHA1LWNfdcQ3x5EXDdr_-f05MViLfaArL0JtIAwuKNrIwIe3Q3PbWTCFzjSzs7u61XYnyp4N9rgmoUYge1kLiIil0fozR2OI9vWWAKK0ULEyeCMcej5Qzq_8UC9i_cdvcXg7WRWeQVByOBZZvTb9V3B6MSRn8oVJTFJgHs6G2RBq83Edt5P_7lyu262At5tVCnhQaIyl5JxqzUftXR-eO1Q0WPOV8f85F6okf-teSzAnetcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7loFHdkT42cSK19N63--ImrHYi2f7B8K7ShbNXGED0NnlqNacHrM8GsjlR3FtUgp8iwQnReG3hrILoXi2kdnk_dK9CyU4wjTshPdOYA2rFCHRbujTLZ4ppCusi_dUkkfpRTvM64xlcmv14EljNP2FJmDiYzdI8LBSatjXAcH2kvRp2_xjz5ZFF0AmVeastFVO4USqZD4z3TIIz3dZ2K6BJFWleK9A2v2d4HPs2DZ91wdtuER6xHYb4W4pHSNVSNTWBWNKcgw8T_ARsYBeHN-vgS-qbVaytCQwIDJAGZZ79g7w-DIRx8H9jkbxoOCrhkrW4EprNzjTO8UTKurt6Qe9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=r7LkZBavyEC59LXEbFAY3F0pyRfkYsbinxtDLBK93-PSEnPsLkh6fOOZ7-YG2oVRhsc3FRCC9iqyTk4sLLz6Ll_gjw1nT_GzmXOrsBjRBLlvNdRdQlCEYw9_PLXTi76yf2jtIMa-UFGtVlyIUGy62GM27n4ElaTcD35CUbPU1XRemrgrVsw-eIpcc_5DOwS7oaBWPHdc-jzF_15-mfWjSVyS2vIG4FNQvlv7A99BKbSG5S8zIGsQnRSpb0d6MXIckN8PPZKX29otTZCunMYEoIK0gqPXOhaMR4ETqdgq5e_WPHYCSXvbezrXsmEUtYQFApE8PFcC4JM42Zlrnati7loFHdkT42cSK19N63--ImrHYi2f7B8K7ShbNXGED0NnlqNacHrM8GsjlR3FtUgp8iwQnReG3hrILoXi2kdnk_dK9CyU4wjTshPdOYA2rFCHRbujTLZ4ppCusi_dUkkfpRTvM64xlcmv14EljNP2FJmDiYzdI8LBSatjXAcH2kvRp2_xjz5ZFF0AmVeastFVO4USqZD4z3TIIz3dZ2K6BJFWleK9A2v2d4HPs2DZ91wdtuER6xHYb4W4pHSNVSNTWBWNKcgw8T_ARsYBeHN-vgS-qbVaytCQwIDJAGZZ79g7w-DIRx8H9jkbxoOCrhkrW4EprNzjTO8UTKurt6Qe9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
