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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JvGmOW-sssEO-QTodu3KnwnpQx8K23chxDhcXoWWQux1A5nnxgmlqe3puc1OBuoPC7pvIGMFqCFLKQGm_9HyPWuwxXYvbonf0HN6065S-FTubLHXFzkebNcCCbz3OmLNMwCtfsx_jH37HJpg-7iji3XWagpOXV3no7d8_di6vdc931KiiBZRgX40uRlyXIeJMozNgI-vS_-OoMTap7qiZZEbKAaBembKCOmPz6ytqczCsuszDFcB3BLKnW-bhjPqfqOQrGRW4GOnaKfIj4ZFuA7QpqgZzxvbJk91E9pn83Ml6MJCpfAgAYs0wJYRpyFLFteaTBZM7qh2vGlWnJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6ApQ-4gxhlfn2Xm6pNkFRserp3kqlAwUkRrpjiLsnsxziBvOhikZY_aaL06YpfXD257OfIze40TmFQEtqiDan3UgaQXs8oSi75DpxyPl1I03wfv3V8RRyXRg6Aj0WM-pMO36JPPdoBVaAyFo1mc_GZOY7_ivC8dq3zFeVV3cs0gXOjSWxtDBkBSRPZTs13IOd9rhgNum653GjPe9ERoIvJ4Ot_feXNHhOKL9bmm1QkaCGxs1NnL1h_K4GGPBfEnHV4Rz6ceKU7GNdpytXxQlN80bPAu2iroiZe2WUtlG8JUFjHBoLcZCOUGF5gciTfVTfEMab8_qvbS5_sAMA6bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1XWnD_JUCsJR11IbYfvw0yNL_K7vb1-fE6uGaLHtrXPEmtzrBECwqxssgGA63TrV57J15pE46LTbO9x6Dy-4qxfFQ4CPqF68v8i8EBIk-z-EKy25J5ZofAcZlpn9kCx3Ji3TGsc2u5U5D6O8KPOx_fMhOae-sfhK5Ry-ii04RY-3U0y_6C7Ruj_4JxlM496oNiTM8MAm2euq1UKUbAcyda0Ljcn9f540SasFoI0_Qrm3NcQUfa1XVYOkKbrgfl-hJb549yiiuPvxsLKIsL00QhoqbiDWyjqlU7volWwqKxTkvIBs1owwlKbAyIOC0LIAGYfhfSLmaqawJDm6oS7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvsb9SFsyqoVEAv5sFhnqB2EiFEcDmkKJR-Vi47BY7LxyJwn0CMuHGgyGcK2Tds25M89LjWS78g84orFA7Xq9lKwjiNxKyBAGL2iwpjbMdZCrBp10JQY-rzcbD8Ie3d96Ds7joRpqQaLfYXqg3F6Hd_muGJxOel7tk1hoaQyWhHgzjDiumbyFUpdJjnQoYxC-r74t2xzzOZI5Jrv1lNvMFsat6Elqmg2HZ4JJtDH1omYVbjMt7L_PxEO2IcU4YVP5rIvMQsmG2rFVtEIRchKxWEtbJ7UpGJPI9NN_a9ldlsefdIV8ZvYogv9YjFTswrUrHlCo67bIqzY9AsJWM_Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=vSnZUH4QAhql6Rpm1oBgu6RpuiaHQJOHSZPV1p27yXhYGyIB95szzbdLs5x9Ce4vaoLvuuLXPSgbx5GJdqAlf4dV_ppoo2JtXuRbTOehJuubZlXRG0FjrHPtPKrfE3PsWCTUoUmt8qqjt3QV_gp1lypUma0YqxoWWMcjxJMzu8nAVuiTUY82OuhzaBkS5ac5F0XZthMwG8blbJdir2GRv2RwY2fRZUdaf8U3mOB7eBGGzTiUAdspIZaNHONrgHca0eKnPHHlDQ9hcVbH3SBLr8KxnImlSZurEeIYiVbbpZ1rL0OXCSwQQJA6nPHWFoCYUP7GEHhwBE7rdLJwu-CYJpMojKZE_WBPEls6xINATc94MXb9-xufweaQ1MBa8snt6jrCh-JO7FXalLY28XKT8rHYC4cYBxhyPppeXXo462MHJWqoGAZT0S3Sk5mdfNahsVLBgh_S9HgEUCLK7kYi2QrG0k2uIiDMrMwHL1GWNVR1rdghDXnMkCktL9Vovd6fROE6_T2wSkqqUWt-aewtoJG7Ep5W_EfHsM1P-kE21d0SzezhMEPwZSf6vEIDyzpzaEIwlDJ6KjWArTGZyID4BiH_X7_CY3Cr2Cx2xeIYdv8uqjPbc0axXmHXmlIkY1vsGXpAnkEHpLTvNqFPnERRHJ6JFBH53GNXbEt6tFJXT8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=vSnZUH4QAhql6Rpm1oBgu6RpuiaHQJOHSZPV1p27yXhYGyIB95szzbdLs5x9Ce4vaoLvuuLXPSgbx5GJdqAlf4dV_ppoo2JtXuRbTOehJuubZlXRG0FjrHPtPKrfE3PsWCTUoUmt8qqjt3QV_gp1lypUma0YqxoWWMcjxJMzu8nAVuiTUY82OuhzaBkS5ac5F0XZthMwG8blbJdir2GRv2RwY2fRZUdaf8U3mOB7eBGGzTiUAdspIZaNHONrgHca0eKnPHHlDQ9hcVbH3SBLr8KxnImlSZurEeIYiVbbpZ1rL0OXCSwQQJA6nPHWFoCYUP7GEHhwBE7rdLJwu-CYJpMojKZE_WBPEls6xINATc94MXb9-xufweaQ1MBa8snt6jrCh-JO7FXalLY28XKT8rHYC4cYBxhyPppeXXo462MHJWqoGAZT0S3Sk5mdfNahsVLBgh_S9HgEUCLK7kYi2QrG0k2uIiDMrMwHL1GWNVR1rdghDXnMkCktL9Vovd6fROE6_T2wSkqqUWt-aewtoJG7Ep5W_EfHsM1P-kE21d0SzezhMEPwZSf6vEIDyzpzaEIwlDJ6KjWArTGZyID4BiH_X7_CY3Cr2Cx2xeIYdv8uqjPbc0axXmHXmlIkY1vsGXpAnkEHpLTvNqFPnERRHJ6JFBH53GNXbEt6tFJXT8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNwXbx8estDLFDVx99kYmW8lG-O7qV3zl9rlQGtXeMp6UUcMOIRG7ZQAoGeNFL5xNP6O8r3KVwDe00CtCq9JW219b1HUQifhpoyX5-r8gzXH1HSFhCBIuEplYeu6FJed4o8zdXePVCbgWVaAzL2jOe00E2HwMsR_zA9hWgq0PHt_9UYpPp1W8t4Gpjm-c4EcZXHj9i32AJiORiwouDskGFi500uBjDamFePVI-sLI419EuoJsjylYUt1SRAw6eFPuG1wakwv80Zgj68G3b8UNaiEvlx3bISkYaNDoyYZQOqMgeM0uB00eL35wJZXNusBKVgTWoYQMH6Q0kPSMl7nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQrHulZH3o8X7tUCmwwJ7sQdbeP5v3aCdTk8M6tBHLhpWhyDbX6CZ9tOHwGModhRIQp-Lh7tEgE8Yz7py9ZlPEKSt0ls4Gh3EDTdSIYJttalGDdfgSu04qrG9HrRHL3mCYbkxBNDwXlaRcencLH1INH3UZyEXnnp2_k1N1XpLACrjkBtm8lWOaqTycJ_d0BQ2w4nQskY8bli4nMsbLOg7U1IeS6WH2Rm0dv2X4CD4lVmOozltkDtAjzKoKfmIHkPTE7Ho6LPDyJC_0FzUsc4j-fvDqtCs9Wh6ZndW_iQklZswNG2aa7zBBWeAusKtl-WPUpvprotl0sWE6bwiIuS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nltfsJm75R01sMpxsYcHAtggqjXdTWC_JQGM5SVzpjNt5arAop6yMFzcyfIzzXSMf3Xfj_g-mk88EUSp3sNChgviv3XHc8oF-2NlfobYoAWWxSJ14isYQJIslxZG1E1PSj-bmbL1TWLpLHrX2_twPFO4k9SlR1nfPfoZoHp_5MXIgk0yfCFFh7biv3wUesQsQ-6hxPGhEuUz_YWMDRjv4wLO4Dco7ufY7hKSuNDN-5BNFHcXENYR_Lm-3EnU45NlfG8hyuFWYfZO3qXiBimyWs6sJdb78l7PY4sNwD76Ezq9yXzer4rST9QMmf0fw6OSfqu6madoFhmoAnSQjRuIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBd1Tg5FWnuYi_lPYMdbwPI8w_y9qH3aDl7LE7h1orQcCdlYgucNh0NEUtmlFQpk5iFob0eAZnHmS8gC8IksAjxGx1g3X0SwUBIRUg3lsf3iC2Z7ANh8OyfEPdw3spELZNJ5V0x6bg5o7MNRIei-Lk6NhCzzJpgqIKr3TTrLXSnRQhBE2iPzm6r-yIDkQwUAkPmtc5W_tE4BzRrjMPSbsa8qvQeYnCdVFK043w1L-ODM82jKK_yF4EAULQJ5M3YpWgHF7KYxT95yaqLRjB1f4qMTXcaSNibh2432zttgSBdwYkwSpwQMwqWFO4aiUQ9mtpq3t-MVLENn7wuw-fsRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqubjHV_lnQmLdDOknF4DEc2j8o1HwRKU2fpjiFdGv3MByCRQX7ufX-hbxTWYl4yy9xwGtJRrKsun51-IkUmmG9_uXS59vM7kVeuvGDYAX_tCf_RAHLkOAogV2gKGtec59GnvaCWNImaMIytnjo3GLByUN3LUDyS4jFKVUPzF99KtMNB3kXb8l1pt7SxD0QFVuuwgm-xAf2jDZ29Fi3l_lnRvCW4A-7upMZCM1CVeQujuANOd6-pLNh74jg4hnO-6KcMCeX7Br-RIyTDUU_DdbQCCyuiEDnLsOT96g28Azi-OowH6a430Un3ZzDFGXSzbL3Sfo8_skb4dAsjoh_2EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1q5bmCKodlUCMLVn7k1I8omVSiO5vjtW31npy9tAug4BCLKY9yAZHF00L6Kk-7kz3Y3asCcA25VK2msixR_UcQEx0xrt9uxFZHI2EPb6SGFAYZqi_d_hzIooDrYQgRJ2hATFI81M8NEFyYUbzj96PUcv3MY8vNPBhmR51mAWbavXSIO_nd4lgoNsvDc9bF02xRzWwRK1ul8RfKyNfQJvq1O4dvIF79nASY_aGVMAY6N_PxNEcyKjYVsMRCL6hyZgTKX4aM17RNTjxbf7mOq-Szwz62RcNbsK7GeB7QA6mz-bdb6cxKQgLLSKM3yENYmNu7qK4H3h1mWuEoZ79wzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKgZBsWmbpUmzUA0BV2hc6rKrK7ss-6X3V5ii_zu4Ucw0OqZ4Lxika5xeyqjOC-nXoV-3_YiW1JSqngLU61QzBG1Li_LuTsYbHw7Uc25mrGRXYf3BCKWFPTHJl_CDhJ-goMxURbmpmfp3AH3qQq82mkERLbatkFc3nNaKn8kBt_oajP6VwaU9sm4B76ZuiqejQv43LM50XVzXzkuS77myQXi0bbOr4Lya3f5OOOOmP30tup0WcQLXVooYYUhhfmWhHCx6Nt3gXzhLA2j8DU8oclck-d9yVXYt8BGpPlZJ0Qnm_4FSz4UUBswe9lHSD12hz55qNn0U4dNEQIC72C42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=PJbW-h6YfxEEjFC-1ggOyKr74pCTA9cC-MOGV8AVda8urEo-WsCBLAVxT-TJxeGIXAiokREJ93TfJGP2u0ZTbJ-bnP8csryIWQtGJ9zChv0xGPh0l3Yj9hisTmw8cUXo_rMFYmon9Xf0M-8KKnB6ksSsc1dQGGWr0s_3NpC_3P_j3FjgpUGobopyS8VTc2vW_0hVtFxnYrQQRxrebYw30pR2_wPJj7kWEZUf5Gzg3w3r1SEDGZS0CWhlDIMrITCKrJWS7lw6EhkDGpiersh1EmEkPBIu-Rga2NXQJ8ypgKX3Xq9jbQBxhbzTBYRxGHaGiynRMyFZcplwXq4o76d81A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=PJbW-h6YfxEEjFC-1ggOyKr74pCTA9cC-MOGV8AVda8urEo-WsCBLAVxT-TJxeGIXAiokREJ93TfJGP2u0ZTbJ-bnP8csryIWQtGJ9zChv0xGPh0l3Yj9hisTmw8cUXo_rMFYmon9Xf0M-8KKnB6ksSsc1dQGGWr0s_3NpC_3P_j3FjgpUGobopyS8VTc2vW_0hVtFxnYrQQRxrebYw30pR2_wPJj7kWEZUf5Gzg3w3r1SEDGZS0CWhlDIMrITCKrJWS7lw6EhkDGpiersh1EmEkPBIu-Rga2NXQJ8ypgKX3Xq9jbQBxhbzTBYRxGHaGiynRMyFZcplwXq4o76d81A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBGD-1vLXLT-YuWc4wXvG0Nl7bsvvLntkt-WHQXYR8059DRn8TvoHKnPK0y1UV4SswswlKPGUtbLqlClOtSmdLeDSIQuMdwD-cO9kg2AayNhyVIbqhEdh-7sYoUZFrnxBfm6Z26ivlq1Z7T3nlPIDjH1_P_ai_nBn-uaC7lTj8yZTmJIXcrZk1UODaeRDD_wf0bPU1B9kbv-JP1AuAUMeRODOJYh5--aRHwnuSpN7bYax3qdkpCHl-74-FpxmOIKMjKgmI5vRHb2-sgddvY1pCdz8Qc47GpnLzuJ3u15XOEEUN2pzTF2Okj_c1GvsAPz0TVyFjz3a7RCiS8xdvDEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WN6Boi0BK4aE9whbi7X1cFkrZoXw92FKuY5dju4DOyfnN3njwBV1D1mKqZ0V749tlsdm6GoYb1sAD0VTMrjpYvN0EIY9kydxQ3a4Crq-a7297Oc2YSnhSlVIPzaHYbp-Yag4PwJ6hcUJUBlUSuVJ5QSt7SHp4EtbURu9lTXp0odGTou5cEIaAjjOwNiSm2s3aKJzzqdSIbD19_XsS9ClC7dph3g7J_oIHYMtPuYHZ-CeuUmQghntHsCBkH23SJcfBNuvVkhSBOH7d2-dIAuoU857pxwFb7SKek7ocCiVpQ0K0UFXHx7u90bCqZwc8dgQ1APYIb7-8gUN0IADzxRj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHEOtgQr85qH7LNXXOncefKoNHBRv4r6XbwVmFjcTH8TIaxlM999F3b4PJ3EGwdo34CK91xBocWwl5y6jr0JkoXM8uaLlwsJlZPFP-3-Hz7uk8TPmNiDDSo5hCkFPHVitBw6mK4rwgtcMBit9pZMH3l9jVjjrgIolDQ1TxTeHTwUThh-5_m6VP1IaN02Hy-wL3b6PN8nSQ8CIsZ-iZdUGuQmMF_oN4YgtCfmaA1eGq52C_C9zYxsoYX7OPwQPGkVpsvJSGGqFDfka6JzPZgzB-OQRyI97wIH5rnmvMGRXWzJn9kXtnRxO5gWuPoRss6a-ULJSs1VTDfXEFZx9-4kYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiRt_dfbrkrcfMGsiu2bgx9hjlRmIyrHd3m1OX2Uiun5C0oIKN_J0FtJ_8uPFM-9klarHfy3eBpe325GXci4OK8ymiPKoGKEFyo9COqJUaE6NHdKJo80Lc2CZAGmMZfmrfDF1pmlFsjesda7jpPhR0oooBCcKWOWCZ5FY9KycudBxbMvQEQE9N4Asau7YmTZrvLH1jDcOUeTRlvJT9YPUElWkVz3MSYug25SP23qkH1fhE4Y2RzeAlDcOL1R9ZwJIn1VJT-pZH-hMae6odCyGQUVkAzbWXXArNqxFf-OnKG5y2pAqs_ybhm2Ch9UTvCmtm4uxngraXCVZ_DQSGzcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PPUgdLUcGUvtcVuHLIpQLJm3lf0TU8DFi38w-uFmgX1WQTCKt2SBgbLcWa2xoLPXLR1Stch8Qg_Us5gFmmIxaInmvYzBZKrbSrSZ05_CM8s4DEoSO6IHOaJuB2F5-aWNrMz-lIdYbcLPpi9578abX2xq0AWx1j4-bUXsMr7eP26ApV9DW2pEn3Qxs9KIyBL8Q815GAje2gynU0zB7hzqmlttTU0ny40lZ1hGLh3TZxJXdeCGk34D8GB47dcvyoAP_a9yjyizj6ejLELpHEr8Lg0vU3msofq6RJ_ZgDjKp34c4JO2CrI7kPCe4l-zY0hvwS-qSpLOZE7ixSII0q62tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PPUgdLUcGUvtcVuHLIpQLJm3lf0TU8DFi38w-uFmgX1WQTCKt2SBgbLcWa2xoLPXLR1Stch8Qg_Us5gFmmIxaInmvYzBZKrbSrSZ05_CM8s4DEoSO6IHOaJuB2F5-aWNrMz-lIdYbcLPpi9578abX2xq0AWx1j4-bUXsMr7eP26ApV9DW2pEn3Qxs9KIyBL8Q815GAje2gynU0zB7hzqmlttTU0ny40lZ1hGLh3TZxJXdeCGk34D8GB47dcvyoAP_a9yjyizj6ejLELpHEr8Lg0vU3msofq6RJ_ZgDjKp34c4JO2CrI7kPCe4l-zY0hvwS-qSpLOZE7ixSII0q62tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcSU-iqctpaPQv3qxxts7Ojp5VopAYh9bjc4ml7gqesCihKPuGprpzcnKcKZPhg4RtWH3Z0orHy9K9aPEpIQFK-GqLdL45o42x-k_aEUsi4vNHCVHRZLDfRhi31BCQjRH1Jt6BwmhUFUaj8WsxXMbWD-COuHxbVBUBEh_D62to-oj6ZHbZrBE8GEZM179O40ycF8zKObxSMzZkXkABXM9vKJ001DkdZ_OD_8Hg9Wriad-0BbO-Z5ldHsD_AFJoFqfeD7GYYVpOHSzUM-CyiOTd6qsCR9tnwjj9AJ1wQ_AKYx43RBBIL4SAniPhfdYyt7x45ejkuWKUdNqwzH3kVuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6hrNUQD3F14akj1AxT3ljvqQPmtqb65o_CjPChGYV4_CcRsdQ-uOlyiqZyX-fqSGMY_aZSyVvhaJzCAuTDjJ1cfoIFB3yzpgF1E25eocdwB0zLLG-eVuSD8W46E-_6xvxuKxt69pSL2-AQwt7YDp-bdpYouQvevByUjHSuEexD_6VfAGnseirZ61lezqjRhUpZjCN3V1EF6rn0CoaKugkyBCzRv0sN7R5iRQdJvN_ZQxtu5qTZ8g3vNceO6pCnwdNx26qVhmw4lOp1eWwfJUIdqtUjMVKIXWaLeDv3HPRmgxa2vVJtnjyWsIJ-QYzOsys6PRoTEx7uj1_l1RCbGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOWuF1uw2b1K4hA62KWZ_1sZHILUNPxdpjLjpSeuOwGBm54GkQfYTwzxHpiv2ywdVE-scmFAsdWPI2iBZn-qy0zovWhb2w4izOzEIj5ZwJTBwUcltZlp3fV0DC65LiuAey-5StqnHY7WRejRTimYY2lxWtitmNujQ1-ClKz3agfURN-x2RUQWybcGoNbI5zMVAO-o4MgbQX0GRyvKD5pmLboegHMhqeCk9WiGliBhHfnGQyQOSM69WtDgyXGiZiAdLYQp4nEjPcmNAJLiIA0B3prMdQ_O25q9aiRrxAHSYAVrcdyCxF885qELSZr7AdrBiMSGxwG_FE5dzG4b4E3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=FMhhTBW-GUB3w-6mYv617S34H65sxmQiM_hh6qwVfsqH_aM5QXdQh2oSr7I8OBFeDjep1B8H4AzRZ3NzV9wV-yebS-cXHQlHNlGYmts1MqQo9kx3M-_PICytHZgXfPSRsIjVhWQwWvj4h6b6G3Ym52IkI4eMv-o9OtYFi1CSsCbdbhsibYPf0F1i3N_Lm8fmfpG6j4aJow_Hr8FjNHAG1gqPcUPWGkPcu4cIoK2NUYaSQaIoSI0QADskNC77yM9cB5InKKVlhDUKkEi2kd_cJRf66qSzyB4WmQN3rvowmJWzI3lTK3Oh9eICVvVTJJCEAeDX1sc_jCBYki7O0MS-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=hHOm4SZZVcilAQ-iqEAgKLPkfUzYkbIQV9plcNZn-ZdCo-DnUO-VJ4F_w3DktCDJPXL1Du2D_cH9B-wa72b9pHneFBnArlU4DDfSp2OVqrFo29bAfkmegU6gLL5CIXtTfTAV46CXLYoNlcWehHz_g29qIGNjj1Y8BUJy9R5kaf5kLBwLKw5PuW7MFJ0KlC8BcVxpcjk9_Jk86FKJO-7Hxu2tkkMTzkbcfRwNVm08Bwg9KqWtbxqgNjtDBrZvMi8CJjLv60V_5rgXR3BvCIF0aaz0OMZ686pnitGd_B0t7wd6kR0t2sFLVryBL_wJ3v2JUY_EEmTMd9Y0kucSuNSdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpN5XpOsT_QRHp32AJMNql0ke3yHJ5N1iPMr4YjPt4aydff-yLbCwYQ3GMxgDQq2c8J72hiAed1TJDOT1pFsfXXui83yRrT_xBq5tuxh4AcIdNV-mwWSYEZ6d7ToassfhZ_NfqBOkb1BRy7Ekor7EZQZtNm9eYGY-37X8wsRby8qwjkZVLk8bIoCGy5HJwoJdXr0exEswLk2gQVDSKdTs4Edj27aXJzyjwxZTCJdSBdDh81W3MKXptP0dHye1MMZVEoxvtG32mFaAtUm7iaUFSoLNDHaRBE_i2QnSMbkfv_y4dctlwa0pGdFmQHTWP1SYu3pT1SM22peSw6M0W36qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHhqOy9m6ob3fr5ijjyMRhFttD3fx1MmQwc9LGmrFwFvBNNY_zpf-9_140WEuo_NlPxNS0Ya3e3VH3eqdr7qSXg1wFiLGgA1lS0IdLszLNDIJByI7T2aEfOGTV9wgAF_5T-L4NPaxubL48_2lV9UsV4_4c7qN8oXTVGgT1tc13dflEaM9-Sm5fL4186yaivTsYJLIQRkUdYMEc5XQGmnzrC-eIifIvAlKTto5z2T0KLbAqaJdQg46A7zcxYDP3OK6shUaZbCrc8Qi2LAOUCZL5ZVrO8X2Y30mEN9JepgLbPW_IE62QAhod8BmAkxGt5BjKxhJhWEl4GB6SWui1IbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=a8ot1x2Gr0ESD90FJB0UFJswsBTQRXaVDIQnybC1A2QXJ7ARGiztKbwz2_nC3ycnWDy5rl9WP6gdpy971eJHZJKi85A0g9AusrPd3cEU-iZgvzffc_QEQDponLV6jaVZMrkYX9VsJGIvLiE-klLwQwEyTTh0CRzpyi8FY2nM1EsV6Bst8IbeZ1hUAJ0v9dcvqD6JxH5HIX4rmfElZ1PmUvPhaBIfhAC_924QNiFSdzMv8rOt_mquu93qmfaujn202_dQ_DAdJPWnAnxJWUhGISqxRzxLt6AHHjkxfhCaXCe9-G8Sn0QZBLQhvb8lUGXJCCwPB7KwWh9IH221JLAsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTP0WWgiooWfTUGgsXCY6kvm2z4l1G8duRWdokHr6OkeEOJK6qh1ILcC8POeDZ5h3GqAw3sw4Np-SFUQ4uXOkbArObU1bgrzNQA0H0VZrvM4O2-kkdAhO1s9VQUOawlKi0Pf3YVSUsp6K18atbH4pF4_kNNDdPQ3QB_N6Awuf8IcaZLpXPLng94QcqSnNh38GSjSNBAopE6H5HPR7zF9jUeSV9oNaWHaCEpH4vQv47MAAm74OZ5PuTsESi0f1BK7toqP0w7u7yHoCpwfQbkFdSL1ik3jZe1ylposmZ3cPdB5hI1hh7ZEJx16wydoWxXV_T41xCctmZLp6E-BmbD9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dDJHf8ElTQlfIU9SP3DR4EzoubMjJA41uACr9yQLxs8aa0hqd0wMQmDPkmEE1t9S3MppFFHSi71QH2ascjnEXRsSdSHsrCu2TQWaC81yAVcJHQP2lBrnQouVogmVbGr5VGjy1wrR_fXzmtV09tRsM5OOzP0BJxcSB_p-W9xDixvaZegZLNHkkqKSc5SOE1siGL7rvPU3paiemFo9rWzSeRzbpd_zt_C1lzLF0_SGIMepyY5kyrX8-B4gGB-o88LLvsNtAQUw14l6zuZjXoiYAp6NHFdzIjozSXb0sjUyRNBr5ZomOD-bIaTLd3TZgkPH_i4iZtdT7Cs-Rnxp_krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgYaaYBnWFtM6wUjaRHzFLtGO8oS9gzx5wIj9YN3rVKepHmnMoWGop6Itud43n6EMAwDmo5OTId9yXkhc09NKVxyOwSwebSoitRULv9XiuHVCb2Cvv3jGe3wp3Q_ch7jq_QLEvUSeF5tJ24yJa7NG3IWQN10jLqdaYuMLNYhl75iYa9woNlJr4OFYldAKTmcslLNkE5l8nEGKjzbUOnDHZuS0rWuHI2Ojszh7N2qxFDRpa0rBYhD-yIgP7IkrwXIhUCLZLSVh6yx4-v4NHADs8iccWIonX7OXkkhLzKQ8DdXk6OfisNT4_LLXl3LD1ClJffc6gI8LSg8FoaaikFDmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn49UxswJzr7A7rqTl6yltt3t5umAlizphzabhHrXaeonfndMNbILVdOD2FCnnw8ufrjybW8TIeANSPq-AeEOOhz4Wm3KFgpiBlQcWC9u9tsJgMuCjed9nA68xQrWm_TSvGh4ABaLaCViggb6ZNdUlyXDkRKq0Kr0n2IKODTNb0p_ikecOpfHs9AK8FCc3XIOT_jRyvrvqUZuoTYDUG_64wmZCNmlfym88IRgEdHkq94KPqTrtwIjYtuE3nkwdsZ-D8uqx3ojPC2fAaY_PMdaidWcYZivPwWVSoWu7MXAsdGrjoz0SgpVz_tOv1YnK___qFbBK1lY3lYV2W4SLZp6hws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiTx9LiDBK65kKy8ZdOkyF1DwjQWzpXW1jxsBUqBrKqpk84dv6-DJwXIRGOEDaOtm_3k7b72_R4K9L8GemVnomy9URqL-Vznsq_5sd5_n_Jp-5Yt8xYDmK44aVLN3ZbkpZp4-ObBrqp5VDwgoA9_oiNSYG94X8_NoYtH9_Iot2wmo4erNMncBcgVqbB_mRHV-7DD9x27laPvyhHGTUx7ageM34kJt-OA8wXQqVm2hrcxX9_7U_GSaA2LKVl_OYGGcsqp0kjyZdRpwDRyy00HYdgyuuXOUUyfhA_hgtJ9aiR4cU_oam7HzrauoJXcp6NC_btILe66xWF-qipx3xZOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMcHg-jxHzgFYIIZF1vt-mo05SEU605OoB2GIqYVxMXEjI2ZBFnUugydd5tS41-1rqun25317wvUMnQhNMJhrB5YmkbwMxOyxUGYUJVY64ktP3oXwh48jH4bGFbNS9p9hHVitCGryNihZHytDsECEWFFIClqTmPKO-wn5Dk_-W6lmEmA-Srgos7xZYXfBUNk8nCeyQUusySGF4M_7GydBznsvC6SzOtD_s_k2piMq3F5-g7vIeGWDC9obt9AqfsHlbCPZk-t5So_aBYyvD97y-YIpRb9GfptvzaOZkgC0e_-ZpEmHFwcCieU3G1rWpDpCzvaaYCiA8DMvBjM69r5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZgrqZ830FfA4cDC7KmXrsJv9aPRLpR5dmlRIb7VVuAkABhV0iuH5R4ODfMo3m5odAwvI_9Rqb2DW3BDXO3wDTqfohgVddOXjVTxTd0OmW4T3HEfEn9Mw-K_d-fPBZUX6MShIODUkDVuK7BOgzSFISNim6VzG4r-mi_OMo17mhbcefvownxltGlbmkWoYmxRHd5_ky9AD0IVqzyrQmtaTnhrFdnahuFz_LjaNb9lZrtSeO2QhSi8EjedmItwLuX8q0d2uhBAR-k6Ssd5EFU2Fb025sawt4MXulu3479_U2246wX4h3DNAviiRk9g8D1n2R2s7-twgr8beiYZIt6M6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B357tKHCB4INedvy_8hxa-KwJZRMvDhJhZ_eEAFuPjwoDvN7MnPDhOO9SRGLMhvm7DBh-FEUwEt9fDI_1-pPh6nex6-Nq4h_fzrI34i0XYNEZLhmoJFvXZmSwwEV4OarV6WOSLVeT-zwnTYWicQtUTSEfKTSdnYQWpRdf1NlPgczikzDA6pThLrrZkG-RNvDWSiq4RKAKVjRhe-qX2Cxn81PSKYDXG_HCuk9YRxVrmRodW6A-wuGhDCawt8MCz1Zc7WD_-JArB4xpchleRvXpCZdO-FKoeyO_gf5F-DlSLzHbiSfC4-vrbMZR68ethYEiyvrps00eF1EHFmo1jjYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOM7tl8D_8ZMYk3uvCSXnGA4r_VG-1_VHqagYpNzgjQ9Pvoqh8XIZe1nyz5jSzXMyJuHs1hzela7LIHfH1fbJKXzXa7pTpu3gk0y8b3aQ6BaTPhkThjPiag8PvuKYld7kMDHC4iFpyas_C7W303Cuj4O8Q4UzqAkjCpy3kwz2CxqsURKhvD2qxdbbJh8WbWrwkeN3cRuDQCd_yu0S7u8Vf1ihBJOz1VGB_MAKtpQVLCXelmXCBMjpjQDCGAoJ938piwicj0CC673UQFYHb9g3eTTCD-PJTFl0h905M1jzhqwMWMWjB9WA_CsuUgWGsXi0Cvb2XImqH6qcO-gwN8iuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrEZDrSpZi__Cz_PkyGd3Kijqvrla5kmi7hZXTQz13KeQJfgMYP5NCLki0C-5pDEnTse1k1YZ0f3c3n65xz6sMqz4_hzteJV_pS1_SO54WefeC7DE_cybdhNU7-lO4jhKImUzmx5OGSItMFa3uDiLK4lV0WUGnasnp6o7FTr4JLps5y5C6T8lgQE80-2CMH_keFwgD52wqq4obrxMJU06XANnIg79nAnVkGsFeEd4iCuFqeSSY8HMAZoMgfd8YtzECNir1PM7U1YktEF4uObproxvfyr8GZmonZgPThaBho2v8zpt__XPw2QBwToR9DZLuMsYbYB1p-PmoOB6kC1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izdm8cA1pw2W5z-7tJUn-biYbsCzEbXtcC0RPtd5tEZl8odOmq-zfQDVvDdBw_RiOHM4TbQ8bookna-04QIVkgcuoyf2aIU5ga8t2xsI5mK_Ous3_r23exOJ-lv3vAlrJVyQdB9nZvbV9DHxQLijUiBrQSLdLG98sFBTo9W32y08eCRHRMy9wQan_8wgIYTDh1O50y0bOcgfaiJUYHbmx29MqYyxd_tghyFilUV_xGu2QbVMvuPhLO1elVfrGbflM_erkG8qV1EqQPyvYFpdNxlUhOZv5LM36v1W9EC0u0Na5dRmeEkujmiaYQ6Jy__Aa-VPdJHUyk2r_Qi24zMTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=iebvTlf-nvRnn_gCwmJqtT5o_G8w7FiS_UxsmFwHB6n6c1jOEiUL-o1A2NiDRMd0RV8MS-O-usfMIrvsqroKPXUCgBwfnmbClG5-FDc9JFFlFQGSDLASQhoVW4v7yVMl5ZptZwhX6Uee3bJ1FJaEDiKikp6k3Jn5pgkqbv4RbXzSjQz2IkbjprMOimvR7M9vfZClwC76rXWY5g4ytHuNPA8ArqHr0lk6w0VcDGmcqoKuNkea0vht8k8Qi-B5Gyzy1LIdal5kSSCR3EzhMqjTzTaM1uyqHdpCYVY_S3JO2w_dkPskEhnNPa4CqC0cx1H9whHkmxhwqsvQjqLP-5Kr3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=iebvTlf-nvRnn_gCwmJqtT5o_G8w7FiS_UxsmFwHB6n6c1jOEiUL-o1A2NiDRMd0RV8MS-O-usfMIrvsqroKPXUCgBwfnmbClG5-FDc9JFFlFQGSDLASQhoVW4v7yVMl5ZptZwhX6Uee3bJ1FJaEDiKikp6k3Jn5pgkqbv4RbXzSjQz2IkbjprMOimvR7M9vfZClwC76rXWY5g4ytHuNPA8ArqHr0lk6w0VcDGmcqoKuNkea0vht8k8Qi-B5Gyzy1LIdal5kSSCR3EzhMqjTzTaM1uyqHdpCYVY_S3JO2w_dkPskEhnNPa4CqC0cx1H9whHkmxhwqsvQjqLP-5Kr3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djEXvjreNQP7o05saEIpqEM8t0y7ho_BJj8VokyyOZWr66vPU684lO1Q26ywzDWKdUCCat-k9aLp0OCdtAqMvsv6i3SoHtD6KnSXbPjwBGWrP091m1IHHuVtSr8SkTNFobPoww1409ZLeXbfm5cyG6jh7Tv2wlJgBZk-qOlCV345oh5LImxldUHMBQIPMAjojblxoZN4NenKXImwOaBM5TwR8NfO4lI-RBuRAy3iwgNKSdvKZnhgsIZ8Um18wO3FLGQnECr_u0kHkB9c9r4aOqxTA0pWQkH9IOMqG5XLeVS9pDwpswWcjR8okCrWL_52skkWMMD-w9LMuCUu9kfBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYo4rm-_9rSg1751rEjybeFBLFLal7HCABN0iSdowpli8OZxbV6YxGmNBhRyr6g2_QOnq2iEA2I3ICCPGQuKPcjt1Ys8FSaaRwoktusrSLB5dgGByqiXWVScDp20DpCdGIBb1PvwlTH_LkcLFoL_ENUATDR-ptsnMKyGCjU_H9e4OGJmO0gYjeYprP8JprlY6bBxxxOhkXNUEHEvBWWFqAgOyFMLq6CuxkYEZWSjeRLxfS3oZLuHuTR1rE1c1PpOhjXUlEhBdmqdKZPm__ItC78OubjWuPxD3M1CvSu13weDNIBp3cCOHBdzw6A9Vs7Y6pEIZWJMKMx9At86wfhdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLM6VaobmqvN1u31WWwOxVkhC9MeDyAqFmPDnS9rElXG0wQBTTPHduJjJA2xaj7UM-nkW1wU1-MVTGA95qKMXB5jQSYEa0siZ-4DG9xps3a8GXe9VAZx76rdH8tMTNU2tLmQZLfNB-SWdpgd0FLFVuPEbKWPTMd-yz_V1ORJ9tUjdqZBGLNnTKXrhYuNdzpjaPehGGCqP2IZLjE67ghgXpMF8DDmT_moV9b_-E29rTVsp-Q_Zwb9fbFyL-a4jFys4brfUtUPZS-RhP8PbsTUjG0AO01Ljhs9h_EKDSEXxKISZTvSTuhNF0VrpdOoti7nFa9AXucV6KS1Jy5w4s4EpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=HXYPPv7FkdAmrcwdGnQEgJVVmYtL2Y9n1GeyETmyuWiKSRglY82ZPG7Ykgi5tOevgP6gbB4orGK6nefgOL57ShWJvZOZEJiOEzwIkbX5hn_Oj1baTe7dIiNoBj5m1nji8KomoA-UcZsbTjwsdKdUPDbAGD3lJEwcSIGITxHAvLfzhvEgshqEHPvhBmf_Pvp5wcFju3_IK5ur2E2wNFf4ZuJ32MXbGep4HU5hF9jOh8X2xT0NwRcUHTDtnqV3lnZoXCo5wZswpqFVFr6w6XDd9E-0YfBQ71712bUVXtcLPUV5UnQg4az023kjT6Z8eZMLbDxwC0oy6viupwyzkggazg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=HXYPPv7FkdAmrcwdGnQEgJVVmYtL2Y9n1GeyETmyuWiKSRglY82ZPG7Ykgi5tOevgP6gbB4orGK6nefgOL57ShWJvZOZEJiOEzwIkbX5hn_Oj1baTe7dIiNoBj5m1nji8KomoA-UcZsbTjwsdKdUPDbAGD3lJEwcSIGITxHAvLfzhvEgshqEHPvhBmf_Pvp5wcFju3_IK5ur2E2wNFf4ZuJ32MXbGep4HU5hF9jOh8X2xT0NwRcUHTDtnqV3lnZoXCo5wZswpqFVFr6w6XDd9E-0YfBQ71712bUVXtcLPUV5UnQg4az023kjT6Z8eZMLbDxwC0oy6viupwyzkggazg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rffbw3JWzNhrGMjjzU1hdHscV0o8VBRXIniYK-fF6q5vAu0tUyG-qdBkuNE0sEDBT9YRRnyHJH55q86XFH5BygSFjpMkC2GmS0OiN6xC3EQjrEMCZKz0fhUzLk1hE2OLasoKpSOdr0Ht7PCZ08VRVbCAw0sP49oGkUEG1ALFFh-NYoOk4g58EwTmONhfaVxf84TFgqjC5BRDhCt4Nz3JvYqtikJchxthBUmjsU0Vckbv_lQS7MC0gQgAVpOAcKf55Ot_sT7hyEwVlIr2zFaQmNi-v9XCTGriSi5Ubac1HygXEuFvZMgLO3aFqENnRhvzemX80eDH8zWedscWeR8mdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj9TXEvJxVLXe-Jd6wUWm_j9ddHRGP7vZvbyWm6ySO_0yeXEEZYY46UBlVsFu_i_wFYCyUJMwv7TJO1hV3qreKNHLcL6ttwN49b4avidN41dcPUMVkHDKbFKtt4WuGlGxA2FBzmCajd_cGVGQ9N0JuPBzUklCJrCDzBCHZYf3Y9xDPjusggJlUo1Qg5FxCNKlkQCEwqpb65b3Nn11GDjtSyY7YWIOX0xpXsB_V8OlluGksySeBGrw-s5Bom7usCIgrbqBjqXPCSkf0VeTrSL86Gne5xt9XFe5Bwx4m2PpymHusk0gFXYMvIMCIY_eYq_CkMMiL-9jkfDx_1iyaKfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8ilIPrNDWPeMDxPerXziyG7QEf4JONT6v6ftjit5QeTJfci7srcBCp3RAwAcKkY3L0M4AUlP4mnyTB-kZsEZrZ-0-JWRgzQm2SWzKabYoGBF9_oRByaUyvh_5krrTElBeLi0sMi-vNhgd1nK6AYGntPODivALWi0B32VfL1vikLlL48UPvDrPAB9UaNWePxHwsn_9nukShrCwY3zSfXKDNnAgaxyWKYiTTw7VjlEmNunAcmqLK3sZTPPEVokdjJiGWRrgOG4sCi9MoHcuvt0uYw_G7L5HeTEZlchsPBANvd99J7c1Mg4H6yXkgZfcGVcqz5eTdGtNK_jHHtWhcOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQzJ7vqbySwJtX73drekEBr4NsZ3ORs7wGjHTEDZ8iskghErLAFArD0HRPLLtYfHEdZ8TAXIsvmJgc3DwvwPPuLxKh24cMTDF6wxrleKUi9STJJDn-o7Ut3V2nieERAYM-E6AiJ9dauM_snGA7U-CrIlsbuYxZIRRaXx2ZXh-C8-SmonhqolVm0Qr_CoCzzJxAZowieV2zJzsGUTVbJ597rTXgm7SPjrlSIby8ZYR8mb003yV5Z9gOzbBFshY5bnoCiPo_UVfCbl6ac-7TYy5rHNp5RkBfVPZwOJdz1ZKLGh6XXgqM8lrgpkOqiK8UmH7RFxdMugkt7iBB7wxplBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5h9fhC4uTd0dJmnb7FrqxZ81csrOAX1KGgTkUHxJBynVnHM4pzsAPaUg-tklzNqGIQMRspU0qCZIP8LaOhEF9EU2JENSPtm3xnxNAzMxdgzTm_-u0Oau6l0K5WNsljslTpQCApU4wHVz6zg8gvXaQkofieNlTXJgb1Cx3HPer7v4d9rB-FQuM3pVu58ZrpBBEtfYFvwl5nyKDZEy7Wryu5DuQj_CMzcRApbGShXuSy81nxGv2T00Hu8baSh9DAgHHSnsBep4fP8wQejsCVfpUgzb-lCMlWp7seXFiqcPW1i2jLLyHaO4mqXOjQ53pAlthbblOvrskfhFI12uTraoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3HZuQEYX4nNEa5yWg2v3F4kMXDjHVMVkdmrIGW9D9aA0hkV6k_eqYdxMsQtu5kj7vusq0ZAVJ-KYEE9bdzTLt9uICXfYpwGTxpSPx3A1LCWZYIaO2NLoNbWhG66KJrPTKUMlinmsljdxdMPoZkMhM2AdFuWWyA__nQXGu87-pBRbDdQsfmxWcaKE3LBYPo7yFiooihBWZJHHLh8qiolzpaPA0iIDXqgYdiK1G-OOCPHHttSVQte2i3_b9tYrHl2VlwQndaJ5Z4Zw6hKw_6IsVXg0rF3N4F9sqTQjwSH1Ay6pyil0jHHQKQ-x4pJF9OUwHQl9yRs6TmXTI03WAF0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWRGr6tR_6zVDg3Zf0XfvXKW-mY17kMmPWUd2NSDOODSqIlpsclbMJELLxY4OK41vbND1GFc0kqBL4ZrMBMwfFsMKiUa3UKOokm7tCvTgSkW0o_-FlckGlzysstHlqiuDzDDqvNIZfWuVnyZBuyZHifoNssksnhScL9oqgSejrYjDJD1j7rWrnnDHargn-_z9h9AZvVOdQ4qw3NMNSoYUR5f4LDlNqIBO4Fzg_tQtN5J_Q0yIZckgfsJD7QrEhIoYy7IffOpgyqpNg46Qo2aC2GFoUOmhqz-dTGhj-u_bMZrI8NgWE8JwqcMj8nsl3NfXHCgxR5SPjuJ7jpIDOHHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKxO6ygZLq1nSqQuoHt8e8jSuawDtjUpd7nrUeF2vxsL7uh9HzFLRb51wfEy-O_1YBNldscGGAXS0rr5FEcaa_E8tktjHf2Icf7xTtzRFZ6Y_cE0KNjbEVvN5TEFBVILCBBKeeBftQjkMPjOlj-HTlYjyZ0_wLK9IbQuBsy9fl0PpYwN7G9xqhTAA5gFMuGERw6EMCX0MqlcmfxKk9umlbR5WmKmggrG6moQTaeu_tOcDhra1C98Y5bTxVf4Bya7oBs9NswCBwAKPaIKjccPGnzjVCZ3FdIdRrdH2Ul28ZSAu5S4bfYoDUHrvt-auuoPLbBlfrOr2ZEuWFXqFB0TlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJpaNQBWaBuaU0YTpsANvRcS_4YR_1mCow2A5YMro-ofuJoJheofcAsk_HJi35QNrFoh_gCDXyItCw3XykA6mMZ-lfgLcidQMyXJI_V1rgxqJ0GXOh7We7XkLBtt4f2pXSM-Q8yTAJx3BP_AxBhFLxwV_31TgtbfJWrAx01ABDRivIeTTa02k29bMYvkI0PUxrQXmLHo9q7PjVHF1xADVa7yyMnJC5my473fiZOFugRFvIIj8bG-H-3v4Wnc1vQgzQCQRZ7QxdNQtzrZjqQR9quCa2GOpGXqxNBiKFoNCYOuoF7tl_XO5Ud4HPTwGnxISVsppVFQojCJxwMj_KVaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAP-GtxQi6GlW3C6zhdVl1BktLDfanhEgJy7fSPzyu-5Gs4Jx5g_DBvx8n4efI7CBEXCPX4y4MOog8am6RFpvHVwTPjrFTJJJDZ3Tj6e-EuCaZPJTo2EJycra8Jn-9kF-OJgzTgg1NYR44MmL6lcXYuf2lBh9G6GLdW3obggOIzJKuIQZHJYZPUZm2tl4OjudtyRBEElOLkMAqh6KXSHKjDkGvetuBoltv72lO_mjdzmsS3dqO0TpchpsY3re64Lw__L4cwAWXv_tjDro8rtKTj_kkRC1lJH09sT9_9UcVPBBC8WdQDi3HRXghRfEYdvhJLRhsK2kobq0xp2eGTldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkHDGAQuZWyfNfLjbm6QxLIgH6nAAQWC4Ve3Kvqv53v1huJ-ZlLwGI1rhOunx-BQVX5gaSFzDHm4ZGRH6YwCdGrK6fqLQ97hkAwDbAuTUpsXCB0OsqG0XixbVrdbNyx0-X8vW65RiIQn_gfGU-R2atQ2ShdYf1lcN8Z_8LtX0LT6uNqoGtNjciL_8AxZ2nsN1Sj_HBKItZGh0VtVTJW-rovx8-B8z9W4K08Ysk1SL_B_Xrvh439hvP4-0sxrRztK1RPuHYFGvJBA-yzdnk3xX79xyincfgI8uOqwi9FcIIxhptAxRacyArJ25DugkC_0k1xTGkMBedjC6_VtyZ9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3vAWHg4Bth-ePONmA3JF9zkV3NZ_OV1_J_zKvDdRAtGwR08dYs0KfnnXWYG9OVGoYdOZ1eiP172vvPTllSObP8nqnWsK17qvvOimhKtiOe520HEyqGLYyVNSL24Mm0YmOqXZ8LcntqlNi5_MEpi-XVcrXLF0gm9QunY_94FZ2FIAvspBk3imPhCbn03caaqqnvaB0ESU_ySuzziWwgDy5fmJNyKsqh35Lzd54WVrwWmCJnCY8BJ_NaGyzpQAZ96DXg2G4LNjgbSCN0V1aYbac7xl1ewmAaqRtxhTC5K_Is0YBSWNjRiJ62tH19lyOJtrB066xNC3ecAflhtJeqjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWbTkxZY9d4tZKJATs-PLg8yDq3Q2gQtzfgiDGr83u0rmoJODdl84y_VguknJ22MmvLkhbdwmFaHvt6zCuJZ-gPZUDxmfjD1PALLpn25d7GtrdztYscY50L2adzCqNfY1P2pMUBrR8glTmvV-B6w8B1BldqHZKB7AzlJ5y1e5asIIWxJxnAim-uoWyq-wXkWC_i9kmjFqF--6vuoCXQyAQb7rHBflSgKLfLV427wpvABDpLqED8II42twV4XzXBrbpsPxBNqEEX4980eAzyM-79Sod3Eyr85qTbC7Ypj1EDfZ5TR2qUmLGCYa9p6PLblgMH1NQUa0G5J-TyvFeiMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVEE7J8GFoyiE0uv-pndJsLjaZLkLzN42UMMTvh6nLf_CwOkDDmFdrFis6MoEKRAsl_SHjdYyYiXlp9SrlKZHMFnQghX5rjTIk-SDcKwM0ZE-UqjgVTsqVsq_v7ZF4xPrUSaX-P1UzzVBLeke3Mu0SrLyL1-OAuG6c-WPvNoAwGGOxo2Rw1O1_Zrg_IRaPqWWTtl7y5ASlcfOWVQw9FS5ghw-BsbjYbdFCkm7pfyWo73jvlfPPTnEYSCdnwv14CJZSa_9C7euRtkxkLgEjsjywPuF1a8EgwbVhS85utrMgA7zESV_U91IahVfBh02wFUGGvNozo7xEWLt0ZuS5bFlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5CPlMVuBury-WEX37T1eMJxM2lNOCGAAIkyGbguPe7RdmGKa1BzSIee8mwAw0oYuMLMA83NKoU_jNMj2tcjtUO9ZFdAg_DeUw_gKaWdhFBhcgPSaL7JQByGi8x87U7YB4MCFXGPb9gYe8aUGswwAJ_c6dp9rJpXSQ-czBMOwdB4GFeVqeXAUPiEvY3m1drkO9sUKp70B3PZZTXw3yT6j2ghvBhvOGrCkYNxDTmQ1Mp8gL-9F9g1b3YiuR0ZLYKL9u5LlCf0hW3F9DQr0qhZLciBtLXu-7AANCf2NjpIhT2oyAqYIo4zQLS5awj-PJrKVWLqxV59Sbt_Z6cCeLq8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsFUYzsW3YWrDqUsXeiVh2JDD9lgS5UFlpZAf9dTLVCv_d2iJmkMO-RH_1PqudQMIhV0CWBOo1opmb8RW6gOMr_iQ4dcppFzuTtxt26XHDKfUWtmfhSa5KkRR4mKzppwUPfDSTiIWqtHdtcNZpgbEwntwar5-1l_SuPN5IijfyyLgAa4NcZlZ8sicWp5dwpUrF_B-RAgOM2Itz5pIesHRp0x-9dt21DCzPiVN8WpNAh43AY7-NF0WWaxjnnUNfB668XlV7JbqTNJewviKdfa5TRmPfugku83hs1g98DHMsLg4IHqDz9QE43mM0FQV3rqWEN6zMrEZZke0AgTbOGpdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXCIoZe0UO2UVleG_w2aRptHbBC1TwMhGCqRseT64E7j5GJmOGxCN-6CWDeo0sdI2zouqOrt4InJJ9ll2P_CEijL5tClXbxlpi9TcVHIo5cgY_yd-0Vq8WlDNwbT7gA29QP6ofncSxzyW3wfMc0jXysPcHfubaptRSc849g_Cp-HadtW4k1ZO2rSFMJrmW7N9HvL_Rzo17zf0uAySQ2UozxwiK_3j6cTmDbapjr2O5Zx2Ka4y7H0L80QpjjT9ikPJHC9g2SRnp8LnxqA2kbw4LOZzkFEtyKTbaUWdxwA3nTqtMW51wpwgoFTbcYPCwj1qrfU_ut-2TlsGXeACtpBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=ifTfWmd1p05nbCDXCEr7XD7cdy8zTGkVUzrQQokZz58RkDN-gSNVfx79MmZPQrZCChW4zfzUR076pYyb53bfQLbQCtmS7z2rGMyO_qBEFwpGukGy-iBFD8GtPcQyHEwD_3IidP6P9kKUdAsmVnTwEAC_-GwgOxPSdd7JNWepAN-FE2FWwcROjx59kHtVpHLErKCaex1QmAaaHgcb57JU3srBuOQlhvmZmn1H4iETIKJxXAuAV8PUdhfN7LTbmHprTxZSLYmzoxFUsyH6jty2Yn16UxMaflIG8EtfpwZLFmeDd7zPTdPXM4zliBc4CEULoapyhUFdrj3Wj_j0rSuxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=ifTfWmd1p05nbCDXCEr7XD7cdy8zTGkVUzrQQokZz58RkDN-gSNVfx79MmZPQrZCChW4zfzUR076pYyb53bfQLbQCtmS7z2rGMyO_qBEFwpGukGy-iBFD8GtPcQyHEwD_3IidP6P9kKUdAsmVnTwEAC_-GwgOxPSdd7JNWepAN-FE2FWwcROjx59kHtVpHLErKCaex1QmAaaHgcb57JU3srBuOQlhvmZmn1H4iETIKJxXAuAV8PUdhfN7LTbmHprTxZSLYmzoxFUsyH6jty2Yn16UxMaflIG8EtfpwZLFmeDd7zPTdPXM4zliBc4CEULoapyhUFdrj3Wj_j0rSuxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p99isDm8Dm5UROPf2HRqZ2oAKuqxh4X3XsGrqfRXFswXWuZ3IayqI7eqGSUAKxhz8fUe0r8LW20UeYty_NZcrcLkwNutVUshPlmrzJ2NX94jRk1ic2uvLnXF-1xys8bVRZ4_DlbqF1wwC-YN5RdbcI5BInbYiHp5Y0SedlgtWQDzNKkraGwFhoc3z5qF5mxoLMutrEbBd9TZ6YOENJUGRcT7DhEb5ciwE4DXPMjogrwnsgmhTvbtnbNalH7VBOJDi5FL1FMfimcOT6afJV3Nkey8ssijXV6L9uMKbxekUt0AQOmcXACIR7w7zojo3YG-H3kDORExErAeUnKM6246VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWFb7K3m_w1qur-MvaH1UiS-XEcFzhtd0NJUpBKM4XMY72knWdspsGhsrq5f_OlAgVBI3MN-ZwTMt1IZ2SAVzq15SYSxlzpdmAo-Gql1ZIIE5NAwX6pDX67hI8_miQW5dA1dkMAtC0t-VXxnGYlYqSd7GCYj6S9-ngIq3aAUv5uWJi-Z47nYD0087faVHMI1au8XzXJa1bQwjAAaxyT9gQ_JuR8suAkvfAaKtZcQSv3AZ9HZj_K72j5bKYua11uYutxqw6WOqJZarRT9LsYF3nTqVBxSqkxEgV2jo75EDa7Aq1Smaa7w9hF7tEENK-gOaPaQJBtdwjYlTOjc4Adh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vaz0oSJLqmiBms-gh4nWT9Maz7OnY_Col6_kPWNea3BcwVswdCOYAcR3b5-Kxovkz6r5aXgucRBjjR_qDLcN3WoCJsjckgjBeVfIfagX9ZFBENvOGybgHbNJR-odItT-tyeXB6oWBjmyHafVIPnuk22DTKPOU9LJv5C3J2dwSoZIZ9awkMsnITh_LDbO7tcUJgh8l_bOoGgo92BOuuNgtLnm9_iqXYkbyDfc173Ft8ylbSIX2P3NDr72x2rbzo_Z-_riSzL5H9ocRpWGuH42jHBDj57t-9GtTctbFMLJlAShku99lxCy0MhupejTIUHHYaEThprIGZbH4pQOg7Amdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-xK7nBOdnibeaWR5_EBiTy-WC_Zc_CARbjFcZbzj917aL8hBkYZPHAfhF3QPG45W-hEPw39Lc8qEjoULEJfRhyPyXgyri9IeOo4M1oUESMGKYbsXovNW2yDE2aUb9HW7N1pNVJj6QTePDJRY-fhulMqdCYfwzWfLY7gfVckYm_jiAiWs3eFde_jBbLOAUaVJNDq2tPHPNuV3mh2DOyPtpKZ8C60rq1JfhSExdS5Q3tJPXR_BsHFz5vJhGRKB5VQSklAejwyAQmcaRyDaIeGZVNIULCfyNudHWEsndOdh-9a3msLWCA09-6TOVwiZ2LqDLsYqH_jObgQgFEoncO7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsyMUIX0B8cvKjRbSVEzJe5JbW22c6PoPZ7Cc88qbMP9T80ajEi0GxzbML97paXqa3NliG8PVAfu2vw0MelGPUvoSAOCN7bNRhPpXW15ojDTm3517faRPxsV_0PqNGBTNF33W3RRmtcvyghiyKac592CGqPD_WE9VO7ziA87s2oQuo9CDYRxdytoFbLYdglKiqArnF515fn0m4xZMQf4_6akNXIZS6A4lv8fVSwCpALqC2gDW5wAkdzK5EdKzYI85EofKkzrPGacv58EW3B1p88njjL1nHbww7JUElCiidY6olutLzQqjP1bWzweQqfHfbHd4Q3-Lftz2WQ1Bz6OAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu5uaXXYF3oGWLUK0KADtNgEmfJdK2SUU-jV4LBtSmLVZ8UpixuhczumVHQ5LYsRhzR2T2Q9oBfRSxEDQcIO-XjcPyjaX2xvwY5Emhc-YRE1SFQXohD-5HRPd1xnuWIND0jqUFS97A2WhWBtDS-dqRTHDCxfBypme6a8IxgmH9OKmD242DgZ-V-ILY5jJ7fq7qPQg6zLiusWYB-DMbCGNxHparGddMXzKPzlBalurvStzWlp7QRK7Oa8FAVcIopZQ0vOnjZzlXWKulFKAMjhflP_WVqbDavsgjNXd_Oow5_ZaLbXan0n4wKRxmPk7p6prstZ94HUC6TMpIMThRfH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT2P5u-zT9lsaogFQu8esNd1g73gyqvSYGq1aB8RdVW1Fhk4tTuWGLJ75oRZC7S3F21pph3rEcI3fHztEclYWL5XTQwxnvJUk_IH8zxGfcSdfLwe6U62NlIxTNUqxplN2hBSgj3OuOZW0RWAQzoY4nJjP75xX66h7ZquV-DqSAyvXk4A1FZmSvAG6nB_czHF5nMXBF0NWINP9J6wdx1YDzdOg2IsXMtCxlHDhtV_91P7YfWQDAKND0ysWoK-YEB9KE9LJeyz5kN-t6D3b3XznwdHh_0wxklY_CiAfpxMO9kb2wV82SRRdZqRA83jHHyzin2k1fKZsSzzIKg-kPRP6JSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT2P5u-zT9lsaogFQu8esNd1g73gyqvSYGq1aB8RdVW1Fhk4tTuWGLJ75oRZC7S3F21pph3rEcI3fHztEclYWL5XTQwxnvJUk_IH8zxGfcSdfLwe6U62NlIxTNUqxplN2hBSgj3OuOZW0RWAQzoY4nJjP75xX66h7ZquV-DqSAyvXk4A1FZmSvAG6nB_czHF5nMXBF0NWINP9J6wdx1YDzdOg2IsXMtCxlHDhtV_91P7YfWQDAKND0ysWoK-YEB9KE9LJeyz5kN-t6D3b3XznwdHh_0wxklY_CiAfpxMO9kb2wV82SRRdZqRA83jHHyzin2k1fKZsSzzIKg-kPRP6JSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCFGSwXm1nJlJT5EJE5CpQPRnfKhpkhfQzQ4lQPfkCglELuMHoRbCyVY13ieQwT2MxL9B6MybKeBmVbK-vRBY7uvyFuf5B4ubI85PclfNGLB7AB7dEjk5R5ApYZu-P4QODcVDsjzzFFLG-QiZFnAnhgj4r7R9AWVW6nHPnCt3LAgFKUIt34-IBAIO_V4tuS3Z7dzMesLIebvwwijfVPx4PuiphiwkS5uSu1NZYeKS8GbLrflZvofP0MRjlBgjOrzY1zwUxgPRULc3ieVqP7IEIVQirsDHvfTY_JVU5Xa8s3PL9JbTtJag1exxiNMojO8sAhmW71IR3RKDTaYO-VrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJSJAvGyeEUtZlzJqdOlAu2kZRRDdt9N0eYHDjJ7n85dCcKoPo4_igv3rZkMh3zZ0tLU_LCFLHpaXTNqorPzPgJHJQKUiB4XRaoOqLDmuZhNA5-w8uJ5whnkks7cLPtrbsmpIh4m0LMj3xbFH8Rk75FRvu60DxFxb-vIpzB15kbev-4uYbwp_zhbdQcuYa9fH0LRvQy2NDj7L9N0m4acjxWFAKKKHj8hj088e4BNWTEM0D2-IGiKsfN_BihMJAuez7h4TypNxPWFV-U2AdgDW8lz7CLVMuF_07qp-sb5_DR6JCVN1et1K8nWXeJWdL8OCYppEq1aMhZw4AFi5E615Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPZTnzAHLMX370JV-TNSy8FJUn6Y0TrQbE6lepi70FwXGg1xf3WjAFUwhVV5IvE2z0DxXJ1q-375bjSJll708pPKhUv2dpCfK0gWeDA0rRy_RaOdhRfZlNMXG2a9R7OPl9rwmbL6AYiPvK5KTjP50fXeKtQRaTk5pkIAZvekkKq7fEyLwbGqdBqHC1clFX7Y01tZtfI3ux0lyPi7fOnqKZeJLBGwP3gvwgS3-mAj9vL71vVHbnc7YGpwIapo-qoO-6L7uIpqZTcNgr1S9sKmfBVGRvEVlgBZJVOXDUTh7Ui96TJVSANlZfTnPyGz--bmbVLJ3-i7VUEuKOW_wnISFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=EkVat5cJJNApVmVwB9F5QA46989teQuJrtFy42kQnTuvQTUI7lfJZLmO37bqFDesRx4hW05tbA7gsY6j92tPgzmKDOhahimYFt5gHpW2CjOWq33JOO-_ShIoE2Jj0UZlyArbuu9sWCBYU34uISwW8rZkbbbTH4_R-aTJTIRjyweh4oxuoLoiYhuizzisu_sib1CuZ56leXlXNoVTQZo0eQhgKpJ4qcQXrj0fkgJ7N2QHhxhuCmwrXlovMucVdUvVz2bfp-jDudRkge7mznqLb_PgvaVhuowdQzNF0eMooWq7KtEyX1A_nQ_ARE5k79tVj1Q7_RegjmJoGBCKmjcjCbPKTU0TZsNHY6KpMva_ck3A2chs0RCvWL_x2Sl3lRNJsttFKkqDL9KMgaew2pFTWTrAmWeLFYXROIGDFqy1JBZWLxN5LowgXc0-AwPwmSp5d29G4nLKA-o43JUcrsTpFIrUnwt9hEr1li2TZA0ZmJWGk-sipfCt945PeFwEb_4hFtwpDKi91t_Ckn90KRCCXgiN6bQARrSqSwWFtJDoVBEB3WmpCbXunfSr1G9LGH0Kp24bKtd5W0d9dockCaE3yAksdU8yb6ADz8Gr82_hWIS3W8QByLKbkbC0JfSmpdCDf4mUNop6a9Pd6Z-HGmoHdTSERpz38e9wbPNbv2tU4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=EkVat5cJJNApVmVwB9F5QA46989teQuJrtFy42kQnTuvQTUI7lfJZLmO37bqFDesRx4hW05tbA7gsY6j92tPgzmKDOhahimYFt5gHpW2CjOWq33JOO-_ShIoE2Jj0UZlyArbuu9sWCBYU34uISwW8rZkbbbTH4_R-aTJTIRjyweh4oxuoLoiYhuizzisu_sib1CuZ56leXlXNoVTQZo0eQhgKpJ4qcQXrj0fkgJ7N2QHhxhuCmwrXlovMucVdUvVz2bfp-jDudRkge7mznqLb_PgvaVhuowdQzNF0eMooWq7KtEyX1A_nQ_ARE5k79tVj1Q7_RegjmJoGBCKmjcjCbPKTU0TZsNHY6KpMva_ck3A2chs0RCvWL_x2Sl3lRNJsttFKkqDL9KMgaew2pFTWTrAmWeLFYXROIGDFqy1JBZWLxN5LowgXc0-AwPwmSp5d29G4nLKA-o43JUcrsTpFIrUnwt9hEr1li2TZA0ZmJWGk-sipfCt945PeFwEb_4hFtwpDKi91t_Ckn90KRCCXgiN6bQARrSqSwWFtJDoVBEB3WmpCbXunfSr1G9LGH0Kp24bKtd5W0d9dockCaE3yAksdU8yb6ADz8Gr82_hWIS3W8QByLKbkbC0JfSmpdCDf4mUNop6a9Pd6Z-HGmoHdTSERpz38e9wbPNbv2tU4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwejAbn3lRa_mw3vYJb8mzWO0UFElTqercyYLYaAEiTUjCuq5BvzR-pJ1JqJRyst39TanzWW2sXbhlfkNBAwMrx8cGcPX2bF5BotWa7zvO4DtRTsPmbptn03PNqa2STRyvczBKqfN7QtBPql6Zet-irBEGuqYiKRCTsQpkAUQndQQlPSJaVmVr2yr0r6yDKZI05ektSqX56dSE29b5luqwLInU9_Qyd8VaUD42wce397un6NutUW5kbF78xjp8XuDa39R0esDZ90DAPK0spPhS1x5G4354EqMR2OCmMMU0818A8mzkYPoPojuCCXnEELwBezKYB4DgRxBiIuBLY6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCqQkD93QKgTMTDYFNXlhy_KMDONUHNfDtx99U1ReEjc6_q8FGtrDsN0aoS9A1c5R9EnaSEX42xyAVDPagPP-6lmEL5PUs7QtgSGRb9iFXu1FUHlaBE1Dud2Ruv80OK3bGnF8AOQdh2q6vWN34HQt5VIjrUuK7p5byYGT2BaRM-0b5n_joaTHC6u06zpje-_yD_s8edfapmgpN_UFVSXSFRoNsxWa1osU8iKjqA-l6fP8VPBbTiIQzp7X18ruzWlLK3BPCptZeH6Tkmhm3hbN4qHdjMRYo7tylijrJGy4YCfRHKgfTktgYSTDXU5oNt1eszhrbu6IDh18qUf4h8rqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=niLvYJBqyrmuoith8QaK1MaJFxFQmzdq1SJJcTZHb71tNVznL0-RadOnHo4gUvjBFL2gG_xXx4USccmR13oCliMpkVQ2iFZFQFfWyNqvAwxzldPrqCZS4HpaQz4L-2EP3fhg5OmB5IuMY9BeCZlfBAnTJDY--si05S8f_vJM36aD0KhUZRiuhgbiiNmMxwycsDZbGBjbp5FrpyC9YjC-BF9TEdj0N1Zxd2ZjTY03UJ2_1AX_0Dh8jz3bQshhMNuhFKn3H0V1qgaSTxu6DX_WlWSC6Toqj9UeRlzx8ZUXl9KU81ibcB3gtSsW5Q8sQCef2jq2z6kSPILfLeyEkTJ53W2NethGbrfnUSgrX_A8ZXXVD2CjB9CWsORz07vzD9SJ2FbUEzEqcPVxVcf6qzWV8k7eA22TOt2FXFgeXF4xP5gMzfGVkTGVC4b77oSEDsPfapWqRw-QWosFfTCwNUzunzdk-pAhjo5ETaRbqCFejO8w1lLIwin16H_1R8SAR2pLuJTOPe0GTxGtigPDL_dQ3e4klSruBu7yMXlEoi-XN77kfuqln-naAg7ggN3dcsh0vvg5ClXGyjFWjtbCMbRCaQM0EJPSDx_ShbiotRoVnW4TdsdOIHpyvbu1Y_jCaW1BdjyehudvoTkMRdd0kqeleONBecO6F3kucWvgguLrspw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=niLvYJBqyrmuoith8QaK1MaJFxFQmzdq1SJJcTZHb71tNVznL0-RadOnHo4gUvjBFL2gG_xXx4USccmR13oCliMpkVQ2iFZFQFfWyNqvAwxzldPrqCZS4HpaQz4L-2EP3fhg5OmB5IuMY9BeCZlfBAnTJDY--si05S8f_vJM36aD0KhUZRiuhgbiiNmMxwycsDZbGBjbp5FrpyC9YjC-BF9TEdj0N1Zxd2ZjTY03UJ2_1AX_0Dh8jz3bQshhMNuhFKn3H0V1qgaSTxu6DX_WlWSC6Toqj9UeRlzx8ZUXl9KU81ibcB3gtSsW5Q8sQCef2jq2z6kSPILfLeyEkTJ53W2NethGbrfnUSgrX_A8ZXXVD2CjB9CWsORz07vzD9SJ2FbUEzEqcPVxVcf6qzWV8k7eA22TOt2FXFgeXF4xP5gMzfGVkTGVC4b77oSEDsPfapWqRw-QWosFfTCwNUzunzdk-pAhjo5ETaRbqCFejO8w1lLIwin16H_1R8SAR2pLuJTOPe0GTxGtigPDL_dQ3e4klSruBu7yMXlEoi-XN77kfuqln-naAg7ggN3dcsh0vvg5ClXGyjFWjtbCMbRCaQM0EJPSDx_ShbiotRoVnW4TdsdOIHpyvbu1Y_jCaW1BdjyehudvoTkMRdd0kqeleONBecO6F3kucWvgguLrspw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZuIV-jtP4au6qRvSEV9LfJoMQtAQQ3LrTcGKTzBmN_jVKWPI-9IL2DsSUjLnbP5r9kG7F6Eo2n3eUbd5B1xmkV7dE6A6KqKtvLoQSaZ920gVhNyoYNGNRyzNtlNJ8I__NUJeO7EIjWslhhm4Wf62WMY8Fv6b9ZM7irFGnpof6k5OODPoVLDNg3HJS2GG_FyGJjb2F3wPg9n3AqPj1bdfuY8scBXy91UjMZ9opey3c6C5qFvx2Vecc1VHr7B4lswX_bheHxd2MICPLcr4chtJwM7e8M_kLrJX53Ej8bpH9zWVwtrSc2MDVSircEO7umzc_OGhJXtZw0_nkCpnEzdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfuDdEQu4oQrnHnVGnkcQ5gUrVgxJfR4kbuzQU7tMqDui_jIjnkHdtwUnK6LkWP8f_RO9JoltbzCDoJBADdnuHMb214UNElnv7u6o5vvtV6gPDAEAea3MpPfmF96YP4sRoSAg4OOzR7nKAiPYc7pZHepyELyCuBsdofoQlkDGQTXHn0K_GeVmVC5lwWbSTqT_q_cWU5lQZDz3gC6FUwwqhian3ek7aFLxAELzMJ-JCIDUmSFmmbpzUacypNFxpwAKq4Hsv2IgAy7QWUhPGvAUM_61OEvLUMtxj79BWalghxm3IC0l9lBUc8TaJt6UeuWoKG6ayDIrLr9UfE7TZ2-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3uPfyPsyJRQdVAL12XMH6Cs0w4LJqHl7nVuBkv285YqhOPkcNRVyjPUO_TAMFb6Be3QVqP6WkqZbDANfFZEIlLnXjZdLUNjTlvRBg7CFGtwzREczQCVx5YRlLOK5uDwwaZyOKaxraaV9O4b75cxP9WMVNghAsDzhvM7Bqhjl3vWA6a0hd5mhedgcyZQXslkElCy_thoEsdin__Y1zcWak-Cg8M2SAIsGGvyJ_pvNzbuSjC444JX_cy776nIsnWafbPGlbcCPdxEgRubpSLezz0Ky_bDDVbRsVi7PdH-n8_ab1Qlsr4b2nl_g2DCNROOGDye_wbP7J-uZkQF6Vy3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=tLdTjwt2X7BB1G1Im5sogrQp-gB803F4iyJTkV4S7iLsRElnA1oCRK0ByHlv-U8PuwVd1pS6I2cI0_kD527neZMNZfetgh0FNiLwTuFDIgOrRLPbwl7wIdFbb9Z-hr0h6ZiHrpObPUpx3M4ltwbWEf7Np0VKXTtPmRV0KQuC8QtL6NsHEgybQurBeXm3yMwM_ys08hQEflxR6QAxiJU2-bGKP3N0h8IWI1ajGNnD7k_qy3BMEjTt1ayljRPNM0W6Gl_pvnI39GF0sLl_SccTPFUQEFitLWzyA6xV3nK5ouqHJEp9Om4zGBQhPu18PeVzjmG8teOXYnGC9qD9cNAeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=tLdTjwt2X7BB1G1Im5sogrQp-gB803F4iyJTkV4S7iLsRElnA1oCRK0ByHlv-U8PuwVd1pS6I2cI0_kD527neZMNZfetgh0FNiLwTuFDIgOrRLPbwl7wIdFbb9Z-hr0h6ZiHrpObPUpx3M4ltwbWEf7Np0VKXTtPmRV0KQuC8QtL6NsHEgybQurBeXm3yMwM_ys08hQEflxR6QAxiJU2-bGKP3N0h8IWI1ajGNnD7k_qy3BMEjTt1ayljRPNM0W6Gl_pvnI39GF0sLl_SccTPFUQEFitLWzyA6xV3nK5ouqHJEp9Om4zGBQhPu18PeVzjmG8teOXYnGC9qD9cNAeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXQxymKAcCfuYyb58eoWkDSr4yEbS8ZzKprJSxiAjwtOyJMxZgJCMP2PMI6TxNfKBRNoXx15pDhgFY89dzNkDr1pXUsN3ZxUAXDSxwRPf3dH7_RgSHlSr5THWKqbQN8FD4VNCftbgcqXdORRYiT0MeBTwPjPRgqY7IE6eAeD44us7DIwzJ4J6pSCQiC_yZeJ19QI3v251vqUw6urfzeb25DXbywRl69RpXBLVQHBjsp8CzN_VJzwDjAq000aaIPqw1xGs6htlhIta8bJSOl8i3D0e2_3Wvg5iqQcxiV4LOmFFQZ2Nue0Z32ppCNrPph9PL0x7SPp7DBp7GRAyHkLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjXzWkCa5-C5jttWKkYUTf5cMbeuY0SCpzd8tqlzoiCAxiT6aH31gMpmZln4CWWNQrZkI47ro5IxOgIKtONcw9woBCxviiZh0NSLrCnEhNCD-mYD9FHRCKsCb7DJbDC15hzoufStXsr4nH8t6AQ2inScIpWKBsXpn8cZDmiRjamKb8eeumQ2Pkl1-hVAcGbxAwmCVqr2DI8_Pt055P3xTCzl7h4yC6GRAC3npZjW4QcOybEmces2_-5pWIRlwzY2M3A6eEP8x1ukFBb7EfZggQaHYxs6L-xh2rfgRRdv-SN4mne_zHB88MffcTtc6YCXrD7HrfpET9XK_60M5DZHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn55Qvw55vtvIrOZAYQmX1ku-0TbqAO7OB925ux2ng6Q2ZJZu0Y5j0v_bdV5BbSdUXxx6aVGjte1pE-kE8IJj2gsd-NJa0JtWVll_LP8QMalFl-G8R3X1QJEp32kV3B9MsnJIVmpm2nr8uT31i6trPwfnHyajlSjVpAXyG3toEfNo3rTejGp3EdDDafIqX74wrOZrZtYXQ4Bm2Ntld54lRCv409RZY2woBEzhSwKcmy1fadU7y4BzXWhBdkKe_UDZR_PxMJ_jtOate9FXFmAqKbOLvnEUghLLSGGA5UgAAyuCAwWKAdWW7xKHWxpe-DSWdnHwFiJaQWcGRI_FFkdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=JanLVxxdgu5nx5pVX99YTwOGoVNjbEDzgX8jKJTfXR2WDBxdBQh03Wg3NvNDvV_m_4cmv8wo_ydDaX8NQpE2lhvD9QCwj96d6KR6QD_coC_Yw_E4ZpepyydQBLzQYHLQH3i6ATY8VbVN5hY0wAlCa44YB5GtWM6Aen9aM5vuy06KfEE0HNG8z7KwbHDlZFWy8UlRB_FiMIWQTOncHuvPGZeSaqu2nCAkxK-Q0CtoXbEbd2VNdJ6GOtIaUj_F4JZjDA47Ede-MS15CgcIx5m6DZAWDcxTu7Q66pC9WH4x7B-jvdpTk_ap02Py7phXDl8mijvpFhMq4I2rYHeJROAD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=JanLVxxdgu5nx5pVX99YTwOGoVNjbEDzgX8jKJTfXR2WDBxdBQh03Wg3NvNDvV_m_4cmv8wo_ydDaX8NQpE2lhvD9QCwj96d6KR6QD_coC_Yw_E4ZpepyydQBLzQYHLQH3i6ATY8VbVN5hY0wAlCa44YB5GtWM6Aen9aM5vuy06KfEE0HNG8z7KwbHDlZFWy8UlRB_FiMIWQTOncHuvPGZeSaqu2nCAkxK-Q0CtoXbEbd2VNdJ6GOtIaUj_F4JZjDA47Ede-MS15CgcIx5m6DZAWDcxTu7Q66pC9WH4x7B-jvdpTk_ap02Py7phXDl8mijvpFhMq4I2rYHeJROAD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfk0Q4EJOgWOfFxvAaAEXw8nbQXh5MLM8e1z1AJLlzRcGR3_4x0bkTf0IvnC18ncbmy3LRixjjFJgJgFvUkDJzfTwK1eLkbR5XklvbrDJiprvkID12GAHwZA_fGDZ0575a6MiEtiujiaFUqxHvZNuogYCF3xw8kNAzWb69LUgIs_rTEfHvQRIbC8yvD7DeDyv9Q792_wc4yUTF0nJXCybHTA8kQJGUJq0YL1FIbvvzhvPzuCYC7UtM6sLi-g5ibhsSFnvjZgOgln7zhBsG_EGf4Dsx8Re1lfu3NsmuG2daaak5ez49YhZIb1ZEnwbBB1MGbDRHJRuWLO_1sl5GQXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaRLLsDMwaI3GTYQz9206sSAPWALq9xtmCV8pm7i-xtJ0MuJcn6hvyFR5tS5zzW1Il_4fjz8tO-x8Rx7NtqIdLG6sOI8hvSefMM93Ck1VJnWSNFW_LPBy_nGTTk10LuLI6Jx9OoO4YIfQzSmIQxUQPbIua4Yd3TJDMRjJMBkWhYBgzpFvG0GBVh3s2w6UyIuCfuf2rdfCumKLWLbsZVyTJtwPjh57Q_G_SCHgDdoMjE0x_JBAVkmOxxAfRJq2Cb67lz6KOzJ8UPhJL2DoyJA-2eXvcOSX3vHrLsk_qSsb9uNE_L601NboSH0E0kGuYwh1kOHtas09K6-bXji__gEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0JHI_1XpMBexyJ5TqUbAdKPeWw0esP9L1fcUkD_WpzRPirGtpkhs8KPphlPClxo723rJUUQlOcwgm6K2GlxGLORdjbawDW6V5um0tlcasrRCVMX1J7jVi2a7TevR9vggENUmFW10-yaiWrOuInfVaq9eofWfFguerN933oVjW1o3iHZ35zafggsURnBJbNlF1I4mKoIpv42kFM9GButHcT2qYx6OSL_vpSWbbPvOlmMvxWb3Tb90qjI8_DwPwGbTbRdwBPmjjTIRyQgFdS9hEO3mdIPISB2D-a4dI1Oao8MieflMalLZRkBjB1XsvbHXqpVS4v7Kt3ew_u8RwMLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHQ2l82y7mVP-Buwp4csrqLiug2zjjlSIBiuEIBVIyG0hT8Pu-VFTVm83PtaH8THHIkSrd-9quXUVUhvtTrbnm0VorC3wg2RST7NAus4C_UC1BQaU-UuKu5UdVc50-yLEog8S4rS-HeKgnZsCM-ers6Avz_Z3VWIUSpyb8lXopL7g-uCmUtidlNwwvlhINK0wT9_D6qOrr-YN5Inp2iqy3FvhnKP581rhuxrZJOb4cQ_bahcnUfjXscMurGEIOUJ2sZcd3Bii39yJ_7ceyxzCJsjEZ1-l7FOd6z89uura-KMf6w9SNunxJ385wIOCyPNVmB46OIOCEgypOpA3Et6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucwSI8URADOKKt1UbaAk20V-Rg6mmb4edgn9Kvc2a2YZyqxlbK1KySTrrq8zD7HcNB0CvV_PA2eo5_rbR4AaNhnPYyfFTzDYuKTQRkbEb7-ou-lMzT_Y7U3fz0XXDzDBNxq2-eChzfPPEEGhg347FCCRvtfYJvygW1G5Sq22c9JI0pFtpAgXfIQYptQxcu4WokiEo50lYZPDzDnS5FlFDwkBVUUcH-O8FzWBadbG0Kw08lMqiFRGCBcAXqnZ1hSk4B6xNQ2btlGsyThKyrq5lA5HAhDOLRC2OPTqy3NIUOnjkCQ1I7PWZk8hFDOhWnP42W505ruCWVYPWFxVGElnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRBxN8-WNhUJ8WkM5NfKcuoVlJ4TBPCgG5I8A2dT0kBrizcPg-Baa3nabqGX-4k9aXEm6omxJGPVCtLnw0kGHre3F0X0ltnyHO6On8V2VyGXihyE15s0c99ibNx5u-E9h0YZldtjc2DBP6VCZ84IUOeilb4G7imdHEggKPkJ-Cw_m28wp29tFA28_mXcFndZDsGEYvw8kD3SEAqFk6h752lE0X7kcarBKlq167FXubjXjgPbaJ4tIm1UEnFleIlyTMUJvg6Z4hhGKxcxsVdHZmErPvwBVqwUjM9lWNXKPSkIFzg3M6aH-LOm6LwnPuzMwRnjlQ9W76Xya6FGzyggiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNsGi8YGhFhxJmkLIS8jdkWs5jCxqGRzB9Tn47p33IPxKvStNX2ILELURcd8bz1h4so16dMMj7stcW7NLZX01fTV5_zJzKPPH348qwSu3je-kroJxEyJdxj2nGvJX46RRTZ1n9sr8mMgPS5_NY1HC_b4tWk6D3lZPV4_d1MgjcavrljuLa-pqVMw-g6-DPujZJJ8ePtk5-iF3nzaqPyAk4UcM-tWow1AMRPJsWKtheAe-tEUJW4aIV8GYG01wxPcFXvQERHBd5fE4XEWsuWmo9bUMpowZlB43Fh1moIdV-IIrEb8y09E7KCxiUOWHhz-VBGJc9oUWiGTVkrhucjEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJJQhftkLELkqfXI-JkFzJhp_vOEiytvVoQUEgbBnML59TJkTBOqfqdQ-L_T-baI7jRyC9ygjOk1YLyzUPK9L8YYF5GH5EAFD9OI7R85D4gNsMPqk0_EkqNPxMG5mqZUZB3EbLQoJERNvZOl4E7E197AdZnma8BQdmjJg7e_mENE_pLlitkEZljUf6eLPNIihUDKYRObfNqDe7fhqmnWBVCRlJwysXBuRkKO845C0bPyN-NyNLglSwfZq57Kr-yEd_L9toaevNXwhXb9LRHM5THizTG4q5Rw5WNI2HIesEinw5UscZd2jihs3z4nNEkENphrrx3jHNSRnfVkgTHHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ynw45RVR3c8bjA1pq79ZaN7hvnUKxCiy7AcjX8WzjxATBmvG8_-Csoy-Od8aXGsVsACRmTkPGI2ZXaY3DFLFNQDiRiHC3mIUWPWSLUpkpBuIdpYF-o9pLtVguVQOLRCbXfb7CIAQ97B6jydWtB9Ce7taQqy401vqK7FgFjvnq8nJkqj7BCZCCK1T5mvshYFOtmYv68OdvEfwogJuVVrRHDwsjnB23C5K59vVyvjBFUGAqCYrlJ__9EYMRgfdfSg3Ycb4HHCSITFSIqUWVcJda8f2bVIpaTG3StNE5Pt2lcmn3kDIfRW09lAzRiw4jJDKHv-QT_I_b6ZpIenAhdNoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFK1ZhH4tVpBsJlp3OaHoZnSJwswVwBo8yMO_QtjA26sC9ASWn54Rk_ZkCSLl2-mxZ6dHCOe_QnApPKO-zEX8FxXt_y3_KJdP6QRknWkYA9lRu0Z9cWm78yboPy63vHluUMEjFRjSxY3RSazcCf6k-0iT_YrMcLGG47PPLNe2sDdXUqMErk-bDRI01AlJNeQ_-IfaBJsk6F-2ikiPe2UBNpar4FPgXvuqoOQcS6yqF1OoApZ6T1A7LWM7t8XKgaXx2_Fp8cmKgr6QGEl-Tmq4VguCnD3iDCmjIhN3V_he77k_QCamlsmjrKy24C5jHL-vr6Vl--IISFgKc6SRfEhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpsmFlsT1Vh07W0qnIHqnvjeEkfMcHByLBjshPTYxXmi5g3mVkSECtVqh5Khyle7CWb0ITgDGlu9kGTGIiSHSjBAzgZeWNT3PdRkao2a535_7-CqLrQWItFs7MzUaOW7XUaV_jOAGmgoA16de9wflPbc6HknOus7ukUzlQ-KLokZZaL74CojLZ0PHYXdPBODKdQlzMkANS1mRCIGJNLtdI7b_BYmXq77-5-iuossH2fDoXNlMjPBAYVwkRKCEysTPwpHtKPHIgER5vDdqL7zxLxIdQ9V7yMic-Q_yk63vDIPm-d-g5K2llEkmragMRVM7ReLIyyItahU89Fx9wQneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEKFrIymwbcVLoChmaOMb91CMdshXOWaZvMR6pgvpgV-QvMMrkd6aovTXHrXNTcSrIjQQmNBF10kdhszNOtaso_e-oSjXziZ6WeEMlSlWd5ggdwAyUK--spH1zTZZ9W9eAwC2FBUWVjugUx1WEvwKHH6CSVxLMSWxTurAitiP5P5drdF7GD3EEPvFlYBWGtFlny6i287Fr2sPMQDhV-segEFAgQ9PiO3a7L9vfibcUKiK-RmjedoizZgFzOs0GMe4LU5Y5uM8WYFmHDO6fUtO1rrta8DjGDpjcCz-eridZ5rHKDlVBREDJ4hm_iO0RFlIOukCUVwhYhsXvJwAovF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAoVwNEPkZXoj7ejKFZSIiqmPYDUFnu3ZjkFhv4y1-_zcjnnAhR0Aywt_5-NMmzvVxRj88jcbg7j6f3KAtoO1si7j3q2vCwMa-RhmNEh5IR4yAaI_4HojxqX7mJfBhez5aJqLS0OoSuepVaFu40iJwVnQNEV0GTWMmzIINJpzuOgSkGCLO5gapMlUHA4Z7H_-7hOm9rltjgoigbiBpuSxoMUagjGPF0kA1Pe37_OsvtG1a5YzAR7_nvl-fXBL0qDhyi9PUOeZ0oiFkfNV2otDoczwkmU0Y8GSCnpr77nPPiBmTgh83uxbKsths3zvoP_mzi0bJYFs4tR44FZgLrDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrEZI505SEs3MgepUTt_8bH-nugDeEZeAt2pYjYiLRVAez6z9jxCJMaHhWBlBuWYs63sZStODvBVfyNd1m2vb5aVuIR6JsG9xaCNIfB9bYV0LIBgWz-aGtBuhSfUTuFDHK4wDVFLWCl0p86YnP5SiEKSsYVcj43PKoWKJNI8ZjX-OoH3zD7uVKOyCIuBMzUHTrutTuWUX4vk4DG2cBp-9F7A-aygYQrU9nozTrBQdH8qcpEOyCiyS4izDf4-R0pwgaPnzYg9No4WcXbQE_KRYv4celT6tA9qEmkednlIw-6gdvbaiwgFDgUaOqFrwGdMn_iD9B5CTWzYaryH6HVJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
