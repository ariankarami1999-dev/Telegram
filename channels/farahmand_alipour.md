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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 19:27:26</div>
<hr>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG11nrAvuJO_Z1am8f_O0_AzYyqsDCVcRUbIBJkVDCYHPq5QLSQ8p6AFACt2FScVINi2YD8K-uDyb92XwxMvASlVOI4bQsEGXBcA6h-Vxwg59g151wZIlJSmHMeXRyRx2M0RdbcqUtyNtZHoZBclNG-wVuBNvcJOoH6JJ2C4juLqgY0W9iHpMwV7OmI1lMFOB24TnPgK_6XhwrTadFwxxbA1cpoXVFf0L9sjU_Ax0InI-yv6n12t_9-uMlNVevaSbLcIo7fjBskYK4Oo_wc7OI4Wyo3rqBqdhH7cJywUVQi-1-bq0khYgjxd4s_x-8RoZ2hVTIwi1cCM29fuQmLETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwygKbS51-85hBxbck26f6YFpGOL9Yi8JrkoMyNIcXTNv28h77XLZ9ArlWasnxqwSn6YrR1HWYnV1i6M-QBNM9BeGIJTLfDIHe1YWCYj2hehCCpZYBm61m1HVGnoTUCgBrmeWRnpLqsYx5ih_sm8TAQHqfpE0wyHDlSUFSeBjgJhDYr32OFx6jsdUL2Cy0LnDbN47NhbmelZZR88IRt2VZP87v6Mq3su0hx_zIvq5nqWfT-uP2lCWAnhLy1DIi3eJ-Qctd9Yc9qPwpruh5XigUiff-eo1frXB1OMix5j4Y0QB8kdvFoJdFra45yYagNej8ol-tccGeCJuSYIVqv6dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gih06U87ggMC26dTIiZJFrarlSWMWibudfT7NhQftqzxvnlayHDel9w5f06rsNEhhLWYu66bULdURzh0IpnaH_JPIQuCgQJnvQlvsbugnzOaD0DRdnzJtqonzQXOIWu1brfW7XNu461hlqL1XVGsrHi7Yeufkwnh9tS7OFiCA6MMOn1v7uNl1uzX5u0DYZRDEzKgTQdECHQLdTJKTV-aepA0ePeidsMUu4cp6BFEtHxPEHwCx3_8_h2W2uSzae4WN-xKAf7E-9ANDnTTwMPAcDesrH40zytQ7yFHizs2fqISXFjk9oXQjoyHcU9ioa0q7PJksBxMuc7CPrqgnBR55A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ16JGDH2BDsRUnBqXQDctm9Vsm35kdKecGaheZYHNlfKqXXHWPFJZA2WChlz7xpv6iTAhBwo_T0LqDGFoCWUqbG1W3zJ4hbkJNAyyyLfGLwgBdV2N_7A1Bh18ayoPO9OEOUfsB_AC3Ty8q1tSBMc2Jx0f8c3iNN4RJrqolJPLlmSrnFaAF-vTxgR_4YFKqEhsgkMJ-TBkL3d_0LI_ChxdgIN_vns6ksTIeFgrGICLUeCmindyJ-OT2k3fGdxKNNiX1FvxqstOdQBjJ2ndXGp_QLhiI2WHTPHkn4RjdKxPvPSKZQpi56e_w8jcDnrNGXxvmYFrWBGmdS8Sedm86GdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFZifK7yVxqaISzycA4YuaXVjRVLcoUQCBTkOxkX4gLtC4GiQFMDpPYokCDVH2Kd1qW4oONCpA_F8_CBjEaJ0cD1UZv4RarC4TCP3YINeuxT8eGfLiPYC7P9I2Hn-kCaKRCBpYJ4rXp67hqxa3V5pF4lKpcuIs72yOg3Qq4LGSHenX9l7ekwSBj7XRr3TTmZzY111mh2T4p6kJ2OQVNUv_eiG3HDX0GF7u03jsj-o_Q8M27Q8N-5Y1SQwmityNgKgc1eEAiiGkmLNdEfpXzbG0S_HVj0y6CnTXNtzE0E2ScEtZnxh2ySOr5t6dDHqPh_B1ztAkstZoZRZm5urhIUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=iE7ywgwSkf5qbBlBtNsgO8VGg_SLsn4MVsvEp7NCImok9cL2O6fzhNNzUQORNxmCuR9LaSyMO0puMmIW4VzHa-RQ2omn_l5srFMqlxjVp-kKehIDcgfKri-1pxAMlQhNXrSZS9g3lOJ64M23ROjO1fDoo7nsoDTcgiZOyOjp0ukKpKdTSCAgkf2jEq1J8xeait25FCVuUmsdOTpKgSO84b7vXTZLoBAM5QbDSzQKj0zEtUFfRnCnWYkXVrASVFRFvbZZawuw93aE2bo6Fz7u4r4TrSVKqWu37i7Givo5W3ofQ_JtPpOLNeJhtpX9px0vJ6beEhbsihEWfG5dKGqhxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=iE7ywgwSkf5qbBlBtNsgO8VGg_SLsn4MVsvEp7NCImok9cL2O6fzhNNzUQORNxmCuR9LaSyMO0puMmIW4VzHa-RQ2omn_l5srFMqlxjVp-kKehIDcgfKri-1pxAMlQhNXrSZS9g3lOJ64M23ROjO1fDoo7nsoDTcgiZOyOjp0ukKpKdTSCAgkf2jEq1J8xeait25FCVuUmsdOTpKgSO84b7vXTZLoBAM5QbDSzQKj0zEtUFfRnCnWYkXVrASVFRFvbZZawuw93aE2bo6Fz7u4r4TrSVKqWu37i7Givo5W3ofQ_JtPpOLNeJhtpX9px0vJ6beEhbsihEWfG5dKGqhxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HitYXqk4d__cv5Fduyp3TsRPQJfhno4WzFin7uC9VXUqPpx9NEEx_X_0Is5FqguGVajQ7dtN-QkFiWr8tdAM6IhJDp1Hli1Hau-GiN65YR-N7QzGBsbH8pUbdbtHEit8LaT3488Rw-0h6yaF-Z7CXA8yyjRtGIYRnz087_aV0wJRksPGbxF0100Pcr5G6nj0k5W7g4wB-3VMqJqPse2Cp_OOjfLQmi2MqcPSIwzYPtju1YMQO9ze3ZWSPQtxhI6YZUQdvUQT7LGX-dYFS4VjeLq69f28vjbyk-Hh2ups4ZZEfKItkGhLKK89dtQ1KnJn91E4ll2RwXPvEITGsXNqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-wd4pJaBEcfwgkDPnGLHGyknXwNIQQIfEyX9mGSkLGN9kAFMkmiF1lc7hjG0rUZFLBI232BDC_IzZVlDMsVFgaQZpA_oy01FK_Poa6H8eBXh-OragQg8Ws1oE8hvZ4PvaQXXighp7IWvHBqAPhDINGMgN4X7yKkIuvEGXUrQNNdvZkNLYvSZFv1SZUWwvZnW2-tdULPxd2rPRsF2OC9_GhKfD5bjtl3Wm8FdklfJoXSL6xgPMswRlVdBYQT19UTHJ1e-zdnykyYVmgV6AJdaJTfLe6wtZcC1W1z3e9izdu4R4QMV81w6hyZZPcG2gFTu21VcqxDr_TKKAju_ooJ_g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=ev1YRKmOJoGPG8fQtgyL6OcAZtciUPp5Z0BQ8z4N0rF1K5YeDnpsl8Oo-j2-HodgBj9FB4A_JBQUr4tPEgC9MKwvi1hbjhil4rwiMMcok0VHlDtY00WOBgiejh684bHRnMFvSNhyPu09Vn18JlhPsVuV1JobsYtD5WyhGECduJMC1lJw2BUzoKLX0TviC63jTp5j9Vx0WuPEKn8NxA3yLBAWPkJhO8GEL1qV5NE--QYAKB9ZdAbduAz9cOAdGdwihkqWpXVhjmWItw5d_zRRZhO96eGmJWqj79uVqmgJ3Do9ohXvsnP6yqREVteguBmGOw6eNHoXOa3AxGlSxkx-YyAS5oWr65adrZVzmeMxSwlkOUHdKq7dJfMjkmH6JSbrHp6tTCwrk-NEs-ElWvFX7SKr23gu5h008boGVso_bpddPLoF7Edw7SZ9CIjyNk4JlifDOHAkX-QCmzILZsmayoIAmCTWQ58k_YMZoe5z6kgGQjW4H82IkSH8aoapwCChpJO_XQN_7thk5hzqHv35p5SmvwdY5Nwfi8dU9arIKMaBWetV_PX7vT9JuVyzevMvTPzIgq_Ev0IhXeYJJtlCfTsqkKYFeWgjM0zfbhXl91EU--ux8cMqtG8JBreXiWnYUW-wicz5yEZfny0hdHWQaq1fH1G0-6hV0yS_-ZejzJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=ev1YRKmOJoGPG8fQtgyL6OcAZtciUPp5Z0BQ8z4N0rF1K5YeDnpsl8Oo-j2-HodgBj9FB4A_JBQUr4tPEgC9MKwvi1hbjhil4rwiMMcok0VHlDtY00WOBgiejh684bHRnMFvSNhyPu09Vn18JlhPsVuV1JobsYtD5WyhGECduJMC1lJw2BUzoKLX0TviC63jTp5j9Vx0WuPEKn8NxA3yLBAWPkJhO8GEL1qV5NE--QYAKB9ZdAbduAz9cOAdGdwihkqWpXVhjmWItw5d_zRRZhO96eGmJWqj79uVqmgJ3Do9ohXvsnP6yqREVteguBmGOw6eNHoXOa3AxGlSxkx-YyAS5oWr65adrZVzmeMxSwlkOUHdKq7dJfMjkmH6JSbrHp6tTCwrk-NEs-ElWvFX7SKr23gu5h008boGVso_bpddPLoF7Edw7SZ9CIjyNk4JlifDOHAkX-QCmzILZsmayoIAmCTWQ58k_YMZoe5z6kgGQjW4H82IkSH8aoapwCChpJO_XQN_7thk5hzqHv35p5SmvwdY5Nwfi8dU9arIKMaBWetV_PX7vT9JuVyzevMvTPzIgq_Ev0IhXeYJJtlCfTsqkKYFeWgjM0zfbhXl91EU--ux8cMqtG8JBreXiWnYUW-wicz5yEZfny0hdHWQaq1fH1G0-6hV0yS_-ZejzJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=qzyTAXsQduuYQC9AKfXVi8iYEWaMjC2uooY_JOtemHeLOmaIpAZRsu9rCb2RsAqYLRola8QrzXNB-r2MFivH_y6oU9AikPV_5VPBkcls42XISEtZu1gh61MJsp6p_5vF6I0A0wy2VIVvvHzqV9-FL0Vzh8jT3wtbxpc089l6tn1dh_1LbgPH8FU7-iIVzjqMLCKjzL2HStvIUzvG8UU7zWR9lMRdOKRm50WmP01Etf7AzaBrZBOUYuogwLtgApyBTZF_c6AuwK13UBmU0Dh9j464m3K5BsWwrtmMaJX-uoFXdAB9CtGkrK2FUawGJ7sbVenBH_-PZakkuP2hhTpV1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=qzyTAXsQduuYQC9AKfXVi8iYEWaMjC2uooY_JOtemHeLOmaIpAZRsu9rCb2RsAqYLRola8QrzXNB-r2MFivH_y6oU9AikPV_5VPBkcls42XISEtZu1gh61MJsp6p_5vF6I0A0wy2VIVvvHzqV9-FL0Vzh8jT3wtbxpc089l6tn1dh_1LbgPH8FU7-iIVzjqMLCKjzL2HStvIUzvG8UU7zWR9lMRdOKRm50WmP01Etf7AzaBrZBOUYuogwLtgApyBTZF_c6AuwK13UBmU0Dh9j464m3K5BsWwrtmMaJX-uoFXdAB9CtGkrK2FUawGJ7sbVenBH_-PZakkuP2hhTpV1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouHJ6NjkR_RFPZl-MUwBgZdDEUXzOV-hS-TjvgA9IB87uHUTccTYYjAHvzPnFdNT5uSFQcVBOUW_8N5DQwjpz_JzdZ5DGqxOUaHehxMdYD0wUpnzvMygLsGrDaWw3y0UXsxAd84QA37ORi6ZXfAbtI9GUVSS8xeXobWYQmuT8DHAAi0waqWY217iIsThuI9dPSkf0YCZVsJPMYx_ULE_SEXNsdcdF6uxqiB65CQ4ulEmSyqJk2ac71nw4Pwr4x87ylJhgPTHmlm6Ow8Af-hkq6pyNKjNHMDVXwfoXgdWHkA-l5W4EcKkIIdQ-szgoSvnrZzqFwLgtq19stktizknZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix80jaWivx1fID-rfXDUyu51Jayxfxzluu34PbtM_qixRq282NMx_N2nr_htcUu4p6xSWS1_6BjMH61YheCx-gIrpLzcqO95962kZyCVdQo0xhJfSgePg-uvUTOQjez2Kt70tpkSnDVL4FoUd9x5UST9o-sxqrRhUsLS36CvHG8-hTgE11gIITWIw5QHTJZkA1blt72d7EbR_5427eTSk3-HSiS_qqYQEuZnLS9Oz_kr3Ono8eX1Mi2FqGOWAw1qDAvk9suzQw7T5S5n2XQefd0CFHnZAtmVfh-mlX-H5qGPm4YAJPkKNUxXUkgEEhZH4PLnByHcb_VjMEx-wuyS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFni_23she7JnfeoQ91csVSC62pnd865CZB8myOl0mn56E2CgSSBuUEIDTuAJ_w0HlcXub-tXiDMiNm9hOkXEBiBPh783QeMM4IQzFCHmMX2dbq7bmdER5jpeH8oz4pOT-xityx-0naXQH1tUwshjlVZOZHULfB7Rpp78qX4sGJbko1Z3_VloAsZecXSpuHWxzLofrWKYnagJBDF0GZNf7T7sv6bBxOMvba99Q3z7NLmpOHJFNtKJN2cHYbmgibyHHQtcamtUq5hOHvQ5eysPuOx6oa-mDDyI1uyAfwABtNo-TePFJ1b4xz_FfQ4Zuy4ePl3ZhFzqgy53V-Z0mM9AA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ke2eJfy_NT7bb_ZqXPFVK24PvC4Av9NPc1USeTTveSLWSUHXGtQzhqc9vKQbY40Ggidc0f9vfdWeNyqCZlKnx4NE5MYvrhnKCOV4GfaXQ5wViUrlA2LxslWyLrUhVcMPy9sGpYsQBYezwX3XtKj_LvOtEni3A-OUYdsSnl-Rk0YCqTHsXF0pjAFSR1SIkY76tgOQ1Y2bt8qNQoEuo0tGdmIPL7Vmn2iOdSwFtrdRw8EXPPM3S-9Aryms2nxiy9p_TTXGndSRXp7VUAg8dNrU8UqNQXsHefcflEmvUbXqNP2zvXeU7-I5jwOsmvWZ_n-RJOSwC6FTB3n4YuGAhEDnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=ke2eJfy_NT7bb_ZqXPFVK24PvC4Av9NPc1USeTTveSLWSUHXGtQzhqc9vKQbY40Ggidc0f9vfdWeNyqCZlKnx4NE5MYvrhnKCOV4GfaXQ5wViUrlA2LxslWyLrUhVcMPy9sGpYsQBYezwX3XtKj_LvOtEni3A-OUYdsSnl-Rk0YCqTHsXF0pjAFSR1SIkY76tgOQ1Y2bt8qNQoEuo0tGdmIPL7Vmn2iOdSwFtrdRw8EXPPM3S-9Aryms2nxiy9p_TTXGndSRXp7VUAg8dNrU8UqNQXsHefcflEmvUbXqNP2zvXeU7-I5jwOsmvWZ_n-RJOSwC6FTB3n4YuGAhEDnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddaR_i-ab0pY6abWXfoqf8U76o1aqHseZA_S0FlfjOMkAkNCohDaL5yevr3DcW3H_sNgjPHC3DSKRAdghJBtOZba23rwGjU9tYAXDhxBdf6obZrJZAsF-Tn4kqng6G9QYgSQj5cyu8CMI-7Nvaf1hs7oyCIsOGBV6rTEplZuNhAPnk3g_v7CQPFTz-uEcH0zsyhY1wmOPsPlkBOhm_YoH30acGWgbL2qfLwlm913gdktOloQ7X9gf_AuFVSNeNCiEWtil1wHXDPKCbV1ApuGHjJp06hgWqqbRSZ6FiHaXM3dSVthoM1d-iiB0874al-X6dgJn7gsOTMDyEq-QGWWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzVqHhe7ivQ8d53sYyPZZZToIe0722VkARIhiToahUt7h0VkYLOU4FDTCn0KOq9n95Cn7jC8pfkClDsAAn7_LwEoX2oSl-BvxAyjhXC8B3We9qojA0z2gFRa7JwlGSQpXzlDX_Y-vadBemtDPn1EjDddaC2UN9F8NSrdfCALztodHA-66p4SHK0WbcU-7xNW2GADY__J0pjBKoTP1sY2sJKpYomnG6K-T7f6DT3fYo6NyU3P3jzauZnhpTXPDLeYsTpDBF1OYFqRCgBSFcI-JgtyCxMdFPBe8J_D9CGR96xa3HLn6nXbLtyVtm2xUmp_jMnPBl2HRZrjK6ZsSOVAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abvgnLzVgq2AyVZzMFeJnovFU-nLBD3H-kSEcKw66dKdYuGeaGpUlTlS1VKU6wC6doEkoPmkj1OwhUtNUbNgIfoGl7djxzb-Rl-HAnHg7u1LLOgDxZGe74lWAtdWsCM9w1SpopMKgT6hOH2wG7fbHb-DVSq7KJTPtPtmEz6UUU5gYN7A9CVsHg5wFpRuzYdJPNxzeFB2--S3_ei583Bpc6bN3EijL-9nxVA5ySqPzn1BL8_QM5ydXHUtX7RNXcKV73ERKj-7v2_MwYrDwHmRkgGcCRIkT-sxIPGBXvrSnLd3Do577TZO1cjeqPEQWx3_fbQ37W7Wr1zLOMjK2qMhkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiimVVu-8wAMrSFGMI6T6TE3KOF0-aHxUSuvXNXNI5oFCESTUp9U-wu94BZIK3dIIV8XtiBPoPh3Mum6QldG46Ld7-LkArl0D93s-Df2G5Xcvjqd77FzO-prKln-7jjMX-1O3zxQaoj4yBbRtTqbLIH1bMtpuCAByWknat3wrvtl1jCrpdVD74n5YrpvWPJ3tqsvbWjG1UhHHZ-dTj4ij3LiLxqTOBOh4ErRO8cpWjZtBj0lnPeSfydWj5t3V9G9n_9lVk4u-a1Fz5cm0UDd5k-N4oWUd_Qzap3JPAVqPTLtvTbc46b8Gq9AnXzSVlGFybQLHGx_wYBv9lq8ZP9WIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ZVvpJtcFqm8HFIfPYMCd43fvIkOHj_AV9uzM5Lu2l7EFasPDsSYccrD7Je_amCdu2vBM9ivwfkFpuDZLaOzbaN4fYobx4ASsTEw0VyyaSQ-6GnhhY6hqWEobxQuXUiZWI8TaIncWaJ0YXVpYiGF-tZwc5cBCFVCSkH7TVzb3_6vdvkzKgCcjQKfX--MAjvZxJ1PGxydrnINsyNMEk464LWDcSksFqgvOfgUwWdRotxvK645BpyTDnEDZbT9WxuvVzcYOmEXebI3xws4fyXIEpodNCDCjfMDADGIqHw2uwqks7qe3yCeLI5vUF4etfABe6u3ppw8-tc5xgIQ5RtoxtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=ZVvpJtcFqm8HFIfPYMCd43fvIkOHj_AV9uzM5Lu2l7EFasPDsSYccrD7Je_amCdu2vBM9ivwfkFpuDZLaOzbaN4fYobx4ASsTEw0VyyaSQ-6GnhhY6hqWEobxQuXUiZWI8TaIncWaJ0YXVpYiGF-tZwc5cBCFVCSkH7TVzb3_6vdvkzKgCcjQKfX--MAjvZxJ1PGxydrnINsyNMEk464LWDcSksFqgvOfgUwWdRotxvK645BpyTDnEDZbT9WxuvVzcYOmEXebI3xws4fyXIEpodNCDCjfMDADGIqHw2uwqks7qe3yCeLI5vUF4etfABe6u3ppw8-tc5xgIQ5RtoxtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=JcEOljf4UjNVD_vb9E7nhpDa6C33JPuVuHHN2rrdCMjKQbaF_U7slm_F5z-E2GQ6clETB3A8sqr7D6nVf966ZdtdwUzpXPib3Q14Nl9vBfRSFEH_flj8ePqNu3T31-Dn6g-R5hwOoGRaFQ8oiriv1yscW8HNKa_BCe6diyP-_LAkNZQcpM7kzpS5qDEUmRscd5FCwkaBAIw0qOaihpMXTDtTPUZnBdMosvCgLfzb-YCxDM3mDE4JFjRftxFg3LXqb9TmVnW8yZ4FEoixG65K58KyHW8y1ZHg79aX_ipXv4jSSYjIfnP-Q6AWksuCa3N5AvMp2EHge-JiFt1E4KTdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=JcEOljf4UjNVD_vb9E7nhpDa6C33JPuVuHHN2rrdCMjKQbaF_U7slm_F5z-E2GQ6clETB3A8sqr7D6nVf966ZdtdwUzpXPib3Q14Nl9vBfRSFEH_flj8ePqNu3T31-Dn6g-R5hwOoGRaFQ8oiriv1yscW8HNKa_BCe6diyP-_LAkNZQcpM7kzpS5qDEUmRscd5FCwkaBAIw0qOaihpMXTDtTPUZnBdMosvCgLfzb-YCxDM3mDE4JFjRftxFg3LXqb9TmVnW8yZ4FEoixG65K58KyHW8y1ZHg79aX_ipXv4jSSYjIfnP-Q6AWksuCa3N5AvMp2EHge-JiFt1E4KTdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=OLy5Qkpp5bFqhW95YcEPjRkWGl5OGI8ic4HzmHBJ8pxzQ2kTy3Qbx2J4T2uPW_ZXkrGfi56tqjHlZqorMwmAWMBQhZnYUmr8I94TGqjLPcqJNmlE8mIFBhZ3dSJnJEsNOgGKJ5mCGwFPtwpPsZ82MiP4SlX_RHzn4uGdU4enLLVY-Z7B5b4PNuFKwzVImjZ0bgwT0ynwKShjT1KPITwqhiW1PpJyVegRnC7Dg_9L19wFAUrBP0TXQcdneAPSK-qQ4Akr_EVyZseMIQ3E0Hf0_nftaaEGG9Z_p9P60miaOqKQA5Fg5JIeyibmHPOmGMKJWMzVUNnhwYzywa3f56XWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=OLy5Qkpp5bFqhW95YcEPjRkWGl5OGI8ic4HzmHBJ8pxzQ2kTy3Qbx2J4T2uPW_ZXkrGfi56tqjHlZqorMwmAWMBQhZnYUmr8I94TGqjLPcqJNmlE8mIFBhZ3dSJnJEsNOgGKJ5mCGwFPtwpPsZ82MiP4SlX_RHzn4uGdU4enLLVY-Z7B5b4PNuFKwzVImjZ0bgwT0ynwKShjT1KPITwqhiW1PpJyVegRnC7Dg_9L19wFAUrBP0TXQcdneAPSK-qQ4Akr_EVyZseMIQ3E0Hf0_nftaaEGG9Z_p9P60miaOqKQA5Fg5JIeyibmHPOmGMKJWMzVUNnhwYzywa3f56XWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Ni-dJd6SjdmKeEI4KDJKn59hPVS3txbGDpKIpJy2uXIb_twBivn21KdLRi372jvZkQSx0Ngpj2GJuPrdgxUjMUBThFgChL2ab1A_KkREXlaum26r2AoC_siTGPXbubR8DDLblAawxBSwSirsQJNJJrqJUeb-UG2VQ5KrlUDtLMD1_CBdbfT23lQG9Nkmf0RFJUSjKFnHKv_IAw2rsXQR7Nl89ML5tDe0NyanT2V-Fg-xhULpuG8S0b_erIzokWtAp51JuC7oy8E0e-iOdEQFk6ajut5jNbJvpT_VJ8JTAPP59sQu9hUP0dr5zy_C8KuvnZW66B_-MUwkZf9CLi2_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Ni-dJd6SjdmKeEI4KDJKn59hPVS3txbGDpKIpJy2uXIb_twBivn21KdLRi372jvZkQSx0Ngpj2GJuPrdgxUjMUBThFgChL2ab1A_KkREXlaum26r2AoC_siTGPXbubR8DDLblAawxBSwSirsQJNJJrqJUeb-UG2VQ5KrlUDtLMD1_CBdbfT23lQG9Nkmf0RFJUSjKFnHKv_IAw2rsXQR7Nl89ML5tDe0NyanT2V-Fg-xhULpuG8S0b_erIzokWtAp51JuC7oy8E0e-iOdEQFk6ajut5jNbJvpT_VJ8JTAPP59sQu9hUP0dr5zy_C8KuvnZW66B_-MUwkZf9CLi2_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JipKxWec9KE4E2nIAIkk6xcJT92a3xG_dMxpENsPPs-F5klAjaPE77Y5Rn2yJRnI4Rt5Xk0wkMW5s3nKbn6GHPgFIKKcnPrAqhwobih5a5mLKLzKltCY_Bpo_wFBz0gCDBvSlEotjBvQ5mLihEKerGIq5NYqGZfMY4h2joxJUq35fDepoSguUglscULgmvvVnf2ZoqX-bl6ch_A_5L7mloViTRSEZZp-sBqV0xluLaXpeI21YZnGeGEysqeLxIv142CEhbl73foIgDyiKL46HGb7uYHhrqXAixI3jAXGnjonwiLxKFHBnLxZjOmMxD_P1mkpSpjCGj8eCFARoVNEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=JipKxWec9KE4E2nIAIkk6xcJT92a3xG_dMxpENsPPs-F5klAjaPE77Y5Rn2yJRnI4Rt5Xk0wkMW5s3nKbn6GHPgFIKKcnPrAqhwobih5a5mLKLzKltCY_Bpo_wFBz0gCDBvSlEotjBvQ5mLihEKerGIq5NYqGZfMY4h2joxJUq35fDepoSguUglscULgmvvVnf2ZoqX-bl6ch_A_5L7mloViTRSEZZp-sBqV0xluLaXpeI21YZnGeGEysqeLxIv142CEhbl73foIgDyiKL46HGb7uYHhrqXAixI3jAXGnjonwiLxKFHBnLxZjOmMxD_P1mkpSpjCGj8eCFARoVNEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=szi5yMeFOs7r2q2NY1X9PhaBSQmVzUZClFSpNhZM5I0qZFQtqWJo8Egs4wdltHGXZTRyvHl3YrcWQJpwRV026lvRhxo5gnf6NiB_nQU4izl5fkDliYgfSh5iI5C9a24lbh1R164moqQ4JQr3hEoaq9uhBsm2xJ5d08Hv2cgxTDgZ0ymXPDcaPG95CZrSeBkXVjO2SjZNl3QdxY51BrUikxZNRlwcef9rC4OOqb-WdVHpxDicV81DBM9Wei2IUOwYA0R_vEeeFFeRA7nDutaRd00CMWl3TrvgfAzltwJSJK0V8pt_KI7l-J7UF9tPFeEvMBysgSUn9RxKTVQvZVVULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=szi5yMeFOs7r2q2NY1X9PhaBSQmVzUZClFSpNhZM5I0qZFQtqWJo8Egs4wdltHGXZTRyvHl3YrcWQJpwRV026lvRhxo5gnf6NiB_nQU4izl5fkDliYgfSh5iI5C9a24lbh1R164moqQ4JQr3hEoaq9uhBsm2xJ5d08Hv2cgxTDgZ0ymXPDcaPG95CZrSeBkXVjO2SjZNl3QdxY51BrUikxZNRlwcef9rC4OOqb-WdVHpxDicV81DBM9Wei2IUOwYA0R_vEeeFFeRA7nDutaRd00CMWl3TrvgfAzltwJSJK0V8pt_KI7l-J7UF9tPFeEvMBysgSUn9RxKTVQvZVVULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=dks6PPx_pvKCeQx-6x45XjQkHM39gdEHhVpXqm6ujNGP5QkeHV2OvzJroT6tdkUwCsOMBS7vP2CDMJav5DekqMIx0PVGvfqwW0LbsS9gc94nNxG762sEGzqeDTlabD0pk2AY5pU4ylzlUbsWRuHH6WMisC_bFeEaNT5qGSjJX6EXJsn4zbHguXfR51VqrnxTwwHr6PE1j2c3g0mWIng2VdUbJ2HAomxLozhY9KHv-Eb1bL5LP3e6b0kxfGA1htv9pxWzQG6ZA961jZHlklOLf1nIdMMA_fjSlPMbe9eUXo32aAHYGkIv3KHxboAnhOIjz2XayMvAnxYvs4I5oG2SoWahI9gxH9XhyKQhazYN_LY8ogBbASAnoHCsIJWKbjs4FRhOVIToNdsC6Q5YbawDyzsQ3ITwV_GT_RHyP22U_ISlIjHH_MQFi6549ljzIOwVHv33P5PGOsMlR5xZj0WL7Oq9h7cjeOb1gSMP7zDP1eLSm3dhE4q7mmw5OLdknLF3O9zmC3KA6LZqL1lQDCUBTzOVm1uWqwh25OmQWvBXNR_s8EI4xzUTGCXi1lZokwIDxfHmsb6tlr92kB8FYfJBTEScezCaZAB53W7ZDZ57Y-WVVqloT7tqqJbAvrmt9pMRVQ9c6JZAzjWF3mxrmjwzMZzXZnLsyjxGSovLW5rlJvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=dks6PPx_pvKCeQx-6x45XjQkHM39gdEHhVpXqm6ujNGP5QkeHV2OvzJroT6tdkUwCsOMBS7vP2CDMJav5DekqMIx0PVGvfqwW0LbsS9gc94nNxG762sEGzqeDTlabD0pk2AY5pU4ylzlUbsWRuHH6WMisC_bFeEaNT5qGSjJX6EXJsn4zbHguXfR51VqrnxTwwHr6PE1j2c3g0mWIng2VdUbJ2HAomxLozhY9KHv-Eb1bL5LP3e6b0kxfGA1htv9pxWzQG6ZA961jZHlklOLf1nIdMMA_fjSlPMbe9eUXo32aAHYGkIv3KHxboAnhOIjz2XayMvAnxYvs4I5oG2SoWahI9gxH9XhyKQhazYN_LY8ogBbASAnoHCsIJWKbjs4FRhOVIToNdsC6Q5YbawDyzsQ3ITwV_GT_RHyP22U_ISlIjHH_MQFi6549ljzIOwVHv33P5PGOsMlR5xZj0WL7Oq9h7cjeOb1gSMP7zDP1eLSm3dhE4q7mmw5OLdknLF3O9zmC3KA6LZqL1lQDCUBTzOVm1uWqwh25OmQWvBXNR_s8EI4xzUTGCXi1lZokwIDxfHmsb6tlr92kB8FYfJBTEScezCaZAB53W7ZDZ57Y-WVVqloT7tqqJbAvrmt9pMRVQ9c6JZAzjWF3mxrmjwzMZzXZnLsyjxGSovLW5rlJvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=mSM4RqyXfkE7pjkdqD9HfsXHilrsq9pd3h6BEzhjADZmhQzIwSYpRXkckZGfl4BlF3jUPdiBqlhgFUY0hTea84Mgnt5a32PeQyC8S_O126PJ7cvaPALz70zfNR3C4-lniGCm7ZsWRN3TdSVtoUhxhdGsidpVL0rrj2pPup_tffC7fpviwH1344jXuFATCE1jmhYaZ3uwXGhWhC2vwHkRAWtF8TeFs7adKvNCKvaDSjnir2zRNTd4AaCI09xlxIi1YosUcJXZskYm9VdSQPFPAHIRBdQNODbS6L1w8Kh0sMNDMmugyoEWt8b8LE6PEsrGwZsRM-tAvSD5jDKgmolvTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=mSM4RqyXfkE7pjkdqD9HfsXHilrsq9pd3h6BEzhjADZmhQzIwSYpRXkckZGfl4BlF3jUPdiBqlhgFUY0hTea84Mgnt5a32PeQyC8S_O126PJ7cvaPALz70zfNR3C4-lniGCm7ZsWRN3TdSVtoUhxhdGsidpVL0rrj2pPup_tffC7fpviwH1344jXuFATCE1jmhYaZ3uwXGhWhC2vwHkRAWtF8TeFs7adKvNCKvaDSjnir2zRNTd4AaCI09xlxIi1YosUcJXZskYm9VdSQPFPAHIRBdQNODbS6L1w8Kh0sMNDMmugyoEWt8b8LE6PEsrGwZsRM-tAvSD5jDKgmolvTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XwI2pZ_o74NKKlhmzCGUAX7QspY2o2G061yh5XmE8RqGnnraqpc6NlhI7c2zsXVvs0pUQYoL4nXewPPge5X0xbn_hq-Rl2_8Xh_uKzgeI6PYyMANqr_OpWhUHWbb8AZ4QPggvbz9yxMwzkOBPwC1zbbOJqIpyd_OsS-BKaJJk_bvPl7L-7Gb06Aq6Kel7dVS9dKRYz_y4JouiGAWAGSilkwznD78JS-AyLtbaycp0imZ5N-_RmffD1lH7eKhnc4OoTGuuZB0G1xlLHlyXYLoEFo7PjSGqFnsPJ4-_ARshF1yXxoWSkC8v8_GTBPTAcwPQhlh6gCYDkV1v82RINovFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XwI2pZ_o74NKKlhmzCGUAX7QspY2o2G061yh5XmE8RqGnnraqpc6NlhI7c2zsXVvs0pUQYoL4nXewPPge5X0xbn_hq-Rl2_8Xh_uKzgeI6PYyMANqr_OpWhUHWbb8AZ4QPggvbz9yxMwzkOBPwC1zbbOJqIpyd_OsS-BKaJJk_bvPl7L-7Gb06Aq6Kel7dVS9dKRYz_y4JouiGAWAGSilkwznD78JS-AyLtbaycp0imZ5N-_RmffD1lH7eKhnc4OoTGuuZB0G1xlLHlyXYLoEFo7PjSGqFnsPJ4-_ARshF1yXxoWSkC8v8_GTBPTAcwPQhlh6gCYDkV1v82RINovFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ8r1tKEzo-w7LxUaAPehlQS0sGKTfEWDM0EQt3WFvIotS1gpY1OrkubmlGwrRvtsu2svRmzCzNM1NeuHcB1NaSBDkvjXvqqC_rl8BKw48Urur9kQFncL1Fdu_Ns4l90knf6ds8FdiPgdJk4rQOJUEOuyLWD0_nGhZFtvARTeG5UUeu_XQurFIn-41VoNIMjxMKTnp_r08yLI-FJfOxDwErACtGqKqQ-BbWjIwOVnhIf3LcVZjIYntesPHyrqYSLiVjUOgbjsFWYgQCFvoq7t6U043NrkdprEREReSrvKzulOzsrmW7bKVgd6CS3RExngSd4z__uJKLXARfKHlqclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlAh0WRLjhVZnmQlJ7o3cDKYFXFkV-67QKicZPa3thIDBPnL5r2aA1JCsh8TlBd-CJd-qYtdeKNa-YWxOmMYYjAH5sXtyJkHgaCMWxU19IS3DRbhLWnjXGedJfiD-axBe4kJ9UUk0_24dqJD0kbno1c8LaAf9F_XekWFwVEPykAG6G6Dbxeef47gA19LlJd8EAaMV_u8K7ZXLeGMShHGUtlqltPITRZYXs-o8mYpl8UmlwjMVXiel2tLY_h0NxaFYBoH8JwAlbkrgTh9PCIvMxh7dZGli91WGO72YJrcgFmbchfacTmGzThsABlVFC8aKW5y0Fk3f_nxzchUwlPkpg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=bxZkmJYMQ8k3LCUMsALK88DywhB-bOb_7wCnkY__fSDJL4ZRNujYxpptZGSU0lP35Vu1jskgiau376oWId_fR-aYtwuy9MSFnxB5VnNZwb6O8mJAm67MZGclKmvmiK6GatirYbOG296DifNF6x1lhFtKwDYx71FO9SdzrF2dPjj4t1uJwrnP86rALLmj7f3no7JYUmhq54F2JNkmmrXr4llmh8Dj6p0nfquMVbEIoXlbSXDfdEyqIkkmLQnvLDWDfyOx-RsmpOw6Aj9Sr3uKQNT9tJHdPnjPiRN3zgHLjLdnJqs-kHS7SWUn7lxTV4L3x5vEZ9Zd_IgV6r6r8u7AionzOCFFR-8R9ZLVfQHwrI5RPHIjqXm2u_Ze2e9PUN7tKHjDyQN_SyVrMEKfcoCQj1Vsx3aczT1mRTOLzA2ITJX7S5KGZ-RD5NnQ_5lKArS3bvAmq955y3T_SnDV65aPwQX7wtloyXUYoNX16ZJU4ZWNPHBDpZ50H0wDYqau2WOtAQJ5vo5ON1tY0xdgDxWpBhhSzbOu0esLJhmDFL_N-uEwhfubHNQbyjO-_-BuH6q2gXUA9-3ZN-PZEFil3JuaU0v1i0iJRCThmeM8FqvRAlNYvVWHQEuDCBjS15ExXN8tgCdaXiEAJtQcfCiHFuNsKoMGSDVGWa_JHpuXLPu4JZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=bxZkmJYMQ8k3LCUMsALK88DywhB-bOb_7wCnkY__fSDJL4ZRNujYxpptZGSU0lP35Vu1jskgiau376oWId_fR-aYtwuy9MSFnxB5VnNZwb6O8mJAm67MZGclKmvmiK6GatirYbOG296DifNF6x1lhFtKwDYx71FO9SdzrF2dPjj4t1uJwrnP86rALLmj7f3no7JYUmhq54F2JNkmmrXr4llmh8Dj6p0nfquMVbEIoXlbSXDfdEyqIkkmLQnvLDWDfyOx-RsmpOw6Aj9Sr3uKQNT9tJHdPnjPiRN3zgHLjLdnJqs-kHS7SWUn7lxTV4L3x5vEZ9Zd_IgV6r6r8u7AionzOCFFR-8R9ZLVfQHwrI5RPHIjqXm2u_Ze2e9PUN7tKHjDyQN_SyVrMEKfcoCQj1Vsx3aczT1mRTOLzA2ITJX7S5KGZ-RD5NnQ_5lKArS3bvAmq955y3T_SnDV65aPwQX7wtloyXUYoNX16ZJU4ZWNPHBDpZ50H0wDYqau2WOtAQJ5vo5ON1tY0xdgDxWpBhhSzbOu0esLJhmDFL_N-uEwhfubHNQbyjO-_-BuH6q2gXUA9-3ZN-PZEFil3JuaU0v1i0iJRCThmeM8FqvRAlNYvVWHQEuDCBjS15ExXN8tgCdaXiEAJtQcfCiHFuNsKoMGSDVGWa_JHpuXLPu4JZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHNnstDcCxxVRg9lYPG6JZ0vIttloCN5bzYAnpt9JxJCnRS2GeLK8X2CDHU8sHGXTj3sLkQ-5PzIE8fLU3sRZw5ggkK_BWdXr-6g5Vlgu6G0PJLImo5diGSJPBBd4rDnaTErgr8Qqo-DXyD4bDdGkzpaMuDCJIjdO9hI-WppCwbJd8dchpM85se-GS4jBULMtXgRUA1QTnwNhRw-rzIpoKIvKVADbwCwjOd6Q53YvHJvVodzpfBBjiq6AVk_86Jyyh2ZH_Ut1SPpqyW0XiXmYSU6BnOE24JF2LTUXFkdTYHDKuw3m60HxLPoNobGzImntVnxa1cafFnjFJACcbZ1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC-dCOvVjguuIYyb1JsdS5pfurgj5vOZOK9fSWthveO7UcFtBcb4ORCHIJjRPWGohBXoiF2OtpzsxZgCI5wBX2ZjVjCfesmRA8wDLpUo91VyTd_OWfKJbxcA7DhCFEimO2TErQJ78VqdAgtn8zIdCRXx9G3FortyaFGlFofyDz7nYDs99SYvionAkJQep-XP4KkCU873O0hpms8zr__VDu2cunAWTLabz7FKLDryN8lAm4Uw7qnozTcehVR09LgUTMbrV2bemQTpDQ03S72b1lUKFLzTN4i6wvL11xUe--Q4-m48k_6oFye1hHOS1u5zai0liC3Ivyjf1H2PsuIJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBSDgbsxmCOiaKMdJf67Swy1AL2itoi9HOLFxIxuuUBSjCpWE_63dqqoC0jnVgWi5ji-nbEhrf2uULYxabwzCUJowfweppxab-anS3WmhzoOdVHQ8YQuPgh5ZRmo8hzjwgSI940drEwlfOwZ-tJqTvDo_909W3yckK-tkjAj7GZRdIWA5F1lmOqLdbYMONTNk5rkX5hujE1ShKBMe590ibboYyaATby2f_H9O7gUu9T_SdRH_mlesC1hDQeRcc9vtYRnTpMyOnPwPxqVpNd1kHRhpawhWhXRZxcTXdOJMtAs7XdavqLfSuECHxUpkrtqhhq2GHf2h1UXq0zsfJdj1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTwVj1QyK5n7dDEpTUOYsiJM0RCSqh9wx5RhLNebTmRK2-VQNvqxrFv2lvtC1LzTqCRRN7vycFGfLvv2NLH8N7wtvmP_dLrfhkI7q3cOqmmZU1pGVE9PtbZF42RI20EHZ_R3VDXj_lbft3V0Jl4l-g9p-RoS0ymKm9VAHQvCZVaIbvdk8AuJOG_YK_QoE3Be0DkKVPf-0Ui90AM6Bj_YGZfCdd-MSD9EQ5o--WK8mfM-0WOFtGGajY3sc_n-loFt4_BeQceJ618wQ37GdfXJOKk9mJ0cBInrRZfbXJ-6rzL25DIuw3l4tkGI6wquOPd9YQKjs0ZB1RBvFZq_y4mwQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=c2jryyO6amL5_v8M6BhFa6xL1hW0X0HqlCAKGAV08h_rp4ckRdgAMPmIaT8fQ1HIx6z7qDYQMIf76_yOL_dfPcrcaWWSx5072KauySH-Dz03miEsuyCLVy_qXEJMbB0ibhxeE1n4pWA0s4fg2zjBaIruAMlbsXU852oF8HbTurCwzSMbcRQXkze1q_-QA6msS1NyXJ_tAsmImwPUP4WIJphvuWbJUa6W-MtR0BzawjOnvtLgbfnNl2uMAguZgZdnd0V4_p3g8L4W63V-maIQBh4F-mOcXEDa0JYa-8htZY6Mv29fHaoIOHDKCORmd64k3nl58LhtCzqP-12PcoIafCEpZxMVzyC1R6WaueRvUouC9c2BQFBV9F3Ay2tRtRv4OEF1u2A8uSjRutjgKZTLJVWdEIMnIW7QDoyyHiUlwBv1DuWyde_bEru6itVfgGDf7XWIjqtR2N7W-eaxZuMPL5onJkkF6PWzMLbubzGKlgO16_VAGaX56z6-MLrsM5m5XYLrdyk6s57FabPh1wwOY0r4CFKqYXoUlX57sgyzuUpOzUTSASseE1Q97f8GQjBdr8mkT0MnbAUCr_vYrMIwweG2vT6evrCUm-xL5uavAdsEoGKJ08sc_7GOSarfJ7gYCdYws1Oe-icfoqStpT4R5dJ3YNwm5FWokrt1hxv6uCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=c2jryyO6amL5_v8M6BhFa6xL1hW0X0HqlCAKGAV08h_rp4ckRdgAMPmIaT8fQ1HIx6z7qDYQMIf76_yOL_dfPcrcaWWSx5072KauySH-Dz03miEsuyCLVy_qXEJMbB0ibhxeE1n4pWA0s4fg2zjBaIruAMlbsXU852oF8HbTurCwzSMbcRQXkze1q_-QA6msS1NyXJ_tAsmImwPUP4WIJphvuWbJUa6W-MtR0BzawjOnvtLgbfnNl2uMAguZgZdnd0V4_p3g8L4W63V-maIQBh4F-mOcXEDa0JYa-8htZY6Mv29fHaoIOHDKCORmd64k3nl58LhtCzqP-12PcoIafCEpZxMVzyC1R6WaueRvUouC9c2BQFBV9F3Ay2tRtRv4OEF1u2A8uSjRutjgKZTLJVWdEIMnIW7QDoyyHiUlwBv1DuWyde_bEru6itVfgGDf7XWIjqtR2N7W-eaxZuMPL5onJkkF6PWzMLbubzGKlgO16_VAGaX56z6-MLrsM5m5XYLrdyk6s57FabPh1wwOY0r4CFKqYXoUlX57sgyzuUpOzUTSASseE1Q97f8GQjBdr8mkT0MnbAUCr_vYrMIwweG2vT6evrCUm-xL5uavAdsEoGKJ08sc_7GOSarfJ7gYCdYws1Oe-icfoqStpT4R5dJ3YNwm5FWokrt1hxv6uCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=de_vVSP24EDaHWCygutiP593dGtb8Xg-vEcPQhIUSwCuIX5Xh2atTJn13OvthNatlRE5MpudsW7y4rdA81Tm407b-2HSPL6Q09tALstlhHXqdsRvml8K5kshficvku2QkD4ChJGW7b1JOwphXLt7mMSFcnoj9inPuI7a1YDQhoiHDRUgxCTKSTwyFUEo3pD8r6L81HDL5Qe6s92K-gJ4mQOUb6799pgX3t2e8UdIegpPMozM40pX700mb7COOAbeUpYyEQ7o9kfAfPWCyA7v9SqYYR2NAmfcMelztTL_zJkbRQp0Bil_2oFb5AzWvCX9RpdiCIQUppwVjMzYWZX7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=de_vVSP24EDaHWCygutiP593dGtb8Xg-vEcPQhIUSwCuIX5Xh2atTJn13OvthNatlRE5MpudsW7y4rdA81Tm407b-2HSPL6Q09tALstlhHXqdsRvml8K5kshficvku2QkD4ChJGW7b1JOwphXLt7mMSFcnoj9inPuI7a1YDQhoiHDRUgxCTKSTwyFUEo3pD8r6L81HDL5Qe6s92K-gJ4mQOUb6799pgX3t2e8UdIegpPMozM40pX700mb7COOAbeUpYyEQ7o9kfAfPWCyA7v9SqYYR2NAmfcMelztTL_zJkbRQp0Bil_2oFb5AzWvCX9RpdiCIQUppwVjMzYWZX7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijRxtC9Du81Tj_cB2y9aCMGuJsPy510mpLMsbxWypUtKTTV4jIkaPjSy0mZfyd9QnoB2z24fckPwseYTlSid8GOFaROaxe3UWF4NYKeIv61TSAl11fX4e4f_cg737kwU6yMypNkoKsotQ6QDa5LSFHzWdorrDvE8WgIleZtbzG71a396n4RAyypegke4rWrRvV_hXEtGgr9MpKyV4tBF9val3lkq6SFn145WZftLkDbSGxWHCtQPK-vG63Tk3hfFD0NJbojOcdI4NqPQUI8uTR0LpJoIuAO2mUTsyYjE2d8FQnJ0Dnwp3ChQvD1DQRq9FcT2Zpb2z7eBXTbmBM4QzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep75woukyLWml8w-bF5CUssA1JE17c30SNYPvJAiD1KON8QhPC0tvWkrHeiHMh1VTDjfXHKauzTZ1zmrTM9OABz25dsufCZFM2rIoKN94pzCNBztAQcvA-9msCexgAUkGLJXDvOCltn3PgHyolEL1KS4U1eblbGrGdh0YnbpjNkt4ZjSSbQf4ezAhRdAPUFO1N_DgDcN9_4lzB5SkGL50UIOCO1Zg48Tgtna_axs-yICS5cdNlnb-xMlqOm5A_jLmVkiJ98QI9XW85m0Z1lk4L3of-HrrQ1s5D00l_O0amOza3Z6DOoXJbi9gnuERlpU5hn9eyaJ6OeSJqNl81lQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFTqAGb_RszokCT5jh03zfzDGZMKpNPyqaR8FfHhsY4S87XqfCcA9RyMSi2G406YAso2kVGX5IrRuO7aEb_XxTtXUzNuUxZEBOt22Zac_ClsgmZ7ISR4VCyOIKnMPubDYKfr_DwAg4XbTYotRzJAWVKIe_442JpajTGQHWNQ9OJi5qsQifqxcATF51cuvt5E-Ua9cFjhlUtZ5x9eKky4bzGGoB3ItmoE1ulIPi1E2_iXPz4TwYdZAls7gEKvChl0g5Kq34Iv-WXzRLVjBTfNhQ2fUKK56MVqByAjyqxKOPWgD8R4DbV3t-WKF8abre5qsXnpsNe-ymYeF7S1oy5OtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDch15WbOBCCCWCwn0GQSSlqG3tYAB4uICUpzyzkQdMamvvSkD4dBypCznvgO-8owPPAyFuMViaX_5ikg2-4djtKlJ5Yhh12P08qKLurz9j6F6BB2eqDPmXjEzFXpUlT66ea5NmMiTgFD0aMbFkVvRa5PilY_pHzK8pi6PNDF0kYlIRCDy1QXzrieUGxzJDnWjWHGq8YUIK-vU_Ah-uuyBGBHt1AWvtXmBy4P1B3yaPqXDW-wKl9GPVXrWanb2PlyYp2XBMkxPCNvf2odsYA7RNAHJHu9f-OS2hKmyaMoPONL9ICC37QTe7jaBEXGm6KFemSNF1shRQlll7gQ_EQ1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_6U4mTHdGQ8iVVFM0RNgrEsNRVQbmSfOX7o-_kunN_UvzKuHhpFFRhNvQ_-nJxTxp5ZGfmoj0Ria3TWUcApX9K9_LvyHRhojsfBUoNAb9G7hZW5Pt8v7W6CZWS7STEhAoY7b0bFteXiOAiG4MFxJUK1hCUZtJWg34JnDNspyS219oCSG9cGlC1DwIaFPaCefoZ3hM_nqRcXT2AQiHkknPHDKLwC3AuRA_DMLwUppxrolfYPfy_bTJG-PfYx_hbyZ-gAHAurOPKrcsnIyStT_g0joQBQwDmIyT3g218x3FBNFBDDBE3E-54-3a7-KI6f1sAoiKNijUJrDEbAq9sIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ5UaKr6d4Ll75eycHWjWV5L6FsiSeCeBgzAH2CoksPvedJccJcZSNMD-ytC5vNyLw6s9HPUYb3EyJVZpNtaGoeI-7PfbTt2LnBLZCnnsq8amokYrUXvS-EJwuj59_e2Wmz1DaFUed3qmy0ZRBDZbmspCmcnmhPzzeoHmvvqG37FfGe-BTeAQSwo6FHMptSrHZH-1Z8UeBt9c_-VJp9EalxUx-H8g5x3IUR9homOqIJe31RKRcXCtcGuV5Xqv_3XpXiprnkKVrJsC9FSnVqKSleAQPw6CWcp5dmbMoALDZtRCwUjhgc8DB_aZ5Hqk_f7S2mSaZytiLT1G0nN28UwDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=VzOLtG-jp-fBu2clpltdE38sfH-LCixeqkCoOFKLQy4Vb9k4Qq6elulL8eSsX2RdDzx7jXcsFCLsoqrLW-u1Wmm0fOBSYZw1_Ht7nndRNDWc3nhRmkPiKM8eHFDfbm7AV2eKs58cEihwvWwBDRFM9lt6WXdNNQJ4dHMgUBLUe0ymKp7UTuhKS8bCVpNkLwxW2r6lju_Z5WTL3Q-QwgI-rfgabjbB99oHXLtuTzEMpnBYv1aX4BJoLA-YUQwaWKop1FvKA5Q9Lxl1sXUU4uxZY9Ya-W2f5Es9ZV0zcVpOLkFkKEl26b0eZHGkDVWLjEni5XxXLddfoPgfYW5zNAtZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=VzOLtG-jp-fBu2clpltdE38sfH-LCixeqkCoOFKLQy4Vb9k4Qq6elulL8eSsX2RdDzx7jXcsFCLsoqrLW-u1Wmm0fOBSYZw1_Ht7nndRNDWc3nhRmkPiKM8eHFDfbm7AV2eKs58cEihwvWwBDRFM9lt6WXdNNQJ4dHMgUBLUe0ymKp7UTuhKS8bCVpNkLwxW2r6lju_Z5WTL3Q-QwgI-rfgabjbB99oHXLtuTzEMpnBYv1aX4BJoLA-YUQwaWKop1FvKA5Q9Lxl1sXUU4uxZY9Ya-W2f5Es9ZV0zcVpOLkFkKEl26b0eZHGkDVWLjEni5XxXLddfoPgfYW5zNAtZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauUgxNhO4w9HB_I7gyxhskVpNEEd1xx8TYQAhkrE0nR1QSuOSJDfYYruk_tct6IC8KmbpDnAs9fM69m19rRDy7hGhuC7Q6dOJnrvYgVS9nDgzZBBG2NqyP3tWdEj6WdfAlwasExlAC5eBCD377k00DFzlydpxXV12xeFOGODWexNy79lQ2HhJXWO_XL6jHvK4XODjnN9uOLk8mBYp66ufMzlWAxYPb8bfBEMfQRMOgnmr7wjHGi2tfb5KKknEjKxQPBSF845OqUsBpExQvJIuO7DbvHss0iyFzMsusCTcEEe2gAYPF7H74fobNgRjBqw5ZHqbVhalV7_tIZVdvOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=lQ6JwhO5yfNGPQL6o8glBwn6cxOW5fiqCEiG00i8CuNYzoCP6YMhTmiWIqFyVLvGQ80zdkgRRcSz9aMDup-dzm5hgiTykmjjmIa9gAeRJvJnU_il6UOdZh0B9-VsE_sNaWfbPwDUymrctS7r8mmdPr-_pAe8tVrPS_x95kd1wSl8sPcua_FXW1NlLXUJj11uItr_egCFSOBgWLfnijKszb6dNPvUZEVU-em5V1V10g5C29v8E2HPLuD-oFu4bPlx77ibVr6GVqcg5fbIOifKevssqb1PEaXXoaEGk8GMsVAHdkSVN89CNr0jU9W2HXuFYev1Rq7wuGrzM2VYG2JggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=lQ6JwhO5yfNGPQL6o8glBwn6cxOW5fiqCEiG00i8CuNYzoCP6YMhTmiWIqFyVLvGQ80zdkgRRcSz9aMDup-dzm5hgiTykmjjmIa9gAeRJvJnU_il6UOdZh0B9-VsE_sNaWfbPwDUymrctS7r8mmdPr-_pAe8tVrPS_x95kd1wSl8sPcua_FXW1NlLXUJj11uItr_egCFSOBgWLfnijKszb6dNPvUZEVU-em5V1V10g5C29v8E2HPLuD-oFu4bPlx77ibVr6GVqcg5fbIOifKevssqb1PEaXXoaEGk8GMsVAHdkSVN89CNr0jU9W2HXuFYev1Rq7wuGrzM2VYG2JggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGZnGH7aXnX8KWsRGuR2iLXSWlhvRTBlfoJloH_XhTSKCDII5JlTzXm5EeSsGDNiIkXjFq-HGR0S4AkEYq4Uxwx4kgikxP_mZGkFgukHUe7oJjpmT4rld_gu88iStJZyE5Mg4D8551TZ9yWQe0Bwar1v5LF5tRqcq5PeajFJfNhPNNehfo11fWjjs0JniKSALtDOkfbAKss2IUs-QIYOkyeIcelTneKJ1pCpTv-QAmuttlR6pjxXAD6ys7NRopsGHid82yCgCy6dNdQgTSDPCj79PuMnZglgStuwFVfWHwDi2_bF5iOb0Mrq_lzOHVqiU46j_KTAoKv7HpuhNsAtag.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFAZ_HkEstfFjhAGLTJfDs7y7BhajYTRQFprFoWjitV0vnTPG5Feozd41OMoqH4v0Zmce6OSuhopxd4q0VjCRh1uBapbGKR7iaLflT0VS87WOjlayNCz9hPkPyPNpxftINUxzWvSoSxb-6YZNQ6oRSSD6joqkt6uRfVxMnc0SuElrnWEFRC8lsydtEo2JZ6mZvoTzWBuG4isnCBIaPEr9enCCcdfAnS6qzur3KdqWc6T06r6FxLMKUK56p7YPCO1SYo9qDmtwZseVnVY-e2nrfC8uSTTXTx6VI59-PPZjEx8QmdPIdXcPYJ2flpVHD3wfFOGeCqUTSBavFQ4dOgBbaM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGFAZ_HkEstfFjhAGLTJfDs7y7BhajYTRQFprFoWjitV0vnTPG5Feozd41OMoqH4v0Zmce6OSuhopxd4q0VjCRh1uBapbGKR7iaLflT0VS87WOjlayNCz9hPkPyPNpxftINUxzWvSoSxb-6YZNQ6oRSSD6joqkt6uRfVxMnc0SuElrnWEFRC8lsydtEo2JZ6mZvoTzWBuG4isnCBIaPEr9enCCcdfAnS6qzur3KdqWc6T06r6FxLMKUK56p7YPCO1SYo9qDmtwZseVnVY-e2nrfC8uSTTXTx6VI59-PPZjEx8QmdPIdXcPYJ2flpVHD3wfFOGeCqUTSBavFQ4dOgBbaM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qtnp8EKUqzxu-0J2lmlJCYznaaV_-lroMyqVqS9vvqAwROhZwITq2B6Gc22agk61r5e0ST_BG91Pzlf_O4mbSI95-6sT2l8J4ezBDSwBfdnRvM-QBMh0riJ1-JJmDIEDin1-d4o61cboWEtQy0L2XaJ5aaaxmDmM2Zm4-KJenGh7zUF2UrFNuyr36oRZjjmx0QECNRF5HA-E8gu7h_VouDhzpqzEeNDcpzWdDfPRImqzhB1tcq5gV6WNiZ-BaNU6VSBs4iE3r-y7lKLsQI9Edv-6m2ple3dmdFJzjlyNPgN5JyJqHL_FNUknjBjHnHAk9Nx_zpZLQZ4ArcmF5YT1Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=qtnp8EKUqzxu-0J2lmlJCYznaaV_-lroMyqVqS9vvqAwROhZwITq2B6Gc22agk61r5e0ST_BG91Pzlf_O4mbSI95-6sT2l8J4ezBDSwBfdnRvM-QBMh0riJ1-JJmDIEDin1-d4o61cboWEtQy0L2XaJ5aaaxmDmM2Zm4-KJenGh7zUF2UrFNuyr36oRZjjmx0QECNRF5HA-E8gu7h_VouDhzpqzEeNDcpzWdDfPRImqzhB1tcq5gV6WNiZ-BaNU6VSBs4iE3r-y7lKLsQI9Edv-6m2ple3dmdFJzjlyNPgN5JyJqHL_FNUknjBjHnHAk9Nx_zpZLQZ4ArcmF5YT1Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
