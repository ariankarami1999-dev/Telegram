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
<img src="https://cdn4.telesco.pe/file/HifdGUr5iOFMqBqQp8umEvMgm-667L8TAB0UNsbw3Ewr4nCM4InjwjlFrmfcbMpMFsEW-sdZUgEngIpgwG3AxpP4ZrqG59ggbkLkIKlCh7b3TnWXK6xSm0SAUEivQdDQal-Id0sJ2zk8yWAa0RaUu9GAZDiZNsT1F5smN62qFSegsmQW3ArxIOm6Oph8ePbUSUwuqhdHKN5TLY3SpnU6t3j2r7PqVYbGwsIE8U9mO-jC6JjRf9Lj6Cvs0DI96-LKk4RHncbF5r5lFPXf-Ua9ft-UnYIWDQaiWZvLdTmcgsDqKEA2pZlDbYFMO4MOVw1zo0koW_u0xuZUvnvfrXpfpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.87K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اورشلیم پست:   ایران پیش از جنگ اخیر ماهانه ۲۰۰ تا ۳۰۰ موشک بالستیک اضافی تولید می‌کرد و تنها در ۸ ماه حدود نیمی از موشک‌ها و نیمی از پرتابگرهای موشکی از دست رفته خود را جایگزین کرده بود.»</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SBoxxx/16505" target="_blank">📅 15:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpKVeGTn61aiGGMSZ6Zk5NvsKGlTFoAH-SCR_KrzADKoX2-zRX2dAWMMx0PKY38LL7srrT5c4WBGyn0xYX9SsctIR_pYhHN6_cLdzMMFRYBgOTOL76HGaQBCvu6m8nH7HTcqlGsnBtMUFopOHPP5UKKEA_XyqqCPHP1-HHAkheY3nhgxLBiDNbYOlf-jvfST-uc1KYNsLJ0Gla0-RZX6ByN6V2bZJ7bRjlYGL5J6IEItPjcJ6nifrkEydgNeYu_fa7y-7swqo43iHQCF9Cwmb8gyZTEWSFe2WPPPB__c_EhS5VyWikTRiQ6I-XAUo7dF3DV0mKr5URF6U3YfQmzQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SBoxxx/16504" target="_blank">📅 15:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز:
رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SBoxxx/16503" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veI5RpO_OntfZV5_62tyiC1dg7Eb4_gUZCX6DhbcBWoOrIlc2hQW7tYMlI8y9RtD-oSGoVSf42ixBu7hE9-AyEjc6C8ZEK0fVJ6U08fY7VhTm2W2LCADC2D9qcksR3qYuCPrDTYgLxNZO9EDwPNxVWUWueR4eZmWEQM1japFR-nkwwSprGUxbUbkd8aSkiReSZkNCMzgL4btJdxKcsvsikPSzcVbNdjV0Ttsz04Y3IJFVwY1FnP-ebjDBmHnTgiTGw6Qd8bD0h-x3WCOLcWoQyCxuslK1iTVHEs0agBAKuJB5iAAsTbLIiJv5qWos5cqs7X6sT7Z4R39IFgngDVE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
هوش مصنوعی "بله" همچنان بعنوان جایگزین چت GPT و میرا ، در راستای رفع نیاز کاربران فعالیت می‌کند</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/16502" target="_blank">📅 13:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyS5S2kM5aQrRK_mqRlssHIinWOxMCfICSl2tK2qTKMfNKQMHXXWPcHqKuiFW13ySoWhYxAifEBvlTRDdkzTi0tyTBzxaogRXPXlt0WmfDvpskl1IpsCn5kmgj7IcBzPMia_v3H7kfALeLxnS2_dI5Yz0504ZbdZ5Un1rB57UGH08aWqRWdu9thhjEAefwMRgqfos8_Y0rPwJRACJGysTmWC7XxAEyqM-7i0Qfh1IBiFEGQKi7_PQveMEYCcFfa9lPun_LpfDRvdbz7J-Cr6urZq5reerHH_JH_fayaS3mpk0M2mmavYBwVyEI44_ikl0xFBP4N4o-ezdK0HjbAKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ایحاد شکاف طبقاتی دیجیتال در ایران طی ۳ ماه گذشته
🟢
در این مدت سهم کاربران اندروید از ترافیک اینترنت ۲۵٪ افت و کاربران آیفون ۱۸۰٪ رشد داشته است
🔴
آمار فوق نشان دهنده خروج میلیون‌ها کاربر حاضر در طبقات میانی مالی جامعه از فضای آنلاین هستش ، به این معنا که کاربران آیفون بطور معمول از طبقات توانمند جامعه از نظر مالی بوده و امکان خرید کانفیگ با هزینه های هنگفت فعلی را دارند و روشن می مانند اما کاربران اندروید که درصد بیشتری از طبقات میانی مالی جامعه را تشکیل می دهند،  امکان تهییه ابزار دسترسی به اینترنت آزاد را نداشته و خاموش شده اند</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16501" target="_blank">📅 12:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛜
روزنامه الاخبار :  اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SBoxxx/16500" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/16499" target="_blank">📅 11:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🛜
روزنامه الاخبار
:
اسرائیل درحال برنامه ریزی برای ترورهای گسترده علیه حزب الله لبنان و جمهوری اسلامی ایران است</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/16498" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16497" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان:  تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16496" target="_blank">📅 10:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌊
شریعتمداری؛سردبیر روزنامه کیهان
:
تا زمانی که ترامپ را ترور نکنیم ، تنگه هرمز باید به روی شناورهای آمریکایی بسته بماند</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16495" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شرکت SpaceX، کمپانی xAI را تملیک کرد و به این ترتیب ارزش کل برآوردی آن در آستانه عرضه اولیه اش به 1200 میلیارد دلار رسید.</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/16494" target="_blank">📅 09:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روایت ترامپ از مقابله ناوهای آمریکایی با پهپادهای ایرانی با بهره گیری از سلاح لیزری!</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16493" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ریزپهپادهای حزب‌الله   فیلم‌هایی از جنوب لبنان تایید کرده‌اند که حزب‌الله بارها اهداف ارتش اسرائیل، به ویژه تانک‌ها را هدف قرار داده است، در حالی که اسرائیل به عمق بیشتری در سرزمین‌های جنوب رود لیتانی فشار می‌آورد   گزارش‌ها تایید می‌کنند که یک حمله پهپادی…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/16492" target="_blank">📅 09:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2pP0ybMucc_gnlcvplBydFf225lsT49g01DPfB3ky-Ok2VEujlGVQiHvj9wAe2_taG5UKbte87gdFP_bM1U9fB-PoXlg4WZ8Zap9DarxBqZQEWOzi4KmpFjPW5QZicxixKBYDcaLj70LcuTTrGAlFk2SuVwBmG4B7BnMpaltfM-BBhxF-ryQQs1I64OmRcExDQWOyf1PAWD97fLQBkWdgnOEI7nRAwXvKkR6FsHN_kfStkMkBBH7zXbbZtAzzgo0D_ViadeS2c5WsOECUraFNf4--Xgmr3GRR-wjhoT_ePdkZRu6u2jEgehD96Aop6CZ9xO8F0eaR3R7kTfNPJxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طرح جدید سپاه، کل منطقه بین این 2 خط تیره حوزه دریایی تحت کنترل ایران تعریف شده که ملاحظه می کنید بندر کلیدی فجیره نیز درون این حریم قرار گرفته است.  در واقع آمده اند تا خود فجیره این حریم را تعریف کرده اند تا امارات نتواند از این بندر صادرات جایگزین انجام…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16491" target="_blank">📅 07:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpB8vSu2dQfQ88He5e6zjXtM0EzwemOLHcA_MO_yoVGsXYTcv-AgU4XIzdIWJjfRLqiCsqmfZ6szadCmYL2IR_xF_TzPfcI6QbutJktqyR13LnL3kOUzapAEX-wPdp_zPrVJIT1j2l3cVotp-KWoaxAwZurjru3fMwOiMlbgUnUzr-Z-wZLTk35Msc4e9x3BOoj6NSkeo5cgq4lQGicxGIgkJCOrtOndTYyVpaeIkRYWZCEN04qUDYm4gaJ0tu7yK0uvpHIrj1PwtaT3mrc_27nI_W1Wl1scArGMfiaHC3AenL0TRnUUQXUHyoARfUepX2--BZPqxfnbCJWAHrBiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16490" target="_blank">📅 07:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn5fn5h1Pcdglc2TwxynmbASdh8HK-aYQckjuiGffsbYfAlGUGAw2o44RbkulqIlJzw-72zc8DYVFkRlQqG6sSCKD43W_OtWfe3O58zaKifq_VIy-dww7pYMMF1fzH2p7RzjwQqFGAo6QqNfy_1QJ2WrktrYH71OybzrTJI5TKKijHajPyTVvhKskAbNkmGbccozg7PIQPPJgo1wqV6XoT_7RbehEi4i9nW47g2d7QWsj_G2UebPFMV0bXPhyU1xomVcNQoeIceQWJYcu1Eta8ydrgmygG-ojrTLaqgAL9ub3aTf7n4ihrj5oR3xsPhXPX8X7aLCQ9EMfXF0rkxLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران، احتمالاً با کمک روسیه، الگوهای پروازی جنگنده های آمریکا را نقشه‌برداری کرده و خود را در موقعیت بهتری برای استقرار سیستم‌های دفاع هوایی خود قرار داده است.
یک مقام آمریکایی اظهار داشت که نابودی یک جنگنده اف-۱۵ در طول جنگ نشانه‌ای از این بود که الگوهای پروازی آمریکا برای ایران قابل پیش‌بینی‌تر شده‌اند و با طولانی‌تر شدن جنگ، ایران به موفقیت در نابودی هواپیماهای جنگی آمریکا نزدیک‌تر می‌شد.
ممکن است روسیه به ایران کمک کرده باشد تا الگوهای پروازی آمریکا را نقشه‌برداری کند تا تجهیزات نظامی و سیستم‌های دفاع هوایی را با دقت بیشتری مستقر کند.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16489" target="_blank">📅 05:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال ۱۴ اسراییل:
نیروهای آمریکایی یک نفتکش ایرانی را در خلیج عمان توقیف کردند .</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16488" target="_blank">📅 05:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
کانال ۱۴ اسرائیل
:
باید به یاد داشته باشیم که ترامپ یک تاجر است و اظهارات امروز او با هدف تثبیت قیمت نفت بوده</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SBoxxx/16487" target="_blank">📅 23:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">توماس ماسی جمهوری‌خواه ضد اسرائیل در انتخابات مقدماتی در برابر نامزد حمایت‌شده توسط ترامپ شکست خورد
توماس ماسی، نماینده جمهوری‌خواه کنتاکی که از سال ۲۰۱۳ در مجلس نمایندگان آمریکا فعالیت می‌کرد، پس از باخت در انتخابات مقدماتی حزب خود به اد گالرین، کنگره را ترک خواهد کرد. ماسی تنها جمهوری‌خواه بود که در پی حمله حماس به اسرائیل در اکتبر ۲۰۲۳، از حمایت از این کشور خودداری کرد و گاهی در رای‌گیری‌های ضد اسرائیل، همراه با دموکرات‌های رادیکال رای می‌داد.
در شب انتخابات، ماسی با کنایه‌ای تیز گفت:
«دیرتر خارج شدم، چون باید حریفم را پیدا می‌کردم تا باخت را اعتراف کنم. و مدتی طول کشید تا اد گالرین را در تل‌آویو پیدا کنم.»
گالرین، که مورد حمایت دونالد ترامپ و کمیته‌های حامی اسرائیل بود، با کسب
۵۵ درصد آراء
پیروز شد.
ائتلاف یهودیان جمهوری‌خواه، که مدت‌ها با ماسی مخالف بود، این پیروزی را به عنوان پیامی واضح از جمهوری‌خواهان کنتاکی دانست:
«در حزب جمهوری‌خواه جایی برای کسانی که پشت به برنامه MAGA می‌کنند، وجود ندارد.»
آنها گالرین را یک میهن‌دوست واقعی توصیف کردند و رفتار ماسی را در طول کمپین انتخاباتی، از جمله تبلیغات ضد سامی‌گری او، محکوم کردند. در یکی از این تبلیغات، که به شدّت مورد انتقاد قرار گرفت، ماسی مدعی شده بود که پیروزی گالرین «دیوانگی بیدار ترنس» را به کنتاکی خواهد آورد و این کار را به درخواست پول سینگر، میلیاردر یهودی حامی جمهوری‌خواهان، انجام می‌دهد. در این تبلیغ، یک ستاره داود رنگین‌کمانی کنار عکس سینگر قرار داده شده بود.
با خروج ماسی، حزب جمهوری‌خواه گامی دیگر در جهت حمایت از اسرائیل برداشت. این انتخابات مقدماتی نشان داد که در حزب جمهوری‌خواه، مواضع ضد اسرائیل دیگر جایگاهی ندارد.</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16486" target="_blank">📅 23:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرنگار آکصیوص:
ترامپ به نتانیاهو گفت که میانجی‌گران در حال کار بر روی یک نامه نیت هستند که هم ایالات متحده و هم ایران آن را برای پایان دادن رسمی به جنگ امضا خواهند کرد و دوره ۳۰ روزه مذاکرات در مورد مسائل مانند برنامه هسته‌ای ایران و بازگشایی تنگه هرمز را آغاز کنند، یک منبع آمریکایی گفت</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16485" target="_blank">📅 23:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از کمک های نظامی و اطلاعاتی روسیه و چین به ایران  روسیه از تلاش‌های ایران برای بازسازی توانمندی‌های نظامی خود در دوره آتش‌بس حمایت می‌کند. نیویورک تایمز به نقل از مقامات آمریکایی گزارش داد که روسیه قطعات پهپاد را از طریق دریای خزر به…</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16484" target="_blank">📅 22:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ در مورد تعلیق تحریم‌های نفتی برای ایران:
هیچ کاری انجام نمی‌دهم، مگر اینکه توافق‌نامه‌ای امضا شود.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16483" target="_blank">📅 22:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:   نتانیاهو هر کاری من بخواهم انجام می‌دهد</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16482" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16481" target="_blank">📅 20:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: درگیری‌های بیشتری در راه است مگر اینکه ایران عاقلانه عمل کند.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16480" target="_blank">📅 20:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#US10Y — H4  فعلاً موفق شده با این سیرک امروزش مقداری نرخ بازده و نفت را همزمان سرکوب کند.   خواهیم دید چه خواهدشد.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16479" target="_blank">📅 19:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wna92lO4UJYaSwWABzBYM93MNX2g6byTdiNDhjrsKB392sYDgiyRrVyDwhbvVl-T2FXbbQZUORK7cN-a241qoy33J69zT0xGfT82N87_ogCsQQUaUXDqrVXrUbc_5wy_Trmpkx1HrWhKZ9blSPkn6Zsw4oqJLRmvbTQbse7PcYQlrpwZEG6RRcbxSu4xMqHkDZ1Ay0eMYnTKdR3OIeX3_M0ID6VHfDahuAHihlm_RcZ2Bai5CHP3kuIhvIBgrzCivi9yyHiy42aopTWKGrKj9vceBnY4e-xJ6bSZEQirP6BfbZlh4w18q4AxQjgu6O_QlKXobv135YMjK06qPLBBAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16478" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3XKSucqj8Pm28Z8U8ZbFOl98FTJyG5SvOU31mZ0Xb748MKc_xj04UaPdLJdQi08MU24RQFW9qUHvlMNEI1b1eWalIqPy6_3tUgL6XrgqRg_UOk-826MoRmw1RWZovvvbpGreaSlsyp3yEsbdzogeEBjRA4Rf0cipaay80rFC2JrYhC7uvPEUFVgZAUzh72BHBZVKuam4dc1vdanRiSfkLckN0aYajHUownG4cHxlA60sLh0T6BjCpi7pZOyxAoze0bnP0PmHAcuIJ0k5b2_XZ294nlYONIM_72l_4gia1bMLx_-4TKwU3RPveXzhFj3PabWcyWh3_O-NtTrRDbj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ بازده اوراق قرضه 10-ساله خزانه داری آمریکا سقف مثلث را شکسته و عازم سطوح بالاتر است که فشار سنگینی روی دولت فدرال برای تامین مالی اش وارد می کند.  ترامپ اگر تنگه را باز نکند، بازی اش با نفت میتواند از کنترلش خارج بشود.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16477" target="_blank">📅 18:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗
⚠️
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایران است</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16476" target="_blank">📅 18:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
🇮🇱
ترامپ می‌گوید پس از پایان ریاست جمهوری‌اش به اسرائیل خواهد رفت تا برای نخست‌وزیری کاندیدا شود.</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16475" target="_blank">📅 18:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
ریاست مجلس
:
دشمن از تجاوز مجدد به ما ، پشیمان خواهد شد</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16474" target="_blank">📅 18:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⛔️
اخطار قوه قضائیه بابت برخورد با کشت خشخاش</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16473" target="_blank">📅 12:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16472" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx_PepMV5oY-OwJzIBTsnMRmk4ljBj-qV2_05CBAS8XEfmwLghyt9vYP4AW4n9dG_Ae2aMrBiVIh5Oku_X0Sk4-hLQGIRgFXHLdGhsTMcOnkcJhcL6xUSCjFxCNFKXlna9mmVqYOhnxMydkbOILJK5HdDYwSA53bJ5F0WATX0aD0kk-cwZ-RFBIho_zh4GtB_nOPQkX9R6Eb1XBJA2QyD2CQorMiijD6cGd68koRQxp7BxIhqWOBhj32vQkFiq0hcLrdNkESGvvfxn_alWnBBWPJ43RfhCC1oGfn0KXdaQIyLtV9uKmWEIciM-LU0Oi3DwvxfurGmwcwe_u6GxePaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگرانی هند از ادامه تسلیح پاکستان توسط چین  پویایی در حال تحول قدرت هوایی بین هند و پاکستان وارد مرحله‌ای بحرانی می‌شود که عمدتاً ناشی از ادغام فناوری پیشرفته موشکی چین توسط پاکستان است.   نگرانی ویژه کنونی هند ، استفاده گسترده از موشک هوا به هوای برد فراتر…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16471" target="_blank">📅 07:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16470">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16470" target="_blank">📅 01:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16469">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:
بررسی کلی
در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی، دریایی و موشکی در سراسر خاورمیانه بوده است. سرعت فعالیت‌های رزمی در جریان آتش‌بس در آوریل کاهش یافت. در عرض چند هفته، برخی حملات از سر گرفته شدند و شرایط همچنان متغیر است.
وزارت دفاع (DOD، که «از یک نام ثانویه وزارت جنگ» استفاده می‌کند، طبق دستور اجرایی ۱۴۳۴۷ مورخ ۵ سپتامبر ۲۰۲۵) ارزیابی جامعی از تلفات رزمی در عملیات خشم حماسی منتشر نکرده است. در جریان جلسه استماع ۱۲ مه ۲۰۲۶، حسابرس موقت پنتاگون جولز دبلیو. هورست سوم شهادت داد که برآورد هزینه‌های وزارت دفاع برای عملیات نظامی در ایران به ۲۹ میلیارد دلار افزایش یافته است. او گفت: «بخش زیادی از این افزایش ناشی از برآورد دقیق‌تر هزینه‌های تعمیر یا جایگزینی تجهیزات است.»
در اینجا ۴۲ فروند هواپیمای بال ثابت یا بال گرد، از جمله هواپیماهای بدون سرنشین (پهپادها)، که طبق گزارش‌های خبری و بیانیه‌های وزارت دفاع و فرماندهی مرکزی آمریکا (CENTCOM) در عملیات خشم حماسی از دست رفته یا آسیب دیده‌اند، فهرست شده است. تعداد هواپیماهای آسیب دیده یا نابود شده ممکن است به دلیل عوامل متعدد، از جمله طبقه‌بندی، فعالیت رزمی جاری و نسبت‌دهی، قابل بازنگری باشد.
گزارش‌های تلفات و آسیب‌های هواپیماهای عملیات خشم حماسی
چهار فروند جنگنده F-15E استرایک ایگل
در ۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که سه فروند F-15E بر اثر آتش دوستانه بر فراز کویت سرنگون و نابود شدند؛ هر 6 خدمه هوایی به سلامت بیرون پریدند و نجات یافتند.
در ۵ آوریل ۲۰۲۶، فرماندهی مرکزی گزارش داد که یک فروند F-15E در جریان عملیات رزمی بر فراز ایران سرنگون و نابود شد؛ هر دو خدمه هوایی در عملیات‌های جداگانه جستجو و نجات به سلامت بازیابی شدند.
یک فروند جنگنده F-35A لایتنینگ II
در ۱۹ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که آتش زمینی ایران یک فروند F-35A را در جریان عملیات رزمی بر فراز ایران آسیب زد.
یک فروند هواپیمای تهاجمی زمینی A-10 تاندر بولت II
در کنفرانس خبری ۶ آوریل ۲۰۲۶، ژنرال دن کین، رئیس ستاد مشترک نیروهای هوایی، اعلام کرد که در ۳ آوریل، آتش دشمن به یک فروند A-10 اصابت کرد که پس از آن سقوط کرد و در عملیات جستجو و نجات نابود شد؛ خلبان بیرون پرید و به سلامت نجات یافت.
هفت فروند هواپیمای سوخت‌رسان هوایی KC-135 استراتوتانکر
در ۱۲ مارس ۲۰۲۶، فرماندهی مرکزی گزارش داد که دو فروند KC-135 در حادثه‌ای بر فراز فضای هوایی دوستانه درگیر شدند؛ یک هواپیما در عراق سقوط کرد که منجر به کشته شدن هر شش خدمه هوایی شد. فروند دوم KC-135 در منطقه‌ای نامعلوم که نیروهای آمریکایی مستقر هستند، به صورت اضطراری فرود آمد.
در ۱۴ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که پنج فروند KC-135 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران آسیب دیدند.
یک فروند هواپیمای هشدار و کنترل هوابرد E-3 سنتری (AWACS)
در ۲۸ مارس ۲۰۲۶، یک مقاله خبری گزارش داد که یک فروند E-3 در پایگاه هوایی پرنس سلطان در عربستان سعودی در جریان حمله موشکی و پهپادی ایران مورد اصابت قرار گرفت و آسیب دید. در ۷ مه ۲۰۲۶، یک مقاله خبری گزارش داد که E-3 در یک مسیر تاکسی بدون حفاظت پارک شده بود.
دو فروند هواپیمای عملیات ویژه MC-130J کماندو II
در ۵ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که دو فروند MC-130J که از عملیات جستجو و نجات برای یک F-15E سرنگون شده حمایت می‌کردند، پس از اینکه قادر به ترک محل نبودند، عمداً در ایران روی زمین نابود شدند؛ همه خدمه هوایی به سلامت تخلیه شدند.
یک فروند بالگرد جستجو و نجات رزمی HH-60W جولی گرین II
در ۶ آوریل ۲۰۲۶، ژنرال کین در یک کنفرانس خبری گفت که در ۵ آوریل، یک فروند HH-60W در جریان حمایت از عملیات جستجو و نجات برای یک F-15E سرنگون شده در ایران، از آتش سلاح‌های سبک آسیب دید.
بیست و چهار فروند هواپیمای بدون سرنشین MQ-9 ریپر با ارتفاع متوسط و مداومت طولانی
در ۹ آوریل ۲۰۲۶، یک مقاله خبری گزارش داد که ارتش آمریکا از آغاز عملیات نظامی علیه ایران، ۲۴ فروند MQ-9 ریپر را از دست داده است.
یک فروند هواپیمای بدون سرنشین MQ-4C تریتون با ارتفاع بالا و مداومت طولانی
در ۱۴ آوریل ۲۰۲۶، یک مقاله خبری با استناد به یک سند نیروی دریایی آمریکا گزارش داد که یک فروند MQ-4C در یک حادثه سقوط کرده است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16469" target="_blank">📅 01:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpJY_xDci1CNXPRXrM04RHAxSKANiyQ621ut2G_qEbZGcFcoxI8sFXrdbcy1vgPRWdeL_Defty-VGwLAvE09j1w76wOJjaxILIlPaZVrTXtasJdJbKklnKxdubo1_ytZtM2g9tTtjTjq-BL6GUatq2RCUWru2cQTEl_PRHYeSN4zslXVqy1zjuwQAVxq0Hj2AgDPURCgXBzHftyWCLu9qSZ6Pk0NmqXTeKUHPasa8oB0H3lFLepDd1JJX8FSMXL6O7fwvYxPlyUFtiYEed8k5PTnIArySDTE67d4pRc9jrcV2__qFtph6gYqG0LOf--uysVdUCECOAoRyUHEoooc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16468" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خداوکیلی مملکت عجیبی داریم!
انفجار روی می‌دهد دلیلش نامشخص !
گردوغبار همه جا را می‌گیرد دلیلش نامشخص!
وزیرخارجه مملکت به نیویورک می‌رود نماینده مجلس خبر ندارد!
سبحان الله !</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16467" target="_blank">📅 00:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری مهر ایران: صدای انفجار در جزیره قشم شنیده شد، علت نامشخص است.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16466" target="_blank">📅 00:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد
چرا ما در خصوص موضوع تنگه هرمز باید در خاک دشمن مذاکره کنیم؟</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16465" target="_blank">📅 23:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ در حال ساخت یک پناهگاه زیر سالن باله است
او می‌گوید بیمارستان، تأسیسات تحقیقاتی و اتاق‌های جلسه برای ارتش، در حال ساخت زیر سالن باله کاخ سفید هستند.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16464" target="_blank">📅 22:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16463" target="_blank">📅 22:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیروی دریایی آمریکا یک نفتکش متعلق به شرکت ملی نفت ایران با بیش از یک میلیون بشکه نفت خام  را در اقیانوس هند توقیف کرد.</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16462" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16461" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔺
پزشکیان: بیایید اروپایی باشیم
🔹
رئیس‌جمهور: بیایید در مصرف انرژی مثل اروپایی‌ها باشیم. ما الان ۳ برابر اروپا گاز و برق مصرف می‌کنیم.
🔹
اگر بد مصرف کنیم، در تابستان و زمستان مشکل خواهیم داشت و این بدمصرفی به گرانی و بیکاری تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16460" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ونس به جای ترامپ!   ای کاش ترامپ صفر تا صدِ پروندهٔ مربوط به مذاکره با ایران را به جی.دی ونس معاون خود می‌سپرد و خودش بخصوص از اظهارنظر در این زمینه خودداری می‌کرد! ونس حداقل گویا و آرام و قابل فهم سخن می‌گوید، اما ترامپ با زبان تحریک‌آمیز و شلخته‌اش فقط شرایط…</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16459" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16458" target="_blank">📅 21:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
ترامپ می‌گوید جدول زمانی برای ایران ۲-۳ روز است، شاید تا اوایل هفته آینده.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16457" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران: من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.  رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16456" target="_blank">📅 21:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">معاون رئیس‌جمهور جِی‌دی ونس درباره ایران:
من فکر می‌کنم اینجا فرصتی داریم تا رابطه‌ای که بین ایران و ایالات متحده طی ۴۷ سال گذشته وجود داشته را بازتنظیم کنیم.
رئیس‌جمهور از ما خواسته این کار را انجام دهیم و ما هم به تلاش ادامه خواهیم داد، اما این کار دوطرفه است. ما توافقی نخواهیم داشت که به ایرانی‌ها اجازه دهد سلاح هسته‌ای داشته باشند.
پس، همانطور که رئیس‌جمهور همین الان به من گفت، ما آماده و مسلح هستیم. ما نمی‌خواهیم به آن مسیر برویم، اما رئیس‌جمهور آماده و قادر است اگر لازم باشد به آن مسیر برود.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16455" target="_blank">📅 21:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/16454" target="_blank">📅 20:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمو | مطالعات تخصصی آسیای مرکزی</strong></div>
<div class="tg-text">🔘
اقدام نمادین دولت تاجیکستان در انتقال خاک مزار «قهرمانان تاجیک»
⬅️
با پیگیری
دولت تاجیکستان
بخشی خاک از مزار «قهرمانان تاجیک» که عموما چهره های نخبه و بنیانگذاران تاجیکستان مدرن در دوره شوروی بودند در اقدامی نمادین به این کشور منتقل شد. از جمله این افراد شیرین شاه شاه تیمور، نصرت‌الله مخصوم و نثار محمد از بنیانگذاران تاجیکستان بودند.
🔹
صبح روز ۱۹ مه، امامعلی رحمان، رئیس جمهور تاجیکستان، با ادای احترام به یاد و خاطره آنها، جعبه‌های حاوی خاک مزار این چهره‌های برجسته تاریخ معاصر تاجیکستان را دریافت کرد.
🔹
نماز میت این چهره‌ها در مسجد جامع مرکزی دوشنبه به نام امام اعظم برگزار شد که در آن رستم امامعلی، شهردار دوشنبه، شرکت کرد. پس از آن، خاک نمادین در گورستان لوچوب به خاک سپرده شد.
🔹
شیرین شاه تیمور، نصرت‌الله مخسوم و نثار محمد در سال ۱۹۳۷ در جریان سرکوب‌های استالینیستی به اتهامات سیاسی در مسکو اعدام شدند. آنها در گورهای دسته جمعی در نزدیکی مسکو دفن شدند. پس از مرگ استالین، در دهه‌های ۱۹۵۰ و ۱۹۶۰ پرونده‌های این چهره‌ها بررسی و از آنها اعاده حیثیت کامل شد.
آمو | مطالعات تخصصی آسیای مرکزی
@C5_Amu</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16453" target="_blank">📅 20:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به نظرم با توجه به اینکه این بار نه نفت افت کرد و نه نرخ های بازده خزانه داری و عملاً توییت مثلاً صلح طلبانه ترامپ بی اثر بود، هر لحظه احتمال تهاجم نظامی آمریکا و اسرائیل می رود.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16452" target="_blank">📅 20:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت :  برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16451" target="_blank">📅 20:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr4AhivuKz0SiZeri1mfBRjKZklFhE9wpMmagjgckYN5vcBngpaOlrdTCCzhbPDppXOT63HX_DxH9eZbLTMSeGD6KOg4LTnhiuvyaDc7uW3jvfohy8xfbAN1rEQk2iIM88okLybUnRuaQIiKWj_KlojZVqzs1Ws8k1Yf0YbpYCRXAzfmHh5_NmcZpugbCT6oCWEYN87ymAbqNtNj0IqY7bhbsyWhyB7AWWmK8bB4N2j-fycQ2IM-v72yk02yOQ0fwCQ75SAk3rwBXmSxp0ah5oHEG6qa_lYTHXAY3m-692_PbI0vibdRrMA4oLsfxfa6hm4jHiiJMQa3qIl6gMyc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
غریب آبادی ؛ معاون حقوقی وزارت امور خارجه دولت
:
برای ما تسلیم شدن معنایی ندارد ، یا پیروز میشویم یا شهید</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/16450" target="_blank">📅 19:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVDlOGOWTQwhsM7s8L3Hh7m5TaOHEqJreJoyt1J8q2hvqe-ZL5dW0TNR56ZIGnutdocFPzOBSlvf-H1cK2Qg3boh26bNd51DfUGetqtBuYtVEVWO-hD8tXtRFjOV5T-Jf52yokUUYIfEjBd9H3_1_HYfaAhFTfXkT-vSZaeY2qWMaiaqlz-KvYFS4vPXRA5jxDxFz6LUgTqcQEmShioliwe5MAQcLJjURJA27iOQbPNu5T5FqfHs3Wj_mWF-ilR8Bq11a5Gt5iP5shRRd_wKrgeIm1ixkI1vTZAQ-3J_psjCgYsK-Gu0wSJWa_vhcwdT-Ge9SZXqv7L-QF-E_ASU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه اسراییل بزرگ روی بازوی برخی نیروهای نظامی این کشور  با این تیمی که ترامپ چیده بعید نیست به این سمت حرکت کنند. بیخود نیست وزیر دفاع ترکیه هم نگران شده است.  برخی اطرافیان ترامپ رسما باور ایدئولوژیک به اسراییل بزرگ دارند.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16449" target="_blank">📅 15:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SBoxxx/16448" target="_blank">📅 15:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینقدر که ما نگران خطای محاسباتی آنها هستیم خودشان نیستند.</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16447" target="_blank">📅 15:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پدرسگ های کافر هر 5 ماه یک بار دچار خطای محاسباتی می شوند حرامزاده ها</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16446" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فوری | فرمانده نیروی زمینی ارتش ایران: دشمنان نباید در محاسبات خود در مورد توانایی‌های نیروهای ما اشتباه کنند.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16445" target="_blank">📅 15:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭕️
معاون امنیتی خوزستان
:
امروز  براثر تست پدافند و برخورد پرتابه های آن به یک منزل مسکونی ، متاسفانه ۴ نفر از شهروندان عزیزمان مجروح شدند</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16444" target="_blank">📅 15:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هاکان فیدان:   اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/16443" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16441">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هاکان فیدان:
اورانیوم غنی شده ایران باید خارج شود یا به صورت سه‌ونیم درصدی تغییر داده شود</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16441" target="_blank">📅 14:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16440">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری تسنیم:   فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16440" target="_blank">📅 14:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16439">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در بازگشایی باشکوه بورص، این نمادها کماکان بسته خواهندماند:  #مبین • #نوری • #پارس • #آریا • #جم • #جم‌پیلن • #شپدیس • #زاگرس • #بفجر • #مارون • #شکبیر • #شگویا • #اروند • #بوعلی • #شفن • #شغدیر • #شجم • #شفارا • #شیراز • #شاوان • #فخوز • #فاهواز • #فولاد…</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16439" target="_blank">📅 14:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16438">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1y1gm5duKfuXFz4P1kAq4oI7oWiWoLdW7tKM0khS3kudhmxQG83QZZRBBeiF98LTxp9oDDboky27I30BLn_7AFSpml24icq8606ZcJPJctJLu-AgoU7LqlPAjU_vhglToRxclZHih0IBqqwXW63o_eSx5h0S40QLyV8KZ8jA0mFWR02aR4rCl4Nm4assEkKsQKa0S769-nNCyT0VZJCmz5Ldb56ldpYPP0pNoMMkkW0YooYmFldoLpGGo6E_j8F4F5oXvF9U7EmTFjubH4vWkx_TFYGG5zvT9xhb-UjaHx7LDjfT65LFLPpjt53JXGy0jjLgHfyauTGHB-84OGpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای دارای بیشترین نرخ زادورود!
هند زیبا در صدر!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16438" target="_blank">📅 10:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16437">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرا میخند؟!</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16437" target="_blank">📅 10:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16436">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=hcf-bZQqd34VRypfyT6sEAm5OSA5dsNbmovXO87YaswqxefUlgeSloC9h3HrPaJMrhFFWZTqeM8m_2hl_Nw8NZNOedcwyS2COIxlZTXHj4gj1l-dFbHsLJFlVjR2VwWpaUiycweNwP3y2vL-tEtAJFUzsLa_S_M8BPbirwmnRn8Z1crbQ0VmG7zdSA75_8HPqCrRtIQfTsaIe1Jj4PIwgNFh_uSEN8XWMvwlxIne_I764-X3L5BJ0oePywlBV0d9JlDO6u1wACDzU_RipDHwxwK_RjdIopc0YVAjgEmeV8p1D4SNLttShDW-QpNygxDN50ZjVE_WYWB0JqxWRKW-sRV_ZhZ9oChPtUleEerZnov7W2XZWW5698R-617q6IyaoovW-nu1rjkkYPkq-XYmxNe2di0yO_pS9US7p1Iqv8XWxxoQEjtMRFVhA4jmHTdbO6ROV7rLaABQdNrgHUVZmypQ38SbWaHXp8cM0rQIAmNuNWFot9yUPXc_NJM0m2GPcymO9XKCLQM1Pr-ynH7ekdLV36s9g1RToHlm8BbUPZk19Bcz0M1H04YRMx46rPHKzjOVWGkwAKhML4XGlSZe8iey4scJxdoHo8xQnX-XNzyuNH_3zYgOUyzg6twfeF837saCrxDh51MR1tzuEY6woRJJP1KrPBBx_KVcCzSmDkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe204bf88.mp4?token=hcf-bZQqd34VRypfyT6sEAm5OSA5dsNbmovXO87YaswqxefUlgeSloC9h3HrPaJMrhFFWZTqeM8m_2hl_Nw8NZNOedcwyS2COIxlZTXHj4gj1l-dFbHsLJFlVjR2VwWpaUiycweNwP3y2vL-tEtAJFUzsLa_S_M8BPbirwmnRn8Z1crbQ0VmG7zdSA75_8HPqCrRtIQfTsaIe1Jj4PIwgNFh_uSEN8XWMvwlxIne_I764-X3L5BJ0oePywlBV0d9JlDO6u1wACDzU_RipDHwxwK_RjdIopc0YVAjgEmeV8p1D4SNLttShDW-QpNygxDN50ZjVE_WYWB0JqxWRKW-sRV_ZhZ9oChPtUleEerZnov7W2XZWW5698R-617q6IyaoovW-nu1rjkkYPkq-XYmxNe2di0yO_pS9US7p1Iqv8XWxxoQEjtMRFVhA4jmHTdbO6ROV7rLaABQdNrgHUVZmypQ38SbWaHXp8cM0rQIAmNuNWFot9yUPXc_NJM0m2GPcymO9XKCLQM1Pr-ynH7ekdLV36s9g1RToHlm8BbUPZk19Bcz0M1H04YRMx46rPHKzjOVWGkwAKhML4XGlSZe8iey4scJxdoHo8xQnX-XNzyuNH_3zYgOUyzg6twfeF837saCrxDh51MR1tzuEY6woRJJP1KrPBBx_KVcCzSmDkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داماد شهید رئیسی: شهید رئیسی اثبات کارآمدی نظام ولایی را رسالت خود می‌دانست
صادق توسلی، داماد شهید رئیسی:
🔹
جوهر اصلی شخصیت شهید آیت‌الله رئیسی را می‌توان در دو واژه «تعبد» و «ولایت‌مداری» خلاصه کرد.
🔹
آنچه در سلوک ایشان به وضوح لمس می‌شد، احساس رسالت عمیق برای اثبات کارآمدی و موفقیت «الگوی نظام ولایی» در هر جایگاه و مسئولیتی بود.
🔹
تمام اهتمام و مجاهدت ایشان بر این اصل استوار بود که مردم برکاتِ ملموس این نسخه یگانه و نجات‌بخش را در زندگی خود احساس کنند.
🔹
رابطه عمیق، عاطفی و سرشار از محبت میان ایشان و امام شهید، صرفاً یک دلبستگی فردی یا عاطفه شخصی نبود؛ بلکه ریشه در یک پیوند تشکیلاتی و ولایی داشت.
🔹
این ارتباط ساختاری با ولی‌فقیه به عنوان عمود خیمه نظام، با این هدف تعریف شده بود که خروجی کارآمدیِ حاکمیت دینی را در عرصه اجرایی به ثمر بنشاند و حقانیت این الگو را در عمل پایدار سازد.
@kakhresaneh</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16436" target="_blank">📅 10:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16435">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:   رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است   پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16435" target="_blank">📅 09:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16434">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون وزیر امور خارجه ایران:
رفع تحریم‌ها، آزادسازی منابع مسدود شده و پایان دادن به محاصره در پیشنهاد اخیر ایران به آمریکا گنجانده شده است
پایان جنگ در همه جبهه‌ها، از جمله لبنان، و خروج نیروها از مناطق نزدیک به ایران نیز در این پیشنهاد گنجانده شده است</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16434" target="_blank">📅 09:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geW5178hel9_XA43kOuQwjuYz3KhjNpuBC8yZqgcLqerGdc2YM9VYEKrCg-Upu9wUElKNbejQRHEAL5OaYxI9JjTflDORCmhEK3zOk7c3r3kT8j4S2JQZCf9rUNq47F0MJusQxhmmmoaoO2UxQJl6z69FIQwZP6C2qqMphhlOpLfWNYEeL50JPG4vLh5OJwk5cfiUu7nUZkUHTlCg9YG8yfJcGYTUitc32pL7BF9UmY-gwT2pezcejTHtszkSIwjJRpbEMHAQCGR6Q_SxMj8Hw3zyFkSm9U0_wXKX_IjlYtO7TE-7ZDkKDLTeqW9tEiX5NVgnuUKTzTXJKKIlK0xfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ نیابتی آمریکا با بلوک چین در شاخ آفریقا هم نمود پیدا کرده و دیشب نتانیاهو اعلام کرد که اسراییل، استقلال سومالیلند را از سومالی به رسمیت میشناسد.  جالب است بدانید که سومالیلند از ۱۹۹۱ دارای دولت و ساختارهای حکومتی خودش است و اتفاقا از دید قوام نهادهای مدنی…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16433" target="_blank">📅 05:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرنگار:
«آیا گزارش‌هایی را شنیده‌اید که می‌گوید ایران دیگر درباره تعهدات هسته‌ای صحبت نمی‌کند؟»
ترامپ:
«چه سوال احمقانه‌ای. من چیزی نمی‌شنوم، ما در حال حاضر در حال مذاکره هستیم، تو چه آدم احمقی هستی. من در این مورد با تو صحبت نخواهم کرد.»</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16432" target="_blank">📅 05:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy1Cy0EUpoX_zvqaEhFODIvrwM0awdVwb5-bx7njmyaQo1XRR5f_VbjeEjz7SOveUXkMo8HtzYisOIy_le1unpQwcsMQ_HQ_iySdiDmp0IK8LakzNzlLiIYwvJv7aThlETx06Bi2vO9l4Z2Me58t1r7XP9xvAzuMS5dJ3ZZ1VyTfEy7o-EXKh4Zniv8DMLnHIFg3Qpi7xRR_B0esOk_eyQzkp7zv3MSSOrakK1KVBkfMa2_VdgWmjaq1iyP3GBiRRx8phu3W2QmUe4ifUw1bKLiCK_GyTvLKCsGrHtwPil0cNJFC4gmVOpFq5rMmiwtf4HFVl-gUWmjA9lvpeyUwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب گویا شماری از مجریان صداوسیما فاز امام جمعه بودن برداشته و با سلاح در برنامه شان حاضر شدند!  سبحان الله !</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16431" target="_blank">📅 00:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تقریباً ۹۰٪ از کشورها اکنون شاهد روند افزایش بازده‌ها هستند و نرخ جهانی ۱۰ ساله به بالاترین حد پس از سال ۲۰۰۸ رسیده است.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16430" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16429" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQEmV11nLV0ytctJgcYc-NzyYT0K_MXEzEViIKbIlzbeDWkNEYAd_efZ3i_nQM5uKgP4Xm9EDI1qiJEwnqbVLyusvgX8aF4a8JYRMjrT7CAd5ycneoffh_6ij5XuIZ-eNIeUx1qTYWXzXcgVfOvukzpgTUf3jX8sCc2OzeOrq6c6RCEMZS_ePHIrWLPiNg-LxrwRpCxIDTHnEyDBmpfR--Av6Mi86zwStwxBNDRBmEYnhZ4q9dDpdt9o1C2oKe6_or9Wv8AhOGQVpH0LURGterexul8lUR_XuCbYmXtPBcEeTqGHfULxilh0eT3AD_D7v9vfSfBiUkJK9eg7FG_o3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر!</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16428" target="_blank">📅 23:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرگزاری تسنیم:
فعال شدن توپهای ضدهوایی در جزیره قشم به دلیل پرواز پهپادهای کوچک در حریم هوایی این جزیره بوده است.</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16427" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به خدا قسم این مردک روانی است</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16426" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic…</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16425" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">I have been asked by the Emir of Qatar, Tamim bin Hamad Al Thani, the Crown Prince of Saudi Arabia, Mohammed bin Salman Al Saud, and the President of the United Arab Emirates, Mohamed bin Zayed Al Nahyan, to hold off on our planned Military attack of the Islamic Republic of Iran, which was scheduled for tomorrow, in that serious negotiations are now taking place, and that, in their opinion, as Great Leaders and Allies, a Deal will be made, which will be very acceptable to the United States of America, as well as all Countries in the Middle East, and beyond. This Deal will include, importantly, NO NUCLEAR WEAPONS FOR IRAN! Based on my respect for the above mentioned Leaders, I have instructed Secretary of War, Pete Hegseth, The Chairman of The Joint Chiefs of Staff, General Daniel Caine, and The United States Military, that we will NOT be doing the scheduled attack of Iran tomorrow, but have further instructed them to be prepared to go forward with a full, large scale assault of Iran, on a moment’s notice, in the event that an acceptable Deal is not reached. Thank you for your attention to this matter! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16424" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8S-A9A7JYOB6oCex-PrERIr-RrSjN3h4vXNKq81xfnbibFn3_klexhnoLZs30OGHH-7Y7Zp61RmSnhJcOuhEwjVbSwIjoiDzZku5hcnFxYAvEM25WxF6lls6jLfMQowIlhSGiTDOyGCe6OaQlXheLUPsIbLQjyfr_eKHb1ncb3xXeAshIV2j2QpR4EMhJc4ZEza4Wx-9pyaSCcc7rbDgJILnoZ9m_ztrWN9RLwNnmyG25DxSAslrWsDMlNP-kDRWumfhxgUL5uHzisgTQ9H9MAnDah-1s6Pvzgn0J9p2fj_-7NYd11oc0Ys97oPDAys3cn2V7ec_y22Roao9b4eww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16423" target="_blank">📅 21:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:
«رژیم ایران می‌داند بزودی چه اتفاق وحشتناکی برایش می‌افتد»</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16422" target="_blank">📅 21:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16421">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♨️
پس از رد پیشنهاد جمهوری اسلامی ایران توسط کاخ سفید ، وزیر پاکستان ، خاک کشور را ترک کرد</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16421" target="_blank">📅 20:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_IJbFN9ArNd_J6RIqhSwptk9-oScQ7fCGrhWZLqa960L_VExcaMJ7eOKrwQcpVh702XTQzjzbDkxHKHvTIilhDrrigKebGsu97vd3Dc7RmeZfcJjs3KVKw0-fWDC6GuzAfjhp8gVGCbDUfTarFjfhGnuu3l3DFhmpEffGNex8EUinhs7FTPQVkfipzTNodnWYe8e4_VIK42SoJzs3uMCWGa2raRTmUl8h7sC7gAHdDPUF4esc7Wl0kecsKx1Hd7Qk2_YK_Bn1QHqmzLmsADlbEG2TX3VpaMXPk4R7qNJUxTGZfXSC90SchQ_dbQ_U6aVgpCEv8yXbSVUvnsTUkrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16420" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قلعه‌نویی، سرمربی تیم ملی:   40 درصد عقب‌ماندگی بدنی و فنی داشتیم که 25 درصد آن را جبران کردیم، شرایط سخت است ولی نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16419" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16418" target="_blank">📅 18:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16417" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📌
تأثیر منفی بسته شدن تنگه هرمز بر سیاست‌های پولی غربی: اهرمی برای ایران   بسته شدن تنگه هرمز می‌تواند با افزایش قیمت انرژی، بانک‌های مرکزی غربی را به سمت سیاست‌های پولی انقباضی و نرخ بهره بالاتر سوق دهد.  افزایش فشار اقتصادی و تورمی بر کشورهای غربی، ممکن…</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16416" target="_blank">📅 14:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احتمالاً زمان بازگشایی بازار بورص هفته آینده اعلام شود</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/16415" target="_blank">📅 13:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SBoxxx/16414" target="_blank">📅 13:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارسال پیشنهاد اصلاح شده ایران به آمریکا از سوی پاکستان</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/SBoxxx/16413" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyNhcc80jOWDjLr3TZrpT61YMQB2orhsx0g9esmln1l64eoZAs0KWs0QtsFQjxMwTmcCXiOUqaUdtrAqivYYO4Rn2hXGlpsc2sym2AqQ19zdZEEX6AP84slGSoHbddORQhsuO0Vv04CAS2wFJ8at3zUjzMdPgHd0TupbkE040CEHcprInyO6Nrn1e-nGB6J2PYxvngddzIIRDI239SE0BNP5dlXLhrc2-lXLTWVEt9r6pk_NZLP5OyxWKCQzhB5SkADFlJlJqaHKs_29LNgmtObIAtwbAR51-tOj9wC5I3SpHht6Bl3l7QVy2JyO8S_OLRvpGMeaq8gORT6w0S9leA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16412" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🟣
خبرگزاری CNN :  کابل های اینترنتی تنگه هرمز ، توجه ایران را به خود جلب کرده است</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16411" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcMqdRtVWlLsHhlpofIWJnd7Z9WZUWtEDCKN9A7DErZ18GhnuQJXBM2EmOzXn9PxJEKPO3_KPfYZ75_7l1Y3Cqx2E9807a_ZqQ5m6sYK7mBuc27jSubOgNVAyjF-xFWkpLcSLYtcy5Qrc5Wo0KIC3FoBmil8VtNtp05o8SXj2CV3kD_HubFN0b8OhSenKzMEbUExIX8w9VutLC1iUULmbZKSs68GYCNaZjCFbc3sndLdIC0MkD0dFGoyutPfYeINK1EJ7A6VeGtTGGT9Y-tj8SEMNQ-TWe1c3IF0W_TpkdwS87vj4RP05Vz3BD2jjyLnG7F14H-3jBTX_GbsBByXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL -- H4
💬
ارتباط با پشتیبانی : @cyclicalwavessupport
📌
کانال ما : @cyclicalwaves</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/16410" target="_blank">📅 09:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjTauvK_MyFkSnuTSpGwJGl38nh4dN63FtQNZ5BMr0ld1_qxyLQQud6EfAN9k_C3iPju8Q6Vy5I9b90FD9aA0q5LtXkYl32YxY2l8CDkjcUUwss9UAo-kzZLsyRsem1i7FU8E_a4Vwu7m1d3WtkVVrWpu1n4hYkWOeRC1L1u00uOVJ_fJHa_MK9xu-NKnA2i2jrAQWUg9WHRfPYuAmAn5PgaOkF40SL9lPxwC-0ZvgdB-PTTkZrq9PbF6P5jzZc_Do6VLIgt1vXAtQXeQe9nArkgHFGRbT66uQBMtOt5O-QytOlxXMZmdn8scFkS7T758fG_EPIeFiwHSUjkKyLACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین که ترامپ مردد است بین کوین هست یا کوین وارش کدام را انتخاب کند نشان می‌دهد یا دنبال دستکاری بازارها است یا اساسا نمیداند این دو در دو سوی طیف سیاست پولی هستند؛ یکی بشدت هوادار تسهیل پولی (هست) و دیگر طرفدار متعصب محافظه کاری و انضباط مالی (وارش)</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16409" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">#URA — D  #سهام_خارجی  این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.  نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16408" target="_blank">📅 09:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تأثیر جنگ ایران بر بحران انرژی اروپا
جنگ ۲۰۲۶ ایران با بستن تنگه هرمز و حمله به زیرساخت‌های انرژی، شوک شدیدی به بازار جهانی انرژی وارد کرد. اروپا، که به شدت به واردات گاز طبیعی مایع (LNG) و نفت از طریق این تنگه وابسته است، اکنون با چالشی بزرگ روبرو است. بر اساس گزارش‌های اخیر،
آلمان و ایتالیا
آسیب‌پذیرترین کشورها هستند. بانک مرکزی اروپا هشدار داده که این اقتصادهای وابسته به انرژی ممکن است تا پایان ۲۰۲۶ وارد رکود شوند. افزایش شدید قیمت‌ها، تورم را در بریتانیا به بیش از ۵ درصد رسانده و تولید صنعتی در بخش‌های شیمیایی و فولاد را با چالش‌های جدی مواجه کرده است.
کشورهای بالکان مانند
یونان، قبرس و ترکیه
نیز به دلیل میزبانی از پایگاه‌های حیاتی ناتو و آمریکا، نه تنها با بحران انرژی، بلکه با تهدیدات امنیتی روبرو هستند. حملات پهپادی به اکروتیری و دکلیا در مارس ۲۰۲۶، منطقه مدیترانه شرقی را به منطقه‌ای ناپایدار تبدیل کرده و صنعت گردشگری این کشورها را نیز تحت تأثیر قرار داده است.
در مقابل،
فرانسه
به دلیل داشتن سیستم انرژی کم‌کربن و مازاد برق، کمترین آسیب‌پذیری را دارد. این کشور با تکیه بر انرژی هسته‌ای و منابع داخلی، توانسته است از شوک‌های خارجی در امان بماند و حتی بر افزایش تقاضا متمرکز شود.
به طور خلاصه، کشورهایی مانند آلمان، ایتالیا، بریتانیا، یونان، قبرس و ترکیه بیشترین آسیب را متحمل می‌شوند، در حالی که فرانسه به دلیل استراتژی انرژی مستقل خود، در موقعیت بهتری قرار دارد. این بحران بار دیگر اهمیت تنوع‌بخشی به منابع انرژی و کاهش وابستگی به واردات را برای اروپا برجسته می‌کند.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/16407" target="_blank">📅 09:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">تلویزیون دولتی آموزش زنده‌ای درباره نحوه استفاده از
مسلسل پی‌کا
پخش کرد.</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16406" target="_blank">📅 07:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8PrOzn7eNmSnTWDdI-lsT_gcHlz1FQyRwc56lfPQ3wK1uiOZ5NR6gom6k43oXD-mtKLhPzEcNdx5n4J1E6FwfoFR8HidHOBIfbb7pM5gxkieUQzj5GWVyPvjwsV8_p-ajiYbLRojXznuS3ksYJDuJOPrRkVq7TKFHiMSbIdg88X3POdzHTkQsacY9_jfqnCvdN6x9os2UwbygcGujVWYOTjTwVeJgn1lwc6Ray_PXhSuk9mj0fbjMAOk_krduYeOzYs60UBH73qz71JbD-6PZv94y5RK71AoceVXPSIBnODIqLdIVtD5MeyQytcO93L3ly1dzrMuwrcntDl7NsN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gold/UKOIL — W  افت 45 درصدی نسبت طلا به نفت پس از ارائه تحلیل.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16405" target="_blank">📅 06:45 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
