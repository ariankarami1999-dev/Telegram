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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 20:23:49</div>
<hr>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_cENEcyz3KdrPktc6xwVO-41qmrE-O461xrx-SUYxTMPUrZcIhHGy8ghtxmY87fB_2Dvtbtd_R4gx5pRU2qtuoSTlsKRzp5WyJ73Cl_dl9iU6EQ_noA5tvgrYWA_vaAcN1RGianHTHLEoQ7gFiRRgwgoIpeE1cbegf3-TA0DJCcTDFBtnJcXKHzlqj4HAmO9BTZcEdUvaKvT4j19ys4K550_CA_2sJjqJ1NqYcV8UDrS45D1lwfOa8VQxqgAnQ0bcs4TFT7rw3vqcu2EHIGCCUR8p6-Hd2lJkIr7c3pEDwIstOtDEtO6eWaDQyUBGKQsZUljNKFgk0tokSm87eunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQXUyQRexI8rnYBe_K7nonq4ipjLBVFJKXoSaBoFkpCUd50VKHg2aYEMAIuXysQ6DPsK4y_2nd22Wt0qc41dDnXbpuoQI5Kh3aCUo18ZeTvCb65irmWZatQ7U7U6om9Lvm3LvbNGj-rbLf0M4OqoB0yM-jSKBRXmwffpBlV_PSgUyQpGSk9C7ybe3aCaxfXiCvo3NWYe1p91Not4hBShUSUhzXCEzTTbFMYww201mjrUwXdHoKDyQ640Bm7RsCqVIV2Tx99HYTRpicdq8wjngPYfsPgZnBCCFN8V0fl6qpgQsvAI6eSaP7OXB-tt_qjErd_pZvsOukikYwDbCY9FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDwsnvH6xtXGSHr0bgr5BxoGSZxuUGwdGg1nzvozujFkj9f0RQ9y3NUfE5lJTrllnXc7_gKxL0r_3BZAI4OpT4E8dYeKE-5eXYzOhlUHS8QGbOuQhX5Cdimy8u3EE2OxCvx1k-nXCLWXalT4L-JlDv3Xdg0-qTjG2Ye4yIrz6Bvb9oVdF7xFOHZbHxuU9G1zcKcqXnQE8D5F6MfTMrzBAA8KOTXeoz0UJBMNVW7HpZ4xGuvY0O0jHz2JCLUz3w78RK93nrwUgX_VR4NhrBBdw5nk1AS8gNP9hYw9yqcyaeBoH-z4bUPtgFHCtNPpcoF0T-ljt4h5VDjwxGAebEyGGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi8tyV26_-KbjLq3xq9h8tH3GrRcth9RnLEyZGBJZapE2hYmbMPU79AmAdMr4SlbinjVmeLYVGVhHDxNM8tkW9pXcmumrYDei7bxJqIS3PdkCvQORzoX5rXd4aEpeR9G9oaN_w-qpik-VyITXPy7sjEpQLRnNp-OtNy_ZH-kpzlR7-KeSBOt3UAqO2xwX0hxcOQO38Q-ctFyX6UVIOdW-MbeAN32qzOlZA5RHOp4vNpK515xSG7SYqSo0lSkeTcZejLmvnHZr1cNj3fVq8xp8SNnyAb9S4dW_ekMO9U1Kk_N_8PYupFl1W0vJSMo9v2Lt0mZ8NJmjEsHL0KbJQeLmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClFc9eRtwOD3h1KQCMvZk7RcWdKeMynzF2BvqHl1puDnwnF4QyvqxSclf5ildeMqgL7ZPLBAIS2sxlvPJuYGuEgc9GIithG8Uh8hrDtSNnVXs87COmLKzoyce73K85r47gGbK01hj7xCUCif7ZoTzHJjiR4EZEAzZdo1W9RPi_sY6Th3ZYc3B-HI55YTWWPN_iP3H3uK8a_VoNGLg8d1woa-bSBOn0H-Mj6RzX6UaEq1wOmutB_Phu85TkHxFTOjtCCgb3ScNpYDjkEluqq8m1F7JIWCqGzE6XCYUfQiIG_XwzD3sKHxyvNHABoWXN7aDxL5GrlXvyrdduGw8VXdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucBWTW3kPIAC_E8Yg9z0t2kZ8i10MBv_-xl3G60mndWx_IKo-SVwGJ3TncEsx9g8Iib2eIUQ3FdCy401z5rC08y_SBdeY-pFTy0fWE1NIruFY_ZcW_UTceekYhafQ_uMZwBVs2vLSQSyKD2e0mMxZvyfSYBRr9A3TuP6nVpxvW66MX3ciN1MrFiwtk0ZgWShVl-WtG6n3_UcTh4zNbv0IIXl4ZMxx6mo40fFxMXBO4piQcgpYA6EtMZ7ruF7tQGIQX8ID5hqkOj124wL2oi1kpogx5DP993pnaSYegX4MKGGi33po_N4bOvVV6d3rQZd5TajcSkOZdUvN_Vld23ZEA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=AHuAtdr-4LNK46A3_cl0Vk8biY5e-fJSy8HAWw0CH_RA4TTGOZJkZiyk3RyqASwXpRnMAdNNKG-9haaEXORxyMAhl8N_P8h9PJ8pRYw-WNJST3Dh_z73mv4YhOUoL3jjcnP6vATaBbybwb-Ct7JB5Xrcw0m72pFuPtTv4iI6X1jUdEj4tcL08ac-YUUW0CL_BllSSvB7NO276eUFhCvv-c-3zV9ujXTAxRX80cjIMof-_q3MxSyj50vzRnUHPW9x4X8bNjB0Et_eZeIN0_p-TuItAUT6ciES5yh4S5r2ofSByFHQmNgtZ3AH2LfroNejQaURG_v0Gn2tj4xrIH5daaziyikYxKpH5gqGGnkc5bi8fE7eZD9sq_K5gewByNznMqB9xFtsemBkY5IQLdPq8WrWpNxDiCJ9AchKO8tB-M7oUYQo2DBx3rUQKp60QQab9Qc1VoMsUw2c4ye_YHw4VUSL-k7A-vL0QTh5T-PFHEYDAoua-Jf_23Ema4L3lpKROrFGj4YInBy7jyeRm6Cs3_bRXYMA6wyz3I5Z80nukgVozOr4R8DHTislKJHvRt5pHNy3_oDM3DBGd9C0rMPNW92jIBrqCIIs9wE5tAIkQohTIbJ4Gd9sfaB4u62LmdBWwPP_LKLXhaUGErYUdpinMcMc4e0s-M3v0YNBHm2i4Ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=AHuAtdr-4LNK46A3_cl0Vk8biY5e-fJSy8HAWw0CH_RA4TTGOZJkZiyk3RyqASwXpRnMAdNNKG-9haaEXORxyMAhl8N_P8h9PJ8pRYw-WNJST3Dh_z73mv4YhOUoL3jjcnP6vATaBbybwb-Ct7JB5Xrcw0m72pFuPtTv4iI6X1jUdEj4tcL08ac-YUUW0CL_BllSSvB7NO276eUFhCvv-c-3zV9ujXTAxRX80cjIMof-_q3MxSyj50vzRnUHPW9x4X8bNjB0Et_eZeIN0_p-TuItAUT6ciES5yh4S5r2ofSByFHQmNgtZ3AH2LfroNejQaURG_v0Gn2tj4xrIH5daaziyikYxKpH5gqGGnkc5bi8fE7eZD9sq_K5gewByNznMqB9xFtsemBkY5IQLdPq8WrWpNxDiCJ9AchKO8tB-M7oUYQo2DBx3rUQKp60QQab9Qc1VoMsUw2c4ye_YHw4VUSL-k7A-vL0QTh5T-PFHEYDAoua-Jf_23Ema4L3lpKROrFGj4YInBy7jyeRm6Cs3_bRXYMA6wyz3I5Z80nukgVozOr4R8DHTislKJHvRt5pHNy3_oDM3DBGd9C0rMPNW92jIBrqCIIs9wE5tAIkQohTIbJ4Gd9sfaB4u62LmdBWwPP_LKLXhaUGErYUdpinMcMc4e0s-M3v0YNBHm2i4Ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=VrcjsW5nZjwFN5XyjJJXj3Mfa6sfAIAyqmQtYeDbSWFi-t5T-Z7SbTkSmI6eW7uncz7czIURg3wqm42KjpMSHfqnTDlSimTNkqVCfBDCx766fpiobu_pFk96_MIwXHtFXqJzsLu9pyM7CjpPsEpFPHYsI0dVATQGBmOwXioTB7kohN6Z4GDyU4eq_P86MBY7m7EhZzMEX1swDLtvqEMBEHnEWzRCRt6qGcyfioGKnlD5rMVXJ3_XNWF30UCPJpvaIa5GwVfC_-x-XqLNbSMX9gTJKSXaakXZ1K6pjuIZFeWA9Yg5Tz18l0Dwull-xdbsB_OuMByiHWljunirSbeRmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=VrcjsW5nZjwFN5XyjJJXj3Mfa6sfAIAyqmQtYeDbSWFi-t5T-Z7SbTkSmI6eW7uncz7czIURg3wqm42KjpMSHfqnTDlSimTNkqVCfBDCx766fpiobu_pFk96_MIwXHtFXqJzsLu9pyM7CjpPsEpFPHYsI0dVATQGBmOwXioTB7kohN6Z4GDyU4eq_P86MBY7m7EhZzMEX1swDLtvqEMBEHnEWzRCRt6qGcyfioGKnlD5rMVXJ3_XNWF30UCPJpvaIa5GwVfC_-x-XqLNbSMX9gTJKSXaakXZ1K6pjuIZFeWA9Yg5Tz18l0Dwull-xdbsB_OuMByiHWljunirSbeRmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBsOvoVIf3b-OD5lTBbLCAzU2_ZBEBPeq_OgKDjO6cD31042MjsMTi5RZqNDwG2fpGcm2EUG8bgUo2NvIBX3hoyUTUXrputUhBuBaUys7U7X0ZwJ_30hIaVrwAaE6iQsgYfON7o9tUBLTkb7aJt0LYyjXKPkbIDW6f-9mvOjLFTLdKHZl-QRrAnm-2uJbV8YdhLXUOyAropkPXveKeIC62_XyhI0V_0a0Pk307WZO-H9X_U_uEU5kG-8yBIz6TsQAX-2eBEA9hdydITgIVDajWm-9v9XrQl1XxSEdugtYNIazv9AbhEy0vJVDydcKY4Chw7VM9pTc6AO7G7iiXK0hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk4w_A_7qq5tLrAcDq8CMSGljnMpzrEj2r6Fnood78RPKVOAO5XDhs_kj7ZuozaOCgNQqiqfcioG-1a6GOSos9_hqpUiHzgCFmAGlgx7X8-mJqHZ_CiTIxwUA_CANRccamsFeH6yQh0WmLzQ6SCFHebVpvqttqHQgH3RxOQtTn_f309X5_YG9G3pVxZTJaD-w0n6jGXuYIdznQeq_-UTGJlSYJkROkOMl0qgUW6c_blTb3ndyO1ccJnyi0KRdMkgY-YeTRvEq95uuo-44ZaZRMuetNAUC-7HUpBfghnGmD-tdECkGi5XbGEY4UBvoq8oXNGbXU-Jund9YxjqtnN5sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkQ6rBP3m7OoqD680nEWMmRvbA8qt_ZGOEcQVGq9QgsDJW3X1fNz_Z7odNhTiNZgu9Uz0qiLI7B4zMjc9yj-GxSWfVaok_hZhaU52SZgrut8v9_Gwxe9D6K0vzdpAm9KnZrFaWhiYIWrRZobV5DltY3N4iGKFs6QzhmJJseOVEsEsySzfWCeWWe9TNfpn0foc7cp0sEV-9eCjfGghfdAcbyXfMGTi-5cqnGtol_53S4eILr2l_qt7m2PxIBGw6uNKn5Iikljr6eED8bJv-vsA5_0qgoPE9wgfQpYut73cCcMlHedqYPuc-Xxt79IjYQ-4PvNrDD52WB1mTIMWptCmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=sq5fJqHcdi6RrreAj2vzG5QgDteYRPWOJr_PFsh4ijpdAAVFtwW-Fxm5tYWx_1d86yRHuyj1YEjF9OsG-TxR79ATidPcBx1gNaaVXqjkjvbYX4gd9z7FbKd2aaVRqzXypaMp9qxDM7MwA66sDlHspXw0iGPzx6k5IYVcC9nSaPux1BIA6BjNwyLrPmN2xrJfnv2PEd4yNDzILuYXgXH-bWxQCV8WaeB1gxyd91uRAVZAfTng93cIJgFpJ8NbKLdrTlbAkOf4x276x_F1_bQhEbJ68raTDWzKG0PZSm5DI4WObo3MVfAdL6mKkck9hwgt8nKDaTL9zrzJKUwOZr25Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=sq5fJqHcdi6RrreAj2vzG5QgDteYRPWOJr_PFsh4ijpdAAVFtwW-Fxm5tYWx_1d86yRHuyj1YEjF9OsG-TxR79ATidPcBx1gNaaVXqjkjvbYX4gd9z7FbKd2aaVRqzXypaMp9qxDM7MwA66sDlHspXw0iGPzx6k5IYVcC9nSaPux1BIA6BjNwyLrPmN2xrJfnv2PEd4yNDzILuYXgXH-bWxQCV8WaeB1gxyd91uRAVZAfTng93cIJgFpJ8NbKLdrTlbAkOf4x276x_F1_bQhEbJ68raTDWzKG0PZSm5DI4WObo3MVfAdL6mKkck9hwgt8nKDaTL9zrzJKUwOZr25Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqJggjTQF_F2JNdUCkEQ3LGvciHTezKu13MLeObopAsHIjaJC1OWoMpKHBLdj4NAFNhjK03eO1-S1pat1MbVhwOSUsMnnkLv_FCLJz_W1bj6V8ZpUmaH2VmQ_j55iL8ghxy_1x_YyOe-p_JT3GxznxYtfaG4MhG41474h4rsWSDxDFYjyu7D9ZFKCAoWzvap8kkVn0WnMLC1a3fi3WBwmmkePar6s9gzXGxQB1oLPw2jGnT6xgnYv2lqOicXb-ibq9haeaM1Jr26OjoyiXe0oBedmEQ2GQoY70kO0JoJXc91N1E5C7oMacASjl0G7eK3cfBkQr03C19T5bo0ZENY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akkvZjjdrO0onmhyeLd39sAqvhgKQXIx_0eu2Urs-qBaFG_rcSPjrlb6EBh003sMg37njUdlpGf-FOc3EnE77e5zopBrB97mld_PNHEQQVR93AxKxHfk6O0DW6_cephEW0h9vCY3Xj6w_ugkem2UjqjMT6WvhzuHAhpvs_b-mXcQE5CMtX4s84m-1VUwS5zheF9kwJBRTpdMKTm4X8hH8a4bNfDQlAth2qrAgzXP3KgslWQhpAZsSFJY1ha5uRod-Ab8nGWX-6TXZws1cBNz3JgJ9CdOtQG4FCNexxJhpW65FQL5-EO1z7NZuVnnG_4Dso7jLWQOv2ScciPMHdXSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPP6KNGQBpG37G652k-BXAcfkuEZxJM0caVCxG8OEECxwDIzkxXMXAjE0iuMm5cP1px5KbtpCy9M_zb5wg_OY59Qd9wc7wBUzqLf46bf-TpU7YQdMrT9vTC0kjQdHOtJehO5WwFTtsRPWnVvDYokgjrVbW7hmEbRhEBxNDu6OTEBGK5gi368Pw98M5IOIqEiZiODO9Mnarw0Lzg9Z1mDnqxWGsvpVLdr1sR7CW4k5LSx-V-ei7_DMEouHtCKsbTJ7tZ70hjW-5CYmrgSmI9AfNOxty-UBHztyYvmF1W_OuFTeP-LJMlQBDR4DcxqK7PZpFhD85-v8rltr-JdgXHHWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFSERygUlH61Wv2lYtfxq11y2pf08Xw38ucSj4xexPoPnQ4W3VPu7o4HIi7Xs6bWqlipw_5qV36Upq7V0bcZnKXXuGdMA7fnfoKD66G4m-DQPYWqA8oR43WlSoarOYmFfOAQ6z3YYHGcj8u6OTCy_i8tkn2WwEfNyOq1VHMUc7nCWDWn16IeDBNQiLixL7KzNZaOwwQBKL1S5j1I16C1eKoYIV9-XY-kRyNraGWDQYtDXAJxpTPfrNVY2Zr3gtNVH7f5XqbSmrMJ86uEs3MlWljWp0htm5KMzqyW0ECHPF35nyBTamVY61vAJagEX94FC8wARmNl3aZcTQjF18rTGg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KHDuh2iLyTEMQfD3FOQb_a3JWh6h9w5cXUbg-4XqdpW_DUeEhZgXR5dt1Hxtg0SZw2ofqCMDARatWLuuABTIH2-gy0gxLTTryC3bxQ4XAl7iPhD6oQdAPwQVF6wAGca5yWz0FXMH9CDQ7r_JfDuMpSjVLVy9V1jnWl5uBmkpk9epx83gQ5wR34LtOH5K3QyJqLlWPaiqg_pHpF7Eb2Eu5ZF8zDkpTop0jT0OD3Ilm-PjVCWZTEwz-c566hryxsKVc2ThYYaOdpyLk4GDvsM870I6xSexk3ZND3zjbHKAWpuEboHPUZfG8y8BcAbqiKekZo6pb7QGjCYw9RlNYoTvKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=KHDuh2iLyTEMQfD3FOQb_a3JWh6h9w5cXUbg-4XqdpW_DUeEhZgXR5dt1Hxtg0SZw2ofqCMDARatWLuuABTIH2-gy0gxLTTryC3bxQ4XAl7iPhD6oQdAPwQVF6wAGca5yWz0FXMH9CDQ7r_JfDuMpSjVLVy9V1jnWl5uBmkpk9epx83gQ5wR34LtOH5K3QyJqLlWPaiqg_pHpF7Eb2Eu5ZF8zDkpTop0jT0OD3Ilm-PjVCWZTEwz-c566hryxsKVc2ThYYaOdpyLk4GDvsM870I6xSexk3ZND3zjbHKAWpuEboHPUZfG8y8BcAbqiKekZo6pb7QGjCYw9RlNYoTvKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=h888nVXEYe22CxdEnscWhib7sgHTFKGS4RUcRHa1-BvwyrlEAFgS8scmZaTKco2zZPagWSuvVAzRmx9W6YiWvzY-rD2L3aZD32ciFlB5IAFtazz71OaTMBF5-jzHh-jSOWHkXR_bQLpbJU4S9ZWWYKCZqZG-CIabIVgwx08paev9R0qrHWmweruvDl0EuHfss2GSI73TTN2H48qsBkPMJP010JNuodJOeSiwCu1QJo7HngzMK3Sm3Jwi18tto0GqaxhaEP3yymabqu6tmcuJ_LEHCQb-iGwtpE9yqAmVVHHrjtEtJ_uHH-KLC-3czFqwHRHehpu51_hP4EZc5J86xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=h888nVXEYe22CxdEnscWhib7sgHTFKGS4RUcRHa1-BvwyrlEAFgS8scmZaTKco2zZPagWSuvVAzRmx9W6YiWvzY-rD2L3aZD32ciFlB5IAFtazz71OaTMBF5-jzHh-jSOWHkXR_bQLpbJU4S9ZWWYKCZqZG-CIabIVgwx08paev9R0qrHWmweruvDl0EuHfss2GSI73TTN2H48qsBkPMJP010JNuodJOeSiwCu1QJo7HngzMK3Sm3Jwi18tto0GqaxhaEP3yymabqu6tmcuJ_LEHCQb-iGwtpE9yqAmVVHHrjtEtJ_uHH-KLC-3czFqwHRHehpu51_hP4EZc5J86xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pbx4WRu0pwzNUbX4lstwExrOnJ5D4WkVOjQCJ9UwF7qut_4SbB1hq2SA-1KmDWW-cT3l3RRs-VBpji737-hBGSgUYiz8iXduWiDGweX7RQ-Dy_yFi0n73JRXF0cI6J8pJSbAWGxGgGV5TJ303fiu0ovUYEJcP85bMNyON9MZKQz3YHKOrixAEJ4wkk1Oe8SlE3wHLxaZIRn1k0CfEF2uj-OvsDcagcvbbahpXER5G7qlh2aSVd-FeuLVJyNFgIqkTKPbRNQo9FuwxZxD1HLcKalmo1Z0TW8p4sCt129tyMF4sgC7ENh21C9A5KfEnYruY-aPuCbcuOWmhf76dd98Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=pbx4WRu0pwzNUbX4lstwExrOnJ5D4WkVOjQCJ9UwF7qut_4SbB1hq2SA-1KmDWW-cT3l3RRs-VBpji737-hBGSgUYiz8iXduWiDGweX7RQ-Dy_yFi0n73JRXF0cI6J8pJSbAWGxGgGV5TJ303fiu0ovUYEJcP85bMNyON9MZKQz3YHKOrixAEJ4wkk1Oe8SlE3wHLxaZIRn1k0CfEF2uj-OvsDcagcvbbahpXER5G7qlh2aSVd-FeuLVJyNFgIqkTKPbRNQo9FuwxZxD1HLcKalmo1Z0TW8p4sCt129tyMF4sgC7ENh21C9A5KfEnYruY-aPuCbcuOWmhf76dd98Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=JJudihgQUVIKX2e2Nr0B4HUmzGSFEmWhRKimzU38NTI48Q7KhJqrwZNWG_A8qYFxCVc1JSD3bslncN6WB-VwczVtQ55eOnC1sYC7a1uwA6kKyU6382vzS9442TZJDrKBJ0c05nNztUY4OcbAUxnkZJUFRkTrhDpDZXRmR0-euQoOu4go8M034rJZ6PXDjibKd6LUf6fHSBtDAI0EJDj5Tw-_RQT1M4CtxE_PPl3FYsk3TzXddP2GAhW0GkUjWjAClTKnrKH3XB2_qJIDR1rg8DwembgQbhrGZXSN8tHqji1meW8abitoGFIZuoYm_XsX5hPyFtS7TQCmtxDjCyUwvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=JJudihgQUVIKX2e2Nr0B4HUmzGSFEmWhRKimzU38NTI48Q7KhJqrwZNWG_A8qYFxCVc1JSD3bslncN6WB-VwczVtQ55eOnC1sYC7a1uwA6kKyU6382vzS9442TZJDrKBJ0c05nNztUY4OcbAUxnkZJUFRkTrhDpDZXRmR0-euQoOu4go8M034rJZ6PXDjibKd6LUf6fHSBtDAI0EJDj5Tw-_RQT1M4CtxE_PPl3FYsk3TzXddP2GAhW0GkUjWjAClTKnrKH3XB2_qJIDR1rg8DwembgQbhrGZXSN8tHqji1meW8abitoGFIZuoYm_XsX5hPyFtS7TQCmtxDjCyUwvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ru8NOL9CONqKlXOQpVk0JcWTzYl4fhn9OvKQLx4Gu7ag-lt8oyHtbeL_BKG2L4uVDFKMbefebibize8vgqwSy1omfKaM6kVAGe28C7Qr8Vv9d-GRfSzb8cp6nw4K15-uvTaxUKCFSR4-Tu44WDbIoPV47dEovf7Ixq0dht8WCyPBlPUN0fK1e2L9h2PASTMDRyvQk2iY4ZLHv7Mf0uw9VnVRP2EWYNIlpVMIYyvCB4FyT5BvpdhpGlwEP2jsC1J2tk8d1F-4YRBxBWLp1HtlSVML9EVGhLMwt4HXfyi22Wev94BUe3J-wnSrbrgfedkKhhViHcbvmvX6ajybbGfu2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=Ru8NOL9CONqKlXOQpVk0JcWTzYl4fhn9OvKQLx4Gu7ag-lt8oyHtbeL_BKG2L4uVDFKMbefebibize8vgqwSy1omfKaM6kVAGe28C7Qr8Vv9d-GRfSzb8cp6nw4K15-uvTaxUKCFSR4-Tu44WDbIoPV47dEovf7Ixq0dht8WCyPBlPUN0fK1e2L9h2PASTMDRyvQk2iY4ZLHv7Mf0uw9VnVRP2EWYNIlpVMIYyvCB4FyT5BvpdhpGlwEP2jsC1J2tk8d1F-4YRBxBWLp1HtlSVML9EVGhLMwt4HXfyi22Wev94BUe3J-wnSrbrgfedkKhhViHcbvmvX6ajybbGfu2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=doSVwMSZf8uTJJEyQjOgyynyU9FGURnVNfTZSKpsOUWMFCoWco349dnadssrn1kgUqo9RLke0T9wf6Tbfx85-b-qc8uTsE-Nuw7TOWFbcWQg0BRQHQQhBMvvUyOPezu0mMfQq0ZrTMypsnWTxHng4_8des3IDxf03IxXd8nY8U0qWE9W4xC27a9xVBi5JPxAOMXhw1cu8jHmT1SoaiiFekGV1gbXBwHrOAfAmVuyNxHn2r7_0_O7wcW6oPRm21Jkk976-mYmCLoAioVxBj2tU7M1o32vDBM3p71gX4TpxC40JyGAqE-Xu6Hj9EXIHbkaIUF3lmfFzwIV7GQN9t9pLYFGCeJ7BNGfX2khZAoL_pBdKiUxVAGBZK_vcs7_YV76M1VEJFxdLXjifWg2WnCabPBFWME5Dejstaq0pdQ3TbjSBjzQrEap4aBj6d-8o7vPGKmZZ6VDm9DA64wC4zVSNJYUWhLvIwKFjzRQlkq6Etx07i_ez5xPd8NJZPBSBDuHdi3wSSibjwtx6f4itZ_kwJbQqDETDYGWsGEPdTGjLD77wQSSNph8rPoTmDD1rzNHBNz5z7XMQA7mL1NpeSvTdVNd0SACzLYoEOc_WWQ2j5DeKr4INv7kILg1TMJJjrb6HRJMkbLK4swBC9ha0H4thnWTZ6KqfK9ktnm4IoVLEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=doSVwMSZf8uTJJEyQjOgyynyU9FGURnVNfTZSKpsOUWMFCoWco349dnadssrn1kgUqo9RLke0T9wf6Tbfx85-b-qc8uTsE-Nuw7TOWFbcWQg0BRQHQQhBMvvUyOPezu0mMfQq0ZrTMypsnWTxHng4_8des3IDxf03IxXd8nY8U0qWE9W4xC27a9xVBi5JPxAOMXhw1cu8jHmT1SoaiiFekGV1gbXBwHrOAfAmVuyNxHn2r7_0_O7wcW6oPRm21Jkk976-mYmCLoAioVxBj2tU7M1o32vDBM3p71gX4TpxC40JyGAqE-Xu6Hj9EXIHbkaIUF3lmfFzwIV7GQN9t9pLYFGCeJ7BNGfX2khZAoL_pBdKiUxVAGBZK_vcs7_YV76M1VEJFxdLXjifWg2WnCabPBFWME5Dejstaq0pdQ3TbjSBjzQrEap4aBj6d-8o7vPGKmZZ6VDm9DA64wC4zVSNJYUWhLvIwKFjzRQlkq6Etx07i_ez5xPd8NJZPBSBDuHdi3wSSibjwtx6f4itZ_kwJbQqDETDYGWsGEPdTGjLD77wQSSNph8rPoTmDD1rzNHBNz5z7XMQA7mL1NpeSvTdVNd0SACzLYoEOc_WWQ2j5DeKr4INv7kILg1TMJJjrb6HRJMkbLK4swBC9ha0H4thnWTZ6KqfK9ktnm4IoVLEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gnKlAAYjT12MONYuvhVZ7xtP9KQipO8N3lN01bQY9ayZ2l9b3n-S0PoPYAffoqd4_iT86KnBRcADBSkrMcW_Cxk5DN_6tnnxZkvT4M1BI2mSEafadNali6dadXODRExOpl37XEfpbO_sTG_Ks2w6cCXzCSUvpUP_CZjvVAbk4gA9BJhhzrh6bsi1nlP6bWY75ytSrLPBbWHYYyUwbk8wU-384fuBDdscAQGTAND8bDZ5N2oOPw_WU03GDHaslJZEs9UoScCM9ZFu1aQjz-ACFa2Lw4AfKheCmOwN8k9hf-_BhgrUkoPpXdTMEQlcll-WxF4b_x2-PGZn6Yps-6J_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=gnKlAAYjT12MONYuvhVZ7xtP9KQipO8N3lN01bQY9ayZ2l9b3n-S0PoPYAffoqd4_iT86KnBRcADBSkrMcW_Cxk5DN_6tnnxZkvT4M1BI2mSEafadNali6dadXODRExOpl37XEfpbO_sTG_Ks2w6cCXzCSUvpUP_CZjvVAbk4gA9BJhhzrh6bsi1nlP6bWY75ytSrLPBbWHYYyUwbk8wU-384fuBDdscAQGTAND8bDZ5N2oOPw_WU03GDHaslJZEs9UoScCM9ZFu1aQjz-ACFa2Lw4AfKheCmOwN8k9hf-_BhgrUkoPpXdTMEQlcll-WxF4b_x2-PGZn6Yps-6J_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtNJQ5dva8sgPH6aAuTI9kvHEZk4DahE2yT6wtVjwti74ZyKPW8TWp4p110CL2MJIvJW62hsD4Pbh5v6CTduudXMCyKTT9_TJaP8pZc2ysYxK6qHb503r8Y58x0k1-inGgAH8EdfI7_7y4eHqlDHQwKWCkOweMukT_0YbnKTFIq8zyXqMdbAeMoYKJHYCXjdDfeLO53naw0RdkukzR2CxrsJJ2meFxln9oerZjwvau3W9cjIR5mC6ybVdMr0iiju3Zbnfts2GmryIVP6LB9PIIPMRu7lnrkQEopITZamL-VbfKW_F5dxloQhQJSTq3owBWRdnVVa5EGxMEuU3DZPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgCg3mDyH-hdC50jrZLS9JskmB9rpbnJ5GDgpc2C5dLhFHYpVva93wqyqdVm7UWrVczPlN8t80KyozVISXHqExmHPdCltUOzdh-krb_Iiju9yee8ShnIDZS2o8zF4rk24SeppKA84Rse2C7cWRd3hpsGFvXlneukkA-PFYiDlbV8yEPRtQz9-BHU8Oxl0PGGtFiZm8Htmkzkl__yaxrg40mqE56-2UZwQ6bv4RBrRCju_Blghm5SsxjBGEyFzui_5UVOB4Ay_7LuenTsptAwDlRotQzCtO1cg6gAZNLxAA-wABYP_XEZ0VSyesNI63NaM3-XH-LfZZKbyaBhd9kQIQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=P6koSUUf2j1fJxn_qJUeT4R3QXcZmQ8BeTUDuE-mxK2uCJFs0N7SYyMw_rCRiQ-ulyp5ld9o38mm1Y4YsJVCNAo_1JxeDvlEpGslsKXKNO-aR5VqwlkOz7ZpAzWUI-xTyCyrXzlnfYeUwd_rc6vmv2pdOpLQcHN8Lo42S1T7kIQxVNf58aFS1soHo_vHHouL9B9jKnN4mjSplJLe5zPVtm4Zlj5HZ1hkb1n5AzF3B9me6Q6B-9jqFWMBCbAZkK9BBfbZBm4pb1nEOM3xckEmqRzplRBHCBk99QOLRf0eto5GXl2E3rtaOoC9OV-EiDmSyr1tR0x7L87PgX3xTRw3GkXk_OcBE1qhOsRUpXG-2tx3RdE64aHr8w8WK6wD5wrnqF3TA2-Z1jY3WzNRQudR_qot8hcVLPP3ywjC7qNlnaRxiUzfSxRwysVLMhpfZFDiS0QRAdtv8mna3TymBAfvh2rfDkGQlwUm_hhSeaAP3b3ELkUka_5H307wK9F9QY2v48XpBG-lw19SHAHfruOX-QWlLqMagsUQ9PX6GSz_2YWs1uNboKSvyir3QufqPpVt_XjJfmBI8mIAwIefBF13ZIUP6nSgXSwD45NtmANyEVK74XDc_gZ32zGUqQSf6eJDwyWLEH7npMg7PiLxo-vCYEeVRfO4HNFMXzQGosiYa8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=P6koSUUf2j1fJxn_qJUeT4R3QXcZmQ8BeTUDuE-mxK2uCJFs0N7SYyMw_rCRiQ-ulyp5ld9o38mm1Y4YsJVCNAo_1JxeDvlEpGslsKXKNO-aR5VqwlkOz7ZpAzWUI-xTyCyrXzlnfYeUwd_rc6vmv2pdOpLQcHN8Lo42S1T7kIQxVNf58aFS1soHo_vHHouL9B9jKnN4mjSplJLe5zPVtm4Zlj5HZ1hkb1n5AzF3B9me6Q6B-9jqFWMBCbAZkK9BBfbZBm4pb1nEOM3xckEmqRzplRBHCBk99QOLRf0eto5GXl2E3rtaOoC9OV-EiDmSyr1tR0x7L87PgX3xTRw3GkXk_OcBE1qhOsRUpXG-2tx3RdE64aHr8w8WK6wD5wrnqF3TA2-Z1jY3WzNRQudR_qot8hcVLPP3ywjC7qNlnaRxiUzfSxRwysVLMhpfZFDiS0QRAdtv8mna3TymBAfvh2rfDkGQlwUm_hhSeaAP3b3ELkUka_5H307wK9F9QY2v48XpBG-lw19SHAHfruOX-QWlLqMagsUQ9PX6GSz_2YWs1uNboKSvyir3QufqPpVt_XjJfmBI8mIAwIefBF13ZIUP6nSgXSwD45NtmANyEVK74XDc_gZ32zGUqQSf6eJDwyWLEH7npMg7PiLxo-vCYEeVRfO4HNFMXzQGosiYa8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHNnstDcCxxVRg9lYPG6JZ0vIttloCN5bzYAnpt9JxJCnRS2GeLK8X2CDHU8sHGXTj3sLkQ-5PzIE8fLU3sRZw5ggkK_BWdXr-6g5Vlgu6G0PJLImo5diGSJPBBd4rDnaTErgr8Qqo-DXyD4bDdGkzpaMuDCJIjdO9hI-WppCwbJd8dchpM85se-GS4jBULMtXgRUA1QTnwNhRw-rzIpoKIvKVADbwCwjOd6Q53YvHJvVodzpfBBjiq6AVk_86Jyyh2ZH_Ut1SPpqyW0XiXmYSU6BnOE24JF2LTUXFkdTYHDKuw3m60HxLPoNobGzImntVnxa1cafFnjFJACcbZ1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaRP5u0bzZPIWPrs5rXc5GDoUME66PETLVXmFfCz5vsl4jcjR3T_zOCgmDANzMfYYBM83YfsLEAOATnnqdZKffF8MWDox04WAxcl3e29h2H9p1x3tSlX2bDNoVElmIRAjYyGFaVlUdWmLmeWOL-nSiAP4FQ77eGHUDbXBVjAm9BMkPR9hzXRAlIjp-AK_Boei10BHHQiiAeHFojDYmrLowuqSNpZqBX8pvmFLKaKxP0jZgKZBovoDBWTPTIvNYEr0GRZ2zHfUH9A6D-gccShTZEJgn-y4LPNhPydWBv7pIAzlEsShqC_AryNbfEnYu-3UnoUwFj_jBPOONWdnX7mow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hixTN9wRfdh4nwEriBg5FDXNzm_tGAf649vOnK-GRd5C8wZkevDHo7zXCT9bahnxs2DS12n1RI8Sxeo6wls-soG_XorSJ-rc1unYHrKpfNs8TN3CpLXcna6Lkc2IFnNZYA0NSGGcLMLPJixkIjnMSqZpCAYSfCYGjdxFxTnEdl4hRSNxZhU2xSYcvtd6mNye0jXuBrQvoYJfpamLhAAXS0c2eV9s50Zdcv0qQv2QDiXy105Djg5ZfunDgnBlzVNOKa1Gh_FzX1giDceBtajBENv_Pn-egIOI2j9CYjm1N7GT4aXLDMdqhKj3mFAA5-6SKwtaY62CdQ6HY6gnMAI1Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkqbwLr5m15o223OxcP3SjmwsCBQrvyuch8CoF5ME300E_zpn9Ij-Ik0GvGmzmheCwfbj5XIXof-HD5m11KxRBbmqZmfKLOq5VHZBSDCIZJY1JXiP_NwxnUul_ynJ1ipQOXCALfxiNOy8Q_soD0w4qyU1xX9wUMlhlRfKYeQGeDBMh4H1xXA_9QscNm-LwLCyhfCgFUlqjja3zp3RdT2voGSGF-5XwxXbGB0vQK8yPnaxQjK5K92AdQ7EYRrbuywcKe2Txmdex5N8FtCG8_UubFmY9iNlHTTy1oZgWR1Ya06CbMISK2zLL0W1ugvHXFeCpTl8WZFe1ALa1MynHX6RQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pNGDrmQ_qIPW4Idr0o0sfm1zvJN-WW_1QLEQUeQ_IGCCbH5JMnt9pnsH6L4h2tn2saj8pcZnoKo2AIMNSzcxBEMvs4HZVqrcpzt8SYmHju-t-FJgvFZtcsPvS-gNaEIJvtYonv33tO9gCWasubApWfSPYT59RetN9Q0J06RPEsKvJdI4Ug7T4u_oymENEChI0HX-mdBifamcTdbYRoiOQnprGB4x-k2LVP71LPp-Bo0bwWiIrFGn489g9jCc340NPjHj-CcZF4_naxhoXsOT-OcVx5PTwXwmlw16EajaO_TJo7tl5evJPrLa9m5F-naj4O3ZmK2unp2KhnFZgSU72w7KAEE39yE53AJBjmRhfGS7yEdfgAo-ym8nPSqHxyNbaPru4mcGJPdywFJQTNzN-A0i4Ym_iSlpqJXgALpLUsvKsbsAifJir5NhTt0AvK6RDF5tH22L6gnyhJaremVdNhSXsJSKpZICvM7lvD5lajh52xTYQN-iFHBDYITXtjuz52nQ4n1SKiktOZ0RLI6L2TWWR8lnKg-xdY7TY2BglsC63dPMNwAwNCTJ-pD1U-zOrADeDPQo901Vu12-IyCQv786uH6L0OfKV0TvzUvs0xgzxKLciURGjJNDWgr0xp7JZWqzv2xmiHsmzj6QIXF3wzZzyml199-zc84KraYihNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pNGDrmQ_qIPW4Idr0o0sfm1zvJN-WW_1QLEQUeQ_IGCCbH5JMnt9pnsH6L4h2tn2saj8pcZnoKo2AIMNSzcxBEMvs4HZVqrcpzt8SYmHju-t-FJgvFZtcsPvS-gNaEIJvtYonv33tO9gCWasubApWfSPYT59RetN9Q0J06RPEsKvJdI4Ug7T4u_oymENEChI0HX-mdBifamcTdbYRoiOQnprGB4x-k2LVP71LPp-Bo0bwWiIrFGn489g9jCc340NPjHj-CcZF4_naxhoXsOT-OcVx5PTwXwmlw16EajaO_TJo7tl5evJPrLa9m5F-naj4O3ZmK2unp2KhnFZgSU72w7KAEE39yE53AJBjmRhfGS7yEdfgAo-ym8nPSqHxyNbaPru4mcGJPdywFJQTNzN-A0i4Ym_iSlpqJXgALpLUsvKsbsAifJir5NhTt0AvK6RDF5tH22L6gnyhJaremVdNhSXsJSKpZICvM7lvD5lajh52xTYQN-iFHBDYITXtjuz52nQ4n1SKiktOZ0RLI6L2TWWR8lnKg-xdY7TY2BglsC63dPMNwAwNCTJ-pD1U-zOrADeDPQo901Vu12-IyCQv786uH6L0OfKV0TvzUvs0xgzxKLciURGjJNDWgr0xp7JZWqzv2xmiHsmzj6QIXF3wzZzyml199-zc84KraYihNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=cFzkVtn9LgN8gMEM2LyrD-UyV7nX6K-MAsgmmwAN64eVrALuwtPY_4TKHtq-mRy-m5kje1oNW9uI0AxgCnuziEvulKngHF5en490S8QJRSObvr84rWQvGscgi2Q2PFgvritX9pU7gmT18bABgbLc_IA4aD2adLjo11wKYy4Av3_trSHNLzkIJOvxt-r3d3cD3eyq6usUTLopnptAnD068YoPiNBDNA-fz6ikSld6gLSNBedykLjUS0OgFW0UeNBA7JVZV0paKUrHRE8sOj49krW57Nso19UcJe3yE-y8D9hVibmT_rHgYSXwzbQvH0UWIntweMV2cIr9mTsqUo_rsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=cFzkVtn9LgN8gMEM2LyrD-UyV7nX6K-MAsgmmwAN64eVrALuwtPY_4TKHtq-mRy-m5kje1oNW9uI0AxgCnuziEvulKngHF5en490S8QJRSObvr84rWQvGscgi2Q2PFgvritX9pU7gmT18bABgbLc_IA4aD2adLjo11wKYy4Av3_trSHNLzkIJOvxt-r3d3cD3eyq6usUTLopnptAnD068YoPiNBDNA-fz6ikSld6gLSNBedykLjUS0OgFW0UeNBA7JVZV0paKUrHRE8sOj49krW57Nso19UcJe3yE-y8D9hVibmT_rHgYSXwzbQvH0UWIntweMV2cIr9mTsqUo_rsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEQk-fspydasFY6q4TGFJ8LEOmzjasj-F5RLZmVzIEacf9EqQ49Ju4i7SK6Qk41mz_Ak_i6p74OudpTJdmv8RVKgkBwlbrfyw9bFaSUYvSy-PS4WkdOeJ8g8cYCAujPH2mlLQGjffyjqPwa9gVFafHWF9qdACr7BowstiZb3hNBo7AwSqphLQKluPJRVGa1tL4jZ1_0-1PECgozk4qJeIddw8z7RqLuHZ1333yrLAy1i2tO02Dmr-BFfrW0FV0W88RMMA5xjQrcYq9RDGiqy_RKAH09j87EcAat2Z1SMZPCgBNEom23rA2Z0nuUz0JEcXO69wDWd70ll6MvOsO9t-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs_SN3XssTZg2IXbUnxIbgFgR9UdUP9eo1q5pdedUMbrgqvnbQ6mtgQWOfSF9aX1X8gTjS0AgVM6_hE2mvaM8WcaC9to3IewTDsd6jY3Ywi6LbMLmKlDRN14cWZ1v72L1saBfnyV1d6u-qQGUMBieatN7w4bgmNPfA9K6rq0nVcaP8gQrGbRZBvk_4wmrr4GclRU_INA0m1SgT08fX9_NUlD-s3DsCkjbiHC2bBI1PEZfp3X_jihWBL2NvfNdnrqb_Iy41qtOh0pwVPFT3tz_Ruisthv93Pr6Q8hboSgDlQ73MQRqSyBve2kQGH6GyPMKQGxif4sn1gxO4eESRPaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6yZGSw_NxZalTai16-qkCbtpO2QZUQ4iWEkV8dcjgqfJa0I-ornodHJu5QdaYiD0V_2rEk1c_ylsY-5B5Jyf9ivYynsqs41qyhNbbt7rvEZ6GwRjIRbxciR1WQQeSnMkZRCvaTdy_J4BMOzVFXrv4JhuVx4jOZTMuY-XUvtJnQSuDgLUVTwrkLQf73gnZa85fvcaN1su9afc8WNsf6CUcaJxXZ7WmiObdY9A_jLruQ_XsJ7PJQW24N2X6frxRbZbOkm23ELZ-9V-xlQmjy_eYntqRVdOTGhK94DI8jfz92mxJP_18UPYUnAQ_Hj2W0OB4-R9_vgPKVFrBp-92s3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-bahimNPHehGHv3VvM-gsssCCUCLbD0fPgpve8DI6f0E48Lx_LIHkLnFWA1gEFnni2ysm0JRqwYIgSL4zlPGPkj2RTywd0-lx0KjOktK7lNqSy7T1FgU6dfEDA9dITLpmhqtjsWn3VJvCy9Zswg94yqv0CzhTTjiz0f4v7lmNDOvWsKL_tDJpesnT9mS9bomUmG13xaGhqvBsXe7qPh6EkukOmPTmefp2YcNQsnOkRBPB86R2apX_dS6KM2rgiT7uOarjy6xj7qJN3hYDi0COXQPZNnoY0CrENriWz_kt_qx5OVaAVH0u92y14GteI6MXFR-XxOEOlzHgecd8rIgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHUKzHyMyWNJhwV2ogIWAFVs-S_Uf1HvOtFw5UQIzu4sp4YL4DYzw9Re1w1PCFGpsUoyX16tAH0gOqakTGlmupDBUSDY__4bNbaJv4VjRdXGpECtQ82HBiZwpFGfuMqN9_xJ4VrfDr4HdWNU-tn1QmtOZ_rekZkJi46GCQUYvFVXvC2vZ8rS7wJORndrFM1V80Uioj56CRUVCnRypu7lgQr_xV_GswOptkEmcP8xqv9U1nDpyj-UPizi0_qRBg-aQ_YXdesMI8cJTf_tbHr1quYptqUFvnQTE2DwaojUj9pY_zoiGYAeFpkvMdFmt_wSREQlD4O7JIiPy94_iicydg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4_5oeH2gsbTBNtbaV54qjiqcrWFiNwrvwNNNAzrhpDlwilVwPMyCJojT5zZ2JYnG1Uo7AKa7i6TTO0PLBApAAKbTSxSSBBrJ5hYw_XiHdeDRR_Ffqhjv3FOQingXSAgXM5L7gGeReFxYOEH8xf6d7re87QHgDe7G44DhR96oiLFqDlm7t7MjWLR93_VePq0SNpGXibTwpdEQG46D8ePKR861hqQb6OfPRt4Ssh28vMCPk_xGepgG50IEmh1CBgTNmG--woWIew_JJY3uAaNiD86JSg9Pla_fKQCthXhF1a56Rb-8F36vA6jAm494beWiLGcmP9IzehdNNGC2raE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=JXrlw85SHaWCEmsWsgLe-o8cqUFmomxkBR4wIJ_daxMBUyYtvKJcU58u-8i2gfPF90pIMfR_YLP1BG2sNbTXxSELECmqbqEuEf-PdIFjt5c3Z-HKLyQ3ahbTpgWNccWe_bS47k1K0UzLxBmbjIfgZexnV_gbMMxo_dJ-wYro_ohnVftpYZHGOP7U7rQiyuknvWvSoB9I_zZs1UWXfrcgqoQOINGI02Yn2hpFwwW64Z6raeMT6RUbo_UnJ1gT0voq8Whfce73fFtnmRHpCYXxYmgXFCUD_yIFHAOV-4WvxRqt7EI4MA3C_3CsLv4rojzxNHWj_dYRJcTj0SZNM4pikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=JXrlw85SHaWCEmsWsgLe-o8cqUFmomxkBR4wIJ_daxMBUyYtvKJcU58u-8i2gfPF90pIMfR_YLP1BG2sNbTXxSELECmqbqEuEf-PdIFjt5c3Z-HKLyQ3ahbTpgWNccWe_bS47k1K0UzLxBmbjIfgZexnV_gbMMxo_dJ-wYro_ohnVftpYZHGOP7U7rQiyuknvWvSoB9I_zZs1UWXfrcgqoQOINGI02Yn2hpFwwW64Z6raeMT6RUbo_UnJ1gT0voq8Whfce73fFtnmRHpCYXxYmgXFCUD_yIFHAOV-4WvxRqt7EI4MA3C_3CsLv4rojzxNHWj_dYRJcTj0SZNM4pikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh5X-kTN9vGN11JUOizEIoDabQtlNXm2ZEOK35gmgs14ar1a_d5IihuZ24NeGcHJzMDtLBiGFDEV3a_MuJNuwrj54PCAHddsJwJlu2x9RpQoo6Sj5PXmWX_L1ZH6AUj4Fpg2pUyVsCyh-TS26qXsmx7-wsIYjuCPIPeg4Sd1vlezgf4jTowde_TDYv0nxGUlo2UmvRfGA1tDrEps3YF9wlm4lSei9kVGbr6Vzo3YF0qgGHi93FlaTrpb_QpInC8GHhLp25XLiWFis37KfpIwg-p8Oh_fnY_DkBpEtL3XH7DLZZ5NRJRLjAVXt2co6lj2RBWFLoFvKVi4uFzoHtaxKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGEyaZhB02QOZ7Hw4supyAr3Q6r-BpludSZL4Gh1z6kSlhJbR38bbqb71zFyoG6OzmKQVaF6JxDdj3WvkLHcSpcQPeE7rR1Thi3XfBzgDe0ve6zSn-cqwHD4cIeKkSdnpPq-hYoea64J7BgVFcTTDGSGZYT6Ut_x0QVtPxj9fc9PcglA1MVubJHwcTjyLOf50OEIddXfqPZ-RYGa_HiiCl1CoRtf9nT6TwAzw9Rk4xTguwtSTiLIBx4HBj1cQxgAM2pcSY7tQY238qwf2P37Z4EJOJtJwNNp3GkssH0NmGe-VyJ3QxAkFoiPacsiaP56ZeWMu4e5DqrJ4_xw38_Y5ZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGEyaZhB02QOZ7Hw4supyAr3Q6r-BpludSZL4Gh1z6kSlhJbR38bbqb71zFyoG6OzmKQVaF6JxDdj3WvkLHcSpcQPeE7rR1Thi3XfBzgDe0ve6zSn-cqwHD4cIeKkSdnpPq-hYoea64J7BgVFcTTDGSGZYT6Ut_x0QVtPxj9fc9PcglA1MVubJHwcTjyLOf50OEIddXfqPZ-RYGa_HiiCl1CoRtf9nT6TwAzw9Rk4xTguwtSTiLIBx4HBj1cQxgAM2pcSY7tQY238qwf2P37Z4EJOJtJwNNp3GkssH0NmGe-VyJ3QxAkFoiPacsiaP56ZeWMu4e5DqrJ4_xw38_Y5ZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NxBuL-BQjdorPmVLykmQ6YzpX4G0hJ8Mv4M_8YuXcS3aHIx4kjym6kutBrwtB3I49lRfAc3Va4BI-Rly2aB__6x550SqazbBA-dbCTxAJlJLGoPSIr1KohUxy4UwqH1x7Kuk39v89B4zEfVog5xTNBJQNnAosVcjwt4eFehskFHzzHnydNJSdN3cgCX0pdVHwYk2E8ggtvqzMpbukjREPrVOaMfp3Kku_-P66j2Oil3ihnTe0lwUTU0iViXqYoqNkrLfv0cbNVXxB_cvj3FZCyk_p1L9RM0NWY0LmctGvGjeo181SFzQZD5q0MpWEudsNcdWVAT6dsU578cWWN58AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NxBuL-BQjdorPmVLykmQ6YzpX4G0hJ8Mv4M_8YuXcS3aHIx4kjym6kutBrwtB3I49lRfAc3Va4BI-Rly2aB__6x550SqazbBA-dbCTxAJlJLGoPSIr1KohUxy4UwqH1x7Kuk39v89B4zEfVog5xTNBJQNnAosVcjwt4eFehskFHzzHnydNJSdN3cgCX0pdVHwYk2E8ggtvqzMpbukjREPrVOaMfp3Kku_-P66j2Oil3ihnTe0lwUTU0iViXqYoqNkrLfv0cbNVXxB_cvj3FZCyk_p1L9RM0NWY0LmctGvGjeo181SFzQZD5q0MpWEudsNcdWVAT6dsU578cWWN58AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
