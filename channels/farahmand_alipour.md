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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 02:57:18</div>
<hr>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpLPTPAcRiz1elQUzrUfPOCpSQZeB4iGjRyAwRp4HonHjcdMhY7NZRLkmo7-9QFN9C5c0_aegQpyXbejKZcjgPw6t5K7aqV9REpUy1rujqhR5Jt357hGFcuE2dwZBYgh6AAxCu1qvLy3K8I73_s5EPvomn0hKqmk7XRJkGNVE3XdLm61Q3EcoS4kmyOQwIZ9wNdnrjyNAzDlazrkRR-reTfgzMwQiPTbRnylYsyxBMoeN9dnanbNTi1DA-bi_PKzF2ks9XJsr463RcRNATeJx_eQnjdxQWVkAH7bcHxUrfEiGzI_uBciBhH_dABFdWWc_FYmDhssxvd3MgaNcXRnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNuMdVD-fiLCMbNkMTuiwrtmpE0AU6Yx68mxqOMQUfVVK0KMdJUv1xcoC6BZUtp_A5BzoYG7Msy_HUfsgElcAhuaAfQ6nL3FB-zJSjeLnYHMAdUenO_uDxKLvaZpvUDaglECE1ONt3pSk9yqfXuRQ2YAJEcDVxouGiPeeiDKq1qhBD127nI_FCTWJjdvwapO2Hdl01-AldCIsGEfbk7V08UVHFcwQpV6HUfnripFPsCHT0N_b4wz4GxCcRzySb_TTLK9pKPVLs8R6EDAoqdLdJ4hO7RdvcUUiuSEFMiDgWe0xx3zDE3znSIqD_8jEuisuO9OIt45cvhV2c76E5EwmA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nm7lndpxC3mdo2-oNecqit8Wru030ZMlqctM1c4MPqg2JXKCT5hzEU_h4At2xu1JSi2opv7-2Tijkcu38FXjBTjoqR0g29mezCEpGYmw4nOyJNYcHg514fIjXJmnypkYDkD7i4ip0W7Zd8bW4yKaOOo_idR57ALgA09uTwDCiSmP_FbmEllB2Fkgw--WRjSm9Ip9JcovkIwwghTiuYohE2Zwc_cYl26y6keYqzOBpANBwFhKZojCzqMtCeAaovUshuyC6IbqonKCykux0uGScw7IAGYZ7GvpNL0hG1YVkbcui6_mSChwRg7hlUVSIvZRQwJB8mFjCmj4KMfqnKGhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=nm7lndpxC3mdo2-oNecqit8Wru030ZMlqctM1c4MPqg2JXKCT5hzEU_h4At2xu1JSi2opv7-2Tijkcu38FXjBTjoqR0g29mezCEpGYmw4nOyJNYcHg514fIjXJmnypkYDkD7i4ip0W7Zd8bW4yKaOOo_idR57ALgA09uTwDCiSmP_FbmEllB2Fkgw--WRjSm9Ip9JcovkIwwghTiuYohE2Zwc_cYl26y6keYqzOBpANBwFhKZojCzqMtCeAaovUshuyC6IbqonKCykux0uGScw7IAGYZ7GvpNL0hG1YVkbcui6_mSChwRg7hlUVSIvZRQwJB8mFjCmj4KMfqnKGhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Kws1LAy0IA8bFBrzyViAziTc1yBwKowk3THdD5dChT4SHw0ZAhBs7bSoHtLwX8lvWpIDUHubQb2OvOlN-OnJ_ZVMeTNKusGvW12jsyHIIkveFtrVe2Z-9HDtZ6puQo_KxmwPCCwJ3WiTxzMWSkkSNTXegCor0VnN2M0Iw4BvRdYGf6JQ-Imk6rRfV3Z4dfdkePDaHV7VGxcv27ROaKkmeuKN3Bk7BzrI4Wzdg5I4sEDeeLu7zFSBcZVBtWX2Uuuan1NZdj4z0C3D8jEeb5JJCYmnpRreK4QIgaq_HmzVrpucrbbkF2px7hhmzZf-01-hTGUGJnRNRcNTgY1s8mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STXETMr5FkrbSg5lb0b5_JpXIaQ5T9-iX3-IaeLlzigN-K78BzUpyIXq2iHka0oRdC2LtxVysbYDJeXKgyHrhej8Ss4uqaq9G9uJJMdD3tqKENV_shWuoPtT7FBKcvlxmtDz9cxJaGMENYmu4YngBCILSpW9bRw1XxnRpRL2IDdwjJT6vu6xiRXmX3wWuTJah9NSg47LYaEf0tUNBrEid8iK4ozIE8O3lDsZjN8VQGK6D4rqAdSvMyszmKMhje-no0QGXrM3Y_jknQv74je74jfl5kVmGxLDE9c199MNqMSHZYp8ERrQj2C15gOs6loTGOp9SpOZ9lAwIzlSwKhTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Trvh-VP0JPsWJ-B5F0RLcnFzaOjWbTy_V0w1jRP1hShNLZSPq_CnQ2NrAfMN12_FcjHIVCPCGx1sUsWKwUroQrS7ZXKzdkemDNg6_EDRAkqJA4KDScAWBY7gjnVR7mo-FJkfFMSUw6OlThUrr8HeOygnHtbpPvGQFru1ZbGHLdTXiVxr81Z4T8REIuEvGKze1VAI_do76a8AfHe26-A5K4dVg1Vp6aqa3VmQSI2bkAfGgz3p0P14LU1GmM8JsXLy-yPRdD_esy_OUBAZ5cSbRimjItVpi-roq4H9eiXr7llYqrZNebMkwL-Ygws3mjY7dwK5hJ8d6Dsd3w1l5AyonA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaMczlNd_XaD4PcZNybailk32eqoBdMXD28cdWVhf9ujHT8U_tvKQ1cBijldhIqqbXAyZiNZB4L6Z8oJ0x5nj5Pai4Dwza-W7zipkfBW4y6AO6tiob7GBUHH8NeEKyJhsZmizpLql4DgW9hpSouMbgsww5S7T9Aaudbyy98zKcPYyluJF43fZjJWXnj9jXmNO-55P7RnpPcCjZZkyE2AW0gTwwa7TX0yc0bOFAoD5RNa-az6Dt2ZaqKcVUWDWbnDpNAnkUwnj5AL55eRWPd7GjwOS_c22p17tnQUtQ6EVMEegHpyc1BidtsVA68hXm4rduRjivqBHOydy0bDd8zqrg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=gzL53I4u7s11FOBUCGRsLXE-DLuFE0pXwcS0b-QD2-ZAJARkxOA7_V_42Zgg8FgvXjE9R1XWgDx2B3MirSVEy_Ia3J_S6Ho_iQ3E-5slCCVO4hmvzubY2pjOlOxAeWUm9wjF96dWwNj8dW3vwbVIdA6SSDOzO5KIcx0n-BlrsvIB1Yk7cbS4zLPWF38gV8xNRemeyE0IAjjWk75XP8md_JmFi2mmtbJr9Xtrggv0q6UbuieJb_IpaVLG-M_KckazC5qYaL9bMj39bbPrEsAM7U2dOIDYX25NT85vf_KdCY7bvHtLgjAQXUtNaxsdCrbbN6JNlkxDLpTnc1c1Aoi18jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=gzL53I4u7s11FOBUCGRsLXE-DLuFE0pXwcS0b-QD2-ZAJARkxOA7_V_42Zgg8FgvXjE9R1XWgDx2B3MirSVEy_Ia3J_S6Ho_iQ3E-5slCCVO4hmvzubY2pjOlOxAeWUm9wjF96dWwNj8dW3vwbVIdA6SSDOzO5KIcx0n-BlrsvIB1Yk7cbS4zLPWF38gV8xNRemeyE0IAjjWk75XP8md_JmFi2mmtbJr9Xtrggv0q6UbuieJb_IpaVLG-M_KckazC5qYaL9bMj39bbPrEsAM7U2dOIDYX25NT85vf_KdCY7bvHtLgjAQXUtNaxsdCrbbN6JNlkxDLpTnc1c1Aoi18jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=hmRfffXLZPdcqwRYDjlM2732Dm7DEw25Ir_VUsKk_TS7upwo_QE4jbGFZNfqLIHvmn2Uwx1wCTfR5ukE0_U1vYE0jswG6QQgi9bMedPTeDMflgCQdVPLfeMtAxms_81j9mWSKPgWkYeDCx2_R-WuKQqROqVq_Qer_S_tYvwFKN0Iyu07zA6fa38OLaz1JiYVOev6zPHnB99GdwIopJk3vGC8sFTkXs8BBzpd6YXXwXnI5869f8clBiVHTqAVNeaPSDy598DuioZ-IUpBOZDo1GbZclex6ilFplfZA9wNzpWHZn7pntOcSwGBCq0BiGUerg7Of1uB6QCSkeU1ml8hWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=hmRfffXLZPdcqwRYDjlM2732Dm7DEw25Ir_VUsKk_TS7upwo_QE4jbGFZNfqLIHvmn2Uwx1wCTfR5ukE0_U1vYE0jswG6QQgi9bMedPTeDMflgCQdVPLfeMtAxms_81j9mWSKPgWkYeDCx2_R-WuKQqROqVq_Qer_S_tYvwFKN0Iyu07zA6fa38OLaz1JiYVOev6zPHnB99GdwIopJk3vGC8sFTkXs8BBzpd6YXXwXnI5869f8clBiVHTqAVNeaPSDy598DuioZ-IUpBOZDo1GbZclex6ilFplfZA9wNzpWHZn7pntOcSwGBCq0BiGUerg7Of1uB6QCSkeU1ml8hWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=brpSIb1HttclGJQFg4MyymxC7ARqD7WVkB5XyD70gpIh8RCG9oiBwkG9EumLadBiy6hWLXfZ_2waUhN-7F2Jn_v8jhU0YpMGcwfRE_dTsHUiiDIJfBAYbCKDAhXSOM37olf1kRTlAHO6M5XNm1AhQSZB-AP0aOffcYzr_3mJ3V82-86ixUfsWjC_iiZL3krlENkOd0R1uDCKzXOo625wbz07UaLuhP0z7LVXuOO9BGxETuzUeQB2VpWTjX3wr9-aCQgXRJgP7bl4_vu0dlqVJpFlb_qJo7GZB4ZaoFbm1e0-Z7tVuG_BsWJ7u_92jXfDdzJL7dMl2O6TNd27w5kukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=brpSIb1HttclGJQFg4MyymxC7ARqD7WVkB5XyD70gpIh8RCG9oiBwkG9EumLadBiy6hWLXfZ_2waUhN-7F2Jn_v8jhU0YpMGcwfRE_dTsHUiiDIJfBAYbCKDAhXSOM37olf1kRTlAHO6M5XNm1AhQSZB-AP0aOffcYzr_3mJ3V82-86ixUfsWjC_iiZL3krlENkOd0R1uDCKzXOo625wbz07UaLuhP0z7LVXuOO9BGxETuzUeQB2VpWTjX3wr9-aCQgXRJgP7bl4_vu0dlqVJpFlb_qJo7GZB4ZaoFbm1e0-Z7tVuG_BsWJ7u_92jXfDdzJL7dMl2O6TNd27w5kukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=DlTK4OOmEF0shcOkPalnuaAmSIudp0-i7ORG_tfoULd0efS-7Sm_-lRAzbMXIMUjNsZ2ZIkJ1eKAoZtkPah4sqFOzScqGmWe6ChKt4bkK8SobmLgZyE2zzNoENUlKG_M3HMSaxp4nsa2pR3n04maRSjNcjqvfdlRlxCERariZYi77a0zJFN4QF_ju_Zipyt28icRQadNteCGLFY5R09lgjyx6hIz6BrDjrosJ1KsohNIgzvqCA-vH1P8GVUuGv_NHCZ9iL3Gs6A3nMkgH-e-zjMkwqPnTV3TK44cdfgQvQOqCjcgpAk2JM9QCa70lIynuAK57N9XnNDlwohUnxgKzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=DlTK4OOmEF0shcOkPalnuaAmSIudp0-i7ORG_tfoULd0efS-7Sm_-lRAzbMXIMUjNsZ2ZIkJ1eKAoZtkPah4sqFOzScqGmWe6ChKt4bkK8SobmLgZyE2zzNoENUlKG_M3HMSaxp4nsa2pR3n04maRSjNcjqvfdlRlxCERariZYi77a0zJFN4QF_ju_Zipyt28icRQadNteCGLFY5R09lgjyx6hIz6BrDjrosJ1KsohNIgzvqCA-vH1P8GVUuGv_NHCZ9iL3Gs6A3nMkgH-e-zjMkwqPnTV3TK44cdfgQvQOqCjcgpAk2JM9QCa70lIynuAK57N9XnNDlwohUnxgKzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=VAkSOD4NzZYOdFl3bxHDcpUaYBtPqQWLVMpl7WcKSGM9CStmbWfYO78H9W9L7M2V_bYL11GAHpn7pO9ZlJ5rYNY7dAOmu55mLgSq_LLy_NQnetbRjw98kvilOFRx0lVLgnB8FgKXhZ5kmOdLdAoGtukDGy5hjW7NBG4vQ3USzSqH4M1NOx_Xg9H5B-XRTVzbycps4g7POlM1gbatVEbeby_NgJAJO5baprGS3n-jca24JnqzcdJcyybOR-yycDj0rMuZS-VxvDGr_j8zQkmS_ThrW2CC6ERcLM0JIdqKvd0bHKFz5m_0aFdAViBbswQJ44tWZ6c69Fw1Uk9xDLWZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=VAkSOD4NzZYOdFl3bxHDcpUaYBtPqQWLVMpl7WcKSGM9CStmbWfYO78H9W9L7M2V_bYL11GAHpn7pO9ZlJ5rYNY7dAOmu55mLgSq_LLy_NQnetbRjw98kvilOFRx0lVLgnB8FgKXhZ5kmOdLdAoGtukDGy5hjW7NBG4vQ3USzSqH4M1NOx_Xg9H5B-XRTVzbycps4g7POlM1gbatVEbeby_NgJAJO5baprGS3n-jca24JnqzcdJcyybOR-yycDj0rMuZS-VxvDGr_j8zQkmS_ThrW2CC6ERcLM0JIdqKvd0bHKFz5m_0aFdAViBbswQJ44tWZ6c69Fw1Uk9xDLWZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=YNXI_YnX-T_Yr9Xxv0LbHz_I9kps3bWF6SEGDHqyNiqqXYs5D46OZgkp7vCRKpmnq9vx9nRiWq5IpRbNpOiZJKE71nCUsQu-4IDnMMLXXR0ipphfAaDrPLMwtFs9IYiSXNH8njwZ04VR0S2bWYZA8sW6dTjQG2Nni1Y9r7VqofzgolPc6MKPsjDC0kv0m697x_TTEMyPMUARxkxlt2nddGoKDc3OOnzU_i4HgOa_vXBqbHr7V7mMghWfE3lLTki6Fv6WxChUgROaoTki6VQnXIPKM9oCLd02RcEMncNG-9y4jtywuG4U2H7usdnPq7RCRqLmV8-85c2wtCQpKpbg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=YNXI_YnX-T_Yr9Xxv0LbHz_I9kps3bWF6SEGDHqyNiqqXYs5D46OZgkp7vCRKpmnq9vx9nRiWq5IpRbNpOiZJKE71nCUsQu-4IDnMMLXXR0ipphfAaDrPLMwtFs9IYiSXNH8njwZ04VR0S2bWYZA8sW6dTjQG2Nni1Y9r7VqofzgolPc6MKPsjDC0kv0m697x_TTEMyPMUARxkxlt2nddGoKDc3OOnzU_i4HgOa_vXBqbHr7V7mMghWfE3lLTki6Fv6WxChUgROaoTki6VQnXIPKM9oCLd02RcEMncNG-9y4jtywuG4U2H7usdnPq7RCRqLmV8-85c2wtCQpKpbg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R51nAfn_VbJJrfO0mMO6D1lwLR-djCLuRUavkmfsUFglH-B6BxNi-s0XNdhMkRz4FoI49ewMwJOsedgI08eZmXIMknGy9_sp63HNA2sc5IBPixopT2H4g-JdV1sHoOat1M8BTZPpSqvJC2XYOLSDoP4WQGg4OQxNE5rzLxP1kHLrYr-Y1x05jwR9DmJziPuUE1LcqWsyGoJos9q0nBBj-iLe7Xft2V4HVO93qTrSrkvDv4gvmSa8DQgzzr4eUGARC8TSp6uaseAZegPafNCxS-u_ttSanY6eydeaiIVJZ7W3icFIUwBOn9j6UJt1vFaYWMLCtErx9AWtUKLPIoTZmqJPiLPeHdOCbC6YTK68xHnEs6NipQThjU2F1or4DnsCwTmoGsHINlKa01TjMDx5OqSg93nw6drVlOuQg1JQ8xO4kGkNHmsnIIoAO5MFwLBN9YE0742JzddxnTmHX9rxWSfT_e9le8telMfGKElCJf3Q6woIksoEBbdBAviL0B67-y7NLaD5lKMUn1gd-PVDt8OzQMOdi4PDlmkXb7sNUPjnzupfSKw3OSs3bEeyjVBiUO4wkQdVg1fLCz_YKIdG764oH_afJKW85dx6Zj1aflB8WxMrplM8tisiUFabfhsVXprQv25o7_nUrHLOum1v3Y6l0rQxy079jjo_xm0nx70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=R51nAfn_VbJJrfO0mMO6D1lwLR-djCLuRUavkmfsUFglH-B6BxNi-s0XNdhMkRz4FoI49ewMwJOsedgI08eZmXIMknGy9_sp63HNA2sc5IBPixopT2H4g-JdV1sHoOat1M8BTZPpSqvJC2XYOLSDoP4WQGg4OQxNE5rzLxP1kHLrYr-Y1x05jwR9DmJziPuUE1LcqWsyGoJos9q0nBBj-iLe7Xft2V4HVO93qTrSrkvDv4gvmSa8DQgzzr4eUGARC8TSp6uaseAZegPafNCxS-u_ttSanY6eydeaiIVJZ7W3icFIUwBOn9j6UJt1vFaYWMLCtErx9AWtUKLPIoTZmqJPiLPeHdOCbC6YTK68xHnEs6NipQThjU2F1or4DnsCwTmoGsHINlKa01TjMDx5OqSg93nw6drVlOuQg1JQ8xO4kGkNHmsnIIoAO5MFwLBN9YE0742JzddxnTmHX9rxWSfT_e9le8telMfGKElCJf3Q6woIksoEBbdBAviL0B67-y7NLaD5lKMUn1gd-PVDt8OzQMOdi4PDlmkXb7sNUPjnzupfSKw3OSs3bEeyjVBiUO4wkQdVg1fLCz_YKIdG764oH_afJKW85dx6Zj1aflB8WxMrplM8tisiUFabfhsVXprQv25o7_nUrHLOum1v3Y6l0rQxy079jjo_xm0nx70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=OWO3QAi0TOuRkwuSMNItcQba5aGc_milVMf2s_MkQQol_5FCviN2Bl_39ECa62rJ9klTG7gF5I0In7kSPMIl2-UpQCLLQEpj-l7MD7mWvl5Wjmfd9L3PYfJvFpNxnGmJ28YSfjQISocISGqObGABJm_SRL1e60tzql_1ne5Fa5p4buMNcoZvP2k7eOj5FLR7dYoaqc7qUw6aIOg-1tcpDJPxluO4IHfgTQRu-CNyc2zXaMjsVZdQnEMrFMzR6TwMvFnFBYDeuerfST1e4MCHoa-epB2DY2ogLWRAMuDfIyjdu0zwWSVpAD1QhcDFDerlEsFK5zY7ii51I8SzAX6s0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=OWO3QAi0TOuRkwuSMNItcQba5aGc_milVMf2s_MkQQol_5FCviN2Bl_39ECa62rJ9klTG7gF5I0In7kSPMIl2-UpQCLLQEpj-l7MD7mWvl5Wjmfd9L3PYfJvFpNxnGmJ28YSfjQISocISGqObGABJm_SRL1e60tzql_1ne5Fa5p4buMNcoZvP2k7eOj5FLR7dYoaqc7qUw6aIOg-1tcpDJPxluO4IHfgTQRu-CNyc2zXaMjsVZdQnEMrFMzR6TwMvFnFBYDeuerfST1e4MCHoa-epB2DY2ogLWRAMuDfIyjdu0zwWSVpAD1QhcDFDerlEsFK5zY7ii51I8SzAX6s0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMVwPLALc26OzEtIlq8761o9oFgU8RJkUcsqod11ruSam9RpSUBppojC6yTg2MjJ2WWn5l_bVKAZ8NCug5BkVT3U1Noqqo__lXGc7mzxv-sAa-uI_KRMKkarEYKPvdPDW9rCih7F4Ounn8R7P_roS8AkxkNYW0JZj0l5yL6-GA1PFjg_IMTZYHAZ1DMRLBR6CHBKucXeyoZ4buloHYMwSWEls9wMgaildV7qij6kxUyzvuh_jQteKXBk2zfBRNDZaVgTWtWvaAxRsHJBIJ8YwsrMNrErpHgQmguXOY2pr-QBw46dh6yJSbX65DL5rrROrmov3P0Tdtr7sw9qs0X6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk4SVRE5QBW0Olub4oFFFGoe8vOfszlNRVXCc6qso6QADSJTRp7cySidO4-1xKdXUejLrAqd0nb5UqDbvz1TRM6j7gUxxVY3meeHJ3jGQkGqCh_uCO_qDEhNRVx-wHuNgjyfEUI2KNFY2fJEVyFxNZph3Cv-fHC_56LSNvRPQJHyntbIhpiPTvaknhaZFjwl-nqFPvLLcDFBWWM3Pq79ih7at9lzM22GulSUpnIkukX3xHDyHLnBqFYtx1BHIBPGOH1Iuuwsphjt9ym3So9oGgBJ611hFW5ozmztEOOJqmMcYO9O3f_WN8Ukn_3duBn9soHOK5MNErES3G93csUcOQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=gxPgDb3BL3vvZRW2OK_zaqa62giygD1KxMGtfpUR5LlXvhedsaycp7xkSWLLXI-rLNp6r96WzaEugRXFuUxD4JrZbCfTGFiE3URORUfVk1Cd8V4Z5qgnBEyWwJgMuAtPNQ0yWwC-eVbRGXMFMaCH8oLetOvANrMSjSFyIgPsrlhZmuEd62V0bPe41nQzHstMMwROoSV0wNK97Weq6KFykIEU2v3-ipSu6jKS-bUucQOKIPAfzjvXLDuDHXpIM_Rvth1sSIrhnJWs-3AUS6ZfHoSDkrmVVvcKdQhviZO7lEnQFUpkFpU1FY-CU1EK9-P8JG0wMHrLbDyuad6vKX2rai-gfSxCwFcd9hz28u_eyHPnUmGHTO_fO0yjCBk_c2_86e23Rlq1TdS5E257RPqaMpQ70yc525wXZV2dTsjXCcmEyHtX2kpQak_No5ODFTeYaOywjK5qyyPfUeUDJXaHFQTZp2Limi8rrhB-vlZWJlDcmA4X-2bPRst6IRxbZA3nJ6OTfVAtaS-iAroa1m9sCLBXbVkq60xNir6UV6leiuxm1StjLPVoUnABGrMlrdXIxkPYqvqVeQ91dR-h6hI5quukt-gxEFNtX1lXWbxUBba9AszDEhktlzr2aPEN3AsB2T4UihbkKWDPrndSChq8l2e3ODOC_gA5EfjfgNdWEqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=gxPgDb3BL3vvZRW2OK_zaqa62giygD1KxMGtfpUR5LlXvhedsaycp7xkSWLLXI-rLNp6r96WzaEugRXFuUxD4JrZbCfTGFiE3URORUfVk1Cd8V4Z5qgnBEyWwJgMuAtPNQ0yWwC-eVbRGXMFMaCH8oLetOvANrMSjSFyIgPsrlhZmuEd62V0bPe41nQzHstMMwROoSV0wNK97Weq6KFykIEU2v3-ipSu6jKS-bUucQOKIPAfzjvXLDuDHXpIM_Rvth1sSIrhnJWs-3AUS6ZfHoSDkrmVVvcKdQhviZO7lEnQFUpkFpU1FY-CU1EK9-P8JG0wMHrLbDyuad6vKX2rai-gfSxCwFcd9hz28u_eyHPnUmGHTO_fO0yjCBk_c2_86e23Rlq1TdS5E257RPqaMpQ70yc525wXZV2dTsjXCcmEyHtX2kpQak_No5ODFTeYaOywjK5qyyPfUeUDJXaHFQTZp2Limi8rrhB-vlZWJlDcmA4X-2bPRst6IRxbZA3nJ6OTfVAtaS-iAroa1m9sCLBXbVkq60xNir6UV6leiuxm1StjLPVoUnABGrMlrdXIxkPYqvqVeQ91dR-h6hI5quukt-gxEFNtX1lXWbxUBba9AszDEhktlzr2aPEN3AsB2T4UihbkKWDPrndSChq8l2e3ODOC_gA5EfjfgNdWEqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1yPciD9jQdMHvKP1Sj9zPieJhV7a8ovEtX0dF0GaKjDWj0TpuC4kBfjeNsLeyLRkX065bpey6VzwwWou3xTBoGv2nK5BQ6xE-j7gCXf1_X5LjDZXka-xYwDQ9xO3iYmPbAtSDKuH_w6CsPrjjSjCuYOpXk9de5gUvPnXXof2zwu4LrMv0GJSe1Jyrwg-BT8iXn9NCVXt1Z46S0uOG7uqMNvC0nysFqMsKVKACkV2D1mccKv5M0M7geO8kElFnfuYS7DmEdFJlE1FX8QkfhoKSPNB9BtQ3WLuC5QxNr4utTu1fNFPgMaKpTKp8tZIEDYTlsjTJCm6G-yQA-JYGCbWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1kG_cF81UwGiMplW0mHQmNjP8CnmrOfXUJAtfoYpOSVLBesReOIvoHrU43oqv7Mya3zPsjXWeR5PMrSKSfZYZBYRbV8iNSNmpeUWIRD-uAKQh1oD2Qis23tcnjfetFPHodqmHPBvvaagB67-kE0Ht6Dfaa8SKRXItGR5KsHavMnnx-f0ZZj18nCHqInX2iGclD770RTHqcnIzUbMxMxebZVFhgbTaj9dPYW1AtqxtPYGyHtRmixAOZasHYECZ7zRHQHK8h8Kc92knXDzmWKyMxng2IkENf7ZA87uOFlKWRG2ZkA4djwTlqwd2zC8qquPXeOLv5XfcJ84ARLGm0nXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8sCcpFfOivhnhjOv3V9oicB1heZiM3ShZNyESa9qmqD40tCdsDmqqFpUiLKNQU5HjEo4P3FuSUcSlqjzDdK4f5zs6qrSrFnBbY8RBe7EFAIOFdnJmS_ebTIpxJPEyUuu83okhvV1DPmv0Qa9_gBciwSf9dhJ3s1j4PbdjS-lj3Wpr11XjdDHHoKpPDi4bALS9MBi80v8SjUzVUyn_3cuwXxyojh3zf5zsSxXQZh-gsz1a0fTjG-mmzXMHRVVy10nMbzMev9e8OGO8oIOgBlHsekOew55tI9RhIPCG0JrMR-XK9fFmsSW-PvCI3Xqcteezs1GeuQhaVqlhjc4pYmjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IQ2dvkOd69612aNAxkGH3jsOXG6g0f0ji6xdwR1FV86h7S47lf94cPgrr7oVpvELmqYc4gUkXIkeI89xviGxtHRaSd4uoGd3CgAAsPtirleci_APjGJV6rTE4t5LwBwceamqLD5cxueX8a5t4T62BRWyUzVkgHP73qTsdj0x7gpkqCB6Stk2ubCw_zzBO7_k0nFnhoYzwY30CAhmgdHGqfuajVGRFJfCsMAJ6mDkairHfzd0a9oM6kIiZefAFxZlTkQF93Rnw-I_GwaAJzSMM1gssqUcDP-HI21CTT0FlgZNe3SFnPNNbKPvcW26e1bzCrD2kWMK7IALH3W1MO7r9mBKGRbcMftmpApUSQWifIUZXP66TONDf_HiVJYKpaScgEagKTA468PQgSFldHdMlY8ss86tYl5zdHFB6ZGWjl168iez3g9yOdFEO9c3xQNIkqqkt0eLsIwVwUi-E9weUbCD64VC0CtsKcXKkWnXPTCgx0itnZqSLQCmle2lv3jQulFdYV0uviNWzNzpWNnLS2Fs7RRGpbzxQjBeRLrp_jA5B1jNJvP2N-mwyu92C3lDyJSVZN_0Ugcoy7uoBlrhxLKMX75zMYhPyXS3tLv2y-XTyu6RzMn_pF96WL8WGyRyeEHFW-y6ZtZBuMn7tnPpXLhaCpqu1onHQZFInsDZQnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=IQ2dvkOd69612aNAxkGH3jsOXG6g0f0ji6xdwR1FV86h7S47lf94cPgrr7oVpvELmqYc4gUkXIkeI89xviGxtHRaSd4uoGd3CgAAsPtirleci_APjGJV6rTE4t5LwBwceamqLD5cxueX8a5t4T62BRWyUzVkgHP73qTsdj0x7gpkqCB6Stk2ubCw_zzBO7_k0nFnhoYzwY30CAhmgdHGqfuajVGRFJfCsMAJ6mDkairHfzd0a9oM6kIiZefAFxZlTkQF93Rnw-I_GwaAJzSMM1gssqUcDP-HI21CTT0FlgZNe3SFnPNNbKPvcW26e1bzCrD2kWMK7IALH3W1MO7r9mBKGRbcMftmpApUSQWifIUZXP66TONDf_HiVJYKpaScgEagKTA468PQgSFldHdMlY8ss86tYl5zdHFB6ZGWjl168iez3g9yOdFEO9c3xQNIkqqkt0eLsIwVwUi-E9weUbCD64VC0CtsKcXKkWnXPTCgx0itnZqSLQCmle2lv3jQulFdYV0uviNWzNzpWNnLS2Fs7RRGpbzxQjBeRLrp_jA5B1jNJvP2N-mwyu92C3lDyJSVZN_0Ugcoy7uoBlrhxLKMX75zMYhPyXS3tLv2y-XTyu6RzMn_pF96WL8WGyRyeEHFW-y6ZtZBuMn7tnPpXLhaCpqu1onHQZFInsDZQnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=bErZHcyFNsp_3zKQIVFi6goEnUJcOSAcyGnqQdE-90db-C_iKXrrFkCWGmDY2yYrHMIuJBxr5-C5Ta3B3iJx_dRyDhEyxzzUWi6JXUs1ggDiSiRZYmYZ2TJ-xSCkCgeodfp2UVdmqTo3OtCtMId7FYfyvAD9RzL9Frd941hGXj1or5dU_H0ATmL3afSxUKKZ3K8UbwUjW7brWMNPGDrBDE3GDpw0XowI8M3CsjcOvnThYFMU9MZgzWQBIa90pG3NQZ65JDb0tXdP9F8ptfvV0DYavibSMgxsW_u2UilCBL8fa0c65hZcY-lLDY7LOlq95mviZPPxrveBYDlAER_X3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=bErZHcyFNsp_3zKQIVFi6goEnUJcOSAcyGnqQdE-90db-C_iKXrrFkCWGmDY2yYrHMIuJBxr5-C5Ta3B3iJx_dRyDhEyxzzUWi6JXUs1ggDiSiRZYmYZ2TJ-xSCkCgeodfp2UVdmqTo3OtCtMId7FYfyvAD9RzL9Frd941hGXj1or5dU_H0ATmL3afSxUKKZ3K8UbwUjW7brWMNPGDrBDE3GDpw0XowI8M3CsjcOvnThYFMU9MZgzWQBIa90pG3NQZ65JDb0tXdP9F8ptfvV0DYavibSMgxsW_u2UilCBL8fa0c65hZcY-lLDY7LOlq95mviZPPxrveBYDlAER_X3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URa8Xjix9c3GdLNFcOLDmmy8tBqMKcazk4XPdvBP6c1owd8BjYaR4J94rxhtaIDRd-yUCwqogWtBqE4bgkdg-SLWD52TS27CmGCG3biBFbFNucjnnvpL9U57nGPSI7TlKiQC-Q29m5oDNyRAEo4ytVww4DRNmU60F-GPLJRcODYv5FSVP_8cXEpBWqcCbz6NBQ9KMNsvK9QONXAZMWGXfEO3SMukja_JmjSglJW4YABb4sshp1KzKtX7G5z-c6eg6r9XO-utdJfgXg858X02Wfcv8R1UNGVdUfxeiCi-X3qUN2QjtVLVE6Xe5Ea6fYxM7HXY-8erRq5M4Tp0fF_Rtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fltHtz_4PMg5L-Y6v25ki9CZKAmv3_XRu_6noY9VKivBVx9qVY8D4aYMFoPpyOS8hggGpct0vXYzA1bS_Az_NqAb3lSsoayvHsFGTFyppgs_Ui3we2ChO0AEe3aOzx6tMb5Nc63R9l2ycTb5TIFw2649DnMY2x2m1shxSEYuupr60wMTYI3r2ytT2wfnaBRkavOPGVj_Pq_3tTEFEqmwtuj8hoWQFTbybSftuTDSgD5xgIR1-IWENspdEbeRRErTeoTMtCgO5QXb1EvDNrqsD9ubZibFCazySWRahZ6VFG3SxnphpytTkie3rxqzL_EhY1jiuh8x5kQI707SzH71SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9Ek4PPEodA71x43oA7s8evCCJapt2IOpJCMjMK9BckZwDhXeOJaVk0XYsRxfiaQoZldjLB5VjPvwgdYvpZHigJ2JcsbpijNcGfDfvWX8syCEos1X0Y6TjRa4bsYAx8DbxRHR5fZG5EPbdZaePuoNXcOUvmiu3Y_3EloLVUXyuLoXFYMOPEPjm9yOrKFqlR3bbfHQxd10A4DW1DBahWQC55VD2lcZkRwVuCyMRe5NWmb4hmPiD7PcZLFGgvdIH-gDanRov4W5Eyp3grSsG4OcIrhEyi0oME7lgRbEWtsKUFowMwHSaswtdiIu7yu-xITaSkOzeOUqZAhv8-3E1SLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxXI_SZfUssx8HcjdevyARu9VT8COFEgNIeTKQzVLoQClFUh2AW-Kf7SkuxwbcXo96neP7XNKpjWzFc1qJeyBE_hOBsbcwCSae8rR8dINpIeHFYZPlZwZvSlL0SAQmpbZAkeC5ovcmItSzlhJlCTIYIqKt2N96Uj3BoE281SxBcYjJy6IzKMUfEXZLvqCHmVwJsH2AEdLJl4EmRVqyrX6J8uCOVuuqkeF1K-FEqgPrZp9ZkdQZx94e0rOAZZYpw4rICgIXXAlyJylueTw6R2wxIqwiaTIqLRLHvRmclVSpnSfLQpYuh0M78MB7nc-QwfGNlBEUGpRfg1DO6nd8huNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl3hOxl6T7B2LZcmfxwlWmYMQljcQXGMO_Cv7moiqWgQTmMrRR1Ztzw5Y88-mau9N5YB8GS1RJnoU1p0Uh1-_v0JVy_1HPYMy628uVAW_FEIhiF6Jv4-T9dFJb4VpEHD8jWZmyA3NR5W9f_-LzTUGyKgarx28rrtcebe7SuNxEqHD_4MpswbKqIeaVTuGTedxo4XQpR6bEccTIJlfhdTzi0yS9VltH4P38nmeSrdZUJO4m6cGszuVv-0isdFvCBoJN-NxZCLh0loktYQqivfK65dPQCTpy9W8CvGePi-sl-y3UkAP0ZB-Lvd7-mtZXtxUlWhlzgpBCUe2HLJ-vuz2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iVQQbIBf_OZcMhmB9ZGrbBHyJf1RFdtYsoP9uPeviOTOahUmg1Dg13uFvs6VqtNVgxnpbrVZvO3NJv3VPy-T-Qr1mmyNWIEsQyPwadJuOtRsERCle20bGEZlNofL5Lxg-29WWrmSaMfM4Exz4os9VA8SRXW1vHKWjzKHNRpUwEN4BMHeGEDrozARDlwsxKnPQ0155hg1sJPQYuDI41oYaI5_yO64KeM4NDsVHfqrq5C7wb9P1-TIhCoKY0rBKbjH9jMUxu-c_pWj8y8b5DAIIA8ssODBC-6d5BSGpnlii2FlkjKdjBzL46aOOKokA8Cd-L4uVp3newqjLlynIr9blQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iVQQbIBf_OZcMhmB9ZGrbBHyJf1RFdtYsoP9uPeviOTOahUmg1Dg13uFvs6VqtNVgxnpbrVZvO3NJv3VPy-T-Qr1mmyNWIEsQyPwadJuOtRsERCle20bGEZlNofL5Lxg-29WWrmSaMfM4Exz4os9VA8SRXW1vHKWjzKHNRpUwEN4BMHeGEDrozARDlwsxKnPQ0155hg1sJPQYuDI41oYaI5_yO64KeM4NDsVHfqrq5C7wb9P1-TIhCoKY0rBKbjH9jMUxu-c_pWj8y8b5DAIIA8ssODBC-6d5BSGpnlii2FlkjKdjBzL46aOOKokA8Cd-L4uVp3newqjLlynIr9blQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMjTmv_qJZc5s6cZaC2o6AbtNMjulfSaguOHSzSOJrQdQhsqvvRE2rxd7mCcYUlMbpVgRGnjJsoxk1weI44_296IhwLYVR460MLT4txsXNrdNOZSwk7JS5o9R82ThxwO5MM4PWGI5hNBJgTdDOBtKsbP0MKD2FuqyFqPJQomY8589Wj9ngUqdskja_oCB42B5fTNglnrpvPv6XtRnmgJ6nuRkQoZY37NF5N2dY1KBf4-WHTLItniK7NIfmqIuhkW227tYERvyUapVUFqRYLBV36rFOV4LkxBsYWrgFvr6p-4XTaEAWsXJZ34uLfAbNGYjWnpqckXeqb-5Lb0apBQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Gd5Um7D2lmwCrdJ8bpNFzZQg4Xw64GX-aeuqcYb2Prcn--S2N6zKIgEtwd28gTNd3mGp07tbxsYOhywDhSeUqz5vWaQbYI_HMa1gyaTf2RZL2izmMM9bgvwyPTYJsp5llyW_MGtDJLu8-GdiYtJ5qOJzN0MdKTs5emhezDG01padXw4nIfNvc289nnfl_HTJK2OWzf91qZ89yOpH1K8eaODvnS7_MdJy95yFBBURHfbQXCfp0jch8cHlfr0UT5sETXEGuGhoU4daM2PZn69AyCEtSDePk0tSJujupkCNO_CEn0XDrT1KmMPWqEqvSKGYGnvfn7uR4X4uu__PwjcKtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Gd5Um7D2lmwCrdJ8bpNFzZQg4Xw64GX-aeuqcYb2Prcn--S2N6zKIgEtwd28gTNd3mGp07tbxsYOhywDhSeUqz5vWaQbYI_HMa1gyaTf2RZL2izmMM9bgvwyPTYJsp5llyW_MGtDJLu8-GdiYtJ5qOJzN0MdKTs5emhezDG01padXw4nIfNvc289nnfl_HTJK2OWzf91qZ89yOpH1K8eaODvnS7_MdJy95yFBBURHfbQXCfp0jch8cHlfr0UT5sETXEGuGhoU4daM2PZn69AyCEtSDePk0tSJujupkCNO_CEn0XDrT1KmMPWqEqvSKGYGnvfn7uR4X4uu__PwjcKtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2A_iCTvdcQD2xok6ZX4wUMwKWD6SzAi2XrAM-YzSSCFnNBCPlnrDyE_xy8zszsfqpxW5Gu5yNCiyM3Nq2FHCejVCMGDJtCnFf6eiiUMuPAdRKiTfMfI7DRdgT_JQ8zipfCQS9WEiqwiKWZm2BxYdFIqVOaGSvspl7a-ZySL1cGU7GRxNYI54w3HfulmEjPwX674itK_vMdKWw9vIKQ8XjGYsbRgCaClur-Ghf27foai5cWomBc9UmOwRLHZRr3YGriGyG6e1x3Ln20TKXN2icV_Cs0vboSw01tMsq0eIcEeLv0QsVW3uoIk7dJSDEBx85OMTbYgZq-pjH3fepJoMg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCqFSu9VTY940jZ-difEDprlQnDRS_zklzOOnQFIBKvqV-U1keO1uKcgT3TSpYJwxMrYIFc281JoJL3_mNGabLPR2q27DKS8s0l8l_9GSHB7yWyUjrO1BoJc6uaaVOtJuHlwk22hjlOtdDO4eJqRHRuCIK9YvOGitst2igOlwBig7scISirOY4_AUzYdk50nYtqrUayWtwKw2YCN9OAhFLK9IKM1H4Jo62m0HofvX-qcH_8g8_gci6GVpabhjWe6YESgxdfJan05DGrk6NSOX3FkuCK2cJkfLeNwrsJFfPE5eFxg_pHnhrSB3gvdvAyHtBvX2H6I_fiGRg3eMSD50Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCqFSu9VTY940jZ-difEDprlQnDRS_zklzOOnQFIBKvqV-U1keO1uKcgT3TSpYJwxMrYIFc281JoJL3_mNGabLPR2q27DKS8s0l8l_9GSHB7yWyUjrO1BoJc6uaaVOtJuHlwk22hjlOtdDO4eJqRHRuCIK9YvOGitst2igOlwBig7scISirOY4_AUzYdk50nYtqrUayWtwKw2YCN9OAhFLK9IKM1H4Jo62m0HofvX-qcH_8g8_gci6GVpabhjWe6YESgxdfJan05DGrk6NSOX3FkuCK2cJkfLeNwrsJFfPE5eFxg_pHnhrSB3gvdvAyHtBvX2H6I_fiGRg3eMSD50Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
