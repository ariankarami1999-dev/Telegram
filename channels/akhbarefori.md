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
<img src="https://cdn4.telesco.pe/file/gfPRKWKhdEZ941-4Bot_YxMc9Ieum1kY164wcePbBaAyfrHStdqGS1rFIZRNP2mnxt7evizAG3OB0V8U8T3bwl4nKWjN_TQrS1DNAKu09R9Ny1EupijNpi4lKRY_qq55dAlhVgwP10FWyF74HxPXsoiX3sKG0qII9R_ZekNZQ6d4taoMhdh79zHFCiItVCHTMiiQ5_WTcjPRSmZFDowWYmgod1pj-VH8SrAZTkI6kTbvDrO27LT0iRQevySYZ3YalZKSiSHiVzuRd61cgAcMsODlGY0v_bMPiCIPonbtVCOI9wmJVyGeQJssGJIh2xcwheerXJlBo3_8XWOwMjxdRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-689521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
وزیر خارجه ترکیه: سوریه می‌تواند جایگزین مسیر تنگه هرمز شود
🔹
هاکان فیدان با اشاره به بحران تنگه هرمز گفت سوریه می‌تواند از طریق اردن، عربستان و ترکیه، مسیر ارتباطی خلیج فارس با اروپا باشد؛ مسیری که قرار است با راه‌آهن، بزرگراه و خطوط لوله توسعه یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/689521" target="_blank">📅 16:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ee1bed1e.mp4?token=Nq4_-FLW4N7d_Ft9Aqhk7QfN0lU5J_jH-jlb3ei_1j-GExQh4TMBk6UIsQMMMo4ViSvL0CoajjFGnHXB8zZGPbYKTNRhl2fITB1j_Ds6mk748TGnpicmDh16dOglMXDg-Q5AlZnjCs3QxAM9Wmdcfyp0Eths1JP-UsF5eqaK8NlFTEFa9EtFIdJZaymihz-nX12vDl0ov7_nFklFpx6JXlk17F1dx5yQxQEA1a8xFnqaGCpCKxYJzIukXaed1hgAV0uUkNs4dt5fVtSZRmQNtPUuHXL2leQ-k5YZCk8wZBL7QL4fDU8_L3LdqrGen9zwUu3h7BHfpYDD3NirvNJFug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ee1bed1e.mp4?token=Nq4_-FLW4N7d_Ft9Aqhk7QfN0lU5J_jH-jlb3ei_1j-GExQh4TMBk6UIsQMMMo4ViSvL0CoajjFGnHXB8zZGPbYKTNRhl2fITB1j_Ds6mk748TGnpicmDh16dOglMXDg-Q5AlZnjCs3QxAM9Wmdcfyp0Eths1JP-UsF5eqaK8NlFTEFa9EtFIdJZaymihz-nX12vDl0ov7_nFklFpx6JXlk17F1dx5yQxQEA1a8xFnqaGCpCKxYJzIukXaed1hgAV0uUkNs4dt5fVtSZRmQNtPUuHXL2leQ-k5YZCk8wZBL7QL4fDU8_L3LdqrGen9zwUu3h7BHfpYDD3NirvNJFug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دلیل افزایش شدید قیمت سوخت در سوریه، اعتراضات شدید به رقه و دیرالزور کشیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/689520" target="_blank">📅 16:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه سه و صحبت های جالب مجاهدان انصارلله یمن در تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/689519" target="_blank">📅 16:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
مهم‌ترین محورهای بیانیه نشست بریکس؛ از محکومیت حمله به تأسیسات هسته‌ای تا حمایت از الحاق ایران به WTO
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/689518" target="_blank">📅 16:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مهم‌ترین محورهای بیانیه نشست بریکس؛ از محکومیت حمله به تأسیسات هسته‌ای تا حمایت از الحاق ایران به WTO
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/689517" target="_blank">📅 16:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: در دو استان کرمان و سیستان و بلوچستان خودروها علاوه بر سهمیه خود ۵۰ لیتر سهمیه بنزین ۱۰ هزار تومانی هم دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/689516" target="_blank">📅 16:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhaJxDnJNjf7-yAZCARlkdhInLv6gwbVYU0pwDvQJC5J90iBICy4Lje7StX2qX8bOIplC7t0knLdNDjk43WzlTE4LuvcFn7LV_lLlKfFxjLXr5_e8vb69FgwqbvyPhG8k99_KA02w2iEp7qLX5GbIeNq7sXFWGdylzOGrDTFHVi47-ltcEnMfDduED6IrqQeqWBNqqPvxgSbwod5AJkW4woaa-LMKBgwWiZjXydNLOWZXl9PTgVyxwQ9MBxLKHru3mkj6fTrpxKi-cwUR3rT3hPQlJZhbsz1Ge52v06pJdZCAXgTY-N8WDKG6ra40PidL2CHesx77WiQt7V6OI7lSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
لورا روزن: قیمت بنزین در واشنگتن ، برای دومین بار در هفته افزایش یافت
روزنامه نگار آمریکایی:
🔹
اکنون قیمت هر گالن ۴.۵۹ دلار است. این قیمت روز پنجشنبه ۴.۴۹ دلار و روز چهارشنبه ۴.۳۹ دلار بود !
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/689515" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/689514" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c725d14d.mp4?token=LE6r6iwYFvQBUajLn83HOr196B8TlnvqjpAuCLATjKzbNHsXVh_ltwD1hQh-AfKWgilbyQz0rki6BA1xOfnEYwDeUePi6mNb2bh2yftdYwDP5j5dIQMoE0CE1Wogy3YIg_mhjMSM1jeRQmg0_wvhfHZ10wVFj1xTV2vivJf6SY_B7MSG1v5cwTZXJnCv_miD5hWj8oiYbL4tS1yVpS3-VwmKnYpkpUZQ9P2bvyHBizyy30UEh71a-h4s0kfZmZtMgrMz57nowjkcwHrmlSgjQ8qvwCMlSRj3SgbbGQ7WiEHo7cjbv3-QPn7Thx2UPPp-T_stZS4sYZ4CZSlqlNsPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c725d14d.mp4?token=LE6r6iwYFvQBUajLn83HOr196B8TlnvqjpAuCLATjKzbNHsXVh_ltwD1hQh-AfKWgilbyQz0rki6BA1xOfnEYwDeUePi6mNb2bh2yftdYwDP5j5dIQMoE0CE1Wogy3YIg_mhjMSM1jeRQmg0_wvhfHZ10wVFj1xTV2vivJf6SY_B7MSG1v5cwTZXJnCv_miD5hWj8oiYbL4tS1yVpS3-VwmKnYpkpUZQ9P2bvyHBizyy30UEh71a-h4s0kfZmZtMgrMz57nowjkcwHrmlSgjQ8qvwCMlSRj3SgbbGQ7WiEHo7cjbv3-QPn7Thx2UPPp-T_stZS4sYZ4CZSlqlNsPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای بالای یک میلیارد تومان مشمول سهمیه نرخ یک و دو نمی‌شوند و تنها ۱۱۰ لیتر بنزین ماهانه با نرخ سوم (۱۰ هزار تومانی) در کارت هوشمند سوختشان شارژ می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/689513" target="_blank">📅 15:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وزیر راه: پروازهای خارجی برقرار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689512" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای سواری شخصی ماهانه ۱۱۰ لیتر بنزین سهمیه‌ای دریافت می‌کنند که در سه نرخ (۱۵۰۰ تومانی، ۳۰۰۰ تومانی و ۱۰ هزار تومانی) در کارت هوشمند سوخت شارژ می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/689511" target="_blank">📅 15:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efae34b51.mp4?token=HS1n2UDpRcOJervNEkGcYzpIORePlQGAbpL25RWKxbexDWLgR2PJZFcfpTaLcf9p0KCq1PCH-Q3oHAXEZKPFRupAf6pYDXldDG57eR5tMY7xtjwlbyeGdpfw5RyY3paMkkisA3pDeNvewWogumNGylEzKniIgQFj6agND9YGDrN94poVoNOpHg3lJCVvne5a4QsK37GbLbIe-NpFaDmABdhAT_D-OxNMEY0L0iK7-vv4G73qg3QC1ibX8X8-375F9DBoY4ehcGDGlsrCetOMM_MoRScuolwOLSM_JmVhDkPheCv-avYTXRcgeKI8t2SU9mkYJZNaTEsxTiD-XwXj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efae34b51.mp4?token=HS1n2UDpRcOJervNEkGcYzpIORePlQGAbpL25RWKxbexDWLgR2PJZFcfpTaLcf9p0KCq1PCH-Q3oHAXEZKPFRupAf6pYDXldDG57eR5tMY7xtjwlbyeGdpfw5RyY3paMkkisA3pDeNvewWogumNGylEzKniIgQFj6agND9YGDrN94poVoNOpHg3lJCVvne5a4QsK37GbLbIe-NpFaDmABdhAT_D-OxNMEY0L0iK7-vv4G73qg3QC1ibX8X8-375F9DBoY4ehcGDGlsrCetOMM_MoRScuolwOLSM_JmVhDkPheCv-avYTXRcgeKI8t2SU9mkYJZNaTEsxTiD-XwXj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای سواری شخصی ماهانه ۱۱۰ لیتر بنزین سهمیه‌ای دریافت می‌کنند که در سه نرخ (۱۵۰۰ تومانی، ۳۰۰۰ تومانی و ۱۰ هزار تومانی) در کارت هوشمند سوخت شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/689510" target="_blank">📅 15:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxMB1Aqkb0XSNerq5XxFmdJpqwXrKKeUx6AgMM87S6Eiv-eGBIXt3fHR2GputgFIGy8ywKD3CGYMPOJ1gSSS2dW8C0aY3lyRJU9lQZod6d7mzfDAoTfK2-Wy7k_-jM8Y5li4aGyZgkgzrkezePOHag-BWgTwMbw5SfQ3CbEXJTR4hZlwi7Kr8yqk51yA8fYvkXI3EgG5WGJC3p67FaxXf4dsi2ASWKkYyojkJN4cubS9nCuHdR9w954BVAUjh69Z1lYizCJ9n9GI_s3pvf8vn8BCnvQo3NyQJu71ZalaEOahXrpREt8vS57nfxWFAV2kXSQL4OQ2MDmS2BRvtwcLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس نظرسنجی‌های جهانی اسرائیل به منفورترین کشور جهان تبدیل شده است، با ۹۷.۵۵ درصد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689509" target="_blank">📅 15:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwSsDLNZj6-zmALD9Kbi-91YNzayOl9LbjqG5Meu57euPdKD-0HP6Wm_MGFOQ2KNwqb_VcQKl81C8amODWpa593hYz40j5NjitFdL5vcFupJLMtnJXd3zedeA9BPicoF0UWKzVcNe4ra3q2Cf1NlaQ4uLI1nztqEvnU1JUkxiHns3ifhyZopwRwLRVv6O-66ExjtcIbwA-elRIYJNb3tIX2ZvA29qE1j1_FFLKzuEA0Rg3v0Zap7vydey4aU-Tt7pVMnBc4drXTJja6PNuKtPxXDsjjKsn6N7nMrGARBblfeAAjAJXHZwbExMORdP4kkyq_B_79KoEplo5nxmxFhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نایب قهرمانی سهم شاگردان پیاتزا/ سامورایی‌ها بر بام آسیا ایستادند و سهمیه المپیک گرفتند
🔹
ژاپن ۳ - ٠ ایران
🇯🇵
۲۵ | ۲۶ | ۲۵
🇮🇷
۲۱ | ۲۴ | ۲۳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/689508" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b56220818.mp4?token=haiW8jmRHeb-IyNgV1csUtjo3zI9zWJiRfPnY9PUPymy7aX1Bt8ulLIAHyPjANdWvgO1DrnHZ9g697Hz8WtFkUsn9tq8ZLnh-fPLLKtNHWH6CE4vknfLwdr43EfnYPDYYypDyJLZ11XCyHaVYwhiiRWxPkaE99Xf0AkvHy1GyCLlrA8DQFMQzlBAeBSMA8-PozXhgJ8GaW-Ho0fomAvF6dAZfw6q8NO48ghkZflVbIM4E8fPXTfQYZJX7_OnddUvEYKzIZ0Yvq7F3aNU88qaf9qI48VDYPixlAmfubJhZGxvA9OtKe_flRXnwm5Eee_eBUgl7zOb56aWMIWn-_bxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b56220818.mp4?token=haiW8jmRHeb-IyNgV1csUtjo3zI9zWJiRfPnY9PUPymy7aX1Bt8ulLIAHyPjANdWvgO1DrnHZ9g697Hz8WtFkUsn9tq8ZLnh-fPLLKtNHWH6CE4vknfLwdr43EfnYPDYYypDyJLZ11XCyHaVYwhiiRWxPkaE99Xf0AkvHy1GyCLlrA8DQFMQzlBAeBSMA8-PozXhgJ8GaW-Ho0fomAvF6dAZfw6q8NO48ghkZflVbIM4E8fPXTfQYZJX7_OnddUvEYKzIZ0Yvq7F3aNU88qaf9qI48VDYPixlAmfubJhZGxvA9OtKe_flRXnwm5Eee_eBUgl7zOb56aWMIWn-_bxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در یک کشتی در تنگه هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس در به‌روزرسانی اطلاعات خود از وقوع آتش‌سوزی در شناوری که در تنگه هرمز هدف قرار گرفته بود، خبر داد.
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد کشتی‌ای که پیش‌تر هنگام عبور از تنگه هرمز…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/689507" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b09d3e442.mp4?token=T2vbLg30Y8fhM57jcwWwja-VQe_9frVLkCqOJabe6jkZBBWfm4O9HQU3Ttg33Jxg6OejK0nao-YYHjGFeKmP0PC9fnECOmJ4AlFNpZMCFWSGb9xkuhJ5hqvEHLOHjbdTGuVSUrrmA3Sem73s9_49O6bsKvx1C66-qLAJ0kqQ2AlPCml1cbgBkE9qpbtALJfjsgdxfsCCykR1PKXLDLgOqTep-55p4b_9rLuG0iSdZygQeuAD8szis1x1Dg76nAMyfJRjRPIQTy-6eYWkmUmPONlZW-4L97d61uG9SpY2iCPvgNsiO20F7ZYe2eFt6Lggpf4aBac3ryS3DNuWlTRFqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b09d3e442.mp4?token=T2vbLg30Y8fhM57jcwWwja-VQe_9frVLkCqOJabe6jkZBBWfm4O9HQU3Ttg33Jxg6OejK0nao-YYHjGFeKmP0PC9fnECOmJ4AlFNpZMCFWSGb9xkuhJ5hqvEHLOHjbdTGuVSUrrmA3Sem73s9_49O6bsKvx1C66-qLAJ0kqQ2AlPCml1cbgBkE9qpbtALJfjsgdxfsCCykR1PKXLDLgOqTep-55p4b_9rLuG0iSdZygQeuAD8szis1x1Dg76nAMyfJRjRPIQTy-6eYWkmUmPONlZW-4L97d61uG9SpY2iCPvgNsiO20F7ZYe2eFt6Lggpf4aBac3ryS3DNuWlTRFqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی توهین صورت گرفته علیه شهید رئیسی، علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689506" target="_blank">📅 15:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حمله دشمن تروریست به یک کشتی تجاری ایرانی   فرماندار شهرستان قشم :
🔹
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
🔹
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند./ صداوسیما  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689504" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3221d421e6.mp4?token=YOdODcSDZBPPgGNwJ_guixZ_4P5Hdles-gCGiSgkCy6ryhMLdWcwAlvuEukedHsSI78V8sf_Ns0oBJV3BEOo8ZQqlKMqEXeJ6ve8i8Qwilpalt_JTJ9CF0PggfP9LdBOQrTp6zGo-K9EFcqTlaP_DVPIpjyk0CRbXXzU0iutlP3uGDEKp_-MVvtSagH-qnOJzoU-rKtx16JInUeKJrazm2cQ1D6bi3ta0vnXzE5sEwLgFl5n5XcuRnPUoSUc5l_ivGbs-inN55wPcIqs1vGaF6cskucimmY0PF60vCLEByqzSAcVjsCeJKANGPlEBQJGj7GQBjpX9O8bGfLAvnrXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3221d421e6.mp4?token=YOdODcSDZBPPgGNwJ_guixZ_4P5Hdles-gCGiSgkCy6ryhMLdWcwAlvuEukedHsSI78V8sf_Ns0oBJV3BEOo8ZQqlKMqEXeJ6ve8i8Qwilpalt_JTJ9CF0PggfP9LdBOQrTp6zGo-K9EFcqTlaP_DVPIpjyk0CRbXXzU0iutlP3uGDEKp_-MVvtSagH-qnOJzoU-rKtx16JInUeKJrazm2cQ1D6bi3ta0vnXzE5sEwLgFl5n5XcuRnPUoSUc5l_ivGbs-inN55wPcIqs1vGaF6cskucimmY0PF60vCLEByqzSAcVjsCeJKANGPlEBQJGj7GQBjpX9O8bGfLAvnrXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد روزنامهٔ عبری به جوانان آمریکایی: با ایران بجنگید تا بدهی‌هایتان بخشوده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689503" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKIjZeW4eCx5Q79beKOftvB1YKdUIyMJwExkBPKqkMOd4ALACnhtJIwz1M557lg2a2MmPHxK9tSvoAdT-C4VO1GXhEwR-cVSY4dlne4GiH20HJMqVPQ3t9jrYqtj85eA4M1F4l723HqMPxMj1QpXwHoRNwtEqOSwvBPEMltPv8FY0MYEaWceYStQk5WxUuPs0lepS5ehxBND5NzSmH9MvTNACfDf8hx_dLiv_5d3ZFUxT20Hqa1xhe14PyqiFvJCwPpgW2oZPakRSakzW_qR7Tdv3Mg26ERHqqI_jk7TOuzneLx4Hak5oKN13o92MGAgPvElE3brsPlvYwfu9nuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر بنیاد ملی نخبگان از دانش‌آموزی که جایزه البرز را به بازسازی مدارس طرح میناب اختصاص داد
🔹
سعید خدایگان، قائم‌مقام بنیاد ملی نخبگان، در سفر به مشهد مقدس با حضور در جمع خانواده نیایش امیرپرست، از این دانش‌آموز برگزیده جایزه البرز ۱۴۰۴ تقدیر کرد.
🔹
نیایش امیرپرست که موفق به کسب جایزه البرز امسال شده،
تمام مبلغ جایزه نقدی خود را به پویش «فرشتگان میناب» اهدا کرده است
تا این مبلغ برای بازسازی مدارس آسیب‌دیده در جریان جنگ رمضان هزینه شود.
🔹
خدایگان در این دیدار با اشاره به اقدام ارزشمند نیایش امیر سرپرست، بر اهمیت مسئولیت‌پذیری اجتماعی استعدادهای برتر کشور تأکید کرد و آن را نمونه‌ای از پیوند موفقیت علمی با خدمت به جامعه دانست.
🔹
در پایان این دیدار، هدیه و پیام تقدیر دکتر حسین افشین، رئیس بنیاد ملی نخبگان، به ایشان اهدا شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/689502" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPt6l1NGRMwz9QzxutSizs7x_ecD7A7pPCH7faKngoMkDhGJcC6wZPCnsM02vYI0m9mQkGlhmlzo5TMQAFNRmXaqktKh_XtZ9vfchUxYDn8Uw9Eh-Pr6m8jRVuVrFMlUK-Uw632cxHdYRzhOpXrOsnOWFG-7rhc5xUfSUgTJxr6TxIdVoYtbUREhIqSkF8B8tzOJ3q2MyzEpU-Ke-p1hihyPUhp1lSOm52JlAnUQtzLnYMqsolSkOQXKJC7-4sqUsdrvE8E5C8fCBrKb4l7hCYpgXrRv74S2EGl0RUW5sHhLZ5G4Qa6QKYFhpI00sR9vua0aIu5S9qLjIizZTZfYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت وام با وثیقه‌گذاری صندوق طلای «
رز ترنج
»
امکان دریافت وام و خدمات تأمین‌مالی با وثیقه‌گذاری واحدهای صندوق طلای «رز ترنج» برای اشخاص حقیقی و بنگاه‌های اقتصادی فراهم شد.
واحدهای «رز ترنج» از سوی بسیاری از بانک‌ها، مؤسسات اعتباری و سکوهای تأمین مالی جمعی به‌عنوان وثیقه پذیرفته می‌شوند و فرآیند توثیق آن‌ها به‌صورت آنلاین انجام می‌شود.
بازدهی یک‌ساله «رز ترنج» ۱۶۰ درصد بوده است.
سرمایه‌گذاری در این صندوق از طریق تمامی کارگزاری‌های بورسی، از ساعت ۱۲ تا ۱۸ امکان‌پذیر است.
☎️
اطلاعات بیشتر:
۰۲۱۷۹۳۲۶</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/689501" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: نگاه‌ها به واکنش آمریکا به نشست مسقط دوخته شده
🔹
تهران نشست مسقط را اقدامی مثبت برای بازسازی اعتماد با کشورهای همسایه می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/689500" target="_blank">📅 15:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk3IJ_jt4pPrOaSyjUFiHrUOFN8n8vU96qJcPsoJ3nRJkKoyZ864WMpQ3adKJ-d0MH_kaE3pSXEgnA25HgDNiDXfNyJh8mIAoJcQuknA7JpG_Bw0l7bvv6bs3GkoW6YGFGAPZPa5wcbvBzBFQr-TzRsM7wajvjarIT5ErEkQSZwIhSbUC612dtF9wMU_yR5zCLwqHWHoSFcSQ57yVDV5JsYEiwoy9uLhxH7YcLk94YbZ_NYxMUONvXF94HENvgq9sQiV0-v3I8C8F2Zw_kr6wjEXRo1yFDkPXnn5IU3j0TDWgszfpcBpKbbeEDgfaMlAg-udjmxOcGjMop4RGRpIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۹۷ درصدی تردد در تنگۀ هرمز
🔹
روز جمعه تنها یک نفتکش از تنگه هرمز عبور کرد؛ درحالی‌که سال گذشته ۳۱ نفتکش تردد کرده بودند.
🔹
اقتصاددان آمریکایی: «به لطف ترامپ، تنگه هرمز عملاً بسته شده است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/689499" target="_blank">📅 15:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dea74856.mp4?token=S0ipSXdTSdbt_jzr-bSDlKeLZ7AOLRGH-7B2urQ8C1sBP1hz3i52c9dXLbCwBqGN40aloxA37UFPyl8PSKRhhLW-BtZjE9cVciCw5CdmZBqrsv180dW1nnB1INaKziXln5K75p9tss_xfwlYN7C3vmD9TiCPKCeaPMLoTbic4kOrSRkn2Ss_CfUUfLHQM2Fb-7W5IOUfuNez__HYOBAsH6UEoHbMQ0eDAa9KgcsTarCo-CptpU6oDcK6rg7VEFZgbObCsuLKnmppAoVxSLUrlCROECEbmGpzNcxUlRt0y3Y6Kz8HIxdqBP42W26pwcjtWAqwnRS8ksQeSxyRIQCatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dea74856.mp4?token=S0ipSXdTSdbt_jzr-bSDlKeLZ7AOLRGH-7B2urQ8C1sBP1hz3i52c9dXLbCwBqGN40aloxA37UFPyl8PSKRhhLW-BtZjE9cVciCw5CdmZBqrsv180dW1nnB1INaKziXln5K75p9tss_xfwlYN7C3vmD9TiCPKCeaPMLoTbic4kOrSRkn2Ss_CfUUfLHQM2Fb-7W5IOUfuNez__HYOBAsH6UEoHbMQ0eDAa9KgcsTarCo-CptpU6oDcK6rg7VEFZgbObCsuLKnmppAoVxSLUrlCROECEbmGpzNcxUlRt0y3Y6Kz8HIxdqBP42W26pwcjtWAqwnRS8ksQeSxyRIQCatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین چرا انگشت‌ها داخل آب چروک می‌شن؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/689498" target="_blank">📅 15:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689493">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه: برای اولین بار حقوق بیماران پروانه‌ای از محل اموال توقیف‌ شده آمریکا داده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/689493" target="_blank">📅 14:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689492">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ee587791.mp4?token=aYzj_mkzWHOucBaJGD9HAgd77n85vqPqSYspdyGFVOUiBOQZ_5G531vYAyuNL05b2S3JWF0lU9SKYAbhKfv6LDVoZOgXGfTtO1UjTmU_rvXxbUkNi3j5sio6ybuUm-vssBymlZ4izWBiibnO3HgFkQPXEs4-GG6hYK7JZR-hFjXQmnU3XTQko0avXjyO6XQ-37bMg9Z_6UoVX3g8DGcSMiTi4I0Y1Owt2Yn159d5bv6jo07xvrgv7B2CL_mudB-6MDrbfC4YZaunEgXWCmzF2-Vkk2ksZvmxtg3HJmcPvYesH31wumORXq2v2sn6U52NVdy2naXkVA8X3GWUigtq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ee587791.mp4?token=aYzj_mkzWHOucBaJGD9HAgd77n85vqPqSYspdyGFVOUiBOQZ_5G531vYAyuNL05b2S3JWF0lU9SKYAbhKfv6LDVoZOgXGfTtO1UjTmU_rvXxbUkNi3j5sio6ybuUm-vssBymlZ4izWBiibnO3HgFkQPXEs4-GG6hYK7JZR-hFjXQmnU3XTQko0avXjyO6XQ-37bMg9Z_6UoVX3g8DGcSMiTi4I0Y1Owt2Yn159d5bv6jo07xvrgv7B2CL_mudB-6MDrbfC4YZaunEgXWCmzF2-Vkk2ksZvmxtg3HJmcPvYesH31wumORXq2v2sn6U52NVdy2naXkVA8X3GWUigtq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک مدل متفاوت برای بستن بند کفش اسپرت؛ ظاهر کفش‌تان را خاص‌تر کنید
👟
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/689492" target="_blank">📅 14:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689491">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
«بنیاد شهید آیت‌الله رئیسی» از این بلاگر اقتصادی به‌ دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/689491" target="_blank">📅 14:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN7xlOprEAKd2YpU-Vi4NPolbHHb7JnU2V1Ssoji5uYoesq10LUr1yDqmpNInN92uF0aDSe0LKjPA52HCih6wqqx45TqoJ-frXSoxMJKoMd1EKbfnjCCXUDrGIDyrzsmxHbZhv6SHsns3xIKDaGXICIWhSZ9glmFN3PJiRBI2lEJw49iiWQ98pTo2R8gHKHEdZGxulM2iMoWN23AjZCLm6TEJJB89gPewhoNKrifU27exaWf1sMLIMy7jyE4u73LMRPyURIaH8p9nNBwu-3L5unJcRmqfWLfLZrpJ5B8TSLgntGaYQFIP85GYDlys8tjx9eRkTGC4GXCJnE-7vxiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: سردار عبدالرضا شهلایی یکی از فرماندهان ارشد سپاه پاسداران، حملات ساحل جنوبی یمن را هدایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/689490" target="_blank">📅 14:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct8EFCsT8bi-rwmzrrYtqNT5ymHeVJ11ig3WRJzEI39Qci0v4jjb3l6z0BKDIPzLHIEcE3iEs34NhrjB82Gc15kwclyv-0nHmQwFF23dI84gqoiHpUZv1uYTtCtJdG7Tqd7pneCJKApIdUAoyjnjt7h9OQC6iq-v3X_kyWJl48GTwhKYdg6Ty0r_DN2_BX_3OsKP8863osyvpPN9tMiB4K4QZdgfbcb0ix89CfEwcKyjVsd5xCAznVpTU7PVx68mDkBzGcKKqe64lHS2imDgLD-KiNC3PO9Nxie-O3j_rb9qTNsQ7UQIz9jkdUCA7DhM21kNs2AncDEBCOcE41CW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر مریم میرزاخانی روی جلد کتاب ریاضی دانش‌آموزان ایتالیایی
🔹
مریم میرزاخانی یکی از برجسته‌ترین ریاضی‌دانان ایرانی بود که در زمینه هندسه و سیستم‌های دینامیکی فعالیت می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/689489" target="_blank">📅 14:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات توافق ایران و عمان برای تنگه هرمز
بهنام سعیدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات روز دوشنبه ایران و عمان برای یافتن یک راه میانی و موقت برگزار خواهد شد که کشتی‌ها و نفتکش‌ها از آنجا عبور کنند. این یک مسیر میانی است؛ یعنی دو مسیر رفت و برگشت و یک مسیر جدید در تنگه هرمز.
🔹
مسیر ورود به خلیج‌فارس در آب‌های سرزمینی ایران و مسیر خروج در آب‌های عمان است. البته در مسیر خروج هم یک بخشی از نفتکش‌ها در آب‌های ساحلی ایران قرار دارد.
🔹
این طرح به نام «طرح جداسازی تردد» نام دارد و پیرامون دائمی شدن این مسیر عبور، هزینه خدمات و مدیریت آن نیاز به مذاکراتی است که در آینده انجام خواهد شد.
🔹
این توافق ایران و عمان به مثابه بازگشایی تنگه هرمز نیست و تنگه هرمز به هیچ عنوان باز نخواهد شد تا زمانی که آمریکا محاصره و تحریم‌ها را بردارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/689488" target="_blank">📅 14:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
قرارداد فروش نفت به «آقایاری» با مجوز وزیر نفت منعقد شد/ میلیاردها دلار پول حاصل از فروش نفت را پس داده نشده
🔹
ایلنا: معاون وزیر و مدیرعامل شرکت نفت در نامه‌ای به نهاد نظارتی، بدهی چند میلیارد دلاری «حسین آقایاری» تراستی را تأیید و اعلام کرد قرارداد فروش نفت به او با مجوز وزیر نفت و بدون اخذ تأیید کارگروه مقابله با تحریم‌ها منعقد شده است. در این فرآیند، مدیر امور بین‌الملل نفت مسئولیت را پذیرفت و تخلف در پنهان‌کاری این قرارداد از شرکت ملی نفت ایران محرز شد.
🔹
در این نامه، مدیرعامل شرکت ملی نفت ایران بر بدهی چند میلیارد دلاری آقایاری اذعان کرده و توضیح داده است که قرارداد با وی با موافقت وزیر نفت و بدون اطلاع و اخذ موافقت اعضای کارگروه مقابله با تحریم‌های نفتی به امضا رسیده است.
🔹
در این نامه اعلام شده که در زمان انعقاد قرارداد با آقایاری، تنها مدیر وقت امور بین‌الملل نفت از موضوع اطلاع داشته و این مسئله از شرکت ملی نفت ایران پنهان نگه داشته شده است.
🔹
این نامه به صورت رسمی وجود تخلف در فرآیند تنظیم قرارداد با این تراستی ابربدهکار را مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/689485" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
منابع خبری از وقوع انفجارهای متعدد در شهر بندر ینبع در غرب عربستان سعودی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/689484" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f99f97e717.mp4?token=VLwbtDNcvCsOq-QAGDsJBN4lf6jdYwThsbT2vEEsdm4-0mlioUCPvfEIGOZuradflQrqNHgxxAblKY93fkUEYG6srVJ6RVapfRxzvofAoKgutpvhSKbtwDA8ka2EMmFtK55_YTT68cHvqG5McZfM8p_jP_Iw3A5TVEHpknGcDvezZDFr4ccy6mlnPcid6bJTGxtb9EEe6bogaL1ntbmKwXDdumyMMZBGr120NstNw6BXepJz9fVCWQw6Y6N0qetBjvy3Rn7k84Uskdn3aW21sTIHwpQPL8-Z0cIdPD2GiCZby7F7O_J2KyMUlzKxGTbW_IYYKQGvWu0hnbyNQWXF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f99f97e717.mp4?token=VLwbtDNcvCsOq-QAGDsJBN4lf6jdYwThsbT2vEEsdm4-0mlioUCPvfEIGOZuradflQrqNHgxxAblKY93fkUEYG6srVJ6RVapfRxzvofAoKgutpvhSKbtwDA8ka2EMmFtK55_YTT68cHvqG5McZfM8p_jP_Iw3A5TVEHpknGcDvezZDFr4ccy6mlnPcid6bJTGxtb9EEe6bogaL1ntbmKwXDdumyMMZBGr120NstNw6BXepJz9fVCWQw6Y6N0qetBjvy3Rn7k84Uskdn3aW21sTIHwpQPL8-Z0cIdPD2GiCZby7F7O_J2KyMUlzKxGTbW_IYYKQGvWu0hnbyNQWXF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مهندسی، از دل دریا خشکی می‌سازد؛ راز ساخت جزیره‌های مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/689483" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxETk9zR3ypOZGqr_2Nusu3vpNhWB-bKtUiISQqmp3mtuSzJO1fNT4W5wVWuKO4Bp82h8Fs_Jl2ABnLeQR9oEM8kK9cTIiytQTjytBIc0H5-xX6ZUoJJADKb03KTk7tqFUmpg7bn_MyBPrM8FL6q44q58NeIi0uzeONNbUWoGZtRH7KDLk9z7zgtUhRPI6lSM1oUfUjqBcZxKM5kC3BsKWzd2DZYlnoJ0O7KjR56WXtmUk-u7cOKPHU-Evig9_hoIPylQqEndoBt0gaLAK9PHxNCJbsdMRTW240LHoJKDf3-eOMgqy_-fBDEFD3g44kyBwmVeJvRQoybdNV8c9XF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آقایون‌عزیز با این نکات قد ایده‌آل شلوارتون‌‌ رو تشخیص بدید #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/689482" target="_blank">📅 14:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689472">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhhoSYOOwXNrop6zYGRviWNxYl7zWmS0hIO2a5NAj_DjBh-AUQQWc8_yYUinWnD7IZfjuY2ivPPqdz8Rw0V3zisHWmSW6e6Fakwv0_GTSzn2uWAbWM8qmJUFJD8oVdOpY_W6oRXaHmV9KFG26-T94ndCrHYzvCHpj5ONNNLSmav_q7EQq5wJmhqO-Wo27Sof_cEDYARGXycBK0WTAh-AanPJn_4m9b6xr_d7w6vlU-v6C_Bot0cDQwC2Wo7l4ZuZtZWCa8wjsywSegSRpaH2jozhIKQgtw4Ps-Wlxj1z5fyURKb-vxtMyyNm0noth4nvZz1MxEY7Fx3sd9L18PIWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLio1LmLJBaGLcJM1RFpssGdlSh4rTEvojYGMQVHKoJh_4VWWk4gtPzMK5tD6VYu-ikMrEs5R_33fvmtZeoCC1yqYPCEu6RQoVTcFasjeZhhG9bMklxPOGxm-AhFwXWy6t-0LBiCnuMh1b9C96N6GjZCyHw_31zNLGkDX7ddsiDiMRedj8zRxeF7-q-pjqqOuBqmG1leNNV2vIOOwPYIs-lYwJPOo7jZeCADPKjOx-rrlVn6VIPfVZbvpI2PxDFLVDdSdTuDAKsyaDEr6GezMCHQGfaCRmzI6VZ5KuJG5vlJ0YBBmK1yK4dJXrkwlXB58_WM5_K3nw-_uIZvrN86Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_F9Lwg9stGHVkc2J0LZSAYxW5s3m2qHz5qjmjsAmYN69cDk-H4VFOapZvHf2X6omaduysj6b4ju5HZb9vz-sfHnXhzh_HaqMr-sIc1c-ILO-_YjOZ2eVcy0pkWEGLOwYaCS8jYgVspFWbmEfdoXwGSvtzzKyqsDCtchUXrNluTIeCDpa2EdDiz2l2yKJvON2VGXbY2vvg6fTTDrnLAoiJCAdN_BYOHVi6vVdc5KeMy2eM1vXJLhKszdUkJaaWoOb5ed9GuiuhbdYswN4YHHZ3ywblmEDNMzO8l7EOkjcaKa44FwwH7ff8T7iNaMDiKJvUtthAvh1X9wfF50rTD8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bp23Wy5ZurpC1Qv0KUP4VHDXNPGumjr09Gj0opzBT_qeSv9UJlvd-pTR--lZpVlx_cLhsu2kimkwlMPqh1F4JtYEoD76j-xxm-caWx0QZazMtkJB0vuSigb6qgkoZNcSpJ_BwmHutEhdgLjtrvYR0ts-LYu1zg5LUDrmjmQq8pGLwP4I42x-DpXYe3umu32k4GFhcJ68aX_rSskIpL-BbzDTFBDuZQ5o0J9MMFloOPEiNg0Nz53xAzw2brW0yFCvl20pxW0pvSsZZ0E6wgkUnCsQf7LkdX6I821LhIRHqy5iMSlssatnmS9BAAFQzNuoBMRnyykGKYGWGsOtUV30Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XReeE7cCA-EkVUMCRC7217GxwTXXVXMxDzgqm26oS16USWBMdd6gYdoJNaCkSLLaK9C4Gz6pWb6jyxnCcRZFbZG_fRAa5g8Fd8wIvFEB6utjvAPndG1TNxt-PlfnGDRjfsjMzT7f8B7ex_N8r8JEw0UpuThkr4lklzr2riWNukN1x4y4Ole7--LeUdZUs1mS3FJfyZN4FhqgwQHk7gaws2Pn8O2d3A1h33yD4OQ8-HCuOqrRuvixLEzStohqZXX12ofALF9OJM5q0ccSloBUgdjf5CFhcs9pN-MVqT_ugip8CWKy_hdJ9ewGOFfD6uvNOhut0oY5Z5hF5-gewx4KEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMxOHEJgxoto1cCtimWjOcmkRh2QPOhlcvJuA2HSCgvHpq6AgOUMhH7hNa4pVU5ZIva7DFzEOv65VUwZ522MfS3MbbjFfy0acdKQg-T-Gm9outLDqtBEcSn1T4WgnSX7ii-5iE_EFoFvW7_JcRA-EOfC4EEeDm_KgBIgEBDsm_cbmZUbWRj6AWeiFZlbBy7pIyiSsnkOWpSEQyopKf72kMraN1ht9BEqZR1vZvecqNtQLhPeqGisyIWlg_mHad1VnVxv8z13P2vMtVsWekKorj2badg9bzjmRVK2T2kBn-wGK7n4nRsnvXIOvWXZ8zcWK4D8GTv-pJnmgMHOVS9nQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAYHDzyOFmNiyWR_IK3FdUy8K4ic5CTvVjmfpZd2zAH2tfXgav8b5sOmhWyA_xGQ_5cHKDlDAazTjTfx7GmfkO-Y9rMicts04yJmew4eI5FUYo1zwrd29qWE3GRVg1quaN1OephYfAVsJ7XhGY8iPVIU7fvUrAsEOwOcpbbz05Zw8I6ZMiIFnNd3-U_PZh2lYWS5MHVoNdEQ60RMh416LFX8P4uKetwtribzSbxmKZBOZOItHP6fYGBnpU7pQc8QFbBDqJhsLQLaWa72pZq0byYOFSmWVIGV__cthkdpovb_kHroLrI8jhxs9sKAKYNQIdz-quN_9s0JkE1nZzSpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9MzSf42H-LvVr8YDoi1QQf1QIXvGQuHQ2vQq6qtyv6WorGNgot8X2daQYuNljLnxAsxGcYCU4FAJyaelcocZQVikypNFwZpyOnyY0EREOGyg9uE0lQh8hXXSegWuHXGHbBzLaQrwnhupWJUlX5vPYwww8UZw-0A1cUHuocClvUaeCMacY3-vK_ON9ySY0iZ49I11SmYw-NUk-C_b3h4HN6xSB94-FsKbKgKH36jxarO0BMWus53Nub0PSlGfQhU4MItEptAUQziWeEL2Gr0cENvCCT63y1HzQP7em180bpO8XqUqhAu8ZZQdgNi0JB9iPGmp9MnOD3uaH4z54_shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkPYiLaYloNh6ZKxBnSoRPSqGGY51g4_dvMvrQ3NVplqBB2LfoCJyikoZ-jy5ISlJXNdP92hnKjw-ZsdciqrBE-NpuDjbgT8qXJrhotiAghOQGEb5nD_LPltwc9REmbzbqhWWmoZmxJmjwoRHr52Jp9Zan5aYk5xTXHkk7G0yXaUb520nMZZ3M89eRXEpNs4xy7jvFWqtkO9TTgfJHEno4bi8eVOWMcEWsX29ziNCv29MioXgmahNyaaTIWu3yD4xtKdC6xU2hMIIpnmv0AnkJ-mIOO2QSmSfFRhpRdJKq15U3fd4_2DG3T3iKrHIcHJp__XCTt4Wg0kOH5P_uEpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4wZWabK19mueaqkwE3aH51cMdcVsgAF5ueY9-7iH5xPLVK4PWM-rtBaWoaeI4TqIGvspQvK7jNEk8rNy61xNGsdgcqC7Zn5G7MPX97xbA7EaZeCZ7EEqA-McGuoguOJsRoJ2PCFCh-ShzGXq74_Re934sAXDq7U4PI1EtVrNdiJtSaQ0f7fTTG7ubOQRTt2DVh1Rw6igDSpaD6WPA88GXFI2QYctPhHNkUpFiUCmahVOERiBSyD7O-avHLb7-4lvqPd58HrJ0bN6FxJj8mfXFwiE0q_1ASOzpfOTEJfKePU7jzGBw-VDKj3s8zx0fxytpm3wHmvSldPSGGjas0ECA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
دغدغه‌ ی خانواده‌ها در آستانه بازگشایی مدارس
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/689472" target="_blank">📅 13:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e80b888.mp4?token=MNUscqhWXng4_Tc7Ch7lx3BVkn8VVTRpIZrXSAcZlI8ULpEMqO1rhN-v8yhYi41pW7zmmibqO10o_x6vOCTAy4ZUGIDsbdyAHDZBLr-HjVjneERKpAsUzG9R61OlG0pXwflXXdFG2cBcHcgUz7JxOWl8jqJkVrX4uc9CDJhqO84ZXkkTaIbDxzgKLy0pzK9Dxw4kHjCglCLGSqQPRm5hDd3aZRdkx1sbCsIyWf_3Mse93uJDdfQqJ6uMv8YooaxYACFqAUZ3y07d_PqV3ONCgCTDI8BjBGX1232LpXOAg_Dvkk2XvryPIXEUdMr6tFFjviFZPIRqzDVGQRbrLs60hUuutWW0Mq5W9AkQL2C5jygBCB8YD7SwfCo4YGzO6-AhLuii7kfD5Eu0YMfl_ZvT1j3NMbjLOwTX-e76qR27kbkcFnAfnISMi9qIuh4_GxH-QZdPxIFd6WAAEjnOyRNcJVpRkFXD4BJNWc6v_ut5HOnCPtZb3e_GW_AzTRmgMTHhIkyBD32V0aZSDTJTRATNtHOCTGrIw6S9CNIsMpJwVcHjOijZB9xSXky2YT6PmK5aMQymYcfUFVUUXAAYWp42YhVfTuhRoXOiJDVjRk3U3dxnEDyuZM5RJYUK3CfCAtq7mkjk_cdeIsi7KjyFvrXbM91qJY2PX6pgi82bTNXY_es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e80b888.mp4?token=MNUscqhWXng4_Tc7Ch7lx3BVkn8VVTRpIZrXSAcZlI8ULpEMqO1rhN-v8yhYi41pW7zmmibqO10o_x6vOCTAy4ZUGIDsbdyAHDZBLr-HjVjneERKpAsUzG9R61OlG0pXwflXXdFG2cBcHcgUz7JxOWl8jqJkVrX4uc9CDJhqO84ZXkkTaIbDxzgKLy0pzK9Dxw4kHjCglCLGSqQPRm5hDd3aZRdkx1sbCsIyWf_3Mse93uJDdfQqJ6uMv8YooaxYACFqAUZ3y07d_PqV3ONCgCTDI8BjBGX1232LpXOAg_Dvkk2XvryPIXEUdMr6tFFjviFZPIRqzDVGQRbrLs60hUuutWW0Mq5W9AkQL2C5jygBCB8YD7SwfCo4YGzO6-AhLuii7kfD5Eu0YMfl_ZvT1j3NMbjLOwTX-e76qR27kbkcFnAfnISMi9qIuh4_GxH-QZdPxIFd6WAAEjnOyRNcJVpRkFXD4BJNWc6v_ut5HOnCPtZb3e_GW_AzTRmgMTHhIkyBD32V0aZSDTJTRATNtHOCTGrIw6S9CNIsMpJwVcHjOijZB9xSXky2YT6PmK5aMQymYcfUFVUUXAAYWp42YhVfTuhRoXOiJDVjRk3U3dxnEDyuZM5RJYUK3CfCAtq7mkjk_cdeIsi7KjyFvrXbM91qJY2PX6pgi82bTNXY_es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا فیلمی از حمله به یک شناور غیرنظامی در تنگه هرمز منتشر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/689470" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
نمایی زیبا از منطقه چشم‌چیت، دورود
😍
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689469" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
معدن با شعار زنده نمی‌ماند/ کمبود مواد ناریه و سوخت، نفس معادن را به شماره انداخته است
دکتر سید حجت زینلی، عضو انجمن مس ایران:
🔹
امروز بسیاری از معادن کشور، نه به دلیل نبود ذخیره و ظرفیت، بلکه به دلیل کمبودهای اولیه و موانع اجرایی، برای ادامه فعالیت خود می‌جنگند.
🔹
کمبود مواد ناریه و سوخت، نفس معادن را به شماره انداخته است. صدای معدن را باید پیش از آنکه خاموش شود، شنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689468" target="_blank">📅 13:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSHUrM100fytq4Pdi4Lb91pm44_cs2ICBfMKSHhwgbliF7uAxnzHDSHiwm8zNHeBhCmoTDLLoJxvNz6gUbDEgnslzD1VVmct0UMGoK5yRhdwB5aQC21kIXsvs1coAc-efRoL9eWU3WojYCJDjGeZAx0hI25YFmARhR1jo9OysE2XRStjbnGfiIK8_1bJ2qN18lXuOvheQxGwc4iXD6SaB3iY3mHgcr7He3QTK28_13YZKtpv0MkJy0upyX3zaFQaEV33WW0fNBfxLfMboWYHIy_8_8Xn1a3h6GdFHrJjSFb42fbBPWCB8LpV9w2EYabIwiP0ISGU_hn3LmTccn9VEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5fOiD31GWcHSB6PMlJgvenUMbG1gv3lCToeYUxmI1t_ncW4GPDjjTLcDuoK0KG41CAgiPmTD5x0jtFJ1eub-sJ1xcFdb0TEcI80gkP4BIr29YE-Zh9Kq80QFm-vhP7gxqozEcvkX2vthhDA9E8PGmI84LEK-fHoPKMYX5OOUawwsD-eZr7L8dKRNCRMyL9TI0__H-oMEr_c8VxfumSODCR8wB0oZG9A2bWK0YdxxPKm3MF6Z_eR9DNbpFjJhDKiYtr5LI2Cu7bpOMP6UETvBBWzPYBJxNGN1QR7Yc0NkGm41wb-YDOyDCjTtpvkztjoy-YRt4vFjmDKNS-UbuzsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RcVqNTenRLPh2ZdeyZ0BEPh1zhuIrnOKW1Md2tUFCtoaskHOSPDKy_omO5whYNSjjFTVFPiprvH85Bmfh2DLFP56P7pZGPVOuSe1cQUxgiqkXeSNf-gd4Uq7-rahmZz2W4u_8Zics2inyfPz1l694nlZr6xvKQP0KKsHCowx6NnsHb3efy0cpnmMnBCn7VY55MGL4i5INi745BtpejgAyRdFubGpnhimaY7OsXT734x-fbRCXreJrvdmmeKWp0bm1ob_gv9DeB-ChXP_b35cKKKH7PI88e_kaaCT29GcjslECP4rIHPI03Bhckr2GWzLOOo8a0X5l4lGTyk6SwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxf5aq_1v3EkI22b867FJU0Bm9DbO4WvwdiPosvkMrGSq81h_TapMkKcnx_e_xfzQU87SZ3Gs8l37tU8GVuomw7vUjE6vxMPvjEYDbP8GTYkR9UPi9_9sESkA8QLX4N3hlU8Ln7HQOsXvmovmgJZN5TrkodiLzP-HUFcUrORr0Fc5JAHXZmRuJY9eS20eI8SnIB5z36AaRzM-m5IV8rksKXm9BcO92Ltyn7HVrUySj3LuGxnq0-3mPqqhTLOoJxY5IJinqTBdYDbEPyzHWlA9RMQjXsjuKKiSsHqn0qLb2CLZHqOeGtTL_t8Hse9fLpCyLV3eJOIUZrI33AUMVyN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VozqLMbMQ5PpY25WRinKaijujRJDpyCSU3IWR8RcgeoK_J3M3fOdsgU6KLbnxQ9mCr24CZY2HTn8PkVsuJ8A-R6COxImbR8qoJKFbcZ9L-sQOA-zLslS0CkCXdF96EcPorLppioatqaSw-c1XNYo14GhmBzsBw383Sw9auVNGOwp47ovRsJ51izE7Ref_Llz1M8uINA8YaYrV3j4Y86n6dNaNDMJzHxPfhkZkh0TnYFn0wyST0C_HWWZfxWLPDSrnCvF9iHIPeaFjaVNXAGVBferthXGG7AGuEuvS5XBMvxNzfITDl7rqXg5Pcv2jFabhzdNFur8D53fBjppf9Wi4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDnB3WLNmf0a-CBFI8VT5UeSCl1hV8VGEwkMmTuUS0vQ6F1hpxwL40HcHtkecTmGJY3g77i52qaABGIa4v5kOo6VyW4SkVrRTpBssk_vf5VivFgE1CDln2B0ZltoZb4fdM02civs_YUneh3qYoZkAtbWEcMMiOlV565o3tYpYbqiqwZUsb8fgagjHnOqw24Y7OsYhw3BRsqXVkM1KalN8TFI65bJRt0CRYYeMORsz8wufy7X6ipaHDwmkiX9eoolBRK-iJkCg8OELHmtQzVhO6KcMNxgkfoMoCT-GQKXdBJN5urEEHUKfmaD-hP9kD2jecgeOzvREgJv-CuhCvYVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPGT45y917yZsHaQYNx9ikDsAcHor_4SSY8xxEbQIGRi9Q7kQK0nvd4EnXGfb5RWsGzKOo3hitdRsnxdu2IbBCsrbgw03cWBUCbusxMIOxDyXvWPMFp_0h7NygS0iOfGZHCsakNRz_p-JhIT6CAnWRAh_q1F6futIh9zYwmcrnlwxtS4fvTkwrwspXc_SMxoUet2Ft5faSjIaJrWPBk7FvrqOzgI2DQ9l0voeDnk3cuBXjYpihYfjb2dxZNvl8xJKU7Px2WF4Dgsg0wdRXGFXzHlpcTS6MIja61G-72WW21nL0aAav40ahKFWQZ2Dv5rQ6tVGX0EAQqbT1yRE3-KrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار؛ chatgpt نباید این اطلاعات را درباره شما بداند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689461" target="_blank">📅 13:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689459">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9f44dd96.mp4?token=Q6jb7atCk69CJYdM711i1WCVpb6WApD_1YlRlSJ1Sh5ILxEitKEJ8dvsquJF3fjACLMnVSx0935hBcEDuehYyLfLlfKHybbMYXZmMa2JC8pGArVBIAZefVStZ4cztARoaDAfN9nApVORMPamWGL6Z3RaT22pN7c3zLBY9nJbCnvCYKGl05uwdyAMLpsMyRuzuyIMTiWzOxHuJZKNhqanx1mviv5UTrNqPg1fmVfBtgl2vZY2xNVTr7t_2OVyEkGyCy5gyAhF-MuSO15_lpIMRphZG1HOAq8yjoLmaRFiXQwayADHR9HUM7TTyVyTiDShMuR46NDM-1b1vs91zUy9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9f44dd96.mp4?token=Q6jb7atCk69CJYdM711i1WCVpb6WApD_1YlRlSJ1Sh5ILxEitKEJ8dvsquJF3fjACLMnVSx0935hBcEDuehYyLfLlfKHybbMYXZmMa2JC8pGArVBIAZefVStZ4cztARoaDAfN9nApVORMPamWGL6Z3RaT22pN7c3zLBY9nJbCnvCYKGl05uwdyAMLpsMyRuzuyIMTiWzOxHuJZKNhqanx1mviv5UTrNqPg1fmVfBtgl2vZY2xNVTr7t_2OVyEkGyCy5gyAhF-MuSO15_lpIMRphZG1HOAq8yjoLmaRFiXQwayADHR9HUM7TTyVyTiDShMuR46NDM-1b1vs91zUy9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کم‌خونی داری، این خوراکی‌ها رو بشناس
🩸
🔹
این خوراکی‌ها می‌توانند به تأمین آهن و مقابله با کم‌خونی کمک کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/689459" target="_blank">📅 13:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689458">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عراقچی: توافق با سلطنت عمان به هیچ وجه به معنای بازگشایی تنگه هرمز نیست
عراقچی در مصاحبه با العربی الجدید:
🔹
دستورکار نشست فردای عمان، مسیر دریایی جدید در تنگه هرمز است. جزئیات توافق با عمان و نقشه‌های مرتبط با مسیر جدید را در اختیار کشورهای شرکت‌کننده قرار خواهیم داد.
🔹
شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
ایران معتقد است مسئولیت تأمین امنیت و ثبات منطقه صرفاً بر عهده کشورهای منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/689458" target="_blank">📅 13:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt5pLsuhiAiXBzTWPp1AQi4WysA7ciDsypcXF80dbP86UpCycX-BIWgaBHscKxeEGOprWX-pXsOw5xP73ndmZudQjR7sE-NCLe5CXAHXg8LrFd-JQEujVtsqT9dWHEYEe-NEK3yWpsGtW_aLYTUS57g5hCDG2z7QKNU-YfsZ_OopepT-I-6Or8u-XqZRTq2rmIbQhh3UQa-2Ygc4L508I1xjxMpT8AM3ML_tXw5L7-eAcBr6YOkIb2CW2OiGx1PKhu59kcWKwR9o_fr38F3skbwuBpb4OUNcBWi0nqb46UtG1xuyjIM1V8qJqaAbqx93JbXwtYq5QG0YY4ND0Y7auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دهک دهم ۹ برابر دهک اول بنزین مصرف می‌کند!
🔹
دهک دهم به‌ تنهایی تقریباً به اندازه مجموع دهک‌های اول تا چهارم برای بنزین هزینه می‌کند!
🔹
بررسی هزینه‌کرد خانوارها نشان می‌دهد هرچه دهک درآمدی بالاتر می‌رود، سهم هزینه بنزین هم بیشتر می‌شود. نکته قابل‌ تأمل اینکه هزینه بنزین در دهک دهم ۹.۳ برابر دهک اول است. طبق تحقیق سازمان برنامه و بودجه، حتی دهک دوم نیز حدود ۲.۵ برابر دهک اول برای بنزین هزینه می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/689457" target="_blank">📅 13:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35529d784e.mp4?token=F7re0WF50FwRPyonsFKlrdo8oOBkQ8acvtCCOm_O81dpRrVmBOp1Zkd4IUH_8Jay4_43-uLpU1lZpjL1GnprxmBlYrBH7SFfATYdPMniiPA6tmuev6UEholzW9deJEEl-MUO5B0LX54gTejmiM_spHlESarjj6bS_t9yXnb9Ilx7-iLa7MsUKvhKnwc1V0A9jKo44kfy1Tf5SN8i-65iwl53yP6tXTiIs2lM03stzFN5yvrW-bpe_9y432IJHUX99H6viyOMWrMo2WRJs5suEJXHcCIz6NwNE4gkQyjiXggauiOmPYZLKyCRk9zmeQw1NK8TJ4No-67xuqxpKiS8hAuDM1qTISz8oJNQDEV_B7bI0t-6d1Ab6hk3COHZKzZ0QDI-Dfr_dsG0-ftVN23dthgiMfZU8M7AleRIhHrEzoDVZqlZvX8M03kipJmLIV8boQ8jPW5sE3Wk6S1wW9kBrvuLbPe8N97oXBlm3ejAHFIE-BuSN4p5Or9MHtSgoQ6bwfOp86TSmGN2KPNQPIDcaK89H1cuOLdnqliJ8-n8OrJveYSbO-xr01-uWj2j-UDcmEevXBdw76sG8KQt0us_aQBgr2jT5W8QgL7OAMBDtcnwfnP11OrcKRUoeilYTYjo8oeSO03ZY1_qI9BE91hsAJk08xrPUAhxu-UxBg_W4M8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35529d784e.mp4?token=F7re0WF50FwRPyonsFKlrdo8oOBkQ8acvtCCOm_O81dpRrVmBOp1Zkd4IUH_8Jay4_43-uLpU1lZpjL1GnprxmBlYrBH7SFfATYdPMniiPA6tmuev6UEholzW9deJEEl-MUO5B0LX54gTejmiM_spHlESarjj6bS_t9yXnb9Ilx7-iLa7MsUKvhKnwc1V0A9jKo44kfy1Tf5SN8i-65iwl53yP6tXTiIs2lM03stzFN5yvrW-bpe_9y432IJHUX99H6viyOMWrMo2WRJs5suEJXHcCIz6NwNE4gkQyjiXggauiOmPYZLKyCRk9zmeQw1NK8TJ4No-67xuqxpKiS8hAuDM1qTISz8oJNQDEV_B7bI0t-6d1Ab6hk3COHZKzZ0QDI-Dfr_dsG0-ftVN23dthgiMfZU8M7AleRIhHrEzoDVZqlZvX8M03kipJmLIV8boQ8jPW5sE3Wk6S1wW9kBrvuLbPe8N97oXBlm3ejAHFIE-BuSN4p5Or9MHtSgoQ6bwfOp86TSmGN2KPNQPIDcaK89H1cuOLdnqliJ8-n8OrJveYSbO-xr01-uWj2j-UDcmEevXBdw76sG8KQt0us_aQBgr2jT5W8QgL7OAMBDtcnwfnP11OrcKRUoeilYTYjo8oeSO03ZY1_qI9BE91hsAJk08xrPUAhxu-UxBg_W4M8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از محل مراسم عروسی در روستای کوهستک استان هرمزگان پس از حمله آمریکا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/689456" target="_blank">📅 13:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9SERKtb0jIOBxINEPUs5c48_PxZF0yey424RZYa8DiQtF_XJI0mlB2BhSsDqKdDvMRQ4PbiTflXMwN1ItUC-K5dmI7k5sIFIajlGZRz8vzgBHT5TwFvh3NkACMwySV1PuVGVSQ0_-MByfPoNG8brsgyKaH_08zQ6nrRuMoQUX60fn8U-adAeuytFsVk9Bql_tlNuhuK-6eWgkUhjkDPr2K6zN9ym-g5eXNeLuGsd57zxjtbg8G_OON8gQq7hvl1Tp9n6-t0oPhYz0-h3PEL4mPifnV85BRjjO5Hk9p6EcfBRXSzFKD1Bwta5Fwl7ITYgYGY44qm3IQi-MhakSJBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ۳۰ میلیون تومان اعتبار خرید دیجی‌کالا برای کاربران بلوجونیور
🔹
هر سال شهریور، تکاپوی شروع مدرسه را با خود به همراه می‌آورد؛ از خرید لوازم مدرسه‌ و آماده شدن برای شروع یک سال تحصیلی جدید گرفته تا جنب‌وجوشی که می‌شود آن را در کوچه‌ها و خیابان‌های شهر دید.
🔹
امسال، برای اولین‌بار، بلوجونیور با کمپین «همه چیز برای مدرسه» با خانواده‌ها در آستانه شروع سال تحصیلی همراه می‌شود.
🔹
در این کمپین، با ایجاد «قلک مدرسه» در اپلیکیشن بلوجونیور، پدر یا مادر می‌تواند تا سقف ۳۰ میلیون تومان «اعتبار مدرسه» برای خرید از دیجی‌کالا دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/689455" target="_blank">📅 13:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
اعتراف یک سلطنت‌طلب از افزایش شدید هزینه‌ها در آمریکا؛ شهرام همایون: قیمت بنزین به‌شدت افزایش یافته و مردم آمریکا برخلاف ایرانی‌ها در برابر فشارهای اقتصادی مقاومت کمتری دارند و زودتر دچار مشکل می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689453" target="_blank">📅 13:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689452">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
آتش‌سوزی در یک کشتی در تنگه هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس در به‌روزرسانی اطلاعات خود از وقوع آتش‌سوزی در شناوری که در تنگه هرمز هدف قرار گرفته بود، خبر داد.
🔹
سازمان عملیات تجارت دریایی انگلیس اعلام کرد کشتی‌ای که پیش‌تر هنگام عبور از تنگه هرمز هدف قرار گرفته بود، دچار آتش‌سوزی شده و نیروهای محلی در حال تخلیه خدمه آن هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/689452" target="_blank">📅 13:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6HmUbXJmegtAxnZ6aAuPNFy46M38kT_yAfqLWyupjFclpr8Lopp-NohnVDoV6jLU0kYq3HSx-m-7kLI7aCb85uqoDGWAlhsYzaFt_T9kQ1OB0y2vMJITOqFQN9wWhu2JU3i4BCJLO_ErsEY3Ryv0ddyhQwjjusbelflTr5MoATcc7AkHdA_21OXGGqGU91-EEum2LSpaguZPP0dMfD3I8JYoRf4Fjv4dAg1-bJVa8CJJPaNnmkJh_eh6esdAwx_2gBSF_LT9xv24SUiu-QsK-sQ0RwHSNvc5C27JFh-Ai73h0QLuZADpDiFiTelTXWoSWoQ5rI0e2a2tdT7gmEfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۲ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
دلار آزاد در معاملات امروز با افت چشمگیر نسبت به دیروز، تا سطح ۲۳۱ هزار تومان عقب‌نشینی کرد.
🔹
اسکناس آمریکایی که روز گذشته روی رقم ۲۳۵ هزار تومان بسته شده بود، امروز تحت تأثیر سیگنال‌های مثبت سیاسی و اخبار مربوط به نشست روز دوشنبه ایران و عمان، وارد مدار نزولی شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/689451" target="_blank">📅 13:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQp1R8qvzn___oo92L6rtPPlcThCpfgvjOyOYxao15Kv39fIVG3j_OEgfl-tMZ7PxIXMjXiG6SP1N2tpWhfAOFTArjb4RF8taH-3FYhCPmD0tnDNZuXJM0uBGFj_9OKdQGV5Ndh49K37oMt1alLwjc_Cl2_bS8t4MbKSD5zbauuz5wqx7f01WqbOcsGr5cPjE-jZ3bdCJ_XAEZxgYh5jOozc_2xhFJUPGTOSP-PYSPE0OOutwRdTJ0TM_HJjyTs207Sx9yN_RN6lFPsCLl0Z8xu-tjlQPBtXuiGSLuZ8dgQg9V6MF7gEzHpAT1iLMkzXwkr2dko-G-BOk_tDCnaCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: پس از ماه‌ها ناکامی در هرمز، رهبری پنتاگون در مقطعی به ارسال ایمیل دسته‌جمعی برای کارکنان متوسل شد تا برایش «ایده رفع بن‌بست» بفرستند!
🔹
آمریکا زمان و شکل جنگ را انتخاب کرد، اما این ایران است که دست بالا را در تعیین زمان و شرایط پایان جنگ دارد و هرمز همچنان تحت کنترل تهران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/689450" target="_blank">📅 12:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e29d26864.mp4?token=qW2KincSq_kRSPS9jDqYOHFOmS7pYwoT995ESXaCW2vDUjl1CYPdvjfWQVAKVaX25HI7wBbFVLtn4RnZJS2I_nPNrQmSv4IQ_Wm_MGYjphfUud7Z0fhDj9kiXGWkcsIQ0dZXgcRcxmFV2K5H-Y1FPFLQTLZMMdWw48A6dnBhPVDSVWlr1TN-P-OtX6F_GdMsWJDdvxc-fp0YLCRqGzIIF1Gfn7r4uwR78WQlRl9nH5MwwpeNF1hFRrbkMj7zDj2iVDEa7u6exg4O4jmuu4lgeDg0iLV4_z_sp_rDAOI3AhKjbvMFpTC4FFfRSmYAciD-ClFmfuh2ZAVpZGRz7uSfGUI8-XXAhu1WisigJBUl6MNOxZMmcNUvMSIQqh5YvV4QUudzi3zNgxV7t4c0d-PsK-yXGAlHKpv_uhcfDuvJKuQEegTFSt1xz2OdOGolJ-X57n75A7Q23KyEhas3V8Rm9E5sfTHefWAZtl5i157dXY3yDoNLMr4XytCxdgu_BFOEQBC1NlBGGH3AjcSObVY2-NUbuN6JbP51wRzNo_YJsQX9VFeVKqnbdKCCnAYcFyBsJAG65ggrxry_7ARfba3QwTpp7s9yYjr5kUhwZpmZDAAf3oHwwmYA5DQzV1Wm7AkByd4gUvU5LWNzdHPaLJt2heAOSmQOnz10lw1ZbC3p9lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e29d26864.mp4?token=qW2KincSq_kRSPS9jDqYOHFOmS7pYwoT995ESXaCW2vDUjl1CYPdvjfWQVAKVaX25HI7wBbFVLtn4RnZJS2I_nPNrQmSv4IQ_Wm_MGYjphfUud7Z0fhDj9kiXGWkcsIQ0dZXgcRcxmFV2K5H-Y1FPFLQTLZMMdWw48A6dnBhPVDSVWlr1TN-P-OtX6F_GdMsWJDdvxc-fp0YLCRqGzIIF1Gfn7r4uwR78WQlRl9nH5MwwpeNF1hFRrbkMj7zDj2iVDEa7u6exg4O4jmuu4lgeDg0iLV4_z_sp_rDAOI3AhKjbvMFpTC4FFfRSmYAciD-ClFmfuh2ZAVpZGRz7uSfGUI8-XXAhu1WisigJBUl6MNOxZMmcNUvMSIQqh5YvV4QUudzi3zNgxV7t4c0d-PsK-yXGAlHKpv_uhcfDuvJKuQEegTFSt1xz2OdOGolJ-X57n75A7Q23KyEhas3V8Rm9E5sfTHefWAZtl5i157dXY3yDoNLMr4XytCxdgu_BFOEQBC1NlBGGH3AjcSObVY2-NUbuN6JbP51wRzNo_YJsQX9VFeVKqnbdKCCnAYcFyBsJAG65ggrxry_7ARfba3QwTpp7s9yYjr5kUhwZpmZDAAf3oHwwmYA5DQzV1Wm7AkByd4gUvU5LWNzdHPaLJt2heAOSmQOnz10lw1ZbC3p9lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین را با عینک ایرانی تحلیل نکنید!
عسگر سرمست، مدیر اندیشکده اقتصاد دانش‌بنیان:
🔹
اینکه چین از تضعیف رقیب خود، آمریکا، در نتیجه جنگ با ایران منتفع شود، درست است ولی مشکل اینجاست که ما رفتار چین را از زاویه منافع خودمان تحلیل می‌کنیم./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689449" target="_blank">📅 12:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=TCw7mIY20sIkcoH1j15XyfztZHc6JZ-FvELSbKqelGWQbqrLSkdnG4e8KByKnIs0FaO9DsXA_P2U27KzAeJol0F059FbC4M346tOaI2PP7NPg0AVGHiMSljAmiaEErAHLmAK0HZSi46KEEFPplNsY9cmBMK4Aki7Gnjct7m-RBkOG1auOSncEqg-W9KAGI7YgYnRAuxv-cHAqKIBO5YWittvHzZ6fwg1n6ye9dXPuQe3asngC_T9-j6f1wgFSyomnz0BkDKNfXy50JLVprPVaYUM4WbAYJ8ttHbala9xfE2HqhIiMkJQLpYv0E6irEIWdhDtl70AjLiua6MWa0_-3E3ufQiWforh56YEs93aWSvI8GCLHcKW8kUqNEl4VwM4pxziQv1wrkcbBw0OA-UBW0kqKM_htCEuiAHcF0Lwuv7dhRAXbtWGi70PVbNCEV6a_7lsPCVkNTqx8OGivduMjVlfo-gBAjU-ZoSlVmi6urj4yKlmuvKAXEVb0Ow-l0pJ3m_iQPS9DnpV0C3nSnmRk-oWlPOJ-HI_aKiyiGepoPRb5fTQPOEMualf1T8KZH-IFrvw9cVumzCtIZzN-KOTiB1W-IPdG9PI5vgbprn3U6dGC_HMqV6raj84ksXS9MPipoXDQJjtmjx6Od4hoSeir9XO_8BpTXdxDORurDX_Fk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=TCw7mIY20sIkcoH1j15XyfztZHc6JZ-FvELSbKqelGWQbqrLSkdnG4e8KByKnIs0FaO9DsXA_P2U27KzAeJol0F059FbC4M346tOaI2PP7NPg0AVGHiMSljAmiaEErAHLmAK0HZSi46KEEFPplNsY9cmBMK4Aki7Gnjct7m-RBkOG1auOSncEqg-W9KAGI7YgYnRAuxv-cHAqKIBO5YWittvHzZ6fwg1n6ye9dXPuQe3asngC_T9-j6f1wgFSyomnz0BkDKNfXy50JLVprPVaYUM4WbAYJ8ttHbala9xfE2HqhIiMkJQLpYv0E6irEIWdhDtl70AjLiua6MWa0_-3E3ufQiWforh56YEs93aWSvI8GCLHcKW8kUqNEl4VwM4pxziQv1wrkcbBw0OA-UBW0kqKM_htCEuiAHcF0Lwuv7dhRAXbtWGi70PVbNCEV6a_7lsPCVkNTqx8OGivduMjVlfo-gBAjU-ZoSlVmi6urj4yKlmuvKAXEVb0Ow-l0pJ3m_iQPS9DnpV0C3nSnmRk-oWlPOJ-HI_aKiyiGepoPRb5fTQPOEMualf1T8KZH-IFrvw9cVumzCtIZzN-KOTiB1W-IPdG9PI5vgbprn3U6dGC_HMqV6raj84ksXS9MPipoXDQJjtmjx6Od4hoSeir9XO_8BpTXdxDORurDX_Fk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد افزایش تولید هلدینگ خلیج‌فارس در سال وقوع دو جنگ تحمیلی
🔹
شرکت صنایع پتروشیمی خلیج فارس در سال وقوع ۲ جنگ تحمیلی توانست با وجود ۲ ماه توقف تولید به علت شرایط جنگی، تولید محصولات خود را نسبت به سال ۱۴۰۳ افزایش دهد و به ۲۷ میلیون و ۳۰۰ هزار تن برساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/689448" target="_blank">📅 12:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395aa9a9e9.mp4?token=RqxBgY2CL0LudsrWp1v1kdDKlqnU2FkqKTtlX56wGw_B-B7xNOHVz492pfl7qIeJc8STp_WhLj626-J-Ea11u_0ntsrWQBTpjiNB9edjBB9lPyzyk6otgHxsBc8HugW-cvrq6cqyP3fKrjFobm6rN7Py8xeJQaqPgqjq2VJzROj0ypqEc3FYa2YNI59Zf_a7d33vadrgiV2PIWqk_JpqMCM5miIAdf-Z0Xiyj272z7s55Lj-T4ykGGeCKXw-7geVNS5HcyujFeg5jsE7zQaX0Dwg5HKyQErSewtLWXihOQJ1jd5DlSOYA45PMQpFuHEMRfnD90bzAil7L8QQ5NbbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395aa9a9e9.mp4?token=RqxBgY2CL0LudsrWp1v1kdDKlqnU2FkqKTtlX56wGw_B-B7xNOHVz492pfl7qIeJc8STp_WhLj626-J-Ea11u_0ntsrWQBTpjiNB9edjBB9lPyzyk6otgHxsBc8HugW-cvrq6cqyP3fKrjFobm6rN7Py8xeJQaqPgqjq2VJzROj0ypqEc3FYa2YNI59Zf_a7d33vadrgiV2PIWqk_JpqMCM5miIAdf-Z0Xiyj272z7s55Lj-T4ykGGeCKXw-7geVNS5HcyujFeg5jsE7zQaX0Dwg5HKyQErSewtLWXihOQJ1jd5DlSOYA45PMQpFuHEMRfnD90bzAil7L8QQ5NbbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌صحنه شگفت‌انگیز CT اسکن
🔹
چرخش یک دستگاه یک‌ تنی دور بدن برای ثبت تصاویری از داخل بدن!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/689447" target="_blank">📅 12:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مهمان‌های عروسی، از ۵۰۰ نفر به ۵۰ نفر رسیدند
بیژن عبداللهی‌‌مقدم، رئیس اتحادیه تالارهای پذیرایی و تجهیز مجالس تهران در
#گفتگو
با خبرفوری:
🔹
در حال حاضر بیشتر مراسم‌ها با حدود ۵۰ تا ۱۰۰ مهمان و نهایتا ۱۵۰ مهمان برگزار می‌شوند. در سال‌های گذشته، مناسبت‌های خاص از یک سال قبل رزرو می‌شدند و حتی تالارها، کمتر از ۵۰۰ مهمان را پذیرش نمی‌کردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/689446" target="_blank">📅 12:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e7e6d7b5.mp4?token=cedzF_uOnPDJUiRSz7VQ6NuAkmTjiy2d5VzK8bj3Dj3Ip_owkkWsMrwhYNWNnTbXHb5gL2zOStq9GRjjacpvmH73KnROcpOQbjZvGs4q0ljC05M4odlJsQYjSNiMIsCQuejwFrc8fcXEhKkitqaqbWR5duYxYQYjTvoPjnFkordYmumL1qRhzpd5YcWslSn25MQt026Ch6QzirHu_8N6PUH8KD6tKjghOkYXnkpuw5-gIAeSPQDuLWU03nhfhmFFwwC95xsV0C6ovH5DSnUOfjXtyw16jlYRI_d15srJ2XVxdIXbeIRUAfE1AFas9fxPiVLXJ2WvWELQ5aVACD3OfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e7e6d7b5.mp4?token=cedzF_uOnPDJUiRSz7VQ6NuAkmTjiy2d5VzK8bj3Dj3Ip_owkkWsMrwhYNWNnTbXHb5gL2zOStq9GRjjacpvmH73KnROcpOQbjZvGs4q0ljC05M4odlJsQYjSNiMIsCQuejwFrc8fcXEhKkitqaqbWR5duYxYQYjTvoPjnFkordYmumL1qRhzpd5YcWslSn25MQt026Ch6QzirHu_8N6PUH8KD6tKjghOkYXnkpuw5-gIAeSPQDuLWU03nhfhmFFwwC95xsV0C6ovH5DSnUOfjXtyw16jlYRI_d15srJ2XVxdIXbeIRUAfE1AFas9fxPiVLXJ2WvWELQ5aVACD3OfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاغذ از دست پزشکیان می‌افته؛ خم میشه که برداره؛ حالا هندی‌ها پخش کردن که پزشکیان پای راهب رو می‌خواست ببوسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/689445" target="_blank">📅 12:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
بورس به یک‌قدمی ۷.۵ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۳ هزار واحدی به ۷ میلیون ۴۳۱ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/689444" target="_blank">📅 12:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: ترامپ به ولیعهد عربستان سعودی، بن سلمان گفت مسئله شما با ایران به ما ربطی نداره و خودتان باید مشکل را حل کنید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689443" target="_blank">📅 12:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=mTqC4w3vjMjebu-ohsD5U9VyiEkx_Vl30myAyGuZRSeIsqH7qsBnZAHGuMLqgRZg0fWyv7HRhwvjcloV0bTuVMiyviLfxtJF_kdB-HngnNPZsAys_ydfefBxVfX6fkqMJImHbOO8AYRVCeIm4CtOdhrlwPElyf5UY2xYVbBkCkx-K5QXGnLRmNkdq6mTPHQS5mZEaz_fq-Ueaef4kcr9fgK-X6_ys5Km5yCv3b6XAsTRwycmk0uvdzDyg5lNw61gDiW1F1-t78-rZfh-zOFOeF2Ca0cbX6qpyXNn-eISrXj5KSVL4DSW6fhifxfJ95u_OjGS2-Q1hAul_JEcUkMvqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=mTqC4w3vjMjebu-ohsD5U9VyiEkx_Vl30myAyGuZRSeIsqH7qsBnZAHGuMLqgRZg0fWyv7HRhwvjcloV0bTuVMiyviLfxtJF_kdB-HngnNPZsAys_ydfefBxVfX6fkqMJImHbOO8AYRVCeIm4CtOdhrlwPElyf5UY2xYVbBkCkx-K5QXGnLRmNkdq6mTPHQS5mZEaz_fq-Ueaef4kcr9fgK-X6_ys5Km5yCv3b6XAsTRwycmk0uvdzDyg5lNw61gDiW1F1-t78-rZfh-zOFOeF2Ca0cbX6qpyXNn-eISrXj5KSVL4DSW6fhifxfJ95u_OjGS2-Q1hAul_JEcUkMvqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ رئیس کمیسیون امنیت ملی به حسن روحانی: تقاضای برخورد با ایشان را به دستگاه قضایی ارسال کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/689442" target="_blank">📅 12:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrhwcfJegviJmUQSiSpvld9VU4A2tjxRtJOgoL01LCWTEy_e_GK7xL9JMjZJEVWtXnW8OdJ5JfXLx7Vc5vMyOjNha0gapwIF6RHs7bYtfb5VxdUpJktl9HHLNwIM6AsFSBJTCCYfipSJJpkJKu474r-zOMML_98Mp3v1DaSMS0GDhYBd3SQFZEyZsaiGSf6mySYiuBU6WMYLF1IcX2eN7l8PLAarGbJGQQB-VDmcyzHt78bqfUYMBzuTGInAgcgvKiQvK4M-satNafO7UWg_IFExa40bPs_112QbRhLq9befrIq58xfe4-orzuMGk03gHtc7t-x4IxkBzsOqfeX-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۲۴ درصدی قیمت بنزین و ۳۳ درصدی گازوئیل طی یک روز در اتحادیه اروپا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689441" target="_blank">📅 12:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689440">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a008082ce2.mp4?token=K52VFPFn67jQ0_z7bbRWOU0VjJsFcB7FWx1cBZB3Fpdwa_GDuJ6pgZIogIsXCo1SlseqySvtzed0W_pcESsvXSiaCib5ZuxadYh2m_ExRtg4G0LYcrC1iQCIuZOx-XCX8JXSrR6-XvkM4M-Ckn-8kbPjC6Q8uiZs-M3fxvZechY2XvwVgWyvz21c3qlfgNOPiFF2B1CEnErxyhkcnsMG-EaNTwhIhQqF81Wt8ClYD2TrfUDP-lMKlMtLE-1_lPEHFjbUpQaGQWyycAu2PhtXec1mIa0Y3VphnUwLXL4qWMRlscjqp4AMoofDV3rSnaCkp5KvXlDUfbB4V78Z3FMQsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a008082ce2.mp4?token=K52VFPFn67jQ0_z7bbRWOU0VjJsFcB7FWx1cBZB3Fpdwa_GDuJ6pgZIogIsXCo1SlseqySvtzed0W_pcESsvXSiaCib5ZuxadYh2m_ExRtg4G0LYcrC1iQCIuZOx-XCX8JXSrR6-XvkM4M-Ckn-8kbPjC6Q8uiZs-M3fxvZechY2XvwVgWyvz21c3qlfgNOPiFF2B1CEnErxyhkcnsMG-EaNTwhIhQqF81Wt8ClYD2TrfUDP-lMKlMtLE-1_lPEHFjbUpQaGQWyycAu2PhtXec1mIa0Y3VphnUwLXL4qWMRlscjqp4AMoofDV3rSnaCkp5KvXlDUfbB4V78Z3FMQsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنبیه جالب دو راننده جوان که با صدای موسوم به کاتاف در نیمه شب برای مردم شهر تبریز مزاحمت ایجاد می‌کردند
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689440" target="_blank">📅 12:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689439">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0976398e70.mp4?token=ufXqr0MtaYht7Uq0xz_NM6jGr_ZiVx6FXsXG8HwA1cffnz5NLVQeldfCPo622QuDhYWCDCXnzBN_m89icLY8r_-xSawCOsbdUxxqXW8-SX8sQt7cR39ZZMoZiE9gpMqp2QwUR6cuomxydy0sn0HSUnXr8dh0vh1LZYB3Bc-S3w7oGuqXXnSlUfO6gtHhUrJqUkq-hJP94kwcEMKD_B87OlzZjC5130hTbQu1ID0iKIObx_sU2kHBk5M6ZmJOqmxzo7dYG8jFzhliyKfe7XrYngbhl7tB85WMukgaLDCUq3YEVtqwrGuJJDR6zexRU7CXavv6IdpYfJ2Ud4KgBNuBDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0976398e70.mp4?token=ufXqr0MtaYht7Uq0xz_NM6jGr_ZiVx6FXsXG8HwA1cffnz5NLVQeldfCPo622QuDhYWCDCXnzBN_m89icLY8r_-xSawCOsbdUxxqXW8-SX8sQt7cR39ZZMoZiE9gpMqp2QwUR6cuomxydy0sn0HSUnXr8dh0vh1LZYB3Bc-S3w7oGuqXXnSlUfO6gtHhUrJqUkq-hJP94kwcEMKD_B87OlzZjC5130hTbQu1ID0iKIObx_sU2kHBk5M6ZmJOqmxzo7dYG8jFzhliyKfe7XrYngbhl7tB85WMukgaLDCUq3YEVtqwrGuJJDR6zexRU7CXavv6IdpYfJ2Ud4KgBNuBDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتفاق خاص:
جراحی تیروئید بدون بُرش گردن و جای زخم!
این جراحی نوین با بهره‌گیری از تکنولوژی روز و مطابق با آخرین شيوه های جراحی در پیشرفته‌ترین کشورهای جهان ( از راه دهان)
توسط
#دکتر_طاهر_تیموری
انجام می‌شود.
مزایای اصلی:
بدون هیچ‌گونه اثر زخم روی گردن
درد بسیار کمتر و بهبود سریع‌تر
حفظ کامل زیبایی ظاهری
▪️
دکتر طاهر تیموری
فلوشیپ فوق‌تخصصی جراحی لاپاراسکوپی
📌
اینستاگرام:
https://www.instagram.com/drtaherteymouri</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/689439" target="_blank">📅 12:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689438">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwtZbfmGFWIiLeBR7sj_Bwgu0zPfwdKktN9HqgIAicmrYiUJ5vE_rQPnbFYOTOMjssn6pgGuyBQA1wv60C94qXJrvnsEbF5fsb3NkJLwpFIVcXAeR7k1cf5Ca0TZdhkZTztNrVQMO0TuqYivWTpaUzVznm9xW6sV40OXo6unGiaG4Epi_8_p307W3v4ySTy87az4XO6Sh4QRaSBcdWNF_-Wq638DWXIEYmtPkYrFWumOHLZu5cg5Hj5YXM7wv6yHLt1K7_LaQlvgyYAqAXfFnrbDOPrZSkMVHNOnCToMg3kATku2wxBdt-VOhQ-4corhr6Xg0FjnuGZoKh14TCy1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران یک‌پنجم رأی‌دهندگان به ترامپ را پشیمان کرد
🔹
نتایج یک نظرسنجی تازه از سوی مؤسسه «نویگیتور» نشان می‌دهد حدود ۲۰ درصد از رأی‌دهندگان ترامپ در انتخابات ۲۰۲۴، از رأی خود پشیمان شده‌اند.
🔹
۴۵ درصد از افراد پشیمان، جنگ با ایران را مهم‌ترین علت پشیمانی خود عنوان کرده‌اند. این یافته می‌تواند نشانه‌ای از نارضایتی بخشی از حامیان سابق ترامپ از رویکرد دولت او در قبال ایران باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/689438" target="_blank">📅 12:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689437">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc_taIB2c_omY1BngKoKHt0N5fm67LoXUl2B3rGxlqiLxoUUuILFVlqtzxWyif_Bsrx1QsgwDDb8hYhtJmort0_CixODYOhtBnj_5H0MKdl1xkVn9Zv8eti1DKdTH3SGL1ZjKz5akIGGw5ZzQS27jhPlr5vWLbnLOX7OAY--jrQJ1LS2T67fqChafjBUvO1-Ig12P2SFOcCAW63vE8WsUP8g13sk1_e46zJtCCC2lVDCddd2wLH9iletTZV__-xOh7Uh5jKJ48n8WXeg3q-Xjf3Rto7kPc-wqKC-4njTqXBXIweyWALrnSFdaDz2kaU3q18NBn7-ZrAEoh2bKBatJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فشار عجیب پیت هگست به خلبان اف-۱۵ سرنگون‌شده در ایران!
🔹
شبکه سی‌ان‌ان به نقل از چند منبع آگاه آمریکایی گزارش داده است که پیت هگست، وزیر جنگ آمریکا، و شماری از مقام‌های سیاسی دفتر او تلاش کرده‌اند یکی از خدمه هواپیمای اف-۱۵ سرنگون‌شده در جریان جنگ با ایران را برای حضور در برنامه تلویزیونی «۶۰ دقیقه » متقاعد کنند؛ اقدامی که بار دیگر پرسش‌هایی درباره نقش وزارت جنگ آمریکا در مدیریت روایت رسانه‌ای جنگ مطرح کرده است.
شرح ماجرا را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244771</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/689437" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689436">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
‌مرزهای عراق باز شدند   نهاد اطلاع‌رسانی امنیتی عراق:
🔹
تردد مسافران و تجارت در مرزهای الشیب(چذابه)، شلمچه و مندلی(سومار) از ساعت ۶ امروز از سر گرفته شده است.
🔹
عراق به‌دلیل آنچه «ساماندهی اداری و امنیتی» توصیف شده بود، این مرزها را از روز جمعه به‌طور کامل…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/689436" target="_blank">📅 12:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa08c373.mp4?token=Zfpqvz045km8B3W1ocVDM25jcUfgMoVQ2PNt0XT1M8B6RO5fju3xmjh6sRU8Ame8PQ3jsPBmRFIn0BJmm_MJkD1xpqxPN8nAON3rAyrZg10VTHR1CMCeZ0_I2kihE_6gpUKb6PJgCQvDZ6_Az_iNCJRW1dj-7ShZk0r3MSx2szDcxCn7azT_1ehsU8ifguZqZroeUc_WrGojoCF0MWvvZ09LQ8T5PAPK1eIKCiKSZAdOwu9clLV72IbAqfsZyxD2CYpDCIBdA9-6tj7LayRpSHTQQ2QAEe720M4aPMDqoE6d2wP0THqZbRuAUwtOQorkNbtv-qK_4-VCiw02Fg5Qig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa08c373.mp4?token=Zfpqvz045km8B3W1ocVDM25jcUfgMoVQ2PNt0XT1M8B6RO5fju3xmjh6sRU8Ame8PQ3jsPBmRFIn0BJmm_MJkD1xpqxPN8nAON3rAyrZg10VTHR1CMCeZ0_I2kihE_6gpUKb6PJgCQvDZ6_Az_iNCJRW1dj-7ShZk0r3MSx2szDcxCn7azT_1ehsU8ifguZqZroeUc_WrGojoCF0MWvvZ09LQ8T5PAPK1eIKCiKSZAdOwu9clLV72IbAqfsZyxD2CYpDCIBdA9-6tj7LayRpSHTQQ2QAEe720M4aPMDqoE6d2wP0THqZbRuAUwtOQorkNbtv-qK_4-VCiw02Fg5Qig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلید داخل قفل شکست؟
🗝
این ترفند ساده را قبل از تعمیرکار امتحان کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/689435" target="_blank">📅 12:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a1454e8e.mp4?token=USNKoxyuRmc8SLz17ZyFBhYPmYZUbfUY4Wt1xo42GRKmtMz2YeUgPsnNYFAFVOZnSOyo-NMbIHjRzU8JlClG5Py0NOpwqB-H9dlKTqJuFLC8zmRBnuhB_bmgbRxLJ2YQOWB1PXx37X1J5YQlg0Bq_G7L923BDqWGmC6RgdKflMB70uvf4_WtwMtjsGsnGf-7y7x4Uc2HSyar34geC4_1meKm1kI1ErljdJ-CpohlbPtS0a-MImPJXTex6zuggW6S5zZ40xERZPLsGkMTFgrBhzh_VhrI08oHDnINOgan5j14MdBvM7Y_2NtnhdUX9Jchib-oML2LxMdoeYtFldgH5ITBLfMjgPBo_3Z_mg0PAlzqA1wRUNNpez2Af3-qvuoTglhdQLnpmDjXeGQcniw1bPOsBlIkLJRQmNCYsSpkxu7X-J-_JEL11Ur4D34racE-pkldhVTwqmXo0z93NjxPDo5M8y3OWsMTCQ-iRbfaXk6fvdkRwOa-puwiJ9793lB51VYiCkG11-BNuh_1bBVEzoK62PmruLsjLb3Ev_jwtV8URj_FNPGkLFH4N84I1rz9s1qjVK9mEGK3mwB-NrlWtbCINDru1pJ7IxsTjbXsCBhrRYkedJP9uVEULfK0mDcWEXnJpg9Dzwq1tzLUbo2T3H6gKOA8662JZaZKHkgocVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a1454e8e.mp4?token=USNKoxyuRmc8SLz17ZyFBhYPmYZUbfUY4Wt1xo42GRKmtMz2YeUgPsnNYFAFVOZnSOyo-NMbIHjRzU8JlClG5Py0NOpwqB-H9dlKTqJuFLC8zmRBnuhB_bmgbRxLJ2YQOWB1PXx37X1J5YQlg0Bq_G7L923BDqWGmC6RgdKflMB70uvf4_WtwMtjsGsnGf-7y7x4Uc2HSyar34geC4_1meKm1kI1ErljdJ-CpohlbPtS0a-MImPJXTex6zuggW6S5zZ40xERZPLsGkMTFgrBhzh_VhrI08oHDnINOgan5j14MdBvM7Y_2NtnhdUX9Jchib-oML2LxMdoeYtFldgH5ITBLfMjgPBo_3Z_mg0PAlzqA1wRUNNpez2Af3-qvuoTglhdQLnpmDjXeGQcniw1bPOsBlIkLJRQmNCYsSpkxu7X-J-_JEL11Ur4D34racE-pkldhVTwqmXo0z93NjxPDo5M8y3OWsMTCQ-iRbfaXk6fvdkRwOa-puwiJ9793lB51VYiCkG11-BNuh_1bBVEzoK62PmruLsjLb3Ev_jwtV8URj_FNPGkLFH4N84I1rz9s1qjVK9mEGK3mwB-NrlWtbCINDru1pJ7IxsTjbXsCBhrRYkedJP9uVEULfK0mDcWEXnJpg9Dzwq1tzLUbo2T3H6gKOA8662JZaZKHkgocVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سفیر سابق ایران در پاکستان: مشکل تردد در مرز صرفاً زیرساختی است/ ادعای اختلافات سیاسی صحت ندارد
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/689434" target="_blank">📅 11:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/689433" target="_blank">📅 11:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689432">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts6r0II_V-gFZtRYIE-qP_87F-Lp55Ife-AydQ8flHR0etnxfSRVuMgMpPlc_NyGIQK5VtHyEy-XdL0FnJypDWbKDtQ5ua5qN82LILVwQEvW82Zciz-FTDWeKOEV0l9BIV5zovGW3M_b_mVfozM2VefOPpSl9ALGV7aLV1ulH7DndQxqs4evRZjfxkqr3T19mOxgFLYnGkdldaBp1caysxGxM-J1ZeW3o4qOONkBjvd6g0ySoQV_qI3I9Bv0LbTbFZ2f3pMbpot7zRYj37keSisvDXl7m22RE-MXjadVNJCMeZ9Wpy4tLn-KtkMdT2ejU5mq59uk1zyzLeeJGM1JTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های غربی: ایستگاه پمپاژ نفتی عربستان به طور کامل نابود شده و بازسازی اولیه تا چند سال غیر ممکن است
🔹
خط لوله شرق به غرب هم منهدم شده و عملا بارگیری جدید در ینبع فعلا نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/689432" target="_blank">📅 11:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689431">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d45bc45b1.mp4?token=BCfNtVCNIDZN-JmIn4DNDeGRYZiOtSkIZQcTgMEPG-eeLhQvmi0naEgUdmMn0fRzEZPIilIP8RRLD73jTHkVgCb4YMNOls7Tl8TAxLcCGAkUeDMGTp-ggYa9TCClBvjLY6qC2VozKmU_Vzuew3_0nBMS_Dq_b-LIQ78882OYFjWtIH0DWR9rOkpfRlHcGh-YnE6vReIF0vjBdXFvDz0FUPbgT6I8kYLm0vVp9Hfk4v69YywS3SQFf_aM5i5rD9KhZCXAk6tFxoEwPfByvQCrhmMWbQjX7dmbDWH6zAhG1ZT1zsQAji_KlsJVuqNfI04P8YT9kimkqHVMcff6ejVppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d45bc45b1.mp4?token=BCfNtVCNIDZN-JmIn4DNDeGRYZiOtSkIZQcTgMEPG-eeLhQvmi0naEgUdmMn0fRzEZPIilIP8RRLD73jTHkVgCb4YMNOls7Tl8TAxLcCGAkUeDMGTp-ggYa9TCClBvjLY6qC2VozKmU_Vzuew3_0nBMS_Dq_b-LIQ78882OYFjWtIH0DWR9rOkpfRlHcGh-YnE6vReIF0vjBdXFvDz0FUPbgT6I8kYLm0vVp9Hfk4v69YywS3SQFf_aM5i5rD9KhZCXAk6tFxoEwPfByvQCrhmMWbQjX7dmbDWH6zAhG1ZT1zsQAji_KlsJVuqNfI04P8YT9kimkqHVMcff6ejVppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف صریح افسر ارشد ارتش آمریکا؛ ما نمی‌توانیم ملت ایران را شکست دهیم
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/689431" target="_blank">📅 11:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcd8RXD9nNnERel6KedhkxC-wLKOg7vvzMEa0b7wIwjIh9UVsdHSQ02K9AeUG59PGGIZQT3JxGMzewpA_TS-w19N8ngyp2xs3XRR8S9S2B3FmB1MIX2yc-MeDUSE5B_KRAcli_8InIvbB5zcGJij1IeNm2O2CUVPIkGGddMF3dwqMOWoTohkOR9wV70B-HijGVOrdJ624RRmwVSs_BOGWUVvwdz7Cbe_nJ6ZjLqXbA4LfQrKGED71St4QzVzOI4BTObU2sK_fFcLdBof7lNmWI0nllJahn4eR0jeccp1VrjyevsliaAhnpudVhFmN-BnwZ-WOZVh_7IaKsJtXJoYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/689430" target="_blank">📅 11:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ثبت بیش از ۳۰۰ دادخواست علیه آمریکا و رژیم صهیونیستی
سخنگوی قوه قضاییه:
🔹
امروز در شعبه ۵۵ دادگاه بین‌الملل تهران به پرونده تجاوز دولت آمریکا و رژیم صهیونیستی به ایران رسیدگی شد. بیش از ۳۰۰ دادخواست با بیش از ۳۰۲ هزار خواهان برای مطالبه خسارت‌های مادی و معنوی ناشی از جنگ، وارد شعب ویژه دادگاه‌های حقوقی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689429" target="_blank">📅 11:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f633209e3.mp4?token=c1a33hXE9jTSIy0luWAUUAWHLoN72Nh5OPCUNlCXXIqn_Ropsb9yHr7aRiwMcLFD6qTepEm1ww1nZ7o9hjEArHTMr2gf4IBICwsg59e6CoI3uzWfq-mJJducUCwBqMsrDQ07LjZycpmDWRi8Jc3T_o76JjgjKODEz9lc_DtkofZWXPdowVq4gSHVWqvssUGOm8z1GY8_L3oOat92x3TPagl4Pe0ozArZgwsxP1R0QnVntu6XHjUmKGziulDBAHVIkVdE3lOkPx7chVRoSrGR-wp5LqIARu85it1z9N1yiijtKBR5CW28MQg-Z1vzwlAfZB-LNHQ9RwlYR4dWBbKVJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f633209e3.mp4?token=c1a33hXE9jTSIy0luWAUUAWHLoN72Nh5OPCUNlCXXIqn_Ropsb9yHr7aRiwMcLFD6qTepEm1ww1nZ7o9hjEArHTMr2gf4IBICwsg59e6CoI3uzWfq-mJJducUCwBqMsrDQ07LjZycpmDWRi8Jc3T_o76JjgjKODEz9lc_DtkofZWXPdowVq4gSHVWqvssUGOm8z1GY8_L3oOat92x3TPagl4Pe0ozArZgwsxP1R0QnVntu6XHjUmKGziulDBAHVIkVdE3lOkPx7chVRoSrGR-wp5LqIARu85it1z9N1yiijtKBR5CW28MQg-Z1vzwlAfZB-LNHQ9RwlYR4dWBbKVJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار ارشد کانال ۱۵ رژیم صهیونیستی: حوثی‌های یمن پیشروی‌های غیرمنتظره‌ای داشتند؛ در ۲۴ ساعت گذشته، عربستان کاملا منزوی و تنها شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/689428" target="_blank">📅 11:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b40ea35a.mp4?token=M9v20wdUfjS7kIkRSRA61YFeuo5J7FnFMMjr9jI3TyDhx8jeMiO78lkJs2jIWjPy-fH9-jQb7UB4G1oWa9ln0qNmhdLuYNqcqTfJk8J0LCQJPV9Yzdzs56Bmx6W1iFpViIj2RPHTXPacTB4877hJ0BFooyMpcy1QPXoQfWqxZYGXxN2UQrqWQuOfC6tQFsBmYEiV9drfMu4f1KmzOLJvCB3e5w4dAV7kaw9j_pGj3TCDLgCpjQiak2AlulYUrD6VRL_3UrZgg6Xe8C5_15vPw5Kvh-adro41m9Z7Vr_KoQ-bmr0Os7zl2GjrqQ9ia5Ym2jQEozJecvqHm5WcdCmL5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b40ea35a.mp4?token=M9v20wdUfjS7kIkRSRA61YFeuo5J7FnFMMjr9jI3TyDhx8jeMiO78lkJs2jIWjPy-fH9-jQb7UB4G1oWa9ln0qNmhdLuYNqcqTfJk8J0LCQJPV9Yzdzs56Bmx6W1iFpViIj2RPHTXPacTB4877hJ0BFooyMpcy1QPXoQfWqxZYGXxN2UQrqWQuOfC6tQFsBmYEiV9drfMu4f1KmzOLJvCB3e5w4dAV7kaw9j_pGj3TCDLgCpjQiak2AlulYUrD6VRL_3UrZgg6Xe8C5_15vPw5Kvh-adro41m9Z7Vr_KoQ-bmr0Os7zl2GjrqQ9ia5Ym2jQEozJecvqHm5WcdCmL5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل از خرید میوه، این نکات ساده را حتماً بدانید
📦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/689427" target="_blank">📅 11:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEITPhVR-ptguIjxqF0x5LeJjL7ZTzl8a8aCVoSxwRfe4hq5w8IBSjoxgq1bAiy_ySgQDoJV-ZTemfGYN5_R7nU7VrIWjowJLX24PiKhdSrbqrGhZJRlFbqIWHfEqsuyhZRXZUdNXqkZoA2J5-G_wIxMuePNWSx0RbsKaWYEww8kMqbqaBt5wONhIjeQfd9wVOo7EUEhiRgrDTUtKM_CpwcGXjOjmmbkm5J42p4bETIp3vnMpR3xAWwbH37xx3NpNmJLwiEzHxljhUyMGdHE5HxQMHOfckgZZMOfhf4TuB_rNK73dog9nut4bkNRiwIOWlLItB1rsnDsGa3nyCX0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ملل یک گام دیگر به سمت ثبات؛ صورت‌های مالی ۱۴۰۴ تصویب شد و مسیر افزایش سرمایه آغاز می‌شود
🔹
مجمع عمومی عادی به‌طور فوق‌العاده مؤسسه اعتباری ملل با حضور هیئت عالی بانک مرکزی جمهوری اسلامی ایران، هیئت سرپرستی مؤسسه، حسابرس مستقل و بازرس قانونی و نماینده سازمان بورس و اوراق بهادار برگزار شد و صورت‌های مالی سال مالی ۱۴۰۴ مؤسسه به تصویب رسید.
🔹
به گزارش روابط عمومی مؤسسه اعتباری ملل، صورت‌های مالی سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ پس از بررسی‌های لازم و در چارچوب استانداردهای حسابداری و ضوابط بانک مرکزی و سازمان بورس و اوراق بهادار مورد تأیید قرار گرفت.
🔹
تصویب صورت‌های مالی، گامی مهم در مسیر افزایش شفافیت، تقویت انضباط مالی و پیشبرد برنامه بازسازی مؤسسه اعتباری ملل به شمار می‌رود.
🔹
همچنین با انتخاب حسابرس مستقل و بازرس قانونی مؤسسه برای سال مالی ۱۴۰۵، زمینه لازم برای آغاز فرآیندهای اجرایی افزایش سرمایه در چارچوب برنامه بازسازی فراهم شد؛ اقدامی که می‌تواند به تقویت ساختار سرمایه و بهبود شاخص‌های مالی مؤسسه کمک کند.
🔹
این اقدامات، بیانگر حرکت مؤسسه اعتباری ملل در مسیر اصلاح ساختار، تقویت بنیان‌های مالی و دستیابی به ثبات بیشتر، با نظارت بانک مرکزی جمهوری اسلامی ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/689426" target="_blank">📅 11:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYL_us3u2oZooTR3WY2TMfQ2uucDfhrN1i1lNIokH0RK6qjv6xs9_YZv93nN6MQIohKo9M0b2jqsvFaoDuuYs1hpZJbxRHGP1J7r79vGRh8I4fWClclYMGw1PW8OnfGPxfov2TRiOEpp-ofUo5wRCtP66bqtFuSRH5uc6NLTMbowWEZduEtaH0a97NSoUCEPQIzEq9wL80AmY93jEwKeFIFhT3S1b2T54hR4hTqcWJ5JaenBHeyCMg2mD8veOsO23wqb57p268XEI7zaKEOMHC1TrZyuYSg_VPLK9S99Ph83g6YYrjYe0WIQT85DYLIWGPvrjVNz3K_pP8pr-Nw2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیه با ارائه طرحی خواستار دور زدن تنگه هرمز شد
ترکیه‌تودی:
🔹
وزیر انرژی و منابع طبیعی ترکیه، از قطر و کشورهای اروپایی خواست اراده سیاسی لازم برای پیشبرد طرح قدیمی انتقال گاز قطر از مسیر ترکیه به اروپا را نشان دهند.
🔹
این طرح در شرایط اختلال در تنگه هرمز می‌تواند یک مسیر جایگزین برای صادرات گاز قطر ایجاد کند. بایراکتار طول این خط لوله را حدود ۲ هزار تا ۲۲۰۰ کیلومتر اعلام کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/689425" target="_blank">📅 10:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
یحیی سریع؛ سخنگوی نیروهای مسلح یمن: دشمن سعودی طی ۴۸ ساعت گذشته ۱۲۹ حمله هوایی را علیه مناطق مختلف یمن از جمله تعز، الحدیده، الجوف و مأرب انجام داده است که عمدتا از پایگاه‌های هوایی در خمیس مشیط و طائف و توسط جنگنده‌های F-۱۵E و تایفون آن‌ها صورت می‌گیرد، خواهید دید به این تجاوزات چه واکنشی خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/689424" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0171c995a0.mp4?token=m_17KwPmrmiik7snotxJBLjsqGGjgxmxrAgSCVpnoDsUsn1DSGCghI7mJlyZf27F0PgV8bt3Nxbu59xddYjV22GthXcG1t79W_OwI36Y73eYpFMh2sbo5ViFhYnn5olS0MQfpBvOBK-nIwNvB-QfPBJfLpAVlZkIaKbrFOmTdY-anaW3QnHA8igJelqDrP-QnRVZ9PfCvLN9ocJpH099Y07pKA9rlwEEk61aS9nXj7PZg-X78tz_LmiGq6lUlZb4z-4dfeHi6LAq-Nrw7edukjRsbLsQw8lo_ONUFkGwh0gUIylyqAhE764LpGQikGnzK-6L58gDFiaDvCE4GNiQnWsxC2Y5CKMj_77PAP3DP-J9VV_QqmR36JaBJqmyQ1UoF5FYylA4Uvf9Z4hJ7a-CdC_risPviddEkxZQ2O54D0PFbXZnZCIydxxRqe7jfJgzabIvut5IztFrm_HTJok0Xgy9bOsF21fhzXV3yRP0qm--nuogzS5pCS-3APjC_GpprkxfVksBw-99QrjbneQcCHDl7LbeCsTigJIeeBUi-Y7YJRNwPnkUCXHSBDV9jtjBDSLXYuzgzcV4KGCsCdTyD1KCM9mXfGPULqNzGpIMHkmAcYvoghZje--YaSsECZ_Uqh7_oB7l5jSaJjnN6W7b5q0-ynDtUFsbscZGprciZsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0171c995a0.mp4?token=m_17KwPmrmiik7snotxJBLjsqGGjgxmxrAgSCVpnoDsUsn1DSGCghI7mJlyZf27F0PgV8bt3Nxbu59xddYjV22GthXcG1t79W_OwI36Y73eYpFMh2sbo5ViFhYnn5olS0MQfpBvOBK-nIwNvB-QfPBJfLpAVlZkIaKbrFOmTdY-anaW3QnHA8igJelqDrP-QnRVZ9PfCvLN9ocJpH099Y07pKA9rlwEEk61aS9nXj7PZg-X78tz_LmiGq6lUlZb4z-4dfeHi6LAq-Nrw7edukjRsbLsQw8lo_ONUFkGwh0gUIylyqAhE764LpGQikGnzK-6L58gDFiaDvCE4GNiQnWsxC2Y5CKMj_77PAP3DP-J9VV_QqmR36JaBJqmyQ1UoF5FYylA4Uvf9Z4hJ7a-CdC_risPviddEkxZQ2O54D0PFbXZnZCIydxxRqe7jfJgzabIvut5IztFrm_HTJok0Xgy9bOsF21fhzXV3yRP0qm--nuogzS5pCS-3APjC_GpprkxfVksBw-99QrjbneQcCHDl7LbeCsTigJIeeBUi-Y7YJRNwPnkUCXHSBDV9jtjBDSLXYuzgzcV4KGCsCdTyD1KCM9mXfGPULqNzGpIMHkmAcYvoghZje--YaSsECZ_Uqh7_oB7l5jSaJjnN6W7b5q0-ynDtUFsbscZGprciZsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلتنگی امیر نوری برای عمو اکبر
🔹
اکبر عبدی از مریضی خسته شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/689422" target="_blank">📅 10:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682c96382a.mp4?token=oGiUpHss_0-eLvRGlgmnqmeahKTR1qNhh4PrCpVmLCzRhxp_Z2YDQ-Tw7__mimLQlqktEYfcgp1L-hyR8KQBMGxreewYagTc-PPP4yisbL4lwJ4xfC2O1mvd4MvdRtDQdynNq7XkDGzZFABYbNMAn2ZQSG-QaZM8hipRKU-xqulHpKTUCFqwH7sjxLDfZYxDnnwX63GBF1VCfUg2_RKcyFKGstX5Jx12kRNzC9yb9hmdHoXyUIDx8XimbUk4EhXtm7ZDO0uqRZCNluty7865ZHjy0hhKwlWm48AXSJuIXEMm6m4Q7zuOw5ziTuNctXX58PQNIEeCV4P05L_plKrTX6eITkVWCCw2vlDdrE4Kd6mNL3h1_qnmBIhy_K0_OejSLIJ8CZatO5D7il0HA4fM5tmMm_HOcUZduCdowcLjXu2z4K1yYNk5H8OdjkIrc7TYT9WjbOWOVT1dkv6oUro_biACgJqTKWE0UbYU7uf8qDax8okAJlgVxCXGFsAwfR355_zX1zI3UfQWOO5gikS2QZYI6pa10GSFJCbK5HMey55Fhif9E-kavG7UH0CG9JMGtOKI11KZi986eVhDf9bzeQE1f-wBOJn5uVyDjEdb6gg0nW8OVuybqx2gJMsVR4a5U0teeD2ROEFxDw7gZVtqSIME6MLwkWbTca10ZRBOqvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682c96382a.mp4?token=oGiUpHss_0-eLvRGlgmnqmeahKTR1qNhh4PrCpVmLCzRhxp_Z2YDQ-Tw7__mimLQlqktEYfcgp1L-hyR8KQBMGxreewYagTc-PPP4yisbL4lwJ4xfC2O1mvd4MvdRtDQdynNq7XkDGzZFABYbNMAn2ZQSG-QaZM8hipRKU-xqulHpKTUCFqwH7sjxLDfZYxDnnwX63GBF1VCfUg2_RKcyFKGstX5Jx12kRNzC9yb9hmdHoXyUIDx8XimbUk4EhXtm7ZDO0uqRZCNluty7865ZHjy0hhKwlWm48AXSJuIXEMm6m4Q7zuOw5ziTuNctXX58PQNIEeCV4P05L_plKrTX6eITkVWCCw2vlDdrE4Kd6mNL3h1_qnmBIhy_K0_OejSLIJ8CZatO5D7il0HA4fM5tmMm_HOcUZduCdowcLjXu2z4K1yYNk5H8OdjkIrc7TYT9WjbOWOVT1dkv6oUro_biACgJqTKWE0UbYU7uf8qDax8okAJlgVxCXGFsAwfR355_zX1zI3UfQWOO5gikS2QZYI6pa10GSFJCbK5HMey55Fhif9E-kavG7UH0CG9JMGtOKI11KZi986eVhDf9bzeQE1f-wBOJn5uVyDjEdb6gg0nW8OVuybqx2gJMsVR4a5U0teeD2ROEFxDw7gZVtqSIME6MLwkWbTca10ZRBOqvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی مجموعه کتاب
«کودکی نامداران»
🔹
قصه‌هایی از کودکی قهرمانان و افراد نامدار تاریخ ایران
🔹
برای عضویت در کانون پرورش فکری کودکان و نوجوانان عدد ۰ را به ۴۰۴۰۸۲۳۲۰۰ ارسال کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/689421" target="_blank">📅 10:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689420">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe8d4a20e.mp4?token=Rnv-6C7clZd0swNzXzjWUGSPmGx7aW7QMNr2jTTuDfqUIuBa0r01UaoTsSIT7LUzIOYdHl6KIoY1BW0ziwb04U-RGnOg6DmJf30S8V1DbqbMke3zBkcZfQ9OjmxfEocHG8CyDvNlNadxHjXGczjK41oZS2Qz5J6mY_s_gXLeV_83Li8USKxhykz7ntIHhjuWQ0xLVMzNLbrdWSD7153o1wSA_SupyTDmXxiRjiMtftrTESBsUKF8pHQyOJYalMche1jQu5kWyjDkXMd3xKHLy9jQPZLI6mGdlijL5XiZv1-zCfxaV_vneh8Tcj098e6dyc_FkfcKL81dhm7E7_53EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe8d4a20e.mp4?token=Rnv-6C7clZd0swNzXzjWUGSPmGx7aW7QMNr2jTTuDfqUIuBa0r01UaoTsSIT7LUzIOYdHl6KIoY1BW0ziwb04U-RGnOg6DmJf30S8V1DbqbMke3zBkcZfQ9OjmxfEocHG8CyDvNlNadxHjXGczjK41oZS2Qz5J6mY_s_gXLeV_83Li8USKxhykz7ntIHhjuWQ0xLVMzNLbrdWSD7153o1wSA_SupyTDmXxiRjiMtftrTESBsUKF8pHQyOJYalMche1jQu5kWyjDkXMd3xKHLy9jQPZLI6mGdlijL5XiZv1-zCfxaV_vneh8Tcj098e6dyc_FkfcKL81dhm7E7_53EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوییک در نیشابور، توسط زمین بلعیده شد
🔹
در اتفاقی عجیب در خیابان فردوسی شمالی شهر نیشابور، زمین دچار فرونشست و شکاف شد و یک خودروی سواری کوییک را بلعید.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/689420" target="_blank">📅 10:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689419">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78168ec197.mov?token=fb9VQgXDOLDUcAJG2z5UurDG6Rb-VRRuEc7bYZ0HW-3rVOC1ioRMII3Zt9u9JVCgEf_eQbHNoxR97dxKtTuk_tSXcJBPC6uannkO33CniKmOOHn8N-aDLe2ylUhgF_-oR28lH3kOX61CQf28-_i_i7Hrrx7fENNjQwtdP8c5sxc_EYXCYVqGsdCxZQjy2-gsc4UFtsqP4ZR67TfJuB-vdvIIhxTnsFNFNSB70cS41w2KiN0o0xpg9aXhCxEakSCr2sRNTdQdnQHX6mUeoCHpfc1t_UFgUSVLI0th7o6SIUZSDNM-lXdGV0dKsWyEgv2-hGB4TBmkqCi2cuvq_XeW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78168ec197.mov?token=fb9VQgXDOLDUcAJG2z5UurDG6Rb-VRRuEc7bYZ0HW-3rVOC1ioRMII3Zt9u9JVCgEf_eQbHNoxR97dxKtTuk_tSXcJBPC6uannkO33CniKmOOHn8N-aDLe2ylUhgF_-oR28lH3kOX61CQf28-_i_i7Hrrx7fENNjQwtdP8c5sxc_EYXCYVqGsdCxZQjy2-gsc4UFtsqP4ZR67TfJuB-vdvIIhxTnsFNFNSB70cS41w2KiN0o0xpg9aXhCxEakSCr2sRNTdQdnQHX6mUeoCHpfc1t_UFgUSVLI0th7o6SIUZSDNM-lXdGV0dKsWyEgv2-hGB4TBmkqCi2cuvq_XeW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجه وانگ‌یی به نشان نقشه ایران روی کت عراقچی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/689419" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689418">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGhhAmO37LOZ8fhMSa-m1eoSr_HdlTprOOkgz3w8cdEMQz6uSDZyaWmQMHQcGC7o6_TsHvTFKl8AtQyGsBmeTDqZ2VyLezQkTTaCAlZPF7Nkt0bp_rB2AHirMiO03LZPIBrqHxW4s1tiHjmgdyid4WLej7nxIGG9r-nXNPug7E8WHA6TzT0yeF18tj3M6IqzXdv65dQh8_cgqchowRrGM_NgntxsunJ1Ts3KdZgvCBcmaY9DE2NxX9qNGRIkKGYZjzDcdJJff4rrP7pVLV7PWfwnaIJGQsF9RMUGj70lIeyyYQWRuemcYdjljkwO9OVoFWCfQA_hHPgINCv3qyNFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ رسانه‌های عربی: مزدوران عربستان سعودی، شامل برخی گردان‌هایی هستن که حدود ۸۰ درصد اعضاشون «سربازان خیالی» هستن؛ یعنی این سربازان فقط در اسناد و مدارک وجود دارن و صرفاً برای دریافت حقوق ثبت‌نام کرده بودن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/689418" target="_blank">📅 10:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689417">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
پزشکیان: فردا تفاهم ایران و عمان درباره تنگه هرمز نهایی می‌شود
🔹
ما در رابطه با تنگه هرمز با کشور عمان گفتگو کردیم. یک چارچوب مسیر در حقیقت مشخصی را به تفاهم رسیدیم.
🔹
روز دوشنبه قرار است وزرای خارجه همان کشورهای عربی که می‌خواستیم با هم دعوا کنیم، در عمان…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/689417" target="_blank">📅 10:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe380ebdad.mp4?token=SZ5huQ1cPdv-3V5uID4u4M7nWCqgzaZndQ3GLK0LrUsVcP9CPikgURs3kj6Hd3fCA-QZ1h6yl9tpowGviZRnXQj9asUuyLjWm2J1YzrGtnoX0nEmOpFN71H0MfJkZ_kKqutLjIgtGm8DZb96XZY5TtdmryQ0bzujXjMuD6YairrsvDWGA42frICtrReYvpktnBk8mI4f8QnBkFoQkCY-U9YBE6UnSbyAfcW-NM4a5JPHxW6NQkvGDm7489vDfOYz8KLowjYKOg4-IhJ4SNG6DF8vEQjevKplOBpG-LJJh8I6AsHc2VZe5T25kMg0qWpESN37BchedjX6mbjSJV80CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe380ebdad.mp4?token=SZ5huQ1cPdv-3V5uID4u4M7nWCqgzaZndQ3GLK0LrUsVcP9CPikgURs3kj6Hd3fCA-QZ1h6yl9tpowGviZRnXQj9asUuyLjWm2J1YzrGtnoX0nEmOpFN71H0MfJkZ_kKqutLjIgtGm8DZb96XZY5TtdmryQ0bzujXjMuD6YairrsvDWGA42frICtrReYvpktnBk8mI4f8QnBkFoQkCY-U9YBE6UnSbyAfcW-NM4a5JPHxW6NQkvGDm7489vDfOYz8KLowjYKOg4-IhJ4SNG6DF8vEQjevKplOBpG-LJJh8I6AsHc2VZe5T25kMg0qWpESN37BchedjX6mbjSJV80CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر مردم یمن ۱۰ سال هم نفت می‌فروختند، نمی‌توانستند این‌همه سلاح خریداری کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/689416" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/689415" target="_blank">📅 10:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c0f0ef2a.mp4?token=E9e_3-opi9RszfKqFiFfQPXKkRQibrTzVe7aStM1RujWxrpP6dJZWE9dJFOuv9NTBRaaG89-Prwf63jCCL_gdYSKq7nTRd5Wk3J_Dd_org6rPtZDCt9y2gVyrUoOja_Eiuw7YaWEvoz6R59H7RnF3xHXTefXbapWDti4TjGsBMO1JzTPkNFfqvy_t6nMMh2O29hXSaeUzYDXIi1na45Jy_NxUwyczj3kAnMF6nUwfj0xlvuj6lpDWmq-iQ25Sk2_bcY5A4U1E7nedfZ16M2PgtHPFezEkFnIi82r6GpXXG065duOT3Ty7-pjhx4B0nqZ2b6Jb1j_TabENRncz_YXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c0f0ef2a.mp4?token=E9e_3-opi9RszfKqFiFfQPXKkRQibrTzVe7aStM1RujWxrpP6dJZWE9dJFOuv9NTBRaaG89-Prwf63jCCL_gdYSKq7nTRd5Wk3J_Dd_org6rPtZDCt9y2gVyrUoOja_Eiuw7YaWEvoz6R59H7RnF3xHXTefXbapWDti4TjGsBMO1JzTPkNFfqvy_t6nMMh2O29hXSaeUzYDXIi1na45Jy_NxUwyczj3kAnMF6nUwfj0xlvuj6lpDWmq-iQ25Sk2_bcY5A4U1E7nedfZ16M2PgtHPFezEkFnIi82r6GpXXG065duOT3Ty7-pjhx4B0nqZ2b6Jb1j_TabENRncz_YXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری روسیه: آیا می‌دانستید این‌ها شهروندان عادی در یمن هستند و اینکه حمل سلاح فرهنگی ریشه‌دار در میان یمنی‌هاست، جایی که کسی بدون سلاح مرد محسوب نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/689414" target="_blank">📅 10:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjRlAGy4GC8pi5bJwEh6J2mjkWuWsMQ1CYD0XkuNvRr3eVFlIzrzObuzIwprP4oLyVvvMv9kAPOtWu9EVlfKw5cowMtQbBfme63BhA0UgUGz83o7yrX2QFfnhRF_ut0WaOdKl949wy0Mg_gOYRCqQ-OyXmyg3_sJsWfzhhID5M1uj_9bBesTL0wjpZpdOZrlcMwqWEL5CS3Qf2xpkjri6vQl_RL4LkgDUv7O_qmUFKaeXqcP0Zkt8RKRn_nl1XAQgcsQ1W0NI0qgvJJ4OgeQJsztyrUs4c_5sRumkt7vDWBMA48uM20k2PnSMsA08TJ_-6HUoPnjynb39Ep1mGtoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه فعال سیاسی آمریکایی: انقلابیون یمنی در پی برقراری دموکراسی و آزادی در عربستان هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/689413" target="_blank">📅 10:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb1dc58a1.mp4?token=RzHenhKzsp15wEmAmaDtED4lW2xoQ4A1AqatukS73xjsOCDSRnuIpTZSqR1m-ojVH0tnCs4OiiNao9iOWOMwpFFWb0F0-tmoRIWVsYqeDx6oeQ00UNdtjWMH9sRdaLfqdGwzthgG7Nqo2_t77QgoEUh_injMC9wlXEzgiX7q5lToFp-B2OaIj-rQVTx-MZd_sZCRdmQcJFR5gIOQAPn-MuL5p1eCE6cRd9adaKZowTPxPOwOczzKPhPPqc2Y1XXQvlYn3viOHjSxLu9oe0TvH3vuAEbNwMA5OvhVO7I_SMqZYUSXUf5lF11hadeYwTND94fQO3I0XJukXdUsAeQpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb1dc58a1.mp4?token=RzHenhKzsp15wEmAmaDtED4lW2xoQ4A1AqatukS73xjsOCDSRnuIpTZSqR1m-ojVH0tnCs4OiiNao9iOWOMwpFFWb0F0-tmoRIWVsYqeDx6oeQ00UNdtjWMH9sRdaLfqdGwzthgG7Nqo2_t77QgoEUh_injMC9wlXEzgiX7q5lToFp-B2OaIj-rQVTx-MZd_sZCRdmQcJFR5gIOQAPn-MuL5p1eCE6cRd9adaKZowTPxPOwOczzKPhPPqc2Y1XXQvlYn3viOHjSxLu9oe0TvH3vuAEbNwMA5OvhVO7I_SMqZYUSXUf5lF11hadeYwTND94fQO3I0XJukXdUsAeQpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل کلینتون: من دیگر پیرتر از آن هستم که بخواهم روی چیزی بیش از حد اغراق و زیاده‌گویی کنم
🔹
دو روز پیش، من ۷۸ ساله شدم. پیرترین مرد خانواده‌ام هستم که هنوز در قید حیات ام. تنها چیزی که می‌خواهم بر آن تأکید کنم این است که هنوز از دونالد ترامپ جوان‌ترم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/689412" target="_blank">📅 10:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان در گفتگو با شبکه خبری «ایندیا تودی» هند: ما اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم/ ایران هیچ‌گاه متجاوز نبوده است؛ اقدامات آمریکا علیه ایران فقط تبلیغات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/689411" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با ایندیاتودی: آمریکایی‌ها تروریست‌های دولتی هستند  پزشکیان:
🔹
هر کسی را که بخواهند ترور می‌کنند و سپس ادعا می‌کنند که این افراد تروریست هستند. پس دنیای عجیبی است.
🔹
آنها به‌راحتی برای یک نفر آدم می‌کشند. یک خانواده کامل را می‌کشند و یک ساختمان…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/689410" target="_blank">📅 10:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee8d97a62.mp4?token=fVL4ZlemJnTbPM0UVQ3iAvRJJheumcRKzQoRcHL6_DupfFQGxevKIlKPhRCoBObbr4Sh4DVQj8Qu9DRdSaPy-KvvdbIdvnLTkJVNkx3rXsLOulu1mQqixj6QDAVB-tWbxIp4BRwEEkWPBEkVUwtbBdgQjuKnbanJ78xz0eylYnGZ6Vwt4C-NZOMD3ZURHuNZzzitPdymfS-neIs0wCSOnitms979MiRttzBO_UByKhsLEHEKeh0-ZcUAdBy4JplN1z3KL5Iy9pT14A5tw82Jq8sgO_A6UGP8GZ5D1tx0JIrewOJ2dItgQO7HZmtqFlthoPospHCHPUnfXpse2SdhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee8d97a62.mp4?token=fVL4ZlemJnTbPM0UVQ3iAvRJJheumcRKzQoRcHL6_DupfFQGxevKIlKPhRCoBObbr4Sh4DVQj8Qu9DRdSaPy-KvvdbIdvnLTkJVNkx3rXsLOulu1mQqixj6QDAVB-tWbxIp4BRwEEkWPBEkVUwtbBdgQjuKnbanJ78xz0eylYnGZ6Vwt4C-NZOMD3ZURHuNZzzitPdymfS-neIs0wCSOnitms979MiRttzBO_UByKhsLEHEKeh0-ZcUAdBy4JplN1z3KL5Iy9pT14A5tw82Jq8sgO_A6UGP8GZ5D1tx0JIrewOJ2dItgQO7HZmtqFlthoPospHCHPUnfXpse2SdhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ترکیب خفن و متفاوت که خیلی آسونه و از پیتزا خوشمزه‌تره
😋
مواد لازم:
🔹
سیب‌زمینی
🔹
قارچ
🔹
فلفل دلمه‌ای
🔹
ذرت
🔹
سوسیس
🔹
پنیر پیتزا #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689409" target="_blank">📅 10:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_zU-KqEAp9uf_GgPPc5yE2UtmYiQ9lMqTbmeSzAUWyIP2QdBOOxkRwrn15XGtbYjm6-u859Pq3HQfl7cHMM1lwpUChav9DNsof5WrRl2OC8_ACmNEzkzPVCkPtgsRyJctRtTIqgTzGU1ECFT6yyi9TAvcCYfgKH2bPyy-lMT57AiZWmmfUXTw30hoDS99nxWd42BVkEegiH-A8u-nVdq5_f7btq65WMyD5JzNSDPNWNUiXWOOtFJdug57gK_2-kPYzhCKIpg0bjV4OL_84jQt1IERuKMzL_VchmTizfiOGcG-BRFiOsvpUfkgv4WcUFBCLe0eFBXfEmI75ogjSdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: یکشنبه ۲۲ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/689408" target="_blank">📅 10:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رسانه امنیتی عراق: بخش مسافری گذرگاه‌های شلمچه و الشیب بازگشایی شد؛ فعالیت تجاری در شلمچه از دوشنبه، مندلی از سه‌شنبه و الشیب از پنجشنبه از سر گرفته می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/689407" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با ایندیاتودی: آمریکایی‌ها تروریست‌های دولتی هستند
پزشکیان:
🔹
هر کسی را که بخواهند ترور می‌کنند و سپس ادعا می‌کنند که این افراد تروریست هستند. پس دنیای عجیبی است.
🔹
آنها به‌راحتی برای یک نفر آدم می‌کشند. یک خانواده کامل را می‌کشند و یک ساختمان کامل را ویران می‌کنند، بعد می‌گویند یک تروریست را کشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/689406" target="_blank">📅 09:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d21a23085.mp4?token=OMy04eDcYfFhSXuF2GcHWaprEcSs8Dpm4Id-iaiFCdbmDjcDeAroEpz8R8WHi8p4bvPsbV_woSghYpaVJveC-6LPod8y5audkAqOnoKAf5kRz793lIlqP-i3Ay8DzDN4ufK3ME2Zi8VPM2kUys_AmlijkUqHJ1qcYubUjahMghLa9GfxFp7rNJS0QKSMiPy0Kkp-ujfpAk7O3-nqwosFEULzcgbnguOSuqyW67QdDV8xng6IpBMGHMbI6w2fMYHlqAIqG9bS7QA_bDmprKfcX6aUzEG2CZgDmKyQ49Aj9TknbKoqto7yZCByDBXKS_RDXsJrC2CPp5Drjc74e34x6xIB1q9y-mDfmOOia_pLD-k_MU64x031DVYGb8TGlMyVHFDTGt6zXtFPTgS-i961xjDPeejV1d-WiqhPaQO_OmmJxQAG4tUTMdBk2zqKGOfk8qwI5-WnTImPAz-AtmhXOpnsgCxKN4kLBFo9a3xO4s2P6BVyfs9Et_wqv1Ks_SchFSap3wlgp8h-LhsxIaFQZg109VUQMvQCRVKzU_TfZWCl5BvphjDBXvDe59UHrcz3S70drG9_F0CwlB_s1PqLTYS5AmClaL3UtAYhUDASxFCK-eMmzTPAFs4ldzDfkG3Zdn64uawRtHSQKKvfhekKNR01D6dA93jGLFoPWVz3En8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d21a23085.mp4?token=OMy04eDcYfFhSXuF2GcHWaprEcSs8Dpm4Id-iaiFCdbmDjcDeAroEpz8R8WHi8p4bvPsbV_woSghYpaVJveC-6LPod8y5audkAqOnoKAf5kRz793lIlqP-i3Ay8DzDN4ufK3ME2Zi8VPM2kUys_AmlijkUqHJ1qcYubUjahMghLa9GfxFp7rNJS0QKSMiPy0Kkp-ujfpAk7O3-nqwosFEULzcgbnguOSuqyW67QdDV8xng6IpBMGHMbI6w2fMYHlqAIqG9bS7QA_bDmprKfcX6aUzEG2CZgDmKyQ49Aj9TknbKoqto7yZCByDBXKS_RDXsJrC2CPp5Drjc74e34x6xIB1q9y-mDfmOOia_pLD-k_MU64x031DVYGb8TGlMyVHFDTGt6zXtFPTgS-i961xjDPeejV1d-WiqhPaQO_OmmJxQAG4tUTMdBk2zqKGOfk8qwI5-WnTImPAz-AtmhXOpnsgCxKN4kLBFo9a3xO4s2P6BVyfs9Et_wqv1Ks_SchFSap3wlgp8h-LhsxIaFQZg109VUQMvQCRVKzU_TfZWCl5BvphjDBXvDe59UHrcz3S70drG9_F0CwlB_s1PqLTYS5AmClaL3UtAYhUDASxFCK-eMmzTPAFs4ldzDfkG3Zdn64uawRtHSQKKvfhekKNR01D6dA93jGLFoPWVz3En8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دویستمین شب تجمعات امت مبعوث شده/ اجرای آهنگ «گفتی میخوام رو ابرا همدم ستاره‌ها شم» توسط رزم‌نوازان سپاه- اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689405" target="_blank">📅 09:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
عملیات انفجار مهمات عمل‌نکرده امروز یکشنبه از ساعت ۹:۳۰ تا ۱۳ در جنوب اصفهان انجام می‌شود؛ جای نگرانی نیست.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/689404" target="_blank">📅 09:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de890b77.mp4?token=pF7mzM8Nt-Al_mA4LJheo69XA7o1Z6FtNXgTxvETZr12RMenSei7rws0PmDw6kq-1v28rFllgQmd-xxJKw2QQWseeWWf-Kbn3XX2OndUeC9ZLf9RHIwWgkGfKuvdsKwk1Lkf1INSvZeJUhMpp4gSoQvfHKxS28sfNj_o6m7JVqrF67vjlhmcD-qQmjPSNKW2q1l8teWJm7tZ6t5w7Fv-GGsboM9fr2D7kbeRIaE_B7doT31uDIjuQLIY6n2AxDp1n_sSu6wb29UoltaPETkDrjS7JNnvk3JZ1aP4kGCNz_RhZAQ_RCMhIevuL5mw2-dP4NBL_1cC_ABtsji4dBsYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de890b77.mp4?token=pF7mzM8Nt-Al_mA4LJheo69XA7o1Z6FtNXgTxvETZr12RMenSei7rws0PmDw6kq-1v28rFllgQmd-xxJKw2QQWseeWWf-Kbn3XX2OndUeC9ZLf9RHIwWgkGfKuvdsKwk1Lkf1INSvZeJUhMpp4gSoQvfHKxS28sfNj_o6m7JVqrF67vjlhmcD-qQmjPSNKW2q1l8teWJm7tZ6t5w7Fv-GGsboM9fr2D7kbeRIaE_B7doT31uDIjuQLIY6n2AxDp1n_sSu6wb29UoltaPETkDrjS7JNnvk3JZ1aP4kGCNz_RhZAQ_RCMhIevuL5mw2-dP4NBL_1cC_ABtsji4dBsYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکناس داخل بسته؛ ترفند چینی‌ها برای مقابله با کالای تقلبی
🔹
برخی تولیدکنندگان چینی برای جلوگیری از عرضه کالای تقلبی با نام برندشان، چند اسکناس با شماره‌سریال مشخص داخل بسته قرار می‌دهند و شماره سریال آن را از پیش به مشتری اعلام می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/689403" target="_blank">📅 09:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نهاد اطلاع‌رسانی امنیتی عراق: تردد مسافران و مبادلات تجاری با ایران در گذرگاه‌های «زرباطیه» و «المنذریه» به‌صورت ۲۴ ساعته ادامه دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/689402" target="_blank">📅 09:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc68e4cea8.mp4?token=ATRX70hGe6aBgSFr4yYtD-J7-ZHvsYTZvgrtEho0hbpUjVSucZdvzTJgjgSCgo748p961ZIceRwgVSytZQXjDs50e0f7dhZZGAkoqGwwSCPP77GzNaMWTN19rAqc_tk36pf4UmfHGIU0NvDf2GqA2Ej9kZA7X8_DkQfg5yztprMQ1Hw6HYb0-sHmNeuX8Afs7UoOVZRXamw7Vcx3Qsj70WZ9RaL1zahy1QRFAkoaL_55X00qZUK2sIziIqOC2x98xhIZ_L7zXLTpKJMYE-Eyf39zrHzYKW-vaeSkRv72VvM9gaLrPQ5-V8BokI9pMK8G1H-lfyntWj7089Y6WnAyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc68e4cea8.mp4?token=ATRX70hGe6aBgSFr4yYtD-J7-ZHvsYTZvgrtEho0hbpUjVSucZdvzTJgjgSCgo748p961ZIceRwgVSytZQXjDs50e0f7dhZZGAkoqGwwSCPP77GzNaMWTN19rAqc_tk36pf4UmfHGIU0NvDf2GqA2Ej9kZA7X8_DkQfg5yztprMQ1Hw6HYb0-sHmNeuX8Afs7UoOVZRXamw7Vcx3Qsj70WZ9RaL1zahy1QRFAkoaL_55X00qZUK2sIziIqOC2x98xhIZ_L7zXLTpKJMYE-Eyf39zrHzYKW-vaeSkRv72VvM9gaLrPQ5-V8BokI9pMK8G1H-lfyntWj7089Y6WnAyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد اروزان کارشناس ترک: خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/689401" target="_blank">📅 09:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrwelK_y9P0L6zLjM0CXRHpUhqeC7un4yF3h6WnJxASHdLVqiQxyK57eNijPOTVQpDderz_9_3BMMOPx7wp8iFogUOGu4zKdPlXofTuqKef4BYXwIniYKoMYLYCw9mDsw0Y41V9BeIKUJ6MZAv7tyWYBOwtwlENTBrH-c6LJmbFuxLaLhxXvPq5Xaul0_fCj-ACBqMRqKIhdajIlDX2ry4sIjvo-RxSHxxHn0sMvOG6HRWSYXpcesg_CtH9xHuK-rviW1vCy7D3yrMKfpfSkzhFmDJhRMoEj1ZGvrk5dqCIgLUfKh9DyT6UW3y0SONl4Ly3akvM23U6IUd0c8VRF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمبود کدام ویتامین‌ها موجب کاهش انگیزه می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/689399" target="_blank">📅 09:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEMGYxrs6-ugYHIAkZPqzZXO9Q6x7mhaQj6ws-4QQ5xaJ-ZeqY1jCdMbq2MHBO94sJXQKrxzrjk0hUyjJ2dHVaomYE9OGnbp3UemqvZtAvsUwAHWuPsrz-nJjaglpzQDV-JhggeF6Hn4kFp2GD5pRqEiGwqBWMPCA8hQvc1EuNFFTjDr9QDFYjnft49NPrW3ZgxV1ryxfliR7BQ1P_qI0n8T0jl709gj2I7wwfAdVXC9MNJgnW-4X7HRU6LtnoJOHAGpbYVq47LOaG29MpwPIbp2DGvgzl-tRQFhmmLf3DwqIAc5Z8XKm4NRAycdhJNzC8OP-M8jMD7WVriWsB4Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: یمنی ها از هوش مصنوعی Claude برای ساخت موشک‌های بالستیک استفاده کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/689398" target="_blank">📅 09:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRasa_factory</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33507dbf46.mp4?token=tkJqc3DUMHV3H-FJE-TyRVzS6KdXMRRSCNwfbW1-gLCGXYlURv_4IUlgrpwtGx1lxCnBevPyBhiBvDF9HtH6CmK67bSbM0ebgXcb2-u99s468Hq3yFYTekuJUBejNhMADHCfXKqz4dgG2W32Z2GGqp0PbbWz3b1AiJz51e0ibwsYGEizmpJR1BGy5BreNYDF1p47lQyupol0rxKyYJJsFdsK-QXQt53p-6_Jpr4D3RWBChXHgyi11bzXRL7kRibTtGbE8QCTcM3nPLtlMqpaLri4R9EMKS9z8VK-L3621moiaqwdnSiUZJONZ0Xiffqossa9o7t0XBlg2Ygf0wiSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33507dbf46.mp4?token=tkJqc3DUMHV3H-FJE-TyRVzS6KdXMRRSCNwfbW1-gLCGXYlURv_4IUlgrpwtGx1lxCnBevPyBhiBvDF9HtH6CmK67bSbM0ebgXcb2-u99s468Hq3yFYTekuJUBejNhMADHCfXKqz4dgG2W32Z2GGqp0PbbWz3b1AiJz51e0ibwsYGEizmpJR1BGy5BreNYDF1p47lQyupol0rxKyYJJsFdsK-QXQt53p-6_Jpr4D3RWBChXHgyi11bzXRL7kRibTtGbE8QCTcM3nPLtlMqpaLri4R9EMKS9z8VK-L3621moiaqwdnSiUZJONZ0Xiffqossa9o7t0XBlg2Ygf0wiSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فـروش ویـژه درب‌های داخلی
(ضد آب
💧
ضد بخار
🌫️
خود اطفا
🔥
)
💰
فـقط بـا 4 مــیلیون تـومان پیش پرداخت
💰
راسا‌ دُر با
۲۵ سال
گارانتی تعویض
✅
منازل،هتل‌ها،سازمان‌ها،بیمارستان‌ها و...
🔻
برای اطلاعات بیشتر تماس بگیرید
☎️
05136666789
📞
09153068010
🔻
لینک شبکه‌های اجتماعی راسا دُر:
لینک اینستاگرام
▿ ▾ ▿
لینک تلگرام
راسا‌ دُر تنها تولیدکننده درب‌های پلی‌وود
در شرق کشور و مشهد مقدس
@rasa_factory
|
گروه کارخانجات راسا</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/689397" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
مینو محرز: واکسن آنفلوآنزا به دلیل جنگ و تحریم در دسترس نیست  متخصص بیماری‌های عفونی:
🔹
سال‌های گذشته، واکسن آنفلوآنزا طی چنین روزهایی در دسترس بود. شرایط به نحوی بود که نه تنها واکسن در کشور تولید می‌کردیم، بلکه واکسن به کشور وارد می‌شد. در حال حاضر، واکسن…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/689396" target="_blank">📅 08:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ثبت سفارش واردات موبایل آغاز شد
🔹
امکان ثبت سفارش و ویرایش ثبت سفارش واردات تلفن همراه هوشمند از امروز ۱۶ شهریور در سامانه جامع تجارت فراهم شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/689395" target="_blank">📅 08:49 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
