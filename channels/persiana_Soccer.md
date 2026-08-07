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
<img src="https://cdn4.telesco.pe/file/ggOCrvNvDE5j0DMB5dGuqTehws0INAGFDQKvzlvr67gNyIls9BuZo_s5-JRQnFqhxBG4eZo0SC8tvW4fxfQllPY-oeM6M_e5GwOTJPbd0Vh7abXwM1cpHeVkkJRNAp_1JhisvWg-Aq4KhcAr5oTY-yblDX-JIECAm3r_Ix_X0LLnC3XrqMd5NztkuXYk9Pcrls6CBnABviY2zmWKEWXt2Vd7Np6D9n5kTFWn3hC8YkujL_u5lAq7qOYRo15wE3DZs14nfNLj3z4_S7f1bObrkU7o2_YEMrwSCGT7YU7OIeEKd9Xs3JWaLf4STPEwauXMUs5UDTJqUjOYPbWsYx3vxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 641K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 00:00:40</div>
<hr>

<div class="tg-post" id="msg-27295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198183711e.mp4?token=g_md-SH3WbwLYYgZzMhhWlRdxCWvTZt-DGOISQLcSb2rEJv8hQwzo7cpA_ZFGj66jGJmv3oqzXmcz49nzDkqWzjUe2P8ZRyXC_t_DaJiVvOaQyi9AMs2gIzLWToLKQ41ZgXMd57JLL0DlW9KsaZUyXupE_E805AwfNCpeps8JsqI2kmnZ2CXsU0rkF7czT9DzlYy_saE96J5WSLjKVM0TljEP4gRzVjST_f9IFkyIh00WyVgvOubwfLIw_g-bT-kMfsIZPFcnoIF0DMkMH-JaNK76ket32a9yIaNe8a3u9KRkMYAr30jPovXk0DiLlsvetEq8aumhiE6YkB2B0Mqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198183711e.mp4?token=g_md-SH3WbwLYYgZzMhhWlRdxCWvTZt-DGOISQLcSb2rEJv8hQwzo7cpA_ZFGj66jGJmv3oqzXmcz49nzDkqWzjUe2P8ZRyXC_t_DaJiVvOaQyi9AMs2gIzLWToLKQ41ZgXMd57JLL0DlW9KsaZUyXupE_E805AwfNCpeps8JsqI2kmnZ2CXsU0rkF7czT9DzlYy_saE96J5WSLjKVM0TljEP4gRzVjST_f9IFkyIh00WyVgvOubwfLIw_g-bT-kMfsIZPFcnoIF0DMkMH-JaNK76ket32a9yIaNe8a3u9KRkMYAr30jPovXk0DiLlsvetEq8aumhiE6YkB2B0Mqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برسی ثروت و دارایی برگ ریزون مایکل جردن فوق‌ستاره سابق تیم ملی بستکبال آمریکا و NBM
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/27295" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBRe0Th6xY2jzLv8GKborvFRPrN3nXt0eUS5MZoC2QrUyuhJn1hs4Kh5E_cB8IkhT0c-cMUeTQ9fa8v6LnCcdDN8ebm25bq4YRUpA9UtNscOcvC0tqNzOgnbK16OesBcddLj9cWNvg6uWRrgU2pnmwblMP48IOsUpMmvlU4yaj3bbYvDqYaoulZLb4ho09nVOn-h4DsIT_dcQJORYynPPpMR-sQyTc9Tb6-OTt8olUejFXrxijsTfPENkMXmaUmxgXRsDDsSxARrP-Ved9sZOl0ccG56sf7BqQX8Smd_kYvk92ySjfMaK3HqEcnkxCOCPBqWwQVtyF8Gm1rwGFi15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ هانسی‌فلیک ظرف‌دوسال حضور در باشگاه بارسلونا 55 میلیون یورو کمتر از مورینیویی که فقط دو ماه است به تیم رئال آمده هزینه کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/27294" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcL8HdNatJgKKtlPJm6xYNeADQ9-GTJTcd1ZD1bwrTm80wsGFRo5JGsnUtWnrXiGuFE8MWusqfUMP128G-uMv4jZW_Imr5PVRzZcWXIQPvxEsxeesRR3S9M7Trd-RvTfwoNqXPEPsi0daitNVAxeP3vc9dJNOSJivZcuUqUCFILqUXAbpSf5JnqY4W0AyKYeI-kmdpNvpojDdgGZoa2I7rRPqaILS36HAaW-rBniSJK_G_H96kIJjHhDQK4_9g5lDdKDWdGIBeCj6i6HbhSlfyr_BBnzGHrmHXYLrlkhCmeuezCSYK9L8lY3Wk09zVykSFR2EJ1HCQbwj45gLXp0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/27293" target="_blank">📅 23:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz_DOJyxk4PfQdAfkl6QKvryQ9utqTumdMIst-7fSecE_uf2me_XbU8izTsKNV-Dc_BEFvRtRf2RvcPsVFGrNnUcvUmJKK-IrLDCaDPRrsb0-4g21S4vhhHdhRKgdIV9vJWHGZmqH9uHUy9rWglqQizpNbqGqFZZ7Zj740VoSB7T-iUOuHs_453Xqo_Ci_QWk3NgGsJRWqnKIfMy5hP6NTOdhrN0rouaf-LiJK5J6YygpCFyboWR6GlihwgpwrfHc9t-HByiDWoMSVEQxgOgBVG_K8NSjukbfS2gSnTmvSZn-ZhbO7Jt0GVSm7BULBOduM6UwqYjPdWeCWbuRzdgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛
احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/27292" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdzu7M9uvLJnNcEHYBhqAVGAd4RZvQPIaV2oUpTA5PSAu9xfDJQ1iUahW-57oqlVcLCQOidE9SOXsRWrMWkGa4uDvvKucpl9K7mbPb3PBbdZ5HyNG5jePpqZGyTyOU-gfoavfiaAXLNWBk39oQ-Q9Rnl0NLqO7l9tXGTatb4z039SM_YxagU4iS0lFUCgyBXly8n2CyL_NWZxSsROMDeEGOOa7Va8kYXIZVWoF9Ge22JUSysfb6xgDMvX184JPJlfi3diEbt58N-UgfZWXb728JfVvL4Zu-7PgGhIBU8UtBwfokOTTqI3JpVCumVzkVhgW2Y5j7xmV5KtbCWEHwb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/27291" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6EliXihIS2wt4YewWS4im7xYtNyAQivKkME3rvD0px-3czZTRY1HuGDrkm2pzSrKuSSv2o5Ax3YNCkYMRLIJIc6dtOi8MFq1P4Gm-JDNSPAxCRkb_OzSQQ_413E3DfU2mzfWhi-QYGTH5JZcu7CLrEWOZiN1SoDSj5SUXnwRjUGTd82jGTZyiUf_1P6S1AxOaNmZ7_kl24KSr6cnuI4wd4JN4HF5q_yf5uTBaCrYZrdgnwowrhScFInyTiz4QVm5NFXg_Hoq-nk0yGpJ_coJXfoYd98fKfzdrmNDmYumcipvvsdU7veZdSyS3D08mogotk7onbiwznvzp46aaZOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیو آدان زمانی که تازه به استقلال اومده بود با الحدادی زیاد حرف‌زد تااو رو راضی به پیوستن به استقلال کنه حالا مدیریت به آدان گفته‌‌ اند بار دیگر تلاشش رو بکار ببره و با منیر و همسرش صحبت کنه تا شاید آن‌ها برای بازگشت به استقلال راضی شوند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27290" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiRaQxfWOWLJ7HROpKL5eggDbB06CUahRl12gx9MLHUtZnxs1nDPB3p1PUrngOjShXNMhCLzxHzkcqR7qC8xs37afoJGr3GoIdcetAdvrSw3z_8k36XTuQ17j5bTmKFUzogYgYi8puI1O23jOrIliL0AgTz3J1VuzNLmpJiTROhRWXeX6UB6gQni43YMpsvRFtRBHzeeMt3mpy7x9jbbF53dBGJZ8cr0_FrMmFfrJsMxw4hAzlqZz-ZxPcxGVBVYNpDfZvusPxPdVolILhNS9cqtJTPhBqSi7bn6P5bPlqv2kJcf-RfJVDdPbvTVoS7kIoKQ-g3lxPNxOqSqR8L1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
به صلاح دید کادر فنی سرخپوشان؛ مجتبی فخریان و محمد حسین صادقی از لیست پرسپولیس برای دیدارفردامقابل آلومینیوم اراک خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/27289" target="_blank">📅 21:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRtPnNedkICph0YH92bROFtbH45Yj95DADK9b7ZuOM0iD59xIbzmE6uognW-7WBrd3u6vmuNHoE3iBjns2xW79IiK8snAu1OyZSk6P81Y5Hfo3w7L4qA45nZ3r3JKuYpCsxJgWmv_HXpoyDHZGad3syF01BlEc2NxlHijfRtJYn_x9p8SlgF7qdMj523L-ww4HmEV8QdttRTygvDvIddJliLzpTj7KViwXB_UYcuFM7pv56Vr_IEI8lgLxj8pdixNnXglpclakRwB9OFYbgCo7t7b6gCn_1D-veJJzVQzm7QTbYZpv5JCc8pK10QbgJset6LYdfKB_1kbelVIvrnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/27288" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3BoeZoeSMj9FGESKFAPIyQ1Da3kfYMtHOCff9Z-YVIg0k3v_QcK5f-3gsJrUa0mqfEpotl4QjCik106RuieGUH8iBwvRVpVFDBz6huirKHaQloLITe1-OxlndVBcKH3NXnqjNvHy4n57PIe2_IfW5725Q4tcQMpfvxojuZrbD9w_8b3V6Tw538kWn8DbbGh9Vp_UU2WYPzspfj_rAbNl-mS30pRBtiu6TyeDv3bXEmsDFNdqghDHGk0GtzR2Ttf288XQb3Cwxl8S-0nNgKfNFaJGldG1TUg7dBaLINplfLkkmn7OCx6VK0CUl3T8DQzo-Cd5NWgSw7vr9TjPCJnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/27287" target="_blank">📅 21:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqSkewNppa4kDS0QpVHd5jFBL8cAIyXyLFgTl3g7Xy7uzFoiHjqEZ5aNmtCygq5yJfErc9F4SyqL9SLJUya56WcQBR5SejE4Vfus7K71RZBPm9N7GSlC-YcF_GFUfvmUmi34oZGPNq4cbJD2i9oYslrcZBB9AcIMv8xlnWRaFSGUnrgsgT29dpgpsKgYNZy96HUq-ulEwY9T46_SxwIZyLbMnvEKWrRvAPZmqkla0uso_zQ0jDU_rzbwtexX4961r3mJr2VvoUOjRfp-m_4dm6hLYJ9VX0I9SLDaijlixn-Xdwj8JEq4qfmy0uZKkGRTu6XxQgCPEupkSXd8qzunCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/27286" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiwbXNXy6RS9lbmokLDE99Y74kHiITvVxOSgyMp1ac_Ve31VxWbf7Mk03M4qcuYwzs6HA31uD9BwiKeX4ceIiF5gl_iL2SjBBluLOJpukx9NQcZkeREin1nSqzh0TiRa3SOJsk73QqW0DZ3yEc0J3_bz3aNu47FdAOrkzgZEvp_N3av6faaB4ivQg7KYEugSX8OMRsEQGDKGcXqorK7zfg9q8oFqD-EDobjQp3SS-uZWubOkC4cSomaGpmfnDPnqCW0n9S1WOlp-hNfAwjrQYBBMutIJpeq8Vj46RwWCzr4LeuNl-sEKJOQUPeV8PoPKoOvf_-rPMJ_Hig8OZaE_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/27285" target="_blank">📅 20:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-YVOyyqXEtlHYXJh10essL3ag7Pxge4vyGlwZCYx98PIzPW2asuayxgGlLnabkTGMDUOK585gnKCIAs43K-bttdMthsI4BUiNs7zEW0caQPtbbQZdyYXjWlTEz9EFIGPaTtCy03TTBGjdL5vZ0aJiPEHAAujuD_gFb82PtUwXpsofX3-41vFGRZAX9VixTbg4YCwJocCkh4uxZVgsx-CA7fmxI8t7O0358SrpaWokagV3jTYBgBdWhr8L2b2rKpvmM6Gvsu99WufAdzEKwyPuGJ7c4vIiz_hRxfDKSnJkMUYiJbx_gJMvOIXUi6xtmtGvhpm6ZNC2p0JFTkNtfLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ آنتونیو آدان موافقت خود را برای بازگشت به استقلال به‌مدیریت‌آبی‌هااعلام کرده و این گلر اسپانیایی بزودی به جمع آبی‌ها باز خواهد گشت. باشگاه در تلاشه تا نازون و جنپو رو نیز برگردونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/27284" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=q79jF34C8q_nYIV4QDhoqrpW2D0KdZROx0Q0UARNOQzvJLcOCTjIr0qxkP7K0ZPqj2K7M6yoqvg1kHEecdAjGEe8CKdeeBhI5-NgFhDYb8BJG4BHrf6Vf0QY-eplXMklscStZK3LWPF3o8GRvGkU5-7Sgq10s25Y4km9WDHZImDpanLyJQArQeHaOyoY1LB-uQmtR0zC-R5DBwHDaFSmKzq2SODDvXfrVVszGpbwZRZ3PmWwqdqc1zM1qCps9N8Xh1mYUKz1hJtzfay2QjER1wDPBYzK84MTvsxmipkut32QKdwdK7Xqu_IljApstz7XA5vRJ_G_utZ1brgEW16kiFFPld9zEKVtuyn0s7nNzJvgjZ5BZ2ZAxvJQC656PMW2330ucYtpbhBnEjZw9k5o7Xh3gi_XfRqrT5Imp_KtIA0Gl6jGKlKNcU4ud9ErT96ZcWjP3HWl80wV322EZSt88ndL5e_w9SbWpcSLpo3t6OUS-CiDSXdA-TR4FzhA8p4gVXLSVV7ElBySAS2gHpPeui-64hHDF5bTsYHJXBE0v4-_Z7sxHeJGHC2meYxjIUwLbM48oh1NIgTYcMdwqYjI-1QpBNVfi_DqcXACgqWgCg1TS-FkvZR4MiFIqnSUCnhXlbLC2HjPt2GxOgZooVoZlasWmALSU6WvUWp2Wl2S3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=q79jF34C8q_nYIV4QDhoqrpW2D0KdZROx0Q0UARNOQzvJLcOCTjIr0qxkP7K0ZPqj2K7M6yoqvg1kHEecdAjGEe8CKdeeBhI5-NgFhDYb8BJG4BHrf6Vf0QY-eplXMklscStZK3LWPF3o8GRvGkU5-7Sgq10s25Y4km9WDHZImDpanLyJQArQeHaOyoY1LB-uQmtR0zC-R5DBwHDaFSmKzq2SODDvXfrVVszGpbwZRZ3PmWwqdqc1zM1qCps9N8Xh1mYUKz1hJtzfay2QjER1wDPBYzK84MTvsxmipkut32QKdwdK7Xqu_IljApstz7XA5vRJ_G_utZ1brgEW16kiFFPld9zEKVtuyn0s7nNzJvgjZ5BZ2ZAxvJQC656PMW2330ucYtpbhBnEjZw9k5o7Xh3gi_XfRqrT5Imp_KtIA0Gl6jGKlKNcU4ud9ErT96ZcWjP3HWl80wV322EZSt88ndL5e_w9SbWpcSLpo3t6OUS-CiDSXdA-TR4FzhA8p4gVXLSVV7ElBySAS2gHpPeui-64hHDF5bTsYHJXBE0v4-_Z7sxHeJGHC2meYxjIUwLbM48oh1NIgTYcMdwqYjI-1QpBNVfi_DqcXACgqWgCg1TS-FkvZR4MiFIqnSUCnhXlbLC2HjPt2GxOgZooVoZlasWmALSU6WvUWp2Wl2S3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمیدمعصومی‌نژاد خبرنگارسابق صداوسیما هم فهمیده که نون تو فضای مجازی و ویو گرفتنه؛ حالا ببینید چه ویدیویی گرفته از مردم شهر رمِ ایتالیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/27283" target="_blank">📅 19:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9ZVe9sdW5JQFuVGX5LO_lof_lF7cZ-YJxRn9WzzazhYbbT4xYJwl810NnhKOF4x0o83JMwFGJUw1dSxRYJ1M_O3Ha5RpOgtAd6R_7r_OrWC2nT1sBdxYD_c4CFSGk-CvPQk4jSYvDUii5XXaQ9ufWlldPilv91W6FcMZKEP05OuAilxUTaMni2dTTSxW4TrZgIXJalVPQpVRMG_64bD8d5Q48-wqC0Pdp7eHljLKW7iI5a-ebQjhXjXfjHSVFXM8iPj-XkOxh2dVdAc7sKdkfFR_lkukz0grJ9_ddC0J5lmKZwMWbLFRR8NN9OPCeIk4N75dve7Cu8zqMBzlwz7sOx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9ZVe9sdW5JQFuVGX5LO_lof_lF7cZ-YJxRn9WzzazhYbbT4xYJwl810NnhKOF4x0o83JMwFGJUw1dSxRYJ1M_O3Ha5RpOgtAd6R_7r_OrWC2nT1sBdxYD_c4CFSGk-CvPQk4jSYvDUii5XXaQ9ufWlldPilv91W6FcMZKEP05OuAilxUTaMni2dTTSxW4TrZgIXJalVPQpVRMG_64bD8d5Q48-wqC0Pdp7eHljLKW7iI5a-ebQjhXjXfjHSVFXM8iPj-XkOxh2dVdAc7sKdkfFR_lkukz0grJ9_ddC0J5lmKZwMWbLFRR8NN9OPCeIk4N75dve7Cu8zqMBzlwz7sOx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خون ‌دماغ شدن شرکت‌کننده زیر فشار؛
اتفاق غیرمنتظره در جریان یکی از آیتم‌های فینال «مردان آهنین» درجریان‌یکی‌ازآیتم‌های برنامه مردان آهنین، یکی از شرکت‌کنندگان در اجرای حرکت دچار خون‌ دماغ شد؛ اتفاقی که برای لحظاتی روند مسابقه را تحت‌تأثیرقرارداد بطوریکه از ادامه رقابت بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/27282" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRun6J75UFSWoFQQPWlwwuLcOxPirzSypGpbz-0g-d9jYWzOVcYBSDUnxEk9IEsd6I65VbjFxhgmpwnniUYEB2NzwhMxOzKIWmt7gSN1AEL54oRoT9jQQB553XGBGQ4YmpjLFv00ioiiaGf5D-eI9PNBmb2ZWWvNcPGIgQhHCBzcUBQiWDFsFA5XK-PSezVJZavT_Dv_exyA7ZdrHEdbVZntZQdAEKuf8Ax9qeIgCP5TPGgDRrKdAh0VejfGaQsEGvWE-WF-bjO_yvG1I55i_0np6jmIzSI81ko1PM21kMddaHYYD7R1p-AMn24KnROa78pbikTQ_8ogRppDzm6LUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27281" target="_blank">📅 19:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335a6e2e8f.mp4?token=iTBl0mD6f4oWYKhI47JER3uk-kGQpcWaWx9R66c8QmJ0S9P7WyvTHzXusQxgJwGdnrHIIfC5PTwXhJWrnkwu6xn_sdcrjDYv3B-nc4AF8GYTDVMeqwov1FH3d0yYgKjyFy_DeXyGoElCjIjgfEW3I_5Cwyt5cc_YsXwo2-gsjsiGPjTakUajWJRDMUH6eUsPRMe5NkAWdi2Fc4NpU2NjfUMEw-hVJv_1vju6rPCM18qABTMfOTMPnfgXkI3-cA-U1Vlq0ImibJYp4PyPM68NhOJ0iP-fMK8cSGP6P20awJSr4ZUBINx-B8icLFI3MdCM0sBATM4dAvLQEHOXqKdCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335a6e2e8f.mp4?token=iTBl0mD6f4oWYKhI47JER3uk-kGQpcWaWx9R66c8QmJ0S9P7WyvTHzXusQxgJwGdnrHIIfC5PTwXhJWrnkwu6xn_sdcrjDYv3B-nc4AF8GYTDVMeqwov1FH3d0yYgKjyFy_DeXyGoElCjIjgfEW3I_5Cwyt5cc_YsXwo2-gsjsiGPjTakUajWJRDMUH6eUsPRMe5NkAWdi2Fc4NpU2NjfUMEw-hVJv_1vju6rPCM18qABTMfOTMPnfgXkI3-cA-U1Vlq0ImibJYp4PyPM68NhOJ0iP-fMK8cSGP6P20awJSr4ZUBINx-B8icLFI3MdCM0sBATM4dAvLQEHOXqKdCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27280" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx-bFgFBHXDFZQvDtcv9iWgBBBJ0Uc3KMFGO1Tkqjep3uGtFKsK_gQWxSt_IsSbELesxBJb3M16QqWoWg0GoPUP-_ElAnm-u0WUHCe4JuPAGYJVPLS3fPDKXvWlrNoOUBNhHbdklH4GTME1H8bm4B0OWgoyvo3XLRNTQ6qY6v4q3lSSpweMx2oTNoPDIUQy2fqc4GEd1Gbrbv5Q92cRY0vUHPkpdJlLzy4jVyhGT4yVfqbC1uph3w8SHGv69fv-aSMzNKLXqyuHkV8wRC-uA2AL250WvGc4kImEvRhelo6Y1NHzfd2eHxUr-5vx0ijikwX_3iO6p13PEvgXHxSRCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/27279" target="_blank">📅 18:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcLEaK-BDCP42Han_ZcVJc5QR_EuaGcZC5BBMp4I5Hnd9qLPo77Cyy6DTvgzeIJfXr-5u34kSV9LL_CiJTq-_zWwrrUU3R1NlD8RwkLzQg3WL5G6hIgRKM28IC5E50Z0INMJUAMM-dDMJIrDKU6Qfm6AXctFB4_yS2808fsPBUgETZA2rHiXhzvXU3FBFfkrQAl6Hns4s2gfkoSW4KtpyPLVWQo5Uh2pDM_Dp_kOpc1FDawxpb8-0CcFsIQapBfv8cGxky5CANYblGzuzJwtbTnyBpHBQqP8dWciNUBkadb6IqlavYLICC8LGNAkK-An0dEGJ6vXSlr83YgDOO0xTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار امروزظهر درتماس تلفنی با پیمان حدادی مدیر عامل پرسپولیس بار دیگر تاکید ویژه‌ ای روجذب دانیال‌ایری داشته و به حدادی اعلام کرده که هرچه‌ زودتر رقم رضایت‌نامه این بازیکن رو به باشگاه نساجی پرداخت کنه و ایری رو به پرسپولیس بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27278" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZDWptqnEjfojfm0lezkw92-KgqYQJTCL_FlFkOAjERB08_p5MyJdHr0JIMk0bwzfiVxsw8FDs7ZQYdYCwEnnPOR_IdQmCtvGxKBNgZqxIme1srJs30tufNuKPeM62zsN9by57VT0_OmcorX585sq_hrlXzS5mCD1tlTrqSmrARjWDmyazxBOdZzE_1fZaSZd34Yaj2VL64jneYy-17PF9SYoG6q_qU-J54D0r-Mf1m-eo0NYZN6O4pPcTONIYXo4quLhne41dsOuBE0-cC399rvzkk-2aHLmDC_tOhA2CQEapds0Rl8L_N_PD8vRvKuQIjmA071SfegzhslYy9DKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی‌پرشیانا:شهاب‌زندی‌مدیرعامل موفق نساجی در گفتگویی کوتاه با رسانه پرشیانا اعلام کرد منتظر دریافت مبلغ رضایت نامه دانیال ایری از سوی پرسپولیس هستند تا این انتقال این هفته نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27277" target="_blank">📅 18:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwdQ3LesPkl1hRQ-p-NtUVpl7Io2B1d56ykw18G0bLVveoBVMDT0QYQ8q11DxLTvfpV0psnxT6UkFSr9KQsJxdvp2H0TrbkLP0-QtuzCVadD3vAd_JHgXATq9-f38OkeM3MrVap1igv7cAZ1R4caDlIusHBBRTwegn_Knw3dJ9e9r3TFJV_FiL0iy3-XgyuqQIfCuyKihgEuYmF9ocO8EdrGHAMjJQI4O_fbhCLIfQ1DPhjDNkizaZoADAvn4eo9BN_7VJVDpcYc_IKB5N_8Y1xBjpvwsFxi0JlRH3bDKsl_uR0EjCTmFYwSOduFMEVPPdTK0DOTeX_t1ukfa8GauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکو ماسانتوئونو ستاره آرژانتینی رئال مادرید باعقدقراردادی قرضی یکساله به فیورنتینا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/27276" target="_blank">📅 18:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh07EQcM_72H_Jn0DeTVHjlUqrokZ3RWoloIjRkn1O9R0PHXERW-tZnQcuM5MmHFZrh3ZCpGkeBHX2W2KgQkBCRNgIhZhaCZ4o4N0cUL2bwb6oIdfnBd9a8Zwix_hKCB4-sX_R1EYnf2rkoP8YgyMnkS0BOYC2xz2yD1QL2Q51cq0SnLwzCyjxbzYaclIrVtw4Z5UjYBp41eUEsLz_x4qdO5Qc5RpBcVT_4QAYppYvtPU0WUj4Onq-esRBCFEk6SLwHmWevS9fRBQcPK2nCWXVsWK08EW5ftkOlKw43A1iAPF4jNp4hyDf3PnD8d54gwwMyVg-9WxMtu4_zbZaF3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27275" target="_blank">📅 18:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_u0D-VeRE7XzfnjKwUakQ7pAN-ulungxrJmLiKMibwbSWhE88VEzu80-HTf3F2onb4ViphpU4fG2LCBmCs8FmoP8YiHgezrJQmQ05gyDZNCSqg64PhhlY3lJnfCotf2eBDPe9fUiOLh6pj0oK4t_XNcZdgRKiR4aaXIy8Ul768EpZ7hkuPsDmpo9CZXw-NS43zL8Ss7j3ZJOrf67gTuxvLSTUzAcAJWQFAonbPwRsloRf9ecgunyGyIUZfNxGA_P2kEJYhRdYUFqE8Y-E8SFq4tPpH2Lrby1wTV755FQ4PRHTH-Jraekh5vsu0FBHPTncL3pU1eQtUMC8SW6iLjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvxBw7_fFm8hwMxoSaWlGrEbHqdAlXrovjiD3VNsI3j24iMeBpM2d98LPg1B4sK4Yi6xIRpQw3xlJBS9wFY5ZeKg2uIJmxBN0xGDs2LnSCGGEHGqMswDuHsokVuGA6H_5BRfv-gd6x-KmlBMto6lFPNOP5TqSx-858xGURTSWzk8c0_LG7yhctBKp4dHUQHBIVl6fH_QJTB-EFx1kIUsQTnQXhZh1INEsppR9dFcLIDRZjwxLergDF6SRvtArbLGpBqoTTUjWUq6soz8jhYI8iiim86zkQESiJ3OFsB5qC35tWS1q1g4eYpJ5dSXzyIeieCT5Y40bq7g14AUA7gOoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مارک کوکوریا مدافع چپ تیم اسپانیا به وعده‌اش عمل کرد و عکس دلافوئینته رو روی بازو‌ش تتو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27273" target="_blank">📅 17:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMffyLNJNJ5PYp8UaH7u82Dr4tPP4G5V5UnfE-wzAutRDniFa0JkgmyrgQ43kKF-r-sDRt0o1cx8xqUVn2-txPq5kErsFDtB9H6bxi4rD7InEazmTgGbM8Avi5ugacixSihydLVGRdFzQXa9l48GQgfC3_JHP2hHbrISRfXT_X_cnuTjn3qoSaCD05-Qod99mZJqWPVersaA0zi6HqZiZTJMsvyd5CTNyrvk9bOEfBF-XgCQtngM6i59UzAbComKegPg1AnLjrEFF3q4pBZEl7axahPqO0dqN097Ax10ytUz1ATUm2NaaZHPILeISfdyG-ezdh_ztK9u1h75RQ0kJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سردار دورسون مهاجم35ساله‌سابق پرسپولیس وفصل گذشته تیم کوچائلی‌ اسپور، با قرار دادی یک‌ ساله به تیم گازیانتپ در سوپرلیگ ترکیه پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27272" target="_blank">📅 17:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNCu64jQz6PzF-cm7HyiNoU4ONNkKUOSUYHatkAFKLOYpNqo30FAKY7i-kOuy-rnHgJY5VMs3eNdaJtde7Qym87BWp3jaIJ_6cnN-hP1cwpbdNe2rSRRRQ2VNSTwKS7wDEycr2Kc8hN09PQQIis5GRGMCZ1RQDAd7eQscuQF5N0Nv_2FOIYEAuKgKZbG_Ch0t9_Chsld8PE3nSdu3YlQs_qW882tbYf-T9RMN1sKOgUeujt4KXomcmXrFXR-es1jhj_DyZZiWnT791llFH4Pt4Lnzoalr-pnamGeO1JMItXU2eQwcK-JkjHLf5lUI5ssogJSNLnshpfM6xVpn6ITpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27271" target="_blank">📅 16:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib8sSh6DT1LXzPfdP1weCUfh05F-oEArfQdjUyzYUyO7VVMW0I2i3lprtV0erItATVFqCw5dhY3WU7pAGHO7ET1HWMCerA7yJ1J03FjHZuTgdkBwOut5Ah3391HpV3TlldrgarGbVDgE8eHToSwBiMtxhJQTg9Ye_j1M79amFPk64c6ZJ65HfTrW5F8_aw1EeSYmCBgEkpKtWGBzmX4SN6vmImzyanvFPqzVMvcBVbwdGv7Q8fKISIiYlcrRSR4MVmCXtjOCUQbyj_Wn2gxSDv0bJKJ2TzS9NRglBsrZE1kCY54i4N6c3Gu0n-udeXfdw-0NRXYW_oe4KD0GspByJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ازابتدای‌فصل۲۰۰۰-۲۰۰۱ تاکنون، منچستریونایتد و منچسترسیتی باکسب ۲۶ جام در صدر پرافتخارترین باشگاه‌های انگلیس قرار دارند.
چلسی با ۲۵ عنوان در تعقیب این دو تیمه و لیورپول و آرسنال نیز در رده‌های‌بعدی قرار گرفته‌اند. این آمار بر اساس مجموع قهرمانی‌های داخلی و بین‌المللی از فصل ۲۰۰۰-۲۰۰۱ تا امروز جمع آوری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27270" target="_blank">📅 16:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2Vfgj42l2Lc8Eb7cUbT_FYyF6IFyNGiMe2UP-cJJTCnzMMV8JY0ZO0NG8t37PIAq9MSHqKYMTRxWMO8TdmgxSixeTuzf4mTDUsitwD8BCtu1vC1hgzz_tfvnzAd71V9lo-eDGVEXayv1aNyEzQSn4G_v8fv4ATWcrwfNCFX5M4G7_50TgGlplUu3KmRYiaW2H0hTRqlDEOqWXkBZWkTA953-ox_qnDPnbKM2DmCj5mOCOY1-otVkx73V5dh2NvfX4R1ZyUPZuPhiprt71qnN-5KO85hztWI2zBR6L6Ptzwqn4Q3Otnbgymzfyl3TLbIGUxA6FD_c-2wKpNUPMZVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27269" target="_blank">📅 16:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qd-fNXRpFecvVI7-UWicsUw7Wj55y96FlQkP1w8wKxJMZVQDeywVVLbi-rRa_Kq-cf5rjBAcefCtk_S02eYRlKGi362wsisNDLZG_SavJTVXRopYQbk6j391S_N_Eg9t2C__RBDQJ7aUkIKakuXB8ACMpSwj78MIDltJ6UeekCVU1BsqazSZbbBo0ptLM-URh8ys0374fV-X7rmdxuvHVbAbp_f-77_NEa4I2dlhy62TyaO-puTg9B4ci-RkeeZoYWncZgEwZAl5V73m4ROAXplFg5mwr0KSNbeOzJiA8NGkA3G5nsAGRQ81VAvfq3gGhA68TNM-yIAJ0vPtdplcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27268" target="_blank">📅 15:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1DExounyQX04_UrzEfqJ0sY-UjOOtfb1txDwtChtpeA76of0Ex0MVvT1sF3zs0UPKe5tVv1Vi-3j2GVKFbOyqZbKOc2lC3VEMtSt4WgGQ0b3syEQ1TYd9KnCa_jgOJMFUHdNaTV-aTrVGJFJuBcE_XjX6-99k1miXd1ySvxVjMEFe3X3NtpMBV-wLmfisRe2wNRYQ2c6gw3I0dPQ7f4LdWxXLrFkuh7UtJPRj00xKQzQe-iEP5hwmOdDKQyk7Ma5i5Yn55U0QTatA2RiCl_Ep9nOh3IRNV4az4TypKZ0UjdeA8oRrC30lmqAs9Re4786cApRErsR4jyf_Y_OLdneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت برگ ریزون و عجیب پاداش قهرمانی در سری آ ایتالیا و پاداش صعود به لیگ برتر انگلیس:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27267" target="_blank">📅 15:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27265">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEHiSVbRFhc12ZxGVlcv1zjz5EHn5DVVF-bdYEXf4Jtg_ul9fGncNbWl0t17j-w0dtAoSZYM1EfqVR_Oa9VVkN19x3QWi4RSrO-rZs0BM-JhZma3X0jQndB_rnfIyOTYHmHxvtFpaX9HtnbmC-XD46zLYTZSiCNGsBMCWSCsCYxk5C1e-nLbi0lfhF2pNYJYxnmFb9z1yXXgB2_b6_Hf2E9zpAAG57B2BDyQIwRKQmmCunheYdTJmmldnTag41T3q5BKM7YnA5tPmgYMTjib26xwL6pgI29944yyvYPfvd7ZTxQC4t2dt7I8zbidWrHPpTfhAzYfbAArGyKhkcmYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEIgXMPLWRMH-Thl4cRPWMOFegrf9QE20cWXnE7nM_s0-IAbgfkz83D8mIy-zi9i5fqXYzvhic7mO3RgcuTkL8Y6YW8Y2S7iAz-ygWLWuTbxJ9YJUNcf-uWprA0ptfP1v24Wrt6Ybuee5zv3EWH5PMUIxZUdfWZOBpYeIDnCHVaZcWAO72W4Q2lgG7wHr7H95hArKGFP-Ye-qp-UygTcobp2jJUTJs3ZGnZfLXZyvTftJu7nnAXa_esoc1naFD6nNS1Vix6fap22Izm7DqoComZWd7k4oTwr7SgQFH7Zl8iA2qUH5Dw6WpYjEnucbX_KYhZurYMPHrrUx67I2n_O_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ژائو فلیکس ستاره پرتغالی تیم النصر: هر آنچه چیزی که یک دختر در یک رابطه میخواهد در اختیار مارگاریدا قراردادم امانشان‌دادلیاقت من رو نداشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27265" target="_blank">📅 15:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27264">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGdEG4J44Se6ZkHM9CANaiFRMzTBsECuhcFo6SziV9AhsXmM7keFwgqYmsZlkYMXTLZgDUwrVD4wcNBBUySF61NsS9o-Ro8c2DdO7DdAm9xgMMk8oQonk1y4R58M03XyFxfSpz2I7BfGNlsUtKDf0TX-143eFfROaWIFeS6bzx9ViU4-xey5h4sxFDz1i-vFJQRNxmSfNfGnmJXIJKiEs-1p9KrpcvQZZCs0phy81E-yrq9V2xBjK7yymJDrxeVYFqxHsMBX83oHvCEBCBt3HMwCNzT_91cX3KfWXn6q1P2DRMz-x7Ih-rhFLX-Ebm8iJ2GBH0YqQLsCY726xOtUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
سردار دورسون مهاجم34ساله‌سابق باشگاه پرسپولیس: شاید در چند ماه آینده دوباره به باشگاه پرسپولیس برگردم. من عاشق کشور ایران هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27264" target="_blank">📅 15:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27263">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pggPIRx5VLgAphYz77_FazLwJ54cRUm635fMpDzN2LSROYYSTbDidbvujidQhTWs3OiWHenBfWtmYVohD9DcCurd_ENo8IQo1n2GNysn4_C2ggLGWk9bUrVijv2_qGbr042NJ9VO0L8Q5zPTDegjycCpEeSCbWCCXE4MaF0HnhSVST92SZNllsdwBRp_-JntD06WYD6CFOQ19Ovq2dlPJ6B1M6lpIpAmjXlnCGJYUtykdcHA0WrHgZAVFdco8RocKglFw_z1VG7oB1n-ppuZVKdytr18oA3M8fKf6BjjAUEpHWFgKpBDzX6LJRYj5ppTOPcLvmAqSWo4CgeA5IAv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27263" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27262">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBg7L513B2OQ45tGJNVMchlsFIWVLeg6Cwg5rPwUbGgwzCIa_e1Disa-YpgpaHr0Trx42tssgjcFvsQV-20CoVfMamWZQw-h-aJy5pBa973fjShji6ZwQUonrF84G-xMNnGNJOkBCWwBrTtVcy6Pim1YGMzp3rqdCmWfnhx_CuqCg45MZQ7eKTm9toGsy7013eK_LA8odw3EMfeiEO5swwIcVbjZb3dIz2-JpH-lgEXZ-WuLepL5PWFsh-e_HUZJm3WYlP1S7AV0E2loxYM4bkwsC4wZHt4VjcTRqWjj5id_6pkeFIhJE59R5yE0lJDxk2VQ4xRQZZmdcnFqR1tvtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ رودری ستاره تیم‌ملی‌اسپانیا رسما با فلورنتینو پرز تماس گرفته و ضمن‌تشکر از پیشنهاد این باشگاه اعلام کرده که برای فصل آینده بارسلونا رو انتخاب کرده و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27262" target="_blank">📅 14:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27261">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6M4W5UzrFSlD8j10ACtPR9Xm3hvdrrKaeQzUP2L9ynNwkqU7MfNOn82QC6uRc4kz2oxPuFS-49pzbgoryuBQrlP9QZS2swneNV_xvxmZtVjSlPe4S_LmjfBpPK6kTtLetDtt4l7jdMtrrHrfxWXC8t23W0YAVSwtthdRZWGD9_pEcxiJ3F8-bLGisP7pHR4wuZu2_zMbfNUZDqcNyFN8BkzJeyBjBkdBe1_XIPAVoUXw3oUnI6G3jPr1WWZnwbv_fEqw9NyR4qtdXHgAg4Nqk2RPWTEER3OZCdtjVZZ82V1uOD-lLbBeabU-cQ9byF0kKdSR3TazUqDUpsq5ayTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27261" target="_blank">📅 14:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27260">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRsbFvKrOrmy3opTK8Sc4yho0mU4jajptyTBLE2JfDGqV_V9mkg6ppW8r7QVTq_V-d-5lKvkhOAjGunUOy7TeKBD6SiBEMZ4tg-rnYFQpvFmJFlogakPq1Pd9i5liAluJyIxx7tlT-D_myuf60znbOEFT1BWuS7eXREbDgF53yZdbQ0RqaXT2GyYuFwdx6qX2dje6JBHrKFp9zLvvIk5QOQ6SVIUGclprOJ8T0aLGXgovtCnnnIokjG8Pr8DSv3tIbmWK-bKzlxlehD8rxRY6e6A846Khm_k-zorBM2--5aoHJ8OkXn2FylTFQo6kzhCabGNqJ8CdjQgL8ATyn9ebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایعاتی منتشر شده که آقای فران تورس که با زدن گل قهرمانی اسپانیا حسابی نونش تو روغنه حالا با خانوم مارگاریدا اکس ژائو فلیکس که اتفاقا ایشون در طول رابطه‌ش با فلیکس 3 بار بهش خیانت کرد وارد رابطه شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27260" target="_blank">📅 14:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27259">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab8b5b02b.mp4?token=e3CbP_m_8Uzx42nri-qaqPEI6ur0nUAp6v_Por5LVxRCg1_Q2yUsb9rXlYlFdlRuDLuoIFLH5h25kWbqfU4sVi33DFgHA7ZCRPyrwkJ7TL5ZTHT8dIb61gxsSzm0XTUZtl-7z-lQj5_N488e7wIwi9xyjWiSAQJypkB8U8XQ7aNLQzWx7l2SgE48PqBvCLCC1MXKwevpCjrpYV8XBcpsibluYPNLtk99xZ7iCzrXdxvC2lNwICdztVrkdW-6USL8ZoyZmOULY6rZ04o82CdYTxkn9_xOshWObURuXKoizePo6dXEEdRBU_uFeP70-jucKnEpDtPBiX5CNLV1NCKYSglVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab8b5b02b.mp4?token=e3CbP_m_8Uzx42nri-qaqPEI6ur0nUAp6v_Por5LVxRCg1_Q2yUsb9rXlYlFdlRuDLuoIFLH5h25kWbqfU4sVi33DFgHA7ZCRPyrwkJ7TL5ZTHT8dIb61gxsSzm0XTUZtl-7z-lQj5_N488e7wIwi9xyjWiSAQJypkB8U8XQ7aNLQzWx7l2SgE48PqBvCLCC1MXKwevpCjrpYV8XBcpsibluYPNLtk99xZ7iCzrXdxvC2lNwICdztVrkdW-6USL8ZoyZmOULY6rZ04o82CdYTxkn9_xOshWObURuXKoizePo6dXEEdRBU_uFeP70-jucKnEpDtPBiX5CNLV1NCKYSglVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
شکسته‌شدن‌صندلی کنعانی‌زادگان کاپیتان سرخ‌ها در حین مصاحبه با رسانه باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27259" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27258">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccbbedc5a9.mp4?token=aUgvkz2wcpnvrTFfuYyAcEZcoN5_fOcVC3EJknop0E6oAeEdsWXQU7HFRGIuVRLu8TQ3l41cg0sB61AegEtUaKycPV95hHTB5yC6k_Q-uNY_BpV3dktqVQbi1g1-PZJF9xRzLJCvie70aP5aUB_R8K6wld2BGji9pgpYRbXoK78ODXLHOnGxKRkowuy88JySAmyCJPoY-2YAYzW6ZmmdzBhv0rTWUPW9X6V38xES66dHR2cUkIrcmMo1u4kRYqVQrMEBORWVgqOJjnStPpkIuguviH-JTUPRycsWG0gyIh12_6Z_d-Q_1BxTjLDrDEgyoCK3bJlbOySrwu1H7B2r8mxGao83xAAl7Cae_HNarvddE7DzXNb0JLBUk1hKfo4gbac1jtoAjK5Fa7hU4xmasZo1FeQpRmRffGLF9y-qvwTuKErtLqOoEhlJbuAVhPvl9xhC1wIbo2N4lLNs3gz8fLpYANmFrVFZ8S67wLsklL3Zs1ygwQp1Ix9R8aaFALeL-F7_Mg7UsXRz5qgHY9wf-ijwkBb7McSHDjzFlBwu38ZbGmtb1eAcoYI5QV0Bm-ivP5Gs3YvxqIBnx5nA8iG6jBIRATeR1Eypq9L-uRY_7OF7O-W05eOkSP32XS_RcJgxWs2oRucjVHeHZripaUNEpyNBOVCu12YkCgvinV8kB_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccbbedc5a9.mp4?token=aUgvkz2wcpnvrTFfuYyAcEZcoN5_fOcVC3EJknop0E6oAeEdsWXQU7HFRGIuVRLu8TQ3l41cg0sB61AegEtUaKycPV95hHTB5yC6k_Q-uNY_BpV3dktqVQbi1g1-PZJF9xRzLJCvie70aP5aUB_R8K6wld2BGji9pgpYRbXoK78ODXLHOnGxKRkowuy88JySAmyCJPoY-2YAYzW6ZmmdzBhv0rTWUPW9X6V38xES66dHR2cUkIrcmMo1u4kRYqVQrMEBORWVgqOJjnStPpkIuguviH-JTUPRycsWG0gyIh12_6Z_d-Q_1BxTjLDrDEgyoCK3bJlbOySrwu1H7B2r8mxGao83xAAl7Cae_HNarvddE7DzXNb0JLBUk1hKfo4gbac1jtoAjK5Fa7hU4xmasZo1FeQpRmRffGLF9y-qvwTuKErtLqOoEhlJbuAVhPvl9xhC1wIbo2N4lLNs3gz8fLpYANmFrVFZ8S67wLsklL3Zs1ygwQp1Ix9R8aaFALeL-F7_Mg7UsXRz5qgHY9wf-ijwkBb7McSHDjzFlBwu38ZbGmtb1eAcoYI5QV0Bm-ivP5Gs3YvxqIBnx5nA8iG6jBIRATeR1Eypq9L-uRY_7OF7O-W05eOkSP32XS_RcJgxWs2oRucjVHeHZripaUNEpyNBOVCu12YkCgvinV8kB_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موسی جنپو وینگر مالیایی استقلال که بلافاصله بعد جنگ اسفندماه قرار دادش رو با آبی‌ها فسخ کرد باعقد قراردادی به پانایتولیکوس یونان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27258" target="_blank">📅 13:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27257">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lodmp12fEkiQVPD_4s5zKk_s0HJf7lKy2JuJa4Dz5sGgV8jeQWoUnBdljt7q0ZPoIwLjNiwj38n9C5Jfwx8EE-X1L7yOiMnFqgSMh8wnIx6MmLMFE2_N8dBsSOEp81XDGy-iqdFvN1PM_deyhcXT5izWmKrbbf7QwLS3WIx6DecYDFBp8gY1UOSeBNkgeJO2FQAomUw6-fQytp7-RZoHaiBzoLWIhEF_-iVZ04EVrMdBZLt3UM3hxwD2qAs2K84mRsun1kicY99UFT0Ll_LIujtcaLejyWM5iLrEQNIGtVXTRh-D-PNrI1Km9LZF3WLz9c6eGG2VY3UE9pcQgZ2Cjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد...بااعلام‌ایجنت‌موسی جنپو؛ این بازیکن قرار دادش رو با باشگاه استقلال فسخ کرد و رسما از جمع آبی‌پوشان‌پایتخت جدا شد. باشگاه بزودی 350 هزار دلار به حساب جنپو واریز خواهد کرد و پرونده این بازیکن مالیایی کامل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27257" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27256">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWb4708JWRx37YoJB2AFd6_sjXosmMRt4x0gdyhrtzEssLhJEkTOyrEQ3Dajj3i3WAh2P_1Ep9-aQHqwCyoF3vR12GVKnwI9eCzLuQSvX5YB07PMs79QGDHyYAXVfGI_I4BSgQwo3668MVK_8ztIXpGxAWsegC4QB1ItYWNNzCESDPcUGl2z_z-2QjntpZ3kv911kQowmPfG6Qw25kEHOz0S9MJKCgtaaXycmMl85fEmW2BZxTj7MAVfFrg16dmzTh6P6fFdj6AP7k3gvLRFouaSY9UmejExlWImLuRwomQYK7egSjcMnunQ8qXqh24vSITbIqPPzVFNIhCsCDwiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس: از مدیریت باشگاه خواستم که سه بازیکن جدید جذب کنه تا تیم برای‌فصل‌جدیدتکمیل شود. درپست‌های دفاع میانی، دفاع چپ، هافبک تهاجمی بازیکن جدید میخواهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27256" target="_blank">📅 13:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27255">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc9f95afa.mp4?token=ZoZJYySw0phzhKTDnnL-3G5YSx4Rwgi7HFTxixoiIaRRkLhxOTmt1Y-oCAsyXb94xJ6i8MVJKs15RlDklhMYeN5tTULY-EpCZXbs8BPCgJbx8sCYdAsBTFAmIKkgIalkb33bIEpyWnixRdVD1eLHq967iIevv-70cOMumL24KAjvcbGwXglzx-7yACot58KrZs9BfnWx9mARQik_bqRHNcYmM7Hz_aZS5PAM74Cu6w6-jHe7g3o7ZgUmHOI4UqWVGyLNDOaXvNlycOybwlStRoFUDDp-UL7Bn6n0UnczIgvCF7FnXzaTEdYtw-oG6YBZQR6iwuWSz4TW2m3_2-NNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc9f95afa.mp4?token=ZoZJYySw0phzhKTDnnL-3G5YSx4Rwgi7HFTxixoiIaRRkLhxOTmt1Y-oCAsyXb94xJ6i8MVJKs15RlDklhMYeN5tTULY-EpCZXbs8BPCgJbx8sCYdAsBTFAmIKkgIalkb33bIEpyWnixRdVD1eLHq967iIevv-70cOMumL24KAjvcbGwXglzx-7yACot58KrZs9BfnWx9mARQik_bqRHNcYmM7Hz_aZS5PAM74Cu6w6-jHe7g3o7ZgUmHOI4UqWVGyLNDOaXvNlycOybwlStRoFUDDp-UL7Bn6n0UnczIgvCF7FnXzaTEdYtw-oG6YBZQR6iwuWSz4TW2m3_2-NNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
ویدیویی‌کوتاه‌وخاطره‌انگیزاز سوپرگل‌های دیدنی آنخل دیماریا فوق ستاره آرژانتینی سابق باشگاه های رئال مادرید، منچستریونایتد و پاری سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27255" target="_blank">📅 13:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27254">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ71EhlBfxZ8HwJknPKuD7tYgCqs3J8O_Du9Aa02YVHsAdEUnAXjIoR7NEub6jbGzZvjMbqot-GCn0VGqTQaa4usGt986KNJ1ZnPG_qCIhEmI98Q38gZ3hIbbfACvdo2bl-1mPOLKs9pTw5qYIhY2mq1ChOPPcZ1cMSd_eg6AWvzwnqBGZ_KjaadQN6BMD4klMhLhCZKGynpVRASuCdCTBc7we6aaaJLz5JE5M3bQB2K7MNT9pkn3jI9s_FYXNavpXFtn9gzONRvR7ik2yBPB2gAhoN9o1tmfxgujJzNkvE4cEjssdmnOHGO4hDn9IStSXcMKeUnNY9rZ9DJkT2lQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27254" target="_blank">📅 13:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27253">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM3inFKhoc31SRMJITgY4na4rCvrI4T_2pSC3itfo5x5y1UHdHGJPGfEnn-qLxgSIvRxdJeyhm5CDSxForqj7TSuTa1ZQA0k4NNYjsUKDq8qN5INXOzWwEjamRwE_iGgKWsaKRaPmCu15vyl4Z5_IfryJvCWRqtdc0JgSx7TAfpcuJwu4zouUL3_YpNk-N2L-o6hm4gQaRLLOFfkHspaQ8R6GchqcbSj4EMO3nFLMgH65esAtDkE_o9hYOSbeBVNiy18seXmtdQlwB4itiDnQraYVac0USKvVCSqdUqqyrvV54lnn8V--8XepCFmFfCFH1uoa04JrJfloCX72QMAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از استوری شب‌گذشته محمدجوادحسین‌نژاد؛ سعید سحر خیزان مهاجم‌جوان‌استقلال به‌اوگفته این همه صبر کردی یه نیم فصل دیگه هم صبرکن اگه پنجره باشگاه باز نشد. استوری دیشب حسین نژاد نشون داد که پرسپولیس آفرفرستاده اما اولویت اصلی این بازیکن…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27253" target="_blank">📅 12:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKVuNdz1TzsNSKp4e4KkTLe_djWi_nybiVo8McLlD5pmvXbT9ch_Ln6KOvRy_GajfZUS_vM_mDWPKtUQSaNMraCsLgFlJGSEU8peC4pgst-DDFLTp8iB-P-N5npvyWGBtNFjVW7vGPtt5lLdNyUPkUr2zXvpmjnO8VHtJcqjX9BgP9NG_28rPAl0GQZi-qZRjtIwL59IpPHf3F2F5tbSDWP3VbKhwTFcIX_X2QR-MVEXi5G32nXklCLWUT0-hToJY0wXs25P4vbd6IhIOKdo0Qmefc876BpfP0Fcb0vvUYWMM4DiMvQdenTnNpOUulLXLLPlnRARoZk8GknANnPHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
#تکمیلی؛مدت‌قرارداد محمد صلاح با ترابزون دوساله هست و هفته‌ای 325 هزار یورو دستمزدشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27252" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM9AUgYpyJ1ppPNMRY78WsLJws2WfHARP0KUOGdw2hmRup52yfmquF7MjAe_86v0X4fcBOnIvS1pMwrZcbMglvMEDRDFtuIlTUDFkCFs0qDXSYifE7Pb8AqwCbtdbSxN2LJ0ubFwxrUYZNTUsq6whQ_hH24M1np5v6uhsfqXT7mdg6BCEco33EG6rU2z_0aZLz0KEbt6I20XF6OfDHsbo6_-ZxX3DlrF073jEz4T99Mzc-9XYG7fPObsOzFJ4rmZfTki_vHQ6iz_mfejaskTvDVC_GAM-FPCpHL4qwyOtQeF22znvQVmaA5Lo7KP-sharQZRaVKai5ptFGAXi0xFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ به‌ احتمال‌زیاد و اگه اوضاع کشور ملتهب نشه خواکین گیل اسپانیایی به عنوان دستیار سهراب بختیاری‌زاده دراستقلال انتخاب خواهد شد.
❌
مربی‌اسپانیایی آشنایی کامل به فضای فوتبال ما دارد و در کارنامه او همکاری با تیم‌هایی مثل الوصل، بنی یاس، بتیس، پرسپولیس،…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27251" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📹
دانشجویان فارغ التحصیل دانشگاه الزهرا تهران هم روز گذشته این ویدیو ساختند و منتشر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27250" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlQU_ifmQKnNXo0nUs1rS_tUWWj6kk-H8AITl_QKbkuWJhCpmGBRkA6LxDkMpObuM5-WTaqOOOKwHrU_p3nLfRRATTqIIf-UfGlKJGoRBiLTqxZovvUQwFI6rvxtQKln35rYW6AyzsZqlUr89oyuQdcsA4wJJxBSqJXdd-eFqwEti8woFGDjXA3aaeQ8NZnC4k2m2zuhPeI52CNhRpwZYmpAqOuPWkU7oc9R9ra5EvoZIWlBxq9ZTFD3YnAkIkrH6nAuGmBjORaLtmLy0jtMVW7qzUp_shGg8CYZphqhPvOuh2me1nUK287o9-1xLi0YV7qcJeipHxTiRK0wn5nD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27249" target="_blank">📅 11:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz0IApkcf4iaX5U7LQLTrngfTCsabpj-l8Zxgq9AA3t-tnsiANfE3deQUsW_Eyagp0Wn3grRoPEkR8jTBnG4yV3xHWHgmZ_ZaDatXNVzKoy3_Bmj_3IObnRWLOtIrta0mkRIYEwNUwtGscZwC0qbpE63nzCGHxzDoxBOvlFsxR_BbJV6zy-BeC1i5-diiuXTC7OMSmmVY3_HYLDpVA51CvwxM1MYhaexpNqhB22vVTxc4sSkO2aKzvTb6yR8-mGERgWcj737pdjhRSaJ6Z2h1igh7ZRNih8mdOPnbZyGOR-vcwV2wQy9y0M9EKildJXQ-XPYh7qlLhIajFO17b76hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27248" target="_blank">📅 11:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6GGuyfsV91dcO7Mh1ZM_TEiua_za599cLG5RgG1EUebDH-XNJr5KtQXyPmeoWrucXzmAO0bGLF7oTLCbr_ERm2HIt_t-NdRvp5jZHmZC-9QZ1zUcJxQfRMZ7dHkc-3dyNOrVEHraj6fQcz5q7gSIU2ZHQT8QoE_475nvF29LJPM3ryoYopt7ey9oKtHCEsS8rYJf7CRYxv9cb6_2SOpD-jcdW7y50NXywlf9HxtVO1-bavrsyLkgvvYUO8u1Ce_CyyxXINQ80w60UE6Vg72ySOXE0wyu0qmPYakG4igiXrBXW_9BVEcFHuK3vY1B7519gj063HCg6WIxgTNUbDS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27247" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CswQjuCNJGW6jGllHrLadVgoJZpxbJ-676qdpb2PaDBCcpLLliRmWBBAgCe4ODHwTXKRwU4t47x1N9E3Pg0XgaoIZSFlFcpE7gEPmYlwOL9LEsyVjcqUQT2Pu7QWaNbRBP4TiF46iM8UnBKqVkJzyubRTYyRCIcVmGLhsGGUVCFQxQjncpiQ_oam0KZxN6hMZcPJLVu6K0eYTQCYHUqzVfz3fqIJsQrQn7YOagq7zNPinuvxFFD9dweuoQRRFdKYT1VrK3DJPD6JhbZTXyC8B0EGn1qRCvRMhTSSHLiVYF8pRi3eSyoFmAH_maFHQOzTrHDZikWnWcx7nQjP1HjTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27246" target="_blank">📅 01:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3UvQO9sJ6X23UQ_Y53XgT07caO_7sjrBOURe7ypu5_RYOu-rClZ0vx_FsUOOhk_GEbRZreHIuiQbh5Iq3oHiYNnHhuOJ17XeypKKg5KX1eBXHXy41b4vL4ml4szz4b8g4gWyUxgqKBiE6G0d-Jz98L316YZ57Z7yDKyUSAzoXHXVy4dcX2Nm0aucoLKl_GKuUjvSzdDj48zMUOgoyM9Qrj1ac4wmpEzGzhyu8u717HFTsWQH2o5vcVnrpFgSW2STG29sk_AzN3nP_-YwGFesoZO-BCGFlQ-DDs9d6cRlNPDh8rhqDSFn2d3eNCB-2QaKzyWYCES22iWXu2wNBJxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
🇨🇮
نشریه‌مارکا:باجذب‌یان‌دیومانده و تمدید قرار داد وینیسیوس جونیور رئال مادرید به احتمال فراوان دیگر خریدی در این پنجره نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27245" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27244" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz2Sl3kHYmmjiwvjMGtvfgY7K6Pq3hOvt9wAHEuXvcAVL_VoxJRgjqVOu-hoB0M2NQrwshV97FVdpVOBpc1nC4ctMZ-IW9KBKs2u3bYy7zhX8RJXHuGGvd7zcb8IGm_k6YEU57dgXxgI306jvZteQ3VnGJ5eh9UNlr-7j2Z2D-ni0prgkm98AyDz1h1k-pOu0pzc2gGSjUc8ifkx_QOg_fkHhdrlsZafmInQBHFJcvaBqKyVe-HU-7gH1Drukt3P-oRT_D1BRyD-HAFxSYlRKsEP_G9p0eUABXYzzMVpt-nUkW7-bZ9apjpd6YiewyxBxCfkRv6WNdBqnx8fH7WxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27243" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZmzlUstei67Iyg3qDp0FC1UNzp8EIP4YMscxseu8hBIIsLWk6dE1399DvTCP5bO5_GR8MExoRKNIa4ypv_S3yyJqYl9ffzOiqnLtFi__aEogLKqSn1LnWLnQsSqr5FQq_Z14PXqk0lI50y7tkLEoe8OE2TMErus_C_30o5Wh0qyEZiSn9XJQP5bK8bv66aayduCX6fLP5_n6EnSBgz3G1nRlTwXAkRqNnGOCUA1isncx5fMx4OF9ooTJelkj17cuEGjJpb8UJJwaAU6BJO7Zd02Eywj_6hRUC-4JYc2KqGhEyk_PVKGE24d2Ac9S1N2QRhyOprvCehEPkjjqfVVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها مسابقه مهم ‌‌‌امروز؛
دوئل دوستانه و جذاب شاگردان اونای‌ امری و کمپانی در هنگ‌ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27240" target="_blank">📅 00:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT7pSF3w4rGbkIJajQ51EDliRFmB0ZgESnjsz3LJ_tHWjg_XBbqAGY8msIM_L7NMQQRSX7uOAcPL7aL8SNGcDrhKRfCvFLtKibDn0-jd76QjXW2IoLMyPieGYsKF7NDRYpTORQ33blBz-EtsfIp9MIJafuAxzrIQfXg6Yn78qioai9TipaCRAWzp4UHnAYP-MpM8JUGOBI6q8cWUXKTGx7Zo71PRosvlNShxnCSBVM3sO9AwTX1Cg6NcsTo3NvPZOvGBq7UOsu8ztL1eQCjSyR3X1iyf8WLbTTHaSwY5YthOhJJJyC7fMZ09KdOAxaT_dDek1PkiRz5geRgZi4qzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
برد اینترمیامی با نمایش درخشان لیونل مسی و ثبت دو گل و یک پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27239" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_gAgRNBvcvsmQLh9aEZJWV2vi9dNLG9df9OGqXDYBd5wS70jUTs98tzH__b4yYZlGOOLaJPnIf7OZGUInoYJAWL8R9-ByjGt7C4NkmCMJpL5NSBNxysEXq3GRrrEz2IAgrvu5MRCDjVzEy-292IHB1uIkwKpSHUnQfwrkPe0qFevNERAALJP-oNstn1uigcw32DFznp9xIMpLjeU428EpzWC1Fu-dcZ9kfowpOOmIaKCjHiNMnfDJaj46WIBrNatdDWO22MwWwN29FYN6Jh-NQejN3pe6_2XZuQFwDEUYeofCV11QoQdvnsvxuEgpIVQjAjRFEDgbEIQERawe85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27238" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-IY3vgS9Z9jq3zIk_SJAHJOtD6i5a4aMOUiLkfuBCTi6hccA-x0sN6spTU-3VqbpscGU3JOWG6tW6AHJAd-el8b4IW4-QQv5J9q8FzyVyNz4KDx0cCVihPiF6ub7fui9-RT8AwGqDFVwANY_jy6pGYswlxUy60_ifb7SoVKEJpxrJ04OFVRXf2p1m_sD_tIv8PJ7Yi8Z3iOQWxeFSpHPtcHu5C1slofGLC8Ou6DKadf_TGimVwnY12fHFtLHg3iigjowoOU4MSjg9X_pSUA7JP_PrvaLnIp85v4a4bNsml3Ke09eiNdrSr3jErg1P4kWy0IoBsoJBXYtJYUXR7hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27237" target="_blank">📅 00:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH_jEdEqUiHUuYarrZdgMSdVI0I8DLBP6Mw1KNnTUAIpptvH6dLYR8VuSTrDeyI3Nw-tj0Srndsw6kUTBYdrDbTFoQ3MjLs6w_asbnLOAy4KEnztfCnglvednjY1fxPX75BL5UZgcZTUlhTaYe-o1CIPvLhqMLqzaOeX88afsgqUmK_OstWDdSgu3SoIjHPkQjhiE0O6kGvO_qqCwB-5JTHUFbxcjnY9NJmQch_KWPpl6cnb_viDWY52s9bdw3txn3CNbePT9k7DV2IzmZzHZmp0vB9Nx0kzoK0CkdjC59sGJokSr3PA8ZYMntKzt_ipbtyVcBkVaeCE4gjBr1NwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متئو مورتو: رودری ستاره لاروخا از صبر کردن برای اینکه‌رئال‌مادریدبامنچسترسیتی به توافق برسد خسته شده بود. بارسا به او تضمین داده که مذاکرات مستقیم با سیتی را آغاز خواهد کرد. هانسی فلیک با رودری تماس گرفته و این بازیکن به او قول داده که قید حضور در رئال رو…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27236" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPW81R8f3cgwj_7pJaAwMxZasr1Zh5tehZjQOuUPBL7RhtF1ETTUH7GfWOb0buKhCfUm3KOO04YehS6Bj2fMH8K7XhukrfgnXDdnxX4VPp6HsIzChWUWRplratCX9HDqwABL2-vbcpzl3XfrQMbQ8gDSgjvPZfKJWgkE7752R7Y-gmDgTNtI5nnZKoMzznV9t0yuCkmrQbSkODxCtSoI_imlXy09mjtm7KY83goFVM1pfjWBOv1647r_4aLmtTU8cLTK_8bfDF61L8trxhwTQsXQfa8ih83ehcWgLWD3gVNX3Z1Ybadnrl6BQq6dRBQdFVnNGVHOcVYi54SXnNMyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27235" target="_blank">📅 23:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE49erFzcPGiwdwW0N1rQpqx3m25-tPjJY277kDctmhNvNxfc6UJa4Ri6a2Ihjm5nMndABoaOh4fym5-b2zi5uA9jALqHL5PYVrCi9Qk9TLFU6HURpD-P0Cr5ibDi_2ECd8hSmgAas0Pi93Obe5oA55cF1afugJQ3o3447vzg81y82A9kEXx97C0n_e0HeAS1Z7KH5ZhuJsqqopzIeM5zbX6kqJBSS5L3B8TrSIgJteC97PleapdB0GSudG3PR0BC_ZC-GtCv5e4ciZae6kA9SLY_Y2h7TKIDhrrb5qHcWA5KMSOZHTHIvd3pPyg33yxEG_XLSZMA4sBf1qU1r4v1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27234" target="_blank">📅 23:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=o4jLHFs0V0qDZ7QAjdErxYmHtNXtahaxbtGkBtW8DFrcwRcl3XjLQ3BmO_XjkoTNVEfh28WSvLlExLZU6Gv4_kGM8Hf6gWwM_l8a8GnszfosxVtoijeaJik_2GL5SpA1O5YWqOUzquzOLyIBmFEflwn7LsZUtT8ClxAmOhpfrt6w87r__XESC37Q3u7m_sOd4Febj9UGD-TqmETEun1ycFsaKsClnTsfVGAZtd82pxo_DBis2Z2F_OCLBxECuiP508aoqNNy5wdRK5LI3SV6alf5GrVA19ncCnxrOi3pzzdvqm1KBO2WgaIogWB0cws38AR8ZUbdKJB49HWl9wgU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=o4jLHFs0V0qDZ7QAjdErxYmHtNXtahaxbtGkBtW8DFrcwRcl3XjLQ3BmO_XjkoTNVEfh28WSvLlExLZU6Gv4_kGM8Hf6gWwM_l8a8GnszfosxVtoijeaJik_2GL5SpA1O5YWqOUzquzOLyIBmFEflwn7LsZUtT8ClxAmOhpfrt6w87r__XESC37Q3u7m_sOd4Febj9UGD-TqmETEun1ycFsaKsClnTsfVGAZtd82pxo_DBis2Z2F_OCLBxECuiP508aoqNNy5wdRK5LI3SV6alf5GrVA19ncCnxrOi3pzzdvqm1KBO2WgaIogWB0cws38AR8ZUbdKJB49HWl9wgU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میلادمحمدی‌که‌ازابتدا در ترکیب ویتبسک حضور داشت با دریافت دو کارت زرد در دقایق 21 و 33 از زمین مسابقه اخراج شد تاویتسبک که 1-0 نیز عقب بود، ده نفره کار سختی برای ادامه بازی داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27233" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=veGAx0uvmGdiyfMgruaEHvxnUeijwnDt-eiMkArhQscKGE-5SxkXMwhsLmOBxvUUHzP7UsP8me6e0d7c3O-oDmG9mjlGJ5tK0Mn8fHoU7BIh-jqbWJEx_qDYGW9b0YmnCnLuIlt0CYAojgdZVGoNPeeIFBG0vJyJAD3RR8vXEMOMKTjg8SyhgHOpne6WcFrNEEYquRI3OTMa3nzTkgUg0Xj7PYYukMdSD_0fAgBCmJHM4opSz0PDr-_ZLk_7ubsGcTbQ-WbKo8DKFfloCnz9bjIPQUtYP7vtGo0yYlGPAdkpv4gKkrtAWjmnjtx1VJ4h4EfhUI68EWbZKt5GO7MI1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=veGAx0uvmGdiyfMgruaEHvxnUeijwnDt-eiMkArhQscKGE-5SxkXMwhsLmOBxvUUHzP7UsP8me6e0d7c3O-oDmG9mjlGJ5tK0Mn8fHoU7BIh-jqbWJEx_qDYGW9b0YmnCnLuIlt0CYAojgdZVGoNPeeIFBG0vJyJAD3RR8vXEMOMKTjg8SyhgHOpne6WcFrNEEYquRI3OTMa3nzTkgUg0Xj7PYYukMdSD_0fAgBCmJHM4opSz0PDr-_ZLk_7ubsGcTbQ-WbKo8DKFfloCnz9bjIPQUtYP7vtGo0yYlGPAdkpv4gKkrtAWjmnjtx1VJ4h4EfhUI68EWbZKt5GO7MI1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد بهترین جواب به ناامیدکننده‌ها، تبدیل‌کردن همان رؤیای دور به واقعیت است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27232" target="_blank">📅 23:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-rCj1x0KYVqchIezYyw9Tdg3OyQ2qGnQOKcYU9tdvTP6pGuq0wv-xK4UVYFCn16MDr0nyHFAl1CYzYUVUWPZNsXzUHt5EvfxdUrauJOgOsLwAkgnmRj2w43osHWTuklhbVjDv8IAZPPoHmx_MeIxrfi6O9GiiKzq6CJ82Ijj5JIARz6R9ssSRvS7xvyBHxa9FGsePZF2rr2vdXqwyOckshgCc0_aiPom46G9pEOgFJfHyKNLsxpbcfa3vid05_eTNsZ-mFMqr7-vDHAEshTKJT9klCpegQFujVd45_grRQhKmyBbb7dagt2f2-6_c4_Msi3maGRHQgKr5kJLHUY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلطان‌میلادمحمدی‌متخصص‌اوت‌های نامنظم تو یکی‌ازمهم‌ترین بازیهای تیمش تو پلی آف اروپایی تو ۱۲ دقیقه دو کارت زرد گرفت و تیمشو بگا داد:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27231" target="_blank">📅 22:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27230">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=X5dgrrXDxCyd-baErgz3YCqBn-RGn8UuJmk4CkwgJL4fr-q7mjB6S_UVE3-G5eOAUw6Vqmz8vBinq-XagMuDb4tzRz1GEui0dyz6dWQrFUuvA210PYuy6vfmpRqwzAREw0PFt6iESYHxLDFfkQvgS35N46l-ymeFP4A3w0SpdjGcUhRuiFzyVvbxvaDc-84-3fhRa06KBDe-HhiAYcUXgXD-0mmmXw6QEfMMAqSWbnAPYKQNXbcMdQAVsO6Q89HJDaXEIIpgyKTOZF3zA-DrAg6csFDSKkbYHMJlkTEjLBZwG3pGp_J4U-yy9IaMrOtuE-sOAr3PPOc4kj-Ns6hcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=X5dgrrXDxCyd-baErgz3YCqBn-RGn8UuJmk4CkwgJL4fr-q7mjB6S_UVE3-G5eOAUw6Vqmz8vBinq-XagMuDb4tzRz1GEui0dyz6dWQrFUuvA210PYuy6vfmpRqwzAREw0PFt6iESYHxLDFfkQvgS35N46l-ymeFP4A3w0SpdjGcUhRuiFzyVvbxvaDc-84-3fhRa06KBDe-HhiAYcUXgXD-0mmmXw6QEfMMAqSWbnAPYKQNXbcMdQAVsO6Q89HJDaXEIIpgyKTOZF3zA-DrAg6csFDSKkbYHMJlkTEjLBZwG3pGp_J4U-yy9IaMrOtuE-sOAr3PPOc4kj-Ns6hcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇪🇬
دوویدیو برگ‌ریزون‌از استقبال هواداران تزابزون اسپور از محمد صلاح به محض رسیدن به ترکیه و رونمایی باپیراهن شماره 10 ترابزون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27230" target="_blank">📅 22:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f03bqIpc5XJx7tJilsLkXYPJWSHdawwSonbEvrK_y010zU-1OBJw_-Jw3Gj1bMUX4RnZdOvWLRNiidHs4iUVXulTu0SufTclhEfE7kdYx5d_aMa9W9S_7KRp1MZB9PYSYkMQZA2u-UM_6NLALtailIzTh7QB20wFjeH-gNczUz75V4UTmEN7qbr7a9KLvtESLkVepViNdCfBiDKnVWytxzY8k9Ki0TgAypMxLTEc4jYYDTnh7NSecjIT64sdYZsByWvWkYRdUtV8LHH_CK2RAKzv0TlUvK25tnTuKwqmQFFadP5Wb-OfpwG-GKTKb45bY3CUPs4AU0NJeTIfVKsKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رونمایی رسمی رسانه باشگاه رئال مادرید از وینیسیوس جونیور؛ وینی به سبک یه گلر ایرانی دو هفته رئالی‌هارو بااخبار رفتنش به آرسنال اذیت کرد اما بالاخره قراردادش رو شش ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27229" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86333d6363.mp4?token=ZNj64KZdljXAmMs1xPmSuJpm0BxiQ6KH4R4qxPdnQ9PjjIpHc8nGCEquzkvoZaYq9a1sVm1po4WuyzaFd5GDyvLI8A7PLIb2D8i6AlsgjCn26a1jNvB8zgPPNbyk8Ljs55Xs8TEebx8lIXZa2t2nyxLL7H0BVR0WHENGASHIueIA9G5iZ-jZf0uRR5Z7VxTvYE7SKSb6VsxyRGPS475LMP4xDz7B6VQGb6KzjqJIxliYAued4x3S8FMIPJax3eL45bWNTWPJpiwGTeG0xi8AXjjZhCAyZBu5fiHR1ZW3tP_Kh3l1lnaH6kHt-7Dl6peZz3m4dOsW2euuLNhKysomiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86333d6363.mp4?token=ZNj64KZdljXAmMs1xPmSuJpm0BxiQ6KH4R4qxPdnQ9PjjIpHc8nGCEquzkvoZaYq9a1sVm1po4WuyzaFd5GDyvLI8A7PLIb2D8i6AlsgjCn26a1jNvB8zgPPNbyk8Ljs55Xs8TEebx8lIXZa2t2nyxLL7H0BVR0WHENGASHIueIA9G5iZ-jZf0uRR5Z7VxTvYE7SKSb6VsxyRGPS475LMP4xDz7B6VQGb6KzjqJIxliYAued4x3S8FMIPJax3eL45bWNTWPJpiwGTeG0xi8AXjjZhCAyZBu5fiHR1ZW3tP_Kh3l1lnaH6kHt-7Dl6peZz3m4dOsW2euuLNhKysomiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
دو گل استثنایی و مشابه هم از ارلینگ هالند غول نروژی تیم‌منچسترسیتی درلیگ قهرمانان اروپا؛ باباش گفته‌شاید درآینده‌نچندان دور این فوق ستاره نروژی رو با پیراهن باشگاه رئال مادرید ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27228" target="_blank">📅 21:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27227" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOiht7_aVuCan4sYy6B5ggK1sHZfhrT9FpJ21DSi5RXSycvlswDUKCBZbtjTTCxG1GH8EM46tObXSypP2Bqk_smhWlMGhgLr6OnEtnieT8n_-7ZjAFV8uDqxLoZOM8IzXdVAzo1WfIjI1iZTXJUhCHRA56wpzJuOwnNRJlGJm9Vjne70gwwT3GASXYLaGH16DjKg4FGqG_gSvABOf1MdVrSz1Cd94s-S7gh53px5tgbQj8VEkZP7w_GOBLjYhmJiW7WVAc4FYwOlced8fzr5aYS-KnJasIOXCSHqgG5_8DatSHHdGN67fe2c490YI_KV4FXOHwekYmm8SofXOhz7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رومانو تایید کرد؛ بالاخره بعد از کش‌و‌قوس‌ های زیاد؛ قرارداد وینیسیوس جونیور با باشگاه رئال مادرید به مدت 6 فصل و تا سال 2032 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27226" target="_blank">📅 21:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIeS1rED7b-2nkCPMOUZKopiYIPQGfhTk83zehU1w6_B2eqDlHfii1TC_Sd0tF3hW-tNXtErfWGgmDYclJWjjmXS7ulgwB-H8DG17gS2AIrFqOBdr0-QixACzwN-NQlSnX8UN1jzLbCdbfbuiZ7kGo348cgMv3KONrwJdnhXVVO9bUlCdbrxKyRBNK5GelVJvCbENQB-B6EJFQGpne7NEkp7w7lsLTe6uZdEhULt8j6VEV71YO-_nKKuVObVcA4t-JCO0jJ8xUA0g-ovb9bLW6lut1FqBiwnzAGAnrxUoudO-ZaWRjiX5R3mnGCgGLXgXmgSrCXSIaLx-LeBS47bpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27225" target="_blank">📅 21:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKCf-WNPw85Bk-3J3ekF7zhgN_gFrXcqk6bmwP7ujUdEAsdfvupR4AraWivbGTvijjzxW8kSKfaXCdvwVQ_l8Ld5E3P4PojOKGw5NyXNCqOmrxfyRouhY_h5JgrW0ViBBK_p6ZbutIjOA3FplW6WR0P4PcS7mHZKHhC9gF8zf3gIXbKTDN7jxpNC_XT4zuvAtX_M6gCdXu4owDbpqeZtPaT1QA6ky3DooMAxi6eNaTAs4lqwnwyu6Aq42c96d-zXj4_JaDDyJyWGKV8Zw1xeEUJd0yjzwxcMdp31Yo4mDBvMt56xxbofH5c1hYN05bI8wyMPsdYC1YdAvjn3R3zCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تیم استقلال امروز دردیداری دوستانه با دبل سعید سحر خیزان و گلزنی یاسر آسانی تیم استقلال خوزستان رو شکست داد. حردانی دو پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27224" target="_blank">📅 20:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r188gycIaO_Mk-Vrh4T154qosT56XI7pjfgCWTpaKMXLJcSioWh80aCmGn7aG8Gx7w8IjdAsMdS76OmACR5B8dE7jbH2edU_fJqc049_bgZwcDFP3Ne5DhUm99UE1OlB-X3G6M2haNUblu3uXEi_eh8RZBvgNgK4T9nLyJhicrXebEmqZFX1fhq7Hv9FAoOFInKjYL34LQ-wLqWmht6NXbOvKCZ-67ZALxKaIUCiew61FNF0Ag4LxqxLFf_eTdZX5EReRNmnmQp1iqvpmuS83D-STPLA3zA9_E0Hnrj2BC7M-OP02LL-wExFjVKUKpuK82pnbrrXwwp8e6mfivTYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇧🇷
#فوری؛وینیسیوس جونیور ستاره برزیلی رئال مادرید دقایقی قبل قرارداد خود را به مدت شش فصل‌دیگر باکهکشانی‌ها تمدید کرد. باشگاه بزودی خبر تمدید قرارداد وینیسیوس رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27223" target="_blank">📅 20:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=d65gl9lr9pVuiv9OSk4FbqUFiIClq-zWmic2eTQux7-SAzBUa5539Foreas90QQpJIKjogkfBcJkH3RHHRVLHsLI67MYlSZ6rlG-rT_5opBwD2dmGwiVsOcwdLCGkIZhDpJiJZ1lMqYISQCuFw7lTUPjn8gTHJl5ZOOkOCYJyYUqPaSBAHrg8wvWAXKnp_qL2CpBVcO15LEIRQom9JHoZuiSUneoIIEE4UkrLYhcvtq90U4u25C83GXhG4z7MEI2VKi7Ven1qu_QQ1Wn7qvy_wabbh27rpdnYGP29stZaFOv4MJID1id04f4umq-jKzQiCHnu0PE8To85AxyUIG50A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=d65gl9lr9pVuiv9OSk4FbqUFiIClq-zWmic2eTQux7-SAzBUa5539Foreas90QQpJIKjogkfBcJkH3RHHRVLHsLI67MYlSZ6rlG-rT_5opBwD2dmGwiVsOcwdLCGkIZhDpJiJZ1lMqYISQCuFw7lTUPjn8gTHJl5ZOOkOCYJyYUqPaSBAHrg8wvWAXKnp_qL2CpBVcO15LEIRQom9JHoZuiSUneoIIEE4UkrLYhcvtq90U4u25C83GXhG4z7MEI2VKi7Ven1qu_QQ1Wn7qvy_wabbh27rpdnYGP29stZaFOv4MJID1id04f4umq-jKzQiCHnu0PE8To85AxyUIG50A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌ای‌جالب در بازی دوستانه اخیر دو تیم رن فرانسه
🆚
گالاتاسرای که‌موقعیت استثتایی داگلاس سارا ستاره گالاتاسرای به طرز عجیبی به گل تبدیل نشد. این‌صحنه سوژه تموم رسانه‌های خارجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27222" target="_blank">📅 20:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_1cTwyQpC11F7oLD8adFVK3fczoZ2nboJNjtfM_OUEtqRC8DGjtQCV4k6vWJkACEqFq1EB9AabopTDUWf5dLm3ggTB-E8D0ng02ydA-2kGCC7LGxe8htFt4yDIaY4YKzRKQeJYto3jCJXL-jh8eB2pFnfoYlVK6NvlWWfIrCxEbmWJFDUMWD20oNChH9KHwch9U6qnUTT7zgXiNWxLpPsoV629vl9Lsicvu2osalK1A4hPtS6OcKHeutFd7C6J0IEadxLbaFe2a0X_iO2-pFteE-XaNHd_hpyq6QrHWRAubQ5sa8zaK4Kw11y8Pc-llTkXxQmCNPBRswZf4vAziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27221" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szbCs95ufRBqXrtUQdfp-FCyRWPl4lHut3gC52z1TMTq5vf9H2Wm2QEL3ngC0tsUP5-E6EQdyqDW7gj7RbTOhAqhSsd3ZS1GgkzHb9xPAc1d0UDB86Hcap4EM8uMof7wmD70-OqmXDafRsBvd1-kJAfcsb_pkYHD9kdFQWn5SBoBR77LoHydaJtYO2cBIVYIgYEyH5YYJLcpYMswM113nq65ev78LftlScji9unGXWNkrrUZlWO6mrxEe8xUHNbTpT19Gahoq--P0Cde-CLLa4lKWYFjRQB17hS5QCV1GMWZrPVp5GJLUTOR3tcrYiJtVsk-FT3-qbyT8GVu81UNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رامون آلوارز: وینیسیوس جونیور و باشگاه رئال مادرید بر سر تمدید قرارداد به توافق رسیدند و انتظار میره تمدید قرارداد به زودی امضا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27220" target="_blank">📅 19:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOLacb3tVuEaIiQL2wi6N1AR59DCWGKr9_ZsF9w9lHg1kb8h5Gg6BQvhcsf_KOK5wlYcXE0mf1DpkqSHg1BHAJznIFQ3-zl6z5Sdwlz_fS-LRupOxmPB2kAEoJljJKfBWs7FMQOPBd0UkHJZ8vgr2xLAG30qHiJKn3DGFRQohhEgl8ekiFSjGPRFnmj1ZxGc9EWgtpAXs0xxXAG3p-_ZURlXtLRqkgAVBp2kTLoTehUw5xO9e5r8xUh8QaGWqXkAwCLipU9l_FNR5UslsbgWYjlsr1iqgV2VjEJDMRMC9uy9dBF_oAxH9MbaBGSZ_yrx1DxNgv_Wr1pFoRwYrJGLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال به آنتونیو آدان گفته با منیر الحدادی صحبت‌کنه تا او و همسرش رو راضی کنه و بهشون بفهمونه که ایران امنه تا برگردن به استقلال.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27219" target="_blank">📅 19:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZXQSYKSQrPzRBJp-8_c3C6cTqW4qcFgORaEc_K6qLvu7ATAbndL5mfJNFXWZKypD1OfI4U7CGRIJbv3pSTHOI0Kwnl-z4SAbFJV-i5aUXhc5XXOchLu8ZxQRbZzOlmJX-aRSCQXYNDKuqC0ITN_G3uQDxWHLjHZuRT7iZGo6gVwogl4zlftD_EnxOOyvuOcjGYvwYDGmxwisfHSZN_ABWk8pvEleiSzYJhwfLjzULNBwwsovEHbI62lXug8TgDxCKVJ0ro-hrSGbDHicuDoyFeYT36jkrrHwg270rp2dvwAs89aRskqPl-9T7NoB8Xq4GydGKNcmWtRvXD2lSpBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27217" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgBCjiuoYzaChTrqv8GOBRhWIW8oRFS-0um6zVfvDIGwMNktrwdjDrK-Rj8nfb62RRgi-3MbEMYNER0VSjAWCysHvU7EtmxvgTpXI5dMNzhssC_ViLDmjnWUsODh05TPw4BQD4fTNu037TameicisAAdGbrc-fyZbX6xvBF17O91uvykRjJrkZIwoy1xgbROI3oAc_u1qBECmF8OlOws9GMa8j_D6Mf0sp09-H4gr7mzZ-iAlnsVwF1i3syWjeqUnL2tabxzRaSX1rCtPkQd3HkbrPS6e4aN1-c1kjzvDeYWFqJDC3m7ZNSzN4fD-CeA5Chl7lEeFSeqOYlwRrS-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27216" target="_blank">📅 18:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z62xmrSooPQzTAVP8J_2qm5TuQ75nFF-fPwQLgXqDWf2WCYtmhvQ5H1gFBeL_XvcbyErjAlDE-gUomhhdKEYhAqaTywY-2oVy82w064jFO2Bk3txZ6fwLJK5mltcCKhF9y0-2DdUWeX5INDLWX7da2G-8GDVOGe1ON-q14QKdozARfrqEIHcBcFcPLdh8W4o7SoIMXGRSl6yAJaFMvFfm-0EhVQ5838s2FtflMqpSQN2ozKwNHIgHtRO_8XTnovRlFJ327q1pRmHa3nElsjrx_O1Jx217cXg-li8-3mc64-rebcbGxYsmFGr5MrOx52uixD5wu0t-x5PlVoNPKT_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27215" target="_blank">📅 18:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf0Ov2HBIjgI7QcWOX2dXcqTCQ8njSJiJ5taEs0fksNfregdl7rUKbMLvaKZumw1-M7WWbNkUn3PvrdZn19P0vZ8hBWPWEFeXdMo4Zs10krkohh_69xXrWbl7h9eaoQ780FjPM07xGIxe8DEGlQ2WYqp14RFouV6T8xa-qg-Fxf2mfc7GpBONZCarITjvm3y1DNrS6rud-DH-zEs5PSKClfrYhoIaSI5GvJ-A6Jrf8V_Ox_FS21Wg5wQY9kEvLJcYvzHW_20LMqdP3WEIq5DCiK20h7LHfxcuzBr-KcVwOzlX1cnZigeF5Yp5-nJfuc54DimudJ-LSJeBeT2NwM7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
برخلاف‌خوزه‌فلیکس‌دیاز خبرنگار حوزه رئال مادرید؛ بقیه‌خبرنگاران‌معتبرازجمله رومانو از نزدیک بودن رودری به پیوستن به بارسلونا خبر میدهند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27214" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgr42q9x4SuKU52o-L0__k-mg2TJH1mzf97Q8kP6MLxVEvQ7HltdNX7-unk6x64xT112Bj6g8yFhvk4xdC5f2civQMJCPGhRU5q3VU3CUcrU2JWI3219o0rHTscfk077N_8XWVmyWG_tbY0-q-OOh7Lg_2GtdPAUCWX5P7yqeJ9yt6cxjFOtlWX-WgANXoQMlMY1wRagvZU8IM3Th-9WuWEwVNR2jJZT0UYTmnxzEyFNYe5FsmyIwJpPs1dv0EBfXRJNmdNdLIptcRtKjT2TMigq_C44G9var1_HpmGB_BSp1HDhobqFQD3SSCTNno8e93H0cgCTIkLOAhwFCTEy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27213" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QylZky_domzSK2hbSs8C-uLebUYKkyFJLYHXOkTxc2ubNrONH6SSznFDmHQ4RxHN0wMn_ll15AAgQGIXhfCO7BOvmkQFPM_n_JqKQEQyEYlw8Nl6DvltUmnz_hAwdIMeNFKf_bY6h6LeU6DyBggxgwAn-RbblhVgaSDZlKT9XjSDxrOqOMWchSkOLMzSyTK8j8UJvwrZTthel-6A4v-T3-wDY1kVIWaeVlwzllJGwZrq_PZPATYWgmyWZu9Uasv3Ga1n8_10iKr0RPsC4Y4O5WzBU9RQKPbSVUqQMJ_5PINRmOEZQXLClcX3wGBf4GY-KyMPCa2MY8pj_qY7BN5D2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27211" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLg-Ouo61JbkzRchKlc4zOdJs6LrLlW3uyAzmbryYkbGHdU_CpuYHZ6SO3ZKfcujZnOXxn4dcod6OQYkrME2M-j4GoNUP2pTJJOfr8gAKtAaknFopCJ8WZyK5fqJgMuiVb1onsRHpPNeimHCCXnClggLcYncwpUC-VFn8qLyhLUQF3K3em-UBVPKhaIQnY4eLv5rCmW7B05tPBWlQ4T28xEbW6tTzfu_OvPJVplqXRwwRnYet8Xrd_nD_tFoF1kkG5YlN9Za9iszZzeOWug7nny4ADNNksf7vczPNpI2lWi3EwCdzpgvIF7G3ZhAO5SVBtNu84xmIM6WoDuyAIqY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27210" target="_blank">📅 17:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crF42GXzUK2FVib2UcENJSS_CvF7SVRNzRA9Kl_bpOFqoh9-EvBtRAO563Myo8sxGsbAAbXz_7lDKrW-8IdI3rhGVqoIZ3re9hGSjeNugXFV20ymJ211fKWact0bemHNgaeKt-9OCHdl_pJHXS2SZbyZbrTTvQgsfueGRBPHamLXfW6T9PmtH_UheiAqOK_HeJ_GXFd7q15urFiPBLO7S8PeMp1Lt-klz3zxrKWlrPV1UyuTwpIh8gnAD0eoOEveTqJpkbr7iup0afLGnPpInLKrpbIWRH9dQJ8jipAPXx5F9xckniINxkpaXLy-sZcroQWC_2wrMAiATQkb_NRlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27209" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27207">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbiDWeR5IJ1ggFdgEjz6ou_1LTspmmuDTZjiOv0QBDHHh0wBj2S-n34a_toO9qi7acx0sdj29_oRbkfsl0r0XxSltq55HhEB7LTWmnrlVsNiGht98FfpmePM6BSJtlqUbtdF3mqkCqQnMgPAo3DMOabgMOy_DZWSV8tlI0RJ_072BetAwx7k8w8YjOS5xjLgydYXtYalF3x16SuDv4aA2P8UA6qCDYx6lfHB9ZwS83Tqsn2U02VFofaBub_OU46k_5sY42ALMpMsF5V6rqXnuWrrmTZkJuU2aC9ENgppmGCcni7TqVHXnovrI6-8OziKQFbV6PDO6zq0OkTPRMxgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27207" target="_blank">📅 17:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=ZoSxqoO7BrTalor_8UgrlPgw33nXzUbv1fbty70th85ElleyPUTGmjcwp2Ey9GFEPVKeqfG9CjhrTyrWdTAke_edE0o6Bd2K30tFTqrIsjNXlXfRt6KGSG7xJpok20Ez4FXF6aZ8-YRpQtFeHcC-QWL2gyF13rVBrHK3CGihUTGKTJ-VeXHtG2seYX_L-rnEv7V664H8TaFZXx-OsItA-afQuWnvOfjHFOlMcpgpr36KI3j2qJmqrdiPVXoqgx5hZT-IdPUKRApsKQOkUfmYgO4ICprXMAX5q3cUVJ6LQ_dUHBVGYEloQPOPZng2jGG43QqimvX8uxhKsEiFx94zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=ZoSxqoO7BrTalor_8UgrlPgw33nXzUbv1fbty70th85ElleyPUTGmjcwp2Ey9GFEPVKeqfG9CjhrTyrWdTAke_edE0o6Bd2K30tFTqrIsjNXlXfRt6KGSG7xJpok20Ez4FXF6aZ8-YRpQtFeHcC-QWL2gyF13rVBrHK3CGihUTGKTJ-VeXHtG2seYX_L-rnEv7V664H8TaFZXx-OsItA-afQuWnvOfjHFOlMcpgpr36KI3j2qJmqrdiPVXoqgx5hZT-IdPUKRApsKQOkUfmYgO4ICprXMAX5q3cUVJ6LQ_dUHBVGYEloQPOPZng2jGG43QqimvX8uxhKsEiFx94zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27206" target="_blank">📅 16:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQI47ZoMpCRZnxtxbS7mmsXq6UHAK7aVheMtPvojYUv_YQU3vzmZUyJSmsXvpg00FmZ34cfyKQRh_LikLT8dvofMsTxRF-syzfVmxwHSgV-0snGP_Bz08NZhHdxdvgkgsiBqV9P1v9urPrsQAF2XHic2xOfcB0VM798ANeTCdV4x3H5bHegcLj2-cFY_MJOiWQkNj2xMQUat0K65vuKodpZtun4IF5bpEo1E2gLmpix-Rm2F2lWRWg_LxpD27266AoBF6YWqB54xLfWXguSSoz0YfkknQ2hJjKsIxAtY1rZOOKR5qHWPV3AFuGtBBPg4qCxs2jUruyV0vaXJz6RmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27205" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxFcu3RtfH4DB7jE41RN3cOWgOavWUnB0FnOr7NFhmymaMTJSaYNN_L4LinmlBYvOENX5WgYNKWzp7k9hGA024r9YfC-kMLvkeHPOveU4q6wx4FUgms1Ysv7F1TETftH_ofjDJKSlYS3WyYFDbsiHdQuDcU4gJEQchSCNZvgt1C-AewUK91uJect7x9jeWP7tUUA4bmT5kqr-CYIJQK6PPPxic5J8HQYi1FNCbvP7Le-mKKL-qVeW1K4epU5PN3YDBmX8kCSIHk3d8dhubrnM65JOsJs_n3YWBAZLnPBIjo7_mATMy8Ft7_qJHixL5Tllam79Dh1Vs0G9ppHaMRk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27204" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khQIFtRox9zwSfLeFDhGcSAU7dYdm5EouEHkj5KnG6EQzpV2jUi0w6PE2dupPT5hI24LuEQBmABr-Xcsium26a8rli1pgX9jlPlvdgxj72btLaMf-MiOf1QgpIjyWLe4Cfi3e-d0S7FRLrLyXdmMskFZQt398AkW1-hESYnryYJuLfgGBLDy9-lBT5m0ELDvmqSSwe8QjVv37rFvceFmWcYCRPdPxKJ3mZoJ1OkRvOC7kpUWDYL5qE1Z_7OQRXs_3ziA0SMuLe7Mq4nvmFA3PhC0RC122KLxl_v4IGjkYtuBAOtfzI8FqnqEyXj4DAO71-zfPAJx_eIZQbbmj8jkeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی پرشیانا؛ باشگاه استقلال برای‌دیدیه اندونگ هافبک گابنی این‌تیم بلیط تهیه کرده و این‌بازیکن‌ظرف 72 ساعت آینده به تهران خواهد آمد تا بعد از تمدید قراردادش با آبی پوشان در تمدید شاگردان بختیاری زاده حضور پیدا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27203" target="_blank">📅 15:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBHW65_N7YBr_CaJcjLMpIoGdCkJBrNE_v8S2SZEzM6uvAb8fgPgo8C2CcT5lJ36rLqh1gwus-H_YCrWM6eP3--N1PqgnNF6kKJ1igatGdJzxc37pkTqtge6sLpJgrolQBtUucmze5jvHPwSYK4jqP_8BwKmlpeY-FiJlephfsYe12pqannEgFdE5yIHZDmtvMmf8q9Cinx5pbCVm4RlF4ncAMaqa0cdKGgEx3EcyfnmLbK9wuKFwOdWz3-Q2JGGL4nuQoxRJrGOfbGTHBS9-Jn0-1kSFPETx74AVnmVgJDq7a6AuN4B-gY6MJBAe_mjSjqiLEl0pMpr2gzfkkvjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از بسته ماندن پنجره نقل و انتقالاتی باشگاه استقلال؛ علی تاجرنیا شب گذشته بامدیربرنامه‌های ایرانی آنتونیو آدان گلر فصل‌قبل آبی‌ها تماس گرفته و ازاو خواسته آدان رو برای‌بازگشت‌به استقلال راضی کنه. به احتمال بسیار زیاد آدان بزودی…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27202" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=lkzj_LHHqI7kqZvY1DUn_WAmHwmu7ZyTGi4OfDeQ3pUNLNNyCJPgmyy-Eyl0b1ky1Q7RaO6pu8XNdw1ojyt9gpRwh2KwhOJDT4p9R_r7oP6NN1RMUsuN-dRSTvXTqcgd9Xz_vpPW-4Jwms-wZiYrCWqZ8K5pia5inMM4hb0-xyX8P9mpVDEn006jWBnapQIvQ2jJJz9hl30Y1f0J7R_5Erij9n6P57OCOBAPBmeeZ3lxQgFk0wnxKxBrv4JJUCK3f41u1QJfuP2l0kvm2Ats2lSZpTIM7obzq0-CFuDXyUHUe9gfaxNrUiNACI1XaphXAJJidaTuIuyHYkb39yhJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=lkzj_LHHqI7kqZvY1DUn_WAmHwmu7ZyTGi4OfDeQ3pUNLNNyCJPgmyy-Eyl0b1ky1Q7RaO6pu8XNdw1ojyt9gpRwh2KwhOJDT4p9R_r7oP6NN1RMUsuN-dRSTvXTqcgd9Xz_vpPW-4Jwms-wZiYrCWqZ8K5pia5inMM4hb0-xyX8P9mpVDEn006jWBnapQIvQ2jJJz9hl30Y1f0J7R_5Erij9n6P57OCOBAPBmeeZ3lxQgFk0wnxKxBrv4JJUCK3f41u1QJfuP2l0kvm2Ats2lSZpTIM7obzq0-CFuDXyUHUe9gfaxNrUiNACI1XaphXAJJidaTuIuyHYkb39yhJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aIJpGbeVa6y1pDcY6rVhyZn-Gu_a6o_3U0VkdkQRa0Ulyg51g6TTFsYtj4tj7c3cz5iH9w4goSQrgEbEJy03M4mZuMIkldcl0JVoNwqgBjK5MPpTfWakUWhaNud_rJfOVRbOjiiQy1np3uVYQajDwgfoJShXUcrNIgEKmvnCKikRTzEaipTxTnZv69_yaFn4aBWww7nACPFVCQV0i2m78PM_jFnbXwvkk7xeMEsPf2ng41bucN5E3GVS6BPQ0qrkdLvsw7SPLmSPWsGcbdhUX5LmZ3QRbYjBo7JZxFD6znbux0gS-AHCZTOdvHQ9cYzxlfWpXoCYE8ct75AWDOzNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=aIJpGbeVa6y1pDcY6rVhyZn-Gu_a6o_3U0VkdkQRa0Ulyg51g6TTFsYtj4tj7c3cz5iH9w4goSQrgEbEJy03M4mZuMIkldcl0JVoNwqgBjK5MPpTfWakUWhaNud_rJfOVRbOjiiQy1np3uVYQajDwgfoJShXUcrNIgEKmvnCKikRTzEaipTxTnZv69_yaFn4aBWww7nACPFVCQV0i2m78PM_jFnbXwvkk7xeMEsPf2ng41bucN5E3GVS6BPQ0qrkdLvsw7SPLmSPWsGcbdhUX5LmZ3QRbYjBo7JZxFD6znbux0gS-AHCZTOdvHQ9cYzxlfWpXoCYE8ct75AWDOzNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW1_P1tmjjkaUTFvHfCOJa6iydGvEMN2ib2kjcMFRhUHcWXp6Vl9BBM6uJg7xIZkUR6ZAdEeCOzj6EYG0EfJ4bILRB2siADjx2L9ty5GDD0Vcl2pWnGmrTUPa1eUmGTc4CFzLwI_UiN3fxaTNXiASHNKZ41JqhcBnuvBB0b5wZOSk619UYVFo2T4vVf-OMFcEEsUETATPV8d_B_08Z50EkX3X7t-BS7SySGS7UOmMPzekYaVQmG9wMhx0CpIBttx7GTSMVgP1csiQE6gslY5qxj9MClFwV5V5sjIr-n0gzSo03d6uye6Te8FRGpww_N6mVRS8BSDoA-tGbTV0s38ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOU3vNwd2Y6Ia5j-fyShWZGE10jGSO7Bw9EWSsrf3DcfCRc6VrXlTRaGl6VZE4gGeNHXKHvPDd0-5HgDkLJAS_981yu4MMNq81XfbsScc7Os3uLplL6KH74RSsZZX8nKF_4-i2T7CNTU30tIuNCe3nM3vGKQxr9EJqtEsMnsNsLP3pLbb1rBHbKT-Fnv5UBpZpDq8bxlXCpkBmN2VT3KVOY3VeI7v40zlHyesEUlfu_Dsuy0w7-RnzqbXMRN3mdcWaYFpmK_7tqLzVkIYaPnSO_zUzqOLDrUTapx6-_7fQQ4wOD483Lr6BYopdqNm-zsrgvUkxK76jZ6kH5a_NQ2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEait06zQbSaOkIfYUl0aANYQDftCB_WjjkxRcRQZC-QMEAp1O70qqKwAxWHSB7_oJpZD9LZ6EVabwL9iPtCuQkwKuTkZicUT2X3c7_B8eETSGpCZh7ylSIpZ1vgMegzzptYgybrUdWes_I2jWO1dgBVW5i8MTXgfj56P2MH0zVEHJb0svrh6ucvC6YdAFSJARhe6dclceNwEkJz3evxk6wQlu7bnmIGQcLweN5qEA4SNa0eZJumleB__6AGg-KuuiGLJmSxMrjeiihaz8G5s_prpL_GRWfiZRAYvKAjMMLCRkg1iWlri-wgE6pluuUujZ3OFqKoE5Rv6lWQMgFXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHv29G2VS5d5eMSKN8KOkUPE7VPH9trDBoQW3XA7Rm4Dv_Zc9qBCOsgLDEcXK3GP7drvuZy4Qcpv_vSg6-1D94xs8GH703IARPY7iTXUSmqBwtJQND7Q-pPEfT-nbrvhCj2fzlw_6FH4vtQ3XQQtDZFrNG8hXDD7FDLTKEVN2u8soA900p-W6IMBT8eNgzf4HmIXxdZeWn3_gOI-32cbIx43xHRcO21mQsAkvNa4zJCyREIOuxntC1JQ_LL-T3l64ZrFD8lW1XhXjGvmYfB925TNFx0bcYnkgpU0Ntp9B5BDReIxZUCTjmbThHg-fxiJJqDNWY9gWz8aI_OyKE143V8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWHv29G2VS5d5eMSKN8KOkUPE7VPH9trDBoQW3XA7Rm4Dv_Zc9qBCOsgLDEcXK3GP7drvuZy4Qcpv_vSg6-1D94xs8GH703IARPY7iTXUSmqBwtJQND7Q-pPEfT-nbrvhCj2fzlw_6FH4vtQ3XQQtDZFrNG8hXDD7FDLTKEVN2u8soA900p-W6IMBT8eNgzf4HmIXxdZeWn3_gOI-32cbIx43xHRcO21mQsAkvNa4zJCyREIOuxntC1JQ_LL-T3l64ZrFD8lW1XhXjGvmYfB925TNFx0bcYnkgpU0Ntp9B5BDReIxZUCTjmbThHg-fxiJJqDNWY9gWz8aI_OyKE143V8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnWEdBrEB8lnudWdyK0_AJ03jBfWJPNyyIWX-x2MnUDv1Ls1SO1slc0TpJyXNiiJDp2iIuUnUEXUOyrYe82FfTAcEhMQ_23J75RUREnQPYEWUY8opb-fio1L6weOhq7edK6n8eSun9EABrMLkYTHDtgbMiVpHYhnfpMp-_80VMIlw3yPmfDXrkwhSto_ewhiPx9APvksqlt1ihNDyhCWzfmJbDyGW6xnS5OF83fAZl4UjmB-anEi79Salz578fIZ-xfgnX239Ml7zheuPJaJKRcQ3Kbh3xDdznJrlIShPg2oCJ3JLl9iwbn6Emetyrfc5QjG4V1X0yQI7KLm5xn4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy_caqBwscqHrH6Mx-my5fxZSLvTVsFOx2U1vAqtrz3yhz-mgXxpbCQyng64RUzwG1FMwWVR7Pqjty1dvPV46RRvQoiQElni_OKkOFChChs1qI8qWJ9u9C6XBqbKfVdUCmlCrNWiAA1drvwxRpneQYa-KkzzZvCtZ2NttC-jAnSOpFPFNGaSVe7T7YLiNJU3tjohRXPl9GLx1YdemsjWy3-tg78zleUMYkRO93mc2j2yXorkzpV2hN4zWxMo_rul5hmX9KXuy-yc7glNThJlOVjCgdaW4o2u3aYq14ADpswSG8KrUUaxdWc_HId86EdCdlk7AjlpcGcGyKIdCzLV0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV007ya9ACXMTHvtkpui494IdICha_HpFgCZZzkQiamSecqtl6ts9s6uM84zms5HGG4gDfYrLTO9Ggx_W8vtphtARK0l8KmK5gTZfCgQpxafWC2Z4y0RYOjqN8S9spfOxUpgT1RRQTTmysKz9IFFqLrDuFQCzXjeJB6t2U5U1I1PcM7H0iku2r_yo38zgFIbOCJEU9mngkOWH0BWr7STCJF3y4cUjwqDUkCxh4qcTiE_opAfU55hcjxrkc5MbW6ngTlAylHjaSDy8b6vGFsI2CqIORNewUdJ5UjO1uB1dznBjhH1KrHtv1xL57a8ukNzrggdCSQwjN9DPq2eZgnnvCH0_80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV007ya9ACXMTHvtkpui494IdICha_HpFgCZZzkQiamSecqtl6ts9s6uM84zms5HGG4gDfYrLTO9Ggx_W8vtphtARK0l8KmK5gTZfCgQpxafWC2Z4y0RYOjqN8S9spfOxUpgT1RRQTTmysKz9IFFqLrDuFQCzXjeJB6t2U5U1I1PcM7H0iku2r_yo38zgFIbOCJEU9mngkOWH0BWr7STCJF3y4cUjwqDUkCxh4qcTiE_opAfU55hcjxrkc5MbW6ngTlAylHjaSDy8b6vGFsI2CqIORNewUdJ5UjO1uB1dznBjhH1KrHtv1xL57a8ukNzrggdCSQwjN9DPq2eZgnnvCH0_80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUBwct4YgiqkR9psd0EcN1zCVI8oog14PblrcDiwJ-_9rFHMlEAarv4D0IyJ1hs05OTdCiXFMGqcffz1ElJthQlSAKCRzWNgxtgRj0g58u4X-b7a_xOEIHIZbMvLB5_YyXCTkKhYLbSGy5b2FBtN9S_n4vG35NCKqrTuOWvCgJ53pmPK1cNT8e4SgzfMVXN8-XMNS1_dQeCNi8x3kHARheyRj7dR2e2XzCWFhuGaU9PlX__V6quKsyOXuynwN-ModVIIT9DW_UEFEWbZDJoXXy3wS7SuocupxXHiarEZYXk7dYZr9-4yNhBz2mrdPpczO28SHhuCOHgCjwMTJQuNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=iwptCqcWpwCZBIUQv5LMD-nwQ4hG7PBAw75dSqcJCTki5N-qZ1FpxmrF6IyQJpzXwz6n5Lq9iX1ZrKiaW2Nml9A_LXUx22I42y6eDHkoa_7X8DyiAruYELGgxnrUNQ_J7lfFEn8So2MWP981i0eAd1E6fqWNHV5c2zfyKqOF0M6roVbGbUtVDsMf3DTZl1it2ot8Q5C3ca1Vrw5QH1jYBne_zgU0gvIUAAO2VyQSCawQuStH2MdUTTdKpZBIUbwN_0zDnbVNnYoLgC1h0-uCKFwbtAxglU7SZ2wF0ozD2KGOx_xyRjLsZJO8HP3P2b5rRvJBb8kWNr49b28j6mHsYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=iwptCqcWpwCZBIUQv5LMD-nwQ4hG7PBAw75dSqcJCTki5N-qZ1FpxmrF6IyQJpzXwz6n5Lq9iX1ZrKiaW2Nml9A_LXUx22I42y6eDHkoa_7X8DyiAruYELGgxnrUNQ_J7lfFEn8So2MWP981i0eAd1E6fqWNHV5c2zfyKqOF0M6roVbGbUtVDsMf3DTZl1it2ot8Q5C3ca1Vrw5QH1jYBne_zgU0gvIUAAO2VyQSCawQuStH2MdUTTdKpZBIUbwN_0zDnbVNnYoLgC1h0-uCKFwbtAxglU7SZ2wF0ozD2KGOx_xyRjLsZJO8HP3P2b5rRvJBb8kWNr49b28j6mHsYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=oR9noRat4Um83tU6Aj6XjGnbN_4G2MhicugelEEHAZUH0Xu3uzsMhC2N8uCIBnLaO1idSzox6f1I3AKxCiZjYYll3jO9UluHnCkY_rosOjW4CYqLG7uJG196zNImKCoOohckl3zxZ_emANVgr5ciYahyTHmvimOF6N8XaCIYSs42V1pg0dExIx9EY7aYnhfH0JaYSmfqUKQWVTzLTcGQrMl1K4avWd2xTDDcbHZ5GbSzVxfFB6cQ45syl1kn3_0avXnV00oMy7ah9N18F-v8Zi-L07jNBQ6b0FRegJPmnDDIQiCUlBr95-i2SnQ16prCFR0Dtrx0IRzel8AisM8bog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=oR9noRat4Um83tU6Aj6XjGnbN_4G2MhicugelEEHAZUH0Xu3uzsMhC2N8uCIBnLaO1idSzox6f1I3AKxCiZjYYll3jO9UluHnCkY_rosOjW4CYqLG7uJG196zNImKCoOohckl3zxZ_emANVgr5ciYahyTHmvimOF6N8XaCIYSs42V1pg0dExIx9EY7aYnhfH0JaYSmfqUKQWVTzLTcGQrMl1K4avWd2xTDDcbHZ5GbSzVxfFB6cQ45syl1kn3_0avXnV00oMy7ah9N18F-v8Zi-L07jNBQ6b0FRegJPmnDDIQiCUlBr95-i2SnQ16prCFR0Dtrx0IRzel8AisM8bog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ise4MtItvG8qaLX1ExFHnH3v3GzUvlddQJ0qc1hRQ_5lW2bdge0J2LwfiYXKcMy2OJ74WfYcd4__ttH0PR51fAh_d5Eu0guGo3kaCFJNRiWIctL3W0mqQqqUgU0hPx1gHlvDeoqcKFwefW0fiuU-iLFPPA3vxbIlm8FmZDRhpHc4VbFIPYswf6R9c2Hl4PekXI6ghNAYigtY1mYyil6Uot8WafhdOln-bUW9Q-1LeEgYAMQ7ctTMa1dZ8DTgk_VVf1U6vc9qnpG3Saf8SviQgJ11NXCSZiNjqkpbRQ0xvAhHOEL9SPw8IMPn-_mad1OpelnXpm9YzrEs7WqIdoAo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
