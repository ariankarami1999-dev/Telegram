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
<p>@farahmand_alipour • 👥 65.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 18:14:17</div>
<hr>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=Q6CXGZnjn2KI5q9SEU-v89Ae7-dXLHQCiXQLDMaJwdGKmsKUMT7mwmuYMNvapNrEJEI87CM1pEjQJaxhHaBGiOfJi9GeuqXDjQxEIZ_bcUlUZGfhi_ynxQiJi3LKR2Htom5x2TLa6Z56PX5nSsEGja37pGCrxYsMihCaATM22JT_JyCxNiqmzqBMXzEe2SgCVMS6ktxD_56qI6IJFZmF9DoH6gu6_IdqNV6DDSXYVQyJv2uq_OIhig_YalVRtApTlg2C5Yt9p4RHLw4zbn3lSccLliWf4vuAlIUSQ3rbdhHFgiP5SAhXdru178-TBXLoQHMfsd53D4D4ory_yJt7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyz8KQgG8dyLlA-lOtBtmtNJ15sXU_F_w2osYaNOFrW4mr---7KH2WgfIq01i4mY1DZp_nM-268dGPWcAmlu_YsswMSS6wMNjkoxWPqHIsCQ3-ezMsnzK4KAe1CtCn3Qjjar9xJ7TIn5-KtdsjK2EDaruMjnuRlt-BScjzklI43Gn-WGgl_BiCkwC4b2R97KNbpYLoi9t-bK6Ic_nyj2BTUZkQg62TMP1bK-PqjraY8Y4yATIcoWOK93jIrGY61mTfI4iB2K7BQyRs3Qi6TEZxVs78JhyoUSZQpLrr0_GyACdOLUgFyl47EmEPRZi_FBgpvW9xzk1hp77osAQpd5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwY3l1k1km-H18T7AR5fzIJY965XntYNPPyw9EgZZVwkbRaATZiB3o7JlXJuhPZEfe7VoNM5CBrwYdM_I3k5F8HhIjAxjtiEmBbr6PAyasyXsMAqD90hnw_aRekd28TyERHaRI5JTPgX9T02pEX38tdPKZyIl0wSM3pTtMRHe6xLqRtbCh1XfcTlyKerI7rW8sgyaXRsV57LRT4CdYZR3NGPh83AoUZuSt65Jyj13YOlVZ9HFv8q-QmpXUMtscdvS28GACIF7FnZE_8lEwdix8aUrjDFJchyPEhaF9iXDDGM81GOX4-vi61aFdj3e46KKGWynJs32V5WuCDJkZVXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcKglXzV4H_vXAO2z29h6-c1qsWQl9h5aAxrIdVtVvaWhkzv5x1ravoKJMpYsQJZ7OAjmQQTgAP5JQ-NAqVwRXKW2Dbrc0EUW80wv8IORNqVU1wWUuN1NnXD6ayAmdLZ_DaUxQqKQ_DaaLsyUPUIWERwgcPpCYj0LgSVkZqfQ7KyV1Nx3oneIYq5W7oG_RNyunfDZIgdKUrJ25ubhrfDigNC9FnEUnbD1ODyzUVWQMha6KvAmbn-rpHz5Jt5d9N9McpG4VKasfQpKzdsC0ZIbDa5drE5KaPzKnab-G2vYDLi_w6Hqv9gHQdAWWKyZO9Jbx7sa_rUY8qsLoKomw13Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmUG_DFFyYyHMdYHXMBn7YiEeOBiWZ2oAaVJBOkx7gOsthzfiP9wzsnStEnoir5xNKwmTRQkRo5AyG-rzmAJp9mixq_mvSeALuqAlD7K4mcTWpdd8cf_3xzExxEeWnNUz79QTYlX1LM_oI_88owxuEyYmqriKr8S_dqI6EPJP4xBl8IYUe9j11ekoU-JFMe6yzsBQIVXYMcfI2yvOt7FO2cVpLamJilO1i0OFrgTyoZuQ7-HuKOsaRlomdo8GyAyP3SErMoBVBicg3XzH8kyhYTFiDLMgP-sKRUY5kZ1EXGaJVgp0IYKY-jRayQWL2mmCAOlnOwdttk8rQIlsyN0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL7-jPfZn8J9aUDQyZaycm2pHRUPeJUZIIGORfi-JhzmMOSCDtrnMOHx-ixTraYvbeqgRRyP3ECaqk-UHRCL1w4_CJSAzeTVM2mNP9vlSr3kXWAHULvM8bj-auVS8LBTAmKtZmSooUSi0hucS_VFUy8dv8-zsePFVADqraygzUogtfZtKioqOUWwdvnMPHrd--ZpGqluHYg7EITxynJYBl6LVRVaBLUi3334a-3hRtHPsNWIb61WCp9F1zZBUhUVVzH3LP_A1MMB-a-o01BboWI85eEgdG0_ob9xAr9oTFyxfuWvLR2NBJ7FTNBB8UDZnyaI2v48lG92qGkoWxv1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ4tvNeLANc_243CRhcWn2NZ4zNRJ4hQKpCkyh6K1HAZcqoMda8TmjuFHkRD6nmpiDeUkbiLntJjmkKR6LSstpDqMdvJQmNF-HDKAaS6dqC6gYQnbZlV8DXYcGIEHLJ0dDkjJJk4tdjiEeZITQdN-s4OHO2c8B-u5R_ACqojXtTvFVoBicmjCuXI5PkhV49OhP8oNKhHjp89SDyn2Gb4yTdSgnRiEtbmSsSyrKwxRP1yN0W_IC5NyjK4EGn4QuVNls9o3LYVzVdJu7ngMrtI9Na0D2o12KNJvh8Bppo86zIIsfeKh5568hGHHjCgVT6hnHhs8ospXcFkjylO1lg2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=WwfXI6AAqXtk3kz2jU2dQU-QPs7IABa14fdPMixmxkvd07jc_vH6Ozy4S29rCSStU91wJ3CH46i24-UANOGiSmoPPh42CcTa1CTv1IhoLMnGrXidccgZ1Z7WqSq_z1WR6bOfpruGVRyyv_q1wuUmOjqMwNjKdpIDr4cKqb7lgGSoKJK4ENiIS4u5O4SOMCoLeI51ksC1vIv9aDeN2Z8XJffAPmuRq5Zp0wKaCvSe9Yztl_h6oQjgHqjw9BR20VXH7f-61JFUim0rGO96-3Kcro4oOhc9vrv6aIWx6jy4jmAZFUocL3wUUXSSupm_7xDyd8hQSsYKYd-nZevr9uyJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=WwfXI6AAqXtk3kz2jU2dQU-QPs7IABa14fdPMixmxkvd07jc_vH6Ozy4S29rCSStU91wJ3CH46i24-UANOGiSmoPPh42CcTa1CTv1IhoLMnGrXidccgZ1Z7WqSq_z1WR6bOfpruGVRyyv_q1wuUmOjqMwNjKdpIDr4cKqb7lgGSoKJK4ENiIS4u5O4SOMCoLeI51ksC1vIv9aDeN2Z8XJffAPmuRq5Zp0wKaCvSe9Yztl_h6oQjgHqjw9BR20VXH7f-61JFUim0rGO96-3Kcro4oOhc9vrv6aIWx6jy4jmAZFUocL3wUUXSSupm_7xDyd8hQSsYKYd-nZevr9uyJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stsmfQblYUflU_agziC8lh4mhq4UF_KBDXsLvkue4Un5ZKgHqSPlkrwzRHOh326RacYz1kIbETt49DvUM3ebDurS-0QJYJtHxF5cnj0w01O_Zad-ZVRd0nnN3cAZdH2GvSM95OeX6QfKR1xXuTrSdSHH-CF0U3iwd0QGrYaV75nLrZs6CeAqmY1BBwQYJM-o4-onxv6M51DbuEGLGJsi14lbB7sDvdyK_ZSRjq8jacI64D_VxId70BQrYMKHaSc0bGIG49B6J-IQsjgKobQAaELDEVjhbDrbhWwL8QI-K2Iup4dm1sv-bQ8KKsdsRTFXe9avlUlOwfTkDAYI9z_w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0ujRD9mSVRrzD5YvumWyo4l_YeiNnWsZ_wV8SKAfrxftrbc-j-AVrEsnjzTPR47IpNwJY44qwlHw7JhlVM0Zue_2fdY8RPaCXhkul2-PBzWISZe9_pE_fg6V6FsefIhLONjpRxzM0ICCQPl_fcnlfHn8fq1_3gSs-_k6qL8TqEOLQYNiWhv8xB5_aBnqTKbxP4XckSNNcOqmX5rmExelMcYt4dtaVwUODP7E7Cg9fMS7IXvh-TSSe8JqaSsIrvblyMRVMKGlKneJCij6ZJElhe0it7xyN5E1WZe7HUb_LHVfxVdnRWF_z0OCt5dzbhhBU4yPnKpfVfrgvvMU8hnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=AgpvXnPjibLqLkyeYl1B5JAehRqiptKnyJNHa-KILMUqkr0xtkN2RInb2GCwDYuXnfvl5ov7bX0XbwdzVx6Gu4WTVYpi7aSkBrvWla6KsB8hfNgyYPywhwmxlJwZ1zPoiwlXQpDzPc5nJH_Y07UVJD8h0ZZkJFM_j3KPXjHBgyhymxRHIybQ9OHusS9-9UNwRNjHyU17TAXWD2R3qblcp0yEVMSGRqE2u7dCsiZDb70WEERBGg2VD5aekApFk5KvtEmSWmhqmPlZyUY2bSGHzy0VhzIpXCVMeKsRHi9bGs4xQXd4tlwEVWesWA09xoTr9fD_0TkxI46_P_qKXfNjf7MnTLQjV02RVlgdhl_GEp9zH3RkKwUhm_XfeRNnndGR__kIFpXkGTrMXcGSeDnNE-hDNcSOTDFi83tUq-Y-WKkTiUrCBMOkyrJhwLm3qjg6I6LEHeUu_FmDilQkdocEP_12MebdVBdS7X-ZTshzFJ6X_Z1ZYuHyEayFcEs0DR4IIC_nnywMhRvR_LVrJOqfL2N3yPfN3HSwlbI64FQWcv711sSFCyGj8wMY85K_KX9x9oNfL3ekkIwY3yvOiV46Necc3jXLWzRmCqmLUq4qNPF3_2fnpGbbC8Dh2bkcmgLbMfhFd2EFg445sInPmZZkd_IRb1cnDn7cj2GlNKQvePY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=AgpvXnPjibLqLkyeYl1B5JAehRqiptKnyJNHa-KILMUqkr0xtkN2RInb2GCwDYuXnfvl5ov7bX0XbwdzVx6Gu4WTVYpi7aSkBrvWla6KsB8hfNgyYPywhwmxlJwZ1zPoiwlXQpDzPc5nJH_Y07UVJD8h0ZZkJFM_j3KPXjHBgyhymxRHIybQ9OHusS9-9UNwRNjHyU17TAXWD2R3qblcp0yEVMSGRqE2u7dCsiZDb70WEERBGg2VD5aekApFk5KvtEmSWmhqmPlZyUY2bSGHzy0VhzIpXCVMeKsRHi9bGs4xQXd4tlwEVWesWA09xoTr9fD_0TkxI46_P_qKXfNjf7MnTLQjV02RVlgdhl_GEp9zH3RkKwUhm_XfeRNnndGR__kIFpXkGTrMXcGSeDnNE-hDNcSOTDFi83tUq-Y-WKkTiUrCBMOkyrJhwLm3qjg6I6LEHeUu_FmDilQkdocEP_12MebdVBdS7X-ZTshzFJ6X_Z1ZYuHyEayFcEs0DR4IIC_nnywMhRvR_LVrJOqfL2N3yPfN3HSwlbI64FQWcv711sSFCyGj8wMY85K_KX9x9oNfL3ekkIwY3yvOiV46Necc3jXLWzRmCqmLUq4qNPF3_2fnpGbbC8Dh2bkcmgLbMfhFd2EFg445sInPmZZkd_IRb1cnDn7cj2GlNKQvePY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=itxmjunk_WGxtrlKn3AcGTPZF0gmIC8P5tD7VswB-clYQ7nzO_SOAe7L_r8MneQ-45lS_6rJnnCbnEnZXJLtSxifJj-IHpNP6sjO6wAngpNU31Z60yO3UcgKFB7Jmf3392ZOyUiBlzz03A8xSOLQoErHLQIEhBFGLHx4Gr1EvbiPPVy-uZDnx-Z25wP_-QkCxuGiCjnridUe6JBzmkarl4iO60Wu_Y-NSsMKODmjS3GR4GuU5kfhbM2wpUVOcUJcQ0w6iCAuQDd7ksGOATg-Gjs15ehiczCTDo8ECY3p1dDaiAQ17Wkny79lCnZUdkDt4grfoxqZDQ3iVheFO-pW9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=itxmjunk_WGxtrlKn3AcGTPZF0gmIC8P5tD7VswB-clYQ7nzO_SOAe7L_r8MneQ-45lS_6rJnnCbnEnZXJLtSxifJj-IHpNP6sjO6wAngpNU31Z60yO3UcgKFB7Jmf3392ZOyUiBlzz03A8xSOLQoErHLQIEhBFGLHx4Gr1EvbiPPVy-uZDnx-Z25wP_-QkCxuGiCjnridUe6JBzmkarl4iO60Wu_Y-NSsMKODmjS3GR4GuU5kfhbM2wpUVOcUJcQ0w6iCAuQDd7ksGOATg-Gjs15ehiczCTDo8ECY3p1dDaiAQ17Wkny79lCnZUdkDt4grfoxqZDQ3iVheFO-pW9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkXPg520gwknNfTnaYYT3oQZ56RihYI0LoHHrsAM7eOrQWhhDIcHufTHoL-Yy_n7iQuhwYnk9nmzkankfVWlGMbbfbDy6f-Q9V4dRNj2b099qZbRyeHTFlYPCF2DXKM0guqYIRTNQLNxq0oAJe0hq2R-zqv6QVQRspE-Q2Lr24cJq-qQpWmrjweiYwD0oTO6OaEqcikD250o4-kXt04ZbeN-La2M4WqdWvrh0bKdG8U7bxINyfjxnHO1ZZevxqb3pMRg7oB1csZHXGWjv_GYl74i4Z3T_Bv77XiShj_rMYlEkTbPHE_jPtEZhU6q9MCw_wVQylOU1jGSgDSSa05dYj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIkXPg520gwknNfTnaYYT3oQZ56RihYI0LoHHrsAM7eOrQWhhDIcHufTHoL-Yy_n7iQuhwYnk9nmzkankfVWlGMbbfbDy6f-Q9V4dRNj2b099qZbRyeHTFlYPCF2DXKM0guqYIRTNQLNxq0oAJe0hq2R-zqv6QVQRspE-Q2Lr24cJq-qQpWmrjweiYwD0oTO6OaEqcikD250o4-kXt04ZbeN-La2M4WqdWvrh0bKdG8U7bxINyfjxnHO1ZZevxqb3pMRg7oB1csZHXGWjv_GYl74i4Z3T_Bv77XiShj_rMYlEkTbPHE_jPtEZhU6q9MCw_wVQylOU1jGSgDSSa05dYj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRT7OubYC55C_GhQSow_qZNzt9vJCwHWp0dU82ptT12Hf2bC3iiID8mdpfGntc7zsltu8DYkMbV5kGE5guTKQPj24mSvwfddbvig2nOlv-4ZiQHkhmzC4Z1N81yENxIG1zbBXG2_49vaYAyDsCRsP-0fahLHmN5FBW2jbP2N0uDBOWNA4Li507Vh0wEi9BEKpGwN9KOwU53kvCvMIaErUTj43hgZlZc5MbdDmvLVZDHbs18GOdtKGva7BvUrWNXTe_4E7Q5pzfynhUlOImdWgw_NWXLR9yqxJC5aU3ldbU14hVPZcTKKeBVcGMAdmAEix24OqEN8kS8EHrTywFMfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqYwInD7AepDsNDCJ1C3OpSrv6T5L8UysR9-GxBQAoKWaCN14m5UuznJ6ShfD2MBLrLQw3hA3VgM4gHqMpPcXCplGBui1r5mdOmAfm2WHpBLLoNjudV8IPpAhLjQGDOARPVSFMupIo6K0ycOi10Yj47SuJnKjNjsnpMOphOrlusIAqj21sKgs44-acWFulB0h1lXuscS-nT58Lvn-Pkp5OtpqjCd7go4YEc_rJ_TiLH0BNb-VCCbj3nD0bgGqMhco9KITs1-qqh-gWeoHqxOyv_HjcueS1zkt3cVjh4LGFxyGaL5E2FVNj5TPHNf_pxBr9W_-1PicRbWO2kGzNfU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg0TOn9TWnRqczU-cvBV9htlzRgzlawiXr3woKPswAuBU1wqwD2yI96x2DOiqME3YGlPHXAQE4ILp4LYWbU2BHdUTiqXrDigk-JUSWYzUi7NblUm31vMXmV0U3zxwJEriUUt9OzfmDPY7UTXlc9aAkSw0-bgwuuJqvT-bbGOoD-hsPr4fcSI3qOWuqTm5l0zooAf7ZVu8VVUL_oC3PoqmOpVU0IYsrDepoJ29jRkA722SItK5bXIbc7BLfa7TqqThi9BffkhMNHwFvj1-EU94bkekq_sphxEMd-qbCKslBndxQATkCbitN_-h4jRlQ3m4ID5YZ9EvWqHzwEMF7M3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=SYL8sxHGQHG5JxN9fBUEym8GZoItpH-sOXZfWdpbxOFTyg8znzB1CJsWeHvYUmcyPpf5BsmOVON_34KeP_bvsDqvLF6l0D0sIefQEFoDu5HjdSdd1_QPgaBLrbHfgbFZGUF3kRritWuRsbFmUhDF1N3tTeC4dsklw0D1-FWg-auqn9n9LsMfQcnpfaV57RlsJqebYkUPjCAEGEJ3VC5rC5sxy458wcL3AVZyVt8IuWmNcM39EIYiCCq_5uF3TD62k9v7q1xM_BZtRGt3USNj3uH4ycc0h9IP7EVb93skiOJZweMYW7Em1zEvc8WIaSr_U1iFmfT1IBwX06ZVToragw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=SYL8sxHGQHG5JxN9fBUEym8GZoItpH-sOXZfWdpbxOFTyg8znzB1CJsWeHvYUmcyPpf5BsmOVON_34KeP_bvsDqvLF6l0D0sIefQEFoDu5HjdSdd1_QPgaBLrbHfgbFZGUF3kRritWuRsbFmUhDF1N3tTeC4dsklw0D1-FWg-auqn9n9LsMfQcnpfaV57RlsJqebYkUPjCAEGEJ3VC5rC5sxy458wcL3AVZyVt8IuWmNcM39EIYiCCq_5uF3TD62k9v7q1xM_BZtRGt3USNj3uH4ycc0h9IP7EVb93skiOJZweMYW7Em1zEvc8WIaSr_U1iFmfT1IBwX06ZVToragw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BppccXV6Mug3debrC846TyUmxswniNN8xBwCSY5iegniS7veA3trN7VNg0Somf3xOKFi0WinTLX3eoKRhH9eHi1eiQYgTQCDTc3puPRsLQqfWiOjRTMBpd9W3GrlKbg4C3AAentJzk1WTiYTGW-baR9BsC6jXkxcP26dJT9ygkyWZQLtdsfm81wudtcE20tTzpAC3IgMGZHR_UtiiePBfU_6VbqU932WiGrQ6HzBAYdhKBdwgQ8kBNCn2gxsEw9bn5InumiHpYeSYUTPFWiuMkazD4bmSQ47gIZ8EwbQXHaaGQmMP3jMYZ2B1Fto6lZRkRSlYhJ_La4EeYE8p5iEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGJN2ukXFTvKOwtCx7eClPX3CkQWZX8reXx8XbbxOIq1gZQMizHeKYm9WgPmLv26hQdmiuo3VDG9YM2iHu5wNkh-DrrlaRBufyfZtyb2k07GUzvUINIv3pcICTHUGTjpex5QNzgAtMckblNPlTq5camwk2rVQtsB0uOeu-WTfkpk5BwSIol2GYZoA5tV-vHSkoXZoO0XpLPj2fu6CXysIEEV9J2ArBb08wWvMOSE3XLQ0LPz8Ih033KsIs5bz5HdRdozhuKeLr9N68S2QtcpZVZzgPhzNlS-RvT1pYgufvN9JqJSlaKCKfwbIdZgQSzYnoCSDn2MjoDB8teogQUDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5fpuC7I8eW5JF6-utlTTgAWf8y6ky2KiA74K46dYa_HhbFRWwUoVQtao_2ESWos5Nj1GJe_DA_zt8l161LOk4EzpsiaiA33xjXoNvKBKTQKBMg1BYYIk720wnBRuXkbxHP6PlgnlBZrgmP1LgK8zia3h45peqiQFA_ACQU1okXbN-5YNY8lMZPOPrJWXmM-vG0e-KccCpy7rvQPgpVtGm7dQM8bZ3iFSzhQ4qQRVwUjRuscrd5YnktLahoPCiKbBDdl44Ir2Dw6HDfMjc1fx-9iqK2vNjVuR3HAYZTKNJ1gqMagZswvr1k3Iia-SQ5XIFhMummnN8kd0n5kc8mqtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obRGf835y0oPLkp3TZfbahJ2jxBNPfWEqi_-bx6-bFUeKeyzzrXC2FHpufndmyZqYHGuohDcF17_4L6xEsOb3SEIrYcDgFRUAFnPKS5EJlaOPsLVizaVKMv1-fEgjEWPPmmSZvXDP5NpAx2bB5IPX6pfnDSRVUBGqcQmqhnKN6aL1gG8pKYGlhoR2dmzpOIgKlBZ82KhGhgJZGlrr2oqsePynB6g2oZ3cllHhhnI-UjvZIbQM2YsswpYUjg643BcxHtTb8Lf5h2U_9Pc8WloAOPVnTgwH3gE23842aSbmwA_BCp_d279EvHEXSfkpl0gz50s6UOeHPkktJWPtjLlgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=d5dtMzL46K0uSDyF5yzMqlVHsFJxtRfIwm6K79ydMTcK2xU_2HZ1Y96FoJkFdmNWjSKEG50rnFFBc2YwAvyNzmSgmJX3bcEu4ItjnEj2a8Sv3Zu98xUvBncA-3ySLy3-HaGXPeZzQucsmZMb7WsrWqUwcx_eZoZQa3B3D5WB3GTJgPVqB_at5OShoGmcT-U5pqm2yY6CzuJb3sr4SJjT7HK-LaCFwnTZJnXAHSd2SIXj_bm_D9QW23Q06FTBqhhnEK4a3uZo3rvTzjMPzk3f-SXyzOz-WzV_E7qdQQLZmORXA7NMEycW1ts-u8mc1o2OfzA1K1OLN5v_YtmOFg3sUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=d5dtMzL46K0uSDyF5yzMqlVHsFJxtRfIwm6K79ydMTcK2xU_2HZ1Y96FoJkFdmNWjSKEG50rnFFBc2YwAvyNzmSgmJX3bcEu4ItjnEj2a8Sv3Zu98xUvBncA-3ySLy3-HaGXPeZzQucsmZMb7WsrWqUwcx_eZoZQa3B3D5WB3GTJgPVqB_at5OShoGmcT-U5pqm2yY6CzuJb3sr4SJjT7HK-LaCFwnTZJnXAHSd2SIXj_bm_D9QW23Q06FTBqhhnEK4a3uZo3rvTzjMPzk3f-SXyzOz-WzV_E7qdQQLZmORXA7NMEycW1ts-u8mc1o2OfzA1K1OLN5v_YtmOFg3sUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=b8mPaz6lMqaGz9-QIk6iLwFEC_l2fnQ31npAWBW9U4Mn7BmtI5wT6_NDxSz7z8-RMMV5pbqGrRbgA45JB3c5waqgPPMHSYSG4eb881FP8pDc1fR_sZhzoWoQFOK49xAddhcOJPIdpWu_lnaoVxFKSuFKRhNftJg_mNm0pU0dzXhf1LreboNeJBq-hxdzi2NRKIKeTnk_5aJkyglweAMHXrR7xFmNcEaqef_-H5CEl4HHX64_sF-KulKH-zizoYqoPzop62mu4jm039FZdURurwPn1GfgMcoR1gGlyJPydGQ0VnNXiX9RJ4poCNrkoaVyjuUTUo2vKDGHt4nhYjFatw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=b8mPaz6lMqaGz9-QIk6iLwFEC_l2fnQ31npAWBW9U4Mn7BmtI5wT6_NDxSz7z8-RMMV5pbqGrRbgA45JB3c5waqgPPMHSYSG4eb881FP8pDc1fR_sZhzoWoQFOK49xAddhcOJPIdpWu_lnaoVxFKSuFKRhNftJg_mNm0pU0dzXhf1LreboNeJBq-hxdzi2NRKIKeTnk_5aJkyglweAMHXrR7xFmNcEaqef_-H5CEl4HHX64_sF-KulKH-zizoYqoPzop62mu4jm039FZdURurwPn1GfgMcoR1gGlyJPydGQ0VnNXiX9RJ4poCNrkoaVyjuUTUo2vKDGHt4nhYjFatw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=GJ8shpttfbqxZqdfXK-Tr1tazc7Gz2EX7gK9uLkxijKSI0JuaXhnubVovmoRGO0lL-A6TU992-imOHUZZhByM2l8strrB3tmKAgvWOyexScDnYDpje7AKhBNKFWpsb4-spPTILoOuwXPzpoQvjOmto00YVCqL4bkaLLnrOTEkKjcb2DYc0ZkRDSt4NC51pQemBd-uYj4EoE4R4rexDswTucsrGHtyj3k5auMwqgAgnFmh4IoEYV7Ki0bJxOre7LGgU4BUPdqlQYrVhR_uizsp8Vn9_crx5_V3HWEPwLKh6VTtfC0F2hoLjxWzMHeZJVhNksXTeEm2MN9jUBl1gY2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=GJ8shpttfbqxZqdfXK-Tr1tazc7Gz2EX7gK9uLkxijKSI0JuaXhnubVovmoRGO0lL-A6TU992-imOHUZZhByM2l8strrB3tmKAgvWOyexScDnYDpje7AKhBNKFWpsb4-spPTILoOuwXPzpoQvjOmto00YVCqL4bkaLLnrOTEkKjcb2DYc0ZkRDSt4NC51pQemBd-uYj4EoE4R4rexDswTucsrGHtyj3k5auMwqgAgnFmh4IoEYV7Ki0bJxOre7LGgU4BUPdqlQYrVhR_uizsp8Vn9_crx5_V3HWEPwLKh6VTtfC0F2hoLjxWzMHeZJVhNksXTeEm2MN9jUBl1gY2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIu86b0VHuUY6dRX1SEb_NwMBq9Xgk_uO71xtgP1KtXBj1fZxiHhObuYXWmLxgTwcOxfHtn1usp3MXcLTBoxI_Zc6_Nux2A9WwxUckhNn7wpmVmOkPdsalzu_QIhhkpt9JLJoy2WjUlCcozs3ucWtumxNYoulrTzrGZtFaD5UGJjMaFDJ87j5EOOv2dtif5Vp-RxLiVS0OTPWdNaI2SFL1RhujVEaKC-tzyrlPySXgTqt_4U1ZASB74PZVKTxk9xCZfCSqhPQmV-KOlkNySnaoHRT7cfq4ZaeL-NUxtKaqiAbk3EY2yR6zQJf_53H3MbKHPfuuJhUfR77MlVSOXqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=a391dg-FZUjetVTEwAR-TPz7Q_uWpCgMvJ6e6AW-j1hgfEtW0xlP_nDoK9jskex6IQ_K9zgeW-degX3wgFa0eTacGIKSLZgLfv0nRPe1q91DWJpQE9MdMvA0UyMj8CbpN3NZkqxsNiskEb5qjTkUll1OdY8H69nwIgiL_21DPbePkGeiqmEmQxB-i65xO84OwV9hp7lhHJHuaRlGSRlPPEeuIHKOaKwljkpbHEh8SNZyBPvZgOZf5qMOg38CCqburBaDU6uwRCJ_bu14erVjpWR9F5TMpaai26V96vVy_poP8FmN91KG2yWzdMtFqMi6w64hjI5pKhaCY9CDbpLqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=a391dg-FZUjetVTEwAR-TPz7Q_uWpCgMvJ6e6AW-j1hgfEtW0xlP_nDoK9jskex6IQ_K9zgeW-degX3wgFa0eTacGIKSLZgLfv0nRPe1q91DWJpQE9MdMvA0UyMj8CbpN3NZkqxsNiskEb5qjTkUll1OdY8H69nwIgiL_21DPbePkGeiqmEmQxB-i65xO84OwV9hp7lhHJHuaRlGSRlPPEeuIHKOaKwljkpbHEh8SNZyBPvZgOZf5qMOg38CCqburBaDU6uwRCJ_bu14erVjpWR9F5TMpaai26V96vVy_poP8FmN91KG2yWzdMtFqMi6w64hjI5pKhaCY9CDbpLqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=qeUrSgjR-NtGdfE-oDFqRMd4G3o5z6IXdh7t23eFb0_WOvCyU3CNRdrKcA-N2oVq7_vPhvNsHt5DJ9o1Xon02Pn2Rag-S7-ymlYcpTug3J8Q95L7ChaAhdH0__Dgab3XTCXHp4InWj6IlMOgXytO_Z7rz_p8Q8v9UxzvQJpg_nSek5PX9hJP3CMtknfkshaZkjcLxJ904B-gMYPLvtkHMtghtgSgFaphQzc92kU4VCVadluG4OgQm4FI13rI3pQpCPOWLNdNP8lln-bsVIrwDtTIVKwkwYaQWkM-gV9Ta5M3HTJ6A0N2PrlobvWxB2HrQDcn8ryg3a58cfZ9uyUAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=qeUrSgjR-NtGdfE-oDFqRMd4G3o5z6IXdh7t23eFb0_WOvCyU3CNRdrKcA-N2oVq7_vPhvNsHt5DJ9o1Xon02Pn2Rag-S7-ymlYcpTug3J8Q95L7ChaAhdH0__Dgab3XTCXHp4InWj6IlMOgXytO_Z7rz_p8Q8v9UxzvQJpg_nSek5PX9hJP3CMtknfkshaZkjcLxJ904B-gMYPLvtkHMtghtgSgFaphQzc92kU4VCVadluG4OgQm4FI13rI3pQpCPOWLNdNP8lln-bsVIrwDtTIVKwkwYaQWkM-gV9Ta5M3HTJ6A0N2PrlobvWxB2HrQDcn8ryg3a58cfZ9uyUAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=AP9auI-N1_PQMOApN4AGDcvhAP8pkSmC1p_pzgVUOSs1QKIlxbWxx9Jq7ZRs_KL87FP9yqLvRRl1NbE70rVFI0p2GjDwon191inOYo5guAO6WHHa9iIRzBe_n6JPym3rXQMM9Pxt9pO6B2E5Ul1IYbhSJST7ZqUw95orJxbLDrC58EdnBQk60r_gFXHqseYD43zHWUCtG7c-cxqG9q1CPlPZin1DqqyIN8jvklw1LtPwg4q_1HgnqoSWC3gP5SE8dOGJrOUisZKfDYEbTlFfes8QSREoticD7YgsZdAq3VTWfCqdNIDDW_u1xhnfsymC5xCRz-7Y0EuBEyCt4oUVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=AP9auI-N1_PQMOApN4AGDcvhAP8pkSmC1p_pzgVUOSs1QKIlxbWxx9Jq7ZRs_KL87FP9yqLvRRl1NbE70rVFI0p2GjDwon191inOYo5guAO6WHHa9iIRzBe_n6JPym3rXQMM9Pxt9pO6B2E5Ul1IYbhSJST7ZqUw95orJxbLDrC58EdnBQk60r_gFXHqseYD43zHWUCtG7c-cxqG9q1CPlPZin1DqqyIN8jvklw1LtPwg4q_1HgnqoSWC3gP5SE8dOGJrOUisZKfDYEbTlFfes8QSREoticD7YgsZdAq3VTWfCqdNIDDW_u1xhnfsymC5xCRz-7Y0EuBEyCt4oUVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=jhsHuKZD1HwbX5HngttFUxGZGN5suHXigCgtnP2pmyB82MEgluzrqc1Qe3cwjZ1YUtLowrfm_q1NgrJ30KeNHIUh18lUFDBCiYiMI2uKqYCIfrJFuccBh8huP6COLokadV3Cbdx4M8LcO9XeYPDnjZ4T63oBPcaDQRO2R0cTmDQsPXZ4GoJ_Lq3DN09oP6mwJhuPp-P4Gd6tCJU7xfPSVg4DQCU1MObxM13qOHpNoDplxx_T2PYcE3fkb_but1wxHfsYbzmYdZdH2tS2msideJcjCYXgD4GRlJWWrW9w6mGmQjV6LRkTr5va8CDcQbnysqFD9vB9LlmNImA6afa0wA0ySwY31jtn2dCt8IjgPVFh0fnfrMxIUnOYm7Kq_IwjHng-X_9dCQPvDGnI_9lgVJBZ4S03vONceyEgLXhQvN7Z8BKe6uOEpZ4FRJsb52-8JYt3m4UTV-P94YpMEtToBTnUzJuceBz9RULny9F5218Df90DmlJB9MWR_wXwWbL1rJYh5CAvdBoxvc4y03X6BhCNvG7obxFQW8bpp9uXprB5Rn7I-nTB2OubksEtd_oqDghJsjtRmA2Qb6mdt_YkS5WvhfB7JN9QmdRDoqQqw63L03o8mjoI04OPd3Xn_3Pl4Kb2p_GNlQcDOnYF0TmPDYrN_7AHmFLvivCzYjZmIVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=jhsHuKZD1HwbX5HngttFUxGZGN5suHXigCgtnP2pmyB82MEgluzrqc1Qe3cwjZ1YUtLowrfm_q1NgrJ30KeNHIUh18lUFDBCiYiMI2uKqYCIfrJFuccBh8huP6COLokadV3Cbdx4M8LcO9XeYPDnjZ4T63oBPcaDQRO2R0cTmDQsPXZ4GoJ_Lq3DN09oP6mwJhuPp-P4Gd6tCJU7xfPSVg4DQCU1MObxM13qOHpNoDplxx_T2PYcE3fkb_but1wxHfsYbzmYdZdH2tS2msideJcjCYXgD4GRlJWWrW9w6mGmQjV6LRkTr5va8CDcQbnysqFD9vB9LlmNImA6afa0wA0ySwY31jtn2dCt8IjgPVFh0fnfrMxIUnOYm7Kq_IwjHng-X_9dCQPvDGnI_9lgVJBZ4S03vONceyEgLXhQvN7Z8BKe6uOEpZ4FRJsb52-8JYt3m4UTV-P94YpMEtToBTnUzJuceBz9RULny9F5218Df90DmlJB9MWR_wXwWbL1rJYh5CAvdBoxvc4y03X6BhCNvG7obxFQW8bpp9uXprB5Rn7I-nTB2OubksEtd_oqDghJsjtRmA2Qb6mdt_YkS5WvhfB7JN9QmdRDoqQqw63L03o8mjoI04OPd3Xn_3Pl4Kb2p_GNlQcDOnYF0TmPDYrN_7AHmFLvivCzYjZmIVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=hZk4hcNaRtepWNjj38KxEdTP8PFseCopd3oTQuc-_CcRLKqijES_mmXnOSDWFFw0tirZByQbpMsQnC60LgaqF_06_v5sRsCw0R6I8vVWQCcRDyxYNzbUj1Hvo_90L_cPDHGIs19oDBJyinpN0SgsRnFeM0aFS4n2ahh4EsEilcqcw724KqXHr_tlZUtYT7eqNqC21DOY8Xchje7JRCCH8of5UhvjFFO3A-m8aUoKig-5xY9ccwOu3wBoEoMajCC0OQvmsIFrZiBN-KOqpDkdIVZPi90eW3Ku96uQkeG5Dh54rsBYpcL2YUDfD3-ovZwE9yINoGQbcuh-LaLrlJzLug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=hZk4hcNaRtepWNjj38KxEdTP8PFseCopd3oTQuc-_CcRLKqijES_mmXnOSDWFFw0tirZByQbpMsQnC60LgaqF_06_v5sRsCw0R6I8vVWQCcRDyxYNzbUj1Hvo_90L_cPDHGIs19oDBJyinpN0SgsRnFeM0aFS4n2ahh4EsEilcqcw724KqXHr_tlZUtYT7eqNqC21DOY8Xchje7JRCCH8of5UhvjFFO3A-m8aUoKig-5xY9ccwOu3wBoEoMajCC0OQvmsIFrZiBN-KOqpDkdIVZPi90eW3Ku96uQkeG5Dh54rsBYpcL2YUDfD3-ovZwE9yINoGQbcuh-LaLrlJzLug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XHmx3exOSVqhhjLyGRURoeEB1KSP0JGn4BsjpSvr9QSQx8LMbpDtic7Lwxe2GrzpbckNw0TVaEO0_WAekRcd6UKMFsubCrYXzKqD89eqP05aDpOkudiBjV9URymTWfHk1g3fJ2qJ3bSL4REdcggaFuBCJm0z5iuBBVTiy-GXR4S4WcQCJt33zDOeIYG-S7zI4Mf6pRjlyTZlaOt9rRErF4GjumdHXSi3CNvD98JumsRrK9XWPBOf8Ewmkiu_KnmKqxtnEf6yqMKCXaveL6nP8yEwiywoy168FDqNpwqUDVcVvBMzU-I-A_6EElS3ki1br_7Jt7fZbim_FjNiHYIHRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XHmx3exOSVqhhjLyGRURoeEB1KSP0JGn4BsjpSvr9QSQx8LMbpDtic7Lwxe2GrzpbckNw0TVaEO0_WAekRcd6UKMFsubCrYXzKqD89eqP05aDpOkudiBjV9URymTWfHk1g3fJ2qJ3bSL4REdcggaFuBCJm0z5iuBBVTiy-GXR4S4WcQCJt33zDOeIYG-S7zI4Mf6pRjlyTZlaOt9rRErF4GjumdHXSi3CNvD98JumsRrK9XWPBOf8Ewmkiu_KnmKqxtnEf6yqMKCXaveL6nP8yEwiywoy168FDqNpwqUDVcVvBMzU-I-A_6EElS3ki1br_7Jt7fZbim_FjNiHYIHRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWxUxGJhqxjGqR1Kl4qreTlSF5qF2O_YOSyBTXAqvr-TsUEez0fMGzY97AvWQWKLcrM5uB0OQLu1bXr4I_qdBab39p06IRT7Of1YPhCzeyi09-MmpFcNMpx1D9rAUdeBjtsw8qbYJD2Fx5c-xU7MNhLJL5sPBjD1MJkJ0TDHbjcZ6RmRS1FTDnjXvDhzdhdHy6GGmNAuYisw6ZMODe-J5xQGQWqjWu976vU03Ua-HFO1qSz0Zn2qWEkcTExE2phpDUmVWzQceI_Rc0lylRu4Rk2tUcVGcnppkxJp13mb6mPuiOh1gryVoZezktBOV9JVPCoUeD_9hgRCnJeNyiovqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0VLUDLjqC92AXw9xpreTBnQMLvLGSMu5NadtuVrWoHq9FgEE7pyeJv9ZTwGr8sjFK-dAdgq8vl5N1xOIa1vZaX0Ejq-eTvPEcah323ZOZHG3MKtzRNxmg4nZEJIng-tdeHv9-SwBZ4j6gnTDYf7JI7BjCdDm5gwLbYTeatv8wjeMukvk8SCCJowY2jtqk9o9FqDP3EeSgbT6Z6z-6g3nLuws3jcwUwM2kAZ0OaNSlbFaESQ5eyRIZsRSz6ys4CFFbj3dWtoVkneEvEfGq6GIobMa9dfLr6uE0n7NL3ykl6WBu84nxlhIgrOoj2iaecqsZL021KNGBTsIp6AUkpe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=F9NEpaaS9Hd6VGIRz1OfXQbpfN6GLKkOtjDrVmS41LWIYDHQenmR9oyBZP8_z1SQylxdPtxJjrP0L3qpqK3z_yBg99OEaz0wuwz5XzjiINfauS7gjbo_9TdyhkI35xDNAKz9ZGPiyycviJlWHCCRqUzloaJZg_Lpaf59eJHhVapW1JAwOCls2NJLEKSp0CLrYkqdmFpAZp3gxvbk0uPesyOH8OjVJSIC_H0KZyxqKRUng0_SMKbuouMlKNSgRseMygkovAwFxqp5P2hOjQKY8RKfgPOfv8XyAWV_6XzKBMbMLAyGmGAcRY-awdi7HL3zhjoNMUo-Xi1WOCCWNMHvZJJu0YwsKHU_ysbojmgKDa_QTgj8AdqrAkFkB1TIyAH_0H0_7nNz8D2gnzz-fuOllcugPQ-TJRCNpEGJtdQ9FYN9td7WkJh-bWe_GU8r3sJpJTvPHrJ7bWtR1cqysy_VSdC1c3A7pg3pL-kuOQwuxke5T3tK9zHk8SxcR1P7SyFCV7twq1c_Hx5JikVgGFi0LrnI59iiGi0hZRuFGwYvLJcrfwajMS9za1HsbetfuUPkPPaytXq_7se2dQPmkTSbcMMWSsTMjobzUW8uQW18WQXYlChnVxBWruRUBdjs8jSOwQTdALVZMlkji1qCB1UxMYhoEusf-W0mEPg2WDnHQuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=F9NEpaaS9Hd6VGIRz1OfXQbpfN6GLKkOtjDrVmS41LWIYDHQenmR9oyBZP8_z1SQylxdPtxJjrP0L3qpqK3z_yBg99OEaz0wuwz5XzjiINfauS7gjbo_9TdyhkI35xDNAKz9ZGPiyycviJlWHCCRqUzloaJZg_Lpaf59eJHhVapW1JAwOCls2NJLEKSp0CLrYkqdmFpAZp3gxvbk0uPesyOH8OjVJSIC_H0KZyxqKRUng0_SMKbuouMlKNSgRseMygkovAwFxqp5P2hOjQKY8RKfgPOfv8XyAWV_6XzKBMbMLAyGmGAcRY-awdi7HL3zhjoNMUo-Xi1WOCCWNMHvZJJu0YwsKHU_ysbojmgKDa_QTgj8AdqrAkFkB1TIyAH_0H0_7nNz8D2gnzz-fuOllcugPQ-TJRCNpEGJtdQ9FYN9td7WkJh-bWe_GU8r3sJpJTvPHrJ7bWtR1cqysy_VSdC1c3A7pg3pL-kuOQwuxke5T3tK9zHk8SxcR1P7SyFCV7twq1c_Hx5JikVgGFi0LrnI59iiGi0hZRuFGwYvLJcrfwajMS9za1HsbetfuUPkPPaytXq_7se2dQPmkTSbcMMWSsTMjobzUW8uQW18WQXYlChnVxBWruRUBdjs8jSOwQTdALVZMlkji1qCB1UxMYhoEusf-W0mEPg2WDnHQuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXg67X57sBkSVOX_vJAKLov81lzRtGGR3RH27gNSGV3dXqDY-ljsvU_kHAF9ite6OdhrIgNmxO3MKUA6NgONSwBfPMEqpHr7UhtXqPg363PkH-ZoUUS9hJgF7uzZXfleVICMRthhCHWTqXHiq5niRcFh0Wxj6I82NVccF2np3MTfTXk8RmO5WU4nnl1f-Gk-lAuopo6zigtxMESmdQD_00VsSAETGQTyRwM0upgbFicmH70oX9J3lVcTUIVDE1BJ1WgszkNupA6NdvuKT-oTljzPF1DLX5kS9_LuilZ3N-oVIdMSp0u0VgMO5LwXPvi7-yfI80irWwcAMgy47iYbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqXsq2FHJ9Gbb9Fwky1E7CXJr1731ZPO9_hg5G72vD4wbgSej4OcwytSbMZvFpYQ4gWcj9RfzLdZvwgl0gZzRYegi8mNZ3E1P0CPWAywP-yeRmbQsgwivQA99qoKfQc51i4tAaC9-B2hz4d5QN7OfzknVZfbdwZo6TAkUmMaHNV3A75OWbDQL2z86Xg33mWHVSuc_UUqEmLxxLqRC_2BEsLWKEeMtfb-w4iyGXQDYTxk3m5Ttb76YZeO5IfatSHkwbyc8diuSf1gcRHnSDqa75AC4u3tP4O5T2XcJ22ukgq-meS3BIhDydQmTBx8EeAlODdQQyK_xWTsFXzqOO0CFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CspMSWI_YyKdSwg_eCk-zK5AehTx-YdTLJiC6N9DgHSHdxz489R1holmDm4_q9wEC39Uuvgcq76A4bxkLkr_i4kdyISrjJ_is9eilhCsmPLoOi_1ela056uDpaTTqM391i-3kpPlZTFOHT6YNY62Knm0TZ_ZLhFVsH7_S0F_zBdprl3EWn3JGuhTouQhaC9apBIfmzlpM79fPpATW1f3k8QINNFK0ZBPXhU6aiM52jln40J9--dOYIWhEHUAErRbh_427JCPx8v0Qzf4l8Jx28Ti9_Z1A8OaE6XbzactGkgTjVwK-opcshTpF2qODQ41J1Wdtwodm_uARZD8fIdBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiUc_jiCd2ddBVRcnmH02bhyC0q2gQKwrjqbf-5B9sem5yQMN1wuwhU0TFHMXQAWO24wlXoj_qbYO-9sI9yyxFlfJHNA_rcpOTzFFEoHcZec5Z6tuCRjXos3TGqceMTXos9ljkBMF51M1hdjws7UFduPVO5FM5YKwzFQ2L97xuJLNBPOHCAdW2xWOdK841ga9q7CC_EiMslLbxFGrGAe5g42ft6r7gbQo4qTHVmEde2JWWWJhtLMVg-66oMvM7Uy8y5CUiLUShFPgIDjIFMjWX3Wpb4sgLJ_2H84UVjwV1kLALzqdUr-XdFAi1KOD7bFPjQqLIoSDLr3giwmYcfiEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=C1fknpQ7VLMojIAONSpbnNYlfSdCrm5m0JbOkPFIH2sLjV9yYBSnHqFzTXH0xm9bzhKXAHD8LvMMcophnLAMmKyfj6PdG01kNOlVOmXn5_8PNxpZ32XZeJ20NUtVHgVp-MX_xlxtGl_sKm39Ibtzx8N9ojNTVgCuQHJZmfCpwHfDjlgCGeakrGWnBREsHT-dHqPeu473z1lG6dwUFEnTE7nXqjtIbxFKJew9brPLuVNIyUwjAc7sclVPxcxoS6XZ0vFR3-IgJk4e18-0y5AQsNcYTJBA0RbyOpTGDBNqQ55S-qKEJZp--gY7Vg4T3QUQnVz4XavVgqqHKFd-WF4SjQrr0wcdtuk4mM5hbFgGs9dqF1ae6X32eMlCpFpS-UZA_jk-Tqn_Y3A50RqElrYwAbfPwl3CuNF_6VoVHFAF_TeRanwkxD75bXfb8mtq5wi4x6QOnRJAoauW1ksodoWdzkkhJAdmv1NhFUnsvRReAFum-Lw8CG0eeB4uju8icuegUVWYU8VzjTnsGpucBQ9bOZpxLhv5jNiNXmtIWEWzkauX9UjfnMEl0d847ItAnOftnR0Z3l6q6N7ig7vEc9kwjWvFHyzrIHZcFpwcwCOTXZp614JyReNaEuVs8bcOP87f9d3C-nQ8Mi_gB4WXVclJSgVshcDrsaLsKo8GHMYoltk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=C1fknpQ7VLMojIAONSpbnNYlfSdCrm5m0JbOkPFIH2sLjV9yYBSnHqFzTXH0xm9bzhKXAHD8LvMMcophnLAMmKyfj6PdG01kNOlVOmXn5_8PNxpZ32XZeJ20NUtVHgVp-MX_xlxtGl_sKm39Ibtzx8N9ojNTVgCuQHJZmfCpwHfDjlgCGeakrGWnBREsHT-dHqPeu473z1lG6dwUFEnTE7nXqjtIbxFKJew9brPLuVNIyUwjAc7sclVPxcxoS6XZ0vFR3-IgJk4e18-0y5AQsNcYTJBA0RbyOpTGDBNqQ55S-qKEJZp--gY7Vg4T3QUQnVz4XavVgqqHKFd-WF4SjQrr0wcdtuk4mM5hbFgGs9dqF1ae6X32eMlCpFpS-UZA_jk-Tqn_Y3A50RqElrYwAbfPwl3CuNF_6VoVHFAF_TeRanwkxD75bXfb8mtq5wi4x6QOnRJAoauW1ksodoWdzkkhJAdmv1NhFUnsvRReAFum-Lw8CG0eeB4uju8icuegUVWYU8VzjTnsGpucBQ9bOZpxLhv5jNiNXmtIWEWzkauX9UjfnMEl0d847ItAnOftnR0Z3l6q6N7ig7vEc9kwjWvFHyzrIHZcFpwcwCOTXZp614JyReNaEuVs8bcOP87f9d3C-nQ8Mi_gB4WXVclJSgVshcDrsaLsKo8GHMYoltk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=EudxpYPquVfxb-ysR8Z8zQrb4hGnENcrLEX6XXgniO2x5Men1YfkQP8l8d09nU0Rkpm7EZSyKcdMSbXuBPufKYWhZ1ZPY3OmM4oauIgA0ad4gpSZvpalKovVNUMtLyVqx5UTuRPsQay6pXJQD8ej3eQNw1azF8rHREbpOsDuX7C88A5Rati68US533l630eBRNxRU5BfBYTmNyY2s4Q9YYoHT3jlSL9CALJ3rSgQmCes4L-22IRleqGXyLlpsdCpMibJae7pCo0hcrkykUTk816NAijhQKj-x3Uu35w1jFhBUqcNSiI49NK3DKntT6gqFM8SQP5sRKFuf1Lv2_ndDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=EudxpYPquVfxb-ysR8Z8zQrb4hGnENcrLEX6XXgniO2x5Men1YfkQP8l8d09nU0Rkpm7EZSyKcdMSbXuBPufKYWhZ1ZPY3OmM4oauIgA0ad4gpSZvpalKovVNUMtLyVqx5UTuRPsQay6pXJQD8ej3eQNw1azF8rHREbpOsDuX7C88A5Rati68US533l630eBRNxRU5BfBYTmNyY2s4Q9YYoHT3jlSL9CALJ3rSgQmCes4L-22IRleqGXyLlpsdCpMibJae7pCo0hcrkykUTk816NAijhQKj-x3Uu35w1jFhBUqcNSiI49NK3DKntT6gqFM8SQP5sRKFuf1Lv2_ndDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IImYp21hOj1dYoWgDuJmPP_hn0-gig1BHxuFWVS0vjQH8nQjHh9UqwveUzlOIuw33J-PlpxvuLj_2gP2OElHNXcNWQb0Ti_NvMGpQcEelTJNGw6h36Z4s31sE1odJKyblca6ClLd_cgM3LB_tM1TENreUDXmSYOkBWUhGsk98F6GOYLuoOzCqW9ebrqKkNE3wQq8QijDZPEQvT_jlMg06QbjucPnvrPc25pfkdtjjhfnQJK9eiMfPfOYH2SbmbaEYHGJeFaPzgPcHZn0JLryYvPfaRV9B7t_GIl7lfkA5t3kDjnF5xzh0p3cxMOrSnu_ZcG9IOL21j6GmOrGcsFW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqVmiHC4ZcdjKyuU1Y52lOg4yXOT7GXwcIBCBVuKqlfxaMwXpL5OIP5bY5P3WU99alXIWEBByMHpmL_DGJXQzoyjo3CLucLkggUoa5Tz8HZLaS20PY3WEv6TweI_HhmsTzEusU3jzyxSgD4HimUUw2smycDt5AaoBxM_bai0Gc91cHlZg9H_H7DjN_qoOqr8F_PmYIgmMJze1XNOc26Jobs-fsTH4aN5mNXcceUjv0Oa4VdAoWzlmR5KMvlRnJ1pfq9dOatOVFViAtt1BbO8lAKIcL7v8i6PZ4Mkw8M0mGXsBj-a-5neJaP9p4gk39IAzHFJKNrKIbW7SPVox3fLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJCHrBmGeuvbjZnasWFKLAhlEI2gutAwwOJzcMfuoFOqJDFVcTFcgsWZVjbQWvF_tmV_bPZPSgverAXZ6gCHQyPNE3gcDDeBrNM1j77LZa0bNdQJGiI3FHZiErvvpgE_t2yPh1a_tpsg4NxHCwztO6MTCalXj9AH-ookWU69CTbYv7If6ZXPbt2YEs42y4IkF8uV5aaP0aI4FXTCF6FHWUet6DD1Z2xNaogx4L4fjtoxZVjV1uaRz9HH6DDLuZcWk1qytJdwaGh6JTGSZ39jbX4-0RW8GWqFVeexcnNx4J3DZS4PL8QO6QxuyKT0pLPj-r9OsJ0LIVcBRN-JahM96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwUI_c7uxe5l-cZhABONb3lmIWsbdj9mnFI67jWSSbURMpYRGEYYChDt3enYnsCBEFuZgfCX0yhzxc-qzJwqpW8wlrIu6V2typmmEOMcjjarCauwE_aUXLUwbWqivSz3_4-vQmybFnn3mUI4bCPuSK0SdMzv6Akkw2tF9Q5SLY4cE9260KrkA75tQIqXpM4D9EPew-uxhjks2eq8fAgADN9JTe8R419LSBuDr4H3emAWkqZlap9uskPiM9G419J5_9Nw9ptI1y2NfRTxwGztM6gzfqp5dx92juAQlcg3_DM7fbNEZ8Xf3NynKuVBt3fD0CLIN7OrhcrjGoTzTLrLJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkFHc2qQjWR9BNfQKUQx4-WNt3_L3XqD53RXV0yXOf3p527N3F6QunHsvCkuK4avIZp9oe51E7FaEtcxPrKJA5p_BdYkS71tR49MfZTfpjRQX2JCX91XkKXDK3v51rmlxnXvH_7FBvn0pzq8fS9-oy50HyimhYrLV6vpuTboKADKadhbu1CiZ8iNs5XoxiZQALZqRLCH9HXkFSYOSQtJnaezweXVExvbKF_v-36HCIHbdTQOdJsNlUwrbv-EwUPjuk53ZtHIcNgEVfb3xZJLvr9wAXJxM1X7OHHtNmssH32wz0jHeLjKT2Z-cUDPeNWHy_pxgseu9QIfKMnrxxctTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddgCxnK-WNOhBcGz8yynJX9MA8Nj2DF_B6SKU2E6_H6A8PT1KFO9oNrfn17TvE3uDyjSz1pD3fLHuwFbRkUCNqxAYYqOK47RySuKUSdlLfytkllXClYPoFhx5GZo45k4ybDCJj25XK6rIMrw0LPye6klD05_GM1uRDT3TiHroKKkhtCdRGLxSenEFrT46bnL2eQ_17mel-46-X2TPJwZrLT9PiwqMKDReItelPHifr5wBUZu0HASHZJ3rCfv8PQwR6Vn_bP6zXqlYUjXPBO3BIUij_NGNT7mNrblpea6F8KJfrzKwrT7My2HlvGAzaEcLm9GZ-PxdRq7tnKZooQOaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXGoh8272tHXI2H7r7dCcXFxtjMFq_brNy3eiG3tBjsvqVJqEVG816IU5aBKOVq1wf4sz0emYRycEeXxX0WZM6ysQDKKpXG0-oXDB9Oqvd9m4BUq_cd5cr2xlKRXpAJ2qzoc2atqH1CtjGW0PzAxyZ1rOpnoyIxaTSdWR7dcCjJcb-DF44hA7nQNPZ1kqJ9Rwg71W5jS_Twwl0ApdZnfEOY7L8Df5Z2w0kSqm6mRMzOuPX2bPx4gjMC0lAiekyGG3S20P_HDSHrVbFUTJ9vmDfJMFKES40RfltioVnNomj4cpR_tF_0P9dgZxOksGScsABfQ98inVWTzr-aAtCH9Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=RZvmbCdyxexFhHHFxHQHfZWRWJBELE_cA00F7IkRWxvAuITvDdznkO1rKWa5wx_krQZuyNIZWUsMgIuXA0efmn3ZNWVkFx7ZSjSkcp_htam-V6v4xTp5kR6olp7nnosR5-aMGarGhG-LWOZJAqRPbvssbWAI4B28qu01psrUhB-RPst4N59AIRIMzT3c3IMSxwJ5Vg1ysI_9UCcj8l4nP47USDwrQA1kyrQkn1MNcZdAjz_ZhHedA_8gW3XN3z3Kv6DOk1jxdyGnUbB9Yz_Zbb0r7TDRJyuzYJu0B5PLfnghUXIOqKCoT7Fnn7LCb-L3cuHzOTjiidxolhoXXDcifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=RZvmbCdyxexFhHHFxHQHfZWRWJBELE_cA00F7IkRWxvAuITvDdznkO1rKWa5wx_krQZuyNIZWUsMgIuXA0efmn3ZNWVkFx7ZSjSkcp_htam-V6v4xTp5kR6olp7nnosR5-aMGarGhG-LWOZJAqRPbvssbWAI4B28qu01psrUhB-RPst4N59AIRIMzT3c3IMSxwJ5Vg1ysI_9UCcj8l4nP47USDwrQA1kyrQkn1MNcZdAjz_ZhHedA_8gW3XN3z3Kv6DOk1jxdyGnUbB9Yz_Zbb0r7TDRJyuzYJu0B5PLfnghUXIOqKCoT7Fnn7LCb-L3cuHzOTjiidxolhoXXDcifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmOolyxl_0ZNCBiEjiUSSNa-nZ9_qkHgXnwcWq_9uG7L4FVC9ykc_1V2OVLZex1ZQ93HwjHUFbG9awxa2PoHRsLmqkGcrWfKXSbgu2vMEuloYfCUccfTzDTqXJZh9GvuvPxHQlAAvwrc1YoujgPEbg4K2YoTy8JBobveWUyjFZPAO_3n4W_foxpZ1F7sXkSfxp9qeAFxjPfZZOU9FnW0erYWJvbrg1CBUJ41-aaB_kwdDbP1rFnTadfvd1N0nwVfY0FsW_DNSnatLSn4WnqhUOvu-gU7QgXAfs9CRT1mOwfBl7HxqraNQBekDM8qQpr3jslRMcW1CLkiNJTVVCotkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=BQ7hC-B8TS7f8ZXXTSUspNCIyDHtjU6bAisio8LI0FOHFRmhisv1StFrVvvWC-yz9_7-fRQWlVtfsxx8dhCaJ8eOma1SVYRAlNqvP16nF-2Ka1IWHrkAfYBCu8y39FwTsKK0VhZJXrQ3dW0TCKpqKfotJTdkBqLkU9QCSjKAssY6T_WvT-ENOhbV4NA5SJuPeSCmId3O1M5ytf5Bbztu8RT9xOhHJGasZ3bFXfoytRr0RiDMeeoPjHjRdVUtYXuA4LvSZmXRVswe95mSAiFGnueNV-OLOxt_qUz4xwcSOjgCUndqKIs8X2SqKS8-WKL7BZkVhuhMn5cz-eAwOX5Nvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=BQ7hC-B8TS7f8ZXXTSUspNCIyDHtjU6bAisio8LI0FOHFRmhisv1StFrVvvWC-yz9_7-fRQWlVtfsxx8dhCaJ8eOma1SVYRAlNqvP16nF-2Ka1IWHrkAfYBCu8y39FwTsKK0VhZJXrQ3dW0TCKpqKfotJTdkBqLkU9QCSjKAssY6T_WvT-ENOhbV4NA5SJuPeSCmId3O1M5ytf5Bbztu8RT9xOhHJGasZ3bFXfoytRr0RiDMeeoPjHjRdVUtYXuA4LvSZmXRVswe95mSAiFGnueNV-OLOxt_qUz4xwcSOjgCUndqKIs8X2SqKS8-WKL7BZkVhuhMn5cz-eAwOX5Nvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLrJkAZDTfAOtMbailppmccJbw-86AjKDKUIN1_KTjXk7fI9jRLv9iHRl66lUYLnlZbUfFqkDq-j7QsWIsXLSaqWddACU6WSGlULw2u6SNnD22eNqCgbLD1vk9GbHa2xF3honxMc5nNQVGp2HslexEY9uvRJI_VWdQZADojxK9Tc1X7Dpmc0J5cZ1-A7o7y581NAqvbaRz4yKrRTifuypUIGBGB4Q_KC6_kO_AO8HK5ZGfy2-sQ0STi_TIrPms7jqyHd0q7OrBRZX6JUXIcF1mtmqfzlRLHZKQjI3g-7gPf4Psg4yUQQGLsEtNVftI4K0E5-yDTGihHHKvGi-CAwiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFSbH5hfxLaD2mM_5rlMJ4_3-IoiLK5agkd6dtyIcczMPwI4ZsVtmW7T7np6t1gM43G_hSUeIM7NO9nUebJwauPFKOSi_pJIuhHIS1y92yQG5cDrYhM1T_G892ZSWRI5bCvsoiQWA1NcdtAvzCGEUwds4-YOJSihb94TL0u1O-6AGXej7TuoeO-4WrTpS7LpKy8rjCZeF2dXxSwjnt2G7Zmbata6OLSvrwi2Qn4SIEFLvKJnWVCTPVyi1Fj_Qqe8c6mvxqe5eJ0woURvcEG40ZwfLr3mPlUOUTv4Ay3Z5AuwIau7nsGzjp1wamef6YVbZs32Smg0-BIwjOwlzEaVQSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFSbH5hfxLaD2mM_5rlMJ4_3-IoiLK5agkd6dtyIcczMPwI4ZsVtmW7T7np6t1gM43G_hSUeIM7NO9nUebJwauPFKOSi_pJIuhHIS1y92yQG5cDrYhM1T_G892ZSWRI5bCvsoiQWA1NcdtAvzCGEUwds4-YOJSihb94TL0u1O-6AGXej7TuoeO-4WrTpS7LpKy8rjCZeF2dXxSwjnt2G7Zmbata6OLSvrwi2Qn4SIEFLvKJnWVCTPVyi1Fj_Qqe8c6mvxqe5eJ0woURvcEG40ZwfLr3mPlUOUTv4Ay3Z5AuwIau7nsGzjp1wamef6YVbZs32Smg0-BIwjOwlzEaVQSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=r7WlUEah_bzv_EvB6-1eyhhS0blL_SSCBEEAPtws5w1NipPxoFCuJOi-HktCMJPLsuIVbVlsh498xB_H4391_rES1qkQNgY8tykrh60vEF2rOn8WIRiKtHgzwiONprBscIFqXCIjJZxLIwmx8i23bGsbo9un73T1-mHgilzf7RF_2HOw-JcmgBOinrNFsbsqMe9Q14MJEqDwVCI6BQODAFXJv3Sa2pUNQCgdZAnjhQQE42FXCn_uyLR5Szzp4ScjLvQ6L-XULoT4C2v4aErN0KTZdOj2EF7YNo14zGbeNPEPnEoyUzDv2MzXMFhL28UPNBNXKReNSAC62rCNDtJkuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=r7WlUEah_bzv_EvB6-1eyhhS0blL_SSCBEEAPtws5w1NipPxoFCuJOi-HktCMJPLsuIVbVlsh498xB_H4391_rES1qkQNgY8tykrh60vEF2rOn8WIRiKtHgzwiONprBscIFqXCIjJZxLIwmx8i23bGsbo9un73T1-mHgilzf7RF_2HOw-JcmgBOinrNFsbsqMe9Q14MJEqDwVCI6BQODAFXJv3Sa2pUNQCgdZAnjhQQE42FXCn_uyLR5Szzp4ScjLvQ6L-XULoT4C2v4aErN0KTZdOj2EF7YNo14zGbeNPEPnEoyUzDv2MzXMFhL28UPNBNXKReNSAC62rCNDtJkuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
