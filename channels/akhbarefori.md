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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-667004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/644005e68b.mp4?token=SMwZT2O7NEN547FrykfDFr_3lqxu-P_1avQFB6B0-yq9zSeCS6_SmGZsiU3QXcXE4MaoM-b_JdpBDO0b8tXo1VA7TF11BFRbfv5PQrp1Rbc-cjwbtqhkGG-awPRc0TYAwd5xclbPkDsf_d_uHqou6ZicvViRN1NZ--S9RVZ6_gFn4EnWvZX0VbjCGA8esxOc3RrpFk0peHPILuch7O2vLJK9KYZS3E9NIUkpNSm6YgmaxFxkJW01wwdJDx0_jrGnXIyuMduYIiqcrz_IBPay-t4qsPiGCCXx4o7ADwJUb7HOryA8qXByKauMzYIAtw7GRi1xr9w2m6rXUOxF6DiyzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/644005e68b.mp4?token=SMwZT2O7NEN547FrykfDFr_3lqxu-P_1avQFB6B0-yq9zSeCS6_SmGZsiU3QXcXE4MaoM-b_JdpBDO0b8tXo1VA7TF11BFRbfv5PQrp1Rbc-cjwbtqhkGG-awPRc0TYAwd5xclbPkDsf_d_uHqou6ZicvViRN1NZ--S9RVZ6_gFn4EnWvZX0VbjCGA8esxOc3RrpFk0peHPILuch7O2vLJK9KYZS3E9NIUkpNSm6YgmaxFxkJW01wwdJDx0_jrGnXIyuMduYIiqcrz_IBPay-t4qsPiGCCXx4o7ADwJUb7HOryA8qXByKauMzYIAtw7GRi1xr9w2m6rXUOxF6DiyzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد‌های هیهات منا الذله عزاداران رهبر شهید انقلاب در مصلای امام خمینی(ره) تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/667004" target="_blank">📅 17:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف: خونخواهی امام شهید، آزادی قدس است
🔹
رئیس مجلس در دیدار با رئیس شورای رهبری حماس تأکید کرد دیپلماسی باید با تکیه بر توان دفاعی، دستاوردهای میدان را حفظ کند؛ وی با رد به رسمیت شناختن اسرائیل، تصریح کرد که حمایت از جبهه مقاومت ادامه دارد.
🔹
درویش نیز تفاهمنامه ایران و آمریکا را پیروزی بزرگ مقاومت دانست.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/667003" target="_blank">📅 17:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قم(Admin)</strong></div>
<div class="tg-text">♦️
۷ موکب، ۲۰ هیأت و اسکان ۶ هزار زائر؛ ورزش قم، پای کار خدمت‌رسانی
حسن سلطانی، مدیرکل ورزش و جوانان استان قم در گفت‌وگو با
#اخبار_قم
:
🔹
جامعه ورزش استان قم بزرگ‌ترین عملیات خدمت‌رسانی خود را در مراسم تشییع رهبر شهید آغاز کرده است. در قالب این عملیات، ۷ موکب و ایستگاه صلواتی با مشارکت ۲۰ هیأت ورزشی برپا شده است؛ به‌گونه‌ای که ۳ موکب در مبادی ورودی شهر مسئولیت استقبال، راهنمایی و بدرقه زائران را بر عهده دارند و ۴ موکب دیگر در نقاط مختلف قم، خدماتی از جمله توزیع آب، یخ، شربت، تغذیه گرم و سرد، خنک‌سازی محیط، اسکان و سایر خدمات رفاهی را به زائران ارائه می‌کنند.
🔹
همچنین اسکان بیش از ۶ هزار زائر در روزهای دوشنبه و سه‌شنبه پیش‌بینی شده است. تمامی سالن‌های ورزشی و خانه‌های تخصصی ورزش پس از بازدیدهای میدانی، تجهیز و آماده‌سازی شده‌اند تا خدمات اسکان با بهترین کیفیت به زائران ارائه شود.
🔹
در موکب‌ها و مراکز اسکان نیز ۲۵ پزشکیار مستقر شده‌اند و نیروهای تخصصی پزشکی ورزشی به‌صورت مستمر در محل‌های خدمت‌رسانی حضور دارند تا در صورت نیاز، خدمات اولیه درمانی و امدادی را در کوتاه‌ترین زمان ممکن ارائه کنند.
@akhbareghom</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/667002" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
🔹
مسیر تشییع شامل خیابان دماوند، میدان امام حسین(ع)، خیابان انقلاب، میدان انقلاب، خیابان آزادی، میدان آزادی و بزرگراه لشکری است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/667001" target="_blank">📅 17:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b00af8d5.mp4?token=CKYuLs4yBDFVEKz6Q4VnAJUbp2BdRVEFW8a3Tp-5yH9d_PZnzXPs6SDS1-cbUPb7bjOoMG7PblHogp4FuKFee8Sofl7MHcVXzRAhFmGMFPrbbyLv1DPKmogdJryzhNKPq5uciglT2ZQZ5qsOHIL08EnpCa3AiAntVYO7q8Bm_jKcU_p-4QabdREk-ooo2RoUZHRFqX5FyDQwtUHDCy00-tk6lyNG4LsTwlEygoFgZIeOMKIJ8X1EGUALJYVBkrSUjkpst_9jiVIaNfdro_IYsdlYsJtqllveiMaACA_5eQ-4MFHELwDYGmmIkBqvIHdSClZ7lICAmxu8ARaRyHaupXsoQbjSI1QfEA0AuL65rcPqGnvbf5SYQMGE_1RYK4mePAqTitiKtrYhi7ueZmaQVCXQCoJUBclMkIaHN0IFASktF95GL-Ihk3_JCtN8-IJ4EqJPw3eSwPGnKx4vXiyYu3dcjIDczksTpEkXrUM7m-IeUTYYBCyQmLQPltdYkserGMHVvaGi4w4AlatdtZaKSeqTIxGBhRTOEf_L3eFskiu7_bHGNzoy8ozqLKWPBS6jcoLbjBImGa08Rdz14l1anrMn2ZhMPhONHwp4n1hNruXkn8wZAUKAN8K09BANX_63YLPKZVQoXxL3uIgiarwkqCvCl-UXpynxrMqkioWFNVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b00af8d5.mp4?token=CKYuLs4yBDFVEKz6Q4VnAJUbp2BdRVEFW8a3Tp-5yH9d_PZnzXPs6SDS1-cbUPb7bjOoMG7PblHogp4FuKFee8Sofl7MHcVXzRAhFmGMFPrbbyLv1DPKmogdJryzhNKPq5uciglT2ZQZ5qsOHIL08EnpCa3AiAntVYO7q8Bm_jKcU_p-4QabdREk-ooo2RoUZHRFqX5FyDQwtUHDCy00-tk6lyNG4LsTwlEygoFgZIeOMKIJ8X1EGUALJYVBkrSUjkpst_9jiVIaNfdro_IYsdlYsJtqllveiMaACA_5eQ-4MFHELwDYGmmIkBqvIHdSClZ7lICAmxu8ARaRyHaupXsoQbjSI1QfEA0AuL65rcPqGnvbf5SYQMGE_1RYK4mePAqTitiKtrYhi7ueZmaQVCXQCoJUBclMkIaHN0IFASktF95GL-Ihk3_JCtN8-IJ4EqJPw3eSwPGnKx4vXiyYu3dcjIDczksTpEkXrUM7m-IeUTYYBCyQmLQPltdYkserGMHVvaGi4w4AlatdtZaKSeqTIxGBhRTOEf_L3eFskiu7_bHGNzoy8ozqLKWPBS6jcoLbjBImGa08Rdz14l1anrMn2ZhMPhONHwp4n1hNruXkn8wZAUKAN8K09BANX_63YLPKZVQoXxL3uIgiarwkqCvCl-UXpynxrMqkioWFNVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزله‌خوانی و ادای احترام عزاداران خوزستانی به پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/667000" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رسانه آلمانی: حضور میلیونی در گرمای ۴۰ درجه
🔹
دویچه‌وله با «تاریخی» خواندن این مراسم، جمعیت را «دریای سیاهی از عزاداران» توصیف کرد که با وجود گرمای ۴۰ درجه، با حضور هیئت‌های خارجی و ابعاد سیاسی برگزار شد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/666999" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=jWnX7fq4xb0M7jxnu9aIquWIwZo-PcsXH-0rkjrWABHYTP2T4Nbrp76AmV3a3hJW96iik1krNX-FAF8aBlVL6EvX0hGMK1x3Gsr6po5ckEDG_vVHMFSEqRBgd-M79CTn-TzPz8FQCGuKiTS_9fQygNI02CC5OxJ2MOsdPDwartH5wZeT2kM9NeL3P_pH5A-l5sS8AMjxnINf0IHTSlDFNrDF1u9ONjuYxJz21dO1Jr61_UXajtEJtUKRS-XPtY8sIShpOHkR7VrFZigeFvcuowK-CZmZPStZBol4D3C8MYEJ2lyKThi6njqE1WS89vY4RIZ9pKrvGcWlwrx6UFNKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=jWnX7fq4xb0M7jxnu9aIquWIwZo-PcsXH-0rkjrWABHYTP2T4Nbrp76AmV3a3hJW96iik1krNX-FAF8aBlVL6EvX0hGMK1x3Gsr6po5ckEDG_vVHMFSEqRBgd-M79CTn-TzPz8FQCGuKiTS_9fQygNI02CC5OxJ2MOsdPDwartH5wZeT2kM9NeL3P_pH5A-l5sS8AMjxnINf0IHTSlDFNrDF1u9ONjuYxJz21dO1Jr61_UXajtEJtUKRS-XPtY8sIShpOHkR7VrFZigeFvcuowK-CZmZPStZBol4D3C8MYEJ2lyKThi6njqE1WS89vY4RIZ9pKrvGcWlwrx6UFNKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ايمان قياسى: تمام دنیا درحال تماشاست که رهبر شهید ما چقدر طرفدار داشت/ آن آدم معلوم‌الحال توییت زد که فکر نمی‌کرد این میزان جمعیت را ببیند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/666998" target="_blank">📅 17:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqlL__vXxLx7QMOEv4qoNgR3C214uDi_-qqhgH7eZy6FSW3wJ5CZoucDz3x6Pj6QJS9X5U2bHRVjyxiKhvCRiuh-3BNZ1MfwYBRp1Tx3NL-PWtg_BVkN8_vQleBlgMhMqrcjfYBXkEEGllK4JdcAZxgiRvT1nwNAcPrfPe3rLosmnyuGkRj6IHaA3X-pyfGpjurns_22RTfix730phvh6EUk7ZderhTfiHcQGKdX2FSc1mAQfp-X6tYW5BVOWHZewrjuBXxWMBgNDrXtOm4BtYNSttfAhXBwyWhFZreaeP5Qt8KVJjRCn8r_tF4lptpEQpQ5Y_iZ_Ufiq9nYlXCiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/666997" target="_blank">📅 17:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رسانه قطری: بهبود حمل‌ونقل هوایی جهانی پس از تفاهم ایران و آمریکا
الجزیره:
🔹
پس از امضای یادداشت تفاهم میان ایران و ایالات متحده و بازگشت تردد دریایی در تنگه هرمز، روند رزرو پروازها بهبود یافته و نشانه‌هایی از احیای حمل‌ونقل هوایی جهانی پدیدار شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/666996" target="_blank">📅 17:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709110060d.mp4?token=IeS8xsniS38KgxjccVhVp6P55xnERdWNKv26vneLIEIBnzEfDkTAW-zN1SBGHzDufS7LNYZP6138Rlb9LFReOAYO-eaI3IHZr6ZDiAvOssBTdjNM61GNTP8_SmFUxuhWyP2Ep91HMcBAqu0FisCT1HWtPF2YK5A4Vp9G48uwR9tBIAoNkPeULi3Ci1owC4eLSAG0eFLYNPAa6huX1uX_pXI7SAA7mikIi-XJ08HgW1lpgAwuGkMWQrjR4ILuJDBpSSwmn4h7RA7GW1OoLBJ8zPHo_tvGmaSWjqdrISxa3_IHWL93YnQrr7ofiiVyBa5l-NuL05UmcDPZwHoyFIs3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709110060d.mp4?token=IeS8xsniS38KgxjccVhVp6P55xnERdWNKv26vneLIEIBnzEfDkTAW-zN1SBGHzDufS7LNYZP6138Rlb9LFReOAYO-eaI3IHZr6ZDiAvOssBTdjNM61GNTP8_SmFUxuhWyP2Ep91HMcBAqu0FisCT1HWtPF2YK5A4Vp9G48uwR9tBIAoNkPeULi3Ci1owC4eLSAG0eFLYNPAa6huX1uX_pXI7SAA7mikIi-XJ08HgW1lpgAwuGkMWQrjR4ILuJDBpSSwmn4h7RA7GW1OoLBJ8zPHo_tvGmaSWjqdrISxa3_IHWL93YnQrr7ofiiVyBa5l-NuL05UmcDPZwHoyFIs3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خونخواهی، میراث کهن ایران؛ مسئولیتی بر دوش مسئولان
🔹
طلب تقاص خونی که به جور ریخته شد صرفا مطالبه‌ای ملی نیست؛ بلکه ریشه در فرهنگ تاریخی این ملت دارد.
🔹
سیاوش در فرهنگ ایرانی با مظلومیت خود به نماد جاودان عدالت بدل می‌شود و کیخسرو با برپایی داد، نه تنها خون…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666995" target="_blank">📅 17:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آغاز فروش بلیت قطارهای فوق‌العاده تهران-مشهد برای مراسم تشییع
شرکت راه‌آهن:
🔹
فروش بلیت‌های قطارهای فوق‌العاده‌ در مسیر تهران-مشهد از ساعت ۱۷ امروز آغاز می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666994" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22624cd3fb.mp4?token=i7TEwbyAd3-0EItqya7z7Iue_lyD1hbY78PjT5o0DuWeb63sjk3nX2OlBuXgvMcG6sbKsGRZLQzkpxTt74X2PlONxclW1OJTWaT2yv4GnI09hxxr1dmawHr8wLpCXP-CR1dq004UQOGxaxGT-moz6wL_Ha7Po8Q29sUlTmGVrC-N-RZo1bSjHt_2oAauWOBD8s3Z2tgt_SKg-tX8OByXfF61fIwJFJ9TPfubbG6eSKf1RxZR3lKdMgkmP_1Pax8OJxHN9XsrGbxvfJYFq1zGTG8C2XDkH1e3vevapi38emyJcVQjPdD1-jJI9FNw3_OlOpRFDJu1j3ccPCw49nlOlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22624cd3fb.mp4?token=i7TEwbyAd3-0EItqya7z7Iue_lyD1hbY78PjT5o0DuWeb63sjk3nX2OlBuXgvMcG6sbKsGRZLQzkpxTt74X2PlONxclW1OJTWaT2yv4GnI09hxxr1dmawHr8wLpCXP-CR1dq004UQOGxaxGT-moz6wL_Ha7Po8Q29sUlTmGVrC-N-RZo1bSjHt_2oAauWOBD8s3Z2tgt_SKg-tX8OByXfF61fIwJFJ9TPfubbG6eSKf1RxZR3lKdMgkmP_1Pax8OJxHN9XsrGbxvfJYFq1zGTG8C2XDkH1e3vevapi38emyJcVQjPdD1-jJI9FNw3_OlOpRFDJu1j3ccPCw49nlOlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط چترباز آمریکایی در مراسم سالگرد استقلال
🔹
در جریان جشن دویست و پنجاهمین سالگرد استقلال آمریکا در ایالت کالیفرنیا، یک چترباز پس از اهتزاز پرچم دچار حادثه شده و سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/666993" target="_blank">📅 16:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e0806ea3.mp4?token=q7rc7Gw6GHSYdJQBKhzlbD9MrAihvlZuCFV79FqSXqYLw4SUhDj-o2eVikPjo1Jbja8V5YLJG9Xd1ZKWN2JWmYF22oYMYFngVbByWEbP0Pl6DPKMUiSqUmZt2HO3ucoMO6xm1K5gMFtEXT6yUkWMdcjkiC4GZptUEw1QUOpYIl4xYVEiDS6s323IXmaPQmVnASWlK-Udd-oRHLzqbXUrtfuiWN7hDMNraOpERiSjuUpzk5lShxxcbq5LmFDjCKJfK8IdJjIZwE9MwU6J_u-P-rnbMD5qEeFZ6uu4ENV4oZp9KnsLYFdsCtKBPmQ-siCKnyhhwER26RoUOokKsMNVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e0806ea3.mp4?token=q7rc7Gw6GHSYdJQBKhzlbD9MrAihvlZuCFV79FqSXqYLw4SUhDj-o2eVikPjo1Jbja8V5YLJG9Xd1ZKWN2JWmYF22oYMYFngVbByWEbP0Pl6DPKMUiSqUmZt2HO3ucoMO6xm1K5gMFtEXT6yUkWMdcjkiC4GZptUEw1QUOpYIl4xYVEiDS6s323IXmaPQmVnASWlK-Udd-oRHLzqbXUrtfuiWN7hDMNraOpERiSjuUpzk5lShxxcbq5LmFDjCKJfK8IdJjIZwE9MwU6J_u-P-rnbMD5qEeFZ6uu4ENV4oZp9KnsLYFdsCtKBPmQ-siCKnyhhwER26RoUOokKsMNVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیما نوراللهی مدیرعامل
#بیمه_البرز
:
تمام توان و سرمایه بیمه البرز در خدمت زائران آئین تشییع شهید بزرگوار ایران است؛
از برپایی موکب‌های پذیرایی تا استقرار گسترده تیم‌های تخصصی ارزیابی خسارت.
در مسیر دلداگی، همگام با دل‌های سوگوار شما، متعهدانه به خدمت‌رسانی ایستاده‌ایم.
#بيمه_البرز_توانگر_و_ماندگار
#روابط_عمومي_و_امور_بين_الملل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666992" target="_blank">📅 16:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
روایت شیپورچی مصلای تهران؛ در روح و جان من، می‌مانی ای وطن...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/666991" target="_blank">📅 16:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd400c4890.mp4?token=YJjRvDrhKX0bdKbA7yq2Wij5Wsb7ahJ5tmLdhPYictP-AQr38IMgCYogCeZ5usIGJmKzlOl_nRFUWavSAh_g9cgsZAhH-spILFBnbP1fIYOQicgLYg3_Vn-kwjX126Zdnzl57M__DIAMHKnNhlXrrQvM9R3NDa3NFGdy9JSA-eFO-0v-HFdNgAUGC7ew5xQ7qRy0SxJCEuIhytm6nF28Hef2FsDXoOynRCBNIEMFeQTeEaR7c3999DX-UUdb7q88axdSKv2Fk81kNSRwwRb0fB9WMorNCsvkzOhPiV4fa4yHNxQcULdEcPbLte9zb34wP-Rb28728qHkG1Tq4wN7MRymnIe_EAMZXtdYsAGdPAE2cgt1zQ_jd_iRCGIepuFfszL5E3ztdzogCbSQ1vzTmNJSopsX0dQ3m2gOwvuIUA9_YtThHctx6cONpT8B3a29D9K-Tp_JstUWURE83bl9SI3akDThZE7Ey778lUwPO6imQnpZ9Eu3ai9K-mImeS4DFaiMlic09hPJrye8T7onPRi1zvwfDYl2u6tJ1nXhwkTNarcX6EAwSoMrxG-EwB3Fso6U_-WoHC8fi3A8eEpbMSsxp7oVjJSp17skFneEJEhepKewBD71rOe7jUp3FyA3DwfjRVcrsImOPOZMbdiDt6fLX123AzCFxJVlj9iS-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd400c4890.mp4?token=YJjRvDrhKX0bdKbA7yq2Wij5Wsb7ahJ5tmLdhPYictP-AQr38IMgCYogCeZ5usIGJmKzlOl_nRFUWavSAh_g9cgsZAhH-spILFBnbP1fIYOQicgLYg3_Vn-kwjX126Zdnzl57M__DIAMHKnNhlXrrQvM9R3NDa3NFGdy9JSA-eFO-0v-HFdNgAUGC7ew5xQ7qRy0SxJCEuIhytm6nF28Hef2FsDXoOynRCBNIEMFeQTeEaR7c3999DX-UUdb7q88axdSKv2Fk81kNSRwwRb0fB9WMorNCsvkzOhPiV4fa4yHNxQcULdEcPbLte9zb34wP-Rb28728qHkG1Tq4wN7MRymnIe_EAMZXtdYsAGdPAE2cgt1zQ_jd_iRCGIepuFfszL5E3ztdzogCbSQ1vzTmNJSopsX0dQ3m2gOwvuIUA9_YtThHctx6cONpT8B3a29D9K-Tp_JstUWURE83bl9SI3akDThZE7Ey778lUwPO6imQnpZ9Eu3ai9K-mImeS4DFaiMlic09hPJrye8T7onPRi1zvwfDYl2u6tJ1nXhwkTNarcX6EAwSoMrxG-EwB3Fso6U_-WoHC8fi3A8eEpbMSsxp7oVjJSp17skFneEJEhepKewBD71rOe7jUp3FyA3DwfjRVcrsImOPOZMbdiDt6fLX123AzCFxJVlj9iS-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهار شگفتی عکاس مشهور استرالیایی از ارادت شهروندان و شاعران ایرانی به رهبر شهید انقلاب در مصلای امام خمینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/666990" target="_blank">📅 16:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ازسرگیری تجارت دریایی ایران و قطر پس از ۵ ماه
🔹
رایزن بازرگانی ایران در دوحه از بازگشایی بندر «الرویس» قطر به روی کالاهای ایرانی و ازسرگیری تجارت دریایی میان دو کشور پس از پنج ماه وقفه خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/666989" target="_blank">📅 16:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تکذیب ادعای مداخله ترامپ در عملیات‌های لبنان توسط نتانیاهو
🔹
نتانیاهو گزارش‌های رسانه‌ای مبنی بر درخواست ترامپ برای عدم اقدام علیه تونل‌های لبنان را «افسانه» و «اخبار جعلی» خواند.
🔹
وی تأکید کرد که هیچ‌گونه درخواستی از سوی ترامپ دریافت نکرده و اسرائیل بر اساس ارزیابی‌های خود عمل می‌کند.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666988" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تعطیلی الدیوانیه عراق برای مراسم تشییع رهبر شهید
🔹
استانداری الدیوانیه به منظور فراهم‌سازی فرصت مشارکت شهروندان در مراسم تشییع پیکر «قائد شهید امت»، روزهای چهارشنبه و پنجشنبه هفته جاری را تعطیل رسمی اعلام کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666987" target="_blank">📅 16:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ce3f1567.mp4?token=A3PbOXGIE9xSJBgd6dSlyTKAHI7jDWpgBAfln6ZdIYVXe1ic4BVaZwXq6k2C-iGGsEkDx6R1myD6Jdc6PR8rWWMBtn6zj2lTaQJ9fr6SSDfpSOreBnMgAR8cdiAC2nlr0aBVkVuf0uZR7DnauORxKfGmevH1b1DG9vbhk91MSDFK6ip5DQi6QHIhXdQdLcGmsasbMZCC67-88sbn70lPKGsB-r9_tsUWCzYSNcd_ojCI-yBm1WItA4-cVsVWUITLqPvi6YxmUYEfLV3bWvWoi7m7_WcbXmPQdVDW2sgTCPU-xFex2_Sjo6kUaV_OsJPNWTp0byyLlAZ9Q4wf0AMS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ce3f1567.mp4?token=A3PbOXGIE9xSJBgd6dSlyTKAHI7jDWpgBAfln6ZdIYVXe1ic4BVaZwXq6k2C-iGGsEkDx6R1myD6Jdc6PR8rWWMBtn6zj2lTaQJ9fr6SSDfpSOreBnMgAR8cdiAC2nlr0aBVkVuf0uZR7DnauORxKfGmevH1b1DG9vbhk91MSDFK6ip5DQi6QHIhXdQdLcGmsasbMZCC67-88sbn70lPKGsB-r9_tsUWCzYSNcd_ojCI-yBm1WItA4-cVsVWUITLqPvi6YxmUYEfLV3bWvWoi7m7_WcbXmPQdVDW2sgTCPU-xFex2_Sjo6kUaV_OsJPNWTp0byyLlAZ9Q4wf0AMS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ان‌شاءالله بتوانیم پرچمی را که رهبر شهید ۴۰ سال در دست داشتند با افتخار به دست بگیریم و پیش ببریم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666986" target="_blank">📅 16:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECH5pA_tqgIDcUxvqHxV0Dg90smWV_JuOPt_itNlU_JesHxCdMw_5Tkm5QgaWT3-mK2O5oKTagaRvKWlj-wulkQd-3tRRIrPkMRmQDoFjmSZixRAM8ow6KGhfaT5o9BrN1VJ9TBB8LRcbr08TLpg8Y250he5Cna1VVPvheJHbe7P451RBfLT_Vczgy2kWTUzVv2MS7Bx-vsovpJmVibbYTRGdHvw40XthwM7i7Wwvvv0teNQVGCRUNgvhUPabvd_J9wvtjd-2X4zW3_Q-iR7mgfbLTIeUNa3RrT1vlnm68HGzlVp9PAjAsx5OhJ-Ti-qP3tqD48rzThhZwy0IedeqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف رسانه قطری به حضور میلیونی در مراسم تشییع
🔹
رسانه «العربی الجدید» با اشاره به حضور گسترده مردم و مقامات در مراسم رهبر شهید، به ثبت بیش از هفت میلیون سفر مترو در چند ساعت و اهمیت سیاسی و اجتماعی این رویداد اذعان کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666985" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9BdESwfZnDOjseDhoUWb4GxGVfcFhDoxU6AxWSrFjzu_4Tcw_f9TsJzuURQUoz2bH4-pj3YICPBhGQt7KSAXlcoaqiIBJwBwvlY6c90JBqjxNaIo2o9KgCMQdvdglAGpUDrKp0Gj0qj92Ib3bGaCc832f02FboOziXUMYKjLC2fxFNSyxJ7Alcb2QCAGmt8PTF4CflRb9dVbIuonn_aeAC2dq6uKNd86glkkpqKS7PMpWlzNeiQPSY3iyKT_LyFcaPcoq8nXpIbukXBqiPGnbYEvxWMYwA_PKW1Iur6FyUhSMs4-WS3TJVKtNu9tCjqrwwoa7xrhxwgFs-7nXlY_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مشترک سه پلتفرم نمایش خانگی همزمان با مراسم تشییع رهبر شهید انقلاب @AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666984" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پهپاد شاهد ایران، جنگ‌افزاری مدرن را دگرگون کرد
وب‌سایت نظامی Defense Post:
🔹
پهپاد شاهد به یکی از سلاح‌های تعیین‌کننده در مناقشات معاصر تبدیل شده چرا که هم کوچک است هم ارزان و مرگبار.
🔹
شاهد یک، پهپادی که کسری از هزینه یک موشک کروز متعارف را دارد، همچنان می‌تواند زیرساخت‌های انرژی، تجهیزات پدافند هوایی و گره‌های لجستیکی نظامی را نابود کند.
🔹
این پهپاد مدافعان را مجبور به صرف هزینه‌های بسیار بیشتری برای هر درگیری نسبت به هزینه‌ای که مهاجم برای هر پهپاد صرف می‌کند می‌نماید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666983" target="_blank">📅 16:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اینا اصلا سوشال مدیا بلد نیستن!
🔹
براندازا جمعیت ۵۰۰ نفره خودشونو در رسانه میکنن ۱۰ هزار نفر!
🔹
اونوقت ما جمعیت ۱۰ میلیونی رو ضریب که نمیدیم هیچ حتی نمیتونیم در رسانه ثبت کنیم
🔹
راه‌حل: بیا وسط و تولید محتوا بکن. راوی باش!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666982" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiFvRCQnpOX-Pe9kEQiTC193snDXJpvCW4A6VIQ1WVwQeeobL5BhWmmJBcFzWbBZMTHLzYzhYxijUradzQNHRb10bPPKzSlxrilE1S11Nt1pOYIg-ar80k30k9nM_ijrZAFnieIntsuP5uO9qfryOpK-Z3A5PArVowqnXXsngDIhFOLZGFuup3gWknVtEkifTSIGjvvRr6yl8zObk_PkeRLyP8GyTfqkoI3TpiXVbfxQ2rJ2DZsqBKDJSiYWWSf_-VYkWnFNd6aln5tymZTr-gJAuu0IEOGPWqXiuT7DxlGfwy8QGe4R63KRWb03MDtyn_Q-L-ddgAks4JjVfmDtYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ما شیعیان قاتلان رهبرمان را مجازات می‌کنیم
🔹
دست‌نوشتهٔ مردم در مصلای امام خمینی(ره) تهران
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666981" target="_blank">📅 16:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f11d7818c.mp4?token=m5AJxPFtKPFhJagb8jjXMTPF24vbAVQq1-AOFiEVCK3yFzGLa-K5AIwOyBinfa22nAIAmN5bb4jwG-yA2tOZ0sXca4TVfQCCAYWmg1j6c-gn-aCMHGQLZC1V1HACcoMDkRCjytrUXjT-w8CsJCP0wMP1QsgFOdJ2Yc8Vl3w-icZ_Zfsg2kfDko5jhPqbeGkKuHbLuEay6lGwtUAT6kXKSzdNP90VS7XDitlqQm-mOY0Fn-e5qGndHFtCU2nBGJddsN6H0LPR-RqG9jG5PMfvk5R7d5tculXzpKtOzeHZgi_5ZydqSCA0Niw5VUlo0bCr3ZXM92jODQiUdpsxzj9gsVwtiOYdah2je8MLHktuQcou4Im3hzWW6cBcBsS5J8uT9YJwLCdLvHIlfSnfXRn74QGO848eYN9Dzmy8aHtn-YUGsJTv-qhdxvqXMYI-i-eFAYsDvMnH8TG_rUPV1VZmEUAZzQzzBD3m0Ik0ezg1L2HOUaIy4R9r34mRZihnWcB8v_KZKJaJBYt_KZ9nsGDHPjiwTYFJXefxE6Rx29FBgPX99DevKWEd_fxnQ_f1uQlVdMkr0vBwahSUxUjL8Ujk_9O9p9ZCOPxh3OrqM2vXRgMRqVfSAd5R1vFWRH3zzfAFNpRzFpl_OygGtDQRNv56Mr4SLR2dVWV4dCbKuyRSxO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f11d7818c.mp4?token=m5AJxPFtKPFhJagb8jjXMTPF24vbAVQq1-AOFiEVCK3yFzGLa-K5AIwOyBinfa22nAIAmN5bb4jwG-yA2tOZ0sXca4TVfQCCAYWmg1j6c-gn-aCMHGQLZC1V1HACcoMDkRCjytrUXjT-w8CsJCP0wMP1QsgFOdJ2Yc8Vl3w-icZ_Zfsg2kfDko5jhPqbeGkKuHbLuEay6lGwtUAT6kXKSzdNP90VS7XDitlqQm-mOY0Fn-e5qGndHFtCU2nBGJddsN6H0LPR-RqG9jG5PMfvk5R7d5tculXzpKtOzeHZgi_5ZydqSCA0Niw5VUlo0bCr3ZXM92jODQiUdpsxzj9gsVwtiOYdah2je8MLHktuQcou4Im3hzWW6cBcBsS5J8uT9YJwLCdLvHIlfSnfXRn74QGO848eYN9Dzmy8aHtn-YUGsJTv-qhdxvqXMYI-i-eFAYsDvMnH8TG_rUPV1VZmEUAZzQzzBD3m0Ik0ezg1L2HOUaIy4R9r34mRZihnWcB8v_KZKJaJBYt_KZ9nsGDHPjiwTYFJXefxE6Rx29FBgPX99DevKWEd_fxnQ_f1uQlVdMkr0vBwahSUxUjL8Ujk_9O9p9ZCOPxh3OrqM2vXRgMRqVfSAd5R1vFWRH3zzfAFNpRzFpl_OygGtDQRNv56Mr4SLR2dVWV4dCbKuyRSxO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پربازدید از بی‌تابی زائران برای امام شهید در مصلی امام خمینی (ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666980" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad5c3ce99.mp4?token=JukvfTLVAYYsMFjHpWRnPTOOUgl5mWUoiVBv1tvmGr9raQ28BDGbVR9XX7CtGOpepU-S5pbXOqkfKaVava9uqGAfKZXiR3nG0IO6hc7n0LvmkrcQ4N0TYQjyb8DKxtUzLBmT5K92Dd9UA1YK5XmLpZmj2gMIbKS2QmJ46PtPy40yBOhxCJKaBlNJk-y1jcxcegMoqCC83gcGOnARCX3d_6pJtfwMdZ-uTt3GHTCe7nPqAzW0H_JIzEH1Mb6Db5mCWZIYRZ8-SB7lXrzh4EekBD1OTId--vCAzj3PO23NtisAIsBKcqNonB4PpuUyQCSWD8lQprOYC_QUD-xrWFsR3KozhHVkcOMwlEat0Qcbu18D41xuRQZR9ljC8sQQdjTe6EjikGWsIC5JOCuLpBRNIuq5vz7dAimIPNJylA7dazlZbp54VwUewK8gCURShkxaNmo_GpqZyvaK94vivzGGAES2FOj3XgdHAaOubu5FpQhhcRVF6UXM4m2_D2aZIZLqx0vt5H5YRDbVoTo0sqkcl2KzWBDdCe_U3-11cQVJ1EzYCP0tBhY2iMYKMAR6IXy9b0a17L0bKTeokd85FQaAOSQxed5Z_mZ8OHze-E08m75uXZGNy65ZtVimTCVp5TBpUz--WmclQQlUEWLUujtnCnETAwLELZG_x09WjMFLWSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad5c3ce99.mp4?token=JukvfTLVAYYsMFjHpWRnPTOOUgl5mWUoiVBv1tvmGr9raQ28BDGbVR9XX7CtGOpepU-S5pbXOqkfKaVava9uqGAfKZXiR3nG0IO6hc7n0LvmkrcQ4N0TYQjyb8DKxtUzLBmT5K92Dd9UA1YK5XmLpZmj2gMIbKS2QmJ46PtPy40yBOhxCJKaBlNJk-y1jcxcegMoqCC83gcGOnARCX3d_6pJtfwMdZ-uTt3GHTCe7nPqAzW0H_JIzEH1Mb6Db5mCWZIYRZ8-SB7lXrzh4EekBD1OTId--vCAzj3PO23NtisAIsBKcqNonB4PpuUyQCSWD8lQprOYC_QUD-xrWFsR3KozhHVkcOMwlEat0Qcbu18D41xuRQZR9ljC8sQQdjTe6EjikGWsIC5JOCuLpBRNIuq5vz7dAimIPNJylA7dazlZbp54VwUewK8gCURShkxaNmo_GpqZyvaK94vivzGGAES2FOj3XgdHAaOubu5FpQhhcRVF6UXM4m2_D2aZIZLqx0vt5H5YRDbVoTo0sqkcl2KzWBDdCe_U3-11cQVJ1EzYCP0tBhY2iMYKMAR6IXy9b0a17L0bKTeokd85FQaAOSQxed5Z_mZ8OHze-E08m75uXZGNy65ZtVimTCVp5TBpUz--WmclQQlUEWLUujtnCnETAwLELZG_x09WjMFLWSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاجیک، سخنگوی عملیات وعده صادق ۳: در خصوص خونخواهی رهبر شهید انقلاب همه مسئولین و مردم با هم هم‌عقیده هستند و گوش به فرمان آیت‌الله مجتبی خامنه‌ای منتظر دستور هستند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666979" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رئیس ستاد تشییع رهبر شهید در تهران: تشییع به صورت زمینی و با خودروی مخصوص حمل پیکر انجام می‌شود
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666978" target="_blank">📅 16:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
گزافه‌گویی لاپید: اسرائیل باید زیرساخت‌های نفت و انرژی ایران را بمباران می‌کرد!
یائیر لاپید، رهبر اپوزیسیون کنست در گفتگو با تایمز اسرائیل:
🔹
اسرائیل باید در طول جنگ اخیر با جمهوری اسلامی، زیرساخت‌های نفت و انرژی ایران را بمباران می‌کرد. نتانیاهو با خودداری از چنین حملاتی اشتباه کرده است.
🔹
اگر می‌خواهید دولت ایران را سرنگون کنید، باید اقتصاد ایران را از بین ببرید و پس از آن دولت بعدی [ایران] باید آن را در طول سال‌ها از ابتدا بسازد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666977" target="_blank">📅 16:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666971">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/admRKy65mTsw0rHYYUhLOqirCLe83Dpqz9s6pPFWKBa4kmVIdfdu7V-_OerN_M4854KFJkKKbAnTRs1EvJJzX2wd5D3lFnpt0_NGh2BbeAQit78AibPGXi2LOFTuEQe4v9X1NH83Dc24xaXj1ojWz3qaRzhL3WM6JR2RilPRdToytuoUMu3QTquKBQm_yt-yVSG0Wajm-w0wtLxCkwrkc5kgfN7AIVf_mgbjBdIP-abunhVDABPMrfC2P_g6NKzAx9fbCeciKM3V0Z3T7phbGKN2hF0_FcgRI3JitPNzgEKcceSr8eVpyhcQohIghVQ_WZFPvP8IW-5_uRP1ySdIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-hWtnROe-OOm0fMiZLbxqfIFEqeCzc0WzP83SNseWICG2xEnMNTpEprBiomP0geg8M-hT6IJNyNLN7dQUoOhyVHlso8VIpyldOZ2NtEEfEP6yLKwMdHI67xBGOu-dYdH2fsP34yZ79GyhxbHLlf7ZBDtjpp2fWT2Fo7W_cVf6wiX2GBa3_-Fy22E-GStsoHL97ZFyZ2E_ZqcLfcGMz5HRoB-hUX8za65AUqA625uyOYMJzebPqYuew-yML2fZXhIAWjofJTK_1E4rvAw9PyKDFxqsCgdaLMfwOddjsjZkIcMXSawWlqJl0zZ50dnsgTFtFbtjGPNOINuiF7gfxh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYDOoJRrIAPLDH7oOHsYUg1mGuSwaIlcnIbhC3Xeg1sLlAVjeMTshpkfJYJCExRNfE6z1xAohbqEUgu-FXctlTl5wFcVb9t5HNBhjCrIo0rNXk-gfFCA40C2fbywrqNTlbk17LuAReGRORhVuXhJ0S9fOlkwcRLX3ZlhOCWo_u_OIfbZ99htX8ZP_cU3j96Qgxa2t6_E6klYG_-g8w49uqYxDUBWQtnA7qGCdHoxhBaKcVUEHGCIYqdxrZPU14CQ2eGWNshNfWtcdleskdjxwzV2vEuyZk9U9XjSlZzWeV5zSgq9v4wrOY9t_G879lK81sklfgTVTkJUZsfbEXf2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGX9pOZWxoQm7JnYzsmZjlGhuMos1iK0XR5dU48zDz8eK2xsAp-UUR8nBiYPZS8dE2ep63wJV90SWfpbOTCfBIWr8B-1uMnWq-ddRyy1Ztncx8sTmPM1tcyxVBC8vQ9seLeLo97yw3VHNIqNHiGhWnItzBIuwmSbr_hkCVWFYnmtn8Qke4tnsrdkuDaNpgeevvDRTskACOpgmAkB-PHzfXhxMv8zrJ7W0gMuLEVIL1j3N_KLLoWCSUBf-kfQ_eS8PvDpTKhyP8OToBxl5tYmYPYqSNgkgYQ58o27_Q8ofh988HQY0Vt3w3yDyYi58RFmDnKmepWCE10rnDWWOyp_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpfoHH94KyhEFEhE3Zljh_wtYIoPV43Vfk2__ATliLwa1VIQ0fvJN1d05APluGAbouPevL6PLFEY1UEl30RWkVqwnAyz6erQyGJtEhtj3pXR4YqzTHGEJR0Lq9by7ogPmumnIfkwt78HUzjXIEsXAoOQUUozBbfIAqRn86TzouSRqXdCpBP9om2eGC53hImJbp5Khcuc00X3TzS8CDYxNEwgZC5npOCC0ToEGnJQU-CkbHu0az_b94UZyA-3HOqMVzbQDl1KNyB_TZ1z4oqN5d0weWtmlIncxsdLb_wwSjTXOe1HxxG7HJVTvsJk0tjmxX8PgQePQCghK7wZ5WHNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzkdZKNa_BDms1AdYtUQX7jZPmNlRVe65oKYpkvdjYslAiEQKiOvTKqwj85Y6XYr9MiNm_Yz8RSUQQLdhEWIkWkltae7CHvZEjtvB05xHf0jvGTiOffXcWKGi9GsJlvY2U3LLnFdmEFcf5W3OBGodUq-spHWGI2-rET_BvO9yx643Z3GWszYFSQZMxxeH_7h9lGxb_LZPGHPXF5TVox3UQJOA5-Nli6vgeKQeFdAdFxh_Ed46W4ZQ0AylrvQfETS7ZWUvK1gVtbdEf2SZ5FZCMAeCNO9ExpiLBEsgEODsnGqpAGSrAbo7dJjkv357YXffqQ1KXHmOeN3rZ7yp40uhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از دومین روز مراسم وداع در مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666971" target="_blank">📅 16:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
امروز نیز باید مختارهایی در کشور باشند تا انتقام خون رهبر ما را بگیرند
رئیس کمیسیون عمران مجلس:
🔹
خونخواهی رهبر شهید نباید فراموش شود و کشورهایی که در شهادت وی نقش داشته‌اند باید پاسخگوی اقدامات خود باشند.
🔹
همان‌گونه که خون امام حسین (ع) موجب بیداری ملت‌ها شد، شهادت رهبر انقلاب نیز می‌تواند خون تازه‌ای در رگ‌ انسان‌های آزادی‌خواه و حق‌طلب حتی غیرمسلمان جاری کند و مانند مختار در خونخواهی امام حسین (ع) باید مختارهایی در کسور این جنایت را تلافی کنند./ فارس
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666970" target="_blank">📅 15:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3uLKLAqU3D3WT0JNZUF2_KkVbbvQ4Y14mC7a3uC8mYoEFOSIdvo28rCxuTW4wr1ekhYtPXyjEFhuaB94fWHxbkCK5BgnZ5cSY4MngLYKvzYN1ZV71x6aFk6kg4AhZqanL9zaY19qeVLhIYokaklc437j9dOw-waVchb-iZ8KsfSiW-n0gVHMcVxIxQi427oI3wiTpDzMosh7uLxPKG7YD7YFKs7vC0TjPK0pR7yDsvuppB2YN6IMyNLL3xrW6UedCl5bMZZsmDgzdFAJ12wdO4J2xKlJUa08tsqn4Et3NQlxip9iQbJA-VnPTSFwy8xY4CMugEKizFtU24rmD46iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برپایی ۲۰ مرکز خدمت‌رسانی همراه اول در مسیر بدرقه رهبر شهید انقلاب
🔹
همراه اول همزمان با آیین بدرقه رهبر شهید انقلاب، با ۲۰ مرکز سیار در مسیر مراسم، آماده ارائه خدمات ارتباطی و رفاهی به عزاداران است.
🔹
این مراکز با هدف تسهیل دسترسی شهروندان به خدمات ارتباطی، در نقاط مختلف مسیر مراسم شامل مسیرهای شمالی و جنوبی میدان آزادی، تقاطع آذربایجان، خیابان شادمان، خیابان خوش، میدان توحید، میدان انقلاب، چهارراه ولیعصر، خیابان حافظ، میدان فردوسی، پیچ شمیران و میدان امام حسین(ع) مستقر شده‌اند.
🔹
این ۲۰ مرکز با پشتیبانی ۱۰ مرکز دیگر، خدماتی نظیر اطلاع‌رسانی، مدیریت سیم‌کارت، راه‌اندازی سرویس‌ها، شارژ، پاسخگویی و رفع مشکلات ارتباطی مشترکان را ارائه می‌دهند.
http://mci.ir/-NJ1Z7C
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666969" target="_blank">📅 15:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ehgPoSdXRHoRZJP0SEIO_DEndP2juPpbPrUUOimYAfEXXqFAvHlyWSgWKydomhW64M4R-CSPAkin8jCs03vl3JYXXRMr7gR0FKDpc9tkO63uhx-sz1OosPZAVJ65nz4RJJX-JRaz2WlSiUsITUjSkQ2-o0aCnuqzwH6xQliaIlhyEhw9JRMI-IJL33Vl8Yyn4fK7h8--rDXEq9XWJdho1GNxfYv66l5OPbjRQ3USKvK1Xm5dVVnPF2yh3NQAhx0Sc-w0pA3k6NIiXkkTi889CqLzncqrvgHr2pPO_j2J9Xvou2YNpEetrkkQCOuJCABrjp3NRKXIUqfNHhNndCkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ در شبکه اجتماعی سوشال که از آمار تیراندازی در شیکاگو ابراز تعجب کرد!
ترامپ:
🔹
از زمانی که جنگ با ایران آغاز شده، بیش از ۲۷۳ آمریکایی هدف گلوله قرار گرفته‌اند...
😳
در شیکاگو
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/666968" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988ea66958.mp4?token=nERT_EfH5aoNvIXTzloTalN2HPYgRGQ8otNi8mmVPzN6Nw08rj27m7iMJFR8izAxcCl2tmyTgljJ-2pg4B4VWqOw5jTDwYbz-2YyNsmUl4zCii1ZqHvrLJ5F92D_GWwT5ZTyg8b0JmG_ZxV4qnxheVdxwTMQ1lBfet25aXLjg-hnSZ_Lglc_UEv50AP5FifGoJ2vRbcDv_nsfsJWzS9oZwHADlGjXHYOnGBPXU3N5YgacIi19YufhpR3AiYnU6BwbRxS4J_O6bihtyoTmoWreacchsDP8Xt33VNN9hGI7O53AQ7A4dqDdZDCocFUgTI_doey1rxO4wB13cfH2qKG_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988ea66958.mp4?token=nERT_EfH5aoNvIXTzloTalN2HPYgRGQ8otNi8mmVPzN6Nw08rj27m7iMJFR8izAxcCl2tmyTgljJ-2pg4B4VWqOw5jTDwYbz-2YyNsmUl4zCii1ZqHvrLJ5F92D_GWwT5ZTyg8b0JmG_ZxV4qnxheVdxwTMQ1lBfet25aXLjg-hnSZ_Lglc_UEv50AP5FifGoJ2vRbcDv_nsfsJWzS9oZwHADlGjXHYOnGBPXU3N5YgacIi19YufhpR3AiYnU6BwbRxS4J_O6bihtyoTmoWreacchsDP8Xt33VNN9hGI7O53AQ7A4dqDdZDCocFUgTI_doey1rxO4wB13cfH2qKG_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جامانده
🔹
آقای شهیدمان، دل‌های ما را از گوشه‌گوشه ایران به هم گره می‌زند...
🔹
اگر از حضور در این مسیر نورانی بازمانده‌اید، دل‌های خود را همراه این کاروان کنید؛ و اگر توفیق حضور دارید، به نیابت از آنان که چشم‌انتظار مانده‌اند، گام بردارید.
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666967" target="_blank">📅 15:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1becbc856f.mp4?token=oCf31ZrxI090qeAGgVt68k4a3Z4TxpdWhXkJkZP9Yj0oikQ0YK0QaHF48Ypc_VwLloT-PvlDSh112TZTS9y_5MfNwjIFAyensZPlWt23Hcwg48jDB6Yy7SkLNXdof7BRhumpnZSPG7kPxyZpxoUbQp6aKY5cFtyo4RD74vA_MkhdtORPoSGuz6fjr-lPz0SOwwX3ggMf0CymvSjh-S3wRiuryMF5KyZbR7PTaPJPlFBkk1ZocVtbX13L5KbGONQS8mhIJr9o9b80Jhf-F0s8yn1X0DiyDaNQyMF_9iJGlE9LRNnLMhQqmMlLO1LOON5-MZ69sVwjo8X87BFDZr_XVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1becbc856f.mp4?token=oCf31ZrxI090qeAGgVt68k4a3Z4TxpdWhXkJkZP9Yj0oikQ0YK0QaHF48Ypc_VwLloT-PvlDSh112TZTS9y_5MfNwjIFAyensZPlWt23Hcwg48jDB6Yy7SkLNXdof7BRhumpnZSPG7kPxyZpxoUbQp6aKY5cFtyo4RD74vA_MkhdtORPoSGuz6fjr-lPz0SOwwX3ggMf0CymvSjh-S3wRiuryMF5KyZbR7PTaPJPlFBkk1ZocVtbX13L5KbGONQS8mhIJr9o9b80Jhf-F0s8yn1X0DiyDaNQyMF_9iJGlE9LRNnLMhQqmMlLO1LOON5-MZ69sVwjo8X87BFDZr_XVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا، مثلی لا یبایع و مثل یزید یادم میمونه
🔹
لحظاتی از نوحه‌خوانی کربلایی محمد اسداللهی در مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666966" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWNfQDz633kLR_cMxrr3Ghb2xh4gYtROwdv1knjhECcN_BaptRKnn97F9LoFOQlfH_eHLXBPWD6lVH3o5VG-s0cPyTxWbj6c1PU3YndjQzIVxNDWqUejrIfhmME0K98TdXcbcRGe8FIY05k1So_x9CVJOwSaO4IHH9OweZLxs71fULd7ZxqsVca1rjh1V_U1PD6do-CxGJlSRJD6OI89yTT38bi-SLoT-YztZJJKYPbm4wBC8YQou4Xe44rR20giFkFKqONqsQyQWLOjs6YIF1h3t8EaW3mK4f3tVjBW5Xei_WPNFGiRN3dkf2h-nZ-ZSde9Y9ZzUTQf9mRmZZ6lMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی تارتار به‌ عنوان سرمربی جدید پرسپولیس معرفی شد
🔹
تارتار که سابقه بازی در پرسپولیس را نیز در کارنامه دارد، پیش از این هدایت تیم‌های ملوان، ذوب‌آهن و گل‌گهر سیرجان را بر عهده داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666965" target="_blank">📅 15:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEP9mQfmyFI6ExIyStPBKb4H8oyuBG2O9McpLqblqcEqFsMz7aoTpKuu75Jc0jq6jwEMut7x9xvPzzAFhCjzHuCYRBO4dmxi0jJdEQAYIu4Q60n8-DerAKVITiemJHWAR1cx_3UJoggeJiiCBueArgD4gMA3SnX_RdYCoaZ5KUjIItvbwTzRamrWYfADVq5_nD9D2DzOMda4o6YB7XBIARl-JRZxdj_z3Cl6GhnvLSV9Sf9qBrClYWqcPQic3TuEGSwZ-UosAW36ch58ssBQOpYo5-NlpO0S4joPpv6FwISCC6y8VY9WJm6oYjcoHam994YIrJYZSB9kOvUM2U4dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a44gcgkXDVbhWlDw4bumR27QX3R6lzCS5FT1w1D4bMeGAVPIn3S2vJT2yTgOhjOWndwrFX8P_7sXb5WxSs1afX-hlHdJXwRDkNOjJ0eOr6maB0vgGMZfBEdgCm73_3yEModYJ4p1cPE53tZCTzu89rWCR7x-VIsyF5QqUj4IuaQ95aggepZDwvU149Jc_rG-1JcuDvRLm8Ndxjn2QP0WkdvD71Spuw2G9wg04gL0cRy5BKgUYFAWjehDNI7jNKQ7HW3bZfiBGuWZfSlI_J-W88etK8FymTRbZjB26xi0F9ef20GaqLhINdpTDKIyc7G1Jy15P5gmVVR89-YEiQO_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2wbM-KAdCLE4Wi34GD2MW6ZDZCRPUuOjCYQWPqYnpSwZ86TUw7MGBkQ492ovyUqwC0PhuT2n-_EysDHn1uIhZFGs5AlBLUG3JeOPcla3zBAeOMD98JbmfmzB0qd3YYz1kXLzH1Ko3bV91f2kIGyU-_pjaumEaiuA2LYZcB4Pa1d7OewLswN5RaMKgLRu3CxdUSrwpBBSz7KdoLqb2ZwnzaK5nQUiwd1OGaujYYQu8pPwWTnyxhHAlT7aAyODYptn-10Au9WpoZvViCUysKckvfmyZO3fb-_AvJg5ryZJ43rRdH8pVc1u74RYZ24xpP0f9zb8eboeUBNJWYRp5uXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAGIACk8mIrqT2-jJf3uppTdf35s5MapAoReQ8ZlkR-u7Zp5DsgyK1Fjz-5VNJCPRAV61_Y1qYQm33k8JS1Vf8oyW0JDqlxHDjPtKZSJY2oJ9FjFEKGMOcgtLCvxxrGffwUMSYqnOjQThe07v_YViGVv4x8X2ut0f_rzRv-t-cLxvS-ZyVW0Dn8mA-ix5-hdbIDQgEUcXUPDm4_Q-65IVKkqF5Mt8ddxcrGuflCmI4t3oFOy3quOkmRBb-y0V422MrWEWeNDVWYqqHt1raYIiyv76xyaYp0bHTyGHIZROnBe5JqC71EmUKHRU2JVy4swAFfyCKX9_IQPJuj7Clcnpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر پر بازدید روزهای اخیر در شبکه‌های اجتماعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666961" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
کالابرگ دهک‌های مشمول از فردا شارژ می‌شود
🔹
از فردا اعتبار کالابرگ خانوارهای تحت پوشش نهادهای حمایتی، نیروهای مسلح و سرپرستان خانواری که رقم انتهای کدملی آنها ۰، ۱ و ۲ است شارژ می‌شود.
🔹
مهلت استفاده از اعتبار کالابرگ خرداد نیز تا پایان تیرماه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666960" target="_blank">📅 15:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD5YjxF0ypUXeLZ0Wff9jtL_wQqbq2K8ZIH9Sksq31zYMOuReKr7JGJu3a1-QNuYSSCT4b6d3iBIA-MdCk1Nx1XPi6es2JfrqVlnoGoYwFDGchFIW9qUlSZlhSanJtFNvdNQwK2ZUqf6Z0z7w9DZ8qS39n69z-sBnGpHxVY0tiLKXcXifTOeY1nkeTjqcNAGVCdOeIWoQsUH4UsX849Wv3XJweXmWMTIFa2aCzF_CgdxXu_B9ZH4t7U0pRsQUQMPpuTZKMLUcB9oi9-bFFydx8CRcdQQow_KPkLuINMJJUpngSqX7MXRLQbXSyPbMhzkZ_6mMETI0TjVwl4pTRejbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید مدیرعامل از موکب‌های خدمت‌رسانی؛ نوراللهی:
#بیمه_البرز
تمام‌قد، پشتیبان زائران است.
مدیرعامل
#بیمه_البرز
در جریان بازدید از موکب‌های این شرکت در پایتخت، بر ضرورت ارائه خدمات در کوتاه‌ترین زمان ممکن تاکید کرد. در همین راستا و با دستور وی، علاوه بر استقرار شبانه‌روزی تیم‌های تخصصی ارزیابی و پرداخت خسارت خودرو در تمامی محورهای مواصلاتی منتهی به تهران، اعضای ستاد ویژه برگزاری این مراسم نیز جهت ساماندهی فرآیند خدمت‌رسانی منصوب شدند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5056</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666959" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دفتر ریاست جمهوری سوریه اعلام کرد که رئیس جمهور فرانسه به زودی به دمشق خواهد رفت
🔹
معاون مسافری راه‌آهن: برای مسیر تهران - مشهد و بالعکس قطار فوق‌العاده پیش‌بینی شده است
🔹
نتانیاهو: ترامپ از من نخواسته علیه تونل‌ها در لبنان اقدام نکنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666958" target="_blank">📅 15:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6isCCRac7qRi4qSJ5KwYpw16UpmVZDQyojaHXvGthsDIhrcm2yhN4Kx117Hk09JuvCNpO--X1QMHhVvaouuM6pZ12-Y1VYK-G5mdz-Z1nTeVyFLJ102YvhMhw27tM3hfVVATi4WVlwQfbkaeQCrjMngKeukJVJzoku_TYLKsB24yMHu1TVglLzYgxVtEssyRpgj1FOj4NZ3as7jy0JoVvCk52lER6v5rgQk34UxUYeK6_EYo-coRaz2tnYGeRJXbLpKU44UFb1QiUvUQDIb0o6zE8Ka___gmpsh2VcPCEnV_3-hXgp1c26QZ2-SMOa94vDdKqVNMJlZlQMpdGC1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۴ درصد راضی از تیم ملی، ۳۷ درصد ناراضی!
🔹
تحلیل بیش از ۱۴۱ هزار پست منتشرشده توسط ۳۵ هزار کاربر در شبکه اجتماعی ایکس، از آغاز جام جهانی تا ۸ تیر ۱۴۰۵، نشان می‌دهد واکنش کاربران به عملکرد تیم ملی ایران عمدتاً احساسی بوده است.
🔹
بر اساس بررسی یکی از پایگا‌های تحلیل دیتا، تحسین و اعتماد با ۳۴ درصد بیشترین سهم را از احساسات کاربران به خود اختصاص داده است. در مقابل، غم و نارضایتی با ۲۰ درصد و خشم با ۱۷ درصد قرار دارند. این سه احساس در مجموع، بیش از ۷۰ درصد واکنش‌های کاربران به عملکرد تیم ملی را تشکیل می‌دهند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666957" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fbae993e.mp4?token=ULBgNhYztoEDhUncARHmF_PW1UmdBNeeF3LEVdN4a2h54_KrjU-640GtFZkk1hWsWOnqo3NczxwZaG9lfgok9aQeKKPTfzLGNTAVT6x4XUFbEWOmMe4eA1xpbtb7V3CwkfjAs_JMrUFxcVddhKEMKnb8_Cq0Q9Ym_iinLZ5fnFh5FiIIJ2Jo834QgVNg9HEV73t73dEJ_9U5Iobypuo5ofxGpZvZdnZgO6l_zAhByr6Aw2Pwj34KXwJpOY6ReVxurY5eRlJbtodl8qxnY0Ou1h9cdJ3aacoS--nk3tWaiB6QFtkxA-RNCSqsUgx3oGf4rETxNfAgFUbakrS43wS-5VWz1zvq22CS93Z0s9PhtMpNEwtlHrhwPDz45BWqXWEeM9GvAS_ltUZRmaClSYQ0DX6DszN9bFdICdjgTEMqnA06u11Q-2gDF4hCi6dmK44AQ0aXsJqHH9H7ek4jbxqaDJKwhpEuXeXjeVbZkP1vAzcfg-QMpgJ_-N3GpdufZTFlmVsFmlxjVU6QIZNfbqwkiWDrDychdFQdK8zQhAoLjDEVBGAgoIzt0cqr8m5xuTo7JLncvXOQoFX3e6SGqVftDnR5p63kXylhOld7Ndf_svBI-iiEWBKC-V-NjgbF30ceSyL9IDiFM7JdoOoYAdEtIWOP22gigz4X6BtArZikkaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fbae993e.mp4?token=ULBgNhYztoEDhUncARHmF_PW1UmdBNeeF3LEVdN4a2h54_KrjU-640GtFZkk1hWsWOnqo3NczxwZaG9lfgok9aQeKKPTfzLGNTAVT6x4XUFbEWOmMe4eA1xpbtb7V3CwkfjAs_JMrUFxcVddhKEMKnb8_Cq0Q9Ym_iinLZ5fnFh5FiIIJ2Jo834QgVNg9HEV73t73dEJ_9U5Iobypuo5ofxGpZvZdnZgO6l_zAhByr6Aw2Pwj34KXwJpOY6ReVxurY5eRlJbtodl8qxnY0Ou1h9cdJ3aacoS--nk3tWaiB6QFtkxA-RNCSqsUgx3oGf4rETxNfAgFUbakrS43wS-5VWz1zvq22CS93Z0s9PhtMpNEwtlHrhwPDz45BWqXWEeM9GvAS_ltUZRmaClSYQ0DX6DszN9bFdICdjgTEMqnA06u11Q-2gDF4hCi6dmK44AQ0aXsJqHH9H7ek4jbxqaDJKwhpEuXeXjeVbZkP1vAzcfg-QMpgJ_-N3GpdufZTFlmVsFmlxjVU6QIZNfbqwkiWDrDychdFQdK8zQhAoLjDEVBGAgoIzt0cqr8m5xuTo7JLncvXOQoFX3e6SGqVftDnR5p63kXylhOld7Ndf_svBI-iiEWBKC-V-NjgbF30ceSyL9IDiFM7JdoOoYAdEtIWOP22gigz4X6BtArZikkaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با جلال ملکی، سخنگوی سازمان آتش‌نشانی
🔹
خوشبختانه گزارش هیچ بحرانی نه تنها در مصلی، بلکه در اطراف شهر هم نداشتیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666956" target="_blank">📅 15:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d69c6c7d.mp4?token=Gz9nZezs-glrqtidi29NHurO2uFD9TbPPHwi9z3XFqUJs2tCnawxRpIeMhZkPPI2RDDCGLHWj9shEOrtjVH32bFNBM6E6mSeHPKXFGTh4Z0RXw0CSHYMNSyq2Tky7I4APACrCP8kdPf-W0lpNT4MAxjXjjIldMtelhVEkk-ZCi9liY7-wNpvLDLrlMXbjkoa6ilx_ajZ905Yu0HLKzH7TPpPfgAoPYDuRZOeCZXp4D3wBlKCwvWus4YbqiXAFL0T1oMMej3V_znH2NLg-aUb9RN5_dKFbBf09x5LbhK4wDagPK-ca7MxkB0XUWQusTkRr1sGotpQIllx7SrUxxUPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d69c6c7d.mp4?token=Gz9nZezs-glrqtidi29NHurO2uFD9TbPPHwi9z3XFqUJs2tCnawxRpIeMhZkPPI2RDDCGLHWj9shEOrtjVH32bFNBM6E6mSeHPKXFGTh4Z0RXw0CSHYMNSyq2Tky7I4APACrCP8kdPf-W0lpNT4MAxjXjjIldMtelhVEkk-ZCi9liY7-wNpvLDLrlMXbjkoa6ilx_ajZ905Yu0HLKzH7TPpPfgAoPYDuRZOeCZXp4D3wBlKCwvWus4YbqiXAFL0T1oMMej3V_znH2NLg-aUb9RN5_dKFbBf09x5LbhK4wDagPK-ca7MxkB0XUWQusTkRr1sGotpQIllx7SrUxxUPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید جلیلی: خونخواهی رهبر انقلاب مطالبه مردم و وظیفه مسئولان است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666955" target="_blank">📅 15:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
کارت ورود به جلسه امتحانات نهایی تا پایان این هفته منتشر می‌شود
آموزش‌وپرورش:
🔹
کارت ورود به جلسه امتحانات نهایی تا پایان هفته جاری بر روی سامانه
my.medu.ir
منتشر می‌شود.
🔹
دانش آموزان پایه یازدهم و دوازدهم می‌توانند، کارت ورود به جلسه خود را به محض انتشار از طریق مدرسه محل تحصیل نیز دریافت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666954" target="_blank">📅 15:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
افشای همکاری نظامی بی‌سابقه امارات و رژیم صهیونیستی
🔹
میری رگو، وزیر حمل و نقل کابینه رژیم صهیونیستی، در گفت‌وگو با رادیو اسرائیل، تایید کرد که رژیم صهیونیستی در طول جنگ چهل روزه با ایران، سامانه‌های گنبد آهنین را به کشورهای حاشیه خلیج فارس منتقل کرده و این سامانه دفاع هوایی را در امارات متحده عربی مستقر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666953" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تعطیلی تمامی پارکینگ‌های حرم مطهر امام رضا (ع) از امروز تا اطلاع ثانوی
رئیس اداره اطلاع‌رسانی و رسانه حرم مطهر رضوی:
🔹
تمامی پارکینگ‌های حرم مطهر رضوی شامل پارکینگ‌های شماره ۱، ۲، ۳ و ۴ (خودرویی و موتوری) و همچنین پارکینگ خدام، از ساعت ۱۳ امروز، یکشنبه ۱۴ تیرماه، تا اطلاع ثانوی تعطیل است.
🔹
این اقدام در راستای اجرای طرح اسکان و خدمت‌رسانی به زائران و عزادارانی انجام می‌شود که برای حضور در مراسم تشییع قائد شهید به مشهد مقدس مشرف شده‌اند.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666952" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/644bfd3a32.mp4?token=c6Stoz-RGfHxhwiF6clWrBGM5zhbHImD1ouV06Vpy6xq26qXb_lk4mcR_FiLjWrl5HRV52PyoZFo77FP6J46daQtNBe-Cm8l4jrFLfRSW4F2Zc4BOluUsEuEoEKQMG5oE0dSfRptBSik24YkTlBQKrZ_3I-BsQs4GU46hkX28WOj4NbGvsoypLFOcIVFYG4sveba9I2rS25tdKu9yPkfBxLmVEkCztB_dAtkAvfrCBS-XoI66pTdcfEeORA4z9JKmokC_MECuX5EAQRrc9D6V4pcbuZ_r6OgWzLMhy0_AgaUIi878xI3S-a33euwukI96epYDGMpaXMWz7rqELCMITdiWNyhyFuFCxPsgF-9r4KniQ2W_n82kN7oglmtOKmqxbzrxXtE_AOacBnVODskbuLSXV0acEQcS4HV6oyn_wemjQ_jjSHIhI7wNqu51BrXNpCBiMNeHeBK8zcZh_DJB70rYZObnDg3sbWRl-x1EXz7H5xQ-MIH-tjyuKssrkej-ihn5rZ8iu04ieLNnKBb3tjP7LhfZdcMNqmokjJDZ1FGYUm-NG8RwG2L7YyzBPnFZ0d6vh0W8Rwdb4_C_ktRuQ5vmd4S3PjYPMaRDsZWKofi_zzWktZQzuIOp0aQDgSf8XmKCKgaG5XkQZxcAI0-3IBw6esNVlC5jlE_J0ltxgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/644bfd3a32.mp4?token=c6Stoz-RGfHxhwiF6clWrBGM5zhbHImD1ouV06Vpy6xq26qXb_lk4mcR_FiLjWrl5HRV52PyoZFo77FP6J46daQtNBe-Cm8l4jrFLfRSW4F2Zc4BOluUsEuEoEKQMG5oE0dSfRptBSik24YkTlBQKrZ_3I-BsQs4GU46hkX28WOj4NbGvsoypLFOcIVFYG4sveba9I2rS25tdKu9yPkfBxLmVEkCztB_dAtkAvfrCBS-XoI66pTdcfEeORA4z9JKmokC_MECuX5EAQRrc9D6V4pcbuZ_r6OgWzLMhy0_AgaUIi878xI3S-a33euwukI96epYDGMpaXMWz7rqELCMITdiWNyhyFuFCxPsgF-9r4KniQ2W_n82kN7oglmtOKmqxbzrxXtE_AOacBnVODskbuLSXV0acEQcS4HV6oyn_wemjQ_jjSHIhI7wNqu51BrXNpCBiMNeHeBK8zcZh_DJB70rYZObnDg3sbWRl-x1EXz7H5xQ-MIH-tjyuKssrkej-ihn5rZ8iu04ieLNnKBb3tjP7LhfZdcMNqmokjJDZ1FGYUm-NG8RwG2L7YyzBPnFZ0d6vh0W8Rwdb4_C_ktRuQ5vmd4S3PjYPMaRDsZWKofi_zzWktZQzuIOp0aQDgSf8XmKCKgaG5XkQZxcAI0-3IBw6esNVlC5jlE_J0ltxgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با مهمانی از نیجریه:برای عرض تسلیت و به خاطر عشقی که آیت‌الله خامنه‌ای و به خاطر فداکاری‌ای که برای امت مسلمون انجام داد؛ اینجا حضور دارم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666951" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666949">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
اردوغان: اسرائیل معتاد به جنگ شده است
آناتولی:
🔹
اردوغان رئیس جمهور ترکیه گفت که نباید به اسرائیل «معتاد به جنگ» اجازه داد تا توافق آمریکا و ایران را «منفجر» و دوباره جغرافیای ما را در بوی باروت و خون غرق کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666949" target="_blank">📅 14:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666948">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔹
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔹
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔹
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی(ره) نیز تعطیل خواهد بود.
🔹
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔹
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666948" target="_blank">📅 14:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666947">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کولیوند: هلال احمر با اعزام نیروهای امدادگر به عراق، مراسم تشییع در آن‌جا را نیز پوشش خواهد داد
پیرحسین کولیوند، رئیس جمعیت هلال احمر کشور در
#گفتگو
با خبرفوری:
🔹
با وجود جمعیت گسترده، مراسم تاکنون کمترین میزان مصدوم را داشته که حاصل همکاری مردم است.
🔹
همه دستگاه‌ها از جمله شهرداری، وزارت کشور و سایر نهادها همکاری کاملی داشته‌اند و هیچ گونه محدودیت یا کمبود امکاناتی برای حضور مردم وجود ندارد.
🔹
هلال‌احمر با اعزام نیروهای امدادگر به عراق و هماهنگی با هلال‌احمر عراق، وزارت بهداشت و حشد الشعبی، مراسم تشییع در عراق را نیز پوشش خواهد داد و تدابیر لازم برای قم و مشهد نیز اتخاذ شده است.
🔹
۶ میلیون داوطلب هلال احمر برای حضور در مراسم اعلام آمادگی کرده‌اند و از همه مردم دعوت می‌کنم فردا با حضور خود، قدردانی از زحمات رهبر شهید را به نمایش بگذارند‌ تا حسرتی برای کسی باقی نماند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666947" target="_blank">📅 14:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666946">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d5f474f7.mp4?token=UMGTeUNCT20osQ1Jh6zsA6FQ4L5UOPI39gOoIpleXHUigSuWim4A1mSl1YFWHZFsmuk6A7ftbMNCuxrCEe9PNOU_DfluGl-NBrTLq4YpZ6Sluc24-dgHDIEk4l2oPNdMIF8cD3U2HfU667dvCrmlL0Ta-tPn7Q-BGh1ujgpDQSLBv7KDt-q2AiKx3JnoYmF0YawTc2bfqxZTYozzsas0_hZJKNSaJ8BhmAFEoGWWvUKXOWiFvqoFHNZQDliFgOmQIZMPZu667iKCMgZkzkAAPxXuyJtDcoHnNtQoC3NGwKzg1hJCrg0_gkX3Rd7BGr9x0Rw-uju0RQ-PXxAWi96Oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d5f474f7.mp4?token=UMGTeUNCT20osQ1Jh6zsA6FQ4L5UOPI39gOoIpleXHUigSuWim4A1mSl1YFWHZFsmuk6A7ftbMNCuxrCEe9PNOU_DfluGl-NBrTLq4YpZ6Sluc24-dgHDIEk4l2oPNdMIF8cD3U2HfU667dvCrmlL0Ta-tPn7Q-BGh1ujgpDQSLBv7KDt-q2AiKx3JnoYmF0YawTc2bfqxZTYozzsas0_hZJKNSaJ8BhmAFEoGWWvUKXOWiFvqoFHNZQDliFgOmQIZMPZu667iKCMgZkzkAAPxXuyJtDcoHnNtQoC3NGwKzg1hJCrg0_gkX3Rd7BGr9x0Rw-uju0RQ-PXxAWi96Oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام قرائتی: خداوند به ما توفیق دهد مثل رهبر شهید آماده باش و با ایمان باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666946" target="_blank">📅 14:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666945">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsBatCTh8lD6S2RbSpXVNFaoQQ6DQjC0wcYkeLGjTimgRgIODXTZ83aw-s--dIekjqeSx0I4HeIUFbvfwKeIWTmAHwL9lqjLBUTUedYUV9wd44g8QtRlpDykgzD_Q_YcHjN3RU_l-sgJ3YGgKKSkAL_281ni8U3NCH1i9TmH6srWT8uwEtOtuFHrd1GE1DK6Vq0bJo53P73DkxFTcw9vqKqWNsmdOxgUG7SHEoUnQulmvbUGky79q1zYeVflVLD-1sg0jaVT1JMaif-H1Mo_z-OwOCzqyiz-7ZKkpKu3etqEn54_rUe4O7LCj58bz3jAjX8yqKCbAIKwlqSuqSC2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواهید دید چه خواهد شد...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666945" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666944">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c97ee6575.mp4?token=hGm5v2vx_mT4YuoTi7-FwZzOZM5UXrFhECE1Gz_ZS1FkfEDEX3jNdCWOBfng6Oh_SJcmx7BzsrIP6kCGSpOig5j5gmn_PcaHE9TWI6098k2jG0fAL23FKbfJLfjpXSDrR0sF8egq5cxbdNb9pwR92KkKFf_zCywNCrLXPbnaci9FgeGDexhbdzTycPRnzB3QS7QgmnWbsa-7g1mlSDIdKY1pChtGnCq8X14wJR_InxIx09644j5-dMp33rwCqgJK3L4Y21-gW3t2aVwI5xDYnlison0telnNhP4JVB7ht1Zd2I8E68p60K7ocgLaVDjwHcOrRbZ04kbHflhzMRz77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c97ee6575.mp4?token=hGm5v2vx_mT4YuoTi7-FwZzOZM5UXrFhECE1Gz_ZS1FkfEDEX3jNdCWOBfng6Oh_SJcmx7BzsrIP6kCGSpOig5j5gmn_PcaHE9TWI6098k2jG0fAL23FKbfJLfjpXSDrR0sF8egq5cxbdNb9pwR92KkKFf_zCywNCrLXPbnaci9FgeGDexhbdzTycPRnzB3QS7QgmnWbsa-7g1mlSDIdKY1pChtGnCq8X14wJR_InxIx09644j5-dMp33rwCqgJK3L4Y21-gW3t2aVwI5xDYnlison0telnNhP4JVB7ht1Zd2I8E68p60K7ocgLaVDjwHcOrRbZ04kbHflhzMRz77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار قاآنی: شهادت رهبری نشان می‎‌دهد که ما باید چه مسیری را برویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666944" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666943">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34e15eb8a.mp4?token=s9qJcAgPgYOcb0WxA1Q1JFmLFiIiVNct5kVZe2dJVOtXAH-1dv9HlahK5__al5AnbbimzTU5gjTbTa5iusK1SYA4wGqY-nSaIIDQ8oA89omdm4oW4WZd14LyiBamK2UkuLyZmp9GhXQs9ncBB_uZYM6DeFaDgEC-hk76t96aBgkFsSPIfrXF4WAtJF8437CR8Ugc4p41bnEAmsGK-n1N2v0JBYbX3rZWJczLYyF_4Q288YmGUpVmTLCHThzQ0OmXPV2Knm-8szndR6Kq_0boJ0L1f6fh2E-wys9uKvtDWmfGTXr2pa4w-qbeRiDkA4i7f5XMYs5oREWh7CsyOu35fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34e15eb8a.mp4?token=s9qJcAgPgYOcb0WxA1Q1JFmLFiIiVNct5kVZe2dJVOtXAH-1dv9HlahK5__al5AnbbimzTU5gjTbTa5iusK1SYA4wGqY-nSaIIDQ8oA89omdm4oW4WZd14LyiBamK2UkuLyZmp9GhXQs9ncBB_uZYM6DeFaDgEC-hk76t96aBgkFsSPIfrXF4WAtJF8437CR8Ugc4p41bnEAmsGK-n1N2v0JBYbX3rZWJczLYyF_4Q288YmGUpVmTLCHThzQ0OmXPV2Knm-8szndR6Kq_0boJ0L1f6fh2E-wys9uKvtDWmfGTXr2pa4w-qbeRiDkA4i7f5XMYs5oREWh7CsyOu35fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد مخبر: قاتلین امام شهید به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666943" target="_blank">📅 14:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666942">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7985e8023.mp4?token=sV79dPnd4jmpf7YEzQBmZM2756NTpJnZukqJz3V89dcr4ujHqbbQypaNOETk9Ilo5bba9gud32vaZaByWy3hFt2N15UHxNGerYkINOPB-WZECix0pumZb1-9IP5sH6vEz2K-_qiV1nyOOjc-rraFhuGQeqi2Pxy3h2mPnv_OQnMgR7ysIIk8WejAFZGScb0J-U8bItjHyBNPlR97RCKcqTz7KNKMmlQ2QWKDzQIdyDHlYRBgFYUjFl2JdHONCEMvafGlheZFKg2MWoUEUn6WVNaCIysHCP8cvDZoifWxZJfNAq2y795uoXBcttrdEOYztPRocyrSHdASlwf5woUNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7985e8023.mp4?token=sV79dPnd4jmpf7YEzQBmZM2756NTpJnZukqJz3V89dcr4ujHqbbQypaNOETk9Ilo5bba9gud32vaZaByWy3hFt2N15UHxNGerYkINOPB-WZECix0pumZb1-9IP5sH6vEz2K-_qiV1nyOOjc-rraFhuGQeqi2Pxy3h2mPnv_OQnMgR7ysIIk8WejAFZGScb0J-U8bItjHyBNPlR97RCKcqTz7KNKMmlQ2QWKDzQIdyDHlYRBgFYUjFl2JdHONCEMvafGlheZFKg2MWoUEUn6WVNaCIysHCP8cvDZoifWxZJfNAq2y795uoXBcttrdEOYztPRocyrSHdASlwf5woUNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان، فرمانده کل نیروی انتظامی: برای ما سخت‌ترین روزهاست/ امیدواریم این وداع توام با سلام باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/666942" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6562a415.mp4?token=JGQKjvCROT9eajJPCfap099wHQ9nxBfoO-nzttNHg9pTL1t9o5WWaojNrRaA4oJXCTDn_mb-ynuCrlyYmuRWgw_GRyzRI07CDuk0gL6kjdyrAmfJ3sG9gNqfSq_PkvYZrLRlidWBEX4PutcTB2dak3wD08J8L-rDcG6iGX1tfFZmY1yweDTqZK3eWbWwF9mfS8DexsC_AfUvcx7gXZ22vtsOd2uJ2fKeWQjQuLqhaNNKQDfYx9qhg4kfjG1D5NcW_zqNjtn_9oevaPfWilUEXbyI3DXLZJqr1w_gxYRuNf91ANM1ZA3lK0yeA64ZioAF0pyr7BeBsnxl6QaNieUMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6562a415.mp4?token=JGQKjvCROT9eajJPCfap099wHQ9nxBfoO-nzttNHg9pTL1t9o5WWaojNrRaA4oJXCTDn_mb-ynuCrlyYmuRWgw_GRyzRI07CDuk0gL6kjdyrAmfJ3sG9gNqfSq_PkvYZrLRlidWBEX4PutcTB2dak3wD08J8L-rDcG6iGX1tfFZmY1yweDTqZK3eWbWwF9mfS8DexsC_AfUvcx7gXZ22vtsOd2uJ2fKeWQjQuLqhaNNKQDfYx9qhg4kfjG1D5NcW_zqNjtn_9oevaPfWilUEXbyI3DXLZJqr1w_gxYRuNf91ANM1ZA3lK0yeA64ZioAF0pyr7BeBsnxl6QaNieUMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون‌اول رئیس‌جمهور: مسئولیت ما برای پیگیری فرمایشات رهبر انقلاب پس از شهادتشان بیشتر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666941" target="_blank">📅 14:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666940">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90c430708.mp4?token=A8tH4BAf6QVobgULYwM6PgR5rk-dIpgKg2EiJDRibm2c91IfqGXhQADdKEODSDS6xaMx2vw3tKZvKi6ja3Ux8jQtRUMwCaxW4DAO2RxYSp8eS6NNNGpVSkYNQzr4i7jsg5M1Z1K0pjcCb4vYIdkNMBrcxVYjDMK2wYI-ExJ2IQLicxeVZbTCDnau3SBd5J25ALE3AzeKDJ6pWDeNxxTNyIViKxJ_tt6hRadozvAEG3Z3iCRWr1zkMJF8tdyrRYqNwr9lcr5hq_qs6RNdKAvNcQMlLJrZXOSAQevo8v9QBlYUsTasc2Akj_sD7TnxRCrzCR9kYM4LCM3waHZAkGHhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90c430708.mp4?token=A8tH4BAf6QVobgULYwM6PgR5rk-dIpgKg2EiJDRibm2c91IfqGXhQADdKEODSDS6xaMx2vw3tKZvKi6ja3Ux8jQtRUMwCaxW4DAO2RxYSp8eS6NNNGpVSkYNQzr4i7jsg5M1Z1K0pjcCb4vYIdkNMBrcxVYjDMK2wYI-ExJ2IQLicxeVZbTCDnau3SBd5J25ALE3AzeKDJ6pWDeNxxTNyIViKxJ_tt6hRadozvAEG3Z3iCRWr1zkMJF8tdyrRYqNwr9lcr5hq_qs6RNdKAvNcQMlLJrZXOSAQevo8v9QBlYUsTasc2Akj_sD7TnxRCrzCR9kYM4LCM3waHZAkGHhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش مردم انقلابی در متروی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666940" target="_blank">📅 14:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe1MThZ7jh5hxvhuLtiaTu4LoRguQ2e4W9uexgiCCi8hgMnmfTCzdVCUbrG72BRTh6DDy7MrMsSRZlgzFMWqBXNaWIvtSHAtNXMQPcKrDS-W8hbQHAstP8omignYxwOsmZlb5ggmTcFWH1OU009bGMy-67iPqvtJglctex_iZBylpn3ZUlT3go_PTcfZdpq0YqcM7g3nZXNOTfGcJKsuMMjSw0rf8jJNk5C_pcFB9td3jbrx0sJgwlOhM9Ede7gfGAkJB3wxMIFyFQFTWyMgMXkE_gVjV3_Nzt6HpdaxCv1uFHnB_M_joeMS7Ej2f6gsTEV-26OrhcYGVuxGZbnQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پابرهنه، روی زمین داغ؛ آخرین بدرقه یک برادر...
🔹
تصویری از برادرِ شهید مصباح‌الهدی باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666939" target="_blank">📅 14:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f432b1b38a.mp4?token=dhEQ9DHjQyxv2c2pLKBZeAO8nXetgQd1fLxfuI0tKnCtk3BxyQIZahwNmHuR23rNubXD8bTdkawawFPfpqkxxAWmB_tZjB-ZTQzclV5rwCxojjtHxifrmbwsr49gKqvFzp8BBS4mojRb4rnwPQ4KsuzQeTnTN4YAAY0Qs689DwHpI3x_yzAgcaHkkgHoIn_nUMl8CTaCk2IrijRA73n3A5j5XjRSGEbaPsX3Wl-aZgolpOzpK37Zh1S9ZPbj0StOdYGEJM6hEYnc3AQMyE1gi-NNFp2ewDgjOoOjy8BXiB2ZJ9R_T52ujLRgJCW6pr85zPVpxqGelUxfXWU78_4itqFg-ot5CENgjgN1YW4tdJGREmY3Z7dbZRpbTtUYB27BPGXAQIKdskxq7B6UWSUBSSU7u2ONbW15gvm-lfy09YRuu_IPm0BvdbHJXMPU_SWTu9954wwj2DrYfz1WZXCgRYEICKeDLN3jpkXOgQZ8UOjV-C9NWi9aEMjp7Xqe8QH8ISS5tLQH7Q6yhnWaA4-0fPxlh6CVc69tFWgb1WrTUbME3YirA1-Or359aACY-yKz50ti7FjMOK26mw4ICIeLmgJ3UvNbE6NUNfz5cA2Mw3ambNPE80AR-7xKtkIRWSEYp8FmiNQcK_Ina5B4ryZm_Z0IAuNqcd3oxrbMImktSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f432b1b38a.mp4?token=dhEQ9DHjQyxv2c2pLKBZeAO8nXetgQd1fLxfuI0tKnCtk3BxyQIZahwNmHuR23rNubXD8bTdkawawFPfpqkxxAWmB_tZjB-ZTQzclV5rwCxojjtHxifrmbwsr49gKqvFzp8BBS4mojRb4rnwPQ4KsuzQeTnTN4YAAY0Qs689DwHpI3x_yzAgcaHkkgHoIn_nUMl8CTaCk2IrijRA73n3A5j5XjRSGEbaPsX3Wl-aZgolpOzpK37Zh1S9ZPbj0StOdYGEJM6hEYnc3AQMyE1gi-NNFp2ewDgjOoOjy8BXiB2ZJ9R_T52ujLRgJCW6pr85zPVpxqGelUxfXWU78_4itqFg-ot5CENgjgN1YW4tdJGREmY3Z7dbZRpbTtUYB27BPGXAQIKdskxq7B6UWSUBSSU7u2ONbW15gvm-lfy09YRuu_IPm0BvdbHJXMPU_SWTu9954wwj2DrYfz1WZXCgRYEICKeDLN3jpkXOgQZ8UOjV-C9NWi9aEMjp7Xqe8QH8ISS5tLQH7Q6yhnWaA4-0fPxlh6CVc69tFWgb1WrTUbME3YirA1-Or359aACY-yKz50ti7FjMOK26mw4ICIeLmgJ3UvNbE6NUNfz5cA2Mw3ambNPE80AR-7xKtkIRWSEYp8FmiNQcK_Ina5B4ryZm_Z0IAuNqcd3oxrbMImktSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردرگمی غرب در برابر حماسه ملی ایران؛ جنوب جهانی تمام قد ایستاد
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666938" target="_blank">📅 14:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354e7251e1.mp4?token=s5YY_OjURb16ht6aJBU19cVv6feGWFNeIce8TT3kcmmHYhBeLo1O_2C5H6iGYf6XtPJBM4xiBnYRD8PLarCCcrYTtWKCr59dQBGWbnXQImJCFSuT9D92yGPVlttUQyLyHGwxyupY4q_3AssJHqk_xZQna-ijntnMFU1vKmarhWS24kPNAfsNlrAwZgLO6SXCjs5j_2tsyy02d3mZueW2wSFTTYDihwAVQLiFZOG1IZmK9dte2yybMV8kg7d2lAG3-hSBZNeM2mjXkVeDrjCXItKUvNRvfTF9AWasmcZiBezsELPSorYD90vnJV2LVWP5woW4TJotaSxEeT5cZqfQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354e7251e1.mp4?token=s5YY_OjURb16ht6aJBU19cVv6feGWFNeIce8TT3kcmmHYhBeLo1O_2C5H6iGYf6XtPJBM4xiBnYRD8PLarCCcrYTtWKCr59dQBGWbnXQImJCFSuT9D92yGPVlttUQyLyHGwxyupY4q_3AssJHqk_xZQna-ijntnMFU1vKmarhWS24kPNAfsNlrAwZgLO6SXCjs5j_2tsyy02d3mZueW2wSFTTYDihwAVQLiFZOG1IZmK9dte2yybMV8kg7d2lAG3-hSBZNeM2mjXkVeDrjCXItKUvNRvfTF9AWasmcZiBezsELPSorYD90vnJV2LVWP5woW4TJotaSxEeT5cZqfQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیرحاتمی فرمانده ارتش: یقه کسانی که رهبر ما را شهید کردند، رها نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666937" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efH5E6tWRXsnpE1UM6AJTSNQSBdrLRF0redSbGoWdq3eZnbZK0Hm56HJ7X26MXLjdmd2TkEYERVGXUMeemyvvkNTuG3C_trF9hfJoU-_gXKuuQywEeOUG65SWw88ioxiLvBtDKrS5j3xaoI9Lc6dkSow839nqntFxYYRFeBlh5bT03G1F7CgBcLbZBSu07Qjp_jCCRvsplvmg1ltBxW5nrpCxuO6mEe39QV-aeHH__DDngzGzkHrHzQN8pc-MJGGeiUvmY1OrhE0XGSsWn8LzZ5czFRVxMBST4zTDnDNnE9ZfDn0aHNAwj8nuBdZJD6Kl38ycTPIP1fCmI8uDBct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پزشکیان و فرزند رهبر شهید انقلاب در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666936" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
احتمال شنیده‌شدن صدای انفجارهای شدید در بندرعباس
استانداری هرمزگان:
🔹
امروز یکشنبه انفجارهای کنترل شده و شدیدی در شهر بندرعباس انجام خواهد شد که ممکن است صدای برخی انفجارها شدید باشد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666935" target="_blank">📅 14:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhoz0DhIyQznLsXsgDG0lpNwu3rol_sWihHMGckbeslAoad8VIrDns0ZOTWa-XqTrmtU5suDVm-VIQPfXJECAoqXJX2zwbKxNbYi27Uw_qp1CO0PwBDiv1SFDGtKQM_zd7xNwlekYqlgHwYaikCu6wXh-wyMH8RvwEbA2i5nhTawYdn4-slcTGQ16_8wOk_A3dA1wZ4n6pCRMgcqGK1zDbiCjYQRrVFbhJHhLqujn0lxuUx3sljVXelI-jg2L6yNCcqdQNyFbAZFW-h3ITl3-8J5fXW2fijNrSDAqJkTAeQdwn03cZaavDCbONnxeCgu-p8UJBe4cqMPdC0yG6tQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از قالیباف در کنار فرزند رهبر شهید انقلاب در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666934" target="_blank">📅 14:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسنی اژه‌ای: رهبر شهید ما بعد از این همه زحمت و رنجی که در راه هدایت مردم و انقلاب کشیدند نباید اجری به جز شهادت نصیبشان می‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666933" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهشتم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محسن حسن‌وند که شکارچی قهار بودند و به هیچگونه حیوانی رحم نمی‌کردند در سانحه تصادف به کما رفته و حقایقی برای ایشان در عالم برزخ پدیدار می‌شود و تنها از میان ۴ نفر در حادثه، جان سالم به در می‌برد و به زندگی باز می‌گردد و تغییرات محسوسی در زندگی و رفتار خود ایجاد می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محسن حسن‌وند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666932" target="_blank">📅 14:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666931">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUqJQ7Ncs1H0YtBK1xvFo0npJ1wcGDL3CNLil9hXOj_T1f0Lk2TlGqXEptFTYf0DXvnJkkVu3w2EshWO8cdxFD8QI6JFAA8CgkWCNvCbm3xh92sFy7RaeRQkX7OMFEs2W4l591RE6JYkoS_52NufZ6TBQBupXi3AxoQe4U26LG6YUzl17N4hlU_al9CwLg7Xm4ARWRaxmNr1rDhELfa2vHiv2JdqRi8arvmCsL7OrhaMYQR-7vD-XKLJLHfJrSJji2USpdVKfS2BrA8FuM33dzbLO6PDIh5ox2uh_qBlUi0Vk8yuZvdHcgQ2g5vHItD1fCFDDi40vb51Ub3oD8gr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شهید دکتر مصباح‌الهدی باقری در کنار رهبر شهید انقلاب اسلامی در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666931" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666930">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXCbwV_GF-bIjDIGJIKeFP9HGlKGGJaoiBBF-M6Uu-C7L1gXIjibpptU3wPV9O5qyQYWIayUPrtqTA_6TjytLq5eaTS1bCAmzDi8keZWyLbruVCf0ZNACtEzpmVVKR_Vgu2eQ1lUKJZoGYPBtQycs_Gv6rYnJTQsv6e1yaKNOXv8VWYKUIKgtOLH1iw6k9txGyP9U8UvV4jUiHTaNDM4FchzaFaN2gaVxeiyjYnrYrQTEbERQAB2Lmp2vq2kIfHq7J5HANqPsj218_-qX8-Ezr2_EfBDoBCfx4YvK4NjwtuZU-LFDqlMWl8BDLQ4wLilEiPjagVQtqWk8eWej4BNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منطقه بندی مشهدالرضا در میزبانی از زائران و خونخواهان آقای شهید ایران
منطقه ۱      فارس  و اصفهان
منطقه ۲     تهران ،قم وخراسان شمالی
منطقه ۳    لرستان ،کردستان وچهارمحال بختیاری
منطقه ۴     کرمان ویزد
منطقه ۵    هرمزگان وبوشهر
منطقه ۶     خراسان جنوبی وسیستان بلوچستان
منطقه ۷   کرمانشاه ،ایلام وخوزستان
منطقه ۸    زنجان وهمدان
منطقه ۹     آذربایجان غربی وآذربایجان شرقی
منطقه ۱۰    اردبیل وقزوین
منطقه۱۱      گلستان وسمنان
منطقه ۱۲   گیلان ومازندران
شماره تماس راهنما: 5151-051
لینک ثبت نام:
bayadbarkhast.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666930" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666929">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: قول می‌دهم راه امام شهید را ادامه دهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666929" target="_blank">📅 13:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666928">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIw129mXjT8PuQG__NOxP9v5S0AmsclnP65JLKkmIaSxXtviE88dXH5_1Pb_cGfdZrNYgIFWY-O90rtVRuuE8X2edrApbFei6ymBs0qfGOEwPbZ4_wFMuz6pKbm4c3MBR2WC0JNPUggbO4lCtrWRAXsh3W50M2mDCZb2WqbO52uV_mTxJanXewIaeIEykujCVrr_-3QscrtI2U3Bid9DiI5g85zKTuQ9ONsshp1LctPUZuqw58rjKdx0arR74zXzRZTkLs05Fy0Z6bUkr3xb6hwPSQWMbldicu4Nk6Ixpseqk6qLkXZUuQqXneZRepl1Xs4N1HYs4g4LIL8xEIawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ملت شکست‌ناپذیر ایران امروز یکپارچه فریاد یا لَثاراتِ‌الحسین(ع) سر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666928" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666927">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شتاب تورم ماهانه کاهش یافت
🔹
با انتشار آمارهای جدید، تصویر تورم در پایان بهار شفاف‌تر شد. هرچند شتاب تورم ماهانه نسبت به اردیبهشت اندکی کاهش یافته، اما روند افزایش قیمت‌ها همچنان نگران‌کننده است.
🔹
تورم ماهانه خرداد به ۵.۹ درصد رسید و تورم نقطه‌به‌نقطه نیز با ثبت ۸۸.۶ درصد عدد جدیدی را ثبت کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666927" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666926">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک بالستیک ضد کشتی از سوی ترکیه
🔹
تایفون، اولین موشک بالستیک کوتاه برد ترکیه است که پیش از این در آزمایش‌های خود با اهداف زمینی را در بردهای بیش از ۵۰۰ کیلومتر هدف قرار داده بود. این موشک با سر جستجوگر نسل جدید یکپارچه، فناوری‌ سوخت جامد و انواع برد افزایش یافته (بلاک ۱، بلوک ۲، بلوک ۳، بلوک ۴) است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666926" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666925">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسِدخارجی</strong></div>
<div class="tg-text">سلام به همگی؛
خیلی از ما این روزها و روزهای آینده، بخشی از یک واقعه بزرگ تاریخی خواهیم بود.  قاب‌ها، تکاپوها، بغض‌ها و تصاویری که هر کدام از شما با چشم خودتان می‌بینید یا با تلفن‌های همراه‌تان ثبت می‌کنید، تکه‌هایی از یک حقیقت بزرگ هستند که نباید گم شوند.
🖤
«
به همین خاطر، برای ساخت یک مستند بزرگ و مردمی، به همکاری شما نیاز دارم.
»
از هر قشر، با هر نگاه و از هر کجای دنیا که هستید، می‌خواهم داستان و روایت خودتان را برای من بفرستید تا در کنار هم این تاریخ را ثبت کنیم. اگر خادم هستید، اگر میزبان، میهمان، مسافر و زائر هستید یا حتی اگر از نیروهای تامین امنیت مراسمید...  هدف من ثبت یک سند ماندگار، واقعی و کاملاً بر پایه تاریخ است؛ نه صرفاً یک کلیپ.
📸
چه تصاویری برای من بفرستید؟ هرچیزی که فکر میکنید!
🔻
اگر خواستید جلوی دوربین بیایید، اگر خواستید حرف بزنید، داستانتان را بگویید و از حس‌وحالتان در این روزها صحبت کنید.
🔻
فضای اطراف خودتان را نشان دهید؛ شلوغی‌ها، موکب‌ها و حضور اقشار مختلف (نوجوان و افراد مسن، پاکبانان عزیز، نیروهای هلال‌احمر، آتش‌نشان‌ها، پلیس، سربازها، زائران و مسافرانی که از راه‌های دور آمده‌اند). حتی اگر دوست داشتید باهاشون مصاحبه بگیرید.
🔻
تلاش و زحمات دیگران، دلداری دادن‌های مردم به یکدیگر و هر صحنه متفاوتی که توجه‌تان را جلب کرده است.
🔻
اگر به هر دلیلی امکان حضور در مراسم را ندارید، از حس‌وحال خودتان در همان جایی که هستید ویدیو بگیرید و برایم روایت کنید.
🔻
حتی اگر فیلمی رو از روزهای گذشته و برنامه‌های مرتبط قبلی هم در گوشی یا دوربینتان دارید، بفرستید. مثل راه اندازی موکبتون، خاطراتتون در مسیر رسیدن به مراسم‌های وداع و تشییع (تهران، قم، عراق و مشهد) و...
🔻
گاهی پشت‌صحنه‌ها و حاشیه‌ها از اصل جذاب‌تر می‌شوند.
✨
نکات فنی مهم (که خواهش می‌کنم حتماً رعایت کنید):
برای اینکه ویدیوهای شما قابلیت استفاده در مستند را داشته باشند، خواهش می‌کنم به این چند شرط دقت کنید:
🔻
حتماً افقی فیلم‌برداری کنید (گوشی را به پهلو بچرخانید).
🔻
فقط ویديو بفرستید. عکس، صوت و متن لازم نیست.
🔻
ویدیوها باید کاملاً خام باشند؛ لطفاً هیچ‌گونه موسیقی، افکت یا واترمرکی روی فیلم‌ها نگذارید. من فیلم‌ها را با صدای محیطیِ خودشان نیاز دارم.
🔻
فیلم‌ها را با بالاترین کیفیتی که دستگاهتان ضبط می‌کند ارسال کنید.
🔻
در ابتدا یا انتهای ویدیو، یا در متن ارسالی، ترجیحاً ساعت، تاریخ و مکان ضبط ویدیو را بگویید.
🔻
لطفاً ویدیوهایی که در کانال‌های خبری و فضای مجازی پخش شده و خودتون اونا رو ضبط نکردید رو برام نفرستید؛ من دنبال روایت شخصی و قاب‌های اختصاصیِ خودِ شما هستم.
✨
نکات تکمیلی:
🔻
برای من سوژه، نگاه و داستان واقعی شما بسیار ارزشمندتر از حرفه‌ای بودن تجهیزات است.
🔻
با هر دوربین یا موبایلی که دست‌تان است، قاب‌هایتان را ثبت کنید و برایم بفرستید.
🔻
برای به سرانجام رسیدن این پروژه، همت همه‌ی ما لازمه. خواهش می‌کنم خودتون پای کار بیایید، روایت‌هاتون رو بفرستید و حتماً دیگران رو هم از این فراخوان باخبر کنید تا این قاب تاریخی کامل‌تر بشه.
🔻
لازم به ذکره که ارسال فیلم‌ها به راه‌های ارتباطی زیر، به من اجازه میده از این ویدیوها در ساخت مستند استفاده کنم و به معنی اعلام رضایت شما برای انتشار این قاب‌های ماندگاره.
✉️
راه‌های ارسال ویدئوها:
لطفاً فایل‌های خودتان را فقط و فقط از طریق مسیرهای زیر برای من ارسال کنید و همچنین در کنار ارسال ویدئوها، مشخصات خودتون (اسم و شماره تماس) رو هم برایم بفرستید.
سایت برای آپلود:
https://upload.sedkhareji.ir
ایمیل:
Contact@sedkhareji.ir
تلگرام:
T.ME/SEDKHAREJIPM
اگر باز موردی یا سوالی بود بهم در
@SEDKHAREJIPM
پیام بدید
خاکم؛ سدخارجی
✔️</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666925" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNXe4zE0O2qrD_DiKPRmPR6kiNSwzWAeqybVN7XPTdHQ0MGoXOUwXGaUwfgpmLY3apuyh1xmXbOJZbV_g0f_SD74zxJH3x7G42ZFQWVly16bFdvmin80ZPwFhujbOTExGHH1LU5kyWXjuH9CJjy1sntxgTffWbm6yT2mEaIES9u_IzK8T3u9rrrV5ahGPrvF0kRKnTzH5oFv-Dh-8FIbL6LQz6lxcaCaezva1gi6RfFcz1I_Kzf7Y7s3ODmVPmxBFa3-Izq0n5Utc9oFjUAtcuABltK6BJTKDIhh30RncLwl3cOgle9TMEwLri75fpu_DIoZ8myhwFOdYzjuw9dDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/akhbarefori/666923" target="_blank">📅 13:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkNqVPFy9gBKAEPsNWFq9Lb4qYT-1BE1HkcxCeqJkCs0n1Cir5RjMwCtjJEHUaLmJwoVzPZgeNntCYP9fF9EF7zhXo-wHnNYMQeTE9bllnfVE5LZbbmPviNw_dhO7zVg5e6Yj-G-sK0lL4c5zvVCdJ0xBwRCQ7B3qAwHlzU1FF0TklXInpjN5R7bJBFxv6JaTFQu3qXfG_WcZtc8jb9p_bCxIGkkqf1vncyTJZK9mYWjigLVC7Qgg8xHWdvTihyYYSd-Rp_PQkUXnQxo9IqjTm8lRaq3GgoueGxNQaSIriA2IY3RZDJBGnTy_AmJQ_Be176GZ8_7FHkM4QuXhz6xKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذوالقدر؛ دبیر شورای عالی امنیت ملی خطاب به دشمنان ایران:
این چند روز چشم‌تان را به ایران بدوزید
این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید!
این دریای خروشان جمعیت، حالا در وداع و تشییع رهبرشان دو شعار را فریاد می‌زنند:
مقاومت در برابر دشمنان و انتقام خون رهبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666922" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
قول رئیس‌جمهور عراق به ایران؛ نمی‌گذاریم گروه‌های مخالف ایران در عراق باشند
🔹
رئیس‌جمهور عراق، روز شنبه اعلام کرد که بغداد در حال اجرای توافقنامه امنیتی خود با ایران برای پایان دادن به حضور گروه‌های مخالف ایرانی در خاک عراق است.
🔹
نزار آمیدی در مصاحبه‌ای با شبکه الحدث گفت که عراق روابط خود با تهران را بر پایه احترام متقابل، منافع مشترک و احترام به حاکمیت ملی بنا خواهد کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666921" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
جمعیت خیره‌کننده در مراسم نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666920" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAl-wGQNmx2uiarrtDs-KUnhipGWqirNOgsphhAOgkpX7RH4jDI45KXp5zV5L6-17hCswIbY-sOfBMkWDwoiizDMaAU6E85Zcqye4qRCtIj1hN2gAZaSoLMHYjfh7vYvkPtsZRdPP9DrLsvR1j4Mvkel7DPZOsXd5GXc75xjDFk_mypwleO4xyF5xrXPR7wQJMkuL2cCwSwVBWZySkoTRVoTqEGttu5TiuLchcwcueZ0uL_eYwrz7wDqdA1NzLY_Z8SFiex-ky-aQRbeQht_sSBf5cYU6lmcQI3E2g_qXXC8agJyfsuCdPdmB81nbZSPQOZ_IXOKPlJ5UqImawJi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویندوارد: قایق‌های سپاه ۶ کشتی را از مسیر عمانی خارج کردند
🔹
داده‌های هوش مصنوعی شرکت دریایی ویندوارد نشان می‌دهد که از دیروز ۲ کشتی از مسیر موسوم به «کریدور عمانی» به سمت مسیر ایران تغییر مسیر داده‌اند و ۴ کشتی هم به خلیج‌فارس برگشتند.
🔹
دیروز بلومبرگ نوشته بود ۸ کشتی قصد داشتند از مسیر تحت حمایت آمریکا عبور کنند که به ناگهان تغییر مسیر دادند و تعدادی از مسیر ایران برای تردد استفاده کردند؛ خبری که تصاویر ماهواره‌ای هم آن را تایید کرد.
🔹
حالا ویندارد می‌گوید این تغییر مسیرها با حضور قایق‌های گشتی سپاه تلاقی زمانی دارد و نیروی دریایی سپاه به کشتی‌هایی که از مسیری غیر از مسیر امن ایران استفاده کنند، هشدار رادیویی می‌دهند./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666919" target="_blank">📅 13:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یورگن کلوپ سرمربی تیم ملی آلمان شد
🔹
رسانه اسرائیلی: ترامپ احتمالاً دیدار سه جانبه‌ای با نتانیاهو و عون برگزار می‌کند.
🔹
المیادین: مردم یمن امروز با تجمع در مقابل فرودگاه صنعاء، از اقدامات ایران برای شکست محاصره تقدیر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666918" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت خودجوش و خارق‌العاده مردم هنگام پخش سرود ملی/ احترام نظامی به سمت مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666917" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666916">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sIhBR6RIqgK4zhRj9y9XXpRJxSl-Ueiaq6dToNOL0v7AtayymLakZbxo1NkRpxkBGQypIFIt1i-G3CsaeXLmLps7pIG9rjwvtybDl7GWb80NObeN78JglnbjXDuHj8R_fVrnwsvQ4Vuj-d09_81uXvUULzGknOivDBc2ky4-2T5xNX-eYRM6BnglRH6Pb8i9xzXb2EyOyv5W52_7S9Bvj26ysVLAyK2_o2ObpCYQZlsiKN1XN0caQA_Bc-U2T5R5S0l2o9TmcrVL_w3oH1Vrp9mSPLRGGkjZS3yKMHG2ZEyUjrtyzu2AFueSY3rS4MD-X9QJoovqtGm5bz1KTFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالان اقتصاد دیجیتال هم در مراسم تشییع رهبر شهید موکب‌دار هستند
جمعی از فعالان داوطلب اقتصاد دیجیتال، همزمان با مراسم بدرقه رهبر شهید ایران، با برپایی موکب در مسیر مراسم، آماده میزبانی از مردم و دیگر فعالان این حوزه هستند.
وعده دیدار:
میدان آزادی خیابان برادران رحمانی جنب شهرک شهید فکوری
موکب فدا
https://www.instagram.com/mokebfada?igsh=MWg5bTV1dG5nd2IyYw==</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666916" target="_blank">📅 13:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666915">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تا انتقام خون رهبر شهیدمان را نگیریم آروم نمی‌گیریم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666915" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666914">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
🔹
پیام‌رسان تلگرام در تازه‌ترین آمار رسمی خود اعلام کرد شمار کاربران فعال ماهانه این پلتفرم از یک میلیارد نفر عبور کرده است. کاربران تلگرام به‌طور میانگین روزانه ۲۱ بار اپلیکیشن را باز می‌کنند و ۴۱ دقیقه در آن وقت می‌گذرانند.
🔹
تلگرام در سال ۲۰۲۴ به ۵۴۷ میلیون دلار سود رسیده و با کنار گذاشتن وی‌چت، اکنون پس از واتس‌اپ، دومین پیام‌رسان بزرگ جهان از نظر کاربران فعال است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666914" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufsLgIpy2b2SQ2gypItHjs1bGkdBs48Y_EpFqLszUTYuTDRKZ1oeYHk03OHRp04wGjF9xUyrcI_b4WBntSYutZuZTVrtJPoAEcEXXdS6vkVDvJVwxWvGLTpt_VxjLDmPysIcVWP5b95w7VEj-sifHiwZkjBFriJWTYq0dg9tismsuH_2IbobVzQ4V7yc4pdjBMncSM9Ny8N4BIUS0vmNEjG5oiNDBuUp4PRShzBNmEaKOSGBRlIfnevO3dr6fe-li5ofFAs1FvEiRbgS3xiboFXA3S00pk_SXWVF0qMcEcsh-b0K2zFxLNCyssudluSR6IQ_SnHcUwgI1VFUhYcMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgacVcrZalF3Zic5kWpQdYTizRleLB1KjPG_jrnNYMZZMtetMnhbO4XxSw41k4rClotGYmi6Qftc4qzR3WNLQUnkRdX91zfZUhDCIKkvEdEbfVx3oSSM0cxpGTy2JNXAdYm0lRMM0Rusl-ldtEpJsnNiudCzupRol7stELIhFo-RpYlmcC7IEtPr4gX34UAl2Kx6Q1UVlsmpvshKybEmTIWybdQIy0qnDYcdCWGw-4ftFzPT68YKXI9BgM_Jzv4-6WuafkZiLaFFfjzOMzVwcK2Oe_QwAIQlVeU5RD_py9QOjqXksZW_x9siPIKyY1Sle1XyVPFZqrSplgZZ_lXFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0KfPWMLmMONmt-uxWdKK0Kxn04eKh8duu47R1BmommXadwVbDfEslkAA4YD6-x7jZ3TIXpETdG93BvzRXxDpFZK4xryXrqSKqYn81rx63C0MAQYMapyF5BwwB28OXys0eaA69GUj6eHZicNgk_F-Py25AvSai96x2u8zUr8X-p1sNpbOFI16p1ZQFioRR8DMpJ6ritoa0U7MXq0tDC5QMqmk2IqiSusUAMuEF0B19Uinvdd16r3-_1Shoq-vearN_X-rALsz3nBa8w6rveWmQN48qMms0NyXL1rHI9iLGslKGjVVDmV09Diu-VXf0SB9uHeFvJnaRrc-yDJSa_Tlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازتاب وسیع وداع با رهبر شهید در رسانه‌های جهان
🔹
روزنامه «گاردین» با انتشار عکس و ویدئوهایی از مراسم وداع روز جمعه نوشت که پیش‌بینی‌ می‌شود مراسم ۶ روزۀ تشییع پیکر آیت‌الله علی خامنه‌ای میلیون‌ها نفر را در ایران گرد هم‌ آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666911" target="_blank">📅 13:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
راهشان تا همیشه ادامه دارد...
🔹
بانوی شرکت کننده در مراسم وداع با رهبر شهید انقلاب: آنچه برای خودشان نتوانستیم انجام دهیم، برای فرزندشان، آقا سید مجتبی، انجام دهیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666910" target="_blank">📅 13:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وفاداری تا پای جان/ زائر رهبر شهید: تا آخرین قطره خونم مقتدا و خونخواه رهبر شهیدم هستم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666908" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miu8Sg8ZiChuGLOKKi7UfP7bo-H5gUCBjpl388coMVpaFNvyyq6Vi6rbH4_SI4S8DSkfx3_4V6Fv898t0Q6RH5eFKPhb1DVeHGXPc7yz_lrNsdk3o8W4B8yP-F-j56HbBY4ZF1W-uN39KmWkoGd30XBHvjMFMLmpM3PzggIQwDTMwc9TcGmzGtZQ4MTev_ZDiWgVNkb6eTOepEJnq5SK3a_jnLcQ52AwNtgOiuDnmg77sjvBRQzyA0x8wkWske5Rh4TzSUj2XaaBw0BOcUIPZzWUngrJ_ghkvWHH0a5S00cVEi0Eut5fiK-CgItER3ncZUpwfTYfL94pRH9iaCix_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی: برنامه آمریکا برای سرنگونی حکومت ایران چقدر نتیجه برعکس داده است
🔹
محتمل‌ترین نتیجه این جنگ این است که حکومتی در ایران شکل بگیرد که از قبل قوی‌تر و با حمایت بیشتر باشد و نفوذ جهانی‌اش هم به‌طور چشمگیری افزایش پیدا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666907" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFt_ms3kd7eUaGNH1eP1eFvY27q5Hk5PGSFFpJ6KyCsjW_uuRftCf0FaxHfWjhlmQXMvfHb_Pztq5lT01QN6TmcDyUFTQJW0vDKvQit-4CfhiLN12I4j0nk_2OlTUy0ehUoFOZWgrCnQyK1AQusPPgS2GLpBwFmHWKaqP40_hjyZsThrkPcasGUcy4tsKVMLyERtQuwIjJMWrGTpACHmJ4PCFiHILGIpknVfshklai0JmET1malIBhN1BV-o5jvMhesZEyltzea4cbU_hDiAnQh8RteMNV1z8wExZ_KYdoPHqyU39wvrRwZ0H7KF9GOJLijG3QVKYE4T__bAW5EpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حضور فرزندان رهبر شهید برای نماز بر پیکر قائد شهید امت #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666906" target="_blank">📅 12:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تیراندازی در نیویورک در روز استقلال آمریکا؛ ۸ نفر زخمی شدند
🔹
به نقل از ای‌بی‌سی نیوز، اداره پلیس نیویورک اعلام کرد دست‌کم هشت نفر از جمله چهار کودک، شنبه شب در جزیره «کانی» نیویورک هدف اصابت گلوله قرار گرفتند.
🔹
در حال حاضر از جزئیات حادثه، وضعیت مصدومان و انگیزه این تیراندازی اطلاعاتی در دست نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666904" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666901">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بابل عراق هم روزهای چهارشنبه و پنجشنبه را تعطیل رسمی اعلام کرد
🔹
تاریخ به قدری عجیبه که: اون شبی که صدام گفت فردا ناهارمو تهران می‌خورم؛ به خواب‌شم نمی‌دید روزی بیاد که به علت تشییع رهبر ایران، کشورشو تعطیل کنن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/666901" target="_blank">📅 12:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666900">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدانگهدار و به امید دیدار آقای شهید ایران
🔹
امروز تیر آخر را به همه ما زدند، اما ما هنوز باورمان نشده که دیگر جسمتان کنارمان نیست.
🔹
امروز همه باهم شهادت دادیم که جز خوبی از شما ندیده‌ایم، این همان جمله‌ای بود که شما سال‌ها در رسای یاران خوبتان گفته بودید و امروز هزاران نفر ایرانی برای رهبر ایران دوستشان سر دادند…
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666900" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666899">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا حلالمون کن...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666899" target="_blank">📅 12:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666898">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUpjScpSgSscR2Ksjh6aagthIN0ghlpthC235EjyFRrmSMMrrJ_853jOlmlU0d6Xx-qllcvXoFU-5SSHkAFAH4Xwk6YdIhccM6EHUP9GN0hlIfqqqW3wmSIy_Ri9Cl16U8jstRwZcIW6HTH0ELMNpwgyuJUcS8KYAX5TOZu2dxMdKt24mVKxjLntooZX5YM6O66SZtZq4QSluFZuLwpK8_eDSm6WuEk1YxV4zCbpSQU34HBcl-nmlpPBrKGu-OcyHXzH8fwsat6wFbgaR3o-BVGyowB2HvJ-HPGqZtPqg6VBCBfbu2iifO_yIj3nNtrmy2fn5UOJB96AtpfdATy4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثۀ دریایی در نزدیکی یمن
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثه در فاصلۀ ۳۰ مایلی جنوب‌غربی الحدیده در یمن خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666898" target="_blank">📅 12:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666897">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWE7KFc14PkKYfUUA2nuIY7aEs_fi-ZmpzbEjVWmI4aZHg7pHwSeVj2f7SN3i1O5ntbwkjBiOH3Whf0SqPVqtZSvq2GggKOJZ1-xCqY1XgrXXOvvASaCbI1FN_yXoxhHTxz8WFtzw-G3PpVvDnv2ISNjXPQNGodo2oyo2vuxFc87sr9sJDs6h0IaiZzM3G1_vEaQPpPQVt-mjj54LneintLJAVYdWxx_D01Mr1d1iXxIDlvzAXMXJApizq0cRmg_aB3lBlJiC5C4HODfd8sHP0U5hcVzoyhvquiFbj4ZNw2eBZyJs0-ycxdNnufc3vvhLs9u6bo1MqfMhCezz7hvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: تردد در مسیر عمانی تنگه هرمز شدیدا کاهش پیدا کرده است
🔹
خبرگزاری آمریکایی به نقل از «گزارش‌های دریافتی» از ترددهای دریایی اعلام کرد که میزان عبور و مرور شناورها از مسیر ساحلی عمان در تنگه هرمز در روز یکشنبه به‌شدت کاهش یافته و به حداقل رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666897" target="_blank">📅 12:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666896">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه یار...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666896" target="_blank">📅 12:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666895">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSw_4_lk-ujwzPESPAZFgMEMnrknMM1kiq335BKSU3dqIejVuILGpHQKthEoqDwnDN6w_Cp_T9o4s1zpt94Szf7eu2sn0Vw8_lKpYneQTJ_twuCBfXDbUmByGh3QACgiLjW1WkHIfjols3gmMwxKDIe5PvHwio063i1m2fqTHnkplpNu-DRxvS_GfehjqLOUGJG9y0MqGgkuRYTt2KTtmLnauqQkYqaUcKvdmUwvXgf3p7JLIGvPpilly9FMVJ50LVeuOe4U97-ph8w66vEUAdLUcXvx3NU4iUd5kJtaqqhAW9O0lXuE0Q7EA2bBLTX1CkbA7wqg1dhZiHByjtNF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام آیت‌الله مکارم شیرازی هم‌زمان با وداع و تشییع پیکر رهبر شهید: قاتلان و عاملان این جنایت بزرگ‌ مصون نخواهند بود
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/666895" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666894">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏆
خروس‌ها با تک گل امباپه به یک‌‌چهارم رسیدند
؛
فرانسه به‌سختی از سدِ پاراگوئه گذشت
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666894" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666893">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOEjxr-X76Ju1w5jxhYjJfUM-qTkaU3wwdGCPIWJbXzVT1DAp4OxTUU3jpsPgjRcWJDZF_0R7TslE3d4ffB7SqFAe8y6Ra5bDNVKu8cVpG-AzUx4-gUpqQlZQhAXu_yLyowpL-VHXKsQHmDkkCLqJSEx7_rmKgbZK-JOowKwKczbUihNhIVuIjBLIGdn7c3hNeopM1thV2NVARoBX8HkttkbMQ4HQE4CyZYn_nj_PjVVo77NucL9HsPer3OBJRXlBJDJ9_gRPFu7arLNWyEdocip00FR0SrC8R5Bf2eURHz09VT1O04wJHVO7XEnKPhLDUk1gXI0yBw_ckB4h3CwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666893" target="_blank">📅 12:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666892">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تاکسیرانی تهران: تاکسی‌های ون تا پایان مراسم وداع امشب فعال هستند.
🔹
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
🔹
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان
خسارت جانی و مالی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666892" target="_blank">📅 12:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666891">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی حقیقت به دروغ‌پردازی شبکه اسرائیلی اینترنشنال!
🔹
دروغ‌پردازی رسوای این شبکه بار دیگر نشان داد که برای پیشبرد اهداف خود، از تحریف واقعیت و طرح ادعاهای خلاف واقع نیز ابایی ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/666891" target="_blank">📅 12:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666890">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0lWLCMkiELifCe0IyMDyP-QH6oAL3DFSwwon4ZD0952Z9N-7rvzjuBZRosEZHVi6xl-45BlxZXsrokQj8sqEiqub4X9LbC4n0r4yxwHHuWrFjEcDiea5v29HcpPed4JE3BCGjumTUZT0GQZD5JsyuttmErDVd7BAoLzVF0G-K-un4jHziI7gSwnzPlg5cE9LhMGoTjOWYycrfhUrMOEZEu1wpDOb6qg179aW7J5DlClRe0AshIrWP3o63Hz_V2-mzhV2_glDZK1AL9b1BTgJBuUNSV6wEnIwcuiY3VT7vulY8S1ctdGL8LHr3FP4gomlO5ZXBQ1YOmrZtg91MPG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیو ترجمه آیات قرآن که در حضور نمایندگان آنان قرائت شد
🔹
عربستان سعودی: آیه‌ای درباره دو ارتش که در جنگ بدر با یکدیگر روبرو می‌شوند، یکی پیامبر به همراه مومنان و دیگری مشرکان مکه
🔹
ترکیه: آیه‌ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که نشسته‌اند،…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/666890" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
به جز دوشنبه؛ اصناف تعطیل
نیستند
رئیس اتاق اصناف ایران:
🔹
به جز روز دوشنبه، هیچ‌گونه تعطیلی سراسری برای اصناف در نظر گرفته نشده و تمامی واحدهای صنفی مجاز به فعالیت هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666889" target="_blank">📅 12:13 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
