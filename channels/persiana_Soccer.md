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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 544K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 02:24:02</div>
<hr>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=aDxo6AWg8SYJmZLGU_OGdXFtiycVQusAR3wA7fJ5SUyxyA9QgzsrX7OVT2OYroAxd__2sBsrz3OutZVvAN4lAsjViDYckXSJjE7PlQvT59g3CavZfASfXrhyousk4hvZgqYOlBzSR6a_agyNqvD1f6TEi7EcWxSd3LQndJ83nyL_FqPGzP7ZyRP58Wxfr7lxtANZaxTHamTbB6AciSup7GkDh28cxlNt0FnN1qLoN9UAYN2QU32g7HinZrxl6-r__A-u-GrGUFp0gLL_lPVydgJURrC3yfzdJVthWhOv8Si8KXfDQ3Im-webASuN7aw2aclxnEiWnNInnsdgK3XCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=vosaQ9OV0ocnEFHQwckHzG9Ws44jcEw6eOxf2sjcPtucoi2lHc2hoapoZ8sGNPRT3gvsg1z9tmxQEH70XzWyv0uot5gf3NIgJxlPAbm1EKrLnzMB9H90yJFWKc5TJhoKSAkNYxvJl5Aobfg_lIC6bjwsFp0JphvGw7TQ_loGjV2imEgTssxVwRwVTykARHiFzSVg2ArM1PV4oqd2x_l_Mma-eZqZMgxPZMfXlvx-QPhGFHxF0dNq2WIptNKRbE5cgyW5wQTh6BpajMMNViRfVeRtgnthi9mCxTsvrAENPrHelSXYoKYdkLMamdQHQS35BTWbO-rr_n7yn5o0LDrGIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukJ_B01CaSBwt7R6RaF4WpI2xyOCOv8Z0vJbb5hCTWvWGj0-9YB315EwGDUwBhwwiHDwngNHoo0Lj68X47X2w6pxRXe1QDmo7Bpb59kAGFM2EwRzjuSSmR5WjNx63V3Tubbf8YvtcVY3KZpXST0k4E5BRIIRHSXFtHiH1JgwVL4sjpGWSlh1lPE1a8IsncZ0MsitScVqRNpfv_onA4Oim744rBjftn3xLb4Ogy5G6Y1_ddSbRBo_KThDaiZLO2qoxr1Zv9LWZMc_LsgVEhNHV2HZEAtqm2VV1CtUUu21u820OzR_ix0bq-irvSM3Ou_X0qUE2zDVgmGjd8GycJS9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=G1lceH3I998iimQdTmLNicbsA6Sh0frKwZkih2_WgVxaBHKb2-vJ7jfsiLnaVwhjMZfIsUaIrcHoM6u9W-E_GB1nMrSPxF3OPD-8pr78H66Y36UMZF5D0-oSfZ_rXiA30eAL3vJg0aZTpqNRpmSNIvqVJrqXtrJmTDfvfbGe4SGQJUivfkVqkDiNFZnrj1wWgeDcp-5E1vdYwvUvU7CPHLFrpLXzaG42mHE1qgwR66MMkOua3yhbALRmqSx7xrYI4oxArvhtyDWW_meOxWteCwUiXK8N8JWvr8xu6vPDvslSfwMPtmFuFjIJ2B344zn33yPQKH51HqNb-7gyGAYq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMR7MXafpxlt4ommh7HUAWR46X4-w4kP8MHRdq8RAPkKd198KuK8gy29w3GLJDR1X5Pnbs1wK-AY9YzZBtyGxpnrHfXmFyebNHYS3dTm9SEtd3OtPFPsmqztkJj6l5OAkqAGnWY-LNILy_xnD7dAEUjeFyEzFvWgQk6lTUQ0TfpITswcuqPpqqHjmzjFnhgwwIlRNmbAbNTifzmJkIbb4P9Ya04KsVp7o6LJymAupFe9GarfO__nJUN46AF2usBmYjtbKMjxM7gL36lgbnutyVFlILCclfXbmp5-1j0KG53ppAri7CIjclUl5VFrSH4RVR-qcRmYa3okg6yl9OOJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXntRCzX5_llerWe8I_BojAodCJKRdLkRSTaKEzcwfA7LM_0RXLs7Liwin0cWRZDOwLeYWp1MM_mMw4vM5-l-_Jr4fWO3gdx2DpAgE_rEUvGPQznrEQl8sYTOq0iziTdcIgGHfoup340Ioof8gi5KpV3TitkKTFwd9hBeKuNUWYZkweF-RM8i3tQysz3YWR35DP3de9QG00pPDBFHNLeCjfxlbZZKzuGoqNC6AcfUesEm4SvjLarbPMGB9V7IJ7MfYlRrxIax_vI2nqC59VkhYZUXFkyo8asySVa4rDnJJ9hjcYwM3FWPHOVrat_2UBpE4lLt8mUfq7tKSTWswsDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDp-387yjF39QLIM8YF3Gk9ELwtzT4_4_6B-h8-qbngUZ2fBgrQE3DAGsVxHI6oXG-A06kAD5tUcoL68owOc2otqB5LCsW9SLqvFN05AzZRPlPjiV6QTj4jPE1rta93hrZI7sD7noXFOuBKA4VOIAF2OyPxwr4N9oYY67rqjUUM4wzh_OkRFlNy-a3UmkK6H3vdPJ1DPLuSTqv7_aESMFyRNpBWN7hgQdVpPhnzWmI16lJdDz7tGMiDjVEy02ncjes_-sceYyTGZW1on9h_Sr6YJ8TY2qkBTz_xsiMCfHU3xLzSan0jMac9vzYfgDGmPPOUVxTy_8dnUSt9tHvr5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNSwq_CUBe3JodmPSyjD3v0B3PwVdE7Oyj7nuUIieBsv1BJiX0xGf2jcA5gYSh8kug-Rv8Y2sna-l3SIKCks0aGts_vqzvvhDYESxyilzf7gUIk7ozarKvu0YW8SuRXsMMb8zfOSCPcsZCEtQpeVkm32ZBWLO06LK-olxUqrfzzXQpd_EGiuJyXTnjeyAh8RhSBgmeaPOalrVgyg8zee9YczalBtNPbWzBFIjP5_AedU5330pACKwX6XU6nYS17kZPtXhxqsGbiXf2NtYxAGCp-nGAIs1OF9FL2F0e6TiPd_EjiSCCZAS919fH1zKnh8Mnl7aHgJy--D4ezgdFVM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebjvii_J-NiylWi2SATN5EJvDRjzrB3GaZKs_BoSjk3sifnML5z-r_3PuHKgjA-HDOBXeJrckDkC9z7f60le9ikrbeWqBry0DHdZq5vJvTYKUXgRBl8mS3m67k5xKp3Odkr5OcAqgDWnzUeBe4Ig80mshXx1DUrQ7jVROsAAHfPUrNnx3ihICb4PQiWbmFVl4_teETpFpFkDe9JftFkHHfz1qE_Ls-9t_n5p1f_2TcvAKeeqO8nXz7yjBGVv5ymC6cqUbq06eSaslsH0-3Bie1CBvcpTHN1DTsNeYiGbX_4qZDPS9cNIIJOq-Q81g7aeNKpnOTtcSVqu_t_AbmVZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXAMDDYpY0j98PvxMhmYlTuzt6RwQ4GpaoRfkk5cGEVGPG5T3zbfC-TOReqwggD61q_aZj94DJZs9GTcs3D-jMCzTKNUHlO-IFpcCpZ74SLnps9rKGKeMYRP46LZX8YkIQ0TTArTjgr2fJ2EU1-E7bKsC0W4-X8SoqzxGWUfCz0UkLZVRvtLH9bT_2nSt-rNCH0Du96mQp9Jb-w3hhJrLhYVsHHjtBflSWv7WutV71_0E4l3MrV1K3nuZN9v-qMqF31wlmI93ZlEjF37ByFwAbAUfZswO12dgYTAgACx5vRs_62zlWpgKEl3sjve4udl02hHlgVyoEhEiAKHZ0aDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybw2IwqV8QqCpmKd6gWROsRSdmLLjZgomqU9cpH7F0DR6ItE_SSUZnrpDDsg_aDzTAb_jCYQIlP2Fjnb8yPmbMYt1FNejWE1Amy3utvi9zEFJ7N_2PxYORthruumCmfnboEtn3l27_U_u--DJfqHdptbUwRB1bHDp4SJMIZHYBtuZfPrF4XQ_hdP9KLWPlMIWdXO0xfVh4DGydVBBsDd3defWnD6ANlW4X6dfzM4oVXKgN_wsdqOa1dRBOGmsI7kpv6eH4d6bTzDejVeov6Wg5Zxhcwkhz5V-2aKbuMXxSCaYrQQJhwpE_nK9glbQ8542PFoxKTrnW7xks8MRnzLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmkDFuz1WYQF33okYbOAsNBWxKjcwBMnNQNkbOZ1tDQW3JB4hKfs0e6hVF0kBnury3Bd2gj0NrXsFkDoQ59OzzXs0I7mROLv8cQM-40nipZMo9GmLjZ8gwjgvYaL8ou9uAbpwc3c4eTgsKdCVSXdLLu9E9tna68ico-q2SwjyoXqlkEkKQcSndFSksiokjehtyS9tQ4EuUypwOaGOTGhcKMwSMxwKQJtq1KO0BXsGUdaKpVGdyNODWjBrZyBPasKA77tQU6XgzlUBLzK9YqBbvlJH8W55bFpdDUquvPzxqjiMdHUhWcM7iu5X466pOS-I3JfllyGSHhIul0MI9LY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQAh9HmtJJYsNUu_lbN9vknB9AuP43q2KTrgkU08wDuT5w251e-1DZ0FdaSH6bL-kYeshL-ioZXXyuEisVPzEu8mD1RDrEnsEdgj-XhE-QpsVVh9fAKJrs8LafOJURFvFvC5PnE48ES0B0U6KIy0Yz1o1gzbPJpsiVnIvwbmPLOExOccZdXrLDHAQI6n6iCwwvGucIgV4IqMeen62TzEe_8WPayGBG_VfIn7Qhv_4nq-90IyI65g7e3gYgNm6qxObEQA0WDrvCbBvc-Tg1Z2NiZ0K6ieYhYKMiFLPeG2xIAictDDhbrNYw6XuY-s5khDAyHNG0UzRnYLv9tIuNZYkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2oQ9IxhqJ2I7jSK-v7HS556WlTbqSvv7e-jEIZRKzXQjnDy8VjnCy48mL7z0qI4iaTpadvtWmpTTEuYQeudYRPmFbP0QxjKBQnvW3SpIUHNske6g9Sn_lIKztmVGL-tKh1no5W3iH5Kal4jkrBRouURpJO58lHVoLgS8L4lzz5enMxJz2aGuZsP4lfi_vcqFjcT1nKCsuGiGWqceQzFn1P5_5E23A2NjPljhwGi5LDt94igYZojPLyRxUFrbBUTRM6kgGHYqqGiupSpMnwkXsJ3ax4LelyyOitnERhA7oY8ZW-0I6HF9_bNdzzo2oIk8vbFOofhLSIt6HxnCa4s8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgHZKOjgmRlmIBBB_DIxLu4ncqJI5V9f1nS0sfwLwyUI9wpp3VY_g0xq7qLQknNqpXMOOtljaWROaC0WVf1hNt71hG8gtFHm1XrDKFKaf75PFszawdRd_sN54jXUxg7uqNthLl_uLl_C-VjDcEM2lEPc3AEop1i1DohJ2KZFL01nYWe2ZpyNtwwUlm0nTikgN08_Gqb35ZJZSPtI_1XCflQuCFnAuO3Hg2jg6LYhiA91mirB0OVTUt9Ui2yUiu7vQuUegIBS8EC6U83h1LgOIi-2elpnmHf8AEk798yoSRBRpnDloFtcbP_hhHQJNMcqVwr7m0ICRzHBko3X53zhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYmOsvFB9N8qE68B-MQ6S4a4Zy0GIaXEIdR9NNsKCvy9vxEBqWnm_R7vAxahDgZOsej8eJWQ__GTYU_E6D5iTzrUN_HPdpeL8x6VCqUmJqS4mD4mGueI1yt5NrgRZVDvH2mNNdOpaNsNQNEAn40IlWnunJHxlp_qWIsPzaCiJ-3BZRitEoEF7--9opzCHHWY6JuNUR0US50fvTNPQ3UyDui_GuREgsa59YHV_suRx0s6Ns982joWPRHplQIsvh5UbEUDiHzoz8iG6TRBj8UHi__uoy9KJ9A-3b-LuxlF23lbA4h3mjaWWYlfrOcAM3w3WedYa_NthTg7qSbd2OT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbZADzK4YfrdklWLamyVfr_0tMe_zfDHeigOejwvusYEqjXPvGho2PKCkNOwA4D4v7hFsMcBFkNT52Vt06eOSgaP-Yxz2N3FiFop98H2VnCnl-EipYh1jV-ZuYDI-rAcEIyFKPDsXm4WTqVjs9Oyw02BydKl9MzwSIkhHqbFZgVfolEXxCJD0OqOrcN-gTWUPOYIwKh1709N0wXhAEjE00vuzNEi9RZH1nRmF_J4D3vUsvvOrs-DeeN3N6Llh-F4v-sG0AclWp_7T3Dhr4FBytWRFla7npoPE0fZPOQzkwM-5nQ2LDrlf2ncPzD7vJMwgppW_tcSnz2yyS7DHzfF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_I-Zfw4_AENLw483IKShzWX33v_TBfTWtUX43LzWgyUxkoykivdHltOtEpE3MjGCXj-lPZcXCyhAZvXm3z4yxJ2e1vLp9UukfapjOyUdDtuJ9lBJEu7AC-yKhsbYEFCEC6Tz1f9B7CqVVlicLomOdVk-0JNrd5wj7zBNCJfKqHLxEEz7YV5rXBaJzU3fi3p4Sohwy1JS6qGie80XJBeB0rjBk3NVJ7i9tDk8fst1lud51H0CariyB-ix3Pvn0E1YgBNKP5iIQCOmTDdYdMwS35qZT-2VpogNwN9qDLSk7OHnF52TEO9RhtbStehYa5yeLDBIJJDzko0mYi8yOJWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWTU0sgLrXazGQT02cYilbLgP3GNewWxutf9rxs6GBfKkUJ8o6RcYrrZAEq2bYt-SxmKaJOWTK21QfUONiASLfv6gHrCbYxG8bP2Ejszg9YMXNDyU65Wuq18SOaxWVkJtl-mtA3_xABz2-1rkDv50OjyLt5JAItUAf-L8kinZqTLFJveHA8caUmBwFihAf-EE-FwgU49eQjr5EfJDX7wFwEVmWPHhViy0koYg9A65EJO2zggOIOnpR2KLaZtSSd6bkjfJKXYALQKvo9jXGWforS4riP4KO3gJyXJR2Pc0d-y6ysax-KhgcbcYXOzsiJY9FoErPt671dKHUqLee8Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvxxUs7wQAoqVJCvAU0qArKmESRwNl4cTvpBb-tLV5aC-3_OdYuKuMQuve-lsnK6Y08ViOlNiFIAFcYS4k5mFaymbs_jJ26bfezXs3epzoCFhMqORSZI1BXNZdilCaO351KZ4o98J2XFVE5T95kuyiLqKyBmgfiUFuyY9g1K-zmjBp77oxQbc-M2p-tOBI3FkCXpJh4goJOm94rysuMQbrFww5MrluIi8NwrXMPrQspNbscE618nbOdbf1Bi-y5Sjif4ly_sVTcMXQSz1UHLRL-wPGncLDMvTlcE1yVVX45qlFdr-vAQWuE8ryIBWrwCnWP9hhUPNj1hFsvLH4QNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRTdW0HzJe_MzcK96u-hKdtAQ-22rsviOEV_GoydRe5wfiE3iaRbdkbfBqHQPDRtXG8S77Lpb7ds_jnDvYE3Gs9Iasai9ZzRR7TQB7vUbTWY9DcgBrKW9A7m8Ga4h2nzHElmqGSEQmpa7pncurViomDCyWUuNOjEXhnGdlPa2eWFjFLh_BpgUZrhwPdadark5WAKXk9FClQAvO-CvBFhpmitNznN28SIp07Quw4-0LEVbOMCzbX0zOMkfcPk2F-Z5UjkXPCwIuLl_QbTkfUJ-qDqoE0RDBtIbecX3f_cmvuqJs6Prl0a1W47rhd7A0L8B6AkLxmfvR3477PpkRzK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDQlp2OFnRItB1hO6DyTuKsaMb47ZFMwJjPPWwfZz96ihAhrj4SKLgY-51XEYbM9EcnTOo32nnjJgrQLcbKJk18A9P6N_4cfiqrNGUsHYFpsi576Jg4wu-L89w5tmUObJz3maUMZIwuMi7abb8jFrJO6c6A3jvYuF3NIFnRBZc6pyqW5GkMeqAn3Bt2NIdhxZkKkw1w3Qubv6Uyvlkm41UjCZmrXWTvy08vckdwyUdGEulCSI5QNp1Uq3uMrz1hcHCVOiGbglMKR_T_Tkl_XAhESaGuiUboy0R_JRNIYyHE1nhbba7kcb-EK5iNJoBb8VEnUrTwwOOWXpMTGZCkTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FzlqZMoCYHN5zlMATrZwh_Ez3zoz1igOddFXgTEvV14Auyr32V7VBQMGmtSmoEUfZu178lfEaDRA-0mHDASVU-OQKtBu-n_HavXCvcemOvvf8NGzFX_oOk77lV0NFQDPwD7wPy1lqEgHEqIR6NS-SVVTWqODXGqzUMF7Hrs-v9qp1LaMtebMZ_Q2rENYUfj8nNW3AVHP5QwpzGJoZF7-erzXoGylEAyGS1wRHMeQUuHfuyMAzSIXwSxOTO1HqLN_-LhSNigHDFHswnRMlOdP0BWVjBy8VJXgYXPI3HruX7r39CULjXIBZFyayFOIRSTImhfKRZK1y2ARBGLRyelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMtFOa6bgoS7kp8xrlCF6U9N4dC3wjGXK1zR_I3nfIc8c0jw3Jhy7NG4FdLm_0g2BaGhWNDGp0CtCCqFpdim_7O0JtY-XrvvnKlHTgd1MtBHYY2MrtxF-u7A4MQrLqDhmrVmYIgdtLu6F1pDaW5e7vR8DDPh9eBe6vhqJefhpDtySVSMiJ0V_FcRJCdX5402u85NXQLOEy8x9PvzzSN5bCryDOvjL0P0-KTXHxIoDlce98pg9193NJdp3fli0tpSPMYXgTf-swHPmJybWdqR7hoWZsSe3PbzWPI9I9lATXvwbZbSPe_jOIT_Nva7VCtH-G-I9-KURzHDSRUToOMq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY-khBlZUhuufMxxnbXVDkQVMTBHqP6QrvtsH9ocYPInlxB9l-5c2SUeQPIaTCxtRLGz7zc4kncHsbRwzN_FPOZQemA67AXjuYvLUXfsMmzp_tedoDJP8Gp_CWbTIqFOwqvPTBpbrZQ9mxoLRip_1YmAo6rvb0uPlZGbbRMVDvVUSeIoWP5wrHd5UsmpdkNOEmUoKxT2bFGHxncJGFCvaBRWScYIcsCStFfMuXFbRjVNWsRc-FSAPlxNr4Upugqu5Y6fgbI5YNI887Yzv8BPH7HfZKnhHGL9voIpEUGkVteG1r0QFVXVYBkVB_rog6CjduV6Ps8FId37HXG9RZNDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=AldOikJUAbZXXfSKItgfZbTIkte3uqi8kuFawXCmjYsEYKLXSzJYXztzApWFdWuUI5zPlC-y0D0zkVDTLn-SYbwV5OZ_TAJOybPYBsEJ5uChF6K74MtjKeeX6dOq-e_UbOOElWnvXsnpoWO2hv8Drbi04JioYMLO3hOvzDUJXcuDv4Q_K2VPhXs3r0n1_fGhtkv1WXSmhvjnVF5VgYNs0ea1gjLTRoGkb0XapwIxeRpB9tKhv__N8eXcgZqmyp-vToN0-VLKT1i88JXwUQjvtysXEsw9VE9lyeSsP2LNBGQWSUW0jlfrezVMgjVu892820Yo26Nm4PHjYScp2lJDyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=AldOikJUAbZXXfSKItgfZbTIkte3uqi8kuFawXCmjYsEYKLXSzJYXztzApWFdWuUI5zPlC-y0D0zkVDTLn-SYbwV5OZ_TAJOybPYBsEJ5uChF6K74MtjKeeX6dOq-e_UbOOElWnvXsnpoWO2hv8Drbi04JioYMLO3hOvzDUJXcuDv4Q_K2VPhXs3r0n1_fGhtkv1WXSmhvjnVF5VgYNs0ea1gjLTRoGkb0XapwIxeRpB9tKhv__N8eXcgZqmyp-vToN0-VLKT1i88JXwUQjvtysXEsw9VE9lyeSsP2LNBGQWSUW0jlfrezVMgjVu892820Yo26Nm4PHjYScp2lJDyzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXH1X1KA1qIOU-JcCGcwtUpCDI5-9OSex37rGZF2LGR9tHtCt9ajCXyFN-gNBXiWjRK7kgE4Soj0xKoDvlV3nEZcuggae9kSSKL48jElhqZpIeUqfnziw96_2rS4JFiA7sKLrsrvzi7xJtn3q9awTeYjZiNkHb3CZhC39r49R3DhQ2ZuFK796ppUSNJF0Epeq-pHsnHgwrPBmXLnSqevdSImatTHwzLKqHTeTsksKRdT28qgFCqVHtC9RdJ6sH7gQpehE8rBdqBLZ9bc18bpzDOwTKaNERZBdDFVrD7OxgHiFNUzu2lwvEBs8jGQCTVBSSNyrQw0oybQDGu5kY33Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=DOuK4HaJLiDMVt7lSC6gdy_REGKmlW67AASx58Z3CrZJdzVz8bwW5c0yab-S0ly0cipy8ghFNnQ7r3fmmlYsKwtxfIEwjsy6sLTZzxRGAXQTgy9_hGjV3z1IWVSYpFyN3C6Ld-EQ8Plx2dv9Kbs0zSLF37phlcAOLk92CO1e6xUgLzLncp1ZY9yq9hJmLzN_72nca-ow7WTi1mhvB6y-nF1Ds9AARMMzWHKa43842M4ZdepA68ssUVkAi0gp1lpKyQQmp3MqnRKBeINCqsitc2nmyvWZXjAKlLNkYPOOJ1RE6PUveZrvSHuMnQzHEpQpPu-RP7to2K4d3-qe7Nw9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=DOuK4HaJLiDMVt7lSC6gdy_REGKmlW67AASx58Z3CrZJdzVz8bwW5c0yab-S0ly0cipy8ghFNnQ7r3fmmlYsKwtxfIEwjsy6sLTZzxRGAXQTgy9_hGjV3z1IWVSYpFyN3C6Ld-EQ8Plx2dv9Kbs0zSLF37phlcAOLk92CO1e6xUgLzLncp1ZY9yq9hJmLzN_72nca-ow7WTi1mhvB6y-nF1Ds9AARMMzWHKa43842M4ZdepA68ssUVkAi0gp1lpKyQQmp3MqnRKBeINCqsitc2nmyvWZXjAKlLNkYPOOJ1RE6PUveZrvSHuMnQzHEpQpPu-RP7to2K4d3-qe7Nw9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQYl8Hb7Ml3UY6EvqoUgKrROx3zzZhJYJyOyEXL0VELcaaf5TwcC3W0kWV-zH8Ps_PLoA1mAL1yW7uNYdcDZX08R3w8k8eYgHstC3FsfToJhmKm0mrB2n8JAaJl1VF3Mhqu6vGsgj660wQSq97TtIWAb0YsSvrnhuUn7fR9YwZhC54lE1YB8qve60TwBvCq0qfHzJxH9of5EzHyd7tZBC2f2HTj6vSSJUNUR1t7yj8z48up6X7PxLTPRxBze8XcWxC7Ef64-rhoTFJOGDAk92Xo-HeCk1rnSUs7S-_L4KJ7IYgnWe_sLRn1Vx08oH-zLTRNM9yihfl9EJ7aeShQEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhmGIzbRibfXXCZoJdTTTmRNEi-WV9a-WqrP4amJUeDCA4HyuUO5EEDZYjCzXbMNEJrq-eqldhwQCW1KCw9nsTnUxBF1OWjGjOJEoZkma4hBDnyssPNyL15yWV5nbzBf6J7wAOwlsP_08M6pz3LzzgnxVi2MibtVdkp_eL12rZzNiMpB0fQ1br4aBrQS74iyDBwk3sZdDj_pt7atz_HsaSWsxY87rq3hUt_BkJpeIYz8lNX1qnUCdpHn4RQXj6Yn3BKV_yxvYNkyQoqpXrCD6lTegiFNO933k4Ltd311U-Mhx3yUOwUum6RkAWNGf_nozUgl8Fc_v6kaqo7e-IHtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=vRLIXafoOOUYysjIeELzgXpKeA4hs6yb0Rgyb_xxrg-W0KFE2-yl8FyfwjeDPr0F0T2-uIjqprJFa6Rofem5R1C01UGYZeGnePuY3YKOB6U54whvLF6zo0zLH3YHvDC3kBrdutXsW736iiMnFHh7iBWbrSBJHxzZqPUPDBapJMXv0G6S7BAGQXGg0ld6-DAGXDTY22sZ5c9QT_FoqANs1_ZdnVzlYnssULZzXviMkSsU9m0ilkboWk90jLdlfOkFHtHeLwpWxpj-lWHfAeYnJnCQYAgWizBebJqNLkW0RKkf2fcKcZN9Yh0Yc-glBg5gcSeBFCsUqRev6VWugUyDtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=vRLIXafoOOUYysjIeELzgXpKeA4hs6yb0Rgyb_xxrg-W0KFE2-yl8FyfwjeDPr0F0T2-uIjqprJFa6Rofem5R1C01UGYZeGnePuY3YKOB6U54whvLF6zo0zLH3YHvDC3kBrdutXsW736iiMnFHh7iBWbrSBJHxzZqPUPDBapJMXv0G6S7BAGQXGg0ld6-DAGXDTY22sZ5c9QT_FoqANs1_ZdnVzlYnssULZzXviMkSsU9m0ilkboWk90jLdlfOkFHtHeLwpWxpj-lWHfAeYnJnCQYAgWizBebJqNLkW0RKkf2fcKcZN9Yh0Yc-glBg5gcSeBFCsUqRev6VWugUyDtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLKmtN7x1TZTqqqf5QYOb9d1lO0HcMfqCO-jqEFQd6iZWAFNAwhCRNul-0qfxWYhDQ3ZDRTJuZkuHz5LlcSi2VKJU_QFk0VKhEaMEG9yCXhe_2ZZGNLhfQqEj7PgEx49H3uNly-CO6oVoeCGcZ00ca8P-CDNmKVaof9pM37wxtpL1Y0OKx2JPIPJ3ViCez7KEubkFO0gZcKFEw7Q_RMU3NBpT22bG1Hu3199fx3T7uQVpCYvfRcqL9aytU_W9J-E9oOjRfQIz4g40-kv7NiKZTcvS1R3lb6D_8wLjpWCpq4vG20YO9W1aW3kknt-dpmzmoIMXGgGYQSi6TTqIsg8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBadlCtovZc4kODqo4cCGblDjzII4gVX7As6wv2J6Pnzb6Sl-gIm9rrx2KDMtYsidczef-s2SRheJyouyCxjTfHiaKVVMDIIehMK7bfx8NjdCb5sdItwE9mAYXQi1BHgKMbod98A_2MIOAXToI9G03TatL4CO8ph2_pTlILpFzRTZskkjFw4gK1pKMCNCXpwv-lR8qZwsFpZ0YecX7X09eXP9RG2IznG4gP_Lh1_RlzFs6a6OeT8aETYLoFKYRqr6toRP7hWYVph3f425hfBA5q9SLA07UzdKLpCu3ijajIywFlFwOMAxQZ9RnhRKJn1TKI_DGH4husKHC3MBjxONQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-PeaiScKSvM-sQA2LCsYzi-HFHruvAz-vPsZSfdu-d1eMtYiXic_ulCZKGpr22mX3LwpRPihoiz0TMeOL6eeZwexIZ_FdMnbakCDIMDDKH0VypLCKx1tuyQIFZgS1OthXU7r-iJo3zUFChVI_QAhMkGAQC4csf8Y9cafK6fcZN8hjEAzMy8kNL7-7dNyIg4qs3sEqyyOI7e2xyT9G-PG3ecRN33NdnIFDBcqIsya4FMfj_cYQ44gRzAwK1AKWrE9pPeDdzcxVAsbNRYoxnnwFdINwIl6vUVqFOyrWfeCe0ZIbz3816gY9HnkqPuVuptRIV7KXMTxp_wGkQaI62RNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=r7kRjEfIeI7y1_8ZwvEuavqy-vN2rtGg7eACWPXUe_ilmCcg7wo5hvDsEMiAGn66G5J3En_YIL0J2yigbsdmNn4b5zYFZclqmN-1WayzrB2G3X7dEleBhvjCp0SWJ8Ddxp5nMo3x7mWa4GZfBuB0PrWK1JFr0qRLrYZF6GjFTlTGH6cM0eUUeXoPK2i2_suCpciByvmB5ezwqrALwtJU7y6wNKwosRduVb9ijrp9I_nGq6vpvSfFf_Wf74uWrhx31vrcyN8rDIdKu4c8HqW9oJOIyVE6XKbDprzBEv9qkiUCxQNlHelRIt_PyWlX8p1mNqHrmOOL_q-Bqjttn7ySdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=r7kRjEfIeI7y1_8ZwvEuavqy-vN2rtGg7eACWPXUe_ilmCcg7wo5hvDsEMiAGn66G5J3En_YIL0J2yigbsdmNn4b5zYFZclqmN-1WayzrB2G3X7dEleBhvjCp0SWJ8Ddxp5nMo3x7mWa4GZfBuB0PrWK1JFr0qRLrYZF6GjFTlTGH6cM0eUUeXoPK2i2_suCpciByvmB5ezwqrALwtJU7y6wNKwosRduVb9ijrp9I_nGq6vpvSfFf_Wf74uWrhx31vrcyN8rDIdKu4c8HqW9oJOIyVE6XKbDprzBEv9qkiUCxQNlHelRIt_PyWlX8p1mNqHrmOOL_q-Bqjttn7ySdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=h49XRiXAn0KI0ZVD7MTZzT8XB0bhQaMXJudpzThWncrvJl4C9dqqEgGv0qSDEWCe7EEVCHXHJ7VSi3iu2PkBBn09akH6j9h_zCBS7CaYQ-cMW0yMFvIOBfJXwlD8GWPy_wSCBuKsiu8s5RPbT-znQ1n2horEKc1sGrZm0jxaqkvp9VGDEACaaPCgxPFycFGKRo3PjgATKleyldVV6Q6EqmPRDVUrVJvxXoc7Jusz2gfK-mdI1WBF-rdM2cfiLuhO2Fbk_a96BQ3tnC853qeRWuMvc9v5vdkcC8CmRzvGkubLNCIefX1Pln7jKjsAFBU0cgKX4E-eJDkDW2_2GiptlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=h49XRiXAn0KI0ZVD7MTZzT8XB0bhQaMXJudpzThWncrvJl4C9dqqEgGv0qSDEWCe7EEVCHXHJ7VSi3iu2PkBBn09akH6j9h_zCBS7CaYQ-cMW0yMFvIOBfJXwlD8GWPy_wSCBuKsiu8s5RPbT-znQ1n2horEKc1sGrZm0jxaqkvp9VGDEACaaPCgxPFycFGKRo3PjgATKleyldVV6Q6EqmPRDVUrVJvxXoc7Jusz2gfK-mdI1WBF-rdM2cfiLuhO2Fbk_a96BQ3tnC853qeRWuMvc9v5vdkcC8CmRzvGkubLNCIefX1Pln7jKjsAFBU0cgKX4E-eJDkDW2_2GiptlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d95g8RVlqB4uW7yuUnZbKHsQueLbfQUNU2AK6q8SKc7P6bWfe09Sl-3n_oHJ_4ECZk2jmmCa4-rCASSzDFyJNoNansDz_h460LE5IJ-K2wyzzgX0lDPPXcTegB9fsuRVq2DD8VlSEbwJpT9pXWUf6wgV2MeP9CsvyF0aC8Pyb5RWgbuVIUdMlJsDxgADqpT3EvkcO9Qcy1Cw-ceg3KB6XiILtCQSVV5-y6_mkdCd47e3TAPkG_JpV4qjB8Zz_nxey_OqxRk4MGLLbChcpOPviXwt8AE24AujRDWsN3b9rXBhzIBvrebSYzpPz7NRhiQVHgBYhIavaYMBTa_RNIEOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=iKYxcejC9nifEW-_U7ae6U1N0VAv56R1rfMsng2j1wIngokQsNdsSv36C09z8y_Y4pq0bcNyrFmbPFgR9iXCfzTPeNM4QH37SlFbW298q3aXyLg2mycBKi_yGpYRAuAU6u0nQw9J5U-PsKuYIhHhr6Ie74O68BMeFSrmRWoj6esHrdO7HGraRTwJf4_kVkq2eB0sH1YgSYoS6JjDvg_LakASQhGIhp3F9bdCXPtBUSovRNyqipibFICZ-k3uNmFhYnJR4Kj2fZUrnHPaRK6i51QDiWmvgBfI1DMiOYaKOWI-R6MIDpRRpkJCFRU8cJl3di-CNBozkVj5a0mZbzltVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=iKYxcejC9nifEW-_U7ae6U1N0VAv56R1rfMsng2j1wIngokQsNdsSv36C09z8y_Y4pq0bcNyrFmbPFgR9iXCfzTPeNM4QH37SlFbW298q3aXyLg2mycBKi_yGpYRAuAU6u0nQw9J5U-PsKuYIhHhr6Ie74O68BMeFSrmRWoj6esHrdO7HGraRTwJf4_kVkq2eB0sH1YgSYoS6JjDvg_LakASQhGIhp3F9bdCXPtBUSovRNyqipibFICZ-k3uNmFhYnJR4Kj2fZUrnHPaRK6i51QDiWmvgBfI1DMiOYaKOWI-R6MIDpRRpkJCFRU8cJl3di-CNBozkVj5a0mZbzltVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUvY3bC0OWiqOgz3S1BVHJqlcannMwQmchAicomHoDyFeHfkyqgNMsUrwNuuYQxUqeXi1LICO17ZmjnFLVhI02iL82fQueijHPfJzKmEWvNaZn0Om9hCrTuqmDd5El1n5EaBvm-ps93W7VLyYlCxOXevPd8zZstXZzeIVmz0G-y-4jRjIIiwoVKSG_j-3fkr4K4oyU_AM9p8Gujo-I6k4Mtzweqv8VnGFcHPXBxyxt2Rhx7qEVv31otuJ6DpZVgvc6VBNsA1UzoNudEtwWvVa-oUH5v7DHHUDLVpeYXxgNKyu7NjbRg19qZ5LDOjG0Gt0FgnoYil6yLFgnkidEDhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE81ue8EnPuS8qtg_ohVVhIb4OAqs-DduIunhgPgCBaAPXU_nFlESfRMwy3CNR-oAirUt4H-nvCGO5jtMIxcs_AxgZY9O4m2ZwU-NHhRDzq5Wvun5_J9RN3FdsmIj7vi-5qIFvcONydnFJ98s5Wx7h0ZrOEYseVwrXLHJsI0dJHbiD6ect12Jppw0Vx1afrG8HC7YurpzzB4mS4Hrpda43pbiFq1Jf17esAAks0bXVom2UdC7I43LSsqiDkW_YDKUVAD7Irwln2jhzGc4pBbtfE6Y6nH02v9z8eULCLXb37pOPxdrDzInmurqngW1-nIt1BIM6KUkDTLIqGdpiZ2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbUxNzGq0XmyFBeCkrxv2sZPuPEmvb7nrPSE8VSIAFSnQefFAYkllnYfNnsJNKA5hEzdsA0NUD_NrnjXmK5Rj4pzal5v6nzmykK-BdV80dsqMae-x5cX0p9KQ5_rrVdXfuScKJ5BmTQdc0RiWuI3K6PClpukwDhCyMqMBH9A5jfBZpN3qRz7toQUZy574PduThDmG5u0xLsyWN-IMWwIPequEmmXamaamyKfiLLa6GDPOXNjX__2mRvT5Md9JsMOdKHjT8DLJ1CW9z0YUuukMe-QOuIN-cSKBFEgXqY-gBMjgidyRG8lc9m8zDOLMWvPuuFvx5qSdOsYJi_JSfTZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8nNrJbyJJcVSbdLh-PzTn9FS2T8NzrygX79DXYMDNolBGwPzovdtnv3xvpovTFF7JuZWMvqfBVw1Zt2IlG7yshPWTFrrobVU6DBGln9OhXsQFWGwqU_DbnTe6f6V_1i3xWk69xoLkOw1n2Xk9_Zbh2lTDvBDiM71fVS8HfZgiJU8IOnehOgWkLWODKmvYUWo0FYz8jTzJmwb1iwrStYhEfYWNiJxxScYpG_UvlBhIlB98Z0RfXbxyPzcLH3ipGGT01y2RGcKQNCazDfuU-uIpt02WtfJLkhyL-nyA3o75Y6bRI85mo34jrBPsbM1MWtFFHD7v0o5UkORvoo_H3lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKUc-XoZY-XTP3itw4inhUWHsti0-nbPiOHqDs7bzhC5uzq90Vsh3QlGlefZdZWEJk1Tj3q_nRl8ls3pAOWbSZ9buf88h-ZG8q8QaqrKOOsbfzE7vljSLxo0EUt7uQx8t9-1CWizR6clCmPratRay2aFsoWKfsCEz4v83UT3mIc8JrZcyATgVpabihxhHGudGvsp-P3CCsoiDHRlj2xYP5Pa79mtmSle1WfDsI1BvdEV0dBX5ZWYFaOVLjE4r-P_g_8v7yWbpUPNYHiUJeovpqCTFt88QI47YOPRT8sejkySDK2U2KktZh462Qte-KSoPejuKwD8XiLh8N_4Iyk_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=Uz9nt1sZd0nuD8S0QwgJl6If17ahhMqDh-BXnW8kBTYJJ1vYRByToj7Kzhn5T_NJuWoYLoiZYZW9z6tEHOOgzJFW6EJT9Gkim48Ds-OeA_fr-Fxj0phxZQNm0MCkmkKttyGvofVsGJbdU_hkfthukb5iB1iYb4RdtMFXVwRVHfWrOobFS9xs-Ws33snNBQpaO-59NuyxLqTnooEVfxUxCiErLAfrH1ur4hb9gpMbpBEmyzSL89Xdje-OOwCwl7Axxwe3ozzU01-1wccF8y8KpqMmxM389jdE0txpcgOLcUNhO2hMyZlusGWGzoUotglllPmqSGt4Ed9w-_gPhk2WHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=Uz9nt1sZd0nuD8S0QwgJl6If17ahhMqDh-BXnW8kBTYJJ1vYRByToj7Kzhn5T_NJuWoYLoiZYZW9z6tEHOOgzJFW6EJT9Gkim48Ds-OeA_fr-Fxj0phxZQNm0MCkmkKttyGvofVsGJbdU_hkfthukb5iB1iYb4RdtMFXVwRVHfWrOobFS9xs-Ws33snNBQpaO-59NuyxLqTnooEVfxUxCiErLAfrH1ur4hb9gpMbpBEmyzSL89Xdje-OOwCwl7Axxwe3ozzU01-1wccF8y8KpqMmxM389jdE0txpcgOLcUNhO2hMyZlusGWGzoUotglllPmqSGt4Ed9w-_gPhk2WHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Z8QTI4c0kWGW3VZYrL42nzth45RQOser34d9rh_Q188jhY9Lj1kq9mWTO0DdY6AQN3cMsAXS2NJUnD39R2ZqMhZQuqL2NZxwur0nhkc6xN5OqV_cScFkifLA-Ak9gmGa5mYr1Myo5gjj_pZyfKT8zHdHKmcrbmrZzPMtaODhymp54y28yp6ATsPe8rxceNf2a7wrxYB7vjWJ7OwyoqBA8MT39RC_EFqvvGnYQex39CQm8WtfHpMgS_iCWVwSdKpdLRyPpOZMN-Gc44IBRJZoP6_8YfbGO-Bnf8kfQFUlZVSplqjKcYVrOR2op4FmboVw6gPTUImRj-zIu-hhCYq0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Z8QTI4c0kWGW3VZYrL42nzth45RQOser34d9rh_Q188jhY9Lj1kq9mWTO0DdY6AQN3cMsAXS2NJUnD39R2ZqMhZQuqL2NZxwur0nhkc6xN5OqV_cScFkifLA-Ak9gmGa5mYr1Myo5gjj_pZyfKT8zHdHKmcrbmrZzPMtaODhymp54y28yp6ATsPe8rxceNf2a7wrxYB7vjWJ7OwyoqBA8MT39RC_EFqvvGnYQex39CQm8WtfHpMgS_iCWVwSdKpdLRyPpOZMN-Gc44IBRJZoP6_8YfbGO-Bnf8kfQFUlZVSplqjKcYVrOR2op4FmboVw6gPTUImRj-zIu-hhCYq0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYtbPDSWergYIeoTqNkU7uZJIgj_dCg9A5deUzsuwsfDyhquDxLfGnt4BQAjZ33kZV9B5qzvIyxVF59pMv4szOJRLvXoA8OpEj43_4By_o182XI6rWNveFAK8GaktqtW0oiXq6pTgoVNve11tal5kzRaZFEIXsUx5mhoc5Ms5xB9m7iT47WELn1ap2tNGIFYE3yQ5OWoB65UVyMe5Pb-l77Qiy1eigfI8y0dLJpAm1CzOv6LuIRP6u2xy9SuHjH1vBBOJqYji9mGma3XiH-p3S-TZ8KBHnLeFmGbr1tvBmDHIiFyKc07-jUSU9e7Ub_eCCAZZnk_Dv6fqR18eISDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=Swn0vFraOodlmNGNpd-NsklvkMH8hZ8EAim78x226AVhgCAPyFvxMPJFWzmYsDSP452pVp8J_-ZTlSEcVI4VSBog9ImTwJoZv8OQ1Ys-1OkcKWQvaiB1wWyNs_PnSQK20Bcuy_A83unjg4Gh0-1xTR4uYJrxcmHgpIq_6MrCevpPo2zJyNseclRidoRWcEq8CGmf3PDejmcI7rojinxP95VEZXXDLoTsnuY4S_HKLAK1bs9Rnufm1n1LLhua7QvGcQuXkTBtcYAiY2hyyEIuewvCJ8QLnCqtAJ5udNSXtUX2CDXc5P1bORPGe0XaFyjJbBkEKVqIIeR6iW1jcgH3uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=Swn0vFraOodlmNGNpd-NsklvkMH8hZ8EAim78x226AVhgCAPyFvxMPJFWzmYsDSP452pVp8J_-ZTlSEcVI4VSBog9ImTwJoZv8OQ1Ys-1OkcKWQvaiB1wWyNs_PnSQK20Bcuy_A83unjg4Gh0-1xTR4uYJrxcmHgpIq_6MrCevpPo2zJyNseclRidoRWcEq8CGmf3PDejmcI7rojinxP95VEZXXDLoTsnuY4S_HKLAK1bs9Rnufm1n1LLhua7QvGcQuXkTBtcYAiY2hyyEIuewvCJ8QLnCqtAJ5udNSXtUX2CDXc5P1bORPGe0XaFyjJbBkEKVqIIeR6iW1jcgH3uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=lUi4Nm7BcWpjiqF-I8sYq3BoOE4PshqzQhfi7ELEXB8xJT5fvd1fdqiwNi2MB7gJEF8GPZUkbqWWYDjaGzG3RIujGhqHI1zX14vIZnjT7Ug3ZD77XXnxXPQm9j2xOI1GRHLl9j-bpv3PJ3V81T0ahg77xxYLv6jxstX_uqnHST8tBlrEbZQzJy4sGX8vVfpj-Wywru74Bvf1CkdD1NsoT3uwNfPzEO8h3Wjq46p92G7Px3JsbtwSLTQROIEkoNfOua2kDYDMzeOwNa_B1Uq4nN1bnjUz_BMRvnUquVk-fSsDMeg9my0wfWYbBZ8NRQKrUCGDU8OmyS8h-JJKihBXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=lUi4Nm7BcWpjiqF-I8sYq3BoOE4PshqzQhfi7ELEXB8xJT5fvd1fdqiwNi2MB7gJEF8GPZUkbqWWYDjaGzG3RIujGhqHI1zX14vIZnjT7Ug3ZD77XXnxXPQm9j2xOI1GRHLl9j-bpv3PJ3V81T0ahg77xxYLv6jxstX_uqnHST8tBlrEbZQzJy4sGX8vVfpj-Wywru74Bvf1CkdD1NsoT3uwNfPzEO8h3Wjq46p92G7Px3JsbtwSLTQROIEkoNfOua2kDYDMzeOwNa_B1Uq4nN1bnjUz_BMRvnUquVk-fSsDMeg9my0wfWYbBZ8NRQKrUCGDU8OmyS8h-JJKihBXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElNllBJdwn43mY7ukpOyMEqNunowxMrV3ltSKQxJV0ceJgOq3gF1JYQJymhEOE_Gm49BT0PbEVmIcthVs4RZ3kXVoKquQyEJv-oZNyBNKvskRJTiZwgtsm91rMeUaHVtZvlgXxFs-g5GQv7iIK3hThBhhcFMu0Ys0VEWYe4084CGlA48CMvpyU9Rvoy9AeHjeMSvu0-T_bh5u0mo1wl6psV2DvXYdV6i3D1dYTGgyyjxfOhksBBRMsdlVdS60C0bVKdYz38D8t7SYCDOO2KuXHZvOR2mgw8c-I7UFjyHnQYg7-rm7ZgxByLgQvBSkxWGUOhflMCn6EMsU_jtRUGR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggU0NyNJvLgNIrGEoHdoS1jpcPCGrB-1qqKg5gpladnTi8qLpFwVAYHI86wlvfZ3wBWvq2pPnOv2jRxwsc1a_E4I7JJB0p5QL_F2Np2nVZuz9ndSpacnyhqP-xOokaXUIzCaSgQef1ga_dsBJF1j_S9BOGqI9FAYVd47GPujQP5ox4FkmfSWdm5Zhhepol-sqxMVyxhovla3T5bG6w9tcWti2rO73S5IC9f1DV_7pIhDS9PfsgpD93648bfCvW4-RrzRFZ92aeH_hy61WRqU_yDV6g0xPUgAyLayczh7aOlGc3WH8_1MDJc_za0zYCD2fejPbWc0MdfZIXfoFmZ_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvfX7fqV1uzdD1Gxg4tf9c1BUWO8az1mAbIqAOhwtB0b_UyIi2RAy6RvFyDYSinX6FlGwJxqM9xNFkGe475pJhVT7EAJTMg0_ceC_94qXtkBe0oHt-Kzp9LEs71ZXI6M_xye-X0a0eaRw8YbPol2WSizOJ2SXB7DoW9PiDHrBwVpJYeLNz1nK_rnDuHGCP6ckozcnmZV6J8sIiIjmNGaPdy60VWhMkqcCzhYOh2zXar2WCNQNvHmePuZ5IQ2XV3Q-bb18OIv58OnFBi_QgqTrZp_yDfe8jEsPi5908gL49rYue1RhvIoXLMfahKmY449EyCV8xxknp-56fwbwfbDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=NioKtaN6a730o9xMrXr0F-WFS0v6-wcsFtON0oma8OQHvgvDD9EBEvC7jj_pbNU9RIuYrGkozwHxL5aquh2m7wxeZAwC52Nv9rcREyMhcjVRoGxBzOFMcPGJowzEDccf_KwM7_sanHQHtFWHz652HmzF7OsdODHaCj10HSuHFmfhT8LBMfgV0o1PydDiHO3kPRi0N11vULUTOGWma95Zl_Nt1gGN9QyQ6vFFM4YKWOX6iaznTCRib8GJky6K2bsJS-sxi6y1UtKUg0e4w_eJgZtL-9FmHuO8e3MWNtU4J6D-TBDmLAWGZQm4M3iQdnyZo7sa44viECtVDs8jGMqjEAFnBMsM1E6VopDas9NC17aE7z5gR0V1c5oZCqYxtjqouEDgG1DdsUTFq6AweNfUgt-B3IGDVo71UCNIW2JQj9SMw4BmNaMEal7x3ojV8Ou0m5TgyE8qIsIk_TJsnj4TEeYbw9PEZ3B2p7hXuzq6Dvhky6O9nMLkxr0peSxSADjvnQGzOthgIqbv3ePVI4yhgX2dSsErhwHykAbk7Bb6vcxhoUigdCZM1l12XonzeijMCDOQQJ0oF1r8zO18vvraXL-thKisbEeVIGxvafC_dN5Q-fHjcqbvnKRlFRi1dWmP6I9TOFrnL-Ae4DQ9R8pU7RUaViwX_xhk8gScxEt63GI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=NioKtaN6a730o9xMrXr0F-WFS0v6-wcsFtON0oma8OQHvgvDD9EBEvC7jj_pbNU9RIuYrGkozwHxL5aquh2m7wxeZAwC52Nv9rcREyMhcjVRoGxBzOFMcPGJowzEDccf_KwM7_sanHQHtFWHz652HmzF7OsdODHaCj10HSuHFmfhT8LBMfgV0o1PydDiHO3kPRi0N11vULUTOGWma95Zl_Nt1gGN9QyQ6vFFM4YKWOX6iaznTCRib8GJky6K2bsJS-sxi6y1UtKUg0e4w_eJgZtL-9FmHuO8e3MWNtU4J6D-TBDmLAWGZQm4M3iQdnyZo7sa44viECtVDs8jGMqjEAFnBMsM1E6VopDas9NC17aE7z5gR0V1c5oZCqYxtjqouEDgG1DdsUTFq6AweNfUgt-B3IGDVo71UCNIW2JQj9SMw4BmNaMEal7x3ojV8Ou0m5TgyE8qIsIk_TJsnj4TEeYbw9PEZ3B2p7hXuzq6Dvhky6O9nMLkxr0peSxSADjvnQGzOthgIqbv3ePVI4yhgX2dSsErhwHykAbk7Bb6vcxhoUigdCZM1l12XonzeijMCDOQQJ0oF1r8zO18vvraXL-thKisbEeVIGxvafC_dN5Q-fHjcqbvnKRlFRi1dWmP6I9TOFrnL-Ae4DQ9R8pU7RUaViwX_xhk8gScxEt63GI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6a4wejEGVETdrhEFWNSWG-4WN0SoO7vrIC0HUggMa9TJOi6Jo3UJnNEzC42E1DqU0lt3_DM1gjAIViqnvBo81Y4AfugvT4g7jhQUC_yojmtCo_3OxjvPZAqFTKYJIfscIULELaHfu1R3zHEASvXeDbU3STHbmpzQ7Z7f1Z-q9yxO4YPcU_ihUeNmKC1bCLvjY9vksQ3mJSiQAWsz5ZT-oet02FMd_TopBH3WaK7Vp88J96csLOx68TNedmyorm5SSFyANmcsMZiir_KxG3N0Pvb1ueGGgNtqlun5O6VJxn7-Grvs9FwMvShansDk-7STk8LPTlqqoQ61dtr5xPK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7RHAuW-NIV45rv-yWC6abxm9gnFIljO475qgyV15zthHEEivn3Bb61NaE8DbwIkxHQaggvhs9dL-WVzSpidGPwVs2IbSPiHb0wtBI5d95dwfeQJicw6ElE4ZfiDAbQHOiur7RjyvRHsALIeSumBz4Xqyq1-aG5GMHX3EM2vTo7Y4fAIw8QUzh6EAMhXsyBBtoHcBlXo8SR5WFvYD5YJmB4WIc5xUBr5M-0V-Sz6AcbvblUL6kcU_5ecLyF3VL-_-RxxXu9KgNGW7wPVOi0IVraXO9TYP2i7iFqRKkCh-d1vXo0Pj4UwrRPojbFOTzNtOQ1yzEXOBiCf9cpJTkOf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM9orWJnoqNPzDpTMsGQU5QlcfRPujcjD8mNmvv7yvT_5q3Af0kfyM3X18cqgAM1AVrC1fUmxcWjKfWUHcY-df6427Q_8say83KZxev7obOdJOb-pV3Q4r7qvD-lpiUoFG7IxzQ4Iugo6TTsN0VsQmiSdU3c4lP8CvlhuE6PDAJs9cSuG8lPYrn8kTHOxnlaFN6Q5Ap0MbCJFN7DOZCBYSKWByz1g2b7onx572KI0RGS33CYdX4TI4J-Oja3Qp7wMznO-gt57cF9euduCqV-5iExYTRf0oHeUDyn8dwatiXHcPQpZNOytAHDDZYgS1dzdVYqarm8BozuyeggnKzMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFIvZ8NGoYWDOz5Q7hLSUJelHwkZ07xioTyqOYKVKTRPCy9ExoecjhlD54lIydBHSy-hTkPSppegSjpGMQvYzCPgDz2GCZ6uGOVbGEGMQuB1qgfat5TVieCTxwWghSfGyIB7IC_EWK5zNFjTTU7t4rdWXwmU68cWLAJTarMzMKIlyCEFLEY1671Hu8erm7-2zJ6WZRzZD6iyMwpNp7lcekJojAw_OEVpzi9zufn-94O310qmCVA_pHB-6zZ1cqRlP7IXfLFv_X7Vw8eauxUlf5WPJ1Nx4yYq9GdvVbx9LvwnffwB_nXf2PwkT5u4K7v96abdsTGjeqwAgfial0qJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGeb53esKobuQg76ybSUMSeOoHt6ZIjxHvNvsCQ1jkvxlvubdWBIhBSXs13-lOw16vgDBF3B-bJa_L6a4YGv0sOcnd_APrdoFoB-t6H-5L7DcUlMQj_WAR_OOiYjcmJ1vjQ7ziqg8nSuCf8WNXVAV_IorKM9ioc3K6jiwGqZ3XWPWl25Rh29JlJdSgqrV9nIv-pyIqkX8xWXajq4UQazkVn00wHGZivdmrmVzhX4Zxy_DP3LsoJdYf5QqTIWvMX0t2krV7MvuuFjrct1b7vojIXwPc5SWoYUt4wIbz2_x8gFJCMPQPoZFef0qG-BvsLsoYNO8RKCVrQ44DDAm-VDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=BUvo4uwLrie9l-tRdrxcYVM1uiYovVT91hW2G1YQrNAU2_zhUnI7M3W6QklEPoA4DmgJukCrWKXdYAhA8kPeYk9acGRCCLKg8w7UTYPl3zuV-7POu3ODb6N3N-5o9ye_oo9SGoxTEx4taQ5Rsysz7wopUjxylozuGx2gl6cWejA9JBvgmdu0QwCCwTWJ3MVf8EU26_z80muZ2aazHsaqG0bWoOqZSdwhQfvKer5DWLjUxEG4ziu7zADww1jgLhTv496iblGWKg7vELPTpGniqZkdaIlGJYqyfEy03Niw-Ni7_B94p5zIKmDCBCg94khpo-nbpyw7XPccK1QnW1GBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=BUvo4uwLrie9l-tRdrxcYVM1uiYovVT91hW2G1YQrNAU2_zhUnI7M3W6QklEPoA4DmgJukCrWKXdYAhA8kPeYk9acGRCCLKg8w7UTYPl3zuV-7POu3ODb6N3N-5o9ye_oo9SGoxTEx4taQ5Rsysz7wopUjxylozuGx2gl6cWejA9JBvgmdu0QwCCwTWJ3MVf8EU26_z80muZ2aazHsaqG0bWoOqZSdwhQfvKer5DWLjUxEG4ziu7zADww1jgLhTv496iblGWKg7vELPTpGniqZkdaIlGJYqyfEy03Niw-Ni7_B94p5zIKmDCBCg94khpo-nbpyw7XPccK1QnW1GBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZgbSaSGL4wSx9shDsD43HY4KnwbAUJdsHvPpjtYTt8ju764ni8BzNkJU0gmnv3NXOY-Y47YZp9hy0tctUGxk8oRpTKbCypF1oW8Mm8fFhZeWWtIntIs23sBgbZaVQKL8igSeC27oroshzVf09hFS1SbH796DK8Sw6sRa6tPIQJCCeDXinEFcQ9UPavxUY38cHfsalCVZCKdBUOnugkYmCz29Jz7oxPBvwC5bYfWcm9raZRGlOAVk0sbACiu-bFU7w716-q7JF5NtyTLt4EI9nFMWVaA96eVB4TqmahVJY1KsWgjlKGlkUqDFZ6OOtN2J25eBS6-UWEMxn5oug5GYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlaxCHuUFu81T043P89Mu261Eml1XXKJ1XtnNVmg6beOiZkorjOmAnwMCpKQ4aoxWAjshw17aRzEv7LlP6BiNSrlIUFM2XSLjzrHxqVtODCjzCSk-WdNOlVOdmXedUJsOP_qUglzZPwQLFTs7VKA45dqCuAATzGkj9LHVPuxvwUJXWWR3_1YB4tHoG7z_sXJtBPiI7fogTP0FQNjyw2Xm0TQLnWSuJGIAENsgwHEwdqPUL_70wUAj4J5uJI7cNNL_BVqiBuh7uB011xTBLJAqGUs4BSjR35ln1LqL4digsquDW9TssTXqbkFI50PTvvp9q3XeEQxm5zPNo96yG6QRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDpU_WhM404q3IqzkkWYyRRxff-UOX3Xz7n8ZXsJd1kF8XULpN4eQkVVhLF8t1jb7gdrb4nY4TDZQvwSph1Ktg84bocg9I2P3sSTfmW9U2hfcsn3930g69h89xXlIVLvi-m0NRtGx5YY9-B4yOMCvEhc2a4XE_8qRQoKyHFe0SY2ZM1CIyJHd90_WnlIUU1QKzWg1z4RWuhos7zRiY7EBbN6u9nRGzhKVO2qgbo523Xxg2dgLvCww0CvmyEVGOXSIvbNHHJTBlcYrbfmWAKSskdVW-tDVNpsctBP6AQVG-ZDg_ipcM_01uMuy-OkmUJiaMEk7YPQmklro0Rvtlnmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=Wua9t35EvIeUesfnepJYtFsisDqn1IUVQLCfvuwbMwBpXQEDXANeFoqmIEdJ2tQmGRXvxMgYWJgoQpEc5JbQFdNuEJdACzxkAMZ2wD67IJ7Y9vxpSfDCBuqz9a4qlpAplHpp5fdxQDM_ctW_tkvi6a-YhwxHoXDNDN57S78zFXnEMHsNa2xrECUUFWuRCJgqM5yXbCZiogVkbHunvmSrwCR2CHwFf4DQjgFBKoiHi1p1pzmm6jcIqrWHxlY9PQTCdbLU93wZakSpT5LkQyRcV12Tx2mkovvaFHNvzclwYcjAj_cjGc_s6KIrTgIAveYA5FMg1c9W40xa_w_U146A_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=Wua9t35EvIeUesfnepJYtFsisDqn1IUVQLCfvuwbMwBpXQEDXANeFoqmIEdJ2tQmGRXvxMgYWJgoQpEc5JbQFdNuEJdACzxkAMZ2wD67IJ7Y9vxpSfDCBuqz9a4qlpAplHpp5fdxQDM_ctW_tkvi6a-YhwxHoXDNDN57S78zFXnEMHsNa2xrECUUFWuRCJgqM5yXbCZiogVkbHunvmSrwCR2CHwFf4DQjgFBKoiHi1p1pzmm6jcIqrWHxlY9PQTCdbLU93wZakSpT5LkQyRcV12Tx2mkovvaFHNvzclwYcjAj_cjGc_s6KIrTgIAveYA5FMg1c9W40xa_w_U146A_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdL9lg2n7hit37g2HvFCm7fMZ2sXgrby5ttKF4yL28n08ehHnoscM9a3M3nq6XX-tIDemU1Pyokw-l_UQ-JavdoFR-qVPoz9AdEh6juoI7lWJ1_ac6bihHPGnNOQVWXeGWxJm0kwjjuLczOqg6i03RAGVggavXn6JkKfPjCez8_9KKcqlxJ5K9A563Xyd8VHyXgxXIkYqOEMOLm8udIwjiMtLUzDkmwARM1pYiNMg2Qzwu8T2stwlHU3PFYo2qVaIVypCpl0nN11Vyvfx4tc4zPShnOqOZ4e5nkQkWe34BO0M9uGAcgxNOP8mjXUYEWWFB_RKkfGKwJlCIHvHTwkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyrJTvDGpzRatt1di6LnCii4GNbTUbKwFJEj9fdIZmgmReGvdW_sv0yKNEtFRqXXDXFczto3z2SAGFP56Gl-tIULIGfxCRbIQE04baAb0OtN86Bj6dNtURz3iRp9P1E-cS3OxrMy5SRQ88zAf-gjcg1FHUVbi4vGSAM-JbOCz9zy8ZYTUuX38D8zZ5dtI6lpAMk5k-pFVRrRXHEw3gekgaDawT_bUpw4XZ1f3p2CKpNuYwUHXKgcCLrsQpN07RpRKkFZLW9Vv5-vp1jT6IuMCVbufDtDtfs8rKhaRFK8iq9vgFV_MMaWjRGgEjhM9hZTQDLj2BxP0MQKYDcs-x9UBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkngiAMirPCBoVTC1a7-WJkSJ_1nDFgNjrxAgvZXMY4eaPl9ELrmWLgVUqMhwXmN4rMvjTskcUk5TY9Y1TOGWwtJRZgy8Amq8KL3I4ZFPxPUmUymoaWUcLbkwbdnt6TZVL5KNkOrBE7DewPIy8I4PvBWnNvPYpuXgab39uL-90TfnF2R9de4yILD8oVsrpAQkJJmOlpg3ojwc55A4BuygJijBESiDR5G1hVkKUe6YySsTk0AWFFoFC53jw8yy5SjcV79awyyU5xHZPuGqrUSYOfpda9rk8ds6avLy0_xSg30GOjUAJ2MRv3Zzg0Z1zY5sCdt-tpyBzYIZ2FCw9S-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-uWJB37m8Sq-7yPie2I7cPIynZ_bWyntzF0HK0KSSyLeOeqVgnuynWhPOLOJEApu_MgvHLjTR312glJHind7nEryIS-95feQl1ARkaNO_QdHNSlihRApxN-8UZlSDmasRCyLRm8AjVHzSBQOdKvxswUFUB-ZKLBC1ypWEaJgevURAsKD20yMLfsuvY05Lu9098nd7aYeEefNvEkp8Uxg4lYQEQMEKPXV1bL3hGmhmm7aHgGr3T8X5oMgOwWVmVDegRNCjmciRvBvwRFaGVI0CEDGW5i37CL-HAy4aDPPU0T-xnslqSO_WseOiTJe7u__PS9_CIqz5Rp9rJPVlHD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAMlC8oVBeTu5wW-EKFIrbKGx7nq6GxeiCcY4WkEEtFXHMO6emmLBY_99RRR-3-F0LENCSlAiCUZ75zZe-w_YwsHX7_gtjyXZ_QLi5s-2Tc2MK7BdstghEhv6ZytH_Dk13zvxmkYUhMSLBkcIHwNk0AbJPkXrgyfgcN3FEI3j0aksLHFIiefwbFbMmoCeZMZL63aYOmn8WMrHK_G3hQJ41XCus0aqQ5e-nFeKz54XHYeYbxT1SYVB_Y2SLV9gf9gjeVh0inYePOZf4830qFw8IXdY4mk9L5fJ_Hh7TJ9a1JsftSSNPlrxLdQUzgDeG4rik4n8y2J-OLEFhvWE1mqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=fZA_X0CWWoYnQLx50dOk5ElV4rAOY1_dUBPzJg3_sdYAa9b-yPN-CR8fvUJ7jEMSD9q43LMQt5EByunpjEe_Bl-eZj7wwl4Iyfh6_GDCVr3PPhXJOklrMHFQEwjeMkHU774hZImu-uB8Ot5A-qsipmLiLqMDllGOeVkwLG1O84X0H5_2ofGBpSaLjB6KmYxmZzUU8Ywo8A_5YNBL7u-UrqxzA3VKufrukqdtknr1tKQ8JYksN15Mb0jMOigmlHeL9cCql0mBKQ84pHF2kVISuMiNxHM6ZnGICuBLxj3Kw6xWnFHH4P6kq2vK5zPDHjaujwxQULJ5uip227kYMrs17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=fZA_X0CWWoYnQLx50dOk5ElV4rAOY1_dUBPzJg3_sdYAa9b-yPN-CR8fvUJ7jEMSD9q43LMQt5EByunpjEe_Bl-eZj7wwl4Iyfh6_GDCVr3PPhXJOklrMHFQEwjeMkHU774hZImu-uB8Ot5A-qsipmLiLqMDllGOeVkwLG1O84X0H5_2ofGBpSaLjB6KmYxmZzUU8Ywo8A_5YNBL7u-UrqxzA3VKufrukqdtknr1tKQ8JYksN15Mb0jMOigmlHeL9cCql0mBKQ84pHF2kVISuMiNxHM6ZnGICuBLxj3Kw6xWnFHH4P6kq2vK5zPDHjaujwxQULJ5uip227kYMrs17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=TXlP9apg8lA-pITNed89N7XYIz3lBp4VXaefEuxaWK1gR6noImQihnJMDpEdHvMQoT1kqRxkYoJwfh-riMk6v5roeTEIVXnPea47Rp3h_AvfQtTRSVK5MPUwdSR252DAWmQADgctpw_BGAbKtXhpm4WgEL9d4BLOkaUlTnuHh0plN-Ihs4buOW3jAet-pgI8Fb9N2ARs-v-Hk2R28RRsp-aYbGX2UVSBGEMsIwHKvHH3mMQ9pcXwmb7VDb7b-t_MOWgxP6ev_dtQVmFXa9Bw91HkpZ_-IVX_YoxEqKqFpnJ6m5lhSAJW58RnVUvqwR8GD5HaDdXWLvZJ1cZmmhktiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=TXlP9apg8lA-pITNed89N7XYIz3lBp4VXaefEuxaWK1gR6noImQihnJMDpEdHvMQoT1kqRxkYoJwfh-riMk6v5roeTEIVXnPea47Rp3h_AvfQtTRSVK5MPUwdSR252DAWmQADgctpw_BGAbKtXhpm4WgEL9d4BLOkaUlTnuHh0plN-Ihs4buOW3jAet-pgI8Fb9N2ARs-v-Hk2R28RRsp-aYbGX2UVSBGEMsIwHKvHH3mMQ9pcXwmb7VDb7b-t_MOWgxP6ev_dtQVmFXa9Bw91HkpZ_-IVX_YoxEqKqFpnJ6m5lhSAJW58RnVUvqwR8GD5HaDdXWLvZJ1cZmmhktiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=TJ0OTJBbXZzq6GZg3ZomfdYTVpdAwvVsE879cMXo2tcr2k27kOPKmI0hFmvRikyfkgfcMA-O8kOK_joX5zLn9y3NGJ12UeQ4fZMjU6J3bJDl72oVVZMz8nqbLDSYFqXpw6Pk8pejmndMUfL5LzIkLexiei2kAXIF9toaRUeU_ie_kDKAT4Q6LsfYZQwexCdGvloAQWbA7NMb8tWeliWbw46PU2z0x26_coE0NLENugDA7nt0gK00SjLSYfmbTFDkirArMVI0-5vgzu3_JmimwD49sHMvp6ZWjKxm_uH3C0WN7KlqfzfXpepMom_TJpEYNGdabnKcXbaxPgtGXs6PtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=TJ0OTJBbXZzq6GZg3ZomfdYTVpdAwvVsE879cMXo2tcr2k27kOPKmI0hFmvRikyfkgfcMA-O8kOK_joX5zLn9y3NGJ12UeQ4fZMjU6J3bJDl72oVVZMz8nqbLDSYFqXpw6Pk8pejmndMUfL5LzIkLexiei2kAXIF9toaRUeU_ie_kDKAT4Q6LsfYZQwexCdGvloAQWbA7NMb8tWeliWbw46PU2z0x26_coE0NLENugDA7nt0gK00SjLSYfmbTFDkirArMVI0-5vgzu3_JmimwD49sHMvp6ZWjKxm_uH3C0WN7KlqfzfXpepMom_TJpEYNGdabnKcXbaxPgtGXs6PtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL2vd3OfdWlyg5u5Aoah--UfY2ornKKaNoRHivyhLK5hpGTHzTK2RUnAMr9nd5TWuhoDZBkqeSbwYBZ74Vv4FWtx4E3lh5n5bOMuSLzStyV1njDLAbmRV4PUZ2pzvlySjA0baQMx78x4PMp-gIqUgclaDQ4NOmTbUvbM5G5_9lA4_vJIUuUNYsoD0QKeWp1wCG1azdQCSXpqrEO9FPnQz0Mxdf5GzYSyeZG-wYbREwGovYtBuRjQkAnvBHP_8iXY9KUDuVEeKnRrIrGSPTlnImX2scmLFNtOkGDrcxBstbiSKffO5Ko_YsThOUemFWwbaKtRu7g0MMveoAE3rEKVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_8KYdtOjzIq2kKMRizoehBG0I29EwSplf1v8StWe-iBVwcg4K5QfWdvs2o0N_mOoXe5YWBQOtS2BNLY1Tda-VMElOlS5C0zZL7_U2pse2G6N4Cah4udtv_L8LXuz-oVE4IHwVTMSLNecWH8gZfFNSqQVZez7Uwu3ePkVsuD8N8IykXrNGA56uxjfkn_x9IfHfRZqxAIVTBdWvK1FQvo_WpIZIXMoaqT0K-Qcv6Ytlx9doDMQB5heb0zJkAk1VeKzovcvxOh97Z2nr7GPt8JjzBYfBPToNhfjwhOptGxCI1jUjN_xaOknw7yzm2Sw8ghyjKhg8yCHR5Er6Tu0fsGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAXVSqbb3yp3VFiEJa7DgIHz845YI0LiP49Ylfpgl3v2aHoDG_2yQqsbFfmK-lwHK4-pVhHbnokmi8-m-6tWw1Dzq-_maPyBVy9sXgMonBrcIWl_FWT0syy2pGtLXmZYJ3uBPzJHlHqAwqWuTCHOmiclfFtMLBzSrgrUpQP0uTLnx7oaooqakRaTkVTZHUshYDJKjmwsx9FS45JdJyVoUoe5-stJwX72J7IcxgnT4d-AOBON2FkhhTYByqBLqyB-Dtl3jWlSExYHdggpCxjcJ4pefEFlSL7YH6SAkFhydeoLFlUPfEx_yeAgTE5fdHB5GWvaoMxnp96VboIMCXef1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUiw2Mmiq2jqEuJ2fBM9I3Sx2P5wQ2Zu64HnRpHV2uofYH3o6hOiqoUSMETX6srFGogn61Sbk7KXduZ17YE2xA9eaUBhi2Ff6u1anGqS5beBOhVfIm3jzS9wa9M4CGDnL0-SbptRWJdijkOJ7CvOI_xVXnradxMWlaOIbq2HeWUpnOqtjIJ8qXTAF5Fkb3T73rlpSHyGEV0qscYSkIlF2BNWiDE0g9U2eeCy0lDXLaUEOsXtpHzpTef4BhaRXld2yJFzup69kglOL9pAuEdRj6rSwLDULgZOUDBSf0goCskyJ9apfaNLUHKGr7m9DtmJ7IOau3Ji_lwICjxbCXSZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR6jTNZOtGI5V5sYT98tOCrc0WNh7KgGUlqOOzPN8kMd7UhLsHD_RIrN2GkigZciPTvT_8cJv-wtovE5O7Rzsomzpxb1K-czl5WmesfOiLiI3oxmRzp_xJsbqqJB9KqqQVmRYrV2AjDqoyBh3d7O53tTE-tewTrem_IW-NG-rP3H75sImehmTmBTYk-tJT5xw2AXzxgr4Y6XOiAvc8Gd5hQYeAnZa6ybLtDO_jK7inOltlT2pEOqoE6OW-Z2yOn-yuOPqMhNWPvAtYVdYTmpP3ciwU15OuxenpJCmUner8JkSdjCO_6s0WyFbI8F5WRdLN9hJ6UHedfkgptUSnB-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQrISP_nufDHp9sk12E9WpeyOO619CWA4K7WOvGdWDJC19Wkvq4w6nptCRItQfimgN4gdwnvGyCuKkXcNTEhEjIA8HkS1bYqaRnvUSLPAnQPzoyHkxET9cX4RPS6av7yuYrnDvhPGNjCYNsOZBv4WhD7FaKXwowzigokIVQe1a7aaMmzbKj9zijVO7jfyivvcWGgTjAe6sQZ69-oZdxqoMrS94ttHP3oCzOyYa_nRcfjZ141nFMT8hcsfhP1n7NoJt7sgROb_LZs4eXY33AfFjTLTRdCEtSV-vODuOiPNu_9EWJg9ZNUNXWYiLVQbBlfuMgrRBB70X8idv3JNJrbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iETFcAfapTVGYbPTeWtjhX2--PdgNyqbuDtNsmIiKrhCcZmfXBTsnv6f-69NIivAv5a8kjYokI82JIq7LEN_CXHwHsAlWYWrHzW1mKk-BzPcea7NeBCFTlEcFXsnNBtNZjS68-Nh_edMi-Lkc0wFSI89_Czg1uE727KwdDWOdCJovWVoVGJaqzTG9uovbyr93hcaUZCUnwTS_-hiSQ2Nk8iUCuyba2Ll1Rae6UnwZ4MHfJ7B1KTANpKW3BIrTpAuUobBUM45EDxpDd_54o-kqDodvhYzRfMnIkMm-pfFenooQrz6_rcBab8fg5XK3EuhlMKYPxAeSCM6O8Q2q-DYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5_SX-b9-hi7Qysml1z8LBe584SKelHIst_pZRIyyZ-wWRKRg3KOoQGUOhtw_AJwJV2qXVHyuzqwdv4hKB7i2Kq03l4ktTuEIfxaUEYW8VnR5dFPnO5xBxs7Crd1q7jOm8MT0dbGN7G73kDl2Wh1fuFxHREXXRSrKugGxl6iUS91SxIzFy2hiyd-YhRGF7GfpzHr3gLTPTYy1-MQdWgrjb2I-0iP3YjMQngwrzmByV2wxsCogXtmOLhk7saW2Y3lH1XqbLg2KJbMlocINjLDnTORRl6pJ4aEO7l0P7OYhTjEabPjsoFSiWQy0SUcs1Yyoaz-g4L8cjgrXyXgjIYh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
