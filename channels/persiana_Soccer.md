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
<img src="https://cdn4.telesco.pe/file/uQhk-sN4BYEX2u-XZQCdiJTOwlohhS5TRWvkaDwWKKRR49SEu-Gj0BKi_kM2efxvizIdexUN2xtbsgIJAjSbZ3eBq8TtPqNizxI10tTxJhHB8ihTP1QcJWQ_4WuzQ4LCSGS8CB1SC9ZI993XWs-7i5SYI0GeyfZMV6Ac380EhaEeJdWbgtr1WZYKOuzyUwkafw6z_Bi1hILqGJZRfZKvI1FmG6T62hfdF_YrWaRLlD5QigJg57owXM6Ta1ZvCpmry3O4c1IWMwxO0XmcOvZMy9pWwjGaMeE5_q1_ojZZ2mFS-if6vlpg7DazDDyTWhHujA3NNCPAVx0mpxEUM1EyOQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 356K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-Udv9cN13f1Enyax2S9JS8VnWNsE4-sbwMu1UiA2073DBYpc1co6o8ter_po3ddWkOzyUqDPlE3yWYzPzbeSrtIrYqKhYSfUjvHSeA_585CaZtAmls5I-AYvrZ4OKmZdlTczg2wtSGxPMD6ROELsTw2LAZcJzJcTKvG7_hTwmMrLoLGnto93V4EcloQW11kygxvpIlYKWNq_he-GVrfb069QAp42r693L1JtOFjzJlqQS0YRpBV--oDMPLkoi5ena3NP8pSBxZ-GoNOE8NjoaW6keo4wZNQlnlSdiGp_keOg0ht42a4gDVe5N8AHjSG2uOdIf-lSgKPpMVwTATaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMN7AT8fRVngPS3XUv5d3wc8MsNkCBF01IRFEn1pcTCKpBgbLwPCxhmwZDa-yEh8zfkMInVMyP_jTSKoXV5juBtMyZKzKPsK6qjOadKgD33BGzEr4QbptHtNUynTzjmLmc-mKHOu3JCF2Ad700m4bZ0o87V0sdn6bk3cLgHAnhtUJR3mpdrk2jArjDuHpA8GU33roh7A0Qs1gSa1XmlHzWblFP-uxWrebV8MQ5H_y72SgSgBs2KjvbFrdrWpXOoRSeAWziK04VefQUFv0um9cLRY_mAjuMML9irTxLyKu-myUw_H7-IogGugQQl7gGvUosIGznTnWJI_MED_x4dn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLjnQQ59dRRCgV7u82sDsnyiy5kzunGlS8pZaSDZGrxZ6T86CThu4IFcdenOj0eaWFU_3L0-Mf4zYY70F6DyGAEw7JjEb7PlOYq8fQNTZySu5cnni-bz5WigHW59CELTyN8JTYdWdGdtKe5oFf2rsuiqT_iBdUwwi3fKNYhrBsAz5QCSnAzfZg0gT15f_XybORI_TUL537r70llv4NWdn1cOWvNNPlzH-syMBddjBacusTQb95omkknjWLgYjFs3IVizyULnS2UeBCqmJXWuU2cR21g_a3M1M6NMyYrGFJKdy-2G0qrD7hp3kuafJ7ngYkoadVmT-Qg6acVT-gcgCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGwScrGnSsY6uswge5bAXPzBNjLdDutkJJ_2NuEzmx4h2XB_ULAx5JGEy7M08oeFP-M94WhYRA1YZGGxnJ0zIYI8TuzBNFkd7Nu0TLBe6xIQQskIfNkkinLr4_a9uTDv_QwdIjXzg3NaJEouPxx1sEIzdx4hcUdfWY_xarTQa3iSlROYhO4UsZAD5dAiiT-yGq0hZxb6om3Z8V2KQuHotzb7gM8s3gUdXhIWmwbko3hN6AFA8ezS3CDSvbs_ke695X8RfTwzEy-VcLkvvru7rW5sRKvnFhZSNbC3Rk1JJ_nApIYPMdCvke3vNVENXR-XFy4MgtF0DT_LspxVmIsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1LhQXfUAV1hvnLemCvuhVrH58qle8UvTyaFDlSwF5wvFKp5feNRGuCbYFw4-IX-3fzZarideKCjVEsWbVA92zUu5o6YnIw5UHDsJ7b4iEP-YOcyEJp8xlIoa7Y1BcTk8hpseKMwjSa1vvxcn0TUnzS0Jgi4MVZqHYTYva2bOUFsBValbLa2K76vGAt4ovsU28YPfTARNWSYgYYpX-rpJ8GQbIOVOb4feqLCRqzs5mbQE_e36sgccM9DUOm_q0Y2aRXGY799Jue-q6AwBIya0rFQa95rH8lNb1DT1RhcnbbTuwopW_4qgBZ7kyBz7ZlVMrde4Leir4Afqrh-2__rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkjvtxCqd_7Bz-cGUSWdTaq0IIjalJIKyEQlu-XOlEmEDDfLrxg-uQUZO38Lt-JZ1FhQDL5Y1aFSfmbqA3uzEtk1qD4j993JGr_5IZOWjP5sKDyMZu1pWihPxpYSGrauGh-APoWp2YldunqbTXCnOdWRQIVD9E-BijOkVpMXHMOwPq_YstVXInvyS-d76XhzcJRYGIuioSVv4uhJNqsEH2iJU-ZC6vCTvMNFLC8aJHmsJndJQ_syFQL8MEvaKLBWWx0ICVhnmJTwOxXBrDdaDB8p4o-IIMxTFUN02MAaIzKHrhZruCcRes5X4q-_Z1Nvmz839gQPMbahCRrIUX593Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات
جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت2.500.000.000تومانی رومابت شوید
تورنومنت
#میلیاردی
🚨
همین‌حالاواردحساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24688" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=S9fhAAM-J75y0qxEQKf1CYkpYA54zSx7Gi76-KpF1TGX7HKkRrXD0VqiX6QMMrGbpcP0_Lq0CU4Cg0dwyWRRz4cq2jl6Od7ZDx7yjHVdWlryNFvaCCLxoVCENzJ97R5rsyzoMJNTyecBrso4ifGi8DyHzHMrxncKfjKs9P2QCyQYWrNcKJY7EfLQPPyANTN8CjZgSa_CLMF6sjVlybIEEk741w5BoHgMZOfqjhZoREhFlv7CdxLS7p0BLLb_tDHnJJZvYN2OvpmXTqov8Ik4WEK_PuyAWBOvI6OwsKAQG2rP6WhsqqETOiGn31Srpw3aEY8_UvrFl0JYxI6j4m9d1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=DayV63JvBtYo7iVk59NReyoqS1R3eIxpI5fv8GAm-IB87_POCHLmw5UDQqbO_ECzOEyV_Q8GBmOGMOXiTK7BdZE8tHPteeLq9A3A-Geq5rdECJXx1I1i4DVDrwERCIKKkWsgADyvYeKNyBo_81haL8cxkxvnylYj-M071bZSS9AjylqzUtbk-QIswIxDZZzUNj91nlXVdSDrswfGMhOuyWmlksUW1_bseAW4tywYKvBfOw4I30uEKBVqzwycInNSzS01BO5hiutPgKWv4SGO2pYbrSVeEoNPBNRQbB0aGoEXRbWv_11AgsQgj255iLMW9UgUbuSkKe2mI_r5K19VWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLJgzDWZcG9AxvwON9lYhceyYnLF4GH8BZcYKnzbPYSbC5bVAr_MLEhNQqtRrpi4RcioAANtBgldc4svRg4U2bl97siRHtheVrIPzke7RvdbGvLhH6rCu7XYZt7-Lk8Pf08ZKG7iAILCiD5oq8GM3TEThaR4p5y3f3_5RuLWosk1jxNDX9NoDor5mtgmmY3U8DvxD8_il47lgLiYUiAWOX_tS8OHD2hCAQ7MmODCsIkwqRTwBQLtNrZcYW_C-ihTu81fm0c3rLw7VX7gLaK4v0-J5CpNf7hTIZf8vvqDXL1fC6aM9ALqs0RRSs8nBjiwwxGSIsRBC4P4HMbWQXpJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaCUPqxv32UYRku8h8qkKVQdWEAK8MtSQSZgjbsopbpTzAaponwwGxuokY5DqVCsnJQVLZpjT0jAZuANXM_nQvuBLPdjc7-IKXmp0NpnkvNi2LnmPGR0GEEWdHc8vzQD4EQvMk2wKbgGN7NuoZL8yoL3eF-pMlhW_JEbCnMJZ_X1kGBsVCH9eTc_BRTq-8WnpedUqejDJYhIUmIc5Mu5k6FVpRir2hOrsxT8-3ZHYfKNym5yEY4d8EelsQGlhyiAt9P4KD6YmAPR942htpcoW3bExbmJvk0y9iQirN9flb6Q1XaGHTqgF3W-Y-iwIG7h7T0cfinnefaydKflRMfCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsIXrE17XfkzWW8239RTeGd8uXxt-lz3UBWK42K4uF5GFgeowu3kJOdxtINLIWjFMQ2QxqPgQ71YgAWsnBXCBrO7yxOuK5_inqNfR9S9plfXdlP2tvA6WNcjVozwORoh3FvFBBEwaqbLEYDPL0YavgEOxWLF0yo3QEngIx8j0uZccz0qnqgJtKkGDi9syWYabscwXqfD8LcXHzgCQSznHL3bjZSPoP_EJvK-7WXMlwOdC2Cbw1EVUIl5heJYF80cq5qV0DAN9hndZO2K46pazLC7pXGZlELbyzOBlzNUJxmI9f-sOtGwkIAV-GNtj9_JVBkRgdDWukeenfCaJEaQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=QC0CcCVNr8lkSet0WcVm-rubgZTv-st0xs56uYPnF_IHywM2eFjsGS_hZqZsPORGr4Qi3djSndpFm1ux2Wc1SFE6Mipj8hACInQ3fjTQJGp63GFv5pvY1sSUFhdcWc2O7WBdBaSZlsXn1lfhZk4lv7ZXXL_Af1xoWdYrSMmF_npjpWTJZvCg8LM9fPbivwqPJQzrzKquwQP67DqJCRcKtM1E7W_GqBdu4ux5XrnVcczQsOa9Pjys3GAXXhW-PdCJNPL_mqQkTSiBWqPhDV-sYabjDGDtdAvaV4DLpaz13M0cqQ8BzAuOi7W_6nOd-IX9GlDtVQpiowQc4Yrswikgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESibDmisJKlZ2zyEycqGMW2K333jb-N7lpBKQhkLy5trmW6yFGSF32GgvOjVDYvVJeNwnhzs_Tg3ILjg3fmdlQDAawTZ51pzeSao1mg3oZLGK7_Eui5uZA4xmCmFSBqXp-pa2DYZY_y5SXH-X4Zs3SqxPbAbS_CeN9CkcFkwG4hRbadD2-XIPxeOhbqId05TcolPrWXD6Yi4QeJ9GC3toobkkmIQF6g3n01L3S9N_662qBqLPfhSZwLlxNAB2J_oOrblY9kxZJMcsPLWszT_TuhC30BZfhSSzOk3M3vU9ATgIoybrGzmjXylZyYj5fLgzv3MJV65xOhpxedoHRO-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9VqGRQQwqWCw7DRSm5IRDFfkVW_AChBdyXlUaxdoVe3uUicRVMB09csv2FibYrSmeQpu63gol2w4fU0bVSY2Yzwbii54G_IibMx6VCsZdEQ6-TDHL8LQ6P7NvLDWsNOG53PzBaGnK-qlJOsmVIITlo4p9gUjDiO0QJDjm9YAD0nfaTX-57-fnNunrK9zuw8SAeNHb8XUEEr35R7xDXt1Rs9AgB5ezni1k-NuCTnlymdvB7f1qGPq00lW4Xr9iK_aWfTzlx4bh9zCksjT7A-HcfeYXeczT7hP2ZEMYn_OE1rd9aqxcR6CcTY_rWyvxlovltOJsDVz1u0eOTEN0-iaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5a1o-ts5-egllzUBeHk_zg0YUrqQ_f51B-vXYjBNF-WZJwREc7u112BhGxTxqvFmwosPrYZe4o_a-APzoVlSWDolwBhviZsmVCp6XoAsP5YkNGpfaZe_S8ob0Gf_C2L9Fuuh1W3vb9tmdzi22DmWioitKt6p_yV4B-cO1KFn1V0HeUuLNRyTNUJYjyY6izFoYVdZMyshzeAsQX6PLRbv1q5st9pE8pULl-Mv3yTas5-FOyMLVZvSJNfQf3BcNaPvRUVrxQYK0vZGSpwGAWpEoejubFCNsOW5QmyFB76msG2eWPsBISiaXUzb1B532VO2ytf2xT1ZhWPSuDClWYIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmayYgkO170ckdvm_x-3h8bxi9DgB30vAeRIVswYJftkvIJhQPQx9LQwIlNnB9wA7vww5TI80KHHMwoqhGWD8zwKgXw70BaN-g60z9c9sWJEjIggq-KmPUzY90U-h-IAgIaS6NS_9YgGhzhOggDj-bS1BQTAHEXiFRfrTBziTipv0eq1dWuo3_hjUyoB0utt9BQuJ8N93_FKT0YWz7k54RV4OZWWEEI1eNErHzrdGA3vYVLaTlzO4v__NxXKm6v-uXLmTyxr9W9GeOfJcKNmUHY5L9YulHlEtoTTtngPQkDx0bND-CGmnoD9e7F6cN_M7v9NGL_REUBVBtNfY1ai3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUDTzOf3jhg5g3q8R3rxF-ssYHIx9VOswn3pIVdAIuxz2jxqBOi3LDIVulByD7ocmayMR_91oXhLwPp6XEzQiFEiuepZMnFkRu3cO164q7CP1PHxL9i6S3xWmGEjURVXXpWS6V5TOg_4Du85qkdP5-27OJjHl3MvdXs_i-ve11ZWeKg4m8-SVmNENFHBC93jHxmLzXSHys__Fj1jqnbOUbt1CpWURItMWKJRlCHn7kgJwlk58AUJkuZCV9lIi1E-Z6N8w9eph3bCouFedim-rJmEEI6OdF3v7oyY8XtiW8bWQX_L6zQXKyPXnKqhMWhxE4AAq5OM6jpc5LIhUVxwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWW7h8eV4XQlQ-eixZhR3PMUr_D7KXswAcNTpZ0jp6XXHgWPI6eFgPIIjahPnGE8RzrqlFn65B9GFaEdQT5jxPo5ImkY3bPUsmBvuG7yTyCcz7mTAL9UmbumIezRsjnaTvY1yFazRRznZY5lCz_RzxM12AaC352Y-dA1hvsUeglPn8u99crJ1Bnw8cD-lOwQ0lkI_kjAc--klLfheVDLErisGw-2uuCkCmftwg6IGNWWPMtaDuW1HHrbf-uqo7QAwsVEit_SaHZz4tjbvyocYxxW5Rlm2EV3c0c8A6LH3clJ2z0QT1lICSjKuj_fCc2GEMmt8F-NLPXXNAAOiNEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpbf0olxWIMaw7ui_PDKuMvAkw1D27ez2innIK6SmjaV55_Kd0xBBgLrZBfPnQVNLzkU3JN6v2mJb2SjAhWv7BenPGeoZQDlPj0w0qfplR342tcDj1x2H2aDH1Cb4EPcyZKZMxWBa4kOD6nPSXMKU7dYL_AI8wB6rqqZwifaUp9pl3ow49Dffna4AGKwJYaUreB16AdDlNXGb2Wq7FR-iXGpRxULd0Z1WqywqMwNVaeq1e5h--TtYiD2YSEQvd3yjFAihhUClvAF6qupbrtK4NUDpPbQwWTy-y_11nDZzR4qYxCey0U18HXHQx8TAzKOdWeqDFlUfcOS9uK2PKjmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuNRysP2pXbhx6dBhmffs9qYEuRh-HNanUZZ6G_ol8Us_W4L2YlFUo1Ii3V41w2dDoA5CuOG7UPBAeSEo0X_QworDVFcD41aCaWOwRJK7GyKYTBDx5xpMveBlbl0KVtp2tSHxvO6KyfFm2fhv9ca6z1zOKGmDuWyo_NEKQJP8hKguMvvBLstuDNsfLbMUDLNBENT8d5XySyHX2_oGOz2lldSuOhRoUpxe_eQa5ZJSaycP7MoMiAyASA7lmEqvccpy56F_sId-sA_09obaOpvdBKT0LMyxaCTLWTSXvQLIx7OcG1Q6baZrjADF4xlxp2eYxngwHGG5W3qKo0GL-aqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=oG_dbmZ5BCtpFRP9Zgd4BHDxNVxJU65qszGm_d2DUczZMb5hE4Pr1hcEu5W0dSiX_9pmJGIQs4_jnA6sMpiS_bJVxfeilEnkqk42EbE38NWzuSULIn_aDcGEx3Oet2-YR2dqTit3jWDmmvWg_oNMeCKU1MV1inVwlk8LMgmAPIZpe_ZhWOSGYm5U0ooXEbTkO0tzzcOcxxsoryQ6vDk6MiIm1-T9Row_8Q23yC5Hqa-nwnE8UzfI1Wy10r8J_Pf6vfsQx5KqsUiZhl2K68OvzAkEQyMu776fYm5f75oGcvk28EvoUas4-3SGmEbeC72Iik7B0c3oeqLsLlNXAIOnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwwkQAdIgZvGFTFueIHDL5OVof0RW8FqVwHTcNK28OKlENjfcSzGQckxGAGG_TXJ_tpGTq2dh8Vhj5UgOMByOURa1iOq0EWl2EpR3uBY7xloHe5cU4ikBZJJ-KtJ-pdLul9S5LaFltEcjFp1au3vrg8OGB1P-tqY_jER0ovGWhhQuIQntYyHs0kkEs4WefZjARveT0W28LHrqT9I8dEvUWy06QhpfDiq9T9fRHw8KJKnEj-oXjNuSqlohTDJAO2xoh-ERjA4xSIwcg3gaYwAUI6N2sIl2-Dc2_5M8YZPE-DcsQoCyqaO0KgymKDqMWrv4j7eGAstUqVu2iG2JmeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKG8s5jfuAEvWhCDnu34iHDkapsc2kDGsyVMVWMz32Ez5Z-6TLR_ORMx6-9RdVUXar_USiu7H4tNva2v_eXJW7sIQbxdfR6ZY677L5FsFccc8kgVlFP0YpcvTzCP82aS6b735GQ81Lil3VKn7MeMw9-PZqbcSK-o8YGdAiELxPmK5UEH6f7a4NsXqhVr4VPIxhebE1Ps9g6Mpq-fXk3HHc_yDST4K6WazAnm76_v-HCUsxycsGnlhQxvVI_wZVmJwiRwWLZSIIez2QzIIsN22pEzDdk9OoUqTQmHBy2wz9Jg7wHByZsTHH06r3X-t0F0eILECDGdmELwB_3sKl4oGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=aWsOaYbZHnOfiEp5gQ5uhzEc7uGQ2Z7ai9XQfdw6-Ml_bSliaOWvSgMcyqc4pF6prkW14Blr0IdbpxaDWcRZBgqPxKcvV4GuP2Ltl2NOt-5SZ5CNKz1-srWtd3KM179k2YBs3LAkxR68j_8XUHAwKO6ETRhuhQUrxIEWHyH8w8LppiT32blFndxTRl5GbyYMs6A14_Z29h-DFf1Eer-9T3mevM4v-igsbfTjCthHusZ6M3e1Lm6EUcYkYyWHvS8fLuIAaCCkbWKOYhzMoZ47HM5A1HfR_6r3X59JzdkiunF3nLyW0aG-3tbvGWWAGmGBanPHM44z9C6Z_h38cJBykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=bd55V2NdZB9sAz2KqvNNJ4j-z4KeGEelgsYdUC353UboAXOXotOYYkOBDXZnVMpmLPbFRBSUKPizH7GyLMjGfkf-xRfVFpy_5MTOoDPkwOWQ1HvVRV-1rxeEYa7RdGeznE4qwAX1jfRQKlOO2vr4bDT_to587xiTL43zkCE6Pie52CoH87oNt2cqjMVdOjEagnMbnQkdPog7V0jimFLd9Y7S_NcCMUbXqebuOyxn2L8-ruQrvTe1RkipR0AXF4k62_AKhM2bL6kKVYnYF-cOIQ4iFkuZx0Hj0-GR-wMK_jjRNNgNndNwncLc0-gUeHtBHqcz4gOiG-MeMb4doT92Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=bd55V2NdZB9sAz2KqvNNJ4j-z4KeGEelgsYdUC353UboAXOXotOYYkOBDXZnVMpmLPbFRBSUKPizH7GyLMjGfkf-xRfVFpy_5MTOoDPkwOWQ1HvVRV-1rxeEYa7RdGeznE4qwAX1jfRQKlOO2vr4bDT_to587xiTL43zkCE6Pie52CoH87oNt2cqjMVdOjEagnMbnQkdPog7V0jimFLd9Y7S_NcCMUbXqebuOyxn2L8-ruQrvTe1RkipR0AXF4k62_AKhM2bL6kKVYnYF-cOIQ4iFkuZx0Hj0-GR-wMK_jjRNNgNndNwncLc0-gUeHtBHqcz4gOiG-MeMb4doT92Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=t3BD89_-2mLrd337hZgmVChn-xEE89Pt8KkBuQpXGSVxBONsOMmJb1XQxFSM64gfaQoaHdkaswMgY3QbFgGBXjBO9Iv7SIAKPbzs52Bbx5z5I1J5WGMnAbg7TM_xDVDfdiWg_2rLqv2x8iNbrwgDvYU_bV_ZQRWaAOBy5qk_dRfdmFsa4NKnjE86kaTT4WRho7HragIkbDFnukybjs9eKChs5mV15PK4BB8gbKYBcbempes9bEQfAJaac-1JnSvTGVzc-f70dAS-gIyRtC-aHOjxSkBy63GTY_pQwEbXKK6gH5ikBaWSCNZzEw142lmYF1s8Svkn9RtiK09DMMcuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=t3BD89_-2mLrd337hZgmVChn-xEE89Pt8KkBuQpXGSVxBONsOMmJb1XQxFSM64gfaQoaHdkaswMgY3QbFgGBXjBO9Iv7SIAKPbzs52Bbx5z5I1J5WGMnAbg7TM_xDVDfdiWg_2rLqv2x8iNbrwgDvYU_bV_ZQRWaAOBy5qk_dRfdmFsa4NKnjE86kaTT4WRho7HragIkbDFnukybjs9eKChs5mV15PK4BB8gbKYBcbempes9bEQfAJaac-1JnSvTGVzc-f70dAS-gIyRtC-aHOjxSkBy63GTY_pQwEbXKK6gH5ikBaWSCNZzEw142lmYF1s8Svkn9RtiK09DMMcuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsNarXwCFv3HATe9SUfvNuxtHIc5DloqVSUZzm2f21PIr8IP1ojUKHXM6z0udbn9Z0M_67_SYPHaU9vGfppTZe9mHDXIU0NDh-O9_ozv9rGEG7LzGw-MN313av-0iXJpm7kT_VfIfGkPTTF3u50NiT37Fl4u_VK3-3Og8g24VvFFa20BRSKBmkgPxoYL_43HgpV1YdC6I9U4OIakI8oFXsiKN4DtkgeNbdoziWnc7X_3MmpFGSOJ9LgFEWou8OiWNhD1FIwcApNVk24cwY7lq6kAZJLx5_jIDXCFE1pO-v3zDq_syU0DEpu7jUJmPGosZNB6bZGVxa9KsdpM8oj7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlYwpIgizaEN4CGY0nFyfqtovC4VQRxt9BSypN8bQLa_mAxIrcyK0OokYWT5Avm3ot5_e2nGWJ20LnXoBAYERd0Z1Rer8UhtUb4RLazvECTUdv3il9yGKR37Eo1VUDxme2Uquwucp8UAI8WcyW8YD00XGzoB9GpgavPZ5_amBH7AmB6GtHdnSI3UNVZM664ACyZlKZmVmSCS-NIMb0grbVqryom46hMmphpEmCqx7a75cu5HQ-m8VMp0Ys3TqlxtWiwiGG1EPE44-UhesOD8f0he0VBreZZFVleP8cCk1T60goYTuFDPLNOKC-3gGFHMKeuLtslXbpIqBhWknaiVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7jEhSqCwQ0bPVD6Nc7dP0zmEESyVEGVXQw8u_-4QrtMN_6xczzB5t5gnjpR_9UyWceZ9Xs0BNlxoqBwGXZHlgl1DK-R2cc7_mXZ8gxaHQ5glzY5HvTP85FtH0D3zq47LhIfqM0y0ps1ATZJ0jRwAT74L0yB5grdJoujNOr8NNisq-Akz52lW3yAvgtoQPKQEhIW49sO_rXLIAVxvWJuOoGNray4TEzBEg3BEJjJ7CnYo4YUA8bqHA9XrhU3dU-wmpf90xaF5-RbLMZf0AJ3s7SecCWHlzvY7aGZF4D4TADlrt2Bov-xZLmiskEaoR2mURArT-BJpQzeWZv5eWmefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از هر واریز
🤩
🤩
درصد شارژ اضافه خالص هدیه بگیر بدون قیدو شرط!
😮
تنها سایتی که
به ازای هر 1,000,000 تومان واریزبهتون1,200,000تومان شارژ میده
اینجاس
👈
این یک هدیه کاملا نقدی است!
✔️
هرچی شارژ کنی
0️⃣
2️⃣
🔤
موجودی خالص میگیری
👇
🔴
اگر هم باخت بدی همون لحظه
🤩
🤩
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان r9
@betinjabet</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24664" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB0WQCC1hO7U8ZlRN-Or8VHWnTlXmPK4sEYlSnHxZKYY70KyfThLpF15IBIKIAKCe1UnSHNPlFlq7AH93d1MVWkdZ_F7h6P3lme_oYGo1pltk9dIF4IFDbU6LVryc88zn8krWpxS2QYRlMNozpa_R6AeRZoRi2HJ6lwruLc2ltzwGKY-7PR5tFcSOPy3WjqHqkQd8BXh_1wJDgDVEInMnmHb9-n4sbZY3cE2Jvz2iNyvdXrCwLQsP-MpqT3p63WwenTOyx-5Unklssr2Va3jIW8Amflojr3TGYUcuGnn6JFIT9nluEgPl0okQhXWYp781xQ3rAPDy7DbYfEi_1JNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=mS5brCC1YBHfzvVXm8GH1lgVK3x1D-ePk_UCcPYG9eJ1Lwvd91uAk8RhdjB8tqkLNxy7dCats2D61kcRsMLsTP2kvTquRcrbEqZaRRGY7pbF_v4F-TVEHDamqTZFjo9hXT_r4HYjqFq7ZM5fgmh4yQAKfVSmGdg3rnqUvWliGIerfO3RR2rI5STLFdTcbrz-irb_NJ1SUcRfRWqzDGFZsN5fwm8Y00sY8fc6r3YgV8lJokOI6C_EEQqF6SpkHrEN_FvfZIBR7ozsCfhlhPajXH6CFXlRCB7ZXfXDxtN0h_nmFMCwNJv-R2dJcENKcaLLfw3v7p3NK_Qhg3B-RIlt-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=mS5brCC1YBHfzvVXm8GH1lgVK3x1D-ePk_UCcPYG9eJ1Lwvd91uAk8RhdjB8tqkLNxy7dCats2D61kcRsMLsTP2kvTquRcrbEqZaRRGY7pbF_v4F-TVEHDamqTZFjo9hXT_r4HYjqFq7ZM5fgmh4yQAKfVSmGdg3rnqUvWliGIerfO3RR2rI5STLFdTcbrz-irb_NJ1SUcRfRWqzDGFZsN5fwm8Y00sY8fc6r3YgV8lJokOI6C_EEQqF6SpkHrEN_FvfZIBR7ozsCfhlhPajXH6CFXlRCB7ZXfXDxtN0h_nmFMCwNJv-R2dJcENKcaLLfw3v7p3NK_Qhg3B-RIlt-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG2QVJddcLa1WnzzHtP8mWyl72oGn_iBmJ1G4B74zfmVSsx5xR77UKXmyFrPU7Xr_q65X9k4oqrtPgc3JRxpU5KYE1JDQ2GsBtORBSXTuTG4xN0X3NuwOG3edih7KPMc_9K00ENhbSu8Q9uzt60Yxjhmt9Ox5SA3MA2m5qHe6rFf0OvgkxoaUlXIx8VP0BJId2WUXnoeLEY-Rc0pFbWMhLVP1lCbQMTHJlMG7ztShXns_VHFCVBzZcI7hDIfz-O6_s5FeDTtdsEz_nWBU15Yt5PJlk_ooz6DWzewNaG5qtggKFHuxhoJ0XEBH2-UvZfyJbEllDJBJ7q1HTOUmtn91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feFBKyd0UrX4NnyEIi6v9d26qAR5qG-5_c7iwH6EP0sTsm7XSSROLwtmiH2gyC5Nk0bmPz2apaEHe4SLE7jMh6yq5yeik7gz3CyXvlEmoJqIufLIywbYqEYS1wmEBIA52KRySrUZ3jZoZniYI3EA5OVXfwhzpNKNqfiDZovTJspojgQvklBrwSnlFo9Gy7F4rAlJFlJr8fd24k42kcPWCvwU0Ns4wv1-H5t1jSrdOLodAHFCGHyFzgVPyhq3m9rIQLkJv-SzHwE7Bhbft7a7Mp3qf-tYcKf74qf4coF6S_kam8JDR9rI44SZovAsHSIC2DekEWoUvubic9aKPBJTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmt46wNQ5ZSzwFgJd9j_R5-t2AqzQXTHEAW-KrDrgr0DeDeZzSd_hjzOTiiV-_BUMdq0MIvBcY9OJkHwPcc6Wbg6dcQieUzi4KUInApNQ7H_On1WMiQzDTbE5J9JbZaLKYxIICuVW_G8ujgJzp-MPow6n0zff2O4HqlGeRDdw9DQN3uCbMYvQsXKKqd8A2NBE7YaMAvmfNSciF0wWvCOM223J1WG_6PvNtt6H0JDJ_1wJvL3GIuP4fBRYmBRT6GGxgEY8nKwS-c5WntyAGUqcDo_dpGqHFciG1FqIHjS7Tcie9_O7mHOBsR6OXGHOpk2cgJEBwi4lDsdKo6Klqn1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=XdrMYvE_ILZyzJXedKZbezCUZDTlPCpaSAqea9mV6y5gVgyn1i7DaIoXcH5Q0uqZ6vgJJ0JnErdGIh6h-vd9_q-QXz_S4q-DbCU6qW6B7_A4uoTLuT5F1Ut2ELAdvuyB5n4sa4XeDxKV3dl3gROM2FD3gqIxXAkPH24tU3rlbceZB8yo8OzHiQHOwM9PljSeXtZzQ3shF8xl-DWinLUTPgOtGLf6Oem3dRnIXx_MyXpg0VmodI_nhVV27orGl2ZvJslZVkZYLJts7LNzuHCeck4yeqj6WTM0cz0bLvdO2JVthcFdyw-djunuLiKUpumlNnukel6o3iUBl4aWYanuGHDyv8woEHmDjmsXaGna2xUBcrbiyrMMtFOW_YChPQkJIejBPnm0ScSdfFHBK4e9xpsJc-jIdWDHtIcSTW7DzWDYxf_LPyXSgJP5majFgcg3LPcAl8JbZlN9WzGF-y6DMfaWpxRX98ci8xryitLCQLiwFK_2qRHKPGKQ7qv1YWI9-N7pSP_yoF6HeA5TE-TA5erpOGwExigcVP7lfi64l-eWN64WUnu-HtYIaMBQcXrngsJTa6YOGqO26ZJcWatIYjUuQ-vinF1uAmQQbYybX31u9c48biKBDGJ2PZnl8OwbJ9Z7qx2tFt_aLa7kX8Y7Z29gvnCsV_IYSMsPEyfLIP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=XdrMYvE_ILZyzJXedKZbezCUZDTlPCpaSAqea9mV6y5gVgyn1i7DaIoXcH5Q0uqZ6vgJJ0JnErdGIh6h-vd9_q-QXz_S4q-DbCU6qW6B7_A4uoTLuT5F1Ut2ELAdvuyB5n4sa4XeDxKV3dl3gROM2FD3gqIxXAkPH24tU3rlbceZB8yo8OzHiQHOwM9PljSeXtZzQ3shF8xl-DWinLUTPgOtGLf6Oem3dRnIXx_MyXpg0VmodI_nhVV27orGl2ZvJslZVkZYLJts7LNzuHCeck4yeqj6WTM0cz0bLvdO2JVthcFdyw-djunuLiKUpumlNnukel6o3iUBl4aWYanuGHDyv8woEHmDjmsXaGna2xUBcrbiyrMMtFOW_YChPQkJIejBPnm0ScSdfFHBK4e9xpsJc-jIdWDHtIcSTW7DzWDYxf_LPyXSgJP5majFgcg3LPcAl8JbZlN9WzGF-y6DMfaWpxRX98ci8xryitLCQLiwFK_2qRHKPGKQ7qv1YWI9-N7pSP_yoF6HeA5TE-TA5erpOGwExigcVP7lfi64l-eWN64WUnu-HtYIaMBQcXrngsJTa6YOGqO26ZJcWatIYjUuQ-vinF1uAmQQbYybX31u9c48biKBDGJ2PZnl8OwbJ9Z7qx2tFt_aLa7kX8Y7Z29gvnCsV_IYSMsPEyfLIP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Zpyz87tYSGaSvd5b60PigDc8iq1-9LdSFSvvpAI34sIgupUn2ckOlIm60-Nu7luuPpmSazhGXO_P66YJ1oQtMBbKHRioviFn0q4Xk8JlyzOb4yTbTxszu3VU99FZF8pDxkx8oy61Rds4-sv-UvBZpaT43jOzoheX0KZntjjMl5embN3_NsYJa8ZvKqHQcodB-uTScWeeM15BObxdfANfeFOWdsfnd7Aj-2O28UZFi2U4bpLvQkYj-yxjSe4RUjyVFzFPM2_Y3DhwQhxti1bnoRDCghMrhU94Ue58ePqL1G0ko9r2HPXWBFwALgbi7fmKEqQsyibEFwoZ778KTrusOF_QF3IAuYxldnz0BGINw4fs2nHAKf_vcSK49CiQ0kxNZ_hMrWVXXtOM84DOdNTcM4GAV8NGd6-OiUzk8gFhkrB0s_1ju7WSM1ypQakqPFs1neUxsCkAalvnMH2VwvaVBfQXBgM9JYDKIcMGNfby__HQcO4Qf7IgcnO6hwHooTSCmHXQMOukoRnI7hmCKxitowqI5A10RZaKdL4PsZohZhWag6K0TcsPbsRE5NoyrnsneiPHnEzvLAkSanBn71iB790fbumcXLPenpCVabWyNpLhU0N_D-vDwfBUUsS_7l7xH14ecnviVN4txU7ZwBvKMflX3h-m77PI34HoQ8IIZ7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=Zpyz87tYSGaSvd5b60PigDc8iq1-9LdSFSvvpAI34sIgupUn2ckOlIm60-Nu7luuPpmSazhGXO_P66YJ1oQtMBbKHRioviFn0q4Xk8JlyzOb4yTbTxszu3VU99FZF8pDxkx8oy61Rds4-sv-UvBZpaT43jOzoheX0KZntjjMl5embN3_NsYJa8ZvKqHQcodB-uTScWeeM15BObxdfANfeFOWdsfnd7Aj-2O28UZFi2U4bpLvQkYj-yxjSe4RUjyVFzFPM2_Y3DhwQhxti1bnoRDCghMrhU94Ue58ePqL1G0ko9r2HPXWBFwALgbi7fmKEqQsyibEFwoZ778KTrusOF_QF3IAuYxldnz0BGINw4fs2nHAKf_vcSK49CiQ0kxNZ_hMrWVXXtOM84DOdNTcM4GAV8NGd6-OiUzk8gFhkrB0s_1ju7WSM1ypQakqPFs1neUxsCkAalvnMH2VwvaVBfQXBgM9JYDKIcMGNfby__HQcO4Qf7IgcnO6hwHooTSCmHXQMOukoRnI7hmCKxitowqI5A10RZaKdL4PsZohZhWag6K0TcsPbsRE5NoyrnsneiPHnEzvLAkSanBn71iB790fbumcXLPenpCVabWyNpLhU0N_D-vDwfBUUsS_7l7xH14ecnviVN4txU7ZwBvKMflX3h-m77PI34HoQ8IIZ7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkLntAF5ycNIRD6dlTaY0rBW9BX3WvvNJzHDDCNmDe1Y9tYLgVZe-_kuzq9W8b545--gToCKx-f8OEsw_Ravw_MQvKbnoR36SJ-Nfs9C8kDA__89qIHs2AXi-7QqBvfLe3Qwf7Bz_LkaaF3qQv6_PjX0l8MRKMhgF7xQR255SKXhiTA-Ol4yF6FcKLSg1k_rBPrw_jQw6tpE5YbdB7AAhVQFC-A5YBu7eJVfSay9QSK27wuiBw-pCEmRi64WLF_AjI3tXEx_gQF0cG20lsT3hcFGYRhgb9h4oJS_vHEUKbwCAqqQ0djNtVumcztCXMZ8Ktpt-z-EzuYZU_7ta1I9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=czv_2uz51dMCFB4y08dGJvP_Ib5sfkNA5aJ7EXk5BmP2c9jfiS8005usJltCKjSdT5SZhX9ELuYzuH0WxGU_aCSqxUUQ8J7nirrcvurpPzW_8lmu-ZyGzo9qHqRLLPQzoV_3MZkgofjOrcGlTp4gidsippbKO8cD-ldNG9o7KUkdLBEh_ebxA-BhWkftGnnpNx94pg5YU1CHTwc87qpjLp7Fn5Dd8qsG6mab2dLHBdW15ACjsmW_tk9S-MeLmDQ9mBwc74aPF_g9YzINRVuaNFO3jQD75M06nUkoIAEDdDmIuyJnip9bKBKBm2SVrfI5aGJkJA_yAX7x9aLqLP8okg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=czv_2uz51dMCFB4y08dGJvP_Ib5sfkNA5aJ7EXk5BmP2c9jfiS8005usJltCKjSdT5SZhX9ELuYzuH0WxGU_aCSqxUUQ8J7nirrcvurpPzW_8lmu-ZyGzo9qHqRLLPQzoV_3MZkgofjOrcGlTp4gidsippbKO8cD-ldNG9o7KUkdLBEh_ebxA-BhWkftGnnpNx94pg5YU1CHTwc87qpjLp7Fn5Dd8qsG6mab2dLHBdW15ACjsmW_tk9S-MeLmDQ9mBwc74aPF_g9YzINRVuaNFO3jQD75M06nUkoIAEDdDmIuyJnip9bKBKBm2SVrfI5aGJkJA_yAX7x9aLqLP8okg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvlQt1AcoJGqqr9yn_uBJExSPxXNGR1AvNxMb7A-s73sgZm9mWv9Av9jpHjywtgxaQu8xTvYKcFDIZ65ECRMxHTs0PtQhtlLajZQKlV2HnQGSrfzc5l_oxSq0XD3sRK1BsXzfXTWdCSdSblj5pt59FO9uCCJxY4pYXlLk-LtvDtg3VSyTC-0QawC3BABhhSxqWWXQqh8-erTcibkUCbGt-jvOWeZ7moIlfghnVSLE4MoHmcATpQZIdm6tvD3on_8adnATcZ-9WfmPRsGgpYJMIx_dHLg6N0XqSUG3z4WDP5JOdcBmn5mujnGaWem8r52jC26W1KSgvKFTNF-XpPo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3shvtbEnTHxbfg7RMg8yB_lGKo_Tpw-QMXMQ38h7mMQvGDOtfFofUOJoQWdFq7V-fPlmyKJiCAmiuSKHFsDZY3aGJckH-ZN_fGg4Lt1t_M2JNqa9JQcNN64oCIcHFc7RLG67KmfB79QEtkl5pcTM_i0WOLTXLxWH3_9K8TP8alZUDUoF0NuC3xcvwNRXV2tbRHmbb4ip0qdiVzaCKtIkT1Xl4lCMPsQbpjgSWcsf3E06fQhQ_sr9Ix6cfHM1zKUz9hAGNFpZC1FzNSlSE18RVfyLiqlXXUbe23F2QKoUQwPNws5CiLM2-5FsTLuWyLcf8gnUHkjGrJe5_IipC_4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=ZKOScjWNdaC4xuz5EjVV591twYK3ksnflcnKupj4T83OZdfnBJIJr-8_R75sVpTLRAgcouvkTeTY8ufYVHWARDmkcoYpJK6rWDDA5nUBM-3wuTtPZ15jdj3saNLqv-EVYyoXpxckHXLwDof2nBcccZPxWqscPEpv9qCmqVad00tLJteF4Zzj4fzoK0VVChHSCEY5AL585R55QT9SZZuA8jzKWUTg--1CobSqXoFMdzCnuOUJRap5hAfdnjScHtIQuXoOOS8y8IfvpspQ52x5BgJgANfdd9bfXaZJUUZViJSD7Nn6RDHQkrbOKD5IuXFxXJpQwx-rlEUi8jAdXQIWI7Y4jc0z_5wGW0ar0VuWZb98M7bUyOn13HY1jcnWIVyajH5UHaFiz1pw6MJgvFRwvvGiBJEvGqgyZkyVpxHkaeYXJg6x_aiZLrAFIrPgvZpdQght9DfZDP6U4hvyOZcWfE2RG1hOSN_1U-qTEAFrE3D13i3q3f0bUA89QYYGyuGLHgRdvIR79qKoxcvg-kP6gwoZDz_oSHU5Zh28doWgM81xnISQto568_ywbU-pfa-1dyeOliQuqu7Ktx7k06UMtqmzWEJ7AJD5KHWisfjxqQJK1IMN1p48uVKBj6ETnNtCQZsZjhfGwTvnuXB8aVPtpKrC0WmTznFgORNDbX8i5Yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=ZKOScjWNdaC4xuz5EjVV591twYK3ksnflcnKupj4T83OZdfnBJIJr-8_R75sVpTLRAgcouvkTeTY8ufYVHWARDmkcoYpJK6rWDDA5nUBM-3wuTtPZ15jdj3saNLqv-EVYyoXpxckHXLwDof2nBcccZPxWqscPEpv9qCmqVad00tLJteF4Zzj4fzoK0VVChHSCEY5AL585R55QT9SZZuA8jzKWUTg--1CobSqXoFMdzCnuOUJRap5hAfdnjScHtIQuXoOOS8y8IfvpspQ52x5BgJgANfdd9bfXaZJUUZViJSD7Nn6RDHQkrbOKD5IuXFxXJpQwx-rlEUi8jAdXQIWI7Y4jc0z_5wGW0ar0VuWZb98M7bUyOn13HY1jcnWIVyajH5UHaFiz1pw6MJgvFRwvvGiBJEvGqgyZkyVpxHkaeYXJg6x_aiZLrAFIrPgvZpdQght9DfZDP6U4hvyOZcWfE2RG1hOSN_1U-qTEAFrE3D13i3q3f0bUA89QYYGyuGLHgRdvIR79qKoxcvg-kP6gwoZDz_oSHU5Zh28doWgM81xnISQto568_ywbU-pfa-1dyeOliQuqu7Ktx7k06UMtqmzWEJ7AJD5KHWisfjxqQJK1IMN1p48uVKBj6ETnNtCQZsZjhfGwTvnuXB8aVPtpKrC0WmTznFgORNDbX8i5Yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=oWZ8mubWlnNPChLK5x-QZDIWc9VGqKHsBhiALQnZxr-PwVFo95Qdmtx7VO4vjzz_-1GTTiurd48jYDmB1Zw6ojaYA8mBXxUeyBuivju3Vc3FLoTXG4Xd6uiI5qPr8uCN_tQdX-vN4o7JhZi_LwN-716UiKlra0t5RFaPJeZ1AlAh-iuX70-e4xrj_ELbC6K0c2GHPOvC5B6NojqzQWCTsKUwTBwAQNDTqAy7DaMwTjP2iwzQ-a3Lf4dsQN4on8UfU_EzguuBu_dVqg21xc_6Sd-JxRsplb4EM5RE8ViGS_lpq1h92lwZfnUGvMC_wYhVbzv6hONeuA5_Me96VlaV3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=oWZ8mubWlnNPChLK5x-QZDIWc9VGqKHsBhiALQnZxr-PwVFo95Qdmtx7VO4vjzz_-1GTTiurd48jYDmB1Zw6ojaYA8mBXxUeyBuivju3Vc3FLoTXG4Xd6uiI5qPr8uCN_tQdX-vN4o7JhZi_LwN-716UiKlra0t5RFaPJeZ1AlAh-iuX70-e4xrj_ELbC6K0c2GHPOvC5B6NojqzQWCTsKUwTBwAQNDTqAy7DaMwTjP2iwzQ-a3Lf4dsQN4on8UfU_EzguuBu_dVqg21xc_6Sd-JxRsplb4EM5RE8ViGS_lpq1h92lwZfnUGvMC_wYhVbzv6hONeuA5_Me96VlaV3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Umx2_gHVFwxTZgPPA-kGvJEB69yKg8eieUr_S3ZW7Gj-Zzs0xzE4uvgpM9980phcrVf3KkeV9AKvypTc2yNOc9Ln_LqaQ4IajW-d-K9qFWWRE9vj5lbE2vLqgcaiDr_vG_3ge_eANzA4CdxfC693UjDO4N4jwpDe1-AsuFdGBkxEh9zjxHmL41Bu4wIXJpCwiAwlhBXuFF-GmAbCQggAlB11wiLr4Wp_cUMNOf1LPPwkAW9G5taiiRWhv1M4aqsom-Go-nbTMYMnIjRTndcCkjMweTrVglGAq8Eb8pLApYUadqxKHlyQ4rgxXavmkKWkHQFftAh4Dzq2lI3uwg6MXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPKYq8OYb1znyOenyR8pGJqgDTuPj9Q32Ei_vK1whj5T9dfdENPXuYtbAGeeuam7EnhWiqiZ4HTMfwz0iJIzeOebDKtqg30k4Uq4V97MtQQhY7UUqL_5ZtKmoyv1NaS25M6nxsHpd7afPz-hZ291kitjqF6M09wsYH58ovqkiNGQWqFC_r6iLrp5PYoBDJXynBMQPjfMX2Jkb-47VbQJoKhK4Z3W4iNueLoRRr8XUY92mvEf-cvakww3FiQZoNWLWSF_DgAxib10lU3TAhFnUXuw4uMtV3yyDaWlWelFTwjZrlEuZnFB02-TOBm05dwMluTuWJP_nxr0X4tgo9g_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD0rFmPb-JADbto9ox2WlS9l8oIeyDdA26kDFtEskr3ypHx12G73_JvMbVczPEKO96xOlHL_gxEnUUQ5QIliIbeQjWGrBhT9rmpRzIDd4mcvQFYisJml8tHThE5eAFzmIqqfKLYRS3XIBs9pscTUwdBx-LX8RV5eeHxQK-BEs8VrNLTb9zfsoLHupCy5XLby41BG7o8h7u5B_KxXZlBqf-yRsmgPGogcMZaoAfjukR5Xe9gyYpqQdG8oRfqLmRRY_UNqeejJDadwxyuzUiPeiG0PXPxhnoWb71FPAAgy0khJU0QK9mElJsnLXUSEfpCNQvE2c-4Z50G1ZVZnfwcQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACiLjfsDV_mGbtfsbBVWFkngLgrslupwIUbUGExJsTSgZQa1TzxJHoy4JoCdXyQoyEskUUYOEUm1EYKhfDWzAF-izWBhxAxzqFBiUYLnJGpLTvfvRSlN985fWsYtiF4EZjjgs7K69E2Qoprl2soqtRYg2kinbUc6kxgxsMu_MTIsqUdpS-92URlVK-5FU9g4yirNJyMzXQ5kfNZlnbStIO9VrtleT5TUnW9bm58uAQlPVu_RlMQ88NMl8lmwK63vbpFKInpsI9_Tc5JQBA5Lwq123arJTPRxcNHkIsMgNKh6VckFNdNnxQDSzufJj5lDt2O_NCAGk5Azlquwtc_J6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_U_1vnjsaD4IMsQCeqtuA0BWpdnWrtaesfSTg1fQeMG7liY7APQDkYqNre97umlZELMoZaqrXC4HBxHEqvG2abGBkZad4DnwneQbV5HWFiP3ojc_dnU3kSyEoIIzSFJXEQLgWpfGNLUChTGuOeOtWzGIBzXq0PJ5DM2HqP6JsqzQEtn8Vmf71bzPyxXx1PNVmiJXMFY6QlCt2EECMIwDWTQcdf1213s2BZeyVvoFAv1DPNwlsPWrsRNO2U_nAMaPLPpv_zjJ1w1GBHxQ4w_9Xyotm6-H9MGLEt1WDfYMO1aKik_WdeNzDmQ0OeS6ZVKbF2azdIfVYUNQLSXiFuc2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=Ecqjmk3tRgUwE5ChUCew5yxcNtYNW6Woin-m42QY_-Cj2hnS7tV05Gq4x9C2OTrwmXTKdkJkgy1idXmgk1bvpb-lcRpugPnvZZlLhJi2_8rDL8JyrvGv74Gfj7d2OmFCBIExFX0iOrf90xbJPFpwuz-Dq0SFAe3rJINvB1_SLBEDjOc5bzz1lg_2yI3MS-fMBv98PF2MUeZkBhC00fGuVT_oiJwpX5xuH0r7NmWUd2qsZIpKJSq0nImYbwXvWpUopTFuw-fJD14kJgnpY02ofHktF9YdGPKLm4UjTId1-tr46aGeQV3eiHAKMQgx2Z4kwEux9yS289LWdv8DzBnuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=Ecqjmk3tRgUwE5ChUCew5yxcNtYNW6Woin-m42QY_-Cj2hnS7tV05Gq4x9C2OTrwmXTKdkJkgy1idXmgk1bvpb-lcRpugPnvZZlLhJi2_8rDL8JyrvGv74Gfj7d2OmFCBIExFX0iOrf90xbJPFpwuz-Dq0SFAe3rJINvB1_SLBEDjOc5bzz1lg_2yI3MS-fMBv98PF2MUeZkBhC00fGuVT_oiJwpX5xuH0r7NmWUd2qsZIpKJSq0nImYbwXvWpUopTFuw-fJD14kJgnpY02ofHktF9YdGPKLm4UjTId1-tr46aGeQV3eiHAKMQgx2Z4kwEux9yS289LWdv8DzBnuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8n441ViBc5TLJLa3-PeDHARw6-V08speOhOP6I54S1hqM4biVSPEdwB39Rpixhm73meO6RVPnUJsBjAXhBWd9j4uBYJ9RAN88_BGTiuONOF8PcC430OhzAL65Wda5OtpmN8p_D6UkwurTSt-15KdTt6aOd864S9GXdNa2HvnEqrTEguzFsH2_pqMXu3846NZ-x0svj9pevuwrVhT9iiEA3S8c2Rfjn99jZb7TZV5S0jqyymr09oror7h4tkHGYHigJfpxzsb69gzupWSyHDuLFcUEnPJY7Z0dPfx_Pl4tWC_VWcuG-ZId2COHw8nnnDpXqWJ0cvh63WnfNNxtAzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KItkzU2QkHEL8WNCJJHGQiq1LzwuldXbvD0U5VbxozedJ8pbsJ72wN5PW8pVGpB3V7-K-mHeDXMyGuWPvrqWjJYaGiAmpsmWy3rAstHNCFzTSpqReGpshLDkDjeqzmGtNWt4B1akxpj2xlp0BTS_CE7VqsS_cbDFVySK_Kx-MoJOn2X8qVhYbuBpD6kyRtOnPmAK9TwtJSgipPvcW1GfVHMGnCUpnuK6auXkW7thq9o7pUe0EVK8AEwtyAqceyzdERNRtemlsLw2qGh0obGuBuM95jU2XViaYwoKTidXd-dFK5uRtirf-07kTCYPttvMCDS-l2jbnG0ThJ8Moqwpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3pNXyJ9CigYE17dLjglvp-VPh8G8Erku5auhgiujp-kNrucj_cnZ6f-w6qqV-WhgNIL_i9UASd7XQ8gMtVLE3cu3WXe-f1P213MpO4Xpmacy1RzbGyF40tT90GTwfVAeL_Ezike4-CCqsqb1MHx2ESyof0bGHaOTX0dAI6foo_QzWHNF-bSsIBA-E45r2F2o1Kqg05PiAT4jkW4jTDhkCfBbOAc8LDCMsoTPju6e2k1nFeAg_nwfrkPhAQD1_ojKLw9TmT_GUchrEWRDb5r5c907mlohGG0Mz7Lzi8xQhuuXebesZncfgKr92cnbWNXK5NaAS2sQt9yVBWZYJgnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN_i7JZULM0yJX5QANgWd2AuD0PLAsG4X0hAho-zINxBQE_XM-diq1K_JdfCGsXvlKO5SMs4BPPo9wrZScbOzV7lzgrMcXKUj3niBrEvg9_A8drJuKX2m7DHTsybt2NPDNDM4652BCbkwpK-OFOlOzdcB1fHCc1lvrkIU4QTZFqbcjKweKAu-FWtoeXOFRW47wa2X_Rur1st61PsOu5H6DUu7V8ggqWUb09VI41WxXlzT1pusfUqolt9mN0k-VKlvoXoT78rOTnQxPZSV7YHPewEzU06-O31JWkPYCOSWab_WUyJ8s64v6j85eFXzryeKfvSpTQLttLesaCSOfbGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYxVF7Fi-Vl5v1RAATg41Cv6RW5Mfr2dv6omGE-Wtm6tMC26_ICaw5kiIm5tHiM_SdkJUNsjLtK3lAx5ojwDG0O-Z-VG5ogCHzbQ6-F7mtjcrfaLWZa931Qrsopg_33pfQwKoEn9GoLHIEisyxplKaeHc2olLV7wVPT1uRLcrnqDmwQFwSs0KcPe25cdS6zvYcGj-zVeAFggV0ZcZrumOg6SX8I1RbOg4eokD_AoCskb05X7_GN6SO82Zj0bzEHBaBnA4SpGFao0y0ot3-yPRlMqd_72pRAhXmFB5dCR9sE4aRh2I7TgBTusf8cS3OaAnl1LYsw1wJv2qBwo8UEHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🆚
🇲🇦
🗓️
۹ تیر
⏰
۰۴:۳۰
هلند
🆚
مراکش
📌
هلند یا شگفتی دوباره مراکش؟
⚽
🔥
هلندِ که به عنوان صدرنشین صعود کرده برای ادامه مسیر قهرمانی به میدان می‌آید، اما مراکش با انگیزه تکرار شگفتی‌هایش، حذف یکی دیگر از مدعیان را هدف گرفته است.
👀
⚡️
لاله‌های نارنجی صعود می‌کنند یا مراکش همه را غافلگیر خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24634" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOwQBzvI2MJTe3yPtpSIDThKZaRxJ6KKtFicj0_AoEQ6etN_pFaOH5sAmyjVEdrOVf-5T-Ocjnl7YOFT_AypKIE0XGDdBhHlLfjW7NOwkGGwdnn4r2AIqddnC6G2hw4BstLootiK2GjnwNirU6x5VnHmuWUem00-FtLQjpMTEizrCRVIeMgwP3WOIkfC5I9J7kZtwHPzGv_gikLYoKypYk4sZvdkHNaG0DsW5D0w1KzIAJp5v6TvlLgLshUjMW5jEO_2f5SE9pWr8VwxWhnl-w4uo_LGxsM_xTil7pSbYkTeHdtvw60ZCapJvcj3HHQCcz4g6WwAk7WrtCazPdrUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig11qguHuI5kEG4Ai4BJR7VQMSyBSpmAnkqnlxbLQj_0LRb8W2vR9QowtenoqJNGwHIY5iaWxCYxsNkD9qsFRqv7-Khkmcb-gvyO2fWiNGD4S43zxqBQT01OiBMy0lJrJSwi78qAtiUyt9B9B0blVJUOH0aTiMh1fdJs7TdY1VikUdq69pqz9Rynsp9mPo4MvsPS3P1mr8BcU5UzakltCofEGMPsXWQT3CxxdhMsGGW3Q69kOymL-h72-rOtPxzY-DJtrMrX6YOq0uU-blNr7F7Ed7i_YVyYE3xqQaISUrumN44vfhbR3lyF7DBJvUhkj4Io2FCNc70QfQhQvkhxMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=S3yYPVIYTp4OcC-JgSWv7ZmTIBWU7XtBTSIew0kXUcMCN6vGnBuRjofS2Zd2cZq65ToBHHASzj2nULtOf17P-pMsVqBgeQi1kdJTjFvhXskZSRKxfAlS494krncmsk3b0-5etpTDN0-Gi_v0GfgChHlDqRxwqUv-XvZ2rTvPKLgx6qo7al-DTBuS8H8spRADVj5NIPZVLF10ZY9rHaHJsk2CFgJigYU3zM_8yvSZFePNkak3hh2tRTONiqVtnLR8IODyYD6jHEzloH6DGB0KDzVZQaKC860qWCc7XVeuNpbb4ECqSfthUo5TN6b6fneiiRrGo6x-PILbCWGCQxkrThVSznE3NMXyJUq7C2K19rCViDwpJ4trLHyR9kbqO_vdxbSApneHCcBoziF9CvzZJhV3RqRZEBfwA9YE4hkVPOeUsWWpsC1Xh9vNKGxq21Qe53YwPV3-fZpaLUPCDffUEkSxVx4kHUIe5a0_H9YZyHktqAKVx6ujxm-gL-0AW92rjVKWZ6-plb88K7LyKzPGCAbSXin6Qfj9C8LV6R6vpXD-YV5fZgs4JIoQsAFwbbETBwkZuEMsdHfLt69UxjFFli-0tvhsVvTY0hmWow5BcaBM9LdEN3cPFccgShI-CT2ZgOfZXqzt5_-XqEu9m8HK9LNK-5EmMkAXPotO9zvMAoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=S3yYPVIYTp4OcC-JgSWv7ZmTIBWU7XtBTSIew0kXUcMCN6vGnBuRjofS2Zd2cZq65ToBHHASzj2nULtOf17P-pMsVqBgeQi1kdJTjFvhXskZSRKxfAlS494krncmsk3b0-5etpTDN0-Gi_v0GfgChHlDqRxwqUv-XvZ2rTvPKLgx6qo7al-DTBuS8H8spRADVj5NIPZVLF10ZY9rHaHJsk2CFgJigYU3zM_8yvSZFePNkak3hh2tRTONiqVtnLR8IODyYD6jHEzloH6DGB0KDzVZQaKC860qWCc7XVeuNpbb4ECqSfthUo5TN6b6fneiiRrGo6x-PILbCWGCQxkrThVSznE3NMXyJUq7C2K19rCViDwpJ4trLHyR9kbqO_vdxbSApneHCcBoziF9CvzZJhV3RqRZEBfwA9YE4hkVPOeUsWWpsC1Xh9vNKGxq21Qe53YwPV3-fZpaLUPCDffUEkSxVx4kHUIe5a0_H9YZyHktqAKVx6ujxm-gL-0AW92rjVKWZ6-plb88K7LyKzPGCAbSXin6Qfj9C8LV6R6vpXD-YV5fZgs4JIoQsAFwbbETBwkZuEMsdHfLt69UxjFFli-0tvhsVvTY0hmWow5BcaBM9LdEN3cPFccgShI-CT2ZgOfZXqzt5_-XqEu9m8HK9LNK-5EmMkAXPotO9zvMAoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgrVsi9oVN5Ta_s2toXpnVdAu4jTBJc2I_0WXobHv96u0IOirUTgUSTwuDa8WruM8oIyC3-WXO7kSNFS5e4iK3yY6vT0xGu_Lh2uFgmYWgwQUdwNouPIQP2oYVoUVXiQB4ct6JwVpYus6EWeluz-0ZpoZSMQI7_BRULFlRfPLLSvlkwH3do-WqGbtksfoxcaGGwntTTGtLB7XzS1_niCxKVk4LscNSqIdfaceFmvE_J3cZU8SyoYsFy0AQ3pgFd8azUzgKJbnTYvHwJbke0pQFdxMKcAxNLyjuXDMzu32z1pd5xXo6MN_nRT1MKeTV9w8cbJrvp_NsF7eBh7EO7n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=i8EXsRiUjDQhrYuEy33B0q8sLlM-Cktbstf-Ee2hftxmArCOMvWMYZznOyreG9KtcvNIUGebO95B8THqselbeNzOx2LqbFFRCxRCCD1kRdy7H3V4rX0O1aZX-tzz72yVdk8Td1ts4w9vWMY5GQC_NEzPIeE1hP3l3UPwEucWe7Y9jDsYAgS-UECX1IWVYr46_WgYTMmB9ROr46x-lXvqXXyVMbn4QcP896A8LD-dyADB0TSuTDkD_WGs7UdLJZXcStiPT5B2y9G1aANC0NiewZo0wYg7eivaxhBXH07W9Vrj8Qrszds3-f2vbufGk-Qx3SkSZC_rS3-wF0TuSA1Jig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=i8EXsRiUjDQhrYuEy33B0q8sLlM-Cktbstf-Ee2hftxmArCOMvWMYZznOyreG9KtcvNIUGebO95B8THqselbeNzOx2LqbFFRCxRCCD1kRdy7H3V4rX0O1aZX-tzz72yVdk8Td1ts4w9vWMY5GQC_NEzPIeE1hP3l3UPwEucWe7Y9jDsYAgS-UECX1IWVYr46_WgYTMmB9ROr46x-lXvqXXyVMbn4QcP896A8LD-dyADB0TSuTDkD_WGs7UdLJZXcStiPT5B2y9G1aANC0NiewZo0wYg7eivaxhBXH07W9Vrj8Qrszds3-f2vbufGk-Qx3SkSZC_rS3-wF0TuSA1Jig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=XP-UEXmND86qH-6fon8ViZOLDxaN7VqNzlfea8MZxqxHH6R-L579fI9hXWdiHGbNYE8nZFahj03qasXgHb17ky7Y2WIWttk6Z7cod84NBrCOzjVraPdGAkNTBwpmsDqI5uvjQKdNE_UNYVdvWf6OTY3pVt5nEQef9YI7IS5SXtSsv51kqYJNkV8l_2bUbdyTOBL-ePN8NtI8B3RvIfcDxsPAol55lyB3hCtI62WiMLQ7dorjhHgvRW4qIe5gEluigaF4Pu1EJvUEDxvukSqE6nstzcjH4cA5vO32OI6FqQKv-5Ic1TSkllCadlGPRRj_A-rVDdRF31DrR27BP47-bTTCm30iPvngIe1W0sOS-m0VsFgNYvb_1SE4jx-BP3-aNBzL8KY9YOmXDVYRZwENcX6wbwOb9khus3hW4XBpvfuokVOkjH-sV2r3WCr9USWuDtUt1tlbXZXJIKzQEa9Xein8I9-ZZAbTFpfJy28of9pKvCQvVLqrLNmpGuz-aHm3qMIPcf1TdC-8q-_3uu8bIcCjiXZfYEP7tprN1PIXmOLGnVTualOzWrjAtCZgXJreUkes-gcAB2Z7SIEzEolDjI9ME91ryyF_O1U73I7zijVlGCAO6yfh3Ss9mGTClc1wdv5mb8n3nlNHzkq-Ku4EAo53DyWvqH6tt3CxFGclRtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=XP-UEXmND86qH-6fon8ViZOLDxaN7VqNzlfea8MZxqxHH6R-L579fI9hXWdiHGbNYE8nZFahj03qasXgHb17ky7Y2WIWttk6Z7cod84NBrCOzjVraPdGAkNTBwpmsDqI5uvjQKdNE_UNYVdvWf6OTY3pVt5nEQef9YI7IS5SXtSsv51kqYJNkV8l_2bUbdyTOBL-ePN8NtI8B3RvIfcDxsPAol55lyB3hCtI62WiMLQ7dorjhHgvRW4qIe5gEluigaF4Pu1EJvUEDxvukSqE6nstzcjH4cA5vO32OI6FqQKv-5Ic1TSkllCadlGPRRj_A-rVDdRF31DrR27BP47-bTTCm30iPvngIe1W0sOS-m0VsFgNYvb_1SE4jx-BP3-aNBzL8KY9YOmXDVYRZwENcX6wbwOb9khus3hW4XBpvfuokVOkjH-sV2r3WCr9USWuDtUt1tlbXZXJIKzQEa9Xein8I9-ZZAbTFpfJy28of9pKvCQvVLqrLNmpGuz-aHm3qMIPcf1TdC-8q-_3uu8bIcCjiXZfYEP7tprN1PIXmOLGnVTualOzWrjAtCZgXJreUkes-gcAB2Z7SIEzEolDjI9ME91ryyF_O1U73I7zijVlGCAO6yfh3Ss9mGTClc1wdv5mb8n3nlNHzkq-Ku4EAo53DyWvqH6tt3CxFGclRtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv2YNXP9NbcaWOQmvY8AA15m-G2ZU8Qexnjb34z16EBnPZgeSIyHFeThu_H5NUozkQE8PoHq2UWikU4GeMIxidvqwPt3bMDYWm_gyqb3d7bLgRLqTWp-hJwANNd9fCiFGvz_3qC7XWt6s9h83cuR6_5FRFD1ZN44tvUnI2DyAzuPaVh7epXyDS4ZAqmmk-M8n-Lj8C6HkyPSreAcebtXB8b0n2iQL911-56aRRc__JW6BE6HB1CU8HekSeV09KRY5AjVKOO3NrtV41iw5LDLmh0K0-o9WW58n5RrXO8chUQxsk6sZkPK2Towuozg57bd8xC3bo3P6cLsS82jS2iy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=Tg3kHwWN5mIpSvSoEoc17N5FXMLXQHLrs3xtuyZZCYE2KwPwt3OZeioHIxSlPF42e1l_V8PfWpZH-vEeQm7MdBKZWPeCSxfEO-_yTGpPlx4IY1MkUgaUZDiP7hj3-cI29p52IGkPZtZOV4Jwk8DfGx6_DwC_vkiQgqDDCRAq_AYq7eYvOci_0ixRAahG9iEgqIHdAVogK_I3m2o0S3BlphltbCQLIxVTSSR2e27WROOjwzdfEM4GGU7n-WIueQD9PdVRjesetM3q2UqbRgAxpqM5aMrXhGXwNo7f2ZKUDM7O-gXAF0VSoG5jCeiYM_HIbfiRnOg5xEgdkSgUgS4YT5YjemTXfm2S8GyjGjrlrY30R_k-hMitWq9rq96qoMSuGg-dkEO8wcOzsHOIohfrRPO0PmfmdpaFMXbe5VUp5FUi74HCznoIKory8XB9K8mqd7ZoNMmK8HuWNlq_eAmyiDlAfpTlbcOTs-P-j3Bm2_J0agt-5eAOTHIZ44cDJR6kW5lGP4v3MJxi0ByWn6IqYoPHfad60oVKSSqgGULJ3ay5Wdaato00fvG2cqIoQGpjH7PawtxDERn0hV52zr2TR_ek4n98UBWMLAIFfkJNdVXO6rvGt5IfY_zNWulFvtw7wyVaKhknTziqFJo71gKstUHKreu5qh9fk9ZMkHFIRTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=Tg3kHwWN5mIpSvSoEoc17N5FXMLXQHLrs3xtuyZZCYE2KwPwt3OZeioHIxSlPF42e1l_V8PfWpZH-vEeQm7MdBKZWPeCSxfEO-_yTGpPlx4IY1MkUgaUZDiP7hj3-cI29p52IGkPZtZOV4Jwk8DfGx6_DwC_vkiQgqDDCRAq_AYq7eYvOci_0ixRAahG9iEgqIHdAVogK_I3m2o0S3BlphltbCQLIxVTSSR2e27WROOjwzdfEM4GGU7n-WIueQD9PdVRjesetM3q2UqbRgAxpqM5aMrXhGXwNo7f2ZKUDM7O-gXAF0VSoG5jCeiYM_HIbfiRnOg5xEgdkSgUgS4YT5YjemTXfm2S8GyjGjrlrY30R_k-hMitWq9rq96qoMSuGg-dkEO8wcOzsHOIohfrRPO0PmfmdpaFMXbe5VUp5FUi74HCznoIKory8XB9K8mqd7ZoNMmK8HuWNlq_eAmyiDlAfpTlbcOTs-P-j3Bm2_J0agt-5eAOTHIZ44cDJR6kW5lGP4v3MJxi0ByWn6IqYoPHfad60oVKSSqgGULJ3ay5Wdaato00fvG2cqIoQGpjH7PawtxDERn0hV52zr2TR_ek4n98UBWMLAIFfkJNdVXO6rvGt5IfY_zNWulFvtw7wyVaKhknTziqFJo71gKstUHKreu5qh9fk9ZMkHFIRTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJQi8L-pGac1d1NtGyrCsg3SHgr5pIwbr3FwB381UxZHta9ffo008D9PcZBFVzsK8NhWT4PiQ1vJP_USZvVJCP9VJK-XQftMHfyDI_m07-rot_VZGaPC8c8jTwiXBvkIuNqRwcMTevBYi1j44OpIz-3g6-0rOfwyOGQfPOtrEZRZQMGohBmsoD-i3JbGonNFjLXb2vCpB3XD8FAx2bXTvQyDNllbQuCYDG6rmQVh76jGPafQW-ALdr-xlrZre-DPOZODbthbK774lil_SJa2Lh7Sjm2hCLltAR9SAr45dWfTxyLDay6FO0hqDuLj1ZUcRSaEGQTyv_8nPGGtFlATTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGxTj7nCPp7S81hzUE2zx66qvKNo6GY-KtbHmwuXYW9TeGEqLJtqXBUJyI640k2_sdY0l-QGWh-Zywi0vfIbhHxqzecJ409xjbad6iUz_Gf66oHAj9y9Sutf7hNoE37mNKuNt4Du8R7-fGZQTx3gr5g69RD-VG4JNQOYpkvj1IL9kUOblGyqui2_RWZRc4jdTXCzwKtbaJ1b67Y7NE4Vg9535jRnSONSYUdYa4uKblF-tEnbYyC1CP2MKXboN26KVgXWor2fVdjNLAepEK6-XHEwU00n7iiKD5yj3BrM9kgVpjbu3WJTeqp1DlYrz-FNta5cFM65LmMor55Xks3QpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9D_4hN9u5zrnlQ0H2yZmwJ_QGP2F3BwupKvLoQMOUscABVQBWyvVmx8s2nWSXjxugIxE28ZEIJf6O5ZgjLLJFcJFxjTI71D416rCV2O2p5lJ4YhEqnCvtNv0vZBYXWeFzK9tZmzwJUr0HmyPbVB2IRShHPG9-ME45-kC7l5DLscP8stkaHkN8zWbtHsF-LogEMkltfoZ0KqTG6gtkWdGqkiVidb1PSz4_YNVe5uUiKmtQvzX7jrroZX1cYDflR-DNm-HB3pS0nAkD2x0c5re9uTNnyIFbTgC8kH-H9vKaySe57DCx9jSPtfbGE0ImAsmUycs__-2E7rdMIntWA2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCkOKWkgv9XNQYnj79XElG-dLi2hgVsha_cwYhPfCrFhJljSAmBNEuo-vBQOw_mNYsPF5qEBkIXA0IBavH_tmNM5CGZyoiItv0-UMLfuowXw_YDo-Gillk6vGIg26tfgoBQemdvCopM9u68UU71IsxYTLod2Ih9_x7lSHOuXWp1SiZVcoqLOENZMNW30gzoNap__pEXAU0RB7MTbFpEj6NRTqBzsOfOJCxg4vU4Q2lb3AR9kdsesLglcQ9yfwddtKtxLnC9boqwk9-03aGID1p9IjtfzJNa3et8PcVGOHmPmxCagp2cMJMGrNPHcsxB57kU-ZxcOB7RDgJbSFlkfzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgL6ltBC-Cux-ANISmnsQEabFWL7gZIkn_zCHJ9TBfKHq2ld2bemzZj4W98gdRELD6VLjiNY6ha5dsdMkBCHYyw9zmpr9uJSPaWQOFWliivRoh9WaLRbB2kv1-v-Lgtb3Y7IkvRCmxnJUpBHB7UWUJOelBpzzrPj3tWg1G3UxR3W5-GLkWPw6S1h4k2MFJx-HuPgyIYadk6DWjB06V007azYIfIbiKAS4L5vPRPTJAV67D8KFpygtirz_Sck9eemh9R5jNNN1be3f2Zy-6ClwKKHmkBJ0kdWOI4UeevT_dgvmRYM1rjRaSdoovnt7QSsyPG7dElYqZIUkVeEqwiq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZpKP9M37bQliyLlSBqZNaz0xrEvSiwSBdxLEdMxjkCkIOgRsccD_j5yrCzQAcfVWTBIYnGmXWQKQ6pPtO3QdxiKffb1LAeJ7q9QjfQg_23btBpHbCGjuUCxCg994HISzNimR_FiUoaFgxJL--75GzUtSIaCGM9vP1jHrN23PsDcthwsBeBHykICeW1s5mjkrM3KUnvA-9gBQN-INfw2-Y1AS9Y2nQ-WWqwT8Arqsly-i99cVQBS2aztDL5r2KPsvMg-86CBw6imwuC49U1pKupliid9J8pStVj_r5r1B4oDQZaTKqtMovcWZh3mE2LhUH77xeqJjIvFaaR76fFBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3PuxeJHt72zDL7bZE3v1s9r2jeQsajEfZv4UoZUUvmq6BM080eVToIkYDyJ8oWW_PjXMIqam4ILNsUvpnwq0mSEILIKYT5TryJTOdVOwh2QRycJYpUZhuV2j9bbdjwntQqObFvsLodxdzVhQFtMDtwsXP2Fq0X4qUotm_-boKLz_KKLI1PMhip9-APeeZ6Db_8OYxOsEdnhZsuXiRwO6ubl1BmGu9hUzoakAE4jH7Og4hLmFmscPxKt0qWm4TrvUB4Shs9kG-EW__G7r78So60cJGKQRR537BHpHgfIATAjUrm5TmAP0ZMwoUHQbMlJWBnuNCvlDINpyB7yymRA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZaXI4fKAprO4q6lQpL90NTBMO_kok0P1eIYXoA-nj4PKCM3NZmjdPtZ8wtIadpXgbZXamm0jelqPNrL2BNgiFOpFLZJKl_l8R6SSvaYRNUJZCcEDBvQ95uXcaSoDjzXcftGHmeEk5vBNQEsLkdWrJ3UjOHCBiZ31oEEl3j9lk7My6cnya9X0yQKHtNfpnkoM4DGNAJb0YZKgMYs2u98ruhc-FKJUDIqrs4Rvu2KfhP0NjsHCmBvGkkhV19BlnyE9KhCzNMOonGL4TrIM9osrZtIaRjM7pjNFVcrIQFYuICYwL6DE2sTBdTFJ3O1nsTisXAfTWgOBFh9K9ZOt0OhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAeU0iQwjVbDPhVUUYCSvClCzfqKcKaDzqaMQRlnE7t2S0ozPzYoRCTxFV0qPJLcZ2PuczB4leo1MyR1pdAPA0AUZI0SBwlP4lMUT7-zzcPry0s2fNQnpsSyQREkL6aR7dRH0D-_OBN2zbunKdkAsV3YtXKr4VATDByB6da19hJPlK-B3rBazKR4_P0S7uIQDwwbw0NQt2c_TXL7xH-O7FzYwmRBWPsMbdxB8O7DyKAP-2XUbcwnz3zGqME2pgqaW1VDCgJPAj9AHGxPUb7wsB-o-lTkNZ8pmr2YXu43JLbFGjUwmpRL7iZSgCLMxPnfH6T7l6_wIuPKkuBsWo_Udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK5yx6DAhyoDHaVCoYE67j2_6W3YA18Vm5yaCyib8PtAA6EC1bsZ0ZgjeifKcH6WoDprmQgtKZ_VMY0ydwq63Rys9aIFFKgKFsMhDLTuEN-kJ9VmIni3vh2aytX-_Suks8Du7nbXkzavKSrtQMy75JT7_D2Gdqb9olzSX_ovcxQmK0oGjE4QTHKsMr24X6oFH57rmbv7e59ZL-c3sOCJD4dRqUmioQH8hpTmsH2T607W4-XUbMAa7JxiOGsV0hGc7zK6LjschyMp7X70PVuYPD9Q0IEsCZTgVyuFHVSDwZ8k6aqOZjlVt43XxRd_BmYMNobubGhC814mp5luBELlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2p38RBItgf1ZxRnpY5pFMb4z_COIYAOvLYf7pGSnGek6e_0-ljWiMg6bVzkHYJExqvelO8etwJdj6lLjwPH_T7JxtHxbGbn4xaZhi0Sho-eNqi6XN2vxjOUFLZjY_0lJNP_4CpfPDNQVhE2CA0ZD7bXtBp_490vkZrkDTPxWto9QvPsxl8i1UTXcYXu9cnXKGcoj9LElq3pN2DrJBiN-0kKPakttWHnRoF3CG0X8C8eJ12qfPRvML07j__T0yhdau8mBvKz9rRKl0KNWPrLvznKoYmBOCIcbuPRosdrjA2uCDzfKFi5JbLxzPNQ2vZsFhIMgQZqIyn_IaFlakQ6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVs_fymm0SwGeQQdrqywjqEG4stZsNz6DOsY4Fyd-wF1EBxKCLENFSgjLLChTKQuM2sXaCS-8bhJoMgPshgzFMRN9xYUEDMiwS2jmxkw4A4xeyRp46SCZPoeg_wATqSgzkxKM-SAj0kYWdb11u2UgW2WFZJv7zLTbfBVvV0_G33-Xbl7joA-aN_VkYB4VKEfFjzWxN4la5dg2uwxKZrf9aRCui13DwboEztdNtRF1X3_X5kPPn8boVvwBnVK9WbPsxfhiMq7AHD3TI5QiN6yWZtSeVDNqIEVSXWfazw7vPWXiaFXmQzDw2NiCEoJ6w8ZbSgVzfkqpwyaHvZ-WK8hXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=XM0RgZLEtu2w-rN3WEfJSZd4oX5TCAs8j8FOBBwbiYc_gVmtp7S1BpcnaaR2C_UHfgIYu3T20N8E-w-YDFeXW6RUTQ2c1Il9foFb8GbOewK9RzvkuYULKDAJC00XIMf8PG0HlWcBnT1Bd0gLTUqZymUS07fj9_oaB43kXOZ09F_inB_--ws8twlvkUTcsAxZLaudpt_GfZDSiR5fJNrx8VJhRo4RqU0W9RduIoDemAcaZ7w0c2h3EkVUFRzpGpd1nJg5uCb_4FZrstHY3kY8T2QHT4wgd53UiKiLZg8-dbo-XsGLo6Cww72oPqAXRQGgSkS1iqCf3S5NcMhHGrB03g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=XM0RgZLEtu2w-rN3WEfJSZd4oX5TCAs8j8FOBBwbiYc_gVmtp7S1BpcnaaR2C_UHfgIYu3T20N8E-w-YDFeXW6RUTQ2c1Il9foFb8GbOewK9RzvkuYULKDAJC00XIMf8PG0HlWcBnT1Bd0gLTUqZymUS07fj9_oaB43kXOZ09F_inB_--ws8twlvkUTcsAxZLaudpt_GfZDSiR5fJNrx8VJhRo4RqU0W9RduIoDemAcaZ7w0c2h3EkVUFRzpGpd1nJg5uCb_4FZrstHY3kY8T2QHT4wgd53UiKiLZg8-dbo-XsGLo6Cww72oPqAXRQGgSkS1iqCf3S5NcMhHGrB03g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_pemfTkw1yBoL7LIQ7L6eIaNol21KzyBecYVDvofSkTC9zr_TcvQzfzKcHzldYimy662lLSgLNT6uXb8RAv2rEzk8v56OqkKO0ZRVFdUBh3CcqvBAGk5-xdC2wDlfQYMzeAzAJYTDQ_hd4RUtCqSyogDfFBPoa8K5_cgDg18JycwtffaswWpsex337D0AW9Wx14f01xM0w_XqmY-nFrxVzSQPbkqj8kM4lFLEpjKgX4y5ezwQFHTQY-QAVBmjBVH9m5AzoVD_8SQpEEdyQ0Y87UjdMdnVjz9i3L4PpFteRPEjyppsIh_RySwKbQFuS2z6tbQhudNHKZQq59tvDY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9TM7Ggl2IRnFQZYau7B39unrNQUCLnEVahU_FJ-4sP8ZzzaztY_O206k8cXSW5l-YCywsDWF4as2y-x86mZufpX2l-4y3T7NCfEWVM3o7BF3P8sHj9XsZitbwQnSukoEjo_tKze8n3EMu6dBtZo1HjGzMkwUc4aNm1rXPt2ez2O21mXbcFk4q-Uvlxr6teEyHsErEaiX2UkpjmTT1o7vul3ALRRMowp88XymKQG5nGt0WQN7fTrnyHkq5T5uTNutKwJNMq1oL78_JemWau0XzrRCCruijF8jKuTVv8QBaWY-Luv5qVEpM-zmplS12aaGGhQEaDSUnStJHWDCzM6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfNLDgMYEIk2dbsq6co8Yb6rbQsfOfk9H2asaMsc7RPEPsdxe_Ne2dec81Enb4iZ6swuxjxXVFW7AUIJ8a1sLweq7ZRNmkQ6jVF9p6z8TuP2tKO8leoHTR0EA056HcJO7e80KsXu_NDptZANA252iet4Ikf7J-A7mR7U7ziIUjg46Fz4HMkhjUcMe4R-fF6HhyBsTgzzbcUjvXn3zbA7a0apyKi-o7so42q-lp8vw5yZPf98LqEXVDLLydByzogUYMriVm4OaImRw9fIQ6jW99Jn93OoZz_hkMcFWxeFf--OsimVY03scS7_GraMKqqYasqXlSphwiK7Xd0H_Za-cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXSC8QTKIaHBeoSXetd3cDZdC9hnPtFSYzxB1vu_WD01UEcKMzFYqYZcXKBKZjWkotPPjaAxqhZWOsFpJ9TxOnvkZF3sBPS-A13azYIGESAVGstGo-nr8V7ptyQ0IxOHM3piXs51bg_vHFzSQlpEEF2dGgGAeB9_UhgzsLusEJwrTScrKIWCx5WLhAqEzLA6M2nvfByvn51mQuhjxDlEb7v2j1CBdz7C0msL0k2c15JXyxxWcSvaKkWE4Vad6Nlr-pS9tm_aoxWn8K8OYAOgN-QtHKwfdfzmeXaoVRtGJaArOuN2v2XiI4t4EN1AqGJ2EqZqlPpfwjoO5F0xzhdjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQcf-Ol8Wa_W-gxe_BPL82jbtKr-A9vO_G_nJEXKAnGpflp36zNDX6gPJ4lNPuap7B4IkUmZ2KowKwW8T2O3jYvvXQbkhGvdrrYoLPxWMsv_4LTQvHKGC_2iX6IQOHxlRoqWqo1iz9JchIUI1MC-_jw7zCRGEexzeUGoKrKz9BGn6KpYAP5_p0-93eA450yG0S3E6nnTpgo02PnEWbCnmOrk_qHcB7tZHzvSvNYNzLF7ryZTsSfFOILcNUjpQkwd6WdRoBhQeR3NLRwICkHs00zATG0c0Hmtq1RBqz4dHrMnGpAGy16O7fdMyMDSgO1psO3nVXfbm3Q0cZdUBzTF_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HATzydb_39Sg5Etfw2wcSe3u0Qs5uq7o4ChQ-Qc24s6qatqPvbRLqeu_hM5WA8QYDFkDojyaErfXx68ILYJ9s4Xeb1UrZpqS_HxRj83OwXF09bnl6aK4Bg8w6rNcSBFLYRIc4wCo-RSYsjvI_FvXS4ZOK71jF5cqpWfJO76BVj0aONhAwgi6ltMd_KvpsisJCArYbOUZPnlyxbYvx_4OCiYee6Xaa1-XbBeIFWx0edztGyh_EfusiU3j4D_cSD5T13_MHi0DIGDmO3_09q6oXE4sL5lquJ5qq-_SdcP_FZVreUJ0tOy-7YsDqWCLVG2EnvioEWtNgOm7HFWJNflKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=giZ8eUZsgXYFvfFSxIWeHTDUmOKalvskeZc9OG6ZomfvbaIe0abwL0I-Km7OuYQkIeE-D04z8entSJExUqhk0VlaIBMz409AgqCO1Mvhh-GIrFOnu0fxGFE-zW4E9Nl2XrEdRUzWh0QD2_lS4N7-cY_oj3145s2PDZzLECmgUfX6KIz2dPhG-e_eXX8vtgGw8FBE2oIqcbQnEyl0-q-KBb2-TQL-p4S2NVVeee64VxDS5EZgcLu95LKput8YsTGSa6h-ZNMSsm2JNvVoPghkINWjCJDQ4BRVGh9rrW402g1BASG93qoJqioIaJKASlRMkaCBNK4kf45Q-7DfNibUJ3Ss1jiW-TbOihy94V6AR_SqbpyRMsTgjAxRYaD15T2DYR6ZT-u98OmyeWhyySzTpDnbtWStxwvvml1LhwoCpQYAspELMAAJ7-VtEhTes203NZnCvfDm8rj0MPtnJ1ogb7hQb5hoHalr0whvdDYtgkxumveD6chehcwL_Po0dtok88XPd7C-KPZ5TmC3YUiK52gkUJZJtSwFxh5ZvrGGnZEox1wkwn0HhNk84Tt8fnFd3XW-yK9twcH1bLUCkH5xL3EcHTCuXAORtvIJFbB2noMk_cTP0y5TTx1yY3sjOWNo1vbmk1Q8FRR6QvuOeLJz27AZLbgEum4IMbENgsCUwQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=giZ8eUZsgXYFvfFSxIWeHTDUmOKalvskeZc9OG6ZomfvbaIe0abwL0I-Km7OuYQkIeE-D04z8entSJExUqhk0VlaIBMz409AgqCO1Mvhh-GIrFOnu0fxGFE-zW4E9Nl2XrEdRUzWh0QD2_lS4N7-cY_oj3145s2PDZzLECmgUfX6KIz2dPhG-e_eXX8vtgGw8FBE2oIqcbQnEyl0-q-KBb2-TQL-p4S2NVVeee64VxDS5EZgcLu95LKput8YsTGSa6h-ZNMSsm2JNvVoPghkINWjCJDQ4BRVGh9rrW402g1BASG93qoJqioIaJKASlRMkaCBNK4kf45Q-7DfNibUJ3Ss1jiW-TbOihy94V6AR_SqbpyRMsTgjAxRYaD15T2DYR6ZT-u98OmyeWhyySzTpDnbtWStxwvvml1LhwoCpQYAspELMAAJ7-VtEhTes203NZnCvfDm8rj0MPtnJ1ogb7hQb5hoHalr0whvdDYtgkxumveD6chehcwL_Po0dtok88XPd7C-KPZ5TmC3YUiK52gkUJZJtSwFxh5ZvrGGnZEox1wkwn0HhNk84Tt8fnFd3XW-yK9twcH1bLUCkH5xL3EcHTCuXAORtvIJFbB2noMk_cTP0y5TTx1yY3sjOWNo1vbmk1Q8FRR6QvuOeLJz27AZLbgEum4IMbENgsCUwQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzYwcWQk2GACLRw5K82fMxvl3vmlFCyc9pKk7cQoLJZ2kIeDyWEjPuDiJIoQm_j6Tb3QOa_nv6I9GM_XLkxa3HtHTHluBjaBG1IU9vElIqQb96JZ7lYbVEa0zVP9sfiy88OkIJidqgqG_ZTNqKAJ9TPX_5_kWeViDrmcNSPCOuk2I4h1cyjI-0PTedzpBRDItsZ1Nj1ks3yM3kvlSE2kvfNd2_CGDIHRM-CHNxhf_N2UiW_Q6rn17RW4gYD26XbTlAASg6s2Tj7LaVckQrfLKp5eTlmqAuAgX-iCJ6vEUysEGBhBFK4C8kfwjpLS8BHqZTCclhzjHV25rDCRErKMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=MNQHoPogKEfJ2jqrFYEWzB7sGWsspnxVyvgYn86yJCCpMsbu9Pav02BaOhI8uKItQ6P2oU_XnsNIClbo-nRrNWKu_mF8UqUxl1w4_FnuaOzWamW4350oX0TiwHnT_hEw0tB3W4BrIGzFnITR8mDZ_tgmKFt1mn2Z2hysrCtPaNdb0LbACmki8_JF37tPDaosYbWFnSUGL_TWB_olAeb_BwRYOfHEwhxsBdv8cukEK_o4wHm7hWkMihR_pfPnpTQ7QB3JuMah5ZETPszUSjI4QGNEx-3jg8xuOBNDYst5SDP1-pG3FLeWw2XBCIX5vNUnVGiANDe7gzHbIdvrkLNr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=MNQHoPogKEfJ2jqrFYEWzB7sGWsspnxVyvgYn86yJCCpMsbu9Pav02BaOhI8uKItQ6P2oU_XnsNIClbo-nRrNWKu_mF8UqUxl1w4_FnuaOzWamW4350oX0TiwHnT_hEw0tB3W4BrIGzFnITR8mDZ_tgmKFt1mn2Z2hysrCtPaNdb0LbACmki8_JF37tPDaosYbWFnSUGL_TWB_olAeb_BwRYOfHEwhxsBdv8cukEK_o4wHm7hWkMihR_pfPnpTQ7QB3JuMah5ZETPszUSjI4QGNEx-3jg8xuOBNDYst5SDP1-pG3FLeWw2XBCIX5vNUnVGiANDe7gzHbIdvrkLNr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzFdp8oTwMCe2OGkcSVunHwTPJ2XgRdA-pnCMx-ct1vFo8Ukccgq-kS7l9IBzk0D1DVUYExMXV0LK7i-o3-FmlJ-Za9feSnH_2Nupsd9Ivsni8e1-NtXSY1TSdd5Hjrmxs6R9AiCBUxuUlJwtZ9Ll9w1sO4mAU_MVwii9-gvbP-1VMlkGjiwzp0qWZ21KZpmGBeR8umWBb_btVi0ps_avtDZX924KE0INWmaxnwxQr5RK0mbdk0e_yb_zVxUqhhBzwtrRyYP7ZnhMvzMxOMQ9P7v90x-mojMLKKE6ZVHd9E5UaQPzA45WImo_L3NH2XpyHK4NuofC3WCQEpAkKgcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpT3kWxCWcM7eADgdb4eBSMd0Sz2f9CkUFHdfj5CJEuA1g8OQC1v3sDHaCVCnRQrXNYofqU5FQyQhV4Tk0UzKtd-8nswuTvTTgk11ztMAn3gIVHOPX5iXafkMszy2h6dlLfUlWYzTv9peQu2h_DK0wKrQAS_nEZ-lCT3272EZkpPgJoUoB3hPqqfeiVMjfybMEhF71ggjGYFe6ZsSxd4CQKyZ1r7y4NK7qroRcT24f-WrRTrxGi53grjLgE2uM5hRPDIb9zgLMhVo0tgETLESq0Uk0ErrOMPV0ZrMoTJHT52y6jFVCA54_HbmQa_cbxlPrbFPQW7Ca2AnAfzlygBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q29xaelD9QxXh3lfVm7CYMlhjNcntHfKXeWNDO6dfEYGhXKb2lPXJySSodAzA6UlOEcDRn37TQq63sJW-YmFfUxjAgioO7aW_HkEAUmwqPDeL90u3P1HtUH_27W1FQZPD8DwhpOZRlwIsar9tN9VAg6TMLBb_DUywDzFZkcunbLGUw4sPTxKmY6RBg1niRr5Whk-F2X0gI89bJh9g6rH5gWnCzig7Q48uDfAOPBG0HXqKARkN9PauXr_U8jKxLpUL5JRxT7SywZ1eus6x-WaE97inStH01JxXjV13P8ZBXSraVGTZ99QsXxy14LV-KL4S0JgJJ0wOADHOXl__SjxdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFbJ-zeuqLZbDadcdpbalm8B8kEvbRVaap8nYqbRTDeOg3qHLC6bPdfVhWYS7qxyG5apwRPqzl1dFlsLWy4yzBXsy89_z6uPxIhqp1O9GZWwYHBoZz_YUZtB3cbxko9wlA3IddyY6N0jgUurFHtItc3aUC8sUBFPsiESm84mNfkcwpGBTgVF4yIuYheLIyhNqP-YiYfHCTfX5-skjtQ3s7UddRrCNh22TPlDoexseMJYY6zA7q_7OXGtSCr-i5QYJ4l_MjsjCW-S381iYiaTKpqAKoBe1QX34GH5E3ML8wVygSfCQ1Ollvd014tyyCeBr5KMZsGJeN4kYt8TzTo48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdICDZfc4WTZwSewUNjlEVEflW0mNB9MAwdfpreuNYa1lMiPPNcu_eLJ3e2cOP4ufUBDt4_vSuNbRTkNOl-yNz3UcFwmPfSopTt-O7Vr4g8hBW43u-RlrKKrfTNUqLjfrN6C2LU7ODTQxNS_8XlcSK6sAWBKwiUtdBhTfc8YFRWDOpS7GqPCtQlytCirP1-uxqmKgzL-3e08C81OOz3Ra8dSIK0ZVSRKsxWDJ39plAHopka-ZUjy2UId5SZihOv_ECJaJ3CBOB4jkgwkwpNyBgmSKNHZSDSdUfajPHzKkHmPOZYiBkkfQaKfARSkpNdFlSurSNJ0U1aOnEOqEp-dJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3LKt_rZ3_livZxPoPjoTwGmOeDSL0E5X2bLODmsX3-rATKUqmi7KJXvtHnMi1DQVPZUYI6h8Bw91VO2TAfwxmTzXWt3I1eLq0HcmGbLF6QYLQnUmMOwxqc4tqjAlhMyIt-xHLcElDStRXmSwse3QiR1Z_UWC0zEZcv66ZRfjEBBfYDHxbfSIm7JIeAUZE9pj2Z3tjo-BsUROlJvbcc19GOtuqX9j6LLJUirpZJ9VIOLQPDX0x26jZnVO7qUHn8Zuv_9ymBliAI1jQlQrHjsfj0SeYZr-dBt45SXF5UX-n5Bhu55h0zSBFVqdDC9gby2yImm7nbTn2z_Jz0kxLKcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=Ik8g7vd0nVZkI-Tsz4BTGcCB79WwX3Rms_MZncduMyxxMo_VH6TDciR3GJZI7q8B4PMVFEb0MMcA9LuT_GscJwSJdLRdih-rPco0jVdns-znCTzNUpNL4eoAf-tViGOigb5KPFRctZrLAJexHSwkEU5i8W8MC_XKTozPa38_TU5TdaKEXvIrihdR7iaM7ZRgSBMGAaOM4pJkCQq4Pm57dVO5FQMT1e9_4rlnh1wGuCbztLt6jAWU1iFETFbJzQGRclZcciZNTNg9CiIKN_vY1bhm5ZQb1BS_CUV--lOxr3UUkW9O9Pl3uDxfIy8KcVFpgpVeummSqlQe5TWMKPx8mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=Ik8g7vd0nVZkI-Tsz4BTGcCB79WwX3Rms_MZncduMyxxMo_VH6TDciR3GJZI7q8B4PMVFEb0MMcA9LuT_GscJwSJdLRdih-rPco0jVdns-znCTzNUpNL4eoAf-tViGOigb5KPFRctZrLAJexHSwkEU5i8W8MC_XKTozPa38_TU5TdaKEXvIrihdR7iaM7ZRgSBMGAaOM4pJkCQq4Pm57dVO5FQMT1e9_4rlnh1wGuCbztLt6jAWU1iFETFbJzQGRclZcciZNTNg9CiIKN_vY1bhm5ZQb1BS_CUV--lOxr3UUkW9O9Pl3uDxfIy8KcVFpgpVeummSqlQe5TWMKPx8mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDoGyIJMzmnJ4U1GwfzN6ZR0n_XcoOdGNIXruaTEhrKxyatf0onLWSHvJkIGrteufHEBSbVA2h3Vpl810Z8d1yEim-8iC7avcM82oFwM71FqdulJAzDV_soFM1YVZ3zVbexAB937O2H3JRPGQlacuwlYPxpt0XSimx3vREyx6yf_BqcWAFljBhzi9ZGy1xSS-9HeiXCcCyMvco4xy9rKlLQNj0a5ZpDQVQdqqeqr1ZzrEoSr12oVV1lhizEmgbTuoINcoyiyueMzmw9engjVqYKzV704I9YfTMF8Z94PYHnak4U1vP949FikXgc0zct2nL6Hc9SM51GuNLTnQBtemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCB6uHO0QSrDQYyUnn7Ctid9SQdt_aEmekRtxKDGaPoGQnbptiY-tG5NnGZLzqsE73hOnfy29TOeD_Okl1JhCTdnuWqIoK3AVCbS2tkmkMk9B3YzdIpxB1xg753jtV3M7msHzFuPd9EGvcP_s3TMSqf-o5BDV2qfffeCrCMIuv2ey03vtTT4v4WEHcLHDMrWAaNOdnWwgrZGom9c16YqlFqhxuYmOa0teUS43qDGYibF8a-2UqjtrBYxlSUBAB-1RcNq1lx_peQRXqIZ6ir_K1GIquB1-7VlY8pS8h1EWlLnUq8T0cY03EVu-LaaI7MJU0--Ipbo8fo8OlJKexgMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=rIRaXU61RLDlXHPgS89yVCknOatD_qTrKDA4R7Q9wQtX4dIfxaz7iTEuXY3Go8xdkM98MIqy2zAdQvmocLpTYa8D6h9L_a1jAiTKmjHA7GWto6cF2VEaLWyRfldfcBuTIc9qGbhxik9klf8K5p1vIh_siZ5Hzzl1okQWpt58QkabnFU83q9LYM1Rilikg2aiLrFPaH_K8tV62btRMdGqS9IeXzh08MfDCW2AKQMLTXb64YxjPlwZf8QHjI-p4hSZUqJY0VmRmU0RO7wUysE3JQ4eIE_-Hij_7rJ4YyL87_QFWdH9MHR-icpYax-x-uT_OajjMCFyjfVHQF7ZT0FC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=rIRaXU61RLDlXHPgS89yVCknOatD_qTrKDA4R7Q9wQtX4dIfxaz7iTEuXY3Go8xdkM98MIqy2zAdQvmocLpTYa8D6h9L_a1jAiTKmjHA7GWto6cF2VEaLWyRfldfcBuTIc9qGbhxik9klf8K5p1vIh_siZ5Hzzl1okQWpt58QkabnFU83q9LYM1Rilikg2aiLrFPaH_K8tV62btRMdGqS9IeXzh08MfDCW2AKQMLTXb64YxjPlwZf8QHjI-p4hSZUqJY0VmRmU0RO7wUysE3JQ4eIE_-Hij_7rJ4YyL87_QFWdH9MHR-icpYax-x-uT_OajjMCFyjfVHQF7ZT0FC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=QdxqwE6k-9t16qGaPI5ZpwkJCdeXV8ge9bn5lP9PDpggD1ylJG7DVDEkBDsYQufc5QgTUiTvbs5406iayEAORWyO4Ge0lYzH1d9qxFZ4iwEWiyCYAlKXAbj25QeeWOplFASQVzag0pXFdLT1IDGxRsnE9dNdIQJD5_m-Vc69mn6zVQEu6Za7egdPoAyHM6Z0LNkQ3k2ZCE4j7e7hRL6kfH4CaNwApgQguPqyVOzLM4Z1xtFjSrNR6MPEKz_dzP_-xuvVlmvkhTA8tMXGKjYb5w31i0Ur2H8lChl_RS_00cz8SUBrjz-KN-cY7-iHZMzFD8G0YrwLL__ZIrsz2Ajmi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=QdxqwE6k-9t16qGaPI5ZpwkJCdeXV8ge9bn5lP9PDpggD1ylJG7DVDEkBDsYQufc5QgTUiTvbs5406iayEAORWyO4Ge0lYzH1d9qxFZ4iwEWiyCYAlKXAbj25QeeWOplFASQVzag0pXFdLT1IDGxRsnE9dNdIQJD5_m-Vc69mn6zVQEu6Za7egdPoAyHM6Z0LNkQ3k2ZCE4j7e7hRL6kfH4CaNwApgQguPqyVOzLM4Z1xtFjSrNR6MPEKz_dzP_-xuvVlmvkhTA8tMXGKjYb5w31i0Ur2H8lChl_RS_00cz8SUBrjz-KN-cY7-iHZMzFD8G0YrwLL__ZIrsz2Ajmi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=C8dv0PqXdzztK1WJiKaJ6xlKLSj4-05JxI6tFhFkw8uwQJp99k-5fxZKai9mugDwkflqPwYOgmDoZm7dE4Z7jecsrmJJ07bCnjAwr_jBovs8h4ztk9KUS-Z8tpRZTbKifmRmfhZlVZpfXJGjwhRtKoino5mrKadNvV8ZIjbdZVNKKSGqXUhm6l32baHP60Eu0XUwktmqzr7-Y_1dLvrrv-67eJ-PwkO6Y4oYEJQjyOuowHO5sk3MkiCSQazHHMNbOYjIfRTvDxSMvD9dwF0TjwYIidtSX6iB9asxPn-G6cI0JXUsLGRoIi9bphBLr-CZoEHJpg5j0gq3rPpeQpO8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=C8dv0PqXdzztK1WJiKaJ6xlKLSj4-05JxI6tFhFkw8uwQJp99k-5fxZKai9mugDwkflqPwYOgmDoZm7dE4Z7jecsrmJJ07bCnjAwr_jBovs8h4ztk9KUS-Z8tpRZTbKifmRmfhZlVZpfXJGjwhRtKoino5mrKadNvV8ZIjbdZVNKKSGqXUhm6l32baHP60Eu0XUwktmqzr7-Y_1dLvrrv-67eJ-PwkO6Y4oYEJQjyOuowHO5sk3MkiCSQazHHMNbOYjIfRTvDxSMvD9dwF0TjwYIidtSX6iB9asxPn-G6cI0JXUsLGRoIi9bphBLr-CZoEHJpg5j0gq3rPpeQpO8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcFdHKZ9fFBTAPgdT6jZOZjWKH_-oSocE0N_iko4u-fntKrWOBU5hzpsh6u5I1F2-AIiWTvjSit2YWlE5xthzC7MI1Qd915zFy_luUwSd3lHXfzHswHP9zLrlGVvk34fY1csaTqYoAsSqlNygyhb2UidTBURn2oouP4Bbatnnxaa2MeBS1F2Vusre2grTBzYdi7L34jgpUUKnAXd2TNwCPCsu_QDOKL_xVRmte7tM6NZlW3FasTxpH65jcqQEUCYK9c8PHfe9f6NZs7lJDVmidistAgABKQa3gbLPizjfOxcGPy67br7k-Wx18fwXOcXon5dWXIhRdYN37tN7sTGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGWJaVum9fIm64xWZbTHRAjyYzu8yzngeYRU9H4BAZEQve6PKWpDua--YNX63b9-3IF4B2KsfcZ4iW1T8QFWgoAn06EXisfyafw_lnqfLEIQ_qISLXnPoYa0aHh2O0xlEwtVt0DNGinMe-KyKQsM6KLn8JmcydyO6LfsKN27I9ZR2wMAtEj-7DxOMYZ7gEY2ecg1YoeAdAxMoNehcqPmX43eCa-GiCtrAmLmblbgI2gi8olpEJX_RG2bKSrUSmC0dyghPlSyleBqlB15M_rslkSLO2fa7xItvxL_IsG2oxXcRz3LOI2DjlbabsO0D31k7Lgb21KwYr0wIZQT8ca2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjNlW1mUeyMtypBuxDNgszbVHrYtwCDTq_Yrq0mjaf1GmPs-64YDuKCDpKg2RZjwZDvrGRQMPp_tWYmX-zwwdEKWL7JtJ0-cy0fWgAkj71YQTI56TJnZvWedMfIkIrHwqaTzwQTOCL-Sgx22aNR-i29A-dRgIv9nfx1AElumNFeZibUpN1rTpTBPfhvrCp7z3RP_EzwonXWlOpzOOjzroK8r0_Ubag0n2oySZIFNqcwBY9aqFP4QSpop2hGsK-smjXmnoKAosHJsWSZ1Mz_HidQPJfJtAH3zl1hx1rYl93Yb5A2WOgGZLoD6032hfX4gTD872P2EPB5zX1NvQzqqsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
