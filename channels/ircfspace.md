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
<img src="https://cdn1.telesco.pe/file/k1LuiSAA6BzFMyWpNPfMPjIgpq8d8LveqWg-K26Vdql1ixdOnTailE2qgmV-TJUqnTvT9yhZL5FEe3MB0kSqjr8ngGS4AekVfVR6MmhHy9A5VeY4L-E7KJQSPePnqREL3rxjSwu70QUgdI9fzbgg7MDTGJnFACNrpuEd2vph3FOcnLdYHXV0Zkf81jIbgPsrv4HhSqblNxQmGxsNXhP-0uE1hMzrX6eOzOsNDG1aOjvOZajceQxlpEtcV_re6oJ5aZEoHYvzQi44f8LctaMilCdHHcUwxYz0FzKkEYFyVbqSVHUhHQ89jNUa58utnMU-x3WpA4p-8Q_F4d_S1rqK-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 23:12:21</div>
<hr>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3LeCpG0bS_8u8HBjQgqkbdLJJpCuSZG75uZObNMu7B-U3ZHy9aSLvm0Abd8P32FQNsSw985CFN4E0q30rooIl-ssFX2Gc7LFnX-Y7XQfNKPLyvTlewUzHiEI0G-joXYswlEaZF-IXYboWVgioZ7YJFPLbxnV_h5N771fgyXrF3DvEwgj4gE6WsT0XXdQRVcEvJ-HXaDCJBJQOnso_Ihj2WEXzPYPI-i7V6SF-cbFSrhSqqt6Kd1NXWfcLGvUDXooe30NMDbrI7FsuPv6tLuHs0O9iQNP4iFIK-4rQbivwLo-qQX6Ipok84-iDMVbykK23qnYc43P69rfF-WWYtC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cDjQxD0iszJm__S133reNMRQcy9g4wCp5AM5gpHFXJ6ocRBbuvm2jfRuqKr8T_6BHCwDSXS8CmN0FXlN52bEZ1zJEm5J4b1NNCkB6IjLqZLSdcCovy11S0ww40GI5iXEEYipHc09-ThKJdI-RsIX07RF92WWtJKjbDY2uVcJQttbpXYuW9jHmVsg3UGr28VYJ7ZR_Jo2ovxMBOh3KnhBI0xGuHfz5NP4Nr3K1P-zXJSAQdX5GSuk9ntfSQDiUBpb4eyTL9ah231xBfJBLAAo7Txhf-JYXi2LCMyn3uTFMoRW8MNSKlEszZTuVLSEjC0tSP2wM_JcK2itjUZc9UPymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UZSCLfKPbv4mUr52NhIdJgUUiOMZKNueL7k-5vLT8fSNwu31t1XyGpow0zlVIP7pCoep1D_t-OIRkUJpWSuc66cQNVbTgAPPvP48ZgZdbGZ1P7GHrKMtgcJgB0DPjQMEVSXnU-vcLYxuJns3hEUpOy158B6gslgusXEgcWyDMUGhR7qgIfbpHUWxwcO3zK9jvvEJyrysUasq0WW9ns4KQc7cNAB7hbmxcqoalg2p02DP3t-wqc0ralLtrUBJxgqujMLrj0rhwV-xXBRE4q0oFMwqAeGY8UYH8rFR3E7fBCht-Z7qbjYjR4JODHL59BTuukN_hileXCRAWS4_9DQwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MjaQCmuMgwvqelkCAljtcCHE6EWd1C18CgB1LZbqZjecMP9Fs4Hkdtq45aIpt_N5uNe0BISSbG88XLzASeaBfaQ18S28hz8jYq6qqijDv6PMJRVQTw-sAN7MbvosxDbuiIk-n_VizLlHgODBSyf0BIH-M9S-OjdBASaRgU9tCphaL7VF8p5vmgnK_F1e-bbsSao-kvtVQTc-6qY7md8NEQQDfYku9bhtZpDgiiEMLjpd104Ghnu-HvM-IxMsUKyNoNQKj0LmtliLk6Sr_DtRP5fpuY3xD9FB0UJUy0fjx1w4dykUR0OYQjr5VAlC1afJXmt8sIjayzl30UiUGaIAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lTxqEZsjZP4QX9IXkxYdvTJmfr-DhDDlsZJv1zsxj8JMhnyOgsJMGqygl-XVNpTdi2xrmTfOvB1_eHZ4x4t7kOplyWq8lxjGqmYWEcFiM9YTU8Q3Y6O8fmVCBysBjHimLr0Wfyklo2FHrkkDHhgbHJ5GPRDV8ADv7427PdaBL-NPlAcgsLEBW1e6o73Lbbei6h8fldTxFLWo8R3zsKafi2UQIAKWFD4tsjaQvSHtE6VB5_zFRkr71LW8fLfPFA0fAe89HCGaQKEgQuNlnvPYtxBLCvnj9M1mkDal_nFAdt2FHIoqFnSh0kMZLI9mDdJ_fFl2w4llxivCT-EHcB8YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8o4MOdzrv-N3sxlbXxSMH1mRM1DVz4gkVzcCYI_HLdZGVVMFm-RAyzl7uaycQTDJ4FhY_UY2ap8FOmEanWUcIEnCFcIIRJ_3iB_4xceVYFchQm9jPzDtXtn7gO21TubJ09TONoVvAqMdrej2uKq38JRCKEEj1CnO1AdON3meEfNIU4H8rTaD4GM3q83yjm9yFz4zXQV0J8hwaxRBUbGQilnDJrvfLGgvMg8tsTN3o1V0tzkBbAijlI-c10KX2-gufwZOPihTOI_qBnznRVb3SFmVEAkR8w-b6cDSzfuRty2bHMe9mA7t6uWKchgdDsyK_BaBrBjnW9jEFyIEpLl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qnNRYxYq3QNxdkC0NmZhW8hTBlPazBIoNiqMRLKGi7nMTuNaMUI8MXrpGxy-R5P0zK8_SI-JiBZTtgx6ngacPdxv3ore2OG2V0tH1LN-RoWizk-iDMsaeN_riR5DRckiyoiEJ7UteDRTVglaAdQMR1x8bG_LrGGp0wYuJW7Yb6M_obWaGavPtFRNheBHxUWDC6biCaOqvrNfGJc0ZvSxSEKkzCHErWLQ3p6R9mml2A7Akz7f9AyEhdGoTGjtprVZXBHRFa8fNaUB1YMK9xoxe9gddmVZmdpoCS8niIyUpX-fQuUvXblRR0mOSlrcnH9jOmlV13FFOgyL9VdBfIbXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYuNQ5d3AkpL2Uv8VFp3xLypDiDdnU0NrYwrG2m0SxbL8aUiKsXNK7TO3ABRkuul_DQbOBGz5U8usGI2gzypL7a3R6VUWdLQTC1KX3AaY4mte9h-UMXPsPxMg9wM7QgO204NG_ZAKvjVrujwEA9Ux_TSHNNya-CE3r2hka2VMfDgEXjoV9rBvAiKd96NGjfSbX0O1n6LA0gFDWgSSgiFNy6DekiiQz5bQw3Q3CX5ylW9hYWwpgw1JyPexjTChRWmERmJs_t6Q6ySrvLRH_RpbRIhDcFoQpp-GE-entrRZS2NJQMVX7P-kPnj_10kE7UrJFB5vA_PjCzvKEihKcOxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q__onP8nAev_F6RL4VYJotiS_uzhGiFWUoGdipCrW1BRKDr4gv9kaxygROSlADSC3PMVpG9obP0wUfWQcMkX3MzMxQNnK8SCwOCoefP86t394yzvgjTbSMD0nWWxTrcjzbJk-1t9iukcTGlvO8UQn0PJo_QR3hSvdgeaFVgsqskwdTpcGQ-um4TrJjT1UPfzHpB9f1ECLPnOKfKgIaKM0eL4rkIUQlglR9m2lb1Q_BoD3ymUIjf2w7Eaw6dypudmdQa6CnQL8DKMGXUope6-37ysCe24BwJiVJWvTyxACkI6PCG9zA_2QcDD-0QIdFGXbvGXJ4arkklsVhgjv3i3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=JzwaNavNBKlA0K4OsTFqBLKC2B444DOW2cvFY3znSMqUQt-9H9OsjBedSS9XjZFh6OHq3n8ZWxM5Z3DN3i57uw3yBlXRfHeCg3LPbYSeBd2Q5LbV6T1tDN3DASRNzd7jJAlbNiIgiuAYULJNyp0Kt5pfT75ip3iAQ7Rly9sN1Rk54PB8Q9TkjXcJevhHVUTIR9pcNbU00WYd97ujgNmYAHBlngj7svju6fiv8BJEO6pdSF8Bv5ixz2KkNfA3XAJ1VkgLDDQYbPS0gdCzIC3_4kzaPoxxTpIUhVZARLSTqRjiWXdeGQsVVF-8nf_cwnzjpfnIgn9VpF6iPgHcUw--kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=JzwaNavNBKlA0K4OsTFqBLKC2B444DOW2cvFY3znSMqUQt-9H9OsjBedSS9XjZFh6OHq3n8ZWxM5Z3DN3i57uw3yBlXRfHeCg3LPbYSeBd2Q5LbV6T1tDN3DASRNzd7jJAlbNiIgiuAYULJNyp0Kt5pfT75ip3iAQ7Rly9sN1Rk54PB8Q9TkjXcJevhHVUTIR9pcNbU00WYd97ujgNmYAHBlngj7svju6fiv8BJEO6pdSF8Bv5ixz2KkNfA3XAJ1VkgLDDQYbPS0gdCzIC3_4kzaPoxxTpIUhVZARLSTqRjiWXdeGQsVVF-8nf_cwnzjpfnIgn9VpF6iPgHcUw--kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n2dT9XiPAlAeS2SRI8WaDA4sRCNvhwMDnK2PPnCbnHyT9rHPkl4Yp3WL-wWgZc1adId2Hvsv3hX_GFeVXSgV88PMIF9oEoa2l2ln-ZbfdA_FgqvekT0xmdUx9y0KYDxfqnR38jkj6hYfw_wRUJpXG_ZQerrOuMINrRRYrTRakPpMzgQgEZoIUME5IRwLi3yFuyRmHOLso7vFb7JftPchT2y2pKIiFKk93eBkVH2fA4KurJxc1hMciCxlIYytxnbpFgpv0Ei9LD_3MNmHQkJ5TGMHn5LAviCsiwvqr3EYtLHKuXJ09wcVFdwODcI2F42mQDbNqtNJIoXdvbQ_VTGxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U51m7m4MdkMe-juM02O6-D8fy-PvL4eKLtrK3dmGh6HR-8YIdYZGPhnsneRSYBAO8cZ6LQN-hTGeuPGBH0uhZ4hHWljUGwi880Z4s6dV7Z8IO2QVbgCvf8N--OKQrXHfBsjjqj9iU-YZPKSC6mM1Z0LgnKtO-qgdeKhAwmQbB7UdKISeyPVfjly5FDq4jNZuSvJxdlyheijIbBn018Pe1fQ0tyicyuBdqsqsaw5bhHF2IHM7OU6MdhhbQ0KGyhQL1XKR2Gt8cIRo6qgx4qQsFGzz_Z3nSFiO9Uj9JoWB2fNRKVMOK6ZtTAb2S0fJnq_eaakMz9eSjXNe1guTyeO7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6k28ZIqMmtdGh0KoWU8AGORejhiVK9vQzy5T65b_CbGmCkd6R5kDTAYfFRvKJRrzU8N0nIGAZMcH4Fi-lTvPvGwbBZ3sFKA8nmJf7QYOGBvRXw9mpA9S2efsdNTf3Qk2h-rgIW29c0UzpeUobpI201ygS_0qeE0cmbfSX4d9lcon_rQeO3xS-MKOLgUQNE67UeupAxE2rj8Z33cxrPN2RwX9EF6Q7GsX0Mt0sKFCFJD_0a3j8r8Z6QWQO87sa94EeC3fezBNH5IQpWSDFzupJD0kea21mfRXGru16lgIoSf1wMCsI4auG9yHathA8EAajCeTCQPHfEfIJfnafU9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8CfG3rHRe2EMC9fCEjTuuaeqjVh-E7eb16EGM25Tx1uA8yn0jdnDvvpltzyNF3sc22XmJTAqAvImnlw3ZBRitRAOND0nSlmKso-0T1Hp5aykUUY1mTc2vGOngijd5mh88jw_f4dVTSlAWs-0HfToypTzEjSfTATLQ-CMLPrhRV_WyMRj1m5cdcSXMGTrlawEffXTH19NngdnAFE49n_p9kvf_9PvSJKRjoUSe3ZEo1jDVBjOfNwz3PI1oRmTmJJmVxZE2y2XgH7TEEMODH5PAC1ZbZvfR0Atp4vy6Zqkwj3nkkhC3615c8zBxm9PUnuoCRPmUL96ISeIe3OLO5FWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f44FcAAduUO8PWSC5C2ZYKTU2YVo2bPJ5pweJ24dKAw8yGPNSQcNCy-RngJY67uykg_immrBLK2J1SemwES8wYFnj7ChLDgfygCEe59P5nUsc-JTGNJGAVLlKlhwvUcHBHyJoUDAdQtIlbbVod9GI79dHQqkZQG-kwNxP9GthukYdH1EkXOtoypQ974wW4FxWmmGJPUpSTatSygxT0dd_A1LUVyRGGnGAT0kbl0t-CjCfjnes2nF-sWFPTwU83bAzb5t1bEHwPv1mtY1SVq9LAm1WlKAH66PAImh6Lxo0IbIzXa4GpeRHMkSjf6DdOCDl4v6iAmXMYv6s11gb9HHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2cYjBzDzB6PMPFneFz0oyYKyMMeCUGCGHP_TmEPT8UQRKQvIPshwoI5LNrtIswCtXFrUwAaigdVsFhLewCAiJW8lDBx0edhZ1MHhttYFCE_jWw1uX90X2N42hHXmF3ZletOPNQBIbacIf5QFqaZ4DP4KI2Q7hIgroH08EMizz0iJh5bShQulkaVtr__YBnAWH7vraUUvdYrSFvPLgq2IWUPgidt4-cQWhhhi7Tt0ZJpz2yIAWPChUZWIk6T08arV4GVXop0bI0WflY2scA_mkgzk9vVe7YoA3WYD9YZjRJeHKRjc1O8Hsw-b9P8c56_6jdIGAjSAj-wVG2kfOpiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GmIREmF1jgP1ZQBiPCR47zYJbfIcAO7LNXePXp7qWNE26kZnikG41RLwdMexRaNpCNIGcKM0g3MI9CNYzPowUPYp7MFOQIBlAKv9KAHcLGicw5cXBY7HHNYe5IunjAQSvkSgTB88KzWDyMu_mAhbwkt6V32QTeriNndh8_c0DHSUEmKDMiaSo2KfAxqmCtJv4NoP0KHqG2O2Bp5qPTxEfLNNXnoZMu-qis0BCRjMgj5oBCkvFiZbKjErakubAZWuOsS6roxXv5Quzn0tHzTw-JqD7SUyZn7RXf1718fDY_1L_esKgfn2V7daaKqOfmujSWjMATtNd0L0ydsJ33NnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HNOZhoob9PFF0aPv-j-uPakCvE0sKV66bw5OwjoFEIZk0-O_WB9zWct-Xa_xX4di_n8M3lHQEDp50qGhM5R0nTRXIbSy-vDbzchBCOJR6WbFA9zKYEgrBn2BCCqUrrHk532Bo_SUDBfj2UBh1Ut7aqGElUmeNBN8w3fBZFQdAPGK5rvKpgFAfOwLt74N_0lFlgvwHV_qXBwFy9JUPKt7THjht4ggzK9AkRcb86xOWyga5ZmWCAZCi7xtPSs3GffBZTiZUJDNtSVer5KHJ8-hbHhd-8gyaNMY2BfT3-VBq9QITpryBoeGugtxToyY0STJ_B5q9WtgH5JCiEO5i5PHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYrhr4_34v-zOcBUkEj__AUeEXcNSY3i2sWrkC3lQ9NaXTXPo8mhVKUEa1eAeVmDyoDzwXlZISsA3VF1TIcQ5huxCKX-krFzq4EsrxwKooInyJiHFfabfOfhLy3aKi-Q70ep0wimDqoua3DItsoJiwSZ33e9bHaUTLhPC6nV6mfcoHIb4G-NIMz_di3OP7yBhG1cYawcDEJWtXUzVTU04aemlX6k8a-DRNxyadfOpGei_9a44lr2NwNn4g2AUetvjEkMzWSxeTPN6swTfQe-LlJKMohMN-O4xdy2I-qOE4UbgD1RMSl8vdtg7SCEmISU35mPO3-9pZYveQboPKvaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BwWBEoFR4RBZu6BGPZqoRaGLS4vLDme3WBflKbH-q8fughoFGEVNIDG6KBpuOz3I3gXgaxroJTE1OT4hGWky7HwNwwphSNLni2mE8HQXT_h6WWqYbIRdWYcp9wdtMv2G9hHHWaGX4lI6Tu9do6k8_Rl59VRiSVDigikk_-7DaAbiPJGiCofFHwLC9fRjn0M_jm3bZb-CXiwEWp8SeUvmnE9Ukf5th4TvWpHDu63BY_Bq7tDNDjAjuRxonZjOiw8vONNi1w3z-QrzoMbyylwwV1KnZQdyq6Dd9COKmlKVk85alq0AdQW5N0d2cfy8a7UFY1pGvZ-uK54Eebu0Yj1jrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VE9xNqR1YJX_0tk-xNyR_XyXI1RqrjoIZHTfhI1LR0SXcg6MVqwJFimRtyI06iQaI46zt3c0YHjgm7KEHgPVlh1fMalF3y7Vl5VbUrbEdDlCGkAM2KhD01YfwBT_TeyHGcEQN-XVYz1BBiFZOn9h7ZcU-lInjQapN2PsAuGJoAg0u3cBXL3bDg0jcGK7eXpekv7-8e52-CsAtriLFUSDXiFQy_Y4VzHsvznZcSyTu9hwUa_Fp3uwPUZ5Ld9Fh2DKAaUgipzH-jDEepiUEo_PcXMU4h8wC-JomoyNYsGl8Hnsr7VB8XXD25wI_k0i3tURN8otzPNQsQASrejEKKjczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DpQRy1S3fK1CcvHDotdUXtGkxTiSJGRWj5iCjkZXWimUrIUg--xJlEkb0bKWJ1g8z7nT0fj3eQRjDKI0UnDzZSmssxkAHwKmaPVvj_tDPJ7imrH02nl2jeRHqAaiCVU_dzAFb1SvCb51AiLB-Jb92C9KZu83HrxemO7kqCoIPXVrW9GSJE-whRwfS0Uh2KLuKjHeUEiGvGIS_JH3y7NQcyJNbPohblHElI70WbATNCr7naLwBjCFRFaJN7hLD61iUWyEFGX33FXWJrsHKqD7TdDZkce0sMr4ydUfRrAsWT2xFuQmJMMGDLT6uBS22Ne0DFoyQwSqxVvBZYMWDhS-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGkJlTT_XGy1aNkoOuCX01aB5pUZc-Zmt3VtWl4U7uOk-mVpnjkxARw2v8kuUeIRc0tZr6aBaMU0CS5mzEAkewB2sz_TVM5gtIbQyk-tAkAEFWRcuSikK_qPFSzTFU7IoqMaaVbuJBEaiAo8P3ua20M2rpQI_Z7wfs2cPlE8ojeVF4P54LtnsG2D_Z94Udcj32FvC6lKyqwLt1sFbOqmBaKmeP88QGIzWya61KhgIGDcKJlwSknrAFJqTzf9FwM9y5UccjdyEMs68kRAWiZoTzGGGLHpPwMiqYA94m9GS-dY2SRppfgrwA1ZfVgLp8PWPG7QxVvVNdSzg11ycJWEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poq2YHp6uikiXJ0uda40PX1zUjX9e7PG7Z06M4essnNuVXAUKqC-dLNSPh60KFmeO0x-VQBd0UeqHYZ2inOyCzCfprj1EXfnnZepYLXU1yAi81AcYDiXTMmilrtnC6gjxbXPrQO09kYqr_xJOH5631lFaSi9l9VIIHDl7aeK9cnfbbLXlmPBNmZhj2e5YslgpXz6timynbpIvNfIGGDz2L1Wt9Dp31RXTF6etftZd-MIARmFmF-ZxLzQ5psYhZ7aZXbH8r35LxMnKmQg5oXZpf5wEunTYqSs-YH159F-J-i1Gk3WEjtCYpIx5_TlrWlzRCWp12C0lvAmBap8ggzOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPyWuHCpKbjSaHVlb46ZfU8VvHO3JE9YbSt9uaoSOHZAeB0809alZgFZpkVzP1kAEpLU1mZyHv_OUptch-7qyshaZ1Ca4iGzYfYk0d6mNacgqeN7a4U4FId6r5yZw8y_Yao6fTFtdAmcVGbmqE_MJWUCKgkBCUYvc0XEzKAMBfX3fdQZNhPPXtdpjK80gEBs_JpcSzx1uTfT32mkKwvqQHRnErN4hqcd_QcxWTRMYAvDjLo2nSe8oMSPN40xkktXrhaG3O540T7QWQm5W6NxmhzSoajljubnzI_jCXV9DEgKkD5n2SjwISDxMIkHJL9TapRaNwTjQSPu9ZLDON0RHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BpzXjHc6aeZQnmIjXk8_SlFWzNR1XANXreJcYlJH3LnV2ICiXUuG2aKGQRImqcgsxx_6dfPTIQaF1ZPAlTz-ge_uWrbOakp7-XH4CI3AQPiVy2jHavY_t9Rs1-HEXtbDZvwq_SDCUdWMDunBa4U4ox1UQ-qeSIJeDFVf_owmaFHR9IF1unCCEL-SixSOS_M7WztFyX4tjpssY1nmgmb-43IQbbSRL3pWR7mHJkymc8cXtG6VwSly8qbA1pGgXVXnv4Zjt07kVtw0voD5-7KZZAv7GFBEwutWM4a0pbKkeCqhcg0JWFYZmQmfUeRKHg0rsFp0TS1_E2rRbmYTjM-0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1QFrUz0c-p5VV3ugH0cok-h2_dvKBRyvUATVxUKq2nzQXLy7uOqJQY7Oja9G4MfESR8BYMA9nyIlEG1rYOgaDFJny8OLW20Yn2MMBVHVJnxW33GDzhrVmMokf2_ASf5kWmbVw9JuLr6I7rXMoiPw7lYcfUKVc3W_WavisGOFj9RJcTTSl7wMUo1SnhgsOyVprejMNDtFtV7q5d7rFslRFL7Yv6FSgtnF3xwl2EcS2dXfsCXlPL3CBCrPY9rV4_GL0NLIcAcyuhwRXnsp12QjkbPy7m5kKmwpUPAKuRGSveseb3Mm8irzRM9DVs8HzKc5afa1YVDDz_AJDoGuUIX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glLBbJqj9eo6tKGo0PC1SSYcBLZl-6NFP_erRFLxavccv0huMIyOo7HopHZXSbrFK-mIiM1BAlRDKZDB7uu56OqfV77O1bxvFc74BmOob2EiWGLjuZ6vdpHJqDq9pUOBBplaa8Y-peBu9AJf93c6lB_VG723W0cpndEB5cqaskbuG0wR5vm4D_uwu8zjcmnpDp_UNawO0d_QM-r4fPDcIScokpWpY52vNBd9SUApIM3zI2PxU4K6_ennTlEIz1SRKT9MszPlUA8eUxdyDylCGT8m_fFCThWx6Erug9ibmi-QucEk6rM4bf0_6fQsM1Nja3azPktHye3K5x6LgpxXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XDuP3cESZgoL2lqRPgeP-V4cTU81nvSdT82Ms61cv-DBmRQaGa6g1mYwVB14cH0l2cdTS1L-EaZYfmEkhrLfq9n-2qzDctUgOiJmV0hyJfO1sC9dQgpimNS07boClZZaOdGwLVNtBxm85Io_6ypD-DuB1ZZf9tpXe1CruAwnGdLJRa_o0LSD9SxFlVcoID6ysGR0Hp-BQyzCH3JOMjCTnCk-VJUPV6uH-RCe8aTFTL3qgREMjoKFQHo2_YBrvlRO1XoirCjRWc0oQEXrj4WxAKSESSE-_3ufWvA2svjdceyKE33U6-RD-PEmxIbAIemja1YG4lLO5RlAIxI7OxuzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WXFsktdln_1ZOp409GAHRoWnOt-6eCMjcM_KrpeCDG1Ydp-TfPprwpqmgg4EDBNvLuCIjV5VuGSu-HALkPLEJKH2AxXV1E0AgS2qVs4WM4fcZL5NJVweiEyAjRhOPmN5kxXiayNMBNOGsg16ELDpYrEdfybPlTPCkh754vWNTnBevD4dDznaWXQG2v50Cn5EpQUDDlLDIBz9a8F-G8mePRrwujq79OWJUFdf1iATh9-vo2q6ngLmNcWUXxrG5ghrbHu_n9gZ7UN7QVUq00Y0b9UHJNSgRzqa9k4ao6l4wQuuN0sbsled4TOHjRQVS26QsNmToobqnC0eneiZF6dGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DyRC-tgJWVVMtqjTRJmJI5lXtDr5Wwnss49lnHt8CIXsV0D_0zn0RHIL2JWQKvXfIso3g2fIOl0iia6b91GMYDUIVHZnKuy-jwZEFBG09APIYF9YMUArakwP11j1Wi6edx60OAFSvW0y9uF5DAn-juvmXsktOsGxk8tRajnoCueXRXJhKTRDlvgBbv0wUNtfBKpuULP1C6nDl6btWDDmaUd0gc5Zj0E6Tvzd6ZOBFE5peiE9QNY4l0ERrGCuUw99e1hYMla1hw4fJZFfbr0Qi3YVDBEPcrompr04jEm4jek5Y94l_o6BjijxTB-nnI6UGzJrIo6H9H0IdyXOK-LsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tm5JdPkHMKxQ_XAR_5e3g_5p2s9bM_t04rf6D8da_Q3UifCSEHQuYXZy8dVNwGVuX2sIf8gmL7pLRNHKBhMdVPReXBw3llhrzk_AOpZayWzWGHPcxfbnqhgy_pB7p0n0pQAdVFkWNrkUn-uhbEb56drOrndgYPmq7E3-R0JvckB3_O38lw-8qJuVfoKabPzFMWIWJY94fdQfsgHLlQaBVHq-T9o0sYaecnlUxPiKe91Pvy_GfdgrmmuPnOxuJAvpZRCwOIgZmoOuk1ctchM7ivtq-WJQfLGf2ISbVZVDUjRLbZtWoyJ5zI22u6YeUatupTNI-VXElM3N_vlwhzz37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dm0ES-uNRRG1q659-nj1jiDER2c57AP2uzFSYXfVGBCvm9T87bO89Ogi3iTP6RnjxcUmR8TPLSBOvvcGFDJEIa9MCOjeogcAJbdHCL3k7tBqO3Mu3HJf_60CI3ympZzYU4a6P6C6ECIutWdRlN6M-QlmSd-ZLdz-NN3n9RNJjb1TiWj4HJrqu6HGWE3oYpknuicI0Eeo05WxmnzMGjhAe-wlx1hIe-l8ef4iUXETCMaEUIc5Dcz_rRwojfMXupsKIasvwvjZimQ-fcrRyZRF83r2RcgCoFlZr91w3H8hSyK5oFJ-Na7BuVEU9p6kXH0mIUve-8Ud32pYT_MconM7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hkYNxtT7ouixsG_uAmAvY41Cxx-9oyAeu76us1HmOTk919VeXLjHWJ1HtMkrztib89jOyM_RxKiKS2dWhI4M7H1Y0F2Y7m0HK6Lpj-EVrOEs-aNqQjJWTPvJywCywZvRKUtITXhff1HAH1HX57sBz2Ta3z3tYGaoo_agP3_58aMtxJjIU-1XmBo77Y5oi8KHBgHKJ-O-7oahAGFuvV9slQGsRc5h8Ha3liPay4vDZRUYxl1WvZ4s0W9c-LiD8RbtIv1EdxaHEH-661gzSqDxsDxNrfW9zIViB1US0OYvpAFdn6ctWz6ST3-k3heEa8RdPYnFgtaK0EPupfvzdh-dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBIjCaEA9iDFKGuumLZfmJ36UXY0-u0jfCPICsw7U2xBKGDTwBsZTzxGlS8ToiNwkHWPtyREThPa9y3eai7VTs_N2tkNIrLpj14h2yR4I8bhjqluRu_Pv1tzaBnplx8WVnO2-dDPGsNKlgpcyrhCU-ugs18VX2vYSfx0xRLF3XzHpEvnfQNOtGzDJgBBjUl5kp3Vhtkufkv-I-Hiab3k3efzLHyDfr0aMb7bkt_emFWjBmYnHThUuthRL94GE9bMq6q9MCrJJz_yO9TSlHXN-hLF2NYE3KN73LRIY-A0WOM2itBc3ofk-tk6t2Mdug4L1JkSDJ-0SkfLXocon7iy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJswbGtKnQteHCwc5Fa-TArWZBfmdn-Fq-sJlPkqpe8Swmi3AA_HkFFzgO8uUP4uhEwlKH6rfDYBgxEo5Gof2YPQTCK36m9aCdLqr9Bmcq9aWDj-Wd-q6yFW9byTPoIqvz6ZH94VZ7URH-c38t9b9EKG530JrWed1uw32FsR75bt4AQ_KCE3ukHSHX3XbOwbPDmWj7qU-ato91EsV_gt7fooJp9c53qNM83c8j7xKAFzOEnzLHtKxwTrD6VKIPYEyFsWY58s631RONmPYS0VAD-3wDtUI5UZonq2wPeyS1diHaUAu8f_B4too6Jb5JNqXrSwUgaLyz5fvmWsUQWLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/obFC0Qi_ZxffXi17yVem4wNicSckXiZhL3uq2T_J9NfPAJfaR7K0GBA2rjNN2JKGp1xMPX9TEoaL6bAzmkbXh_6NquTjcTQXdP62BmIYiYb-zWfIxhUU577Hv2d0DrN8RdmE3GeP9KfrioMyf2b_DGtLlbbfHBIfSIknLNpo8rq1OH4mHISgyH-8uRggJRSg94zNRgxpqtFYpcHGIioZmM5Mmw9AdCDNtARk6rM-b7PrurxM7eH54aIpHb3umCFCKUibQC6h0KZcMP_lBBnVyXCi1sJZd3jlZKP7ziih-kAS0oBpBm_HDUWG2o5nN5atnGkYUk0_AAzhvs-Zd79-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k_vKtos5RVokd3ofY_KjhW8g8BM2grHOChWqhyL81ZT2LnAYKBg1qSEBQ_gebxiWFnMlnr89fyJjBTXarHYiS_P4TsLJnQj3_WR8bzv0vC21dmx5pRkkNTy-VNrtGObRZitOqHQQitVcoJMNn13-9axMsJNOatUjX88n2U8ARVs2ZLVxbOJ9SxMwz3fIXlIeV4GPjYBq3vORX4z5DQdWgf9lTrGXSc0ofr1IxWaGEHCXbUL2A5nlsXHD2c2280VSY_xjQXCaFAQUsotCZYwizvzXgMYr19uZ6Fr-mel2INw96A6xvntpcgR5GJKeYT5NKxh5EXT5CHhT3tnFq2qU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OEGdGhiWirC-RlYqIVfhaZn-5pXiSqHbY8F8HggUJqYb_QO6u071BetUrO2H3Ena6O_0bizBKQ7a6KMaoT9Eg3dNAC3WIMtCc_qn2BvoK_qGlrZkpURATbocMoEfzri_J_jSTKuqpssL8dVePh6ujTnizW-nFDuhvf2ak30qJOoqMUyIWGfjwvYeVAq2gy3wQEEcTJsrcd-aMWTJLT_Z11QMxGjr7LbkJHoFeCVz_5beNiyhvqpm0Ajtz3s_pmBkr30VoMtjN7P-rsSd9coukHhOYVEgMX46ZJMjKG598iwNejzlXLmHOvYOpVJcMjCrsfD8XRgMUMXRYEQPyisuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JlXdNnXrAIId7vbQOkP7cZC10y9z7KALNUOkXj6PP-ymIRUuuCYeURWaaX1r_nxlMY13fTmQi6is96Mk1977l_IXzN49arjRsNNM7ljrrXa2-xBH94onpeALB4oP-QyyzNmrLWCD5QNrvNMInUq4lBZgf7CXIPb8Wa27Nqm85uoP-894wRvHCMok5Wg1RK_ZqDzWOlHRHohJiiGuPYjy4oT4MZLjolQPdIWWfEDmU9KFhc9Fw6e8pMTeegLBHzSvhhC0tZryles3rmtI7ammORfMcpjiYOdTGZatOWoCJPHLr-N-VHe4E79T6SoGQYdEFowHVwaQ_bl-RE0VbAxxug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpfWKTBmf92WszzrsPlZNYQWzaymEpHhkbTRPW6eZ5KJL7KL7py1qQKqJbehBWRAz5i9mKads4c53MeXpk29wE9x0qZHAeyliud0tUj4sI6Y9GBbG_y08hSgd3T4PkhMoPr3lRIvbE57vHMk-LdmPS_JrzDtJTyfi158Nc364eiZk7re-m_DfQRNUG4epxdGX8dEDP3ok0CTHIIZMuX1vS6IdhVL0erXwqLqf_lJISqrFYa4Gg_XVD3pxNLa18GpxFSTdwJIcntEWwzsq5vA08p6ir-qtZHgrAqeStOMXTx2LomGDJ-GQcSDo2jGmbd2CVgUPjQMFOWgnu38RiVJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ojvj9su39kcwm57dJecbsy71XXhxp0UYxW6TbZcjZwMrTYlMpCKP_x1ESc76i9XGQApYc4haqX180N_rdnpKVRnQ4deiLMq8kAm0WlLDmdZzDz5lqBoDRctNsL4FEsp7UivSLb_mrz0KMfWT3Vvqb_esYmeTBEH0WoMq4QcRgycpkSiUrjmKCDo_S0Q4IdNf625LBTAdq7-qaDa8jCpK5hCCe5-JN6ZvsJEbVo3bmkMrBXTZKUq1VQOVS7g4yZ4OA44D7tX4ufHjUPoCAhIJlRfWeofUJy9vI9fLJMiFhZhtQ5s4BsbfOb9zBCGcS-QeEiIYJNO1lJ8kiXI7mcHfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJ3q9J41JD_y9DXWOZcrggiHt0V5197fT9RjVVUr_N5uU3V1MO_sLKbQRk8-A5Jdm-eOvjQbv0HDQdpXLxcIxzmJZqMbJDwcZFHK-GCcZmuyIoyOABcY1NBQEi-aKaxX_vA7XDtN6T2RlViNC3JYLfMp2x9WyvAYjSfuYWJDd8gQyd55BZ_IdEV9E-K1-xy9BJ91H6gWlIazBXJnfMJPXt6uMzuGA7MATSMvPrJE-X5pGW6XsvYQjGH7xbYxh8k-JBYZM4W5chTH5zmPF9uDVuppVOnEeuZzRqEF_H25cv_iq1zy5y_On5XuKCMrpNI1yLN4W1rLo5a7YbMZpiYOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmvf0d9iP3XJYStxgS09jBIEzxTNcsUtghqY5AC5UDbWnIT9GiGhqWizWuu-RtadBpE5ymCYVGj_ZZRPERh0v50lkQ7r51Qktb3YAjpSb2RrSaNC3tL91PcJBuK74pF9Tx8W9nnvXOVrq_458WxI6iOnM6M_O0HA2UFu75lfm-mHi0z0EKvkLlvcCogZCh1suoUGJMdxppMnox5Rof7R6U0_k1vdmP0gtB4u7PX7FJWsRQEWObgVMMNbYtA_J0LpVB5QhyKywP_g8HnMoA_2k5HuMG4P_dnIms_kAcLfTpMuQWATH01NxaZcADlvBmnYJV6PGbZFfpTCOxDrDPD_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QZgOiPvGOaiz-DAs-mxeohOUqQUa4OOh1KkOe4FSyrxWzJXRF0sgiJAb4VIiVkZoQxSDR0jOgzlrY08EXu3lfnFm9ALWfd7wg6IEj-jCKAceqOwirNfYj0nlBvQf9j532zJHlJKbe2gACnzyAQLu7Am6bghosp5eU1PKb3Vjiygv651SR9F7T3ZyzstDh1qasRv0_bDSXPtahKnI3MZiAXevsA6lXcBq3h4l9h6IqaFBdDkniDi5Q1iEqnkOj-guyOG9RIYcorG3HCUx9jG85DSjOOPq_ifprC-60MzdfahZxidFQ_vNE3mQEa0CebbCSCSZfdVXqDBLgg6oGra1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y4IUTyLqhYMmrAD9GQ3KrgaoBr_4aj7ucjEoYag-cn72e-VlK3X6llAWD7FhtDT7CrgV3gcmzs1skrYSF-ckdnTN72Cip6S3lCFm91fibaq2-sYMxlsygQTMRtnmBonWKPXT5_TZ8URfmIsHPMEnLcWQyeHFtf4zw_IK4dcSXxWsW1mrSpFyG7pyQthvwjGkEZ9ME8JoM1osa22IgDhrb89PCN6k0sOhLZYxWjhZrv5CNFX6HOC443s5TaHdDhkXnLNyu40TJQrgMeRxWQGCHzRh_xU5kcQ-MLfIy5AfThcRcLraCBlfAJFrKopfMm9zeDazFa6nfSdQk5KANlSCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1KZYPw3A8St9r6BONEHHod-2a93-uiEr5mFTBWhmbsTr_eYCsAoo4AQUKJgMF5h-xg6t4w_f8Kw4DYjQOLpl-0w-FUc9j9RHd5ekES5TgiJK6f9VC3Wt5fiD-qeOsEy_J9hRMGaZ1KGaR5e8bts73d4RTUOjoKLMM4aZiHdzFYYdLywxAXEPpoTD-AJqSwZmb8gC3b5jWhxYNBzuXcN7Wjv5q9Sy_0IAFUG48ZPBT3GOAWaiKhts_-9qWFbGJQkStwblAwTJQ0CY1o0kcye9BZWKb2mTAYLz0S-XQwk8HCoyQd7QF2kroQ0XysyolUDgVPOH-Kw6hGrxzkELtKooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HWMhrg85jCxo6Epzc6_5hjM4iGBtUbJYQAEyHDnw1zLXfs5Q17DE7bfMGKZRqUivKHT-WAQ62b5ly-yl8zRNEXYSJYngvvjkE19NX48mCag4k7qN3Wy3CDkbgaje9trLCUFVxvub9rWTIhV87wz8aX-2gBOJdmxQh-Dj72dvVtevQuDuTyWeJFDAEUnP7NxNA6C-9pKXWJnuovsKEePhzBuuRGptNbZVSvozHsH_1Kc2pZvD35Bnw9BuSwL1nI4X9h9kU0FBQdPphhnULMuWnq42JqLPpb2VVCakhmFkUGBprH66jbF99j9dgYFDVRRXsURZ_-dkZ2bySIvTjb4KlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Oljj0HRKAk_J8SUJl_Q0n9sYxDo-MLKG7kf1OKf4jPj8ZGzBHoIjQHUBTawW6pCtYFxy8hs8VZzGUWJwbOgEqv6sN0wK_lZ-ehozd4vjtgYgfz07JYPC1WdMRH_Eqks_VlOSqFk_6xJumu4IKKZ8832V_-UW5kCPOKVW1L-GT_usMOyg1gdOY-m_nVI_aGNirjhFrXikMmog-ND79-lXXQkJM5qNYPCAQsC_8_YRfijM_HYZRslkm2pob26VJoH6aLSOznNz0icj7RwbWMnIHWmOAJ2MV3PaQCuRA0mcfv5ozEcMWhL0j75Lv3-VQNzzctO5Pcf2N_z7H6-K9TelEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTOvwNASKBBD6VWe_5zdYTeS26emt0hltXGGUF1LwL5asa4XHxmVGAKKkUXXr3fwvR0ZKS9HhlwOxXsc9HdGwgwZPj2UqV-m76gciylc_0rNzj7_00EuzyZ7WXnB5SCEHWMfvFiJjwr8uuqo5g188Bf9ZShqmd2jam8lckFhv--hzwPBvHYfIty4XkjA4LorQgGZVWb6VdblG-SNUSy6APTlUP1yJ-QZx3PKJB2dlQVy52HhL9ls_KKOl4o792Rg_8XwUgxYKfWJLYMKaeRCjXdf-jLPn84HFPUQxfItxyvnRVQY2t6Cswp-gokQqFTMxhkm2pKqsMLp0QjUj0Uwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cMpg9tnwKWaUZnw7m_g1tP99JEWpy8JkMRKmbyisOHwmZyVNIpNgzx3Mbhbdy7EbJxQ14H1rC3yOcsSJ3DUipWvYUVRPKi4QxmIAGZqSO2i6Y1ojJsvHcaxA98KYTCooVUDVpGC2ldPkxT1CnGkMag1RMSIwepjedn4QYcdEJyh24-YFJYGHb_0w3yaCBs-L5B0cuk9ipD1Y2426i8QlahW8cXbEORBXYq8Jb1m9plWABNv79cjP7071gzjc6C0AsGsZOThUAdbf3GOhKDchGqJn1TmAHe9QhGeUaQNXNN30xLCR-dNYNVt0cTivz9vQ7f_SEYrOvrhs9v33f2328g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwUyELeHRHYVhRn3QBHaK-reHUXVIAYCFZRVLLmQRKFVO1EY5cwJhO2l5Ii2adN3y_Lv-jrmi3rQ6dIvDT_0XhSxFblkR_h74UlMwB_JTzrUEFFmdtHoxjsFQ5y8T7YyYVfTK0uvFwk2IBW4DFs8gFZbu8_xK8VEVFE22uuYf9qjubODSKbpoPMf5tTKxp_QsCURarEAefHWGLjJPwp0SOdQnXXINd_FR-mk6IdsoOAzaGCnSJYNSRByXVbiYp0WiX7XA_gqo-AEwmR4iXVHWsIrmHFUzpmAXn9Kf4uhkZ_JOeJCjoquiirxy4oRd8LkqEIbmIT5zXO3ebcfhxAkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GyrLSSD8S9PJiSumiJmAJfhggh4bCMmZZWXgwy4XafqNflGc5aXORpHFmogyCO4Tcaoe9DHVdKpdhZ_o13fkeok9S1BP2rrRmZUAHcEWY7zUgUemqxvVZlWPSjwjvhOcLxlWZ4dM2G8n3hZVPH8ytS5ccfJUR9Qwk4JeCva1elagey1k5Kj9_3gnNWi6l2nM1BNSHu6Pq5SHPIjscMKQq9Etk6cVZYuMMXFGbcGOWqAVs0tzES2Cip4ET11Yplo8lxhJq9opFidbvn09bq-_fjS4W9coYK334HuVNK-OA4oWEPw8XcAFx_J3L0vJw6wE03u1G-z30y0YD3L6Ai0ENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GR1piazQv0IPVE36iQDx1rYqXNMBfs5FERx3vqiGZl2k9IbMiTDPozLF6hvfO1yX5NAl9BSLsK-GjA-9taaiWzDGnv8lV4w35e5tN2ZqtPiMUfEss1jCDJu0aa9Ms3epVS8uFUI_x4YyGGU-yXkjtwqDFQ47WfnU9BX7HaIR09h7HobeLaHPatg8FPas-3Odgjk7UNjr-d0DNz1jRV2OUjKanoKH91p3as9MQyOghQDrY3vMZx1Geg1XZ_pb76jGIZYSwWxb0x0T_KPiC41Jvri_ubn-Wn4WabGiXnfuly36v46dUFzmoGOod161qebyeM-hWzQO8QFg6RWGKkt63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gkCGVLjxJ5BKjhTdK5hO5GrjebM3iUVwphnIwa6OiXX77lHIjRMj-B995S_0yqNhNRm-xut8etubixlPW-8Pr9oGJs-82IuEmI633N_NMYf3QMrkdOKIUFwhRIhO7zguL5NiAsi4zwYMsIS4DC0q9lleGoqyV6G-LqNFqPgAVycf17hsGl03mN9_DpwUeahmyTpcQB02gH94RREj0Zktu1eTicwzWDJQAmGW1sBhv64pRI5_ZNJJcGG3Hrl6lI6CItSW7-kvPjXpBt2fvnUUGJu2iFW58Vb9dVnFNbgbncUDX5x9T-wBf99eNTeU2hfVEpBnLIVuevyNioUno5avjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwoAz2S7vz1sa_4Ww8gd1xYWDIze1pbkO0VApJ3HGDLcEnY_E33fK1I072QYIpWca6urvAzTXZdA0XfBJwPfJOFU2fd18q5vCZ4Ae9X5wG478fmjt_HoCV5K8dzMT8IMfUC2NkR1geA80YiCKMbf5r9VtdTRqeBde9CurGG7oQEeTho41lHsSBluWEuM7Rx_D3t7SPk3zNID2zVo6e7zT2tubfm-NfADLiJssvWod6dBkDgQt54ighk-YzzKux5CTZLw1iiUKHx5kJF87l0KzuxqI9HSa8QEBwZ7jdi7C0NUGD5S-8qkBN5V48DoUlqVihQhp-vo-2MuhfiDmzxv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VAZ-WPqfgsPMzJBGhbfs90jGc6unDTvXa5EWoCNPe6Bjvok1Gf44JIku7qcOa_EbicqOCsss8ntHk7gVaXIX0J8FkeKfCT0ogeRrNwSNJS5cx3FYZEzLsQDMtWiMnZu9BRYs-uTBUubtxQHxKR1cZNNn4DjN3RoqLcGbZFXiqobqR6Tf2EU3a0P67ZGz6bsQIi4Wzqb2umtKI6tw0waAi-R5R8ymJFIC7YaQzH2K6sqEGPx66PXo5kk77mIf75pqbq_Ou_op0HDSYZ0_B8-MTHPiwieH4jyrMmvMRsCflAwhlm_9PQ3DKbaHDXa8-GJuddzgYK1n8rSkHWTY5CWn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CPp9EFef21OsUf_WQeJua4HwWjm3RrwsH0su3z3Ftm9s7ewvfa2H4QdBWM4dONtqgNKGzeVdSoft78CcN7gkDHKQvB0aBryEY5xGs1-N6-M1B1ZEbe7VaCoN7krEM9LjnKDH-sRl0wLuBiTWAENhwIiLRMoTm_iwvTHoh_gvDET5AXNOwVAGJwbF0J6OjKGVoR800qymYCTszPGFYSTERfGdFZgarthEMmXBWM-dOfP2nDmN0rsQ3H3cdFtfhLa6dmSAfgK1f5I-t-Cw7HIE0Lc14TecSbbvb3NgBh0ofa1ieMJ0PgilzMq2n2Qk0sEEYCBPS0EsCP04kUZpq5xMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5oK9fLAsw29bY3oUkmtWXHVW_jUn3FVOPbCzwBO9jilQiu8mRQHk_xPDY9kUsSXc3cbQnDnxaRu7w0yPYNMUAQtUZknaPCvJb8hzXHqYmaEDMYAf_uYrB33_a4Jtr3LbYn7e5C3GaETI802QI7Aqs7unLcWT6wMk3yfD0AnA3gAFS7nOP4T7Vt5PsJi9FU0OHJZoDN1a2nXs_-LouKItnPH2tsb1vaMxFLUjLZcBGL0TZUUhx_Cveqpdvx8tQ6PDCLKouU-uFEMYR7Gnr-XXmYOVIb_NUXeqY444ir2KKnBf_YFt_rBrIBDD6FUHBCcvfmr2lBqLQvdHTWZn7Tnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7J3tQtYBc6cAT1-ihAHQprBolD0Qs4Cz4kD4jUECSX8WIj2YfUTMLD2yDvnv7o3Pw6mtkONPiMLxNvXRssM5x_MnQjUFOo8PDRsuMyipdDDLm4lTiS7tgPHo9D7u610W3oSNU1H3mHPHsmNPP2ToS_-guLdAQ35i7YBLGec64mGId8Fsx_UL9_NN4XBHY20OAOct6qVY_9g6NHiwzgSIBvZAj2GQa_sSWk9P0bzS8m8yVnc9ZeV8gna5M1mMQCjXzbnxBD8ZEcXI8zfmLd97FCbINiF64d2OSJSvkQjVqz0M8d1vO-LMOfNgewGg81e4xSFifrbisAvA4fS1w12wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vI-70Bc3A3p2cP8xDTZ7aDQPe1Mz-VKIg3LrF5mFf1XbjeVgM_N6a8ulGfRlM-G_S52Foo9GLPfmw72-B04BjZHZe5N47p0Kn4H9mBa-2NHNEJomG6BeCp8Z37DE41Ey_ebl3BOAUX0Cm5s2lPhc55_1Jtp2wdUSxfornKZZ8twoBvhdtAUqU2ioay3VR7qZpdPP7bHt1WxFZmPRMOYzdEMH_9d_YQb23rfkwr6uFqPW_1gP2At2MwroWKP0iDHmxJAEP3tzlxA1AkULHgyQdM-M19LbeMVR0Cqnx73OdcyFnMX3DTUSTWpZ5fyUkJQ8p0YUGsi5duTVY0X2AgBFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ejDQ0NrbttrABfQ2cXGDuGs3kFe-2rRTqMWoRQDo0FS1WvS0QiQJAKj1dj82_pGy_rbprycHFVV2fneMlZRkWpgkdENDTnRJXAbLgUGZbeqwxzX2gbBs2I7xz44UfNqwYRbXorei5EnO0OV_odlGBM_i3mYliI6c5LsJn9OVX3NvpH6UK8MO7Efnubh6qPX0EpkFRrRz2u6dyfWQvEXqlSY41RLbWPMqeiIXHMZ7AKntZUt8v6IzQlPu13LXhRbuvn65u1TOJPBqKrUtwqICkikQ0IMG5KDoFrq2LP2M11jXNNng4-B1PdG4VQ3YwVOatTnCsjF6lvFiPHwX0kHSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZEg6CnPWON9ElUPaQHaAf2QpBicUw0QIdkhhwH-qHuIM-mEBVxlQiShIvrdyIITaYM9dQSjTsMvfJVZF8NnX9U144P1as8XYtcOdFH2LctPF5ai_YodhCuUgf3IqwGK8eNQwyKXK3xOpfUqmbTmFxeRr8kNvzk_tL5Mg_0wmNLZk8WpJbkMOE4TUimWWd5BXsVz5cO_FWYix8WzMzRsZ2qJK6ImyIlAjjg720o4JEQN-cFzBR3Fvm_8rrdD1D4VdwrBvDiufWDXnZSnmR5BiAfesTo1M0NVdxlYbKNR_mUsz--55ZEcOzFhwlggm3ZpLiYdLvaIZtVEU_4RMsKWgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tLQ697Ke2ObZDw16ieJUCAVAMuV0zMjSu3jhzSHPBVyKCUyIce9olrKe_T_YKhB2FR98YG06JB2Zv9P5YTDoEJYkSLCfW7M9wCXlqxg8TbkXpWbIgT9KpeZqVV1qev9iGyy8-4nsWuVkJ8auRv9u1OPZ60pfMh8aRGSQdzuaHNIeGXlKiSa9rXu7IW5Rm0xfmfifB6xzPDicMVycenVbvv40xYuKvbpWwzA4HKZrJUKwZIQDbYE7CrdQ3ENKJHhUwk2ILvn3aMy0ELfdDA8evLgzCztxOZt7c6muDqaq5NOsUuI5Ua7A5-WmZbHEz2xdwL4QPtk34jatoNn06yPKSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i95oCfe2uX2oeZNuiOaThrS9oA0f1Q2ueWYPx_FEl2eTLreoOyQ_61L77YVpHapy_5ShgZrhp_eWfrqZz89Xb3wbLmQlKfxNiY7c1g1fBf_reVrV4qQUg9h33xsc7UY-SIuBz-ClFHTNWy4r2MnDjbjEHg6SJD5M-Zc0iRclXD5YPf_U0AX-ZkadOGs-01rtP23fC4ZP2-VVuCU2u8aLDWpefJ4mgvhkZ-Lg2iqmP_2xohoyb-cjiaShkTW0ma7vtOEfzMe8jd80cQRfEb35OkANJLM-Vckux-WaE-9dz-fRfuXXVQew5rx2mnnWemEyOHxRLaLIs3uCMR9KUNTpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EFCG2xyI5nxJhdMn-bQ1YRO_52WLHjOTtqnSWmBHT-SEi8Tk54PDeJ26i4QYoto4_73D1bjT6WLb6AS-GM7nsnqHV5U1z5zkXhQXNjWFG6JlkNr7Qpdf_R6X3TlmLUpg9vR3kRgPHedauncFD-MULWJDeQJIVydlJtrINri7sf39QjE-ecZ-NfPhkaj5AIiTHR4biP6SbdgZJERtG-vVhsE1_oJabv3nJxvRUeXtF8aCNzIm7EZXjlKP7pmA1Rw90RquFBVhjfFPdwLdmSMkUqf15WgCD9dbQ23KM0xT4PZ-pfS218tBRR5oKJhgpux_FlJXDs3AuoMFGovCWbPlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OaOZn77do_OoQIW12X533G0-bkfO7xkC8I63ioThY6rYotpmDfgZIPoDJxLNI2QRxEzJC8AAsXZ1dyjp67CLcw-TE5nh0P6OWNGAxVX4JxwJXMwz3-ot6-6AZ9dzLWhLCTvkv4cc-SGU9X7p4Wun79wHW3xwqc-h60U5fEgXGLnB9QSGUl7IT5bGmEcXed2IWlD8xjy8jqFHKFwCnw8WcksL5m2t_-txZXnInbeR3SNnMqFgmMV6AQc3UcXGrtLzpb4w7UBFtM4onb4-X1fRPIIBeQKjrQXs5sBjGMYfxlvb73vP95MuXgvHY0rAwIhAzN46RUq5XJgkwQD8FottFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tlbw0lak9uML5Og9gnQknXgpuhbKUjZ0dW-Bf_-Wy0cf9yxsykdR9Cu0iqWOUmVItFDmjpdZ8QPfSIjVGn3hjnGY9ANLnUmpga7YeKR4VVzYIOZwI0u9kmeCH8XPkKo0_FMeCSUdsQ9UilAuQlNNk-x8f4HnZLEp80QUAdo5h_iEDySC0HCYjv-d2oRB1OTOGNnuXiWYZBiv_VygNqBYbPZ-vC2EaHEmhiN4IwnV1sIvTT2kTgPE6Hl9IVF6kZ3GQHbKOrgmEyZ6oSytzaUgfo-13yJfNA70_tx-I1m_IiPXAp-JxV4PSrWNpzxVKiP0smWAfeDWrhPTrmurvDPwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcuJtUFIeuUIeBGVUESoAZoKNCYZHP2A7BFRqIVursbtGkZDeJvPBviYVi3I3ZDO9_bgsKeZwDMtRQJE3ObKfof_WS0nr0CKWrnRGYuWQOu3roD14rHGrG5jq4o8cK8Ztdk9svLxqIjvY_7ygGTpe-bfG_-FCC45tJjgcAMVF1E9iA7k1HECaGZPRqT8FKdjiOpAifr8xeBqjne_rBDr1UD_BLbJOI0Vygs-d45ejyoY2eDOdAgO_a_oKxHns4BVFogdmDVkAp7QHXSVj1DjB7yxdjXBi8FpmVLNAYbQozmiGK5FYishYmUZ4F2M43lyaeokgfrI8vY0F5XUCWp4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1xp_P2dT54iB3cD-hGCzYj3iH5OAzwnlt3RidqcxCYRVxjbrSKfSuIQa1ZZ6OD_TUKmvsRXYHPAeJObBp58NM2DJmTDyyfE3yazbhOYLF-5KNJSUlZtgG6CZiZeTFwG9KoxJxavHzV0DZuRziK-BBa1RgDYByHnQzRhpr4so4U2UrL9WcC5kzzQA9L--PMFw7yyymy0ogKrrqLqedhWK4Nmks7Tf8FjmqGKNg_5UvrHW779MzcHwqAWe1R6vP0qqii6X_26puMbfsNqABgee3giOWW1-Z5kRfcggeACF7l-NfY7Sv5Zgh3V-6FubIgbPesJeeKMOOvwnrUMS8maNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlLfrwMrw0gwBlskkKHjPTtgs_m06S3Uk78vDQZm6VFERjHJGIovVOC-uECBBaG67veEPdWCLI1zp7l0hJfs2wIIF2BeooRA5aLSVOGKSjpjNRQEFjPbUfa5aJkiEgZaa5wd9vMuFiGhdQVKrYb8yvOW7Wu_rFV6wS7BfH-5Jc_RAIAJNb5GrW7bBRnRfJflKHOnS3LFwCXxHZ93b12Wob82wvbrF0vlx41UBSb8UEz5xgo3PoBpSTuWTCnqYYNuuV9vtAs0fMTrRKIzV8atklVXuc9-aZSfP4wwVxTewfDwVb7YRlqouZHHdX131cty3oKeF2Hqgmk-X7b3hLgAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
