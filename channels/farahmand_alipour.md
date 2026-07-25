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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 16:44:49</div>
<hr>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-jeEznug_Krjv9k741Jp2_TC4LGoanmlPaV5f612wqPzcVtrE_094gCQlHaeZv16IieCsgWjyQbfTgybH2x1ca2VL8ZcLO8jcg_NlnRFBaHUhgFSJvx15quZqztipHXbRDkUUOHL1M_dYk2337NxmjVva44lpHhGU4BIoQW-qKn-ydFirRCy6T2-hpoFOSE16v86QNdrgf8at7SqcLjbW2UvZ_rWragvbPFGp3yWXzydYT_InO-EMi97JKZuoURneR-EJYfYkZGuGjNXxovDCaP4hXxL3i7TYAFCXJxzC9x_jzlVWkiS4Lwp9scxhjKU3Eh9zFOqhqlYpQ0--EN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjUnMB-R60QdTTB0Y3ma-6XuWJWJLsxEkgWKrhp0j5aeIftknCsozVY8Y6MNIlsCZ828qBaHjyM6fRiEJO70V0DZl2pxdicothX4SW4eD7dEnNnannWTblrneO_xi9YfdMJPN0oWfY_vNgU6ghzEJBv9lqlSq49SpWIgjZtLHO8_ni3JmLtAxvUOK6jHfR5J_aCflgJYrkiYzPHkKoxWtRWTNlrTErGPW6qKB97cUkR80K6jcPfWBHkD76KlST0BMpNNLgKwQwsOqsojbmQLNXUYJQK9PW7LGYhDywsBj_LxvLSRH9RDHAqU7461yQ71gZXPb-_8JXf2zMPBgRPfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwAEgmP2NJE_x8SwC8Z07M5aJ39ObcIPh8ewLWToOI6NHHXSXqALvX07fk977QtaT6DsQK7ZiXUi6PWYws8Lyx8A4FJ4A8XkEtOVq5iSaoSfW7HP7QeaSaZ6R4XSJbsOX6qpS6ENTwzzyvOPCPdzNHAUYdMC5FhID8TA0XmUVydG3T5G-UX8P_9U7konlt6MiNtCYWgD7sqKIt3sEyFgQqhTjgb3XtnfEM2AeUg4OtyjKztzFrvazMeOC3Zf_kMO1pxj6YkjhT4pjZS0bKm40y88iQL8j7yDvim_KJTJ1d4GhLr5PW0jIBM6f-h4oFci1NZcUQnFsMWZjiGAhfF3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=PW15CFS-CGDbI9Utd9Sp3R8KdTfKLOTpfe5sOXpczDXfMx6ad-hPR2tRQHiAWFpWmsdCoPnqQn3d-u7NW8j8z6HKNRFdahJ2Gj1Cutd4wil4KBgQURhufsFv97hV3DpuozCO73k5e-dOjRwU9reZ0v-8dZ88FDL7Thfh9t2e2YG_BFQog4ih3GpF768CEbmoXW5z5x-yZ1Rz9SEB0El2GcrlvkN4VkQQCltMVFqJCyF66cPheCL4B3zR8rEoMOWncI3wMEf3WgiZLOqgbkZt6GqZScWi1rOipUsCQR6Ni3ItN8o0QvSERSuF2GkTCXrhk6hY7zr2pwWqbwo76NbLIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=PW15CFS-CGDbI9Utd9Sp3R8KdTfKLOTpfe5sOXpczDXfMx6ad-hPR2tRQHiAWFpWmsdCoPnqQn3d-u7NW8j8z6HKNRFdahJ2Gj1Cutd4wil4KBgQURhufsFv97hV3DpuozCO73k5e-dOjRwU9reZ0v-8dZ88FDL7Thfh9t2e2YG_BFQog4ih3GpF768CEbmoXW5z5x-yZ1Rz9SEB0El2GcrlvkN4VkQQCltMVFqJCyF66cPheCL4B3zR8rEoMOWncI3wMEf3WgiZLOqgbkZt6GqZScWi1rOipUsCQR6Ni3ItN8o0QvSERSuF2GkTCXrhk6hY7zr2pwWqbwo76NbLIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA20GAL-3TBC1Jbl1LtXbli2FI_LDxOJpRPAI9wcWwuq78IuIRRob0_eHF4wf-35rWLOtG16XpL9Ku8v1zNAcQ2vihhP666NYxOIsP1wKlIih0tviblEuI_G30aS9uuMxlG8_aPd4S-bZSxNe-lEHdnDlX5d4gnTyTq1bCl_MVdR7EMNKbV5RAygljGNqVC4QlworPR-NgH3Th2-weXVMDSOFnXSTZlb1lXg2viD1VYqV3obo-U6-yw8u0mI_y5MUyTFrwaauIFo4Y99jYaUak5cJr3-GeD8x6eosxvw2RQ4k_SJjPFL4lrRoX7QvonSqNbfjql_3UPP3DB1H1PEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p14M3OAxWdb9slAUaw8hJ-7WnZlo9J-2UDx1DqFr6eEn7fft5mql5DTtgMqq__HEWGPJUzPG9gzUIUqcLwIfqpjlNOQrLsgOwv_hzT3RT9a5SYWWZotUTxF9vSkR5flSU-zOuUPCpgjTLmFwTBW8Txh4GhjJegQu5SnhsFlj77dgkpc_T_kCROrPPgO-dBESKAvihszyikzzFJWrWqKFaxeLVf1-Gb75I4w4Q_MOkZOVALqfMwzbkfZGlBQuJMtdGW4tUGZpfx7_fxFO1SBZ_VxTmLwTRj0JZyB5S5hCIdmWiaZqMyLYXRKRq96hNsFvVX8cLJwVBtp0DIRWJaedQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=SHCY18HCfKj2lSHj54T68vMQyI57MfP16QCmhEUro-TgSGrGgSB_PK1muk7XOs1J4_PPUfqcT6vR2MhvOGXs7AqTj_Mg3aFNCgJuRQ1V_UcRWuNAKInviTKo-SxWdz9u7VK2r5od-Nyqmcj52xDB5Nais7TqrEORBWnFgInaflymkVT_EZa2Sgrn6y1Ntg_JqyxgmOwx29luCWJPH2kQj0G5BkwYLtD9hv0tNGvcZYqyz7cv2oW0reAlV416E3ir87jqt8d003lfm2E0nvPsgyw97DrM-gP8cOf6QpLYO8P46-in3mYdwpwfEABLkbDn9jruJorXLG-TARrx8401wqhuPe21JePdP3FZ7U-8DXFMl7uv4Zuiqe0KcR_TGsqNb8JcYGBJ8yRtZqdnTX3fDRVkZ4-qIFGqcvZt2j5mLJPZbauebN6vGFD8iA5WzWXBXrHt-vshBwQp5nfceIdNWO8yVp-IID_O2rtXxZDfunplS4RhREuzmHOXA8ormVA50m5FhdK1iTHOHxYucZIK03kipGKbBSSXbxcP0UnW71OsLM9nBr0MZOkPE5pQJ3BKdgZ95HooHfqyh2fpro3aTODYUNJG9uN-_dbuCiNl9JQOO0GI7ATpWiXB_ExPDDIY69D_5k_DEfpiHuy6xCftMUysMelhRuR3E19AP6UxjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=SHCY18HCfKj2lSHj54T68vMQyI57MfP16QCmhEUro-TgSGrGgSB_PK1muk7XOs1J4_PPUfqcT6vR2MhvOGXs7AqTj_Mg3aFNCgJuRQ1V_UcRWuNAKInviTKo-SxWdz9u7VK2r5od-Nyqmcj52xDB5Nais7TqrEORBWnFgInaflymkVT_EZa2Sgrn6y1Ntg_JqyxgmOwx29luCWJPH2kQj0G5BkwYLtD9hv0tNGvcZYqyz7cv2oW0reAlV416E3ir87jqt8d003lfm2E0nvPsgyw97DrM-gP8cOf6QpLYO8P46-in3mYdwpwfEABLkbDn9jruJorXLG-TARrx8401wqhuPe21JePdP3FZ7U-8DXFMl7uv4Zuiqe0KcR_TGsqNb8JcYGBJ8yRtZqdnTX3fDRVkZ4-qIFGqcvZt2j5mLJPZbauebN6vGFD8iA5WzWXBXrHt-vshBwQp5nfceIdNWO8yVp-IID_O2rtXxZDfunplS4RhREuzmHOXA8ormVA50m5FhdK1iTHOHxYucZIK03kipGKbBSSXbxcP0UnW71OsLM9nBr0MZOkPE5pQJ3BKdgZ95HooHfqyh2fpro3aTODYUNJG9uN-_dbuCiNl9JQOO0GI7ATpWiXB_ExPDDIY69D_5k_DEfpiHuy6xCftMUysMelhRuR3E19AP6UxjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=DH5t-bjBDy6gT3gDfLbvLZcTgU8ijUUZ7wvDVIHuIjEzDpZu_F9MWnAEte2LZrUH5bvb-OwbeVTHBnc5-BuL9aMGuPTOwB-bmPMareRnuMXzcgvzRI9b2sGQQNnLOu5maaP7re41izt0gfU9O5Zzo65nNPYdNOX0CkbtG6nNaYMkyCQncMtwpAN1xlohtrlx8w04_6sNQ_Cfk6CVZf5sHdORRgSFYpOuQXS5SYqgIwxo3C8oXVKPmx4Fr-GwVd4ZLqDE6vbzb-g7ZFMu6MO2Z15ZvTGWO2JzVJ1AObJtKnOspa3LDaXpIp-W9Pf9ARgGyXPp6CA63dC_ef1F3AF42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=DH5t-bjBDy6gT3gDfLbvLZcTgU8ijUUZ7wvDVIHuIjEzDpZu_F9MWnAEte2LZrUH5bvb-OwbeVTHBnc5-BuL9aMGuPTOwB-bmPMareRnuMXzcgvzRI9b2sGQQNnLOu5maaP7re41izt0gfU9O5Zzo65nNPYdNOX0CkbtG6nNaYMkyCQncMtwpAN1xlohtrlx8w04_6sNQ_Cfk6CVZf5sHdORRgSFYpOuQXS5SYqgIwxo3C8oXVKPmx4Fr-GwVd4ZLqDE6vbzb-g7ZFMu6MO2Z15ZvTGWO2JzVJ1AObJtKnOspa3LDaXpIp-W9Pf9ARgGyXPp6CA63dC_ef1F3AF42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmO2qC7lLv3tDJcr5dz44r3eBlfUNWOFc53xRc5CYE-oH2yJDzRzUGPYjRfDLo3JqnpketSr6hBJzbjNiPi-oFfYUgGdgf3lPkV2oZi830RlGLC-UMzjiAoysl-JpS4ExD0w_PnU7NguMffSaaychwMU-icnuHYULfN0EXeV4GyPZxGrxrTc74yA51l369oZYFOoC_VtdJrRvyDvQtt5wHXEZEsg3yTjLMjli5siZ9PPPPtPd0_VdT_lM1vmuKBBHUK6JSsKda2unbg0J7WKFdfvj6UBJKPmp_rVD5Q3iVetIn3ntbVeCm7fkSW9aEKkUI0C0SMlJGSykMSejLvJNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy6CvEM6LOon79E94oBvvNzID2vptZq42S_eKJ677BiCrZFKxH5mf-W3ZEhj2uDWlXLSHL53c1wyyLRQX1CXoWUK7H0XP45j2GStwu9OiyYjgDYkoCYDEwDo_RQCLVpidh3qGnYSjvNqaFBscOueYevTmxi4YvcvLNRIrMjpQ3cEw1amjqMpUFXLyqTkpySFMeruf4ls8NQOsMK8fboPB0gpDM4qaWdmPIldMPGDxpgTuxJRLtl0lJo3hStXQnwdnurw1oOxg4XKwHNEsD1MFTFjqhIcw0ZfQDDwk7O3XsJ-oWwh8Vybyb5oebV13dljMHcMNelpu3Ok_HgOMO0qbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiQlZIg8YGZTuC5xgq_Gf2QlqpwXcpxhLa9FOy5FSpJaWnIRkUkqOgpZjj2Heagf13sPOqBxRP6KuvCcCYu7V3xDVWT7nl_yg2aZosdPiZdORpZ3cw7xZ8_qvb2sp9tf0QG0vCoYP9GEBrSJlroBVYb30LMj4lZrPv0RVbnRmlK9nFdrJPCY3JtBsAjvR_epiSC0aYg28JQfSbwWZdy5k5BlWXnzifKhmWs_ZJdobckt16T_1D78_U3zEHamkVbuLUwq2rYR0OgG6JQ9pfM3YiqubnO6XA-iEsq8qREa0viswzDhYaKTLazr9YWDiTplynR49L2cgIxGInqcC6TL2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=AGobxc3VTzH1FiRjpEWrgtPo3m_YRhowtra8Y-t5MIIvvSDvZANH-E-Y3QL2UJM5yTG6O23-UQqIpnUuAP2QyiIPdX8RtM8seNiskBwhBeyqfFSI4s9_FHcPdQlrdqJkOaP81MGLPBkmUnnmXA-x_Izi1ujBFAXUw9r0nNDg-R1Revahh2Muu_6vs9UZF3Q0J9Wc95WpVvD74b4dsRcUAnXVyWKWqSdi20QDYPwf9hgKA_lyRpQVTp0UlTqdry28EYrNnkHGMivHIaa3efCTkTgJaOThJqJ7vXGIF5x-3BrfVbmab1DXCotYua_64NYUmxQ57_ydBEtMAMjECQgr0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=AGobxc3VTzH1FiRjpEWrgtPo3m_YRhowtra8Y-t5MIIvvSDvZANH-E-Y3QL2UJM5yTG6O23-UQqIpnUuAP2QyiIPdX8RtM8seNiskBwhBeyqfFSI4s9_FHcPdQlrdqJkOaP81MGLPBkmUnnmXA-x_Izi1ujBFAXUw9r0nNDg-R1Revahh2Muu_6vs9UZF3Q0J9Wc95WpVvD74b4dsRcUAnXVyWKWqSdi20QDYPwf9hgKA_lyRpQVTp0UlTqdry28EYrNnkHGMivHIaa3efCTkTgJaOThJqJ7vXGIF5x-3BrfVbmab1DXCotYua_64NYUmxQ57_ydBEtMAMjECQgr0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szFge7YgUNHEjawm1PQvSYZk5kh0dAWNykWkGqy8V6_tXuA0YswRaut00hOMIHwBRZz221dXrUg_BMHu83r76j9j88kIuTPrk_0yl6zJkyyDw0NWeXwGbdYBtFZVioAUCSDXj7a-R4HzWYAKu8nzzjbcuxU9--An-qwJKgKfb3262CNHWvBTJInIkgklwepEZ31vijRp6N7qTlql-ixAPcSaR9egC-3JXrzrkK2qT_7yZcSszHhvEWogZD0fmBH3kaBW3eofjqcn-MetN28BwqgX1FfV5zUxRSXHpxuYtYg9zjIXXOZa8iY8mgspIwNt13RqMEypMvms88YziWLjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUVj85f3660NMdkAQ7ZNudanL2q9xIplT2mtzi5XdBIQhd4PyrXk4QE7OvtBs9vy-Vy5eZDmALanniPU7VjWCGqgjAYnvDt_UfCWoh_m3AJhSHapQPJKB8DQcJygqD49EYiQtzN56bMWbTXuDl6umZzSI2QtuGZmVDwu3yTfFH3n_L3GMQbjD-GL09N73d4SbjIy3A1atk5pb6G3DIvZmWt1WOf3P_oCUbpriR4viz-Oa3RF74tMOWDBOrAQu8LV32qQULtn0t3GZJyEb3A9Cjtbg8QwLntYPSAJoaCV18BkuqDG-X2CsMvueBRlwfJVYKVGRtv5eP8wS27TMsrBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBp09RgBrpWP653jEs_FprJXN8BIWgTiBtQtiqHPeLDsVEX6gC1qu_VrwBri9bMEKV_lH_yvsX8YqaOcEQPDNFn_VTME3dPT0D6F6HnyH1hoUxO6lMnuH7JC16RWqezVc9rpDHwECM-ftrN96RSns_uZ60wjP-7naoC38bK4mXR9_4hY_9DzSSe_duKkfBXr-7_OJVgEdDTqpsTRkL-cO8JnZD5PuOyn9PIUyTG4XM8_JD6hIlnoPzy5P2Z8aLUHEQkvQxUw7ZDXM95JMpZaJm9-R3CDWEN-7W54TQT1prJT4PD6AQnCtTtQY0eff8oBnvKw0Uc0PAKApZ5J55S9YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQlKAlDsJ9ditoi7ACKnNi6upIBUK3PLss-sJEsTsrX1TncMqcHOjDN42cMWJicuG3PhRpw6ft7dx_iYPwsmciFRyWtcQ1t3nRGiE317AegDQ3X5r73Rb9bK7F3WIIyWMNM3oNRoL-H8xEdzl0dWJ3awujy1TfCspPWBiO9pFfPz7fH_UTBTMm7oePLreoj7ckQ4rehDD40TxBvgaSId4ChYhFxZCEUJ1tfIcSP3dUdhXrpn9ULiSVlL2Oie817gRT-NJvleVamRfITovO7YcT54rxzMNzAGlGGnDl3ezxY7CyaI6afoJPN2nog4JcUMkEyNy5zwVAHMQ9XS1RyIWg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=rEK9YoMUTxkJ1FvrQlqHtkPd785TxvkXCVWXfvv4cJnj9ZamcfymOPMu7ow6PbeK4qZMTwCUhUR4iJYWhlK_QhKlR3rzGzclMPl0ziNquwlzCRzJjsdDlsjzgSr3SbYtT8yhCsunBOno6HU7KLMHlmXEUBsls_O_jOMSsYkxNotOVNSXTVTRVbtcD_q5vJxzlZIU2EYgXZR6DwvKjqU048YBU-IUNziZYC7E0JfCc5GoiS9Nn04zaZOOpABfEWSCb919YRZzwu4nkYsvSo1Djynjpr2-LTmFyhXGR9pXYXaW1cv5s-i1Ob-TeoKhqNvNquH3X4YWsk2WnUISxzJoMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=rEK9YoMUTxkJ1FvrQlqHtkPd785TxvkXCVWXfvv4cJnj9ZamcfymOPMu7ow6PbeK4qZMTwCUhUR4iJYWhlK_QhKlR3rzGzclMPl0ziNquwlzCRzJjsdDlsjzgSr3SbYtT8yhCsunBOno6HU7KLMHlmXEUBsls_O_jOMSsYkxNotOVNSXTVTRVbtcD_q5vJxzlZIU2EYgXZR6DwvKjqU048YBU-IUNziZYC7E0JfCc5GoiS9Nn04zaZOOpABfEWSCb919YRZzwu4nkYsvSo1Djynjpr2-LTmFyhXGR9pXYXaW1cv5s-i1Ob-TeoKhqNvNquH3X4YWsk2WnUISxzJoMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=crgBxOLcpfVZf_B_d60sP9PfOZMHNcofQ5YYc0uwuAbOe33DltVWrqD3Ru6BcRJjxnAbtDaU9_l4ZgpWegQ28Zs8sJz_5g9thJRw5MmTHCxOrMHyxtR2kmQSiplSMXvephYc35Jz5maW8i6MMqqmcUfLQcbEEn2yUMyO6a4fuT_E_2k_1YWxWhnnZHWgkp-7vwmXkOKSMRJLSnvawhL_2xXTTVpng_6lHpzQs5a4vw6bNMAmRQlAm39-GVqJFkZL1JdhvIp5qIjrXSAIbrFUrI2xPNs3OHZ2lDB3vTtZ3H1oU2i2c9CfnOCDa11YKMba5_Q8OWLWaYn-PQUE_YEh1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=crgBxOLcpfVZf_B_d60sP9PfOZMHNcofQ5YYc0uwuAbOe33DltVWrqD3Ru6BcRJjxnAbtDaU9_l4ZgpWegQ28Zs8sJz_5g9thJRw5MmTHCxOrMHyxtR2kmQSiplSMXvephYc35Jz5maW8i6MMqqmcUfLQcbEEn2yUMyO6a4fuT_E_2k_1YWxWhnnZHWgkp-7vwmXkOKSMRJLSnvawhL_2xXTTVpng_6lHpzQs5a4vw6bNMAmRQlAm39-GVqJFkZL1JdhvIp5qIjrXSAIbrFUrI2xPNs3OHZ2lDB3vTtZ3H1oU2i2c9CfnOCDa11YKMba5_Q8OWLWaYn-PQUE_YEh1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pndBbtvSc28pxKTdFam02x7MVaFLyhv7D_mDh_xUHEUSsNI9AwQK2eaeo7Rtcq4PdoYUIdhah8pgVeYdqS34ZLjTG8CvJWai2tYdacl-OW2Jnv4mGrAwiWvEg4tjKsveOLj_Tr062WIgFbr3D3Ljj8tsSxMNY2UtKuJAYbl-tyHAWCyg129ffMEE1o3hkIF0Wu66kx7vqEfz-ps_CuKy6XcItWxjs6s0j6y7e6ZENc68mr7hNY0eeEGpgfKAKO2ssFGKiZ2_09yHo8oU_bf28ScESmic43dnTFIHkflCycOHVQZ--3HFJZmeeZyWShSakE2KFl5iwwSiMOJwJpDeOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pndBbtvSc28pxKTdFam02x7MVaFLyhv7D_mDh_xUHEUSsNI9AwQK2eaeo7Rtcq4PdoYUIdhah8pgVeYdqS34ZLjTG8CvJWai2tYdacl-OW2Jnv4mGrAwiWvEg4tjKsveOLj_Tr062WIgFbr3D3Ljj8tsSxMNY2UtKuJAYbl-tyHAWCyg129ffMEE1o3hkIF0Wu66kx7vqEfz-ps_CuKy6XcItWxjs6s0j6y7e6ZENc68mr7hNY0eeEGpgfKAKO2ssFGKiZ2_09yHo8oU_bf28ScESmic43dnTFIHkflCycOHVQZ--3HFJZmeeZyWShSakE2KFl5iwwSiMOJwJpDeOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ0Hc-Z20eyzCSowulr0PVM5fUa6b89US71j5dyfCHTJUvEHYPX3PpAel97IKdk4rRrbnDy09Daw0vO3I6kfg_dvFkph1E8dAhurXgf5Q_Tg3pFc_PiWpi8Rm-LBlf53i4eSTqNx1QCpdK4-E4IvUxnMYpDYD-Pg4p3KAdPWPS0tduSv0Zp3BcdY9ejtdulOnsurE5Et7asJgADm5nW6wXp1xZdAWLfIDdwqqcJhDuvurxpx75HzNKb4HQ3Lot-A26DWmPk72op4pt6OC5f1ATBHtWPglRMqvxu0aJbQwDEVrcnQvDCJTMVrI_0AJ6toAxESfB6UHASASxJ1_SO7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Kjtwwp8CQrAUo6ORsmBeo-Kvyqn-H2HPU2EiywdtABtdYJ0fL2d5dqNys0vDTF9yWYYWhFdkMVL3Kh6rAWgkUogoXe9Ni1PJ4JkRoqBoXn0kC096Ckza95uPezPIaPX1QHxmkjZCxt6iUsF0_ZsDYKYSfBRzowuaQ92OBzJNEgq23irzl7siMa4QvPzLqIrgQeoeFVCHM3449VESyCdnPVBL8zID3foB4Qd8n8R5FUBDLkLcdSnd9lEXacb9k2LlAd0gFRPsCdGsfpA73usYgrNqNbwUwkRllvhW6w_LhOGyynPmibhYp8j8l3JY5qOXWfhcMlVGSqwqpH0r8O8RbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Kjtwwp8CQrAUo6ORsmBeo-Kvyqn-H2HPU2EiywdtABtdYJ0fL2d5dqNys0vDTF9yWYYWhFdkMVL3Kh6rAWgkUogoXe9Ni1PJ4JkRoqBoXn0kC096Ckza95uPezPIaPX1QHxmkjZCxt6iUsF0_ZsDYKYSfBRzowuaQ92OBzJNEgq23irzl7siMa4QvPzLqIrgQeoeFVCHM3449VESyCdnPVBL8zID3foB4Qd8n8R5FUBDLkLcdSnd9lEXacb9k2LlAd0gFRPsCdGsfpA73usYgrNqNbwUwkRllvhW6w_LhOGyynPmibhYp8j8l3JY5qOXWfhcMlVGSqwqpH0r8O8RbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=sGO6hxLGjXS8GW2r2ItjD8LoUnlVY8dz156qfnq2ESQnWiQNTQJp0MPsmnY9xcSE2LzAhdiDKcC3hVDHNU8j7kQQnMsNKxmA5a80zDbtjZUxcqlRyq9hfASSpolvFr-XI4MKUqohvGY8Me7kjpvEM7_mkQF_RBGuvRFC52NNsVZXfZ8Vb_9Qbh8WiEc1HdawELAdFTqq-2V9f3aSi52Y1MC6gXFo_SMOEI45F_zCTVOISpnYWEy1KIbRFbH-LRkhlpPiSRSMdCo1EuB9-7n3JdO0NsX6SqcD2y9bji3a9o01vzVvBBk8AoBqGaJ2h-hGO2tANS9nC73fqY2TdYvhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=sGO6hxLGjXS8GW2r2ItjD8LoUnlVY8dz156qfnq2ESQnWiQNTQJp0MPsmnY9xcSE2LzAhdiDKcC3hVDHNU8j7kQQnMsNKxmA5a80zDbtjZUxcqlRyq9hfASSpolvFr-XI4MKUqohvGY8Me7kjpvEM7_mkQF_RBGuvRFC52NNsVZXfZ8Vb_9Qbh8WiEc1HdawELAdFTqq-2V9f3aSi52Y1MC6gXFo_SMOEI45F_zCTVOISpnYWEy1KIbRFbH-LRkhlpPiSRSMdCo1EuB9-7n3JdO0NsX6SqcD2y9bji3a9o01vzVvBBk8AoBqGaJ2h-hGO2tANS9nC73fqY2TdYvhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=L0UrZlNrGFAR2JwkkhH5pL4-rLyzROnUpvF7amnB3BITOY2_1heboA7ZXQt0AwUeMkOQS6P9IBJqiiOmiwQHPHq2aUThgMNYmp1xi0ZfmIzpNVJnsQsYmT1dKwvDlTuyS67vECnE50R7CBPmUkMD0SGGMRJdLhv112ztaZOp34rW6Bnnv7f8cw3PnL7YVDGRgxh_gUdY2A8GV5hF3GHVB6NgbR2zcEJVASlhYHRcnH86NuezFQ_6ERdNWsTREOZ88MfKTjlK7QL9FAkB3KxGi1dcYYGGhKOCwFb3GWnoV56pHceoNk940AA9CYHXfEb-44wXsVXq6Gvth2dnruyFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=L0UrZlNrGFAR2JwkkhH5pL4-rLyzROnUpvF7amnB3BITOY2_1heboA7ZXQt0AwUeMkOQS6P9IBJqiiOmiwQHPHq2aUThgMNYmp1xi0ZfmIzpNVJnsQsYmT1dKwvDlTuyS67vECnE50R7CBPmUkMD0SGGMRJdLhv112ztaZOp34rW6Bnnv7f8cw3PnL7YVDGRgxh_gUdY2A8GV5hF3GHVB6NgbR2zcEJVASlhYHRcnH86NuezFQ_6ERdNWsTREOZ88MfKTjlK7QL9FAkB3KxGi1dcYYGGhKOCwFb3GWnoV56pHceoNk940AA9CYHXfEb-44wXsVXq6Gvth2dnruyFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ObYJZK644sHxNxthO66F_-NJtdnRBCUMIlcALaNoa3A0M_IT610PQnD__8Z5qVNpz5p_0z7Jt-2sACop5chQSWoQ6l8i5e8w5istGZtnt_eps03VP83NbKEX9ZvIwd2PmyOb7Ddc16KF0-jTE-zlOa_nyXD8rKvV2UdBc_kvFQZyYYom92zRq5ofSRThDV-7GGEOqADX8RIv6WQz9l50yytARuH5b1Wc-aRdQsNnvLc_wclEbFkudnDXSaZNl-bfq1xwvcbzPDfYCilNL8FIn1fSgOb3H8Enz6TDoH-lH8u_hNhgyOQpFp5eHhzJyN4udeFnhZKfpssVEWhAZWuFd5HY7dXFso2HJ-U1Y4b9U7VapFTv5A_n767EFqxyZsp6gG8AUM-J48vGFRWP7wH1h6ZdBaYFJ9dleZRC1wT7kv5HxNbsi9qJpFU02kDbsyyh4Y9ziSXQALU7p6nRUuF16AvHtqat71IdZmvcsPb5QaZ6TS6XzUU-I2vsQTZ2-oYrLFDX5O14qeBefs13RECpoM1rluu0-zgr8zz5BbELgN_uZYrjncBu1QrKH0rEye_UpJQFxFc7yOt2PWaPhudEss8XWceBlAYZLorjxaqd1Nv9uOdg7PY6VQQaYOuwIm3aJrWDx2z2KLvae4C1ZgwpfZza6HR8ckAe3fLdeSskK2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=ObYJZK644sHxNxthO66F_-NJtdnRBCUMIlcALaNoa3A0M_IT610PQnD__8Z5qVNpz5p_0z7Jt-2sACop5chQSWoQ6l8i5e8w5istGZtnt_eps03VP83NbKEX9ZvIwd2PmyOb7Ddc16KF0-jTE-zlOa_nyXD8rKvV2UdBc_kvFQZyYYom92zRq5ofSRThDV-7GGEOqADX8RIv6WQz9l50yytARuH5b1Wc-aRdQsNnvLc_wclEbFkudnDXSaZNl-bfq1xwvcbzPDfYCilNL8FIn1fSgOb3H8Enz6TDoH-lH8u_hNhgyOQpFp5eHhzJyN4udeFnhZKfpssVEWhAZWuFd5HY7dXFso2HJ-U1Y4b9U7VapFTv5A_n767EFqxyZsp6gG8AUM-J48vGFRWP7wH1h6ZdBaYFJ9dleZRC1wT7kv5HxNbsi9qJpFU02kDbsyyh4Y9ziSXQALU7p6nRUuF16AvHtqat71IdZmvcsPb5QaZ6TS6XzUU-I2vsQTZ2-oYrLFDX5O14qeBefs13RECpoM1rluu0-zgr8zz5BbELgN_uZYrjncBu1QrKH0rEye_UpJQFxFc7yOt2PWaPhudEss8XWceBlAYZLorjxaqd1Nv9uOdg7PY6VQQaYOuwIm3aJrWDx2z2KLvae4C1ZgwpfZza6HR8ckAe3fLdeSskK2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=DhlvNOGL9hyyXlzh5FEehsuKD-NyRg0UdI6OjIYDqnWearQPK2P2CKHI0N4313_jCgtUhdy-wB3NpBOJ4f6NFIzFjrA66orToM0nztVVEuDXWojM0DiMkCyTAagsoYfa27GlZzmNzkICwrtDQmRcaucdpWil7V1o35IOrbdE5KxeQwio446nOVsvRQr77uGxIlz5Y3LmRzVmltuQsQnPLvGqk9qt_dsWv8R4_iZ5snh_BHQGlxshEz-EM5F1_HsMRXpnA7wlj3uOXLjSre1UPonHBT5OrhdUI6MLFMhc6gMMoPs3JndWHN4h7_AqKFn6FlB-xd7h75-yKVFhsdPMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=DhlvNOGL9hyyXlzh5FEehsuKD-NyRg0UdI6OjIYDqnWearQPK2P2CKHI0N4313_jCgtUhdy-wB3NpBOJ4f6NFIzFjrA66orToM0nztVVEuDXWojM0DiMkCyTAagsoYfa27GlZzmNzkICwrtDQmRcaucdpWil7V1o35IOrbdE5KxeQwio446nOVsvRQr77uGxIlz5Y3LmRzVmltuQsQnPLvGqk9qt_dsWv8R4_iZ5snh_BHQGlxshEz-EM5F1_HsMRXpnA7wlj3uOXLjSre1UPonHBT5OrhdUI6MLFMhc6gMMoPs3JndWHN4h7_AqKFn6FlB-xd7h75-yKVFhsdPMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=hf6mPW8KJ1PapR3-eUM8vpwLIBdeduTSAYuuGYG42Jmb8oE255GsHxat0JSjjr3j6TtprmAAfss4p59164uaFZEAFFC1amwZA37tOGk0QccKkd6tinidSaR7e7ki1S7Mzrv93Lj71wnFO_PmerxOe-NeTxZrghvSKHg3rzaVYP1weMQFaaP2YtXj7G0PPw4hXjBxUU_K3T6yliwOb8Lzu_3rddcVOPmOSWlm_xgpNk5LYW0jpYuIojAT4LZZsi96iS5OXT2PGisAckbqjFKNYrRjM3C0iix7UG1Jo5Z9ig2pFXsqDjPUWeVZgU3WS8FwOhBIvERBZTSeDtKXTjdBFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=hf6mPW8KJ1PapR3-eUM8vpwLIBdeduTSAYuuGYG42Jmb8oE255GsHxat0JSjjr3j6TtprmAAfss4p59164uaFZEAFFC1amwZA37tOGk0QccKkd6tinidSaR7e7ki1S7Mzrv93Lj71wnFO_PmerxOe-NeTxZrghvSKHg3rzaVYP1weMQFaaP2YtXj7G0PPw4hXjBxUU_K3T6yliwOb8Lzu_3rddcVOPmOSWlm_xgpNk5LYW0jpYuIojAT4LZZsi96iS5OXT2PGisAckbqjFKNYrRjM3C0iix7UG1Jo5Z9ig2pFXsqDjPUWeVZgU3WS8FwOhBIvERBZTSeDtKXTjdBFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duNZPRBFmPlkoblIXKsCbbGrS6B_CeBBuEVQAoMIJT6cM5JngR4T75BvH1Rsl2Kjkrd766e1kI2I_yClIIUkeTZXRM88Qb534zR8JaLFat8lWkZMbk_XfkCFJMYJw5YTKkgF2SHGbmJuM5Hua-cffoGcF1bIIw8Hcz9JwAh-f60yeN912PEcn8SkXWx1CmszN80Vrk_ufFCuLMc9oA_-0LQpgnI_RuvfltKyk2s9B9JXxLDqhgbmkUEeMmee7el0stt50LMrxifu1yCS4DlIu7uER6OWe3pmQ8uXKNcthtBJUmZQKt41m-70DR0FJpkW7ZDr2tCHnMCsX4jnkNBPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIT0aUgN_PTTZbRBTUXjinFkQqP2iemBscZdFcnU9hEucmf5a0h2jwnl2LMU0XzqyF0GngpxDXm5MsX2-bEvzRnOaMiq1eag8Y2Z31FmEt1aANhPAsLbbpPeorJQV6p17nwIn6AOV56yEV7QqwXVWMRt5PbTY-ftm3NuOok6SACDZZqHHN6kQhcMh6tU0DfCriZD4MArdY0DNEMIPqNP1FIoaKrKQlie18vNUdlAT3FUAcCPrmIl_PQxk9ebepEDWXpWgp43oAYsAW4514-hNl2BZInhrc2NWfv5cB07_D7kcdXrWyB2V2x7R_2xKku5YahtzTaM0XxxTcshngQvbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=GkftM68BVxjnh9yqAOqkomneZfVA7iV1l7xpyww4eBdFGGv67n0TEq9rpC_cEMGldaqH2hP0qrQA7LPzeJuBb8KH8vXa8Gn6KbQETEzEyVSro1MHvwihrx4-smXh38ne7EcCkhAdP_Xk6zzZXvkiUuhXxd2pQwlq2IWaMvtzSTtw7oCKQ9DoU5sX3jmv7cj4TzdMR0fodtgGu_bcE-YBn9QCM46XyQDNce8KlmDgNuqYwS-SXq2J-46h8OXreQpabWHpDvEfTotkFj7bLwAVre76R9bWxYPlcTtdporpKeCiGdvNgB3kDD0QhPrUwztOulCs4Fz_wcUME3sWixru-yGcHg7jnZYwX4U9V4kxyOmu2m134EIbNFonm2n_0Omv6gz-bTJaP2v8n9QIdjjpwgWwXKK2lb39sDyvKEjGTiTWIOQ7PmHZ0rHLQVr_vzOswUviIggLrk2ydE2OrI1rfpG-rneJgDX_KdB1IqI2guJhnXdeNiLfNZr6DtSQYRY4VAgvmWINEEp-YQWJRobQDEGspbc0JIq1YDyQHfPmuXORVSRBVs6JAdxCMeTKhf56B1N3_d4nY6nVPrh7C_fnO1JjRyoFOfVd2DW3OEB43wFSIxtxiE-gvNZGmGdR87zXJxoer89QUo-SxxrqJ1KN_Fxsb_AKAE6Ph7w7AKxdLz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=GkftM68BVxjnh9yqAOqkomneZfVA7iV1l7xpyww4eBdFGGv67n0TEq9rpC_cEMGldaqH2hP0qrQA7LPzeJuBb8KH8vXa8Gn6KbQETEzEyVSro1MHvwihrx4-smXh38ne7EcCkhAdP_Xk6zzZXvkiUuhXxd2pQwlq2IWaMvtzSTtw7oCKQ9DoU5sX3jmv7cj4TzdMR0fodtgGu_bcE-YBn9QCM46XyQDNce8KlmDgNuqYwS-SXq2J-46h8OXreQpabWHpDvEfTotkFj7bLwAVre76R9bWxYPlcTtdporpKeCiGdvNgB3kDD0QhPrUwztOulCs4Fz_wcUME3sWixru-yGcHg7jnZYwX4U9V4kxyOmu2m134EIbNFonm2n_0Omv6gz-bTJaP2v8n9QIdjjpwgWwXKK2lb39sDyvKEjGTiTWIOQ7PmHZ0rHLQVr_vzOswUviIggLrk2ydE2OrI1rfpG-rneJgDX_KdB1IqI2guJhnXdeNiLfNZr6DtSQYRY4VAgvmWINEEp-YQWJRobQDEGspbc0JIq1YDyQHfPmuXORVSRBVs6JAdxCMeTKhf56B1N3_d4nY6nVPrh7C_fnO1JjRyoFOfVd2DW3OEB43wFSIxtxiE-gvNZGmGdR87zXJxoer89QUo-SxxrqJ1KN_Fxsb_AKAE6Ph7w7AKxdLz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W37BDNoowbaMv4lFIOkudl29xmtfgJjg1uQCil6c-wvYort2YjE2wkG6cz54rWohakY9jlvBWGMbvH0ZM07Z2kcLJvOW2BWp5AWXqg9BrDd66oRTCyJUOAAEzJKNIrrwAz1qIb5QqSlwOZRg_O9LnjlXJa3VPqYounY04DY_LGyDGGejvljbN1tTsWjbIx92ir-_d3DplKT-NyYQeYGEmh-bqOkddMlMist5XnizsB40bvwJmjx2uYDbn1I2FYvfJ3OfnBr38qwz0Lih1T-u1T1V8soYkR1SdpyGGjOVO3DdtrdHkWcf1oYCtceyl00YSFTSXirw4V_7Q3DAR247kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS3aAgirb_HHgny6OICgTGlB4HIh3xbIVewNZLpFZo0rIcOZ2dqvrLv-kwK5YWuLKe7agHEsqbAR1KzAIcqcvDgFmm7P6ucEEpoujFMi0BmeNMzLGSgkigpYoiZgFiNnhYl2tGBiiim7TmlsrtY9epWDYBuSTqrvNst37pNW_4mD34mOQh656xIfFwmOv8W-bcK7EB-kNX1nzai63uwLWaz0gYCYg_E1XCHnlMt9dHPwFSG5iCtI0MMiBgFTiRvXlphvU2qr0Nc8q3YGfrQvuYzNHa_7pBak1QJF4LmXF9Ov1hybCCUXPZRdA88Qox5f5qMUo0-W8BwdN9t7neiuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flq8vQoIX7Y20-N-R20NOH6M7RdWjXMVbHPJ7tkJVDVF8Gq10Q0DNQvNVUMCZ-xhteXkXNiTr3DwJaPAz1pDMrbWcS8fScluwaewmLItTS7Aj5n5ojyPPoDTwZZbtwQtSzOrOhO1zSEd5CNLS8T6RDAFJMf1Lm3ETyA6SaRzUXTv4uycnurpD5pqpqgcCjRjq4-VQmL5_gp_QZ4HRwCvY96zmXSaMd7SbdT13mx2sL1_LIB2o-VqdO3ehCBI-spfcSM3QBg5GV_79AMqL5q6cBP3zYjulezOCgg8hoBsKhT5j-A5iwsfjYNmKtNK0K7mcSCQ6CS8HkLe7uBDd_g6BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BITHUZZvV1hwYg0lgr0vcbrmKM8fLh87XAV_UMegewZN5zPGFss6Y1mNHAuIZWlVsSAOqatgDuaJhUVE_PaZbGFIuHGhJwUuzY9nNeemDqgby7IiuUZOPZ619RNyaltDvp9US3zhIG3P8my5HSTWzcEnTk_2idjhkwV2f-Kl0FG8OJfBAkT4KBuYQ-bF9_LEHhKu7M_6StsXVJ9UelpuzrdgxjZg8bPmPSjRhPuiUarnhDlJ6cZpB707U3K2JHEoMbas_C06w7LvDSHrHa2P3ilIwNDCw2UB0OfXfFSzDsKRg3D1FogTJVRXvrFSwOKDvXWYOfZxW1hROqYv2_aafw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JQt-Kf2GNWrxX8zNWw4J4sAFkAcG07lge5hGVZedO3gaeaCT91I5vcriH_M-FvHHS2By68W6nwd3_XuXvZF8qbBGuFc_o-FPy9Yt80P8kGkZoE4u7ye3mbuu6nU1kCYhf3M2T_wFdrC2BoQ2lOEMAGzP0-uOWmgLwIIZHWW6-JitgnXvy43CRITYwBO9l52sqmQEF65uye7C2TlsElFrVQE0cfHuBWupGZ1XLEaC2jEokK_6LiZvf6OuHHKWIwTgpQi2FYCBAM1OazpRff6ojoW22_XCrA__LiND-VzQPvwhciCGsPNyXU_ab8hKEAtj1HiZJLrRMBHeYjEInI2kgy_PkTrhOJ7XAo1iuw6LLiDqG97LI3B8k1nPJOlyYfDF5j6RtO9J-6UDZObL2XRGNRpekQPKYo7tUPE12TEAdFrfZm1JxC5ssWGFKVaF8i5WGow2TcdN-T8SC5PGumlBdgevToLbxELpYZKJ1xMIt01gWBQdiJig5eDtSFoRDuC2JGdgU5GsVi9SrnBUnA2Mkp4lt0fyELc408klHGxrp9ClHzKkD3AJKMBwcGYQkGFE4TpeKBxciCGZiQMpZqEyUKMWLTczaVMnsVQgnCHcXKrXzj_zb0_91VogiNuH9jgqmzDaPS5rubjuK0upgfywUGw_-CjbPQo9L2eBH35oRQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=JQt-Kf2GNWrxX8zNWw4J4sAFkAcG07lge5hGVZedO3gaeaCT91I5vcriH_M-FvHHS2By68W6nwd3_XuXvZF8qbBGuFc_o-FPy9Yt80P8kGkZoE4u7ye3mbuu6nU1kCYhf3M2T_wFdrC2BoQ2lOEMAGzP0-uOWmgLwIIZHWW6-JitgnXvy43CRITYwBO9l52sqmQEF65uye7C2TlsElFrVQE0cfHuBWupGZ1XLEaC2jEokK_6LiZvf6OuHHKWIwTgpQi2FYCBAM1OazpRff6ojoW22_XCrA__LiND-VzQPvwhciCGsPNyXU_ab8hKEAtj1HiZJLrRMBHeYjEInI2kgy_PkTrhOJ7XAo1iuw6LLiDqG97LI3B8k1nPJOlyYfDF5j6RtO9J-6UDZObL2XRGNRpekQPKYo7tUPE12TEAdFrfZm1JxC5ssWGFKVaF8i5WGow2TcdN-T8SC5PGumlBdgevToLbxELpYZKJ1xMIt01gWBQdiJig5eDtSFoRDuC2JGdgU5GsVi9SrnBUnA2Mkp4lt0fyELc408klHGxrp9ClHzKkD3AJKMBwcGYQkGFE4TpeKBxciCGZiQMpZqEyUKMWLTczaVMnsVQgnCHcXKrXzj_zb0_91VogiNuH9jgqmzDaPS5rubjuK0upgfywUGw_-CjbPQo9L2eBH35oRQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ZkAZh7IDhBzUT0C4S2XRREI-UPgeCn5WbQD5HjSaSkmus6nrQioavfEl2zTDYnAvqGjaMrZruQU0O_hAOYtgOcUKoR_NRsM_GCjVR3gbkSWcgL_gShR3BoprHHI3IwErhT0h8cfe6TAm0YfbxxItWuosQF3ZlWFnuEyqrM8NkQTj6FLYaUyqVhA5r7OkNYymps3evlMnKk_MnfgTAvEB7pDADHd6d06gbiomsXhLQNv-oRBvg2Difqu6JmY4eapJa8EQaKy06cwVxPvpD8w3hcLM2KSB0rLnTRQwLT3cMs7rh4X2ljmP4UbAS6jcpv5Xv8d7W_QNz77uzcpObx2d5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=ZkAZh7IDhBzUT0C4S2XRREI-UPgeCn5WbQD5HjSaSkmus6nrQioavfEl2zTDYnAvqGjaMrZruQU0O_hAOYtgOcUKoR_NRsM_GCjVR3gbkSWcgL_gShR3BoprHHI3IwErhT0h8cfe6TAm0YfbxxItWuosQF3ZlWFnuEyqrM8NkQTj6FLYaUyqVhA5r7OkNYymps3evlMnKk_MnfgTAvEB7pDADHd6d06gbiomsXhLQNv-oRBvg2Difqu6JmY4eapJa8EQaKy06cwVxPvpD8w3hcLM2KSB0rLnTRQwLT3cMs7rh4X2ljmP4UbAS6jcpv5Xv8d7W_QNz77uzcpObx2d5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRFCmEx9o0Xq4keBLZCuTqa7lars6OWX40j7nEwCVTGxiS05tGi4D-kRbhoFc3eSwjct1Iiz5lM93Rr7udCwBxvStOJGncbrOQfsypZKee5QiHrB6CHl09TdwCDoVdDDZFNSGvtgfGCbNyLozJtmSACp58JsOd2bXQ_D2kwBYiB8g8HfMi92Bzhfo2iOFWh4kUo5sdl6KPrGCUuJgUiOlXmf-f-pUfG47NqnaGK2L8tmsARCN04IOn4UuQytbmG5UI0G_b-KHGzlE5EWDltMhdOjrD7cFjnzjxO1irvPKQ0e_g0Ih7G8aVsj9ZdXhl8HeWuPCqqkn8QVWkdKE5dUCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7E4PiWM08c9FhgpAmt7if5dxXa4vP8Hzhqn7Rka2fgi0F57LrHlPD2KtBGa8MXIW5sZVkNTShhLx3IvACQT7yxS4uNDLaGHbG3iM-xRN82bOT8C7AEGo3SCsSFQ2XZ4iM00uVEpoI5fVmb38NKCGrprQT6ImzuO8fNY4wG05slYUg3eWKhOcMifW9L75TdwTHLAVNrqZ08DRdFIgN_BBVjO9MZbFa9NdhrDolnGbNj3ZgULzH3t9nmp_J-6j2EqzR8ExKyC7PPdSFlurFdsrJ_6ux5N1r0eZ2DZ2GGl-Ik8tKKm7qzlUI1T4YB3FqfPJmKnobWtbwdFCaS6-HGs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RouIkcTUq6crL8LTUUL-G2ta8ruSPJ-nX-mhiuEKjAxTuu9NcIynYIaichEc37o_WHghm-0u28eCCzb5niR1Dc7blBnRO3Qiszt2mHCZCm9RVeVwgq3iNzN8bvEtnOkR9r2yO6PqNgK9lXr4leH8gPIGmCq2ZUeg6RMk48hOyU2UF2s1Q5W0WwPB0aY3hXOQVKnGksY-iZBHOECSw6oZkWgu7OOIkiQ7znWWE82hyj6sGHlKkcx96myAH7f9Yi7zZt_nn-XENO-qiJAVRN8Bv0WeX-jC0Evv89ZxeEqdsqXa04VRraeGiEb9zDVRl0cHFJ6Aev7yGFA0PGCYCNfizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7dsnUTF6SbbYX7mU8Sx70Y8GAQ-ifPZtph9tW1LnAXg2os59KPhfOkNkRcdcI2yzTlQseVNeG961CRVlEMatK-YQ1RgS2D1iQqtg_NGrHWxlBbgq9AEB-Xd9eNkBAKarD1W9a-M7lUUDYjjHVdj2FP736PVZhs9q2AREDFMjqtFEzsZwWF3gsr3O5xxqhx5LDqmK5dT9grMsJwpSqbgp7uSH7pgtXTtC-MHbzeCjeOAv88JMZbefp7ReWyXV0UBdd1a1j1y7M9H6avr-XxlOTGKpu4m5oCOlfiFvybzGKpB2pSlD9K1GyxGWw0fdZVXvHHM8spMqXRjPJhEGQ9XoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbtHZwbS5ZnbGFx2aga2bcyxRGho8liITSA65s6daMQ3AN7hJREgP10y2FgOIJ57FqZujj_YFlyx5W4b0Vocc16HEp3Is-TGY4ciRharnLqPJ6dqxk2S4iDaz4svmytQ-77ioOO3OnwRrVfLLVsHuGApf3Xz2t6NtBPW2x7u1CWsmge9HuQT06P3jrzP2gYnn0kzdhiTXgCpEOQJygObWZBJtBwwuX5wk-kSszsbFxggnn721YeII3Q6c4O9aKj77inDvIXcTHpo1kvR3o1B3u11DB0eP8Rpq88E8JbPE_7s_hLQ7TWzfoiP6aTaCtVZIkZZ5z7C_0t1U6-mtE5fWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUScxYOtXg5B4PFLtfR2hhy0_kezgr2Pvng80YMuw0SMc1aqfWf4rdbrrX3oRFhj2tY3J0Ix2Pi63XyW8KBSAMfOQlZ3ECAyQqsl9wl5c7ao7YTtu6wHA5dMLna9tFdcI-p1cMr-Fa7yTS2zPEi9TarE3nDGO6n4NzJOY9-AEDfJXgZETMhTUj50X-n8S5CE84XpfKirGh5PvXBmCu3Wx-_rnnKnomou8t8EnQfeRi0j94s_ZRB2ogiTH17AT-vzx_LroFII4UGOmBdax__eB3M7YluIhp2Lzm5kF_N1rim5pKWGekh9--EfLE9q2-0FgvQtN5uhWWuuotfL4DNUEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNsGEipnhkwPNT5k0iR6XN5Y-IwESutv-e8xOLAn4QmqSpktxGUHmDBhSpOw89O48HLHjOf87OS4-mtvYR9bt61wyXL3kCJaFxDCOlSK63K0VO4ju6A-_A43CS-L51u3erkGUB7HbWX9pGcptgrQbonFJdX98fFT-n0wa_4jn9Kp5usQKDoQ2tX9CNjaZBuo7YE30kDC20rXM7Wuevly9PPvoocwXZeksHjyBKPPVBAaqZI6SmZUzw8jlV9FklQ31H9z3iO_CON9f8hwU48IxC6AO5c-XRk-vRImvJdfKV0lSljWjus2sJ7vezqm2qiQTNhdHEbQcYc0X5MvHxt8QA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=ZSLlPw32xqHaRhDvuGIicxskJUwiM2HELpvru6NwpHiS2Inj2IduEUjLvOR1AQV-E5zAzjTNyMwuGuBSh1Qd9FTd3KRlkyvO99-BR1ZmpNGaAmDOZ1xOCSXOPSQT15y9i6jX0LZevCMpEixEHWp3PAVcG5BZlDebJSemZ5CBnY2LHq67pT6yeu7tg94zG6e_Wg8O4hZQmE45fSz-ZWcI-8Dsq8uubXaKRkWIgWrUUjCV9XRAwbTXg1mlJxJOU_-SPq6qspFHAa7z0bZAeuAnwwoYu30gQtlCOzhy1OmSPIgDPvbb6KErMn5xSicHIyQPagry2Fw6_sPZPKR9kEUovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=ZSLlPw32xqHaRhDvuGIicxskJUwiM2HELpvru6NwpHiS2Inj2IduEUjLvOR1AQV-E5zAzjTNyMwuGuBSh1Qd9FTd3KRlkyvO99-BR1ZmpNGaAmDOZ1xOCSXOPSQT15y9i6jX0LZevCMpEixEHWp3PAVcG5BZlDebJSemZ5CBnY2LHq67pT6yeu7tg94zG6e_Wg8O4hZQmE45fSz-ZWcI-8Dsq8uubXaKRkWIgWrUUjCV9XRAwbTXg1mlJxJOU_-SPq6qspFHAa7z0bZAeuAnwwoYu30gQtlCOzhy1OmSPIgDPvbb6KErMn5xSicHIyQPagry2Fw6_sPZPKR9kEUovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qagGizQZHDyfg7nGpGMBIepuOxCrp1HKuByS47_Dgr5sdlf8k9cgzlu0-ZWLKTXtoovTvZ5qv5-btuhFlc9-PbPeC01SVep80_wellARHZwXQBXxPMQw0smfbAbhb9G4IOqUI3Sy5QC_seApmd2-XmIQUuMJckEWMw-2nSdRaJ13-fEBdUDb1RpUMwnzim8fQdCRJGMv8ePVekhQ9S_bvDrt9dzFdO7eucftTrdDa0oOFlDJV7T6n2L7_la1necAWwcSWBrmO2ibIQ9tsVBzJIFGiFfu7oni3kFVbbRmDMYwyScmnjvmKq64FchyXwc7uFGGzTRyHVPB5uS6Phev8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=dssd3wlOWHIeaATVCIq-rCV2DgoZ5b8KZLVckWABdsj8f1CTGVppxc8RGQ6MRaRF8paQzZ8w0jCqnIrKwBBLfQxjy_B1hHVZgIEEERo4prxnOPciF7FNVQbi_E6iaVVDSqgD495XG93dtcepZKUzh9cuj7DpVvstyYfQzosryyUix8C3Krv1H936RyemZitsl_AgnUubgMKmtakCP0km2lWikyNwNJVUHhERUkm-zYHpFvsWULH9U11cW3TCFZHdXoF3XLshpsIIfw9NEQdT074zOfWk4JXf0ZAQZIv-4Jz6KtmVm28gaOtL2BXX7IkBQhfyFIvqrx1IcGonHXLAOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=dssd3wlOWHIeaATVCIq-rCV2DgoZ5b8KZLVckWABdsj8f1CTGVppxc8RGQ6MRaRF8paQzZ8w0jCqnIrKwBBLfQxjy_B1hHVZgIEEERo4prxnOPciF7FNVQbi_E6iaVVDSqgD495XG93dtcepZKUzh9cuj7DpVvstyYfQzosryyUix8C3Krv1H936RyemZitsl_AgnUubgMKmtakCP0km2lWikyNwNJVUHhERUkm-zYHpFvsWULH9U11cW3TCFZHdXoF3XLshpsIIfw9NEQdT074zOfWk4JXf0ZAQZIv-4Jz6KtmVm28gaOtL2BXX7IkBQhfyFIvqrx1IcGonHXLAOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBr9VRQyw_U8HcAjYfqDlJ1V1cCcOxdpCDK90eVBRqsrwfKmW-2WNnNGO3yeYFVc0dS2tV7to1FlCfp-nDO2IDUK-g9SiHSYFS0spo8K6572a-PW91yPVTLGUz2dxt7y1hHBCgVe42HcLYGIteHKUGbvadvx1kermcEuVPUMBsU3UYPPdD3B67AyRE7ZpzfUdjnCM_OVulvlI0AJ9Gz0Rvm0S2pI9QcRSBrT4ZwyJloJRP87g3s9RvMtvTXCpNwbXsvYT81NIPmHryLCaOLIKdKTOmEk0WY2pIFJ6wSGZO9IlAbE3af9fUbN9D8Nw1Vg56Dyp2zXksoHvy3iTMt3kA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCev4Wv1yL7aMh1m13iKhRLspax4cFoP42LeM7vgW3ocrtcPUiXJqkjVF47652Oolg2MzcDfjeAzyTKIWpllIEvIHJYaCYfriAf_bMIFa1QEGfuHz0FcnYA93o3CypBdbz8dZt4RWf7DMxKS9IcoJvmkYsW00H9VeavH6WL_LDNTV4KcWdgdDt0qG18SdkX1V3hgGQaBA-kBNZt2CkL2GUPnk2eIiQ7-tCpD5SGRhTSNdC15G6RFPR6-PzDNTOPRuBl7E5xXL5sFruncQ4uuk8MoMb0i-8H0DdpZsaa5VPquDQ-O5CO7GydgBKFTC72WlQkMlfOyDF4wwLNMQAuXqso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGCev4Wv1yL7aMh1m13iKhRLspax4cFoP42LeM7vgW3ocrtcPUiXJqkjVF47652Oolg2MzcDfjeAzyTKIWpllIEvIHJYaCYfriAf_bMIFa1QEGfuHz0FcnYA93o3CypBdbz8dZt4RWf7DMxKS9IcoJvmkYsW00H9VeavH6WL_LDNTV4KcWdgdDt0qG18SdkX1V3hgGQaBA-kBNZt2CkL2GUPnk2eIiQ7-tCpD5SGRhTSNdC15G6RFPR6-PzDNTOPRuBl7E5xXL5sFruncQ4uuk8MoMb0i-8H0DdpZsaa5VPquDQ-O5CO7GydgBKFTC72WlQkMlfOyDF4wwLNMQAuXqso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=tuB9_kR-WglAYaPLwECFB-ffTVWTTEAW34W-U880ShAnDLEZqy4op1i4_f-mFsCyc1u_OUeZEYYwBdlP9Y1sdEtYn-WU4O4LVraI_EOm4DRg7hm2NmCUDkJaHBfsA5s2xoTguZNuXsfsG3L0_gJyAZHcAUGdd3G5XrLJeqpZoTWG99-FB-5nUPmmAYIODUWM4V_VFowq-1TJ297fT8njVcnBH12mfCnIvtCnoFcse2BrzoHYqa4DaZpHMg-mwCrLCqMwXxFkw1erebYTN5JRiUKkfxHN704YaG7JjzU7r8Z02KnbZLzEnvOFkblKDQ7Kqq-RgZtEHuoe6r1X8i04aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=tuB9_kR-WglAYaPLwECFB-ffTVWTTEAW34W-U880ShAnDLEZqy4op1i4_f-mFsCyc1u_OUeZEYYwBdlP9Y1sdEtYn-WU4O4LVraI_EOm4DRg7hm2NmCUDkJaHBfsA5s2xoTguZNuXsfsG3L0_gJyAZHcAUGdd3G5XrLJeqpZoTWG99-FB-5nUPmmAYIODUWM4V_VFowq-1TJ297fT8njVcnBH12mfCnIvtCnoFcse2BrzoHYqa4DaZpHMg-mwCrLCqMwXxFkw1erebYTN5JRiUKkfxHN704YaG7JjzU7r8Z02KnbZLzEnvOFkblKDQ7Kqq-RgZtEHuoe6r1X8i04aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
