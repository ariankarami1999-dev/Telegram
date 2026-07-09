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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-669218">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رد پیشنهاد ضدایرانی امارات توسط روسیه و چین در سازمان بین‌المللی دریانوردی
🔹
روسیه و چین در نشست «آیمو»، سند پیشنهادی امارات درباره تنگه هرمز را یک‌جانبه خوانده و رد کردند؛ این دو کشور با تأکید بر اصل ناوبری ایمن و آزاد، با این اقدام علیه ایران مخالفت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/669218" target="_blank">📅 20:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669217">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e8dde714.mp4?token=Gd3YCWp1GI_2rrdDMNratWta94CrN7bMdO6qTGKADQrzDnUNKrq4fEcrlAsQLF1O3DuCTqKoOAnxhw3osHQKxCnXCFxBT-zCfGAIJAM2BxL1QQwHvkEw6TO3EZ67-CBL2_Q5ocmbNuAORxeXalFiQtQAZcxg4wGULF8eGqyUtNTaFMvlCvdLbuxCdwdImY2GLXa1riquUnt2q9EOo_AbwCMKtLsyXNYExZmrPK7pKUFaJ5ud21v1yp08OLamV7kARGW5wcMATz1e16iHLkxXl53Osw7BGXzAtqhUqRxrBKCori3DG4-MvwNOcpYS_hauSy_gIYiEl1R-lHNHLGxDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e8dde714.mp4?token=Gd3YCWp1GI_2rrdDMNratWta94CrN7bMdO6qTGKADQrzDnUNKrq4fEcrlAsQLF1O3DuCTqKoOAnxhw3osHQKxCnXCFxBT-zCfGAIJAM2BxL1QQwHvkEw6TO3EZ67-CBL2_Q5ocmbNuAORxeXalFiQtQAZcxg4wGULF8eGqyUtNTaFMvlCvdLbuxCdwdImY2GLXa1riquUnt2q9EOo_AbwCMKtLsyXNYExZmrPK7pKUFaJ5ud21v1yp08OLamV7kARGW5wcMATz1e16iHLkxXl53Osw7BGXzAtqhUqRxrBKCori3DG4-MvwNOcpYS_hauSy_gIYiEl1R-lHNHLGxDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیبک یا حسین گفتن مردم در حرم امام رضا(ع) برای اعلام آمادگی جهت اقامه نماز بر پیکر رهبری شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/669217" target="_blank">📅 20:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669216">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1791ea9a1.mp4?token=Z-xafZIIv4qyMK5HonSacdrQb7dxXHUNqX8MEt93lBAbOB87ujW-ZnT7rjLPTvv6InMY08jsIl4QaFIsPdbqlYQMNCbIq8fF_c5-fdXUa3ZM61QCX9eVd0J2Van5F5frTl39qvp_VyMdAJ0G54gCeMmb3zkn4QJJyV4fC5b-Y9WDHEXGIG-s6Sy5LXhYwQqBa11aSxK25ZaAoWCc72w1JQXXwDPOfzzGcJghG_HBuBcOzReEV57a1geM0TX3k0TByQRWliL5TAnWS0Ign-trBxqkDXE8kMAA35jTnKINM9Uc_LTCHBPwYb-5UL11HdnmLj5xb3ijW7NEKJDPAt4i7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1791ea9a1.mp4?token=Z-xafZIIv4qyMK5HonSacdrQb7dxXHUNqX8MEt93lBAbOB87ujW-ZnT7rjLPTvv6InMY08jsIl4QaFIsPdbqlYQMNCbIq8fF_c5-fdXUa3ZM61QCX9eVd0J2Van5F5frTl39qvp_VyMdAJ0G54gCeMmb3zkn4QJJyV4fC5b-Y9WDHEXGIG-s6Sy5LXhYwQqBa11aSxK25ZaAoWCc72w1JQXXwDPOfzzGcJghG_HBuBcOzReEV57a1geM0TX3k0TByQRWliL5TAnWS0Ign-trBxqkDXE8kMAA35jTnKINM9Uc_LTCHBPwYb-5UL11HdnmLj5xb3ijW7NEKJDPAt4i7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در حرم امام رضا(ع): این همه لشکر آمده به عشق رهبر آمده
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/669216" target="_blank">📅 20:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669215">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
پایان مراسم تشییع و آمادگی برای تدفین در حرم رضوی
🔹
مراسم تشییع به پایان رسید و عزاداران برای اقامه نماز بر پیکر رهبر شهید و همراهان در حرم مطهر گرد آمده‌اند؛ آیین تدفین در رواق «دارالذکر» انجام خواهد شد. زمان اقامه نماز لیلة‌الدفن نیز از پایان تدفین تا اذان صبح است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669215" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669214">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9sIxAVoJ3R0542czw3tbCcYtdcu-XORONIxkSICXedE5wiuD72W0yPee5OLmfwrfLxFlPkYPEr5A75C9zkRPgxtrRtjfmWqCqyayiLay7hAuzL3VwpTnW-fbo_ErbzyYKxWY1YHdGg3ocgL9scraHTaEPQ2b55CPmBgSTwOMdav6dlCvJKD8-_DlCEFDu1h1UV2mVxDU9uSseWvQ-QpvUI3ET3juXrbogIF8SyvPF2AcZLm37CDlurZOaiq6fxflUj9mvrD5ftd_wuJldFTcJD3bYK8cKwaYx7BEunuL_XgDNCbpmDkthzwzLywgzGvM4ckFq85oOGPF_zKaGUfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه دیجیتال اخبار مشهد با تیتر "مشهد برخاست" حماسه امروز مردم مشهد را به تصویر کشید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669214" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669213">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
تلاش قطر و پاکستان برای ازسرگیری مذاکرات ایران و آ
مریکا
سی‌ان‌ان به نقل از منابع آگاه:
🔹
دولت‌های قطر و پاکستان در تلاش برای میانجی‌گری جهت بازگرداندن ایران و ایالات متحده به میز مذاکره هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/669213" target="_blank">📅 20:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669212">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
لحظاتی از حواشی سه روز وداع با رهبر شهید انقلاب در تهران، قم و مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/669212" target="_blank">📅 20:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669211">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
شیخ ابراهیم زکزاکی، رهبر شیعیان نیجریه در گفتگو با خبرفوری: آیت‌الله خامنه‌ای نماد مقاومت بودند؛ ایشان همانند جدشان امام حسین(ع) خانواده خود‌ ‌را فدا کردند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/669211" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669208">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuihFBZ0r5LFqaw4oBJvaqNRZQvuonF82tUw1zvDEs3l-U60DVLK_71XG_lBmSVORe2hc3LYB-BMnBcFxuUSLU83iZBdAxtfxJSPr6MAIyrYhv9JJSX7qsxwd2jSCSHN_R4Uy5UMYzSosLXMTgSft94ecqEIU-rzQ7irLHMWx_YzItAWmIW8s6qVa9DG2l2pUQ_hr-jhw3yYzpexNiBdoZk4zeyvRU1HLhnP-SaUJqzclyWFX16qDAOTNFH0T1wPR2aGb1h7iA1Ndl99mZZ7a8FCh-OtEJmOJ9tiN4AKUGHY0OLRIcYOHKmfXmZJ0aZVojE2jK0C2b2x3DLiBIJOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در راستای تسهیل تأمین مایحتاج زائران و مجاوران انجام شد؛ فعالیت ۱۸ بازار میوه و تره‌بار شهرداری مشهد در ایام آیین تشییع رهبر شهید انقلاب
🔹
سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، هم‌زمان با ایام سوگواری و برگزاری مراسم تشییع پیکر مطهر رهبر شهید انقلاب، لیست ۱۸ بازار منتخب میوه و تره‌بار در سطح شهر را جهت خدمت‌رسانی ویژه به زائران و مجاوران اعلام کرد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی شهرداری مشهد، ضمن تسلیت عروج ملکوتی مجاهد خستگی‌ناپذیر انقلاب، اظهار داشت: «با توجه به حضور خیل عظیم عزاداران در پایتخت معنوی ایران، تمهیدات گسترده‌ای برای حفظ آرامش بازار و سهولت در دسترسی شهروندان و سوگواران به اقلام مصرفی، به‌ویژه میوه و تره‌بار، در نظر گرفته شده است.»
🔹
با تأکید بر نظارت مستمر بر کیفیت و قیمت عرضه محصولات افزود: «۱۸ بازار میوه و تره‌بار در نقاط مختلف شهر مشهد آمادگی کامل دارند تا نیازهای روزانه مجاوران و زائران علی‌بن‌موسی‌الرضا (ع) را با کیفیت مطلوب تأمین کنند.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/669208" target="_blank">📅 20:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669207">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تکذیب انفجار در زنجان؛ دود حاصل از آتش‌سوزی سوله بازیافت است
🔹
معاون عملیات آتش‌نشانی زنجان گزارش‌ها مبنی بر انفجار در این شهر را رد کرد؛ دود مشاهده‌شده ناشی از حریق در یک سوله بازیافت ضایعات پلاستیکی است و نیروهای امدادی برای اطفای آن به محل اعزام شده‌اند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/669207" target="_blank">📅 20:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669206">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5Loamh5ffkGd9fkwaHjOSUPP0r6yz_UfS9HBGFKK8Y2DBjb1271uCEEI_loDMWRaNEm_v3uGfV9_uNxlHt1bnMtWA474a_4GafISVq0n2m8Yen-0rWoyU3zQ_-mZX1gZfTvhDRbL4e2JNK2V5YxQX2F2q71f3WskPeSSGhZlwc32f8H3xZuRgrRB6tHxWQcMEPd-Jpneo7uU30eWLg0VizOh_aoSGGrOUwlPajTjINV3LDZy7jgIlSdtqlPMF1soqUXUDyE7OY--rqPlfwvN7qUPSspOiXvrT4_sHxUpmkgdFANWU67ZxegJmp2kCp_gdWjWeBFFYlRcmamGRucSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر رهبر شهید و خانواده ایشان پس از آیین تشییع و اقامه نماز، در رواق دارالذکر حرم مطهر رضوی در نزدیکی روضه منوره آرام خواهد گرفت.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669206" target="_blank">📅 20:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669205">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تردد قطارهای مسیر تهران-مشهد متوقف شد  راه‌آهن جمهوری اسلامی ایران:
🔹
به دنبال حمله جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669205" target="_blank">📅 19:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669199">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUy261WUxiaoz7me2pssvCJ8Tzvdly2Hmz2LA3Vz3txxDM4XvzkgWAlpK40ySuMsw6zXBCU1_Xm-lThHV2u_IG42upnW6F293xoWka2tNfnrYo78-OvJLmuhvd4rWLAcePhx6vcpRFzQOG9yV9-39cY33O6RvweFHm8v0S2aSjnV9GfHaTx8d4j5qry-vmTXTipp5F127Z6-1_xXljf0tLz4ojXrxd2z9vlcJtCvhnLqD4Nn6oLAqrYL5UTmGcpXnyWAOL_31xLfHatLLIAopupvzhRGXSosYTrzX6cM-VlmXn9Wkhezp6ilNQt7j-lISsKSmMgkkY1lPwA2Or8yeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nkdOWWo69CraZduRB4qSVOZDcYh1EaJMww9SXsPednxIdvOJRZKuOmpDkjY9xr-WruXoTobp5HaChh3W9YwtWKsVfyzj_8ckr-h-Wyb4Q5DYzAa40cKETc94V3Tvmo0JeCPSVkydZb84fptev2j9Stb_boD0aq-dW76CDlhH_AFHYJciLNMfImnaYBYyRo6Tph72TQTEXfJGAjWx6MZ0Xzerob0bbxPGmKqOi5O2oeg40jlw5EY1xGZLrZxk7OXXjrXI4PDkV6q4mVRKPKkzdiO29wRVCbF22mlHFzNMH9Z_hrjScArGhrXRHWhIW86WotlT3vM51rIK2FdwDvtv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bmvq3u1SbhRPc497W5Ja3tik3_lv9GhFVq6f8YY_-GqZwgDTX0Opi5GBO1kKzs8pIbBbL6T0g7Eo3QfMSzH9Wl4fb086f9QkRi8zxYxzrHeseCY5cxNYq31WUWjNdUEjIE5BLHVymhxvGmxqjUi-Aj-SNM54ZdDg-nl-GE7p0rRNKLqjpvYB0bvlxCazgrudWT8BA6hEK9O_9r9DY7HVJumnb8dFvECDRJtADR1oeMcafaIRgDNc07n9r_xlTZ2gZAlW9XWHn1fVVkdTOS1_aZ4uqZrTVnmRKs6hXw6SIn-sh29-Mn-tSmQzlSkDK8cJ9IywGEG8_F87HtSOVCVxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwteKgnsK6SBO9nxIv_dpbZb46ZJO-4sL0FIAL0Z9ypOLF1can619R2xvxLIvIzot2EVADg34qxcw82hifHgpsKf6tMIiHM3rh7R0nTVTN9P_KI3ZPMbC9VIqTRuGsFiTfX5aHMlsEnnsdud7anFCUbaLs-mKcX_ev7E6D5ku7UQwiOC3oh0H_B1X7HYATSg3pJTE91IZU1sRNOyUMPYO2KGdeYzWbhyN0WhZatUHP4F0Riw0izPZaTQ1cumCArrb4HLCfys9qTNNc5wgWgFAMSaEWZAL3jsQrpHwvnAiPXJ1vX6B1onzm29c_06YTb7tBSDKdqrc7V4Agleqxaxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YINQJ5XvhTMRKJ_eKZlFMiazVN62ZoisjJBC8VtfniSG3RIG9gqfhDzcuCe5iIi_l51m9uDiqupfoGcmumP-Ox1gpbyZxoyfvEf3Wf7eomKyS5eij7hxjCp_2HoF0qUAKsRrT5XDDq2y1qXjMOEdH556RR58HdjUvatz5o52qpyo1uQ9jGKeyLMDq9MRxIKljpVp61oYcVaZKfCg6g4T0b7XNAM88WRUFEyDLzhUoqbQx7RcbZPfpiPbifZR6cC2mTqcFSdMURd3YqGeIShiKbs73xC50Owhbykq8dqMbd17jo0uuDQ2luNU2vhOpQXWMX3QESQSt4On6JBhZ6NOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMyc5OI8cQ_qKT-LtmD0AZYmH8KFJ7xTrUR3T2mX2uEX14X03dcZ4uB_BDn6SOpOTdxplz4FWISgarN3OKhbl0kHwbpuzwnCOelX8r00xJY9THxu4GgRNJkSK4mo9uDy73E_jvxR6Np66GH8yvKz7P8Rra-0bBl9--okOhUW1XGAob3U9n2CoRi0o61JiaUiiwMNh1OAZfhbMl-hmpEl_0cYDJMYFPtVrzQrOD1wXis82cA6DC6hVmEW0qQGc7oLlAAciLe4g6G2jlmAxRx1s074ijLOgYebOvT1YFq38CFMq8HotFtdXAuJcxk0jDvXbDAhXAVd8z3lvKwBb5hpfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی حوزه هنری انقلاب اسلامی از تشییع پیکر مطهر رهبر شهید در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669199" target="_blank">📅 19:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669198">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e45b27eba.mp4?token=DohR5LSp0x_sPs25tw7zB3pXJHLmXff4mIxZgVPEjgD2c1vJafA30ASSO2rIdcgo6YGFNr3eg6EPg7efm20EtOHpyySjIyiOQej1eG7BubKwTLFhnRiEpiZUB2W4Yi5ooeye1s-D3ly0m8zLYVg7Ci3oIk2ASjzZb1mbR4yOuObekSwZOZxU6HFLKbj8KRYYbdBGY9GecQojuVYkWEi0cVpjoie0nriuwFionO8frmF3ku1Fm5-SpkSDeVHf4_7fv0ZBZr_5OKTbAor1cGJM7t77unBKJXl0Rn-atZOhgKzqsh-06sgRPQXMzBpDIzM2ki9dYSa0vMjle9ATwc7-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e45b27eba.mp4?token=DohR5LSp0x_sPs25tw7zB3pXJHLmXff4mIxZgVPEjgD2c1vJafA30ASSO2rIdcgo6YGFNr3eg6EPg7efm20EtOHpyySjIyiOQej1eG7BubKwTLFhnRiEpiZUB2W4Yi5ooeye1s-D3ly0m8zLYVg7Ci3oIk2ASjzZb1mbR4yOuObekSwZOZxU6HFLKbj8KRYYbdBGY9GecQojuVYkWEi0cVpjoie0nriuwFionO8frmF3ku1Fm5-SpkSDeVHf4_7fv0ZBZr_5OKTbAor1cGJM7t77unBKJXl0Rn-atZOhgKzqsh-06sgRPQXMzBpDIzM2ki9dYSa0vMjle9ATwc7-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید انقلاب مشخص شد  اخلاقی‌امیری، نماینده مشهد:
🔹
پیکر رهبر شهید انقلاب در رواق دارالذکر حرم مطهر امام رضا (ع) به خاک سپرده می‌شود./ تسنیم #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669198" target="_blank">📅 19:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669197">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f558405c.mp4?token=cbnxUWGFocbhZXMu3iYqPTBD5V2_xHRZtvmfrTbfCm2UA3rnKRt455xcDTQSGN_KC8wwHNy-2-S6J6md2AHvPHSjhTEb56kEobEWc91SUG6OdV_oS9ireZNCwt-J_3Uihzum3L-68LT20Ct_7TNhC7wORJuPYbzC_jvXCduc93kBVUOD6OEjvji9bzGjUUYX8IkfxZ9ZCFSWmuXqDAlZb6qLZTd8OqjWnaN4eyIryTra-7aIecRMX2G1-R_6E5guLPuQzA6TBmFBFTnrrvpdUqgoE1Wd2eIEzI9JrYIZR8LukmMhF6_ew2WUE3k4h6NzUXk3zW6UAvQWDDjiHr2cGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f558405c.mp4?token=cbnxUWGFocbhZXMu3iYqPTBD5V2_xHRZtvmfrTbfCm2UA3rnKRt455xcDTQSGN_KC8wwHNy-2-S6J6md2AHvPHSjhTEb56kEobEWc91SUG6OdV_oS9ireZNCwt-J_3Uihzum3L-68LT20Ct_7TNhC7wORJuPYbzC_jvXCduc93kBVUOD6OEjvji9bzGjUUYX8IkfxZ9ZCFSWmuXqDAlZb6qLZTd8OqjWnaN4eyIryTra-7aIecRMX2G1-R_6E5guLPuQzA6TBmFBFTnrrvpdUqgoE1Wd2eIEzI9JrYIZR8LukmMhF6_ew2WUE3k4h6NzUXk3zW6UAvQWDDjiHr2cGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غم‌انگیزترین اذان مغرب در فضای حرم مطهر رضوی طنین‌انداز شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669197" target="_blank">📅 19:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p40KYotB6buf8AwqyijQQ_vJWgPhBGdpbSY0wtZy6riq2z1KH1umzdqQu15i9RXJ6yopn9JyV7S4fgmi6I9RZ9nibt0353FspBla1PDrnBevScO9JURDZS7RDmqB3OoDJppBOSLmSwvGWKPzn1Zh1YFQjcUB7Av-WUEPuhONVCPx3v3NZ6hUO1uJj0EDr1wLSEjPb9oTZOoVjnqdzc_w2B50VcIRJZO1wtflr7RvpPlPdNTdRrFEvKKGgznA30e6vA6wTPlw9FLCOoyBG66uFRNV-XC_aN2IBook0sBsevQcgf73f7ij5bdMEZBlr37HGjl09WwpI-bWpNM-SgPgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMKPhQX75R-u1sW7kjXiEsz0x8wzt4ZH8lKyvJ0c27Hz3hBGe7V0fBaYCYz6FicP2Tz39JQKB6I_RWqFNjcnXBbGfOUyUqgk5BK8OM6iX6U7ofrYpplMzFnFip6-eidPHXHe4ouS-9ktznytnlfJAyiAQH3lSxer1CoukLBkesWsb7WmEIbxLybEvZzSwkesWpv9sma2pdQJFbFSK6Kz4zl_uIBuzdf7PLauApbLvn44VYH4sens7SvlsXrpvgL2AwegTM1AZ30ovyPVY7LScyS_eIVbZPBPD3MaLx7urXeKVi9SrlJTELgBtPSr7mOPmMyXWcduTPmYrF9RSENplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wm0YZTK2I7g5bDHAg63EKj7k0EudV4fNtPSObeg3NnqCFA5tnG_UIlRRtTodRtr8k-je2WOrCIGCYO-_TZVS-RNzbA-3ixHAZm22svYWLOrXAj9NI_YFUtYW3NLj9yKTmnRTfD3OOQOq-y4IvFNJxdYJWcsK-TG2-ZNLO3cAZh-HrC5dDikgs_gxaRKkeJGq1lwe4RJw2GEMQoDsgw4fyCOvaZiRFk-_ByrMQFzy-IIUWW8LGpGxdxfZTY4b0p63rUCr1eut2f8jq3IhP7gDiO4szVmQ4PNu2z9qc_SHmHnU0RCaw4455gmmowswrDaeDV1b0uJpw3CF1YVmSaTx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU5EyWBZM90VtzX4GsvwPjGF0SEvKfSddWpt6IEFbIchckypfoH_eqddg6dV9QnI5MibTkIs8f9946dlm3_x_j9TFW0syVCgBJT1LkPecwPmEl1SB3IzJoV40dzf_71j8QwlrOj_gZ90DPdVCn7Axko3i_Fh-2FYNdwtjFtMh5_O22wCPbR_AhLvmsK5S4eQ3aHMPiTj8JsOfU_S37f7hBBgkK0jlQf7ImUNcpHTtyd53i7BAKHZtuqzSiiBvlAKAHDAC2iaB-5MnQlJFsB7xKWokUWF1fWOf6mViZaOCc-jJJOqQE1BRs90fU-qInVii2aBgZ9moMqaKsRw1r12Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKbKYTjTXBMp36tGGS518e0FYa8mow1F4_Bf33cXwwadHZ4LtpxfEu2GlwCVPtho6xk9Pucd_z44e46ZFMdhngXQHuiQtijzkrnj-NaaOWPEewDUq1sASx5gE6Yg7iLud1mSpNDzpZCoPO5YQaSD3HxdghYpSuyjcm0nFo1bWw-diy_6UkFezCSdeubnL3gbmN8rqt3BsXHXRd6zW7AXR-g0OBxG51-85xs3Dzxlu9vIHQaasU1qdvaQwCYoYQbHDhvvmEJdwRXIqKCrPjaDY2m-pQ-_slSz3DyVBNd662n9ezMd0AykmU-jT7Gz6ajC8qnJ5YNI7Aqux-S4RFWFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LK4OAPnLi7RE87YgaUJxiV6JppsAcizDWKF2lsKbUjEX3pTJt796XnOXV3kbsBi2Ob_5n9aJsm39k_SxIPDm64aLDmo5WbKJ56ZFUPf57j8H4d8zvaEuLTmwkmLMX4zPjzDCxS_028U5Ls4vLR8goARiLkqUPZylZQ1gvv2aZEk5iQxtsQsyM8fpWYg_pSxzjHimgJEsSwnhS4KIEhceMYGOlRZ5sHhaTFWmzI5GUvZoVvh5WLQKIKIJP9dvLmLpvRpM7sByRhGCgDHYrJW3W8w2AtBkvilKvPnhK0MxS_6PrbHetDMEwf40U0It03EfoKW1JY52lpnreCvXNgKasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bcuvi4Po3WzPwsnGrG3qj6-Ct1kz8HCeENwPSpdh6_vAX7CmKAZdhc7F4AQMfCmVXV24JgMVu-LjJk7IIYtFQy8v3oRalW3J-9HB1s561aisxKMSLXEyKJw4KnuCsRoG1JTjpAW3qbMJz6fEpgnNvHPcBl9oyclLS3KLjxsPR4IY5jcE4AQfHlle5-SyU55LRzpz3EWgx98biZUCwF6_E4tFIVTtqsgYd1MsNFQuagdT2fsRTgbZajx7QuM18QYnFb1pKFL-BW2Yn3sKcCSNNn6WJ4l7lkva424QG6OwINi3V3VWVbxRj00elavl6vjPgcfRCo2ymUNSgssMmGM4_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دور از آن چهره که آرامشِ جانِ ما بود
روزها می‌گذرد، داغِ نبودش به‌جا بود
🔹
عاشقان رهبر شهید انقلاب امروز از سرتاسر جهان گرد هم آمدند برای وداع با یار همیشگی مظلومان عالم.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669190" target="_blank">📅 19:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdaabd462f.mp4?token=k8OsipoYTJFwd1-wNdWB4VOw0gd5iHKnfW30aJRFa860whN1SqLAv6MOfxXsPgrL_AnGd-H229nm5O7ap7GSc_LaWDvnqWhnfpaGNZ6nnA-XcoudIABSAJ11iNJwuh3qDiWNdgXOxHg7w-qw4Iz3Wmc9m39RFdLWqivDKgtwylmk_Gnx7fk8wInSpTpGULtHyko56eA8Z_Req12wWANCsQB6W3l8le6lSgH1MnzGNrZQuC95ABkluIE9iVh_z-Jd83pIWT8LWC__VLbWRkx47jKhWXpzGtbdWGZfdTwKwBLjR-laa4ghgJcj1HJCsizpvu2u5C-UIyWHt5O4hetZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdaabd462f.mp4?token=k8OsipoYTJFwd1-wNdWB4VOw0gd5iHKnfW30aJRFa860whN1SqLAv6MOfxXsPgrL_AnGd-H229nm5O7ap7GSc_LaWDvnqWhnfpaGNZ6nnA-XcoudIABSAJ11iNJwuh3qDiWNdgXOxHg7w-qw4Iz3Wmc9m39RFdLWqivDKgtwylmk_Gnx7fk8wInSpTpGULtHyko56eA8Z_Req12wWANCsQB6W3l8le6lSgH1MnzGNrZQuC95ABkluIE9iVh_z-Jd83pIWT8LWC__VLbWRkx47jKhWXpzGtbdWGZfdTwKwBLjR-laa4ghgJcj1HJCsizpvu2u5C-UIyWHt5O4hetZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بالگرد حامل پیکر رهبر شهید انقلاب و خانواده ایشان #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669189" target="_blank">📅 19:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73340ecd2b.mp4?token=S7IF5K0Hp-dSdYCW4V1A9lKiALpXJIkzt06W11LhmvrZOl5mIKLLOe3DMeTrUUKd_NOhQUtBuEl8_4DFIVm5pGrxAWPYWLPW8g1Sfv51bY2S-HPHHb3ar0T3wMNOVmErHkfmPMmDloCUZqybhk9k9BXPg0g4BMs5q6cqxk3kcz1G3D8NasxWL01CBrHOXRwwK5ok2ttQ3Ncn-znV3YGex-gjshDU4Z_I3KPyQ5_a4MI4b6WVC6f24DUKlHUc3GaIViJNerKDBU_kfS1Fk6-pXB7Y0XKtj9zCD5smeWpWIpaOJlMcXZgvTwekpjTPdJ2UI7GZNp7xpO0g5KBPo7qoQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73340ecd2b.mp4?token=S7IF5K0Hp-dSdYCW4V1A9lKiALpXJIkzt06W11LhmvrZOl5mIKLLOe3DMeTrUUKd_NOhQUtBuEl8_4DFIVm5pGrxAWPYWLPW8g1Sfv51bY2S-HPHHb3ar0T3wMNOVmErHkfmPMmDloCUZqybhk9k9BXPg0g4BMs5q6cqxk3kcz1G3D8NasxWL01CBrHOXRwwK5ok2ttQ3Ncn-znV3YGex-gjshDU4Z_I3KPyQ5_a4MI4b6WVC6f24DUKlHUc3GaIViJNerKDBU_kfS1Fk6-pXB7Y0XKtj9zCD5smeWpWIpaOJlMcXZgvTwekpjTPdJ2UI7GZNp7xpO0g5KBPo7qoQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
هم‌اکنون؛ آتش‌نشانان شهرداری مشهد با اجرای عملیات مه‌پاشی در مسیر مراسم بدرقه آقای ایران ، تلاش می‌کنند تا با کاهش گرمای هوا، فضایی مناسب‌تر و آرام‌تر برای حضور عزاداران و شرکت‌کنندگان فراهم کنند.
خدمت بی‌منت، از جنس ایثار؛ در کنار مردمی که برای بدرقه «آقای شهید ایران» آمده‌اند.
#شهرداری_مشهد
#آتش_نشانی
#مه_پاشی
#خدمت_بی_منت
#تشییع
#مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669188" target="_blank">📅 19:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92f15130be.mp4?token=fRVBuRpVLDfUdps6Zi50pkKx5jg4dGUp66UBhAPaWO6d5ZqKP8Szdd99a5xnoJYUbVKcT0ePxQhc6DTwlSaCQcYPGx3fKzMT_mKzoV7Bb5v2MDOMCJyJydzqgd_xxwjQDe82kkH9PBEK1E3cvQtbr5oWOjs5W1t3ARTuajdnnZZqHrPjdAque7b9gfD0ZUBzVrdfxBtWO-PIIp7C_J7m1QXV0aRhfRFWMrqA2rYzxfEFUn1z1i7s7uXdqLuCEsWphRWR8Xum0oYAsGGgYGvJN7_snYfzohNyPShNUH4019x3iGsBFSCNIAA-iB2TrVeTIzzjR0Ki3AFHr7aE8W0u8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92f15130be.mp4?token=fRVBuRpVLDfUdps6Zi50pkKx5jg4dGUp66UBhAPaWO6d5ZqKP8Szdd99a5xnoJYUbVKcT0ePxQhc6DTwlSaCQcYPGx3fKzMT_mKzoV7Bb5v2MDOMCJyJydzqgd_xxwjQDe82kkH9PBEK1E3cvQtbr5oWOjs5W1t3ARTuajdnnZZqHrPjdAque7b9gfD0ZUBzVrdfxBtWO-PIIp7C_J7m1QXV0aRhfRFWMrqA2rYzxfEFUn1z1i7s7uXdqLuCEsWphRWR8Xum0oYAsGGgYGvJN7_snYfzohNyPShNUH4019x3iGsBFSCNIAA-iB2TrVeTIzzjR0Ki3AFHr7aE8W0u8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصر امروز؛ شعار «لبیک سیدمجتبی» مردم حاضر در مراسم تشییع حماسی پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669187" target="_blank">📅 19:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید انقلاب
مشخص شد
اخلاقی‌امیری، نماینده مشهد:
🔹
پیکر رهبر شهید انقلاب در رواق دارالذکر حرم مطهر امام رضا (ع) به خاک سپرده می‌شود./ تسنیم
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669186" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUnzXE82XQHUB3ucptOCclpzA2nGVgU6ZAhgJPUl3w5x8JrvVzRxVnR-7lOQWtELq8TdsElmIxZmfJ4snUI0q1sCgxyqW7_-F7LwgHfZ_f_M2-U4rlXs0JuqIQuEBkRCCySQVwRq7ljzib7pepI92t-ap192m_yiY1Fu78COqfZQF7FgeqoRRPt6M9_vhTSxECe9uLOPVqyZBty5VlC5RRn4xY8GGIfAJzqp0Thinewnmzo_VSw2nVb7Wmvx6DzHCOioHG0UNZKXWhkou8SPJ4yyqzHj78gpY1Kwp3Wz4jH6b9poy_Za_1ioMtpclpDAoS-MuuzrfUixLCD9wv9XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یاد آن مشت‌ گره کرده...
🔹
تا ساعاتی دیگر پیکر رهبر شهید مسلمانان جهان پس از تشییع باشکوه و اقامه نماز بر پیکر ایشان در جوار مضجع مطهر امامش، حضرت شمس‌الشموس علیه‌السلام در جایگاه ابدی‌اش آرام می‌گیرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669185" target="_blank">📅 19:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70f9361a5.mp4?token=NVOf9vvnWAfiO9n7VGz4VlO0wVujVo4BJypdeQU7fqcvhuXHbDCwjuwC7EMWszZqlWsFCi4tKNz0skd0_kaIq7eSNDEeYcNrSOKNKUoHWQ08cf5IhFL5mU9GcLRbADtY4k7I5lIsJ30J8rvJLLUXGlYy1NnwL0KPmeDQEn3qnxlHHxbw2OylxhI0jusnOHHhTklbB3EHIOHoA2xCYQjpY887Dq1aPp8pU0k1wfKackkH-AIr4YDGPbPLWqFYtq5k8P0cndQLuPqYW_GyN-TErx6nWJKpB6OH-3zq1UoHylMb3xrnZ02UbO_LPQ1nZH7wteXlKLlaccMYtPJeyOLd9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70f9361a5.mp4?token=NVOf9vvnWAfiO9n7VGz4VlO0wVujVo4BJypdeQU7fqcvhuXHbDCwjuwC7EMWszZqlWsFCi4tKNz0skd0_kaIq7eSNDEeYcNrSOKNKUoHWQ08cf5IhFL5mU9GcLRbADtY4k7I5lIsJ30J8rvJLLUXGlYy1NnwL0KPmeDQEn3qnxlHHxbw2OylxhI0jusnOHHhTklbB3EHIOHoA2xCYQjpY887Dq1aPp8pU0k1wfKackkH-AIr4YDGPbPLWqFYtq5k8P0cndQLuPqYW_GyN-TErx6nWJKpB6OH-3zq1UoHylMb3xrnZ02UbO_LPQ1nZH7wteXlKLlaccMYtPJeyOLd9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بالگرد حامل پیکر رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669184" target="_blank">📅 19:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8DAV_e6TEf6STvCtp9JNT5qpw3f2m2NJaeY6dbPCh-06BSz2CqE-tVUiXBCgFS8EdS69E1E0fNC6MSrF0u9fYGvhEh64B6w7w9eScJ1bpwWia5xhwsyIEIhsWeaVGvDrMJzrHbLl1LjgUHxP8GNC4GO-55W5d5pEm_fTV3KL3BjRbGHJ7Y6zTmQaZit_y3xb0XmImHsob68uSOA87XvwPV-Y6NMsaxJQrEaE6VGm7eSVuolCk4klyDsldVDjRs-JJhk7nWfAbGI9C2FK71FPFyC2K39wd1Z6kA6ftRECkehbLUedD_Rpt3iGLyXm15-RO5NYCcTITOKSo3hawEi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آستانه برگزاری مراسم تشییع رهبر انقلاب
🔹
تقویت زیرساخت‌های رفاهی مشهد با خرید ۱۴ کانکس سرویس بهداشتی سیار
🔹
سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد در آستانه برگزاری مراسم تشییع رهبر انقلاب، با هدف خدمت‌رسانی مطلوب به زائران و مجاوران، ظرفیت ناوگان بهداشتی شهر را با خرید و استقرار ۱۴ کانکس جدید به میزان ۷۳ چشمه افزایش داد.
🔹
به گزارش روابط عمومی سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد، در راستای آمادگی برای برگزاری مراسم تشییع رهبر انقلاب و میزبانی شایسته از زائران و مجاوران، اقدام به تجهیز و ارتقای زیرساخت‌های بهداشتی شهر شد.
🔹
با هدف مدیریت بهتر جریان جمعیت و ارتقای سطح رفاه عمومی در ایام برگزاری مراسم، ۱۴ دستگاه کانکس سرویس بهداشتی جدید با ظرفیت مجموعاً ۷۳ چشمه خریداری و جهت استقرار در نقاط استراتژیک، در اختیار معاونت محیط زیست و خدمات شهری قرار گرفت.
🔹
روابط عمومی سازمان: «با توجه به پیش‌بینی حضور گسترده شهروندان و زائران در مراسم تشییع، اولویت اصلی مدیریت شهری، تقویت زیرساخت‌های خدماتی و رفاهی است. تجهیزات خریداری شده بلافاصله جهت استقرار در نقاط پرتردد شهر، آماده بهره‌برداری شده‌اند.»
🔹
وی همچنین افزود: «این اقدام در قالب برنامه‌ریزی جامع برای تقویت شبکه خدمات شهری انجام شده است تا امکان ارائه خدماتی با کیفیت و متناسب با استانداردهای لازم برای زائران و شرکت‌کنندگان فراهم گردد.»
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669183" target="_blank">📅 19:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d478d8f83.mp4?token=UnwxcxeSrhzAW7xeM55SeCpP1bkuLGmCUW4AZ9OY0kza_ZC3dzEBOXXTlArkZFr3VIoeEJZcTZjE2BY6CocB3tCg-hpY15pOsV0i2g9jcPgJ3LM4_xQd2K-TxLeh0nwqTPsWm010Lp53OCDZaO78p-h5Q9FzPpNqNc7s1vMb5hDreQbNWBHRCS_lAzDVBUgdIec28V-KAlW_2-yt8stijvQQTGuANZeD3gaCQs6MYDLWJQt7zlY1bvM6C1dXSW4Q-07ezfD6_6lZTMEsXbaX2bo8t68en47xg-3ssfGykL0AIwp5Ey75RMmBA6zZHPHeJiGkiI1cbmEIMXVpktWOkx4vMM56tQbZKno6ziWz9kq5jTvNyxHJDLWnUOsbiyKJS7dcB8og52LDIwkFYR3fwlWLCMbG6RDRNjGucmppxVL73VF4h1KWdrCvjCYSKazg713OXEdJ5tCZbUYUqMdTaxGQtrSjmWif95m1UR6rIbBDFCs9Us084CmyD1Mn3xgJ8n7t9an8Hrp4NZTB_5uJaEImY8xz1B4a8DebjoEgfBGMdWTSRFaohoJ5YPIWgyVMwO7fyyRYR4QYmtHwHk4AzrKEItE1kuDx505CTzYQaDU0CdN8Ho7ECtH0qlpjDgR_YhuTixEGiOEs0Nv56IYM4E_5cdnVEXZgJ2JgMomCtpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d478d8f83.mp4?token=UnwxcxeSrhzAW7xeM55SeCpP1bkuLGmCUW4AZ9OY0kza_ZC3dzEBOXXTlArkZFr3VIoeEJZcTZjE2BY6CocB3tCg-hpY15pOsV0i2g9jcPgJ3LM4_xQd2K-TxLeh0nwqTPsWm010Lp53OCDZaO78p-h5Q9FzPpNqNc7s1vMb5hDreQbNWBHRCS_lAzDVBUgdIec28V-KAlW_2-yt8stijvQQTGuANZeD3gaCQs6MYDLWJQt7zlY1bvM6C1dXSW4Q-07ezfD6_6lZTMEsXbaX2bo8t68en47xg-3ssfGykL0AIwp5Ey75RMmBA6zZHPHeJiGkiI1cbmEIMXVpktWOkx4vMM56tQbZKno6ziWz9kq5jTvNyxHJDLWnUOsbiyKJS7dcB8og52LDIwkFYR3fwlWLCMbG6RDRNjGucmppxVL73VF4h1KWdrCvjCYSKazg713OXEdJ5tCZbUYUqMdTaxGQtrSjmWif95m1UR6rIbBDFCs9Us084CmyD1Mn3xgJ8n7t9an8Hrp4NZTB_5uJaEImY8xz1B4a8DebjoEgfBGMdWTSRFaohoJ5YPIWgyVMwO7fyyRYR4QYmtHwHk4AzrKEItE1kuDx505CTzYQaDU0CdN8Ho7ECtH0qlpjDgR_YhuTixEGiOEs0Nv56IYM4E_5cdnVEXZgJ2JgMomCtpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی رسولی خطاب به ترامپ قمارباز: بر هر مسلمانی واجب است که هر کجای عالم باشد جان تورا بگیرد!
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669182" target="_blank">📅 19:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8f39a9e38.mp4?token=g_8yvffr9p80ts_pOj2skq_uyMnE8huE_PY52eGjxvDDT_bITTFVpgA8ZR3JAhdN91-CIsEGtDaGUxAWzqZMYWxMklSsISF5mT4_XezlymlN9ZpilzTJGFX55Z871tug-7AHTYvf7QFUXj-JbvP1qnzy1T87rLwjn_7aDwzi9Y59OLh42Vule4ROPISxtjiufQvNiP5b_gbPxYBvzNNS28it-njydv5-7gxTLMvZy_QapHObGSBD41n8XbEN4ZHZpMqvuRQJRqN9KlRzFwg2b2EECv6AS1ubC2fyOXtkZg9uhhx4XQ7ooGCRq6mQOXAYCp4w1rOHgYalOwfQWI8oRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8f39a9e38.mp4?token=g_8yvffr9p80ts_pOj2skq_uyMnE8huE_PY52eGjxvDDT_bITTFVpgA8ZR3JAhdN91-CIsEGtDaGUxAWzqZMYWxMklSsISF5mT4_XezlymlN9ZpilzTJGFX55Z871tug-7AHTYvf7QFUXj-JbvP1qnzy1T87rLwjn_7aDwzi9Y59OLh42Vule4ROPISxtjiufQvNiP5b_gbPxYBvzNNS28it-njydv5-7gxTLMvZy_QapHObGSBD41n8XbEN4ZHZpMqvuRQJRqN9KlRzFwg2b2EECv6AS1ubC2fyOXtkZg9uhhx4XQ7ooGCRq6mQOXAYCp4w1rOHgYalOwfQWI8oRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انبوه جمعیت در کوچه‌های منتهی به خیابان امام رضا(ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669181" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669180">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe9d8d360.mp4?token=MqYRzPL2e0Or4YIpRLA0pAK6gEe2qYED0nUuHFdhdheT-TtNbQDOqtgBBhQ2Bp2GuVwDSurAHfD6uiu4FzgHEeYsrW5hcwsGKBtXkh0wm50u6qsIjMVURqFCzxcqOs7EvjyGRVSa13PrvZi2y3qYFfT-aYvUwzGMPo-ZOq9snOk9_3-5vgFfuTTWOhi1yMRJyGgzC5fwM08-Assy06joLkA0WdLLoMzsoeyOrxH25XUvjk8YnySkgIzZCW5Q40wTyvidUcm74FhfA6ff61rsIc1bYz_fTaHR2sWYJjDydqY_W-PWv6Fm7KhKsPF_niDxwfce2XufNmfKVO10PKydYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe9d8d360.mp4?token=MqYRzPL2e0Or4YIpRLA0pAK6gEe2qYED0nUuHFdhdheT-TtNbQDOqtgBBhQ2Bp2GuVwDSurAHfD6uiu4FzgHEeYsrW5hcwsGKBtXkh0wm50u6qsIjMVURqFCzxcqOs7EvjyGRVSa13PrvZi2y3qYFfT-aYvUwzGMPo-ZOq9snOk9_3-5vgFfuTTWOhi1yMRJyGgzC5fwM08-Assy06joLkA0WdLLoMzsoeyOrxH25XUvjk8YnySkgIzZCW5Q40wTyvidUcm74FhfA6ff61rsIc1bYz_fTaHR2sWYJjDydqY_W-PWv6Fm7KhKsPF_niDxwfce2XufNmfKVO10PKydYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر خراسانی شهید به خراسان بازگشت
🔹
عزاداری مشهدی‌ها در کنار پیکر رهبر شهید انقلاب.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669180" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71ba4f091.mp4?token=DxmHhvALw_XAz9oBlR6QdrblOStAXvlE4ESvUrWluymk0RytcCSXuKK_473-k_HH1UVbNhgWhvv-rI9HUvhAVLmVIpklMAqjyjh9-dq6hs4t6fOUMbc-t9RPApmeZ7tYqTTKHeg_G0hpigcZj2KyZFYN2LvQR1Vtp9SrpJ7JCGyFRAOAfIjn3j_tO9y_ub5unXbN5fVgE4T8WpHkGmvpW-tBTljT-aL2T76WXOMhOSd8znHzt9KLgIDp9rF9HcvQX49IohCf8PbdtBOptXB_Pgf62NF-NgaAD_L3fyhDbUnamvtQq9cs1EJDlx_gzVM8_ZBVVxwV1S5c2tl07HlquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71ba4f091.mp4?token=DxmHhvALw_XAz9oBlR6QdrblOStAXvlE4ESvUrWluymk0RytcCSXuKK_473-k_HH1UVbNhgWhvv-rI9HUvhAVLmVIpklMAqjyjh9-dq6hs4t6fOUMbc-t9RPApmeZ7tYqTTKHeg_G0hpigcZj2KyZFYN2LvQR1Vtp9SrpJ7JCGyFRAOAfIjn3j_tO9y_ub5unXbN5fVgE4T8WpHkGmvpW-tBTljT-aL2T76WXOMhOSd8znHzt9KLgIDp9rF9HcvQX49IohCf8PbdtBOptXB_Pgf62NF-NgaAD_L3fyhDbUnamvtQq9cs1EJDlx_gzVM8_ZBVVxwV1S5c2tl07HlquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار مردم در حرم امام رضا(ع): نه سازش، نه تسلیم، انتقام انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669179" target="_blank">📅 19:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpWty56P3-FUpDh3uQr7R8n8pIwjwLQJHETxk276k6ArOFEttycuHP7YI4hWw6OM5Kk7lQ55JZ8LTsDcHob6JApmq7LnR_yrSmlbofxVgkzRTe97ecSy_PcVY4knb-YGwTl_FM8QEyuPfTJ1ZoofyNEH2rE9rDXf5d-vw78I3Y_2NXZdPinzfL_mFdO1PyOT5EITl4_UdWPyFWZi3IuWjpr1619pbsyEXid6CbLMd0yd3RLgCXJKchy4McfDNUq5WQDEPgdyMzwahiXx75ZqqqT8ZWojqMtNod7pbVoZgCkG1CKXXeP9PUCEIm7Dx-5lPAzn2YXRQeKdD2AETY78Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم بلند مردم عزادار برای انتقام از ترامپ قاتل در تشییع پیکر مطهر رهبر شهید انقلاب اسلامی در خیابان امام رضا علیه‌السلام سمت حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669178" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669177">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd37352e92.mp4?token=DQdooLJsw0JRvMKSK6lw7PJb1Q5Ct6YD80hiRUKfCyZXo84ISbATOl54hGeGH8pdknGdlJrLiYdRz7PepXG2eMgvrXC6K3y1SK67kl4t0QdTYcfo0DxEm0ERQyEy9V3JULaRNOyvcNb8XqHXBd6H3hoBktGk1l-8d3g2amQDzLJi1VOA4do-_x6sVfGBVomNOxnHLomBpb_lrnVhzZET9-s_IVhSWx88fSrjt-ZB8OPF0TBAky6qNVCLE3IJLA4bwe-Xfo9bG3LLO-IVi_k0QuR4mrAl4Or3AA_ZPej6ocgSdpLfOxupRnQDibrxbAiRuU41kHxytHe8BztRwt3UjjWeBB77V8BCjDmS7pbd0O50XZCFPZnHdQmo2KmaRgrCmNWAWbZyqSbIdLN_NzC8THrTPMRq5vMIaqugNOtCP7pZzpL2JmFUWijgG8WqKiYOrO5gmNCtMUfcmvT35lK70dWlQcJaiupu9m0wW4fkYEArTvI_VopkXESnSdLnC3iOBzWwOE2vJ8R-oJvgN945Zk77P1UTionWVJ0uK-vaKc-6UeAfdVDMSzYYXJtIQDIJ1Hpo-II97NQf6zUa3R8N19jJ7TZKWu6LHLuEbyedEyjPI6pHgEDBSW1xfSuRpnsYgVSEIi-ES2GaEixOLJozXLJ9jhiVnhikDN7gAU2kdeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd37352e92.mp4?token=DQdooLJsw0JRvMKSK6lw7PJb1Q5Ct6YD80hiRUKfCyZXo84ISbATOl54hGeGH8pdknGdlJrLiYdRz7PepXG2eMgvrXC6K3y1SK67kl4t0QdTYcfo0DxEm0ERQyEy9V3JULaRNOyvcNb8XqHXBd6H3hoBktGk1l-8d3g2amQDzLJi1VOA4do-_x6sVfGBVomNOxnHLomBpb_lrnVhzZET9-s_IVhSWx88fSrjt-ZB8OPF0TBAky6qNVCLE3IJLA4bwe-Xfo9bG3LLO-IVi_k0QuR4mrAl4Or3AA_ZPej6ocgSdpLfOxupRnQDibrxbAiRuU41kHxytHe8BztRwt3UjjWeBB77V8BCjDmS7pbd0O50XZCFPZnHdQmo2KmaRgrCmNWAWbZyqSbIdLN_NzC8THrTPMRq5vMIaqugNOtCP7pZzpL2JmFUWijgG8WqKiYOrO5gmNCtMUfcmvT35lK70dWlQcJaiupu9m0wW4fkYEArTvI_VopkXESnSdLnC3iOBzWwOE2vJ8R-oJvgN945Zk77P1UTionWVJ0uK-vaKc-6UeAfdVDMSzYYXJtIQDIJ1Hpo-II97NQf6zUa3R8N19jJ7TZKWu6LHLuEbyedEyjPI6pHgEDBSW1xfSuRpnsYgVSEIi-ES2GaEixOLJozXLJ9jhiVnhikDN7gAU2kdeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#باید_برخاست
♦️
آتش پاد امیر حسامی مدیرعامل سازمان آتش‌نشانی مشهد: در اوج گرمای هوا، آتش‌نشانان مشهد با بهره‌گیری از توربوفن‌های تخصصی، مسیر تشییع رهبر شهید ایران را خنک‌سازی کردند تا زائران و عزاداران با آرامش و ایمنی بیشتری در این حماسه ماندگار حضور یابند.
خدمت بی‌وقفه، ایمنی پایدار و همراهی تا آخرین لحظه...
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669177" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3BIZMDCC6p_0lGtjsAB29TQ8HbAEnVahQ4r0spUbxLA93PGkU9wMY8g5sVc_z8Dc-_v1bFrdRGtfDWqK_zkOJMgb4rEn_5EFdfEX2GUKtfPPT8_7KRn7aXphCioVudgxfi4Gy9iPundFEDFPIBTm0vjkMuc5pUYFgLeXxUq48mnknVuWkpykWj2eJnFuPpILvq8_8ZNakdWg1Mpef3QS34zkGilyHG7IxrJiQbrb3a70SaohbEY1YKrOCVoKVJTM6TVwCa-pLVa_kEJZxGYt0ygUk1kPcCIg0Vy-PTVADx2DQnmZu7FfsjntDYQaBN13q_gdUcZHPK7azHpqpM9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم بازگشت خدمات بانک ملی ایران؛ فعال‌سازی خدمات جدید در سامانه بام و شبکه چک
🔹
بانک ملی ایران از تداوم روند بازگشت خدمات بانکی خبر داد و اعلام کرد، مجموعه‌ای از خدمات جدید برای مشتریان فعال شده است.
🔹
بر اساس اعلام این بانک، واریز سود سپرده‌های بلندمدت، امکان مشاهده مانده حساب در سامانه «بام»، فعال‌سازی سامانه چکاوک، رفع محدودیت مبلغ استفاده از رمز دوم ثابت، صدور کارت جدید برای حساب‌های واجد شرایط، انتقال وجه از حساب‌های فاقد کارت در سامانه بام، امکان مشاهده صورت‌حساب در بام و شعب (از ۱۱ تیر) و همچنین وصول چک‌های صادره بانک ملی ایران در صورت وجود موجودی کافی، از جمله خدماتی است که به چرخه ارائه خدمات بازگشته است.
🔹
بانک ملی ایران تأکید کرده است روند بازگشت سایر خدمات نیز به‌صورت تدریجی ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669176" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669175">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
چه زمانی امکان زیارت مزار رهبر شهید انقلاب فراهم می‌شود؟
استاندار خراسان‌رضوی:
🔹
امیدواریم از فردا حوالی ساعت ۱۰ تا ۱۱ صبح محدودیت‌های حرم برداشته شود و زائران بتوانند به زیارت مشرف شوند.
🔹
به نظر می‌رسد از ظهر جمعه، مقدمات زیارت مردم از محل تدفین فراهم شود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669175" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669174">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPiPoQ02vILuWVzHWcQ05Rwzoac4rmYgAdTmmivV_OCeZ4pScELBerciRotW6orXum7HWZDdP-wvr3I-Dhlm6W3BNO0dNXzIKl4q9_LE65f548i-TgyvBYm6mh_xJfHv1PXy99ks6f-7F9qm1_9j8KbQElo4fvKcwD4skpMHCfzzLre3U2-UdIER909Ypwkk7E2_wFrywypC3VX3jn63UOwKqfkDI2mKawQzQ7MUwFfktHOSlUxCnxU8lYx3ZxBoPVwidgCituXgfjm9xJlKNP8m4FMsLyVXnTcAJsJY2TL81rbahY04yoUnKMPyl8A98VbQeJa2HjbQAhTHqKz9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669174" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669173">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
با
توجه به ازدحام جمعیت در حدفاصل چهارراه دانش تا حرم مطهر رضوی، ادامهٔ انتقال پیکر به صورت هوایی به حرم مطهر انجام خواهد شد و نماز در حرم مطهر و خیابان‌های طبرسی، شیرازی و نواب‌صفوی اقامه خواهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669173" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff6662941.mp4?token=GqgXTGmPguaKDmxocrweaW42_ZdlDWeJ_UmeBMAYDFlreCu3V_S35fygg-aIFHvqnk-OcrDtaZGUi2_yq-poseCOIMl4Qn82rCBOablxaD9F9t2X4FVCWIKOwiBymHmPTIb1SnHMqDAS33OxuNbZL32Pt1ltJ1bSjarxUYqGo2NhZo-x4LWl3f3TiJHV-ZWejaiUItc9IT_Qyh9s5WVk-nyIUsmzH9kOLp1PgHXzcTL5xgFE3QonHUM6H3Y4uzrIepXkh9I2TAugBSx4eRwn8ISRGGtnnvKbLAHuBt0aHVBSTlI9xOAlXqGAwqoEyPr0tf9fOJt1tFITNoB3Rjiiooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff6662941.mp4?token=GqgXTGmPguaKDmxocrweaW42_ZdlDWeJ_UmeBMAYDFlreCu3V_S35fygg-aIFHvqnk-OcrDtaZGUi2_yq-poseCOIMl4Qn82rCBOablxaD9F9t2X4FVCWIKOwiBymHmPTIb1SnHMqDAS33OxuNbZL32Pt1ltJ1bSjarxUYqGo2NhZo-x4LWl3f3TiJHV-ZWejaiUItc9IT_Qyh9s5WVk-nyIUsmzH9kOLp1PgHXzcTL5xgFE3QonHUM6H3Y4uzrIepXkh9I2TAugBSx4eRwn8ISRGGtnnvKbLAHuBt0aHVBSTlI9xOAlXqGAwqoEyPr0tf9fOJt1tFITNoB3Rjiiooi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از ماشین حامل پیکر رهبر شهید انقلاب بین جمعیت عاشق در خیابان منتهی به حرم امام رضا(ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669170" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtoMqk8biINUm7TsdJA_GI6EAFQxcreqPzcy7e_kF9spbXrdKl0MpZeYqpUbea8Ft8w6wBIuEMBBQI0xYSThvflPaPM-m0cxpNLTvj_Y2MaLadItuf2BW1yUnNbTM-YcfbPxfl_FN1uPHglTsh8bLbjynTY6NOzcevIUDI2VkRgIDfLN57N_tObp7I7bWhuXLhBrLHHhTh0cOr8ikvWDoxi8oSJ4BrR0al7Qa3aBip7HNetcxQYeeZROgOZ4Y3cune1lRFzvrUBvpbT3h2jc3-9MKAoKQKS5pQRLCaz8y2X2xYBh1Ugu6GB27VWkz5MEkRQl6-eJAv3_wQ4PIAWIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669169" target="_blank">📅 18:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
گزافه‌گویی‌ تکراری نتانیاهو: در جنوب لبنان می‌مانیم / ایران نباید به سلاح هسته‌ای دست یابد
بنیامین نتانیاهو:
🔹
ارتش این رژیم تا زمان نیاز در «کمربند امنیتی» جنوب لبنان باقی خواهد ماند.
🔹
او با بیان اینکه جنگ پایان نیافته و چالش‌های جدیدی پیش‌رو است، مدعی شد ایران ضربه سختی خورده و اسرائیل اجازه نخواهد داد تهران با توافق یا بدون آن، به سلاح هسته‌ای دست یابد./ خبرفوری
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669168" target="_blank">📅 18:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba7fc0f1e5.mp4?token=mTSUe85zhw4t6lCCDSu2roWMiKLOaVZPNbb63d5TIxUDO_Yi99VdJtMgarfnS95CpZfz3elmHHOma6P6kSaatoIhrw2nYs6M_8tUJFDLIPjZctSqsLKfLj76LpQUfb_h-efnpgn2nQhGcBwd2RQWW0QaFU9SVfnAX2I11wV2OIYJBeHGVOf8ndmeYXQxLKGcfVIy6C2Q5VAOCqOQmT5KjwkDMZQcuujtKIZlw6qmow4BC-WyWVkk8RgWqlP7MEU_KCovG8u6f7vRo0Grnp-UDwXE2NuWKhc1uxLOLv_Y_EJI7Q4hoEshAzrc1YsgSKcmYxC2ojmPreK0AW6Hhs1YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba7fc0f1e5.mp4?token=mTSUe85zhw4t6lCCDSu2roWMiKLOaVZPNbb63d5TIxUDO_Yi99VdJtMgarfnS95CpZfz3elmHHOma6P6kSaatoIhrw2nYs6M_8tUJFDLIPjZctSqsLKfLj76LpQUfb_h-efnpgn2nQhGcBwd2RQWW0QaFU9SVfnAX2I11wV2OIYJBeHGVOf8ndmeYXQxLKGcfVIy6C2Q5VAOCqOQmT5KjwkDMZQcuujtKIZlw6qmow4BC-WyWVkk8RgWqlP7MEU_KCovG8u6f7vRo0Grnp-UDwXE2NuWKhc1uxLOLv_Y_EJI7Q4hoEshAzrc1YsgSKcmYxC2ojmPreK0AW6Hhs1YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع نمادین رهبر ازاده‌گان جهان در کارگیل ھند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669167" target="_blank">📅 18:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تماس تلفنی عراقچی و عاصم منیر/ وزیر خارجه به فرمانده ارتش پاکستان: ایران قاطعانه مقابل هرگونه ماجراجویی آمریکا می‌ایستد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669166" target="_blank">📅 18:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322f70a346.mp4?token=RDd_oCLWoI7xkeY3ytUS9fuCs7OeISkPiw5O_HF8aNvBU8o-tEoVsu94Qh5xWure3YFdeOM2xN6O4BcN6w6sFMUeeYSOpNa3WxUaCQ5RYPYvbxxOF3D8qLsGjAS9I42ETHZ536zom93uvCR47-RQcuKiIzSjkGUl2L7RqmXsyWSN_ihzy2yzv5Lh-PA_2CpSrw_6s5tNCXbnirhHDDtC_oj4g_mA0InH5yV-ai99W_d1c2wcA6TfQBhwMkzTEcDhXPu18lUSG_4rexFGb34ILKUEnQFxPSWOslc0TJ1TxdQWUHjJTRHJHKcxks8NQQYhjJNMTxjNo7gifK8ZvQI0hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322f70a346.mp4?token=RDd_oCLWoI7xkeY3ytUS9fuCs7OeISkPiw5O_HF8aNvBU8o-tEoVsu94Qh5xWure3YFdeOM2xN6O4BcN6w6sFMUeeYSOpNa3WxUaCQ5RYPYvbxxOF3D8qLsGjAS9I42ETHZ536zom93uvCR47-RQcuKiIzSjkGUl2L7RqmXsyWSN_ihzy2yzv5Lh-PA_2CpSrw_6s5tNCXbnirhHDDtC_oj4g_mA0InH5yV-ai99W_d1c2wcA6TfQBhwMkzTEcDhXPu18lUSG_4rexFGb34ILKUEnQFxPSWOslc0TJ1TxdQWUHjJTRHJHKcxks8NQQYhjJNMTxjNo7gifK8ZvQI0hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم رضوی، شاهد وداع تاریخی با رهبر مسلمانان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669165" target="_blank">📅 18:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdobPnnZF66LLGlU2BcaUDVlryA3P5bgALn1Zv7z9o4fv9u-Cksdq-niNCg5d8ccazfBHbyO0QlX0JzuZORKF2amSXiV93g3jMt5mj4RSyYjASHk_1fCs7K3VzbYKjjO0deHXn6WfRLMXoS1pNfcLDsN_vct5BydwckC7RDn2c4siGfYbhiOsl7PLPkLIYJD_njF9bHx2KfvWVDymK0ejpyZKocXpFDefJUrN65MYO_BHPjeOh-qtJsGeAvlF4V-LEPmjN4zDKWX3KChMG8c9jqZnv_PpfghpOvH3Jdi5wjyjOyMHUizOVd0gVOY5on0dF4Hg6mSfSmZITXISDQ5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماز شب اول قبر رهبر شهید انقلاب
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669164" target="_blank">📅 18:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUKWkKEK1eP34sIhIHnjEZ1EKqDMiFbHlSST87GHNp4jgqZl5yK76kMlV_8-BO-SGGw0LRKqNW0oZDWLspd-TcWhac1z3IpA_9iCA6xhnyyzTKslRNXMPvVOsSbq36vFwCdv231cenkVTBDELnTirE_5Sc6oW_cB5_qOuJ_5Mrq8kc0LvpQBT7llpcGy92oiVNSZvBwPnX6IgvBkM4ZiBzODgSRNV7D8IqSyrMJCBWMCB-uIUyv9f2xpediKScZL_s_dnMrfhvXfQ291K-QG4HwO54QleI3NP439h72m0OFQdR9RKz_mbMAZgmyD7RDr7T7hnjZ8BxKEal7YBhHI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVpnL6utaQe3yQL6piooyo2i0JmAyQ334AlMV_aevuSO9qjlEFa8NFMTABqRBYhhsLLVFZhhGYz7raLpsW2jhNAYkKqUYQfrJqmrk-yEdmLcMVynJj3O9hkYqHwQZwjGkSYNaioKhRus6N7pk11EJrRBZ9oZTuNGF4Plu7fBPazQRuHT4QOzsihVPm-flSnOrnMrXnD8yd8qTmfNzFp_HvNuoccHWRzuILgWqxt8S8NTP-IqrDWVxWS6wHSVH50lLOgbqYTnXjc40As5aS8UY07ZhLeL2p20CCjqXQcbbESUt7_pTF2k194kB_fMNHuV3TDMylyy6dsKP3M5rP3wCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PndKzRv1xuNMhVXz-WhCV5ajht2IilyPaIDahj8yfWq4xATnCCfmo8AFYdgAOb9uQtWshd2-naAJApI6fGx32VnmK_yE80Cw2WV_nFfe9IVi3tEgU_79WMrjytCdV0R2pH5k7MtnfFRucuLx-D45BEwsxVZFL7c_5aupYhWaLvwOKl988glV0V7rHKq8Lvpqq29P2PEOQpq7TP3tzAozbtScfsSHs1YF0tMRFyiJEubmFp5rEfvBYXK6kmiUAG0KpkmoUEemhq3MopoSwLgGxkSOZoiiJ4drLTjcfqpQQfCsGDEFb9ycP4whBavzvTSKYiaC4ju0XsF11uxM7Tv85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQW0RU9TIFBlCLsOW_RTFioEvDlGB9ekIDD2TXLj1S9-rKgN0GLBcK8D45IJk3Z2m3jImXxuE2qf77X4SplVqKXKFtDh3DYbn1-JPIeeH-qCyTqrFxOpLVkUwi6kwFxOiOhIbW8AJeNhO9kwsxKBJZaaym2bpixTReRSXr-2VguVNzIHk5SRcPGHdd4HQ-gVndciMu-ET-jn5EAwiRxwuflWCqPFUDgab4Jzx5QHRQr0qeigb59hzTIIVRwMZ5Gw4DYNgPmNutZNo9a1wCGzd6c9b4VJCrNNzaCD9g7-9N2Sqfb4H6kOd4lTXzovULEg8o-11Rl-O9ieW9lJUewqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhgjEsjU7Xf76o6hIx5Jvp-6BYBbiANJPPbz5idzJE456AKUdfptlQovhg8GLtq1diRo_6KwdMtONki5Q-wqVQb_48ncOoaL98Q64ma7eEhqtR4qCrHTYKe2YEBydX5IYZGqHNNZa4yE9HjRZx1VVn19aAkmW1ppPw_HJAZ1GOTKidrfWlcoCwPzSbbBqsNAId0ZZ9widjAN7CVoZoJP9OaaOjkbTQ6HzFnPrexOdouS_IwSdkFcvwMSNQbwnhLsBAFiYM_zG0pOWr6o5qWrtrLgRfjcU2E32J_OBNMooqMgF69rSRmMIBh3YQ6sr2Gfm7_bskEFS5njO-b1dd49og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKXTPMAhlm8Y06-wjz1dqJ_1h-lbOJ8p3sRjJz6KLsX8rydZB2foZ1KBHmO8d_MJCLfamqdltx9X1j-F2X4v07ZkSIBIkvSNjBjBc5AZwkSD_lSAD7ztCq8nzYmqbED7z0ODqi1RF8Ysbj2stFe3WZdWYmhax-U9J4u6AgdWNzzPEDLUqgunQpk5TzoDw1pJuUGPl03iNrAE9VN-0hax1RIgjzA3iLDDA04ByYWC43mH_RXKM8v80TmEicVQ9zW1h1tSWSPI-NAKx0ilsVl6mohjbDxiHlOPp3ayFJK4SGmPj-7QuW3livIdEEauqRwHuCXxFCqcSSuwmBugpxI23Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دریای پرچم‌های سرخ؛ تصاویر خبرفوری از حضور ۸ میلیون نفری در تشییع رهبر مسلمانان جهان در مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669158" target="_blank">📅 18:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luLaHjX-1dCBECdTEahglOKtDYw1XU3JPztwmDQN56iSgB7EaadtTqZ3_gFkzaSvbVTlM_Pwb_RTgWsflDN5ewfeJ0CHiNL2OyfbIAve-KKSfwhtw9915IsWqTO70_Qbx2T3QNzanbIZNvtW7WJIWmcA6Ew7xWUsRAr6S_wDwOdhTKdPpYhOO7x8tNbBTOmRcpVuLxizaLSJTuSn2Wy9nDJIa17jMWz46Q3YycWUTb0Zy6BPrNweUMTCHZIcIh06Hy2IQkjSx5ldOAG6SCwQ7BNYmWf2IuCTm6iUgr-0_em4-Lr0sgtu1haECJNZDzo8Ao3uGFHifM2P-2wBEUCBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری پروفسور امیرحسین سام، رئیس دانشکده پزشکی امپریال کالج لندن برای ابرمرد شهید تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669157" target="_blank">📅 18:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
خروج خودروی حامل پیکر رهبر شهید از مسیر اصلی
🔹
دقایقی پیش خودروی حامل پیکر رهبر شهید انقلاب از مسیر اصلی تشییع خارج شد تا طبق برنامه، جهت برگزاری مراسم نماز به حرم مطهر رضوی منتقل شود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669156" target="_blank">📅 18:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/669eb50532.mp4?token=qn8ZYyFkiMRLH8MIub9Lvjn-6edEQE9WPzm38V69ZOOEaS_kPh_soQHFgf8pliiDbon27p1rKJE9lZMA3hNF6WUklUgIJp7obumGinMTMqpI2_9xnxO38QtX-X8nNZalnMzrQcbFqE26c5savrTJt59FPihyC02RjIbltuYIhXjalUsGjiIoR6pmIV_VOLyteNHtstQGYNO2R5oaZp4KoyNSvOeAxDtocwG7RMD_v9hFRqm0jLz37LS038sI2lDM2FY4JVYayMduKjkqx2EeG5yBNmcuGXTVWUluXyqWUd_QUI_4n-phtS8CJzEIjkyf1jI8TnxPo3IA8tDRf218rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/669eb50532.mp4?token=qn8ZYyFkiMRLH8MIub9Lvjn-6edEQE9WPzm38V69ZOOEaS_kPh_soQHFgf8pliiDbon27p1rKJE9lZMA3hNF6WUklUgIJp7obumGinMTMqpI2_9xnxO38QtX-X8nNZalnMzrQcbFqE26c5savrTJt59FPihyC02RjIbltuYIhXjalUsGjiIoR6pmIV_VOLyteNHtstQGYNO2R5oaZp4KoyNSvOeAxDtocwG7RMD_v9hFRqm0jLz37LS038sI2lDM2FY4JVYayMduKjkqx2EeG5yBNmcuGXTVWUluXyqWUd_QUI_4n-phtS8CJzEIjkyf1jI8TnxPo3IA8tDRf218rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ قاب متفاوت هوایی از تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس. ۱۴۰۵/۰۴/۱۸
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669155" target="_blank">📅 18:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e31b4d9e.mp4?token=LKBn4loU7HBVIf9XmzNtGdptiN2HymlXecvfJ3iEOFsbKO8HzfgfBKe1xSS8eIWlVnQ01P7j7SKrU87P7WP2iPKnbK-H3UL3LWs0VtmBTZcrf_nJqOL4NCIiFahTjiRncXwOW-gKuI9bsNb8Dl1Qvgn-QnGHY3rhFgZGGHiIl3fQFKgGn8MOiLtb1YULUxr4hSk8rWFXv9J2aRK4e2UTrFAWWwggClfFBCQNNqW-BflkL5E7L1qG_1AnF5U5EIMmx3_33BTIN1iLFIpJr1OV8Pb0DnrPBQ7dfLYd3L4AllRSQYgujfz1ju6svq-mak-rUFHy8awN3eHmPlG7_t8rQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e31b4d9e.mp4?token=LKBn4loU7HBVIf9XmzNtGdptiN2HymlXecvfJ3iEOFsbKO8HzfgfBKe1xSS8eIWlVnQ01P7j7SKrU87P7WP2iPKnbK-H3UL3LWs0VtmBTZcrf_nJqOL4NCIiFahTjiRncXwOW-gKuI9bsNb8Dl1Qvgn-QnGHY3rhFgZGGHiIl3fQFKgGn8MOiLtb1YULUxr4hSk8rWFXv9J2aRK4e2UTrFAWWwggClfFBCQNNqW-BflkL5E7L1qG_1AnF5U5EIMmx3_33BTIN1iLFIpJr1OV8Pb0DnrPBQ7dfLYd3L4AllRSQYgujfz1ju6svq-mak-rUFHy8awN3eHmPlG7_t8rQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب هوایی از تشییع پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669154" target="_blank">📅 18:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195706b1a7.mp4?token=DJtZuAgqW3t43vEOF4z-WDuILnVIOuVjsCsghpzLawTgRfK-nJNkPMyJVsJEpo7Pe7ZZaesaM0JSZDOCpJpH7lGREGmTDjqjTRfT0gGTBwv1ZX527TV1Qo9G_KF-WHGdGADYNMJ7175v6ONX0bs2OYKuhayes6uOYpi5zJlM6BdR0s0x6AT-c9IQjl5lrcr03TRfPr2ORwAH_Cgm5QrPMOzmnmV1gab2h9ORMl3HWcCS8R_No3DFfHrJMQUQBrZviNFykWeL9RGiYOmMnBu5AayoG9iAefFsYdnZVmCs5o7Y1-K7yt0rk8wPv7zc8-W2Z96dfcbcjmT5qjQ0N5bSQ6TslRLVyPTnNVJixHJ-7NNlb5CjN2WVAYqu8dB4QmlBBShXD8mrGWN7b-vh2rcD5AJ4MtrwjPyzekmhaAl1elDC-ZZ0JgcjtTu2gY6ZNtFyOSxQh_xWftSgK6tzv9SmihbIrM4Mk619rLAM9sVK5mfS2jGtUApnC0DjeHpkOby9W--wPOaRHwM6-sHuGB5xSnWOvUfylP4DglePuGO8vYwj6A0PFL73IbIzbNEJrFB8bXlwOpTd441o4ULdB1tswKlYZ7QFyLdcI2X-u7oua8rlQpqkfMmwaZ1SSAvpCPtTWW-jOZl1Nrnat5iAb-Yu3Pu9p31xjYw8bZRfdSME8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195706b1a7.mp4?token=DJtZuAgqW3t43vEOF4z-WDuILnVIOuVjsCsghpzLawTgRfK-nJNkPMyJVsJEpo7Pe7ZZaesaM0JSZDOCpJpH7lGREGmTDjqjTRfT0gGTBwv1ZX527TV1Qo9G_KF-WHGdGADYNMJ7175v6ONX0bs2OYKuhayes6uOYpi5zJlM6BdR0s0x6AT-c9IQjl5lrcr03TRfPr2ORwAH_Cgm5QrPMOzmnmV1gab2h9ORMl3HWcCS8R_No3DFfHrJMQUQBrZviNFykWeL9RGiYOmMnBu5AayoG9iAefFsYdnZVmCs5o7Y1-K7yt0rk8wPv7zc8-W2Z96dfcbcjmT5qjQ0N5bSQ6TslRLVyPTnNVJixHJ-7NNlb5CjN2WVAYqu8dB4QmlBBShXD8mrGWN7b-vh2rcD5AJ4MtrwjPyzekmhaAl1elDC-ZZ0JgcjtTu2gY6ZNtFyOSxQh_xWftSgK6tzv9SmihbIrM4Mk619rLAM9sVK5mfS2jGtUApnC0DjeHpkOby9W--wPOaRHwM6-sHuGB5xSnWOvUfylP4DglePuGO8vYwj6A0PFL73IbIzbNEJrFB8bXlwOpTd441o4ULdB1tswKlYZ7QFyLdcI2X-u7oua8rlQpqkfMmwaZ1SSAvpCPtTWW-jOZl1Nrnat5iAb-Yu3Pu9p31xjYw8bZRfdSME8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669153" target="_blank">📅 18:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
عراقچی در گفت‌وگو با وزرای خارجه عمان و ترکیه، آخرین تحولات منطقه به‌ویژه تنگه هرمز را بررسی کرد و بر تداوم رایزنی‌های دیپلماتیک برای جلوگیری از تشدید تنش‌ها تأکید شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669152" target="_blank">📅 18:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">عزیزانی که امشب تمایل دارن برای رهبر شهید انقلاب و اعضای خانواده ایشان نماز لیلة‌الدفن بخونن، اطلاعات زیر رو جایی ذخیره کنن
🏴
سیدعلی‌ فرزند سیدجواد (امام شهید)
🏴
سیده بُشریٰ فرزند سیدعلی (دختر آقا)
🏴
مصباح‌الهدی فرزند محمدباقر (داماد آقا)
🏴
زهرا فرزند غلامعلی (عروس آقا)
🏴
زهرا فرزند محمدجواد (نوه آقا)
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
_ طریقهٔ مشهور در خواندن نماز لیلة‌الدفن:
بنابر این صورت که مشهور است، در رکعت اول بعد از سوره حمد، یک مرتبه آیة الکرسی¹ و در رکعت دوم بعد از حمد، ده مرتبه سوره قدر خوانده شود و بعد از سلام نماز بگوید:
«اَللّهُمَّ صَلِّ عَلی مُحمدٍ وَ آلِ مُحمدٍ وَ ابْعَثْ ثَوابَها اِلی قَبرِ فلان بن فلان». (به جای فلان بن فلان، نام میت و پدرش را ببرد؛ و اگر میّت خانم است، بگوید فلان «بِنْت» فلان؛ مثلاً زهرا بنت محمد جواد)
پی‌نوشت:
۱_ عزیزان دقت کنید، عده‌ای از علما میگن آیت‌الکرسی رو تا «هم فیها خالدون» بخونین، بعضیا هم میگن تا «هو العلی العظیم» کفایت می‌کنه؛ شاید اگه احتیاط کنیم و تا «هم فیها خالدون» بخونیم بهتر باشه.
۲_ یک نماز لیلة‌الدفن رو نمیشه برای چند نفر خوند؛ برای هر شخصی باید جدا خونده بشه، هر نماز هم شاید چیزی حدود ده دقیقه یا کمتر طول بکشه.
۳_ مستحب هست که نماز لیلة‌الدفن بعد از نماز عشاء خونده بشه و تا قبل نماز صبح هم میشه خوند.
۴_ عزیزان، منفعت این نماز فقط برای اموات نیست؛ مطابق حدیث نبوی، یک روزی یقیناً نفعش به خود شما هم می‌رسه.
پیامبر(ص) درباره ثواب خواندن این نماز فرمود:
«بر میت ساعتی سخت‌تر از شب اول قبر نمی‌گذرد. پس بر مردگان خود رحم کنید و برایشان صدقه دهید و اگر نتوانستید، دو رکعت نماز برای شخص درگذشته بخوانید. پس همان لحظه حق تعالی هزار فرشته به سوی قبر او می‌فرستد که با هر فرشته جامه‌ای و حلّه‌ای است، و تنگی قبر او را تا روز نفخ صور وسعت می‌دهد و به نمازگزار به عدد آنچه آفتاب بر آن طلوع می‌کند، حسنه عطا می‌کند و او را چهل درجه بالا می‌برد.»
مستدرک الوسائل، ۱۴۰۸ق، ج۲، ص۱۱۳.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669151" target="_blank">📅 18:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkXkHVqOyW3TishftSgPNTWTzNmTHuoi2jWrW99H3RhdvgPGX9RQFoKExfMbtWlcFRRncojofySAzQQEDl6RV6IBAZWCSsC-xTLsMwVUBkmj2Umcmc4p5L82AZmB2JRoPQMXszJDTuev8aL_Nxg-QpfGU2FJDjahKApXDvh68uSPtSGbH4AujPyLnGlHu7-1kztpXfU4lWO2tzS70Nvw2aBnzPpUtt2WzjrimcYuH7ErnqdsatJYPAQvyFpKWnJcdvAi23FRs81-xWUvXav9UmKZQfQ9FzvS0W9d9Ny8KvnR2lxp7wGRhVTF98-42TTAC3vLO41x5fYoqUwRQV118A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilnMB1bi6fVAVyUo5-GlUYrEGLNiiePI7635rIUiZvbIG8VMEpqzDxTiC_59ZM_qS665MYiut66VwnPk7pWvoBTPJCWYIxsBySGR_umndn4uajYYyQlymXPDw0m_tN9SzRx7oyWl1-z7FBvuOncCoYjYm4UYdvqD0GEmrNB_H0_FZs2Gj0DxxPChNNVriOBlnjNvW6dwzxtRyVzzxDfAibdiHTVJ1crJ9iSUs5wNPpKgTVfFfLHUKoD3gvGBxew9OM1n-HSxgACvstg9RZLX3FcjJn_J4n9OAHqGR1AAK1Qfhrh4ehNpzexC-C1dbcxcmXs1W45pw6mcvpFHiFb93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbQzMc6F9jRP26hQ33PzSJB1OdmBwc5Si3GnoXCVc89KSDT1PR5JVT1kGS_Dw_ilNPb9a2ARb1gH-4GkjVUboIhSCRgudAxEOONbegk0BchzxdQvAf09B3xZp6qkNEmOS1u8y7j5RdD8ZQLLma4TniXc4VFrGKg053HblEDtqsNZbSNp7POnbw7TPWi5YljOgqFNQiLj4W9eThEBiVhkcM3j2CezN5kegjtG0U72ChKY8BGYH5kXOC92vNhVfo00F1H9r0V2XRSPHv3LTW4pHm_YcdCZdxO1OoXVKpEz51tVa4UZqCsm2VARHo3dreopY39PBhqTv5iKk7prqcO35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfQgQOwzBGwjNFINs9maDJiVprPNug3ycwefdp90E2gzXW22_ehAhtM4C3mkuFJATUwjmMM12lNbC-DErrrg180g5UJQ5lar0qW58zCPy_vtcJqb-AhNauEH0Y1Dvchm_hzrK3sttoeaM_R6ydHm4mq0Ndkzp29bxV_2ZMwS5jUlDbAJpxwq8pTAZjlGRj2qaIDv-lE_x8GYDYCikIO47nNZrhapUhQDR8D_IAMkQVSbE9ZwrU3uL9mlao04ddSrwyp3mB89Bl6sIEQnfvm_xw7zIR1gsoEUcFnjSyF6AUMysv3GOSJjuXVg4Th4mKBPB-sXfDAJhHLHbBHeZ6sFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5H-hrGqrHDlO_3RcsnQounx959oAfGnHpsc2V_4o8x-wQMiuKS6aBX_2RXLEtkgbhBFYoVAoNAYgTTQXOUNMDCFO4UK92sphWmJRxwWTFhVC0wHAdW-psIIZaloNM3emF_R0mnis5EGhajvIcWoEtKbwoqx0h-yWhu1tcIRb_D8aZ6TRpoOjAJ3M1xxRdugUqRLQZkm-YtBUa8LSsCuWAtA8GUTH4S3ArPVMivLLOBZqx8raUOgLwY0AF9B0yOR5FmyOQlZnu3EK0SqqqE79ZF_r8-JIcUOYaK2e8UM058TZLve_uH9Pq7A2JQ0LHvbz4TyctPz0_1D4lKeb2fYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw3Y7--BmNTuHR7Ix3F6lAEwTEA9euFg4jmufA408ywfcqay6G0CstNF1VEEXy9h2bntRpfWzT3FETlN900ecTPI-Pe_XJuGNhTdYul_JEZgWx4ZGjF_b6Ndfz05sl3FY7f7o_hboD7rs1dLnyTdOFMOYR5d2YBD_8Rl72NIGe7_Atkyp56X2KJuMjgvyCv1YGhBJbmcoBuWzZ6ZMag_9WhCFb5gu8jdBvJTrg-MekuI6BeyjzBBxq_4kF6La8BeEGqZEprQ1OM48wDf6ouHwpt9Dm4VwRWo3HpFzoWgJJZSQEEASFojCx-5BUKNSu8ykRnQbZQR5WrQ8wQnm46XYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4luywFmn6Iq4j5UI2u3BZOSBxu4rBx5gk0N-Bd8LsJuRWMQDQqgj16LtF5UC9FPKq-69sjD55dGdjHJh99X-PWTXWjAM_dmSVToOLz7KOVWNsXMLMcM5mVyPsuFU0YoMBP1mgGJPo3qPUJvgo-QqTyh0Du7Bil-E_1zwBz7Zx4piUVwX9TJeTy7SkktdxooXGinzWQp5DtMio0-0pe51GBLQ1v-0VTmzK1hMkOlO7XcouriqQBas5zqstrLQeiKqOrueP2XJ5grxY4q-blZELRu0RIaJEZpxGDwUHbgdKSzeIrDRb2KOAr94ronxmBv4HiapJyl88skFRJsZT4BzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نظارت مستمر و خدمت رسانی بازارهای میوه و کانکسهای اقلام اساسی و بهداشتی شهرداری مشهد در ایام میزبانی میلیونی مراسم تشییع در مشهد مقدس.
Samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669144" target="_blank">📅 18:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7891a68941.mp4?token=hLKnILPgQD31z6bVbgpvFjGAYsWSwrX9YVSzP3bQTRfiQBI8WuY18l5TFFpFPjQwkdVVN5QYvlL9cl8W7nxmdJFvKBPZEBfjNyzGWx1iKRjECFbOZ8L3hNA_jVTxfba3uhtYhWMyYacdsl1wAPKuF26zCBPVnF0ozdv9RcwyW15i8V9dqnH1GJFsgylnD1iDG-zZMt7K1f4bIP8R_M15hPAR7yZ3Lmki_haRoxQEqaQgCwqZTrNxl4BA0D7cqFmshrCLLFygMyUiPMokqKPB4-f04v0CYn7PeEvuIr5rNJe2JGLIF0R5pISo1C8598Ppz4rDNcInRX2sXxoY2rhX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7891a68941.mp4?token=hLKnILPgQD31z6bVbgpvFjGAYsWSwrX9YVSzP3bQTRfiQBI8WuY18l5TFFpFPjQwkdVVN5QYvlL9cl8W7nxmdJFvKBPZEBfjNyzGWx1iKRjECFbOZ8L3hNA_jVTxfba3uhtYhWMyYacdsl1wAPKuF26zCBPVnF0ozdv9RcwyW15i8V9dqnH1GJFsgylnD1iDG-zZMt7K1f4bIP8R_M15hPAR7yZ3Lmki_haRoxQEqaQgCwqZTrNxl4BA0D7cqFmshrCLLFygMyUiPMokqKPB4-f04v0CYn7PeEvuIr5rNJe2JGLIF0R5pISo1C8598Ppz4rDNcInRX2sXxoY2rhX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حرم مطهر رضوی در مراسم تشییع پیکر رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669143" target="_blank">📅 18:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqJwy1AGFlRN3TFmnYBB5P3X8EhG5nxgdU2DzcPPpJWXZ-RxFxU_XMteJGCxUs93JqzOmjoF64qbu5GUSxbGtmQXT8bkfRX3NsEGrtx9NFWS1Hxdxoq_KDf1iQxa8p-Kex2P-79xUJGvE8PepONrSRmbZOsYycbaybnRQPm-EEZeNzdshR3BLwMSPFl2HIfncpNvngeYu-4uL0I65W5oMHgTFK-9n-10u3DmfP3-VfE3yOR11CvmKavC5l-RfNFBTdvdifbfD7ozLb_dWFnkkSbd8_vzhEs0X2Gh6luxQ-lip4G_A8BsMjrn0xTp1Nx8kyC5szboQNsM0y5eGnu0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد ضرغامی برای واکنش ایران به حملات آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669142" target="_blank">📅 18:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2e1a3e20.mp4?token=F61qtNQ4oDi01bVumiFel_FwmViTQi9dBrd3j_PWrH0uJbBnb0XfuyfuZZH2M63hiPidPLu2JfrzlrpqORPzIZURcBwDBScNrOHvcHR00fZrkfYLo-AKLREXH6HVgMHl8_AM9HL1wACn4UAQD8tIG_47BGAKdeWC3-9humEvbH0ynUEl578yaO2N4hjg8nMbISbjjke6S50I3GLZSK1LDq_UiTeTAUItFf8cmUNp9XqHDRihf5Rp1ra8i_oXaImc6Ahil4UXlkOTILiOciPhmC1CN53LBVE2bmV5keCt1Ol6Kcp65lIa03eVILlLvk73FCpnDxguDv2gkffOAIHqVRlrg6Y2E5vHrPysjyT63s65G5Gu73K8EMSP45Jbgux4Ppxs1yDvyd3FtWRTBGhel_6FRpc8wP6eEaXvjGZV4S2fQZCbSGJVXe5_jzRbr11EXAcdgDW0N3YqQ27G26xlquZL9oZt0AO9f_6MiHHTGh-yHCa2HAxtvybZnlEHCQ3JMoGf416b5pXMOg1H2TPuPhSLUFJmBAW4f_pVjtNmsx3KFGk5ky9iQdJngbIdBxKDXCdCwZKnvFnbDBBxwauHRIfhm2U0LKh4LQYo1jkWb9TI0n-YAKBVKO-LuY4pDEfMPsOoFLvIscDsXheYKhTYV_H3q_oal_ncS-ZLpNcttCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2e1a3e20.mp4?token=F61qtNQ4oDi01bVumiFel_FwmViTQi9dBrd3j_PWrH0uJbBnb0XfuyfuZZH2M63hiPidPLu2JfrzlrpqORPzIZURcBwDBScNrOHvcHR00fZrkfYLo-AKLREXH6HVgMHl8_AM9HL1wACn4UAQD8tIG_47BGAKdeWC3-9humEvbH0ynUEl578yaO2N4hjg8nMbISbjjke6S50I3GLZSK1LDq_UiTeTAUItFf8cmUNp9XqHDRihf5Rp1ra8i_oXaImc6Ahil4UXlkOTILiOciPhmC1CN53LBVE2bmV5keCt1Ol6Kcp65lIa03eVILlLvk73FCpnDxguDv2gkffOAIHqVRlrg6Y2E5vHrPysjyT63s65G5Gu73K8EMSP45Jbgux4Ppxs1yDvyd3FtWRTBGhel_6FRpc8wP6eEaXvjGZV4S2fQZCbSGJVXe5_jzRbr11EXAcdgDW0N3YqQ27G26xlquZL9oZt0AO9f_6MiHHTGh-yHCa2HAxtvybZnlEHCQ3JMoGf416b5pXMOg1H2TPuPhSLUFJmBAW4f_pVjtNmsx3KFGk5ky9iQdJngbIdBxKDXCdCwZKnvFnbDBBxwauHRIfhm2U0LKh4LQYo1jkWb9TI0n-YAKBVKO-LuY4pDEfMPsOoFLvIscDsXheYKhTYV_H3q_oal_ncS-ZLpNcttCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر پرچم سرخ؛ نشانی از عهد انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669141" target="_blank">📅 18:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نمایی از پیکر رهبر ابرمرد شهید تاریخ و خانواده ایشان در آغوش مردم در خیابان امام رضای مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669140" target="_blank">📅 18:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
در آغوش ابدی خورشید/ مروری کوتاه بر تشرفات این خادم آستان مقدس رضوی به حرم مطهر
🔹
داستان زندگی دنیوی سراسر مبارزه و جهاد و لطافت رهبر امت اسلامی حضرت سیدعلی خامنه‌ای از مشهد الرضا علیه‌السلام شروع شد و تا ساعاتی دیگر در جوار مضجع مطهر امامش، حضرت شمس‌الشموس علیه‌السلام به سرانجام می‌رسد.
🔹
برخی تصاویر این نماهنگ برای اولین بار منتشر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669139" target="_blank">📅 17:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b602415c.mp4?token=QWrDGXDCEGCRTzjyJ5dmvHF0tj-uLzU1SpesBFRrd5nWky2nrS9XbOueLikAaQ0zFGE3n6j9y3rOfQjK40QQRLGErtGEsRJcj36aX4ayrHZD_sW4907sUVHId-Lr_ThecxEJmTCOj0FSsFeqkUvkf_nIZxY1fWOxS9kwcgqFVg75Hsx7LX3M5JTG65084ScE39pIv_nnU96zH08Ys1nAdnjkQHLBmWaXJzxP5pQR5CvZn-KdymmbW5nk5KIfBwZQs05MntC_fCorzXm_QylTbj5G9TBgVhdumvOUM4SJT8bhwPvnvNXPo3FxB_osPxh2rfwWanNQNwNRsIqltADhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b602415c.mp4?token=QWrDGXDCEGCRTzjyJ5dmvHF0tj-uLzU1SpesBFRrd5nWky2nrS9XbOueLikAaQ0zFGE3n6j9y3rOfQjK40QQRLGErtGEsRJcj36aX4ayrHZD_sW4907sUVHId-Lr_ThecxEJmTCOj0FSsFeqkUvkf_nIZxY1fWOxS9kwcgqFVg75Hsx7LX3M5JTG65084ScE39pIv_nnU96zH08Ys1nAdnjkQHLBmWaXJzxP5pQR5CvZn-KdymmbW5nk5KIfBwZQs05MntC_fCorzXm_QylTbj5G9TBgVhdumvOUM4SJT8bhwPvnvNXPo3FxB_osPxh2rfwWanNQNwNRsIqltADhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس بدون هیچ توضیحی کلیپی را از بمب افکن‌های B2 پست کرد
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669138" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669135">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STAMg8hs55-5Vi9b907XEG8orRcMaBS27Bm4jwww4KikepFALB-B08NjV0vwjKpAkZH0QcttMMhJc-qZ8ty3ZUx9DF1sqMawIyAHgyL08VyCDMCg3zvfbOBHu3JvQGZ68P7HyYTQG6wCIMNOuDvbj4Gw5_A41wri4lgHPJBOuj3DzsHiCoKwtdJbEBk6g0rorFfQd1T9ws1ZYdZ4sMSPtDpPhjLgE1hIMU928b34x4k7ul2rbHT4mnehLDkriMxeUpNLjMOQM7mxsCSvZrBHkZyasP4i_fmLeL3JAYWRpKhrawdeFYEw0wF93AxLdk3hJU2KqE1--hl9VmWYjepa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI40CnLoryCBxDitz6BShn16H6HVEVBc4ZVsP7JlXKAIoDI-UWVrCZJzb32mlkY-5yNttCppR0Ml0KYYwWQRjIUR-oQgc_wWKDx1PYrH8CKtiYKpS-a1MCI7OoxEUYZdBUqzhfqgmarla_nzQpPvwNQDUk_Vld1r7Z5PD1ECT_cUFV7I6wPm2pZ_M6cprEiDRYIfji4ADQ3IMIczP6_GGbGSU_58x6PwHvfnPGaWyUcc5PYCph-ISgnVaXKcgs7cGlJmql_rdzDyza3386rB7hB5BuaGRN0FWst8sHntuTj9_s_Mo7Bnp-Hxb39yCIe6L34u4ckdMWgRzPo_rQICeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d47984cca.mp4?token=p95OxNLguPv2z1LtjDQaeZ1EVVKz53On1-cHR5CzL1LB3dT5yTcAqsP9BWrXdXcyC07InrF9C06lgbfqAVBBfTuN2IlngaeeFPxSK9wTAh6PtyFaIe0KLjwo1XA3VhRZOj4RHFoljYJCTx_vdGsvKpRC6ELS-WzDmnmaqER1ElS5ACnsjiFPw-iD8K6CL-186r8whtMOesHRHeoPd1Y2_i3a1U1LlzTBTGZ_hCkWvSn4kOatSA3CUNVtCrJRvSn0krxuRYZKq-pFYuR8Sl_j8bZAEzYcgEntcy2I_mMBWbzRHsIrh0lXN0RH1LnqaabUF3KZcmYFhhAgmBcxYd2CeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d47984cca.mp4?token=p95OxNLguPv2z1LtjDQaeZ1EVVKz53On1-cHR5CzL1LB3dT5yTcAqsP9BWrXdXcyC07InrF9C06lgbfqAVBBfTuN2IlngaeeFPxSK9wTAh6PtyFaIe0KLjwo1XA3VhRZOj4RHFoljYJCTx_vdGsvKpRC6ELS-WzDmnmaqER1ElS5ACnsjiFPw-iD8K6CL-186r8whtMOesHRHeoPd1Y2_i3a1U1LlzTBTGZ_hCkWvSn4kOatSA3CUNVtCrJRvSn0krxuRYZKq-pFYuR8Sl_j8bZAEzYcgEntcy2I_mMBWbzRHsIrh0lXN0RH1LnqaabUF3KZcmYFhhAgmBcxYd2CeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
حمله به قایق‌های ماهیگیری مردم در عسلویه توسط خوک نجس
./ صابرین‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669134">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcYUDbKmFtadaNJPl_9euHn46K9tAk4MFXtU3Le9AgTWEixIB6-5trswMvE1d0rYbPxvAd3CVio571I-L3Xh3bOkAbQU7tUslIh4YmXzYkDnZ8FtQhbVSa-6AHW_h9Ys_lLl4C5T_si55rYrH278BOnTnQsCzXZ0F_TW8OUj5vncQWCPLhcBXgkHCguwNGRNWighW8Gif9fuwu1bBAXcgpFJUbdPosG7DqnvKudE3LmZTOlNIuoH1dk6QskvHr2JcA8w8b4MU6xlL-Qwsq4_3VGLKwiCWYCyKkPA3lsEEuz-oQ6PgNfKIoeoMsXGSRf3N-RlKstaXV8gUASFAqo0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت تیر اردوغان موجب دردسر نخست‌وزیر بلژیک شد!
🔹
اردوغان در حاشیه نشست ناتو یک هفت‌تیر به نخست‌وزیر بلژیک هدیه داده است.
🔹
این هدیه تا زمانی که هیئت بلژیکی در بلژیک فرود آمد، باز نشده بود. پس از باز کردن بسته، آن‌ها متوجه شدند که داخل آن یک اسلحه به‌همراه مهمات قرار دارد.
🔹
این سلاح بلافاصله به پلیس فرودگاه تحویل داده شده و هنوز تصمیمی درباره سرنوشت آن گرفته نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669134" target="_blank">📅 17:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNWrrdhfY9r_1IlmJPQwVHFSXkkKe5bfGyPyKtCliFvgGq0NazWoxMVvkhfIBNbVwKKTxrIgZRbD0gHosaSkdUilzWQY2TR0RoJOZAx2wmcmNpIbu5K-yjH45GN7omRkaImoIBzeDBg-VUlSLYHpaDPPXWvGcgBNMkV8cXXsqzLE2_sk2uFrUibFjTrAHVwDg7tPjdic2_829oS5ig_HVjwqliCCRQ3OzJRY0pXG9QqZ_NK_MCVCwNjfTMxGU4VRUlCT1raOWnEiewvs48nMHyVCFwURbhbsvr2WYe_mV1GSh_JwrNKTC9s137VLxi_O_7IawVi8Y0bAWRZJ-8m9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfbaaxpJVS8a3cL_P-KXNE9sazTLbMqDsH17Hgp0f82AGpksrj5qhYV1LLspnnfjGQ5O0biH_q5AYunswtnZvZmwMRZ1BYYHxXCoXdx9yQEJIbk_O4d6Zh5JPlNpucPlgcQwe-U577-oR1jXDGzKbI0r363Ax_NN5nG1IgGpB_vqXsCsjQ3_T8cRD954DqEki56Vt0bjLqXud9bzC5RyfmIyypOiE1PXFOeeJM8uZ0JdggSgzdgC8GpY3Zx8oDM3Yvsazw8G583APMlMum1LZ4yJQNy4zczVU5xOcRc0i4wyOuVf3vxqsvg9z5_qQ-3_RabzNgo-wZAyrnh1FVZo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBOS5R9EOUfgI8fNi6FmFk1q3VA3ybVp2ekU37Mmi-jEA5FCwH73dawdmXBmuv4ORurjbZXOUb_toKOeikV99Lfv8nZpKXkW0DK0Q8Pj5YkITNEeXYf2rNeB1MWYpKncEEM6pOEGMGDKeQ4vNs2tDdiU2TtQ51oWKDs6t2Va8RnVmTtUAxr2jFTtgzZmyf80SyM1pNSL5iOVB8nsNMfeiYf5h5uahNZY7QsXdYpT-J5wNr6o_OyA38ToxvM-UIYD6x4fqQdE4gsyDxYE2Y3pnGorEYOZ_HYtkx7Ua8m1MDx0MMt18vM_mRlOk4oNsoWz1SnNWRluEo_u2p1jMVXFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8kY7lAyVTpEJO04JGROakMa5eIOB1knOuN7gsoUC4TKGWGfXIhdtAy1pa7Y8ab9I2-1lp8rb8RMQnOp4wGrqIsNVxwMqljdyR6G5IHhcoyqlBRkoGUTS2vWkGgN2MR9mnc3uVDxwsVOutuhtbeGBHHlZTvzddGBNpZjAYgON69dABI-Uha13u6LJ6wfmimZ_9Q6mq_g9lw7aT-n1ZPBLxLGL1P06hnrd5IXnjd4E80RKGm0xjm-EBh_F4OfL6dqT5o2LhPl7znbpK9OwozEy01cGPvEJrif2iq0VsceoniL1BgDeMDAof15G7BFeuZQl5jPGiaqmrmzUpR1qOgn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2Ur3CsPt5uiibvqOcFji-HVUwioRK7zRwG1NWrIGEkP4Cnlhmw6Wm6JI88SArQN8ryvF5IJaZ3wdzlyu-Z28ZV2JrHhq4fM6cHZQkcpmI75tIEBcuDiHL0yiDfr_Pp4gjz-Isuvrzx_EV-3qvAWP2V0MyEAxVsLoFXFkSXj6WT0_EixkJJYB8Pf-DRqt8rO9L9ngAnjoNHJUyIQiNLSY2EBKM4NoZ356ojg4nnFtWLOYUziRHPVAZuTl_gBkgLuDXJR3QMQriuRCcrXkoj4kAoGwhio-xX2GGcBpWhYUrSi6Hy3xlCKKgTN2OkhhgO92GOWfGGTExx1zMgYlYQwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3iiZi_kKe_mWO2Vt8t4U5_PeurbHvdbQOa-bvAAUy2zekIMm0A4WvIVw8XJyfW57ew7u_edjrBDjN29UmQDUeQHFG09BtcnF9HyLlbqxpUDO-DVNaevwln77ohuu5swjeu1AujB2j-_5WkR8pH7DrOAf7WBI5CiRZuCMK6HfhpJGNFKWJg5O-CFnD9yMTJxqrqT9JMzyDSN0PNx5bceQ8D8ZkhRFTvEPaeZ8KvRUZwC1Xj2TzHTZapV_gh1iW58gCun05VcLgAqebTxoIiJ6FCiNc61IsAog0Gtv0viqcx6cgaKRWRPd3F7thf-p55ZIrXfI7nq48qUSPhAbvRqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSwSispwCXHGeqeDJwhylEd60T4Z9fNHFs91f44s9T6Mv2e0TRhYQOQWbKJkJsgy9oNOKIRJ4jl6iG5DQXxy1347k11wMi0PFZ7RhxQnTxcPOl0ZwyQjaYZ-pqaRbBxxMGbnKy_WH3AFZAAyAJny0awtzYvWKEKQKEzcE839LTXYUK85F_qAknMmxdrfT7mcXiwUdNAakaY2dLF8cViefDkfIKIgFByctiUphL-Sw6sIHGqwQnsbc0nYIm-FzfNsDFKuU9MhGYdl_3U8XIv_tfhKtnK9i1e8kOZLbjI3_7a0XuPcmng-Z1n4VrnwVrq12HX4pdnzHUKKseWZ3Q_c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpXJ8hM2xDIxQXQjVH7M-AZk0dR8ZbfO3j_GFUXJjk9ZF6TzB5QBhMGYqBbev2HpgW8EdHvvgSt04YTk4JX2KhnFsaKL2JoKjzTn78CPcjMi670mu85speBVz80pNeCud55XaSxXifA8VrK_ZkVbJAg10YvzUnMD_uifCqgyHTQGEDoa8g8nXg3ITu7F3u1ZuMd_7qsbk_G1xejtWS7D-wB-5kQDTSXZDHZsLvrzQfWYhMbecXfaZWVw6xfzjPyBIch1mNQNq9csPKbIIAWalrvzz6Xe696fIqQkEfbmSnv8Q6gJmJuzYvVOxIglz5MJDKjo_EcSnlIqQaeR00EEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYIQ-Me1Lxhw-NvjE-2xNU4jSFlnnfXBYm3hHsh9EzOK15fuyG7t9z8O9K3CpfbhIMlU9zx5LxwKqRc3V9n-N-PFoezqe-k5MNcGbj5i-rRMucPs9yqq7KgaiBhQaVsPNlY9yQLHpNK8qI_T6MJH1orddmJnn83IFzSSaMFw4NppwPFepq-2Mh0bHxG16OaGS6l3vdMJWUJCriQNbo8aESFx3LhEdG6NNVKensyf_oIzM8LurKm8V0iDuSJcsMRpAAye1w10BtDr2oCKnYvd5YEB93_-wNNJhxQjydBRF9ZxDvQ-V-1GJIzmfBNWGxdjaL6_eZv4nfPNKocGKh8TIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXmQo7kR2En5vor-Ncc_w9oydVnNof9qH2aw5fYPIydnKX36P0UYpV1XgRPADyDWJI-cKxj47Zkk2YpieTLNHiylvvZVb9tVdEI4bIcJ83DFMlJ8I9DjZlfdcLvYssHjs6vow0C0_Wd1nSA4H0VlGKB9Y5vMDh19qW3BTD1stnwAVd_sR-Kv_G-s3XnNdiLpLdrl5lISqL05ciHYfs2JE9EoJEcMUzu86zYzX_XP0l6znxfW1NtedriqPQczdaTx0ne2XrIDQQhrH0ouVHx8ap0Hrc40nT6zxiG094NoMQkxSlY2zqEah5DS17QxEz35wsdwx7c2VjNSw2S2V32rEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات بدرقه و وداع با رهبر شهید
▪
️شما هم روایت تصویری خود را به شناسه زیر ارسال کنید
👇
#بدرقه_یار
@badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669124" target="_blank">📅 17:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دریادار سیاری: حضور نیروهای مسلح کنار مردم، نمایش اقتدار و آمادگی ایران است
🔹
رییس ستاد و معاون هماهنگ‌کننده ارتش با تأکید بر اینکه حضور گسترده و میلیونی مردم در مراسم وداع و تشییع پیکر مطهر رهبری، جلوه‌ای کم‌نظیر از قدرت نرم جمهوری اسلامی ایران است، گفت: این سرمایه عظیم مردمی، همراه با پشتیبانی ملت از نیروهای مسلح، مهم‌ترین عامل اقتدار کشور و ناکامی دشمنان در تحقق اهداف‌شان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669123" target="_blank">📅 17:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=XWgMBfzFCnOOYjNLfIXO_PDPoOikVVQcCKsmTnHSf2kJCfphbYi629FnNjCuiFTqyr-IfWDXdNDyZcktXP1i2-BibJNlvmkUwFYzJA9k9AF6oKQa0mrgQhCPowcI_65VTKIVjQT4vB1nXNer03DvnSab0AdbXwWsCu6EUnqF2ZBcWTTHD9SsZemjFeveVZ2H50rpThKy4tbqvpe6bZC3N39tqtSxNs7IsbqGnyU3obBcdHPlsP4t3w9PwP2CT4PpHmMFmqITA_f8-cqKut44W1BU78xHWaz-fK7PdEKTavrFxfd2qq70NofmBvaRC0k28BIDaG2IRv3mnkuNLeuKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=XWgMBfzFCnOOYjNLfIXO_PDPoOikVVQcCKsmTnHSf2kJCfphbYi629FnNjCuiFTqyr-IfWDXdNDyZcktXP1i2-BibJNlvmkUwFYzJA9k9AF6oKQa0mrgQhCPowcI_65VTKIVjQT4vB1nXNer03DvnSab0AdbXwWsCu6EUnqF2ZBcWTTHD9SsZemjFeveVZ2H50rpThKy4tbqvpe6bZC3N39tqtSxNs7IsbqGnyU3obBcdHPlsP4t3w9PwP2CT4PpHmMFmqITA_f8-cqKut44W1BU78xHWaz-fK7PdEKTavrFxfd2qq70NofmBvaRC0k28BIDaG2IRv3mnkuNLeuKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته شدن پرچم‌های انتقام در تشییع  ۸ میلیون نفری امام شهید در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669122" target="_blank">📅 17:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
عراقچی در گفت‌وگو با وزرای خارجه عمان و ترکیه، آخرین تحولات منطقه به‌ویژه تنگه هرمز را بررسی کرد و بر تداوم رایزنی‌های دیپلماتیک برای جلوگیری از تشدید تنش‌ها تأکید شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669121" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669117">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHmw7thPk9yFZK1vG7YTy1XUaSW-_i13lrQzxzk_iNiOnXWGNYfwiCr5ku_AHGIX87zkldH4uAsHI5enuNSDdeF8Ydl8Dkvnxeu7tKeCnEVLz4U6Dbgh6FmyuaS0O-0SE4NIkR4n921zqExAVnNN_IWD6Hxt0ARTkUXuULjKKsHeYaeMMKqf-KW7OVzoGJjItshq29pOI6gl_9qOEIjhZsZd58bXJO_XcuDo4U99ykYiJ_MVRQrNKRq6tfZOf8pxfU4hVKBZyiq4djefQuh9Hal40arM8zn4JwxS0UdR9l0rndcQ-mjj03LjlvEw4V1URmozMzqMDsstrhxcfvgW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vA6aPqIGiewOJWA4qme-vuyoNZU7LzSsCm9hUD1k_24ln97VBPU7E-wbsM45O4H04brhD99VwKEmKS1uoIZazKqXxcpTS_xvc4VyjgNqenZFYFUKMQ33MGUbTK1hmzws2uqUe0UeehthpHSlQiCSgUA_oxKf9xwV_0j9crBg2rQo3VIr1zLy33qomoqG986g0NrWzJ9CVaTHpA4bR55rn5NYh-Q-WnTji89eo4ipnUDPIiNUrc2Ho9xHBmLRA1fnjICQV-VWESqNyBZMnEByrG0QhPBaP9FiO1cSbUmJNXysWzXIe6NmjOvtkEm1OUyVIlV9ja-FMhsQAnGKR8Ybgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBV3qTFEXooJWgayO1z0ouuzf6gdoNBqNaV-nPboSqzhxSaufD6p0JrR6TgzU_Vqlg0Dv2crmf9kBAY4Ma26tDBnbZqwbyOSpQvJtRhLMSAoqJy92RBBF7CB5D1nF4IkxdzyZV09XuQ0LHgtQ82FeQpIijaOL1OOKpfJ5rECqDM6DAYMf5EtQymEvgbLmA0UetfUROUzDuRLk8-YORXybcLpIK9fU-d-MMs0ootyGz75SV11dd955lwt-fGNNyVfE60HZPFvrO-FtpFwrtNKOoDqq1RyxWqZPyvcxqYtLHanY-U-Wt2jMjueypGAzDxrJtv7XEsqoWxERT-86kzgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlj_ZwR4PVoVhyzINUcuKSzh16TDJDn_hPSLeuc_stB-XF3HZYcuiBm7zsTc16bOxgz3Yq9EOcTjdVrfHEuxVTnwOkSCsXBMiT3FrQMyqnv8va5XUCrEsGPwgqhplt0kmW_1KLmN4WVMTPrq_m0x6UY4Wiul_SHf5dynqgbMLupwwNkQ8XCNCUmCgkwCLQRKniZ60r5CBx__sAbUgEJ_qvcC3sg5eobXrmVqXDNuvsplBNRMLizJ-0n2XKotvFdj9jVAhSMQBVAjik7wOhdjlwoYFTufMXJjFepUaqZr9L3Hg3ExqHbce5zV8KfTi2NoBlUeM3GGWEUzCbPPQZ-dGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
معاونت محیط زیست و خدمات شهری شهرداری مشهد: از اکران همزمان و یکپارچه ی مراسم تشییع به صورت پخش زنده در کل مناطق شهری با استفاده از ظرفیت تلویزیونهای جدید شهری و کیوسکهای هوشمند شهری در شهر مشهد مقدس خبر داد.
Samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669117" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6f04bbe3.mp4?token=sZseQmVo4SM6N_M82_wd5y2uOqnBJPPD3DDWtusMyRfVZRTRRVjCFSrC-p7EPEil9z_zFyDomberG9q4OfpsQKC3AEESeT2J64Hcx8eqVaKz22x4KUaN-DAE88raql5rXuz-zCFz2l5h6_qkO8YXUc83GzqkKG54Qh6bfCLBX8L5TJIy9I4cp19FWXfZmwYvorz2Rxntnp2aOYI9d069ykjdt44SclbRWpoT7jlcIDt3s5NHZRZLNd_mca2QSkdwdw9DavZiEX2IUTLFQ-PdcIwJl6tneU-w6_26r4tv6JeldZYMSTqBCVI2yM5yO8v6hszKJm3jtQLiBN6n1BYCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6f04bbe3.mp4?token=sZseQmVo4SM6N_M82_wd5y2uOqnBJPPD3DDWtusMyRfVZRTRRVjCFSrC-p7EPEil9z_zFyDomberG9q4OfpsQKC3AEESeT2J64Hcx8eqVaKz22x4KUaN-DAE88raql5rXuz-zCFz2l5h6_qkO8YXUc83GzqkKG54Qh6bfCLBX8L5TJIy9I4cp19FWXfZmwYvorz2Rxntnp2aOYI9d069ykjdt44SclbRWpoT7jlcIDt3s5NHZRZLNd_mca2QSkdwdw9DavZiEX2IUTLFQ-PdcIwJl6tneU-w6_26r4tv6JeldZYMSTqBCVI2yM5yO8v6hszKJm3jtQLiBN6n1BYCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: تا ۲ ساعت آینده پیکر رهبر شهید و خانواده ایشان به حرم مطهر رضوی می رسد و مراسم نماز به امامت آیت الله نوری همدانی برگزار می شود
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669116" target="_blank">📅 17:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
فرانسه و آلمان خطاب به تهران و واشنگتن: به مذاکره برگردید؛ آنهم مستقیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669115" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669114">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
روایت زائر عراقی از حضور در تشییع رهبر شهید در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/669114" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669113">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3692b8c6.mp4?token=gz7_H0GZVbbr1r0Q3X_IjqUXUvzRT8uc8bxgrra_n6th6TpIF0U0fDQOVf7uRlaPPG9NueMJpaX84DwHazqex8DUJBfHfO3ouYdxL0tuueePUkCaKhFsRR5Khomjb190GbuzuDn1TMMA7HJVig5B6u7gDds5E7uTd0Xeu0jFeKayx8EWhzkJpw6L9cFsiZS2R-MEwyJSTeQjiPHPUpdxNMWghhrOfmUWPJhygLKqYG_9ko4u1UwMYW0O8FQ6_Jh6bnsoA1ed32ikqqT7U3BSD18cNmGwDHZm8CGYi-VdrRDXCeywtCK6z0MQq_iPLg7aFRRH2IeoYGKfut5cSMYlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3692b8c6.mp4?token=gz7_H0GZVbbr1r0Q3X_IjqUXUvzRT8uc8bxgrra_n6th6TpIF0U0fDQOVf7uRlaPPG9NueMJpaX84DwHazqex8DUJBfHfO3ouYdxL0tuueePUkCaKhFsRR5Khomjb190GbuzuDn1TMMA7HJVig5B6u7gDds5E7uTd0Xeu0jFeKayx8EWhzkJpw6L9cFsiZS2R-MEwyJSTeQjiPHPUpdxNMWghhrOfmUWPJhygLKqYG_9ko4u1UwMYW0O8FQ6_Jh6bnsoA1ed32ikqqT7U3BSD18cNmGwDHZm8CGYi-VdrRDXCeywtCK6z0MQq_iPLg7aFRRH2IeoYGKfut5cSMYlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریایی از انسان؛ اعتراف سنگین مجری سابق CNN به سیل خروشان جمعیت در مراسم تشییع
این یکی از بزرگترین خاکسپاری‌های تاریخ است؛ رسانه‌های غربی دیگر نمی‌توانند این جمعیت عظیم را نادیده بگیرند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669113" target="_blank">📅 17:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669112">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=CFomYaf4ILP2ZL8X4Ek__mNi-qz_DsoPFdBSSqp8FcCXVBC3XsEM6FYfUdp_ehqimvXK7N7Hm0UAcP14ddpRywK3pCVlwuG5-c3fXjjl9AL8TgduqvPh6pCGo3H_7tChPg7ZlJ2EJnSnIoTjBIWoglZ1RyJYY8hfquqSiFvPWz14UzDzfB_d67Mad3tWFHU5kzT8OGfA4jaVXLxHZ9VyciaPcM1UuMzIElwI64onY7jh1O5s_4736odAiJEiM22p_6II-ASKz-6Mt2rZTpm_4CQR6pipNmhNzlEUqCz2lkie01yrLY3W83P-OAukJ_SyoUPVffXfYqjMegq95AYmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=CFomYaf4ILP2ZL8X4Ek__mNi-qz_DsoPFdBSSqp8FcCXVBC3XsEM6FYfUdp_ehqimvXK7N7Hm0UAcP14ddpRywK3pCVlwuG5-c3fXjjl9AL8TgduqvPh6pCGo3H_7tChPg7ZlJ2EJnSnIoTjBIWoglZ1RyJYY8hfquqSiFvPWz14UzDzfB_d67Mad3tWFHU5kzT8OGfA4jaVXLxHZ9VyciaPcM1UuMzIElwI64onY7jh1O5s_4736odAiJEiM22p_6II-ASKz-6Mt2rZTpm_4CQR6pipNmhNzlEUqCz2lkie01yrLY3W83P-OAukJ_SyoUPVffXfYqjMegq95AYmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحن پیامبر اعظم(ص) پیش‌از رسیدن پیکر رهبر شهید مملو از جمعیت شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669112" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669111">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2154c194c3.mp4?token=NI70pPT5A1XaXwDM1dyYkUShhApzXneIgUab54gSTcicsDuE3mTNPKpRb3IEmOLppkIZly9dkWL14Aa_wee0CjjLJAcKT8-7TPoe_JkQFeMlg2CbRlzD9Elwy2WXPUnMsdK7S7KFJYa8knHG3h9oIWzIEY3cZpwej1BUCjssoZg6xdhP1R41GLykQq0wW4kuqQ5tg2W6FzFJbW1eV1tWH4C5gNEN_66C2RXqbFk5TVbqtu8luj2-FS_uyjkOMO1csjLRTjhzo__mhSA4bbSoaR3JG6mzjV4SxjAG2xAx6exS7qr7tGMfMhLtZeU3-XH4r-HpBnca6WjHcmSwn2th6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2154c194c3.mp4?token=NI70pPT5A1XaXwDM1dyYkUShhApzXneIgUab54gSTcicsDuE3mTNPKpRb3IEmOLppkIZly9dkWL14Aa_wee0CjjLJAcKT8-7TPoe_JkQFeMlg2CbRlzD9Elwy2WXPUnMsdK7S7KFJYa8knHG3h9oIWzIEY3cZpwej1BUCjssoZg6xdhP1R41GLykQq0wW4kuqQ5tg2W6FzFJbW1eV1tWH4C5gNEN_66C2RXqbFk5TVbqtu8luj2-FS_uyjkOMO1csjLRTjhzo__mhSA4bbSoaR3JG6mzjV4SxjAG2xAx6exS7qr7tGMfMhLtZeU3-XH4r-HpBnca6WjHcmSwn2th6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: مردم ایران اجازه نمی‌دهند حتی یک وجب از خاک کشور از دست برود، تا پای جان برای دفاع از ایران ایستاده‌ایم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669111" target="_blank">📅 17:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669110">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961d949833.mp4?token=kruGgAnelbjXInxQFQOgX48h60WYJT36EgGCWcvILE1SLUwcRRJ_2DQZ6izB5B6hxASdzP9KcuFrJw1LcIkNcWwwkKwdKs7CVz9Z03KWDorxH84CWS3ktj9JU2PutDMzaa9AVAmdR_Q1lwrheU-duQJ9pC2Fw1cGU6yrgQEiXIyL4IDVjDCf8A5yI97xR2EqY74BQYq6BjTqwVGc0j523pXPEuO3anKsWi7f0AWDB2JuYiPqhCnZCJvbrhifBHLONNvW_D33PwmP8KTHk3RJGm4hmcuxHyh4qwS9zBcutbUTH2kkVfMXdhzRDB_ypsHo-7aNh71gNDRVGC-DtUFR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961d949833.mp4?token=kruGgAnelbjXInxQFQOgX48h60WYJT36EgGCWcvILE1SLUwcRRJ_2DQZ6izB5B6hxASdzP9KcuFrJw1LcIkNcWwwkKwdKs7CVz9Z03KWDorxH84CWS3ktj9JU2PutDMzaa9AVAmdR_Q1lwrheU-duQJ9pC2Fw1cGU6yrgQEiXIyL4IDVjDCf8A5yI97xR2EqY74BQYq6BjTqwVGc0j523pXPEuO3anKsWi7f0AWDB2JuYiPqhCnZCJvbrhifBHLONNvW_D33PwmP8KTHk3RJGm4hmcuxHyh4qwS9zBcutbUTH2kkVfMXdhzRDB_ypsHo-7aNh71gNDRVGC-DtUFR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز جنگندهای ارتش جمهوری اسلامی ایران بر فراز آسمان مشهد همزمان با مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669110" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669109">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98c78bc00.mp4?token=ooDrQ7S94C8022hZOXtFXr_QZGKTyS7fT7Gt_3b2Al2cFhWjhXMfwtOmd-tfVDBrzGGp_W4tGANAHKJl5pQheI1zcAJLaHeUNGobjteQBKCHvMbrUzrD8EldI6KUNzWv7e73ywKmpL7UBHr9PhboVm_yq7zRvL1U-nludbF3g1aWq_YodsCff5K7otcmfYbs1z2aVqwoLgAqz-z7Ifl3ZfMpV_lGBU3PtM3BEsCEArkDj2j8Kdzw3FdTSvjCMlD5cRNUHnfBjkPHPk-vx6x-colZRktZ9000FuqoB5ixxqgNXVFFFoQWYMD7taHZAVneghzB9PYLgwouxZsL5twm44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98c78bc00.mp4?token=ooDrQ7S94C8022hZOXtFXr_QZGKTyS7fT7Gt_3b2Al2cFhWjhXMfwtOmd-tfVDBrzGGp_W4tGANAHKJl5pQheI1zcAJLaHeUNGobjteQBKCHvMbrUzrD8EldI6KUNzWv7e73ywKmpL7UBHr9PhboVm_yq7zRvL1U-nludbF3g1aWq_YodsCff5K7otcmfYbs1z2aVqwoLgAqz-z7Ifl3ZfMpV_lGBU3PtM3BEsCEArkDj2j8Kdzw3FdTSvjCMlD5cRNUHnfBjkPHPk-vx6x-colZRktZ9000FuqoB5ixxqgNXVFFFoQWYMD7taHZAVneghzB9PYLgwouxZsL5twm44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر از ضبط پول‌های جاسازی شده در ظروف آب در منزل مقام عراقی
🔹
نیروهای امنیتی عراق، ۱۱ ظرف بزرگ آب را که در منزل متعلق به عدنان الجمیلی معاون بازداشت شده وزارت نفت در شهرک تکریت(زادگاه صدام معدوم) در استان صلاح الدین جاسازی شده بود، کشف و ضبط کردند.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669109" target="_blank">📅 17:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669108">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e74e2b8f.mp4?token=HL4Xh9oK287thdhm9STsSfy1ENomQ5jBziLMLd5UpEUAi0VMW2oKsTBxkgj3daMPrTQJhpxaTgDaL5bltnVmP3JBza1JcrGHbdluvqcgiQ8dfnyIA5SsSWb8luc6TiDtNE4Unuhbwmr6D59DLlahiL5PF4WkVd_Mnyko4KSHoyO-RA-0HxbAdgUpDNzcIDwtZUD7K-OFUyVBM23Yktv4TVD7wGRjEzN-JMFZnWw2xKrxssK2Tat6oUy9GB2wKefNXpobgLf_tR01rt7JmD_V_L88GzPZDAgzuAg3y9FZpxtFB24F2RzBKP9MHS36RKu_xWl7cZcbsSw0b3DhqUIN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e74e2b8f.mp4?token=HL4Xh9oK287thdhm9STsSfy1ENomQ5jBziLMLd5UpEUAi0VMW2oKsTBxkgj3daMPrTQJhpxaTgDaL5bltnVmP3JBza1JcrGHbdluvqcgiQ8dfnyIA5SsSWb8luc6TiDtNE4Unuhbwmr6D59DLlahiL5PF4WkVd_Mnyko4KSHoyO-RA-0HxbAdgUpDNzcIDwtZUD7K-OFUyVBM23Yktv4TVD7wGRjEzN-JMFZnWw2xKrxssK2Tat6oUy9GB2wKefNXpobgLf_tR01rt7JmD_V_L88GzPZDAgzuAg3y9FZpxtFB24F2RzBKP9MHS36RKu_xWl7cZcbsSw0b3DhqUIN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری زائران در کنار خودرو حامل پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669108" target="_blank">📅 17:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669107">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3134345d79.mp4?token=X-sDFlX5Kfz2EjC6-7eOUXdMbbC4xs-aHlud7yo3KmlTGyceQX1tYihZcyR6mTw3EicfWuootqeLpVIcC4qzBjcatJYBb78pvc4GlwvIYSe6kd8REfdvkl9mxkgoMN-6HhpVd0ZtxBGNYIahPJhURz1FCF8U3F_ZgfQLRyVHR5rBAprcOcE0B3js6krRfNP2wce200hh62CwivJracwzwgl4RUcMs7OFSOJ8Xp_M_0iBYopO7UYNErcT6hGL496IRdCK1Sa88wm4iGag-9GHDltQhnbau-XKGNNNAo2NujmyXs7Ez3J4arlKzCuPTEiwcXsARwL8bAApHvS9B1RTYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3134345d79.mp4?token=X-sDFlX5Kfz2EjC6-7eOUXdMbbC4xs-aHlud7yo3KmlTGyceQX1tYihZcyR6mTw3EicfWuootqeLpVIcC4qzBjcatJYBb78pvc4GlwvIYSe6kd8REfdvkl9mxkgoMN-6HhpVd0ZtxBGNYIahPJhURz1FCF8U3F_ZgfQLRyVHR5rBAprcOcE0B3js6krRfNP2wce200hh62CwivJracwzwgl4RUcMs7OFSOJ8Xp_M_0iBYopO7UYNErcT6hGL496IRdCK1Sa88wm4iGag-9GHDltQhnbau-XKGNNNAo2NujmyXs7Ez3J4arlKzCuPTEiwcXsARwL8bAApHvS9B1RTYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم متفاوت خون‌خواهی مردم: ترامپ را خواهیم کشت
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669107" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669106">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c89b01cb4.mp4?token=Q3xAvNxM1Y-cZE2l-BcavhUOmKbowHV2jPxk-h2DfXNtdxXY_PgUtfgTX9RCaq9tKQFQirq7z3AGk6nKOvfDjCXRzR2TILCAtChYFascPmF9TEjdlp1bobyvpv4Pl0R0fH6pcc3QwbTyYvnxO6i8jHOpnuhDEgFfp-eFYNgnhUuUAy793dy-8L8CDBwP1B3cD3zMCKRhQXNQr1kjUZP2KOMcHgLAA47zhnd0d89nx2jluODGRqWOu71M5FxS2CaBdDMq6HDh9eIEoeogn09xtVgeT6K8ChCawuIGLzQuPCFVQc9mv2QmXupOifr-JOwpnBVpf44vNIEPinWVe7lRdoPu4dnuZDnpp3ImISto4Aq-78PWNsDbVboMYWBGzS2HsjZXhe8kkuWzexC66lGySegFAzKeNjthZzKpwoe6nQ7KhNgo2A88XptHVRO5AgiPsC5GPMqVnUOMTj10ehSBB0M1YtZzVG5xLxgBis6v5YBEmqj1mhOOKb7_DlwGgc1Re3bjQ4zcfJgcsLxLDXL1-ZLtD5pvUEuu4blLVrAkPcXwAFZ8AuErCBNAx-cg36GwiedakxIBgybsEvM1vFHG9w6ZDtvHljhAKGmVJ_kz9FaQHUyMmQ7CPMC3abnU-l2a9Mseun8KnGqIp1ca2zPeRxJyLxTbG6QEO2gPLBWRDcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c89b01cb4.mp4?token=Q3xAvNxM1Y-cZE2l-BcavhUOmKbowHV2jPxk-h2DfXNtdxXY_PgUtfgTX9RCaq9tKQFQirq7z3AGk6nKOvfDjCXRzR2TILCAtChYFascPmF9TEjdlp1bobyvpv4Pl0R0fH6pcc3QwbTyYvnxO6i8jHOpnuhDEgFfp-eFYNgnhUuUAy793dy-8L8CDBwP1B3cD3zMCKRhQXNQr1kjUZP2KOMcHgLAA47zhnd0d89nx2jluODGRqWOu71M5FxS2CaBdDMq6HDh9eIEoeogn09xtVgeT6K8ChCawuIGLzQuPCFVQc9mv2QmXupOifr-JOwpnBVpf44vNIEPinWVe7lRdoPu4dnuZDnpp3ImISto4Aq-78PWNsDbVboMYWBGzS2HsjZXhe8kkuWzexC66lGySegFAzKeNjthZzKpwoe6nQ7KhNgo2A88XptHVRO5AgiPsC5GPMqVnUOMTj10ehSBB0M1YtZzVG5xLxgBis6v5YBEmqj1mhOOKb7_DlwGgc1Re3bjQ4zcfJgcsLxLDXL1-ZLtD5pvUEuu4blLVrAkPcXwAFZ8AuErCBNAx-cg36GwiedakxIBgybsEvM1vFHG9w6ZDtvHljhAKGmVJ_kz9FaQHUyMmQ7CPMC3abnU-l2a9Mseun8KnGqIp1ca2zPeRxJyLxTbG6QEO2gPLBWRDcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تفنگ پدری» با صدای پرواز همای منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669106" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ec89bdd6.mp4?token=hRjpZ6ihu7N3bbTZ-OvxjqYTrD7IoGcSkOguciLemmkQOnzlzoLtWzQHlLyQmBvjr56o-6PNbCMWh188HvulcgmcI2u8OaQWCLkTWn7kFeExY604ytVZafPzGN0mx3H2Ax2F_tMcK-CryxYjs4ocGwQyB4ffXwN0ylgmGaIPbsbs399W8umH76-Bf4v5qI4j2_eFBTwG3aGJSrF83BrlT7TfHW7KXhpFCH-IaEZIOmW70AoTtD01D7fljXp5BxXFIhBhhzvJhKnuDc15TocZ1epHw24D0cD5zRRa83RV7FZMdqAmWoxR3TppFlrml4UZljVJog6CeYg7SuxXwX3TL7Jo-3oTaPAL_uIgx9ZxjnVyxLQ-cICGrPsfNelwOasCqf7FkHp8KU6TSVbqcnQLJQ6G7NqhJPf42TeQ0xZHTySWa7TqMv4q-o1df7iWpyO0uwXnP3IG7ZljiNKFN_HJCX1C8OZMkwGlqR_YPNEHTet2i7E9B5wd6rS4rhv_FeBpUchXH2wmZu5iAqO-EbTb3lzK8oZyzJ8IeaQFv-alJqGW1BlIn1ci_pwC7chq-LLviUOigHmIGcH8-VHU2OZ2Beeu3AeAg3FVIuOztwxwLXDEpBIaXH2qQTI1K3FIE_rtLQW5j41jezLodrRmCIgoa5Sg4Z4vR82spUrt54ykV1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ec89bdd6.mp4?token=hRjpZ6ihu7N3bbTZ-OvxjqYTrD7IoGcSkOguciLemmkQOnzlzoLtWzQHlLyQmBvjr56o-6PNbCMWh188HvulcgmcI2u8OaQWCLkTWn7kFeExY604ytVZafPzGN0mx3H2Ax2F_tMcK-CryxYjs4ocGwQyB4ffXwN0ylgmGaIPbsbs399W8umH76-Bf4v5qI4j2_eFBTwG3aGJSrF83BrlT7TfHW7KXhpFCH-IaEZIOmW70AoTtD01D7fljXp5BxXFIhBhhzvJhKnuDc15TocZ1epHw24D0cD5zRRa83RV7FZMdqAmWoxR3TppFlrml4UZljVJog6CeYg7SuxXwX3TL7Jo-3oTaPAL_uIgx9ZxjnVyxLQ-cICGrPsfNelwOasCqf7FkHp8KU6TSVbqcnQLJQ6G7NqhJPf42TeQ0xZHTySWa7TqMv4q-o1df7iWpyO0uwXnP3IG7ZljiNKFN_HJCX1C8OZMkwGlqR_YPNEHTet2i7E9B5wd6rS4rhv_FeBpUchXH2wmZu5iAqO-EbTb3lzK8oZyzJ8IeaQFv-alJqGW1BlIn1ci_pwC7chq-LLviUOigHmIGcH8-VHU2OZ2Beeu3AeAg3FVIuOztwxwLXDEpBIaXH2qQTI1K3FIE_rtLQW5j41jezLodrRmCIgoa5Sg4Z4vR82spUrt54ykV1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این مادر، همسر و فرزندش را از دست داده، روزهای تلخ تنهایی و افسردگی را پشت سر گذاشته و امروز آرزویش، حفظ سرپناه دو دخترش است
پنجشنبه مهرورزی این هفته، برای تأمین ودیعه مسکن مادران سرپرست خانواری است که در معرض بی‌خانمانی‌اند.
🌿
نگذاریم هیچ مادری، سرپناه فرزندانش را از دست بدهد .
💳
6104337737614782
💳
6037707000289144
💳
6037707000426027
🔖
IR 180120000000001264298063
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
🤍
🤍
عزیزانی که مایل‌اند به‌صورت مستقیم به این مادر کمک کنند، در واتساپ یا تلگرام به شماره زیر پیام بگذارند:
📲
+989101785282
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669105" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669104">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
عمان با دریافت عوارض عبور از کشتی‌ها در تنگه هرمز مخالفت کرد
🔹
عمان در نشست سازمان بین‌المللی دریانوردی (IMO) اعلام کرد حق عبور ترانزیتی از تنگه هرمز بر اساس قوانین بین‌المللی تضمین شده و این کشور از وضع عوارض برای کشتی‌های عبوری حمایت نمی‌کند. این موضع در شرایطی مطرح شده که ایران در پی تعیین هزینه برای عبور کشتی‌ها از این آبراه راهبردی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669104" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31dbfab06.mov?token=bIrwLdM2jJlgiv1nSnRFLtLnOxMXsuDDKwKg9rsKAYUd2XwBD9XdQCLTRQenWONIwfoskLhX68B9VwU6KMN8tgMl0B9sLkM0XwLBMmRkyj2_E73Ei2_r1W9rRJ-z4ce0ht2XsOy8h3kRwoZuSurhRnlHjDgn-ugnR5bnXCuZIRqsDd0wW7TO3SeVUObujv3nhBzmt26L5ivFMR9Rny09LYyBu9nj7Fctkgd8RtPMzF8WD9SODdC5hBhzQUVDE0QlhCOqM_Gaq6kmTufU2lIUz-B_8TzU0wjdE9At3epN-7ZQNsZAO1oTXdhDv_PIuduOTURJvIXcOuRfsjvgU88MCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31dbfab06.mov?token=bIrwLdM2jJlgiv1nSnRFLtLnOxMXsuDDKwKg9rsKAYUd2XwBD9XdQCLTRQenWONIwfoskLhX68B9VwU6KMN8tgMl0B9sLkM0XwLBMmRkyj2_E73Ei2_r1W9rRJ-z4ce0ht2XsOy8h3kRwoZuSurhRnlHjDgn-ugnR5bnXCuZIRqsDd0wW7TO3SeVUObujv3nhBzmt26L5ivFMR9Rny09LYyBu9nj7Fctkgd8RtPMzF8WD9SODdC5hBhzQUVDE0QlhCOqM_Gaq6kmTufU2lIUz-B_8TzU0wjdE9At3epN-7ZQNsZAO1oTXdhDv_PIuduOTURJvIXcOuRfsjvgU88MCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای «انتقام انتقام» مردم از کنار خودروی تشییع پیکر آقای شهید ایران در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669103" target="_blank">📅 17:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669102">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بدرقۀ آقای شهید از قاب آسمان #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669102" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669101">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJswMeftjPzRCRG5yTDLDUl59LGRsX1MHhHttYeFmReQR-w8rBI7pegvXviwPVYmIGloTyiqwBoUJwXRV3WpdCcU-uFcdVIUMF81hErOujbybM03QmxUVgZ19_uTaPwjfRcgrs7RDzNFsgS0jUbfe8dNYo2Osabw5aXzuk4601fbzCk9m7nEHtCkclmyLezTLjueq5pBnv8Wzx_J3rjAAL1IJ2-xcdv4nlhv74yeJo-uedvP7oE6AiP2H6RMhjw5rG-apTR7KxMtXMsKUYsweT-psjKRZs6Ed1gR3M6EfjTceBmBnCByhjn5roaJC71B8jrSa2ltkp8OYMH5mPPqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669101" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669100">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=vU7O-5-xaG-q8gGF0OJWlJapk6EAHiLvzaspi25o9xMeINfaLchLQMyUAIsq47pS4Cnv1HUpA8GYoULrRlnxtO78LksGvnZ8q1Xa-YvmdewHQ3vIxlpKIfEkvltAsUc9QhTBL98rzaL6pKEBM0F2v5UIYHTP-q_Zr4P6oHzdDsIoyFH9CrMPU795RXG_RGe6ZEeF57JX8SfahM7LMc2_MeEuLw9BxOY1rIHnT5aiuoYrVm6X8XHwvS8ksYEzzHq1igbXKrBYny-tRviFjkMnhIr-XFZ_tiRPZUHD_72yqwuz7oNWhoTJ3oocAZv02uDzdF0hj6mBM7FgWvmr-W0j4xngFMMmklETumFSZOnRx-7ufayhYoii_-3juMu3OyyJF-027yiZN9ASyihHI2C6ElIGcT9oGHkrv0kbunHzhWknH65u1DyWG0xyTDFBNCZOc61elQMpkvY7KnnSY5UkIfrqL3Ze65-w4KxMtw8WM-ZBlT5MjjWz9ojWls4hbm-6w3PMKkidZiv8up_FoQ3-iilyvXeiA2NP8uPj4Cox-ZjJHV4Ugv-WMZljsAwnjKrP_D8pmDp_XQOWsHPzYMjQ237luN7rW7zNYXIeAweLFjTei0h4TPMjd6pguo1tDq-A_e1iYCe6tOjB7O_3-HPjKDHTqqvGiwIfDeKx6UicgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=vU7O-5-xaG-q8gGF0OJWlJapk6EAHiLvzaspi25o9xMeINfaLchLQMyUAIsq47pS4Cnv1HUpA8GYoULrRlnxtO78LksGvnZ8q1Xa-YvmdewHQ3vIxlpKIfEkvltAsUc9QhTBL98rzaL6pKEBM0F2v5UIYHTP-q_Zr4P6oHzdDsIoyFH9CrMPU795RXG_RGe6ZEeF57JX8SfahM7LMc2_MeEuLw9BxOY1rIHnT5aiuoYrVm6X8XHwvS8ksYEzzHq1igbXKrBYny-tRviFjkMnhIr-XFZ_tiRPZUHD_72yqwuz7oNWhoTJ3oocAZv02uDzdF0hj6mBM7FgWvmr-W0j4xngFMMmklETumFSZOnRx-7ufayhYoii_-3juMu3OyyJF-027yiZN9ASyihHI2C6ElIGcT9oGHkrv0kbunHzhWknH65u1DyWG0xyTDFBNCZOc61elQMpkvY7KnnSY5UkIfrqL3Ze65-w4KxMtw8WM-ZBlT5MjjWz9ojWls4hbm-6w3PMKkidZiv8up_FoQ3-iilyvXeiA2NP8uPj4Cox-ZjJHV4Ugv-WMZljsAwnjKrP_D8pmDp_XQOWsHPzYMjQ237luN7rW7zNYXIeAweLFjTei0h4TPMjd6pguo1tDq-A_e1iYCe6tOjB7O_3-HPjKDHTqqvGiwIfDeKx6UicgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقۀ آقای شهید از قاب آسمان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669100" target="_blank">📅 16:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=heJsK2sh7mYg5fLHaO0xCoiyApPeEgzHwB0Zrbt1nMFr2iWHFMgq_P7U9To9wf2Kb8pUYaO2aOyulp3vDT_-ok7sCu8q4SXO2VoaluOTZTDZ0hCzTIQl-h9vi11RfaCYH3knHIUT7cj5sVwm3YM4H5YJTo6dpfwu8SCLWKs5Pg_V2IMp6AzWxFB6vL5VmyNrDnx1QOqpxqh_RK66NpEM41YgzrE8S66Io3mofXaZsVzAIgnZQpU7gNYv0TOztDp6A-huTIex-YaBU7TGV8s7G7CPVNz4Mf7fdK1C3lX8ZvqWhfMAyHX9YoL0iMEhNwQs5F88zqZDxGAUv3GxvCs1CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=heJsK2sh7mYg5fLHaO0xCoiyApPeEgzHwB0Zrbt1nMFr2iWHFMgq_P7U9To9wf2Kb8pUYaO2aOyulp3vDT_-ok7sCu8q4SXO2VoaluOTZTDZ0hCzTIQl-h9vi11RfaCYH3knHIUT7cj5sVwm3YM4H5YJTo6dpfwu8SCLWKs5Pg_V2IMp6AzWxFB6vL5VmyNrDnx1QOqpxqh_RK66NpEM41YgzrE8S66Io3mofXaZsVzAIgnZQpU7gNYv0TOztDp6A-huTIex-YaBU7TGV8s7G7CPVNz4Mf7fdK1C3lX8ZvqWhfMAyHX9YoL0iMEhNwQs5F88zqZDxGAUv3GxvCs1CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام هاشم‌زروندی: از تمام کشور موکب‌ها برای خدمت به زائران در مشهد مستقر شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669099" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dfc6e9330.mp4?token=m2bAu2oxAvOdLiR8p1AXMextCRT2MSIbiNpGj-IFc-yGX90V1NEtdLeBRJu1a3cPywgDa9CAkY7gUccsjJapSqHjqznDME5RrnQDdqzh8tPyYCb2l5ko0P4ikQk7-7qoRsn_wvSTiMoiEwS4Kw82JKT9RyfHnnMgp0m1OCMg3OJIb_SFqDAcPNkRpUaZVlAzorKcH28lvee1aRC7CCyJnHSlunFt4AAvyFMec2w767LA7Tnd0rH_gFBF8ccQMaYHR9QDmL3QWGiu49c85cJW2a9fpIoMyaMEq_AwqG2B5aSo07JwGblmkvqMK6E3-Bk--s-OJ_nTNpthN9lLC8yzQLLDmAa7MrvzCKCuCHSUE-wa7xDvtAnSisIshSpOdT2rtD0Wm61JqDGwhbXeBdBiLOwN5lDhKrUEH2yHYPWeMzHIHkeeiFTROhPcK4JsqJF-lQ_x05vgGbJQG0amdrQQLvnk_sjYi0hZlmnP6AJWW2nCLVEBYbZFCNFE3vz9pmYWFTw0auRiX_KOqk3zvvSOqS6hl4_4FFS_0OV4rmv_vRMdGbKq_v5MvVCn1ihBw5hl4I3IWqNWg2I1k-B2_LJWxrLWfM81oy1K3-OIydlozmHFEsn0PSEQqspK9YUwqkcGi5bHR1I6TRm9eEuGVQQwR-x2Plpx7VMCaFkM6DoOUPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dfc6e9330.mp4?token=m2bAu2oxAvOdLiR8p1AXMextCRT2MSIbiNpGj-IFc-yGX90V1NEtdLeBRJu1a3cPywgDa9CAkY7gUccsjJapSqHjqznDME5RrnQDdqzh8tPyYCb2l5ko0P4ikQk7-7qoRsn_wvSTiMoiEwS4Kw82JKT9RyfHnnMgp0m1OCMg3OJIb_SFqDAcPNkRpUaZVlAzorKcH28lvee1aRC7CCyJnHSlunFt4AAvyFMec2w767LA7Tnd0rH_gFBF8ccQMaYHR9QDmL3QWGiu49c85cJW2a9fpIoMyaMEq_AwqG2B5aSo07JwGblmkvqMK6E3-Bk--s-OJ_nTNpthN9lLC8yzQLLDmAa7MrvzCKCuCHSUE-wa7xDvtAnSisIshSpOdT2rtD0Wm61JqDGwhbXeBdBiLOwN5lDhKrUEH2yHYPWeMzHIHkeeiFTROhPcK4JsqJF-lQ_x05vgGbJQG0amdrQQLvnk_sjYi0hZlmnP6AJWW2nCLVEBYbZFCNFE3vz9pmYWFTw0auRiX_KOqk3zvvSOqS6hl4_4FFS_0OV4rmv_vRMdGbKq_v5MvVCn1ihBw5hl4I3IWqNWg2I1k-B2_LJWxrLWfM81oy1K3-OIydlozmHFEsn0PSEQqspK9YUwqkcGi5bHR1I6TRm9eEuGVQQwR-x2Plpx7VMCaFkM6DoOUPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایی برای سوزن انداختن نیست؛ روایت خبرنگار خبرفوری از خیابان امام‌رضا(ع) مشهد در مراسم باشکوه تشییع پیکر مطهر رهبر مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669098" target="_blank">📅 16:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=P73HDmjYyTx7AhTB0ksdjuW3zmfnjebGmsLPVHUaMnAdGzEqTHaXlQ90UmILY6-9rBipN5Ilgd6c6vd9Y4CDhodmvwgNfmuw6rv-g07AU5R6jfhAukERFquUTTqaN_GGavLQb-NvSuALAzUwJ5RKPyFLLBZ8csja0XJEZjQ04PoZ-6PeVZQjEkouVLkAvYk3vj9Z70qctsG2FYFqwNckpAPht00wtqjCvzX4d9K1av60ZXMCRV5LaVKFC5yJON6N4QTGsbJv10kvpa0fQzbJVNCUnPFDZo1DT0BrER7FsXK4T15yIycHLEEskeF_NZJw5FsLcaXvgVkxF2Bg7k5Xyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=P73HDmjYyTx7AhTB0ksdjuW3zmfnjebGmsLPVHUaMnAdGzEqTHaXlQ90UmILY6-9rBipN5Ilgd6c6vd9Y4CDhodmvwgNfmuw6rv-g07AU5R6jfhAukERFquUTTqaN_GGavLQb-NvSuALAzUwJ5RKPyFLLBZ8csja0XJEZjQ04PoZ-6PeVZQjEkouVLkAvYk3vj9Z70qctsG2FYFqwNckpAPht00wtqjCvzX4d9K1av60ZXMCRV5LaVKFC5yJON6N4QTGsbJv10kvpa0fQzbJVNCUnPFDZo1DT0BrER7FsXK4T15yIycHLEEskeF_NZJw5FsLcaXvgVkxF2Bg7k5Xyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب در آغوش ملت عزادار ایران، وارد میدان ۱۵ خرداد مشهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669097" target="_blank">📅 16:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZSkD0MRq3rNX-n_E6sMjgtesbmYyhPVvGH94OZuqDlnBmlKcRgENEPnsrUSZrHZTxvjV0UyksCLr66-KpIuwTPGYm_dDvPhTXFQTJnyV5WCCRWufv_L4g16EQ-1o1VeebJ_d_X2oW5wSZZGQ9GjfTWmOfX9jJRg8wswKrWToBAmgl3vo5N68-SJTqfsMyp8URoL_07VJgFftNqqiK9XuOg-AU-mc8OxZCUEBu3kk8_mTnk-XeJbZLVM8P_aOkYCLFapDKLAFR8blWhmFGXgSY2YnQKHp5RmEDz0d60G3Y2KGY-D6MyaeMPzTA0ZW7PGa_AXV62DLxvK3jXG5Kl6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مسئولان عزیز! چیزی که باید از ترامپ بگیرید امتیاز نیست، جانش است»؛
تصویری از پلاکارد یکی از شرکت‌کنندگان در مراسم تشییع رهبر شهید
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669096" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=K2JGOiU7MMZQjeyHHc3o0H-5COVel5LHoLN0k3Rw4jtAPD2Ei-pvF1ibNlr9-doXDgvX44YLBFnYFBaGI6pe2hIxz4PQSKie058axC9x0Jnak6acaarH0JSkmwkRQubcdqOdA7F83zFdmUHTRkKWzWVRlhW0PoIvPq3jWZnWdw18nXd1N4E4l2B4X2AhuCqHrnjIZpGFURsXAERmGg9J8IzAjdpXhrpR5qNA5oaZ_9b0AVs4eW9N-OW0T_d7bOW9bCjCfV_nDVxUd9BzKj53TjlzDpz4cV2OPWZc7tvGjm9FRicPuE4dqTgmZLUWm2iEjQPI78agW6jEeRTC-5T6YjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=K2JGOiU7MMZQjeyHHc3o0H-5COVel5LHoLN0k3Rw4jtAPD2Ei-pvF1ibNlr9-doXDgvX44YLBFnYFBaGI6pe2hIxz4PQSKie058axC9x0Jnak6acaarH0JSkmwkRQubcdqOdA7F83zFdmUHTRkKWzWVRlhW0PoIvPq3jWZnWdw18nXd1N4E4l2B4X2AhuCqHrnjIZpGFURsXAERmGg9J8IzAjdpXhrpR5qNA5oaZ_9b0AVs4eW9N-OW0T_d7bOW9bCjCfV_nDVxUd9BzKj53TjlzDpz4cV2OPWZc7tvGjm9FRicPuE4dqTgmZLUWm2iEjQPI78agW6jEeRTC-5T6YjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کثیری، کارشناس برنامه پرچمدار: اگر پیکر رهبر شهید در سایر کشورهای همسایه مثل ترکیه و پاکستان یا هند هم تشییع می‌شد، آن‌جا هم شاهد جمعیت عظیمی ‌بودیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669095" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pri1E1zpdk41_QWKNlvgQGNc3603qQy3Banz_GNeU2KVh-5Mm61P10bq8O3FFvVZwuvwjU9prJok2uce9NdSHZNJhyJe7Sx2Dy8k6v7I-tAhviBLSTFzg9iFaDtKa2O74-91qhawbqV80HvmZaP80Rb6m1IxxrnZGsvlx8tLJT5jpKMSWXI-gnu4uH78v5i0eOMHPJo9MVNoQfGtSXQqvfiWugQQzS_zBzJOg3F-CIKWcP5-TJMv-AQEII8LmucIVnSfXhgBTlgi1I2PWPuItfe-TsgCHs17qbUcsi1_wvRw_2BONYcF5cs_SU8DK1zgVnNa8J0zNuNexiob7Da-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خیل عظیم عاشقان رهبر شهید در کنار خودروی حامل شهدا
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669094" target="_blank">📅 16:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb44dcb20.mp4?token=kYUi00THqmATZLPKWjnVECqrPmDq_6-_5GBZd2byMqT9-sA24MBlpYq4kTo7XsuuLtXWP9oSiTI9yi9ftHXIkwwkSk3HToyofn02RcazwK4uWB-zGPaF6BuMlGCOXgUe24lQ6P5gc2Hajw2Dhnt9DW67O9-sG_u0L2Cs8Rgl3CdB3Es4RqhDYdTwI3n2mK8X-PV0ECXwM-upnB4f4hlWcvc2Khn4hreqlfk34mknD_zzN7JxgVmLsPHf2SjXsOyxRwt0dC4QqUfSeZFO11kqoH_i6JaDJTxs4S0k6YTNv0n2z3JyabmIWHzim77qINtFlKGX4iVzY1rAoaHyk7-B8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb44dcb20.mp4?token=kYUi00THqmATZLPKWjnVECqrPmDq_6-_5GBZd2byMqT9-sA24MBlpYq4kTo7XsuuLtXWP9oSiTI9yi9ftHXIkwwkSk3HToyofn02RcazwK4uWB-zGPaF6BuMlGCOXgUe24lQ6P5gc2Hajw2Dhnt9DW67O9-sG_u0L2Cs8Rgl3CdB3Es4RqhDYdTwI3n2mK8X-PV0ECXwM-upnB4f4hlWcvc2Khn4hreqlfk34mknD_zzN7JxgVmLsPHf2SjXsOyxRwt0dC4QqUfSeZFO11kqoH_i6JaDJTxs4S0k6YTNv0n2z3JyabmIWHzim77qINtFlKGX4iVzY1rAoaHyk7-B8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرگزاری ریانووستی روسیه از تشییع رهبر شهید در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669093" target="_blank">📅 16:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6mWqAYtETjZQ5Zk8YU839XAcmojWLUgg5-bwMWB7kdWDZbEBGYzthUtWfT_uxF0cMJVBiA0H-D675iL3Bkmp57kRprUCn5k6b5Hh4FyhPN8-O9dMYbQpLsmIoZLBszxw_vikG5Uf-DLeJmXhilQMAQbGt62kYGifl5WrQkAWI4pCRTQGK1I0Ckch51UYYu8_e_Rl3duRP6t1zL4qC1t_OkMY2FB2-xPzQKsuEUAmmQwFiAGQPRrFjc_r7Vj3orrvVXiRLe_u_7gyJwSMoh09qCaygrirrc9dl_iInbcn3cIXfIWxdA48qGRYZDIN4RZCfKh59iYNZD9iswkSSU0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر آیت‌الله سید حسن خمینی به مشهد مقدس برای شرکت در مراسم تشییع و تدفین رهبر شهید
🔹
به گزارش خبرنگار جماران، یادگار امام آیت الله سید حسن خمینی برای شرکت در مراسم تشییع و تدفین رهبر شهید حضرت آیت‌الله العظمی خامنه‌ای، وارد مشهد مقدس شد. / جماران
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669092" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669087">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlQvzBGKWFi74XH0EpnUWljuRWR12fd99pMOZjaHC0wtpzQ3gXIiLQZdt7uks_040dVIqOXHCQk25l7DlAAJUGGmhxkvqQl-_JGWvLIZ7UZu8Gl8X-2q2FVIoy5wrtoXB7MLZDQjhK65iUpKwDCoQADbbdju-xoxKjbeToYVB0PlmGD-34clpohG5oZaRlW5aXVzDi_KAaGGxZnJxtSvg54G2QKyntK2UjY6GeTdL3u2H56Rf5IzRbQv7ZveCKPXCsA6AExSuEO7d-r4RO6bUpez3BeQ_2_FclcbzQB4F6OJOrcG8ccASekRJ5zwtklUW34JLYT34nG7L1FjizLWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3u1BkpvYIWh3oXNwNmiuBNmaSTiWLoXRyVuj-nFpvlDaBUEEl9U2oHs8nNwGCB0hwSXKtZWs0aoVuDr1NEEK-LUGLi4Eo_l7powtnaGMsLJMGlcQl1XTruOiqGkaWMpsF8Dy1TDQCWhK3_YmAUoylpxIoWSXC_p6zle-Cy7Jg8Ris6MJLJWbr2EzH9o57vsunORs_qmtHcY3JNaGBePw7rcIkWxXr9k-TIFg1slF7kqXTNGM4C6-GbgZyVKFhOHza6nUn9SWunHFULiZupSb2uUR3Fg4NgPYEBT6Jnu5M-5eTrALW5Kpzp1mP--XmZcjy25GpOiBRyIKCHLQZvjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcuwBkrrBCtW--GhYFZQK7hGkU041oDUuufB-iASp9Irsg-s_JW8FH1GvWiF55ai6dySjORMMjSto1B_L80XzeQTCS5Dell6klEte39Sx-e8oQb6Ib5voHlEry8Zvxph52QCNhd-lZjnJ9z_e7SaWlwVwhWO3IJZCl_GEqv3WpFeac8WRSJs0bv9luSnTNifPTkC6DUaSoZMyLbSK7yigFw5zTYcRqqGSDycZAztYyY4WQpfZlhvPJ0PtNotqSOfI8OgFrRBSs0jUjzB7VQfe7W7eFOxzOogOYi-RDt-xz1oyHgcFSakcq6h6fuUdaWqIlw-G1mUdMQn3VJMUgiiTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4806ae948e.mp4?token=Kfp6q3pekJQxNJq6BB4uTwVMyOk7bTUUMfEMjkQJgjA3tqvQUCfrCLckovY29NH-c_wegu8adBnPI1oGGQgG6lqqrPKn1kSd8EAs8DXdRpqRy9lZmbAiJBM-XkMEAoRd0H_hnsJUXADEar1ILDkdjb4tGIKIC1NkHFNl0aD_1HFrC1i7kZJB71dD1P4EskoJQSS9sCmTaOU4BFmcQhghhNx0No3FINWSQ5yeyY-FfFHGQt9iWC8Z6vv1xnLR2yi4D4IMA6EbuGCGhG1qMIxEcAvXNmJUuMNTNE97TBMVF8bo5ANLuR-alWYPBXGDlS4EPPgtZwEj2mXe94r3t5ZUa2HfOFDumUJWfoQ_WeA26MDU7DQzGxWiT_8vjBACmrGp-BWrQBSuxBB8WrFkB1gcRkbXed2YxRdx5EBF-v4vaL-TQRcwDVX94a-CI9jZnWi4nQBvINsjIElSeag0A0coHSh7dMecpYXwkBaYYL6sHdo3yNoaygktMcSdIqrSKsf2aVLFwmGzKb2hVFY8bVDYhU_QgfVX1kIJ5868DAQvWorRiidi4sUBlUKd-WbRi_qmoVY6VcXgaY0P5dknDbJOxKiXjA0Ux8i_5ZaHK-LhkVA7Ycwa0luqqPfOSgWa9E0i36CZ1mWJpO1atIKuvnUpJa1oFrNjT3-HF2UN9qgCe6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4806ae948e.mp4?token=Kfp6q3pekJQxNJq6BB4uTwVMyOk7bTUUMfEMjkQJgjA3tqvQUCfrCLckovY29NH-c_wegu8adBnPI1oGGQgG6lqqrPKn1kSd8EAs8DXdRpqRy9lZmbAiJBM-XkMEAoRd0H_hnsJUXADEar1ILDkdjb4tGIKIC1NkHFNl0aD_1HFrC1i7kZJB71dD1P4EskoJQSS9sCmTaOU4BFmcQhghhNx0No3FINWSQ5yeyY-FfFHGQt9iWC8Z6vv1xnLR2yi4D4IMA6EbuGCGhG1qMIxEcAvXNmJUuMNTNE97TBMVF8bo5ANLuR-alWYPBXGDlS4EPPgtZwEj2mXe94r3t5ZUa2HfOFDumUJWfoQ_WeA26MDU7DQzGxWiT_8vjBACmrGp-BWrQBSuxBB8WrFkB1gcRkbXed2YxRdx5EBF-v4vaL-TQRcwDVX94a-CI9jZnWi4nQBvINsjIElSeag0A0coHSh7dMecpYXwkBaYYL6sHdo3yNoaygktMcSdIqrSKsf2aVLFwmGzKb2hVFY8bVDYhU_QgfVX1kIJ5868DAQvWorRiidi4sUBlUKd-WbRi_qmoVY6VcXgaY0P5dknDbJOxKiXjA0Ux8i_5ZaHK-LhkVA7Ycwa0luqqPfOSgWa9E0i36CZ1mWJpO1atIKuvnUpJa1oFrNjT3-HF2UN9qgCe6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماهای نزدیک خبرفوری از خودروی حامل پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669087" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669086">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سپاه: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد
🔹
سپاه پاسداران انقلاب اسلامی با صدور بیانیه ای ضمن اعلام در هم کوبیده شدن مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک هشدار داد: در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا در منطقه از آتش سنگین ما در امان نخواهد بود.
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔹
در بیانیه قبل گفته بودیم تکرار تجاوز پاسخ ما را به سایر پایگاه‌های دشمن در منطقه توسعه خواهد داد و در مرحله دوم از پاسخ به تجاوزات ارتش کودک‌کش آمریکا این تهدید را عملی کردیم.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک در هم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا در منطقه از آتش سنگین ما در امان نخواهد بود.
وما النصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669086" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669085">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpmgDxfvQyom8dbjgX8qW0URp4BGw4SKTuPx5BiTEcrc3RMNiqAjjCkod0xl7-hquz4IVOQfPcwzRYyFQlUg7tSP__8AQIoXoxcJ4nfECNSR0SAXyY7vr0ANgZAPsyOhaTahc1mq579Ru1pDZEgSGjKtcIavvcCMlqGtG3Mv9kKnZNomr82nLPX2XqmtMxzSwCooSfbSX3brbKS7VQlqcDMhJ49pmHD1a5RzxLAJGLzmempaUZXBX0QOP8ob9lgQa81qBBhcoRAKbYfS9LmY8GwHj5yceJlS35pSDfXd6MRbW3zJHRmXFQpFnLZW8snPlulSmrCnAoKhZNsRWqPTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لارنس نورمن خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آن بازگردیم
🔹
بیش از هر چیز، تمایل به عدم تشدید تنش وجود دارد و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو خواهان آن هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669085" target="_blank">📅 16:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
خبرگزاری رسمی عراق: مراسم تشییع پیکر شهید آیت‌الله العظمی سید علی خامنه‌ای در کربلا پایان یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669084" target="_blank">📅 16:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669075">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hujm9r-FyMvheuAoMQCOG9juINzSA6vNMSlnjAklvJ6iNL7Pj8CNYo66F7Z-ulYdMPOyk2nw4yIpNSqjWgq9uThZE2bLeK5SbltEYUM4GaY4jQ6iP8odS90rfZCQ3jDuKQFWWpXV0a5bvmifd-rtEOS9d_vE09-qjsvMdWeI47EURxid4G1_atgGYq1UH5I96-boFci0KDp3CmJQNycPzCEtTRg9G9xsojx0rd6qisPlOgOGIQri2nfnai-lqsiiEG9HdpupjHxIo1fC35Ecf2rSxSqiPAojafRSJKXFDVmNbMp1SlVANpkRW09y0TjAy_DPZG0RDW-sFkAEuxLUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDNBA4HayU-OskuB1NY8309V-SgXLeh--v2dP4jGZEP07I89FBW4XuXU4qAl1_5ov06LzywqzaL9EO4TI0FFAg0hfsA6YbGu42nNgUTICOCAcOJfB6qKpRaIFqsJYo1ZMEQlY4M5uHs7NZXdhaNNY9HHJ1JRVDXI5NZvIkUMJMtWzMNfrRgyVzRlHCj8ujYkqMY0HQD3fV5trCDABCqF8E0GR0I42KnU2r3mL-dI3-WfoZToT_bT0WFG_IbXaW00NXLnZbZ_xZBO5VoCIxiU7TI9EiyR3A0zYuxGGZ-l4ckSmKYL4RdPJv226umWj8HPxHoCV96XTqA1aMm_Qo9E_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4zhL1rypJMON7HJcDn2JtLTMqRZf8GMwwDqpOn7D7heb4uwkqVHvfbBE9Qc7c_iNS2jyfdeFzAGNrDnTt_0wPeaEeZundP6mZh0bkJTmVjfeoroTTV0HZljpWLRnsLyUpy3jO6fYLKv7BhDUkm4LmwEKs5y87-XRVvzbeihChqcilVWavP-DSBOwXlTV5y-oTT0tEclTIy77BIQZaGQGapKdshRUQU9eFSD_T_wfPMHE54SB-TEdhwC1X4pI2j1ZFu5jYsvsdpBkg1n-e4usF_o-6yfRWZmLeQTvvPvc3OEIf_PjFDNAQOrqs3oDyni8-Ve4a36toQOQ1kVC1aCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xyo4Q3ZECY1MG9nVNV4X3DJziRo83xFc3cARbyLaZoFzvkL7wmtUwYGP7QYgeGuYbmKqM-dY69jNM1NQtfUDyH8SRDiO4aaZoPQV13mKBpPro-ISRSPYjWKWLy6d7H4EIxXs6VQlIWIXD1pSjyrwckmkss7L_IWLct68SkwvTYvy67EyYJ-eM7NITsLRoPEQFj7esX3c5B-rVHqjpopxQOvGTduFcdFqRtDg8uS6CJBwZg5DueAYeBbjx72U2z355-jiJ9msSMGWuCrrBHZw7GZzTO6lghm_-BvEMOdgiUQG_FltcQeLTmOTQWFWiDyZzWugiymFbUe0P24OUGV-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyAWkbh2fp2OJIKYcBTtKs_Ny4OJf3nzwsWrfHRCodFYdH29YfZfqz-nYmpLEDChn_L1NL7gO2y3n1RphQZt-0Y6pmrNtMu_auEYiAHoBP-71BG0fCFlFFKroVLLcCVABfXuc59CuDbSK1gxWbqQ1a6K2LR6dre8sJlP93ldsZAD4hANT-2aD-051E7RdgUWXSgwY0WLG-2mH-DtT-w3RCjHgItIGpePKVT7eQs_S9PJcySML2hGOm8Qt6-aRIs0Abd8n9-XxB6PxBOujNiQZUFUg5l6D7lCAgXfDPnwij68Nk0D9xQZnFoRG2UI4mYP69juayz6W4L5ES_kvJcuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAImy4UrTk3Ain4hj0tnU1qHiqelG7O_roZ_Qge506fBqU6E1P8bnjaGe9SRMNMZbLGvoPqjkafudmYhI1kQer83UHwb7_5ZimwtOy_kj00MIO0x4S-qRr4XqiRZGI4mDKwK1HpQDOR844gYTVH4OtJ5zeoKUNsnq2MozNc9uOlm6fGUEfGoTDUKq5VfwSQqcNubAbT0aT_dwaCmcWWgreLCKB8wcIa2RzVVACCFyKvTzGlhTUux0LT8434YOpZToEd52jKl5080EkSlCTq8oIAzn8YERTnTgbyI1444ozuDDulGMjTSACkA9XTKhJaxgzxLfXIbm6os6zPXO7UVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5Yvaoshe_-Ow8b8Hst1cVcV6iQH1d9jcjq64OQpzpLj8iFciu556iu4myLYiRUB97KQ2rq71Tv5qUmJfLCuFY2XXuLzfxT7QBx7Tem44wXTfuUOW2myufkhtdxsPedHIYW1CSUZYu6RY_ycnpKQ3UAc7Hlo_KdT_0LQhMYkhs07hzI5080i4FL2r5anzluRyOm65JF3IAlspirdXwJWDffBRUjUc9MFHJRgHt8uYrNIH1tZ4aEdHS9HgKq-e5-VwbUA2VcNXYliHnstBrtW7_N5qlR6w7k3Jhq-1yVlJrO3GSPOon5tovoCxoVdcOWcJBXvdI-e9Zfw_g4mtpWt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIg4K72XR_T91YVAgFvFFhAws6fxIhD9x86T2Q1aYr7e1fiG85xWJ4kWxBr0eL9Y7XC_-BiTkVxewZx33uoRr6Q3-QsM0fiPAlQ2Cdkfck4H6hPZkiKbtQvWNo2Px-bd_fi-poFo9GSWzJbbClSZxeXfWyZBaWOApOiySXhtUB1tBiWDMx31lX4qN3O8TrTjsr7B8ao6fXH42gh30aezPj1AHmIb8rQ2kUNwbxVe8VS2UGoHxAnaKWonmUkzSmwLOwBbnIcVIrvjPjTVVHNiKAXh_9YTm-gbr_HZ_0zggm50C6OQ7CkWnMkyIm-R7ABPkm4fspp_HYskrTnJ-Rnu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-fCDUwreWgjrAZuYVSuxi6VoKGRdD8BZ-B6GRnZbG7eR0E58akR_lKRmTbD-X07c72hvV4Ba02JsG2LuNJJhnga38xe_A_6hYuKbxNQdtL75C_r17JFgQxc-3TPblvkp6ZVd7VDB6_2lRJ4DDfeT2REP2iRjeyiIeun84Lz3EC_01wN2hdtwd5dlQuh0yTwdu3AjyKB5t3HlmzmOr607NpSoUg7kgbefYKJ0VgpLstCRXcj5ayOY0lBcBLyMCc_z1-Le08kCtCpzfwN0CSbeu44dtw630BgJj9WSbzbU-lyl0Tsmf0NDf78882zw9TIyqOrF2AW_uB6wjcD7N9Vdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
حضور مردم با مچ‌بندهای سرخ در مراسم تشییع رهبر شهید؛ تصویری از پاسداشت راه شهیدان، ایستادگی و خونخواهی رهبر شهید است.
🔹
شما هم بخشی از این روایت باشید...
🔸
تصاویر خود از حضور با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669075" target="_blank">📅 16:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb4108a03.mp4?token=IB0FTjkVRJ5Bp3rzgLz4mxj4h-U0LTDuhWocVa8VKAzAebbhsUINkK8HaZ1zkZgKhgpXD9bttfWNHEqJvQfQeVUReeGl-zLwIpHhB1Cn_dFwqk548epnXns8iAseWvDQGjp1XG3Od-P14dPu0__wlBM6N4dq4rLsX31ZPVVnnMQz61ZB6EDM0Ubk_sotfJzwtQaH1AdM6zQMkpRKcIl1vNKqgO7_gIYOvhX3g5i5MpwORJe4Wu10S17ajNnhvE3cUUL1Ed86lDE_CPi315frLWZlR5UoGPYWdjV2OT0wJZD5t5v9Qu58uuDsC290fc0_ZARr5KMwurXnbm7QhbIHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb4108a03.mp4?token=IB0FTjkVRJ5Bp3rzgLz4mxj4h-U0LTDuhWocVa8VKAzAebbhsUINkK8HaZ1zkZgKhgpXD9bttfWNHEqJvQfQeVUReeGl-zLwIpHhB1Cn_dFwqk548epnXns8iAseWvDQGjp1XG3Od-P14dPu0__wlBM6N4dq4rLsX31ZPVVnnMQz61ZB6EDM0Ubk_sotfJzwtQaH1AdM6zQMkpRKcIl1vNKqgO7_gIYOvhX3g5i5MpwORJe4Wu10S17ajNnhvE3cUUL1Ed86lDE_CPi315frLWZlR5UoGPYWdjV2OT0wJZD5t5v9Qu58uuDsC290fc0_ZARr5KMwurXnbm7QhbIHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش جمعیت در مشهد برای وداع با رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669074" target="_blank">📅 16:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
در پی حمله اخیر به نفتکش‌ها در تنگه هرمز و افزایش تنش‌های منطقه‌ای، دولت قطر اعلام کرد که برنامه‌های خود برای افزایش ظرفیت تولید گاز طبیعی مایع (LNG) را تا اطلاع ثانوی به حالت تعلیق درآورده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669073" target="_blank">📅 16:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669072">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تصاویر ماندگار از تشییع پیکر مطهر رهبر آزادگان جهان در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669072" target="_blank">📅 16:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669071">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c3bb1ce8.mp4?token=MR3EcmBvLWbs3x0-TIx_qkt9-ckN182OF_iPaz13r8Izkqi7L4wWFPPYbevWoBEOeH0rCIZ58bjEchd2nVavajnVew00Yk45poMd9C8z26SoKDKSTvKDZZsId4XP7rQWeP2yQ_XhLieyUz0qj_CjQUsSLo88zTyYieq3ZS8PkvvTW3GfktjNEJCvEVJNyeZO_Y-zTiDH14cVjXhnDuhXSoQ4E7FZtNrlDMm_VDM__2hFT-ppva9Jb5E695ZiUOJk0rg92wl2ITUbTayPPnaFQ_c5RJTShhFHm2G2S22AX0b033LEzeIEabcizDjG8ezCq55cjRwOaMZqhwd5gDmWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c3bb1ce8.mp4?token=MR3EcmBvLWbs3x0-TIx_qkt9-ckN182OF_iPaz13r8Izkqi7L4wWFPPYbevWoBEOeH0rCIZ58bjEchd2nVavajnVew00Yk45poMd9C8z26SoKDKSTvKDZZsId4XP7rQWeP2yQ_XhLieyUz0qj_CjQUsSLo88zTyYieq3ZS8PkvvTW3GfktjNEJCvEVJNyeZO_Y-zTiDH14cVjXhnDuhXSoQ4E7FZtNrlDMm_VDM__2hFT-ppva9Jb5E695ZiUOJk0rg92wl2ITUbTayPPnaFQ_c5RJTShhFHm2G2S22AX0b033LEzeIEabcizDjG8ezCq55cjRwOaMZqhwd5gDmWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات موشکی بامداد امروز سپاه به زیرساخت‌ها و تأسیسات مهم پایگاه‌های آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669071" target="_blank">📅 16:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669070">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0b685053.mp4?token=g4lnz8Odc7mGZLfJwRamsOMkiy57yX2YgMCN__jBIowcRCfZHxqN4xDArDcsMSrWB115mUqDAfy2TiLzJxZh7tqKvjK1pyNS7Ds1P44Ae8aJmc_MlzdvNRzlZ9XeLUTCv8Ct9bqsfuWiNBJzWKp4O4BEXkmQVe8K3PN04YtNTi9H_h_QFq9GLZ5QWwLOzsIxcTFO5XGDFdh086nLSABkD7kmhurq29vZ1xxdwbjr0uLT8tqoyASY02Jsn9Qlw10BL2U26HRrdRKRnSeaSKqzWuJNHpU4GYWOSR3TyDEDmXlCMy2lJv9-DFdXCuGGFBs47RovTgLYjKgOSGTKvYGpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0b685053.mp4?token=g4lnz8Odc7mGZLfJwRamsOMkiy57yX2YgMCN__jBIowcRCfZHxqN4xDArDcsMSrWB115mUqDAfy2TiLzJxZh7tqKvjK1pyNS7Ds1P44Ae8aJmc_MlzdvNRzlZ9XeLUTCv8Ct9bqsfuWiNBJzWKp4O4BEXkmQVe8K3PN04YtNTi9H_h_QFq9GLZ5QWwLOzsIxcTFO5XGDFdh086nLSABkD7kmhurq29vZ1xxdwbjr0uLT8tqoyASY02Jsn9Qlw10BL2U26HRrdRKRnSeaSKqzWuJNHpU4GYWOSR3TyDEDmXlCMy2lJv9-DFdXCuGGFBs47RovTgLYjKgOSGTKvYGpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز جنگنده‌های خودی بر فراز آسمان مشهد
🔹
صدای پرواز هواپیماهای نظامی در شهر مشهد شنیده می‌شود؛ این پروازها جهت تأمین امنیت مراسم تشییع پیکر رهبر شهید و پوشش هوایی محدوده حرم رضوی انجام شده و جزئیات رسمی آن هنوز اعلام نشده است./ مهر #بدرقه_یار  #اخبار_مشهد…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669070" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669069">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
منابع پاکستانی: میانجیگران روز پنجشنبه، برای جلوگیری از حملات بیشتر، تماس‌های جدیدی با آمریکا و ایران برقرار کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669069" target="_blank">📅 16:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aza_7XMkeG4mIRUwpDnljEObygINI7S__T6T7EFl33Axe4XQTPUJIhHgb_PcnjtQ_PhiCb-uXvY6rkGXXTTGituCAXxiagBxOe7O3WYr2gW0n-cDITFDQa2zz_Ccdhfdfb2hYRWo1GqYiTa463rndW_CmYimE_71uqIyt5BYXPsD6BusYsixHNNujoGNDwG3prmWreNBMLJ8qfW9bU9rmtcUHSeLTRBf8Ekjzmp-3m_b1LVycuBQd8a4IfQJ8rgR16LbW7waX6d5elbkba2GbsddhdTIgZ4Vh0sRYBYY8EvjxJu9aU8PU6ZB9_2zOpzL5l15C3xvQgdmTBiIH2bxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/669068" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تکذیب شایعه حمله هوایی به کرمانشاه
🔹
منابع آگاه با رد شایعات منتشرشده در فضای مجازی، اعلام کردند هیچ‌گونه حمله هوایی، انفجار یا حادثه امنیتی در استان کرمانشاه رخ نداده و امنیت در سراسر استان برقرار است./ مهر
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669067" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
