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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukJ_B01CaSBwt7R6RaF4WpI2xyOCOv8Z0vJbb5hCTWvWGj0-9YB315EwGDUwBhwwiHDwngNHoo0Lj68X47X2w6pxRXe1QDmo7Bpb59kAGFM2EwRzjuSSmR5WjNx63V3Tubbf8YvtcVY3KZpXST0k4E5BRIIRHSXFtHiH1JgwVL4sjpGWSlh1lPE1a8IsncZ0MsitScVqRNpfv_onA4Oim744rBjftn3xLb4Ogy5G6Y1_ddSbRBo_KThDaiZLO2qoxr1Zv9LWZMc_LsgVEhNHV2HZEAtqm2VV1CtUUu21u820OzR_ix0bq-irvSM3Ou_X0qUE2zDVgmGjd8GycJS9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXntRCzX5_llerWe8I_BojAodCJKRdLkRSTaKEzcwfA7LM_0RXLs7Liwin0cWRZDOwLeYWp1MM_mMw4vM5-l-_Jr4fWO3gdx2DpAgE_rEUvGPQznrEQl8sYTOq0iziTdcIgGHfoup340Ioof8gi5KpV3TitkKTFwd9hBeKuNUWYZkweF-RM8i3tQysz3YWR35DP3de9QG00pPDBFHNLeCjfxlbZZKzuGoqNC6AcfUesEm4SvjLarbPMGB9V7IJ7MfYlRrxIax_vI2nqC59VkhYZUXFkyo8asySVa4rDnJJ9hjcYwM3FWPHOVrat_2UBpE4lLt8mUfq7tKSTWswsDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDp-387yjF39QLIM8YF3Gk9ELwtzT4_4_6B-h8-qbngUZ2fBgrQE3DAGsVxHI6oXG-A06kAD5tUcoL68owOc2otqB5LCsW9SLqvFN05AzZRPlPjiV6QTj4jPE1rta93hrZI7sD7noXFOuBKA4VOIAF2OyPxwr4N9oYY67rqjUUM4wzh_OkRFlNy-a3UmkK6H3vdPJ1DPLuSTqv7_aESMFyRNpBWN7hgQdVpPhnzWmI16lJdDz7tGMiDjVEy02ncjes_-sceYyTGZW1on9h_Sr6YJ8TY2qkBTz_xsiMCfHU3xLzSan0jMac9vzYfgDGmPPOUVxTy_8dnUSt9tHvr5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgPedxORJXwDG9JfYk7d-GB75b8JOe9BwA0JX-lw-t6gjp_eZ_tJQoGHDq3USBi79JzDBI5-MweLEonR7WJyAKyiDK3tDT_3_xE8E4_KG4jhpfJWeaFQ84eZJAtyWvNZUcdWyHohgipMlN1V59zxVgz70gYLEh4w7PODBjQGr00h63WJj1CtaE2ZtiEaUOEY6gbDE21tUCsi379ggO3V3f1pQavWAIykre7PXg21AoM60B5hEJ7E3enK5yfIsXcr8BEAYE_xepQGfm-xC4UKx35T8-diB0xY79ji4TrI2jPDeOi3mDhsUwxzPztXVxju4V7gK2therWAjFspnTF4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyYuSngrJVuKNGAdeAn_lgNldlo1sTB4b1Nlp8io34kzYruzDUXUD9R8t0umKxSSo9AsPCcFceeD2imDawVclo7lw0YdScGUY7u7-EnzDme60w2nbopG2wLmADIVQFOZX-9CC-ot3xOSldND4TtOF-HLBjGPdl1hWm7wdf3GqMU_4mW3zv47kKC5XP-wne_TCEex5LfisLyeBt3ygX0GP1vxjgQ12vW7MHF8gE58E63H3LqInBP4QwD8rpu-0-9ZS0qy37WFV6dlnHyeqGLY8v3gXJ1gEE841hyOAKb-T9N3cpdBDGQFpmiC7y3yOI-fHNWy2Oz5EP6P4LSvJlvNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGMS02j77E-MhuVRBpfm1MvYMKhsSiDrxsV2Bef3PnrBjXSiNmeUYxl0U0Y7uN-SWY9w716i-frk_pYWQKCl5U7YATGzSIQWXNgO9igcEwHhFQbMAYUdpbKzK2J5WmL6jOOBZgvS7ZNaOoEcqTPmYKlGsdE5WxfiiZDpq8hnpfT7zZUIXI3gBudNuqz8Lk55tGTiRUaRwpJZAfbBEBSCi68z0VADV0UM2gU6EQE88K1TmdaOS0iCHEfUMIc3XFPv_QWE5afYlG9RQmkoV1dhwtTQR7qUQQiGrDVigq6uv_6V70ogSz-XTlXj7p47VuJdW6ug6fKsN1g90p4vwvl_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT76mXE4fjA8u0B4fRitUU3MbHAX4UmErDJzRnTM9qmGFDbSg68HW6KyoquyNE14FPJiG7_dP52iTA3QQCVwN6fynsUJZlQQfVw6Vhawo4Q-RvfEhNxJRt5oy1mjs727WE97RPr0o5YLfQx59zoViCjrZ2n39TFsdV30oLr1cCBzqXe-6DR_3m3JIw_gT8Ze4_6hGnsNvhvxd716CYiRaGEInt85wSwf9WvXNB-FoJt-irxEIKhheZvooI821M8OW13jYHuFIy_KA8TDTu6f6KEQPDCFV7X_f2NYF7-h7kvReJLA1nOQKISl9EC644cVwRXzKsUgqlJbiaEauHBriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opI7U64p8b_9aqTDWnUqiXF-YjI6tvV3X1Xr5wDBbeMzIBBnt1TGHt-3jgKklK_bCqGWBlfpO5Bz0NSzriXPzRofNjh2Z442Kjf49ZsivBVOM-2IFr8s1YpvXoiaIJEUpigqVT9V5lHoCxwvClB5Eldg3Zvm-XjUIC6GLw8PzMoJQXX7MgjQwbCE-xFJYvqlj52csciQFky0_ZwR5BDqj_SHnGvvwvYwkZSt5ddXtqHjLk_3_gk-G7oqNUb6-Ix4McevWr8n7Q62r-1PbxUwR7mboweGpI1S3wuYTGhOXiYptlCphM8D4L0XxqkiDam1Ktk8dPHaDt5pLVXI3D5LsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCIGffXGif0z7QbIvm1K8R3WSOBTLOuIPFqO4y0_k0GDe5w55J_40QXdYQGi2ouHT4gm-n7LHBzElwXNlXTvOc9bamPC-Fv1TRnBW91F1_5nGvToMD_R5EkxdRShTIE2rFOMYBK7ZwcH9oAMEmfxC1YTuM8yXrye8HnmSpO33w592-1hrR9dsll3xQdPB2C13oIJUvcKMrvbWjRMGInNe6QyrCyf4cVHCzO6uEuv60zWFHJ5uD4tm29Li1DC35CvwIG7hrJnGWQwwq30IrUanIDsqQ3O7mU4SfvqFj47Ne0AMkDNP66f8E4Vw8VJhoLRG5x1XDrKRb8q7pfnCG0JZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwwRCsdgpbi4C0SNuoFgVwzSWmMjLGJm20SYTHVhBpUz7xL5sb6vDlTjkOLtBSzkrTNTSYv7TiKbQtXxJ6fpvVqpSS98pgb-GoC_oi1g-TYF2bdgxAtJ_7CUiCfwO4sY97qoflCktlRcUWcOraTNjVrR6fC8LLd-qeuevTEDbiSPxoxXL27x-jiEG74sRQdGet5IpjACmxHogiCkSaYXFoU5y4EdLbUrJYptZOs7-bY3jZG5XLa0SI2heedeLnsBfnlPklbi54p6yMJuKkpXtG8TTxjqomg4_Xj_8K4LSOa7t6pu3-4NcJ7Z8UCBw5uzYTKecA7yA-LYWRcNvXq0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTO363PbdmP3WTxXJt14wrpeT710Rvk6IBxqs43mFZSPcjwoLnw0PFAcIk360oMMJ2ihRX6sA9j0a3h8rmIlPK8vQ-yV86R37G3uRpwBVvCr8tpwwhfVGPmCjtNkViWyd_xJKwhVOVA7RGNXGkT0_I_X7oOndvTxjKibaPjNQ_l8ecJIfJeEmhLFqbF2h1uZxqLvG0W4EUJtsD1QYNLa7nCTf_zEqDenEWJ6sNLe_rRtkQmmiO2bERiPldpkhvmKoWRsYxDS4kwqA3jclVN5TaWYR9dfBcqJa0AnyQhSLmxjhb76l0sQzl_ohvvUIUiOb9YT9TBtLGwlVLPy1-0pKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCJ7aZ1iHSqAzpXx92OWTd5attlf7FbOYuHgtAo0z6X_j4u5CjcNO03DAYsU8t59zLHpgIPU8dB-uhf2OymT0-XT0hgC8tDSKimynQFPSB3q6yoS01uJGR7qS9Z10i85kauIUmcH656B2wb9BQbfbxcA6zKwL2OUPdtnpnlkO4EttvQ6W3Xm-Oj3i3L0YD5OwHHN9siNDplqz3oBkoBIKPIFkVTa4W1pq2RsZKTCtP5sBV8IiG4-YPhmue8RYu4WPUcNNho2yihVxMFGJYbw-sagNedSlqgmBOIGSheSE0fM8y8HrbX1AAQFgFz4IEnG_mMlWdJJzOVkcKoJO4DOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCI6d643iJDuGLzZ5I3wYbunu0TQK1_WQGkZ5WJ74pNAbLoJDSt1uTIyOI2SPS_mR3nP7VZz-a5cboT7iheRiPeUpsYTZUIJi3xxtQDyOY2uC5hxs65aWYN_FKlHWKz9r7plJvdHuq_Du66rEer1H6SXkh_tP5WfWpu1gy1jcjQeyno32KPImkmA_6IHzuo2hjXyUtrXSD2OUwpK7bwHf-L5Y_suSL4mtT-eR-eDSBaewUvVkSubBTNDQfjUAlVvsaDysWFZ9VKo4Rc6Mi6iSGUyMPjJDQFRLrGveUq_05pmoq3xtRUd3q2vagv-BfmATrmzoMQePUI23xecSzNJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIMOQgb-xoP1x01zB2niuU3dEc7xnLE4B_jrCPitOeD0l8KdKKhgNJXtilYnQN4iSLAOU2z6fSSCT3MHiBIbbCmxwgAMpqjk-WDmTkD9HxwCv17NY6Q2BtD6ZC3x3rQz_-yVp1ex9yy2XgLoFBxSZBZW_tkiSREZjjDq33YbhZPpZL_NK3_NHWpY0mb7Bmi9oizQpFAI0e7mEKESH_bJIhZvg0Fsof8QzNfJHQkKS15Yea5LPwab384QdH-Bw-MfQ97HZgiFQjg5RJ2QB7O8l5vryuCEsc1WoqbOHRwk-KnvVVt3cICdM2Ch1K_0gWxYcLugAP5f3ydrAwJqW6QqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf1AJQ9o3RcLOm6Bg1IMSt3-T3n7vG4_zLDy-J0y-ip9w-CCT8idInmxijUIEaSeV6bTKiDQACQWRSxFjKMGL_eduR_QKxCWmjz0X3WgKIhQHTOs3gY58KU4gdE4R3XPLlayQowUiOvEiUohZwuUaPpojL7osLA3u0kX--tz_ywg8OiGZoNZBqLca44hEKvkUSOIrAgW_vuopkzFiUd7m_B3_J-Hed8FgS1r--aF18CxmCryTAo2J3zGGxKDmbAtAmBsd_IqirXwd40gINiHSNn93v1ONpYFwOTExzdxBCAVCEjH6fft7DGFMSPtsSyI2kvVSTCKP5iIhFzKitXmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJiAx5r-lsF2bqa7nK6YQADfmAAv_EjysTlCDsrmWCAsATFW37hDM328cFPd4PNQ7zy2yd37OrHMeCJBWvCtoyrr4461UKUw6iXCRMzyBTbK3bzwZqM6icFt3mbYlj_YrEU8HH_wl0XpBUg1_FK87RsQdl4Sn-ObTNxXtCUh_k8EY4ZPvXuHr4Ue1FWvH-OdbpIhSnmFkkOsBHZ050A4HcevwBoxwQNwGtUWFlxAwdIV6AIXk_qgiTc-ULZ0O9249HCFbj8u2OU85MmOOLXUM8UCqkLvZsxzQbZ7QaD9LnknhRTNhP_dvNxwecrznRTBrD-MtJdJDxWFlzb7OC6cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH0WAkTAQT0Imknye3VWe4NBkZl7s9yp1dPvv6fDYMOD6-4nIqVJfLNmmaAC_qBpbsChnOA2naMS5TH7fe80OSGTKBXTmrIZV4UM0wiORDHhpTv4AFXMtGO6-z8Wj8e6AiTx8ci_u5A-4Be5OCzi8T9LY8L1vBdnPgf8AU59VVWr6NmOUdSr-HxkcWL3eK2nBhraCz1DRedB2G_DOUvJXP44c9Tv7Xdd1c-X6hWN5NRnWZovqcV5HyktmMHY4xMPK7rUWBBbh1hLwn3OF7ZAFvFPwkR_EdUmlB_SAe_EUuQehPGz-uMopsqyWid4rjmOoSqhlw-djlcvPZgSCG0O5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WigQrkQVejfewC59O8tiuE06TbGR1lYQ2oRFT1hw98ZuLHym5omgzg2t678ylJ7xQM0-dqWn9TsdwR1x0l5xi8FimqYAHdon2rcI4OzGMZScX90QE7Fzsk1oyW9WTpH0ZAM_OTPn5aOfCA3j5I94JsQ3Cz0yMDdlPyBLuemdAwu9kq_QCgm1zP4YBs3JzwtDG5uQvN9XuhIpOte0rwVABgHxl8Y8n-LY0VEsreopZevmvYB3Xxf5L9Ci3qt4gbtDnFBMjey_uyUxpYv9wWFox6BoJxp46WBsK4ZLH4fgVSaN2hIcP_ymX_w2vtpYQfU5Ia_DqKYwxkZ7rltRpasW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmJiy_A6k6ucVxXUUzYVlXXfzEEXSOBq1vDZz17eNcmJvjiLYIWl1qp2nVopPLWrWdpOeD3Sspf4x_0so6NDq-dS53INzCuVkapag302wG1N_UXkcSolQl7g8h2vCwFQD5LwNgecXETHpL20j-TmqdhH7Vmv9N7RR_gGfSKerSG8Uqw__b1VO_emhlXNWpPJs7ys2FA8CM2qo6WN_GhTrDDheeEUMx0sJ3MiaOxw4QwyD9JvNBG_BIPpmUC_NEAJ_eHskliqh-kjfG7RHBiCzUpv_Q3G72K5yCTXUuj9eNUn5VIygu9tNm0p88MO4cStbGsQYr584cE5cHH6IHR8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFVjye_P7S8Yv0mUrn0qiaDyQshWwjFVibp1G4GkO-rE1dR_y6KcjQM49aqtkvPmtIwNTYW6_tS1UJRTaYH_hT7D9TjHl_EHc5ougtcyu_w09FCfPLFH--gjo-tHDGodXkIoT7nnAMXd9BZP3canA4B9wZ756H6_H6j13J99nwcoZhFZpaZLNl4p2sS7tAdENB6wURImUtbxOMs2Z0HaBNc3AkoPvmw4jce5a-AecaI83lgdU-RCZL38vWboP2LH4guncPgUUltPo7vsKPBtDzYvQiH-DnYdIuQK6aHoNcJfGgQGMldTNTY3s2oA98yxTFTz20IuO_In4N7MZlCggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrQ4cTwCgyJr5cZNFd7VsZgiJohtXnB9rgRto1ASzxRgeZbLAxutwMUb9DUBIiOltPbfDVF94cN_kzsHq3J7nnZJxsWTr-E_IjSSGGNAeAwIchUkPxICv2Qu4cmNk-GqVhpRNYHreezcG1KzdJriqCr9qmIm2qrPCbmm-yaMS_XPzOyNZnrVq_z2YVTOfaIrpH4lG9KqjZ5JHIuirPLCL0IcnMqmHwm7_sWUFe73q_1kwKIzE8teRiXnbJIJ3GrHv1-kkCGFurGsLMPh_ngMeHAZ6E0zoYWdtW6IN0JLe7-_8n9XhCi6okwjRu5PYkjIHSzPDkkgqFjDRh6FHPipmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=iZ4sUXrh6lDKf3yT2H9qTTjTvGbpilrEhs4a7oska-c2mN0Laxm7qY3jkLyHpL3WX46SgL-rF-k7i8PlHJ-sU_FxWPvc07zHwOVTJcSlAL6lAn84KVbcP_enUamVveoIxK3BwMXoTyI29R2CNplB3qQpytojcrnnGlxIYX8d2OMLART-20lUOroSXl-ctonw6dLD_S9jXHZjxrpf5Ogj89gterKJOzdegc7ZkEcOWKP_yprnRcSmJ_kWMDMwpNxDvMtX5HGpiNbH1evZlDpT1XgbjBGEdkeHzNccUQ_qz8zW3O4wI3-qrDtvPbwa073-Sbz4Aq9yUXhBjUr_aSJyYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=iZ4sUXrh6lDKf3yT2H9qTTjTvGbpilrEhs4a7oska-c2mN0Laxm7qY3jkLyHpL3WX46SgL-rF-k7i8PlHJ-sU_FxWPvc07zHwOVTJcSlAL6lAn84KVbcP_enUamVveoIxK3BwMXoTyI29R2CNplB3qQpytojcrnnGlxIYX8d2OMLART-20lUOroSXl-ctonw6dLD_S9jXHZjxrpf5Ogj89gterKJOzdegc7ZkEcOWKP_yprnRcSmJ_kWMDMwpNxDvMtX5HGpiNbH1evZlDpT1XgbjBGEdkeHzNccUQ_qz8zW3O4wI3-qrDtvPbwa073-Sbz4Aq9yUXhBjUr_aSJyYjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzXg061jodvdt3zSFcRgdaNVdqDmcxPLOv_Y_joajJiNCQzNpWfpoaO4FByLQdx5mDOm62sPpVS20Q_LnB9_ixGTCnoiSvCSLAhaMPzYik1mrAK6xih7wQwC5zXs01sTlbbqMweqodi9MV0TsAoNXTJD6Z8Qswdg5otvpTsGPC3onDmlYXwqnpgrbzUQL_xAXLK7x3hL5JsropRsC9eSnLDnOks7ctFOrof5KdcmKX54Vdv1hgMWfaK7yr9CP0I2ObQEsIi84z20xBlfZ0snfrLIpzpQfoDMySQOyXZ09_SGb7aN8uKSWGlmCTyqtdgTYj3RYOvx43b16z3cCMyc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=vLotpyIDmmXq1mHl97Y-5GNfav8kPTfI_olhn1AR2zBMSbnu6Pj6gKASFZ3A2iEm_iUzFkqDGqoDWZjXAJ59OtNEAeIw38vIrwyU84l0rM89CWh6ussoZXLyuEVGtV7PntiWwTey1HlzEDAYa3Lh3OzI0Wx39nk3ZaKw0qtll-v2ivJRknCgsI8D3S0zuMY4Z2pczwGP0ypZgFZwRhY7YawrSawye1UiD6BbGgpdyyN_8O5qU0bpvUEd96lbVJtHLLlZY9gTzKql6S6u3e3SNXGIYB61mN_bbmH0aTLMGem_3ooM7rRuXUo2VqiKaxlrP4I2O6MFZi5V8sffxT-XzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=vLotpyIDmmXq1mHl97Y-5GNfav8kPTfI_olhn1AR2zBMSbnu6Pj6gKASFZ3A2iEm_iUzFkqDGqoDWZjXAJ59OtNEAeIw38vIrwyU84l0rM89CWh6ussoZXLyuEVGtV7PntiWwTey1HlzEDAYa3Lh3OzI0Wx39nk3ZaKw0qtll-v2ivJRknCgsI8D3S0zuMY4Z2pczwGP0ypZgFZwRhY7YawrSawye1UiD6BbGgpdyyN_8O5qU0bpvUEd96lbVJtHLLlZY9gTzKql6S6u3e3SNXGIYB61mN_bbmH0aTLMGem_3ooM7rRuXUo2VqiKaxlrP4I2O6MFZi5V8sffxT-XzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZwcACvhTQ8cwczzhuYYgOcnrT1OJOWPMBQ4AVa_SrvVtKUgug2Q97SUEj6p7yQ4g25CivY0oEbM9-OGArZO-zeoW3DCfRyVL23Cqe0bz7fjIv2HAO2ngdcIKnRbl17tqscfXe6bgX5g5Qb9fR2fVvGaonbEwKX_aVQesDkNpXbeuQ-5-5j6x9dmThHJzPon10ysT1x879BN5Kx7UGWokSFGiEPkBzYq-ikOme-RlAqpgQOkl49VSVYW2A1tmSj_l5lJazlQmAmiVlT7Ed-kPnT_b1LU-cPIrS1ciylUiYbjxacEq3KxjFl645cBY0buKneNOUjO5p7ZheOiLVAN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj3vBGDZpXPSvl76XF8D4bMiG6chaCIEWDMjOxeuVV5FyY2kTvr13s7hQDsk72LilhhQuQv4UQsen73lpF04EfWfAqYm5G0mhRvD9rIE_hwZAatT3W4T9bvvxZL1XL2-eKA6Or5Lw6FW7Z7uFYmf3hJOE8FvyGDFy4QiBAF55Do8WIQBLc42iwxsHz5X-fSf5eOfgjM2K2hF4ksQjoIivj2ZN40hzhd2zFAxE0bmzilhEbUwWg07WnVs_TNIapo6ARGwCRMn4ONlU3KEjjVc1mooiBTIvjFeTMdffYm9XhaTXVSZqzYog4Ty56XNAPAd4Tz5mpwKUCE8DiWsPca9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=mKENatr-6zbZwa8yVBXPsZkXvz26FJKiBc9T_ru5oXugfJYdmOntRs_OqgbPmSknt1DcuJM16eRTM1mJi2sJEP_RpBDJ2ilakzSIe5_ji2LhDVRpnzpXcX08gbPd_C-peH6vfWlFvx0vvRTioXt7nr1t-1p554lPgtf5DT3AYlMeMUK2bg03-2iNJVThxAOmDfqwl1lZ_5fAlDj1QK0dp5Yo2kCtyMh4SgZwb-aLKmlkViPPLFq5Wb_XJty4kx70K2RExy4nsgZrzP2wnTiF7C0XM22xIAznfJOJZHV0VxJVRRGqxwdkQi0kXm2jOjW2oH2OHPFvNNeqkLOT6yPCzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=mKENatr-6zbZwa8yVBXPsZkXvz26FJKiBc9T_ru5oXugfJYdmOntRs_OqgbPmSknt1DcuJM16eRTM1mJi2sJEP_RpBDJ2ilakzSIe5_ji2LhDVRpnzpXcX08gbPd_C-peH6vfWlFvx0vvRTioXt7nr1t-1p554lPgtf5DT3AYlMeMUK2bg03-2iNJVThxAOmDfqwl1lZ_5fAlDj1QK0dp5Yo2kCtyMh4SgZwb-aLKmlkViPPLFq5Wb_XJty4kx70K2RExy4nsgZrzP2wnTiF7C0XM22xIAznfJOJZHV0VxJVRRGqxwdkQi0kXm2jOjW2oH2OHPFvNNeqkLOT6yPCzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsh-Bd3nkfk1-E3nDNMlkj_AQiLGwLSKH8uTIglAxaRmWJeesRYFTijnBpuV8HwSBT4ZokSpM5l1TaA2bMHKhydFGo537X0rgYF9SzDOFJ7pRWPaLbAF6oHGkVPe7cEIBUuQtzId7Gm6LJl4t5GYj0bY0L80jsT3ZcsiKm51WvhXnnYVNGOIHYUY3kCi_d2FeyY5OQNmQjylaYEuzXMO2sa2Gtu9wsQv6stiT3BTznni9_99UfB6jW3U8RXtBdKZY4UAZWSXwtNMxNfHD7Tsx8rrkMo3JRAUg9bo1e6v4xQzpeIFrSwTgL4L4IOM7R8-Y7CtuposOIll0mPgZJYU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sa440DAOrdOf1QVNIReufQWtNhG_D0lt-jKGbTU7hV03LHt4JPGechfYhuwFwqVLmBPl8-thKiOZ0x81ZfTkwRqlX4fnm9PRy1WjeNldbSfVj6YqaFqx8PvIhG-rDswjBQtN7gMHqOzoZXdFPRRorhbSHIEvnjhM1Dvkrm_HIBN-O9kp-2-jEISq4BNqRrfp5QNxHAXWPQRfOszbOwwX2nqb1ml3xVjMoZzHVaxBRqHKoe_z_IAID1Ncq9iMI1Ps_fazof6k4914JD_Q_bTK5zyiw2C15igb5L_xUgRUhyaa86l8NDkragFN-xq6_RmPCHrSMyYsNKyphxRqCWPg0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx3diKAJ8EIg8qJtwpatuq0IPn8R6159hnJ1P_BBEk7bDFD-UjZTcD2j6BlVaes4tPROLaZMY5xhihbSg__4-8k1Ac-uU3Ij26NGf4GYdnhgp4mulmMPXORUJ54m_xgIAiAcZWU5f50li6vPHxmRXlvjRYxf9Kp_1865jYkI7co9TFwsHs5m8g3J1JiXw97BhYHYmdy6r5rpAdmexrGeUFojadbJmfSvCVx-ew2YKlk402sOVQM0u51s4gTdBAWyu9nqQWCvm72P69Q1HgC2cilybam_b-P5OYR05YN0TfXyFPVj9Uwe6BiJOk2H0x6alngWSfvOVZz_I2PGiVEKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=vSpE-KSYT9z-imYASAB4QQZxr2veOQ4Gecy7U6LuaJx3qCEP4QszkigQbSynYrpY6-DfL71Al6dobCKR121zocJvPPfFSYY7NHvajJecdKZGxa5-xpmblnsJyrl-u9Y4DwsSl2Yk4HTCH0H7GgUD4PyCS-vN_SftCYeU7TW5Mv_96qIOAaMmmsuI-OkxHFsDpY6c_RawW6W5NT-TrKKvGE6wI2tJlsGsBP9rbjjgqcKDOYPeVgJ8X0B4zNRLG9_87yKjhEG66RYMs2N2DmbW7SdhbP9qP3eFEMyhzpnaFhupt5iCcxC9gloMu8yH-XuhvOiQpmcJSgh6LiV2glYpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=vSpE-KSYT9z-imYASAB4QQZxr2veOQ4Gecy7U6LuaJx3qCEP4QszkigQbSynYrpY6-DfL71Al6dobCKR121zocJvPPfFSYY7NHvajJecdKZGxa5-xpmblnsJyrl-u9Y4DwsSl2Yk4HTCH0H7GgUD4PyCS-vN_SftCYeU7TW5Mv_96qIOAaMmmsuI-OkxHFsDpY6c_RawW6W5NT-TrKKvGE6wI2tJlsGsBP9rbjjgqcKDOYPeVgJ8X0B4zNRLG9_87yKjhEG66RYMs2N2DmbW7SdhbP9qP3eFEMyhzpnaFhupt5iCcxC9gloMu8yH-XuhvOiQpmcJSgh6LiV2glYpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=mDGWhujjh8Rj_KGsPVH5V0ShXIXIpABCNC60VCziaFMJ7YLWIGn37Kw2MHCYkkNRze_6IjulUyiKumZ4o206adSl3D9mG6eyZS-43F6fjZTejnLrUOMj7aC8tuHx8eGy1IWE-eTOyczKh_K_ep_cTl2w9ppu95EHcr74AUH3-EU8-wWKGrL_C1RZNL8EZUQG1ovWsKHkCSMXg2jVTJ68ShMf7bj4WW3mXH8Ig6Br_zcBAqfWcWzR1t18zU21OA9WCWSs2Z8P62tzD-zrY_V5PQLJEYEp92JtwQlkS3K7ulCeLclglqQfU4PBnU4ZfEMpXtdHAVSQJ-T2xko2YWxB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=mDGWhujjh8Rj_KGsPVH5V0ShXIXIpABCNC60VCziaFMJ7YLWIGn37Kw2MHCYkkNRze_6IjulUyiKumZ4o206adSl3D9mG6eyZS-43F6fjZTejnLrUOMj7aC8tuHx8eGy1IWE-eTOyczKh_K_ep_cTl2w9ppu95EHcr74AUH3-EU8-wWKGrL_C1RZNL8EZUQG1ovWsKHkCSMXg2jVTJ68ShMf7bj4WW3mXH8Ig6Br_zcBAqfWcWzR1t18zU21OA9WCWSs2Z8P62tzD-zrY_V5PQLJEYEp92JtwQlkS3K7ulCeLclglqQfU4PBnU4ZfEMpXtdHAVSQJ-T2xko2YWxB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQdqI49SVLnjEdLN5_ufPVq8_1KdrKY122DEwDNwydPlDVHY39GRB378_22ccUixIrWbBFbBc7vT83pQlSCaiPBGtQ_-bou2s5Kinn5TuZAWbuFUF0rGnXP88zSBRMiByqEfbwABkXZY591NepV86uwyL9JCCB8mLmisiv4nYbXPa149meyeIS4g8YHaIMxVaASJuWPa72bnxap0yIHpXabPBriCnerpfwp_SCrATKIR_FiypG0wm3eFfk-iQjCDxacsL_hSN9Ja9YEDdc2i8Qky_RthegQhckIYJjWYTpSajuEy2D6i73b2uCt7U97bNkc0ef94riUFsXEouV8xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-PQWLxo0jBRRROUGbDm3Irs9atbXqIeeqbjWSm3AxpRt0ViLs5xj_tFYXkPRXUmUIWwDnNk33JosEC1JjHyF6j8tLZxz8RZNu_WocXH0HLXMwyNIIcwKzPMWh8u0A_gqN4iaUEwiK0OjdxGW8zxcqBHNJggEPDTgrkrpyAZNzBKOnahWFvcUQ9M5CPdGUFUpxeGlDeb2Ww435hzuaHyb7XQRK43Ki5NgdEqXeXTFaI9g-Fsg9PhoNr2j8wrTMtGdoHOcD-EnMDCs6oEzk0-G1Z-TOgKEWUfK5oGhWYI78jNpS6nyovjc5ExuvczdoQ9mfqvmNU07gHyCBYMDoIm9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE81ue8EnPuS8qtg_ohVVhIb4OAqs-DduIunhgPgCBaAPXU_nFlESfRMwy3CNR-oAirUt4H-nvCGO5jtMIxcs_AxgZY9O4m2ZwU-NHhRDzq5Wvun5_J9RN3FdsmIj7vi-5qIFvcONydnFJ98s5Wx7h0ZrOEYseVwrXLHJsI0dJHbiD6ect12Jppw0Vx1afrG8HC7YurpzzB4mS4Hrpda43pbiFq1Jf17esAAks0bXVom2UdC7I43LSsqiDkW_YDKUVAD7Irwln2jhzGc4pBbtfE6Y6nH02v9z8eULCLXb37pOPxdrDzInmurqngW1-nIt1BIM6KUkDTLIqGdpiZ2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1bNrnv0WauoQ232xRMPBlxUMegp2Mmpu6ePmkSgcyDVIlRT-tRKHvCqHQ9hjYpVEw9z3H-UoV40b9HKZR0Cjb7PWLCjEglOHx2VfnBpJYN3ysRYRPYhe0-O87gcbTbl69ls5vhqwHnxiB0X0-AkJd-ohoGbPSJC17IqYiVAqachZp-CEvqHMEDhluzRicl4Z89uycoMrEsa31S1eJjIQPLB_koXZHDnUTWSVa7Oup-BQj9X3Hw6FJu0K3r7rh82zBYcXDs_XVHdftORg4VGwbnEMSMqeM4klhg4UoDELnD_KEQ7EILBjdtytHBZCjU_TPMZg5ZZsOGuQ9EcG4c3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5HNlYZHgNXB120jwHaOnvwNaApXOxo1ADgmA8xtcZNSViL1GGoUKTUd_P85w9G9kH43VY-ABY44KGNcN0wOB-ATsm5XC0OY_JOAEtTa0aJaoywcZSlfxY0-1gVOhzjE86QscCk-ItmX6seeYjBHRDrd7xvOdRwhUkOw4ZqalxGfARFpLsUoNCTh_l5J-uHiZdzdD4ycmlO2AvuMWjR0jAB9fzLuchdCjfB4NR8D2lDV1iMbERpKeiuqI_oAhr4daUUJe_8804vu0o86aKMx9deQyCgfgVZ_h3Sqe9i5vAHx_rkHouF4gLkOxQUxFNNuA97Ht14o7VTkU1smOgcG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le9hxW53cr9xQzyI09PVyLy27BBmOkfybZJS_Qa8bJlAyYSEdLiKN73Kp_5k-C-ls5qYJQAtR5J0TCDGjGo_e8Dk1L3BakcIgIEKIT0bZaTyxd6jDN88wpnlZ-YUavaxWeuuMGoPfblaFYEy5SbojlGHJMxZE7K49sGocknxzXrGqkcc4LWZ3X_in3qXfDgGmiH68sYzXi2JExb_QTeFMHc0sABGgxTpM8NnKPvhc3pYFopko9oq3B0zqMwTdU6mxqPFM-jXCUXeppVsu-HooxIPeN0CU0nXiR_G6FZdxelU5KqnD8FArTIQeRDXae-HQ6K61qQNWXXVwyvFPLKt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=pOc274nBViWhYrojUumCupchEpHM5Np1ruS97vdjk-5WA9nXzGrOobfCPtQKyw5cQgHILazuRVE35Zh8IX4jpckllDNiChaH5KSb1KDQOXn85O27_MR7R7T6KyJkl3GcYSr1IGE0_xjtKF2PSef6rQ7NrPpg1v_OnoziMJiyGle6_zZH5pOdqaQZ9WJBGYgC97P8xX6iKOecH42KVmBocEs9fKQxxrE7_TpRN5JMSV2ac2SkHjq5rll7XbWV4SOSZ8rvHQdzFcoIo5LaqolNQ42tEemaYOAOpKpjpQuyqIY37JhaRlQpDbWFZhirjcaEM8rn4JkZA5zyKJbpZKddxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=pOc274nBViWhYrojUumCupchEpHM5Np1ruS97vdjk-5WA9nXzGrOobfCPtQKyw5cQgHILazuRVE35Zh8IX4jpckllDNiChaH5KSb1KDQOXn85O27_MR7R7T6KyJkl3GcYSr1IGE0_xjtKF2PSef6rQ7NrPpg1v_OnoziMJiyGle6_zZH5pOdqaQZ9WJBGYgC97P8xX6iKOecH42KVmBocEs9fKQxxrE7_TpRN5JMSV2ac2SkHjq5rll7XbWV4SOSZ8rvHQdzFcoIo5LaqolNQ42tEemaYOAOpKpjpQuyqIY37JhaRlQpDbWFZhirjcaEM8rn4JkZA5zyKJbpZKddxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=ClQiS-5_bNBTmIgYSLmpXVQFUNjJG61F2W0cy0npVK_XTi8CmCX90kPE-wOTlJBPXYQaHpA5bz4q31IJR9lIq3F4lgImRqnACKVCYXWa28q_LdeJuVU7k2dXyjqjDmYVmQpkdWxt42rkPcSY_y7sMXsxLs35QWbUs-jvelYCVbr80tNZuQ2yIP60dWM8TmnJgrQizmgsrXIUFrMuG3YSewDzCo3tGIy1g4scmy-PnWz5NYIUVBw3s6s2DLbUPtCE6fjjA9QWdMWa0KKi6AqMVKzZSze3zTOBMKpVO8T9kpJrW3hL4YJQAQcBy91zCul0F_yr_jAmB2WaxI3nsIvwGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=ClQiS-5_bNBTmIgYSLmpXVQFUNjJG61F2W0cy0npVK_XTi8CmCX90kPE-wOTlJBPXYQaHpA5bz4q31IJR9lIq3F4lgImRqnACKVCYXWa28q_LdeJuVU7k2dXyjqjDmYVmQpkdWxt42rkPcSY_y7sMXsxLs35QWbUs-jvelYCVbr80tNZuQ2yIP60dWM8TmnJgrQizmgsrXIUFrMuG3YSewDzCo3tGIy1g4scmy-PnWz5NYIUVBw3s6s2DLbUPtCE6fjjA9QWdMWa0KKi6AqMVKzZSze3zTOBMKpVO8T9kpJrW3hL4YJQAQcBy91zCul0F_yr_jAmB2WaxI3nsIvwGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBbnoq2U_tgrqYaFp672ugD2uts1lQk096zv25rh3lxYa83eCU-sj51Y2pb-KhMvVUO0E2BgPnaecXbhZhv1Bx98DQGmDgeskcWSCNZBlrJDvNJFd0lmrGeCLbnKrj6OLDi4GRTQnHqjUBbbX5WESaO-FuhKYvIRTsGGlQfgdQdZeP0mYOb7bUMrLzhzMzBava5r_aka0POxJ1QQAGk4YRqh2IkTNNj6WFOh3kM1XwwH5U1y5sdsUArk8WTpstH1LqBAhy5XH9_wYanAGajs9I7LAtk4M3VvaV68BjGiBBPk8edh3ptLOlVHErjnEUMEGsnnsIMKXnSkVbYKqpxfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=NFT40FiUfYk0-c6bVVr-ti2AWnqIX7EYKzGDizkNDdPZlF_C7c4qEdbJ3bspS2Zs2uNHvLv6Sm1GACIXMFk83ytUXQJHjHubkJ-VZRP7QKmo_SmRqPDukT7byAzCuhir0SUIjmGNy_iNtn2hJeT2fl7dRyQ__qiedY9qZQP8LV570pRISHgAz8C_6OlkOqD1AXFa_93YOU_SQYO92k-8ADYxzw7k0iOA3x742F4rE6Ngugr5tMbPwD-5DCCK61s8wd7OnRtKY8M64pKXbDZx9zN0mqMfwb1kIDrq09JogN8Ca39PTH-hjej14LIxgHT8MjnHhKF-6vrQenIlGFh6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=NFT40FiUfYk0-c6bVVr-ti2AWnqIX7EYKzGDizkNDdPZlF_C7c4qEdbJ3bspS2Zs2uNHvLv6Sm1GACIXMFk83ytUXQJHjHubkJ-VZRP7QKmo_SmRqPDukT7byAzCuhir0SUIjmGNy_iNtn2hJeT2fl7dRyQ__qiedY9qZQP8LV570pRISHgAz8C_6OlkOqD1AXFa_93YOU_SQYO92k-8ADYxzw7k0iOA3x742F4rE6Ngugr5tMbPwD-5DCCK61s8wd7OnRtKY8M64pKXbDZx9zN0mqMfwb1kIDrq09JogN8Ca39PTH-hjej14LIxgHT8MjnHhKF-6vrQenIlGFh6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VPkRE9_-DYuVNfmEFtYGQmfIyxL_wp-HxaebLXHqoh4FeirDMOB2eV2wHSS_BXgS2W14wvDFn3l1aOEBcEWexfPuQQ3-ZxY0fc_MMHGOj51L4b48ASJoMGgvOLrZweJAnTKBujUojtxPhUgZhQqIEARP86lry-Kp7StN9RGGHFHsAO0g8o2hyKrOmMpmIMQ9LniTLe-vu7RQcHLwM454O550gIV0hUVnd-OK_bx3RzymSkIIxds4LSxtl0FaL7m6HBjv54VyRVMGoGHzCwtniZw29pSo6ZsSjAv5zqyiCJuMOhZ8qnaAOc_bVrsd_MXYQI6ctKJalE33Y526_BfKYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VPkRE9_-DYuVNfmEFtYGQmfIyxL_wp-HxaebLXHqoh4FeirDMOB2eV2wHSS_BXgS2W14wvDFn3l1aOEBcEWexfPuQQ3-ZxY0fc_MMHGOj51L4b48ASJoMGgvOLrZweJAnTKBujUojtxPhUgZhQqIEARP86lry-Kp7StN9RGGHFHsAO0g8o2hyKrOmMpmIMQ9LniTLe-vu7RQcHLwM454O550gIV0hUVnd-OK_bx3RzymSkIIxds4LSxtl0FaL7m6HBjv54VyRVMGoGHzCwtniZw29pSo6ZsSjAv5zqyiCJuMOhZ8qnaAOc_bVrsd_MXYQI6ctKJalE33Y526_BfKYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK8zPWJDXDuqYIajIajI1KTvFuOk-LVKKxbXZ-yzTRoZFr7ht3SOkubaULMOHRXyHg_SzFha9WmkIjTauMOZwyf_NgGF9gDWK0eibXjHXL6vAZhAfvK24j51olLEdUBILUVwkh419MGGRolFqUS8Qnt9_OSUrGIFHgFySpbzQKeXSeYgO04qF7_g90ymzncvMYJ_yyinisqCfIPfMsF13yCfhIcr6IFVc04N79xgPv0mK15UrwNGgxVz1lD1_tuoBV6KE8ecDjI45bENMyrfEcBx27oDk_3KeS-63_bOUzorV1TJvsRyzu7bffWZP5-YV0vJdfDfsMLQtIZW9M82kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzxk30IyaTdZsz34FeFSoD_YAP2JhdwDEMk5aB3wD6jd5kJYawgiSdnCfQUDpXiGVy95_F_ySzxjPuIMYuwopnANDJk1HLrjxsjKmm2XsczzbCzG2FTE8Q95TORQkUZjFXnr56HJzUbQTHmyWlGebdPS7xX8lEyHNlxshCGWjCUb9kUI1PoMD0iotmqap7Iy37rfZPus7kipmtk3izN0iN755dB7mHXSzT3SLZ61ysNUdDkmB4FedcIE46jtXClcyeoGNUXOOUTfvOind9AzlY7urDtcUMc49dhQkp7OLsyymWJLWcQ0lQUdl45S8uwyVJzx0jOL_LKfN4Seoxjatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op-D9MSUpG7IaV4yLSn6rmW6h50pAEdC5AORBfVP_akc3-ik3dgR61Ye4wiSpXojtD_PPKKWNYdJxdWjyeVoQHsqVoRfudinMPMNaCy0iqMhCHwlvBgFlNtCEcXJmgcFYq0cvSi9tIXIDC4FbTPbx7Me2Ngk886RMoWR0BLJt-UIGlnz3xomL2camPEKazj3jC7MYFIZxZHYofj3hbCJvsrvHgxMzRmATEzdmUlWzazO-IJYMsLHJCom0fwIStfiYbvpkSffOLyFpHK1uyhM1EZct1LMbo5dwPoNMzGxKvIedivhgIVllqYOGFlUXi1oDYpecZBAHBPVJQHtQWrXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=CbNywiUH6KzYQV7CnFerpEboZp9I6YEBzJxS39DnVVkJjw88bkEWcTRiavrLa0YoVZwCrQpTdmD5qnd5-2z7HEa_XnggiJBksuF2eZkQl_Z1K7d9LfNoixtcmw_iczRP3Hs6sSstzKnVRl85iGYGs4G_IcvAf3aTxJuLe-iC7FfI1q-cEnGW0-PA1nysjlqoPEROGXBcFlFtCPytXknVn8cbRgC7gjEvx9HqgdMVaqryhMg0bVm1jhghr7bnrwszNVXHMm2Eo8rXJ3JpsfVmLl0RYHOQY9k_wJCzDu1cdwUBTmBZnryhSbD9BN-srnpdPFjuV12vRIX3bXJgFBp6ywqST1IYSQQSUKUB-cjLDirSI684-FtePDLggKSK3GHqk2mlrsy5kfdDqG-hXkUE-REAAmIh9MnA8akUAkeVP1LOs75m5wTfULk3h7rFghob-EWxNtiJbxqC1_ue2BQv_PexuAgLMriX-LQRQCx1yN4Z3c-JD9H15SJdaFMGvCnFsCE2xBGQbOcxEALR0kMinXPAivd1GOhc7miCDFIFa2G48Qiep7cYBDdiSLrif8a4nPuG4hzFdmu2ebdSdrPXW2bmC6xGQ57BCJcn9a7_ffocvJLI39TdUFLpVqRnUcY-O6gtZqMf5E9iXqyjkcpRQUJQs6px_tE_nHh4S1zlPuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=CbNywiUH6KzYQV7CnFerpEboZp9I6YEBzJxS39DnVVkJjw88bkEWcTRiavrLa0YoVZwCrQpTdmD5qnd5-2z7HEa_XnggiJBksuF2eZkQl_Z1K7d9LfNoixtcmw_iczRP3Hs6sSstzKnVRl85iGYGs4G_IcvAf3aTxJuLe-iC7FfI1q-cEnGW0-PA1nysjlqoPEROGXBcFlFtCPytXknVn8cbRgC7gjEvx9HqgdMVaqryhMg0bVm1jhghr7bnrwszNVXHMm2Eo8rXJ3JpsfVmLl0RYHOQY9k_wJCzDu1cdwUBTmBZnryhSbD9BN-srnpdPFjuV12vRIX3bXJgFBp6ywqST1IYSQQSUKUB-cjLDirSI684-FtePDLggKSK3GHqk2mlrsy5kfdDqG-hXkUE-REAAmIh9MnA8akUAkeVP1LOs75m5wTfULk3h7rFghob-EWxNtiJbxqC1_ue2BQv_PexuAgLMriX-LQRQCx1yN4Z3c-JD9H15SJdaFMGvCnFsCE2xBGQbOcxEALR0kMinXPAivd1GOhc7miCDFIFa2G48Qiep7cYBDdiSLrif8a4nPuG4hzFdmu2ebdSdrPXW2bmC6xGQ57BCJcn9a7_ffocvJLI39TdUFLpVqRnUcY-O6gtZqMf5E9iXqyjkcpRQUJQs6px_tE_nHh4S1zlPuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upH42jwE540epeX6wI61BmzBLQu0zhzzSseZGKhVpf5c8WumgWqnLmI5sjGGWw9wm4Elo88MOm-BSXMcxKd5Xq4aAlGUIR5GjHIyyIoojiih7Gl5gvWvXlV9-6GVIQJqZldvjPGe4rn5_KB4An7sJQjEhp92w2kNb38h5FE8Yd5gUj0L_fJxWssEtHRVKTGC5Akon7ddgOwq1TA33hUhSwisia7B8VYTiubadrSXliDUBv2WzNM49nFoL9MYYBlYr-B0R1w0mhT3sAvx7Uue9L9oFH6lOB0RiaJcnJ-UnO7F_ZLxldLhQMpDXiXQTPX7bS21vV_6LuargPeDJFfYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIsJDwDASuN1U8AfpMw81ASKptq6uZbJZt5XdECafVh-qNn0luKzcKBVLbX8BzW2d1RdmQJnKnO09udVucz8IJqr1_gC6_J4KNy90M6nM7KVbkJYWOL_CuZnx1x20IIb3x1dUg9L6QOOI-UYIjJxgE3UCy2FVUoYGg1CBDnn3lY454ueRrTgp7r0R4A-qGVhvJOcs6b0ZojeKSOq7sOQzNJOV6S5DBH_v-NYwGYfGLcnD0sh_sRRKNSkJNz8pZXayvlWVl5OqEvWf6q6RgjN2xIGfV1pBaFKkxoBPBkUJf1AK-3h7rFeG08Q9VkFuJSWBGwGF-W8CSoIVq6ibrItiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiRyDOOzCIBh32K8nmTBAMO2wSRShQHcO8afatX8lwe9yeiW23fzKXiIbQsWA4P14Ll1xcPOm6YH65nH3o_Y2aduIHggVq6AxqWzDUztGu8ZaOA4bN8E_CbhgjpWcRj3M2vL_dY4fXzYh24BDeYFMDjyAma4Tlcag-p8CcZJPtl_Ab5W238FiKyUHKkSqSx5vwrSZCbdkXSRVdtGZ_7vzebiSWVRIMx6OtyPo8ynsfzOBC8tsLl7ogAwffLqHBAH8HupxQ8EW2Z2lmaAA6Vh5x_dVdb518KTk16qUOMExGxbDY5dXux9btPeMQanZyrxIBNytISEFtW2ZZytRLUhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALpJlrv4OJQG3gFZZK_g1lDcxFkZD_aGQUbbM7gk25VDr4V1FNj7ZciwJituKhs1OeOCIwzLeGIbXD5y45zkrcyYXbR9j-LGlXg_8biLRpO_sru_L6MjYKsVEDjaxjTPblgQ3rmiqOp2iwhu0FBnRYFs-ttCN2U_v58yuy1C9B27n_JmV3DckGWaQXtFvFfV8VaQ7H_t-43HH8t6nEaW1gsyuk2hehDowAABqbf3KOPrcpggBJiaceWX--RJM_Zcy6MHdK6I03yg-RGyJm88-PfEXvWMnqRBnbOzx09_KNDEFtzLx8u2q2NTFjHlnL73TaSvQH65qh9gm0dmxZHX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvxyV5o6NyVFdT3SC56Ig-sG4E1WiChQM72-MEiPPCFDGp8D6PYHgtJpDJeXQ2rt8UWn6YNWi_UI31nC2J4CBqz8vIfwD59qOeN2CSd3Eoo3hVPCbKj5EB89400DtPZX76WpJaV5TSEhfMv03KqzBWuQl0xIwah_PwOJURTcGJEoicep-rfU4Ov9IvhPJBQONEGq7NPQY5u5JlRCAaiTQNjpP3rWZlcKB0HyHQJbK3D5OvymQQGX46Lg28JphxIYdOLGmeVpua2O2OzGzychBxDuv-hGLVyap-GgPIhdaG5XlYPO9TI8nkgt72G4XLrTqzP3PuRfqqa6ZSdzq2laFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=JBWf0RRYUajRtTcb7-jhJwu1JAl8TfqCFInmqy7PVGN4_wBOxs5fV3xaBF4V9LlmSxJnfGXpAyzSUHsAsZiwdcBX2ejtIvSaaYYMB-33I9fWTrRrj4TgYxAyxeBYGD8Wmcx9n0QHOAUayZfL3KWuDf8tDrQ_BqtvATeyjwUdMTbw7yXztyQK-AVKp5lgsC6nt7FEFT8QnzpHPVQzyRvyMInsB1zSBFDcnXDiFETAy4etqlM5TGSjwU3dz-KbJBdd4adJX4JFxPand_eMQtNCKHusoqn0uj73-vzaS5ix-F9b8xggT3I_VdllgVZqX47IjuKitCpovH2q9iSg2qrD7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=JBWf0RRYUajRtTcb7-jhJwu1JAl8TfqCFInmqy7PVGN4_wBOxs5fV3xaBF4V9LlmSxJnfGXpAyzSUHsAsZiwdcBX2ejtIvSaaYYMB-33I9fWTrRrj4TgYxAyxeBYGD8Wmcx9n0QHOAUayZfL3KWuDf8tDrQ_BqtvATeyjwUdMTbw7yXztyQK-AVKp5lgsC6nt7FEFT8QnzpHPVQzyRvyMInsB1zSBFDcnXDiFETAy4etqlM5TGSjwU3dz-KbJBdd4adJX4JFxPand_eMQtNCKHusoqn0uj73-vzaS5ix-F9b8xggT3I_VdllgVZqX47IjuKitCpovH2q9iSg2qrD7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-7rWmsn3ANntE-_tjchES7xHfyVZqbAWT9K9RLS03goYI5p_Q6cJQPX60FRxvsz58EE738PhNXtSG1SDglB0z8z1UJt5LrlOMRxeqjVuueAq5ztnAINmjI5G7io47PXbQVSJzDs5iDb2cZuKbq91rRrlzMP3nArHNrRK8fS8z_tsgE9a-U7jOpk9sQZ1yNqENLqqsBVURA9BcfttarO9THAA_FO3Ul_72YLpQaWJp2_o3Vu6-2WZ4EHPTOSEOu3DAGkOqr9tDo0xuk-HCR79MGSl9t3XG-KM4-dw_WOpHMVGdRmKtXDN_bSIBd0NUzrgccGpvoDQR0XAvu2zQLjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdTk98cwweZpueIfcbK21e5iECbYIt86C1tLD7SCIcuEHYhy3-94yLPAxNI239hfI8PkJynB8_PIPwBb5WMi9JQwuFuGYsjqcZWn05sGBb_trQ0b5-n7HgTBFKJ1r97Qtegn_e1UKZLFxVLWvgZXgAt-bFoNsuTQkW7IGAxjnlySBeMoegrTlsatsbZoj556_hRF7Kc2XvVnGJcqJ-oq3IMgiLIeViQuNHNlY5KPnfFg5uyyik3ocHBSICNsJUUdWojxaJU3Ii8w02u2U7gwO6GsWOr0J2vCqynocTbROdm0UPusjNDC7kj5vqodRN58x8fgSRbb6LP3SuvbXE7R3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5DXtw5pP7h-d7deDKTas0YFknA3hOzcVUtkCzJ2o6ry7p5j3FML3cTD0Qet94JE5ru6EXVOyxHmnOnFaaEkA1TmTl-pIoytOqzAp48f7rJeJDrfLbScYLJomyKddpVjWlnLtuf41mSjgfeXa5UPCCDorDjFTRUp-453xYRH1JIi-P2E2_lFqac3jQKpzQLLnVFflaVK_Oe1SCrdbBL0RJSIzU2fWB1qFaVFfl0FNjgFsBIIzgm_IukbdGYnW7u_FfckzarjHbtsMzeSvSYMYJP5KXUq-Ba_H5OtQyMhIBBlnSY0f0QQ16R3OUe3TDs9F8BVqbLP1CIVJ7oFgA5F5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=G5oEZLDDUAZglnS0e4Ze1Xl0mnu_kyAXfnk_sLphfqJpUT5ogniXAN0__vYBKDozxuZNY-rT3Me8AmWytoXwhI36TR6QJTsHHZIuNKMjQaD0DlJsbn6j0jSQXITnUwCpXRnvH-Wpm4OwlRFNaJrRwm0xuvLiTSziSBXw3s02NY4ecXlzRyV4cXZk7WLljhLXwFZ7rqyiNE626x7x-KyeBiop73ZCnakGmYa5BAMw9iKw9QcZ41ZNC169CnBgfQgnpjcq4ZJtVkry6yO6pEnBi1K0A5yea6FykbfwenHXRFYd2z4HQkxDepsNbRMmiaqQ-BsgOvXy1BYx5eJeoby_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=G5oEZLDDUAZglnS0e4Ze1Xl0mnu_kyAXfnk_sLphfqJpUT5ogniXAN0__vYBKDozxuZNY-rT3Me8AmWytoXwhI36TR6QJTsHHZIuNKMjQaD0DlJsbn6j0jSQXITnUwCpXRnvH-Wpm4OwlRFNaJrRwm0xuvLiTSziSBXw3s02NY4ecXlzRyV4cXZk7WLljhLXwFZ7rqyiNE626x7x-KyeBiop73ZCnakGmYa5BAMw9iKw9QcZ41ZNC169CnBgfQgnpjcq4ZJtVkry6yO6pEnBi1K0A5yea6FykbfwenHXRFYd2z4HQkxDepsNbRMmiaqQ-BsgOvXy1BYx5eJeoby_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBix07JML5iggR7V4fPCx91eGJj5bwTuzS3yBbC6svD_PY3J1lE-Zco04oY-EHXRPXDmYmx2RTpXJ1w3rC9u9xUhHBv3-XiKZHSDSEjDoMApcilpnxzTq6UjSCe8gBuIyRQduLWuqRM6r8Pe9Scb2U1WGrVY5OIZEPhHvCBzguFAcw4psVF40fR_aEuxsTSZBN05khY85iv5tmq4gIOLKXOp3HsY-cb4SgZlVbsQudU6yuo2pfl7MVPIIw7W3Y3sBifb8KejEKNnXAwYdWlXA4-LoFdsaNWeRLpP-qpgStkzgFkY419wOKu_hQ-m4p3BpfuVUJgFZ69AZkQGVK0tfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQYNgoCx4TmmRLiRRnLpt-0zs15nTFafN7ugVBmp16TNTfLMAgYYzCjZRxXlTsdHwGHI9y5SdW9G_VUZJ00dqKCWq44yPzj87GwtT5pXy9i7-X1hE2stfUefthPLETZxNOZ82iieXlDuRWSvi4p-76lt3swRiSnhF6cxlj4czU87p211BxXEChWLzGbNSdabrmFLklBG6kWyVdWLnDpMRAJOT5xVhm2S5sfCBs6cNWdodvAGj8f2EuZ32ySSgBBxuBl8cCfnsnKcVpgdel8RIqhO0zrl6E6tyEZ1nc0xGPjGm60ZOcRk9Uec3QPFfZyra3_lV2qpFyiNoojEi3SR_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmOEsW9-YfzXXzs2snzhz0LwwkMsd9JXReqxveTxxKDRoPVPW0zGzyCvnG5lKe1dn9eG7A2DPw-4Q2QHBzrMdkXqktTQIvdY2X-U1-OQ_MQRWnUdRIZjkFVhgTCj9Cf8RNBb80INxSazWlsOPNZySXc38YSkCEauSWnZ87-Sc2JHrNqtcDNl4973k1o8hIpWRxQJaS-GEoNuO1zPq7ct93e1DeDqCQCRPs-R0akwSeym7XADtluzc06fKJLZGcMss__MDB3XAR74jLMcvu86IgGVywuysZSbAs6elp54hiXUgdeSGhe-eq8JYNlNMZHEZRgDziNBHAJP1nOqHihYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRg0EtfrpM0fXBXrlr5x5yNucDsBMq9x8_IBgDA9DYqh_srdijLrRkd3tuR29Lia3B3RQRD6z3azdETofMfo5JRE8cAdpy06EP99TrPH9rbN53nwQJfeNKgR8iZ6LPrziOAs741o8MTdtE3diwqbiknsw4ozNHxkQtPGLw22Qs3wPHOuGH8mg-n8THrDoWRPU8udm1jA8Sp0kUyoMAYjHSYrlGhz4A5Zl5xEUMwomSzr1X0JV1O-jthvwAVieeutOcL_ceMnR678w4ENZWCatPN6UxDzpHD574hHTN7LuLueIE8imI8yd1Y7T8Y7knVN58iTgNa5VLn6HweMwAykzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzfVmGldn36y4pfHezSGwksUejVobnz1UvkXd1HDlmQCadF6c8-kpmIbBfy99MR6FKfdyalIZMz8GRFLQ2-QvBryVO2W96qW6wPYYT-ISS3LMSQ9auNJF95KLdaSjudsXvAg2RChiQAE0EO-Lz1zAkaPx8V5htUb7-fyGcN0b2p3zs36_y9LX_wmhLhjIjlsqoqoUeHSyygfeEl7AfIszJZfA1d5xmV8T471DeqYLsYJb0oRYDe2Bi5hJyicE2E2RtiWhJ5xhPc-TCAEFC6a0pUHnoiobpZq3TA7QcDasf9kSJEY-cb7kFj9gjQAOtLRDc0aYxB1OxW9cdmroKZnCQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=sWsfHxh0UZAq9DaMY4bo-e-t3sJDnkHyH7jknGAnbq9r3ZukqbYXr3l3wDu4qOaJyjbLeZ3zeqsYY9NKTmmLZqJBc_lPJ_yoqdfnTmp4qaR8Aw0ImA7zy2Lj5mTwJvLkGPCcweCzBijnhkEQNnFs_D9wgefCiccLmmYgymaJ6y4u1jvJMVLc4lIYJRxllhaEscLW1XF3YlewQRINAWFQyU9X0KeOGoOoR8j18VpAU1Vo2mOpLEiOpqsrSNyoW0ulMpYSWLbrc9M4fzOIkqaHKK7MVK62wPW0tcqS1-R7HeNnb3qRv4zTlQo730Hsvjmrj2ohezkMy33bo-vc0Faztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=sWsfHxh0UZAq9DaMY4bo-e-t3sJDnkHyH7jknGAnbq9r3ZukqbYXr3l3wDu4qOaJyjbLeZ3zeqsYY9NKTmmLZqJBc_lPJ_yoqdfnTmp4qaR8Aw0ImA7zy2Lj5mTwJvLkGPCcweCzBijnhkEQNnFs_D9wgefCiccLmmYgymaJ6y4u1jvJMVLc4lIYJRxllhaEscLW1XF3YlewQRINAWFQyU9X0KeOGoOoR8j18VpAU1Vo2mOpLEiOpqsrSNyoW0ulMpYSWLbrc9M4fzOIkqaHKK7MVK62wPW0tcqS1-R7HeNnb3qRv4zTlQo730Hsvjmrj2ohezkMy33bo-vc0Faztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Axe64mRqb7IJRX5VgMCraSrhB_lWWOt8DQs6C_M5UDgU0P_wirTO1lOC79aTBvssfyd5P5UbnNMuHaAXduW9Ojiy2CezuGWxG3sKr4SAU8D_q1tBDXxL09S6m84suU0nIFQw6ZvA4sz8I9hJCuFc24gSGUeTKGCud0fOZQYTrJeDatbpMXyHgbL3Z5qWxIVwCfC-TCAEeDlq-faJrDC1NhsaNFqvlp48vPwgvxdy6X5s56wuLrXl6mGfZrkdp_-Tahapa2mvsZ5ijA5zYDXdmcVs7IZJXdR46eYs_ZgLMgjJ4xOu2Y6mhYlPRsntv_HnCkBiPfzoTfmCiypY5BeWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Axe64mRqb7IJRX5VgMCraSrhB_lWWOt8DQs6C_M5UDgU0P_wirTO1lOC79aTBvssfyd5P5UbnNMuHaAXduW9Ojiy2CezuGWxG3sKr4SAU8D_q1tBDXxL09S6m84suU0nIFQw6ZvA4sz8I9hJCuFc24gSGUeTKGCud0fOZQYTrJeDatbpMXyHgbL3Z5qWxIVwCfC-TCAEeDlq-faJrDC1NhsaNFqvlp48vPwgvxdy6X5s56wuLrXl6mGfZrkdp_-Tahapa2mvsZ5ijA5zYDXdmcVs7IZJXdR46eYs_ZgLMgjJ4xOu2Y6mhYlPRsntv_HnCkBiPfzoTfmCiypY5BeWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_8KYdtOjzIq2kKMRizoehBG0I29EwSplf1v8StWe-iBVwcg4K5QfWdvs2o0N_mOoXe5YWBQOtS2BNLY1Tda-VMElOlS5C0zZL7_U2pse2G6N4Cah4udtv_L8LXuz-oVE4IHwVTMSLNecWH8gZfFNSqQVZez7Uwu3ePkVsuD8N8IykXrNGA56uxjfkn_x9IfHfRZqxAIVTBdWvK1FQvo_WpIZIXMoaqT0K-Qcv6Ytlx9doDMQB5heb0zJkAk1VeKzovcvxOh97Z2nr7GPt8JjzBYfBPToNhfjwhOptGxCI1jUjN_xaOknw7yzm2Sw8ghyjKhg8yCHR5Er6Tu0fsGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqzWtBldXyQsKvVaAgGslf2PGr2iXiS-9fcyozpbmksy8KAoo5zUIViNt5_c59A7bZ83lIvGd3FQsfVkj63TqV7QiUFKUezyAmcZcsuasPfQMaCgl35STwCEU8vTcErtzgWVDHqGjfRISpe5hZXGkEJyD0DOIZMWAiAjh7AlfpeVp-XyOwEOXmCRLePoynxfzUCJnAlD45Dggn43kwg9uZDeJQ-Q9-0CIaDguGZ-4h767OO9E94Al-wUcKZg6Iuec4apVLoMuJ9jyT_RMD7v5t3c2Ln77bt2YzCB5ojSPrUaUXogh4XsImHOPv97VHJQo4NzPAvb7DKvo9w63kvyjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0M6SSVso2qlvTlEhBR8d4JDFHQkQtwCQTTRyseFQB2_NCKvggYGaatJJIbWnVavXmQ7g8zy_O6Kdye9cAirAX8tlIsIcP15eCye_-Wfpw9vx504UXkPp0UJRdssSmKMToillrbUbS7MjGUYaYbA4mhSWCp5i8FQlCG3IWwcJfA7Da6XBk2Ugt0fE428oLqbXUZQPcUFgtTj7JhsDCXLb0XMzn1iuNu1AWYAvefKdZpeDiYT3yevNdrkG6O8dBzJUWw19C4wsq6_HWCp53JhSMfpXm7gUIox-MjsbcPvWrrlJURUwWBAmce6ZjKqu18aBop6mQUmPqLgVtysr6rURw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKzwBokNWZrTf9YfqpBNpgHAPxreY0iQxkBNsRwCusI9cyW1ST_iGi_JXi5wLhWxvrQ4LHFF9xmKSIzfhm7nX0aovwpzTFkCEVXi6aLylLQhWHfrT0EdqY0SFqTE1gw9c2strTMfHaekTJWchQequXUvXjKmtAicRgOa_1UXLdBHl27wudBM01p4VYrBnqh6pv7vJaR8Vy7B-nuHXkz2d7KB78Niixi0G83LaRV4WS2Dm4KoyXgkxRpEkjkW4AAQhh2Qgdql5W9nXt6qo-d5PmApG0vX9hYVsjohIK2986INK80dpoVmuHpusaLhlUQkRoIPY2fp7VFiQusxAb_Qdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgSemgkgT2eJZJ1nqBf1dNuDTsNpGRwr9KuTSoOctWht6z5VoT_IJaDAcbTC3Yw-de2PuC9zpCw41qSil-rtxMFv5P6afyJpzZgKiV9aKr-xpzlcaMK8ULZZYGvxXCGGd9cG2EnuDscG0cFUjmHYy2H89rkvDiQj2W6t32LxIt4sTJCOw0V8mNRhGxjWMShMexjX9GTTqr48SHY8W2YSgSdRlZMGqh2JxckOJzIkffVjQHd6k_Ec-wYN3L9K0WCqz3HWiqjq7wo_Io_iFPThHFi6gfpkrUQECUsFsSwrU7cjujero2R2uJYyVXa7RboVLLz_sS54LGHLEVZD3ahw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKlLxKNb5RzJ5B6j7vuOu_uYsZLYUBGxHVam3K-fWNLwtROqYZdKjS5s3q_hn-ZQWzFmeyc8PibxuU9KG_6eRazZ3zVRi7l05PzNC-RKfRh0tOIK7kDLJ7axmBUM0UcpsCWCTTteNs6uZOBiBDQTW_Y2OcDcdFd_SnUt5TR7Neq8icvW8WkOzEu_03n2cFj6OmMJjRFYJMl7cC1bRW1pJpDzNRAX2CKAefuOvTOf2zjaIam2JzT_dnqr6Zo-3EYRERZr6jNBW7Qp_fWa7FyXGODVxxjNx0VVj5lYeBw1lRFFVIfrwX1bwo0O7UNsSSEaUO7_qlyO_Zv5tJbQHrYLjQ.jpg" alt="photo" loading="lazy"/></div>
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
