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
<img src="https://cdn4.telesco.pe/file/Y_9jYxvmFl1znpbbK4uJLDO-WndKTwTstP8Bl8JSfUfFrClFjrnbuJ7zcHS-_wuX10r5E-YAaJVFpMRZIwx6N1N7xxiQtjqDs5LO_f8OEDpmQzAOQVTriLv9fIxRaG6pd0YAIlU_7XZGw2NmHzJyz5be7W4XLZpPK-qCp3MAIJUuho-j15cpyfKKtkqOfKzyV3o9sGd_a7vzkIueNvF5NsDmQ9wVW3Ki3bbBm2Vizu6RSap1VePe79ro03wIlEB5Vas0b1Ez35LBimoNguU40rQA_uaGd2syZg2Qzrr5kESi5WlFHYOdIm1kcoA_kTKvzZoSSnXQlJU2iJDgMqGrhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 15:31:30</div>
<hr>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک‌تایمز:  عبدالناصر همتی به مجتبی اطلاع داد که در صورت تداوم محاصره دریایی، ذخایر مواد غذایی و دارویی تا پایان ماه اوت به اتمام خواهد رسید.
@withyashar</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/withyashar/16440" target="_blank">📅 15:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada09162bc.mp4?token=EHyEmEY75bUKbheAotGMaSOIkYwjjpSP8U6Sq3oFut9OycEzQ35H3Ed0UPnnNMbD5BLu5Vgg6LL7SbvgZHvfcxCAuWIivw3Gs_mfWAUoWSAnS4lAcTbpxBWK4ZiXORYV1KcZqMweTRdYW5T1PxFqWVJ37HldKYSOT4ma0sybuw3YV7Ms_sZmKn2CT_nzqvnJJRR3msjtC_gfABPOyViyEtDRgGxQRQwUBE7r3V5MEXiXwUeANIPqrUDjMjdqAb1H2ADpGBnfS1nO3zYrXc2H2OSEHPKDVR2C_I-lCm-qTRPXfuTaUIoWVmeuT9-BrZWa2fo72ImP_KavCwAEbrEzkJtTvm_iUj-UYehhK_4Jfy4wbtT2VgOfN6lTU1hm7SW0DpX52ygmzBPaN2q6DBhwFqGq15a4NEAmCr_TqX3ijRjRlKEh2EpWg4fYPYw_XyW2wfz4_ymDVrfbcw1Nlx0cV8HOUwJ4ZG8QmVzULDpXB8i0uanlIm0h8pa5eDhBNEAFXjKwCxXW-Xa1twa1KHasnsksD6-BRr3w5aPIPmxKwlHDCZxhmORrycx4YHV7lo3S0488KS0yJiYw5khp0AkHcId72scfNRY4gpWXyAXgr7luuI44npgzPRPRjkplMpTSSu1klw1td-rKDuCLVsS5HjL-pm1V0p36N29QUiq7JxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت نیکسون در ‌تهران ۱۹۷۲
@withyashar</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/withyashar/16439" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDOT5xqGrx6_6aIQT9d0aHwVViAmQVVLrvHMz9Zd60XgwsD_4PSZQcqCTeVGK-PQh0JJeGM4FAVADkL3TXSDwlgd6L6kHIlX9elLJYd-t-OEI5GgNqtbhHum5-PlitPS2iRkjRRsO0Py4PU4WS9g6F5md6ybHPjVEt8mbx4BamMtHXGw8_oOcdDpNW7EWv5VCJPgZ5_4wX2e1jVnu7xmWZPV0wt5IS03bH-Ihtz7-nTLuu-SFGNBEg9lD36678kLL841jGfJ_JH8T_xb83SOt_fa9Vme8FpvMEFB1UVNZCTnB6_mn66XM5BTCzO3TJZkrKPo789K2f8KzmcKElwB-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند.
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/16438" target="_blank">📅 13:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DefKqHIRss-mDqL16Az75XTg88fdQUgKusF3rySHcVNHgOlni5LAx6-3o8PrfqXiq_pehtX9Ew926ME6JcIs05RwRNt6SGWwjvrXW647b77L8k7XxnVdqgyCohoHu_tPwknZ16qAciocsVy7D_4P6spo6to7CRee9I_w0zms8PjKmooYSMxouTMFWfQ7Qc5KCBQBofuozeGQfkkFFKqi1IyI7ekUklndvpmt1J-c7hO1fLT7BrgUa1QKQhbJlvT_fm41ZjsanQTA4OIZqeWTsWqkw3vEmYO2AE7t9NU43IP7Ntn3ZdtKQbJK_nfkjQSpoEn7L1_QpE2HLU1M_lP-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان درست شد ، عباس مکار و ممباقر نره
@withyashar
😂</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/16437" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSDAociZJEPOSMHE1LN4mhd4eqaw0yw4IQ66m9t7YvXH9iFGb4Q_KOdwSgQixxvPe5gsEhMEJC_Gmorm5K_hiqC4kqKf8-C8HntJ5lVmQvo7lsyLK3C3eVftjvRs2_CF8f2OvjnOwKM57CUYwC9V3Z7s76bMlyFwTGwD-CFm3fmeLT8OFRUWkXtkE8Br7lg9OE-c67e3Q23e3hD3xWDfzIPQFb4Ol7jTplBTG-aii3KgTQUaYwieZ1Mn9M6NSxSRBBCHfVjthy06SsjAUs0DpgASLFtpqwcrF3_scIO2RgpcK6SMv5tOnYvWmBe3cSj5RNYl-lfYSxqXMWsJQLju9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره حمله اسرائیل به لبنان
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/16436" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwYnlfD9wImvOnqwFCtfmpeoAjaMTgIrC2bn_QerlYR9CGJwxGtom1zNBI1zIYrlnXzmn9jx7pp2cFL_HnlB3O0CRrKHn1k5bEslXfKlmXAqNVT60ErfNDLyyxJk-bSmSQzlmCoDaf_9nANHhwgKqOoL54UyIfo_Qb_ICZ8Cqdkk9cMyzhVjCcbZtb5IXWzDGUbuY_HMJg2yIXrpugBsu0VnS7SLasH0iaGG30x2st_2DVnpKYK9QtnKm5P1NYL20rwqtJPAT_N6MZN4IMNYH2bMoN9VnduM9UY62S0Ngd2iUd-Xa0wwidsogdGzRBn2cBmt6jd3F11PPrL-eJAi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : سری جدید ۱٠٠ دلاری با امضای ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/16435" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">افزایش تولید نفت اوپک با بازگشایی تنگه هرمز
طبق یافته‌های نظرسنجی بلومبرگ، تولید نفت خام اوپک طی ماه میلادی گذشته با ازسرگیری صادرات تولیدکنندگان خلیج فارس از طریق تنگه هرمز در بحبوحه تفاهم‌نامه ایران و آمریکا، افزایش یافت.
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/16434" target="_blank">📅 11:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZjn24YUiTjkMH7dfvGTmQFNhECdaqheApTycOQWD-XMlSmmqlaEWVHx8Kymyl04unvXqTvLwZ7UPbUfg7h2piSiYAc9rR4pbQQJMCrCdTwtyM4Qa67gnT8bUoQ39ir_xrxguemGqJT7eHNRH1oLZNIC6S7oRwmbs-HNwPMNyRviiFulNfAXWQbL-IOL15oiyQjHAGiSXjQN2KJ6WvXQH2ldcWkORtxNo7dLaJpwkYqYwxqexHARIPp6J0LrQIaHYq9-jHgDN1p1u5VJO1LE-4AUaRUf0d6YPyKtP7ugHu5u5Zd06eFqDwHZJyTQhOnCi0i3oDa88Q_lOLSIhPJelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MotgdfaW7aWnIto935imi19cTki2AteJvjwu8_Drg55WHtFSZVUtyO6EJnMn9YLEhSZk3q1kaAO0y2XDUmvCbiYgtTpWbUgwsyxszfbs0_q9JaNRqeLDKkpHyP5H8Wky-HD-jNFW0YhxpNyW2eyOUXAoaaW1YkECRQofS3XTVm0TkrVa3xJ1lSyW9rjc9YB-E-hRq0rcJ4gVW6DxFwNUG_Z2vb3G2plZTGNfnHmrEryk2VOKLFzFieb2NP1juEITiRBABBWR_Mrvr7rVNTRI9BSv43650-Zc2y0FIIwenoXfh5YSPRZB6shSvmnfguzy_kuoCe0ZbsTlBdQjz_s-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=qx_YnEbDCU6SD4gJpjqBRLrhnARE78BrtutBKfUbsLzVOsBepIQtz0CjgHcFJsPZ91Z8QalNGAiZKaPgIonTWsikMp6BT_Pz4OMy0XdpRmw39GjJcmWq5gtnV7Uw3E3c7KcL4LVZZjIBkObJ_Uvartbstd5yr9bSL4ebH5IEsqwNWed4w3WCXbN33Fa30-aGF5tdgJkIDuF-sDJ3MkOEV0hQhGkY68hJqIJ29L-8KJ4fXubEMt-cqgyZqOW_9-CEW-Gpx-ZNAvgbntJFfoujmuy45AEaMqHHX-l_hsKE5yrQuWi7tBa9smYassdjttR-5ELbwe_M8QMGS-OE059eZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=qx_YnEbDCU6SD4gJpjqBRLrhnARE78BrtutBKfUbsLzVOsBepIQtz0CjgHcFJsPZ91Z8QalNGAiZKaPgIonTWsikMp6BT_Pz4OMy0XdpRmw39GjJcmWq5gtnV7Uw3E3c7KcL4LVZZjIBkObJ_Uvartbstd5yr9bSL4ebH5IEsqwNWed4w3WCXbN33Fa30-aGF5tdgJkIDuF-sDJ3MkOEV0hQhGkY68hJqIJ29L-8KJ4fXubEMt-cqgyZqOW_9-CEW-Gpx-ZNAvgbntJFfoujmuy45AEaMqHHX-l_hsKE5yrQuWi7tBa9smYassdjttR-5ELbwe_M8QMGS-OE059eZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=FTNCX6AreHnmv7UibkBIZTF9wMwiRPbiqsjzaDQWkaUlr2xu2ccb-yiHC74197S6_YtjPYh3rvc4ZkgCMnKYIK75Ce2w0Ped3-dNpzKrw534LoFcV8LQEbNOwCZuxDi9Llqex0pRERpRgMQzV76pFBARekkqQ2_PBAwJy5lgeb8X236Yz72emyX6_nJjwUvV-J_oZ_gYzvyiatQ4_YL9EJY3S9dQmoyY1xNLE65nrUOZ-aajmP2cBw0rv3tZhr4lKkMfWsOT1xmD8JpMy1BRarxWZPC_UPv69g-BiJZuGbZPAIy6HGyDexP6sA9NVxu1DU3LCQH4p-Phz01uPnRq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=FTNCX6AreHnmv7UibkBIZTF9wMwiRPbiqsjzaDQWkaUlr2xu2ccb-yiHC74197S6_YtjPYh3rvc4ZkgCMnKYIK75Ce2w0Ped3-dNpzKrw534LoFcV8LQEbNOwCZuxDi9Llqex0pRERpRgMQzV76pFBARekkqQ2_PBAwJy5lgeb8X236Yz72emyX6_nJjwUvV-J_oZ_gYzvyiatQ4_YL9EJY3S9dQmoyY1xNLE65nrUOZ-aajmP2cBw0rv3tZhr4lKkMfWsOT1xmD8JpMy1BRarxWZPC_UPv69g-BiJZuGbZPAIy6HGyDexP6sA9NVxu1DU3LCQH4p-Phz01uPnRq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAJUgK_uq6HG57EEEUzFIVXFg-pvhCISko75PjTX6YWbzEfJb4OqmsAv3Wr0WOChx-WyxWQ1iSkQ1-uPANo3DIDm61xvTGgKeBI-gv0Qz3-fdz9j2nJ6-a6Ihgh4I9rebafV01yzKejQnnOln-4MJdfxP06hnesA0Qp5dd-EMpiqbhjgHAGeUyHOAdWf3bFX7qxZgY-b2HrxA_kjNHjKPFdqWHKRMSSY2ISnRATxIC-IK8E1et-Gi79GvpnWOw7shhMHLo7JJn0792EgGWvuSOY-WQn3yYXUdD-xwaDBTce2JKsrGbspbnnx9ffezQhaaprdrlW3b9s9m7zCUAGCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: جان اف کندی بعد از من دومین رئیس جمهور خوشگل تاریخ آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16403" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هفت خواننده سوپر عرزشی به نام های علیرضا افتخاری، محمد معتمدی، پرواز همای، مصطفی راغب، رضا صنعتگر، رضا شیری و حسین حقیقی ی آلبوم به اسم بدرقه برای رهبر ضبط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16402" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی/ دیپلماتیک اسلام‌آباد جواب داد؟
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16401" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=DH0DQATou74BslQMQKBIIq4of-S8g0gWmIzgGvywe549wOjtlXsWU0y4heoMQGJy1g5AdMBOzYDnR8rY4-vpch5zSLs3GHnqclwvwQfZ9f_x-FwcZDYGdce3-hmTR5LliERN7WRQmfkfKnapiKbHwjhN1yUsQDQjYGRysDH2L9My5F-Zj5DhEHMOvYUFUQUdQ8EFHpBciPEuQiY0vG2jxggw-vHfrMoCZCt5U5Y27T2G6f--whftygvRBeH9CyuGd8R9kVF_JTkGCe12ErA9Qf8LDfHJsmcuy8QGrprprYTgv556Fu0HqA0vVDwqX0pM-y7Jd3AoJaCPRau2KJIQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=DH0DQATou74BslQMQKBIIq4of-S8g0gWmIzgGvywe549wOjtlXsWU0y4heoMQGJy1g5AdMBOzYDnR8rY4-vpch5zSLs3GHnqclwvwQfZ9f_x-FwcZDYGdce3-hmTR5LliERN7WRQmfkfKnapiKbHwjhN1yUsQDQjYGRysDH2L9My5F-Zj5DhEHMOvYUFUQUdQ8EFHpBciPEuQiY0vG2jxggw-vHfrMoCZCt5U5Y27T2G6f--whftygvRBeH9CyuGd8R9kVF_JTkGCe12ErA9Qf8LDfHJsmcuy8QGrprprYTgv556Fu0HqA0vVDwqX0pM-y7Jd3AoJaCPRau2KJIQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
خطر حمله قلبی
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/16400" target="_blank">📅 16:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=jWLBzA7ztR7L0UIDm8Y_5z2Ef_5MD77ZXOvAHwi2nzHg5Rvja3OLrwpitzkoW9mt7sZLWdqmCKwESIM9bXZU9CMh0q-LkKfgWLwmQf6JtEaE4T9HGB2wqMiCksgnNSmSjxYcElCjR7yskPIwnrFrbmET5iesIf4Ml8WD2Kx9FpB-dEvdxhJUikjVDvPG1V8F54buTccUJ8-G-1JPl3A4PjwlA6KIBBWXsKFnsMDTsERPWjpB6nI4czKRGLYNrhNHHI2EvQ5UVqm5qrxnPGbZvTSxP5_p3GKt2fY7Aiy5KWZSDJj2nEk4kCy02Xc5PMpoZ__kCiGh5u0epU4ln_4Faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=jWLBzA7ztR7L0UIDm8Y_5z2Ef_5MD77ZXOvAHwi2nzHg5Rvja3OLrwpitzkoW9mt7sZLWdqmCKwESIM9bXZU9CMh0q-LkKfgWLwmQf6JtEaE4T9HGB2wqMiCksgnNSmSjxYcElCjR7yskPIwnrFrbmET5iesIf4Ml8WD2Kx9FpB-dEvdxhJUikjVDvPG1V8F54buTccUJ8-G-1JPl3A4PjwlA6KIBBWXsKFnsMDTsERPWjpB6nI4czKRGLYNrhNHHI2EvQ5UVqm5qrxnPGbZvTSxP5_p3GKt2fY7Aiy5KWZSDJj2nEk4kCy02Xc5PMpoZ__kCiGh5u0epU4ln_4Faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqmxXSIWeHfK0LkdwqxNFLIqGD350BLP4BYqiMWL7MZucjeJGGgZTwKWzdRs3UsJDnH_fXjGDpTk8zM_S1W9UaSbIqFwlxj7nCPN12D3iVHYONTgUwnWYRc7guwen9VKk0CQ0fxuc6-QzeUEFNQSzPCh4JOF3uh-vU3w68-6m-jg_j1TO8h3a1Fd-l4-2PVGKaawXat_tGWpBUbpi1T7G3xk10MQU6qfrnkgBWcWjO0_DOwWX6lJqNBb95vKfBflnf1n0JZNL6K6-eydQqvjQsBtI5RxbexvyrofMhl-ffzLKTRHkcTu_PUWLJXsG1Ec4bR-AkpeLKjSL2Ilvz0bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gi6hP82vW0MSZGplufbgEUYh3I7cRag_OHfy1tOGh36-iVJRMI3my3MaqwNs3w0bhWl6jkiqQBtZPOAA2I7BwSSl6pWZgJU1-5v-Zw1ARenqzbVmBD1CHVy8GENJy-prkpnlPYk9w0j3pd4DYXKLoHq3RYkESOqkoNW9nsOP8GJ3UrlQ5IFo75NrCx0tn5Jde9_dpAlsbAzdZrvJMgwIqqrrUMVrtHRzWSwznQ3fXFrZmIX3elg6-2ehDNfEXwi4BA41xzm-pPnI5_PfvbwD3MvlN43utj-nMYuhvY6JoX7YTx-BYsazyyFUClV2ThSNniGzrIYqzwTGF0pzS1utng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqfnnorInXq1zqqLibhx961zdBjmzMCQa2CWyXI71eSR06bi-5RvxKknZXvPKgyVBef-X7so87ZrV2sqStt3XrIlnP4Il1NXQp2Gsi0idi2yaXgqFer1iCKPc09_dz71M0KpC5xBbPQRcFL0KbeJP3dMW2Sr2j4YZjKOjyTQ3x722BHuNJ--H16VtWV1q5uejuBrmPZe1CXQGwLz7MXEo58DGUEQZudKUlc5VMsvSJVZQr4DnMLzIX65mNHxTMK4isYHMWNmkKLxeJO19-gfMUkFd39X2uIYxRJwlHJb53oOXcEj4rAiKjBmL3cF0pVCYMMWZ7pt86oMBud-mc0cSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس از تفاوت تابوت محمدرضا شاه و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای  انگار پرچم عربستانه
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/16389" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فیلم مستند «جاسوسی از تهران» هم اکنون با زیرنویس فارسی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/16388" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۴ تن از نیروهای نیابتی جمهوری اسلامی عضو کتائب حزب‌الله توسط سرویس ضدتروریسم عراق (ICTS) در بغداد بازداشت شدند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16387" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16386">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBTMYAANn92lqaBm3RttsiwW6a-qf3MU7i6K2KeTVxAnSSpXwawc6AGSu0rBwN598JZ4BdUXs3fJIsy1NmWBtxkSkYZxkYkm5371Z6cFS9tHKxFwZ39kNNU7Bi0QPmFMnlmy7td5-00-jY5ulXECkslHhQGx79euDvduQefqEsPaq41DFKY27Rd9VPIUs9jE1zfKd-r00oIO_ftdAsQ3R2LF6-gyLRuq0CNl70JeIh3jXqOyy6V-pyD1PPdhjOqwzNJciRuWVNWoqeq8d9Bxx9vqauWonnN2ugjbOFJTeSeFUOPsbzrZjpM5UgomR92RO2ZiIXg6bE9yC3SNtbr9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادان : یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16386" target="_blank">📅 12:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید. @withyashar بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16385" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMFZ_v-OtXLh6pBeUXXrS-KvzLQwh3uIYgPz317W2U5n3vDyMTUcGd0TyqMGa33oID1j5iopo_ye0dmaEtQu0A7HUNHxqCx_zNkZqqdsh1hY2NRVNTS2FdFWcx4lH0Q2zJr90B2zddB-WXcGVGHLZ7C-5CcIY4JulBsDbOs7dxnLCiA6vgSE2JZTZ14ZnvoiVP2rVLEGNBpRVDKuAGFRg6ACI6x13gXXfByYxooq4V7cFcdb5WBnJPFWRRUj-LiQeTdHJEtyZXwxouTHtImO7BE4K1cZLwQLGouko9xdOwvBEAu6sR2lZhfHLBIc2zpmkh6auNGF7bNImJIoaAVeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16384" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کل تهران در زمان خاک‌سپاری رضا شاه (۱۷ اردیبهشت ۱۳۲۹) جمعیتی حدود ۵۵۰ تا ۵۸۰ هزار نفر داشت.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16383" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEUPZKuqS0zBaWQqqflMYYA4P0C4Um9EMxT1giB30KRIZLoXm8i28ovgHdSmaeccdawkavfgdXq_hZsPcSHIa7CfWsBmtGZ54-M4g0KqEVGiI9GyijFPvfJzm86cw4QhrWckskjQ4JJEN7K8wi2F7aF4W2QKHkfbPE5iUyupyklPKCS1IstHqQcbHYH1TtD5nawh3pfncao-EIKTpzycxIMgKvwSO-qzpkxJMSn3Dnb0rrobiA6HWdNZRUZZJLTf661Pncq_YW9VS0KolDOVWYk0IoWi-Qh9pJSBMP4WNk7T9JjSSAAOZ_QG_1dNrLEePS01ACFZ2fXsvvm9l-1Utw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16382" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16381" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNu4oPeZUAV986SVanmeUb6YRYO5hruVWApjh8KCGFQvxny3Qvlnm34xIyDuFNXKz7xWTUEjXaVfLZ7BeotDt1lt7II0t_qwyw2J0UOXaXPHin8iMLB1FcXyau6GRJ-WM1-eqs9n3uWVlyRjOEXBBvyUAyX2K08WZAac72C20S1zZBIld2_mw0uyuwSWtOIT21ssOkyA3PLLNB6qM5jy43z9ZLWiBcqZFpjmw5tXEuAZ1QztDOUoCatOCdBCNYnu0RgPlPWfC2PhZ5KPZz42eO5irDyLYGSetWIhvFNUoWx71Kti9OvVXF9__kRGx6nZG-iojg77x5yA9T_TGsjykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادای مفلسی احمد مسعود
(فرزند احمد شاه مسعود) و هیئتی از افغانستان به تابوت علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16380" target="_blank">📅 10:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16379" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق  @withyashar چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16377" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق
@withyashar
چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16376" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: من به دنبال تغییر رژیم ایران نیستم
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16375" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است. @withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16374" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=OeE3rjTUmesm1VCnOlr90Hx3Z4OkzkbKZArfA17Q2rqeXjzqFlI8zQ1ugvSbXLT0e5AUOQygGE6QCGWnVfI2XQgcUdsxqow_DIvSO1Hmshb9B2Lx-CtpprFPn7dqOzZoLjt7vXUzCPbK9kkImPtZ67aAfJrlpc6t6D4_SH8rZEyK08yd1UR0kBQzeg4j9BDPcsz-NILC3gHZmJvO2emiAwVxmitB32kNu9Znie8Q5CKdaigHESiOFLi81fA2k1y94LGJyisWpp428CPqEGT8xzhgJdkVYSm3d6NS9CPtBccWkuTqdSk-OesJVzaNCAthzts0m5C6LwrrR5vn5zkGSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=OeE3rjTUmesm1VCnOlr90Hx3Z4OkzkbKZArfA17Q2rqeXjzqFlI8zQ1ugvSbXLT0e5AUOQygGE6QCGWnVfI2XQgcUdsxqow_DIvSO1Hmshb9B2Lx-CtpprFPn7dqOzZoLjt7vXUzCPbK9kkImPtZ67aAfJrlpc6t6D4_SH8rZEyK08yd1UR0kBQzeg4j9BDPcsz-NILC3gHZmJvO2emiAwVxmitB32kNu9Znie8Q5CKdaigHESiOFLi81fA2k1y94LGJyisWpp428CPqEGT8xzhgJdkVYSm3d6NS9CPtBccWkuTqdSk-OesJVzaNCAthzts0m5C6LwrrR5vn5zkGSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان، چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست. @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16373" target="_blank">📅 02:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKsugsIXU7OLMyRyJD5JAiH3sHGa2y88oAKfBRxxSqIfo81CyuW2n7BhIORgPWzPIpbzF271MYj0Psf-U8ry-KqsBw4uAkqKWnbvqbX4ctAfsvSKEFioNvODezlyJt-o1KLWb4fzLORnOs5AwF2VC_PNmpIqqhgUi9fih94iKXnMjb_AZZVhhm9qTtojLx8CUcsVo--lb0Q0SO3bB95bNja9kFKxZwie3XlLV07LDn9fmWcLzfLhbfRV06ClbomDjHnDoSJkwScJqVXTtCBeZBU_whQaFTCLidNmlL5WFa0jxwIcV2a9mplt3IL3yH24OhUCZ42AnXCB2fra-9AhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان تجمع و عزاداری شدید نیروی هوایی آمریکا برای عظما
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16372" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان،
چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16371" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leDjgfwO1t7LzIPndb5E7vmDpyIo9KwAASgQAd6HyJfJzN75-31au9Ygj45WQKjF9m2P-ch11iYpEKyF4aqiJYhZnmnyZReQ_k-Jz6m1kQMIjk-bt6td7UZHS5GuintWnVa-WLe7Du_yJ0UcYPEDMdd3AH3ZWX7HwF2iwBJvawnYM7tBTkvFjKi5OBzAw_kXbLh_vB_S4pO38KFtlcddNpqgr-DvTJ98Leg9vQLGkgdvQgeb8oSQFWmiqp-lGeCN7SlfbFjlRg3dwMILXup2V9Mxh6uVFE2VZuc2M38pIe-Wq-cMHB7hW015gzutbaIqL9bPQGiWR5TzDvX6G3EFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند. ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم. @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16370" target="_blank">📅 02:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=k2HPd4VP65szwyqK26lYyMKoIKX9IGI-qCdw1IEfXBu0sQJMNsqpZUcKpa_JO4B_jyjCIeTD9GCTcTTjPfP-eZmrh99ZiCOIkp-oWqaxsEsbJ_KrxONSiipeKOplWizNt2VdKRGyWYn9i6ovdczaiKvRXbboOuHaYQHa0ItjXJ96tVjAerOJE9tKf-DoPMNdBQuAvvOI8Zg5pNqo--REBkab_DGIv1VYHOkz-3moYKVuxY1e5anOohB9sQ-whDRL0dvodx67fr1LnAm4nkPTqkfZLpT5r4EQK6LrsA0H1y_OeYwFrYxcCK2RNk9Xc0WbBwkPP6U7tWLd1EioxQCQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=k2HPd4VP65szwyqK26lYyMKoIKX9IGI-qCdw1IEfXBu0sQJMNsqpZUcKpa_JO4B_jyjCIeTD9GCTcTTjPfP-eZmrh99ZiCOIkp-oWqaxsEsbJ_KrxONSiipeKOplWizNt2VdKRGyWYn9i6ovdczaiKvRXbboOuHaYQHa0ItjXJ96tVjAerOJE9tKf-DoPMNdBQuAvvOI8Zg5pNqo--REBkab_DGIv1VYHOkz-3moYKVuxY1e5anOohB9sQ-whDRL0dvodx67fr1LnAm4nkPTqkfZLpT5r4EQK6LrsA0H1y_OeYwFrYxcCK2RNk9Xc0WbBwkPP6U7tWLd1EioxQCQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16369" target="_blank">📅 01:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=jR_t-txqJA10qBFbC3wBbUtjbLYqe0QysDg56Gk17TyU79pfsmF78zP74F_eS8_o0LCqEwAtHUS_32n876We5QJoENkz-dsHkyr9ZykBPKAvVKNfTQvZwBc3q9LGx8IwX0HGkLWBR6UiS0_tcYGlpaihzHe2JnI-_wBcqZxMEvtQsNJSrph1bGUuCOc-CGqsXvuzHLoxDc5gg-8gwpeRdY_KPCL63nRq_U5Atsqw5zTE64E3DB6TeEBpkrf2SPb-iV95bL6ebqusrP8Do90jVjMtoLSKIQ-lrolvJj5r5sa3FKeCtIr-R4a2-XRbToIjuNyoXiQj8C2Dz-1_jJH3GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=jR_t-txqJA10qBFbC3wBbUtjbLYqe0QysDg56Gk17TyU79pfsmF78zP74F_eS8_o0LCqEwAtHUS_32n876We5QJoENkz-dsHkyr9ZykBPKAvVKNfTQvZwBc3q9LGx8IwX0HGkLWBR6UiS0_tcYGlpaihzHe2JnI-_wBcqZxMEvtQsNJSrph1bGUuCOc-CGqsXvuzHLoxDc5gg-8gwpeRdY_KPCL63nRq_U5Atsqw5zTE64E3DB6TeEBpkrf2SPb-iV95bL6ebqusrP8Do90jVjMtoLSKIQ-lrolvJj5r5sa3FKeCtIr-R4a2-XRbToIjuNyoXiQj8C2Dz-1_jJH3GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو قبل از خواب ببینید تا پستای قبلی جمهوری اسلامی رو بشوره ببره.
@withyashar
🌟</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16368" target="_blank">📅 01:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@withyashar
نسخه اصلی با زیرنویس انگلیسی و حجم کم تا بعد با زیرفارسی شو بزارم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16367" target="_blank">📅 00:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=infbnl0wBft7ZdFMgcy5h8YOpAMwNGxjlfFUwBtLNVr8vOaAUnGnPO1TO3wfC1kGfcWaWXjeDce8v67-OqQaFuf7LFnknZ2vhr7rmNNxlRRMvLWKmMRZMmZG6RkLcqQkUHEKifQRldow6mLHL6jc4TSSJD-dilguVHZqAsg_fwnXlhZD--vi2CHkDGTL0w_OKjrCltmKVUS6t7qMstO0qVrA_HY1bi4gbL0757bCeDWQHCU3Gzdr2tem4JwN3v3OeDYEUW_4neZnks6gypGXoq-xT-gQd0gSnnjJcx332aqByqgP86IQYFEXsil78a9h1TKMdfidRBuQUEYWgGaOGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=infbnl0wBft7ZdFMgcy5h8YOpAMwNGxjlfFUwBtLNVr8vOaAUnGnPO1TO3wfC1kGfcWaWXjeDce8v67-OqQaFuf7LFnknZ2vhr7rmNNxlRRMvLWKmMRZMmZG6RkLcqQkUHEKifQRldow6mLHL6jc4TSSJD-dilguVHZqAsg_fwnXlhZD--vi2CHkDGTL0w_OKjrCltmKVUS6t7qMstO0qVrA_HY1bi4gbL0757bCeDWQHCU3Gzdr2tem4JwN3v3OeDYEUW_4neZnks6gypGXoq-xT-gQd0gSnnjJcx332aqByqgP86IQYFEXsil78a9h1TKMdfidRBuQUEYWgGaOGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یک مداح حکومتی:
ترامپ رو هلیکوپترش غیرت داشت، اونوقت رهبر رو زدن هنوز خاکش نکردیم.
چرا راستش رو نمیگید هسته‌ای رو دادید رفت؟ چرا نمیگید هر روز لبنان رو میزنن ولی بازم کاری نمیکنید.
۱۰۰ میلیارد دلار طلب داریم، بعد برای ۱۲ میلیارد دلار مارو کشوندن پای میز مذاکره، تازه نصفشم گفتن ذرت و سویا میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16366" target="_blank">📅 00:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=Vcb7mAIpaS_yhb_8aS1P4_mfzkBWhSmvd1NGl_S_gxosfG73Ilr27ABroJ8A5Wv8eOi1_y2P5AGMAT79VIyhtHmmId1_Z1Pc9Ga-bSX9-9qPHGbkd7kidOuMyH47shMe6882lcJTTWyJvI17cbC_WqexrziVdcoSsVN6-T7gGTNXeVg6TsTIEquNh0jANz-jNmgMuyEu5qG72G3DQpIhiLg7FfR7V7ZF2qmV8B4NGAECL7Jh0M5wKGlrw8bliMn1TwUw3ILPiSqxSutL6V7ccbS-s46WwKLMacKg8LbSMx3DKWgkSGJjSSMBVe8EXG0MkjuO0l6VkA2itOmqIzlEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=Vcb7mAIpaS_yhb_8aS1P4_mfzkBWhSmvd1NGl_S_gxosfG73Ilr27ABroJ8A5Wv8eOi1_y2P5AGMAT79VIyhtHmmId1_Z1Pc9Ga-bSX9-9qPHGbkd7kidOuMyH47shMe6882lcJTTWyJvI17cbC_WqexrziVdcoSsVN6-T7gGTNXeVg6TsTIEquNh0jANz-jNmgMuyEu5qG72G3DQpIhiLg7FfR7V7ZF2qmV8B4NGAECL7Jh0M5wKGlrw8bliMn1TwUw3ILPiSqxSutL6V7ccbS-s46WwKLMacKg8LbSMx3DKWgkSGJjSSMBVe8EXG0MkjuO0l6VkA2itOmqIzlEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت
دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16365" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">لحظه ورود تابوت علی خامنه ای به مراسم
،
امشب در حسینیه عمام خمینی
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16364" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : خشک خشک ، از دیدن بشقاب پرنده بگیر تا نرم باز‌ کردن تنگه هرمز
💥
کارای اداری یادتون نره ! برام بنویسین چند وقته منو دنبال میکنید ببینیم ترمیناتور شدید یا نه
😁
⁩
https://www.instagram.com/reel/DaTbNq0x1Pf/?igsh=cmx6bXhnYXB6aTN5</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/16363" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/16362" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_wBrbJ-oD7UVhRoY49pP6x7LaRA1juXJkfGd0qriaMuY_CWqkkOj6f0LqvywxHu2-y6RWuBWNh0kN07ulwaOoRXHPCPJywEdwx9tR4K9S7JRaUmZUDXcsOeeNebCyBOJZJ-3fiX6iXYqaFMgTdnsRs0kKMumd5nzVuNZHSjsyFJZFrA_kdR1_sfz83aolqI9ZFDMyZjle6nBw_4qpDZW57OBv78YOTckcAqnmeGXEzesa1WzYb8qx39GCWpE3OdWIAShPOddaxCW2Hwsla7VzgU5IayiwEe5pfFXILOt2wgp-eaSAzIVEnkVNlz0jmjKE8s-13I3KmWyV1lCvbVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست جدید اتاق جنگ
💥
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/16361" target="_blank">📅 23:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مهران مدیری : با مرد ۳ هزار چهره که دارم میسازم باز به اوج برمیگردم
@withyashar
😐</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16360" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHD3MXisQitWdRvPx6EmaaALOej87NxMvnzgVzLAT4ghcQrFj7LV0TSsE-1Zk2incU-9dytHJI_YR2SAFir-pOn3jWkuYO7inyxQLSZ9-ObdxGd2UF053n6J48c2KeEx6RlIQafJreGhtynshbDdRYfYEGgLOznkZxf_Kd5zC6gxntSp9AWO7im0BH6i89y4VnEnXE3fnISnyj89roZtLmVRgI8DKRseJviicoiIzCNaBkwcnn-UR3BGA5E2z1sZJBBvAfHAGPbXjNKhK1G6MMxc8F3Bfh2vJn0ycfnVDn-bcKrQUYy7qQVqLj73s9cr14DNbseNIQq3haT628b5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های عبری در‌سالگرد ۱۰۰۰ روز پس از ۷ اکتبر : آنها بدون هیچ نشانه ای از حیات، در حالی که در آغوش یکدیگر در تخت خواب قرار داشتند، پیدا شدند. یک خانواده کامل که در تاریخ 7 اکتبر به قتل رسید.
ما آن را فراموش نخواهیم کرد و بخشش نخواهیم کرد.
💔
@withyashar
یاشار : اسرائیل درد مارو که ۱۸-۱۹ و کل این ۴۷ سال کشیدیم با تمام وجود درک میکنه و اینارو ول نمیکنه خواهید دید!</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16359" target="_blank">📅 22:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند. @withyashar…</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16358" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16357" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16356" target="_blank">📅 22:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRwhoBWnYxU-MZ0lW3Gw_TE_smj2G6GeDlpxKnzf1Mz6-hgJXjBlDI-sRMIgtktigTSOFKtFfehuoSMFTv6masODyzIKMBGofe1AJAQy2IIvOjKfLwrXN3CohKe9qjem0Qch9gCmLe72AERdT919c-5BZqza4Ps_9feaOHUfot5MAq4qzkFHwYMKnsYNluw7ZwGzPtPgEFXTSzEI2dz7Co2mdA7mOi5CMjI0Kl3U4-wK-9-49myooT4yQir5rw8eA14-XJNDg81RSHZmV8qyO-DkNAFdYe8lW7E2t-pzY8O50Zjcs5rP_7Nr88fJTFLKcWRaAL_yY_Uj3X7eJtoYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید.
@withyashar
بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/16355" target="_blank">📅 22:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ii2uEdrj9CjcliFJjpENOwmWLXgKZJ_rLcTQe_a8S4aFObQjcQ-kxbIxeRV700-afMgemHZ12p9Sw4elGoBsO49jHSaU53uG1W_75AceQ8xMVCj_QOBeyzzHPUpKzjvv-BKFreEf-Dqb62dU6_t0vAnbkOnkvd88_rjZShjvUiBmqyCl-_vnOFP5kfMc3eUbHEDcp2W9-Vm2Uh67UKFM2ulkNc0OGCB67YACLsJ8yGKJ4WBCK7Iz8vsoI8Utbjpq7326ajm9eWaVw5kQAVdMvhF_dYC2mmQ76YH7wU8Pf5ChDxcWhTsen7x6F0Sxrpnn2YwZxcnrGCi8-Wp7h3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام صفحه مجتبی هم اکنون
من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود.|  ۲۱/اسفند/۱۴۰۴
@withyashar
دروغ نمیگه تو اون دنیا بدش دیدن همو</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/16354" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16353" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=r7FqosaCDGTogjzLx252h53mOWbaLmAVs81y4-_WMpD918gOXdbPTuXY1KhGrXaENK-ubfbUPmSUtwbwHGgWorzuK0Lp0WptGYVFjUHhqBAxqt9ZzKR8kXAxe6hoyuarlXvzqqwkSenjqZ0at4slTY98k0-YhNpacIdNjMXz6BlWik1H5-bM0njtZcT4fnqhus_5ujb0-YR2zeVxBuDy2LUVKgLNIJj5CxAN2WCtQABdiUvY-llnU2p2S8ZSPBspV5QkSmYE8RsYD0nDlGnxw4MT9Kdzn34I3sW9KL8_5wnQsJTf9TyhyLKz48_U1tcszPWqyr7CTpwupCbgQZFV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=r7FqosaCDGTogjzLx252h53mOWbaLmAVs81y4-_WMpD918gOXdbPTuXY1KhGrXaENK-ubfbUPmSUtwbwHGgWorzuK0Lp0WptGYVFjUHhqBAxqt9ZzKR8kXAxe6hoyuarlXvzqqwkSenjqZ0at4slTY98k0-YhNpacIdNjMXz6BlWik1H5-bM0njtZcT4fnqhus_5ujb0-YR2zeVxBuDy2LUVKgLNIJj5CxAN2WCtQABdiUvY-llnU2p2S8ZSPBspV5QkSmYE8RsYD0nDlGnxw4MT9Kdzn34I3sW9KL8_5wnQsJTf9TyhyLKz48_U1tcszPWqyr7CTpwupCbgQZFV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه 14 اسرائیل قراره سه‌شنبه و چهارشنبه، 16 و 17 تیر مصاحبه ای که با جاسوس های موساد و شاباک تو سپاه کرده پخش کنه
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/16352" target="_blank">📅 20:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.  https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080  ترجمه : آقای رئیس‌جمهور،  بسیاری از ایرانیان…</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16351" target="_blank">📅 20:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نماینده آمریکا در شورای امنیت: اجازه نخواهیم داد هیچ عوارضی بر تنگه هرمز تحمیل شود
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16350" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uc6KPCmzUeo4otB_q-Hkj1Zgb0B_QGf7Ci8uOw8doiqz-L3-OogGHZjCfoJ5mPNS8Az9K2gJKdK-KRkXkLrE0EBE8jySPPFsSlqr08NyNhlsi74nynEyaR4PAXASzIlLDx6LTkTfZsmDlBCkuckUi_Py1HvD7St5RhaHCCtfGLzc9JyLm_tFUvyIlsbLCtvbvrZb1R77fj5XffyFVHNsprlCuVQ_eGwooRj0_0w87fvQh-d5EsBad3jY9bgsGU54sufGGuAHMf5I0Ek7DX0FGNoJLNKpPWHITtTTLIPyUSNUhkPw9Y3I_bTrIgz3fi65toldsq49MxoWGjo5cFCcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد. @withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16349" target="_blank">📅 19:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ4BYuRDLoG3WYjNvkCJSvyjvtOVIqz787tyUCzhagZh28Un2sZfOUZzKxNHPEZR_Ker0kz_bMKxbmnvMID8Khor1d8gf5Lp-HOWI6_vg2JFv6eN_KbdmYS_a-n9ZWdz6vMRi6Yv3v9e5-ixq8IIT_RAhY8A83NE5yhhnW4FXV2ZEcTvRknZXH6fhoAQA4wGlu6sbwAl_ECBacK0dPa7sIbAGCEpy0w9qOHusRD8PFwsBymlb76hJKEwO_jABRqD3G30TZl-KjrXIOA4txImBw4kahsbQKwB-sk8O8PyCXkryjfZOJr22wA11fVUqHteJr2LxEnwTHcf0t97xQnltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16348" target="_blank">📅 19:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/16347" target="_blank">📅 19:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده به جمهوری اسلامی گفته است ما بخشی از وجوه مسدود شده را آزاد خواهیم کرد، اگر شما از دریافت عوارض در تنگه هرمز صرف نظر کنید. در حال حاضر، تهران این پیشنهاد را رد کرده است
﻿
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16346" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش ها از استقرار گسترده نیروهای پیاده نظام و توپخانه ایران در مرز با اقلیم کردستان، عراق.
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16345" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش درگیری در مهاباد @withyashar
🚨</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16344" target="_blank">📅 18:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جان‌باختن شش عضو تشکیلات مخفی حزب دموکرات در کمین سپاه پاسداران در پیرانشهر
بر اساس بیانیه منتشرشده از سوی حدکا، این درگیری در ساعات پایانی شب چهارشنبه ۱۰ تیرماه ۱۴۰۵، در حوالی روستای قزقپان، در سه کیلومتری پیرانشهر رخ داده است. این نیروها هنگام انجام یک مأموریت تشکیلاتی و سیاسی، در کمین برنامه‌ریزی‌شده و سنگین نیروهای سپاه پاسداران قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16343" target="_blank">📅 18:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پزشکیان: کشته شدن علی خامنه ای آغاز فصلی نوین در جمهوری اسلامی است
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/16342" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش درگیری در مهاباد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16341" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">این ادعا که «سرکرده حزب دموکرات کردستان به آمریکا گفته در صورت حمله به ایران، ارومیه و آذربایجان غربی به ما داده شود» کاملاً بی‌اساس و فاقد هرگونه منبع معتبر و فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16340" target="_blank">📅 18:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">روزنامه بریتانیایی ایندیپندنت : لطف‌الله کاظم افراسیابی شهروند ایرانی-آمریکایی مقیم ماساچوست ، استاد سابق علوم سیاسی که در جریان تبادل زندانیان میان ایران و آمریکا مورد عفو قرار گرفته بود
به دلیل رد شدن گل ایران در جام جهانی شکایت ۱ میلیارد دلاری علیه فیفا طرح کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16339" target="_blank">📅 18:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16338" target="_blank">📅 17:21 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
