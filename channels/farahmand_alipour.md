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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 21:22:00</div>
<hr>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhqLZIw4aPszHN4hhN5JnJGr14vrVfmyBQakgtL-HqBEUUxIxXiIPSQHmCDcnOQdVm5PLK-EMCvtCu2Wye6o4zdO9Dw8do_O6VI7JAP_CUFHXCTyK8haa67rS39TaUGnRTWL9PCdnwjrn7IiQ31u4qJUbbT0PQTFRchyiRl8B3qh8H0yPqjQFpHzXrBg3cDsbLe2e2b7yT-hyg045AuUE2U5f5RkU1yYE-HDXnk-U3u0-hB8tv4cC_ahSfTXCQeuoDYzznQbZ4YPJxHpZyeJl7kaMiAzlRtclSgzBFqQMApvB7N2wbEcvFwxu3Ja0KH2IAi5En_H0x0kQQLPYRo_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG11nrAvuJO_Z1am8f_O0_AzYyqsDCVcRUbIBJkVDCYHPq5QLSQ8p6AFACt2FScVINi2YD8K-uDyb92XwxMvASlVOI4bQsEGXBcA6h-Vxwg59g151wZIlJSmHMeXRyRx2M0RdbcqUtyNtZHoZBclNG-wVuBNvcJOoH6JJ2C4juLqgY0W9iHpMwV7OmI1lMFOB24TnPgK_6XhwrTadFwxxbA1cpoXVFf0L9sjU_Ax0InI-yv6n12t_9-uMlNVevaSbLcIo7fjBskYK4Oo_wc7OI4Wyo3rqBqdhH7cJywUVQi-1-bq0khYgjxd4s_x-8RoZ2hVTIwi1cCM29fuQmLETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8UBGrxgMo8WMJCmV7ts2U_Q3ehFPvPuWBLS-053AGy4nhCZ0SyVSvh-2JrqP9w5CevOE8wU7d9rNnQ6XSIdCZiCUX0dSrQ5vaIpWrZgQwZsAgQtEdSfPyDagBfgwhjneJGVG9wBY_o2N0Fg-i8sX40OKcUnETRmBRA6A8driLnORXziGJ_GozUlQveQ1khKCXQA70lnH_mC9b4BggD3hvSWbruWcrTcsJM1bzHpX5u7LpyrkKLDQIbnK5GR2yTHfvkzdp3pji9UD7_WqO_A_4Xoobhsfwehw-qfj76K3S6QalJYVKt9l_PzDJfC-aqv-EW12vfMQmtQT8_J2H6wmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlmYsls7ZZCb_5H3ckSZpQkbSTR11eYwjWji-4jlzQFc53QB-w7nqnxbqbkiPbW-89aDVqWBRTEc2Oooo2IaFbnu11pA0vsyu49cU69m32oKV6fLN1fb6SI5bKyvD7Jmy_Z1mgzkaNRy-mLxC779mA6Kr31Pb4IyGLk80EirViFwYTy4PmC41uvqbdwrQqQtvpAkhi81CCL8BZlZLe2oahrpXDD-ggGIpXSYrfllpKH91il03t6CjA3lSQRC9BCmzj_CJmjrD1uMTJV6TsK1P85b_fWffScgnf8X9lBS1Vm1c4hqQyMBCf1u3tE8m3Z1ggWz7YtWQA2rAZJtKy9WTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRWOg3_4Gb8V1S6ztiQXvnqD-peeRUXY8ubiPuUl_A-eZmHIklsEdAtahPvTsv3DF0sVbh7pUqdYPaflWyjU9whVdhvKczFWRXzTxiCGLDWyKO41YEQL6BIxS4l6Vd0FGJ2gWdg5oS6UvoTu3ZaQ5IA6MOl9F64iCtFSke74OIWarwBO1Bwoiv-Vk4Afm3v_RORJzPQDSin7Ty7MT31Vu25KnQTfRUiaN3mv9aBCe8tsR2UfkUYNmu9l8DDFNjE0GYtz4EgXEt3MEQn4eWmPF9HwIs1I4zWpVdX83dPnWtYeruxiCQgyu9IxhmAzU623p-06b9wcsgdC0dbyZRqP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz7GSSXWIaODZZcKbrxqrNgkuQQpNBjaj0ZgWDOwxnyR9Wn2_m4FxNxZeLHtosL7aF5sSKZMw4PXtPcq4MEHoFCfPnjvXeGYxSHjTdKlWuOoi7DvSl3FOgZmhDr0uFhRxeWtCfAcylZKm0kK3RRxT5DnrR1Xvp6-3I1G83he9Jomrb0FjBV4bYPR_50aZ-w8ayIWd6zJp4WBB5BJ_tR1wt2l9WRQQMGC99WAbrfDIVcukDhbCDXXiNmKCOzQysuZmshWvfN0oUvUDat8zsfV0btoFN_sX3BOGFUFYELoUhKmgX7om_H9ehHome-I-P-j_mTQAlLRKiZljxTVVx_N4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=FpYyq8FgMbPJqaBB1bxWPFKPOgHs5dZXiArLCzDfCRkHu7NY6T1lNNdBzg8bFZBoUmX0scvWQpIl0_xbIV4FCt_NAuuwUYY52j8TAIQFFRJu6msZqlD_N64pFFO1I_1KKTiUrub7xLPCF1OrDzFkRnx3D0gpo9v-J4VbIINvAUbF1FAl7ISWr39Q968lMl_jJnHPeQeIPaKkX3wMFk_Ji3sZqaQr-0PyGq7G0Konk-p8hEIkixTv_hZjGY0KDeXftz7nFgHAFI0_E15EMGdPwLoZgMQgCbj3fKAimDuqY9uswPCHJFrTB6wtp2HCr7Ji08uqCS4ivS_w5zgCAPdogg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=FpYyq8FgMbPJqaBB1bxWPFKPOgHs5dZXiArLCzDfCRkHu7NY6T1lNNdBzg8bFZBoUmX0scvWQpIl0_xbIV4FCt_NAuuwUYY52j8TAIQFFRJu6msZqlD_N64pFFO1I_1KKTiUrub7xLPCF1OrDzFkRnx3D0gpo9v-J4VbIINvAUbF1FAl7ISWr39Q968lMl_jJnHPeQeIPaKkX3wMFk_Ji3sZqaQr-0PyGq7G0Konk-p8hEIkixTv_hZjGY0KDeXftz7nFgHAFI0_E15EMGdPwLoZgMQgCbj3fKAimDuqY9uswPCHJFrTB6wtp2HCr7Ji08uqCS4ivS_w5zgCAPdogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0MJXDwYIvn-18a0X0tSLDAe_vrzQ6ve4Wymud57XKLtnKSBuU5RSVPlHF20K6gmRJHxKbsQLN5q74IoXfxqXYiZZZrh_cFOwf8Ohqi791PZYo-Ad5X3jzWu2IbUfMOTptS6NF2rdc7w0tSaWn1xZBNu0b9QdBJB3-roCtUPJK8o-bjF8RHk_WAZ8-pxjwyEh0NeGMjtmzlzCot0ecSF247wqrIuyC_cbrG-KsVGf4D_dmOqUzBCK6tI-hLhczexSJEAk63QZgy1U71LfUthhGN7zWiPYrDJLkYmdTL08E8-Vdt-xXRsUfiQUYY9mxCF1l8invhjGgtxhJ31Rh1qYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1T3U7cuWH32LcuoIGzlijmGWefqo7_ZZUxef38KdRZz5VLlQJGECs69qj2INR-giOy2quJtAs9-B7_7aZvf5GIHWcVQ3HtvmM1iLaDb0mylNYoTPIuEMiHvmQb4_IzDrKqQZJ28hdfnvgeKVb9bwUznEahoB7o80o8c3bske8oi7kWmXHt0Z3yLSQO-SobUSA9v3yyOYAyQQYXDnAphVinYlQwFDvaSJgeuTVkmw7loPe4YXaQ9DWxvuXEqPQ5HeFDo-v7Jngyop1yWmmYgECp4HYfxN8XETFuUvY5RqCYOdfnw-68pT41M1V9kP9oyJQpynLx2IwK6IPlLbJW4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=f7vRU6gnfLLPL6FZSPzOjZNoKVmPQ9mXFFKnndIQwc3IBLhkLVXVybu1wU0FK8_vJdmqHjUQmVtPdidId0QJLeIZYcPo-p6Sce6dz3VrSIFKT7qCuvQjvg89AcxcUHMeNvQiNMgoDtBMRYFsvqBDb3CBPMNN71tGpK7Xt0TM2G5BXPoZH4vWcULA50UMDDI_xZQHa_kmgsa4B1T8tgPzmZEB6n18KIUBVQGW1kk_paC4OTjjMcR6jnhfxJWK_IXeJZHS7VT3isuDPOqryr46EP84S9FvEWZYqV6961yelPVfd28bdU3GqjnwbG_tlNkV2wDeN7kbBBD5rV_0dMFUREtSOiYe_DlBiBh6nbaM_xsvDnCL0tjjZv2plaexnDH_gt4Z3jb2VVqeSEhvKALMHXb7xXKNX1E1X_g1PQgXihCA6BO8JVSM-38z16urrd4V6uXifYECqc2JU_EH1m-BiuuwwpvC6DZjx0PRQWD1VAKs7kSLWapdINyIaFncVdsioOpWLo-KgxdcQVMZXBtByoe-5dszkuD1JsHPaR8lA1TKOnyM7MzMVj6hgdi4ghg-rhxkZKbuOYx47e6BVrvPhanp0e8k_6lXCBDY3qygQtBlQXQIjUnKTx30dj2DtXrI8ArVvAWZnkROFwCutnkORjScCS70BD_an_pesyHh_iE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=f7vRU6gnfLLPL6FZSPzOjZNoKVmPQ9mXFFKnndIQwc3IBLhkLVXVybu1wU0FK8_vJdmqHjUQmVtPdidId0QJLeIZYcPo-p6Sce6dz3VrSIFKT7qCuvQjvg89AcxcUHMeNvQiNMgoDtBMRYFsvqBDb3CBPMNN71tGpK7Xt0TM2G5BXPoZH4vWcULA50UMDDI_xZQHa_kmgsa4B1T8tgPzmZEB6n18KIUBVQGW1kk_paC4OTjjMcR6jnhfxJWK_IXeJZHS7VT3isuDPOqryr46EP84S9FvEWZYqV6961yelPVfd28bdU3GqjnwbG_tlNkV2wDeN7kbBBD5rV_0dMFUREtSOiYe_DlBiBh6nbaM_xsvDnCL0tjjZv2plaexnDH_gt4Z3jb2VVqeSEhvKALMHXb7xXKNX1E1X_g1PQgXihCA6BO8JVSM-38z16urrd4V6uXifYECqc2JU_EH1m-BiuuwwpvC6DZjx0PRQWD1VAKs7kSLWapdINyIaFncVdsioOpWLo-KgxdcQVMZXBtByoe-5dszkuD1JsHPaR8lA1TKOnyM7MzMVj6hgdi4ghg-rhxkZKbuOYx47e6BVrvPhanp0e8k_6lXCBDY3qygQtBlQXQIjUnKTx30dj2DtXrI8ArVvAWZnkROFwCutnkORjScCS70BD_an_pesyHh_iE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=RTQyPhjK5-UHIO5XzEU3c8Q3nHcryLcHQbLzSYcCJDjzGkO7GfYV6fhs_1q1tKgJWyX8wlW-ZLZfiTT6ZNwLXalUK8DVWN25J71EljOE6hi6BfUeuwIR0P1FUI1xq5TkhQx_iQMk8LZrWKlfJ3Zsu_03PCLBlQEvVvrpyAZgRXe2IaUA8Abgp-fgaKscFVcisSLHCszAP8L-cXsfl4GaEZiCCkIaPwE5KrMsurNBCqK7mH1cV2WDBqxzUyUNLhUXFaniEsw_uoE36Zc7XunM1Ri9uP4RL7WQqd4BwaU0lSqw6V87npwFPiBv02GqVHxZKrHSw5I5iXMZeC37H8PIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=RTQyPhjK5-UHIO5XzEU3c8Q3nHcryLcHQbLzSYcCJDjzGkO7GfYV6fhs_1q1tKgJWyX8wlW-ZLZfiTT6ZNwLXalUK8DVWN25J71EljOE6hi6BfUeuwIR0P1FUI1xq5TkhQx_iQMk8LZrWKlfJ3Zsu_03PCLBlQEvVvrpyAZgRXe2IaUA8Abgp-fgaKscFVcisSLHCszAP8L-cXsfl4GaEZiCCkIaPwE5KrMsurNBCqK7mH1cV2WDBqxzUyUNLhUXFaniEsw_uoE36Zc7XunM1Ri9uP4RL7WQqd4BwaU0lSqw6V87npwFPiBv02GqVHxZKrHSw5I5iXMZeC37H8PIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnKE8iC7DbkxQCco_JcXqBO33MNHBP5RDS74_inIYg9MaA6MtYS7AIapCzHxR1NIr96tgX_H_Rhw6UKKVMv1rG8Hn67KOqvGfUFULiWWDe5VIYSlB8sbCEmDNUK4nTDCiwDaXX1wCWcV3KRgJNQzFLWhVqG-2aLyaWL0_bNWiYXPdiVh2qvVA_R4BHysZ7lNoehPCbKJmnvm1DPxZA3iotCsfM0SABgXWqqcO_deAbd2-Umi4KYXpN07ZQXNIoJ9zo5BA2Ef4Mgzd9Cg7kflDWowqnJCU6phzhVcaauhEx4F-PgJE4YrPf-tRP43LKCReRl0cM5Zjb-BgzIEj_ssfW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCnKE8iC7DbkxQCco_JcXqBO33MNHBP5RDS74_inIYg9MaA6MtYS7AIapCzHxR1NIr96tgX_H_Rhw6UKKVMv1rG8Hn67KOqvGfUFULiWWDe5VIYSlB8sbCEmDNUK4nTDCiwDaXX1wCWcV3KRgJNQzFLWhVqG-2aLyaWL0_bNWiYXPdiVh2qvVA_R4BHysZ7lNoehPCbKJmnvm1DPxZA3iotCsfM0SABgXWqqcO_deAbd2-Umi4KYXpN07ZQXNIoJ9zo5BA2Ef4Mgzd9Cg7kflDWowqnJCU6phzhVcaauhEx4F-PgJE4YrPf-tRP43LKCReRl0cM5Zjb-BgzIEj_ssfW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTzjrIYJefWSBTT0b7-wdj2rZWwQU8FjRmzl7B2o3KT8u-IJ9ukoLFUGCm90rbI81wZg2rS2K7uLys53nSDozHU743dg3uQ-AHKeeF_1O_l1Hc_gIhRqNyoZ6Ar49zxIJtcL_nPKVq8n9R7SJQCqTgFLj3to6UTXzuROy1xW09wBWIgozcgf3FQDa7AhmUolS_uObYmAmw_pz22rc7dN6Hye7nPpJA14JKaurVP35z-uWZgxt9MZ2cnqx_d4FLIsUZ7StLxzIIh6Xd-hzSM83CmW0XZWnEyD66xsR1EgXrtKDDh0i6kb_kkqHkQCdzT_1HBVHY059YYOVlh6ni--MA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsyP_1kI-GeqpGZ84M6Jp1qQ1eoaHLWicJQhECAlqMlSCgfequGSrQQTNZFbuVmU13uu2uAcFxGgkBcvlC-9BmxMkd-9BkhLuj-2yZwIYsRUKizxB6-DSuyylXVifxK6IArAIyXd3reSriGMMaSmm_D7FrT-gVFsHNNamZ10jLHgx8KVhai8n2HVVndOJ--kJ1WPE2AJw0Slj66-tX8xxB2zBmjdGyBbYDwHTJbOz-s3R07M3Y0gmJ_9UYA912T-yqV7QK-f9RMVe9MQ2oq8Vtf2iHSVjVw5suuwZUC2g_zatViFj88JElhDzDyRn38UqZv6hS9zWS46LGkJhxUl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4t85VOV5Bv8zOnBaLMhg9ZZUemzXWXENCjbYdyCCfNz2KeaYpu3idxAJCrMufoi-Z-V5mD1yAMk3KQQBifnsyMNSUbp6cC5unu_NLPwAjHoTLpR-f-dVqQKF6ot5clTlnaEua7vVXcbkTzL9Gx2r5Dn8CVGq-yWq5wM_YAP4-IF0z_FbjB3JPenv18xwZaU5mjyJEqc9OyIK3nbRyKTJpfTWOGlNYco1Qbdw5hBfhxINmPGPpx5lZPrc_CZmXRzJJe3fKxfvr44NVBCt54t27MnvZxtgmUImjk95f6k9clJfMBcfoDzYGvplyIJkkxS7PjvNMGtCvhCnAWsRmzLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rOIRlr1NPDYNjUTJnh--cpaC7PO2mUw5yiPKLentNxYwkPaHKvSNrwJujqC99t3URmmytXD7GkyCKdtHU7H2vguCklNd84-UGfn65tscj8RCx40HdZs8jfh1gw5yW7mONx5gTUCoZzX01MX8xEkojOiOdxDBpQmVyZ_KpWJhbVJ4HV3vFb59S9dpZPYF3gdwUBtYl0cMLjLOXVc-bGgbl0TaVEdQNsC9A-ziT045aXyhT2ibt7ulFJv-Y_uGeHiTHhyueYnYpKBICYQhMt_SRVKkgfRWM4L9tOTNNfJPez0aCqyb3DbgB1tJ9XmSLqIxyz3aNePsvJiJrQMX3RNfgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=rOIRlr1NPDYNjUTJnh--cpaC7PO2mUw5yiPKLentNxYwkPaHKvSNrwJujqC99t3URmmytXD7GkyCKdtHU7H2vguCklNd84-UGfn65tscj8RCx40HdZs8jfh1gw5yW7mONx5gTUCoZzX01MX8xEkojOiOdxDBpQmVyZ_KpWJhbVJ4HV3vFb59S9dpZPYF3gdwUBtYl0cMLjLOXVc-bGgbl0TaVEdQNsC9A-ziT045aXyhT2ibt7ulFJv-Y_uGeHiTHhyueYnYpKBICYQhMt_SRVKkgfRWM4L9tOTNNfJPez0aCqyb3DbgB1tJ9XmSLqIxyz3aNePsvJiJrQMX3RNfgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm5t1SqrDYy9vGJvyPu9IhjsQnS7RqfnkdZlMxhdF50IiLNfFeS_ImFv3PWL8bwNFE-eu50fyNM8ocp2vRf1CeWwv8znKNaTFTjjyxw7qPwrLBFM_1IbIYv354TsdYTFNGPb1Sh7SMlTQgC5UkRQqsTGeCFpYnqvwKDYXso5_lF2YKYSE1eROYjbfGJ2QqigHWqRugUwmx8QGXAYV6p9UgaWoleubhSdVzMMXeD1wt_cIdajPuiKLw3SpjPdeqMwBjxdCoXdXm_YMJ7aLGx92wYtcT2mU-Ufuef-tqLH67TNl-njXKzR5elmOZCTjygAyVjTStjOarMikSJiACCiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aR-UaAUOcgEkxA48WiJpMfTNifXKmycE-GGMXfWXHtGp0lXyy_x_NHeDr6jkKGlVdviacoEUJniuHlVoRkhWJJD7-iV39ovknmeeiWrMAWzXk6LxOc92T5A4IeJv50aOSrJ8Oy3Ii3450BqiIz_mUVZ9eQ598D_apXyTn6AvS320K9YXW18_qWTe8jp7KcimOMss1F8eT7K8nuG6ldr6zD3vArXpD6wLzIn2Iv8XLmThoByGiD0JdvbZ0xr4u2DG0L08Q6IorAMMDaYPEMvw3434IgwHhotXGiJI1rsbSlTWH2ssqRX8MORt3owH9KjQPVEchWopdvGtwN2whGM24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsc36-Z34quT66vcid9GhihlhOeafw2iEDj-nJ2lyTIIypq5aDXJ9yhkd_nhhwll-6q3xrSB_fMdYtR1J85f0MWFjFm7KRqF8CaNN4q7iazV8X-u8Moi7imm5-xLljjW1NYquPXmjUHi52dwrADLQ6NxIxnb5cgMOz3KAU7ut_TCYLFVE_AgIgA_wuuvo3nUXF1HUOIFyXWf8nsS3fbed9hmNQnGrv9_KJdSQOgN1ah5opI9IdjnrlW-rc2BJetiQdL7tdZcb-fkvbren7fhxfF-lkHdxtwv2x6dwUrmyFzNvQk6XfEWNrQlskXWEWAYhV8vJOptxU9o3VIGBXSIvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVHlIK4wNJvOtxi1aFdkTjyVa-firHjDi7-JsPfMWFKkvEXpr40OSk-L29bpe8lsMQ5Oqv_XJfwWbdjT1npeqqoljUNN_Zk6O_rV0b1c5PNBwmP_mP7SEv0o9QFYwoCtJSJRqzK0-imJi0xr2_KfyTvyHvMNnJAa2AQ34qlktjp9LO7pv_78EW80bDLkMjEdsVUvI7zW-P7jmmgE5PzKrhBDV-DruDaAd-x5Q_nXK2liYQXjmvXfQJssG8mjbbiOvUUQaPi2do3qSDRiNSNkUsHTzOZpRt1PwoWK9gDkHz8HMyDJGpp7CzihnxbPPJqI9ERsc2hCUZytIy2-QCjPrQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=nXYAD3457-nfnlDulUPrrnWaF1tWY4PU6vcuUV_-acsSgoR7VzgFt6AlhsbxHWC-XTKhmdYaDxNLshepu2JcjKsF7sRbwbZGFN9PDSam0seBCMx53KrKGEM6wQDG2TNGTLLXM_LfKMOpnnHme5fGAkD-g56qLEEAPLsnBPn_2ehyhSmE3F9S3iGj2YIxOfHLN-bWEHaVpLYYcbA6SL-_G0-COwab4M-HJDz02Jhflvz59pFoSmNsZiaWuDfTgww2d-yzHS69XYLHKYxhkhFzp2O-EoreNi1HTgZyjXo-qV3RGVTEbpY2J-wMzW0_kRrIM9YEysCgdVYjZyhlDAeBB4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=nXYAD3457-nfnlDulUPrrnWaF1tWY4PU6vcuUV_-acsSgoR7VzgFt6AlhsbxHWC-XTKhmdYaDxNLshepu2JcjKsF7sRbwbZGFN9PDSam0seBCMx53KrKGEM6wQDG2TNGTLLXM_LfKMOpnnHme5fGAkD-g56qLEEAPLsnBPn_2ehyhSmE3F9S3iGj2YIxOfHLN-bWEHaVpLYYcbA6SL-_G0-COwab4M-HJDz02Jhflvz59pFoSmNsZiaWuDfTgww2d-yzHS69XYLHKYxhkhFzp2O-EoreNi1HTgZyjXo-qV3RGVTEbpY2J-wMzW0_kRrIM9YEysCgdVYjZyhlDAeBB4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Km1gTZqCNYFXEtkLqAEoSZQmxLftetCIVeslIr_kbj6qvB2uQr6FnkK_Cyl0X7esHcUjF25vGZnzSlfYm84P1sODOOZIv1ydUkMorx5Z0iy61VgoK7v7ptnNNUetYWGfjGEso2YpViBoFlliQxE5fNuKbncEGx2ULeE785NXdtCDJXpaZjapVM1w2aHj5QAVT-ETFnEu4Vt4kfWMP_aOn1UYsc4C8eJoOByMWlefZPWPDONvd_QRcDjD1dv_5h5sUcLCGzY-VSNrM-DsaYU7sAYHuVpOAIrHEgoahoUPw1g4_ul6WYApIUX09lsLynNvOFWC8tioF0sc6cPS_P7xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Km1gTZqCNYFXEtkLqAEoSZQmxLftetCIVeslIr_kbj6qvB2uQr6FnkK_Cyl0X7esHcUjF25vGZnzSlfYm84P1sODOOZIv1ydUkMorx5Z0iy61VgoK7v7ptnNNUetYWGfjGEso2YpViBoFlliQxE5fNuKbncEGx2ULeE785NXdtCDJXpaZjapVM1w2aHj5QAVT-ETFnEu4Vt4kfWMP_aOn1UYsc4C8eJoOByMWlefZPWPDONvd_QRcDjD1dv_5h5sUcLCGzY-VSNrM-DsaYU7sAYHuVpOAIrHEgoahoUPw1g4_ul6WYApIUX09lsLynNvOFWC8tioF0sc6cPS_P7xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qiuPZIG1ONshiEAnCryMlDz7SgQulobLQXs9zykUiqkE7EpHi65dYH8Pm6edlUuSOiFoKwPrgK1H_9585ZUkyg2ka9aEJskJe-sDw9CVEkhSzINbiDsQ7R4bVXVtRK_SqGaTHJAnEhzixD7Gwa7EhPd-fzwEKfWH1np0vkpSff9rzLFezTQNZcmZHpwFcdfe68YCAks_Zh_vNAAY00fuduIiohhctxHRt7lUrQgxxyPNimlXKfIFlAbOUrxvy7Lhk6wbSd3-NAXIEU_cKH-FEHAmkiMEp0Ycdy_2FaCcvDCf9qRUTi4FhFebu-eUhdHlZuHu6AeF4ZcFfUiaI6zM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=qiuPZIG1ONshiEAnCryMlDz7SgQulobLQXs9zykUiqkE7EpHi65dYH8Pm6edlUuSOiFoKwPrgK1H_9585ZUkyg2ka9aEJskJe-sDw9CVEkhSzINbiDsQ7R4bVXVtRK_SqGaTHJAnEhzixD7Gwa7EhPd-fzwEKfWH1np0vkpSff9rzLFezTQNZcmZHpwFcdfe68YCAks_Zh_vNAAY00fuduIiohhctxHRt7lUrQgxxyPNimlXKfIFlAbOUrxvy7Lhk6wbSd3-NAXIEU_cKH-FEHAmkiMEp0Ycdy_2FaCcvDCf9qRUTi4FhFebu-eUhdHlZuHu6AeF4ZcFfUiaI6zM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMbPo1yOs4E3swIvIdovmCoBLV1bbEvIDgFtS-shZzAivEcu3I8fgwobSBk-MIYDnppfnEZq1S4aEXzbRq2Ci2n9eGN-YyIOXB8vuMPtAd-azqhjVBnOec8gtDsCBs4d5pNwqzHrUMb8UnRFbSq4KoCLRhQYwSQ_p2icGuLFjyVpW3LKKxaXHTPhd4YKliQ8gBFWq9baKZmbFXUSchXCHWTfKZOg8QZ2EhxF6eiXu8kT608fmiD-JNk74af1ep62Ak9w1q9GMZcdpWuF6SwGXVDLo0Roj_UbW9JnLNIFeEdS3fle2JJ8c8OAZ-uFbRSYovcGcDhjVYzvJInhKz7Xhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PF1o6dBBqJd7jMVcTPhHzVtnIw3soUwpWDfp0eDDqiri1_wj-9KNPGWaOOHQVfwLRGC7ethtbTTF_LkFo9fYt3qna38DdMBdybE77mOThc9inZf-vevShdKGLzk4NIcXmuNpsh5GiUkFMdwS0087-7zOFJ1gswK9Kg7XyPl1G7rMmlzHli0vd0NxEaTvcjOtdawNframKyw28dpKmHMoFPc4f9mVS07i8NjgpD9dIHCEImTupQ2VEZEuL8v_vhU-XcTqhaYuendrSrDiQFUNsvdMYFxNCD_vTkdbDpSZlbd_dmNGemlZzgNDqjD499GkvqoK4WjqWT6Dq9SUu2KyOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PF1o6dBBqJd7jMVcTPhHzVtnIw3soUwpWDfp0eDDqiri1_wj-9KNPGWaOOHQVfwLRGC7ethtbTTF_LkFo9fYt3qna38DdMBdybE77mOThc9inZf-vevShdKGLzk4NIcXmuNpsh5GiUkFMdwS0087-7zOFJ1gswK9Kg7XyPl1G7rMmlzHli0vd0NxEaTvcjOtdawNframKyw28dpKmHMoFPc4f9mVS07i8NjgpD9dIHCEImTupQ2VEZEuL8v_vhU-XcTqhaYuendrSrDiQFUNsvdMYFxNCD_vTkdbDpSZlbd_dmNGemlZzgNDqjD499GkvqoK4WjqWT6Dq9SUu2KyOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=bz9dibFNDD4r_Lr05HA9WI3c6U2iYaicqOLW2ZHHeU9aCi8Rppm9lqpJMEcxxcDouCimMLa808r1N1Y-J9XUqh5LDGZNYTQxNHszcPw9Po6PjGtaNesKzmVm-D2zUrMauUDhnFooMygLi_yPZwgXoMDiG6fTEOybrRw_eKuBIsUNVomtDvJJyiioDaaVLIDGlF-CeiFOgbcSkY2AYVlmFWD0JmdKVCaiTaRQvQjAMwFQF8uHg3iO8iovKkolOHa1yzevXYmlB9QDVsEgldGXZ-hPz9IbHpa8aExmw8VDsXivg15WWfFL8aPzLVRnuhFbBHbLUPI1srxZ7AAKklmPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=bz9dibFNDD4r_Lr05HA9WI3c6U2iYaicqOLW2ZHHeU9aCi8Rppm9lqpJMEcxxcDouCimMLa808r1N1Y-J9XUqh5LDGZNYTQxNHszcPw9Po6PjGtaNesKzmVm-D2zUrMauUDhnFooMygLi_yPZwgXoMDiG6fTEOybrRw_eKuBIsUNVomtDvJJyiioDaaVLIDGlF-CeiFOgbcSkY2AYVlmFWD0JmdKVCaiTaRQvQjAMwFQF8uHg3iO8iovKkolOHa1yzevXYmlB9QDVsEgldGXZ-hPz9IbHpa8aExmw8VDsXivg15WWfFL8aPzLVRnuhFbBHbLUPI1srxZ7AAKklmPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=KdT1tTikrBQKjMz4PtTNkuEvNgBa_6HJTfsNXl_kYLFn_Z1zBUVriuHCvmq79oWQeVpYPmwbZkNF_cujX2XsLQqw1TS-bnZEtanqIHhLZEN3K0LzrLNtmm8l1_D1z9pvE-FJKzlVKz5gICVixm0DWA9bLXo8OjZBHQTnET3MyDot6W3VW_L0gJpFJZjXXvADJcddQIcRoIXv5nMK0_ZLQhTuuDpMDs4n90unAEnOurZZt0fL6hlYzOx0DD-6MSsXinIPzzwYg3wFB8K1rNRW3RIzWxaTcvwDlAjurhPk9qurG1k84zYErEqiresxo68pE-AqkOf3DGfhBWV3MVzCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=KdT1tTikrBQKjMz4PtTNkuEvNgBa_6HJTfsNXl_kYLFn_Z1zBUVriuHCvmq79oWQeVpYPmwbZkNF_cujX2XsLQqw1TS-bnZEtanqIHhLZEN3K0LzrLNtmm8l1_D1z9pvE-FJKzlVKz5gICVixm0DWA9bLXo8OjZBHQTnET3MyDot6W3VW_L0gJpFJZjXXvADJcddQIcRoIXv5nMK0_ZLQhTuuDpMDs4n90unAEnOurZZt0fL6hlYzOx0DD-6MSsXinIPzzwYg3wFB8K1rNRW3RIzWxaTcvwDlAjurhPk9qurG1k84zYErEqiresxo68pE-AqkOf3DGfhBWV3MVzCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=GfWinny-JumMS8_73MbGC2eD1PEOBW0SISEDrZ5Gf6bat-SLa7DMONQQ47VrwrHRx4Xtqw_9oLieFxV3SHswFmd9U4XdUikE0GZTsbZhyyLM7LzQFazZ333YFzAlVKbtZMFKUWN0eL8gN5Pj_10oiqYIBW-km2o5bsn4auSgrl1iQQUcD-gCbc69Vq7XZuTVArLWmVgjjUueH-5o-o1NrP0_gb6c55lPJuAfovt-T_C5xE0gEDE3sLy6UFtQoh4FmU1KXfEwY5df_84rS0O6DOff-z0XYtkUIRSJ6jWOejTm1lE8ZaB6FDEDlM8F_ZgOhnozxXjjMzXBdhHo_5W5sqQdpGWKxb8sz6cfW9QVf1FlNmwJ0Ov6cub8BvQBjvhdTD-OiugE6aMIlsrHtJZ2i7bNDsD8FyTdHVw48EUXqZPBkQW96l9o2pDKwr0OIAiR98Esm6IBFj4C4eiL47gwkoq63IOqSP2ef0KlPQQKYMHuHxet000HoN63NROIK6WrapihjOHJZ0cONNQxAbX5ToVDo0ELRMsAgJmoURcqRlxoHH6ToidVZ1DNiKA4kO8E7aGLxueCsDp5tcpgbLA9XpYSGCSu1fTMtteUZD1VKs1u8cQCuW80EpGYuZd5wbyAzRpBf_tdgbOcYhIdA97ngrlbDN8bO4adgqesQL2aYao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=GfWinny-JumMS8_73MbGC2eD1PEOBW0SISEDrZ5Gf6bat-SLa7DMONQQ47VrwrHRx4Xtqw_9oLieFxV3SHswFmd9U4XdUikE0GZTsbZhyyLM7LzQFazZ333YFzAlVKbtZMFKUWN0eL8gN5Pj_10oiqYIBW-km2o5bsn4auSgrl1iQQUcD-gCbc69Vq7XZuTVArLWmVgjjUueH-5o-o1NrP0_gb6c55lPJuAfovt-T_C5xE0gEDE3sLy6UFtQoh4FmU1KXfEwY5df_84rS0O6DOff-z0XYtkUIRSJ6jWOejTm1lE8ZaB6FDEDlM8F_ZgOhnozxXjjMzXBdhHo_5W5sqQdpGWKxb8sz6cfW9QVf1FlNmwJ0Ov6cub8BvQBjvhdTD-OiugE6aMIlsrHtJZ2i7bNDsD8FyTdHVw48EUXqZPBkQW96l9o2pDKwr0OIAiR98Esm6IBFj4C4eiL47gwkoq63IOqSP2ef0KlPQQKYMHuHxet000HoN63NROIK6WrapihjOHJZ0cONNQxAbX5ToVDo0ELRMsAgJmoURcqRlxoHH6ToidVZ1DNiKA4kO8E7aGLxueCsDp5tcpgbLA9XpYSGCSu1fTMtteUZD1VKs1u8cQCuW80EpGYuZd5wbyAzRpBf_tdgbOcYhIdA97ngrlbDN8bO4adgqesQL2aYao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=mSM4RqyXfkE7pjkdqD9HfsXHilrsq9pd3h6BEzhjADZmhQzIwSYpRXkckZGfl4BlF3jUPdiBqlhgFUY0hTea84Mgnt5a32PeQyC8S_O126PJ7cvaPALz70zfNR3C4-lniGCm7ZsWRN3TdSVtoUhxhdGsidpVL0rrj2pPup_tffC7fpviwH1344jXuFATCE1jmhYaZ3uwXGhWhC2vwHkRAWtF8TeFs7adKvNCKvaDSjnir2zRNTd4AaCI09xlxIi1YosUcJXZskYm9VdSQPFPAHIRBdQNODbS6L1w8Kh0sMNDMmugyoEWt8b8LE6PEsrGwZsRM-tAvSD5jDKgmolvTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=mSM4RqyXfkE7pjkdqD9HfsXHilrsq9pd3h6BEzhjADZmhQzIwSYpRXkckZGfl4BlF3jUPdiBqlhgFUY0hTea84Mgnt5a32PeQyC8S_O126PJ7cvaPALz70zfNR3C4-lniGCm7ZsWRN3TdSVtoUhxhdGsidpVL0rrj2pPup_tffC7fpviwH1344jXuFATCE1jmhYaZ3uwXGhWhC2vwHkRAWtF8TeFs7adKvNCKvaDSjnir2zRNTd4AaCI09xlxIi1YosUcJXZskYm9VdSQPFPAHIRBdQNODbS6L1w8Kh0sMNDMmugyoEWt8b8LE6PEsrGwZsRM-tAvSD5jDKgmolvTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=i2t3kocUTI-cq0O0x9y97-NwrRVb4kH77PyhXZj4sP5rsENs6xNzI3Rz3GPR0WGo7GnPdqZg8WglJqC6ZNzRMcqtIrDS2gixvYu0LihzNpzBxTQn4jPl10mq-zgNrOiMTdIY9GAWbBlfdoPu4cdBvVcGDqGmc_JvqoZwpQY-obDyKYleArOO3GCwYpBKFoWct3z-ARDSDfFyWqzCRR3UMb1xi8EyYJiCDVAs7QugCpj5hBkT7k1s0vU4hal7CTo9P50fz3l3n-sYjMGy5p_6bJT8Df4HV1G_BTbM4Py9uNbTuRF-FFbL3aIi70wqnyAtlyyQUtBy9ToWjGpNWQXCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=i2t3kocUTI-cq0O0x9y97-NwrRVb4kH77PyhXZj4sP5rsENs6xNzI3Rz3GPR0WGo7GnPdqZg8WglJqC6ZNzRMcqtIrDS2gixvYu0LihzNpzBxTQn4jPl10mq-zgNrOiMTdIY9GAWbBlfdoPu4cdBvVcGDqGmc_JvqoZwpQY-obDyKYleArOO3GCwYpBKFoWct3z-ARDSDfFyWqzCRR3UMb1xi8EyYJiCDVAs7QugCpj5hBkT7k1s0vU4hal7CTo9P50fz3l3n-sYjMGy5p_6bJT8Df4HV1G_BTbM4Py9uNbTuRF-FFbL3aIi70wqnyAtlyyQUtBy9ToWjGpNWQXCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8oAPVkedcrLfl4KwaWDz-0t6TI6rWcjyCGDw38T9c73ul3YwkSrFDIxe2aU0GomcKMtvTpu-IgwQNsZDjF3XRl01QHgMfdjk4bp0Jj9RsbD3HcyRwD06ocVYZS_vyyDhJTwl5vIYTdDhXJT-74-DvtRyvr57uPAxuZNPYOkFj3gRglmfBtzLl9mB0ACG90jeVcLp1qUtN2fsY6tov8oU21SuILyeSUAkg_d9joNktoljapfSFC-k1wDOueIZilHKWubdKoVsXi6fQFK-Y3LeYgnvFnXnuXvo96VyVrY6b9ojedYPJKen02RvSxsuyn64M83nu2u6N4naMiZWCwXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft_UK6BKMSH-eYwshClyfrpED6DHGkhNvRiqkf46ePRg0iAsW8vv1eCBlLdd3anK8A8azxHvvs-d4qOxNPe7oD-lUo6vBeQt0J8rkUL0eoc9w22Lp68S1a69HA0evCqpO41Qz5KHSAKQ5ft835kR6HfhGzl8Tlq-Tq83olcdMcvJZ4BFiDvTnFfmsiLWrvw8Red1Iimed-RquQxY5ENJfuqZT1ptkvPqbbC76hMGjIi78w7myMvdWiKxVcg3aX2rU8ee5iM3id-aqbOBZDrmVYNX9g-OTorYxDNMXf_ikccE2j3GfhxUGNCYEb-v98Bhw0lwo6311jNH9B2IHZlMxA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Yt61HdT51bdcjg4n1YNK-wN_-X_hJ89NYW6fsY7D0uqFreBLpX5ursU91iz3DHlel1bqm5Rh14sLJaTVtA-ArgQnafB_40wr0g_ft_czh7Gb7K3lmS9OM9Sq9jEQ9Py2V6CDZ5Ke-2IJyFDRGiX6WPmEThiTId3fyvge_9CO2r2la8WCnZap4aQSeA2UQyIJSOi2b4eprOZRqMA8naV0F4nhMHMI_P_44hnj9Et7XnOYHarFksRTbiLZxgAe2P8gc80WEZYbiVbmfcjNkELpANyf_rwwXsJEnUHLRFS0mIIqF83y61l8kmUvIpzxzEBRXyS85TUL6fZtk6wZ1TZnq7V71xf-vZiTHAD1P9E5JT3gQQxcyrbQlueJCQadevruNXELAkNdeWle7Ri19BJgZmhr4_PaFcwtr0QHlWTGGPyl0qyId0DnpLUXuw13pJLGx8rhUudno1IENp4d1CCUBcXMOW8_xyKhrsJ8xqIWt6iYwOeofjTNf7HWlUVITmOGBwSf5-C72scuHwVKdH6Gbiad0SO1iU1BCNAE7Ozr6bkh9v2NXk6CU5PYiu-pvqwNtEQpRqrFXxEuhcqOARbPtMmz8wjG99qli-hQpGKC3RhSlbJ7WQyiP0zDyYXIK0Qht0W7dp_NbEcF15YWsBCvYrwitdcslXkaGKAv6uWQaUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Yt61HdT51bdcjg4n1YNK-wN_-X_hJ89NYW6fsY7D0uqFreBLpX5ursU91iz3DHlel1bqm5Rh14sLJaTVtA-ArgQnafB_40wr0g_ft_czh7Gb7K3lmS9OM9Sq9jEQ9Py2V6CDZ5Ke-2IJyFDRGiX6WPmEThiTId3fyvge_9CO2r2la8WCnZap4aQSeA2UQyIJSOi2b4eprOZRqMA8naV0F4nhMHMI_P_44hnj9Et7XnOYHarFksRTbiLZxgAe2P8gc80WEZYbiVbmfcjNkELpANyf_rwwXsJEnUHLRFS0mIIqF83y61l8kmUvIpzxzEBRXyS85TUL6fZtk6wZ1TZnq7V71xf-vZiTHAD1P9E5JT3gQQxcyrbQlueJCQadevruNXELAkNdeWle7Ri19BJgZmhr4_PaFcwtr0QHlWTGGPyl0qyId0DnpLUXuw13pJLGx8rhUudno1IENp4d1CCUBcXMOW8_xyKhrsJ8xqIWt6iYwOeofjTNf7HWlUVITmOGBwSf5-C72scuHwVKdH6Gbiad0SO1iU1BCNAE7Ozr6bkh9v2NXk6CU5PYiu-pvqwNtEQpRqrFXxEuhcqOARbPtMmz8wjG99qli-hQpGKC3RhSlbJ7WQyiP0zDyYXIK0Qht0W7dp_NbEcF15YWsBCvYrwitdcslXkaGKAv6uWQaUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9rkdCPYWbkmA3DE0eOOV-gPfV9nKdAoRckxXfBT0FRJdXGy2udx--U-9DgDQRP8dH10r904DJPDy5SkwpDbZycWYGaybc0fp1ARF8SKVnJnnR_TXGdH6hxwAtmmo-Xh4k6M90f0Ggxp8dh-TeBRVTyZQbuNbYMx2djUU94BFdE8rDj7qTDkyhgU1bjKBZojmR2cizOLRJPhn1mSpN-wkIhYHqfZxb7-ACAsY3P9z1hSDuWVilPWTJQDGD6G_pCNxdJP4rtB28FEMRnOBlXWay-p4SqRmlRo7ic-rI9xELjJjMUaRZMX_2bNaLMdHmfLhMWPoxdGDw98GE_PCn-TuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGhhg4aGuscARJlvbxDoBf7Dm78BZQsXk6yBcAbu4TIpa9yXabz5kH8-J2aluADzYvwX0IKoGzruDOOFca170tsG94TSKamc96kQwz9nsBnSxNMVG22kRBUuVz42_RiKNt-u7H6X-XMV7aWNT7gETypBvJ5rTYCycrqzrcdc-0go90RK68MxEbQYuklDGYcFGUYPs6fRYWL-LFy3YahwobdbP9q7hsJpzR6n14WJ8hd4EMB5B5xYsjzz7spI7Y2g0BT2HLhwnrKh3xLKwBaRweA3WAw3uqy2H2Srzpk1myfgWDnL7RsC8Ou6vUtIVFFao7_d46crE15h3zgUd1t_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxbSgklLIVYjPpuzkQoKkBxGMoI4p4-lDIzwssRMNlLwwqNw3BawJ0y2g2GblieILoyatbEGMF1oYjDrFrf8FbBZufYqO6cXQir-3JXH8yHGyBoElgjRTf_Y_3K2KroKdsMzg2DUBtDXgoyUHJ3bmH1es3NDIAIOyL7HlkID4EHRtEEH91G7dyoa3Pr35fgweI3JhNNRM-P4ZYrRnSFeWzJbTeJctxLy8zgVTl8GfGOpKzOk6bA1E5dSUysWsLAlTANlkMc93fgGUbftB87bin2XC28NmvyAWnF63SUpRaa-3RIc9fBspQNYh269DvE4hsrpJw1jzpJ7EeANHWO6AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dabb_Jk0i4Cghu7X3QG8_dNf1zV8IAbL9S3FLjT9YX76qJcpqlEIRG_e19rOdyK4B-znz4SV9iPUMXLXVU85byQ_1De8OEq5ST4_4eHryiel5SzKwyv6Lf5edHj9w54I0TOkbw3owwfwzdcaU-B1kZYoFrfoal5wZi9Zqi-2Fl1hvWggO3CMw8b7kAelhyPIfkKeRPz9_Q2qXiKdB5RaJ8URjttzZ6jFCPuLWNy3rJF_gm1yMOFnJGFk1jbTriKngo4862RHrL__3c4Bz7Y_8Ivqc5aOKAIg9dSkRr0jtlS_SczGE9Tj03fh4wW3g2xHuGMIQfiYZmATgkg_X2Xykg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ubZRy9fgbLJ4iTHQfGQBAV0_El3OrbKNNCD7HNpEEpPfHbnP7_qyl-U6v1HmizKiOTEFdBH8GCM9aNTkD3ScwTzZK-vpZyhpPP9-NTDXIaJSq0Ck7qCljCEvaPt_a3UXHrHbSbQfv55WYhgAkshB20jBTvxIE8-UY-nIy8TPnPs5LCk2w_NDRt61edEtbYL_dSuFCG0FjL8qHGE9kFLF_yDaXhqr8NwNQWIg03NhRQF0LUIeh4wu1HZrwSVbEc5SCR_Jm5w1MLdRFhAQ-aJLTgLPQGP1tOmXhAC9yfESYksEoW3tnxT8SdhmRS5pnYDSWRBy_qGdv98jrQE_tZf2DoRHWHc_eEscVWAPtKQC3yn9O1Gk0Wz7kXMlu6JIV2ZDqsh2_MYc1Zqf2eDN7QAeamgt8RbO_vOyn9wFsCOE759Sbi4LGMg7xkMt9HaJ4dWKIygriM-1lZ0lXM_47bOXCJilRsvU-tihfcfAWmOHLA4cFfbg2xLBdEh1L3tkPuXrms0AX07hrQqcDkc-SANiPlGyog2SA90By4XfugYEyrtbUxaBYIREOFPOyDGub67RxBMKI1DVr-A9Q1saKniAQiEwKBBY8zSLuu4NQQIJn1BgPZFfOAiwZe7YisHg9BQM6uFYP6VnD457xUIOPg8EE28hfJaKw9X3PyoFPXwDwZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=ubZRy9fgbLJ4iTHQfGQBAV0_El3OrbKNNCD7HNpEEpPfHbnP7_qyl-U6v1HmizKiOTEFdBH8GCM9aNTkD3ScwTzZK-vpZyhpPP9-NTDXIaJSq0Ck7qCljCEvaPt_a3UXHrHbSbQfv55WYhgAkshB20jBTvxIE8-UY-nIy8TPnPs5LCk2w_NDRt61edEtbYL_dSuFCG0FjL8qHGE9kFLF_yDaXhqr8NwNQWIg03NhRQF0LUIeh4wu1HZrwSVbEc5SCR_Jm5w1MLdRFhAQ-aJLTgLPQGP1tOmXhAC9yfESYksEoW3tnxT8SdhmRS5pnYDSWRBy_qGdv98jrQE_tZf2DoRHWHc_eEscVWAPtKQC3yn9O1Gk0Wz7kXMlu6JIV2ZDqsh2_MYc1Zqf2eDN7QAeamgt8RbO_vOyn9wFsCOE759Sbi4LGMg7xkMt9HaJ4dWKIygriM-1lZ0lXM_47bOXCJilRsvU-tihfcfAWmOHLA4cFfbg2xLBdEh1L3tkPuXrms0AX07hrQqcDkc-SANiPlGyog2SA90By4XfugYEyrtbUxaBYIREOFPOyDGub67RxBMKI1DVr-A9Q1saKniAQiEwKBBY8zSLuu4NQQIJn1BgPZFfOAiwZe7YisHg9BQM6uFYP6VnD457xUIOPg8EE28hfJaKw9X3PyoFPXwDwZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CRj5duocn-ao2FizzJ2ITMWhyiXCcclGa8wv_qFqQ_OHhgsBSlvqibcCz5Bxan1hxth56huTgroxQyWdvM1Q0eu_eoMmqYJ1KntSwDdjvK1xIJorq6DW88rBCXJNvYej6sFvGw81T8CXTMw6QgS6n1fcZH6qbyzNIEQKkGW5H0sSD_uVApWlMQkzXGqBGzrP2ccras40k7nb458kuC8S7PwbLnkCxREdsZPByTxC_PBJsWp2XyfygBaEj_HKrnTwn2uOPDwZV_xif6EUbhMLPCD6KPrdenT477XjHcuAOjp-UE5Cbwh762IpKGuCQvXyrln5mjgKYqlozjueyHt_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CRj5duocn-ao2FizzJ2ITMWhyiXCcclGa8wv_qFqQ_OHhgsBSlvqibcCz5Bxan1hxth56huTgroxQyWdvM1Q0eu_eoMmqYJ1KntSwDdjvK1xIJorq6DW88rBCXJNvYej6sFvGw81T8CXTMw6QgS6n1fcZH6qbyzNIEQKkGW5H0sSD_uVApWlMQkzXGqBGzrP2ccras40k7nb458kuC8S7PwbLnkCxREdsZPByTxC_PBJsWp2XyfygBaEj_HKrnTwn2uOPDwZV_xif6EUbhMLPCD6KPrdenT477XjHcuAOjp-UE5Cbwh762IpKGuCQvXyrln5mjgKYqlozjueyHt_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYu6urojlujvBswd6xzVFJfW4c3jmxZyRciMseujywVJaqdLYdEWqbyhtMTv5ZnP9JTPbA2oztosvhnvuC8g_OzaD-wPZXBM24E_r5QtjrV1-mb7-jP_ds2f5U2K4jZoHKZHmrVWyIVOLd88-65-r0XoTwHTaSNViE2uNrVQ2IgTkdUHdXsnzFruGFGlSQC6S5Rj9YInJGjlv0KYe8MI64IlXqt7jxoyt07F7_Mw5MUfqLIvzISuVbFmWYFNwti9iZ2cS4TqlbDol6bM_DxlMAYg6Oae5SymWhza9MUqrKD32awkKZr47qQn8ZngfygIzyBbftMgUsGgoFFYwVANNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUXPQAYoNQ8GS2lrDgD0ec6G_3BGr18vLV-Vk-od_X7npzQlSCt-e2nWhYgkecDBL4aOMW-GC_e8eQ0Wte0Vo-rqrxTvVJxmHzC6k6wpimAED_tjxSsjb6fge8GiL3doRlZcg_0LrI0O1ZcV95OHfxdbkaGrgwgYJ9ZRwv5vpADbIBw_8kuRWFTRaeR2R1KdD99UzviwfHn2b9q60NNuO9lO-hvqBPD7uxVcuD1aWJaX_9iWh4qWi_XaisyhnrbYRxXTb71lCqoO2SlIXnsw88mKUZZOZo8c6NhdLcoE7-w8Cs6veBzEdKrcAHRF7Iwca2Cqp3rrpF4at7GbfA5Iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XU7dZHKbS673lYKx4h9OjNt69fiaDjUitD9OV3THPaQwKHl-uL0heyeJAGm8AQJN62L7_gi2xL4rO3_2le0QDjVO4eCoX4kk6UbqpEFTYraowo6NhPhuCJ9RQurZiLJWA54sU6KTZSwhFGe7kPSyY4I5Bw8GNyHjyqtbJq-_o4iHCJmnph-nP1t_sv1ELK6U9pZ_XOi8fYsZAvXlHuSi09SaQI9a_qPhRXwlr-8j9vxM3SQHOVkfQ8wGqGe7fCatMOKefMy6HkVf2Aa-Y_HzWQzL9S9ROfvGFIOjDUFGRoVNJoyr3Ja61WEIXoiGNQjbz0QzNK3rvPNYlRtoiyYmNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ik5yjGJe4jexUfUG91Gx4MV-QejisUTZeH5YARkrKkf5r6toI8AA3XVSwJ769kxPbwoh-N3vb98j0DQcEVo9YumRaEZHxuTGrAH7sP2jJskDaz0Z0Y8OPcgn79Rwnnm5dcFzR-Bs00htU2-OYjth7cuARQUCQulmqhiwtRrL2zL62XL19Ig1b3c93-2KZkAwI3J3PVQ71Y5_rARGRRmRbOhnWQepq-6NEKECrF_AzgDe_iZeOkkDV1zdG6vf_jphW96CDYcplZXOm64f3_cSjkmBBHVlUFQcL0-Rr0XPVD8JKwbU143Zsy-gb7mmwEktOJ2k6A8BKGj493_2x70uXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMp8YbDUeU9ZLdJX5-Kz8kX1Ax0SCwZnr2nhIXAtX_zMO7G0q60CaXVIetF-SP7auxKV3xvL5Jy395EXNUxTp9GYOaa9nDPgUTphd-u32OrnXdzYpgKc3PeDZqXaXNx4xcGStwIeTNHO0oYn68sYd7jr5EMPo8NldC_bBInWVLkMVEw7jUkx1WnqO3YsR0qwWfjch9fEJCSgJzFrI6jUeEPJihyyaRDlmoQrtcdZH__rOPYle42u7QlTRkKd08c784ZR7xLDYhMAJUxAdtEHN773DC1VCITrysxGRrRQ6a1-NOiX13UONYQE_thE5jHIrGE-7b4YelySggxqW6gNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvD0vn0LhGVBoui_-YQxmUKz1iaxsAgZzfaithqaKqhDVVV8gRoB_3mLrnb8ZpC7el6NLnit849ynV8XIcBPxvHhZZuASpGmsy0KGrzvW_W3UbJXs0-oQVlYiE-c1DrDWhE876-mC7uCai9RTywQ--GxYpb__3XCADB33NU-b3WrGwC8e7BFWC7DiYmwqyCNv9qV6TgyVchw2FKVlM-nuXmOYzjV5FkB0X-eD5FOmfoXS3dvHYoE4WkZPthzxwdTslEM-v3RZEzp1RvydqwEcdlM_9QgoHSCYbk5aHZqaXrPCkt66yWEDY01bwQP3p6CpU7YJ1-DA6VkuL-67wPpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=X5TjBwFogE3AXo-3ml6DZGKs3bzZOouhnKcU3O7_-8Co_Dq-N_yUYN1bF7vg8KMTusD-MmeSY1aAXkcom927dQ9edu1GJJ9Ec5vNe534XZgDcgn3TjTL54SBN9vhMo1yKN_esqP163XhPdbcaPQFfMKoe7IJYtHqnbdG8ijE_u7yTWjCRnPA20ZP0Fmr-0biKVC2b6tCnHXAKf4S88Cbv8XFaNFGgcT74FyzDpsvN2vZvK1KhEHAQbDp45H-BTp7Orcmml1TKsV4yJT_da_8gMdmJ3q9n6WW1H8ttt8YSLlcwTe7HnJX45cXEhmLEEXXTwHBL7Zg-dYShL5h8iOAww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=X5TjBwFogE3AXo-3ml6DZGKs3bzZOouhnKcU3O7_-8Co_Dq-N_yUYN1bF7vg8KMTusD-MmeSY1aAXkcom927dQ9edu1GJJ9Ec5vNe534XZgDcgn3TjTL54SBN9vhMo1yKN_esqP163XhPdbcaPQFfMKoe7IJYtHqnbdG8ijE_u7yTWjCRnPA20ZP0Fmr-0biKVC2b6tCnHXAKf4S88Cbv8XFaNFGgcT74FyzDpsvN2vZvK1KhEHAQbDp45H-BTp7Orcmml1TKsV4yJT_da_8gMdmJ3q9n6WW1H8ttt8YSLlcwTe7HnJX45cXEhmLEEXXTwHBL7Zg-dYShL5h8iOAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STaxVcsJZYZYbs8q_J9pAJugogusKMnt_KlQWiYVWWuknLYkHH7e3vfSknjJAwcnBO5fe_vk_AymUkx4hr8z-_JaZAZ0ZpdCGPEltRkNTYMyRLNsy92bKf373UTTwCWjQTcwUUhpgb_6-84YA_GiVBlLpCp3SIRAMnQMqNdWSJGtNUB2q39gQP2Xz_2Vywtby0g219mnvTS1uNcgWNFmTYVfZmOOsTKcOgm0taLYZeWb948fpC_UWr_WEw58BKjRm23-SJl0p4nAHv1VWWW0AIbP5VOK4Zngi-D6rnnAyn0SFfE0Y9mWRE0FvQy2gcda5KDPHhkb8gYg0zj-jNfmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QF9JzWBLqCtMNyykYw2zRNNV5GV10Qac_JmcV0Nu70kNpYkmN_Sqcd3p8JRqDMmtSTViPiasUtwgOruwp9qZUFOEkgJXYxR3tkrji-r58RNnxmYRA0rkIAYdcfFGGzp0Wk9KM-lZrm4uUPgYm1e_QJIFNFHutvffhnfvXOu_EQQ0iBwJ7mdumhY2WTscJTbH0nfvUNeQs7t8YXAyT4MXtTqHIPXKHkWdn38Dh8vIqEKBreTMSUJRaPg-GtpUzOJGOO43jLZuzxCzyk8L2opwPsz3HrqcVDxFaEV1oB0szrWdI5NCWNQ_h_x8yeVmDZI4s25En-mtXG9gnoVRIrl_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=QF9JzWBLqCtMNyykYw2zRNNV5GV10Qac_JmcV0Nu70kNpYkmN_Sqcd3p8JRqDMmtSTViPiasUtwgOruwp9qZUFOEkgJXYxR3tkrji-r58RNnxmYRA0rkIAYdcfFGGzp0Wk9KM-lZrm4uUPgYm1e_QJIFNFHutvffhnfvXOu_EQQ0iBwJ7mdumhY2WTscJTbH0nfvUNeQs7t8YXAyT4MXtTqHIPXKHkWdn38Dh8vIqEKBreTMSUJRaPg-GtpUzOJGOO43jLZuzxCzyk8L2opwPsz3HrqcVDxFaEV1oB0szrWdI5NCWNQ_h_x8yeVmDZI4s25En-mtXG9gnoVRIrl_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3DegLzsjE4wITkmJ9K4MGM3w1qnoiJ-z2ifVLHR85Y-BRTs8YahY85J_y_i80AnychrRCupEK3uyK4dDjiIXwOvdl4YJED0dCRsg1Wpm-Xh2JFj_JNu8Q-bjgcMirKQqVESUJF5Fb0_uVEFMqqYWmWZgnKwM663mllbVfBBARHuEHNtaVKeMmLcgJ0YIq0fe5lHkbPdk4BqOg1JiXYBrvGLRNy5BTbUGMq3e0U15yPg6Hwulih8uP5UmEb0uXKohYZV0PALPbjMgFJTyAmIBgmolywtBtr7iAiC45CXtDCFCTpWBF2S6FsWmgzfJhZpWYaH9zkTLsyaioyaxqn0fg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGKWZdRgfXGcj-KK2_U2jxyY1k2DyYmM7AN6gKqs2EESNaDCG_vUrem44sohO0S8E6ya_y9kAUj1pdym3QD_o83BTBpyMgKdASGhl0Fnf7f2uXB3YjsT83bTyEWrhIyKLcfvyJxqxOwF5kWOTmZmGFFXrx18rzTYNrd-x_iWW4yVNzy0uGm7-OLHNWFCWGPnqB2vSIInD3ajsKGYBPKF5I_8YG_o0Kj0Qf5qDEO82hrt6bv6n1FxXYD-ZuXBWRQhM5JOpCz6UC6HBsqnrh1RtUBxiSn2Y7i_8Um_5ePibNmg8v51gEyMJjLjiZlZEtWv8nj7hEyuvC4q8j1azKnbZ84Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGKWZdRgfXGcj-KK2_U2jxyY1k2DyYmM7AN6gKqs2EESNaDCG_vUrem44sohO0S8E6ya_y9kAUj1pdym3QD_o83BTBpyMgKdASGhl0Fnf7f2uXB3YjsT83bTyEWrhIyKLcfvyJxqxOwF5kWOTmZmGFFXrx18rzTYNrd-x_iWW4yVNzy0uGm7-OLHNWFCWGPnqB2vSIInD3ajsKGYBPKF5I_8YG_o0Kj0Qf5qDEO82hrt6bv6n1FxXYD-ZuXBWRQhM5JOpCz6UC6HBsqnrh1RtUBxiSn2Y7i_8Um_5ePibNmg8v51gEyMJjLjiZlZEtWv8nj7hEyuvC4q8j1azKnbZ84Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=KxxO8e6NGb2MdktLj4knqf0e8_J9Uzi7-Ix-wgIMYu-qhYQRBpp-EdQ1c_WBKL9NDvhIxwUk_2SxZiDXDF6Nx7ZXff7ixK_4JUCocL1kUN9HnsvvpIzWxSW_KCexwDniqpTHcGEoHOeNOlnKM8T1zwbgtJ36OicM0dLyORKTNk7XTiFlFOQ2uJc-jf99LzXMrBqCtrWDwe-ePnJgUE20Qk7Ua6lx14qHUAH1whgTVQtC-KZHTJ3LVws66AHjVESju3i4nRtcyEfZbmZLTWyRcx5fP02Opnq-tf6HTUWVp3ks4SooFUOQ_B7zlC1EXZaqIN1THZ3pg4Ih7JOXb0Nndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=KxxO8e6NGb2MdktLj4knqf0e8_J9Uzi7-Ix-wgIMYu-qhYQRBpp-EdQ1c_WBKL9NDvhIxwUk_2SxZiDXDF6Nx7ZXff7ixK_4JUCocL1kUN9HnsvvpIzWxSW_KCexwDniqpTHcGEoHOeNOlnKM8T1zwbgtJ36OicM0dLyORKTNk7XTiFlFOQ2uJc-jf99LzXMrBqCtrWDwe-ePnJgUE20Qk7Ua6lx14qHUAH1whgTVQtC-KZHTJ3LVws66AHjVESju3i4nRtcyEfZbmZLTWyRcx5fP02Opnq-tf6HTUWVp3ks4SooFUOQ_B7zlC1EXZaqIN1THZ3pg4Ih7JOXb0Nndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
