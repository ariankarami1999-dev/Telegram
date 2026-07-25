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
<img src="https://cdn4.telesco.pe/file/iFySZc54mpNiRi6w9AM91ZX_zH9AqvZAobhQi9pe9pANt9CYhF4uG2QbAuKvvs_8w839wjMkyU68lzDEaXHoQOiOBJy9Gjh--9S11PHqOjMV3Md8oJCAmK6nKdPfNOsuspC0E_VOA6uElpMOC_FfpnXQauNBMaQLrYK2GJ59n7_Xe6zLqHUlA2bFGpU2uMrWxF7uRTuX69fawxjoSFzKCzCEzIBxe_N1ob1RITj_gqXHfG4ofR2Jw4LIHbEBJ-dxK4QP5TLTQ2IOolXLUlElo0qeirn7fuVntElIkKwp8Mql6AsqoSanZ2a1AY61XLpPDUWG9lDKioCLGW_Sx3InrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 00:45:30</div>
<hr>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bwKIFT6rHv7h7wMZ0HcyUVJwO30hmfuqheis4NOTjIyGH8SlqenOQS2Z-YVkcB2vaQ6tQ_xK_OGfbM8icGcoAfHBcKXgIE_1BfJv8dIuQHi62J9OgWbTJ8Fi3cZebngmj7xyAVCgb6NBsAzRFoLpCy65DmnpZmHSOOsfKPTfoNAAQuD2nR19bIYLCumA_DO4eC1vkCO3M_lJe-yIBsirCT_VjGPBMs3_kNtsSZq_jb0YHFGxZeLBiKA_OFvqgBKnNA3Lx2nZrv2mcEK7Fv4JtwIDWCnuX0uU4vBM6vAakQrwZ65WGeVtM6b38tPyKas3-ABLB3BrO_P8Im3Ceye3FESsxUv5ZAvSxh-nJRlNmrrU-o81T7wb5945ep-B0uIC8UWoqAjQCHdX4sUwdGysSk50kJJ4OOOETCdiHeIV5D2b1ZoKFGJw-BEsoku3X8_U82vtkdOs8SSV3Ep9EKNh_l9OWNYoS2I9FtcmWgAxxUCwcUTqvcsNer540MLOlYCzDfMglJ1jhVk4itiMOd89-_j4iRGlZ2sOzrdx2AUQCfCC4wmndMnhwS2OzN-HdPbJpEfomxj3C_CjsCrCt2naW_i_Spp519BarMwhWJc9NLCqZBtkC_XVeKQDBPdd0Pl4rB5YGv_EiErPwuWglK7nahYsoygnQBpotyE6cF_uIBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=bwKIFT6rHv7h7wMZ0HcyUVJwO30hmfuqheis4NOTjIyGH8SlqenOQS2Z-YVkcB2vaQ6tQ_xK_OGfbM8icGcoAfHBcKXgIE_1BfJv8dIuQHi62J9OgWbTJ8Fi3cZebngmj7xyAVCgb6NBsAzRFoLpCy65DmnpZmHSOOsfKPTfoNAAQuD2nR19bIYLCumA_DO4eC1vkCO3M_lJe-yIBsirCT_VjGPBMs3_kNtsSZq_jb0YHFGxZeLBiKA_OFvqgBKnNA3Lx2nZrv2mcEK7Fv4JtwIDWCnuX0uU4vBM6vAakQrwZ65WGeVtM6b38tPyKas3-ABLB3BrO_P8Im3Ceye3FESsxUv5ZAvSxh-nJRlNmrrU-o81T7wb5945ep-B0uIC8UWoqAjQCHdX4sUwdGysSk50kJJ4OOOETCdiHeIV5D2b1ZoKFGJw-BEsoku3X8_U82vtkdOs8SSV3Ep9EKNh_l9OWNYoS2I9FtcmWgAxxUCwcUTqvcsNer540MLOlYCzDfMglJ1jhVk4itiMOd89-_j4iRGlZ2sOzrdx2AUQCfCC4wmndMnhwS2OzN-HdPbJpEfomxj3C_CjsCrCt2naW_i_Spp519BarMwhWJc9NLCqZBtkC_XVeKQDBPdd0Pl4rB5YGv_EiErPwuWglK7nahYsoygnQBpotyE6cF_uIBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rgjOzvTv-QWmrxpNPoUMhmc_tX-uIx2f9__FS-KWvxRi9UDIayMCkVbW5duAtlJugi5rrxh92663P_ICgBS3ZfuWr863LSFAKgcPUJa76v3bgfUzSRBudIwAdVz-OUmUPNtGi-vGXhoKAVPE6yn1TOWZGzpdFf-K4sBeyY6vp-UH6z-w90Zj-EWFhg-2PLXzrjoXIjEgEcS3WhL-0V7yblUtUEq-DZAOp9xXlhkNyP5PSSvm_xS0hhQ2zBxuvxPHi79_6UuTOHUc5dQxRLb3epPDyyvlPwA0GstndFbOVE4x9e0kFelSxFc-uOBOKYzZvk718dwmVHFIKv8_JliY5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rgjOzvTv-QWmrxpNPoUMhmc_tX-uIx2f9__FS-KWvxRi9UDIayMCkVbW5duAtlJugi5rrxh92663P_ICgBS3ZfuWr863LSFAKgcPUJa76v3bgfUzSRBudIwAdVz-OUmUPNtGi-vGXhoKAVPE6yn1TOWZGzpdFf-K4sBeyY6vp-UH6z-w90Zj-EWFhg-2PLXzrjoXIjEgEcS3WhL-0V7yblUtUEq-DZAOp9xXlhkNyP5PSSvm_xS0hhQ2zBxuvxPHi79_6UuTOHUc5dQxRLb3epPDyyvlPwA0GstndFbOVE4x9e0kFelSxFc-uOBOKYzZvk718dwmVHFIKv8_JliY5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJnCPX_5JLTYsSkHrsMkoB1cgGk_5SSpCXa6yE23DU2B5ZdYdTmXwEO1ossqPkHzG65qfxU7GrBZ5NKwJuLr1FwwLeyDtoqibQ5dWv0e7__xI1ggHvUq915nNt-Gp8TEnmwpIs7LEBKsj_OHdrYUmeLcXT_ujFtkfxR64VPv2twAb-jyGEO7aXtjgvCKnagIC3DwQyE6OiwlUTCfOgYbFqxpOWi7EBafhrwew5kH_DOnO8M1FPPQGmy_8fJh_ReFNgChWbUR8oxzc-PlIM7_yWyIjzsBd4ikpHvKFTQuaVCwXwFnZ01yO1TeDB0YJ0mkF16eKqTQiCHgH8-m90X1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcXJQJYm6PG8qihJhelZKStJEaTvhB6nTJdLpbDKA1SCKZzg2eKwSZ6AJdRuBATLNUEh_w9YoTEkTCq3VwyH9tpaK9gNsgdIf90EQ47kEqurWBIUY3orVOOUnkmUB_T-ptpzmeWfIcjuhi5eG0ZNfNmSiuIrkzU3td6FypKHpJIBemc3GUkCg9IT-JMb0DRwjD8G3TprRdCOFwwQTWsa3pO9fCBOB-tHHqkaTW88fnGraWkUOFKwVa9-1EK4YEC8LDVBVwzrHTpQUbt2IPDRRMC5VVG-KEJOL2aDBl-FVCb0OvUHZn8XrPGcvcxZ6oA2_V2usFqz8S60_uOFQy2uXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpTgfQosvsdhoOuYtIyfJXM6RXLgbikL9iyvdQJqyOxtDymPXXspZV-2NLz0PCeADv92CMkBCHDBSAEeV7qGHUxJY1BSAqWNVgmiTHmG5pWdBeT0TEx83TvRTyihkgyriYl6lH8HtXq9ucQE4CzwocCZ_UK9bx97xs8BKXwNL1ZQHTgkLItY9T2xV-_NH4WZNtAHv1jOQQPD4o7_oeNwnnf3FubpVZjDExDdYHRDmH4qeL3GU1SLRZO2O4DbBVqV8hIunCN_uJMAqqQa7IdlbVlktAHxw572SZChQUkzaU8h7RVPqvfomVFscn-BSyPkltHNzLYPOPqHLJxXsuya5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSChypBf4KoTK5uXnvRHi5FpA3JjLLygPdnyDZqCxdU4ELbFdib8GF0K4k6upVqjTrSD6or8qbZAZVT6P61Ik9kDdbGcK1gqrYiWKuT2y540jy2-YtLihwsZplTfS8GkNtE0ASF5mzNMQvLmiG10aXksRPqR_NplWBWLtVGgIzCESsCKW43sihH9rnUd4L0Rbz8UKJSzLg2q2qVeJ-kZ2hQ22QE6xBxUI58B12Ac6-fZ77OJmGUy0w65hRH3HxB-0awcruJKm44JO_P0yyBt0JhR9OaHYK5KZOJ6PWCOrHUhiyL4747Zf-Wn1Au3U8BMhCRLHlEsS3N6B5Wnf3Urzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFPLym7ENCUg0O1Elto4u5hrNGEdBiMlpC3Y30JZhCDRKj8f6B-18Vrikmg33D-vgsFrwRlovZHr_qc3dniqtpprQHYAGQXLzzVB7kj_fX2vESKLG4VC1efiUKO8XUoRN3bFfA0b4ODkOteTBtLb7Lfb6Ix1SvuUr48DGdTxTUt4GC43KeoLSFyjmbZ0cqHbErGZWGTv4yun0E8sYy6ML9lhGBahm8lDk2mooO78NSk5_Zn2ESnRLkcjzchdvsrziGdcH3utxwh80FZ9r-o0zZ1EuOM2BdGTuz1H0z0HsMFVL0yvXyDxlWADpCXbtJJQfbk2n6XyNPL8UxJjrUjCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lD3JUcduC6-mESu-PbCH7pbmDsg7PxZ_UcLgSywCuUv7YRmVuUW2DIKPL2D2iTs9sCtG4r_mKAcT7okGV4NnSSXggZcTgZiCzucYP-ZjD8aj3qMXuGCi1rQ8w37hhbWZuhsXxMXQ-DfehcwLoyXoeeQHfmaoNpZiSwnsmeuMEOwXNlwJfJ6eXTPEbGKRWKPL7IlRpS153nGAJAD3Bv1rWOBZEILMmjBi5JrE1g-Giboq7EGTEBqKtGeGjvN3yOwHe06gvNWRWGoY2k1T08bzCy4kzcH-u-_Oshp_87aVuT97CQz71xW-xkLTIHLy8z3pGEs9ND8Rtbaj77azace9Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=lD3JUcduC6-mESu-PbCH7pbmDsg7PxZ_UcLgSywCuUv7YRmVuUW2DIKPL2D2iTs9sCtG4r_mKAcT7okGV4NnSSXggZcTgZiCzucYP-ZjD8aj3qMXuGCi1rQ8w37hhbWZuhsXxMXQ-DfehcwLoyXoeeQHfmaoNpZiSwnsmeuMEOwXNlwJfJ6eXTPEbGKRWKPL7IlRpS153nGAJAD3Bv1rWOBZEILMmjBi5JrE1g-Giboq7EGTEBqKtGeGjvN3yOwHe06gvNWRWGoY2k1T08bzCy4kzcH-u-_Oshp_87aVuT97CQz71xW-xkLTIHLy8z3pGEs9ND8Rtbaj77azace9Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2KEaRDzQ0LDfmXxMXauBqHqH6LaUJTJLQVCp3tdAMWcm4NhvgESx1IDu6UBRvhBVhIeLZ4bbgsiMb-h9Jm7E7cSTi2OtEFre6oVi5sEo3PCC3klwy0YpkpGxu6U_0lfC1k1lwrLGwXcFKxt21effEE5bgv1exiY2lWV_x90oPo-T2kIZ3_6cdLiopTs07d_2j50gkAurLbB1mYJ9epgvMo6BfIbZUF-CzmuZgYDv4zEcDenPFNHWVoJ_CEtB7s9DrGDuXcNp4R2-gigWrjCmO0067xL9jAzhjDQTU95_nyJMsdvZqC7es3zhkX-bk5ofQowKobboCl_ozquxGSMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXnSNyp3-LX4foIpbyQA2GYfBt7GYysJZed27u-FDAEfapElBxDuM_SluvTQhJxXj-Yq-pi6raSlRMUPw5yKWyRUYdmZgwQ9dzayo1uSGbTdaomtnf5BOSg1qT5Gyy5z5YhAOD4Gx7oa2tp_u4WAyFBDiKFd8SHXQkOdlcc_ifjkcMUUu8yobT9kWO5skai4jJx6QvYaXtKfiZuGHhlldk3vMvIrugBjrf0UFRrpCRBlLN9dpz6u2DK3LGAYAavG-90xROwRBKapmn3sfSwk6BHopELrHBNnd3nlynCDUe2Rzl4Gk-ujslME7mKYBE0O_4JqD8hRhWayDk67EDvQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OAsaAuKbO8aP6R-gHDANhhRaboXnn0BWxNsUM1sJtINYRtZlmKTnq-05uwRUccjylpahMy95CrBB5YntMPb_4daOsOQ_JCrWBcUInD_5vGhuQmgyRM-DdHdh0ZC76GabTeVGRcDUWfqNdE5WXWZkz2UI-RgK8AXCMbyZGMJ15vk5NyyWpQ0Am2uqBFQbms8GrEmWf4o-baNtmn_UyH02jEUSFUxIq7uJKipUIJ9rIOhDAZk0rNIs_-wL5n5eWB9mUZYXhqn1ld50mjTBP858168uxHSMgrCpiuyM63iGgEkhuxXQkoLitiKUkx-TC9SjwaDQBDQlnlsywlWETuQDgZxbf_kDy4NpKaUnRn1oU2UXaWmepcTTZLBHozOfUNgXEqC_AciErflt9PWzhIEJy67YNC_ZU4-t6RvAw5HwB9Xec_bhkxYtB0vDKUn8D4kou6bWS45Henc5Bbny-p6gUNCfDRC09U_46Q78bGeeowrs1GThm6X-nzjUgvRClxz6NtYlLnjtYtyHhYWat0YHtTegP2q3HakVXeHRPzq5mMaBSTIAfix2Z6WHeKc_ugcu0MuxoU-aLH8LyUv_M2llKV_T-JEFFLjPTRWThZ3Ev0zMUHwPHSufDqbn5k3YpYAYoY9flaLNpNCp9YlK1H4Jf-wVIwbDnOY1BFrugmEhws8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OAsaAuKbO8aP6R-gHDANhhRaboXnn0BWxNsUM1sJtINYRtZlmKTnq-05uwRUccjylpahMy95CrBB5YntMPb_4daOsOQ_JCrWBcUInD_5vGhuQmgyRM-DdHdh0ZC76GabTeVGRcDUWfqNdE5WXWZkz2UI-RgK8AXCMbyZGMJ15vk5NyyWpQ0Am2uqBFQbms8GrEmWf4o-baNtmn_UyH02jEUSFUxIq7uJKipUIJ9rIOhDAZk0rNIs_-wL5n5eWB9mUZYXhqn1ld50mjTBP858168uxHSMgrCpiuyM63iGgEkhuxXQkoLitiKUkx-TC9SjwaDQBDQlnlsywlWETuQDgZxbf_kDy4NpKaUnRn1oU2UXaWmepcTTZLBHozOfUNgXEqC_AciErflt9PWzhIEJy67YNC_ZU4-t6RvAw5HwB9Xec_bhkxYtB0vDKUn8D4kou6bWS45Henc5Bbny-p6gUNCfDRC09U_46Q78bGeeowrs1GThm6X-nzjUgvRClxz6NtYlLnjtYtyHhYWat0YHtTegP2q3HakVXeHRPzq5mMaBSTIAfix2Z6WHeKc_ugcu0MuxoU-aLH8LyUv_M2llKV_T-JEFFLjPTRWThZ3Ev0zMUHwPHSufDqbn5k3YpYAYoY9flaLNpNCp9YlK1H4Jf-wVIwbDnOY1BFrugmEhws8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=W7RIROLrfecqU85k19eGlfp5fAunrVPU-302DgZrVbUkP1NrjXIDEnvnTwkCjG8GxFvDij1AKlfbVTGdVIAV1Q0sx5orP3gsAKpWgZ7pC8BnlJaN2WQ62W_5Z_6umW2HIBzdnX-7u4z58w708JROuqJ66VlASyew8vi46nJ8SGRwW6G20rskvgdUD1rj06N66c-7ZqlvHzL-e347I6sc8CGY0utNAnxTZWOOiOPwrKGDpLyCu4z0T-8uMzQOSJtsjfDTEDJGnRTFlCvVwblmYd3xko0sXO3O3ZPBZfNNSkfgmSu1VUfIZc2CwwfUZ1xv0wKqN0lXi4DUlKt2vZV7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=W7RIROLrfecqU85k19eGlfp5fAunrVPU-302DgZrVbUkP1NrjXIDEnvnTwkCjG8GxFvDij1AKlfbVTGdVIAV1Q0sx5orP3gsAKpWgZ7pC8BnlJaN2WQ62W_5Z_6umW2HIBzdnX-7u4z58w708JROuqJ66VlASyew8vi46nJ8SGRwW6G20rskvgdUD1rj06N66c-7ZqlvHzL-e347I6sc8CGY0utNAnxTZWOOiOPwrKGDpLyCu4z0T-8uMzQOSJtsjfDTEDJGnRTFlCvVwblmYd3xko0sXO3O3ZPBZfNNSkfgmSu1VUfIZc2CwwfUZ1xv0wKqN0lXi4DUlKt2vZV7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMTibaCUIh-aER9B7mH98Adhmze1bQE4nJYd9QayKoizShLoc9Gghf2RiiT-9LPKKjW2_s65lqf0xx3rm7zAGPf66KAcPS1UrfTwf1qF_1A0ET7wuDPK1SLV0965G4u-k7ITSBfHLR_RJt4Rpj3JJUDNaKvxTgYqZiMtRmQNhlF50XE3yX8ObIK1pQnD5WLgfMiRXKZwohigyt1H_ZQRYNVe6fAKzCJoRsy72VE8THzNhCAMTWIbSB4F65G8j4_GELMxQ_E6mvXQlGiJC9SjWp3bHFaj0Snv7QtSHnfel6CJV7TB8Ap_12c6BNYJ0FTq8W-JtU4chxs_3cMbI8sOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2K7MHBNB25QoBDhoM3Pf-YqSiwJWd4Dq7IodPhSeq6Hib5I0Iz8LHPnGeru8DQ9g7k5g-4LA11giYQ4NRieoWhCq2-wwbti1-xJ3aFENMYpv5VgZpcTk65Y2usYkE3Od6IRo3xYvSAq0VhbZaSyzXksNY0tlzv8jOCQ2aRuc7SipPSNLfqwNCCwrqF_NK7MugmJH8uQ_0H4cxyooW8JeOtJ32UVLbTa8PPRBfglliAcnlMC-es_HRq74-aNVXXkK7E7cyyhSP4-u8mYEB6lXyXDnaF0X0w8UXW7uAY1vQC5flIYVBMAEVXiP9hHzgao5bwUZhS2cTQ2V_GNhMxPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5ZPtQ2eZCoFyqaTHnhHqhPvAJYjGQWJbJWfJ1Wlm6x2TRani-LAwswgwcA9LqKIjK4jR0WZrGMzHrtyLC1oxZlvaXAitOIbPm9Lkmc7H-oN_z5yEFRHdoJiVaAdrEiRby7wlSPqI9Gd_WKtKBNZn1_FVNLJrVt8iDkFbxKNyMzs_sN99P-LYL4Vdbpq43bLAQCGLylW7BPKQzXwVkcZxEZFEJvyDclIGZJg8HYX25jpGn6hzZja6etocCTebJftPICwSxBHQ6vD78oocBst-Wo3yoTsk65DFAH7VbkL_NQI2-KLiCwlaNBswactMrBlrFo8pbbSf7ySgBudzqKUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=klU5k1opkt_TQJNiMhpzcio-gJrj9kTIsQyTP6oRHNGTiU-5k7iU43MkDpfy8Kkx91t2jA8-IQMFqjZqrjx5nLgFHbS7-HHL51Y6kisAshDa6_W5OkI7Pp9IkcPyFLkIVa2B9kqHqSpFg6peb9Uz7KLhX65E7tY34vX4E0DXdiIRoQ2z_TUIFJHPyPLJlojW-EbO1M6HPL9B7tEAK9p4bg5kxuYtB_gW1Ef5zDGXa5lq4Ya-eVYFwW3b6tIhGohG26wNEzB0lsREizaCAVXwQ1CJGvGe9QNgKxnTGfXykaL04e3EXhIUTURwG3OmcxSb6w9phgWb01DtshMdrdmIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=klU5k1opkt_TQJNiMhpzcio-gJrj9kTIsQyTP6oRHNGTiU-5k7iU43MkDpfy8Kkx91t2jA8-IQMFqjZqrjx5nLgFHbS7-HHL51Y6kisAshDa6_W5OkI7Pp9IkcPyFLkIVa2B9kqHqSpFg6peb9Uz7KLhX65E7tY34vX4E0DXdiIRoQ2z_TUIFJHPyPLJlojW-EbO1M6HPL9B7tEAK9p4bg5kxuYtB_gW1Ef5zDGXa5lq4Ya-eVYFwW3b6tIhGohG26wNEzB0lsREizaCAVXwQ1CJGvGe9QNgKxnTGfXykaL04e3EXhIUTURwG3OmcxSb6w9phgWb01DtshMdrdmIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB6nevVc1zftLPgZT7FWcOyr-WakW4pawukEiY0oVy1Q6IbzSvbORGEDyhJiRqKWHVfidmOD4PukNr9-Vzj_0b9r78n--C1V5LhoRQpFEE09CyDx1G2pFVTms4xL363sow6zqU3AdYfScv-VgbYgenQDPk-2H6vWyQ9ESi-suFtQas3k7x2M0G26sf6R_wcY0saJjSfSleL5pbwCKt5nJPPcqN2zEjzqjqdkW6lAunGcY2pi58QAsKqZhDJN-0cRlbvaEukEtsvIhYuyi3ndbw01-3FFIa_TYWswXtHfMvlceKCSHQPWM_hJ4qnobmbQx9h65l_5LDaZYQ4Q7t6RdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ6WYb3NOeRV8Zyw9dBXz-UoERm5n8sl6V_ycLmoCZVyH5xqdWQo25v1uKBNZoBY-ivrHyyBYwQ0LICYzv9vOetokEuwyvJMc31Kk9uZYeBmDLfRBNZeKExFm19G_jzCd17V3pwwr8FgcvyhORFMt4LqA7EXDhyXaIdl4ocnuijnkZPoDrx5w2Cvgrf5pOU2SLFYNHkrPspXR64vR45yDqWSe6Hj9-vQhHH9aay_1vQ7c8BkkkJgexuHiY5PG-CUF7EcvksMoyU6k4CxNJGHi7AOPE-mGaRgiVjgf9tjwL_WKabwhS0eoup_6VVc_fnAMu78XvNDToiHa1dlCf4UIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tRJVoDmQs2KEfo06KKTfoB5v5sbZYjJ3alBAxdFKNIHSa1_-WJzIQwyyHSNI8su0ZpUXYYIQiKos4dYzzXmSNjQtFUmcYGNla4tj6d2QrDxBsBxYPSQqczsiXT1HiBMxolOUin-tWT-WhAZVgpsfQTzQQCU8KkxBOmUQK1J992eXKONVKf0Lw4oG6NDNwZLTL3xC5VOJGW5IdmXYYBezK15R_RcbfXuteyfBBYGSdjVzP7L0JBP5BAIxKrSTeP8ytjKzWH5DbrXkh4LY1cC_Ni1dtwBJSqbFrgXZ65xER2TpdJVo091Qrv5zHBG5_xmsyAbLykodArD_BwrGRol6GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfpu7XZcDGf2jrc0uGvf-0dcJSCOaUs8zpnMCYXIbnR2nqq8aJotf7nX_vdNGFZ7sg4cAEB6YDpaRyOrFWmrNZsUC8ZXc9WmRqaz4Rbxbm2KBOaJQQ9JmIiHDMs2Gxt5EnKMcsQfbggasNZCrvTQ-CUH4Zx_XFnjuTNG5zEFgwGZCm64AXzmo7Qocs-Jt9vPZQoURr-nzVDwtCCrr7B0Bvqndut4McirElA5bxk4-noRneYVFa2m4AoQSRYmnSaMpY8HAcePCe8jmN6uhJaObldueHQMPD-fHbK6AGN8nu_t-cX2mDDLBBISXPn-oAGsJ_x41Kc261QFbj_JTJeWOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=U5Lz3SeBff0z-XKAvVL-gr99-gDsA2yWgbIIgf0zki04TwqQsJ7TvDK2Fixdte6deuFPlp0nAWjhmJnLqtbBEsEAkThLuHaKxiF1QlX_31UZJsjXm1f7XIdVIE0gkvVONdyYqMLrKTiTJP3tawSR68-OQqt8njHn39emZeWAZSAgwOtNGJyY6qIcEdC8-XgM2pEjltBb46-bbbYw1KuvCjXVJ9l-eJRE0U0dCUoOTUmM3EZ92gVdltCf3VbA03Fjc7MNPVtdG3rn2RN4K-TsdKKdLM2Xk8IylrJeJdikxPC0fQiBnl4z59_TimwTnEhUiXAbl4GnmMozg-ESeCv-bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=U5Lz3SeBff0z-XKAvVL-gr99-gDsA2yWgbIIgf0zki04TwqQsJ7TvDK2Fixdte6deuFPlp0nAWjhmJnLqtbBEsEAkThLuHaKxiF1QlX_31UZJsjXm1f7XIdVIE0gkvVONdyYqMLrKTiTJP3tawSR68-OQqt8njHn39emZeWAZSAgwOtNGJyY6qIcEdC8-XgM2pEjltBb46-bbbYw1KuvCjXVJ9l-eJRE0U0dCUoOTUmM3EZ92gVdltCf3VbA03Fjc7MNPVtdG3rn2RN4K-TsdKKdLM2Xk8IylrJeJdikxPC0fQiBnl4z59_TimwTnEhUiXAbl4GnmMozg-ESeCv-bTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=nafX1gz7CPOPmT22AqkBDq7YGS1nM-rbh3jH08QlDGryMK0p8ywz3LeAzT-ZpoPc_cbV1-AMsHgDiLxmxN21EYAjeB9iTnQhSJGAqQM_VfoQ15UeLYCRfro0ZY4ylOVlj7owQZw6h6lCweOtyYLSbq33HSInstHXoJPQy2jT2CmZsYnABeGBQX8poN9IpsOxMjn9wMwbx_Kc6o8IKeFPRHTVd5VIhHJ7yOsBCCOIeFP002Uz4u1jK4DknyoIGivpSwPqQJedFA2EKdZBC4WDM6OAjq2lfg_pYEXtWZ-NTR0I1gdRdBv54pX20gRZV1A6uOxZsEdHrZRakcmitCxGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=nafX1gz7CPOPmT22AqkBDq7YGS1nM-rbh3jH08QlDGryMK0p8ywz3LeAzT-ZpoPc_cbV1-AMsHgDiLxmxN21EYAjeB9iTnQhSJGAqQM_VfoQ15UeLYCRfro0ZY4ylOVlj7owQZw6h6lCweOtyYLSbq33HSInstHXoJPQy2jT2CmZsYnABeGBQX8poN9IpsOxMjn9wMwbx_Kc6o8IKeFPRHTVd5VIhHJ7yOsBCCOIeFP002Uz4u1jK4DknyoIGivpSwPqQJedFA2EKdZBC4WDM6OAjq2lfg_pYEXtWZ-NTR0I1gdRdBv54pX20gRZV1A6uOxZsEdHrZRakcmitCxGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=Bzraz6Ry1CHiVvu5ONdRB4d7m2FTMlURmz9ZiJlX59MPavL7pwMkCQud3wlzPM4z13mOpQr68CK5-iQcW2HG-mAXbLcSfJe4aNB6ruashWAaUTmh_mfqR7g4os0kiTugAUTnqvU3wpbMGztPgDZfxIlWD64LkmtuNRUPQcfv0pFVp7PKK6a8qNQ2fPwxLAFjp1Za1r33HNM0nNdJ9R28UWVXhC5u4axAeVNM-z_xR4oqsJvrv6eGaZC7XOgGAmW-8fFDZldLSnAV0ChOo4BD4T5R97Mq_-lcvjusR3L0MBf51CcALyEq0zpg3ZcfMlCKsRyIYen0gyRHWx0nnqerdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=Bzraz6Ry1CHiVvu5ONdRB4d7m2FTMlURmz9ZiJlX59MPavL7pwMkCQud3wlzPM4z13mOpQr68CK5-iQcW2HG-mAXbLcSfJe4aNB6ruashWAaUTmh_mfqR7g4os0kiTugAUTnqvU3wpbMGztPgDZfxIlWD64LkmtuNRUPQcfv0pFVp7PKK6a8qNQ2fPwxLAFjp1Za1r33HNM0nNdJ9R28UWVXhC5u4axAeVNM-z_xR4oqsJvrv6eGaZC7XOgGAmW-8fFDZldLSnAV0ChOo4BD4T5R97Mq_-lcvjusR3L0MBf51CcALyEq0zpg3ZcfMlCKsRyIYen0gyRHWx0nnqerdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ_EJhGBO6x1ZQ1WtJPo0c64Ud2XFefcNezfV5PGCDvKehxYS78tB5mFRJBBUxAUxcv3av05IdJjW34vr047F4APqk0iMGZuVOvTJsN0HV3pwq-Puedpr59zSa2_nEAL7StRTpR7knHTyRxAxsejUQY8j7akYLARD57-QUK69D2-2awSEJSQszbufe559itBaeTYorvZDLdkKBCC04uYxnHgCp7WnicRQMiE_c2YuOA2Cb-__-QqugOXI5YdXp1-bcb4ai-Xr5wnSINbk-CKnzsn2x4xKTmh5njCgUq9nXdiybU61LdEZhYj2FAgASDjl7TyQfdO9d8Q8SBo4Myn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=T-nTWBkiJ_fReW2dK8PehRpCp57YEOIoiV-gkA7fiBIEKhxz6zHmLoS2UFJK5OclsD01DQ94Ov2sq82BKwo-cvk0bPEFo4t_80tsoMopHf4r_m82E0gWH8eQmt9w8xMEhj00qXlAB5kxO5AZLLwm65akERvVfmU7z23C_BNXpLQEA6snWZ4F1LixA4ZcXOMUMULWEpQoRzo5xdYzfUuHMM-46KhJmq2NE4nRrCWBS_k2vcjAAhE5pK2SH84mcBk4M-F7TIs4bMgIRfXokTtM_2qBR2-iRedzuyCTMjp7HXVzDOkv6NovPdsrZDofTgM9Ava3yTI1MHaLdR9ULqYjCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=T-nTWBkiJ_fReW2dK8PehRpCp57YEOIoiV-gkA7fiBIEKhxz6zHmLoS2UFJK5OclsD01DQ94Ov2sq82BKwo-cvk0bPEFo4t_80tsoMopHf4r_m82E0gWH8eQmt9w8xMEhj00qXlAB5kxO5AZLLwm65akERvVfmU7z23C_BNXpLQEA6snWZ4F1LixA4ZcXOMUMULWEpQoRzo5xdYzfUuHMM-46KhJmq2NE4nRrCWBS_k2vcjAAhE5pK2SH84mcBk4M-F7TIs4bMgIRfXokTtM_2qBR2-iRedzuyCTMjp7HXVzDOkv6NovPdsrZDofTgM9Ava3yTI1MHaLdR9ULqYjCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=tTa1hMK5UZKqLuPbMrZ9IK6Kp-L6scdtSiLtIaJ2tm5LwSytDM5t2RKeTsntuarbkaBTPUsxjvzqvcoGL7Kj_AZxDZBp7JYPFqC3a6eQY0hOEGvUu5pCoHc8NLyQxqwbocXVp5OLfXjvvSPeS9l-_7LyV2OIMem_jlsdzw5lI9jkPbjOtuSwYcFrf4TGV3E-jULoLNtC6DRoo0M5EMKZ_HcrQjO0dPpDpU3-eekU6F6Q1eizdxV8Tma7VIvhF-noRNFFsag8BIY_JEgQ-60ICA2i9WYRWeuD3XWUCS8VjFAEkWx_pYRLqWUpOf4rbTwcqEpBfK_WDY5-WFtrXd8fFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=tTa1hMK5UZKqLuPbMrZ9IK6Kp-L6scdtSiLtIaJ2tm5LwSytDM5t2RKeTsntuarbkaBTPUsxjvzqvcoGL7Kj_AZxDZBp7JYPFqC3a6eQY0hOEGvUu5pCoHc8NLyQxqwbocXVp5OLfXjvvSPeS9l-_7LyV2OIMem_jlsdzw5lI9jkPbjOtuSwYcFrf4TGV3E-jULoLNtC6DRoo0M5EMKZ_HcrQjO0dPpDpU3-eekU6F6Q1eizdxV8Tma7VIvhF-noRNFFsag8BIY_JEgQ-60ICA2i9WYRWeuD3XWUCS8VjFAEkWx_pYRLqWUpOf4rbTwcqEpBfK_WDY5-WFtrXd8fFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=gBqp6BxrBkKRkqatFjP3nvZR4C3oln7f-AeVnMHfoleyI_14JTGeafmwnSN_X0jtJDNW5bLO_UrXDqeKIc3PYFMpDqYFaSiGAaW8XAdbEcxSIliSyVdNhVkkNLy14PW8TTJFMeAqGHlmZfFI1Ssli7c58t0CyVrUfBFFufiqJg5sVvtqz-qqljP-W8vWN0HK0mOLg_-RG7Ljpwdyg4iQJFN_o1NL7hW17iaS-IPXvVpyUin6iDCXQXNCsfyCef90813Dv78pJaT5sje3tH70No0RPAl_Lz24buY0b83cV803TxZp-3Q6Nx2PnxrSiLwLy_UuM1kmKxSnphOHgR4cAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=gBqp6BxrBkKRkqatFjP3nvZR4C3oln7f-AeVnMHfoleyI_14JTGeafmwnSN_X0jtJDNW5bLO_UrXDqeKIc3PYFMpDqYFaSiGAaW8XAdbEcxSIliSyVdNhVkkNLy14PW8TTJFMeAqGHlmZfFI1Ssli7c58t0CyVrUfBFFufiqJg5sVvtqz-qqljP-W8vWN0HK0mOLg_-RG7Ljpwdyg4iQJFN_o1NL7hW17iaS-IPXvVpyUin6iDCXQXNCsfyCef90813Dv78pJaT5sje3tH70No0RPAl_Lz24buY0b83cV803TxZp-3Q6Nx2PnxrSiLwLy_UuM1kmKxSnphOHgR4cAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ds-IHKUg8HZKsUWpKSf-TJyQRM3lJPjsI-0a6jXtdUH73ALXJdwvh7SSXxmyhbkUUNaU9RfBYrHLKX3OGv-yN0FZco8ifbuC6M3gH3lLINmgkq2gfVIM9NUwC5x7ayXeIEKLMT5gRq2i6F-rOWcswOda0ZAz_N19_xhBQBWHXRw26baj_5PkjA4LEfusTrv0ptnuRpda1ARpRdW6x411kot2T8DjeeZvj-YSDi32rSXlmgc-HXFf_qXIpJRbkSJ7tJgYZy0oLdv9hg1hKLnVWRaPNJAmD9V1ctpJm1oiZX4qay826JV3RtKsZsgaV2k0iGTUHCxcvPCljnZx0EP8GiPN_hcoaWZE784Vb_gBRdOTkEiXIzjSkyUgd9Lre-KmzEMRb8fxWSowZfcIzYSYtNd3GirQCZh9p1k82JUmnwn_hiB81fAT_UovcI7uUXq7AAva2EoDLjfZ8FIjyysh4ZMhPknNSAURaJjneZvL5_ENrZ5YlnyGioPaHIc8lqv0cLNNPSaelr-ATO_TdMIVY0DjaXQsobCbcLqgd7TC7pdpkZfaRk3VuDwzYXbsI4FdN3CZvjO1pUBe7GS9SaH6RF2wxVPc3W0DRg9F06bV6AEKaX_FAqwExu3IH33eWoB57gEsUwsrCCk1DelfLeBrOtMs_vx9X35T0DK7xI2yMo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=Ds-IHKUg8HZKsUWpKSf-TJyQRM3lJPjsI-0a6jXtdUH73ALXJdwvh7SSXxmyhbkUUNaU9RfBYrHLKX3OGv-yN0FZco8ifbuC6M3gH3lLINmgkq2gfVIM9NUwC5x7ayXeIEKLMT5gRq2i6F-rOWcswOda0ZAz_N19_xhBQBWHXRw26baj_5PkjA4LEfusTrv0ptnuRpda1ARpRdW6x411kot2T8DjeeZvj-YSDi32rSXlmgc-HXFf_qXIpJRbkSJ7tJgYZy0oLdv9hg1hKLnVWRaPNJAmD9V1ctpJm1oiZX4qay826JV3RtKsZsgaV2k0iGTUHCxcvPCljnZx0EP8GiPN_hcoaWZE784Vb_gBRdOTkEiXIzjSkyUgd9Lre-KmzEMRb8fxWSowZfcIzYSYtNd3GirQCZh9p1k82JUmnwn_hiB81fAT_UovcI7uUXq7AAva2EoDLjfZ8FIjyysh4ZMhPknNSAURaJjneZvL5_ENrZ5YlnyGioPaHIc8lqv0cLNNPSaelr-ATO_TdMIVY0DjaXQsobCbcLqgd7TC7pdpkZfaRk3VuDwzYXbsI4FdN3CZvjO1pUBe7GS9SaH6RF2wxVPc3W0DRg9F06bV6AEKaX_FAqwExu3IH33eWoB57gEsUwsrCCk1DelfLeBrOtMs_vx9X35T0DK7xI2yMo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=VE-lHdUnmEEEMIIsAVxwY0p4zCv__uw1mNVQCUA771HookGrNDTMCihqmckSE3VjybryPB79BuBD6pGHi7bf2YXw4JOv0fDxneYIWRQ61ZLl1_FtdE93iHx7ysydi9CHtx6hz4hciDLVMgP2cOn1S1Gk4-8yqsY1ksi9tiJfHUooXwaxf4U6ONwqmL_dLghQO8qi6HFPP8CTGKeZbKVxqbKPI2n1V76f-FgzhN3H8SeKFQetM6387Y4mdkgGLl3EuyWvd9B9l4U8cscJviLj47WbFJBJxz3z-f9qOdeSAm9rqKar3lUijmwoNX8c1zlj6T7KuUfseCka1Z1M3LmfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=VE-lHdUnmEEEMIIsAVxwY0p4zCv__uw1mNVQCUA771HookGrNDTMCihqmckSE3VjybryPB79BuBD6pGHi7bf2YXw4JOv0fDxneYIWRQ61ZLl1_FtdE93iHx7ysydi9CHtx6hz4hciDLVMgP2cOn1S1Gk4-8yqsY1ksi9tiJfHUooXwaxf4U6ONwqmL_dLghQO8qi6HFPP8CTGKeZbKVxqbKPI2n1V76f-FgzhN3H8SeKFQetM6387Y4mdkgGLl3EuyWvd9B9l4U8cscJviLj47WbFJBJxz3z-f9qOdeSAm9rqKar3lUijmwoNX8c1zlj6T7KuUfseCka1Z1M3LmfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gUW9qrOcBqTIkIz4jTK2_CeT_xo7j0wPbaXIaq4VbphStFOZy0up2cQWbbKqZ1kl1fgahmABSiVP3OtItHLgm9Mu3gkjAB_YayJmfbIkyUPY6AO95IUClxUFGe63iANWl3VOA1DOrTwWj-dpI5updl6WBwtRMYCfMiXkCuAPfgZw1mu8T87qdeXI0-QZu9gt4OjKYTSyrSzpWCo63HIoc8lpKX0HgRV-uRcoaksG9vUGF1A5lX407i5HjV0hynWOz0g7yqL0w15BRs0eKQ5OCGvux1K-c-BTbyZoYCH5DwCztfl0-MMWdok7z3tbJm2JrkcfXrOeRuiGDD7SdrZzng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gUW9qrOcBqTIkIz4jTK2_CeT_xo7j0wPbaXIaq4VbphStFOZy0up2cQWbbKqZ1kl1fgahmABSiVP3OtItHLgm9Mu3gkjAB_YayJmfbIkyUPY6AO95IUClxUFGe63iANWl3VOA1DOrTwWj-dpI5updl6WBwtRMYCfMiXkCuAPfgZw1mu8T87qdeXI0-QZu9gt4OjKYTSyrSzpWCo63HIoc8lpKX0HgRV-uRcoaksG9vUGF1A5lX407i5HjV0hynWOz0g7yqL0w15BRs0eKQ5OCGvux1K-c-BTbyZoYCH5DwCztfl0-MMWdok7z3tbJm2JrkcfXrOeRuiGDD7SdrZzng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meMAVqnx0xlNLt5WVK3cdOj-myE21Z5-Nnfx-WcYexulXdm2YTWkaGGsxGKbSOgdAPtUya-joAwG7PJU9V-WMo_Q0nMRVEy6h4WF7ozlO0Z_FH6Oys_H580mD6ABuG9DZlaRGjppEVPN0XhHcbV7E3hP0I_km_xRaux3Ty3Lffq2GOCwbQM0tPVp_o_dzX7ZYbSTCzPcDlgLCLy7L8MdkCsQv9S5s-D7fSSRwFT4B-iLdVwv2w7ISScwC_ZldLvEkZz8JgMVUAEra6NEzwMH1pt8ad0IqVIIOw_aXOXxO0axFS-0gF9ahix8gYihScEAC_Cjbqs7QYb_3rDRvxuQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIXhL8C1cSA8tNE0zhmLnkspWjhC2Accxgma5naV_vQv3H16083CUyK1JWZa70uxDUwzu5H4ivVjjLEkyO_c2R91gwxVn3CX8Rm0BKw67lvdThreQWeVuHurs5UFkFX1xxYYpqJcEAe5F7eQvO4Rz1n3QbWxw_Bg1d4BAkCXYv8G7P-YhQ3IgvCzSwN8NFNTwm1QIyaJDT4TNszvGS5S3F4DKOGfeeXDwxqFYWizmNjr9FMTfeoJmMZ-2Dua4rsjiU6cYxA9G82HfgA5Rj8-ttcmtdowDrov4L6-fiijSIirMLvS9F_IdWDlxJThUH3dFkdB84_gbdtBgYW_XL17_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=NE8xmPKmekGj5RkaRs_aN40yQ2qRsFkWQvHUzfpswVXQcqqyaiyIkM2_gKAEky_uLVA7Wb0lPrKCvHfOnS5Z9w3t3IM3nzm6AFdkEX-ApoAkJnmUBorhLTMYXpty1-xP_ST6_Sq7eQSXX11ovL2lcp1c3Butjs6Fh8oOiVCPNsr3rtzRzRJyDzcTReeTRlBNj5ozSJNKhIQ7WBXeWMOnGQhV3pSgAJztEvqkmjAJcWaQwhSRdGP1OZVmLHin5Q3p6WLmA7qBLCU7el-ewwqHztSeJJ87-JUo-0OeYjwWsXyqyNhjiOTNegGKu0-1OZWYsra8heJpue8TVwyZoCaf7pMnhBhNoC-gB1mbwrwwfnqZOaFS-RwLuSQJ3ispD74j2b-rPkahm_3gjGhYxl2qRVV0KS5oGDQVunga2TG64vPuNVyj3D7FFydCJSsFbtwp6Rr0qNK_sVfys9nMOn4L3aN9w8C_ulX-jPZvYpaahwWYkwjEWmtcdGqUluFOUl7WWCwwuu1tIcV3N4yuDhi5oAdIy6zv8XkJW8a1jXvbaHG6cOfQhn2rPnFCZbxwIMkrHe4PF_K2OXg-4k5Hoqjf3qmDPBKmfHJ9IOxhk97PZkSdD84vT48g_oP2SuqsHM2qDyZ17OaIhvcN3xKgVyGpmdmEgIBGsJarUY_2AhQEhzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=NE8xmPKmekGj5RkaRs_aN40yQ2qRsFkWQvHUzfpswVXQcqqyaiyIkM2_gKAEky_uLVA7Wb0lPrKCvHfOnS5Z9w3t3IM3nzm6AFdkEX-ApoAkJnmUBorhLTMYXpty1-xP_ST6_Sq7eQSXX11ovL2lcp1c3Butjs6Fh8oOiVCPNsr3rtzRzRJyDzcTReeTRlBNj5ozSJNKhIQ7WBXeWMOnGQhV3pSgAJztEvqkmjAJcWaQwhSRdGP1OZVmLHin5Q3p6WLmA7qBLCU7el-ewwqHztSeJJ87-JUo-0OeYjwWsXyqyNhjiOTNegGKu0-1OZWYsra8heJpue8TVwyZoCaf7pMnhBhNoC-gB1mbwrwwfnqZOaFS-RwLuSQJ3ispD74j2b-rPkahm_3gjGhYxl2qRVV0KS5oGDQVunga2TG64vPuNVyj3D7FFydCJSsFbtwp6Rr0qNK_sVfys9nMOn4L3aN9w8C_ulX-jPZvYpaahwWYkwjEWmtcdGqUluFOUl7WWCwwuu1tIcV3N4yuDhi5oAdIy6zv8XkJW8a1jXvbaHG6cOfQhn2rPnFCZbxwIMkrHe4PF_K2OXg-4k5Hoqjf3qmDPBKmfHJ9IOxhk97PZkSdD84vT48g_oP2SuqsHM2qDyZ17OaIhvcN3xKgVyGpmdmEgIBGsJarUY_2AhQEhzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfL_hRkXTafwBPCTWhajrTDkSBYt6n6JETArAMycJ3ld_Y02bQtGZNsu1T3D7VA2Vm3-_QkTrj9iBtOZ7Fp4sO1DDvqnpXfiaHdkEdZUVzXXS5TtMw2R2iHSALJBtR4YfuTZrH2JI_iEX8yEycGw28ttBxJuHtQh5FDIwApMIWkGrFttv_FfWTG9UItRP_QO23D1fXpxy96sz3bYdTWfhvLsRRfnYX7H0aaCMykv6mRvkjI2j9OcOoUzmSpYnUpcuo5T2QGY1eNbOQkjiVSwrNpL7wnX6jpAiECdP5qGKEmFZPp5ehy3x6_hREe47XlrKB11nL4DAjLPJm39h3grfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNq5wD3tKFrMbvpb1kQQlM8XgHWPd8TXBxUOfQLvZhpi25WoNCEEhU2KqmCMiBE7FObJf9Qeo-lqmVTRRnNZor5qiakJqKmoyigjucJ9-ikBSOrIfKL7vT0xE96k8twIbVaUYtTZHEJAZTOcxI3LSuP6nyOOo4_fOg3x5MPEs843-fxHFKgsAx4szxIIW_pcKwaqxOHk0Y_s-hncEmExzHU8z1a7plVb7-qrEPu6Sev3hniSBJWWEvYx-zf10ZjnbRi_ymJiPFE1HC_7PKpXQo0-L_S9qeRBtHx1owyWW4mKGyhUmTGRhv5Hn_1yL9w069M8AcmCXz01fHVBvMM7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msbnJQel3VcUu3hwvtDDn-oRMhqqXTeEljAsO8KzISOezRoVArTQ_McHbX9ng0r3JvzCJ_7jXoQCy4AY0A5-vuh3RHP9kZgxKfX4pAnUwRxiA5b_LNCqF5ZJ6Wr9GljL3w7eeLU-r2GAPU6z4nd6aEerKQC1KmRBtceKGxP2-sQlE42qVwZvZhJ-foPPZdogvEawkG4h4BsTYlDLWBgkiF3dNl6TEdLmvYdxBoM3F6mGYWFpRAtlTT4E6-LdjA21dhyTsfd4IvzMtBy28ngzSLS4VCOelLiiC2gHeCGY7tF-NHBmnX0onO5tTFF0H1h3kYGlzLshq9Umm8dGig9ewA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQkhx0bgseC1XJ8Bjexnh-pSDDFl_0TkcLRcAvcgAkPelwQKTAbeXlJsjEoucnYoMcHlgaVbk-1TNdSm2N5-T3aKdV7T4psQhTJYDiutCumJyEgQ8xsfYlw045dW7UpNH00UDlEo_e669RRBBgkSX7B2I9jCTwIwUaaOGDyNZiERUZqkftPlKFdr8NZWbzRzi7MNfub1BqKP0twr4pdfSSZB6c3rk1KSBHh9lS_DW93wvx8rTXd3nsxqZZFkRNOj296IpoF-AZeQtj5JJHsEAMDFUXtIudT3QTR4iJrCjIV4d02dbtxBv4PPoGoSsQaJw39FF5C-JkpATSjoCDn5cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IVa4y64GviYf0pSI58M-ncU9fV_FxLhXTBccGs83DdIlkSrAAV5xAcEryp6mHQmO4QfQsSH21Q1vJpJKnVq5Kky7dbOUeacJkE-jv4FGusoMV7wVwHVyVrfhdzDX6IdLadv2guWzt79TTkPmu6nFNjiH9n8O5xaQmBsAQH9o94HPr1UlZJTnRqrfrzb_eJ5tC4gZx-_phgyhyv08JH5YkCAfEqkt71HQsjM42y5IvNYu-1NcRtU2nF3DdXSDs5b2DBFwd7SE3Y84AlKgavi8eYdEuLMhgefkLqm-ej6jgQO1jgnsmxpdo14eWOurHlnchSxcJCFPgKHFI8drkYwhObPQXH-WudtmH9R3LtiIaPBpPxTSndiD1PtuM_N_DKFTLnD-1vr3YWhdy7PxXqTForBjOuPUQ0K7mXDqTjhYkSwGcxxoZXZtInA14TiaowPdzMu0yPA-FrijZcddQRi_EISQIKD5FAITqsZuhnJiobSKq9WldrMHjYR4t755TeWUG7wJA9K5RX_FjDyddy0QJ06bqdZ7fQxjAAHf_bLnFxlbcp06ERmad8nrmvU-WWsYgfSo8033Q9xzw2NznZjkA3hD9ToQnpbjbK-_k1ByQpvpjfo1WKwSI8JLaFZdH7rBZruWMJ9VcIxB2h6myCs4lns_bD3mXyXCZkglAl0Oheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IVa4y64GviYf0pSI58M-ncU9fV_FxLhXTBccGs83DdIlkSrAAV5xAcEryp6mHQmO4QfQsSH21Q1vJpJKnVq5Kky7dbOUeacJkE-jv4FGusoMV7wVwHVyVrfhdzDX6IdLadv2guWzt79TTkPmu6nFNjiH9n8O5xaQmBsAQH9o94HPr1UlZJTnRqrfrzb_eJ5tC4gZx-_phgyhyv08JH5YkCAfEqkt71HQsjM42y5IvNYu-1NcRtU2nF3DdXSDs5b2DBFwd7SE3Y84AlKgavi8eYdEuLMhgefkLqm-ej6jgQO1jgnsmxpdo14eWOurHlnchSxcJCFPgKHFI8drkYwhObPQXH-WudtmH9R3LtiIaPBpPxTSndiD1PtuM_N_DKFTLnD-1vr3YWhdy7PxXqTForBjOuPUQ0K7mXDqTjhYkSwGcxxoZXZtInA14TiaowPdzMu0yPA-FrijZcddQRi_EISQIKD5FAITqsZuhnJiobSKq9WldrMHjYR4t755TeWUG7wJA9K5RX_FjDyddy0QJ06bqdZ7fQxjAAHf_bLnFxlbcp06ERmad8nrmvU-WWsYgfSo8033Q9xzw2NznZjkA3hD9ToQnpbjbK-_k1ByQpvpjfo1WKwSI8JLaFZdH7rBZruWMJ9VcIxB2h6myCs4lns_bD3mXyXCZkglAl0Oheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Z75Ux0tJzip3L929YRSVDPFHu4IsrRWTwNnXYA-gxgZjnrdvVd450IoUh_yoccqLIEng4AnPaL5E84LNccRSe9mXo3YUsAitk1X_zwlgo2_EL_46Hwfdvybf7YCGb8yYBVyvDOfDnUtXLGaTNsuXqqUdRuUEmYvzZyFqTwXbl8VPQtz8w05i3xww7o-xsFHMBXNYbEwpRFecr-HpGQiNrYC_7NiaYPOyBxjopOIgIHhSEDqdC7EIS-5ikAr6FgNZ2OdW0k5aIgR6JTYBfgGj8FoTMhPivNlPnuU1n8SY8hM_L_8Pykuuwhhy9W1SwGBmQeg0mAo_kO_0IV7SfOhY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Z75Ux0tJzip3L929YRSVDPFHu4IsrRWTwNnXYA-gxgZjnrdvVd450IoUh_yoccqLIEng4AnPaL5E84LNccRSe9mXo3YUsAitk1X_zwlgo2_EL_46Hwfdvybf7YCGb8yYBVyvDOfDnUtXLGaTNsuXqqUdRuUEmYvzZyFqTwXbl8VPQtz8w05i3xww7o-xsFHMBXNYbEwpRFecr-HpGQiNrYC_7NiaYPOyBxjopOIgIHhSEDqdC7EIS-5ikAr6FgNZ2OdW0k5aIgR6JTYBfgGj8FoTMhPivNlPnuU1n8SY8hM_L_8Pykuuwhhy9W1SwGBmQeg0mAo_kO_0IV7SfOhY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdmOn56U50suLDonNRT_qWTKDRvTa6a1zEfgOoJlPdjV7Uaook9Sk4kIlRkWccnH6AJmq4jCjDMIpZHDUWhN5t0Z9SO7rF-Kqh-33nGzfTcVa402Iq-JGvs0J0jrxj6RX9ViRLOoa1S9WBUnMOy00B6J5x0FLllVLieRVHTv3__rjoewMBPFxDFITJTKpMAf2JboBOvHJhUXR96zoUqZhKAWdlKhHvwSfcu9i1dtOKqBR_BGLfQJAS2xBQ2WG2-Ko2jESybDot9Tva3JqlrLWeUXAKQgZaNh63QQ77o5ETl7mFs0NMNCsj5ATVXd4rTwgHTa9VcQ-fkXJ7bvrVXb2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6m-pUpXHfODcNJ8SJylppRmNxzqjyjZzk5ZZ-YxSCSjhs_eiiSBYLWocx-yWS_8GZU9JCTu3t-nL6jHg4rn5k1sMuZKWHcs1hsdm2rD0d8ZZ-xT72tkv-IviPa2OPgDkOdVS14TqC60gBdB5cqY0EMhfN4S9C3jOR1HUWsGz2RhHfe3ldMsdD1AIauOx2FxAImVq7zb4a4hp2sO2Qm83PpSb6gu5HO5IlDKx7NJvYui01SZMmzlE5WaXemEAU08hxmUXpcCKlqfMEXNg_gVr-ZLSTuxQBbYKG1u09Xvjrh-vFNBnoAJ3apSf4g-jRa-h0EnAnACeCZmOO9LFcG8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/la51jaNIfht_-UAXZrhB5jnGOB1euB3eT9iHCvEiamgzErmzTFPZ_JROXPhESFn8bCDceUPjIZMp9I_cCKWX-THQ1In3fRWxasKK0Xd8w5V7S8QbphdrnYKXBw_k23el58qiFpya0sprTrlpgDNyL7923nJGdPqFw7G47xhO6D80YihjaUxf5Eb59gz5SmuERPh755LKNb3ds91yARUozdbJ97oz1512Y0nWbHJ05N35IB0TGmqGBsCP7mBCfvUj5mNSdSV5Zal8PpmAfi-fN5ao_sE8HpTyelUUfO4Or88Vd8Z3yCdSW6HK6IFBYvaB8DbEqGfvJJJJmzOYVdjoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jm7fXSeUs8Ia1aonfoeaZgnbJgLeXvR71-1uKgeeI9L_omV32FlIJt1_oAsiAsdC5WAEwsVm_lZVuXBrWNGgig_Fx09yVJF6TS0y7bHQvN9QxEVJTdl3aoXEnGbnHy6DSIwrikSN8vIxmL1MDI-SVou6K5zvRCqcORm0qKnujVy5WRJiN50JI46_Ce-mfoXjBGWO2xiUp0y8GnYhz-KtZFNGdSSPpTBQm5KpycSM5FACGGRXq3fGApHXID_I8Th62SMsvg2qBnoNAQi-fugGXf31fM9Y-9ym0UsKelG4-w5duyhFxUSq1jXr9z4bcD4tI1VfwIP7usWLEG5RT3S8Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6i7Ta21B2WhBgmQCokwwwB1AEYMeEUCvyi-A2zHu7B8lav63Vrl1xyfsNRP_Qq0chQ66e4is2CFtWUBsGLE_EDCitFqEG550JhguilZiArY57QJP3VyiFiVSHgSli2PPOmYdce2kRc78ANLwt5bCL-5IGONhPbZFOBKlyXvG_iMbbVnbghn5KQtpB4Fmvh8bbIc6NizKit4n7R_bHoKgWWEBy08uFkqygk3W5k3hXILtY-fZcx8yhaG43jDIhsatLtwjw9ln3OmdSkWB-PeJM77vLmwJfE0GefVud8-ijeBdvrpOtOWrNWE2HSvTU8LDv8TqFebqXqD8dc8wYDLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxs729LUwmWpEJQoyVJTCjEF0nNiZcC5ogvh0W9OTrpMUZSvbo9MxAh1b1hL6PIf6x0Z_V5dlsTJRdKd1nbtnKmr2URLQVeTd93mL6J_FcYxbKD3YbizWGAlXUzhsPiniO1kJrewHofdo4guow_YQQw7cJtCgfG6qYkq40UoIxFEWHGFhBDDSfTZhIX1wn84TWb9js3Oz3gjkLc7yDIvdgxE4iXw7Bb2244r7tjLgzNBdKFyJ0_rSU5KJp8Fxyq2VYHOUzRADrMQ6XKGBdkxgbfPL4xVG4GrSb9JA8kRWPaHdFoq552cZeb6r0k-2Y4wY6Jb1JAHVltvgpEk4c9bXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAa2O1SWJjLih2wIXdSHV2YUh-SfHflIm6CiCa_0rUQWb_NgA_lQTRELFrpZ-WIEhRJcsxQxQb2gsRUGgPTRXZKA2C71USSTy6JxJCNLcbSF_3h7MCM5y-LY-WYSbhi2JMucNrzFVVS47wxIwNVSQ7ycR9_SzXb56rp0zlsaNPrcWXKL8S_ZYM-Wl8_cBWTfeC7gzjCBVFt-F-6D85SE2lEQWRonibuxERGQitT3oFFR2C3D_Sk5qGYpaQHey6TXbeRbv8vlWzWIv56ZyyTXNsnvsWpRlb6Zx5gupk1q_IOwrearTeKVakVhfqI6Qg4qUWhHhw0PS8ZtK4OWaVEvTA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=k-2o5MLdhvDJLQ4NnKSDQWzTxkP467LqGZO9MXf61tdhceJ3JZrTwRcinLh1v5Jih3JP2_NYDJlhJ0OLcx-gBRnfpQBw7xOlncvk_ZJ7Zrt1OFUQvubq_Sa3Om-6IBR9lJoWaIaYdJeV5-hdSn8918mlHbSJfvCP3ghzFcwScIv_03IJkc4yPLlAf50hzs-ATqcTQn0wGj8gxd_pRO-N5zwloXGaA5w2-RoBGNU3cqLjJ6sR5FzpLAQpy124dF8dnhSZUxTB1IB0JnB__MxREQuuxJBB2SAGfkuBvBzJsMZcSKEkd9GJmiYk6yyRGK4uz1de7GUEdQgcCN4i7tfBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=k-2o5MLdhvDJLQ4NnKSDQWzTxkP467LqGZO9MXf61tdhceJ3JZrTwRcinLh1v5Jih3JP2_NYDJlhJ0OLcx-gBRnfpQBw7xOlncvk_ZJ7Zrt1OFUQvubq_Sa3Om-6IBR9lJoWaIaYdJeV5-hdSn8918mlHbSJfvCP3ghzFcwScIv_03IJkc4yPLlAf50hzs-ATqcTQn0wGj8gxd_pRO-N5zwloXGaA5w2-RoBGNU3cqLjJ6sR5FzpLAQpy124dF8dnhSZUxTB1IB0JnB__MxREQuuxJBB2SAGfkuBvBzJsMZcSKEkd9GJmiYk6yyRGK4uz1de7GUEdQgcCN4i7tfBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwO7iHd0m65SkR0s8vh-Dj8Nn9VWt-wStLa5PO5lVRQDdV3qMGWm4Yypbfa4rlVwAPtORoJM-U_rX39CG8O3fsio1bVuAfEYhuXfPW2M0Ppc12Igr1o6jfIHam2Af6z4v_Jsxocj1AqI0mKSO3O9Kw-Jme9dUWutavT_3t-hVUf5yXcPHtEUkVBMK9mQ8u2_C-_BTMjGClloJOE20FHCeZvBUIlFywNyJnZX8L2PC7eypH2xb6Z8PKBsczaHxAImEQP4oAYjec3M-HBuRTMWmVGk-9U1PL5gv5Dl4lRr7Y5BpdllF2v2hXTLYkCWdmQaWaWd-kDg5fM52TulprrWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=A1d9xpXYsbYCoYXLddi0-7I73k1foVSqYalJwHJIuz34_MW1xg80G21FF4DUjFtng9Y7izhl6QdsJYYL8UeCs8uWxamFdDd0QkFWSRasdeZQkbi3GvUJvVjC4cE_EqiI1EzhO4Xu3zLKGIv3UMNHxJNQeh3JKtEewSkpG9yNQDcbDG-fYnyahrWBo9zG3sLuwXS3HM83grQy3GhVvq0Ro01LWVYMtIcb6ojVY2pZkgZ7hVKqWbSS8peD8uj5fZRIl8CNt4zb1ylozj-7R5U6ORQvoW-uvj4uyT6pgZ46FXzHPaZTSj4EmbWkH5fR9l60uu-trL5hsFrRX2a3pVDhsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=A1d9xpXYsbYCoYXLddi0-7I73k1foVSqYalJwHJIuz34_MW1xg80G21FF4DUjFtng9Y7izhl6QdsJYYL8UeCs8uWxamFdDd0QkFWSRasdeZQkbi3GvUJvVjC4cE_EqiI1EzhO4Xu3zLKGIv3UMNHxJNQeh3JKtEewSkpG9yNQDcbDG-fYnyahrWBo9zG3sLuwXS3HM83grQy3GhVvq0Ro01LWVYMtIcb6ojVY2pZkgZ7hVKqWbSS8peD8uj5fZRIl8CNt4zb1ylozj-7R5U6ORQvoW-uvj4uyT6pgZ46FXzHPaZTSj4EmbWkH5fR9l60uu-trL5hsFrRX2a3pVDhsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvhVU6EAN_QU1J6jxobxKeuz1rClS4ktJth1eD8UYbOUP618brFEB6duGNjGtKt508bt2Kj9ktnh8cWUoWZliyni7MVYVuQbMiH7zeR5Jk8bN6MZReILqQEs69aJlINp0ym4AXSF8GDVqlS2CKk2HuDue7LD4kWTp62jvqqvAznUrtCCCBHLZ_tQyi7qIZvpNHZwiDJtA6g7roS-Q2gfER9b_5nolddVkrX8HyJB1aQcm0IGnJxjq5TYop55BCWXpFb3V2AG3Q-MQSMmR6AROZCFDZB2g4V3RD-Dq0l9o4QtKmY7FGx4jhNc9-8prJOH2LlSQP5ZupYxqa6Njg3wLw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDKtnBrutSolWpvCqxK-Ezo2FccT3H96wNuk31O8sfsKR4LQWyb2suz1vxZgAn1taP_ZB43gCUs7JeGESLZumb22LJT3DruS1Rh6zMp4URSwK98dV7z6tLzIDGJzBYNEgKzI0TXvBHKumwsrPrsdty72tM8jhOYQQ9y40XknENdxUP4GbkYIWo3jaZNiOqJC78tpepSRyNfK_5YFXUAjsUYQn3J6Jqn48XQK_THrYDR78XCKMaTZh7rubl6ENweIeBam1406EDpBDhiAuhtljSbFaIWOjULCdIGu1HoiPkrZKvaam8TRKvYSNgNWaSz6dzpYu2SEC5LJiUfoRuGRtr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDKtnBrutSolWpvCqxK-Ezo2FccT3H96wNuk31O8sfsKR4LQWyb2suz1vxZgAn1taP_ZB43gCUs7JeGESLZumb22LJT3DruS1Rh6zMp4URSwK98dV7z6tLzIDGJzBYNEgKzI0TXvBHKumwsrPrsdty72tM8jhOYQQ9y40XknENdxUP4GbkYIWo3jaZNiOqJC78tpepSRyNfK_5YFXUAjsUYQn3J6Jqn48XQK_THrYDR78XCKMaTZh7rubl6ENweIeBam1406EDpBDhiAuhtljSbFaIWOjULCdIGu1HoiPkrZKvaam8TRKvYSNgNWaSz6dzpYu2SEC5LJiUfoRuGRtr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
