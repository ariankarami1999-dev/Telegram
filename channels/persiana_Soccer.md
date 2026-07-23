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
<p>@persiana_Soccer • 👥 542K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 08:59:21</div>
<hr>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=T4uxifSQcKAf7iEzyWmGCGk7lj6w_xWvmlfZc5Y81SGny1LWC_uhyXyP9xg3Yt3sVP8snF-_P0lmdjmRV2LrG_re3lScnySxoHlVJP43EeT9InWg8b6GuNleCWRGlyswF0h7RY6cURUlBd7_8pQ2FfHwRFUGkfnrO1kbdPaPiauIjBblWah64pUFPBG5rSZLgStsI3X52C4-Q00vAmHlechQrs3Z24T_In-CPaVe3mHNfDW6jkv0XYJperl5QSUOFdUSrVnO0vLnqGH0fkQrtbv_IfzqNh_-AunrN0iJ4IEJZEjGMFImfAS5ayFCiQp_yDP6o5GcU99ualNeJc_iQG192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIF666WOdbsz4II-VYTtzOhl8qKJNXwTP44KwdYZJ2m4rM-6iE6gNjS-6hdMwv9tfms9wkxAph9mQkI4GcHdxLWt_0t6m2G_gVL3P5KJ2CLs57uvy9UHPcXJcqvw7e1XHfap6FQeo0FRDc-KySsE5u6jkW7e-U_9A9aoRNpwAL0RdkQScRqqwRa3T1v-9gKyedh_DvENCBmY5R3mBd9XMDS1hqTKfthILCRS52moh4c5DDlywO45xWQLTfnppbcZJuM_f5p7iB8ALUrMQUC44HR_CzxrCLZhB55inXLQ2FB0q5HsaJE_Bj8w9S7LTqB1Kti1Dcb4dVbY6FC4ew1uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukJ_B01CaSBwt7R6RaF4WpI2xyOCOv8Z0vJbb5hCTWvWGj0-9YB315EwGDUwBhwwiHDwngNHoo0Lj68X47X2w6pxRXe1QDmo7Bpb59kAGFM2EwRzjuSSmR5WjNx63V3Tubbf8YvtcVY3KZpXST0k4E5BRIIRHSXFtHiH1JgwVL4sjpGWSlh1lPE1a8IsncZ0MsitScVqRNpfv_onA4Oim744rBjftn3xLb4Ogy5G6Y1_ddSbRBo_KThDaiZLO2qoxr1Zv9LWZMc_LsgVEhNHV2HZEAtqm2VV1CtUUu21u820OzR_ix0bq-irvSM3Ou_X0qUE2zDVgmGjd8GycJS9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMR7MXafpxlt4ommh7HUAWR46X4-w4kP8MHRdq8RAPkKd198KuK8gy29w3GLJDR1X5Pnbs1wK-AY9YzZBtyGxpnrHfXmFyebNHYS3dTm9SEtd3OtPFPsmqztkJj6l5OAkqAGnWY-LNILy_xnD7dAEUjeFyEzFvWgQk6lTUQ0TfpITswcuqPpqqHjmzjFnhgwwIlRNmbAbNTifzmJkIbb4P9Ya04KsVp7o6LJymAupFe9GarfO__nJUN46AF2usBmYjtbKMjxM7gL36lgbnutyVFlILCclfXbmp5-1j0KG53ppAri7CIjclUl5VFrSH4RVR-qcRmYa3okg6yl9OOJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXntRCzX5_llerWe8I_BojAodCJKRdLkRSTaKEzcwfA7LM_0RXLs7Liwin0cWRZDOwLeYWp1MM_mMw4vM5-l-_Jr4fWO3gdx2DpAgE_rEUvGPQznrEQl8sYTOq0iziTdcIgGHfoup340Ioof8gi5KpV3TitkKTFwd9hBeKuNUWYZkweF-RM8i3tQysz3YWR35DP3de9QG00pPDBFHNLeCjfxlbZZKzuGoqNC6AcfUesEm4SvjLarbPMGB9V7IJ7MfYlRrxIax_vI2nqC59VkhYZUXFkyo8asySVa4rDnJJ9hjcYwM3FWPHOVrat_2UBpE4lLt8mUfq7tKSTWswsDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwu5L_IszwIcMwcL7q68HkFtctbYuSyM6ia3IyluQ98_kTuVehJlUe09z3H4UKYfAX39wcdk7tAPlPyT7ghroiHDIVkZAwa3Bmhv2T0g0E_-SKX9e6S6GsUVIVPNFz5ABpFc8dkDCZ_6OU3zoHcMj786hc49D-riW1z_QA-JDln9seULUKafU-r7YBVxoCswsYomxFqsfWNiTG6kBG-1H7P_srLsVaG0x_tQS2eNmlZpZrCpcmpQFMb4q_qWPjSUcWEWB0c1hY2OXH_EEdDn1eQOIq2qmw3B4o4xPHxriIIWG5bjNab3F0O1WTCNT5nc-Co9PPXq1fYJ7acx169WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjMdbhSYQEWjQUmy0VvoCtrSuHypGsVJ8GJjEXv-yQvAbIFV5NfDjBKkdC4CvUHwLoRPhGuibHtEluMVRuxufUZ_nd7K-MYW9nLeUSeJ-HRuKgpZFqg8ga5rT6MqZ55Vv5bI_Y6RUdbTg3FdknBa6_huii772iL9Iq5dylG7wde_BfMmWl-LhCYaOuZyb0RD-6kGsFKmvdlBedWZ9h_2RU_r8116qCgzwIkMOcQK4X0y1J2KTxzS9uvWNsuHJ8dz-l6Ic6uJgHsEMWzJxmSzj9wnGdhJV6hx5bSzQT00cT4FesVZKlsOm4fQYaUpFAQygfw1L_CYkul7r_aaM99yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqVFtM3NniFHa5J4RseXNmyMGrZo5HFKlLOIc6V17ihBOhdAg1-su2zDR7FTWR1V4T1zcnjHtkMSW_23nhnpIcWUqUWU9V0Mg9WOcMnELfX_gbNTrCDrrYmUTP6-hlpmj9-SkpHqnMZLfPNE8bK9aqPXx2_sQvEQtCPKr21FWng1cQ7GJ6bt3oxyX9O0TFd3O32dceq5-xFn26pGyXDWS462iN1FBABU0zjN8_cn-GCjePLYWVf_RUlMuaOvhBz-TiRMktIAUY6zv4S2Fn5dCywhrnHNwm_itYML_N7lsIPUlWakPSN2gIWL7EsdPNYmx2T9cMyJw8GjZyQExo4bNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH-fL3kUYiuQSKyh1HbE2Zh8ZUGlUmiPpLn6fH3TxDbCIngRwRtSJ0JOP5HbApmhV9ePRX4c-9PCwi_20A9Z5QWKWgTmdFWdG7my7wwwfCiKnF6V9_IzFOfXxW2HavCztdxHX2xxiNKytnfnq-XUezVm6kmV9eEC0yqJs7Ud_BXBBkiDfEI5BbC5qrev6CHWqav6EU4Fln8QOKykA_P5hUZyguExTv4wGCVsoZZK42K9PrmDVto-RrJAJEpsYMoPsN7-D2mG8zkoxncq6yU7_CTAxYSK4UuVJSWG5zLet8edRcEQHqVgeg5VAh_9iJSgsVcP3jHDkRfqAOcjxVYFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kximxwa1xSeOGT5EhPtdRmGBA8AnZ5XlycBuPLj3apMswUNnmEBVAj0cxJMYIonDL3X-iG6GfxQGUAzLM7kZJUns8TjYOEkHU0djHtVhoI7n_lyLz18abFk1flfyAODGaZB4g4p7r-yaSIgFUGM_vRt37RoFaaRx7ZiytgL_h-PWgYTRyzJ-FYFWJF-Aj1AGF4lcRMIvowzPgM3A6O4nQR2e1JsvpLSXvzhUh70zu02hOv1NKcsQQjybTgELhgflErpSnKg0kDzpv_CUsBib-LodrVTjrEk-OmRWDMWScOgJVgWzZS9iHE4vib8DjQ6NKX65N662h4HakPFnE2cGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCDQ53dVRSVLigWPOWQioIONilyG8qyKOqzB0JikvX4OqovCjmzVk7DrhLEKo21yZpv45r_gzvl_cLUXxRAl8IUiPoVC2t0bxqLjXQ3g9zoepr-CHPAuG-BsAioQnYZtNeML3vmAOe7VoZGSPGRmQAwVJTY8kFaFSAVVTK4PKJEq2gGtkyJWXVise7Ftu9X713qtl2VrgM-oLhM2KsEhLljDsCxLyfwrii_q3v-DgmJj6H_C08JGVw2T8BNRJapg9_APcDQ8vStxjwcbO2OPaAhrWIw7jjVvMtamU8KE-VBG-rCD0t-1qJl6Dd-Uxgf6FPVd3pbFS4sXXdJtO1GQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plEyJ4c3D_tK9Xst36asfQ1kkjS2ydDTgo68ed8d06Pg99POE0mOko03hzNdVKC2settf9OCE64jQqtIk8SooNchm8gU1khGU-XYr7uxiMVJzKXX-1EmlyhYCz3tOPQMG5M3AVgKbGfS1Njz6dtpkIMiKuL4Nay4Hg9kkzIBpx3sjEu8Uj0cxNtlsZBI8pufB-RKaYsuisw7C6WMgnifrSKHcGumwIyXjg865W-iIpkBCxxHcemjyFLE_VNTc1Txr2LVIu7HFwzuYU7sp92D1WAcXp4eKt5wRTm5fC91OsziDLhgrvOkilcK1KnXT4WCUF4evKSgsOEfXhJ8gu93pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xuzg5Un35W2yUu9F6gQcKtq-6u2Ed6s1WjeP_Z9PkIImX9A2f5rRk8blZvgFT8jNTKGcfACuIfaNLkGw5dNYxf_w27E41Kfz7avMO9IY_dVLg3Bftjmm25ij4K686u0OCvJ-udRHM9DHNyonTbPR2KncLXETYLmNMCK9l6SYTfC8SjpnYwHIVqVKKTJ6bKpO_R54-6Ao1pDlW-0UVpOR5QNcMSuqEGt9eeE4LQzfbqtVqU2BuVRLYmYvdPLjrxPytvsMB5SvhcoXqL5SYjO8-xqctmnyqvXCUgbxloOajxZidnSjrhWT_EvsOvFVtaGvQPuFY9uwcrUVNHGVPjQ2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJUCgor5VbZ8K66NFXQ28mA09IAIss-qmDgkWwLsyAu3r2kbhsfx87hcLMHkvDsxlBc-0D9gpmmcpAc6-NjipBUEM6Skf60iJARVX1-vj0rDBmIUThFFYWApiyNcIWM4e3smB5vjHdqskxFlbvC5QNQLQ2TLtqhtmnTU5czvf170CBNIyX9lok4FAZdxbMMqdGVlR360bFUrSxQo5sNcRCzK6ROKvd46aBfeHY6IrdwyJn9e8senUPYpsdSLrMomPGIQ-QWWjp08VMEYVmRO-pxFVEZ19mAsR8-kJkBz32ilk1H6JVp_NcJLDFVxeV9qCRhXuQ6UxURAbSWVWDIOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UOZGvrhoLMm0LxYdc9PLcF0um46JqCJbklLZXFE_xX7BJ59hOU9WoFC9kkCMZqjfSNVwB57Gi4ZowdxmW5CaU8XzpTaKtHbCkr22m21EDgS9F-_b03M-wfXq0Al_hByTuXyBekpJZlJw-EqApGGWhcdnAIdRaxslqLp92u5J0Q3-yJsVDeLzBFh-V4Xtke7LTGZLMUj96qICCsmAlYKoUydpszslwqWqHk5iiTsQ-O5tFFabxT6iGoIEKXE3aBOFRLAv_jA5SDX4PLnn7cwt7GXJGAhK8rsoOFGOBpO4EnW-OZJOKx_zQJoUAn3dZgtNrjp_2vqfNzim4BBgSaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G60uWOq3VCMfmlaOs3M_GgpWcIqr7YKvt8hN4AdR_oviN_cuzR3txXsOIiEr4owiUBvLnNinWaJDTS3_PRWN74j6rEir5QuPPLXqIQQLi_zAYaSNUvu8HPMSI7yZBCCaos6RVDEqz4BtasQ4nzJQ4wB8XVH2cD1w6010KSrakwwunMyCYryk0hx2KtKIWz3ClnXasKZG_eAVColIL0i6xrayYr7Ptkf9FlVYEWBrE-NfIE_EvzXTx_FwBoONEhMAZ4oqtj1JFdYa0X54T1Na2y7zbzi9cT_Ao8ClK1Ar5VOjEr7gIq5ADhVzaBTAkHqEdVZaKYZIvhWJv7RQaPR5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhl5lWbVz3Az5HdqcZP9Vi8-xZU1pNPdhFK1SqFNyVJ1D1YVExR0SgeOQ5gBhl72rQtKWXNummB5ZCPcCF9NyfJvh8rz3rW3Q6fxBtf2wUqrudWFwHqG5vZcurwOqQ6vWAI1K2xjeoK1jsuyWhJpFmS7qmUbLoTa3QNcCvARtyAAhapTuEB8Sd_ifrSUtjvNuMxi3g9Ad37eI74L_aFpjFefcfXy1KzHFIuv7ZWp2PnrqpF5ybGl8fEidCn19MLpw2PhGDouVdhhHakxQ84tBbEdxxeR0I8QKEwlmRLAZBnfDUWpnLSH4UIBDO_I6udW-itit3HLG0_xCk5D2Zp57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhgPzf5uBt7UUqdK3UCtjfSKDlkXSajOkbW3exoOOwP-5yjhagFN5fPksycU7BVvQHhXZVnqQ_6bpD6Tmn_3k8qZVVG0iM-ZVoXGIGC-Lg2Bb0u7F9DBPnOcDu8Nj7SJKTk6fpE3bquGAPG566hlZ1wG0mUXR_xS5EHAQL8zRqvqgdzBR7IHRkuAf4mkhNaS6_zORFOV_avvYZsDoI0ihjaGLXZ8x2oCug22dBWbaF7FP-qTDQLc8hdI0eDqvHNXHpgxD_h_f6cM06VD8i4_0ANd_7cYyU7bLIpgh1d00CatW-Pzv_oPxCdBAGZG4zYqBfyqZS9WPSD_LmcyORosZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70ND3F2a9V6v4ZtLg0XmQH8QBCYRY_ccX2rfvDTql1Z_1NY2Zl9fSnipaGnB5M2BnfUNzNiuAKUUjJ48MMk_kCJHI78pZA3AMU8kQlyA6y8LGAdseO_RRJ16wp1j0kODKi3IIhALPeOuMN6FUkBpdG49lJUn-YA8R8G4XM8V3bokWeGkdNF5KoZ_DRvoF9Yrt_RXITfM3TwOT9duM4jQTC_ibY9Mjtz1v69sWcKst-aSFE34LfmG2SB6vPm-gg9CkB5lCTwL7oNUgk7dEshuqTktxdBzfhoV48FFtqD2vNj0QmZlMlRGZGTcavdIsd8AqhGNtWy0uMvdYw8zrPNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eb_WnG1YG57dc4XDBtTSXatrbWuMUVcKhKiTnv4Y5eqeaCCf6GcQx2F-N_cnfe0eqgQsKgrgsp8rYX5qZ4QderOu-CjREupdkuW1Se2EUwhMNHtP46akV9scOWwCWMnTolmavQJjrtIis8Y8BT5SgJbHoRBUtDmIlCHRzYySSTrjoBiichI9G9BKa0zA0mmWmKp5JHrCgcU1ditMFIkcSSBPs9v9FCYt4FEONNCuEMaiDiJ5nuxvpyKR7-RU7Jvx8VFwz1p34VWtBd5EI8j7SsIER9ekA5kO0qk6naxELqy-gtFO2mXLWzAnP1KN7oFQgGuLQF9pwAgn89JLWabiPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy2-tY8LzaIU7AwiORYqmPh8Wy0bYwdD_6GWhDMgT-8m1oa-QhyvFHTf5ZBrl7DQZ_SnQJk19pySOE-DINIHtxkTZ-EqoDjxoMEoTxmCiMxDavflu-1STKMCsCvsWnMVKncWx9Bm4lGpJ-6q6Ufgit7hikbvP58WSS444LI-VF0wMQzIOYws6b0dZP3QdFBqfMOAES8ip4Hcr-oS1SHp-In2pznaRviNgi-Nbt8rlWExlFN3CtcR45fIyjB5tRO_0zYOysz6Z70kGQXLQUPpgDF2wtw7yF_Ek3FE7PEdnt8L7_fLJzxD9TWsUjEMRZTkNFB6qJcK3hrnA7fCYhWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSSAoSHotcKzsifmL5Urg49WD0rQhZpQS3q71oxMrWEzJPCBnvS5xkeysgq90OJltkBn4O630DWaNFRgc9T_Xwd6vrCoLKPFgfQwnv1GgIKBAr7WOtEFmWPRWgaOHp3YnVAT-HKNKw1tn9oetuaEfr0JtiuN74vjkQlTjbnBKJ6rwlDfRlFSRDCwBh2dV6mZHby0Q5ih3XpOILpK53ZhuqJ9J3_gGnsFgT2NbllYD8ITbUQ5OFnLQqHGuNxJiVfgf57vbPKP-Xi_8HKg_4cWDNHnsvd4y4Lv5QbseSgrUwKf41HrIO4L11swj_GzAnnedM1Du-rPZeQbFzFiWqQCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pry8JtCWaoSfBxKuF47E5XSHvttHF8yfeMMqXUSXmJgaGa0PUKv3pUWX9SvlPIBjaKCXLBElcB-t-Kj3MC1XrZsD13XnFSGhRfTbcOBnjK4hYRpJ3GpRjEEQbZV0qNHv3nsDhjJd-cFtYmjxe78dWIn46wf0A_W420OUgObXlrn2RDIuOy_8KgbVFzBvLoRyxl5joYsBcqaNAqUnOcCtBO4IVoMsCOM6OF9XXF5C4J_gMGyJdyjgck5NzdK-vCMkmwIoRF0W8PF4x_Jm0foPNB0I8SX9Y9JisodOLLT-XU7eIqYckJm-85ef5qijMje7atfYDdy87-g5BlCI8Wbx0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYmOsvFB9N8qE68B-MQ6S4a4Zy0GIaXEIdR9NNsKCvy9vxEBqWnm_R7vAxahDgZOsej8eJWQ__GTYU_E6D5iTzrUN_HPdpeL8x6VCqUmJqS4mD4mGueI1yt5NrgRZVDvH2mNNdOpaNsNQNEAn40IlWnunJHxlp_qWIsPzaCiJ-3BZRitEoEF7--9opzCHHWY6JuNUR0US50fvTNPQ3UyDui_GuREgsa59YHV_suRx0s6Ns982joWPRHplQIsvh5UbEUDiHzoz8iG6TRBj8UHi__uoy9KJ9A-3b-LuxlF23lbA4h3mjaWWYlfrOcAM3w3WedYa_NthTg7qSbd2OT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R54Nwqcc388yid6zHjewZMC7-9ePqJw8RAGjxwrQxiITsHgeOzwYAYq3zsaoxsZS36vHYc65Yrodq2q_bLOK3qhBkPBiM8xtMw0oj6PJ6vFWmCkoXfGqfR4fFnZEudkahbnpbtVzFragSnIr7bwUY221fCVgQj-3zX0crEQlHgL91I2vBTybAL9VoRURcJZtc2iiFT7fx0hc3bAE1sKC3YWu0yEYr_JUJkgHKNBf_i-TCP1vAeavZJyH2Da3JTuMuX5TMfSXTQVVXL4ZyQahbn0NJyD18EFA8jF7PfbFGWGFMhkZeMCTZMsjZvsBZyYrKhC3ePPH8CVOrZRV5_E-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz3jTW1G0_xvif4rDQTe2ZP9zlnl1r9nxAipSAT_N86piwDshYj5m5B6P09dRCd9gN9airevrP6H0L4vswKyROihmyY_9lXBJOPb1g1NbC5Roc4J5gFVtfjrUhvvK4Hj_LHbd_-NcJnAPivjo3yJgnW8qvB6jdEvI-HkONENQMJT8oGaH1ZWcKvfCQSSS2BdSOUmUhpvBlKGgsUn2uo0t0etjliofxcuXElNJSu3v3he22S_hoZ_hHKoG-ofhzmFlat0IttEl_Kre0qvw1Kc6dBfCBHzVam5kSCt6HfgHLNnC-cw9nzyXOw8nBmRKzYWHgdPYVFKX_GPq0tYDnw0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlG1fwN8it3DhIk0614efhKgIexNkLb3gkGGtXDMCYnltTTRWpEjq4oZdAhP7QaLJEGUBPMdD3cgN44hghSnfaZt6DQMPq0fIFHcwZ55UP2NTNDa0u0421E8SoM1WO5bOvSnUhw_Tt0dPEaV4YlNi8TcLARn-kyoboqZL1NLaDQL9H3QGvIWd6WG0DC3E7nrsw6Abss9vq1bZ2GO3MgzLKxHwLOhkOig4SbXjVO0uKTEmwW9xK7DoQ6LQcBHWmEyWm9Qg-N4sFStR5eX9t8LxMpofHKRI3poX8Rez6DroOOBqeHBUdPCGLrVPMnnIh6LKnuB-W1EJ-mce9Zgv_3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvxxUs7wQAoqVJCvAU0qArKmESRwNl4cTvpBb-tLV5aC-3_OdYuKuMQuve-lsnK6Y08ViOlNiFIAFcYS4k5mFaymbs_jJ26bfezXs3epzoCFhMqORSZI1BXNZdilCaO351KZ4o98J2XFVE5T95kuyiLqKyBmgfiUFuyY9g1K-zmjBp77oxQbc-M2p-tOBI3FkCXpJh4goJOm94rysuMQbrFww5MrluIi8NwrXMPrQspNbscE618nbOdbf1Bi-y5Sjif4ly_sVTcMXQSz1UHLRL-wPGncLDMvTlcE1yVVX45qlFdr-vAQWuE8ryIBWrwCnWP9hhUPNj1hFsvLH4QNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At0TZunPzRFT2c0bm5gfNA7l0H7Z0w6fKGwqYIXaUAtO7y82LL5ZYkhwpBCIDZbD757gdAj4GxHwhG1Y--g2aXQJb7-x6ZfWTgle1WHOQMxfNZvbwCE4e7a2ayM7XSLzzmKcee_DYinJ7uJIp5eeJxrvww-GWWPsRhMzGPJwL90hAo9QxXj-1Pp_mxugc3bIIKBRsWGtC6HjlYjF08AWe2EpYIULeYkCoEyPKO6eDu4aBM0oX-ElOEWUNqZc2wUIwL1127wVbem6Zw6kpJma5ZE2YACop2haSIT1QBPC0m7q7Smq0ae3hRCn69-d5JT4NV97yH3o4jgleyBa8CMwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-DUfV8q6DVx_VQK_co0o67-_bnC0g3V0ksAQnNo1l9y6qmY_H2TsKqpINAI-7vrpioRMCh6jIvZxVJTMw-1LoObXV4I2b9XkVKkQIXeQbp49PeYkTT9tU56whLEViwzofNkMjERCi3ZhXfz3__2dIJPAYbB-RPOm7FKK3Hkf8xDo3TPiXUu_MjXb5sZiteNZIDPngIBvRMXUtByL5fWKR4Zwe6DarBERNHVyMrCr5w0PI9z1p9CDto786Epggh8iuSrK47AwV2exNQidQMSKYzl5zduDaPuPM6L90DY1-CBon-I9W_n0PX02bztqwJSBQ_-xlHtefMAB_aq5xTYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FzlqZMoCYHN5zlMATrZwh_Ez3zoz1igOddFXgTEvV14Auyr32V7VBQMGmtSmoEUfZu178lfEaDRA-0mHDASVU-OQKtBu-n_HavXCvcemOvvf8NGzFX_oOk77lV0NFQDPwD7wPy1lqEgHEqIR6NS-SVVTWqODXGqzUMF7Hrs-v9qp1LaMtebMZ_Q2rENYUfj8nNW3AVHP5QwpzGJoZF7-erzXoGylEAyGS1wRHMeQUuHfuyMAzSIXwSxOTO1HqLN_-LhSNigHDFHswnRMlOdP0BWVjBy8VJXgYXPI3HruX7r39CULjXIBZFyayFOIRSTImhfKRZK1y2ARBGLRyelw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMtFOa6bgoS7kp8xrlCF6U9N4dC3wjGXK1zR_I3nfIc8c0jw3Jhy7NG4FdLm_0g2BaGhWNDGp0CtCCqFpdim_7O0JtY-XrvvnKlHTgd1MtBHYY2MrtxF-u7A4MQrLqDhmrVmYIgdtLu6F1pDaW5e7vR8DDPh9eBe6vhqJefhpDtySVSMiJ0V_FcRJCdX5402u85NXQLOEy8x9PvzzSN5bCryDOvjL0P0-KTXHxIoDlce98pg9193NJdp3fli0tpSPMYXgTf-swHPmJybWdqR7hoWZsSe3PbzWPI9I9lATXvwbZbSPe_jOIT_Nva7VCtH-G-I9-KURzHDSRUToOMq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY-khBlZUhuufMxxnbXVDkQVMTBHqP6QrvtsH9ocYPInlxB9l-5c2SUeQPIaTCxtRLGz7zc4kncHsbRwzN_FPOZQemA67AXjuYvLUXfsMmzp_tedoDJP8Gp_CWbTIqFOwqvPTBpbrZQ9mxoLRip_1YmAo6rvb0uPlZGbbRMVDvVUSeIoWP5wrHd5UsmpdkNOEmUoKxT2bFGHxncJGFCvaBRWScYIcsCStFfMuXFbRjVNWsRc-FSAPlxNr4Upugqu5Y6fgbI5YNI887Yzv8BPH7HfZKnhHGL9voIpEUGkVteG1r0QFVXVYBkVB_rog6CjduV6Ps8FId37HXG9RZNDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=U3-p38p16J_TzRW4lCXLjwsjhhhEmhX09JjFcUBWrI673fnO6pDAONR0wcPErSYQrcPC2bFsmjPcpb5mx5qJD8Y21isb1vwIKQWDdIKlgNX1Ue3zQMtTDBgi3S5a6GHGXjgOos0c3A6B9N5OE5TDKSgqm2RvYYgDPuyfPM6VbCYJ58b0WQDoXQ_rI-5UX5Y9rKqu5bU-Bxy7uQ_ufBMiVau4D4UuopLbERgoS2Iaoa8VFtcwBMrL4BeYTaona6f0jg7v4v8kYgLHnETGvyDEDOAOeDYN9vRPM3l5fsncN0bv3gupDllV8gmoT1_j3UvZKIOS0lHISEgjpUmzyuVn2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=U3-p38p16J_TzRW4lCXLjwsjhhhEmhX09JjFcUBWrI673fnO6pDAONR0wcPErSYQrcPC2bFsmjPcpb5mx5qJD8Y21isb1vwIKQWDdIKlgNX1Ue3zQMtTDBgi3S5a6GHGXjgOos0c3A6B9N5OE5TDKSgqm2RvYYgDPuyfPM6VbCYJ58b0WQDoXQ_rI-5UX5Y9rKqu5bU-Bxy7uQ_ufBMiVau4D4UuopLbERgoS2Iaoa8VFtcwBMrL4BeYTaona6f0jg7v4v8kYgLHnETGvyDEDOAOeDYN9vRPM3l5fsncN0bv3gupDllV8gmoT1_j3UvZKIOS0lHISEgjpUmzyuVn2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY7mmRwqGJOxsg7AYTXXQ6WeBxfZklaIFb_JypKQ12Tb4zmv-GERJfGA6kpLRlOxYOLPUq6e7QLyr68KIBu4SORzdZsg4W66RcuRerU0Pp6lJRMTau9AfbwHD7JdM1oMwehjnPA_gPxqNRXJvNsK2buDM__pSkGp_ytfXclLpZkRBNh4Hcm3ZFgILIk99MBxV9RNeidfD8keK-P_cjRBpsZQ5eyKQgvBNbftOx6-iUePiLVzUoXKqy4BeWZ8JHqLNQYMxUL3b4oraXSGgrxGN1TCzjHGuiyDZNUqd--Iea9rhuNf31z8NlP8_b1gHMecfANVhPvAVsyACf1HjULH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=jIZsd1fMHzQVfT29nVhFUgZxPgO5xDqp5OU-mmjSEm7CepD6Wwlq3xC3RpGHwkSydtyeybaF7U8BGQCs9yvPPI-f9q0dzzBTn_Bg-2wwX3m1REpXi-HUBtQhjVEBDHZvl-ZsL_MtVJj1_MyI1eVNpn0UQSuEl8yvJ4-fxivPuionkqr_VRPPTmLQOZ2FB2UzP8imlfRgbTSG8iUVgR5K--K3Tt4y3IS8mWFVBSjYqaDGkn_qoOYn3cOhEHfQ9-xnSvnWVtEyzccTPVA07J4bcXuGord8MnjP_y6DWO2hk2NYXQv4xpStGr9cR8gYPGof9Mqbq87h4IH1FogxhKlFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=jIZsd1fMHzQVfT29nVhFUgZxPgO5xDqp5OU-mmjSEm7CepD6Wwlq3xC3RpGHwkSydtyeybaF7U8BGQCs9yvPPI-f9q0dzzBTn_Bg-2wwX3m1REpXi-HUBtQhjVEBDHZvl-ZsL_MtVJj1_MyI1eVNpn0UQSuEl8yvJ4-fxivPuionkqr_VRPPTmLQOZ2FB2UzP8imlfRgbTSG8iUVgR5K--K3Tt4y3IS8mWFVBSjYqaDGkn_qoOYn3cOhEHfQ9-xnSvnWVtEyzccTPVA07J4bcXuGord8MnjP_y6DWO2hk2NYXQv4xpStGr9cR8gYPGof9Mqbq87h4IH1FogxhKlFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J62YvMFoR3nVytEb4-D9LYLmHMdj_nuozafzIYwlcoilARG1V4Sj4y-cQyfFMpwrvZ5TTR0KAjKSYBpiBpPNZE7f12xxBSuUF003vQs9Bty_Vt3LNEcMZBvQ77JZbWooVRwm3cdVglgY2uvavSzadWx3EXIna0QCq2KZob74St3GBYsyiHRgnp1b2Y-uuaALi8nkMQUFQkbImHlZds-MThxWb-_B2OxZjnAWopEbyabet9TDnUlRuSJI_rOGzued3jvaumX1lBqxsVKFPRyh7bEm3gavOycRhLn3fYx7NvkMLOu_zEwcYpyl9FbYRpQltn15_lGesJasko2oLPD83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYyL1tqsL69VDVdF7oWwX1abrEi8M0fwAxftxroVyBYaCogB528y9rOGSFP4TFao4rJPTtQFkXfesRnJ5RhlAq1r0fBrLh9PMAfKQB8dY1JBXYeQZ1DhyeRr7wwC5KPWgWAL7q3BRyunKnJXm7dAj6qzqtvrfOT5xlCZJs5PBJuI7Z1sjJaIWq0rVab-C7yu_4U2TeOOwxaaUE78_XMVm12LSjoKCzTLpZGwwfQjlnuOvjvwVC6uwcMPd_O7BQtG-MEywdHF9aVdAOP7wG9mAiegaJCkz-8fOKPqHBmGjv_XiuAZ4BTg6P-SDgaAXRUMsKUDfHPxGuok7_LseGp9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=TeS1Up_tlrBnvzFWO0Wf4fPKvx3mnSUFCWch5HHqVTN9ZfZVV7qo6FpjUAEtci1nUtVrFCdMcuFxYig8kn36u2B_kX5k4mynDRrNIyKEg_jdMRocCLGIlPNfhZd6kpaR_25xyEU3VXMDSmxc9Ft5xQ-mmuyuFZ-tqXVhLEwmqxEzgk6BsLNzY_aDq2IScjudZBP_cjegyjkpDwG_uTH2R9DNrv2SOMbxDl5sPrPknbJrGrIB3Fkmd1pM2SIuwcrOQrkL9B0yLTdF3r-KJiC94mzbY2EIkYZ1TYJ9Dwnh_19oZGQSIhVNya2d3Np1wm-x-0kYLY9r-xRAeYnlcjCxLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=TeS1Up_tlrBnvzFWO0Wf4fPKvx3mnSUFCWch5HHqVTN9ZfZVV7qo6FpjUAEtci1nUtVrFCdMcuFxYig8kn36u2B_kX5k4mynDRrNIyKEg_jdMRocCLGIlPNfhZd6kpaR_25xyEU3VXMDSmxc9Ft5xQ-mmuyuFZ-tqXVhLEwmqxEzgk6BsLNzY_aDq2IScjudZBP_cjegyjkpDwG_uTH2R9DNrv2SOMbxDl5sPrPknbJrGrIB3Fkmd1pM2SIuwcrOQrkL9B0yLTdF3r-KJiC94mzbY2EIkYZ1TYJ9Dwnh_19oZGQSIhVNya2d3Np1wm-x-0kYLY9r-xRAeYnlcjCxLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJZmGt2YIayJa0eM7JTCoAG20NpoCnxnoJxSh1UHaLUNvYhwfuBSobWlCUxfmS_t1CDuj989A_SBGuE2nS-YM7EMQUPWYC5EU0wU7wM81O6k7f3u7_QvSu2DLq6wWocdwgy1uGSmb5nqvDnpA7Hhzff5ENEDXX0UjpUQJ78Rzn0QfSQ4d9J14s_rCbqmpoF9DYYIr2BJ1mEG8_NTd0mouQaWnWPW9ePY11m56COcrFn_ps64wvEGFj49cGzc2r0FjWfG_0WQgp3IHzaXFe6mvoweaKU4eo8-cGOleGzpIlcc56mkUJC1xQ6vGtNd1E5Eel0Qj-iZsea4UJ3-d6iGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G50x56JVgxahxWW81dDyWphRnbnku-jpOdXu4zspToXS2NxaUgwitJKluHf_m3582XRELC3G_ZhdZTPm-PztQMSQ4ody_h25uBLcxQCkljC7VrFUKO8g9_d73duThjCNdYWZeEtVDCXyYgfwZlcNYmJOJpyXa22rqgRzXwUblyB9cGRO9RNgqFyJKN5jFHuNS0Ze7ncU8lh1010GrMdW4yBWQNkZWSkDCxlomaGXqz7bEZUlR-fMu26ksHaMk3CXndEgWxefdQOO2Gp5Aucia48S0mQVdMHRVSq46IKGU_VjbAJ8fzwJ0P1CQwyU4Nd56PV50QDC8kt4Spc1cmSApg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMkNZBY68123h1s5d_lxi_of2VhaUSJRR0Z36__Febk24Lq-GYeuIDzQ1-zGqNwlj_uk5x142N5vAFrUj8PBb6Pu-n1eqobllx48wHhjPQH6GgZbZlh33qqzIBXdUL0RJIC4_VXlo19GZSJcWJiyVsznpuENw0E3Ut9i9GIGGrwfc3LgXNj_W8l32pBIuZQClc1yGwn479QG9_EJGMB46rOCStiylagSg-G4ojpvUwf9YR4LxcuThVqIdZwc2x9vEQJt6wArOVx3c6rnVPVKsSvcnm4oBPKT7OUgZoA0Adzi3_mwJ_XsbesbkeOMTZh602kOByyC7YMooeNWALnGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=KB7ADYZZgNeenCn9-aV0ItWECbbKcdh3bv6AgdsXOem5_GtNUrOy2SAmW9Hx1ZfOxVgCSZg8SfiQJiAhohlUe4mhQQ6Pa4s2MIP1Z9DsSWZRQ_h_dNDCi56tOUqgp8Jb6RAkRbRblRYyL-qOD3vtCZGmOpbtx1Tuuep4qLFq8goL7kZKm9SSRu0JLsdWek2c6Ao6KkMPLxGefWpKu-N1ZHTWQPKqXC5zpWu028UGbYwqoGLEG6obysF62wSeqDPZIpwzCx2XOluBC_BeSgctUuUL18Q8rYPLMaqzrZkQM-zGbNNaHrLZmYXAlKNZsGUXfTI_3w1QS63hEIDAQ5isTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=KB7ADYZZgNeenCn9-aV0ItWECbbKcdh3bv6AgdsXOem5_GtNUrOy2SAmW9Hx1ZfOxVgCSZg8SfiQJiAhohlUe4mhQQ6Pa4s2MIP1Z9DsSWZRQ_h_dNDCi56tOUqgp8Jb6RAkRbRblRYyL-qOD3vtCZGmOpbtx1Tuuep4qLFq8goL7kZKm9SSRu0JLsdWek2c6Ao6KkMPLxGefWpKu-N1ZHTWQPKqXC5zpWu028UGbYwqoGLEG6obysF62wSeqDPZIpwzCx2XOluBC_BeSgctUuUL18Q8rYPLMaqzrZkQM-zGbNNaHrLZmYXAlKNZsGUXfTI_3w1QS63hEIDAQ5isTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lX-8werYKb0HfHnGXhfiHbWS6fO-6f-wmX2VxieIZ9hg_ogMbirFMkAQm6H2jkj4djyDt99sMeYIkHwNKt6RaRYbdAsET4RTNyoGa5ll8L-3xPtUnUXl3o_or2MBax36c9PMWonh3rnHX3-4E_yQUSifNGhpNpPNetIv9RMheFOqeM5RuF_fil94pzuS2-RBylyieVMO2lklg7Jle0algCCXqQ4JFV57cZ5DTgd2ehg1jWA9AMCIE6oV3t1fwzywaVIYxHODeWiYeZhWLYFKNAiC6zZIe9XYRSykNF6V0GzM5GwVhAcyNGdD5kSHqxUrev2f8_rkLjF2BpxofmWIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lX-8werYKb0HfHnGXhfiHbWS6fO-6f-wmX2VxieIZ9hg_ogMbirFMkAQm6H2jkj4djyDt99sMeYIkHwNKt6RaRYbdAsET4RTNyoGa5ll8L-3xPtUnUXl3o_or2MBax36c9PMWonh3rnHX3-4E_yQUSifNGhpNpPNetIv9RMheFOqeM5RuF_fil94pzuS2-RBylyieVMO2lklg7Jle0algCCXqQ4JFV57cZ5DTgd2ehg1jWA9AMCIE6oV3t1fwzywaVIYxHODeWiYeZhWLYFKNAiC6zZIe9XYRSykNF6V0GzM5GwVhAcyNGdD5kSHqxUrev2f8_rkLjF2BpxofmWIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d95g8RVlqB4uW7yuUnZbKHsQueLbfQUNU2AK6q8SKc7P6bWfe09Sl-3n_oHJ_4ECZk2jmmCa4-rCASSzDFyJNoNansDz_h460LE5IJ-K2wyzzgX0lDPPXcTegB9fsuRVq2DD8VlSEbwJpT9pXWUf6wgV2MeP9CsvyF0aC8Pyb5RWgbuVIUdMlJsDxgADqpT3EvkcO9Qcy1Cw-ceg3KB6XiILtCQSVV5-y6_mkdCd47e3TAPkG_JpV4qjB8Zz_nxey_OqxRk4MGLLbChcpOPviXwt8AE24AujRDWsN3b9rXBhzIBvrebSYzpPz7NRhiQVHgBYhIavaYMBTa_RNIEOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_o3IB0FPykzNTJIMChhr57gmCtSYD0ZUuCXLeGu2S3DC3u9J9O_99w9xMe4xK7BP7J4R1wcx_cta_zVXP3cSPLYDd5bCWSJhmaq_KLT1CnONM2L8uudpGBIfPRJDTfw2EoiH_Oo2eb77OUXh7Ly2X1thXs0_wnl0sR7WrrErFMCM19OA2Ki2mmZDvysNAh3QmfaSjMqW_DADObaOrmx7GyB3Ui1qD1QVwuOxVU3cKJThmP9D7_cfosNHZmWVsLuNMNH7ImEojrZN_FqlI1FkyRwzmMTP_bFQVunzpqKChJhoLx29j11fgR7OLTD6RS0ZZUEP-zntdFg-ME7S5ae0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE81ue8EnPuS8qtg_ohVVhIb4OAqs-DduIunhgPgCBaAPXU_nFlESfRMwy3CNR-oAirUt4H-nvCGO5jtMIxcs_AxgZY9O4m2ZwU-NHhRDzq5Wvun5_J9RN3FdsmIj7vi-5qIFvcONydnFJ98s5Wx7h0ZrOEYseVwrXLHJsI0dJHbiD6ect12Jppw0Vx1afrG8HC7YurpzzB4mS4Hrpda43pbiFq1Jf17esAAks0bXVom2UdC7I43LSsqiDkW_YDKUVAD7Irwln2jhzGc4pBbtfE6Y6nH02v9z8eULCLXb37pOPxdrDzInmurqngW1-nIt1BIM6KUkDTLIqGdpiZ2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbUxNzGq0XmyFBeCkrxv2sZPuPEmvb7nrPSE8VSIAFSnQefFAYkllnYfNnsJNKA5hEzdsA0NUD_NrnjXmK5Rj4pzal5v6nzmykK-BdV80dsqMae-x5cX0p9KQ5_rrVdXfuScKJ5BmTQdc0RiWuI3K6PClpukwDhCyMqMBH9A5jfBZpN3qRz7toQUZy574PduThDmG5u0xLsyWN-IMWwIPequEmmXamaamyKfiLLa6GDPOXNjX__2mRvT5Md9JsMOdKHjT8DLJ1CW9z0YUuukMe-QOuIN-cSKBFEgXqY-gBMjgidyRG8lc9m8zDOLMWvPuuFvx5qSdOsYJi_JSfTZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw-V7_t2L9HaSyCP8vP8yODQONTOlGZC2PMeXzluIc02PbYW_yK0b_3A6hsht6ORmJf7fhoaNXM2CUjrEo7bHh0Ql5NO7LepU2uVm86CSW12WI1XeeV1haCzgbf6CTPMzUnYEoUQgVI8WMw_zriUDhiqiuKUx49HJKnUuWYgpKWM14SLJN4jSRfy-ie1QfYhmNUF25zy8o_OxfwA9O4yTk6f7i8aAE8kjTcThRKLI3_dQBN0iRslQUoFtQ5xc3zYq369tAEOT9YTYCUexqq9nLK8ErFngipKjIf_kysfuG94sK9z1w7BbE5dAmI0ajKt7i085nCx24lyds3tFyHfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKUc-XoZY-XTP3itw4inhUWHsti0-nbPiOHqDs7bzhC5uzq90Vsh3QlGlefZdZWEJk1Tj3q_nRl8ls3pAOWbSZ9buf88h-ZG8q8QaqrKOOsbfzE7vljSLxo0EUt7uQx8t9-1CWizR6clCmPratRay2aFsoWKfsCEz4v83UT3mIc8JrZcyATgVpabihxhHGudGvsp-P3CCsoiDHRlj2xYP5Pa79mtmSle1WfDsI1BvdEV0dBX5ZWYFaOVLjE4r-P_g_8v7yWbpUPNYHiUJeovpqCTFt88QI47YOPRT8sejkySDK2U2KktZh462Qte-KSoPejuKwD8XiLh8N_4Iyk_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=QFeOlEsSzW2bio221vbQxzExtnVm5DlC32eN-sJanV5B1mdDarUAunHbP_DO5vkI1y78MXG5cs_lww_rIIVr2gHWoEFiILAU2PiegiRR3Dsikb0sE2DQLtHRZXpRZuqjrw-INXrW-W49kWwE9tgLy593vyeCiYO21VyzWGniYJWk7uXtrqEMxdVLTmV0qpJliUoWT5Z31YQMk7g-I_0a3I3azZIy2Oing27ac1aKhUuLGptjgZX_YOYmaqNaqtVwT_AXc-TJQeV_cBh-5A4l1DaXET26n6IpDXV_32aFAbHFx8xQclRTdu_gFx4GL5Rbkb_zcJ_Wzn5YDcBaTGzaFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=QFeOlEsSzW2bio221vbQxzExtnVm5DlC32eN-sJanV5B1mdDarUAunHbP_DO5vkI1y78MXG5cs_lww_rIIVr2gHWoEFiILAU2PiegiRR3Dsikb0sE2DQLtHRZXpRZuqjrw-INXrW-W49kWwE9tgLy593vyeCiYO21VyzWGniYJWk7uXtrqEMxdVLTmV0qpJliUoWT5Z31YQMk7g-I_0a3I3azZIy2Oing27ac1aKhUuLGptjgZX_YOYmaqNaqtVwT_AXc-TJQeV_cBh-5A4l1DaXET26n6IpDXV_32aFAbHFx8xQclRTdu_gFx4GL5Rbkb_zcJ_Wzn5YDcBaTGzaFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Q219qKw6jLXx4UoQedjp8-gRAgWYn_G2ez6vhTj4cVvQN7MdU6nG65NS3iP4dy8FQIOSCkdSWhBU3JdBCe_t8dfy69DoLa8eOwdBLWOXCq4T2F3-tL30GAFocKX99m20DaTitw2OJcYKODClFg0_A_eGOLPYNWx9oaYDfkBsQFLnfT2UEWVFZOR7B0EfJztyB7jBZfDfpdyEWeoIPe1e5yR3USrTigN-Y9FokMIPozQetfga3IogJ6q66voXs9mmIbSZNS9PEFhZZB2GboLaFBWBSsdE8wrMaH9CosvePxlArO1SYi0hZQhGdrPjF_H1Ys3ANOmVIECPjQTnujLw-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=Q219qKw6jLXx4UoQedjp8-gRAgWYn_G2ez6vhTj4cVvQN7MdU6nG65NS3iP4dy8FQIOSCkdSWhBU3JdBCe_t8dfy69DoLa8eOwdBLWOXCq4T2F3-tL30GAFocKX99m20DaTitw2OJcYKODClFg0_A_eGOLPYNWx9oaYDfkBsQFLnfT2UEWVFZOR7B0EfJztyB7jBZfDfpdyEWeoIPe1e5yR3USrTigN-Y9FokMIPozQetfga3IogJ6q66voXs9mmIbSZNS9PEFhZZB2GboLaFBWBSsdE8wrMaH9CosvePxlArO1SYi0hZQhGdrPjF_H1Ys3ANOmVIECPjQTnujLw-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTvbKreX0vLqZvWQseCqx5Q7laNXoA6dkKFzKsYLVw8OTaObWFLcHLixfqmHf9czfTqt9VZmkMVZzLWAJiLFT8-Y8UJiNn17sKC7V4vZosk1Guxu4w_VhMRokz-qwlR_tkyr73VlX6xPTZULMEdR1zaSiqlTQKnw94XyhKVWoLyvD5Sbxfr_R8ASCViWMYN7rweRcGTiXUxfmpisQ9-pnYcqCKM2jvgKmr0v7YAwonKnwupaRqWpWF2wg7phn_k7xXsAWBywXkxT2z6ymKxuY3K3IWcUWEwykeR0pgtVKBaciQiPHytxUl-75R9Hv9TVVWdnowTLRQkVs_lefA3fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=ujGSCUvdf8_Sva2n7VzylLU6siaiOlDIZDQvCw40-s_Pvl6EFxrmgElDO-3nOKau4EPl7b-aZ80G1oiJfFG0BzSzQ52WjOBVth8LkX1JEkIx-bioiYh9Njiw0rUFM5WeZV3tsW893uxKsUrYQPrRjo7W4UmtEj3DzmOrLgAEV6mOedj_tnCI2ff6jWCo0h2Jzypopf2SBgSa2RFIJLlsrJiUp1bgvUXY0lARL5WVd-xZHeo3Ek3XjZynINIFJEbRueR4UEHavlmRfxts2FCLLiZXBbSR5w34BzfjL7BytRvmOD5H3gcie9QbWmio4DA4kDMP38sH2QVSQfh9BGukNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=ujGSCUvdf8_Sva2n7VzylLU6siaiOlDIZDQvCw40-s_Pvl6EFxrmgElDO-3nOKau4EPl7b-aZ80G1oiJfFG0BzSzQ52WjOBVth8LkX1JEkIx-bioiYh9Njiw0rUFM5WeZV3tsW893uxKsUrYQPrRjo7W4UmtEj3DzmOrLgAEV6mOedj_tnCI2ff6jWCo0h2Jzypopf2SBgSa2RFIJLlsrJiUp1bgvUXY0lARL5WVd-xZHeo3Ek3XjZynINIFJEbRueR4UEHavlmRfxts2FCLLiZXBbSR5w34BzfjL7BytRvmOD5H3gcie9QbWmio4DA4kDMP38sH2QVSQfh9BGukNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=UobQOPYruCcKMFnlwFshGrQhnZTdEvnTHPO3tOpo4_9f5Q7KrCxgt0d4JUo0OmrwFoKgo3skLii-76htYZPeOkZioHq127fDQeMfoy7ISYx07ERdQDvFylZhrNlXMhZK1PfdIC3LIIgl-38f9T3FDNwH2K92YDzYPTr1jel5FqQBBpUCYcrO7olrw_cy_WYD02fRdua0e7B1mPGKZOfVqDECNwYNTJoWHLPkYIedYt2mEjIbvvyEFxUI_pCzvVgdif8F2lGT6J8Lw1cH2bNtjAy9l_PSRqjAByej8AQaa4Sb3m5u07f7WcgrdnVMaM2XxuWfa3wsVUvaIMt3ibpW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=UobQOPYruCcKMFnlwFshGrQhnZTdEvnTHPO3tOpo4_9f5Q7KrCxgt0d4JUo0OmrwFoKgo3skLii-76htYZPeOkZioHq127fDQeMfoy7ISYx07ERdQDvFylZhrNlXMhZK1PfdIC3LIIgl-38f9T3FDNwH2K92YDzYPTr1jel5FqQBBpUCYcrO7olrw_cy_WYD02fRdua0e7B1mPGKZOfVqDECNwYNTJoWHLPkYIedYt2mEjIbvvyEFxUI_pCzvVgdif8F2lGT6J8Lw1cH2bNtjAy9l_PSRqjAByej8AQaa4Sb3m5u07f7WcgrdnVMaM2XxuWfa3wsVUvaIMt3ibpW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7vA0dl1Ouj-Vu3KeIQ7yiM8HpiltV9AhPF0wqLZ1120_EeaByw4XbUQ8LYnIleLC2HlR-ZsfN0T8kOqK9_SKpMiSwiVQ50jit0DjZDPcnLLLXgTEIEwiWoWfb07R5ZBUrw0SAvmaU155ZsUE5Qq9oKXJalg_GUznQhcjBrBayE40qNyRlRZDVUNxld3TH0AGzjYBO2rHc4L6H16F2f1ekFkBjwlc-hFHX3xBKIqn1mAoc8XQVz39j2cygp6g8CvVwL1EFc1DUbJ8NM6c7A3l7rDvitx--VF0nFYv2aI0nwSNDGFS5OqkKLQoP4T7VN9FzP4SZ7y8e-knM28SI778A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3KzRnxW-WnMYgsa_XGkA-OK0FruCzT8fOS9-0fZt_x-3odC4mbdVi5HqbhfBEO2kvDpA8XT2m3tfLnifbMd6UgGYDhWjLcdI4dhNuOuxAAv-FSi5autxSHOmg78P6xeFdY3TA9qNl4T70KbjB-wLpPyYohp7-nIiU0SHoULIGqA5jH5ZXoPw7umosB5KvrFrpd-Yx-jUyq6t7xzgFR69S17_eSIojFiL7SSx9DmgAPmu1dv7uzoRT-6u7BkcEdt4k1w9a37Ege3tz3lGgldBZtBbtAMxCNS9H3qbeTv8kGb2TeKadcE6BMV1elmmPWW6Q9lgR7lM1-TEMfO5_3Hsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRBbNBUAQltJi4lpX6YCL4fSz5F66bcR7Qfu0zK34FO-wI40QbNSYRtBo0YVGAngHlHdzU37aATu0drGGFmT5uSuEmJbr7tHJH6vdk9CDZtgUcgllX3553AdUzXzLGwzZajdOG0__H5gnut6j1K49pfVTHEvCdeSqYHLLAzzZexrex3RL5_XyvjsaR7iZM5mLu3JewDI8cX8p3NIjBdyV3KrN7y5mqvX7gEDg1dSRGfKyXR7SBtX1YfBQflcNnnHvExdJ0cRLaNWefTXiNZG8gt_x42B_LTrfFw7dpcnPuezHkpgBcLgIKveA62j_Vh3lJO49eDQcsp-7Q_vZ_WHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6a4wejEGVETdrhEFWNSWG-4WN0SoO7vrIC0HUggMa9TJOi6Jo3UJnNEzC42E1DqU0lt3_DM1gjAIViqnvBo81Y4AfugvT4g7jhQUC_yojmtCo_3OxjvPZAqFTKYJIfscIULELaHfu1R3zHEASvXeDbU3STHbmpzQ7Z7f1Z-q9yxO4YPcU_ihUeNmKC1bCLvjY9vksQ3mJSiQAWsz5ZT-oet02FMd_TopBH3WaK7Vp88J96csLOx68TNedmyorm5SSFyANmcsMZiir_KxG3N0Pvb1ueGGgNtqlun5O6VJxn7-Grvs9FwMvShansDk-7STk8LPTlqqoQ61dtr5xPK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCuq9UUnosiBx6DFln16mS94vAQi0uCXp10SRQExCcokMl9yAC_n4st5U9cXm9PzlEk78Vmy0qKLeyRKBSH-_5kNatFK21NEvVmnQJahv-rAgQ5mpEo2vPYt9oGTAsbehKW6uhJR4sOgaEcLPRWcLHosN7V3fwnAXLCbRp4LmJBcrobvdrJUmTHVGSi4AA6CaiI8djh2XMkYS-2cVFG_y6cB2oLY-7091uO9LdWTxqUr8Eokb2B1ielEj9uZBz_mOil7cKy1RIGmgrPDhronU1dgnDBXkgNeHfCATVDNFkpFdV3hfrpG13ctcJb3gDn0nNbZCCWtqNYbQzdB_5QHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKUt6CSPFqPHTyW_qNW4qt1HA0TnUkF_zSnmYY2dof6Lw5vAlc8D756uHjRmvyfjoJ2yf11Cn9HuzwUw7kEs0GK65gwDAeOIcoEnrnX-32d8leNUXQWjPYXgHScWGVlOUWSOGDFj_-7G2iDH9pSLlc2RlmYEffsPaT_DJAcqbDbzINlSyFgo043yhv09B4cWohwOqwjTCFazs8HjAmsv6ZKpS4PLfmOmsVExbmhShd4E2VLxJ-7itPLti59XXrsgRCOUaxJHISrxV6U8k7UNxhJ6TXqKQPOQ4h_9CUCTJkraz_om7wO3X5rNR7t_gRJlDIGst2a0IL4L542JXNXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er_bWXwFsI93HmUmG4FWMOOFnX2TjN5Scocz71qE58cjIH8KQVUur553y8ZSgPdrr7JI8dVIQrKNt2-k1GiPU4ITCVe9864p9uzAF7QiqELKWKFVzOyBtxHVbk56ynpftwN4aLrH-fsDG4mSGK0-PUt5C3oc6SMagI7Qswgi1xKQa09CJH077-b5Kd3e6ZeeSgpmpNJ_bod6RtTrAp_CtulsgPyIpAm8OlXiHL5fISeHdvVtkno2epMOMzBLfvnMLVe40OsYC9a8sCxXyDX3eUfrIaMcfJQlCvJKAFrLUFuNLjJ1IsYU3u2mAGZsaGD0LOQejc87GPJbjiJbSKhC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGAPLERSqlbfWXECqjnGS8vXNr5BOmcDebFpgScvtRE5-WLXRmWKdFUpH5sSk45EswEn1393Fs52brdzEhEwVBoV2YhU-jSZMWNQaSfKB9cthMeQg3hBxy5IFyw-f61woyfySe7rts6vIXpmAgfKDgpwDwPEgkfoE-Jk5JsiFJZpy9Zrs9lE70SjvJbd2D0OysE090pc6wLNvPY7KAo5ESgURTEZt0ZYkBZ0XCiLHD7P8nMlsttuLVhwIpHOE6LjuaToU3qB6bSXkkQnSf5adjynRGswcZqbI-T3iie9TBJMhp3AUz47otEWhZ9Cac0elo308a0b_b2AZcSx5YGlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=DkJwC4DLZiz1-lr3brCfvy25OzQS_exgX9Wnuax7qP-DkycgUrQTxToJxw8pwVT_VsYEx2Da8bHXm3m1KnLTG8dq90E7lbiF5bBWVlCM1D8spYGEBbH6oxc3kIryIFIS496bDdzyxaDWJACOf_XsOvz3picQeken8rRt9C8TtUSk7YmmD8fXC3JZwxTwklhmyldHgFa4-NbVTNhdirZ1L64yWN4i9-6y7xZ6p4ij-HNfB5MSGAP5skuAttdmzZmbpBbaKFcQSsXvUhciAPMyA8_6AnQXDbd5ASGNAl_6wAs7uapcGfK3I0uXDjdAZ19nQFrPYh2fuOlgT40UNF0U4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=DkJwC4DLZiz1-lr3brCfvy25OzQS_exgX9Wnuax7qP-DkycgUrQTxToJxw8pwVT_VsYEx2Da8bHXm3m1KnLTG8dq90E7lbiF5bBWVlCM1D8spYGEBbH6oxc3kIryIFIS496bDdzyxaDWJACOf_XsOvz3picQeken8rRt9C8TtUSk7YmmD8fXC3JZwxTwklhmyldHgFa4-NbVTNhdirZ1L64yWN4i9-6y7xZ6p4ij-HNfB5MSGAP5skuAttdmzZmbpBbaKFcQSsXvUhciAPMyA8_6AnQXDbd5ASGNAl_6wAs7uapcGfK3I0uXDjdAZ19nQFrPYh2fuOlgT40UNF0U4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjRFSPT5tnOueafA6Hr7wjS3cgA6TyW7ZA9ZKCydiOE12-IPuUrmRQIjkhrwdIvz8Y9Y3Drp8Uxx5-psUfC3DYC1rWh1mvwEJDFC-BTpRRu-LF1-pondl-u1uRBskk_PCjt3qz2FpsW6tXjBPRoG4PvicWda04znZi1clxDMf7oNzp2N5N1JR_xA7iRWdCtt7CYHRfwLdJWs5vqxBMpEjMRV4V2dC4-TQjZImJs4X2Nb4HY9eu6HtAwWlp4k4OckAV9guGNwObi0B9RhMM0NlvpPtECsL8TedQtXx_JGJe7bcOgAB1x4LT4Ax7vL7apkDqY3553Z7mjSPImvydT1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJvgMWFPGvaNG1EZy5qxgN2r2ol3OiCUUKA0Luo9BNrJXtyEBTPYakkVBlvbqfaFFQ1k1O5lPhfAhtcYKjtUmOsFyD-yV8I6s9cuNoEHH279BgHBp3vXwKDRK8wZa0irJUcARTeNK4RKwgoovniulPp5iiJSk6amUOQo0DrqX0pr8GYd86nOenCugFMcKrz4CAOO__p6aEBEmezhU850jhUziO5nnwE8FfiboExbcPDZ4z1ZOn88Q5ghd6h92oat8y732RIbqHVQZP4_IL5MSo2LjZ6tWFID22GMwFIu974W25el8_y51Hf-qwlCnQZMQ7f-tSslD63-Bj4mzOJGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDpU_WhM404q3IqzkkWYyRRxff-UOX3Xz7n8ZXsJd1kF8XULpN4eQkVVhLF8t1jb7gdrb4nY4TDZQvwSph1Ktg84bocg9I2P3sSTfmW9U2hfcsn3930g69h89xXlIVLvi-m0NRtGx5YY9-B4yOMCvEhc2a4XE_8qRQoKyHFe0SY2ZM1CIyJHd90_WnlIUU1QKzWg1z4RWuhos7zRiY7EBbN6u9nRGzhKVO2qgbo523Xxg2dgLvCww0CvmyEVGOXSIvbNHHJTBlcYrbfmWAKSskdVW-tDVNpsctBP6AQVG-ZDg_ipcM_01uMuy-OkmUJiaMEk7YPQmklro0Rvtlnmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=VbOIcKPZg4P_IphqfnBY1qAi4-CM9Mw_EDj4sTRwObleuGPPzkY25GbQE-8KXAHlsUMC_5FF9xLQZjLC1m3idSW6IE7srMxX_TnFhOVeud1uDkIhZO1U_zZi30IEPVmMpmqI85mokYhj1G6WRZJxLhhbe6q_g0fx3ivNLi9UZQ8clKaJxN75gjUo8QcQgyq8m0AB0qCFMH8GD-QHesOyaFo_nSSL9oRVutssXle_Oz4_sWw8BBK309am-jf_7AfwOxSfv1XK88G_t86Up-uCLzG08vBZVi9erlB78s0lGbG_aEsUl2OVcPTj4Gy8H9cVUDs6WAboKuYUtsrn9oc-fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=VbOIcKPZg4P_IphqfnBY1qAi4-CM9Mw_EDj4sTRwObleuGPPzkY25GbQE-8KXAHlsUMC_5FF9xLQZjLC1m3idSW6IE7srMxX_TnFhOVeud1uDkIhZO1U_zZi30IEPVmMpmqI85mokYhj1G6WRZJxLhhbe6q_g0fx3ivNLi9UZQ8clKaJxN75gjUo8QcQgyq8m0AB0qCFMH8GD-QHesOyaFo_nSSL9oRVutssXle_Oz4_sWw8BBK309am-jf_7AfwOxSfv1XK88G_t86Up-uCLzG08vBZVi9erlB78s0lGbG_aEsUl2OVcPTj4Gy8H9cVUDs6WAboKuYUtsrn9oc-fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdL9lg2n7hit37g2HvFCm7fMZ2sXgrby5ttKF4yL28n08ehHnoscM9a3M3nq6XX-tIDemU1Pyokw-l_UQ-JavdoFR-qVPoz9AdEh6juoI7lWJ1_ac6bihHPGnNOQVWXeGWxJm0kwjjuLczOqg6i03RAGVggavXn6JkKfPjCez8_9KKcqlxJ5K9A563Xyd8VHyXgxXIkYqOEMOLm8udIwjiMtLUzDkmwARM1pYiNMg2Qzwu8T2stwlHU3PFYo2qVaIVypCpl0nN11Vyvfx4tc4zPShnOqOZ4e5nkQkWe34BO0M9uGAcgxNOP8mjXUYEWWFB_RKkfGKwJlCIHvHTwkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlzwCAdpnEPO8T0B9UZak_CoCyJysz9sCFefIBPdjIxhf7LM_gkPdW6cltl3APIXx0LZTsDX7E3GUp7I3TuKkcWe6NVN--mDtD_wsXLIuf6aqusiLd-1siYfWTyWLqb5sTUrqkwPOQ_rQvwdgbh7ClEB-9RG89a2EXaJhWweNaDx-p_Bxmv2w29MmH9OElPmbkBKwFpOP1g2YPj1mT6dubciPqi8GFbNCu4lAhufxfiyP_W-llIBqx0muWaFaqLv1FfDWedtn_BMNnjmtPsbQPQywQqLFaq1V80S3uwZqlXZTFo4cC34gqOi_fwdiWhMrmBG-LBBivIQrOVL_1kI8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkngiAMirPCBoVTC1a7-WJkSJ_1nDFgNjrxAgvZXMY4eaPl9ELrmWLgVUqMhwXmN4rMvjTskcUk5TY9Y1TOGWwtJRZgy8Amq8KL3I4ZFPxPUmUymoaWUcLbkwbdnt6TZVL5KNkOrBE7DewPIy8I4PvBWnNvPYpuXgab39uL-90TfnF2R9de4yILD8oVsrpAQkJJmOlpg3ojwc55A4BuygJijBESiDR5G1hVkKUe6YySsTk0AWFFoFC53jw8yy5SjcV79awyyU5xHZPuGqrUSYOfpda9rk8ds6avLy0_xSg30GOjUAJ2MRv3Zzg0Z1zY5sCdt-tpyBzYIZ2FCw9S-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3MugfeHwxXEp73DPyg_KS_lXyhxBNFZMI_Hrb8_8032lVNSFI2Yt_Izdj8ppsScGsTciku0pNAbtt07sDDFu7k42eN-xzV8ySlPHLavzxacI7tKhmpi9-pS9yDiiEPWe3vCUsUB6KIqQiPtRUQTSJP1Q_HIUdjBPLozk3rY5ZVFLqobP5hfwixG5DljU8X33I2_Tp-phSVwzxFtR8t4MqDTodSZcQWgdjN-Y3ANy39GODshhFmQtWL0Ge6YMtvm4L1EX9IGmdklVya1-nT3Wr1v8HlvRUMMooh3wCDxIlLuqRU2bykkoogtZvGyBeZXMvfXp2a1aUDZzPyvNMCMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcyHt2aDmv4xNyfnn16jVJvYJvIVs2aj2B4Z_S257KOADZlVRg3daCuYkLc17gJ1Q0YZTa5glKAX4696IURxPvKgfzl-zsOoGz68gAl-81fnhZAdNfyCZQrCrAAdOZmHg4MczHQ7AzLCfmPv5-VTs4iJuKehZsR7dHaowLYZHWZgbqTrKAQsVhw5wXkqCfS-hx4iL-DebScXFfIIwMwnJve7fzMQvHj7somONiJnWEl9-HEkQHyehwfHV8Zb-hMrDqbkTCjKVCHm_J-_DK9L__JXuM_I0rxD3TC3VWNqNf1zNMO3oHlegq_jxaako-HaGohDfYXGTElEhIbivEFTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=mk80Kvt7dSTCBkPgwNjWcfb4f_kNsGoc_h_PtkDIp8NbLUbHMt7tqJQVQw5zVRqIdTPDhs1KulVlZ1HdgQesy4CKX_eV02kKn4RTdYZs_MrmvhTVjXdDX4V6Ux1ux-6Vl_BmZZTIQbO7MfAUQXOjD-rZXkzKqVoAb1cVQJMlfmj3IjeAmUvjRhZ3yTuXSVjIAiWWyVtfVmAcD2LNfQD4XM8J6xB5gBFoDF4B-iCI1ZWSNov9I4MCnR19PkaLjIG_doGcRLW3PUKVF3DRU7L4g1Ht1EMQl__IOhCb8-BiYq-5lJtt1NoCVyTOjO72psyL585AqB5VTyQQ8YmIRzU3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=mk80Kvt7dSTCBkPgwNjWcfb4f_kNsGoc_h_PtkDIp8NbLUbHMt7tqJQVQw5zVRqIdTPDhs1KulVlZ1HdgQesy4CKX_eV02kKn4RTdYZs_MrmvhTVjXdDX4V6Ux1ux-6Vl_BmZZTIQbO7MfAUQXOjD-rZXkzKqVoAb1cVQJMlfmj3IjeAmUvjRhZ3yTuXSVjIAiWWyVtfVmAcD2LNfQD4XM8J6xB5gBFoDF4B-iCI1ZWSNov9I4MCnR19PkaLjIG_doGcRLW3PUKVF3DRU7L4g1Ht1EMQl__IOhCb8-BiYq-5lJtt1NoCVyTOjO72psyL585AqB5VTyQQ8YmIRzU3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=O3YLB5-y0z9CxiKP8EQhmbDBVqHvmV1KLsTUanH7wvxO1ZDOB3SB9uT5N0GU-TNLHQcRwaDebxJz7F6PhhpaEJ0R3z_4_71_e0fnajtSqLtojPN1mfdQnlj03pem2E4tUjQjIIiDqgjHp4ZmONLAMaDeNhm8CY6-LS8vqrCtS602ezFFxtwCEX_k-j2R6neSyCAclLc_v543n4NrTR8ZhW1u2sRTxZoHCEyNS7JpySvgAMeyUVOad41PqRJ-p_0k53FRXE2UNrMZMeGblu36gt1D8ulS6LcJL26-DXPvOc60WFx-fPAHUCwR1hY1Ym8nyewJO2-GSV6Q4UsQRFAeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=O3YLB5-y0z9CxiKP8EQhmbDBVqHvmV1KLsTUanH7wvxO1ZDOB3SB9uT5N0GU-TNLHQcRwaDebxJz7F6PhhpaEJ0R3z_4_71_e0fnajtSqLtojPN1mfdQnlj03pem2E4tUjQjIIiDqgjHp4ZmONLAMaDeNhm8CY6-LS8vqrCtS602ezFFxtwCEX_k-j2R6neSyCAclLc_v543n4NrTR8ZhW1u2sRTxZoHCEyNS7JpySvgAMeyUVOad41PqRJ-p_0k53FRXE2UNrMZMeGblu36gt1D8ulS6LcJL26-DXPvOc60WFx-fPAHUCwR1hY1Ym8nyewJO2-GSV6Q4UsQRFAeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL2vd3OfdWlyg5u5Aoah--UfY2ornKKaNoRHivyhLK5hpGTHzTK2RUnAMr9nd5TWuhoDZBkqeSbwYBZ74Vv4FWtx4E3lh5n5bOMuSLzStyV1njDLAbmRV4PUZ2pzvlySjA0baQMx78x4PMp-gIqUgclaDQ4NOmTbUvbM5G5_9lA4_vJIUuUNYsoD0QKeWp1wCG1azdQCSXpqrEO9FPnQz0Mxdf5GzYSyeZG-wYbREwGovYtBuRjQkAnvBHP_8iXY9KUDuVEeKnRrIrGSPTlnImX2scmLFNtOkGDrcxBstbiSKffO5Ko_YsThOUemFWwbaKtRu7g0MMveoAE3rEKVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_8KYdtOjzIq2kKMRizoehBG0I29EwSplf1v8StWe-iBVwcg4K5QfWdvs2o0N_mOoXe5YWBQOtS2BNLY1Tda-VMElOlS5C0zZL7_U2pse2G6N4Cah4udtv_L8LXuz-oVE4IHwVTMSLNecWH8gZfFNSqQVZez7Uwu3ePkVsuD8N8IykXrNGA56uxjfkn_x9IfHfRZqxAIVTBdWvK1FQvo_WpIZIXMoaqT0K-Qcv6Ytlx9doDMQB5heb0zJkAk1VeKzovcvxOh97Z2nr7GPt8JjzBYfBPToNhfjwhOptGxCI1jUjN_xaOknw7yzm2Sw8ghyjKhg8yCHR5Er6Tu0fsGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb36oSXR-i_JQNtzN7YNOK2lgL_77E2RuTBRpGW7ng1cVOXSoLW5XlWq-Xb77zrdaMyu4BoeLbbJFh_FcWLU0TCzMCkgWGYlrCtFGIkuB379CC34wPnchlDiO0PswfYCTg8NnVoGEWIrplRmySijSMVXJBxr9sMVg_-fBdoqQNydg7dT29lxCwy60wjsyQsnIDra3o7k0jTHco-icmT5k--iIYY32vE4sJxRq52O92ce4AZvWq3xtg7HvyL965zCNWQWumki4jrdaWkyBekirIB85jU7-gkEgE87geoEDvNGLBp5c2dtYB_VAXBXKepQ2qMTjknVO9ZfhJIx-DWwGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzyY6kFcsEJwWQDp7PaIPPFtPpsRmK38hAQH-2LC8cGlWmyX5OvwrNr1YdzTP18k5oO-4J0KFFwIZOvrVJ1RAdOEKxwjcQ1sYt1d9ZyeGjXsBC23HO8_uuH_3R5vIc98vz-Pb6Vx-pjYRRe6n1ZEBQkjqMZAQROf0_hmQkzXd7_3A9mUg6PKNpa_nH_sjhB0Xb9kd5bEzRFsHcKNkJlLMvOeOQOYWeWnWNFI_PhdNBuR8dPv08fYP4KjOHP4QleBXm2SLPfC2rQ-HYftgh1aHv2KQhbhgS0PD7OjwkiVU9uUDDY21kZ_wrinJVQGUJk0D8eYY5eiK3y9uoYx8hmDug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR6jTNZOtGI5V5sYT98tOCrc0WNh7KgGUlqOOzPN8kMd7UhLsHD_RIrN2GkigZciPTvT_8cJv-wtovE5O7Rzsomzpxb1K-czl5WmesfOiLiI3oxmRzp_xJsbqqJB9KqqQVmRYrV2AjDqoyBh3d7O53tTE-tewTrem_IW-NG-rP3H75sImehmTmBTYk-tJT5xw2AXzxgr4Y6XOiAvc8Gd5hQYeAnZa6ybLtDO_jK7inOltlT2pEOqoE6OW-Z2yOn-yuOPqMhNWPvAtYVdYTmpP3ciwU15OuxenpJCmUner8JkSdjCO_6s0WyFbI8F5WRdLN9hJ6UHedfkgptUSnB-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVO87sj4s9uHcKUVpeqdvS9UMYiTpvQhMi5lLtPzr61nSIRo7SizFR4Zzjw-fVDSNJPF32YlBHt63qwCR2R1fqRhmb6yI9AXi85s9Ls_TrTL7DJZ1FHQ2aedj1je2zm8Bqr3NUqIDu0UA4AeiU_w00K5QtKMTT07ObK_aNm9BWvuNTaf0S_QFun-nZI97QFhb2-O4NNquTlo8wvsKtil98x7vkSnNbidcwfxUcodAeSk_PUVliSuLJV7vud2H-MwEk844Rp0-B5eNuj6wqsiD-hjFHKTsgTfnbpTBotCuJ75HfY89G4c6Hl2z6BimwQrXNGpT2SbSzEN4I_q8oD95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
