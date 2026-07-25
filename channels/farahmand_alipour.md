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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 12:59:04</div>
<hr>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5eWsWeSl16VVyJJHLGsbtXmGDd1giSzzBA5hVq58u07AjaGp4A2KUOgfh57Wi9NkWIy3upTSVfNAz7TihZLSVPxhmtajpAUhvczIvor6L4ruyaDsmKv1evieXqreUjWwMcydFFNsw7NvZEM0ZS8F2PCJH4qHWTd7iul1I7wHmv6BzYAV9iYX-9R-Pnml1u4f5j0eS5FRBg-oJBU42cNYOyokhoOU9xoOMstH15ZLZugfZcDllPk43T5P5xtiXArdebiXBBuli1y5gRsTqh3f37XP59g-Lr044vyq89xWQQ-fTxZGsfWozY-egX5QB9Yd4MDq_2FHkyhtSgWqjycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZyeY8hRrG6zpSYuBqgqhuLAYRHmOi8bNDP3sC3BH36FiEfkMeLWY30edsw3EMAzfnRsYaATrLwIeusZeCiGOP6dS7k5K0bGxCJgPExYl0b7bvzLeSPrw4sMi0A5eZLXfznC5DTr2EPehStOJ36kQcIafkbKdLE3kqPO1EFuf5vgsQ-QX3HLmQWzb9FAJRonA3IOpwke9voIHelkLLcKlI7AofJhYc72VWDaaBnRd-nBcAgcSbiUuS3yauYtPTliTQKk5go6H7eYaDxYxPNaaCshYfpfbgjhD40tByvSJReYEl58jwk1R2WXK4OJ7DtDICNZoemviE5xYpnehPVZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYwDUnfRY70RqPX7I03oQBfh_yiaYagzMhEcoAZYt2AdPiqW9RFO_LPunTLUAT29Yab5eKjd3TK3OJRV8C7rDrgmOd4WRUimFejxWnjyxWXcq626BIQ2p4UwOi2v2MMbeqf2sm7P9LjwRICU8oaIYufevOXphVafv3xLuQT0XDswnDoAEpqtODpDFmnlWMeZ-EPGHoQMOiHlXHbynKqAevQgvXPkrU4eYRGO9FuhKjQUm9X9q6idHF22qXkFINkz-Vs1e5WVOusuWAHWKEbO-dhdRtRvWOi_3PIG-SfUvK6NvQo4WUgXXeTiTQxSvgjW1EqPYnYEHJzlTQPF-QdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFxZdgIdZ3nhqzQyv9ZjtssKeSkYorsYemlYgybOQ1wlfiMi-pupIOsFsRVx5wKAv2hOghHdTw1G-IhxY-7MgWA4sr3T5_ejKWxSOndGG7N9VdGrOJub-Nrfsclhy_a6FDZMaNtPvvCF2ybGwkc1SbNrKUtN4PB_8hJW4ZjDgf_9la-DEGAyopdPNR4YA4rGrkdPG8SH-GU1FJBdC0Vk_qOv6PYcqqeuTPutoQ6dopuqMPx4pZlzwwJwseau0V-NN9bzh8yZuZ8PoePRANyv0-T61lBjyHVhSD90ROeN6-uHQ6T51TtNM9_Fxgd4TrQlGrPk3zjJMfgc7RT085YJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFX74a6nsStoFi_KitK4iAhz0dtkBtd2r4JhvNDxvW7yt81r7YPOTVMT2ABqCiTIxEWUhDdt2V1sbTtTx4ibwP7jl29ujqeo3JUozzbXM27h3S6lSW8NB9alT8KY9f1K6V25OIkitHbYn58j07rQqfcIHWFmeFF2kkz3eC_mUnIEYhMa587qV6dOEGmhavkVUuvzEOO4n9s1IisZZWccxBhs7hu2PCxQtTSv6coBbLX0JsMXJ4Vrxa-KB-AqpWc71x5k_X--BSVRNQvq3H3-gfFBNZBGBVVssPEdelyVxJki9RRXJbddR6Qz1KVEXTYXiRcFdRKKj5TcDO3BNhqCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyz8KQgG8dyLlA-lOtBtmtNJ15sXU_F_w2osYaNOFrW4mr---7KH2WgfIq01i4mY1DZp_nM-268dGPWcAmlu_YsswMSS6wMNjkoxWPqHIsCQ3-ezMsnzK4KAe1CtCn3Qjjar9xJ7TIn5-KtdsjK2EDaruMjnuRlt-BScjzklI43Gn-WGgl_BiCkwC4b2R97KNbpYLoi9t-bK6Ic_nyj2BTUZkQg62TMP1bK-PqjraY8Y4yATIcoWOK93jIrGY61mTfI4iB2K7BQyRs3Qi6TEZxVs78JhyoUSZQpLrr0_GyACdOLUgFyl47EmEPRZi_FBgpvW9xzk1hp77osAQpd5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=ko896pXBfWHHLQ3QHVi68rSWTff7W85D1bR9jbNQLgKewT6o0KeUEHKvDV9bTxOfE7ijyKITqEbmLUL3s4H7fLqFJ-8QDAbIuo67cNhbff2lPsAtbAoZdpVwhd4Z8ZT7usbI200xwwboIIc9WM2gd3GLqGF1o63BHv0Dpvg4_7ci-iGbf4mQLw5pJ3TFAnrXHibo17FtI8jq5t2tYoBZTHWStdcNNY_Cy5zXxa1DkyfXLj0bBfzWYOeNNDjBlgkzsbOAD3YLlWlE4fOuiZ4D3eDUWpiE37XfZwuAQ9NEwYqnTLGpvT9EtKKI7nKrv7ofPyz0A0hycuE3E9_EdFxp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbcaFRE6JbgCs4AeEp1IkKA1x3gRIXfuDlrrW_3-lDB1swXEAtNql7hTuiYNguKK3asYnyFfgoD_uJIIMwXLjyvLnpEEG5BM0NTvH5kOemS8eZDUcWs0Gws64SCa8C1cqq8Dt_vCQ2nU2DhjXopRRpaarnw3jUy_byDWm1JSYtj6z9hvW6OAom3UqfMzkFnPfkCxEKCX7MkE1Ua4w3rUA4AhF1Qua8eR6PofXRxBtUsSkEH4Yd3CVzrLfXT8iSUUFnSBg3UxL2aKSgh6b5tCrTpEam4OI8_uS_PAD1ieM8ocJTuCjCCK9NNhGYmLWRympV9z9gtVY5UGlGD5foJQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=jQVwvBt-Gg36-ImaRhFkJG19AoF5GId86iTJQicWMttR4Lo4fPfDyg-qG6YR6hwF3-WorPCmpbP5tjxsohTRe5SdXWu4M0o4f-Q89fOvPZAHU_BW8qspxMbO3bJk-mFfvhiKDfvwQms5Gd5thxNmwElZ-W8GVJuhbBnyBUhN-eUHnZbUIMP62Rn5rBgxf8wkNaiO59Q0eecC_EM_a2gfbOkopzNv-MSnspIICWKlWIVuLZcjBbKVKjVobUfD3gDgPgennwFPUpWBmtMD1UBLjaapDW_OItAZj_k3-AmH2w83mnhciuon9uttn1Z96Le7Rw8KafJouVPkQldo-mcR-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzWj-RHZcQYNuZhc6T5HSsYm9HMfRp9bPL51m_SxFRKW2BYnEnWpZ37TpPxZ5JsRBtZR7egTrulWoCFlTZlLN1k8L5hXHU5ClfTavw5T9kjaEekOYOGwVzyS22GneLpDR5zoqXxqY1LBC_DaD_6QRKssMlqfN3byCqf_jJRJgM7rd34UunS8MiY6Ql_PYWWuspShadOJLwFLFbwBRl1ovm_h_im-qcvpcg_yIXnd2zxwefRIIJfLjzcj3x2d6IhRIBCPXE0yjOtonxshRabg06s5mMFAUwztxoqn1rLuSwyO6cN4hLq4bMG1t1rna3cXFjOj5cQajqvCx97xQaGMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn9dKMR5fvO-ZWasFVV_OK6igM-n0w6wX1OpSzI48_9QIoIen65pjxBjJiihTePxpwbPVveeVwqyzIclJCOUX19f0pfVQrGJHKFk06NJmFAushBiClWeu671ijcb71tHvXBQ6jaQLNjMj0fDr1e0BL8pLnZAkpJqCQzSMkAyTcnoDFD2tlvRx61mpk2g3oGl6m9q9M9d5GP6Tppno5BujExI3MJjjqpXhasILhUE_fwtg08Z28UNSM6i7p2Etp8fmI2MFt_ExcRu_hl2GHUt4No43rRpWPZKVzxJFTKBsbIF_RdTzSNdI_DYZb1WDSUFItlLmUfi177tELCd-l7ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_hUx6gbujC3qprdCt_6yC_b_CSMG6P-1sFP4dQpKW1CBMD5UtFXrQvNYkIg3MaHL9_pfH6lyMvxH0bVbgf3ajT6Nnz4tEwxeMaimbWGiw6NEoaqMJTG2ongqb1lFDn2PwUu8X3G7NKJDBHCSxUnCdiFCgIZuvGQKtPvWQJsTvhOdDL08GL4lRtnPP9x50JaheMvmkr4vJhsO5KBqWtbZf0MVoRB429qaoOKVHm_zKn0D6Avy_wa6-rCzMs9bUK5Z7XbA_b5CWvZ_ybXEYc1avItcosduJkz1eTk6f7Xaq0dw7szeOmaqSIlVqCrwW0J2Qt5BbElHSHnmR6nVXjSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDfhuwUVA7D_vukw--punel5VYWFSWuPlGiBExSYEj--tTFv4eUzPBUX0LQiX_fcPh8G6V9z2nEac9WJzaC-FmE6hFPbLv43Yiz958Qjro4DN7VGFAjTLJh_m8JyODFYYmxAs7Ndio3phyQMKwfIaVFo0lPOpakaRQHWbniwzOfmhex0vrgFyLGvu78C3MAiXupDtA3e6yVXnIQBemQInE5mcqzH3YzNUVZD_CDhL8rHsNCw5YvKr_1CHbf5ul3PDzMktrqT8yKnXB1auS38vTfuLTb8DhGMTPAl9U3pCZCAGfh6NTHF8O5OxL_cAKFcZvZo6m3fU6jmjZQZDl0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfKoV0gTyaCZcUulO6eoMt__181eK1aDzHb7BK9cGQS99Dg907jlT9LXBT2HG0ku32WOusIa_Pj6dOzPabVq0SfCCFquY8ER9KrYh324K6YBX5lYyOKj1HW1lWw_7FEn0AMO4JDzgK7cl5GEUfqMbOGfeVT950G2Psl81WBmNQKy46XVCzBREiCoZfDQ6MmCBPATf_YeGfNcCo6ZvsTK47L9NQG_udQkI37tJ58L1Dk1963XZFgpe1B43bixT7i3WLbQ3efeJBeJlNkR4GhgNJoudo35qIxr7QOSJTo3tdK_D9i6QF-1ZxU09Fig_NlegPDytC2Gz2ULTFlUicMwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=IHrIS2j9oi-GDX6x7kQMPO2zOsrv_dA8E1Nta0ZMkxTIVFFQB-sO-CjlMFIfoiyXS67LUuRmbeNzkkJh2lmxs3X-zhzchkngVYq501P5lGN4WDYFbqCqQDCCbFfoYJuVWvv5iQmc5eE8NOFqADL6sIGUgfF57pfRWxXDZzhaO7lzKGbyCz2Uw_nFaCFeSDQ90nmJLG-AjfkcB2eOXhbvO9XFCT8724TxT4qPlBPNfeGMUSTZAf-86xi_4aZmeEjsnmMmrMKgwO_d0dSmd61hFSJgWitr3Wn8NZw1kWpLl05E4JikLgZKb6fYeFH0gOiNxguEu2nWp6n_VDD80F4LqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwXa9iUMlN-q7hM1IcNe1la2OzoB_pN0HVPwrukkvOm0_0da7dftCGn21pxlXsgVGfBkA2AGQQOaIQktLt9whYODABq66kzCNepfaaiblQ_rU2UceWsbfFV32XJMN9eXQ6145EW-zCsjA3GZDgxgDiouC61ZO0QkEz1rpOWEXXbNhUF3n3wTG0lNimh48Je93aOyQKkwe61h4YM9REblDLvxFmvbZbpWG24IsGnVAsIvxsP77bG4HdBTvHqZzaDDR0ksenxBf32XkbCKSFOzbW1aim4BH-NSWcd6E23LcjhsPd8Sq2FdPxtjZMPoo5Ij2YCXL_jl0hsH01bA9zcBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVISdUPgUwdx_eekRtNcjUJ9jQnnkLoaBE9uJtWXEfsHZ-w2SKNRbHIv5e4aA95PZOQV6qR3r0Oz-NrzLcHdf369SyRNy92XrAngYm6S0bVDDpDfhcny_u9Y0rREK5PHJ9UCpDM853B1EmrWaUPirBq6ogkUWvGutTWHA79zJ9DTPsIC2WY988fKysnjX2gK_WOY22gBZtBqzIIcoQeiNf18MjrkqyxY3msOIIZIiuEDCEDQ1qmtkUH0qXxiAacQx0_QvYYFev-wJk7BBICU2fW45f2lwZWD1ug54ZzbNTH1KggEYhDWc6au-Vaw0vajBKMLj0pFwOdF6agfaGH00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MgEX6_bH5RzNPVZUIR5vGtv1Irvd7tsHgkrdi4XkGh9nAdst0JHm5Ri5WhIfjVHBxAoKbFRPlUdaNQgVxftsrZH0JbeH8fu7i84cYVc5pivJDSqUWwMPpweLCa-IRpyMa_Rrb2ThnGyC2BF-iFqHiUfM2GOvbCGzmtVXO7WaFvAO6QkqXrs1DRB-3RhH421N0MPsm2wOwo-kiiztyx1Z1FTZnOSHl8m-N46N_SglgKOSli87FxCuPdWkx3-WD26rSz2BBzv_Xerqe4bM-Aa4OgKuGmLu2he1E9QHIWOlflPfP_mjBJWjqmMIvjKGfQP9y1x9bXuaaBm0ckuhHOE-RXXahr-pVM2D-bspjCIhmc7DRXgtrFej-nlRmoUpudmNjbkJ973UvQw5qpV_fVsic92IV3JPfB70e3afvT6zKTi-nIPUpPOpP65JDEq0-MUc8KWEBANmDYSm6JETaxzxhjOEHP87Ayvwl_WsAEeMjGF6iB-nFsixOMLbfxnIBmv5wYxoQ9im28cfhuSLr_Jj4BquaPzsLX__Hc0f86R4H0_Yk3a0ExlIBxOrmZaFuxg2xobIMp3QGg8VIXeiPaZHzs28Z3h_w2QBCcZwIzaSQPZfBduaSxYuv26yWuvB6Nz4ns5o9ilVqKIyV8sD4Jp2WGbJXiaUMEVOrbtpnQX0Rno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=MgEX6_bH5RzNPVZUIR5vGtv1Irvd7tsHgkrdi4XkGh9nAdst0JHm5Ri5WhIfjVHBxAoKbFRPlUdaNQgVxftsrZH0JbeH8fu7i84cYVc5pivJDSqUWwMPpweLCa-IRpyMa_Rrb2ThnGyC2BF-iFqHiUfM2GOvbCGzmtVXO7WaFvAO6QkqXrs1DRB-3RhH421N0MPsm2wOwo-kiiztyx1Z1FTZnOSHl8m-N46N_SglgKOSli87FxCuPdWkx3-WD26rSz2BBzv_Xerqe4bM-Aa4OgKuGmLu2he1E9QHIWOlflPfP_mjBJWjqmMIvjKGfQP9y1x9bXuaaBm0ckuhHOE-RXXahr-pVM2D-bspjCIhmc7DRXgtrFej-nlRmoUpudmNjbkJ973UvQw5qpV_fVsic92IV3JPfB70e3afvT6zKTi-nIPUpPOpP65JDEq0-MUc8KWEBANmDYSm6JETaxzxhjOEHP87Ayvwl_WsAEeMjGF6iB-nFsixOMLbfxnIBmv5wYxoQ9im28cfhuSLr_Jj4BquaPzsLX__Hc0f86R4H0_Yk3a0ExlIBxOrmZaFuxg2xobIMp3QGg8VIXeiPaZHzs28Z3h_w2QBCcZwIzaSQPZfBduaSxYuv26yWuvB6Nz4ns5o9ilVqKIyV8sD4Jp2WGbJXiaUMEVOrbtpnQX0Rno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=ilpmlQg1ztkVxfA8VgbMWDzEYqINwTDskETUmtdsKRztTyM00eg1mAb_vibvB5UVF7_au_bf1BWQLUlx7w9xTCN8yRsEavyDmAKaJDOhtigg-OrmBCFb5lZOqZrBm7zZXQyv0rmdFQ1V4cpIYyTHxRyqtsOSrFEX32zo23DrCkgrOYlu-haOuW6xiuvnqIM6W1vuOi9vKuZtdXRPZOMGoS7WXG4fZ6QRorNuqtoNswrJHk6noswswq-g-Ky5UHjQV1e-1FVdUKgv7Ph2MoGLi8cIvE5GqzKPcYHQq3QqLJQgEOFjFPCz7ArVTs-B1UBgIm3qcvw-55Apt-zRVg_iNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=ilpmlQg1ztkVxfA8VgbMWDzEYqINwTDskETUmtdsKRztTyM00eg1mAb_vibvB5UVF7_au_bf1BWQLUlx7w9xTCN8yRsEavyDmAKaJDOhtigg-OrmBCFb5lZOqZrBm7zZXQyv0rmdFQ1V4cpIYyTHxRyqtsOSrFEX32zo23DrCkgrOYlu-haOuW6xiuvnqIM6W1vuOi9vKuZtdXRPZOMGoS7WXG4fZ6QRorNuqtoNswrJHk6noswswq-g-Ky5UHjQV1e-1FVdUKgv7Ph2MoGLi8cIvE5GqzKPcYHQq3QqLJQgEOFjFPCz7ArVTs-B1UBgIm3qcvw-55Apt-zRVg_iNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiXCOt_Hj9BfeMxyUxyLG2Hro9pKv3sJ0Xf53Bw3hiss91g-4GTw0_ZQ9uutHwEF8Ars9n0lSlS43Y8TiPBhavLG9HXXFLuE3lWrRi22146jMhgpTZZgOUTrkszcrnwJ9UEQY7-lvQR8bVbVQoCo2gsfltv5iDMj_Sy3hJLGTG8QOnkzSmQo91v5X640hi6uze3ArX8_v6FKENNTC-L5U1sibceRThISZqfWQ5YPsNL6OpnXvA0zIhxGR_uqs4Gho5xifFROebQ8t_UE6j9gS_ObraidvW_kWmRVRnDjKIKi5flAxjTlOPT09g6EWNpykMLWxNtOwYEHfcoKR4nSG5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiXCOt_Hj9BfeMxyUxyLG2Hro9pKv3sJ0Xf53Bw3hiss91g-4GTw0_ZQ9uutHwEF8Ars9n0lSlS43Y8TiPBhavLG9HXXFLuE3lWrRi22146jMhgpTZZgOUTrkszcrnwJ9UEQY7-lvQR8bVbVQoCo2gsfltv5iDMj_Sy3hJLGTG8QOnkzSmQo91v5X640hi6uze3ArX8_v6FKENNTC-L5U1sibceRThISZqfWQ5YPsNL6OpnXvA0zIhxGR_uqs4Gho5xifFROebQ8t_UE6j9gS_ObraidvW_kWmRVRnDjKIKi5flAxjTlOPT09g6EWNpykMLWxNtOwYEHfcoKR4nSG5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt8RrGXrsRfw6f7nJ5qN9bWqYDBTz3z7BWt-3KGUu-ySpOsT7pSVXPz0KxRdEn0upAzptyZpDt2TYyueb7jE7b-r-Z7RJWO1lgFmuEXc3EAEsKfudpLPiXGoixidYQvEIxef7R1A8rbcmuhm8XWraKercWTAtRpQNuoN-qWbnucmFtrAoZ3jw_0_xciVo5NNjXaA59nh0jKu03WGg9N7hibigKcRvJOlVXD_nFWOf0Xf2mLm1REwxxvCJFwuLBBylD-IZk_azqs2DzaF_mbcoxdj0h71ROn3rUmJuSzN9ehMZrXd2gixz5qj8ha1ZmOkwtUamTAKzmSApG-8zv_ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrubPnnOpmlpFoOvz726AwgaP6tBRqT8LcnuFLueMf5iLTTj7cAnqGl4LD6GNxRpLK7bp65ilMIPdsVFny2nL6Ci6fweTYfEVfMGm4Z8TYEOfNCLK8qXirLMNlbfws3m6ROxGIpbDFjCpy7gjRdKN-8R6zJLsNwe_Dqac8QBfr88owGaTuVjLQQYzYqsLiREie5fTXJv2PT29EzEear20YiYh1hMuPQxVWwA4YlR0At5w4_Z2E5X1Y3T8Wcr1KNQJPuzZJe8JH_gdq93ydQ03toUm0k9nJRyYkq1hWXfMIarA5BjfWYZh1-K7Varb-ELZn1A4EYahJjatuSCbF59hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2WefPb2phj4cmgZCTIaWuLTbNrADB4JvCwWCqpINSTojTaE0erCFjnM5kqdJ6BtDT79808hCkTDMZKVquREc7V-GWLqeBde1viBma2ZCcxSkHwraXPASjkbULQO4dLos1XYFbW2eR2yhhRzxmS1pD5M-npCprehE_nI__jku8l3V6_7GbnAykfInFuEVwUiExVJlJrR__kLii1OR2H4DGecn4Ot8Pfp9wDp_LNynF8Kmir-4oBPpgC1d7vue-p_aHVkKSD2Ex1GX5IkDX0tDp34Vcv-nEXj7fXL7lquTUIZfY4Gf013xZaS6I01kk2I0mEERkJiH7Hl_z4XvLkRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QI1nAQT6G1Bqj_tUK_g4xSij3S6mwvOFLjVIIK9_pid_0T8pfvUGKu5wE7G2NWqK4B6PVQYn0rvfSs2c3KDNdyV8G0qW_kavdxLFDAolWNrMc7unzEndGwJ-PVXLq_wx5-rjmGU5e95QFFzhV8BREmcXtvMMVX33Cs3Qwb7yB2CLGDc-WBMdz_yZxEtpGuaTDaTQ30pqwZGY68ny7b1q3tT4KoNxr1E3PGa9re5rL34AQOcn07ox6gl19_GtMjJvbIZ90uIJ2U2wU3sV2omvp2X3zW2Wxx80e_sWKGmi52cEPGq4yrzyN1iZHsmUk0uALhRuo8JRoqGC8b6taehXQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=QI1nAQT6G1Bqj_tUK_g4xSij3S6mwvOFLjVIIK9_pid_0T8pfvUGKu5wE7G2NWqK4B6PVQYn0rvfSs2c3KDNdyV8G0qW_kavdxLFDAolWNrMc7unzEndGwJ-PVXLq_wx5-rjmGU5e95QFFzhV8BREmcXtvMMVX33Cs3Qwb7yB2CLGDc-WBMdz_yZxEtpGuaTDaTQ30pqwZGY68ny7b1q3tT4KoNxr1E3PGa9re5rL34AQOcn07ox6gl19_GtMjJvbIZ90uIJ2U2wU3sV2omvp2X3zW2Wxx80e_sWKGmi52cEPGq4yrzyN1iZHsmUk0uALhRuo8JRoqGC8b6taehXQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw1WPk6o297T5LMaoi_v_ce0IwJQa4zfwuXmnfeJK1FqGqUAjZcXFRVkhsLnG4c8XdPv6hbPVJAPoAAKQ3wVViVUSbOn3S9meetKwC1QxMG4_N10vt0DwNwbnf25XQYeAgdSxx1I3tGpXR4vCPd8SaeqODb7XNTi8UeR3STGpIdT8ypFpdJvPwliBGYTn_sGzY3Q0aTnvGqBRRqfEkDF7OVjPS42QGcCjnlohX14lB6yKOKjg5X4LE_8MoGC6vdPp8rS2broCgH9kdtmF-pjLFrH4PskFEXNZ2dYSoJXinVzWNHcT_IaiRVBsv56LgH0Z-NRuk9GGremNYUpxATdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-VKxPTjO2figZ7HRhJ4MmHxb8pV1FOGgsoVzLwe9WdPzG7QMTl4AkHZp-bRM4UWSzb5HEi0IdhHfluedbSRrSgS8dQ_L4EvWMW01bUlbsWoKrShcLaUBohuhfB-oFoYFiFbOfYc24qNS8SgWHt6XBIY0d2QoojEgbxtXowSw7o0FIUo7sjQlBOELP_99w3My3F-w-dcX8WRI8ANxYGJI_3teoHDkpSlDy7_kSJiO3WqlXvEXrv_F9QYUKH80b_E0svBe4CWYog5YGHLEmlO06U_vtWwvfcbGRSlTcf1zUQLPyN0gYNF4vZI_7wuyGtHr-y8nRgKbGXxIjfD28FfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdLVxnQG-iQ-vBwlD4pgVksP5OmT_pxX9hZ2zcoXVR0k0XeoncXaFAJ55NsTR_6xqYQm9NfaSSFC-A1uqeKleApaqDYdwWt-vkjhxA6AKbyTKAv243xG2M4ow70-KUpqX0eneCB-Q8JCl0p-0BJmoEOUTi80UuT79LHN7jdgohD3-3zX39ZB-zamGOkoh7N7tmJNIgcCYOgDgxg6iinqdAkpAYreIZzAjv7axxSEOOfE-ltaHv4U5B0wfOjmh_wLcrVkIZ-q9MAqcJBUKbMZu9ZxAxzD-LiCXNr1Hv9WMF5diic4Mn9wPcbcxmzwv1C5Vlu7EwpT7DTBd2NjI9K2tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mzvz-oLcY2sH7vZY7ofYUEVO5QgOViPrWpqaK-mihFY1yDchQUh0F2I1vM1MxvVgwqYXCD6DfOlRHUC95xfhViczWIK4kk4EBDhtBMYAwTIXoKpuRleqBslOFWdgwJs-soEIMNq3Zqlo3OMog1zSww77qBZYXYMV2ko2U3YDjcdd1j74ScGi6ZoFxrTaf_NWkpFSq_Bt4os96sntQQofh6GQvQLknwuTBrbpHtKZ0sJbgRJMJO7fD1r_gcFOrlnH7HH2nqhoWleJiMSsWpVDTmFUXjFicJDwvx7XTEolFCx6yR5ZwNxjQbUaGJbLyVj3EDgZEOAtqloqNRmAIHOL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=JT4Mo92jd_ffOefuth-oQQdhTHukghpJff8SkMSw-pyxqK_cGgiqS7qiYpx1agW_WaHgTBmkuW-oNPDm-lk-gFnVyu3FlNfuK5yt3ZpqkNO1n5T19bityA-8TvEGNjtynLyTeJKy50TQqzJhPJnvF_teieyJGaG8YaoRFaC4aUML6ZxXGVk1mcgb77bDoPxoQ8YgqHnc_Q8bgpx077mI9XlplsdnylqPM_NN12ydRGxcxEjk8qJmdh8fHgXuZn3ybbhJwsiuBabPpsQZ_MKHsgV3CnVD0-DolqlQ8FayYbGH1sgNyxndIRLB3-zYcTdvZgvAxsaQc7L7ZT5X004YQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=JT4Mo92jd_ffOefuth-oQQdhTHukghpJff8SkMSw-pyxqK_cGgiqS7qiYpx1agW_WaHgTBmkuW-oNPDm-lk-gFnVyu3FlNfuK5yt3ZpqkNO1n5T19bityA-8TvEGNjtynLyTeJKy50TQqzJhPJnvF_teieyJGaG8YaoRFaC4aUML6ZxXGVk1mcgb77bDoPxoQ8YgqHnc_Q8bgpx077mI9XlplsdnylqPM_NN12ydRGxcxEjk8qJmdh8fHgXuZn3ybbhJwsiuBabPpsQZ_MKHsgV3CnVD0-DolqlQ8FayYbGH1sgNyxndIRLB3-zYcTdvZgvAxsaQc7L7ZT5X004YQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=q_nHs21LWJszWjIPCUYSr3KpUr1I8ZVRXlwV4nEFVRIgFrZSgGw17zS4IhyEWUdUjqfIzmS_2orOXv4g7SMy-Q1rSbBlRmHtq_I-1C9QsV4imSPDwq6NWByTIcdDSQgmIQP2L253QdKTsW_bV-5EPi9VZa75Ptf0NwN8FaTCuKL_A6Htg_JJZg4Du1FRhNp3a7WKVEuYsUQKe14Fkaau5mF58s6_GvMmbS_Tp4WVwW4erT7KKroP3IFX5RpkRpALTRywGke3jkZIF1g4435-RnYRBRYx3Ypm8TOXPwkxgZ4bWgJEPhOJfH89cTUDkJvgeKRI6u_xexY7737dOEzoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=q_nHs21LWJszWjIPCUYSr3KpUr1I8ZVRXlwV4nEFVRIgFrZSgGw17zS4IhyEWUdUjqfIzmS_2orOXv4g7SMy-Q1rSbBlRmHtq_I-1C9QsV4imSPDwq6NWByTIcdDSQgmIQP2L253QdKTsW_bV-5EPi9VZa75Ptf0NwN8FaTCuKL_A6Htg_JJZg4Du1FRhNp3a7WKVEuYsUQKe14Fkaau5mF58s6_GvMmbS_Tp4WVwW4erT7KKroP3IFX5RpkRpALTRywGke3jkZIF1g4435-RnYRBRYx3Ypm8TOXPwkxgZ4bWgJEPhOJfH89cTUDkJvgeKRI6u_xexY7737dOEzoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=C1D17nkJzFVwpo5Mq3aKFfhlJkbGBQL7aNxiDOndkbUVRslCUU1LnsSDcTuphD8DzjTwO7jntJQDXWJwNun21ZPNsZ6EJUD8DpZE4hSaYRkCnI9AmYkDfyfA_7NPX_9j9yPROxdH4vcbCCIW2kHw-i0d5_v4CKg0NCRc8gkByMTOJSrZFrJJUwpx9exxRIze8oJXpISUz-NUdvbWI0sonRk6y-FQz9yIQG8toWiRnrtTJ-AEodoK7qdkIKbLjR4DEwssSwlE0Ism5W_aTDPQXlQzT_6sINTjsinp85fjcT1sSElS_8he7hxB_Nwg-antMmCbbqCSrRiK4dJMJe7rqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=C1D17nkJzFVwpo5Mq3aKFfhlJkbGBQL7aNxiDOndkbUVRslCUU1LnsSDcTuphD8DzjTwO7jntJQDXWJwNun21ZPNsZ6EJUD8DpZE4hSaYRkCnI9AmYkDfyfA_7NPX_9j9yPROxdH4vcbCCIW2kHw-i0d5_v4CKg0NCRc8gkByMTOJSrZFrJJUwpx9exxRIze8oJXpISUz-NUdvbWI0sonRk6y-FQz9yIQG8toWiRnrtTJ-AEodoK7qdkIKbLjR4DEwssSwlE0Ism5W_aTDPQXlQzT_6sINTjsinp85fjcT1sSElS_8he7hxB_Nwg-antMmCbbqCSrRiK4dJMJe7rqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbUJvZX67pDuJ2s1w-mQ4qxBDFp8Cg0UmETWt22OXuLnslxXh4kZYGPdYLfkwJsEDmCUaNs_xBo8312HFjJno1YH8UdZPT5rSAAKAhSuCRZUGx1XL8qqx75v8bX59YQ03xNa6GTnzNRv1qnl4A7PM7BK8CUZrdZKvn7a6r4dIzUQ5D9SxuXHM-gBARwX1MzOsy_wgrB1ERKCvKgn2nzeib9ykduBjSgFJPWM1xQJ1SEbOocXnFL52QerWTUsGB9nWxTL-SeP5ZgqPWXS82DHPYlWR-EsjmS7wsL600oU6R3_4lmfz8q6_rEl5UM_nxHHo-Aaks8-EJUgRXL8SDkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h4ZB6BBTqjWDWCUeKjfQXJhV0SyF2rEy2nMuJ9bLDQmnWwofdb847GY44Awd6QnEavDkRDfjRE1r0iKq8lWU8_J24u2gMu06JNzEbGny8wE1Cx1N8JXACDMwX3q3l3ZVroObij37ZzJhWJhCb0LSCj_kRzVbNCpnptG0wkLjJx-8nkYo16lDNcm2J8HBlzqb6Pz-gsgjqIfF1AGvkNpfrdx__A4A4IgUZTaFm12fZ71B0CerWDsQxxDda7WRBE7TAGv-FKkUchWUnYMyX4TLkjd8C3ZYoHigRjhipSxNUsde4bcMoiWXvNFkjkVdyOew5sJvwizXzxSdJ4fDIKr_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h4ZB6BBTqjWDWCUeKjfQXJhV0SyF2rEy2nMuJ9bLDQmnWwofdb847GY44Awd6QnEavDkRDfjRE1r0iKq8lWU8_J24u2gMu06JNzEbGny8wE1Cx1N8JXACDMwX3q3l3ZVroObij37ZzJhWJhCb0LSCj_kRzVbNCpnptG0wkLjJx-8nkYo16lDNcm2J8HBlzqb6Pz-gsgjqIfF1AGvkNpfrdx__A4A4IgUZTaFm12fZ71B0CerWDsQxxDda7WRBE7TAGv-FKkUchWUnYMyX4TLkjd8C3ZYoHigRjhipSxNUsde4bcMoiWXvNFkjkVdyOew5sJvwizXzxSdJ4fDIKr_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ZUOmA2NMACvfcr0G5KFjhEFcv_y5kzrIFtCgxgGH_HYwfJUMzPrTyq8qpAHY2T57DjgegeJ9woLJZC81uWLkzuEjVLJz8VcBFJz2f2l-d-Pij7iI-feeenqFaDHua_TXo4YLDUOGO8KR6OYP_XGlPhjQlJq8NAyHdz1E5qMWepEYRHc7OZMZ_ZyeBmvjkog6yz9-09fVnXaxEsJvNgUyzuZtbFtZUOnlZgn7Vr_OiK3o-DjCX1K1aG-EmeoXZVBhFH_cpDfBD7PT6256FuD9jFWMe3mBlIQAn31BFD0GrDQ0XryT0ahw4NXFrDfVZF43hq8tq1AnghLZxlNmYJQ7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=ZUOmA2NMACvfcr0G5KFjhEFcv_y5kzrIFtCgxgGH_HYwfJUMzPrTyq8qpAHY2T57DjgegeJ9woLJZC81uWLkzuEjVLJz8VcBFJz2f2l-d-Pij7iI-feeenqFaDHua_TXo4YLDUOGO8KR6OYP_XGlPhjQlJq8NAyHdz1E5qMWepEYRHc7OZMZ_ZyeBmvjkog6yz9-09fVnXaxEsJvNgUyzuZtbFtZUOnlZgn7Vr_OiK3o-DjCX1K1aG-EmeoXZVBhFH_cpDfBD7PT6256FuD9jFWMe3mBlIQAn31BFD0GrDQ0XryT0ahw4NXFrDfVZF43hq8tq1AnghLZxlNmYJQ7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZLA1t5uHix9HNI9xFd-8gt4NlYALuT-EIQSusyzAxUuLXE2i_WQDJwVu_CrmxT_MrHHguJhSNRw5ph_RbHsbNkxu4I4G4QaSy4m_gTQ6XkfBeqP5yQfE2eFPBbl4SykdULafPHepJS_iB10lsDuQH9DCthFV9N_0MzQZGmQGhgRBs54it3Zw2bvS5N3rvFlM8WELQxJrQlymu-X1n4eD8pOEx0oL3vGJ6T-Y5POAP_bbC8CkVo1glvVVRt0dsJFheVnAH_aU2C4rvL56Ky5_fafIs8Eepbh4yjRgsq4tn7sZUgf1ylbE1eN1cY1t4qLyamYGw96lOt7ahU9vKvkn-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=ZLA1t5uHix9HNI9xFd-8gt4NlYALuT-EIQSusyzAxUuLXE2i_WQDJwVu_CrmxT_MrHHguJhSNRw5ph_RbHsbNkxu4I4G4QaSy4m_gTQ6XkfBeqP5yQfE2eFPBbl4SykdULafPHepJS_iB10lsDuQH9DCthFV9N_0MzQZGmQGhgRBs54it3Zw2bvS5N3rvFlM8WELQxJrQlymu-X1n4eD8pOEx0oL3vGJ6T-Y5POAP_bbC8CkVo1glvVVRt0dsJFheVnAH_aU2C4rvL56Ky5_fafIs8Eepbh4yjRgsq4tn7sZUgf1ylbE1eN1cY1t4qLyamYGw96lOt7ahU9vKvkn-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=LfdBZuaamMUxX2LQ1cLCmqGZncKczELUFr8C4B2_Ns-v0goryO8sWt3kGItK7qMpbRkWBp7g_GnyjEbSFBolKX2prHAT5QDe4qQTgEQh9zmvNuixFKlWREbdLG60tq6w6g8Lc_5TO8w4ZYq55C8kPCjEPWP9As8N5eZrsCcmLaKcm-8c1vvEVUP_GxKrec5M1wmayPlQweJylJYlEMDCNfbZydFxKAk1GYxRsi6UHAfPfGyFl_RsPPJIBHMw_NlLCYeB3AMGUz_9lHG_ql1LExo4sV-2YWMFwP0IS_bh2u5B0F34-b0hkiaPjVkmp5LZ3k5Z0zW60B9KYSZ5ZEF3j2j0JkWOmgjhtget4A2mYVt1pOg0FU1p-6QQad9wBnVqJNdWGGMArrzgOO3IWVxNU4UieBGjph9CT8ERaAGNk5SY8l4ijASFIDsfP9xsD4ZkTQRLppAPHj5eBS9nJxs4_LflqbKXexSwO-BAj5ydCAe1rIFgLaISzzgLKm39NzT4ncbOZnRlazV72Y2IaI8_F4hb6lt6gS-kbU05MxX5gz18q2W3OcLWYBTXFwfAmCEf3epYMr-Ce2vVJIeomeJzg-qV5ds5LTesgfdRAM980wY4GA4C572Ez7w7U8Cp3_MCIJfHbezb76_lCqKnhN_njOJb_0M_AkNUfKbZiM3R4L4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=LfdBZuaamMUxX2LQ1cLCmqGZncKczELUFr8C4B2_Ns-v0goryO8sWt3kGItK7qMpbRkWBp7g_GnyjEbSFBolKX2prHAT5QDe4qQTgEQh9zmvNuixFKlWREbdLG60tq6w6g8Lc_5TO8w4ZYq55C8kPCjEPWP9As8N5eZrsCcmLaKcm-8c1vvEVUP_GxKrec5M1wmayPlQweJylJYlEMDCNfbZydFxKAk1GYxRsi6UHAfPfGyFl_RsPPJIBHMw_NlLCYeB3AMGUz_9lHG_ql1LExo4sV-2YWMFwP0IS_bh2u5B0F34-b0hkiaPjVkmp5LZ3k5Z0zW60B9KYSZ5ZEF3j2j0JkWOmgjhtget4A2mYVt1pOg0FU1p-6QQad9wBnVqJNdWGGMArrzgOO3IWVxNU4UieBGjph9CT8ERaAGNk5SY8l4ijASFIDsfP9xsD4ZkTQRLppAPHj5eBS9nJxs4_LflqbKXexSwO-BAj5ydCAe1rIFgLaISzzgLKm39NzT4ncbOZnRlazV72Y2IaI8_F4hb6lt6gS-kbU05MxX5gz18q2W3OcLWYBTXFwfAmCEf3epYMr-Ce2vVJIeomeJzg-qV5ds5LTesgfdRAM980wY4GA4C572Ez7w7U8Cp3_MCIJfHbezb76_lCqKnhN_njOJb_0M_AkNUfKbZiM3R4L4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Ap55-qE_2C6GE0ZfcmXdA09ithXiajx3ZoaLi2AdMVnrhUrdFjQJpicT6G-Gm28NX6GDrI1CW2lyS2gY3u1wGVQBGl1tPg50MRl4uAlPQq718fLaNsoK-W67vFRiaTSzCrbmLMWKBAO68CqaoO-CCNCPIAOMcA9YJSEmPRAcUINTWZZVH1g3ufycWBiEA8ptsEq3ylr43mTNhTDHWEKHd72JmpYWJ146HxbdxxMvNXamEhix0rx4DcB9rVUy_W92qB6AjIZ7mRcJCTh7MeTR1Oki_4dilcXTE6QhWMjLzvDITTgskxCinmQB9D_kZh8PgFpwls-Lqh3_PQWfURVFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=Ap55-qE_2C6GE0ZfcmXdA09ithXiajx3ZoaLi2AdMVnrhUrdFjQJpicT6G-Gm28NX6GDrI1CW2lyS2gY3u1wGVQBGl1tPg50MRl4uAlPQq718fLaNsoK-W67vFRiaTSzCrbmLMWKBAO68CqaoO-CCNCPIAOMcA9YJSEmPRAcUINTWZZVH1g3ufycWBiEA8ptsEq3ylr43mTNhTDHWEKHd72JmpYWJ146HxbdxxMvNXamEhix0rx4DcB9rVUy_W92qB6AjIZ7mRcJCTh7MeTR1Oki_4dilcXTE6QhWMjLzvDITTgskxCinmQB9D_kZh8PgFpwls-Lqh3_PQWfURVFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=TSN0ucCKXwrl_U-dWYX8OQdMxWKuY4nvhV2iKrGA81uUIlfq7VUgCDcY3xu16_avJI1HMmOTiEb6OVQS4sEirUuntCDO4I6cWLcP8qiiXZlQHjd5C437MweroPEb_lxryq1D0Cpz73Bg4In0Z5F17taEjOLC6QJtOhpYAcZLQp-x8dUjcu66dp_nCbSrnM9R-AUOZWe7wGVK6JX7eekAjkuUnMt2p-_tSWbEd7eFYV-0bosprQSwR57aNfF9H8btLU8cm4RTFiFlAUlW1tv04ourdzA3ic2S1wh3u8eE2dF5vM7oCkbAcb-cYQwNvx_bausplS2wvsHVSByygAocew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=TSN0ucCKXwrl_U-dWYX8OQdMxWKuY4nvhV2iKrGA81uUIlfq7VUgCDcY3xu16_avJI1HMmOTiEb6OVQS4sEirUuntCDO4I6cWLcP8qiiXZlQHjd5C437MweroPEb_lxryq1D0Cpz73Bg4In0Z5F17taEjOLC6QJtOhpYAcZLQp-x8dUjcu66dp_nCbSrnM9R-AUOZWe7wGVK6JX7eekAjkuUnMt2p-_tSWbEd7eFYV-0bosprQSwR57aNfF9H8btLU8cm4RTFiFlAUlW1tv04ourdzA3ic2S1wh3u8eE2dF5vM7oCkbAcb-cYQwNvx_bausplS2wvsHVSByygAocew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF0STWQ23g8g7NV7AQw1he3AY318HJl1U_e_WatJlxdR6dZzt7H8-gK296v2eQ_uttgfWST_RphUDFx5IQbYtnR9DPf02TL54j2g8YUJbjsBImRtUqqxXEeWlP3eAjHqEBSowdLYIMFGmxuJrqde8g3r2fg-yU4gpgeCDpTNRO1IIY2434M4V1xB4argOMTi6tzwh3fuZM6tqI3hxuk6fSPmcupxK8HKG6lGMJKgTX-fmbKg9UIzdymXUWeVgSxD1ZufMDQ_UgMx4RZS1JdH_UuFD6EJTJqImHR4ZBm_PD73Lx6N4YDyBgRptsjNJXxB1vlltf4z-cph4QjgF9g6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs8ySiXABUPBUHzjesZVK-WFBCzJo798m8fogLB4IfMZcFoNAXr7YeNfOdj1laGO-T0L1aHqkQ-SLFu_h1fbnr9smDMkLDiubKAh-5Wh3RAuX0aHQZbN5kISHKO-0Qxv6t2CO6-E_VzVq-TrgCgy2XHiOf0iukY92dLlYzSC06r4OKiraxh5ZJjT46sP3CzVo49ahoZd4yAFfqkEvsv9xOC5pHBOP4an47sA_tWkbtuUWskalN1xib5VJmpCpx28q8N4MF2zJELAKqku1_kIR7GtpzJ3T-6lJkYQGSeHaQKsZxDaG8P5t6z6iehDyj9WsfRmIDkjJti0X690wuNVYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=k1A1V-Hg5khFEh_SgTBQFhA3UmPOiilZBasUoWOLGDBBjt1E-6to_ud8aP8hVUNTXFtpbEgcXEepbiUPO4-QHA_P7t4uh-Z3FRWyCtbdZOvcCLaJeSXEHQNF6TSQCyVGnmqbhb04MHqle_2x80wlrAMQGi7ajJwNY_qMK-1OpD8Qfq5E6gUAzS6_WRn0LeFBTU4Z91HtX73fPBozk45akj7l06KjOAWpMii9R1PJDYfHcNgZ8daq5YAp6jdfOjxixWUF9iUAsJOdllvqK6YgpdFy3XXiSKS7Z_z-ve9jcD67ATVYkVV9ChRCPgV1uHW07JG7t3jZuxDimFbYmeWa4HqQD0kxEVx1cTUjWCDKRINxSveKNmiDJG8nV6AYc2C-ThETymLjTlaw2IH0Jz4zpB9Lxjz4Waa1lrC6PClIAlpoeAhu0TnMJGm7K9ueiAie0EyKeQt8jTq88J6PyMfRsjjiq0ja7aNEHuZzVCjer1_vw6kk_xTmfWcNSLJ-8nd92eV1mjBGxZggsWz2jJLxo2EKpKzNyRmrUXMLtP_yWzM5oi81EEtgL_fczqoJafR99vIjO_F2_L5E453B7xIAzaz4PhGaLStKM5_H81wR6k8m6n1ENMYWBdtDtft7SbwtMWWR00xHdzw5Q2m0iIF5sdfGjDTE4tyVq4f8xBQeIf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=k1A1V-Hg5khFEh_SgTBQFhA3UmPOiilZBasUoWOLGDBBjt1E-6to_ud8aP8hVUNTXFtpbEgcXEepbiUPO4-QHA_P7t4uh-Z3FRWyCtbdZOvcCLaJeSXEHQNF6TSQCyVGnmqbhb04MHqle_2x80wlrAMQGi7ajJwNY_qMK-1OpD8Qfq5E6gUAzS6_WRn0LeFBTU4Z91HtX73fPBozk45akj7l06KjOAWpMii9R1PJDYfHcNgZ8daq5YAp6jdfOjxixWUF9iUAsJOdllvqK6YgpdFy3XXiSKS7Z_z-ve9jcD67ATVYkVV9ChRCPgV1uHW07JG7t3jZuxDimFbYmeWa4HqQD0kxEVx1cTUjWCDKRINxSveKNmiDJG8nV6AYc2C-ThETymLjTlaw2IH0Jz4zpB9Lxjz4Waa1lrC6PClIAlpoeAhu0TnMJGm7K9ueiAie0EyKeQt8jTq88J6PyMfRsjjiq0ja7aNEHuZzVCjer1_vw6kk_xTmfWcNSLJ-8nd92eV1mjBGxZggsWz2jJLxo2EKpKzNyRmrUXMLtP_yWzM5oi81EEtgL_fczqoJafR99vIjO_F2_L5E453B7xIAzaz4PhGaLStKM5_H81wR6k8m6n1ENMYWBdtDtft7SbwtMWWR00xHdzw5Q2m0iIF5sdfGjDTE4tyVq4f8xBQeIf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgozo4-k9qYOY8F4cReTKNqtISQgSSdSpPfhIv2TI0ZcBKyU2wYZI1UDDl5n-64Eno9ZzCh1wcrsgg_T9zfO_LybSSnVwspMeb8zBQnBLLqKMkoVkZlVvzxMLKQqUp71NiiDHrHvkgdeLvU3Qz8EV5_VgjVJxtQL5K36nQ94Es8t5yl-w7MdI4zhSZ0ucQrS0YArTri3SmyNxC5RKLngA0JqdSScsQiwOB1BGbxJLPI549SLqfvYpH1c7m0ECmp11pGGc92LfUaQjKD_IgS8b_YdoAZYZLyz-bs9oczpsVRBS5ZXCAQNOgJNzRhUxp2XHQoZW0NN106vDxTXN-loXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-2EHH56RGxih8zNvuN2r8p2azUdMMd2yks8lU35V2lCjIWzN-XKRMfHnmvim7HItvMtSXBpJpzc-vwLF-HTUu-uXjITCSPPZQuFl9Uf19GlvZu7GwuoFIWlM6n9a2yXNw5QO6JJZA6dOjSMEuLSXgJmUOuIlUP3nkzzYlKHglSi2CQ8yWIkOFNOHdbwbM6iIruems8_P8dD4N1hL7BLT9mpUH1ENb7WkBW0sQkxYOGyCkEzNxbQAkC5mRhR_cYWvDhq8jmS56wKXM7GpnyfxbFpsW4GBP-T7GMa88hTme2Y5FYD_Quq3WELC9yd1JkqvRQNAe1MpXYNflS0MIOjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPk2CssJ8tSzMgehiI2mPKKy1qeNBGlvYayfXA5dNceVSoxSaigLK2QV7lwEirO0Fk8BBdipmopR5a6fMFiBUeC2qekFYnWpFg-vPdN1zdqSt1Y0xYuSp8pSzc6ggTJad5XgRjV-1qujf4vJ_88ImW1s54mUnLQqrAqxUhciWLW1mUhhSwCS-ctlWsTlA0DmT7SlW7gUzMC5TpumfykJnYPl6vQqxF9VDMTsATZPjqGRH1jDJpX8pIuBLagFPEvbVUKzIwCR1TY0E6FGzAx8wAGEaxt8Is7OnanWdMyzZ-sY0-vPrnKOI2S5FXcDKclFC1P1eo_LCQGlAOWtDoS65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJfT-KSUWXUKmDkqUtEjCTw0zrH1GuXuAUZLfmnONLSZnshSJMGjkR1xSkA1-6y-j4FftjS_56y5fVg7jtdFoOsIR8VK2_Cw2YqLat6XEgMIrAKo7MKxhDVl4J4yyV1Ci6-HT8Klwlv1ZKY6EzU9rUzAyJ7GHdEOn-tmdfCZPggqHYI3Rqjbrub0iQozrrP5bh0XuAHOW1C0KO8UHWsKMOeQncjn7ieGrW_nWu2aAznJUUnDSXj23Rob0yxBa-ieCDwinhUQg4ssxQWsZ5_oEjvWVU--YWyhgj4MNzB78grNQRrvrHMPPoiMUw_c086656v_7XFofIZNvwtgkDeh1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=XixlUSWGGbr8Ec2GWOM7XqgiUbLIyQk_xWBm4PYxpMmGznZ_Pnod86z5VbKbcP2uZir4gDsf9S2Ve1MVFKvNitAHUURUSrv8sWyoZZlg5WPM9VkHUuosb_bW5KX5kCV7LcsWLKCxE80UP4iKvdTEOvoQFA0CL1b0A7KWoivkOqdxh9lOFk7oLprxcQ78O4sFKPYXJBNfMEPsnHWsqRDYYGHHwn8ERhCwFqXxSYzCMLzoEYGhyWDFhirgYeZzDQBOP7Qr8MfRqOOtCbn28TqgtwwaA8XwTy3Yx0ylgzZ5R2iZMZVUF084toV7JcWlvLGw7BFkEg95IDFoAAA2I3M3KVEx9dQn21Qu4QF25ZNce8AAKvd0cSAPZsY9lhQbayCp2tIoB8GWDZc7w2Es-phMb_x-7DouR_T6y7MZWk4SAVfwGBoDmq9S-ANBHTNSrG4ZTXXQrCLj6pi_URWdduIigwGk0_hKPe3xOjetnkGI-hyaIhSSevuEiEkEq2KzQXK22pzbw7zQZJLx6Btf7m7uwyvGXuEtgWG0ac-SKh7o0Hrij3z_X_Q6HGOSWhZ8F9_Sa9PKLsEWjpXz0S_LR2Add990QQP2sR5rMO5e7psUDA4vfr1i4yQRm4dHlIo4EzIL5F7LpqX08fcBXU4zOMKwCmiVc7Ts-eIu6qFfHSWOqZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=XixlUSWGGbr8Ec2GWOM7XqgiUbLIyQk_xWBm4PYxpMmGznZ_Pnod86z5VbKbcP2uZir4gDsf9S2Ve1MVFKvNitAHUURUSrv8sWyoZZlg5WPM9VkHUuosb_bW5KX5kCV7LcsWLKCxE80UP4iKvdTEOvoQFA0CL1b0A7KWoivkOqdxh9lOFk7oLprxcQ78O4sFKPYXJBNfMEPsnHWsqRDYYGHHwn8ERhCwFqXxSYzCMLzoEYGhyWDFhirgYeZzDQBOP7Qr8MfRqOOtCbn28TqgtwwaA8XwTy3Yx0ylgzZ5R2iZMZVUF084toV7JcWlvLGw7BFkEg95IDFoAAA2I3M3KVEx9dQn21Qu4QF25ZNce8AAKvd0cSAPZsY9lhQbayCp2tIoB8GWDZc7w2Es-phMb_x-7DouR_T6y7MZWk4SAVfwGBoDmq9S-ANBHTNSrG4ZTXXQrCLj6pi_URWdduIigwGk0_hKPe3xOjetnkGI-hyaIhSSevuEiEkEq2KzQXK22pzbw7zQZJLx6Btf7m7uwyvGXuEtgWG0ac-SKh7o0Hrij3z_X_Q6HGOSWhZ8F9_Sa9PKLsEWjpXz0S_LR2Add990QQP2sR5rMO5e7psUDA4vfr1i4yQRm4dHlIo4EzIL5F7LpqX08fcBXU4zOMKwCmiVc7Ts-eIu6qFfHSWOqZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=FqMY07-E0b2ldpLl2qpBGLt9K2VySuqjbsEjWRlbwh4KIirzbLRlf2WM8GGHBq7nez1tu4VMKTD4MkTKwSO_PRA9e6pjCG1Bp1g_J7m3pPSyIXiHx65JbcipJz3GIsgRRdLnTcwXDYYQkpt8mfc-kJ4kuGg7R36XRXiJgBcu3swE6vG3UnJuIJkSHoMK239Z2vEWKV4F62_bzqq4Jm6M62InrhXa4jHJUbQqRwxPBi5o6IKOyqAxn24nPGeo1m3xrztgA8MYlPQKp1IdcgywFIIYtqXot3K3lO8Lq3n7_sobxQwmrvlDgY1swezyWgw1No69JqJLkvjxNtDyNVbbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=FqMY07-E0b2ldpLl2qpBGLt9K2VySuqjbsEjWRlbwh4KIirzbLRlf2WM8GGHBq7nez1tu4VMKTD4MkTKwSO_PRA9e6pjCG1Bp1g_J7m3pPSyIXiHx65JbcipJz3GIsgRRdLnTcwXDYYQkpt8mfc-kJ4kuGg7R36XRXiJgBcu3swE6vG3UnJuIJkSHoMK239Z2vEWKV4F62_bzqq4Jm6M62InrhXa4jHJUbQqRwxPBi5o6IKOyqAxn24nPGeo1m3xrztgA8MYlPQKp1IdcgywFIIYtqXot3K3lO8Lq3n7_sobxQwmrvlDgY1swezyWgw1No69JqJLkvjxNtDyNVbbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBAHa5M8ZFe9fmlmF2nBboSNpV-HyjfPXMXqW4cUnFnmdYqt4TjnCUG_JIx6AkCLEdL91zD_6MFpH7Z3waWBGGn8tHJxEA52dPl3TyscBCqUv-IC1aZyNULKu77fGbrkqJCsf6FyHTNTsnlePKWhbyjNe5RfHOhuXRizJpSJD3eBQg4NIPSMTzO3uKyru9zyqGMQPbunqnbgSaA0SOb1FDKHtfXrtK_F5Yj8wTPsUjdS-zuyQzlZ55Ay0_-eFCI6v4CPcl8EVtCtxGCZrON9B7wfyc6nCA0pcJKuLPn9V2eJxQR-HklwGaYKOykNd33k9lyNRCK38bxtxBDQa2eS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHFSy3xGX4YFRo1dkafsMc3mozqs1kfQ3mJN4iyiAc2m4NYK_yLu6rtD46f-KXphJNt1LyQBdI-YD1AGY0wffl-qbZCW_5R_9rCQRR1JIw4bIdcwfqeLLPEks7sEW1YqdowrxqYmX8fg2BXr9_9dW8TkVAualHAl3fuRk0zE49GfEZq-CI_U-GrUc2KCGVR5mYKFPYYirx9cArts1yseiCRp86tJNvsweq2cv4Cn-8Nhf4Tf0mj8gZUsNv2dzhJgu8-FMaU9vNzcURaj61c1ChnHnqxzmpz0L3nJUGcoM1Up7hxGwNasoi8Df6F4BrJnfZ9LF0jRIl_GHyNqJrnTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYDKniA9U4qGr6xpzKcMKoEQdTxTAv677X3eOypC9ZSr9UeN6lKfJgRqUg-X86yJTJtGP8wVebzaYwPcYi-Qo52MBxbW5Qa3iFm6K_YS8GKtPyGXPm_ht86aQIXGovpyg-TSavRYDt4sexmgbU1tEtO2DpUseBVOSG3AxColrOzxedvOIloNoKmVEcR1jdWkyzKZOQs4lIlA6TRcREyQx1FCYMHSakcItzgUh7shGpRp-P3KWVK_K_Ocw4XRpYVQJ42j6zHUJKX7IFv1WWds7lEA4_vDn0betOkpSQ-pGT8uFk0pCzHdXIZmis8kC0F7100PMOHhRlD5dzDqVenUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nupvVfEB3ksH1nEMTv1jt5VZ92WB_aebo7hKzsJPCmtbg-gKLGID5xb0AA7pQzXMDeY9jh32m-bZbrWPbS_rZr5SWsRl4LsvT-1x9mzbujnwNv5tB_cPGac4tjgLe5JMDLHsr8Novp5BN5Ihn3Jcby2SFp0_6SZ9DxRtNoYsRIVQ2ottZ1sfslKe3CrxflARn4G4ZwRe_4faw2UGyVGXu2dib5eJKADcGuKbq_PccyRNrZfXtL4NLZ6IscsRD8KAT8ZT5uXOjYbQTf93-EjmH5IE5ieorZ55cs2qvDcXuLMVA-rxUupgDtvOrN6rwU-u4_ZYGZrfBTbnezytwQvwgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF4AVr5qwfsna7kQRzFLjIpA6olpOklXmfqH664a8GK2jRUa-Fbo93rc-R_xc5AvrnWl9g4jg3mCluIXU1vuCvs97g0DJVdvn_S7xXeanrfX4l24AepMqqL6yzNS9GyCBh30lMlgURN_b74-41xoVknQD2lBp8YKm0-FFf8EtVwaNwwpTYOdmt8W6xow0E9EuheTpaw6n84RVWgqKINn4p5ScbbQ4SiLnwiX84TsGG3AVh3jWoTJiBcxGlzvB8dZK3M0lhaWUcX1XaX3CKnZcdKGe5bcpOWOxrm17uN6O3eYZ9LtDvZTK9jZjE9KI5peEYdwf5JgULU3ssDVITFgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdgWEjMLbQ5y_yDVdXQSjP1pEzuR6MID4AhJcayap2qCXketKIkIdpl1m5tWojf0u8qFk0C5iIWALXWjp3f9ff5TEZn2Jzl02BBgQHrjsjHKVF--zfWOTiHT1nFV7cVRIGg76grBOohb7PNzfx_N2aazLw2xAFKhuWEBq15eO5ttXwk3OUKYvBJc7K5Y6LDNP0-cKirl97i01P9-oszhThBGxw0Qk95xvMy4ir40w-3jHwEkyakPS92V_HgKQD5BFiVJZumw5dn12RFtiotTY_a73Ql_7ImTV5nW_25iQv-ErFG-4TdPVxQTEwqjYXEnK6ciKLd8aR_HZ2AOAGf7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIesK_DEFTFKQj-lnoY1RKxKcFplUWjdgWg637hdiofstblDgNhMIOzi9gtsyC1Q0QAehVcw8qajt1cPm0Gbs7iT87gzj9I8RZLVLVqG0c8CjoEn37gbQz2sknSeIEUG1VBCuo3VwRoGXVNXXWMfYeshiYN_-7Uma-4RUZiHVcqyeC60Ku3BmSifIJGcxU-p5GUwmZvAm6isJptZVKhsbAer8leLiXgpDHtH9GMk3fFtKMPqdfvMCnaAngK_PPCn5MdsnhID7fVf860viL-fysS9gznsk_NPZ9WibEBuWBEqNUzXW5_GvZS_6sniFgLXkVXyipj_96LB5f5uY6By1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=fuiotDcKT3yDaFVo0RQRxTDwDPl0iS48s0STB22nG16QMihM7sjeJ0sDH3YdJwnHUuyMnmfCMt_smv6ix23bFjh7ATgjo9JrePC1NvZtryi0Ih7gvUjK2Yu2CPS-nr9eEUtwFPCq1jZ2BSAjlzRcL2zeTCoTEd9y89saJAL1vhqhBpGa4o73W-jUrjyrVqpYuqk4b39WIz7y6HVL6r9qerIvJbdjdO1kbznnYUj8tHbHSXH_VbnKeTmYZaZ31HESYdl6ULDv_AEZBNFsB-reyOxJqv9iY9VuHlinRsk73ESdr5gfi7Q2as1f1XSCDK58RbNwhIcKJCFKlB9yA-8eaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=fuiotDcKT3yDaFVo0RQRxTDwDPl0iS48s0STB22nG16QMihM7sjeJ0sDH3YdJwnHUuyMnmfCMt_smv6ix23bFjh7ATgjo9JrePC1NvZtryi0Ih7gvUjK2Yu2CPS-nr9eEUtwFPCq1jZ2BSAjlzRcL2zeTCoTEd9y89saJAL1vhqhBpGa4o73W-jUrjyrVqpYuqk4b39WIz7y6HVL6r9qerIvJbdjdO1kbznnYUj8tHbHSXH_VbnKeTmYZaZ31HESYdl6ULDv_AEZBNFsB-reyOxJqv9iY9VuHlinRsk73ESdr5gfi7Q2as1f1XSCDK58RbNwhIcKJCFKlB9yA-8eaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oyLObQsPzCAejZeMYS3EmaOP5PjrlH_XJR5Iz10pvWACA4XOeBWV-NswDoPavhuLBKeVaokYSA44XCpiyHmK-MJqgLVwNjjROwn4xTN8l906kng53mZEG-oVg3m-m1J0VD2m2kkTRu4-t0u6s8j4nmgeY6-PnZ3PLqsmFI6uOVrdJ5yTooXu3ESrWIEeXCFyPCk0qvZKCn6mtY2HOhJ4PD4STB6YZCeSLMTQw5R-Sz6y0EM8DWBPyv3q8XoUHPgPGEfBTjfdeFsollz1_dlDRB_VDVd9QR0EP1hTT4Bo04xvHPeenPf29F4S2B1NtneKvyClzzhSrkgxd1p9Ve2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=VpRCAiOk2A4rcJjisLKDge3HlRu1SvpyH7PaGJVNQDWV3APXLh7nf-5rbsmKQ8mz-UJF_chJ999ED6i-waPB03lTiCs_wsWKh3DP7YoTRDkZI_4_Z7n1cfoyNAfNkL3BOvvihuDkQ-6ok4vYgXR154ZHyMrFHNKlGnktdwqUsZTMsGcUYyhS0AEHHmj_wWjat4bsH0sz3YkkWW4LFxPr_VkNr02MMIkd1oU7RqwtewYsKcl1VKOsKrpokT9eC35mkjtnKcQOY5fkWQ8AHLAgC9LenYfRgDEz4G0zsXhbOQArp6bYPsUkZDXMGL0_5dNvUQ2l2PXk2PHUmmD8LNIUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=VpRCAiOk2A4rcJjisLKDge3HlRu1SvpyH7PaGJVNQDWV3APXLh7nf-5rbsmKQ8mz-UJF_chJ999ED6i-waPB03lTiCs_wsWKh3DP7YoTRDkZI_4_Z7n1cfoyNAfNkL3BOvvihuDkQ-6ok4vYgXR154ZHyMrFHNKlGnktdwqUsZTMsGcUYyhS0AEHHmj_wWjat4bsH0sz3YkkWW4LFxPr_VkNr02MMIkd1oU7RqwtewYsKcl1VKOsKrpokT9eC35mkjtnKcQOY5fkWQ8AHLAgC9LenYfRgDEz4G0zsXhbOQArp6bYPsUkZDXMGL0_5dNvUQ2l2PXk2PHUmmD8LNIUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB8pvO28a4hgzobR8gJWKHSobJwLIkqby2FyIEqxw1abSQeQ1aa570_3ivYhikAUt_7JxdjGSFkk9FoTM4B7uD3rp5RdSZWqw5WzG7ODuDoq6NVNtdSIaCdwnQgY9f0VEPZV4Dz619R8C8N0qSyiewuBem8N2vkfF7sDLnObUiPHBtkvPWNpCLB53ZlFRBAk-CIcR97wJzw8jRN2JCQrRPNOtn3l62iC3JMaM5bc7MK60RC1HXbdyWJDO-pAgP0EcYFezp3rKKyNobTo5BCfKccX7Yxhsr7uplq4qUYJK6joQsbVqTJtjOXneS1Q8DxTPfCoe5weiGhqjpOyekZPEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZp4sWsQjaPpUmj7R9S-z8HTo-6xljA4nOpUMGarE1jziYINrJGftez9Qt-OzYF66OjDwdvTlIqxLJ0ZckO5xOL2PXFYfJqYuW5cDg2TV47na0DnBWOXKsgHLvaMhPgpzDgR69_Qj_QYRJHce1K-f_nMTrhVga88M3GXL5C3iY6WBnWxwJh2_pZ18dt3UPkJVsZHhGEusAaW1nTt5ZMoCjJDWx0CG0MkYfK2rdqaEXQvscdh_bdxp26eZVaQi2uR2ZJaQHhkNUJhmngPWSSNWrRxspw8zqs8jiipK75-Z7WN2dWamjYQVW1fbJdKH_fB4zWgQumWHLb9A5Ry-m8EtyVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=neHkeRSJKVLcSbyh3D4cyKJdeHHTdrYaomTAtr0nMd2ObIxNbLOOk3GdnL2XkdcDQqMsBxDCpLYdpDa-G_IDXpuSSUdLoYQ7tEgv2keHfPWlOEXF_lPKckyCoEnrkKENTZm8q2cWGrmJnsgsFqJYwo2_yjp8_0xbU8Vlav8kC86_cwJlrTdNThGqzxIlYic-tFLARZN6x7pKRVV_eqhGv-4oUC-6341twWvUCQk4yakLbf5T-2_nEXzEZ8CBs8QU4eVTkVJecRhX4pmO9N2fh9M95KasxDsljDu7W1hZTHjOKgjuzplu90k8O27VR8ZsR9LfliaLCLJdH8Fb7PZZZp4sWsQjaPpUmj7R9S-z8HTo-6xljA4nOpUMGarE1jziYINrJGftez9Qt-OzYF66OjDwdvTlIqxLJ0ZckO5xOL2PXFYfJqYuW5cDg2TV47na0DnBWOXKsgHLvaMhPgpzDgR69_Qj_QYRJHce1K-f_nMTrhVga88M3GXL5C3iY6WBnWxwJh2_pZ18dt3UPkJVsZHhGEusAaW1nTt5ZMoCjJDWx0CG0MkYfK2rdqaEXQvscdh_bdxp26eZVaQi2uR2ZJaQHhkNUJhmngPWSSNWrRxspw8zqs8jiipK75-Z7WN2dWamjYQVW1fbJdKH_fB4zWgQumWHLb9A5Ry-m8EtyVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=m-smQIqzVe9Q7CebaBvEwAvlN_agBssOx6iJcE8qKPv6ASJW6J0iW3sn6k7AJpkb11_Ppzy8SopH_WTpaPV6wV-RLuRWx1B_Gvf8TfUJrJMFPUrBlh_mnnmCgTmNWeSwuCi8hSpNj6xZKqVDHufSzjy7Nx8R1iSZLUZJ5BUEbGxSIuHy2_9uFL00hm6_17PLiR4ZooSjQJXVdevuEhRS1U5oj3lHKe1wHu6H6D5lHjw8T8Uk_VDE4Liw0_YGPO4KBMdz-Cgi1eZRCzwLPr4WiqlDpthNkL-c_FwuisRSzdjRorxQkXqTuEPpEzJYlNfYx27T13ejS-iPrrb92sjeGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=m-smQIqzVe9Q7CebaBvEwAvlN_agBssOx6iJcE8qKPv6ASJW6J0iW3sn6k7AJpkb11_Ppzy8SopH_WTpaPV6wV-RLuRWx1B_Gvf8TfUJrJMFPUrBlh_mnnmCgTmNWeSwuCi8hSpNj6xZKqVDHufSzjy7Nx8R1iSZLUZJ5BUEbGxSIuHy2_9uFL00hm6_17PLiR4ZooSjQJXVdevuEhRS1U5oj3lHKe1wHu6H6D5lHjw8T8Uk_VDE4Liw0_YGPO4KBMdz-Cgi1eZRCzwLPr4WiqlDpthNkL-c_FwuisRSzdjRorxQkXqTuEPpEzJYlNfYx27T13ejS-iPrrb92sjeGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYXd1Mu_bjdR6mkVnhpQ26tmRe6bUjCHBJCLDsVGOye2tPVKGVmYL7V8AiHIS_ciGh2hRmVBy0dqBsBUxSSlmekJwFr5ck8SxkAX0z4-WinTzDeFU4ZNMOCD3dMa8JrvIdCr-xpe_APGlgeTYdgYNrQlyqDWNPoiYSdR7h5vP_BesWJGaHPpIknhaZ2UH6s2gDiw526SWetLmeXZrcdgdPSNC2oAgPITnXNDefw3FTIGNn0g7J1zOKuoJ9J43Uw6u4yLecaR1VKKQOtwirURPDahF_CNPog-Avftnz0HVsBNNUL_h6asL2LUNXKC9-xyxq-LV5voCTMpFxTjVmfEtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYXd1Mu_bjdR6mkVnhpQ26tmRe6bUjCHBJCLDsVGOye2tPVKGVmYL7V8AiHIS_ciGh2hRmVBy0dqBsBUxSSlmekJwFr5ck8SxkAX0z4-WinTzDeFU4ZNMOCD3dMa8JrvIdCr-xpe_APGlgeTYdgYNrQlyqDWNPoiYSdR7h5vP_BesWJGaHPpIknhaZ2UH6s2gDiw526SWetLmeXZrcdgdPSNC2oAgPITnXNDefw3FTIGNn0g7J1zOKuoJ9J43Uw6u4yLecaR1VKKQOtwirURPDahF_CNPog-Avftnz0HVsBNNUL_h6asL2LUNXKC9-xyxq-LV5voCTMpFxTjVmfEtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpyKquIyalFJEWVCTvT7LZZM9cc2dP_VWTyrK7PUtSG72s_3mcrRfB5-gLsSrJy_97Bl8ohVfjY2ORixciD6jpndm46F8sF1xFBajWE9X60kCDed7XqukNqVTiKClf4wB1yt-qOSrGdMyNgI9OeyFGAkvC82Iek3OG_v-qi3PaGhr5V29Iv_IAbxDvwlDGBgVnQ_Ll2TFcAoRETSc0hs1ImFntXzOXYZm25ltLYNnzNkYC_l6BumkpPuSMcL02V-QYRXNUbHnzqCn6KswMDPT8nyViDVc2vaVt2rbaPXtU0VTae2dsoY9jWXa0yn_VFg0qdzo0OJPpHMVQEdjJnz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
