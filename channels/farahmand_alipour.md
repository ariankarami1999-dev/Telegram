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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 22:24:25</div>
<hr>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqLZIw4aPszHN4hhN5JnJGr14vrVfmyBQakgtL-HqBEUUxIxXiIPSQHmCDcnOQdVm5PLK-EMCvtCu2Wye6o4zdO9Dw8do_O6VI7JAP_CUFHXCTyK8haa67rS39TaUGnRTWL9PCdnwjrn7IiQ31u4qJUbbT0PQTFRchyiRl8B3qh8H0yPqjQFpHzXrBg3cDsbLe2e2b7yT-hyg045AuUE2U5f5RkU1yYE-HDXnk-U3u0-hB8tv4cC_ahSfTXCQeuoDYzznQbZ4YPJxHpZyeJl7kaMiAzlRtclSgzBFqQMApvB7N2wbEcvFwxu3Ja0KH2IAi5En_H0x0kQQLPYRo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyz8KQgG8dyLlA-lOtBtmtNJ15sXU_F_w2osYaNOFrW4mr---7KH2WgfIq01i4mY1DZp_nM-268dGPWcAmlu_YsswMSS6wMNjkoxWPqHIsCQ3-ezMsnzK4KAe1CtCn3Qjjar9xJ7TIn5-KtdsjK2EDaruMjnuRlt-BScjzklI43Gn-WGgl_BiCkwC4b2R97KNbpYLoi9t-bK6Ic_nyj2BTUZkQg62TMP1bK-PqjraY8Y4yATIcoWOK93jIrGY61mTfI4iB2K7BQyRs3Qi6TEZxVs78JhyoUSZQpLrr0_GyACdOLUgFyl47EmEPRZi_FBgpvW9xzk1hp77osAQpd5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rgjOzvTv-QWmrxpNPoUMhmc_tX-uIx2f9__FS-KWvxRi9UDIayMCkVbW5duAtlJugi5rrxh92663P_ICgBS3ZfuWr863LSFAKgcPUJa76v3bgfUzSRBudIwAdVz-OUmUPNtGi-vGXhoKAVPE6yn1TOWZGzpdFf-K4sBeyY6vp-UH6z-w90Zj-EWFhg-2PLXzrjoXIjEgEcS3WhL-0V7yblUtUEq-DZAOp9xXlhkNyP5PSSvm_xS0hhQ2zBxuvxPHi79_6UuTOHUc5dQxRLb3epPDyyvlPwA0GstndFbOVE4x9e0kFelSxFc-uOBOKYzZvk718dwmVHFIKv8_JliY5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=rgjOzvTv-QWmrxpNPoUMhmc_tX-uIx2f9__FS-KWvxRi9UDIayMCkVbW5duAtlJugi5rrxh92663P_ICgBS3ZfuWr863LSFAKgcPUJa76v3bgfUzSRBudIwAdVz-OUmUPNtGi-vGXhoKAVPE6yn1TOWZGzpdFf-K4sBeyY6vp-UH6z-w90Zj-EWFhg-2PLXzrjoXIjEgEcS3WhL-0V7yblUtUEq-DZAOp9xXlhkNyP5PSSvm_xS0hhQ2zBxuvxPHi79_6UuTOHUc5dQxRLb3epPDyyvlPwA0GstndFbOVE4x9e0kFelSxFc-uOBOKYzZvk718dwmVHFIKv8_JliY5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeTgBkJW_3X_tcbHCGNwKNC7t7BRqqhlEBK1w2-5j68PbVRZO_zRBcbJ1Ly4WhcJ4TODn-K2RhN0qS8VslaMi3EjLrb3br8yJElunUmXCsxNQ9FBGR_f3jr3Mt3VILYg5OuJWpmZadhGXlNM4A6ChklR1D432bZ_jUJivCfHAqef-0-3dZNXuqoQL7NTuGj-6e5fQtnyiN2A2JqCufp2mTCAqtC2RGZS_a03b0Pavw21VRbf5xPz_oCmwq-I0lwiGdaB6fKAch9cJ6_zjYe-isQLnbxnFcZlgoDRb6UhxejIUhZHlMtwJqpN5lOR1QLsA1etyycV0UQXuTFyTI_oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZDiBrd-R1BITFmRhVSzV8JDBd3R58_xTlNMg9fjSQC7nVsbKRReYbVngU3Dm_QCU4jpLTSuJNJKu3gqKd7n1hMkyeedqXW4uN_gsvmj_-1-UKKrqKi-VJVQY4oSKW6PULdGmFCrdOz3OxYFXby61hRrH8kMmYzI7T1VZS3hw31teX0PPVQQ0RWQ6duv0r6ue_yHFbJnJKumrw_HnmwL8N_VNHPlRwyc1bnOXQqwhf_RCHdld_6d8dDfz-pOHPee3bLNvjR0vV8KiHhqnYL_uWMJ-VcqAUQjItD4_6OqvQPQnJ7A6V91qgNMuyAK03-4l_oMFmRtfGJanJFxrVYqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHv4jkd3l2UWPee6O22n6e010WQAvvHuKHRICY-uL59fcAA4MPiox40VoqKjCSuqnKTuTsPAbdEkLPLDVsFRcRRE7tTvg_b5cI-0UgwmooF2gRh6-vEDduTEU3Oa8MixMPPBl0PvHx25KkUGCNyvu674XWnA4KFwjkZkVnG7blLnBOubnRBVOoSxmMCRlUhEbNIBvzPCIAlIiSlduLOvpa9Fo9Vhe5T7QuOgEReiFSUaO5FqJAl3_hpWqQgGjRkUKWdbQIBxDF49lg1DJT9C2fjwK9vBHAN1-EFebXFmsD4-zcZJlpRtruV10ACEO1q9tqau5DwPVItxJ_53ov58tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTgUNY35MFpfpZjpLblOuTZCnzqzERFosED_2UB78EPMIxh_CuFRWe3vmvRGhL3IR8GuBtXrXKCzeZcq4h__pKXwKmZQ4OrInhsma59Jh2fPDiYspFB8jZlRqAuP7j6m1THiWTjde2LHlxNLv9qMBa4aztJPIPwJg37YxjXTJ7Nu1RcMLgUiuq1eOdDlZel6XIgVu_TGdfgMv7ga9IjfiMeTmwzij5IEo-HBY29Ivt6NkWv8U06fsiKmDOGOSbXZfCSJYzBul22E5R7vQ3NknpZv5aYPGqBa3Q0-lbqiPkZhsmY1YgRLr7bz43LWos2k2yhQXFpKDn2nbqa_BCZs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4my1Sdqw0tiXjOxVjVUzal11IW4sr1xDcxp8-aab8VZA4U7qSB7qDfcaa_-04SbRUAvB3781vK2HcDmu4bDn5-DAoY81OvUfCmlhblkeO120YIHfGVEmAUhIpZuzM6y6nt64W6mXuGXko9-Q24LmjOdbOVawKIILod6qaZPHkxD7hOBLNO2I0eWIFprpJVd_MYhxON9Vabn-zXOFIK-ROrOT0e1fGGACDYa0TLeTudZ7XY6P8NchtULHmQMIpg8mkuGG46ic7dZ7jiD0YGxp6eKeL6MohKtgwRdPERb4VH0ZGY4r4ka4eLUceIhkEaEAuUBnBAcrs6qW-V79Shv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=qy4Ers6ns4CxlG9U_RB7tXSzabItVyj2bH8axLCuoMfAE6DCgraDloK99BhQXZsqAWk_8oOipHBeBntVFrKlMTNtzQ8XIZMfbqv9tvTBoIaosd0c7MP8wH4cfxSsLknZ8ecmQDQiy397KMiJnAKfjg1RIRhHxiwtHWQoDxt3aiG-uiWT9fM-wR4smOhZ0tmmZjaS4gydBY4fAz29mrjuKXg8wIp08_5nstbMCiPb6K_NNN2yHcEIfsYMv2s-XauDJEEOLVHN5vM9BT9XrIdOCkhUEnq164fDa91PvWXFlh0O2AJ7W43d-LyVihelQCgw-jzp6IDS-kG42W_Xb-f1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=qy4Ers6ns4CxlG9U_RB7tXSzabItVyj2bH8axLCuoMfAE6DCgraDloK99BhQXZsqAWk_8oOipHBeBntVFrKlMTNtzQ8XIZMfbqv9tvTBoIaosd0c7MP8wH4cfxSsLknZ8ecmQDQiy397KMiJnAKfjg1RIRhHxiwtHWQoDxt3aiG-uiWT9fM-wR4smOhZ0tmmZjaS4gydBY4fAz29mrjuKXg8wIp08_5nstbMCiPb6K_NNN2yHcEIfsYMv2s-XauDJEEOLVHN5vM9BT9XrIdOCkhUEnq164fDa91PvWXFlh0O2AJ7W43d-LyVihelQCgw-jzp6IDS-kG42W_Xb-f1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMxG372dFLDCl2B-TRGkUpAlmCblLJZ7Qsq2eT9tYNaxwXwKfYsdEBfDDGlLdN7_h_MtSHbyB2gYij0CRw3GlBmatbJB35SKCVJSPc3rgWZXDJPJxoq2yTNPvsIkEM4YY8n27vNje0bC5UAi8oYBQ8knE3duzRUy9yAFypCRb1iNGBzlM-cIbK8ugXz-C_C5-LETJI8sR23EIZYDFjDihCSexUqVWH5ggY90lvmc0gXifHT1HOnE3NCdlmzwHeX3vKS9MVbGvlMs-pMOafumKOC12qCHRC1sPClvzmCZxsB_P5DkmfuX9vWR7KBCX6CJdg7rHBmM-sN4O5fAqWbsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnKsoxUbNi1Y1rFdzIQA9aPonHXpJAADueHQXCDYGV-w0lA_4chKe39mD16R30HUMRX6OoB3Ma_jLa8-lwcDxD7RFqv70rgSXQ_kjKscrAMe4nIv042QZUYCT1cMWZmlkV_1A6cDbeLqxYWVXblUmbvNW4x_8ESnRKAFRIkx-Epx-siBH19RJf3NfJc-o8AvCTEdbHRYAk_8RhjPNxenNA9KlAeCLA2J2MsnLXffQmVInBm8fL3uACLF9qAHspy5bT-ftJSYDdLek1aTfE3vwzwyS0dmOrVs61tfRCKZVsQVTS92yvKbrl_6qpxyyGYfT7MUUTnCIughZsE8WvxDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=pe4jiFrXv-DoMMV07I22_lRmiRJxDStTPIrO8GR0_2TbOtxSHcgjHwSfiaIwXRnInXT7rxEWBfU4C3El4_zzvkyGBm31UhN_Kai4lwN7IhkzCw8Axpvnwe_gZ6WhpPGhhZVSPcHlaLZaPlQznHLwfgxgDjzesBRAEVMEHkE8QEkKVxw2XhQS1MH2OZCdm66JHCvznMWFqdWmE5YyDA_RcdJN8YNsqcrEWKhCbItg_4iRu2EQXKYtOaZ2loz_FzXoHcTxr9wc4DuPOc8eo8eIEm7Hw2r2hLFeVsxhoR1i4Y_xoLC7aMMHcMsb8Rl_swvSkk47SUmOAcGFW043WsIBdBtSjNj_4CGUul_zh4yyqay9FPmKuwIrwsvmvbKmG4BwyszDTwk04qEoc-z9e3BdMCmzFh2CxwZfVR8b0fhiXkuSy5XpBp3GUiA84G8cWnNr2GPrakNPsG5oRQqaeJr-lQKKqt4VsR97oE0_i47L0Svh4TnKY3Nb49MZJbzqFc6PS3vn0WA4DYBUvEnogKFgsbI53lsD9EWUEyf2KkkIX1E1X2nziWYWlwbdMGnQs7KA5Qwyfx-uellxevfF47Y8RpI5E5MTApQJpmMQ_HNS3EkTe64jD6Ap9hYSCl_9_MuBKe1q9yxpvtTWjGDMgJFdbjlrXHdnDpiykJQAs0ry3iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=pe4jiFrXv-DoMMV07I22_lRmiRJxDStTPIrO8GR0_2TbOtxSHcgjHwSfiaIwXRnInXT7rxEWBfU4C3El4_zzvkyGBm31UhN_Kai4lwN7IhkzCw8Axpvnwe_gZ6WhpPGhhZVSPcHlaLZaPlQznHLwfgxgDjzesBRAEVMEHkE8QEkKVxw2XhQS1MH2OZCdm66JHCvznMWFqdWmE5YyDA_RcdJN8YNsqcrEWKhCbItg_4iRu2EQXKYtOaZ2loz_FzXoHcTxr9wc4DuPOc8eo8eIEm7Hw2r2hLFeVsxhoR1i4Y_xoLC7aMMHcMsb8Rl_swvSkk47SUmOAcGFW043WsIBdBtSjNj_4CGUul_zh4yyqay9FPmKuwIrwsvmvbKmG4BwyszDTwk04qEoc-z9e3BdMCmzFh2CxwZfVR8b0fhiXkuSy5XpBp3GUiA84G8cWnNr2GPrakNPsG5oRQqaeJr-lQKKqt4VsR97oE0_i47L0Svh4TnKY3Nb49MZJbzqFc6PS3vn0WA4DYBUvEnogKFgsbI53lsD9EWUEyf2KkkIX1E1X2nziWYWlwbdMGnQs7KA5Qwyfx-uellxevfF47Y8RpI5E5MTApQJpmMQ_HNS3EkTe64jD6Ap9hYSCl_9_MuBKe1q9yxpvtTWjGDMgJFdbjlrXHdnDpiykJQAs0ry3iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=dUnHqnbmTkj1N2x1qugsC5FEYss1NKzd9R7_wDUsMQNEjBvY5X4_RUN4VdM4BIJ8oOlAKiV6ticqJ2I6Dl2anmStQm6YBWIGcDb8l_44wuNTFLPqudVX2PLAJQFvyiYlgvyZDj-_gHe1nbYiNeybIZAR8E0jl4j3OBNu8pXDcYmTSbBaKPgK9lZNOw6gMEb6-kspWR5eDdnW9dBfAo_gqtLibBjTUMMduDlP5gpqROpUHEWSP-HhCKmB10foJIjmkplyIcGROJQPvkMWaMFrQTseF_-kAxVrr3m-ROucdscMeVQ9H5hvktHe4DAvgI18q6jnB2G47Wqj1eEfxiyLGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=dUnHqnbmTkj1N2x1qugsC5FEYss1NKzd9R7_wDUsMQNEjBvY5X4_RUN4VdM4BIJ8oOlAKiV6ticqJ2I6Dl2anmStQm6YBWIGcDb8l_44wuNTFLPqudVX2PLAJQFvyiYlgvyZDj-_gHe1nbYiNeybIZAR8E0jl4j3OBNu8pXDcYmTSbBaKPgK9lZNOw6gMEb6-kspWR5eDdnW9dBfAo_gqtLibBjTUMMduDlP5gpqROpUHEWSP-HhCKmB10foJIjmkplyIcGROJQPvkMWaMFrQTseF_-kAxVrr3m-ROucdscMeVQ9H5hvktHe4DAvgI18q6jnB2G47Wqj1eEfxiyLGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqKszslOl7A0mSRiECv5tDCGj_DXqm9TYY3u7KiqmAPYlQ0GPpr-3_wSduIpw1voDvTP5dqsiI4-STs6ESIOhvLoKrFkZMiHy3YcdZV-PitXvxgZzdpDcomwpaXZVcMue7Gwkoc6gwVtiO-67ZO96D65vur1D6rl4EyDIAlfJEhhkAds6GJWT9-0oDzqvCmwHfNY_GKzgH3exAfCs5_HrLtvWYzfqdBskGe6c0rajG5yGXO29EgtH1mO-hyaksVgR9E1ivOt5p4L2HoV_l8__gRpM7Tui7LmwiDOntr5IjrKD4LQV_7avhtqsiVMi4pTiesoXbzGvzMIvJO-cAhxA74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCqKszslOl7A0mSRiECv5tDCGj_DXqm9TYY3u7KiqmAPYlQ0GPpr-3_wSduIpw1voDvTP5dqsiI4-STs6ESIOhvLoKrFkZMiHy3YcdZV-PitXvxgZzdpDcomwpaXZVcMue7Gwkoc6gwVtiO-67ZO96D65vur1D6rl4EyDIAlfJEhhkAds6GJWT9-0oDzqvCmwHfNY_GKzgH3exAfCs5_HrLtvWYzfqdBskGe6c0rajG5yGXO29EgtH1mO-hyaksVgR9E1ivOt5p4L2HoV_l8__gRpM7Tui7LmwiDOntr5IjrKD4LQV_7avhtqsiVMi4pTiesoXbzGvzMIvJO-cAhxA74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMRV1mGF0EYtF0D4liiFEuRAI30k0MXGxdSxDlnl0Y6eZ_sMZkXCScF9vd8KD5e4_8kZ7YnBB7xbNy9PO1eNWUIugMXHfgcwY21Lp_HkRmVzT-GptCMLjY86lIzijU9hBM-hN_EEWk0LqZLB2UtqT7CpmD8UrWcNnW2HME830fPXcFkThfjWxpyurHdpQj-S5_m9SOXccuMwcxv1qJhX1oSO_TTrFh0ezxxlUh99hglFkTPL5N3umdURxvMfXluTDoMwoR7OrttY_mRf6WFE0qAFFfy6_y3BdCYVAex5MFKcBHzkpptJYWvvb8ll9qvcdpPgqwZEE1F34Ug1X9thng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2i5uE1jS_jQImeDi2W3ZCLzzv15n06MwCZOEPRiK4GmhcUDSULt90GAHQHjbDwV12m_O69MHl-L6xa1edIX6UTVq5hGTx0vChg-vLBN_HUc6E_fgijllOyMwGyIfHQ7575KvhIFqVVK2asIAVzfAzyhrYuzZQdGVjvhqHqPEnCYnuzAdBNARwzoIxR9rNdwUgKrgUO3Q_e316Il9T-9DBXB-8LjbyoiWU2kyNlDdNWhRTNWQvtU8xJrTpQfPfRl0vp4sGzEjqdjTcit5DiKiNC0ZK5caZBmdLCQbGXo5wPsNpcAWFoauFxvpDW7cghyOT3C5wP-9Yb7YQOo22U-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF3ftXzg--w19C1nxWdbT6VNs18q-0gG65cPI46gqTIEiNqBAc-Ww0QolHuuEnc3xtAf7xebPdqj_F86Ai94_e1RADCe5nZ4qlpuwmDAfh-DLqJbsx-SgIPRBkNCzrhb1_PFxe2B7JyWDyugl8U1gKmcnE5v-0bCXh-tW6AghlZK65Ev9Yzie8uH8iCtohF4SdFK79whTLtZMXki_ADzIjVicEdZMmd3zl7YRYYwa0d8hKRpJ8C4Znu9MJCu_am9vgYsAIj6mIQk6OcsDk_rGCj0oa-ASSS2D5xr-BdalOU0djar1zDBOrN_jorO289ZBaueaQVhgo04kCM4cosvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=OZA8VHF8tx1k6lD9dV89YChi9x60iWoHU20bbKt8CanNHsS3hpsvj-E1rEFt-7H5RqQ-vCkLDksrNcOf1tpcx7BPsJ8pALUfXPaMemiNdwsOc83pndL0ZwVrqxjKlsQ0jwO86G8kK4gOgVB9bYk1NQa-qTjHaEqkAfmWa1rSyhpAm0Oti02blS5yxRsAF7DgR2lBjLvndqfBrhCaS3DJ_LDHZkJWVXlsAP56ecg3rXWisqv7Ds3BeJKc5RPp6y8N815bN0bgB1QW044rSMAYCaYSBjY_O9_kSOX104Z6YtjHLoKdAOwBwBQtThXPvu_7bzi1HL30BCxpTcEU4pkJGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=OZA8VHF8tx1k6lD9dV89YChi9x60iWoHU20bbKt8CanNHsS3hpsvj-E1rEFt-7H5RqQ-vCkLDksrNcOf1tpcx7BPsJ8pALUfXPaMemiNdwsOc83pndL0ZwVrqxjKlsQ0jwO86G8kK4gOgVB9bYk1NQa-qTjHaEqkAfmWa1rSyhpAm0Oti02blS5yxRsAF7DgR2lBjLvndqfBrhCaS3DJ_LDHZkJWVXlsAP56ecg3rXWisqv7Ds3BeJKc5RPp6y8N815bN0bgB1QW044rSMAYCaYSBjY_O9_kSOX104Z6YtjHLoKdAOwBwBQtThXPvu_7bzi1HL30BCxpTcEU4pkJGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQiof-Sv-Rb4WlGSRAU4CPDDfmXzdH1A76YiweMIAPb4dGRGBa_WE847AQZWTqELNc5KipjsXv7cOmNCIcQ5p8piExz1Jwh1n7rEOV6QWbpg254EHNpXXLQ90GRLbo4kzm0FaqSHCr_q_-Cm6b35Euh2Hi6YPsi8_pJv7sylHp3wosTezROvlREFYaCiy8hjT6iLDQjQHAYMvZUBX6i57LCUvq4p7wiK2B-cV0WFdCcRzdpKgE6E5m3-atUfKR9m3-4CkhPURUQWdS_Zq4r-efoY_3tO_g1x0s8Mm1vz8JQZSC2QBGMPAKeH0ZLC9zEZbUFTUtEJzt2k3qmf71Oe9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esfEi-RS6IxEz-QdS-YQwcmSCYZTcD3g8mirZx75DO2Hys5TK-8YlLRC_ldyx3G0LgjVQzeBufeJN0GeRgjHDqDU-4Ha12W3B47MrJ1QuluIomWGURMuOjXo3qc8AftueAUok-iHZj4rEKCO7k_wemmsJAvZiJJenaKJ7zVb-0jz7MpUGwEKj9Z49zyKinQLLnLbofVfVWWWel1A1XODohYAj9dd1ij6pAmxk5rBuxy87z7YPfUqi_wg4VhP8tWtbNw3J-pr_uwfDniJI608YXKrwZIJx-03uCJ6RFGTw5yWXbkuiPfXR4wnWUKC_ZnQm6JGRGORaGXneyZpm3tJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD_6rXQAe-TRORcTLCPaZBuAMEyLP3otqtv497S8-xjiHn6rwh1QHZPFfdMlFGpos2ryAN1Xbzi4USt8RVTCR--D3Jssqznxv349p26wwhIv3CL7amecCbV9BhbVSvjiML0MaNteVRX5bMB92NW0pn8k5BEJt4ZmPnqi1H0FJX9w1J4EQ3kMxeuVk6V6KFQorgfYYL7jUJ7kOmOMcBreTUOQGjpBeWeW_gKWQFFRI7j1Nwibwg9RXhio03GWuPnxDpwJLXIPvZ5ELOtWK1730P8Pny1LIba2Hyh7eAW-AdUtQoiQMQb4gTZ-EOxFdwBVnqU3LeiIRhWk2mKL-BvyRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swE3GbY_Oz2Cz-3rxrSd7wVww_FB-UL7ncQfeNPAkO3ZeAvVJ034CrHjUYs6IECeSX_rMtmGgjspoKP16v8YGb3N25jAnsJWn_B76gkX77t7eIIr3UOU3mqGNM8zbl4-Srw1aMid1UYz1LUYqZ8XugLe9Da0M-SRpCWwpyQ04dAmhz_e2jl1NMb5qZt2HgBPrHHzqyEuQ5kr9hbiwokvGgsvN1mOX-or1InIkzSG7UWaZW2vdhzqlUrq8uc0CgmkMYKCwThVIMGl8ZvUnITelqpAayb7tbEieeG7fvaRmWhAZlsKvRBYWNvBiRNX_QfIPjahmSj_x2Vw0bTgm32zJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=U-6y2R6DikdsJEzqVdNBpp95B38T2R8JJbuq2-BxE5a3BNxUB3TY88owozJ_yJNrJYGLHfTJhoPulbZgX4JEFNFnPpFhaSC-oEcOkXHyV4bqqAgAMYZXrakWKyMbdWsrq3_--PyfdWImj7Z-hbdsA2vv7SK5W10UjZ__Zv3RuGfLUEYcVCTkeZRcwGq6xiZR4JcXv2GZNqAhN9hSif-1F7tZgdZ91Vv1AAHZJgK30L_7CQvTY_7un6fJwuJwDyiuB3pxLEauDReGS_6BZgKDAc_Qn5l_QOlafBk6sOSC_8eBzQhb82UEXEWFIzvYZ2W4vTF-EETGG15GOaCiAViChjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=U-6y2R6DikdsJEzqVdNBpp95B38T2R8JJbuq2-BxE5a3BNxUB3TY88owozJ_yJNrJYGLHfTJhoPulbZgX4JEFNFnPpFhaSC-oEcOkXHyV4bqqAgAMYZXrakWKyMbdWsrq3_--PyfdWImj7Z-hbdsA2vv7SK5W10UjZ__Zv3RuGfLUEYcVCTkeZRcwGq6xiZR4JcXv2GZNqAhN9hSif-1F7tZgdZ91Vv1AAHZJgK30L_7CQvTY_7un6fJwuJwDyiuB3pxLEauDReGS_6BZgKDAc_Qn5l_QOlafBk6sOSC_8eBzQhb82UEXEWFIzvYZ2W4vTF-EETGG15GOaCiAViChjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=eAk3gK_VjYXFrMvExb13yJ-rMF2uRBKhuSc_CeMc-BiPqSPZjW9u2L1bN2KGwsussanOY9TxH-MlY1A99zTwNdC--bRQH1eK_cz6ZUag5ruyfbQCdJ1alyaqi5P-4zl5ensqsYIWPUhdB2nDqBKbNrUL_N-0T7AmgQxAq0Q2i6Qdwhp5eM8w0Oju9tfaRLPaNopNi6lV0FtuQPzNkhDRImboIS_10-XqEVOYiJGQWO6Txil9K1DFHFaAPyGcAaxj2AwsQIeod4JN1mukUZnKYy0kQSGcb1rD2YQ4lP6fP5cs22x1WfFhqyUFmlJ7phgdOupgZfqYCeVZ_D5YOBXHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=eAk3gK_VjYXFrMvExb13yJ-rMF2uRBKhuSc_CeMc-BiPqSPZjW9u2L1bN2KGwsussanOY9TxH-MlY1A99zTwNdC--bRQH1eK_cz6ZUag5ruyfbQCdJ1alyaqi5P-4zl5ensqsYIWPUhdB2nDqBKbNrUL_N-0T7AmgQxAq0Q2i6Qdwhp5eM8w0Oju9tfaRLPaNopNi6lV0FtuQPzNkhDRImboIS_10-XqEVOYiJGQWO6Txil9K1DFHFaAPyGcAaxj2AwsQIeod4JN1mukUZnKYy0kQSGcb1rD2YQ4lP6fP5cs22x1WfFhqyUFmlJ7phgdOupgZfqYCeVZ_D5YOBXHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=srMwkOG7nyX5WBdfyBcjVnJwoLm1oFqRjM09k2RTYAbDtmdX44U6Cz2uyvtwBsT0xixIxbdR6HPldVJ-BBXVgZPepZr1R3IquLmtTYz2IQcsflCF3yF_CaJyWHHw6RgVArvgFmMEq4AqX8_WTwFIgnmPdsvBkSWOXXh8WDEIIslujzPMZd5ysDEu7saibxbVueIy1ovkg_j6O6XJBVfmBMBXjaFe2OlAqR8RTjSSqnzCfKcSnP_bD2XcSvP-7PpfGE3Z80WjRfAH2wfDwkFvIgHmQAHk-GdXoCeVp1hf32rQuV5lkYiA_GVDwYPIKnl6aOlX8dJWlgpXWtSJ7R5cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=srMwkOG7nyX5WBdfyBcjVnJwoLm1oFqRjM09k2RTYAbDtmdX44U6Cz2uyvtwBsT0xixIxbdR6HPldVJ-BBXVgZPepZr1R3IquLmtTYz2IQcsflCF3yF_CaJyWHHw6RgVArvgFmMEq4AqX8_WTwFIgnmPdsvBkSWOXXh8WDEIIslujzPMZd5ysDEu7saibxbVueIy1ovkg_j6O6XJBVfmBMBXjaFe2OlAqR8RTjSSqnzCfKcSnP_bD2XcSvP-7PpfGE3Z80WjRfAH2wfDwkFvIgHmQAHk-GdXoCeVp1hf32rQuV5lkYiA_GVDwYPIKnl6aOlX8dJWlgpXWtSJ7R5cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Y11nhR1LzMxQF43xlEYQ5ilNWDb-9c7emyg7PGCpFjDFZpbmXRaktvl8iJ4qZ3JT9oTgB3Cth-TXENhzFMJK1iCEShXa9mX8nJllN5bliL1bQt4RnTSV-h01V0DQveiwLpKmNNCEUkNBkmHYoJpiCkWmalaaSB_OQeNdtTsrWchZcM1icLNw1I7x0kTX4iGny3fee5jnH-k3Pq6jAxWDOstuZFTqo0Xr9dYGp1kNl2exzoui6df9kemJrsg5PxqsIIg1R_aKmCnx-PufUB-57rSDNHEZhIedwKAyzxM5rfMusXJzG7ynNu0RRqpZf1Rm2mzUQVrGHXqTEF5MPCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=IGmDMvEh70CI2jKIEp3ecVISc30VmbOL9iUK3nfBYqM_I3u5W73Viin2B65HPwaRPlMLm4H6FClAMPlzWaKsi2HWT1dy5TfgF4Rn_S3_s3BcWfNDTNULIWFcc88ZzVV92RVk6CorUwVE_L00QVc55fG9jNW8R-3AZY4i4qVXGu44G_fAxWkcfJoQzQVUZQOkM2JpuoMjKh3yJUHHeDh-nEM_MBJOouq-G2OpHN1_9xqbo3z93uss4iK8_2mVREKt0HkxXwGwPeRP-snYphkyo3VktuWLby3LjUsZ5szY162qMC0Xp4yMUziX0T-QA-h4nGhl5iAE_sMEYEnPgeKZXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=IGmDMvEh70CI2jKIEp3ecVISc30VmbOL9iUK3nfBYqM_I3u5W73Viin2B65HPwaRPlMLm4H6FClAMPlzWaKsi2HWT1dy5TfgF4Rn_S3_s3BcWfNDTNULIWFcc88ZzVV92RVk6CorUwVE_L00QVc55fG9jNW8R-3AZY4i4qVXGu44G_fAxWkcfJoQzQVUZQOkM2JpuoMjKh3yJUHHeDh-nEM_MBJOouq-G2OpHN1_9xqbo3z93uss4iK8_2mVREKt0HkxXwGwPeRP-snYphkyo3VktuWLby3LjUsZ5szY162qMC0Xp4yMUziX0T-QA-h4nGhl5iAE_sMEYEnPgeKZXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cAYFnP5JwRpSHy0W9NkHeYy9C6UMZrE6xxXMmKe_Agma7oGTUu5u8xCsKAJrZIFFAt8Xz3DgOl-Gq4q4xokrNPlnfniuAC8Jbl_ll9jiKkVKNzeVHjXimvZLaLZT5wcDIXjgtltuvX5Zbn5b-PBRe5jdpW_29HrQzYxUxAkeW0EoimyL6iWgs6UmAfi_wruzSmgaxHL5K_ovoj2izW9HZoaW7ovDHRYphqKP15jIguMcDXsKchC1FC0rF-36_Z35uxqhnKNlLsww3zRFLaB4mR1c9YpFFTHRemRIMlPyp16ADz4fosNUsRIdK0seFhF1Prw831vjdpKvQBlk7Hw1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=cAYFnP5JwRpSHy0W9NkHeYy9C6UMZrE6xxXMmKe_Agma7oGTUu5u8xCsKAJrZIFFAt8Xz3DgOl-Gq4q4xokrNPlnfniuAC8Jbl_ll9jiKkVKNzeVHjXimvZLaLZT5wcDIXjgtltuvX5Zbn5b-PBRe5jdpW_29HrQzYxUxAkeW0EoimyL6iWgs6UmAfi_wruzSmgaxHL5K_ovoj2izW9HZoaW7ovDHRYphqKP15jIguMcDXsKchC1FC0rF-36_Z35uxqhnKNlLsww3zRFLaB4mR1c9YpFFTHRemRIMlPyp16ADz4fosNUsRIdK0seFhF1Prw831vjdpKvQBlk7Hw1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=cTuBPeUwb4oiXWueNxJTkSoM8KNkyuYj84OexOBZCTPjTNk4kCGd3yxBSrhPW4v3RXHbjr4KvpUli-G2QfiRlyY-xeXx7BjxItGs5dJA0bT7bUuIo9fhoJSduyOxNm8KyX5704tVLVWJPxHZd-hU1k_4-8_AJpj7fNYQ84ac6hna_Q4_y9lWMXA1ekkvjTUuEL2Jo_EP986xSobsR51iz1mmrfn7uFfiFM-0FqWo5wZ9hFLWS-tYUPEJ4BiObpDeA6SMO20OG4O6Zo64sHCuktNntJWhSk4eHtBZ195p4n09ikbGjdL62ooptvUW1oUF5oCS1ysRXxnbISG8lgRTxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=cTuBPeUwb4oiXWueNxJTkSoM8KNkyuYj84OexOBZCTPjTNk4kCGd3yxBSrhPW4v3RXHbjr4KvpUli-G2QfiRlyY-xeXx7BjxItGs5dJA0bT7bUuIo9fhoJSduyOxNm8KyX5704tVLVWJPxHZd-hU1k_4-8_AJpj7fNYQ84ac6hna_Q4_y9lWMXA1ekkvjTUuEL2Jo_EP986xSobsR51iz1mmrfn7uFfiFM-0FqWo5wZ9hFLWS-tYUPEJ4BiObpDeA6SMO20OG4O6Zo64sHCuktNntJWhSk4eHtBZ195p4n09ikbGjdL62ooptvUW1oUF5oCS1ysRXxnbISG8lgRTxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=uSnKwKbnSDk6NxnIF45WPijvs04tZ3C8UJ_FF3ymapZpqIua_sUa-_NpkEUlZIduZ-Y83xZreHrW1lRObWIkWrZv2yE5uGak8ugrCgUyF5Niuma1ddgTfhXb5nuWDe1VF30QdHyaoOySH3f5XmhDX99o8--4B_IDRg4eQuH00m5xMh-klf83ZPXQal4b3phXA9Cla6rPWWCEFLbY3bR9yQHIEA5t6YbHIfPHsx3HX9aKEulDTlSWFCXPHj2L8ILt1ovbbZZrs8p-3xXKI4YpeU7ZE1E2Tmgi_h-ZyFZTuHmPh66XA8GJIHA0pVB64MuHxWG_6z0-gUT9xnUYJpeEYHXEGEs5m0WkCAtGQPs1oYnk4DBUkwAo7uHcvk_RIWaKO8M0ewm9rVlUOUP1Ym7GOF1ECEax0Xy1_0oIyXdwSTpFF1tAelEV8llB37VfdklVcnuh5UWOZYBlkxDde4udhhNfSuYM8DRigHMQB11JlnInhn4RGC4fPSk9X_LRZq72O4wZAD3pIIjkJ3CGiZUmqNtqfVfTmf0HFz2yRRbcs33IuIDexV2Vr5y4yn9PKqO050Sf2_N8rMhs_7SokA1MwI58YT5rMPNriIdaSnbSWmmmQ1Anui5-ger4As2yCC-1V7X4JA3xVzNApFrX7X_8B9iESssvKl_zcyPOa1c6ndY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=uSnKwKbnSDk6NxnIF45WPijvs04tZ3C8UJ_FF3ymapZpqIua_sUa-_NpkEUlZIduZ-Y83xZreHrW1lRObWIkWrZv2yE5uGak8ugrCgUyF5Niuma1ddgTfhXb5nuWDe1VF30QdHyaoOySH3f5XmhDX99o8--4B_IDRg4eQuH00m5xMh-klf83ZPXQal4b3phXA9Cla6rPWWCEFLbY3bR9yQHIEA5t6YbHIfPHsx3HX9aKEulDTlSWFCXPHj2L8ILt1ovbbZZrs8p-3xXKI4YpeU7ZE1E2Tmgi_h-ZyFZTuHmPh66XA8GJIHA0pVB64MuHxWG_6z0-gUT9xnUYJpeEYHXEGEs5m0WkCAtGQPs1oYnk4DBUkwAo7uHcvk_RIWaKO8M0ewm9rVlUOUP1Ym7GOF1ECEax0Xy1_0oIyXdwSTpFF1tAelEV8llB37VfdklVcnuh5UWOZYBlkxDde4udhhNfSuYM8DRigHMQB11JlnInhn4RGC4fPSk9X_LRZq72O4wZAD3pIIjkJ3CGiZUmqNtqfVfTmf0HFz2yRRbcs33IuIDexV2Vr5y4yn9PKqO050Sf2_N8rMhs_7SokA1MwI58YT5rMPNriIdaSnbSWmmmQ1Anui5-ger4As2yCC-1V7X4JA3xVzNApFrX7X_8B9iESssvKl_zcyPOa1c6ndY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=qqlx5WPdwr3n-9l1DXU80X0GUvYZCa44V1bnTYN7SAljzsNDDUwUyzbtFFC90Y8-h7mI6HHXcX7-AyQ015AWfiYscvAcKoEosZ_eUm0JQeRWjEk0puoGT-glEReA_oBMmGixApr1XCEDqyvsj-8RltUdk4ORCgiyVRy0vfb3oWQtZgNuIBmjf0zNQAYuXNNwCesJDQH0gIGr4X1KCnwvu_V3YpIXqLgg-xq5qfMEwTxjPl466zNDAWoTmeNfxoa2WHTwclZlq1dkSdPP-EI6DMvg21DJWa9SLqCGHzuc3pI1oFoftLGyEuqGe1g2l2tx73l3P8xqbh9fF1E-4uZfVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=qqlx5WPdwr3n-9l1DXU80X0GUvYZCa44V1bnTYN7SAljzsNDDUwUyzbtFFC90Y8-h7mI6HHXcX7-AyQ015AWfiYscvAcKoEosZ_eUm0JQeRWjEk0puoGT-glEReA_oBMmGixApr1XCEDqyvsj-8RltUdk4ORCgiyVRy0vfb3oWQtZgNuIBmjf0zNQAYuXNNwCesJDQH0gIGr4X1KCnwvu_V3YpIXqLgg-xq5qfMEwTxjPl466zNDAWoTmeNfxoa2WHTwclZlq1dkSdPP-EI6DMvg21DJWa9SLqCGHzuc3pI1oFoftLGyEuqGe1g2l2tx73l3P8xqbh9fF1E-4uZfVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=k1KZ6yEckk8UtVBYjZn4R-DebDaWwuKGOwoymflGQjluQuHW-ixPkOJv2CcaVoOn7mrNt1p6gYxBykPaFcWoSUWuABQFG3-s7L6CWP-j1p4z6R5k7-fDWoQpFhMqTrq4aXEBu0dbLp8FLI1vJ9zgeuJ79YqJOkR0T-TP_WlD3yvwbeEVDNmK3CW7psjKaJCY5PGJaKWdDm2Wb67wzi5JNtq-Fr4yRnXh7Jbn-waOAX_yxEXhsTNsqLBOuVGp9Zc3yCk1YqEijXsv4Wa9n8XGGW7X0H1HFGhUgmOZ0xE7TZ3ykSxKjKj7T8oL11VTswknfY3tsbki6wmqNpUaC7-3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=k1KZ6yEckk8UtVBYjZn4R-DebDaWwuKGOwoymflGQjluQuHW-ixPkOJv2CcaVoOn7mrNt1p6gYxBykPaFcWoSUWuABQFG3-s7L6CWP-j1p4z6R5k7-fDWoQpFhMqTrq4aXEBu0dbLp8FLI1vJ9zgeuJ79YqJOkR0T-TP_WlD3yvwbeEVDNmK3CW7psjKaJCY5PGJaKWdDm2Wb67wzi5JNtq-Fr4yRnXh7Jbn-waOAX_yxEXhsTNsqLBOuVGp9Zc3yCk1YqEijXsv4Wa9n8XGGW7X0H1HFGhUgmOZ0xE7TZ3ykSxKjKj7T8oL11VTswknfY3tsbki6wmqNpUaC7-3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BklPk3v3kua2PgDziIP27MCvAq231JB52HlXpLf1N5kr9T6bZvC_VT4nDnJ-nuvPHIpbVwn2Y06ynAIlt0biZP9s-1rZUlzMeMpgnxV63xYrautHjGw8idlPQkfCt0z9hyLG2-mGiBfyzZvm3TfX8iuCLJn5PTNUj2znT-eHGY4qgz195pvKhax5Lu6Wsm1Zyg8T1BeWEU686Qs3iojxJFjlGn12dzmfquds0VB8jesBIRMgO4arsGVuTOaQmcNdeUN9ux0gmO98ySjGFfgIWktQ1v_ZjBSYPWa7eH-FK2OLMCAsI9nBs2my32pM5Or3HGC0HRBsXJgRnPLy7M1sRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmrG7bwkC_CAPUFLAa0bYhz1OLxXkOmUy4wUhKaA1997_ODCwl7plNtfLXuBnuq2jZSgzXjCKluA5rE_FOlycPMQhji8O4pU_VaFRCIMdrOpglp4CvJmQfdLm2YHvEbqBs_agJ3WkiGUFanCVPaY1Zi6fMOTi8jF6jiV1Oy5fM-qkWLJ0hZ3jb7lwTeyK15AwPmiKd6VEIFzUZqnedv5XdE1_fzbGDGc0n1TYOEZp3iVWJs-pURWZKUmMNc5FM2Pa3sYFGr6QHFMaRzRfHSRiSz9jh1TgM6sgM2biuVxIV3s3nMmndJtgHD2JY4Cc8loHfylxZ5KdXJXrWSqeWfvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=vHZY41JvcauPBr_FeLMC6PAiw9Nte1JKjENkcb6T0x9EmjQ34hd0kf2JMMM1sCTRKBFUNG577-60gWhhcuIgmMcx3BzG0S8hjs47814saOQC43gRSJ8lIjK2dlFtwwc-EQcwM1DSGe_fRNY3Balul2M3BvOMdJOVmoOVu3jjV_VBcrmPZeKWrfar3qwkURR_B6N-JR9SUlk4O7BV6dorV-9IFTbpDiY-mCazaZmcezfZPEo1KrZtBIUwywfq6rgISos6oq8co_vyLDQNAhSJeGchuEqy0FCU1xcdPp_dIkmIq_Tx6C4iu_x-qxyocsmxEhoqNRmF9aPh2Lu6eJ1_45wOm0Kft4fV4VcfEByBHPXgCAc2YNmqMJNb8-sBGqAqUSuZaYzdqJxFJ0QqRcBWFixa0Eu4w02YQRrtfQXmieuKInlARUmNNwhBnuqiJ8TwsrK7jnPbMSgxnsppoC89V5GFqNV0uxbqup7TfzyJOc4ZLWFiUm3IbkZU2JVk_kZVpTecUGz15xgX63pQpWBQbj-FdGzSjcA85w-BGnRI5zb2LeZ1GHW74t5tBj-5pYHEA-U4ZsIxCYJgpTrXYeQKIt8c1ISA5hUQ_33YF25AIRvkcRaF_kbGO6tkC1RNYecOTXKhrHfbYFVYTd7YKk-uCKt74K7QWiWvveWCT9CLsjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=vHZY41JvcauPBr_FeLMC6PAiw9Nte1JKjENkcb6T0x9EmjQ34hd0kf2JMMM1sCTRKBFUNG577-60gWhhcuIgmMcx3BzG0S8hjs47814saOQC43gRSJ8lIjK2dlFtwwc-EQcwM1DSGe_fRNY3Balul2M3BvOMdJOVmoOVu3jjV_VBcrmPZeKWrfar3qwkURR_B6N-JR9SUlk4O7BV6dorV-9IFTbpDiY-mCazaZmcezfZPEo1KrZtBIUwywfq6rgISos6oq8co_vyLDQNAhSJeGchuEqy0FCU1xcdPp_dIkmIq_Tx6C4iu_x-qxyocsmxEhoqNRmF9aPh2Lu6eJ1_45wOm0Kft4fV4VcfEByBHPXgCAc2YNmqMJNb8-sBGqAqUSuZaYzdqJxFJ0QqRcBWFixa0Eu4w02YQRrtfQXmieuKInlARUmNNwhBnuqiJ8TwsrK7jnPbMSgxnsppoC89V5GFqNV0uxbqup7TfzyJOc4ZLWFiUm3IbkZU2JVk_kZVpTecUGz15xgX63pQpWBQbj-FdGzSjcA85w-BGnRI5zb2LeZ1GHW74t5tBj-5pYHEA-U4ZsIxCYJgpTrXYeQKIt8c1ISA5hUQ_33YF25AIRvkcRaF_kbGO6tkC1RNYecOTXKhrHfbYFVYTd7YKk-uCKt74K7QWiWvveWCT9CLsjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlgHIblS6tYz_BwEpjn6eSeovFMjJXFRdWfUQOIM-aXOatReaLO6HADe9Dbp48YLHReU3rGKmv3dPgElSOnMqlaVsnUFRR09unkxRWFLEir4eSczzxTQNeo72X_kyFry_Hx_chHRnAShtl0qHzm-Qhle4rOSfi2CIDULJTk-UO8S_767IQzvCbSOuDciMVikMYtKyFkoidJPvSDwgJTtauVLBB_oxaGiPg0dpS9QkIcx_I5IcI-5B9vvFfKlR7UQSBjhRFRUjWqFCjNL44qdg0ZoupwDRZAadhRL1BT2CFDELm8eHeKP1f_pMadplhwCDQCAoPspeU0vqbn_j2trFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMY7pNhFOxdb_tCsTUMOfFDfDie2E6HcLy-ufCfe8M7jkXicIgt-U1v5_2RPgnSqbqBzpiWQ7MKAn2QEJFrSY5Zq9DS6hkQALTTxjpju3-LkSsQFI3JQ0tPbTBcxeYl-2U4h5i1FkF3vMzU5rY7Ty974u9F97Zeee2FtyEE4hHRqWnG26Um5por2Px4Oc5_pCrlzDwXbiub_cPH7gpdH0X8m1sNG5aDY9ubjkUMGql5T-bBDqMs2BYnNMekC-dChHPyYYnV4G2rIOmTyzdJNSTPwzil2KAOJ-FsGnChK6lGhZ1gAKIti1gYqdTSaO5ncTKV-WWkzNtvS3vGXfXlfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rczSrwuGuYZGRCysFopAcl8CV463Sk6-SZnKRK46tL0J47VOws-1zvicaum2cBmLQzsXmgNTdZ9pKzgS9_li35RL_Lf2hT1MHU7whf4FoNeGv5-7c8FRLNnecEmzFEGp4kg4RM9siyW_YR77YvW3MG3QwP7gOA-F3u8dLI_N5mK27orw2DrjuwZwr61AwyADvDxP4IkZSL-wew0qIdSamGSO5yhFkkk-FqUnwYB71CRgim0OJ1Bx3m88qKLORs_jrU8H3J8r3YWrRDtyqhaF5uGZueDmG8jOB821lnJhhLpzD7ggyVY7lLYZHkI1DMZ4OfEysDewRnBxUsQxv_FD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6J0Euvkqmd7mSArqoXwdKYhT3Cp2my1jdMCvdZUaR2lUHCsiLnz8NiATBoZmf_bdcj_imBvgss48TK5L1mLQYelJikWl0lBzgDtJijvS6yQEiwAE2a5wtRFbW2l3mmPyaz4RiFeIogE3unpsGn9uqT2dgOkYuv79XXbbKTL3aUfW_Fx91tvONZ_NRZrfSO0A5NMNyKG7ZG-nzQ8HSwS2iuDo0VMiOxGRUXxIU0lZinxKWysVe1StFaUDpX9s2bhBMV0mVkpeEHAPxGQLwxkufluqUM7O_V64jdlubxvkAF3kGjC7_WeoUbgVktbGlN32G2oerTdZj4x0FZuqTMN8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=XxJZhInhkSqvOPix0597iqEX2QJadawLewtd_cTeK2FQm6x8P64MMeReDnlfYuwRa26sheA3brqm7R6jaoqOOWmGNmShJbmsVHUdgjHAzhrOsyYKLXFIpf3aqRviwFQeJODMUs1L46iALZHYYINnGGS2xzlxaDDEN2R6afojS4aog19xrs-a41V-0wFQWiSkmeYqbmOmy2Vql_kRZ7C3ATP2bebd_kbB7rbQVlndPexunJmF43SalFGVVBa8ja2bB1HPxXdnLpQUDFoMzt6-frwTiuJZsBAJcbseNq-LWNSYsiSugw-wdf5NdQ5jnUuds_Tm5LhAepJLUcL7L39qeRldnJ1zn2BCKcZlDHOXTBsZ_dgmdjBpyJWC4-I3lpHRrnYbZX5-82poCu0fSwaQdiMIk2XWVOqpMBk1YIJrHN0v-eTzJ_e6hKVDoYTTDqZ5NX66gW-9iabbxjPsMorT0CXFKT7WRO2FqPlYoU5g8N0cLRY524LHi47FoQAJvtmzxgSn6d5QTUCVXcTQs8IsWJWaD739b7EWHbmc-ANSFFQ0hY6rpL6d0uzPvlv-voWGx2pbD2Oj1PO4ehTFKGVN3ADrQnOdnR5VLPYtm6FSrM0RRrhVluRagAYExqC2ou0o7GCZSBbOuvmgu0pY3qIqct92bKAKrvF8iinZBM8e5ho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=XxJZhInhkSqvOPix0597iqEX2QJadawLewtd_cTeK2FQm6x8P64MMeReDnlfYuwRa26sheA3brqm7R6jaoqOOWmGNmShJbmsVHUdgjHAzhrOsyYKLXFIpf3aqRviwFQeJODMUs1L46iALZHYYINnGGS2xzlxaDDEN2R6afojS4aog19xrs-a41V-0wFQWiSkmeYqbmOmy2Vql_kRZ7C3ATP2bebd_kbB7rbQVlndPexunJmF43SalFGVVBa8ja2bB1HPxXdnLpQUDFoMzt6-frwTiuJZsBAJcbseNq-LWNSYsiSugw-wdf5NdQ5jnUuds_Tm5LhAepJLUcL7L39qeRldnJ1zn2BCKcZlDHOXTBsZ_dgmdjBpyJWC4-I3lpHRrnYbZX5-82poCu0fSwaQdiMIk2XWVOqpMBk1YIJrHN0v-eTzJ_e6hKVDoYTTDqZ5NX66gW-9iabbxjPsMorT0CXFKT7WRO2FqPlYoU5g8N0cLRY524LHi47FoQAJvtmzxgSn6d5QTUCVXcTQs8IsWJWaD739b7EWHbmc-ANSFFQ0hY6rpL6d0uzPvlv-voWGx2pbD2Oj1PO4ehTFKGVN3ADrQnOdnR5VLPYtm6FSrM0RRrhVluRagAYExqC2ou0o7GCZSBbOuvmgu0pY3qIqct92bKAKrvF8iinZBM8e5ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Gj_2coXf7okEPtyRBK4FVggJ7daxCIVsxC-jMIT7zcHUVwDuVZgZHrKbN4IeDEIRBEP49HRh5j_n753hdIZR_paUXgN1V_4l3atrnMHVq2Bmb8LvsmtyAjtll4FJsAXXlot9S0rdzUW6fBF9VpfQx2SZwKG6d7Uo6mp_R2Yy1qiFoGsx1HVBFeeDr1zAKnnJUYi5jzHiZSESqBX51e2MFrB4efERXwNb-tMloiD8wvAdhG7xrbHbEqwn0ZeSAyY1DzqdgBRzlxusDkoFM5YUJwbh7rJlum8mVBkc6CKZwV7-Nqrr_zRY4AoK7-UbWifFIGdudmGdvARr7T1CirVf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Gj_2coXf7okEPtyRBK4FVggJ7daxCIVsxC-jMIT7zcHUVwDuVZgZHrKbN4IeDEIRBEP49HRh5j_n753hdIZR_paUXgN1V_4l3atrnMHVq2Bmb8LvsmtyAjtll4FJsAXXlot9S0rdzUW6fBF9VpfQx2SZwKG6d7Uo6mp_R2Yy1qiFoGsx1HVBFeeDr1zAKnnJUYi5jzHiZSESqBX51e2MFrB4efERXwNb-tMloiD8wvAdhG7xrbHbEqwn0ZeSAyY1DzqdgBRzlxusDkoFM5YUJwbh7rJlum8mVBkc6CKZwV7-Nqrr_zRY4AoK7-UbWifFIGdudmGdvARr7T1CirVf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9ja6D40vs0Yqm93d7UWy1vWqLk8GyTqwSTlEhiTpFhDUqUmZKPNmHropyt5eHBfBOnZU3tU8V_Fxc1hSdQKIDNK0F2wYNm9fIrdSXhCxrhWOLQTLDcdpNixrA4isLn1cD5MpZwXaQew_l8lkxPFy9JrwsWMSn58FXAIS_-UtAQxoFDnYFuKDrPj-48aCpJiPCducO3Pg87oA4YCu9XiRz9NGFsCWgU6Hml1-Ir0_jr_KAbbUWL1VTGQVlUiLr6wTfPpJI1xhMd9ITDL7UHYfIddIAxT6KBgTt__tXquMYXAX3f8PemdbaAS_UzXkkmPIrPqN8URCh67JFRh_O4MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpMQsq4szad5yr0aGamsv8wJyuSQeUxNP8tneCvPF5pubXaGYdoSUEOg09NH28uLLE72unWkkPwA6rFXKBRc5JyVnnfzgDeg74_jdG5M1zVuZuC4sDFs81tCEQXflkDnnGccycKYSa37_qH_o4Zaqm-El2-Y592dUaGP1X7kJXskTp3xYFtzWwsjehpHGDstbprLj0mbbTPQ_CWyhXIUcEotr2V9DZ3_shLL2PjZF_PtyyTHZU9eJ5K25bYTEzg3DYXfEK4qf6yAzl0KninmWU1hQCAR8ZBzFvrNJKl6xS-yuGlhIG5vdiSvn2hKsFCzMVqRWYZG90Q-7EymriNEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQUMwnDNYNBRFaBX6RnEBqOg4nj5w6hFQwtN1xxKMLinLlCDeHSNla3O42XD9Jea9OhU7GpQvzYE8DM6VRhWIn-iQkfpeIj6eZo6Zd1CHT-3mAOh6s69-QPebHxupsE8s9pX86U1ceww9_3mqZ9E2EfEK3HFtRFlL-kwgTsLBZvBzazqmX1YaR7SqQqxea56Pf_4bc_ZUXI9o5f2eWRfaN3ol5ZbgOMnMiMJ8E79AEWqHFtBUtSOmlDzNiOfSxObFShZVn3Fppii6EvpL7ajK7UgKJdJDAWcHLJIJkARVSAFDUFPFOSc-lQvv4VW5AiIWU2aJ-8GzErEEfvKx_kXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vs90vPg_I4E_a3DwuMLh_nmuZQr5duObepeS19WpF4k_iqrwCp0SaHJbGwRtl1je4QBtwnn-KzpLodsfX9yKSQFArheFUTN_v95U3LjSS50jF-S4w0eM-Mt_4ZXfA9aMNwUNx0UVJKvZppSRVRxKOi0KzFxJivyDffMvVhYs9QVfmAl9bOxBbkFrBtD4YGBVa5Z2YwN0HLT7e9p78o8qnuXlaeSUZ_lk1ies6Iiz-1GiyB8KKR38qHKpcQRq7FHhIm8hrfqrowXJY9miYTn9_QMau8mRAxXo9Vr9YqlQzsl_cykzq1J_wxdFmKkYzs3jI5KCz3EHpx-e08b7BPSWwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHlyMapPk5sWCrp3iZ6p9R88_pe7evxf9KorVdACK0ceORaK1Dpj1rUOzGGPbC61UKE8PlAXeBOh2lnt_K4nk1C2vFkC4B76JxISoqmwfM-NO7LzgNswh4iA70H5UJHf6DcoTPfM-CHJJVYySVrVPQgi32wRRBrf0_AbabT7UqYQXuqpfFNjvOUDFPGQM3iBk-xiYcGy3bJtQeh7-XMMEMCuNl8zJQhVf1oEKEGuvOyfMD5GZLX-sskBk_rNr78fWrKrRbzKhhzjgCZhNLpDg4fRsHrfvhpMpDqTkNPO1reGKmdQkZgxpYtK7ZDJSKfa17b26Fkde3F5e4_-bkruXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGKcxqDOMaOEsF7ib06O7WOjFOdILLdcaNgNSun8bnZbtSzwC9hGpxLqHwFw-MvpOCb0YDtGHdjiiYd-k3ZdzKkPvb7hQNraCfCCy7Rl6BiDAr1n0kiZn5g3LPxHJ4xYNTPyNlwx--VHcmURSYV-UKf4B5jvfm1tq3_FVAX1mfBigZA6xLFznHeP-hHWYE5MgzvVYPKPRjfWaAbJVEPNaqZiLcfwS8NWkbe1jH3fyEPjt3GZg9OfFaADjIXYT9dPWAsaA_MChou9kD_ji2o-1ld_mKW4_L3Br-PUj-jynj1WVVowpx2r9SR-_ItLd0sms6M0SacM0ylE6-DTtCRm_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQX3_OkxKRwWCZqNrglSRqmlp5vLWNpmuhqqeNuK5ksXAjDu5cNb09TUZsO-bwCjnAiJhKWcjUee-mMWaZEt4AtFa4shAmwQ47m3p60I8U6NZqpj4zbMv-O6Kk0DJuD3-BMB5F9W5TES1Xn9H19YHpSd2YLOVF4l5QhQUunC-yu36mJ-xaNFovEfba9a-TwmZU_6IyK2F3XfJrhWuiRJ7MKXoRfr_-3xhwcAuf8hAIDpy8ecSfTaVAU_gOo7lAdeisGIpHZsGa-SWgvbf_vAiF3Mf5JmmqNDt7hTUvcOE761tpnxEj3mwZpu7z_rO2aJQ06cSoNo2dGseuvKDnDoRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=SrYv0fdZZr4ZKbwLRIbiT1L5VGkkNBHI_3oZ6t3L8dwuoDiCSAxyvdK5Jo-EH95MT-h_aJ1LdachpxPcaLrpvbTr18lgAhmEL2MF9QRW-LbUYko1f-H9h8sNAiY0aWdOZgD8rpeC_X5T7_FGVwMXz_ww6kRazNPWNZ_yJAQ3hKTR-hPn68sxw0issvkrUSL5is7JwdXWSCL3jEu6omtFbIBPiMSP9YAEx8M0xPta46X24AeXqLxwlcPWhkdj_i_CyDDU_ou0V-5riteFmoXIornoCTG_jO1G1yXEny-aA1xqXuL4qbxfh6x2LuJZhPWS6k9ghRcKc9iJDFDynQdcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=SrYv0fdZZr4ZKbwLRIbiT1L5VGkkNBHI_3oZ6t3L8dwuoDiCSAxyvdK5Jo-EH95MT-h_aJ1LdachpxPcaLrpvbTr18lgAhmEL2MF9QRW-LbUYko1f-H9h8sNAiY0aWdOZgD8rpeC_X5T7_FGVwMXz_ww6kRazNPWNZ_yJAQ3hKTR-hPn68sxw0issvkrUSL5is7JwdXWSCL3jEu6omtFbIBPiMSP9YAEx8M0xPta46X24AeXqLxwlcPWhkdj_i_CyDDU_ou0V-5riteFmoXIornoCTG_jO1G1yXEny-aA1xqXuL4qbxfh6x2LuJZhPWS6k9ghRcKc9iJDFDynQdcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4xqgPz8ylzjtdFTlJf0eP8CccACkZYY4EFYUgvu2VwsPc2mLO7L-I5WrwWT9lVH-NIAc4YMXdMV_rAlF6OsyEcMdyDpcW9S-g2pi9BL-3c92F2vt1qYoyZvgFEmUuFRBipcIwzAVatwQOmerXMXWEQwgCvV_uZjsMLPeiV1OQx1_7Ts3taUKfvHHd-CeAeDTIvM9KW8huFTN0XsfXSgNurz0MDLudeXltM9c2xoJ7xQR79eutuKdDpmszsYimKP5KN5HLa1YZqj_j0VXrbbklnuni7Jc2HB-GLlgMFgXyGTrKI_oyqy3y5EtSkQ8osRTyMXY1qSQXJZORKlz3gNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Cke41Ym3iKcHF-jnZt5JswKzN41J5EGCFxk2eibusX3n3-3pYVoL2q4gWhaCtIjO19Q8KueqhpMnA_i_iB6fVVBYknTMJo124PvYrXJ8HAxdqy68byCO00PNSKqN7V7UsbG4XZ27xJrGLc7O1W5kvTYeVjyytcOW8cWDSCrUcLyl-jLTF8u5eejKSee2kf2Z8WEihM63RmKHheoroT-tvRhwr6D6xPS2DzBjGD5l2-2ZWGJwXT8YopIHy7NGUGM89FO4KEjNDM3K-eXRkEKCjryd9z5MmRN1N_a64zwgN81C15dxIR4z8OHI1IHZzwuJtOUPMQd_0ccBcf3sK16tBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=Cke41Ym3iKcHF-jnZt5JswKzN41J5EGCFxk2eibusX3n3-3pYVoL2q4gWhaCtIjO19Q8KueqhpMnA_i_iB6fVVBYknTMJo124PvYrXJ8HAxdqy68byCO00PNSKqN7V7UsbG4XZ27xJrGLc7O1W5kvTYeVjyytcOW8cWDSCrUcLyl-jLTF8u5eejKSee2kf2Z8WEihM63RmKHheoroT-tvRhwr6D6xPS2DzBjGD5l2-2ZWGJwXT8YopIHy7NGUGM89FO4KEjNDM3K-eXRkEKCjryd9z5MmRN1N_a64zwgN81C15dxIR4z8OHI1IHZzwuJtOUPMQd_0ccBcf3sK16tBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSX7HxPTB4t5wdeHysp4xhFTo9V75eR8OoBHuVsxyzLmnMZ0PtNNh03mfzfd-HxVzA2MpL03kAemuJIYMh8wCaZSeCgddk3S7jrIJ6HYY6UudBw9lvnFU6JO2UhLJXl4aV7_CmtRB26yoeVkHx6FQd2cXiowpcmf6IRZZJEiuteL_QeO1yPT9EY7ONlZkD9Xe-sCv6UPmjslqDlaZ4rvKn5z56w8iB6Mm5XTUAjstTiJLZpHanEw7rIOcoHGvWQmniTyRRPQupW6ynPftAazjVKIVSwTnVXVJIT581nFPGVBt3tqbUa0oZcRAeAzJW9fsp_VEDS7AfQ0SVNhZUS5Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHay6CEIWx3fKAsMb1Vqi0QMYPrQxEkP0D4TUe2vbMIvDxembvu3L0toDE1tX8Pm7dJyPuyr_zi5ju7554lNxvCuNvQDQghZoU4JHKj3eC6bEciZCF3B24vaDD_D3wXiBUrkxvv-yHx_9wMW_NVCjQLJQlAoTUBQngCa7Hwtwmsinop6Mj6IuVjtbSKFH7Ky6GLzo01PiuR_jbxEMbboPvziRN9VZN6xeG6rSGMOepkXqekluk6_If718Ejy_sTMDLeji_8qyL-u0YM9iaUXqwEt25Bq1RN6ALdml6cK89tnRoD6IjI2Aonxvhih03qQGW6hJkyCFgjjlSVIaPXhtXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGHay6CEIWx3fKAsMb1Vqi0QMYPrQxEkP0D4TUe2vbMIvDxembvu3L0toDE1tX8Pm7dJyPuyr_zi5ju7554lNxvCuNvQDQghZoU4JHKj3eC6bEciZCF3B24vaDD_D3wXiBUrkxvv-yHx_9wMW_NVCjQLJQlAoTUBQngCa7Hwtwmsinop6Mj6IuVjtbSKFH7Ky6GLzo01PiuR_jbxEMbboPvziRN9VZN6xeG6rSGMOepkXqekluk6_If718Ejy_sTMDLeji_8qyL-u0YM9iaUXqwEt25Bq1RN6ALdml6cK89tnRoD6IjI2Aonxvhih03qQGW6hJkyCFgjjlSVIaPXhtXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
