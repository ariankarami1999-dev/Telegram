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
<img src="https://cdn4.telesco.pe/file/eAMM251mj5LMAALZBfm-wmOw5is_4zCHZ1PNoWF-c-vVXgcL7FJK2TqZsp3wldmUyXvwNe9fHe667qRniCRH0Ns69WmXEz68RSt0tlg85qSFf0InW7UAs_HNIBHijI4QUZND3Ge12EGgrnzoPyRKoqyuFmQlfb4xNXwsBnO6CPi_BaWB8IIgAJ_S9amNxPRajwh746A5l1ytvsgf0CQ55t_wq5XoMAzFP1MOPWOQYjOeaKVr8H6yyImwF-60byhiYU2M2sRUECAZp0LjoaUZFYVdQNwosPnnbDja3u1yOtN3BQYxaxQfF5HAwYIJTD-RvsaXUayztZfjB5i3wn8Qig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 23:13:55</div>
<hr>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRSRmuqrKlK5E5sN_Y797B5Pn0Gs64b5mI4OrpsCTsjmWGCc5qdiIeADWFbbyi9F0gIjBAcsNUn8oMrGRRxjoztBaySOy_73l75a7S3rN0ZWlve5tS1Y88_Ja0-LjWKZyT9hYB5keI1Cva_KVa3FfDQHOBPZThBSM0yytcr64J1IJzUPXfcvMpa_PG5whQkhVwMDK2Q7_GX3hoRl-T9kur1D-sE2BHMhT6NEvo3zJnMuxgCwZhJE62t6jYhFRGlMxbat3ZSSpiFaAnIOOQj2wD8xlHcFLRZT0pGZFhituN2JY20grYSn2iHvOADwBQZYQ9aB6f5vpP2FkT6kYbbFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWvSRcCICRiskRIHH_E3LOUgTAvhTNZyT_9hyiW8t1x6rPD_4UsOgAfdSs_U3jtoQkQHvQPzR7EDb47mrJcftCo3t-IZsLUTWvVVueIM4h0BsRNbibImzsaw-RUK8dClQVA2-KnLhuivcStFleJVNo5QT51heNhkBPKzu_z2O9enngJC1pJR5RlEPVxn4-geqAJLOnnth5tMwgW8oJmEfue9Tiwm5UMe7Q6ChuwX222luNOHuWNhpq0Z4Fng0FrIQnzbZkQHLxJ8Y2sojyf0efIxXm3_2g0GVeQCNvMfpl3IVoYTsN5d3oYVfajW7ti8W1h1M0RJJyPxfwotnymOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXOBGBkOXNA5VaaRiQj8REq_B98Dz-bTnicnvw3jr6BiguV1QNzpcuy98KiFg6Q60114ezuBVHwKk-9QxrC5lSf-dn8h4-YDvqcZOve3lmbN8G8kTm1_ntqtZBW-3DPqSmG_CHFIKoDQxF6TPVG3KQC6iwH4uw8OrmzXre74D03jPkm6bI9DEx-tLmeYWZmjnE91BXvdRr87ikXUDVe0zeoalsi9eGEl9kuP7R6LeeFh9vYy-RKLx-GXsmU42VZ-NssRmg_Q2zM2wn2RZYxi35200MuBZsPKa-4cvkBDE46tmFbWekuOlIS7e5QijGROaUyRMnmdg-I8W3_Zg91n7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJGalCUD8dQ8Eo39gyQQNaLEgyWykLhrhsk23sfNpv-1L4ytPORwgxZMRucHomfyokENOW1CiL-B8q9VoRNw2Y1Im2Xu9ty2WwXXPUObNy6xscZ5osbjUmWuG-AIZVn7VkE1lkts8JBxBYXo5eNviW8smDcrjB5wnIEwQS1kT_EWvWN_IecC5djEfQKY-lyNTW_VqP9P3upeDxQzt4GajpZSEwreRONUz5yFafcDOEBi_B40723wUTlrCexyM4KPHiEDNHWatQWpyv9l-FUHC6DAGkJNf64WcOcr6DXBBj95UB1X2o1GkSAlSlVri9uYnDWpy2f1xWb-5RIFLV4Zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsjCYlvdTcIJd8bPpmthLRiVHKd8jYdLZrvNaHlyxRBXurMNCS2xkzXP8xT917CyC39zBIfWRLCmG8C7PiFxMOXgcxz5imp-R-Krh9oexDiQPcjweH2xfZy2C96MOaLkmPPoe-dB96Y2GKvFnLmVy4aauamDwxPvSW1LTtcK-ecyW4eiWjGUXJYIR9HllDiEWd_26sDB-e85x4mHqjgwSeGnKT7MjIn5iA2F_cMnssO-Jw8KqylgLNrnPGcPsLAFKCB0ConxUy5tlVWfeAJ5YCYaPGqKnnaiX9jHQMw_CxZBGiHHVScqQqpOBTmtIfxEVZGSuMvDsVtgdJqHHwurKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSiJHjTOy5GxfFw7O7zNRNZ1H656WL6mfBGBwUTcg5QZqu6FrI55YngdxTTm2J6YibzsqRC2BgT7I2iXB4vphHNA9VbzOr9l9JbWW_P2bpCJZFnl5Vb-4D4OunV4bF6WXLfLxahXKrK1Frn-UPgrAYIysGXRvzjLVMhLiFmUOnDYTU8_UjVdFgkgkWLeGMWOAL9vFsG0_qgyOvhYzsE_NHrHGYB_PFOLOxf3s6CzoWRGAbEM2vmq3U0zKX6EcXDIgOXXd3h0FRA4B_XO7gAMeptZHdspnt7cOyj9oky4tnE4rnSkTlT2i3VIkjmArXGfMSCSLc_yRZ-VHx_qtCMsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEXEEVADXqmquCQ_Wg-jKgCkJF_OvfcsKq7PSjhBXf5dFy0JR-2vr6pS9sYkX4byCvaYRu3pgwfFEe42o_J_jMmUzsLInGSl-APFqu0080FI27A5mDnHhWxEI2rMGfRFIfgYvP-BYuIs6erBnfno2R09ivdhrojCoviUCpDZ9Uaz73PoL9gXk6CpXcjyHbuFmmDP1MZ6wXlSNe29M5jrKLhtKy_WhfoBOutrVG35H8thW7p0YQgyePDoy9pFiYmezckyW-MM5TB-CXU_XZSfvcGYKbVAWl73vfiuLKoBEFUnv7kk2RJXev72bkMXooxIzXZRdmcqspW6kZRE1jUq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY7IlKPtSdQNmr_J9trOT__ZqZvFa54XR453mFz7HEE2FWOExq7uQOsW3OTYU9dEOP34o6OM-1ZCAYsoaOZu7Ew2KqFBqwgA4eYpSCHTA9-WyG40bLPPhY-tYXdNIzbb8-xGdx6h1hvCFRCxf3vU13HNS8QLQfhnnPwg6ceH0rWl4V70IjtsN0UJQ9X8w1jz7A0mnQpVgD2L_qx6o3jw0jlTxOb4k1tD1XFnJjz5EuRBRcM51h5WWC3xs0apMEBPdpWIScrJRzBqAPXA-ELA51L9taamX1VuBlb4r-pEbW9uzm4xgMAMDsR4dmGexpHL4yakKjaNlbLWXkxoN7KDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D01OmTvvurkuwYCpvZQPbOb_Te7yJ1ytlda0HOa6PJUqzoQqdQQypl9ITAD8J8X_TFi9s6KAmrFtT5kvQZquf132ZJWXTnpckm9HM_UhegQMfmmGx_roIvnn3ZD3akX9EhIZ2Mlj_TcdHnLJ8QlbHxVWVxesXBrYYNys1uylAR1EmFe9ettmwoVFwAvccmL9YkFB1MVgm2nnQbzvybwuUnQJV89KJa1uoNmm_idv_iAb_sCAIWS0AZuELejs0lOsIAd7OMuZVMSeUlP7wRJY81HR8pI2a4ymFzLZLrOviV_ZNYC1KBnbcRXWXOnEJZs4VxKLnGtLNwb9K0CqzAZT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlgsVPOew2D8smBbRzNvSFqLo-gmYL6U8Q4C0rMGLJ36YHVLjSaCVBsatkTPRsBy1OvuRqzmcJiDsRsvTjnSC56xLtM9_vCZXiKQyiu_e9IvAR15LAMzerTK9MvsVcYMbN43_WaZjZZEa6NQYTk_PR1aN1ZJepcOe2zelVy1Y_QTPMehpv_ICOV0nTOldjJcjQLZW34LPudWbQNq3c9sId1CcsGDO9easfhsZLgBmylCHYz5qGJRcrviGAeis3TbCDM6HK9R9_KufvDj9hBUDhkBm88ULDr3Dh_BMnuxXQJ_KMkLiF9LmNxRDLyeirWya-TlWpDJai9i_kE3uEl0lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OY8s2DwI6iyJsKFMbUe26xN5nQKUm-ZCyhjqY0jQlHO-NjJzcxYlyyaP_rP3c031tFCIY4dRWq3O8p3WPTrEwWeH2vUxOFvKWjGyHAY063bRGrwIjGSamAApJ--_zccqQ74aGSNV81IB5sre_B7CFaVji5bdoGT30oOYJjVlXAmpJSYZWcTDxaYVqRWIPTZu-DSCICkeiISTFxpZthf-dJVlS_GXIzQO-X6PsyN-KHkzcuxsE3QhxDQFy-iLB8anyYAyGcu1b_foO54c49B2NP11ZxwVQOGdrqI5rYpNnvO8bS-xDA4OJyHboPKQ1I23awlNue_I9fqWgvjGuQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4yGZSslhzedIsa-94Jf3CHIvtXnaG8EZMTRkAj2tp2j_CS5bwpXSe8_I5vA9NE8Jb7ELPnsTtj1l3HwpOpOFRCvqpWrJUxk6h-GveOWMOKItlgkunKJFFdGIU_QiXSAAQJK9vwyxjpaXedwKRLjFgIRVyXdEhnZCY8DaLYkTOCbR1GLxrs6rs9vDmfBdLLOUNAzRw8nfh2wVwyLwUqGC_4ivhl5dAJsLyKKonlvf_3vn0VCx2ZXJN7NNHiKjgrkoJsvB1wST5NSDMl3P5itbFMl4EKZ4hJX4pMo3hHYV84BK6APVSL_EfWB2gKZHhJlyeIlR0PdlhuejI5Bh1R--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDfjRQ5rSZ58Nq4qLb9oytctivx37WM9Vpn3QIOaUZ2QcXpiDh9ZBqJwpxXgZz43MTht-SgoFkoTHMFBJVjuS-Q0nCSrjJ1SiqcbqM7usESJ3LuVnyNq5TO5dVwtv4jbArAjlcTyS10p8cbtWSjNV5ME8Gc9SIp72UBg-y3acxdXQ1NW6kTHdH4_0Zp3Djky0hJbHNOZ4s5tX_oh1k00bkUsr5X6eEF_oeIYVEEcI8pmv5alk1s7mnoao2rIGFWgePq-RtQlcQdwARI00D7DcUmjmfiXkQmb5MUlvCGkhPHKE6NIrtlq2TSTb27q6qYsacykrSDJnZozQhh2VU8lZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SldhEvyIPDVjBPERRH-XJyvo8_EKt7XeNVF8HqIIsNJgae0VnH3nSRxncpzDPcNnBjVS4iI4p1xlhYLwjVLXOsn3tUkvIPzKrUvcpLpqL16fnI9RCB06XGwy6rpkdrkNWm91nMgmtFvnjOHkA2rQr4KdYaeRMMch8v9gzFTIXqwXd7ghonO3QbKQsIOlP3Jn97uh8AA9S5IpzdBVZ_e1pOw6Z2rIZZjSXnZtzCEbmbWzId7ih_AdRQ78XnC9JvduH4kvik549LtUuc_0YBXs9FWXcnVCEQlCFfhczNJspk246XFtMBjTvVp-crYHnX7QKLxZy3s8jQWL5eEI4DHOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9KOxamd6ISM6tGWs_lbCZ-lu74MQZULsLjehbQd054l5DAQO_Vp1XmzZPFFqfKOum6z3M2XaS02lXGQj4zq7u9fS5YBhiixbUtvzZAz277j2DBXoaAnr-3jqnIPeK8xlpHX2bdQh9cFQTk0299p_9hHo2OSXN7W0iS1g347IYNu2SJkxIG320hdNahMHOg3p26pnShSkS6BLU-opoFmg9xynkoqcjxtp4F9ZYgqKTFmr7kLXlGONO1CFgLuri4mGWlju_eR7j_2MY00VbpLb_NwJWdLqlO0uK-enbPoATNdzlcDorOdlwaa4vZkH9SX7wr4HrRBhzto-mwTFhVQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjeS2Dk0uuMutyUYK9HL-9e6ieaqCywlM7dnNDoF4zhMmeKLD2qIECx9v4AGjkmMPK62BdW9cQRYleD3XDST76cdZwdITK1MMpFCQk-R-6ZYQvn8NBcsUDVgm_a-HcbOiD_wUMZMG_QauP0NRNOszVzzQqi4uqoNENFmqbe4OuUTWsYax4X7ZwXjf9lqMfWaZWMWmtTp67SAf4R0p0Yw7U9NLctXGD0tkMh_3KvPbuWuFoK3HgPOwa7e-lE2BMv1gudcgURCGquano7mFsAv0TBdS8oSpRq1jsL9VY8j7wmM2uA_bFAQ4mFypjk68-ftsGrjzN3Ggy1q1qsfQQ_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBfNwwWchQVLp9ccFmTh5sj-n4FNMUryzoRTEb0WMn6rm-Kmjg8auEhJdFn6-_Z_rOCpGpk3WT89-UY9511y-SAN1M7wA2faGyKa9wC6nxLfW733jAOFo_xT10opoYRqaJI9VLVsXQLjfsO9w4w54j0awC3uMD8vMamZc4B5byw44qm8DyQm4B9516_S5lpfB_UaI7MMkAEf42gpQdDP1bE9hZDSSTJWpCVpv9B_-R5UKUqfRQFOkAoEhszj_3DZN9TAWy_0ms1CD55ZkLQwphlrBOoSG90XKwkjK5KzwgcBAmIONsY6ImFxWdVzHuqqPQB4Y9Rk2LTOLQXRP_dHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8dSMgq7bvHi4fUu_8KOfajXjY70OYKxOojRC5ObcriY4wGAbUf3jYaO-mWiDGTxd3Om_iphAc1k1vIsGcQQZwLcbzBS1iZYOy_nAZP8i48oi93fx3MPSYXL65vhb3txdRXV0_Js7NeRUnZrvV9oZxjCH0ktjcZGJErqRHSRDYsvrya2RSUhmvZDQuumkWiMY30FV0niwgE04Vd9CXrbluRtWP5-4s9JFtx-dIgZv1Gu4poOKhPym0vVqOmWcSv0I1pK32Hm2llnenQWcONKX36GW4RQdWaUWkUG3EFFRiKYN0xXpU7X2wJqOxy39o8njP6nf3FUiKJqGX7IEaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyARmuUmnRPduzk82QjwF5ZuepkbW_veqmdwgJLUyqxLbt9Y0thpkqoWJd3bwN3BF_NY_NCgNE2j9FbFgeXfQcZma-MlpUS3tDhT__ExqP9IRnDMYR_tVNO4bhhrT8nsE6-7Hgkm_BHhyWG10BFdkU7pBkvXIvBmDoRsBAmRCsJoaqTwVHnRg2rNbiwitYy1HZqFj5bXfz-O2gwfJpgZ0sbQTZfXS6nxmfIfz-ZbaZEw-fuhgOdHMqevqhp90rFL9NYTAe-UkpbmjCkbATv4YgE50MryS6pGjQZloXOBfbjafMXR2cNNe_Cy8JTrsA-k59Q-yQxMY1rhxvO0IGe1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQi5g2en-5YeMIbJupz-d8r2bqeYEenNHRQqHxowg36bzIeSqylqONBrRci9p1x5iO6XFL_U2cY4YNI1gaDYTPiLRxd117lW3qlmkbDmrbXr4jxy3hyosHN770_f7iKc_61AD7G1J5igQs3yS9vw9lf5enTDtINw8Inbw3ZKKXSTV5Odm_aOyT7ee4YHGk8p5EJwUIGeaj5m3tgU6jkd4FrApdO8PX4qqzxjDjAPtBeyF7UNCN11hgTOo-q_RTcaW2xIQYUd_c36s5obJpkiFv1mpJLt7cQ1GZO4-nKCUAk2EXYenRlhr_HxtB3nO4w7B-BMejLpzakfrKOJe6d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_lA-Zn5sqV7IYcfwB4TdaN3Ozx7AuJ1ArcG2UkRwGHjoN4t_ZgR0nVyGp8Se8hQAEBW2AuZ2nfWqiEeL7u8uBG3WCjMVOEg2tq1oNip85BymObDsKKCKyCQCIMTVqBfsUR9--CT9MTI7OntHu8pFHf1z6egfn16DAotCq4HNL21H0HOJ9zk1AiAVuGCn2XiztCktIakkmufCiSwkXAIQ_hM-9vyaE2BMZNbXj1G8-ewhAouzIu23vQbq0CuC-Yr3c12fhq9igyXcnubcT9Fk_sNOB-VHhrSca26miLwDxIHJYEhbWpkMuk2Kz3v3htQIDpZ-EaHycCtuIZA3WJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7lFCTDZGn1AlS5287jxg69w5vaM2gySPSuwQ9-JIp3-JVpy41GQ8xhX7r6HzM3oWFiGxJfh3lududPyckgotr4A5lnMxLabrjzA40azcp16mLCw8B4yoxqf3dD5mZZD0ul2uY1hR3cIb32XvRrMMG9jkrWVpaVfVvIixnF9VJ-Uo6btSXeyUEdj0UnKZ7ssM84X7TmtrPANXdZS_MUNT8eQqkXr62ALUq4k17wtvh3enH2R8cRhHNwaaJzhFUaqCTOvG91t2Z6gFPBqrlvQFciVEtp6JVkgIhFqzZmthsgwTp2iv3C43MBKrpMh6Nt2waOlVDPSMYV77ccMqBHO3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCjbZIiJq4XKSdJtN9nYP_V8DxKQw0DYSyCQ_wdEZDB-BocfCnkjPuZbbcWFNolOH_FNJv0jnRCCmQAIPpeM2i3olmOrSi9KdzWrnKgZqYkvdDkIE-FXgC-qtYQmre_43ik7WmbCGP84mn1NXEcKa0apq36zAkZmKKVqrTWabWk7GrSE-MIZWg41t9m0wLDCViuNuHguuWPJiLohSFMgNw4UwWr03oMzAjgZ_GuKhdQmVMaMbjJSN2_8ZOxUk4fG5lDrq2b7r1hzmjFSIs3MT31_W387JqLSTFF14noXtpUY6CMKS3_4VhJNN8OZz6BULvxDmFZB536DDtjWblGMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_2ZACWubCK1ABG6YSO6C3kIJ6Z7UBHl9K_1zYk_fwJD0a3cAP3RE6INdyTAwHtWhEbk2tHRWQdQlSBdv25XNAqbi5Wv6cfc9hqRpGYxLlkWC5XUOmAzxWbuzez9_jSu5AN4lsJ-6o1CiognjLEg1k24x0mXjaPAS8tLTfkTSa7FysncPcpahpS6SFJAuJWLZ-TWU0ISVLWt-GAX-oPY5HmPSdOzptMu6SE-fdVFtTVmHfAhoKTVoL9Z9VoWTDYWYuic8S3OY4lcL9B4k0i2WB4qVc6yPqrWfly-u_CBJ776cQZNc7xw7aDq2oDP8OinQ07aiGu5p_7_40A_q2xkzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUw2drwT1RHECqMbQ2Or5zKiCcU9uaDetsYTkIgNF6CCPmF3dwIUEIbD5p4uZYa2ILZZlk3_rgyOofn_-G6hOv7gVEgYrLd1ljq4mxy9ahrQzuFqK040T2zs5wmrDhS3IxipjNRGE_TYxPJ58CqxuG5f33cZXlAfMAgzEykfuhxSjejEHCl5zUA0TkF5OESEwymaSovcLobaG1Pasbp7YjGp3vv0bGlMSc_dDxEp_OF6krgpYIwvegc2VX-prCD8TKPa8mOLXOij7DioAuCqWr3p9Au_jRihb9-ntKnS_NDNSz5fABZknRN0MEimFaaSkhUXH67FnvN_Pi-jwJZyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29030">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVvqGIyPNYXVfiOnU04ujdH0sSkNnxrwc4TAko8YL49vGLDLbn30ns8T6uLjts76CULWZ95fASCjBAZLZ_JsNIHVt6mflPh8dGCBHNQxAV2vyVX0THXcmHPIL-ggR6EDVycyB7clDTxvWzKAqnhQROxz5aFCYeJm8ZttHOum6B0O1DAzHNtPPPS0NGUA7HRqTwqsJhtY9BWF73S54mq5su5V0KiUS5q5Rh2aI1TdBJpxDRtyoUD4yJXleAOvafN1bHAp_xJ0Q6F802Vp_HaUcQVl23SNeh6wJORYkvWLRUbD97RBuwV2wPKikgxITPpsHC67VuvMaFFSnIR8bPkZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته ششم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29030" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmoHw41y142BNqCAhoVPPjvYldqtuXYlN9sg9tKsrpfM6xNV1JsKOdvHc9kpYNFkTWtT-q4dSz6JDTnTQBhKu_w3Rp-BO9mHbYQr_bGdKz78yDY_dM02vPlnKWh89wL1IByVnYktDMdcrJqIyKfRR_1RYKTqtKtvlcz_CIB1O0-lVZEyPM-BVyKI7AJ45Y65z7akAiochmbYvlMRmA20jAa2AGTewhweyrkJHq5knd_Rh33nIzubytc-9TtXXP4197mpk0Ve6cgFe7PRU5wrsK_gxqJKrVUa7fSlppSRaU-pY7jGdLLHG0q5JD1yrwwtOMA2UwWV1DENGGrTKDzMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4wF2lm610y1IqhHx7EGxOPSp-JQXXTP-kjhV9itZa0YT3ku2eHnRJRNZAd31d-rU-S66-IzCY404EHbZ70KBOReHvMfqOKyfvYSBO1fwe88CI_KBXWOHPHcq6r7yM-YdqTm5-YanwqpjbwOVUvSUCWvS9Wzn3ZQFaG_TAVp5tfPsajn20dhtBdwsIOGN7Npa-9PPnsHNqG8yOgb763b5WBm94vFXhVA13zlnBnvHR92ZnJfS2t5sZRhGIpD0KY4qG6wtLxdmQBEsMHbErukaE0G5Kq3g7W7iu1Bq469vxmRgXx39NDeD_1HYbuLcMUoOEvSO7WTdde5i29AnA6V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYG8SaSODOFWKM3pXOfgxoi6UF7xFoOxhT6boMbfaApzMAZZmY5BqTeybsXHLyQa6-ve4KeXdqwLgFgq_TlRaHt0bEocE6PvK660EHKTKdk4_pdd1OWg-qpMQsqn1oEgL5aXt2PuW0TL1t7n1BiYmM-KmUVuz3HIBSCW6LHVXsqvNZVWGQh2OGYc0rwy8en1Yp2QYLem93ZE1WT51MsigQZ_7iT9ysZc6HhrnqcyHrj5rQV_qYz_Z5eKiwkNfE1KmBvhZ939ZscUm3gjQU-cdpiy_CCnMKwCCQB53NYNJowbI64wD4ykFNA4RlRcEQO-gDRwa9gKh1EZtAS1bfAkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJAEah9fswP1bysHox6BWzVIHf2F1rzTUQAO42IwJWNASNrngo2RsLAhWvHWyZHfMLB8o8E9aVOr6SAJ5w1fq2QaqzYv8RuUPXPwBh_RI6oyUI6xCipAVTbFvQVTT-N9UDFyqX7XgG237ERPtkE_PNs8iWiZGEQWvGd5QCKWeIraS-og0j4oKyo_ivbS52q69keCkecMeycI7zKogXDdeSfoE0IYq7FWv-6kxjnXEMMiAYpBsYBdwlMRESrxmA-QMHGqA6m5nFAwaAwpI_WxC5piK_embVRNcF2T0t7uNIt1_UwUG_EOd9LKqG5a3ETqDXJ8nrTqHYQyb8IsSs3fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvSbFG-j0j5oDPLb_7qfQApLHbkH2QWDMvOQlvH1oAW4Kvt0aRmfhxit2Z7637vzcY8bL92SYrBy3yx-z1ruC-SnYyLRcWX1D6DWn_lRJ5KIxIYu4n1HtUiMn2RDttjFNI7GytHZDE05p-kjoAFJATnnqGVHAtwbBx8gZvVJMuOczxsCcWutxqmH1IW8mjNV7QJYuWWFD1q3naLUPJ0cmY1xqgoHSUFnOua3akB0RB5--eWMfq88NgrMdeT50PiEZqOhepTJ7hBijbGBtlOkNeZASNENFjz9YGY2GlGLH44CePjvO7Wt8IpNZ1C12zO9ImyNUf3LDEBs-QlejF7TOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIQfkx1ahLY1C9x0AgRbgi9pHY2GG5_6ywVGf05lqt6Z5c5PE0IYT3Q4PZ508gfj8ClG90HqjBdP3cIkjIRF_F2UCZCfzNaBjnYGt0B7P2wG_pP0uQMNH7DkR9CPJO-xuMAppDflRh5gzQ16K1mj7UyueXknWHJWutndyBpAFyzHemZG7jagkhDQxOLbVlnYEU2XQngUcrgCLZBOk-zMz3SiDpDAfbuTciDlO7jRu5odLUtjLuoIC6cGbAeW7--sv0OsgF05OmgLLzA4kCLC_ryriHoJhJUCPGIqsGmLk57p7mcvtNzmJzg-JZXGKCD3rtkUvAuuk0r7xtgAcqhrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0wctuF_4BLobvE3nYgFyYui8RTSB3SHGbI-XzrvkGcDpXKy2rsj0OaYTkZyLSPMLhH-n22DX3LBGYRfcW6kh0dLT2Kil39CGd-LK-b0NLUJT6x4_YB_YD4B-WGLbsZYI9qNEbbiUkrbKKvh3TmEFFqEgN37gaXb4YhK2RLKOfI_UioeeIHhCwNYdXaW_kEKsgYf3T6htSlwBYdp-WfV31FknUNfbthF-cwM_ebons4sXBJyQ33zfc9Kty0paf_MNrsLBQLiHgfm8zXonfZtIzs52JE49GtkfEmZb0tf9YkmcPDx1gKu1JKFLQCI7blmJqwAe5khRWVcnaY77cQNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc_NnBwKd1xSUrbA2-e3r4IZDyu4mhZgIi755l_MyihcbUO8xFsEBSdWixnqmIJkhMsXlg6EBg3mqFMTxuD-L2KFrrQGq9YcLKKPxQbQ4N8hJZXs3-Qj1jhy7B_DvNAkAQfOcsSSeVqphHvWm1yG87Wnjcc7hNOYY67ROZsaag86WBWdVLK217_KzB6vcsRgVu_zLiM6PqnA0L_Mbq9H1bcCmzBCHoN36uw0VOVDCmBI-6OcWrUcj61-gjAhVnFZO_yNlRfgssiQZfQeE4g5_zmErUTZ8o5tM6Cz6iD8gcEx7NLxYFhDQ058SHQkGPqOubsxliH5F20HIACKlEYOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFGtQMBGSea0mPE520BNUsr0f1D-DJiKesQbH7oeSgsKiOlhUr4RcOpPqEfKqi1-Qcf-ra88PTBUDJK718J8H0OMt3EJcOn-2x_SkmEojFushOLJPKytdbTKaKK2TzlpL8Qs_uzGgt9Kg4z2YvVRLXgO3UqyfUF-GjbTjx-4vj3x68Q1VYyjG6EJAmyyhGtg3YFYD3N8etmcI4utFR3Ao6t2ExTsQEiVbIfhKSdsRB-NWFNal_zCwdPxL66YMrKhp2ZD8g_f-XXM90oaVfHcqewXT6ChOlMyKIw3HqQIUxppXrJRq1qht750Flt4BdrhvNv8D3yZtJgdoAWGQKQTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCsbln9JZljuriC1fvGJ5e9leZeAfE23abaJq5imW1wAr5Iu3R8PwQkF-ng3PtM_g90XwXOMbzvkSQ4QK-1ViaYsIA_qKeB29LCp8_6Yz6RSbgja016Y7pI7ybAXY6ZnXXFD8vrDeQCSXtAgtArfXroaJkI9TIStkmAadckPCPnuB7nhKrLk39puEMfOvpLohAP7yzoxv2AL1STf-a6v6Z12GFo6A3fO5xf0YeQWZY8u8QxeH_jj9hnkuWLPi-fouglHUG_BIgnxelwheuFo4_ckzVkrylKhtD3iYlkKT6BGU0UAY8B8KWgv4e3BEfXQeCsnfqytwii2DHIJWRVKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piuOvl4xx9sgrVxhHxaXV3c0be0QzMmvEpa9QJsV8_q5RF4klPpwsv7Hz4te6JD_E514lLsR-9g4jQCTDR-FFavYN-BDWImenunefA5AJHfCEqDmy9oeHKvaH9n6m3wt0NGLSbn0CJ970ol1RteTvMtPc87Lt3KV6-ZJeghLdiJn8pzxI0XcBlCaSamHI43bizMa_Mz-BF-tluQhZbw3Y3uUBMLPU_c930GZ659RnQgSXpINSXOLbGbXSUaJ-h4KycUAnalrWvjV1SxUySf0ZolOeJEiZfeMBW7Lw5nf6XcjIEwKi3Tkz-gqHl_q9ce0Hnj4o5KAyHq_5K3UtKauxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAANBJwmjl3ZLiOD5CnTUKZfuI5aCr0GpvOXhMRDEuFxKtS_NKKy-xFbU5rJ6I6XDcaA1qUPJelp_gyCsrfSA0Zoi408w480OTTbcHUiWkDWMaSSoBuq2HQ6-uOyVlR3abJSGEcLriFnsqejbjBf_XIHtS0B7JhnOG-WUitX8EG7hKVsiZMF8b11IJk3si8-Ptc-JKt1YBGSTFd1WsGca9FdoJ9_2weYsAavSxqTduXv0HSoo3ldfvJwtYgGqVofnK6nKhvqY-UECC-L3ZEa1q6odJsZ2YvimpDess6NrMm76t3wx6PstifKtIcWz_ls9YbYGLdF-EF34gENgTA93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcr0H41fgbmnzrygGmSePnIk4k08JlsLpIWdnZnvQp5OwEfvluRmaWq-YiDWy8N3B4YON4y7QjUhWefZpR8pPiRr8zwPpCmLMMbWJ3KqxHp2Br1ckZH38aMuqQiF3VIw-wLXy20Ze4oYiTGgfzjrymGdpJC4K45YDVnXbMPkkNLxksifTUfvFczvgZxnxhZJ3tnQPz2Jehv2SmCGeJL9Nq1TWdoxpM7c3e6JKkT8H-eeom6gpV5RsiugVGd3mFop6zUwkOmkTFSJ638esQG5WO595ao4EJ6NM1kQP-awZA83JOvs7--Snav0w2_cuU-7E4WiNTNw5qrQTLkvWcEsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhOMsRxXe5ZaKtZPFNrRzSwPfINFupFzaU1N9WjC2L4RAnqlE-Nkqe4U0Ln4NMdpXmYaUX6JOyStnnP7gTUKkMxFeREBroPsUoLmIv8nuSQdg8vRHSF-fnIVrSdQxXNpZnQh5V9-pqxsLkKG7LO9HVrV2PcMOxn5oS9otxRvpOLsbIqrliuaDPjkXzEIo5VcUYMBo2EjkzqMzhdldv3rZPw8hm35EKjHUpCfnH3ls_8eks2Snw66TtEaQMMbnqU4nGhy8N77jBQxVHcNBIW2e2-ASIzdntG-XslVZfnCVZ6UtTSjwktiMtQBTR4EeyTB09uMQ8hpHVcTF23mtyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvnBcB3uQ-C-0cyKORJe0e8IcPPfDV65XHhDTquFrn_r29281t5tJFQ7bbHAWdIv3hQaEnI8jMHcI8z1Df1or3sFhxEXVfn1me9Q6fBihHraaIWsibF9t80ZsAsBOugZJejNgIqzlO70HSwAmwGCa9mMQeCLELp402irvCRPuVEwTAVxsoxbv8pVJs68ZRw1u2V5Dd-9FwoR2azE-CrxtVuGlhPrvMoTSKGJORbgN5q8xggpUAv_Q0podZBKg1QQMmXBcy1-FvRiRkWCtojLWVzb1TKvZIK6PCxdQjKGMQ8QI3O6Tedw2dbIFPOMth0S6Yi4-SsqssVsvSpRjge3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=SqPwDgXYyw7jdAUN2lpmx_sbUkGyCL-TwEkYVEJxZVgVYXbJkzM08WGdoi-xhBaQKvEF5OGdv7vHdwNNzZzLgWBzn9IxxdMXRHFy-79FPIafrbCOlJfsl7rZg-uuFgOBbcb-J-9VwM4xkM3nLOy4FaBIDEAOaBma8ZFWBMztnj1s3w2DtsNYAZ9BfsI79OTEjTAxaIXT4M1uo5oTWE1v17y-_BeOwBRMgKVQB-8vZOcAM74wQ_br8YpjiqYSRXA7M1cLWz5FwDVNpbA8eJIPhvl9ByhYfK3HUCA8TtBSrio73irs1CxF9Ebk840bIJ_SjG13uIOzuNQzylwzSZpiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=SqPwDgXYyw7jdAUN2lpmx_sbUkGyCL-TwEkYVEJxZVgVYXbJkzM08WGdoi-xhBaQKvEF5OGdv7vHdwNNzZzLgWBzn9IxxdMXRHFy-79FPIafrbCOlJfsl7rZg-uuFgOBbcb-J-9VwM4xkM3nLOy4FaBIDEAOaBma8ZFWBMztnj1s3w2DtsNYAZ9BfsI79OTEjTAxaIXT4M1uo5oTWE1v17y-_BeOwBRMgKVQB-8vZOcAM74wQ_br8YpjiqYSRXA7M1cLWz5FwDVNpbA8eJIPhvl9ByhYfK3HUCA8TtBSrio73irs1CxF9Ebk840bIJ_SjG13uIOzuNQzylwzSZpiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbTnY1Fao9E8d_Cyx_jSUT4e-4BuMmcuGFnKjMdZIVZ0a7fWo_ttqdXlP5Ca7-zH9fKI5ovOzLBHFFm2vq3v7yPMGC4aHPHvIdbmRF_2XffAmuX7wOsI9L1Y9UUqLtE74kj7NTnQvOplNmpXzOF4q47mPehZG9YiC3pEeln1SXMcHgM7TPI0XdyY3ZJGPjMyp_NJnhLmRm39iYFmdXbVQkNHqHlbE03I-jiQpx26f-y4KFLEne3VCgedd18aKwiM9yJ7FeKFktS9qFRFdSh_M2uY-q-fUdbgwbN4UN4RJVnOywSreVRceemTXPctMUvl7QsF062Ql4sS2QyvdUw8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-9EEIrtN6-2cgPliT66HD1_mmnieFcz47w2749Lw0vrw5y6IREmfqEIe3nslPSU1bn-gJExKqGOn7zt5BgNqnWS-5Hb0uvi3fP1BgidwVOQATcGzbrygriKc2nPbj6DAp20UR7flZnh98W0cl1ggy-EK7cb5qy0nawC1Lffx-whTHuVF43Os2zzFQweT-FgseSc1Bmyc9yl1OVFk-nBx8tJ43mMTWMsYtNhEtnOQN9oStkkXoB_BtgXGpGsngsnDN-YMwu3lsxHAAVimoaNVuEDpVzWjN9h9_CilYpArZTmx7iMue-pKTj3jrPbfaEj3CXHdGTWT6Gme0I9c6t5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUVnAAWpyCjsFeesKAg3BM2eGMHxFoDE3YAOu0kkE_EOLVMQrzIKd4BHEQYp2YJcKNpMj91ODy-b_drazwD9kUfLAq1DHx5QSTN90AfGK9Bg0_qqsZ57AyFCtGwuLMBgdUrnqdvb7MFVbQM1a3kzQyIUFkqT7r03M7BQg-3Wzj02FoyD64McK20yCqob-5o9Ql39Cz4HNP6JAwNCJwzSSrduEN0QblNL4i0StzZord0LzZsK1fl_Oo9UNkBnRloKgKXHwb-O1xmPA9gRlxyZ0mjrVW_qpstyJ0C927TMp0tLnUdVt6BbnY0TlvzVAiY2edTqKqILq5VQ3wG9bbZlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nREOkOjw-ip1oZSzHAM2Ia4t6sac7YF-mMjVsdebYN4tF1ivCQkBICsMo9WZE9fyD0ecPCmSz57lVfGg8VfYE-NkYItTTpsEPJtBG7qmX5oUIecTmV1EXqtXbZMepklZNfACdssSyIYG83k8z4tVkp7qdzunsvGQlJtm0KoLA0--oNJxftnt2pjDVcHXr_WzAD82xwIa2Qv6Lh4Q-7egUyfmuZyt6g3J4fGl52P5NCMgq55cm1opxoHFLpbTuYwUDNkM8aPy3VBhjHEYTGUEP6AqIBLmmYb8BhQIvwldCNLWhw8mdemtHfHzJCB43wZiM7W-X3evuDdrECf7LNVW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVB_Z-n5Zp0fiO10dt-Cp-nbPURUxxxl5cVJQk12GZ64FGnQTHCXK_C36HzpvZLq36JGiLxn5V9NWb7GV9eooYW-lby8PFCAqlT3V9weFZ1keg1HahKJS6qcP8dfIH7onampbN6oJiTX0_7-wD5PSwxI_1WbnTbMDX_alHFXDaduxEeC7aX6IPSjsRMK3ahvLSOM_QmCwZQlXWJW27ppvmogYuoJ63OGKzW7TX_yedJBOktSXppdH9p1gdHJGChcXP3Y5L_4bjt2eVKdLiXAQc35VblXBpesb3ZFmXr31A1YVfkk9hdVRVsD1JktxRpS0wyVAtKfPN6Szg6qR18ohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnKtnBNEHb_3WySJOwThB7xQFYQKqNfBIFgTSh9eO1jw432_oX8FqsH8Z4ccDLrYIKgWnayJNei-NWMc5MbnzCFSbYF2BTfNjHh0FTfnl3VgkauJvQBnEmkqvCcV_GV2tSn30CV7fXauWRurbsFUV8f9-7bmK-bp9UR1oaHJ3aLeu6Ir8Y5z43AzaB7-Py-E2HNakv5nqV00Q88hZnMZJJonAzZ43vIt_2zWSd8v8Nt2EQj8u5EByJucc_XYz4OK1jY_vlLSmf7zfbUEk9ejPhYE38jEx9aw6lMryuSw_EjWfanqFTXzdxxbno-ybVFosCzd22pMuJ90E4te7EyHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3bWhEzLAuvpP7g04acibsZT57cf8uxHltQR_MrCIKq9cITW_AlUuLtJHr60R2X2WRa3gh0kBYXsS1reUBzzOgzVOMi5mVOhfaEtq1pV8Wyab4cL0BmzZ4rDuXq218CKcmd6PB3WCJpRAkgUx6BlZKqvdPTUYUV34vNzaIJX1xoDw8bwVvIrMA0PUDTeIUaUdV_HSDkxQn7u3EKIoNm56cZrH1pAUn3iFh127oxyMkURNLkZt4OayTAKzfI6p8EhfZbtD0uWa_lFhwpt_GL10YpO-X31GdMHiHQqYzWjkysZTRKSZ_F5IP9MZaqzD9UB5k4EPNQ5VaDubSUhiZlZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuZU8yC68izCaNYj_m_SjsCUPL9GDJzI_L7TPZ0SVxgjbuKo1nmi_fqelV-gyu7gIMQGWLW5C9ET8Bne2XcZ2-IniiYcur-aGH2MaVe7vpBGYyGBq5756v2ux4BbZK2wsSQq1OKFcSCvJBg4BNMsSuyGbFOAt32v82RDzRNmizu6oV54DocoIAckBiLVvCKegre5Axcj-PcOdUUfIslXS_8gZ_UK4p7i07707rMllEHOEEyLdWC-JHcQEraWLFCbLcnMwyaINZoJ4avYasf_ynqrSffcWM0vyf1kyflCY5z4mOGWtSwqUNCauHrPCBCXUg2iCz7Cia-8VFdUDe2_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiF0Bffai17lMlQtKF6vpiVICgftVUevdcQXMk9iOgKTwzd7ObPzJLP81I-YZ4nVcrefCP_sSZWuG3nwaRqx42g5BLlequYDCvMeSJl6Dr8fVqwrKsWjuPWgY6MNmTIwouvkVrdMbHtVbfKeJOE5kcfTHzCZD9XTMKNpSPzqXQDZOYdUm-6pSti1Yf8puW84KKWrgV_MIBD9_oRtyq5LSz5_U3yZyUg6sIdPwKxeVui2b-5vvo86tGNGBUsJkrhCQSeCZdJAGZChialLrMLpL-lt81xBzlAMrIZbJkiUpcbSd0kTXcdUEYb00BQ3juH6He8ftcIoFzlQfOXRS0uzUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvobpQbq59pSiKwxGFBiHeoGUuU0ZCvaUZQZ_tzcSp4nKc-_pstwXibPRjaUJm4fSSNVsnD1QLLldNctd_bC1ncEl1uSOKK8EKzx7o6k9nS9e52RqASk29fW53I6KSGuu0Txqd6GoclFLr1SB8KDIKiJ7zDfJLkGPCbYnyTh1SUTUH0mUw9CcT6onxgiJTcg6TaX3y2vzcMCCxRyX-2fPpDl5Az1GMqoo-1wbq5KEwlj53AfOaaWeRGXm8J06Q2sRgIhlHq7ESMg4U8fZEjwWwJf71OChubPi3SHGtxrjz87064EC-H-bni9J9KrFX3UXfVP0HQt-F-beaFZUA6Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQ6e8llQpaguY4UF8ULm3Oj4VW2kfTI18n-sgf5zMxKWb5Kiwy1zCMQitOc5hZsCuG-Mf4_nPiIik-VagIBP9PeYDupDEmzijgK6qqbYoZvwpfa7pt3ZKoM9wYjdlpA8dyX9FfZZk3hfJoctefFIqY6gxNOwE8yeW5CNGH9Fv5K0TkzPkoV5fCODoXew845G27ru63os4xhXYuERPI7TMrcz4e1rd4ssMLy48z3hlRQlhT-eInDHd7WxoR78TpOdi-WRrKJIZAnmwHb4AFR12ebh1HJfaZ7Z_jqLkhas2826vM2HAfq13JhYDwkiOkiVnKClhFlgnSxQY_eboI6u9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXVMPkgxD56jfX3kUnb2WbzTUprkiSm8IRkOiuNSulD74f3QC0ZEZl6rUFzgJc2ZdqmEd1XiC9ylHafLi_IbMn2rEYjQHMSN7a6n0uV0dC_ItMAPXSo29t6Ul2NYUFh8Z7avhSNd1fktDlwmaSeAi7AeohinJUbivqLEVf-HHxeRcyGb5z_Do3g-5nWgpZHbuZz4ZhgghFfyy7L0fQQHIG6ebHAcNvQyvxabLQXAWOYdmURknOgLNfeE1f03cvgY5lShoaPvqMacSIhKDCJLfAv9KhmI0C7eMF-Pm5b_u9BkKqK0-D2pCNdia3J1NxAIl7jRawBzlFr50uy53PWscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuwSTTYV6QOrsP32VjkQF_UlowXxK5ShIqwRnIQlx7XEL3eEFMS_y95_dgSZNPgO0730kLBinsrQnBuIvb264GfwcKt5qewN5VhH-qxAZRs9T4p8nNep3T7f-IYgEXJjvMTELv0AcfeEj9YKLaAlwLapRlQuiH3Pda6rZKuGKTUdP1emrCV5jRt2kBU4PmKsq5Zgp_AxEYli7C-ebi2Z9xFgQP2PrpyWKTCaO3_2hFF2YCfs_1chG1-QSlrrKCxLdO0WbtrSFX6s7X3rbt0AeAxZ5i1VpQiMjUhr-baUnX8_ESYFGzKrVRa6aW3OsaaiNdcpv9mNSIPGOmNMMtmU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPctbsxrnIBoF5i45XmFy9_uxOY6VooljMU7Exc6NGM1WcSAatAyNdUyNFuihukdVdy-FshGeO7fR4JERwZqSkyDV4E3L1IlI0EAUd7luGqcF0vLCTAzZHlkrtTfrU0-Gtl26tX_1e1VSLWPtvfcJbm6UqWNxa02wCB0a4m8GyqzKkbTYC_RRyPNHVWoNGJa19XHmMahz3xLhAuq2cECrFHwnG3TdvAWPwdRVJJYPm6UaMsqJd4LxDp0_BJceOeGQtRARQ9vnf8NuH8QgMvh8ImfWOhN0ybRgFLhzO7b3facbyuZ-Opoj2aY1mhT7mgQ_c-gU_S2VGJ8gRrHTCt0rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=DuP2KB-2rjKqKK_JYb472TGuNd1QslDZig7cpYqSBtnrvn5wMBNu34pvXA9uiqzJdb0eQi92ng0Dq00kVg82y3gbChHMGP0YE5_5RDBqp1NxkW-mFNGE4Hl7YYse9_AdYH2klg9oFwPh99KHvnxWpdoo_ODrUrwT2TVDVM6j6j6RhyrpzIRoBi0RNH1v-Zj-bWi44OG4dhdKvITG7l1SCag2Ev1p5DgRJeleqIgNBxPfSglAK3Ln4LzNrfJga-Rxxax5Uz9CXClw21PbdvFKriAn9eoXZXFVK21XhCzjTJgFz1ERb2uyWaTySoj9nztZ6ZlgSjuLJkUz8DG7ycOhxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=DuP2KB-2rjKqKK_JYb472TGuNd1QslDZig7cpYqSBtnrvn5wMBNu34pvXA9uiqzJdb0eQi92ng0Dq00kVg82y3gbChHMGP0YE5_5RDBqp1NxkW-mFNGE4Hl7YYse9_AdYH2klg9oFwPh99KHvnxWpdoo_ODrUrwT2TVDVM6j6j6RhyrpzIRoBi0RNH1v-Zj-bWi44OG4dhdKvITG7l1SCag2Ev1p5DgRJeleqIgNBxPfSglAK3Ln4LzNrfJga-Rxxax5Uz9CXClw21PbdvFKriAn9eoXZXFVK21XhCzjTJgFz1ERb2uyWaTySoj9nztZ6ZlgSjuLJkUz8DG7ycOhxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os_29R9C0rJXZNtwgiFIOqQNwcjqVvilqy4OB2A3nJb7fAJejPuhDoci8gLWcQXRiF54eMECYj5srLQoDuCwHYPhQdm7rry2HEPxVuBjIjDbdKG6nQhPx5dVsgxXXpWgf_4xIu1e8X_3YLsIp7vLTMdvKX82KNjZ_O_2gB5FUfycdCDySTAhvyspvTqRmn7LXNZOj6DrEJNfrnAvyII5Mswazh-vcdhgxNZkdp4p7RGGmrka-5nYuQxAK6sD7rBp4a5VC5-vOdD2Fmkz0QCWymkfL-zpPNujlqtgJRi7DL6RQKz328Yyxw9gbUBzBsTAAsd7XYZScOYGjo6bC-eq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDC3iVn0FGk1JCl0M2oJoDUSvgqRaGzkhH0YybmwTKkBNtSrnzaiefQiZ0MjGSMuQ9K88gBYoSNlYkv9kZImotg7VaVcxN_7HMBIzt5Ovs83zTFaRMp8IfUIkK_Zn08wvMztiTJma4xKhd1bNg6E6OIgPZBFMen4vTTHcBfjUUL91Fx9r-d84gZct3-Vo-kA63imG0FxzY_wnm3xlz3B4q9zrgnL7nt--OSsGMdo8Gi_rECppMuwqkYhqV9-fQuwSufNZLVXPMuzZGaQml0W9O8ulQxsg1gRq5P8ObEyPnio6ysbph6uJHbYWL4bFQ7kFjUllXh2neyS4D_Fis1d6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm-j7Ou2RgQtNoBskR2ND5SAguUOkDdNISRSPqajg1fbkltFTGoQ_u9-2MbsUczqPOQ8xm1CVRAPns_YzX15DxAzw0CB9fkv2VxUhFe4eoznPPayLcAKYY1MrqC2yv49uV-2bDYpKHYNQ51S2ucy2MVGeCvakQzxilvkKjPrgbTtLDqqOoiidad34LB2hHwmePvNeclFRc-00OQYIAkV1esX0CFY2RZiYoBsh5bDGSHeRvltE7jDzF4ja821OYElDdkCM6J1rscQmKm14yt8i4DiW-89TFh7PpkjXCbdF3kPhhtP6CjCDj0cBvkAddtEI5GyAYWRqkZYQxvC43wtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouIXhNF4UsslMWX1TmLwmwvTRDNb0B0X-HPu0pAKYHp1L7UAMzf0FwrXOxHWIZIL35mDefld31ltfnr1PRDqaRALufdWO0musSmSt2EvDd0NBsxDsNgrA68TLQ-Ay2jISFqfle-qrnqP78z6RoZLxbPt3H43KPhkp2WSaPBW5CfEz1hSQcsW7G7WSEVtrs42EudzlvWTwZxQvFbqJorH8FNgu4c9ot5XwOjxI4OBD5G3LLurHJjZN_-9ipPvI-f6QxPUDqo6IqLx8OjQSJw6O3rz20Z6RxGvIDpK0BtU3YR2bJehUj5qIKUbnLRHmUEvNI0qAa6WatQxWcmaYGKkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=cqMdcEz5D_n8JTvzYtY-Pzp44WfpuKga2ohppT3X9xjtFwRxvaKANFe4l0C_AM8ds-OYhGLXJ1ECIi2_AtAVrMxIfrUbIznbeHBcFAUU4TUwPTslF8vNjMXVIvuRUAIOvTW7O5bdCTDdoQBtYXt2hXbRvq7Kd5wm_ILFjXy0Z2yUFgRdJN4SJmtfeFEz0bVl9tWgnohF1nofBBCXnN-x_Ed0-4YD57DAq3iw5FB4g_EqpVS_mXQtMivXDf1Kel4c0ZI2Yuo4QkhG1GKIMJVoutkZJbt6LvU8x8xuuo1jr-yNE7dTkGkv1ZHPH40MIC-Lxq2z2XMit5bETAztT0rt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=cqMdcEz5D_n8JTvzYtY-Pzp44WfpuKga2ohppT3X9xjtFwRxvaKANFe4l0C_AM8ds-OYhGLXJ1ECIi2_AtAVrMxIfrUbIznbeHBcFAUU4TUwPTslF8vNjMXVIvuRUAIOvTW7O5bdCTDdoQBtYXt2hXbRvq7Kd5wm_ILFjXy0Z2yUFgRdJN4SJmtfeFEz0bVl9tWgnohF1nofBBCXnN-x_Ed0-4YD57DAq3iw5FB4g_EqpVS_mXQtMivXDf1Kel4c0ZI2Yuo4QkhG1GKIMJVoutkZJbt6LvU8x8xuuo1jr-yNE7dTkGkv1ZHPH40MIC-Lxq2z2XMit5bETAztT0rt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHH8gp_o1BSGEhqa5uZZJX72W37UlV6f60ccWxd1LPabErJDp7mSiGLjEV35l0M296PDueaS88tm8Ar06UtBT_LEySQpr8MYHBSG-eDbASipKpnv4dxB472g3U7zaeQ3nVEBkXo04EocTmclTx4RZjyhWz2u4PBLtfDWkZuFsTQSrE_OlgCE8DSEQcjjVW2o_sCR2sTb4DX3JB8Tau-uWTCSnZlb0gYnfwOQuwivtPw3tE7AWeHHoyIkn2E8DbcdoJT6enECMuajGxKO_gf1OLo-1BQ-HbINYJe_-fiYC-dPcPPjihp2bnavPgNsBHPzyIkQkKi7WrNjEGavDXDxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=L5SWraD-ShpHoogXnkfgHto9TYX-NqEN72pz_XDm0OMkREoAtNVey497LnyI-KAi_fviZIfq4LiA5IP-rP3WBLtgOP_Q6OTCfgdVuckLwbePPgHZMpRjdLAgKCf5aNSq76xhFymVe4BTzLV2FdSeQHAdAF4NvayY57xPLsGh5PEQvftn59fFiQONJavIsKYgTyyFlwbmV7Bydhwc6IhY8F27sDis0VXGPNQBkmTr5CoYKw-g3vBVyo9eSdsR57VpA_VAxwaGS-EjeHxuGa5nw-oqdCLLrfn4uA5ZYcw-qQjtV6SjLuih_q5AkX6qN3Xkf5co2e9X1IG9M8mrFCgSQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=L5SWraD-ShpHoogXnkfgHto9TYX-NqEN72pz_XDm0OMkREoAtNVey497LnyI-KAi_fviZIfq4LiA5IP-rP3WBLtgOP_Q6OTCfgdVuckLwbePPgHZMpRjdLAgKCf5aNSq76xhFymVe4BTzLV2FdSeQHAdAF4NvayY57xPLsGh5PEQvftn59fFiQONJavIsKYgTyyFlwbmV7Bydhwc6IhY8F27sDis0VXGPNQBkmTr5CoYKw-g3vBVyo9eSdsR57VpA_VAxwaGS-EjeHxuGa5nw-oqdCLLrfn4uA5ZYcw-qQjtV6SjLuih_q5AkX6qN3Xkf5co2e9X1IG9M8mrFCgSQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVHWy79Dk56N_OUMry_kxz1XIcwtMoiLnVc28HfIGoNN6MuX_MWvVz9vdBetjDirmDesVZ1e3R6F4ZCWOhcV6xcrw49XTGn5vxy0ffOEMWAoSkjDaTkdpoDA_Z0x58jMpV1d7ofVwqfrVMGv4gnSbGKX_QA5mf2rMFyW3Wtt3hJSpCC7ZOmhMu2gfjbjm-E_w-oQMulbYal4llSXbdh3awMt3hugKOISvByV1iaQrNx4poMIWooy2vrK3Fi31TKmLFM8x-KeDaHGWyDzWLm8EvYDksRq2LJxvDkN4w3pb-_e2kOSwsin4xyAdzGcB0_2IxMvjsNf_B2Wxwgcc-pSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqJ-FMnT3fUDljfwPr7_kJW0Ae3S3a2GJHVdhfgMJhNbl-BDtPo3XR6kAw1uHnIehzO3NqYU73ZCgrzWnoCW6ZPYE8bJG3dDxISjaFSHyGFtlE-OqOFsPF57kyFNfC2yD-zPTVwydhYAUX5k2Jtw9EWfIS6ZjmatexRa2GkkP7bviWG5CEOXfGfZPxOhD6nhNURHBMcJIaABaAPnW3eDsxLdtVu4A5zzV57YalIAjhq2P8qH3id1OMjyPWsomNDbgX3zHeqrXKwfKgVsGm_a77TKSY5B_czmc0Io_I80nZ6_53ATDuP-nje3r31x2ov5lwfunQFzXVvyiXP4ulW3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4ta_Tj1_HNPXd6OeTOD16RJC2DEjJN4_u7Es23byHe84X-TVjwpIJtSauNTU1mFtG-UqUBF3vd8E50-zeFyjGyz9vZYvh6CDHzQ-0bEPHA4bPNU4fUQcX16lQY4G2FPCIemDqJA6wHfmY_W14e3nfkSc2HQyOSAL1izgL7GNdbUb01wVyjPhuzTX5QfyYUlh6u2hDFg2zijniQVxPr8tLYe88SbJSpVPwLy01zPH_0IMM2nlKqdjuZUSm-LFLQP6JGYLBJ-8shBLjpcrY4WPLx0g6MOeXlHAveJLHkCsoWeuSwUxoc7ezw3aOqWqOeL3ZNTJI1_-7WH00s85eGKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjtQwyuuj7dS34w3Ggz4FTBW1b6xpSHorSV8X2FA8kTdVl8eSIZfWJG2c5YL8UAwmQZkZPjIDKfPDHLch2CZl-gpXxQP8KVKIkwq03UdU1oJ8KN7ZQcdi8m0qtSCv1pG9TBCOa0B9B7_RHR146mjhUx3tDB9bEk89QmmFK1kOrlu_o16ggnU76nVVylm32WlGPRujnAK3COcZ_1PSP-zYwN7YUrsfZIa6Xmoewog2xDFdtSOojOACujbunFsyp4pl9iE29a3lVbn0zj3irpT2Txs-nShzw1myhE7vws3_Vkd2D9ejCjbHPLR2VMXwrwWjZvQSEjM43fj1bxZ6M0jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0_hTMb0c___m6csBrUKaWl1UaYbtuHD0tSF8hZtczGhoiS1c0vQt8yIkkkmlKwP80O2suZV0c-SkQK241ld-hfNmML6wgMWvUW9PJ_qK1nYYo3FA9jQN9qhmAjNWt3M-2lV8QNTKb95UcCuBoIJlruIrY2cOZj0kWUy6vFgJzFTKZW_dL9rB3xZgx2sgt6NtEoxw6F-8gehtwNRJuyImDdgQ9duCfROnSxKKyeaKmvxsdTiU_76POfah-SoW4ZQ5GC9t5SHE9Yjgz-W58NSs_WSgV7LCdqlnc15VP1OC1GiqGPtNkLWGcZG2tyz6LhBXT4TYEYeiVH2TAa-bz-pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noaGb2gV47pJ6p7YL4V_bce0A2G1pSiVm8nGc-f74phGjyfIzcntbJEsjK23DCvI32LidyDNlKdERLzllO0jR9UsNuJWrdXltIgQW_z7uiVJec9Fx4OlqVokmIsGIh3yw5Op3MRyyjuYp5LHqzMyV42qXGN8XomzWTlihDlFTGq1xiMZIQVKY3hl85h4kGTHM9EzOblKNg_ls-Bj2ar5tFObJKrYc5oIeX4lF7fISTdg7THl2v5aRFtZJ1xh6XuWCCJ-DDB9fMbwCFg2J_999dfLSOqLxFBf5twGZyfSuxo6LrC0shfFyq5sUnoUftCpS2ZsryVEozo_OdIXbYd11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=Psi92kRLQNObuwaGaXuZa4MnwaYuF8m7tuMdtIDyMrEqkvb5PQx8H4ylSolD3LOl2wlLj3mELhI3P8RF9oIuWKYyHCNGYYXkNj-qbO19TrCL8jbvwo115uMdvQsB2nCY-0JHXsSXGNNe62j7KAsqTRg26XF-UMu4-vXsGvvTM2vSDSgDG_w6SK1YV1IyUXuFp1H-kucvoe4rcid8DpX9KeofYs_uZAdL69aIcUxwOZIP2lPmsvIB7tm2TQxsZ6njHb1t2A9beQb7c-FDEC-Nl-8XpinJzM8ydTqbqTbyd1u6NQgMhWYtNUE9E9G44AHK4FC7xreVzdegsPJqZFeMnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=Psi92kRLQNObuwaGaXuZa4MnwaYuF8m7tuMdtIDyMrEqkvb5PQx8H4ylSolD3LOl2wlLj3mELhI3P8RF9oIuWKYyHCNGYYXkNj-qbO19TrCL8jbvwo115uMdvQsB2nCY-0JHXsSXGNNe62j7KAsqTRg26XF-UMu4-vXsGvvTM2vSDSgDG_w6SK1YV1IyUXuFp1H-kucvoe4rcid8DpX9KeofYs_uZAdL69aIcUxwOZIP2lPmsvIB7tm2TQxsZ6njHb1t2A9beQb7c-FDEC-Nl-8XpinJzM8ydTqbqTbyd1u6NQgMhWYtNUE9E9G44AHK4FC7xreVzdegsPJqZFeMnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=oqR5rn3KvJU_0iTHsPPuVWtrXYDesxiiK7ux9m0zf8paVaTSw6SBl9V6ALzGSn-YGRTvrV5x62wT8Y8yoiCeCpR9exKvShAK8KCkcz4LV5ZXgNgxwzClD1wNTwOjsYNTWmgHIL217yojfugAH-MSln3raUOcHAUrw-KWTfjzFMn58O5lMvD4T0abVdW6HO_PRWQa5hbTNuWwAvMchbq-872VtMM5fWbjZzfT25CLBYkhSFwmJ2r8WBoeeUFLETxSA5n9F0U23Nm4xf08CIaMOejLxdMM6qB0iZVVz__p8pUIsAZTLUK5ASz8Y-yPUEcMUtU2h9HroIKa-I4ZPIQb6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=oqR5rn3KvJU_0iTHsPPuVWtrXYDesxiiK7ux9m0zf8paVaTSw6SBl9V6ALzGSn-YGRTvrV5x62wT8Y8yoiCeCpR9exKvShAK8KCkcz4LV5ZXgNgxwzClD1wNTwOjsYNTWmgHIL217yojfugAH-MSln3raUOcHAUrw-KWTfjzFMn58O5lMvD4T0abVdW6HO_PRWQa5hbTNuWwAvMchbq-872VtMM5fWbjZzfT25CLBYkhSFwmJ2r8WBoeeUFLETxSA5n9F0U23Nm4xf08CIaMOejLxdMM6qB0iZVVz__p8pUIsAZTLUK5ASz8Y-yPUEcMUtU2h9HroIKa-I4ZPIQb6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDwCUsrCEuc1PRuyLLbq1JtKhnuEj2hjkY38GN1_kbsFPL2p62KgWT4nap7uLrFOgIyn_qCi0t0ikV0bTTxX38yaqawFJmPvV4mllg9Em9zs65_aqMppHLCMaT_gZD9waZRysxpDaA3m3u2L4O0gqu4Jc-iT3B9hhp3ZJtnKHXMcSMsHM_N-3RS1wgioGXHCZCl8HuGKRjU6_MZCK99QJbHL7gkCYhvJx0XDk3Kfx7R-VqdGM49ejK6whtk4rb_vXqM0Sg3xpYzYwumHF7BlqjV5Z3ZzJXXJ-Gf7GErkkzesUV-e8SVRSTBRRF4wMw5iaq5CWd317EyN2SirJUcSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=X9lyjWGP7imfoITYLmm5V8tBxz4gOgzjmDDzECC_FFNQpl-6vHd8bG95Auw6jf6z3lk6hl7xkQornikf1GTYxxj2x_TpcYBiHfLDMYx7gqJ9sdePdjJVUYjxPbAGzsCEkNnYr_bVV1whJyu6GjIrv3nRJRcy2A2jmUmZSsd1MkqMjzVmvicKcuan9a8S462NnW0tjuuKCnw1lV0uZzonaKH8iHAXIIO3Dtew5SGyHEKm9F8O2_7nlB2MWHxH5NgZqgcGqSfx4rJIyu8cDCzQAZ-SEPta1vF7TT-uHFy3Emz8JY8qIcOZXc5tizU_wruys95PfX_ZILWPNQ8ZXb79Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=X9lyjWGP7imfoITYLmm5V8tBxz4gOgzjmDDzECC_FFNQpl-6vHd8bG95Auw6jf6z3lk6hl7xkQornikf1GTYxxj2x_TpcYBiHfLDMYx7gqJ9sdePdjJVUYjxPbAGzsCEkNnYr_bVV1whJyu6GjIrv3nRJRcy2A2jmUmZSsd1MkqMjzVmvicKcuan9a8S462NnW0tjuuKCnw1lV0uZzonaKH8iHAXIIO3Dtew5SGyHEKm9F8O2_7nlB2MWHxH5NgZqgcGqSfx4rJIyu8cDCzQAZ-SEPta1vF7TT-uHFy3Emz8JY8qIcOZXc5tizU_wruys95PfX_ZILWPNQ8ZXb79Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqBJfM3OJNgyh9C0NBgvvVwpW2vIectRHGXlfPpWDfuOYjbhyy5xcjvLC-LMIXsmnhYJ2NTlTYtx30HFvK4WXGhJgD3Jamk4iiBjDs0IkG3XN-eoUaQCzP38UUIS5DfGoT93dAgeFokv2995AmERK7WCtx284kQ8DRFjwePNAe0Nne0zPjaUN07uT97nm_CD5xHRYPcDkwJCXlu8-aHeWt3aZIIfP7I7SftFBvIBNo_46XfdnffMFBRFeE8M8rU_fQ5JKHQ56axhca1zuPAMA85XLQk5nyJybJ99pZnSyIOxyyRDhbe4b3Bee8pAhA-AzZ0ljkr3T_jZ7XIp-76bWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7MNMGhpQrh_SdmWThdjFbbBAQ5V2hZ7RJe2V1QOdBb-h0_2lDOqrYam-kBfWSG6QxI5xAEtoBXjvj3H2BigtXCeZWaKmUamEQkmbdJdcK_QTZDw09wqtwpS2LeFvp2rbz-uCgtENmYpJnifqtQnCzS225X-_n0xjo4Vwr6Sar-_fwUx9gT-0f9SKmWCnRhoXzS9qzP8jj_sUYUUkBshbrXGMjoHeUlUeGddDTX979v2gVVxz9D-hp-9opmlHBgC3BL91VIi1-c2hTg8oo20YfsbVWMH5TprBitu4Rj58VzasOoUX4rliKeHjI6elDoJTDeNexvpAIsnrhugXorOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIg3qDRBk_n0ogKX_8M0VeyTad1Ftc331hf2vAq7nLQfJJIJ8uL3fnTnEWrbdCtODOVg82HysN3FAI_4xcv4A4eNn5dl380JiUrxqGqMeTn0slqjoUzvD-TnYbfOCjM4XfFiYx9CUStglXpJXQ6lJBxppkEwxLkf0-3fuxFnjXeIEwf-i4IR7JRlx_cR17WaFprhY6WYMzJ34Ooqy4RWPIBF-sd2tl_HMMtHHRtD52rzeZutscoIP6HuUGBgVVAPRrAMsu5nszws6OZadxgZXgdyoP9a0BF3nbxibcKaQBbnAA0s6TQO9FN57opztbuJkN0EeplVscIotqrl94t0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAcmSAqi2HPcpP6JpC2MlVkGJEn-1Lb3j5h4BuKld6PCxlI6cjselmkJirLaA3ts5M_g_OLWcyprr9tAwIVv7jiGPFJbIcJDK8-9AWZxis06iiUTyRGm_w1uGKRvAHWvjcvwbfMRmg6FDAHQ5wVmxdMwM6m3BxiqTPcb7jWpAXO4SRVazIIbAa9kG-oMDcONYZrLWwm_cfSejCGylP3uGH5rUz-ItksLy_KVruA8aJCOeN-PdXnJz1KHIeFb0Ay87r2mvFC0KR9nQjoCmQ0jxNb3Lu82OxhC_IUpQpYBvjItDvNy7vouww3zar2cchapDvXer0O193c1aAnnZEC_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=Lqz_9sjV5USwVUVvO0fBZvZIbtIgLD9bVXlTZ8-xXYVYS1TfvgWJjvjnYJjONM83PyRXReh4vE5MOij8kAa1XEBecLa_pMm_OEYXUVf-GrVqj36T6WqPwJCQmc9-6RSImFNCvXb3qKrW8jSsYtw0I3hDenPJ9UsGA1C1WDo4EioEItpY8vkv2b7Y_hCUYcjswUeluDbfKi6VxU-fGki2mXYRBhR68QEuFdWFwGbDaiumqzak_6mrkvXq_-wU8h_E38zxlvNuWKNjTsq7F6m7H0anQmluIykJeKljoeMY3xvIm7fCgIv3JjPlL7rO4qUbxInAgq0CS9rovf00BopgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=Lqz_9sjV5USwVUVvO0fBZvZIbtIgLD9bVXlTZ8-xXYVYS1TfvgWJjvjnYJjONM83PyRXReh4vE5MOij8kAa1XEBecLa_pMm_OEYXUVf-GrVqj36T6WqPwJCQmc9-6RSImFNCvXb3qKrW8jSsYtw0I3hDenPJ9UsGA1C1WDo4EioEItpY8vkv2b7Y_hCUYcjswUeluDbfKi6VxU-fGki2mXYRBhR68QEuFdWFwGbDaiumqzak_6mrkvXq_-wU8h_E38zxlvNuWKNjTsq7F6m7H0anQmluIykJeKljoeMY3xvIm7fCgIv3JjPlL7rO4qUbxInAgq0CS9rovf00BopgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=YQmeKHYj6a7NtvOWFdia4W6vlVTXkBYM42xGWZD0iHmb6T76dBAXltBex9OaMACLnEXt6ijW73WCai-4eE80foV0WaDzvu351kv21tTA_GO5FbZRZeZ2BQooXVXOEeCKCiNq-KcBeTHyZJCBBO-GeycHACr7i_J-67w_uA0JMQ14o94cZrCeS5F0SVS3r83Fe1BUmW-KD05D7Q7j8dCEkbK_JAGT47SRABJQv85Knzxq2jnswU3drxT7NAUIbq917KLueSgcfVBqZH6YBnQApvsWyop0yYgg7VpP67E64g-6NpJrf2qeiOFFPplBWDmjEpPKofIl8u9yJ2eUZ6NIrFjW9YoDnzMMdub5xxV7_mJIguwqCGRGcqVOWjy3fqpqFvrzWHUNqRF8XzAiEJWu_udF7hHn9IYYZqSRQdjh9f6OunAP80aTcQlON-NumIkCp2REddVLgSoCZDAEnlTxG3VlueAqqBzwtjAJUCQXaFWR7Ep1j3_mh_UaWqF2V71BXYGvHhgNz7Aj1cEYWJSqpUtkqX6bReJ9dgHwKMOc0YsXE3Sd9m0KmHk-Qh8lNLW5koU1kyxm86F6Wul4FWAC63o3f0jvN-IYyOASYC2TK59dwwNQbXmIdc2bZxGh0dxaTYeVkrvQlk1DXs2l_q9RUGD3vSBvjdos8YyrbAJWLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=YQmeKHYj6a7NtvOWFdia4W6vlVTXkBYM42xGWZD0iHmb6T76dBAXltBex9OaMACLnEXt6ijW73WCai-4eE80foV0WaDzvu351kv21tTA_GO5FbZRZeZ2BQooXVXOEeCKCiNq-KcBeTHyZJCBBO-GeycHACr7i_J-67w_uA0JMQ14o94cZrCeS5F0SVS3r83Fe1BUmW-KD05D7Q7j8dCEkbK_JAGT47SRABJQv85Knzxq2jnswU3drxT7NAUIbq917KLueSgcfVBqZH6YBnQApvsWyop0yYgg7VpP67E64g-6NpJrf2qeiOFFPplBWDmjEpPKofIl8u9yJ2eUZ6NIrFjW9YoDnzMMdub5xxV7_mJIguwqCGRGcqVOWjy3fqpqFvrzWHUNqRF8XzAiEJWu_udF7hHn9IYYZqSRQdjh9f6OunAP80aTcQlON-NumIkCp2REddVLgSoCZDAEnlTxG3VlueAqqBzwtjAJUCQXaFWR7Ep1j3_mh_UaWqF2V71BXYGvHhgNz7Aj1cEYWJSqpUtkqX6bReJ9dgHwKMOc0YsXE3Sd9m0KmHk-Qh8lNLW5koU1kyxm86F6Wul4FWAC63o3f0jvN-IYyOASYC2TK59dwwNQbXmIdc2bZxGh0dxaTYeVkrvQlk1DXs2l_q9RUGD3vSBvjdos8YyrbAJWLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLrfPfXM14YrW-SFfe8UBnAJvDEyRWvBNwq4R8D0koRXdh_1Z5WDCqRF7lAtGc8vWR5GGJQH9VnKUyL3LNCLVmt64HmjC4bAqecS1kAHZykfiU1qDYNppxbxvq4po7-TvdzSQkevm11IFZ5iuxsciH8nQR6HRG5P1R-GNcGMH0LaQw3GwvRR_Gc5Leq-aAUQNkuwP-9euv6gkGmPiIw2JyMDskSc2wBm1CgUIs_YD3eL157MQMJrO5NKsYbNp-dHCP04U9Vg1v5-L1G6G36xYS3yYZLMMM_ANmggXtLydrjwsebrFrWFCLsSj1Bxnl3hJNGyzPsDVC7tW4wTtGwHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1yhLidrEaH7dS0IBMLA7iDtzrpgYEhXOxiW5kt7Ipa86pP0-ou8bAGlqoLpwe4iHG9GBEVkwxOy4MV8G7l1u4Tj6oW7Ts1BmRaFhHDXA3G6E1Sm4PHham5dkN8Y_J2HOK_jOkGO-Utr3YJ-0UlUKnbAQLfk_PibvGRWwfTCUG5uIxjMlUxf7epf9saiqE6o6Tf-itWtMRk0CWmheqWLglFX-Wnb14EVm48qyy3kYl1QmGuFvE-0JSm9oLMn1b5B2a4ziVy7WeAbw2nCM-jp2N1bPB6BIqjFsmBLJGaxY9DO1HnnZ16Ik-9SryeT9SHZaq_xvrpZ7cJpysYNua9pVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=XubR-lSPKFqFVJA8AqD4n6YSpeeVLg2Ofl9p9ZLpOy2GjgeXV230-oPuj4Bu4LcalhKvnPHyZ88OJmmKBuipq7d54EywJnH0STxYrO5Nm9GsRbZ27R_HTntIQit612_M0n1lZJo5vO0TKHTprZE5-9T9vpICLPaYYLolhV2CdOfaE1DCG4pxozKzP5yQIla1kn8ryppbscCUXWkstJFPi1Idq5IOJBOD9gkAov7XULcoVGLhPJgog-nemmaalhx2h0ufDoJ31aaTDqih_pxhhML0XfwPeIMGmVtc5vV67Q0csdzDBk2tga2OOT6RJZmliWlld-cvcp4JHtpg-aJXcQFaDSzQ4rmpMFbfkUkPSeiuJ0RKimTzX1FiZaUNRgCmRM02rOHcztqP9Xd5HjIKPDrVrCWIrzP_Wh99vlfF2bP-TEDi_5ureef_nkf9qXFT9_Z5aEHDh4p9JoCFHP0lUYGkiuAPuIatAP__KsXxI0LSSXuBGgPmaC7ssjJQr3r9kMzZMUroPhyyvRNikeSI40M7I2Hy8A-n4huw18vVJxDlFycZGonQ5ZxWysi_X-wBYGhIBsRg0e0jZIpalr_fnzNhLcYBEyZt6dhKWvIwmfIIbVgMmKk_XAiAJJCd4-cA_7afCD3tri_ju6pG9n4Q1mrRQihjc2k29PVJ7Y4uWLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=XubR-lSPKFqFVJA8AqD4n6YSpeeVLg2Ofl9p9ZLpOy2GjgeXV230-oPuj4Bu4LcalhKvnPHyZ88OJmmKBuipq7d54EywJnH0STxYrO5Nm9GsRbZ27R_HTntIQit612_M0n1lZJo5vO0TKHTprZE5-9T9vpICLPaYYLolhV2CdOfaE1DCG4pxozKzP5yQIla1kn8ryppbscCUXWkstJFPi1Idq5IOJBOD9gkAov7XULcoVGLhPJgog-nemmaalhx2h0ufDoJ31aaTDqih_pxhhML0XfwPeIMGmVtc5vV67Q0csdzDBk2tga2OOT6RJZmliWlld-cvcp4JHtpg-aJXcQFaDSzQ4rmpMFbfkUkPSeiuJ0RKimTzX1FiZaUNRgCmRM02rOHcztqP9Xd5HjIKPDrVrCWIrzP_Wh99vlfF2bP-TEDi_5ureef_nkf9qXFT9_Z5aEHDh4p9JoCFHP0lUYGkiuAPuIatAP__KsXxI0LSSXuBGgPmaC7ssjJQr3r9kMzZMUroPhyyvRNikeSI40M7I2Hy8A-n4huw18vVJxDlFycZGonQ5ZxWysi_X-wBYGhIBsRg0e0jZIpalr_fnzNhLcYBEyZt6dhKWvIwmfIIbVgMmKk_XAiAJJCd4-cA_7afCD3tri_ju6pG9n4Q1mrRQihjc2k29PVJ7Y4uWLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjIP78nVH8Rn2fge-Gs8SGUqVZNTubsh6GoDjFhJmfMmeABkTYSvLHWecleMjRPf8LL2muBnx7_V-8TmiUOpFPnHVxvtpjo4cc6aYPLnM0uragmgVwIVclQ80ZdYNZhfrp8wI4uvHkYU1prEM_SVXIK7l450ct3HUylhAjSSbU59StcO-dylgBnYlCE_cXURX09iSaV6FVhj7eMTmu33VeUCGRERDl8VD51rSO1Z-7u69ZR_r9XGY4n2b99Pv7uV5iQXFQtZH0aUt3prsEtR82SN3jgUXL97R6LV8XKm_ixWlCtrNCNpAgwFSu_EHdmWcfGRo8FFQda0RgLB75EeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqZo9_qa331FNzykjn6fGaSOK9PSgonCq1aLPUpy9Jw6LJX0dMWFA3q1U3nGXDML9TuTcCMsSHfG6pZ5PWesqMi5FH0fgeLWbzO9qzdr5BQgUBtXcIDEQl2XP6725b90aX1BTwItDEKMC2rTQS3CzRfsaEXSM7Yr5L8X3_OtntYamyIX5J6via9uuiqQrTXfoJG2GizHP4i1R86iwCKpE71_vAqWlI_anfVTZ32YdFOsI7fBKhJL5a_doRySCq4aEOzffSJiECqIXnV8g4ANtw_4YCi4Rg8nqekTUSc-QpFjoOSI-Xa-5b-cQrWaCaydU37eB_2-fZBJIH3MMhmKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJ6a8fn-TG4SarP-s_gTY2Vthv0TwORx-GnhdxdaFseRUAsmEOAPrFv59n6eXPR8w5RC1_im2CbXrKVR6cgSAa6ceKRVW8Q7tI1o-aYX6Qz1qEUzG7Mgr6zNfxCxWwLo0NRptR1u3XWCv0Yg56g5yRKgZi4I9yKMRbVRbHZxnXbJBv1U5yOjM7rfMChOhSS-P6gI90uWm7d-fHLY60O_K1HMhXYv28zHyknvNkvziyIx8K1_618DIcyx_NvNaGOz9-UBhBV897INfA8oJ7_8Cf04k613Ob8LFwNWeTM8wR72EfkXNh2l7ryaMw8QvIbGQ1TZySgCIODOydcECONqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLFlOofUGQ8iGgZMkU1UeMzaK1Qg0f4LDPNKhjdp1oekDnjW9D9oiAigLBvLLgggsHeAz3vy7FrmbQ_xeC5kx7vxnVaPOR5wEBmvqnELOC04PPYONDsTJ-z6RpOH3Yf1WYFZtdF-nR0nT1AkGox4xVIrc36kdrm6Gbwglxxl_iSE9x_st1LkmsLoNQTIWKrwDfQt-2hN7uT_g37v2dmLW3hqi4GrfBRgfyP_PUasjeo7ju3f-lRi5lRdUQrgqHbms6RZEeCsYJ4V-ZGu98t7KHRJht7L0amw8I4waqlTAqnzthR5ckMwxpR_84eiK5L60qGeqKe35pvNDqsJ0REhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5S4S5DS3GJG9FdIQXLSoLojV4cSyk5lEfwJhvxS2kSkXYnBlPN8AB3gXmVQtLlqVVAEpqK6IeruOw0ZXGO7a8LS6t4jGKExaQ2t1taAB5GnFNyS0FF7keKXWys-6-GkAxzLNrDOyqkF77s6RhCiHsfySji6wJ5nIEfIoVnUEjJQynT8laMBr1wICZ-SSce9XHj65tBjuLqCwEy8W90Z3b_E5unpixHeLjzyr_pme2Ghb6xwZR_KVThFrytrTsIMzmzzSVL4mOxc2bA6IHWqJIewwgX1EnCyRGHViQ_1g2tPa4kizu7eg3Csnvbof31TcjyFMynLI4KKPKxlPDtsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuGO_-gwHlpTCu4vC-CUQKz3jAvxVVfNHU8Mw193vZkiwt1ubYapMALQ3GYErJpsLhmvYRlODdcE_d6ULa2GcI_K5sqSMoWaGtozs8DX_Y1Y2i6LTBEse9EYj5jg29BN373IXdNMqg2QIUJXqCUcUnRuQxOiYmbjZ8L5Tr8RTFQCDvMibJJGOkZp6d24aqRf1aVSWvATZhed6MuzgxoRIYFUSKCRJSFuxCyUP21PA1FTRD8grDRGcsVab_uvS466OxvKi0f9rBMdiNZLgDN-flkgBELvld243gC2l6fMreYgttHH_z875XqnsVWjQN4ntlednDPcVszeOyAbLvtOew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHGP_PX4qw2ZK-k9f-NZkqHtWGiBJGea86bs4okEgjdtjC9ZzlrEbptLb8iwe8y5Xjn3gQTcoyabzqDZyHoGSJ0sGXBxlokbSzoKY_4W23Gw9lysPb_--HOQ41itaMaqhP6GrWakXLn5glxKCEWudHrZfMnujX__qc11EbA4VbdEaFoPNeIU6Ep9Nf_IqJuqI_y7ZL9bjOUte_D3tEJyeBTABk7vlXm8eBEDuGZrTVTEt-ZYdaG9EgMoo39weO7iS7uJ5-n_Sdto79Dq1lRugni9kPa6rMS-HwHmJcF0YoDhmxkVPX-6KX2UpudnO8_8y9ECGgAwmb8qFENJ1HXYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOb4r7_C1woEAp7Rd0y_um-b8MkSCSHyUmT4TkyV2IPP4trRHN58ZYutIb5L_QqsLwgywwMtoe1rd_JBeyItewG25Eco72u7FN-llJnc15tF_cdVlVVgjbh0UFZZKJ1te036pn73UUWUGsdyRp9Be08Li5QaD7ZrvXfCtmUbEMfi8-xCSDSt3eQEPujRlql7mduopANndUivEt1fzA3_Z6cyWpwrSsqEvADpUSmqRi35SNAd4pWlEAESCnXQTTQ3pqVoTDRNljtur3hdvg3nwwtxeQaA5md3SnTPT_bMq3FvZIpR9BnG4DoAfLQlDvUisQ96gMer4K8LgHE18HXhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndP2Cfu0DWy_UfWcIF7n3ZvKIcb76vS7wSF5oMlnjypUIqV0Hzj5DfS3QKTQu4T6PIzRB01EAKbUBqmZ6ZXdaFtHJrBADTCgqae4VbdjZUpLA9DsDP3MUmo9guPeEPruWq5HowvWptKQTW7orB017aODIyzMxHfKA3WWUI6HKlabNBFf9wOTvCMblvWGPwZ0ker-l3m-V5eeuHRq_Wu5g4rsbiIM3LQUslUVyhRnxEuUm6Prcsx9CpYUo0o163w89F2Vs6F-6FoeYx3pXqFS4n8bjzQ-A5_xaz16HrDPakLfIu3aT4DwI0X1S6jNrlF3SoUX5jVvifzAwl6GUMovZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zntb5LnTTt8YOJCOD_qd_QsYweCumyLkltEKU0Q_o92tXSDhF-d99Tp3xSbjBQwtBTIro7669eAU4Hh3lzBQfHGm1YBnibIjkoS-_IxgkBNO0cACX3h2GZucyG1N_p9ISwxeG0NAfaQnwg6snadKNhwkrLZEE-qwi5p_jJ6gwJlHGjJD8nMjWmLX_bOYlykPs9OF4wnbjvJnSCmAuoP32xiFSxz4ijdibSBTA-caXOY8M4zU2_CrhB7sllyjSxuJnTNwAPns-Feb6UaCVz1dVH-UZZ3lqPlm-uAc7theY6Cdsuh_t3u9WME7yXwQiLWxpwovSIcmZBYsbtcpkWt85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0lJOQSU0U0aZlH3uKme15B9-rrLbuswS2LucWyqqesEJs3INwNI9WXwZXsFpcBml6Qr7i4valWShSEqlVGBKF2skaP7TLD4sFuHO9YSpR26O85kzoKdIg10s8-TDiXmrWbh837K-4RBsnLCUBChQqrLtIcGIRVBJny_BMIMiY2Z4BQt7FSRLqwyMoLWpjHlRVQ8YXE22k_v9s0Sl3ZkR33wmajVM57flHqVqdbHXyckpvz81d4CkcdRg9-vq6DIruzetEi3gYtyKhFSinIT5moEGHPCWta-7T1a0RyaFvMLZAj49Ygj74eNbU7BAs8mmZ2mc5LtIxGktqjKgYwV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
