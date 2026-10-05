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
<img src="https://cdn4.telesco.pe/file/UI0X5Yxl5g0V2r4tyAeZv0dMGyOQImQoX8cYT7UR194V0O2ZiUVKg7ixroeFif8M-Fp_01rGSADsqra9IP2Tnt9B06hnozvhDvSxWJx43dUbOp2ZEjbaJ-NQNbpIEVxv_FKGvHJcOWP01P5SPRSLfhiil8BxnadcGruic_JI-gnPXu9XaGG5jhfBLnO8PSc0Zw4A1_LqrHXemIV7AthWqDZn13XWn83yMLW0eoUhRoqrsVU1E0rrL9MYu5HRK4ZIY6ITb9QwekOyi5AVQNkyXdheehflvXBhWn6y0F4B4sCDGV7HjpgKMnGACP2f20FQzZVaD-j-5EIqZe2E5SIm1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 455K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFTceET7WxaSc9k4Uufspte33bYmla3ZupzJClrtYjT0NSOQBkJbEYUGlybqNG0KPs19ggnMMYXspszux_mJZNUS5axJTG4UhoYeSf3-_NaExFK8dR1lfsJ_65_K2h3ngtpPWicMvidU6Tg_xuGjmlP4jlR82IXtHXXvmifjlnEaT0BUCJnFx41wmQfaI-lZQSKbqYFdExgBRpAIzPYOE-hqiW6Fztv8Gmq-w8mY83rQ3coJ1ZPnMMKCF66gPsN80rqklZJbk-SrwTru4b9zf3G2FM7OMWcZsoiwYcU1EDhUVT7q8GxfzyBdUqKEbNCg3ogmpqa3df4lGNRnI881Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2OuS4j9ED8x63KHpfX0NU86oAVkR0R8t776ZAtTgoHPIs2qksNmnyWH8KXWbl_wPh0T3Ggat4BQEZA7hB_p-id7twaRsRcHLTygnsAK-fEqjpFLKG_T3hp4TIAk57aML2ZDhO2gvyQ989nn6Mp1fR2nCha7yl2tW01C_JDZSstZuZDixX5VvYXQAe5ljIPzMSBFQ1KQdbGMAL5lLm8o5bGXM-s8b0yrQLZke68WnTUpxLNjbPLTVq9nk0wlWYGuX0nlUBb1ST0cwcb5tNG0kyxUpvuynvj_KpEbgv9tCrRYMn6oTaXBqqS95kvIrgUocJmFHbbgB1A_F_6nTzVxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=aXyuZezMsFJx4n1-z2xJDfOxoyXfKtCcip8LKbxjzuTFW0wX7r8B2PeC5FKTQVO51PsHt67AKwyxLtiFPkDQKtlyM82SS2XUL-aTi2HZY-DxS8Vjo0XQmepkfb0dFCj0Liv749qk8HSMFykunM_XBMLCbpD5NQ-27jqEzNJXePG5DVNaCFaQFTIfz9g8iHYNH4GP0z237Zsq_jBY_QZqxyOfVsSOtFHnqoQ8B7W6D5jYoMWGdYZiiNnyKqJVHn9Uy_UONLmL-SMsWyVxWPuToOJ-4rB60n4i4z4ic3FV64g2pF251zcr-XEXRSMxL1XU9gKQgnB2Th8XGVbHtnGASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=aXyuZezMsFJx4n1-z2xJDfOxoyXfKtCcip8LKbxjzuTFW0wX7r8B2PeC5FKTQVO51PsHt67AKwyxLtiFPkDQKtlyM82SS2XUL-aTi2HZY-DxS8Vjo0XQmepkfb0dFCj0Liv749qk8HSMFykunM_XBMLCbpD5NQ-27jqEzNJXePG5DVNaCFaQFTIfz9g8iHYNH4GP0z237Zsq_jBY_QZqxyOfVsSOtFHnqoQ8B7W6D5jYoMWGdYZiiNnyKqJVHn9Uy_UONLmL-SMsWyVxWPuToOJ-4rB60n4i4z4ic3FV64g2pF251zcr-XEXRSMxL1XU9gKQgnB2Th8XGVbHtnGASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چرا باید عضو ما بشی؟
🔹
ارائه فرم‌های دقیق (BTTS، Over/Under، هندیکپ) با تحلیل فنی.
🔹
رعایت اصول مدیریت سرمایه برای جلوگیری از ریسک‌های بی‌مورد.
🔹
گزارش شفاف نتایج (برد و باخت).
🤝
نقطه قوت ما: گروه همفکری اختصاصی
علاوه بر کانال اصلی، به
گروه همفکری ما
دسترسی پیدا می‌کنی! جایی که حرفه‌ای‌ها کنار هم جمع شدن تا قبل از شروع بازی‌ها، روند مسابقه رو آنالیز کنن و بهترین‌خروجی رو استخراج کنن. اینجا هیچکس تنها شرط نمی‌بنده!
💎
همین الان به جمع حرفه‌ای‌ها ملحق شو و استراتژیِ برنده خودت رو بساز:
👇
لینک ورود به کانال و گروه همفکری:
[لینک کانال]
https://t.me/+-M99R2qSbdVhOGI0
[لینک گروه]
https://t.me/+M_YAiGu22l05YzM0
⚠️
هشدار:
شرط‌بندی ریسک است؛ ما اینجا یادت میدیم چطور هوشمندانه و با کمترین ریسک، بیشترین سود رو بگیری.p12</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/31002" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgTPjdDTMamUj-DHvrNqsp-B2FMGSGwS-YhsAW72Oexap2MowONfs9DAD8ELJUZ1FpRkcDuszSwEQthOw5L60_8aRqjBMj6_G6Msh-KyvTE8hkrLm9U3KTE68-SQd2oj0Jlw7muccejjp_wFsufZ0AVbIdYMh0Va37TasZkTfTUI3QXEZfDPI1xxyrUZcwaIe8QCdYej1EN_yHIQsN5KoEaIDJj2T0W2Cr9x2hCKyhAbUetRUVLKV6lZ6dLipWV9vCJS4QenDGDSU4o1Vb03cp9Iz6BFknUvzzoXQD0xBBM6ddNLlnZGEJOKHF_sZh8lnWJHmu7SZFk3ZwGV1uWYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAdv78xDcGqEfUlKLRq1E-WNEFgIP-DtG67jzxdKTRUczQL9BtVp5MpG3jF7UNJ8Q0ZesFYUMk8O4dCYfl6_x7X89FMCFvT6JcuDb24AnrkDmCtR7f6FjAks6U6Lpx_QSuGBFaeeqXFg9AMi1l6H8sQIM5JSiREEjPEfF9Q3VYk2ehhDxBE2QpU84qfSp4Ty-Iv8nT8SVi3GSRuiZYoHQChlhW37o5ByNSZ_3DLRKDfC2YYv2P3ljijXlAL8KKypD76uyDniiXcBO1A_243HFtXHUMstcISYimiJjql6UuMmqQdOp0GAMYqxoUYou7U8vQcZyzz6xuZE5qVQzJxhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afh0l_4gk47WaxHhc3mA_VFyLZ33QWpSrVDGbs9M-lGVdAeklCRKoRBQwTuIUphUdZ4B5hxnz_G3dfzrcMalduf5lstJUQSC21sE-foO_2LN_4ZmTtMs-ZFsrq2ofLNpmN9InTHhTX8FP0waUM9FE3j88Xukc7dY4VGbFp3SxGscXxgHoA0iTskzxxAWHmhjnAOV-75JbblwX2PDh-zsLqC4njK1eRnzvQkPl-jfU3yv4iytdGex2F2fPu0Z0eGDXngR9OWpLDxOlhKAi7jlLFOatvuoz7-l2qjOfr13GdIf-3QuNedpdqlzXTI2Rgp4mKsWPLGaOFgLNhmaksSfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8HpjfgG5QbPAxrWOSU0QGn8CO4wnOPluZ-CL3WOeHYt74SMntqFX2aGITIxMvWCrr7GcTNaVfJuJveavnM8NJmuxJEJBT4U-0dQM6CbFgHLfFmPF6CHkGP4I4XPXNDIAI14gitfWBgXRRhvPZbcHiZACGUPkPUM2yxuP2U0yTzubnNp9Vqqw8s0PQpagaDAFxU5su838_tyPvE4QDIgXHRnWRUrGDkQKuOPuhwcRT8eiiYNoZGZcmq4gPkySBrB5B427-i1Sn-jmXMPeSbgBebd89hRvywi1WpOM4gD9RHuLWKfzmY9MbwJBDoJ18Bfcos3l0uwZjQV2hjPzjGI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8Ficu-SbVIo0BdDL81yAm0gxd0BI6lq0dhl7QkM9TUv-bgPBOXIvo7e7MHEu2ORnmlIgfRiLHikfhk1Ja-MqeTL6Oi7s8eHL2kzsDEaXPGCESVE-Lpph89N8-rbYp7jg9nVBcnHXdYsr6f-iUmKhqrd7xE9ZQUd707E6Boc7X4wZYW3tlNWnO_7FeAXmg0jIYqhJgfOGIn4wHyDKQSVxY48LHb2x64Ho9hx2F9_GmVddQCUIVJvw1H80R6Kao77d76nexSsDtEJpr8pyljZgWwnyeXwb4J2qSbvvQCmqRJri6QDfjfiHUnVR1Xwz2ZAEkxWATCFGYpWwrcqy6q5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=KKT3520e7KEpcY7a4q61ykPlYlcSbQLsnDh0rs4AgMHojJMq7kWpiF-ZZm-d6Yl85O2T4TgXqK_7mQUANQuDJ6XJSckSOqscWUN8uziRRROgrImS6oR-pYb1kD6XNq-fvl_B_47V7X4KrYnBcP4Jql5xbPuvVqJbbM2KRA23o5I-RmACxb-PxiDCZb8y6UIw1d5-iRc1skHdrn5qi4djiswX8URQNsvPNpKlgrQhjpIPiIYA93gGTOcTuvf8xSuNb60WC7_myHmo0rcWQcTib17kyp2wgdPePuwRHngEap1b8uxWDrknJb0byfQ3Tn-Sm2CmhESR_ZWgoYTjRujpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCyumyKyKJulzB-nNs3NUxU4fXr0zzF21h7SuD35ryaqUiU6-YP7DOcy7oBFO5Jbhld-zSbwE55I1wxZTm4vHe0b4Pdk1uwqmDkdxohZ2w5nfg5ppsN41g3OXiD4a3Kp_GavMNiETttRtJFWypWiEH-SvehgtTmrGxOU-EUl0yESmRhoBWrU3WePLgOnFbakiYep0k3f36wJR5zrg1J6PXHswzFcQL3ycCurIlUP8nLsEYvHtrgQWG6kcnb8sCQhfYFg7HRwEvLdzpUb6NGsGbNHqlb9foCfX70b1uQVgEyvLlQkXeM-HUfqWV7onjwNXIgcjbsteROiKe22cAtHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=RG1FxbTcMTEBKrF1QpFu7hzOHyw8UaXwssK0mh-htyJOiw1_8JL1ZCpK8XU1Bln7AkmqbzvylDWdPcPBZyqAI41aXkg9_cwU5koQV3qE-gKxC3QYFg8YijXfNZETFjO3lIMkq8WZPdh9Nu4D-IVjAdmRVonzY8y3reaQ9YvfUmyGFtdozRmC3n4luG09pJD1FUvsjSnJDj4By_nSbWGkmyJSgKWYlaaDikaLOBV7t5Zhbqb_lb9P-lV8emIbI_IlLAoLd7A_606u2NtiVcq2PemMPeilW0p64Q-lvVzQD8So1HgtbnNAYxgsLedRBgy5sk4wv7oPjIdMovsoJkklKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3CrZrngqj1tywV4Y0D52IOCK5pTlhYEBVYqY6uUC32Bga_e22QPf0m1qbwypuz_3sQaHCU6UyxMGTRfHPyzvC2ws8qf4EeqR4hT-jbZuKeh5Z0g5xU3ddBjW4wUMi_FI7A9fuFItn1XZWRyoRS004ix5AoeyA8TduOR3vy5LGRyNUvn-6ocF_3PAHUWhRt6AKGdGh0oldL6QNWPernU1uj0vGn_6WePYFGelgZ4MqBPZ_uQk59hTpQ3FoVO4cJhZ2hS_-CR9nRDjJw3nO_a7VExWWXTtBUMLlZmMKzkHKOlg_Yl4f1_kN450dihfkH_Cz2G-q-OyStNjh7vHdEVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iypxhvB64SQB9oqGwDS20zs7lpHQgIDnYH8Gpe-WB9E93Iip4CQNHVVjT0TDcgkBmIvYqNmFr_C2N7IkASSncAKnTH_6I2sU79N6Jo4JHMAvDsMN1x4E1WghtfGKcjS2cYrI_pB7QlyeOhVIQdsRKucZGI350SxSGuHn3VwVq7rImxFLd7GhLw4PtlCLYLcl5XUdnTDOCq6zTuCM3TyT6Nsnh_OAhd6RvzMSvv3huBMdv4qhisIagw5TzRA3-t3qyZFNNhLgnGrHw7bESP0KrF9oYJuU_iLyC_ladzRGbBRhgCzToFwW1Ptf-qv2fpLqb5UqZK5fevmYN-Nd-c5bjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOHcdqUQgFXziCvTp9LPvIMMjPSezF5gD9k_n0ATg1-xFQ0TksnJyiyEqrwlS22w_FYCSldWLsrGmYQ2FXc2007xrULUAksQxdyfQLl9KQQSDNQdMdKUj1qF_UqyS2QX3QAb1o0DCcfOu12zBuJjUC70CApoUWIHxvGEVGAa_BW1Ce7YxlcIZ5Y5kW_ZkM61VA6b_QF2wk7AM8hjJ2Avx9kyjG8F-28PrE6kPmkJnCcsWzpx_uYt0Rz1EFbi9SWBYm4nJB83htRXXOzT3SOOD76QnM5fDoAW5JBiniWNbPxQzXO89S2Hh4MD2Mr1qC48EmePUU34uBc4t3J-GSSrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEIUAa9oMrYbVcqYiLQJnpJGptjweCb8lBZZvkcwauwGyZJ3s4QUXAgHGgiYC8vJFfl9POBrCWS7dlBjaTPLiswPCx8LmqbgNWaFDNrJP7Od_msNyDa94IQbcCCrQ8-my81zQNxUZYZPCp91Nh6_vVS30HzKIjx8gn3VJsCu4ckXf8ecB7KUu8QPhY0zR4HrGXiMlNdYg8sWb8TSxepbQ52eKazDfpizO5xBkrN-olIc16mbO64qe5893qvcDG6z8XAxvKjE9sYWbY2JlVVNt8tlpLoVVPWZiFwRKx52tm_02dilPd0alggEXlZxmSJDyx35wmP_ahu3Y0vgcYe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=s_s3d6X5kMTcW0Ji2hDYvcavtkn6pzXZr91y5uT5ZY3_LfyuvvEAfTrJjs_f03mcpqkpolDXTCNTWmo354P4GWM0uPtX198RpARL96K_AXEQqDMs0qYU1ZjoExKSOjGTJBMjL395yed0rZp5ysoEOeRQSiNZubb1jB18bJqIyXBZs_AbITvpjHrXUKQB9WItl9JbQeju30MHF4_BRN1om22dHiFq2Et-IklYnjSeJQMRa0SUnD7FRj2QCPjJ--tqTJJlJAJh9yoT7SYaTrEn_hMtq3dMp-uY8TXuK16p7hUrntAZBg_YfBQddG0xPC5kVZ5_EH7B0xmCcaY8MBFqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA-qOt-vfzmVhU3WfFM10r6oOD6pnOdbaRI9DUl9iUma3S131-oCJn2-3QXJMthC8PxnZVr_v7BAD-F_moyDB-d8my0VV6UZqL8VRx5fhs8BaWflUllGInhxX2V0mnQLMDgvSYxb6skBkEKrvdyAmrFH5qKYb4QAUR0hmm5lX0QKE8jdfrROAdCrlTvGAsb__wQB_SP4JPFniEuP9palzsBx_PqeuxZ5CipFMdSzSaqGz5bG3U9QO9KpCoFzY2h6eD1XoFMm00U1zHVQweIfvIFJ_rbVBXKsnGjoy1IZv2cgEqpdBpRxV6n8N3PwUbgVzEk6nU5KufvXsU68ejsDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=dj64RcMV3p5mxzCDDaMHQmbQRfdA-KSOjab-kwlESwQB0Do62hPw_8oQOTXurLHlniWEt3tcRuF6-HpmWjSMqwAzPjeXPS8SlUFIQq3NnugTxp6eZaDftMQtlidkXCUf4mi4nbWf0fe4jnhQQku7TrppO_mzggSvSoafL-yI7txoqTcVhhxLmSgriDLAjp4zLlQF6NmWTNkqA8_SSxmYr9uR_CVCmXBZitudV8gP10-LrMsujGDnvigIWjNSG9zwPl4lrXMCsagbOCaBrTXobTTfh9tRfAgLgBmCdTBjGOyc7QaCDt5Wd3a2ItpDs5y-Y7NDnGFF20tGt09jB0yIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JXWBkCxmPAGCY8YVAuznJQPVcuNL6CT2UUA_7JKlvVBZeOiL5AYSaERxU5bhXbyw08EXpIR8AQOJf7q_nIY6ibyCUfHpJ3nLCyKFXWHj_y3t9iO2JuhK_yhWOSObdJrBpQYkGDCocQzo-cI2_EgWGnSKDKtw-DHVn4GqXlmbCQIR0MhDWilOEp3ICG7wTGPvvLYdEQmiT7XaYlvxE6k_XDQ1bSEGrQMP8R-UFD1d0VRefUirQJxJLj1HdVOMy9TlHvvJLN17fr0dMW0GILHQjujwjnUJps8ouXNeNSEPZFTQRqWRmuw-yySHvPeQ9wgoyaa_2GcfXv8yQdp-esrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdncHOBWIBghy2f8AyUNAasSdkGaGjQCuP-_XY1ENIhvtS2ElDSiVpvSQjBTL3v4S8ovgcaqqyp_ymnb7b4gHMh3S6puRbbDNeRDq4Hfxu93htrzss8qOSD7fraO-iEKZz3wKoyjr-nAbPcGgaPM-jdRJfjUW0t0_DfVLlTmMsQtFYarnYpvOt83TAs3yep-iE729GNs_ZomsV24b9CGDyMDCNMyqNkxSGng2WfdWoAy3OfjLQnGx3gfqj0-o7S9qfzCMTXnlrmAE3W-7C1B2u_cRYDR-zI0Z79d_TtzM_rbIJlgCnBoQlOD3mi5zrsPF51RRk9qENrkjhIPXwbbSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=sgjkRF_9yP8Hg3tb8n5GR0UtTRjn5wcg5avNXv9tC2qIH21Khykd7jsKURJrWvLg-YbvYfQXMSYavDDYXuWCwTUJIIrK62PwVzwh3un68PWk5tZV8jEdzX83eoQhn24Ln-2GY4ifHnxOmlLpyl-J2E4pnV9KpSaDLMG3GKq2PJXcGMrGHo5ho2lFnjHYRdnqejw2bQE8vleH6dyfu137L-dSRmrCq3mNhEQu3REdtW_LeZtZP6_m1D65X3L9MKTGiteDUyzWdfEmMI6bOUDGWFbg9g059wKmErggBs59heXvsdjR4NhjX0aajPT198WXcx_XWfec4BbX0t38da45tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUvZjPdou-NHY2M6mERuX7HKctX5PNSPQqCRbRutqTeG8Eaq0q0BtiWFDyJpMce9Oi7GVjCgRGRDoH3ZY5dz6UEzc86qNx4r_o4AXVyv_c2n1KMs3d4B8Olk_u36aahjJe8GOKbcInPoORJE_J8EJiB4VFcLaDTeatkFxgjEAJtuk-8Xn_p67bvCMPSEhBEVmyBj4r_HTClO_8_HWdARhDjnoOP0bjVFDHJIwwq749HwIKAMwkTQK5GA7Q9AHkkKCR7YY0aaRRLTLfuUVs4LWpN1oaAmWP6WANTZ2yxz9upGWhDTHt3TEyXASBTu2xQsVBfVbE7Tf4cVuj3gpVkggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVkXu_MDYaXN850sbnNZCW0ze8tb25A79STEQM8diplbZdKH9zaMACSzWJVWcZ9OqPEvK11b1y2O8pArsKStIsGOvJ-nwxdUaF0kUjZT7O8lBUOapkyvM_Rxf6Oh7_06rzU5vs815YeD2TLaB1vnkgdrVhSCkg5D-xvWTAbO0YivGmJgnHqcQ-zyFNqyxdyRoi9IMD-sGuyI-ZTRjsZ4-vyE2bU1drxfiZ5CEd6WUo-7FXsB3Xgcljwke4BycpjJxG2tVd75K1QNn1MUSx-BiR9MTzaN_HLIwM795Sk6basHEhPhjffPAnAWj7PI-TnKzN4B8z53qEqi4DdI1gxsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCpzNR7cuqJQbFYbp2lknmxlvQvS4oMltjWY96J1541xqqqf4EyqT-Wx0ilpVXePw6zaw3ZmGJgb5a83mg8nAAb0VWve5rY6QjOcGgP05JP1eDv6lzIjvVncI2ZXife8qXcodmwZhztaMWnTxiHpSX0zjouSLBNUIEyeNXSUFymD0g-p3OBjPXBfo1oOU_FuHDPxazA-RFgqKxNVCiyYj9gi9CN1HFK1-qLsDvecYQa5UOL48zcDQu5j8qCgTR14DXviHmeMifpnYWdVVCSl6xCaVTtBmwYCcqN4tjp4CwiMjdnrjoNTcpGj5l6N6gRbxy7-30ORS98LQ_T4THIrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPwdEptZRWa9oGTgr8KyPMIB3xsZzJuGxiCASxfgTXwZ4sL1ITpvupCbtdqWjNuxfcbh3VeOH0kMtuDZN3gQXbs_rhaAZq30iOTW0kCTgR_x5vIR7cbZfokFx19NgHMxGljDQXwo6KSmk1rrbB1RbLKPU4maeUxUly-XmlymfBCD7uv1LZIj1S58Gp69dZ3zvbKkkk9OZpLRugrnH5ijT82IyQhYI1H6q8TPtnglKgWs8mMQDjaAOEduDwQEftWMF5Y4QU0rIKrk76uk2ibdMH3KGyE8Qjqua89BvHqTEUmAornNY-SWRFfvqOvbAlYezr-14Q-KlqX2ue2kylRpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emlbymOifkxGGwZsFkAYHT8v4lOv7uJGL3WN--92jCgovc0in0uURwMeNGLVvhA87ECDx5rVsmuKyzgtFn2APeFIZPUkaLsLeXfE-NvUXy82QeGjOMtpg9aSESzlUVvxvMYL3ANrsPyiDzAywI1W0dn3S5Lh5Sp1gTKe48MZayzTNzW87fDfp5TTHMhh4rIpDYeeJzIr0w4_HcMuuv6zlaj4ISC1K4bT6fUdCaNRcLJIbev7oFuq70TdkzqnrahGgXMQ9kQQX9HPfiMdueaOxhYKehXRkamRUhboOKAtcVbxEbPgpcI1uaVbF7z-x0XsGunVP04AHZTcO9GnNass0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoxELDH_VIk93iVeJ8evw4JRtCVOz-73cvbGDBPGOyp47TZ69G1DKFXoY-odzAdjagx33tXQSNWIoj-ZwfZ2A4DzFHJH3at5s08UQquH4ei2kByI8CjBzuBM0YParo-luHJezgh6r2Ck8Qb2GT1nl1pfNIrVCVwtDxT1wsSvGa5wgTPjLQEPCq5GwHV9mWNw0fFok5Vxq5QW8ZDuLd5zTsltEwalK_3IC1ndgPHJsD1FgDrXfw7tvA3zKCSG0OFH2M1PxGe08P-Q9orMQ7fQP42dwsjHnfXYjnmzJQFSFX5TXyUFm1eWzayD__TymzXv_0HtWQEfbc1kZW0UIlhYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/30974" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbLf_YLL6KOa6vl643QDunlRkmOq8VZ6vFyd-WXxVGCJIPdafNWl1Fzj1afJDYh1zCaLNvESRqzhPWhyaex8ZollA7Z9kJ-hbiQ6VI4WWRp2VgNxruSHTeVBEreGzJ5fxkPSoLHX4owZ7UneffMhKS52lX_y1Q0ubVyCiS5DfhQVgtv3FRG04Jxq23dxeIvCcsPu8ngaFQqCTDKhHJarUywhcGaTN0G2WHTQQ2ubkWxFerlYgyO1tf82ARelBAaOaAte0YJX4ZhIRMqUeRhYyrHQL4uLlU23c1SV-ZYs-DpqNaYCl93umwbc_BtLmPtB_-Ta90LN58O-MTi5xMhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5TZfAfYyPaJoH310A90FsWoSEdAxGXZ9ICuLEY_byDjHZ7fv3DIz3T7h9GD3px4fR_W6Xy4vNfWAXK6-mU4HUcrnquYZMIBPE-1TX9JyRikKAU9LYv9M4BEYBc03xO7C0dwU9lExQqtQecw7hiaZLLMCHc9Vfnd0nvX-JTkZG0anY39rK8kXdhot8_JG1uKNBpCqzwdzMb_ngGi6L7Zb3vhvATNAfvd_vWQpwiecLbqnw9LMjw9scciJBauWQ43xPz8ZOU0irxM2e6WPP5sRGeZxbsCLxDmsLWGcTqx3RNFh6ojNNjPLweCdqHq83bRzAnLsvAkMKmZnOfZC966xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCc8QQRLCrigZSVay1lXY4aCWUTsAIV29ereUaCkzSSQqJyW1_Pyjxdg61YWHd_6nievCUiUnCf81Q-BLknmZwBA5tuuZLypeIcTWKR8mTTdIfoe_fNquUNb3GzVvVssUyyjIeELA_ZGoqo9pgW4CP8HIpBJdB9dY3zP7jAS8o4kclAlug0HkO1uOX5G4ScYtgY07EfFUZdzVHh0gFvp1NBw4wjZjeZFI_DnEAchJth-hgIRg-mikjhDEWndUssnxlnewdl-MemIOfTynII4KGJNx9vPvgY9khMcmyyHElIElGe3yogNIZUHTBbL-MonbdgcVibSLq-weyL-fyHfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPS6S8I3Dsy4n88ywREL8q_KAjZbeUQsRQiQ-P6Cnvh-8c943OkMnBKM9aoJyrhIRom5Ux16oQKwEEcT93B8Y0SXvBKpnH8gWz47rfVtFxA2rLU2c7oQH2bT7tusKnmCeUOGBldaHTbRR8gwLA4o2CVil7z1ffnNBYoUmVZXgqlqoIzYQIXepxk88z61P5LUlCnoi6MdCf8LWlao2MuBRXqicWSJzXo77u-RwaRLKE_I7TDratC03-vkYI1ZG6KHdy16z2z9L5NsEuLBeBql3ESpOX_flF4UQO57PmQPe6PFO-6Bxg7bJXNm7OWAqSviSr0xjDBoO0l10mQFTXwLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2-A3IqbP55_Dt6Mvqok_nGCf-1UWNA12qI3lVmQQLTioft8vhAVnsbLpttmj-1uyIpkWYts-HQABQl8RsDiguyF2dl-keRY2hV52Ih7emTAo45zZtKFEFJyIxHd6a2ji5XY-wdiierqTGdOQWxbDEXG6gMsTvdiIIbBsHQdBu2sPVS8g6EdP5zFFOS57NCQgIT9DlZ-uJzX3IGLon4xI9SOVz1-6pSw5Uwprppu5GcSdeO-lmgxTOtG71NzLq53v-Lm5GL--NJr_nDhfCd-bLMqhu4mPnuVVyHi81qMRGndzx2Hi53geL2vNNLzEwfv9x1yGW9COwO5fx3s3sxaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEc3JTNEYD_gFuIYOHUSiykplnl4etDNxzrXG4f1rFZqLqFm0Ta8FuVgWFOS_mL6s7jEALuwl92YD7r05jgn0Kc-CsMToNvk3nvU_RKjyamlWpbLqH3-QyZitgKdG5PUSzowB5LbPB5K8eX_ZOB9XjQpgxiIiiVEW3udeExrKX3nTmMxLknHqviQnHi1YvU84t6rFtug_Ikhk-QfrSMh6sSYdfee0CTlRumZqCaqtm62XngCUgoCIF0lZFPKR8xw_lFjbvsQUtX7VQis4Fx3bQpcXc1pA3641uScbnGU-1z1YDFqrcbaBdCveGIUI5FIaeVEJwTT8ydYgMYLPP4XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz8-bmVtISQsbM0xpGVOx0pWAN-PWEXcryQP5Puo_nLeEcmQTxIuoQAct9YxRbAa68gpZqc35-68eq9YfmCOP6YQGzT4plZLFPVKeZV_Pm3AE3w9fskWw7RHbLx9i-5420F3GwBCVFTDBgCBXHmkabgQc-yNIiRKsl56X_S4aF6iXXmKVLjI2dAyFeCSzqASEP1_4yckwuEPBhcSVQ3NBxsKC2-nOn0fPPkKMztSBmdPk_sJx4LxrOizBrMZ3Q0S4Z3eK70LyF2t512H2baCuWdgMlvJtL8c0Nq_cR7Mw5sjBMzoa3lz8SjU_Rin9zhZYyzrAi2bGDkTH5IJSz_4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQBbw0QxsMcU2j9fDTVlyesjvTjc48NLes6Z5WG4cF5fhTG9CmyUKbAHjrSc8Jw8u8VoBNORVUKvIrb3q2aHtj31zEkjRgspoYrWI9es1oDeIuxC--2P6oTyIel1sFAUUBn5Gp8rMzEAumEoB6N_Hhg4cwWZdATbKrGVJG7SmBD2nA-nzCkeAvqWYDW5HTPX6x4wPLGuHp6RrOEBtXVURa1gJUDLeBKECpcfId8RarV03UZ0N4I-KiKzMNGP8k_PJU42mU55KIb3Es9ul80bi00luv5AUl_q7Ex9_2TKr3gqDpWSUF4cBKvD-oK0S9b8l6q5vxQu9tujxDljADadbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAwXSffpF7TnCslp1QjeOnqmdSzXt-iHGxqj723bW2tJXcHhn0AXZxhZUZbK9uoqE7GCdZ40cjlv9ikkubLEBNL3KB33ShSroaXCSOGtqVkbndRkhixBZj6wweokIEMx7BQA4wyDnMTlFhgtdD52zZDaAhyIToeEqmoPO4J9KybC6YL0_BdfalUqjQCbXMHI055p7rVNTrEwR66_Oe3MsQMXARzRGwz9gh7jQddolIlF4dGpnqrr5-W-aqQ2oDA9_Uily-429gDp-YvyINgfnhvvekgyb0fkzMl5yIFLNbHM62fnJfArabcJWXfdKj8z1w-xL8qWBhRrKBiKWvOKVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1UNJevM4FIMYigb_zCebTlLgXMD2v2rOPA-kp5gV7TAg_oE8jPWNnpGacxJj6yvhFHeShaWtTLsnTXizhGvYI8jYlKTaisJhamp2LIWa9h7JBfvqYON47-9GBMubVpTz35niavu8lGKKnvLLArO0zpF_c6mLYQFekBrWJrQqv7maq5Dzgoc-0jBd2fLB06zbnrfV6JPGgJfCFL1nx07oeMCjDrQACqUEj7ySVqMD3pNdvfhZGEBcQk3NhjwZz9B9ZLiP6KNSPhZ3w4tiA67POGLKfNzRLlkidZV3HQcj4wBfeVGaXkhzoWQcvljA4sA-dIfWdZglt6byn67OABNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=h-v_iyfgmkpo8kBK9gmjUJtk9nRqTNygJn-0QaVTm1QZlb2CfAtJdiXz7PMqTcV6lvKaFK7HJ2vsE8NFkC4TAKJAKA6RA0wvnCT0DLCP0mP6OytkBXHkusvYsoDtZBBc9wrgsYt2Oe9upnNy17zkHDU783MnjOQYgSrPa8ezvQCLA-VyMY2vZ1-fhzq3RO0wr8bJGWbNZJxXZeVxWlvpiI9HArQEpUT41W-Rapn0soN6JkfAXXT6RrtGN86yZeHxCJecyjQwAoQVJjMa8uohwIKWKuKpVp3SP2d91ys-Vh_lqG3Sx8aO0oYCdaw1Mt_7QW3VIRUsP-pFrgIrU7iR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=h-v_iyfgmkpo8kBK9gmjUJtk9nRqTNygJn-0QaVTm1QZlb2CfAtJdiXz7PMqTcV6lvKaFK7HJ2vsE8NFkC4TAKJAKA6RA0wvnCT0DLCP0mP6OytkBXHkusvYsoDtZBBc9wrgsYt2Oe9upnNy17zkHDU783MnjOQYgSrPa8ezvQCLA-VyMY2vZ1-fhzq3RO0wr8bJGWbNZJxXZeVxWlvpiI9HArQEpUT41W-Rapn0soN6JkfAXXT6RrtGN86yZeHxCJecyjQwAoQVJjMa8uohwIKWKuKpVp3SP2d91ys-Vh_lqG3Sx8aO0oYCdaw1Mt_7QW3VIRUsP-pFrgIrU7iR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk2XE4QsVR1YhU5_2MJO2QtFcEHZSzJWvZIWvvdnwzzCIbg8rTyKRE6pHTZ0dv8mhlbaLWJIUNljzHs19Ml6ITmpluODY3g3s5-TmUzYVI5EX9nqkfDsXxdVpL9ViZ9ac_SzQjjnfDhedaTtuo1rPZqzrT8awbYthBXwQ5SHc9D-QbEvO1rqCFhsdEtOX6cAsgKjn8GjjlLVU5bbD9CzTQMMD8IQ-XmTjDmRRJuRd3iTI65OXosBJ5e0CScc74ufCyfZdxwZPJ_4x1vaTaixaVReJrYILNS4ZRtxM5h2-qG-POluE4gC72ljEbsdKGvQYLNj91KBqBp45pqOLfb4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8OmvVQE-phzPWiNotVNntZ-H4WR12IgzgdiWfsOIdoElyyUlMFDDl_vJTQsuwPAXQpb7khVtKvxTLcR06_ztlSZOMJ9l3ceP-3JtgzEhtCYJZA_g1aaQRvL-yV3T-lAdR2ViJTdNjFiyKmeYHDK8SIHm2oybmhpCKQDXEWYqTuDQCTmiG1ECUlGcasIiSeBDHY4yEHdfhn5oWsx3BTkWqhfMNJlcuyYSeP-nAxQxBoJAYAwGkh-90hoz99mNb4QQ2S93dM_ja3k9J3iESuiEjYx4xxgSQkkgWeAtpcKbuVLuIjrw2xewT-CPb2lFVKI85ldqd__VKFBnNvNngEIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5fdKA5B8dH7plVXSEx0jGqEhTsxbR5n6y80_UGg1zRspzwpX5JiZttwqZGKFrRmj871Ll96IYYNm0eiCwupVF_PpsUhE8uYb0_Y2MyOIe83hzRECDi56A_RRENMjWw_TiH2NXeGL5Gm5jFc4yi_TLlW7W2W8GaNpzxbzWKX16lfCvxz3mX8gGI4WjSem6rFdaOu-Mr-y3o5ahzkmtq8kiCV5i7e_ELYik3EmeiRWC-EevPz9Lf9LanmHyLI93Z6QLv6_vI80QwLAleQ_Dn0utT7pAW9tZssxccSMtx7MfsnDUQvM06jdIPY8dD0aFjzS-gTRuMYMiWlS6sNxieq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30958" target="_blank">📅 12:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=U-ACbJ_uXoqbLIowa7FkfSwViAGWh8j8qiE-B8MgFxZ8hWLxm77KtdfGL3LiZY5jTjxOJwBVD0mMpzNwQtX0hda3X4Kc3At8w7Bc2znZB1sGpyidZjotZ9dDmK5hlHv61_8m8eJNNHW-HYYIsFusQZZAMwyydo5Dhj9bw5C3TdjHzhDdnRMY2Z69uO0W9ngp3-6jpyew9ZCFu78zg0-1oiWdFLjIrzlkZfW3uTdoq7Q4kdbSRgAcpbcaRbAYFAZWWBCTu5JnibO6CaosDkz9uSle354AMHPLEWOkbUT75abSOv_HRMT73DZg_DLsznt6cD8XUFeTK7v-HP8NB61aXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1a682d8a.mp4?token=U-ACbJ_uXoqbLIowa7FkfSwViAGWh8j8qiE-B8MgFxZ8hWLxm77KtdfGL3LiZY5jTjxOJwBVD0mMpzNwQtX0hda3X4Kc3At8w7Bc2znZB1sGpyidZjotZ9dDmK5hlHv61_8m8eJNNHW-HYYIsFusQZZAMwyydo5Dhj9bw5C3TdjHzhDdnRMY2Z69uO0W9ngp3-6jpyew9ZCFu78zg0-1oiWdFLjIrzlkZfW3uTdoq7Q4kdbSRgAcpbcaRbAYFAZWWBCTu5JnibO6CaosDkz9uSle354AMHPLEWOkbUT75abSOv_HRMT73DZg_DLsznt6cD8XUFeTK7v-HP8NB61aXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
زیباجوی عزیزمون با این وضعیت بازی مقابل تیم‌قدرتمندهندهفتگی‌حدود180 میلیارد تومن درآمد داره. انگار وینیسیوس واقعی رو کشتن تموم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30957" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn-dN3GGpoK8r42flBca1PPlQP89hazvqAT-QmsgbSuqslIXh34nuo8Wq5qMWfoM3ueXJmsa_Or0wZun1UQs2i3ZZNQzyiJvmNyBgjqkWMGzTD3kcZOEFASYs7EdD0FXRAvfaMH4uNcT26AvGlhMljEaMnpLg-h8wU6ZEatzHGK402GTEEFpWefORMZn6XGQ-nMb1-KxVakEes351TdufXJGrYhbNNe5BCxv4PoY5WWgdV344TBlVPbsdjuniYavSWEbTR2BpecIiMvOLA6A8Q2f8GyZphmldozwDZAU13gt5XNNQ6UhNRCctq5LQazgY1DifapZZmYSnPIMnznk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ در صورت موافقت امیر قلعه‌نویی تیم‌ ملی روز سه‌شنبه ۱۴ مهرماه در استادیوم یادگار تبریز به‌‌ مصاف تیم ملی گینه بیسائو میره و بدین‌ ترتیب مسابقه تراکتور و استقلال لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30956" target="_blank">📅 11:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIGd0RSGKDf7b-EOBNQ2CfKUoGIwGA8zCcblxNgyrStZKY37OVw5Y-6_J4WlZOPLc5bC6XHKT9dOQRKdVZyvbZxu0RsLUY__wsTgFnoU-GhJVQjM0Xp2GJfxHutz-12nBuGGiXF4oOG3BaoeE2K6ozYdcBlSgXi9F9Ebv5vUT2DPv6fdyePQR0wZFaO-eLH5JBPZPgWcprmyhqvxs5IhE27-Tgv6mMROuF5mV94bqLSadmmhjh-NIBEKqXy4ZxalMlYYXuqOgn-az3_qccF-J_fAyfbdiT3OZVADgiP-ju7gN9aEBrAKayYhelO25nPPD_GXM-cjrwslfZzxrs3SfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30955" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56284423e.mp4?token=hK-wvHmCJrwXu5NTcYxrf6b0jp0zh7tBTX7uh1MtwlAPNVCa5QP791K4hO-GpRAXggLR2Mcybc8CeFrG2jD9KsDTThE3JmRuNUIWoZ7qCOr0G_vdLYoBFGw-GI353h_Gg2m5ZzXyaeBMjr9S9yf_UIXHjocpNYAQGobzF4Jo-KAmjXLU31JY5IB8N8j23ienv1UFwM6uJ-mgRGEUiG-kYjHHsqGl7Y1jAqNRb2rorcHe800CfvdL-ecYxQK3SSuQMw8BjoEMcy75dmhpd_jrzXg55m9MRZp4AiFtAwo-R4rF5ko29FhoyH3Go_pRA_JVWgmqRY0wzmOC3oCFYyi_pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56284423e.mp4?token=hK-wvHmCJrwXu5NTcYxrf6b0jp0zh7tBTX7uh1MtwlAPNVCa5QP791K4hO-GpRAXggLR2Mcybc8CeFrG2jD9KsDTThE3JmRuNUIWoZ7qCOr0G_vdLYoBFGw-GI353h_Gg2m5ZzXyaeBMjr9S9yf_UIXHjocpNYAQGobzF4Jo-KAmjXLU31JY5IB8N8j23ienv1UFwM6uJ-mgRGEUiG-kYjHHsqGl7Y1jAqNRb2rorcHe800CfvdL-ecYxQK3SSuQMw8BjoEMcy75dmhpd_jrzXg55m9MRZp4AiFtAwo-R4rF5ko29FhoyH3Go_pRA_JVWgmqRY0wzmOC3oCFYyi_pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از سوپرگل پشم ریزون ستاره‌های فوتبال درمستطیل سبز؛ گل‌هایی زده شد که هم‌تیمی هاشون هم برگاشون ریخت. عالی بود واقعا. از دستش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30954" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvH2BqEkAG2XwZZolz3890D_w1mt_xU9aZ1w9oHy4KiXc2wJMUoAOYs-nXdF0MOWUwLhpvBYDTJJNoYEfAPr5Nmr7n0r4gfMq0mWUl3-RuoepElR80O2ccub3iObgL5iQEPNZGzEQoBxoVlAoYiucAi9oN0Ozxvfcfu4CjIvMaByZGxj6JP24tvedmBgM8svHTsfNVujLfaOE8nJHiVZpUvqS7Si4kts0KJ4o9oIzfD5fzBRDVxc4I9RdSFG7TevJOh16xG1bdI91J9or6OM4RRrruIONXUa57Ljgue5DWuop5-1UXum68WTFwbXMTuIBxHKxRp18YE65SAj23be7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اگه دیشب داخل کانال بت ما بودی می‌فهمیدی چرا همه  دارن درباره‌ش حرف میزنن
😂
🔥
😃
تحلیل‌های جدید  امشب
سیف تر و آنالیز شده تر از دیشبه
😃
♨️
آرون تیپ=
وین
⚽️
✅
💵
😍
فقط یه کلیک فاصله با وین داری؛ بیا خودت ببین
👇
😃
JOIN
JOIN JOIN JOIN
😃
JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30953" target="_blank">📅 11:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4212a360.mp4?token=dLOgHLm9wpUa084kSpHaleRTcCyRmSCw7Baavs81N9CqNsbPclcP6Hch5SN1DryMULtnBeDsCmwjNI9j27XmkAxd6d5isSCpQlGOKo-2ynAsqbod2Dns8VQ8LBdwiHmmUPKC3qKj1nw4FaYb30VmDCh2AqUxrE8WJ0oIBAXpE0AtYqy-a9ausBpe9gZywC1hibBL0TAbM3Az-pCoF7H6HtE3rORIqQdq_NJNMTfpHCJMkQX6cLCsfwxDUXT0_n3re9VlszdaVA8KZRIlgQDqIujQ_M8HQlNu3s_lAM4AUYCZHLzi8Hl4vMs6BM3IaIkwBCvePbf6eqefTZp9KXK1XzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30952" target="_blank">📅 10:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=L0hm2QG7Vr-b1dphLbaAaxr84H8qNMf7FxF1Gjwqilwc8coDcVC9WS4PT7aGIg7LSuUWglCRsn-ym9YbBvqulwJXllNtE9QEMv5omuCTEaIvyQv62oJ7qPwDdrvGOS3T4ztrDd-D8OPX01utASBraLz1JYK2RQD3fpRgGUoBbWUnhxN6yhhUdySJW-SBphu6qZkmqRHad83v_na_v_PDi2i-MvMrMdXB-PzjPrfJgckszL9US6gKePCOwUWIq2dyu7p3_TZFv4OZFr44lZtoUWPYxqjHbuDflGRyk9RZfZe_vw0jN7KtxdxtsoxCRTtSV3HMPw97R6pnEwRKOjIsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c94cda5.mp4?token=L0hm2QG7Vr-b1dphLbaAaxr84H8qNMf7FxF1Gjwqilwc8coDcVC9WS4PT7aGIg7LSuUWglCRsn-ym9YbBvqulwJXllNtE9QEMv5omuCTEaIvyQv62oJ7qPwDdrvGOS3T4ztrDd-D8OPX01utASBraLz1JYK2RQD3fpRgGUoBbWUnhxN6yhhUdySJW-SBphu6qZkmqRHad83v_na_v_PDi2i-MvMrMdXB-PzjPrfJgckszL9US6gKePCOwUWIq2dyu7p3_TZFv4OZFr44lZtoUWPYxqjHbuDflGRyk9RZfZe_vw0jN7KtxdxtsoxCRTtSV3HMPw97R6pnEwRKOjIsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30951" target="_blank">📅 10:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba85e2ae9.mp4?token=WtElvNLSq67tFwwSKOhsRuhbo5drrAvhBr6-9Jnz6PD7iySADFPss37rxJAN02BaN61iidVOs34orri9_Bp_YFUU36OEAznIUYqdX0VqjgXI7BAvNgJBsbKAmkmdhWP_w7foSrj9VFxhBr09vzAIjetDsUhkO6VfCD0J6SpGCsBqCQTe8MsADhgDs9yg-R_G_A8eGKEAqdv1-r9GeF5_6RqRjQOZJH_P2Jvynykfb1cqa4xxm4LAHTlbu3wkEry9QaJLm7qYPR9k-sWAJDJDAdDH55yIlYtHV5ZYUBKrlL4CPBWkyRIxxAq7SCZoiqGIGu3YUbwI-kjLfh2hGUV9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون یارو مجری بیهوده یادتونه که چقدر راجب فیلم عروسی سعید کریمی بازیکن سابق ملوان گوه خوری میکرد؟! دم‌ از شرم و حیا میزد! حالا در نبرد دیروز تکواندو این الفاظ مثبت هیجده بکار برد!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30950" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtQfx4wJrgfuDku7LSROsPmXSvwGS2Ph2QJ10LvU07Cvk08T3uLBolYwCdnepsXUattEE8hFHNGDROWLZ0rcNDBe3gw1LhMLCeQv8ipeZfg39nNHMXocWk7OLD3304Whf5RLuUQ3IebaDycSqqUNZ1MKmV18A8_ZQDWzklczCXanbMSAdGAyhMzYR7VmeLspqgYlGB5XNkk7u0eSnPIE7mqmTbphRt23xrmU6V9cZbRXbvjH-iu2oMs_RBc1eFRX4L5UMf1X3njhIpxk6yDH2XRBNE-FgUIzZP9OihJFybtCWmR2tKTtmpn-UTHSls0iamaFdl_slT2kuIM8h2NAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای خبرنگار لیگ برتر: یه خانوم در کمیته اخلاق اعتراف کرده که با رابطه جنسی با چندین داور، برخی از نتایج فوتبال ایران رو تغییر داده!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30949" target="_blank">📅 09:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCRx87dLHvGPl0eJtCRAbg-dxkLR2VpQaza6EirVwLMkffKTaboI8PmV6k1Z74FdpQRi708884MWlo5ZYKzW-u-VLY0Sj3tyGZeqUWiAw0X7ic9l-N5yDb34ZOCpfFqEw425ioFi8TZU8ADJPUhAWmGm2QLCgjVaxsU0lN7p2shC0Xdel5No8ehnxMR6MJIRXdnk-TvnFnYReY_Lc6fo9qui63gbVmFsUobtZpg1APs04n0NA63Xph57XMsPbC1VxAlK9fUfwJnNdaG5PFuEHEqcs_-TfPIMzsQ3KDAaO3fl2aDFFvCnG0te320fPeeYRAqqBKWhopFXgDIz5gsjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30948" target="_blank">📅 09:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htf2yc7rl3f__1bHhjM4jp7KUyqXak5fRC4KvqYUzU-ePYDlYcXsFar_7JS_aojD7pkFfAhAs6NMweXefF9XlMjJcX8cHlD8gIlVQI4Q0CdTKgeIZnpQaJ9d45E6d8vX0u9-BmNGqpPb5vOlIWBGMIoUuX6HU346GkxaNTY-MrFgUlOlnx1bzFH-tkF76RkiBDjLD3VlB0IzAj6R_tN3nrrElW2LMK-xxZDW6C1pkh5oeiY315MOe2SshfNbepMPHXEwTGhv9IwdOtOmCNtF_ESPfiutlT1YAOTCXx8__OcLhgUJXSQ99SfO1GDG6XQZ5G375Yyjzkgl-wmar9BeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه روز پانزدهم "پایانی" مسابقه تنها نماینده باقیمانده ایران در بازی‌های آسیایی 2026 ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30947" target="_blank">📅 09:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30945">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp8afzPqJdqJ6gSivn9_k4t_lohNADB-YQAedg5EYupnId8BThCbLSTxmRcqJSnZk3wwstqwqK-euqWdWz73Oeu4qt1t5voQAYlCd4nSkEs6705hLViwVHZUrA0VqqtH229xdPEW4h44QoqBPrAZ_Amv-QdL9hqWoi8RsoRjle_9RGuOxHlTHGxxYnmkOmpPj_1yNsneUBZTJT34lBfqec5UAafQihIBbKxY4gekyawCAn6aencMIwBBs2QKYgDca4oodbDo4SdefVf4E1AAHO5gFu2A0msainkEEEet3A-LCWTT3Hh1j-u26ckeD1Rb6zzmmbCMFEoMusFB6V3PDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز
؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30945" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30944">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHaHkfxPrkBKXLq7Gvp5AbW0tLhQB3Dl6DU8SY24wfb5GMqYgmHQghcn6l6OJbjKggl0V2oa1kHVeuBOXyd3uqzJuGo17NCaAGrlG-ZfVn-ZWmisjAgJ4m1jS7WSD2kLYfWx-LxOgtQZX5tLKIn4FdD6SulmcCRQLsZbYjKfd5jGVmhdP_ZOaUNa6ZvUUAliJ6jVzKq4p4-pkZ1igMubNSJWmiLhX7WY1qjUo6dSddUi4rCVlQG2fknU9We773pR_tNmiscoy5og73HFEzNl32soTGro8c8kiBuYnFkRULeKoKkolmfl45Mv2I5ok8MTCrwu_FyYnHj9K_zMkdGtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
تحقیرکرواسی‌بدست یاران توخل و ادامه روند فوق‌العاده اسپانیا با دلافوئنته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30944" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=JWQ4PSOJPsSlA7n7zq6OsekmAGj4I3rZCKexAFLqhosVNabYdYWCUejjlLXAcYkbR3o4yGWc7evEYg5tW0He6SoPHy_HkWabitv1qwxKkuljaw2zqTeV7FRWs5v5uXkGuXmo-atTYue2RQLHcEXXtL31p4avsOTwBXVng8CQFO9D5tPNP_rcpkoX-oUf49Tk8OofoXKEMD0cll1sF7eiA7x5eqv1hQQY3yDq2cVZwg9ie-qUJCP8zbMvRO7raHEyoKvMFyD2gHKEJf-H28ZWzcx_6VCynnPNE0Me_BlEV8qG3sySqz8BHvnuQOQ3UpNbQjRZCyfspmbgZSv43A6pR31ff7vnbeMZ3GL3JqlRBah1xICdd0bz2yFc_MUOuwf7tRQlFLKIi23KhS3w-yxWV_vNVaIW5tvQDQfxWtMLj0yjuRSfJZF-I7eORrcIKdb08w20HfFwIV9h4a2c_92Hyf0XzBc9EoBvZqvON3PKy9xnVwNNTsytIGyXTNPzF8d9tNnRWMrYRIDH9qycGkIu4iXd3PZWSwKjN5QBkj39AykwODb1Vk5MQi5kmY0Ectfz24r_tQpdqezGnaQ6pY9d5grNlGIFPa_hxLihFnzkKecY7oXwK9Y5KlPCaN_Dx97c_d96uAl1EU0tScROdGEjDnHtwQdjamC9cB5XfKwgz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df8fe53e9.mp4?token=JWQ4PSOJPsSlA7n7zq6OsekmAGj4I3rZCKexAFLqhosVNabYdYWCUejjlLXAcYkbR3o4yGWc7evEYg5tW0He6SoPHy_HkWabitv1qwxKkuljaw2zqTeV7FRWs5v5uXkGuXmo-atTYue2RQLHcEXXtL31p4avsOTwBXVng8CQFO9D5tPNP_rcpkoX-oUf49Tk8OofoXKEMD0cll1sF7eiA7x5eqv1hQQY3yDq2cVZwg9ie-qUJCP8zbMvRO7raHEyoKvMFyD2gHKEJf-H28ZWzcx_6VCynnPNE0Me_BlEV8qG3sySqz8BHvnuQOQ3UpNbQjRZCyfspmbgZSv43A6pR31ff7vnbeMZ3GL3JqlRBah1xICdd0bz2yFc_MUOuwf7tRQlFLKIi23KhS3w-yxWV_vNVaIW5tvQDQfxWtMLj0yjuRSfJZF-I7eORrcIKdb08w20HfFwIV9h4a2c_92Hyf0XzBc9EoBvZqvON3PKy9xnVwNNTsytIGyXTNPzF8d9tNnRWMrYRIDH9qycGkIu4iXd3PZWSwKjN5QBkj39AykwODb1Vk5MQi5kmY0Ectfz24r_tQpdqezGnaQ6pY9d5grNlGIFPa_hxLihFnzkKecY7oXwK9Y5KlPCaN_Dx97c_d96uAl1EU0tScROdGEjDnHtwQdjamC9cB5XfKwgz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30942" target="_blank">📅 00:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko1FL20jr0MLUIX3JEXd7cXfqVG8gmd13rEFReGe9lopcBwKkYhPdm46P1SfwActe6X_jRLxAhWYQL8k7CcrpSthEIPvKYOfHqj3E0uxwci9uvRMA-Ydlep7sYX7hHAYu768idj8fNT7djHhyEBfkMzRWu39FXQUE8yNEEL_n3gRmQW9wQEf5ckPJwM2XSiaK0734gExYuL2jMO8Nb8B83JnTPYztmOJgGiwSFaU9CDQQVEW6fv1WaqJcugWdnCilDf49OXiAlfrMtrIT_C6GmIm3XKColxZ00FDx3tGHcOJ_pD2ToLF4KV5QLHXcGkdo_GgljkXJoa3L8d62zh2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌‌سوم لیگ ملت‌های اروپا؛ لاروخا در شب درخشش‌لامین‌یامال و گلزنی‌رودری با نتیجه قاطعانه سه بر یک از سد تیم ملی جمهوری چک گذشت.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30941" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30940" target="_blank">📅 00:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQUvPyYAnI0JDHTTi03W2gDOvdN8gvdKW7l2sMh5mdF7hAWwtANKk5ddDIe0nMnQNZC1h8hl-Z_NEIuP9T68EdouG0bPMahbyxvgRMpvBnD4uEQEQ54WmiNzkTP9txApt0gYTH2c6PiMzfLx2s-yv9fpaDRr-BLf35ijyUJge-hy3ODmhjhEBU7ZkMQFcrb4UYaRBHlZTfJQB7ooHfhw6ScMxkEBVlqEI_FZafYXeGzJX1ycuHNrGFiDm62v4FEgE2bnpBAGnRlcEufOPelifQQjfjZeYOEa0mduKCZcdPAXmwYGPjGg2sBQpTyCCipfITyGg3Xsgp_AJR5GuSCpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30939" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjXvfr-8uRL_oGqQSUGifMvm2mktGry1P3h9viAqZEq1BkwrXtW-1UcmViJzj-8gqlx77DG7fRZdGG8Xnvxc6mD2GifUaJfEVRdlu0TyeSqf7yc_vz0b7RjSI4Hsxe20sgtcq8KjhXhZ1alg0D6Ja2jmFwcr6zH5o0XgUgoS0KFvOKHtN3Y1WfA5KZ1jabB1AhVTrBge77aKkn384sEueSK65IZTYHPl87PxqJntczeODOvQiriCaojonZ3X9VGCeEQvRbLO9aGq8u-czY2UgeEMimuI0w9Pi7z3PfpqXz9ZC7aSq3EEjSyVJGfEGeolZByb0B4f1-G9Pilg9Tdvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30938" target="_blank">📅 23:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNYWvu05CkPTcN6Xf1ZUTv3G7VKtEgKmyapMMEa_POHWVCEm4TwljnuRMDEU2WmohA5Mnyv8G6hilqfFqMGq5oo9rKpDQHXccUn8xaEdQGfgwWzCR6uaB8wvnUssxCEsfe_ctZ2n4HjTO09JsxpWlwOuRLhoo9aytHTUuv_lYbHpQ7XFzdL5Vz_go7tEsyXyDkmUiClcqPOFz7u8ZASZDger2AMpnUKSoT7haKuwphpIQsWgulveAtIMNX60J8KNtZyp5os7rvEhGuX7cTL3l32d85QMy1s7asWFvXWGm8MjwXqlsKt-HAlWL2j4VPMj6uwixVGg4XNw7SPNDp0Mjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30937" target="_blank">📅 23:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_xrSkOnhioBuYtMqkGDk_zUP9s7N8eALJPMk45eAyc07OeCdXG2r67kl6w6uvf3vll8LF0gEXHKBwjdmUJDDll785n9ixLG1E2aN3D_xAL7Oc1aZ6FDisk1X49Nyz-AbV91VRMxWUuJw_edVi9P1TGOOtMP8AyZjpaM8uzHKkhhQGN6ltMgIEFkbq3kVeWCR3C8rM0-WvX0njJqZfv4QduiHvYzNNCqcyiBk29vHEpFbAYHVVkzCHUJDgsGZ225a3XjzwX7pX5MeB1kxdnpPyG06Vpox7Xp-tRk8be9UEVlQSoN5GYtaXlCZ2olULABbQWqNGS_foFjpSiI48HeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30936" target="_blank">📅 23:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=AB3rtA9jx6Psa4sCtZE8WW4tX9iImWD1IIKCAFXUvZK_yyi_83kseAwxsRONPvMm_t-yBXvRYJXXQ39cJmZn6XwbaYs7dOfXhK9i-xrIsWcyNk7yZgYTNGuvxYY3o0hQ0tm-1blS_yvL32voeQGAU8hiUyefPoBPZJSRefhojvoW4DMTTKmby1pISlla4_Bsv4Ap8nhD3O2MCORyIFD6KNg3W82a3BUYOo2e1Uv6RABVF40hRECryHu58ntOMZ0ekOeDHWsMDWr4kf89S4wvMobp1MJFUrWqGTaaGv1bwPvWT_o-1bAK2X67N-hY2FCGLPAy-3PpYTdsm_obVUVASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f069d8eb.mp4?token=AB3rtA9jx6Psa4sCtZE8WW4tX9iImWD1IIKCAFXUvZK_yyi_83kseAwxsRONPvMm_t-yBXvRYJXXQ39cJmZn6XwbaYs7dOfXhK9i-xrIsWcyNk7yZgYTNGuvxYY3o0hQ0tm-1blS_yvL32voeQGAU8hiUyefPoBPZJSRefhojvoW4DMTTKmby1pISlla4_Bsv4Ap8nhD3O2MCORyIFD6KNg3W82a3BUYOo2e1Uv6RABVF40hRECryHu58ntOMZ0ekOeDHWsMDWr4kf89S4wvMobp1MJFUrWqGTaaGv1bwPvWT_o-1bAK2X67N-hY2FCGLPAy-3PpYTdsm_obVUVASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی که قبل‌شروع جام‌جهانی بازنشسته شده بود و از صداوسیما خدافظی کرده بود امشب بار دیگر بعنوان مجری به شبکه ورزش بازگشت.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30934" target="_blank">📅 22:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=nkETReHzWX0_dDFTHJYAY3ku6UyXnPDaBTFnZ3aAnX52luiQA4pIT1H-LqVfH5qx6IdIyHwe00RMSObRdola-C-SZLgsvFb-JBV-2T2xIZqRd1BoJWqxQLGjYsv5v5BBuXE4nykXkUMI2JGUy2Bd_jRiWnT7cZ1baoE0jEpMSbVqFiPgPO2veIdcQj_odPd9SjazYgvMezbKR54jL4JhQWQxDW_ziqgAaeiSRxkCQuenK4cHlI_MPrQSNpUgwEDHI4KIO_tF9NR9lpv5s1xicoqygGZOLTjsc-8gxe9G6OOU4t5D51g4aveuXFUoq-xoU-5mCppZo-pabMVM4uKPIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8329d169bd.mp4?token=nkETReHzWX0_dDFTHJYAY3ku6UyXnPDaBTFnZ3aAnX52luiQA4pIT1H-LqVfH5qx6IdIyHwe00RMSObRdola-C-SZLgsvFb-JBV-2T2xIZqRd1BoJWqxQLGjYsv5v5BBuXE4nykXkUMI2JGUy2Bd_jRiWnT7cZ1baoE0jEpMSbVqFiPgPO2veIdcQj_odPd9SjazYgvMezbKR54jL4JhQWQxDW_ziqgAaeiSRxkCQuenK4cHlI_MPrQSNpUgwEDHI4KIO_tF9NR9lpv5s1xicoqygGZOLTjsc-8gxe9G6OOU4t5D51g4aveuXFUoq-xoU-5mCppZo-pabMVM4uKPIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30933" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjoHW1FV19plejp7cqwZ5DsnHGV1f2ZK90yHuYmfTO42Zv1e_hVxDzOWuXXu0JK1TjIdTzl24pPyBO9bgmyyplJRwAJ8BmEFudbW7YKyYChoKpQrELM9KUc2xTOaY-QQmtG-j_86BdbhEeDnm1lOa16EleQ5Fd96n-5kJpaKnL8P_hkIiXuVgm2iz2WzKzidBnL9f6DpeWyvknB1813auvct5vN_DsAKtQVaiHZyCEnHl7HzhRSpdS3gtKchX6ZVqVRy109R6yUUieXh1XLpji9qvu18dRrqQbXJhAWcsgHtqr-vvMucQB7HVSy2e1m2Trwdz4kFYZU7CaT3Kk0iTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ولی کریس رونالدو با خدافظی از تیم پرتغال درس خیلی خوبی به‌ما هم داد؛ جایی که نخواستنت نمان؛ حتی اگر تمام خواستنت هم همان جا باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30932" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30931" target="_blank">📅 21:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j135yDJIhtaqmgYG-GnN9vQnQc5JPmEDOo0SL4OBsfIkNZ5uzVSsxarUS8lcGFsTqyn7vd2m_phTWkdhndSKO7lmnZ6LfY6aUL90SmLo1IesSU1MMpRdGafD4yME91QN_BS3gUWxfsj7gfVDen4BYYkCmdJ693xlWCqWvxpNTr8hVtUyVtHwuQAPB1JqPp700PBINS8-Ab7jSYfgBqsiW74ipf_XIkecGcTJP9PL3DtBZvfhsS73kjiYaYmXcp0ckOKStQ5VseKIp0f9AtANQuQHlUPJUhyZZAfSpeVlw5VQ1Qnnk43ZLVjq5Zn8n8gLvLw9W-iWd18HQIBaBEhv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبرگزاری‌تابناک:گلشیفته‌فراهانی‌بازیگر سابق به زودی برمیگرده ایران‌وکارای اداریش هم انجام شده.
‼️
درروزهای‌گذشته‌آهنگساز بیژن مرتضوی به ایران بازگشته بود و رسانه‌هامدعی‌شدن که شادمهر عقیلی و معین نیز بزودی به ایران باز خواهند گشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30930" target="_blank">📅 21:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InvRVdori2Hc9jZraDgOBOeppoeAn0f54C7GGtF_nEcNo3TPBUgIgbb5-xM2tW3kfTFgPKtbRz6XN5fYGRV6fNjGLl_mLw-NTFMmkS3UsqmzGIov9TQzOKw5t41a4-GyZClrlIm6jObYC6Qgm8SXvtjum6vmIc8g6gGgB2zlHxcbDu9Dy6p7KUvCR2apZoU34CH5kX2xaZLw7TC5YTjVtmM7BJd8iH7aCL9ApWBmG5sTbBkXD0L2p059bmsBrx5onYecH5KTMMh2ZwoZDelCfvlPrSR-qOvj6RPQEcHWK9LysydgtNBwzlwz_4ShCgLo_mZrH68UT2Gx199AOnMbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_-JxjZ6YZyfK7cHUv_9dklUCAh66lxSxrHc-YftUjj11dhng36ZJd-u1VVrr3LU4GzRM-lqaDWtQLS6KhIur6grsEVrNGCjkNuXcugIhzoyGs8wcOzaxsFzn6YQqBWx9NNYdeAYBtQfJunLGN0_VSB_q-VPEku7NOt88sKBxgc2WT3psa65j0Fg_oI6GlQHAURhq-I-b-9_4zfo5j3Q5A89jWZusWwpqQIF6ko3dwZTMSKJPaXh1mGDFeg9_iAbKFS3Hz_IpCFhfMKhT7t1IQ7Yt8KAbCxYgooxDcs7Us5vA0-dpiWwofy7tdevr1qIQ2qDiyhV64HFekgp8ezVBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرنگار شبکه اسپورت اسپانیا و هانده ارچل بازیگر معروف ترکیه و فن شدید منچستریونایند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30928" target="_blank">📅 21:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=nfTvxT08DwUp-GgKVJWax8dS8bxJ-RW8NTbKyhv94eFh-Hka4UEOaQp9n9K-QHBR22IseOcO4fSLtCNeMJyj7VKswPIdNquRDoKP0mwFiHjqqq0LV7Kw-sctyZL6S187pSlEoh-9Bb8yr-E8T_Lgr4SBlCeeTxiUzXF1YdQZLCZ3YalYBxYIYgtPGTWRWV6a33Vcx8vJv9WsLju6a3EBzwedqMMKK4j9exz_ewN2HCfsxL183LMzSNu21N0KNomXPJhK9fBFEY47VcGofT3-p4TEAlM_azLGK0ZHB6daapT00qDZcLmUwyBO8G5epJ0ZOVuljT-mhnx7zTraWdTiwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/470c5a8148.mp4?token=nfTvxT08DwUp-GgKVJWax8dS8bxJ-RW8NTbKyhv94eFh-Hka4UEOaQp9n9K-QHBR22IseOcO4fSLtCNeMJyj7VKswPIdNquRDoKP0mwFiHjqqq0LV7Kw-sctyZL6S187pSlEoh-9Bb8yr-E8T_Lgr4SBlCeeTxiUzXF1YdQZLCZ3YalYBxYIYgtPGTWRWV6a33Vcx8vJv9WsLju6a3EBzwedqMMKK4j9exz_ewN2HCfsxL183LMzSNu21N0KNomXPJhK9fBFEY47VcGofT3-p4TEAlM_azLGK0ZHB6daapT00qDZcLmUwyBO8G5epJ0ZOVuljT-mhnx7zTraWdTiwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کریستیانو رونالدو یا لیونل مسی؟⁣ جواب توماس مولر اسطوره باشگاه بایرن‌مونیخ به دو گانه تاریخی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30927" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=EnCGMiynMhFyr8W8npQAAb9PZhlURVr8KzWlq56nu1eYNlSApTmSUV3IT0EAffxJIliJJi0RBV5IiIja7VPH_g7hCkrkeAeQa3TEV8ALfX6mzCsS8n1A_iYXxhwRy1iKhkwweIZa0HFR1Jhm2iVlRH9SROkggK7h0NFXQPC_Qo3O00-HAYCa8b4PqghEzWZ3xvjSYRcZ18LtWQJE_q_AyJI8IIheBjHTzMrX23CaYrVGzsvcF5Z5Bcdo8aNPSBs_MzgB2XSHfyt1gQBFuZ8TO903TYkMOT1kIEESr57qzUvm_fppB12GD151uuW3_89nivY2uSONbMiMw4eDTDWGBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c9ed1281.mp4?token=EnCGMiynMhFyr8W8npQAAb9PZhlURVr8KzWlq56nu1eYNlSApTmSUV3IT0EAffxJIliJJi0RBV5IiIja7VPH_g7hCkrkeAeQa3TEV8ALfX6mzCsS8n1A_iYXxhwRy1iKhkwweIZa0HFR1Jhm2iVlRH9SROkggK7h0NFXQPC_Qo3O00-HAYCa8b4PqghEzWZ3xvjSYRcZ18LtWQJE_q_AyJI8IIheBjHTzMrX23CaYrVGzsvcF5Z5Bcdo8aNPSBs_MzgB2XSHfyt1gQBFuZ8TO903TYkMOT1kIEESr57qzUvm_fppB12GD151uuW3_89nivY2uSONbMiMw4eDTDWGBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حمایت جانانه و قاطعانه فیلیپه ملو ستاره سابق تیم‌ملی از رونالدو:
یه‌تفاوت خیلی فاحش بین رفتاربازیکنان با رونالدو و رفتار بازیکنای آرژانتینی با لیونل مسی وجود داره. من‌میبینم که وقتی بازیکنان حریف مقابل رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو پرتغال هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمی رسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ واقعا اصلاً راه نداره!"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30926" target="_blank">📅 20:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30925" target="_blank">📅 20:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmWzPxnW_zDI3fyGNXvjyyv5Pf3lqwIe3zBhE-8wwmS-e8PPcsKRnRFxH1XW2JJzw_BuofkJi-Fe3080LuxrQ2twNGCmFJ3fy2Y320dYLmNQTqp0KXHDoxezRqHlbiuvW_qncB34D457Tzb03oxzj9VfF1PznG4DMsUkDO95qqJhXvJcH26ipXVcFrnqmr84QzT-34-20ptPqizzac3FvDgUzo9DDtimKWbEFelNfS8TQ4ctNf2_GLyBhwtyhnA-F82yHoY3_MfBuoHFUBuR7hHKEUmVhW9AkclUSftZrSF_h8iiK47MUZJlHFNOzXsUon55ffz-XwMMXxuVfRybdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برندگان مدال طلا، نقره و برنز فوتبال بازی‌ های آسیایی در 20 سال‌اخیر؛ ناکامی مطلق امید ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30924" target="_blank">📅 20:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2e3a0sCkNLdk-ThxD-mF3DInQEptEaVp2Mcnldikto6a2icTyf2_EHT5mypb40V3NgrRWITiQXatc0zi2StuJmCPj8hnnkMdTv1Iq96YqY4x7KM88G91dWQdOTU_wpdCbmJ4M964a0SdvxThR4ThWBUNCQ3lg0Zlif7VHx2lvgSLUdG7XVpZ4350d0ed4zmiak-LLqTGpE2lnwcutqcsDX0XyGi28KaX1E4DbMjN9mZ6U1GLlGDpCvEep_uJZHbCmFMYeSf-w8EJae2kyu8ULTW52-M4CP9cVz1dL6sZgAhZR2QjxDPR5RUjf8i0phNzz2Utv0XqgSZzJfwfKc7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30923" target="_blank">📅 19:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0WfC8qyhtxy2sqmxR8Pv-b4KOm8pH6n8Oxg8uUreMlOeLHwz4VawtUEpYV701EfRc9PZlqGPjYb2vMBNKEGl2cPezxBSvmYaG4oEKADB7yTQfJE-zOAKCbYZlahGNevjiWLeEmpPvnxxYOZSqi_oE2cGaeYv2mQ5bVUm2GuMx7aXnjSDI0eM0FUkQlM2iP10SC-7qMRK4BK2uATbFGe-JlsBxIefhvlX9HVXaMRBzveeMkcW7U_cBH6ZQngT6YDhIk9Wl7EP35i1nY1H7eBiTRwOrgiry_5-7_zc5BuTYN7_QoOxEL0yK5J7FG9PAX8gxJwrAwqIlmb_n1kZDklmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30922" target="_blank">📅 19:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30920">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DweogSvLFb7ChwkEHh0VZgB_mtF5BXEiwV-UvLihNXpslCHjBTUpyHtsPRJeQe_VZPQoF5ORzsrEsgDIU6DQoe8Ad9kBGwtN1R8VfQL0ovSGuLoBJSUGBbQjeNwAf21pisCFdfAE9M2n8GygwJ_WSAOZzIkEnG1Ov7KxjNBeSD2InPkdlX6zIXqSCAyEc3BheS1GpWtkbrS99iAldIwM5Ul_0o_5KfLj18M8Oat_1jTHSxZJOsjF1iCi2-2nVIxq647zjqjCf8Lfang7tjsLqQUszGLPjQBgCH-q9GkM5qVHxMPgOz6VVh2OAFwEH-SE8eSnO14SdzFNpYJK8o2QlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVovmlomkxAikMb4wEOuVq1cZSDajsseE5By4nn-HAwVSu1GQcw1V7qDJzL1kie7Cy7g0RGs8qsqdFcBpCPXyi_m1jtLQVigojhMJPHr3U4yUI3yTAUecyGrJVmvHTOFRTogQPf0xaa8hUWnLx8C0niIgDbakhTp2MNHxawg9Dib1T0Z6gzE_y-LNu1zVFGN5_sitBEqEQ8_-KKH4zvcexaQrBXgawyzgQHRJIjD-0tr-9jD-lF057LZza0LhHDM-Uk4k9Wi4hZ4endf-iTa9oSlpBt7mvMxAjYt-GR6s3_s23gk3DtKeZ94AuRl9Q90pgCKM2nBW-tE1xFG70STEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشک و فیزیوتراپیست تیم‌ملی‌بانوان‌ایران؛ روز فیزیوتراپی رو هم به‌همه‌فیزیوتراپ عزیز تبریک میگیم که‌مشکل‌بازیکنان‌روسریع‌برطرف میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30920" target="_blank">📅 18:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30919">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWM4qy8yCfKLLJAv5QfaAzauN49noUNcqhdDKA7Bw05Oa8thqZQDEyEvKAkeagNqM4FHeGQFYYMvsGS7X8Dmd41qUIsuJR6-pGmXmZMUpDeg1JeXZqIMAru7N1KsbnJcHvWdpwP0kwG3t2OeadfINiYP8uEGQqqXMZ3juio-UbYmpNH1-u0VJ80w1WRqqh9PQBhHdAEHa_SFx9o8FKCmErnsjijX8XBgr6yFFmOgzKvjSt-DBEe6VDvdgKCkHhM0QO-bH5JJgaSiOuR3lyoGxdPrtrkPe5pKr6s1shjzb52DjQ5cuR5C9QJA9v0AvE-Guge1vVn59KDExSKWd8RPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
عملکرد خیره‌کننده و فوق العاده لیونل مسی در دو نیمه دوران حرفه‌ای خود در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30919" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30918">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1-GB3xgzaLkp1C_-8rIGlXHVL7mDcu5cXs9XRpkZrDMY8Xa9sO33XWrdJBhr6lHEDYg7Ui8_Myrt369mYTI_lmySQ86YKVeVughRKqvZ54u0AXid2lzb4AyDEPQ5b-QBR7muyQ7CSxP0DR2T4-HvWFKenAlPg1vsNHVFO3AcR2E02tNCENy7LVolKSbcXfBsw_oyEV2R5K3PgwJfBDE83wtK7bxSIOpANtJWQdrIle_sT5lu437BO55OrIDdr2_XY_4KPQbfvdryFJ_jG3IIH2bUPVtAaginL5x0cD7hH3tqxq4XWFQmYWKviYJggrYKZ-PYDBjCRu82W4r_hxmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی کره جنوبی در فینال مسابقات فوتبال بازی‌های آسیایی ناگویا یک بر صفر ژاپن رو شکست دادند و قهرمان این‌دوره از رقابت‌ها شد. دولت کره بازیکنان رو بابت قهرمانی از خدمت معاف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30918" target="_blank">📅 18:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8uDp62sxIWtPZQtHsKOMYPNdPY_aiROU_uILs_HOo_M2cWndX4pgREkgevbj_7Ws8XFdbbUstjBkAAvT9Qk_VV50bcAUB9ofK5iLwlCz7kFD46RY1E7PNqLo_R6eXpk_nDlkVuxRUL8gL9YWlMrroPwTWrKC317S1P4-_QgPwz77tFtSEGioqrOEWenrs6fTNLGeGqFfLXmfHSnIMN6VZamP-DdsNDcSU24ziRgrDtYD1aRvlgQ1syQksuYo6KV54QLKxWV824Y-nEvdkYqK6aKiKXlKSbzJt9nEYs6XnOz1GoEALtg-TI41zw3S0myE22g0AoR6ZhEACvlYvWbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فیفا باشگاه کایسری اسپور رو به دلیل فسخ قرارداد یکطرفه علی کریمی محکوم به پرداخت یک میلیون یورو به هافبک ایرانی سابق خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30916" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQumcjVySN44dPJW-pOCrmYGtGscLs0vkc2AQ3QIf1Sc-uI_rR8iAGJITAEvAvs6iqrieH2-jNHIajWHd0oFcwUQueZYPHPpQolLvYcN9SDi8eDuJemzWg9Es_1Fy6DZLpJ1w1lNpmEgiGp7Ol4BffAF14l2fY2u6FnuSplgmsNEXpkPj3FT-snGxw0NTqkWHwmrhLf0CaYlAHkU6O8FQ12_iynohgUkTHpRcxlXaoeP4PW5-TdY3VzwJrIw-JDg-D44hij9SFt5nv9cml7NtQOdFDROfrIPqP9ct9KSII6336luedQJc2gE2g_nLDAVotxTwlDV9yBNJ3cyhsfhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رائول آسنسیو مدافع رئال مادرید بدلیل مصدومیت تمام مسابقات رئال مادرید در سال 2026 رو از دست داد و از ابتدای سال 2027 به تمرینات گروهی شاگردان ژوزه مورینیو باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30915" target="_blank">📅 18:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30914">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6D2FDd3r2GuROi6YgGevNUHTCvhV6LA-SWp7IpYF9gQpm90MUwGcCFokwWoCuyMiMpRF2VEKI-0zkySrEOZQ6QJGimB5dW8nPk14i8PV6zllZ9ROJWqf4WFksZS7i6MLHKI-OU7zhzjXYvvJUB-3HFsRuFfyIL0oJYrIUza_TcHilrE9BoUzrhjmEabPXS755dcYLXvTPBbqHzDsCph61Q5sLLCzF1Qs0yDGHQl3efJIk95pyicrcMpXqUls8bf4F0WiGlBoBiT8fW5QuygpZX62jcf9gD8HcPlVZroNcuQEqShE7-Otw_oM6zvKtW7vv4Tv9m-Mp6N8Z_yBC9HAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دنیس اکرت مهاجم 28 ساله تیم ملی ایران از طریق مدیر برنامه‌ ایرانی خود علاقه‌اش رو برای عقدقرارداد با استقلال در نیم فصل اعلام کرده و درصورت تاییدیه سهراب بختیاری‌زاده احتمال آبی پوش شدن این مهاجم ایرانی الاصل بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30914" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30913">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0WeQps-oTp4msu4RZ3g4Djngnxqs3nmZ7i-M6YcjE0VrJQhIi1gwmsdjaxqsyVymYCTHWKGb0FGoa_sV7GGwgPbVZKi86167SvZ62bAhmXUw_zaC4Eu53LNcwkXjyy3v8qJtgx2SxT4eRu2AKwImUPHvB0uryla8pQya6F0QgIa2WEY32f9cX5X0Fs6BmC3y373Y4nJv4HsKVsC99L8q7v9vk9RC-N9XDVP1rPxOZmoMHdFt03i67uboq_Xt5VpROQuvBoC-WY1spEjtf2iK0qsCARdRNcKwxOfW01OE_MmFmi4nxRloi8Lf9US48cZDfVIlibRmZqLhT5s0ibo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه فلش بزنیم به این صحبت‌های تلخ ابوطالب حسینی درخصوص قیمت دلار در آذر 1404 یعنی کمتر از یکسال پیش + دیس به امیر مهدی ژوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30913" target="_blank">📅 17:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30912">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkLA1F5vX9ZEUgnHHFHZxTrLhYOpH97jzDb-T6plxD8mg6_W7I2ypmkdP50yzP9JcKAoEFqtxhRSuyjtxpI4clg0d2XpBWy0erzo7QiREqL6YGINyP03puqRWLTra586LzNPWQ6YjxMZXMV8GMQ9qiuPUSBA_8kazh65yR6qF8q2qhk8a0kDD4lWRkIZp6j06IiAW47IdO-3SdMgyo5VRRoiFc7LpO4-KWonmvXuJ_2ilztqUF25Be7MfCIr8dWCmEpxVi2JyTByE2mzJgEoFpCkQEE6qMMkU_mDY7Fo2xjIljlAO9Z13CALHPY4-nt_L6lPgDZi2gVlVIY659wsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هر ۳ جام‌جهانی‌که مسی فینالیست شده تو گل، پاس‌گل، دریبل، خلق‌موقعیت و پاس کلیدی نفر اول تیمش بوده.‌ توتاریخ فوتبال حتی یک بارش رو هم کسی نتونسته انجام بده چه برسه به سه بار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30912" target="_blank">📅 17:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30911">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dq2sqaWyQfW1MwJ_tigwfQE1mdxEGsSEnZcK0D4t4332LELzMn8H3A6etS4i4g2x34XkvEvQP-ft7_dN2yY2HEQ1pv84hTUVh8-UE25UZA1IyT-IWP1SDK2IDp57p0G0jVp6coYkgpyzEVeHLwtVcupKdUL1Wcuf1cvZ_QNXFMtRDs1WnvF6ka0C4Lja52s-RW3G_8WGITHN0fUrvEZKXAS0uNF-7pWmEuNTMWgTYzdo0oe8A953m6EdKgSvz55Ppq53fBkQbKjv_l0ZWYx5L8TLc9jCrmY1C4KXHAOzPoUNy0A37YRUkYBiS2akJ0t9RwFlMXQ1hDdUFMJ8_1FtLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
انتقام قهرمانی آسیایی از ژاپن گرفته شد! تیم ملی والیبال ایران امروز بابرتری سه بر یک مقابل تیم ملی ژاپن قهرمان بازی‌های آسیا شد و نوزدهمین مدال طلای کاروان ایران روبدست آوردند. البته گفتی است ژاپن با تیم دوم خود به این مسابقات اومده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30911" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30910">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=khAwQhFzBBjuwr99xtOOkmXJMUANdoflwNT275yh1na1WjeYpsfIai7vwM7r8Ise8dRU_F9U1qk6S8YOacs6gPMnWEujyvWhPtj4SbQa0UQpU7Bh_l1oruLJgHAER64xgLd1qyfdj3MI8Y9qZoWJ8vHAgDQFPnfGvueIGnfziTlr99yhIkgDlqQbseviCt-PmGkffqykBquKdC2m3gTIFY6cJHmOW-8RG4j1x4A6sgXxARKPqjrghkY324pkDbsGbiIsFjac7MPa40BElhyLkdN1X3TqcmDDHTbRzUZJ3_lPFYj2qOixip57MUVbsQkrPRZP_V1bVMPlqWaMeYU2_kqDU8EpW6cF02wPImnUdzn5gZ6oYoR4cX8SfndKZ1IzIxS6RfjQCLfa9QXsKFebolfLQh5aK8FmQVl_Vg4O68ZjtQ83fSPIYWbbOwi5LmU7EcmqSNO1R4rguU63CJpIxbWtlNycYnzChEtMWQG521bgsHO9VPg63D_mRnZ1SIFERGUHEr767G3Ni2-oFv82h_zOgxyzzl2zrWNJ7VYB1EhGDoInTt7uGND-N6LH6BT3xYxxBuSIUQoiIZiMhw4PP3n-KAtRSjefvuOZen7QcolIvc6Yua63k0xCGAh500fltptBrJ78j398HaaLRuamdEA7BDx39LMJhSHoMp21blo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8339ec657.mp4?token=khAwQhFzBBjuwr99xtOOkmXJMUANdoflwNT275yh1na1WjeYpsfIai7vwM7r8Ise8dRU_F9U1qk6S8YOacs6gPMnWEujyvWhPtj4SbQa0UQpU7Bh_l1oruLJgHAER64xgLd1qyfdj3MI8Y9qZoWJ8vHAgDQFPnfGvueIGnfziTlr99yhIkgDlqQbseviCt-PmGkffqykBquKdC2m3gTIFY6cJHmOW-8RG4j1x4A6sgXxARKPqjrghkY324pkDbsGbiIsFjac7MPa40BElhyLkdN1X3TqcmDDHTbRzUZJ3_lPFYj2qOixip57MUVbsQkrPRZP_V1bVMPlqWaMeYU2_kqDU8EpW6cF02wPImnUdzn5gZ6oYoR4cX8SfndKZ1IzIxS6RfjQCLfa9QXsKFebolfLQh5aK8FmQVl_Vg4O68ZjtQ83fSPIYWbbOwi5LmU7EcmqSNO1R4rguU63CJpIxbWtlNycYnzChEtMWQG521bgsHO9VPg63D_mRnZ1SIFERGUHEr767G3Ni2-oFv82h_zOgxyzzl2zrWNJ7VYB1EhGDoInTt7uGND-N6LH6BT3xYxxBuSIUQoiIZiMhw4PP3n-KAtRSjefvuOZen7QcolIvc6Yua63k0xCGAh500fltptBrJ78j398HaaLRuamdEA7BDx39LMJhSHoMp21blo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ امیر قلعه نویی به فدراسیون فوتبال تاکیدکرده که افشین‌قطبی بعنوان سرمربی تیم امید انتخاب بشه. درحالیکه جایگاه خودِقلعه‌نویی محکم نیست و ممکنه هر لحظه کودتا علیه او آغاز شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30910" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=MrSxYogKs4t8KGC_PweaZGD964e-VcvZdtDsFRDLOg5q4Kvv6lS8l3Bjrqn3MeDrU9_S_DjaU0dw8zrg67M8-xxOvad6GDpaZLhFPg9qOrVvcPjYvo62jXEeGKxcMWb6zFZaruRd-TpMk0uWxseFP9Q3Ik9F4G9Ogqga6JVy5MDkU2KaEwgm5kKTzzvT5CkS_cXyrp-LYP8cWQIvj3frX4IAwKKJIfEiZ9G4KWZBgcNXCBcEMZNgXLkpan06NgtoyKvyb7_Jqh4MMTfsI7KCF2ewER22ZslnGQeD5fmD00VP0vgP4sF_XuxTdOOMguDchp50n6jXM-sSBhcCHPTRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7722f37ae4.mp4?token=MrSxYogKs4t8KGC_PweaZGD964e-VcvZdtDsFRDLOg5q4Kvv6lS8l3Bjrqn3MeDrU9_S_DjaU0dw8zrg67M8-xxOvad6GDpaZLhFPg9qOrVvcPjYvo62jXEeGKxcMWb6zFZaruRd-TpMk0uWxseFP9Q3Ik9F4G9Ogqga6JVy5MDkU2KaEwgm5kKTzzvT5CkS_cXyrp-LYP8cWQIvj3frX4IAwKKJIfEiZ9G4KWZBgcNXCBcEMZNgXLkpan06NgtoyKvyb7_Jqh4MMTfsI7KCF2ewER22ZslnGQeD5fmD00VP0vgP4sF_XuxTdOOMguDchp50n6jXM-sSBhcCHPTRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30909" target="_blank">📅 15:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPXjS3-screPcT_BA3_QXO68FbQ7jYlmvtOBGP1faPQuMtAxPhUva1K4Wif7mByiR7F36DTrlCkx9YXm9jndmh4KMZjR9r6n-lswPxyV1AgylKkm4nU8zAXXlYN6vL9ic_9kPStD8cklTjsL-4i9I5F0d10BNETRHtr6sfayYr3mqyf-Wz6Gh-f2K8EaE8aIHJZrSUPWUVC5APa8gjJAimeEGgqktJO0AxZqzuIrDG__BGm-beYF_Dto017lnKtXMdcSppvRXBNcthUV-qlMVZkAIo7_hCv350Biwr_pg-LbDVjBpfQgQaRnAhRAL-fiPS9tcXKv9dLrRP90Swdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30908" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBbdqiH5_ZyoDOPZmqdXC_Mn6P3ZnX4F9lYwwVPLqbRMTlIRQgs8K-RaoBpY0e16ycvDm9tWc1yjDaSIJ2wRDWoax4fYk-zJhwGMUcIA4wr6vDI0l4WaBFxfyiMG_DnlYocNuM2pYIYcoUHZaJPKcv9hH4IhLFtDZ7l8B23pPj11tveWJhKp6wWeYUlUCwLn0VxQugzpgfWPoHNudGIbEzqLZjD5dEmNpW8N7VVeCHv1iqR_vxlLoum3Yoo_7Fsjdie_tMlOy7LbG5ntsbBfmoeluav-8mrO8sRAIcB1HyBA5P4qExnCqtlBlIm8PhDeXZYIhx8mp7XJT_NrqwIc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30907" target="_blank">📅 15:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwZfTLktQPixID14wBOXBCEx4kcL_lLAVH6TjA70T7pJkm-RxRN0RoUvhw_i6KMasehcObs7n_-4sOih8OrOlfx-49xDGIxDy4e5_GwkAaoox8DfGBdk_1CUO8eAQdkSg6N1FL9XHJr2Xzj_kdbeuwZbaSJVAwG4JI2tTGsbJIhWxs2y6IdreEkVPCMCnkhPkasX509DxO_rsiAlSFVGxs4ehSytLmlDLOsgjxAawuWVwodgz2bxGxTnJm3XePQWsDXL9u_btuYXP06MjCZAbHHfPTJd0-1O_34PIIQQJMtJZgUP4-MJuqotCS4yiqj9i1ijrw8STPI3deQib6r7Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ 10 گلزن برتر تاریخ مسابقات ملی؛ کریس‌رونالدو و لئومسی اول و دوم، علی‌آقا سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30906" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30905">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=L-YzA1Uq70VmemIsNH44qVTDWoQJakD4kNBe8pGXyEPP-Js9NknpFW_zz2f2eGfcsxRHsAsKPOsvY_lRa0zYrswHP6EJVhtxPVCrgHE8Lm9sS2puqKwO0D8rMIpYyB0QyFssBcHTvwZbs5ASRsAWml4O45hGf6AaDFGYTjOo-4sDpZI0MlLCncuKcqPEHrxEyluHpGaoY7tpSULSQH1FkJmFkNmFINcEfocqipYkpqS7sXPO8TYuhr32UE_811u8G1hAN254NB8TBPgnLSKHqZTG8MZXvKSVfu-VW5V9QCA0aw_ZIzUucjg_O0YX5gBayoqRrXxjjbggmT3VABSi4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e69e0420.mp4?token=L-YzA1Uq70VmemIsNH44qVTDWoQJakD4kNBe8pGXyEPP-Js9NknpFW_zz2f2eGfcsxRHsAsKPOsvY_lRa0zYrswHP6EJVhtxPVCrgHE8Lm9sS2puqKwO0D8rMIpYyB0QyFssBcHTvwZbs5ASRsAWml4O45hGf6AaDFGYTjOo-4sDpZI0MlLCncuKcqPEHrxEyluHpGaoY7tpSULSQH1FkJmFkNmFINcEfocqipYkpqS7sXPO8TYuhr32UE_811u8G1hAN254NB8TBPgnLSKHqZTG8MZXvKSVfu-VW5V9QCA0aw_ZIzUucjg_O0YX5gBayoqRrXxjjbggmT3VABSi4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح بعد از پیروزی مهم آذر پیرا مقابل یوشیدا از ژاپن‌هادی‌عامل‌حواسش‌نبود میکروفونش بازه و گفت: ببین یوشیدا با همین خستگیش حسن یزدانی رو چیکار بکنه تو جهانی اگه بخوره بهش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30905" target="_blank">📅 14:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aosl_G5K7FFchDQWhsmMb7fkjUvU0f-2GrWdDs4Ori67PJt7XkrwZTOE_2-njji1Jv6H80_ToscMs8s9dkToTsgDe7lTMcWemuddlGCYzvYKEv2z3kMUe8Zdh-woa5vE9KNM_D0f7YLL1JhYW93g1VH4vI-c1letKB9CpwAHoxRemv_z7PfZQxvGsU__zUQXbOo6gUy7EvnOSr-qK4XmMSpuroih6TLxYgDhsLovaELxofXO4vfwRGPwSusBYMe5_rUzFKQXfaQzFu3aRyY4et95O-QyA70xRw5LHzkidrMTpxn2-JuSGz27afWEvSLEbBuZV6CInJmcTxgK9RcUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌‌های خارجی معتبر پنج گلزن تاریخ رقابت‌ های ملی رو اعلام کرده‌اند که علی آقا دایی اسطوره فوتبال ایران در رتبه‌سوم این لیست قرار داره و تنها کریس رونالدو و لئو مسی بالاتر از او قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30903" target="_blank">📅 14:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntkid2-4bzvmGgvLaYdtQyeCK94NvCbdORL3PPg45O5rX37D6Neh-gSO7Wi0N1m4jS9HTPCnXkjmb1roPsnwEtxewmP-V5vzoA2i-MonmSVhYSP7va5gcUR-n2acdEbsUUX6IJYi0TYDUjfcabjWGuP2lSQvNjrMyuzddgvGnFsUzilBo3l72F5-IMAGjiISeEcZbsU32dnsWqphwudEuVducdYoJAoSyGjCPCEXN_ddtTWj5BLN8uVMi1XxLWyYoaLEgvW2f7LwHZPERXIakCvabfaPK01Qt3pQYxVGlL3nzqVPWhX2afLoloHX25TtlN2_OtftpLIc6SKcsNpcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلای آرین پایان تکواندو ایران در ناگویا؛ سلیمی در فینال وزن 80+ کیلوگرم تکواندو بازی‌‌های آسیایی ناگویا طی‌دو راندمقابل‌مارات ماولونوف از ازبکستان به پیروزی رسید و مدال طلا را بر گردن آویخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30902" target="_blank">📅 13:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLv7Gjo5blS_euyFWldMBUgAzEV0XdaymjR2bkR65N-lpdwud14r7TDZ1BKXowJ10zRp5zO3BNgIfqMPPg-XFtZ2vowJYB-DRKkTprF73-i9kkJvjT8NVZ7zpnSaXKdT1tuYJhHO7i_Z7zespSOenv1PdHPrW1Ay293tO7HkY9vg2cqPvZomGlQdI6tJxVI1CmM4jLS7SGWbPu5i2DUQRrxuGfYufF7tgKC6FId67B1Bv8YLVYQN4EzXN1R5anVfxKLyDbM8wixGDeK6yau2LBk9yegYgqCJyWozYVcpx3mY0SrRLcIV-EXo-K-Bk5Cc0Tv0eFkNubQgrJBWxB2Xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال سرمربیگری تیم ملی امید رو به افشین قطبی سرمربی سابق پرسپولیس و فولاد خوزستان پیشنهاد داده و درصورت موافقت قطبی ایشان بعدِ سال‌ها دوباره به ایران باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30901" target="_blank">📅 13:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYv7FDgHgaJqoM7vCgHdEalSJnT5JzXRp5wzYIcAxRV04-Nz4rMQhsnMjDB_DHGOyHihV90E0cQPRpTStzSyw_3DZLu2s6r18-5v_b4wgS0JbIxwulO6tTNMl78bDmvEL8x3GOVKYv_Z6fj-QzBKDwBTKzORD2WazFZEDAtwKZTRF4YrXtH1rEhkK3jpzXG6Yje-Ea0Xe5XMNxxJRWJb8junCdhy2yDY3jClHwgmAQA1yGB9CG2r4y3cYklDq4IRPSx98WX3KTZUwOfiCKtnuvOV8iWorQvAYoP8hW-VYPmTDvZCv1BvJr4vkZ8sAx0Acps0O8nRHD-fPLYVs8BTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قیمت‌پلی‌استیشن‌پنج پرو تو دیجیکالا به 345 میلیون تومن ناقابل رسید. خرید یه کنسول بازی هم برای خیلی از جوانان ایرانی آرزو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30900" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30899">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyyJ4Lyvp9xCxkfMHJzZHxSAVmdDzeuwaeOmLhUwsaUmwqtnloGEk_SphP2HQX1D7zJa_KSON2twBFfNxLrX4r864ug7mMvXIQpCBl68J7j1zW9vI2FnArC3lA0C1PaCAsRkFY625otkQyIM0fWnoa7ZIXpufk1XrKf2cUwsIzG07qvQUA-2vtE7iPie8CqQ6z4mcBxMXnAYl8TgW-LRnsS9WcsXehLPMwlSTw-QFjPXDQSgE61cQzvH3d1nQLxfuZiD1prc7l0eohbfKXX31GTSSiE6CadDsHrPAyqSWCsjRjPZlvVEDFOkhpttxV0xF0hP6bghCpIYY8Vx_E4amQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل خاطره انگیز و تماشایی زلاتان ابراهیمووویچ ستاره سابق تیم ملی سوئد به ایتالیا در یورو 2004
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30899" target="_blank">📅 12:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
حسین ابرقویی نژاد بازیکن جدید پرسپولیس: باعث‌افتخارم‌است که هم در لیست کارتال بودم و هم هاشمیان. تلاش میکنم بهترین عماکردم را نشان دهد.
🔴
از بچگی پرسپولیسی بودم. مثل آرین سلیمی که همه اهدافش را نوشته بود سال 98 تمام آرزوهایم را نوشتم که آخرینش پوشیدن پیراهن…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30897" target="_blank">📅 12:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBFS7JoXzzHo9-L4FN-XYH1hQm4ltJpEt_AmMApGcH4lSZBbSefcGTDArnsU98aCwl8Qk6-i3yC6LBs09rb2gsZ95kChAxwMATJTE68zmYuEMZdLjJKrf2KYA7Cuq_FIrp97twZGzjU8pJRqGvjEVxk7WNxu5FosWJGpZWxw4qMOyYiZ58n5R-nHCKBgClsBnIFvoMH9lSrlpdIeNSh4fGZHZvT64y78tc69dInLgASBFZgk0xONoOoeQ489WFJPWVUJADe5KQUQmeVwLoM1WqpoGRHRUIWf3cnsV2ED1GcZfk0deKTO8hSdPq8Pq6GpJPnieWTr9HbjiSdl5hDtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیرعامل باشگاه تراکتورتبریز عصرامروز با علی‌ کریمی برای‌پیوستن به این تیم جلسه خواهد داشت تا درصورت توافق نهایی هافبک سابق سپاهان و استقلال شاگرد نکونام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30896" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=sp3UpxBs-ZwxpqMId69yi2XJE4Nry7-Dmbwyp4csmYJuyWJDxuU3ooixGKx8f-McGF0pAC0L8DDacGETCZ2Ip_gEf1Gcaw_86Cnbs4y2a5sK2wiThoLbAiK3ViJE0wgLcaoyCn6ueZ5Ta1GDGFnM2c9fZ4pEf7r12h59w0TpG7nAarmYkIlxIp3oTBtFDIzeifVgfVPMtyPNYKAU2Mg6UJ8ujiuXkIjQ9wvIc3i4uF_D4VAIqqhECuC94tVInq4pFhfumrkJOi_KQh_EsGWSFSn9a7wxphojP5ehUamsvraGwxwui9I7EiduvrnCvM6b4QnqdF88T1DHA9OQc83I2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a63af919e.mp4?token=sp3UpxBs-ZwxpqMId69yi2XJE4Nry7-Dmbwyp4csmYJuyWJDxuU3ooixGKx8f-McGF0pAC0L8DDacGETCZ2Ip_gEf1Gcaw_86Cnbs4y2a5sK2wiThoLbAiK3ViJE0wgLcaoyCn6ueZ5Ta1GDGFnM2c9fZ4pEf7r12h59w0TpG7nAarmYkIlxIp3oTBtFDIzeifVgfVPMtyPNYKAU2Mg6UJ8ujiuXkIjQ9wvIc3i4uF_D4VAIqqhECuC94tVInq4pFhfumrkJOi_KQh_EsGWSFSn9a7wxphojP5ehUamsvraGwxwui9I7EiduvrnCvM6b4QnqdF88T1DHA9OQc83I2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ درواکنش به‌خروج کریستیانو رونالدو از اردوی تیم‌ملی‌پرتغال از رفتار او انتقاد کرد و گفت: نباید میراثی را که ساخته‌ای با غرورت خراب کنی. اینکه بدون صحبت با هم‌تیمی‌هایت اردوی تیم ملی پرتغال را ترک کنی، بی‌احترامی بزرگ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30895" target="_blank">📅 10:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOCjSxhzj2AYNa4GKTe6h3doDkQqDZ2z6-vXPQU6KD2UUZoVRZydnSs0e4lV0pFEiwWbz5gPNQBl6fw7OZPJcarNT4HCu4P939a8KePmItzBWM1oVj-3OFOLLl-VcptiYTw24qK0oDRGs4Z9jFHpPs4nNPzsboTJBxRzEYhWT3baVWPgiHYPg_JuflMc3BpeBU5dBlWp7ohkYYWH4WZUN7aRDbZy_Nl5MGPGPwlT5nFt3amRpoV41LdvnOffsUaiN0gCDdcJ2Ji0AIjko52n-Ei7zFTmcBkiQQoikRCe9UQdnTQdMoN08BruYwIoJe0L3WvDqKu21CM6KXEe29_gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30894" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbYJKBiinIIqMcJrMb173ze2s-kslZKgpQM-KWVsVi3cGoN8SierOS0TIBl4cVxn8lVveUOXgsKtq82MoHHa-FGXtjqkzA_njxsHmn4CMM9o-k5PnTR0bpDHXG3lHZTut3HDQINnDwwv-17BGvQo4rN2l6i3yCmLDKFKhYtswAuIUZnaKbIj7wuVAZG3Z7Du5po7SPWre8HguV6O8yRcO0jYhDihb9mJC-EBMwpQGREqFYRp6iYktl0oTXKkmYzBojyxZhb0Nbh_SoJ-IHOk5dUcXI-M1McNpaeFVcHlgw4mEZqizUf5cMygHvaAiu9hJ1L0iYachZxN-b6c1jqT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه
آاس:
رئال مادرید توگزارش شکایت‌اش از بارسا به یوفاگفته بایدتمام جام هاشون از سال 2001 تا 2018 ازشون گرفته بشه. بارسا تواین‌مدت 9 لالیگا برده که تو همشون‌رئال دوم‌شده و اگه این پرونده به نتیجه برسه 9 قهرمانی لیگ به رئال اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30893" target="_blank">📅 10:36 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
