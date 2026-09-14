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
<img src="https://cdn4.telesco.pe/file/J8vVpPyR41eYPnO-i8wts9AEHrQLWq7a9SYaqqNuprZnaFUiMrBFuZS0Qx9UHVuYumyMJuKMYO6QUqvEfKjJnwDCNrqi6V2g0AgC7rlyCpbsWTjSssnLCj6Ch8Dj2-gm96ZO7gBqDnOVX9QmBpd961EKqsdkSzXU7bmYnl6b0_DBC3PC7SZY_MflMkTondqF_YEUXRTNS95LuezNZaIoH9zJ9xv7z5fBU3S3QcbNdnL4o4GZikRd-u__VFJ7lEzYxLBIxJnW_PEvrRihBQB19HVC6QJ8wJ3Oc7MOI0EH9P3fk_bRZ6ChAAe8r3nNNbrFl43qMQsn6kjQJ-fIEr51dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 517K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdnldCEQknoU2SJxor5HRL0ebrC-m4n9aywmQsPAngHeXmSiG572mojjHMP-syMOx_sZe-xz3Z71wZSDdgS795XzBzWBghE5XMn5CdqkdrzRNs8tgeBiBY-i837JyjsEDLbe-ivi05AFVcfSnCZzWsxipGrL0ioBJDe24p7ZnZ2l-JjTDIjXNwXLAvjBZ4ubjcz1JZOApHNRk-lH73SwOJFJPx1K97u3eLOa57kPfVkwcECh-gBatE527YarGVvmYMTnz1n7qWklOYYDznKmj_lqGK_84UZs371qhI0sI078bPV2pvYuzTRm5tJAzj9cg3oaJmqgBFMLM5t9WFtDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnr9-O2hlSsSWfdroKoD3_mvuJF0TO-S0VqE2i78gLggUd83FICp0mIKWtZb-XHZGmWgKP5I6AfHscYUfFKSqDvhLqBbdxn8nN-T3f5IADIVKIACqVBf4cMnjgx_akE3F85TPLUWSbuNl8lkSCZl0IbndTKo8LcWA4kBEmBqvYjYHkMll_gJwII4siqTJ4AEk4WCEPzu1iggLWks6SmUp7J82rb_4WUGL9iU8ONZozTI6YSxj36zGxxE1rYi5lSySmMXwLb015UxUQRZFH-CubPBAXIXWQu7o7AXJiPzhHS2oX3V_kocDG6Nqs-JNgQwpJ7qg4ZMCCLht5aJh1SjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29725">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfmp-eI2vnHbc2jdeHTI9_5pGOyC2yg7hHZa11i8aRoP8n2YtZ2WFCod_1NGdH8QbtwiA1htoksNFc4tXkrZtodp49B7AwS8SZ3EgVL-l4rjFUHQjY9nlo2CeM7vvKYBu3UTPqdem457u3td6rpKnoDmDzZdDglCSSuEPl1tAweVVrAiwPXmmY5O8-zZcBgnRrE9QaAuFhYXE8FZsdMJCRsV4UYq3i9Als0J3xi2Ub4pmxEGFfjDr38_JxYtZy9sabMVlninxBYsnKjIKnrH7tnAMfjsLbu5kAsqv4rJPIGgiTq0zNebueJwOdN5Bi7kGrPlVQE5QVdSwLp-Mv1F-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤩
🤩
🤩
هدیه ی نقدی برای تمام واریزها
⚠️
چه برنده باشید چه بازنده فرقی نمیکنه بعد از‌ هر واریزی هدیه بگیرید
⚡️
🔔
سریع عضو بشین‌و ثبت نام کنید و برای تمامی واریزیها
🤩
🤩
🤩
هدیه ی نقدی به صورت‌ووچر دریافت‌کنید
💵
💎
سریع جوین بشین چون عضوگیری محدود میباشد
⬇️
⬇️
⬇️
⬇️
r23
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/29725" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdAPVHFYmTqqVwa8dCQuFSFl-qgJdBCM8wqd1JuF9WDZ936QDBoVPCZD49H0i7ZRG1gnd5A613lqm9JKwjbC7StD68pVSIsL26tJ43pFJg-e0fe6-G_kAAIpi3vdZEPzduWegUeKzsm8ONZL9lUkitd0MZ1V9YVHPyhe6wXFCmlWdlqh2IiYN_rXLjJ8HVjAqGKjndSVmrSdYoecVY4ThEwgumP6M6NPLKyx08-OMhx15X2h4iDvm8-Ob5L1AnUNUtTxqkYCckFi6dNcK-LHJFAoKqejo1-5wQUWjENPQAt-0z42mFHaq_STzUz44J0q48zbxgPrh3CxfpugSCUWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp0GuB8DOseBnZjSHRxjyzz4h620WH1ZyQzxjzRH6vt9efQ1sAhHj9dodEt4L2cwnH05Ku9mg88nIcxzo-1wfaGSCW7FE_HjmUz0a05ACVT3Ah3OV7LxWKb6mW755ncpqX31UhpDNlr-gr2S_aclidbIfSlO4EXhMyOmVY3HT2qK0QwfucZkAyf3gemN9TnzpbSmzptMgm49baoBa_va8ZrWG8GSuA_b7C5OACU4jqT66hyLaq-L9LQDZ4cocZYOcRjul1HpHXfOJk8gfDZHsSI2NHLi0Z3wxOuvDDgt8-xhtmcE3yhABH8bcpYld9JpgqG3Xcy90_tKW0cULG5Ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddUjMhPzed8H-nlDq117CNn6xV_FwUgieTKhqETYT3P40nx9h0uwDmdqifakS591leYWHLfj62zWWj4PSBTFkJ8G2JRIyuTZJGGSbwkGU9YLzseW_lxBHrkOLgCd-0M54QCODfwWUTuvC9QeYw0VEXpE2fDB_Db2Ivt2KK7PFvOI-tasfoAwySVKGzNQ0c350GTkDcSBJwbC8Oc16SxEYUwCshDzSuROy4n20dM0IAT4iqYCmjhFpYpHA2-FOYr4MvqfP1q11rQ99eGX4KnbyBfjvVMCWomZrSsR7SgmNOICwac03Hy0Nxjn8i66OoztHg1iGQZ1cZzluhLXMDjibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IND0oQoFKC_sWzlvc_yN5Xl4M8DQ1nzCpeQK39nYvPnoE_eifpu-huc8PvAY3jgfmR-cWx8yeublGSRwDlxJfHjJWZQHCbyZQXeMFX9BZV9TuZrgJ3qsxA4-aueWVBM-J03SBqe7X-SwtX0wTnR7XfPqn__URr-eTt-ya6U7OfxZDHkhvUxsgAC2K7Ls-XK5JAf5zPe6GYEft6WjXw7GuL7Ue2_XulJ0YuXS9RPbjRefeJcQ8QHegacT10dCHTN1hAeI7rEgOj7rcRSazXZ0pKl0ptYFLOs63L71ibWfj9KPwmDCCDGCvadaB1ZR44CpCEbW39LMMX9k14QuKBK5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrE0DvxbwIHsazUfmrk2mqkWA0VpksrCM83GvkY4K5dD6et2T-EsEHw_QGJHAVZ5QU1Q1WTfLFfayvEh8IAUCozDjcJa4UdrdSXddKsBsamamnIWBg-wpto0sYxzdE-7kA0eBrbY_hSDpyCNhIcsqQlnYZ-0-x_i2wcVoPSkdiJR7zG-xjbIsiTginjUrYVj_xLXBcVWZAI5dyj6E2G9SqPm17Pmwh-afXmTpvQYuUbZjAxw_lKyhcgAnVHhPu7fXwECzNdfQh7XY0-c_NDBiXlhN1Bl1vBkVGufPhmOtaMfPoT7S84szF404H46tSwvpXHUUCn53CjsJjpJq_uHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCHlKcEsqvb4YCL25BdxdcT50Ka1Wes48iiCX3QdJi4gx8lpt-tZwNAOSXKDn2W6HjTUpG0FiYPoKeYWeW56HSij6cj2nvpBZYkyeR5dgQ7neg5au3YrY6IBm2Dn5PaCPBM_E_cuzNFaOmDr-ftUu0T7dGEkzXvSHkCYtUIGjjR0Ik06E_LkJOIuzYv9fzCotuWfJmP1Q4QdEQXcO6JV2Mil9G52hO959UlztZCCJmNPN7mSUglKiXuhv5HZqNrVSvEUE_ifts7mgbNIlCTPm-kVId4kOWD96J9gxBKnOZohqO1rOAqVH48HmnFZo6GRMvlPcLc1ibYDHBJwVgJDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4pVT3k190rqFhf6DyrnjcCci429V-2rBkhpUDl5T27NlUPgkcLQ5KXz19PdiNW5-rxCdHEzbQJAXSVrgKx3AKIGKIoXfCc3i8SKOAnI87Z1v1gf0r-WD3Pu3XuQkTvtaiKoaLxUCl40ScPCXCDYJk9dcPBQS2lg64gZFDfI-bAAaWPA4c3o-3G4lPNkqhFK3c5FDMXxVoxxbrpC74iKvwemuR9YA9eLUhhSTGIWVmqlXRCcMNk9T5_S2-e8W5uNfToHOQSsnDAahhsaCW28JXrarpQNcDu0BLB71BGPXFcWzo6xIPDGrUygkjJdSFHU29S19cLWolVBbHrJ7qmJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONGrwZ7p5dmzGUEr6h6bnAc9DRsNY2OIUNGn8GWBIXMCOAsuVZ1nUuy2GraJ2gNIJYJuS8H_FvZsbl1tH4qQMPI3hJPnwXI5_zfcWYRhmE0UDRrREn5uNQ8bl1sns9nt0pw_TlsudOXSmJR_aarMVZ28UqEVhLUK_XmbvC7eDRxiDi4hEqJHpps2r1djT9RCjyg9v4VDqBtT9trZFSZpbh-k1EEEyb4NXe3iLCerQlidWvZOYSEJtcnxDPfLpbVFTJ2hNf3phVG6bCCngoK1rBcUm8wUDYnr5aI2202VzJy5lK6K1As4y4czu0-LFg-7dVqG9hdBIZ7hwM0ABkT90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSAWtDhh4x8nX8zVmsYAio952kNg3EPNuJ-wKlWW-aG3m-fa45V5tvlysxms9B8Xm5GExqQ9klPT0H9jBt1qDlpm8bI2j05vsuIxEz42ySz5ep9cSV3-dZ-t7r7BZmZMn6c96YPUyOnR6C9gb36BYI4D9kZEnCUkRFfJKp5FfSahkigFiEdVvaNB1CAHhboa1J1w4P5gQ7IdFDsM8KK1jGUlqZhLjgppqn8f3v6Zk0MICKu36SB4mMnWXd1ZVDBelibvSDEVvk70bFJavhS6GpDFAiVNCxU07isbRb6_zcUB2EvYqucOERsNla3rRwV0V3FSfdoRvMXYEe5iZvh49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE5dOmrggkgiktf9CHYWKPRQmX4Mq4X0iLE13EODiKCjx5n4Pr-1yw4nY5emmyHyT6tdWa7-AP9xlvwBEeayF4nIFZH6htei3lepdhr-bN0tXJCT__NJn01YyqWvbHOSlS5V9Hjs1fIKI3VjfA4SKNCMTOnJtw3AqBQzkqFCtqovgSYoCXoIq4wfX3zi4q4A4uD7hf9jj7h26AXsbjWxYTlstFHoKRZOA4IvGmlM6GtEeHrNfTBKT9pwh4uVhBsgSJUbAQGEL1YWwizDmoN00EkswUjmv-5XeEXPB-C4GC1mJVA8a8uVEpQVRj_dCSjWZwMkY1NhtC3sRdTS6MidhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdw-XvfHdxHhABv20xr-V3YdgvhrrHwQkhXyNsArGUVGU6Q23Js3dY7GALlzkk4v-JH76CGdqbcE0WDKwk5w0_4koxCmgB2qJEYwUjnBqPWg2Jgy5kSJH_iMSXFMO1f_YNMc1N_ZuTWUGAb-UUANVe6C1LYs5OjJ27akVm7a2c5jgUY1oHdeEYtQZ7lisGt9bGl76rLqu6lvvk9M9AeRaNT4PXiXfR67W82LW5HRL8sU39zXIvuub9QaIs6AtaTgUnsuuX27vPUGtj2_BhD5a2ep1IXp_EVww8U9zFwtE9wPyf9c18q9xILJP2PMWyWNa3MqQN2Fk6su8Fi8GrWwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_mMWe8Br3VA_eU-BkxhyvSqUBm3gPHpw5o9tXxoPhhrNXXy2FiX2yRPIaRKI6GjIXr4MtgIgoDCmMsJvf4bku0k-xYaK_gqtHYIK-xG19TZ1lI3XHtkC8zInDOMaununHNlqu3NB2WcpCXzVCrxlQ4YGsRUOrtV1GuDu6xyzarVKSY4kQ0fndybSnGxockcLvkMl-JN3SD6zj70EuRC563NUFVL2vjId-fS5PZINaOkzt_Rf2noTSZhuUldUlfVtJ9d4libQ4moi0yIuPrJlv5IkrvbPTukELIaOavMdsXsW5wRQBt-peFoE4HLcLlD_ls5VmFhTbuE8wdibS28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko0-x5Oc3XZF2f8CxTPocqrZlA6eQQjBJEvm_s3kxvnGuu2gG-63IHWZ_eTuHMFMjlzcMkBtERvRrB2sDDlsBiYdoCPAiUHylGdSwzVxlkNoJvKywWehWFBgBgpQSRCJ9mo6DZ_Ri0QjzfcRmckMDUhEOeWNFhVZRZPPkg0cLRIUyOokB_k3dMdJDygn_7wAkjF1gykKhIKSJT1jQ7znsb67U7wta-NNQ6Cm43nQwLPRiV05LQVC748WI3neXavvTZxM8qLBx35Qu5l8N8VUcGlvy6ReriorLLabUwcj3Z5vj_uidGNmsELLIuCh2ejUs4WKnQkhTh92ECb0mzEKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWOrnu-p812CL3XkQUGFly589-2L9k7kEELi1DR29QCPFUqFMKT4V6WcqcSD74kgdo9_Kvso2IXQzeoLvgeP-nzik62exiaLcVsUuB3xQZV4XFB5mBHfxQoFPnbRd0p3mIvuaqHte4gPq_onyAStT8v4fewjl3cDAMJ9mVK4P3VzRgk4isCmVl31tnloniV0ke-EoFinTMHe7ROYfoutxaKPWP97NEoJC8p6dU4Xzh9GVP96XpJlPqcbBjhtfLSRrZ3PqpWkwyVqVQzu85FaO1VHwqIKEQFGP55iljF1A3lK0zySeS30OUetrPhN8JfOgFCouRdoCF4kpdnN-1TlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3yfAcU5yrSrL88bwASaWQUHUyjUHueWqzYB5yK3ZGII2CV2mMomzEhPBCeTL8x8ZiY17thKXdov9SdncHzRAHCFINU1qJzys2NE4Lso_IQXUWAnkmg4QlPeEe2SUtm-Yl9DXxxy6zh7G_DU5ukiRkflBIEsnWa-TgiNgGS_oaJoTVa7hqsesAe_d8eao_wEYursQMlqn0NeVVghWqqcfr8U30beW3zH2t7J7NfU5FMpr-cxQF5-p9wBxNE_JbUZX8nLekj2mI1YRAh6bb3bsEzNg3dHKwjzb9QHlqIoTTRo3L302lk7kYOgDPYC5QyV6FwEq74s2BvSuMY1XfmNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0jojF_Ta-HZcbeK-fBI31jQAU5TqvZnYvICT0StYf0Cbr7YRH31pm6gyFDyDh-2al6T5BCzXPTYRCb-bE71CN5-4jF4oSyaZbS2birWvHMpmzy1-g3kS2zDeiYkyYBR8ODLK3UKzA42y16mMBqGP0o2Gt6J0ue1TC8r6kgyvXZBxe0zMZZF3Q70X_bYOSskIyW6A4MnAicx-pNcZ_BzmP2gQuV0MBWtZhGTGWhbpbxVQ3jQInTuNaomGY7vi_bcX8vQ1f9JktG2QW2-Wu7dW3vvGL5N4nGFj36FRg0uwNd7KB7gqAshtATk8kIWdCyYMK0thzS43M4GzAKqdXRWsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh3i1yDhRuY_pPF_JuHv4pQ4b52DHjbGrJrOd0uPe4kWGY8Z29oJ8YMH1PrpfaHprWY_IgQ5d7_F4HPl_aS5pOEKN5prxEUkdh23AiFGqLrGjS5Dz-4w9GRGICIkWTTCdGrE_JSUiAgQCqgxyX3_vxTJSN4ciJYh6v4uVgmzbtKlm9WpUJyHHBGGAc_kGQkvYU0HzjzHlWVLl_uyA6jd3uDL7e6z3uWFMwcpgtYuW5paN8gYRA1FskYKXmKu00oL4kSI5uw3O9sCIqinAcEBfqiaXq5rNVONvnqj_i34TsiW0OyWwKhFjxyFpRN76fkLrI7U17KGAjFjzH-nVQKFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_jUgMhGMZyAS_RDuwvhlLPFyMjzn6auadaGCafLCXF_EkxJ0yNjNeYgCozcfuWt6ejzLM5dW0OIRMn2Jp6zcIcOKWW3-Oy7dOlSS77d-VwyDVQw31bd6Ou4nLe4_G7FQ77rjGxIE-WhL1Yzak9lDMdbRvxmajdoq7Ze42tC07RJwx9ubsq7WhC_m7qgS09BICpT9VDF53h3JkUV2pn57I99_FLcvtmG7mm8On_UjNYY0yvpvLaYfBprFDiEZeoFoAJjet5HiA3-g8FxvMyyO2j6bSrmc8jO7ehvQaigU_kLQNopcSLi0WGl2_QCDoQl2OgTpjk1Ss4vR3FCjPnj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqlx8WEzMrxAl3cwk5pzxsDI9J88JaznMhnr5YqcQsfmVc4OvYjehRouqxe5V5tKIPqTW5_Ek1fjKxw36oOVxZw4iVUgffANYNGj60rVH58AlUIYnShyH0KT4J-sZaWl_HumuzU_qa0ZgHK7rZJ-ud_OYSYto5U5tCcy3K4mD-d6hSQrWBBVB0sN1nLTAv_vpVzgWL7V9gMXqHlW_GcavwjiHj_TwGPFF8dK-JKyc099p4G-HboVIkIN8W7PJOuonC4wu8rPw514QQsAAYlzoD-lT7OfP9rEabflAgwuSXBya5wUiZ7raz8jvoUz8HAef_WJFIBjIXO-ODgw6XGTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKAFajkbwLw15KmioZJMysYoPIcMgTODvQSWaTdJ1z_2N9s3TwR6lXZhEBo-XnSbV0HcyvUdjjGZQMaeg0UTn2K_gWjwtMH71iv0gaxjlCFh15da0rUIUh1Lyyf7ZzJJi9q-cSj5BpluAAkeNftWRMslWi7nnUACmGPAbzyjGMgOBSYvergVB964wAmUawKhCGUdyARySJHgIFP6PrdyF7FFojkjImlxOGs4K7xj6RdQ8LFUfNwt081l_sn3omJYyXIimWpZQDk8VEXROBCVDHukLWTXl8cMya-0oWq9PJr_W-fGP3n9KmM9WEVc1kJ2GdrUYhcTF2ZaAqjtkPHL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4GkSKrjJp9_V13opeTTJPV5viJDQFcn8KtxbNQ6mvrayt6EEhxy3aTWt59DydbTTbaOCsHGXHW3axoYVuXfapsLM1j-vH7L_rXDN2S0r0IOWcHQbIjDq723lpxBaW2K8_iU5FUSDwWkr88KeQltyiGjOFqPmwqA4OwLofJCsAqu5ohryT1lAawlsQRHcBlRpnhfelEEWowKg8OmVF1QdQ9CQn8MGukzB4K7aNLsNQV6kJPs9xySBOEWno3hg_v97CkDApS_JlTKjT4Q0NEBL9_Q99QSC0m7-ZMciHQoFvwTQI4oi80Hv0vB5EtzkTgzYD0PJ6tcrzmyYwdnOr9F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrvYLYGZicYmBODzD-XRCvPZb_Ek2vO5Nns_nJv8K0l2B_DPL9kCo43h-gumixdPnaH3COgRtsNvgbZP1_CXt4vESeZchidRlYn6yNzhaKhlD_5Z3tTd9SXh284GS0dnF0Myf3ysYx4SpqTPvWg4PPAI1f55bwxRxlsnzSanDg5H23p20MbtwN9q3XSkjbnCf3XxJq3J-SicAc_81Q04AcDY3cIoMJ-GyWJ3eMC7ZhUg_XAPqe_FOzInW8MRAlOIiTs0s2vU37pT-2zg5aDh-dOk0if_S0iWFPgGo3PWTw8kt9GVsya4LCngv5S3CZZV6d5g7BewDive0FKIL76P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=PRXrqfFfc9zu78KPs0xevAKFLQuEfHBy_vK-fm8mh1borIUI0AeUjI1K0kQNrdcJ9B_rAZqX0eK5CqQ6H-62JjjS1MUdQ0LinrDm5Eo0246oMnxXQsY9Y8FGtDEHUEoNQEdFxP-IRe7iJ0na1UIek8fkTDAD-BU-gYG7mFCUzarOKMQ4cJK00pWusj80FO7nUuAZxkhlPstk2-zvv3UH9vFL1pz81Mu07JKHj-Ns5K3VnBoeRHjc8l-7ooorQ_uZtQ9L6wegVPSPIsw-_EPO1rlf3cgNvzonhGPP3BVM3gLsahiO9GesmcHUNo8LmnTDWR20_lEN9gAWM1xbwnRaaYyBS0zNZVBHTjkxZrVXRoHq-IBrUfFW_T2qoAGwr1GNdVzYoRQ1s4mvodn8wSiQ6NBtSJxhwV2TTzBmgM0toUuBa2bKhljlDpG-w5GORgFbKsgSgK8AQJapYUaiGaFB474Jfb2qG00er6Y6eMqbsGBk-dOilp_h0Gzv83LqnYW-3_e8YCzr3rZ5m_LLSVRXRDirgvcHbpiNVwjqtS4e1_MJpsRVD7sOxwcafMXHySG7rfQF4awU_Htv_5fyv6BxjDng6g93k3qh6qSclJI_R1sUYxlz0PbH7qNuoz3qTP8ERdSHj74vGDH4ZGtdPr6DkJT0BijiW3B1IXcGGyYMzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=PRXrqfFfc9zu78KPs0xevAKFLQuEfHBy_vK-fm8mh1borIUI0AeUjI1K0kQNrdcJ9B_rAZqX0eK5CqQ6H-62JjjS1MUdQ0LinrDm5Eo0246oMnxXQsY9Y8FGtDEHUEoNQEdFxP-IRe7iJ0na1UIek8fkTDAD-BU-gYG7mFCUzarOKMQ4cJK00pWusj80FO7nUuAZxkhlPstk2-zvv3UH9vFL1pz81Mu07JKHj-Ns5K3VnBoeRHjc8l-7ooorQ_uZtQ9L6wegVPSPIsw-_EPO1rlf3cgNvzonhGPP3BVM3gLsahiO9GesmcHUNo8LmnTDWR20_lEN9gAWM1xbwnRaaYyBS0zNZVBHTjkxZrVXRoHq-IBrUfFW_T2qoAGwr1GNdVzYoRQ1s4mvodn8wSiQ6NBtSJxhwV2TTzBmgM0toUuBa2bKhljlDpG-w5GORgFbKsgSgK8AQJapYUaiGaFB474Jfb2qG00er6Y6eMqbsGBk-dOilp_h0Gzv83LqnYW-3_e8YCzr3rZ5m_LLSVRXRDirgvcHbpiNVwjqtS4e1_MJpsRVD7sOxwcafMXHySG7rfQF4awU_Htv_5fyv6BxjDng6g93k3qh6qSclJI_R1sUYxlz0PbH7qNuoz3qTP8ERdSHj74vGDH4ZGtdPr6DkJT0BijiW3B1IXcGGyYMzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFyWN9YK_hMZtGmwNgmZbFyelEX5x-ghkImmZvHCNJbirEuOKsrjA8Bb-s4QhVBtuwko7B1ekMSxv5a2IIuj3rA2SKJtZY4h-c2KXrttQyrGb4_qiaQAKuz_TdgHBsGCAZkqG_ydBW9kwG23UThtdlWQAHICW4rDVnIFj8t__CrBVmA3rvkzGH_ytBOHAtF581QZUR6WqZaIri2HdFYCg5eAzT8A3AtR1yTfl1UonpN1s79QAV3hcLIoYP8KXIbJOneqHayTvIgx5evyimPEUYm8QZd7ODR-ZL-s8v1Ngdc1RzC6XJkRpFgzzg22RRr61X5FYohcq8hLiv0g5lCD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5X8vphW6cwTHTfj-DlLlz1Gb9EJ1uoUhUWdAFofFnwwuTdLthcqKCS3R1FVtDdMNF5n9yP4xUlOYnqxghNzYMxV9ineN4KryixINLoaSvMtt0i16Sv-0q79Dj-LcsruQty5-GiglRGmFa-BFiZz-SySOK7_NLMybwIQjPDjRp2h-xZ4IOZRWdJseMsZMbX5A8qdA0De7aK1znWs_5oxs21D1iciKty9hGHmYJYTqzY8rkCwxaLhZ0TmcEKvnXu993IK0DV5Udrv1LRswD5KO_EIbLx8qxJI7D8F3h6rpH47ww_w4ANCgulhWpQjoZRy1fYhi0z27GJISd6iX3QTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=nyLNvhFYYCrUa-pr-viX9T44xlgYNKB_TT9Hy3QL9xAnWn1ZEpdlR5D_bke-jzKnjgWndNDA1dofIAS3nU_WgJbok5EhHFupHk_J-9916-yFFbZiSsnsy4-h1zU2kfkQMYMpJ-ItVfc5COWYWw4wheMG_1wyzfWoI9MwDNe2EUOmZPK35YPbApR6uN9InRz1rHGLEAMdh62_tH5x23c2eDGkyBcSsI_mk1YobtjyWtQJAiERL2S1Sz6E4DyHWPCQu2P5qurEaayu0T2TYQ_3l__6BSL3tokpbRuonqcEhHtRTxvcGTw-s7BX1nyfC9nbqR_tNlNwSzJMuk6bbraz7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=nyLNvhFYYCrUa-pr-viX9T44xlgYNKB_TT9Hy3QL9xAnWn1ZEpdlR5D_bke-jzKnjgWndNDA1dofIAS3nU_WgJbok5EhHFupHk_J-9916-yFFbZiSsnsy4-h1zU2kfkQMYMpJ-ItVfc5COWYWw4wheMG_1wyzfWoI9MwDNe2EUOmZPK35YPbApR6uN9InRz1rHGLEAMdh62_tH5x23c2eDGkyBcSsI_mk1YobtjyWtQJAiERL2S1Sz6E4DyHWPCQu2P5qurEaayu0T2TYQ_3l__6BSL3tokpbRuonqcEhHtRTxvcGTw-s7BX1nyfC9nbqR_tNlNwSzJMuk6bbraz7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwmTWrFhk2xqem0xwMasBHQueI7RMsK73fI35AVz2h57AYELVGHNWxT3XmsixNVgaC2-aBf6KWGBYdw1WpkA_pRTpvzOTY_R6EccZ_RqP-2xaS51y1xGYK8Fk9bmswdPGiTkwT32xEKe7HynxZEfKoiBjNk3hnNeCkxdlk1tdX1hccr0zth4dGmHZ049OsVLLecvapUVHEkw9OoEUmX4XmRGcqbp6sEMkKI8oK5JB9DIA1VJfmANhcCb91-V1mrP3qk3j4LA4yFsF7Yics51jT93icAHiCrN_AoCc7mZINhqvz8QfxbX3IBTeBXm6c_GQ68HdM1VAO7Squ_XIfhUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J96raAIyyfkIHLiF3ubpcTGJpW62YMp2mlzeo12tGj-3oR6cWDV4oDo_HtXhfzgv2Fp6mr4DpaUMydMbUrB2MMDTZcOIpH4RkyHy9dApSN-IVhzOGRvizMCpw_bO8z01OmP0I4O0Yw2X8nU7tfpyjXwrinL2BF3A4V9BpDsGb4YtPdVG3OyZ8ha3YvwmxCurvzK5GDoGTpK4Nsb_SpiVRm9kR-9QhxTJuct9qwDl1yQ8eSRLCYDm5sDx9EQ9QmXwbn5JC1kBpD-id3tNN7NPF4VCj7Rm-pe8iUfci5vuXiieVS2w2mB4L6tMrBkgM7M8iIZu5ODh0QqynoO76dMXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0sMx9Svj14pS459iZOLnTiKk2wbuQAzF0B1vLgVYQtRfdDs1nGLNzQl8rEygP_SnwVJK1mjDklKqtnvlVqcRAA8-Tgrzpi8zkza-dFsEfBHrFDrfmj1G1GReKWKhuNZdIb7qmzK27NmHaskkef64ZyTA-dNrYJFWexhTRWNtGbwYMmm9SyUJLe-pmN6pYmI_dzkroa0XPJdBqtbCa_2P9jOaqCnRF4J8fPqKwp6N8qsCe_STwTIBFz97V0RzQMULpO2hdAFyevUOOW79U4xsdQcPxaB5_AlvWIOpGptYmrwAEGg4K1WSfAnftgogsxZwzmBP6B2O1DzRVeTWD5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlngNi6KHtKL0_pd6b2W9noQeZu_vsg0TexgELA9WyeqVreZUrbEQM3eZ9D_dzQBMLBeewHbQOZ59_nlYmLVy_DW58SPKtlYbq6MP_TmzxATrKNYsHBTMkfZBVdMrdmCjdr8FsKkNdIPmDimkFEhifv37uhSb_IBiSln0x7xtMmTcu6uhpTUknNCMIMDDqqVEokFn8TutgB4Fq2zjLkzSOKITUmUM9wLmZWcZibnJp-gCBoTxOoOYlQtyxHkqdsYiFHDu9OG6SBi0fB1gfmind1rpXb1Jg-CDTCQBT1S6SvT0X_PYoo_-a5PdwqqNHTYMi9FWDnSrkpTesnccjIH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SST3JdODqeUiYQLzfI2yHB44jsdxnxjL7elONxDIL-Sfyj5dcZIHC9DbkZhFpjn9MvWCgmTc6IY3LMDfNI8KDCYk0muMh77ZNybjGk-0fI_P4Z3x_z09Vr32KIRUh_RGo6L-jOA977NzkILIdPY42RDZPA8lkhZLmjH46p2KpzIORVp-2N9Lfc0ZADs50JpCtePHPvgDGgYOFvnbXe9P6W7llgAGll7_B401nGGc-HXQlzOqcD_kpnZji5v2lsTpHBCzXKEqMaGnMerZDbkiSFSL7ySRvLkJ8GX8_Q5bftqBCuGIePBZWg19jiIVELh6hSnMeMyWVFQG3B5weSWJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoYeidKELpqMqOINMky_1oQfpdQADZCNzS9Ojl_1hDsMrKm31iP9obkSLovpSIcx2TmoismG07571ipP55hnlM_IDXVSTypTw4nrH0KEDJ3aqhyhKHMogTL1KsriM9rTYfFhuwJh8dlsXlILv_BbCLN2e2DJ9vqbbmIeCou06ygCRqyoCz4r0VTBAEkNf6kkuNy33CURDkfDSvoinQiOsADKVCscOQKpgoErPZAFelX2kwTxIU9fJHR6sTb_qa9Bq8YSfkUmpGCBQtEg3wQwGCZ4iNPENvz9hfJgbbHI_849oQ9IvUgL8ysIc5ORCEQ_v4sxp98ewlc0ZlBfz8aCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2r6lUkHb1p8HX858KpW__-nTpcZbm-uSTsCmhQNoe-HLV4_iwAYYnCa3w37ByMAAZc2jr2tgIF2SYmlrjAs9PvdZXfjJIRHt5TIK1j740Hg-k89MjMZdMdGs9nb9ZzNL7G-7njwJWftZMszeh7SRX0RHqU_LE8eYfR-cR08hzpDkxgwDEkmJoEMG4-D4OrQVZ7PnEg8GheRDGcGCTYybHI_hpOUY88rndO_1gW0y70n7l1XjF4onlzIIDc55OnyfxgLgYNgFnjyPWAuGV1looLCDQihh-oLwVl77RhfukRlGxdDY9P6B9XUeC7sy7JuAale-c8hUlYH7BqT23Dy12ok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2r6lUkHb1p8HX858KpW__-nTpcZbm-uSTsCmhQNoe-HLV4_iwAYYnCa3w37ByMAAZc2jr2tgIF2SYmlrjAs9PvdZXfjJIRHt5TIK1j740Hg-k89MjMZdMdGs9nb9ZzNL7G-7njwJWftZMszeh7SRX0RHqU_LE8eYfR-cR08hzpDkxgwDEkmJoEMG4-D4OrQVZ7PnEg8GheRDGcGCTYybHI_hpOUY88rndO_1gW0y70n7l1XjF4onlzIIDc55OnyfxgLgYNgFnjyPWAuGV1looLCDQihh-oLwVl77RhfukRlGxdDY9P6B9XUeC7sy7JuAale-c8hUlYH7BqT23Dy12ok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=MZPgV27gS9daZ9RnbGS9aU6BYW5BWtvbX5smxvojDYqYykwE4QWxaeGR53TKJ3cnY17pie20kHDeeYiU02GJ_Vho2rlLcLstZ4qe9zdqs1ACpaRX37bVd7r9ZJpa6q_CyPE6H-Rsuo4BdGw1VjVgJYJSujjZ0J-W3allDVs8DDqmfViVpZ40X_P1WTNviiGUO66Uae5BF-GWONtY28b_Av903gsrqBsf7q1gPGYyrOb3v4VC5_LlDuxwvA2EjN2qLyelE4bXUudMBFzpOMzRZBM1MruT7ibfrbFSD9L94po3aXRjMd-vdkyHRuAI3dPhTA_CSrA1tuluQoPOL0xmtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=MZPgV27gS9daZ9RnbGS9aU6BYW5BWtvbX5smxvojDYqYykwE4QWxaeGR53TKJ3cnY17pie20kHDeeYiU02GJ_Vho2rlLcLstZ4qe9zdqs1ACpaRX37bVd7r9ZJpa6q_CyPE6H-Rsuo4BdGw1VjVgJYJSujjZ0J-W3allDVs8DDqmfViVpZ40X_P1WTNviiGUO66Uae5BF-GWONtY28b_Av903gsrqBsf7q1gPGYyrOb3v4VC5_LlDuxwvA2EjN2qLyelE4bXUudMBFzpOMzRZBM1MruT7ibfrbFSD9L94po3aXRjMd-vdkyHRuAI3dPhTA_CSrA1tuluQoPOL0xmtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUEvTYnbg2wFjYYNS4zWtmqarZKfwJxunmuVWZM_ZBmWC9jgy1ap-BphCOr6Bvgs_XWqhjXJj9GQ1eEWxj-K1-t8TBv-pHae5RkGK4XscDJcZYwKQGvt0KGx3RVCDlz4HvUHPQeygCxqHmi-H48bkdMg3-kcXh4teDSDxsdyxUUcIvz7dv6SYlICxVLVSHIW2TfTDyp8RL5c5w42_-z9jvjOjD9U6ASjfYW5Q4UB6ZIqe0TaKiLecIoJR5YVW1_3UFSdhVI8jrHazSTTTGiR74fWlPmgc9l5mMRY9b4T6ZKo9L1z4QvxsO9RKK7K9cRU8-J71YFEiHumgOM1ReogFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RenoQqXM00gWv2LbFxq-i8LfRDp9S3OKx8UMs-C184mfHAnmoDLDGyE0iBsehsrPXkKLsOIkEkVhW2NSA7KLpMRB1sYauZbsQHUUkSS8LGVvaGHO6SNTkxGBvRSfNwmD6dIaHkrDYXkH2reB5NtZzRg15t5wT2SAI9MD3YL0K-3QN4qGijA_dy2obTiVtbYqiO5KO04VLYvp-q2C9cHkPhCCm2eWKeZhIKyp2xflg-H6Rk2EbgC36E7kWqcEg0sS-n-mWYFhy7C9Cdk5TJ8_yqUxBc4vlCvX-Tdxin_ZL_jHPttL2nELSVKJ3uY-SAqezMwlpVzy4mYeDyoO6dTn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9P8pywIzH2CdLXZrvvnSMyxa0uCTgtLCpz5I80MZqJzPiEC6UXAzqMF_aS9JP_lw1qIReMm8QQSuwpPC8p5O2C703LM0T8LGHvRcXXXpxdXTPMDVjCy5rEW6294q1JJTBKpoT5Nlr1rlOr3oesQx-NU3-OarlMteChz2qMinC7Gm4gPnyDk6Mcx_LI1S6qOz2SBhQ8bvBYnuhWeVIUOC92o_Htj-JUbSe1tlcvSb0v6wHbl7PYlQO77AP2aaKqa0jP2ACL2r3PFIWjFpi0_yb4Gk6r7Td-NPdnIv4wDGRuRzQJDmZWb58TK0fJxWmo81m269Fc26HcKI58OoXqOgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE3eoS1_oql3rbYMWyqrqOoehfi23gxbEJgT-2-k6e3KM0XqJ0XQ8pTHUmJdSCczl3HO3r1kA867VWhb8Z1h-Xfikx1QmVk_L8agR7uelRdRL24UOeY1KBS8UXnvpt2s4pdox0LoE1_jOlMUMbQ6BDTrfoajBDNfmRu7qObo_OjOUZnynvxoM41oqNPtQWcLh7r3o7dWmRkHDtZ1nEW_dgPhSDe4NoJ-dkNfWZRgtsOC4tRQE-8JdmDkpAhc4J9OBB3flKZTvRcEkujWWgtAALZDjOqunDHxm2Bq4Aj_clt7jRSaooPS68WSPHd4eVKSeHPjEcYgn-Vg-9bTPbtrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=EnqNb9P6F-F_1rPgztq94QYhzp5pWxdeV5smSRkRw6--dMrSTYKSHAFduVRm6iQgZohx_UswuFBmr0y-mtczAVFRay5qV8RCd95KgeTWxt2arXDAFt5Tla_2M-lbOsa-uCMjLoW3_HmhvZim1n7dxgZJdwuUa4vgvrrB4AljuZDQ-Ajp7N5C8966j15E5cTnNwrYRgMRHSWYydTao3euIZGkbCfk9EHyVR-5JwDrUHTpcgRiyCdjfzk21uKJ26YvWihv1vADb72iOOTqUQlDBnWj6kQWxEB89Vwk7GYL73KAxxjfSiGFuDwbuX0ErLkG52b1IRWYhmcA_AFtEz7ASDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=EnqNb9P6F-F_1rPgztq94QYhzp5pWxdeV5smSRkRw6--dMrSTYKSHAFduVRm6iQgZohx_UswuFBmr0y-mtczAVFRay5qV8RCd95KgeTWxt2arXDAFt5Tla_2M-lbOsa-uCMjLoW3_HmhvZim1n7dxgZJdwuUa4vgvrrB4AljuZDQ-Ajp7N5C8966j15E5cTnNwrYRgMRHSWYydTao3euIZGkbCfk9EHyVR-5JwDrUHTpcgRiyCdjfzk21uKJ26YvWihv1vADb72iOOTqUQlDBnWj6kQWxEB89Vwk7GYL73KAxxjfSiGFuDwbuX0ErLkG52b1IRWYhmcA_AFtEz7ASDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGsAqevNusJfS7AjQc3sb6kHO5knqCBlcJgApnxvIcfOv1yOH0IGTjLMDHpA7_A6OsWxQFcSZ5u7Gm0Cz--oF6GtqKhyAYHQnZD7XYwmjaaPAVSAn-Y_dIsw8sb8WTLQcviOSmVnhdj6YFlDL4f6HaCWxBOh0fA9mmK6P1dAS3lmqWSG2rIGFuhykZV-pgKunNv1nf39pBWNxZND4MR1L7kjixHWqXRXJu594_Ptw2G-nxaZ93uI9ntxLHwBsxs9NdzWOQCcc2x6GXAtKz7Q2jNb9CkrTQp_575e4uIRqiO1-jI1hfbwtldUw4wsgLNo8v1YB9FfNeAZQa9T5x74-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii-sSuaGtSmN7joJCfPfBtgCZ1-GQTkauNfwbIUmoCS2Q-rh3B4NyTaIUw9Lwm6hPINLdawt-TQsapF70LYKujlDBO5DbJrsHKhgaEw6b6neARapNmNS3TprC-lA2356HkCiXICUWP_mDGTVJuDLj6f1ILY2tFPRs1JAskZfr-M60_4UkQpYPC1sJyhh-aazrS1JtrOWfw3UQ1-l1CVm_8zRGk92jSUxT0GslS_lQK68ysmqrdlOR3NP6Efx1aVsReS49n8YoV4BjPZLavWmboaGsEb1JkyrSAgmytbyEa2oc2YzeU58cSQ8kl6CZaNqR3yvYVhBviuPaDkm5914ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGzwbgmDGXmwns10OKIhej3CnqYBkZ8ShEpK7ElpQwr7nqSekSZyvN1ZAtItuX2_cpzhYOz5RW7K_ECfj0xYGdP4_TFMmy8yo0gC73qo83V88Ee476_CQFcgup6U63Zr-NhL0w_vvXnKMNWKCt8G6rW7tcZFA31ZIcGEDcd3Lvaqy15OyzLIlu_GvLibXOLMDAP2IHNDCIBkpzDJzrSGvx-sy6ophdKgfmor5NiAJMDVad4_5VYtNMzZJ_q68PgX3PeI1_sky7feRRb9NycxSGllksClkn3Z_6JPMPKiqi-66SzJoh1wZSzUo8pchIuMwOZDmfp-O0jat7c-NqEt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=WaJruStvRuzXdQe_-0g7kalRTrCJfD_LcbwiRmrS5Nt_JyOfL5DbaoTBuTs4OId11OvFhjUGPVt0r2Xkc4CF9vK_noDVNBR9-M0ekS3MIU7Q4t8HSEgZ1ACliiOcD2-NXWcVn6O8niW2Bkza1g6vCSSkgh7tfGjAfO6QrMVxu-WU4F60AATzgS_1mdUxqGj5oE_V_2GpNUEJH70LIXqN1UTo2iXNhjCP61awFy_QyZD_JlrjmeR2bZU-fJ91Ru2M0cFo_uxF7ZLs73hhAV_1g3jIyr9csfoWuS3JdwJ7uGMPtf25O3jUTXA2joLW5IoAT-CEcNs5OhCAl33JkW6ing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=WaJruStvRuzXdQe_-0g7kalRTrCJfD_LcbwiRmrS5Nt_JyOfL5DbaoTBuTs4OId11OvFhjUGPVt0r2Xkc4CF9vK_noDVNBR9-M0ekS3MIU7Q4t8HSEgZ1ACliiOcD2-NXWcVn6O8niW2Bkza1g6vCSSkgh7tfGjAfO6QrMVxu-WU4F60AATzgS_1mdUxqGj5oE_V_2GpNUEJH70LIXqN1UTo2iXNhjCP61awFy_QyZD_JlrjmeR2bZU-fJ91Ru2M0cFo_uxF7ZLs73hhAV_1g3jIyr9csfoWuS3JdwJ7uGMPtf25O3jUTXA2joLW5IoAT-CEcNs5OhCAl33JkW6ing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5nrCvw74If24WdgY8P2FqiUH0nzTazRZZedD9R1zH72XP6VLIy7oONH9qwYWyh6rze4f58qpTpFnj1I0trEQP-f3821qN6mve4OmFc0bKh8a3QuCnNwDIbMy71Bbd38IcEkBZeeaNi9gxj28kmL1DlGCoo6CXcZDMoCsbQKKkjG3EA6FaYMEW9sKu72Des67Ha-0lvh2lzWieQ40hI-sWuWS4uhzuewnApsvrU_vbF-BvSoUj_wCXpK0vDXH-NwMFC2NMUaGJppxQygyPIRTZ5gvDtaS9pBhypJPuX6hGzIwSohoXGKFCuOKi4-Dfy1qL8BcfxWyVoEiu6_EC-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7GnrkmbTVmZyRyukfsC1NcO9OePbo9IhUXv8M2UsSFp5NRq46Cr917wLEXiLP9Z9hB7W82JZeBmpTILkcJLXFjcrwuPRUoAsBlnfN-WUZBARrsJno3DqWBftMFlpbVGbs-Ls5qj2F4SIqOoQAOu81hJEaHPNg7myqx8nXwMfBpg6Anb5GzESUQXi350mg5YRBKaxp3Qu6-RB2GHiVdw5lPFfAjKYAsVeo1uiSHVQ4X6GLdGRInS4YCZDc9XbYPaidbKqC2x5yrrEgCZPq_1SyaKEZrhZYzfSCk7eRO_d3ehQhopfB3f2huPu6wYq9rtZuQ4duF_AHdL6jIF72AhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKT2DUY36eebBDQMFrKSdDLtbRTsJJyD2VFeeG_r2ohy8M_A97J_bTfA-P66jdP1hDEoyOE3G6KNYKODd32egFOUKBrMTcTa2CUCdJmGy6NnsbmR0xng9P6lukxBnREOUo8lORqE_SOop8BSkjpOMmP934CsHb4AMQx5mJkTT6PnhwgxrLFrywhOA1mXKuPx_-HTkNhPg55yR1_XWcmiHcCVKj8LnY15X1QWXA2hi7iieCpaz_U7AJOUsT_G3aglVy2yvuxw-27UOxKEgkPacg2P4-lcQNyaw7zpkWJ9Maj076eIXFW5sX_jdfyNXQixT6ipBwuIkDwV9j8HmM-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=HcrtEqxmvDDWnL4nE8W2EdYwRL41MqXGZtOQB_euMCGQvbng_z1uMNdSC96rjtRU1---3ruNwYvfeokOUSdksTIPtVf4pYejdjKM_dhMj7Yi43-s2E_OPacQxAMKxOCXHei8qTq5Zj280kochc6cXfvqYNloRq1AXjDA9rOS2GRfGl0vv2wcf8VItymABX38SSIT8jFjpZHjNM82PRQQlsgte0REmuC7toHx13Xi3BVRUQb4XM4wqkDCZHwopCwe7FmX7Uzu_XBmkVXzbnGD1Y4_nLfHjmmp0eR25uIRC0x-eHKdvKF_vE6b_rMOAPkrOhYu_Y5YM_mL-Gf7HlKOiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=HcrtEqxmvDDWnL4nE8W2EdYwRL41MqXGZtOQB_euMCGQvbng_z1uMNdSC96rjtRU1---3ruNwYvfeokOUSdksTIPtVf4pYejdjKM_dhMj7Yi43-s2E_OPacQxAMKxOCXHei8qTq5Zj280kochc6cXfvqYNloRq1AXjDA9rOS2GRfGl0vv2wcf8VItymABX38SSIT8jFjpZHjNM82PRQQlsgte0REmuC7toHx13Xi3BVRUQb4XM4wqkDCZHwopCwe7FmX7Uzu_XBmkVXzbnGD1Y4_nLfHjmmp0eR25uIRC0x-eHKdvKF_vE6b_rMOAPkrOhYu_Y5YM_mL-Gf7HlKOiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrPcJyQrMcGEPzpHQpeP6vFULFVzjzYmbE49KM0GXzbLuFT2rqgQpbz5ecsuqIWEiqFFhr8vwMX4FvKLGSWlr3vDm2g8Y8O15Ays533N3MtmrTFiMsJjVczgqO3kbJcAiRaAMOcWSjiLB2GGtohaKwV3CDGBl43y5cPuL87o8TeFqShVJgCh3YQDMycP9rFOE1UJ1EvcpayGNCzRI0ZSm6YNZt2LW2eTqH_N1fQGqUOxhklM9kUJXCFD-mLRTAtH0uIVqDJto-Nr-lYbMHuUNnkQkfRlZcyx-56_lgGbB8kYX--M81ormB95KInXbKfg4a8p4eePUKhBxI7MFvUYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVQA6HWMZI7EKr9iRhEtp1YaEuI4nwdVc-SMTvOXNX_0LGDp5SKYZMuo70Zg2wU9sycnYdGpoxhFtX-v_OOE4bEVulcXjd9X0aOKR0dxeBFk7eHVlOD28aEoPxPP0sarp2WcL4V0aSlh42pNCsSV06nYujcAikjCaDyii-eqmUSZ8iDxuoGwIWYtadMynyHmiWbjjY_E3_7CNmkXFcrCeX0WvYnFfBTzXQSn18MjifH9ZKkUPKApYt_34WewU0lZSKwTwvLohSEjx_Kci7aSAVUL1sgtrv7eUtfuhx0N0vtnpojR0xXACrdtkKCjzSQJKZ0S1g-TkDtZUGsncaVPjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBZUVRHN5XOFOUtj6lMWdmITtGv7VOVij8HmFEvWJ-TBjq2p_ZrN6kAqqAXv4NL3Gr_IyD8oU9XjGFqYg4JdUG6nJqDbOcaX9K5b9TTzUK3pewRp-NAp1M2XS0XOIcESmU6tGpp7aQ69Op01I8dO59-E9bkIqoisYiYlZvyfg12f063RUhseewyrqMBRieIeRHzr1Lug8_j233v7OXlPPom8alRMwkHzT-VQJa6Pd3WKwe_KZZ0nu71B0JkCL7I1Q3rdgKZPJlcoXFoDY9Idms-nWmXY7idwl8cX1VOtf4HvkyhKcP5NcDPSN7MKp3fWjByaeLFSA1wa2bvAS3KqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_tPD5IXMiaf59m5B3G3A3xsClNFKA1ELV-XCISfdyThPvzpE0m6ry1RiZVAbaybkrrdu5Ssaa6zdfIVtD1z6M--6PDX42KSdU4EZNhwOtw8U3JwX5ZC37ajc6juleq-hMSFW9kHtspZqM8i7dAV2GlMUY5d825dY8dtkCOK5j954BnvTvuC-gzjIxdtaHHHpNCVMQQUqtzwobYD-OPGC9S5g_CmxIdWHTr6WRsTcNyYimuYcUPW5EnDGAiAL_kQlpPXVOi4LWCHSse93cVE0Da34p3KUZG8vPqpirPrZQdd3vwywgIK1wiczguNGqo8YnEuIflQPwbr44mklB0VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdrF2IGOiRRbXJQHfG0me9ZEWOLXbSz2YeuMSZbbmacNIHTS4GNGnK-ZnFxwhhXQd1cE5UxJ92Vb6-X53KItqBDLtgYeUiuyQqc9CNln3Rls6MzHJUBDLb5_n5rp_tr30-8MId82UebW76mErT1NEYR7kGsRlRSsGgdt_b68PdY-lj9p-ivmqvhycVhVA-7_WrVj6_20LLF-hCt24FqMw7eB3EcZmGbkpydo0CCyi1HkHQmoC6xPS-Zo5O-qzHJNTfp_qwQ0jpZPyCg4SrgUKUxS33csRK--wwZNGnKQ-GHHNPTXzyQ7yRoIpIcc1_2JvB-pQ4q17-Irtt6yc-2M0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=OKg1RDc50zjx_Wwk-8yMnz19VuJlU_j4SjCszjFoBxTQeKkBQkgBYtbPEV94QHlTaPyosjT93JF5tVO8rv0kf3VLnxl83DUK8dWJri5nSKapT7romD9WFh6ZhaHoCfAG3kDVkz6R_9Bzms8c3swmTrHCf7VScY5-OfEvey42yLOGuYIufKodAXzLoZLwtDxNUlPtN44e_U97_C5cIP2i6mI-yGDiuyTEwTGmWeUrwQvf-h8iFut8BDHqQpUitsyVcRav_KZKTHhv8-vHdNW7zPWFSdvNDd1G3ikk8a7nlhCMto9NYoGglmEAi7RI9aSFKdebXmrJEJH9_JRxYVygLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=OKg1RDc50zjx_Wwk-8yMnz19VuJlU_j4SjCszjFoBxTQeKkBQkgBYtbPEV94QHlTaPyosjT93JF5tVO8rv0kf3VLnxl83DUK8dWJri5nSKapT7romD9WFh6ZhaHoCfAG3kDVkz6R_9Bzms8c3swmTrHCf7VScY5-OfEvey42yLOGuYIufKodAXzLoZLwtDxNUlPtN44e_U97_C5cIP2i6mI-yGDiuyTEwTGmWeUrwQvf-h8iFut8BDHqQpUitsyVcRav_KZKTHhv8-vHdNW7zPWFSdvNDd1G3ikk8a7nlhCMto9NYoGglmEAi7RI9aSFKdebXmrJEJH9_JRxYVygLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLXi7UKAlQq955pLEKT1107jbIMSX2JCSGpQFU8PmIlHWL4KEM1e0Zgx8hTHssXjwK3VRaSEHcc5A3pxbLusyjNvxF91uoI8615efjaNbqiJpW7IqIsGrM1qluOne_lRNph0mgwhD2o8tUAbwnDKaY8cDnuAP1B5UUNy6E8KfYqlvT25ltzqA9X3snq7OXFU9TyMbAjja5t-tOHzGcAGjcfIloKjflnpGMAQ76Md6q29CTTFMaypZnAmeQBrvkxMQMPqlymA4fjj7aU91yYUsUT7zgV12PnFfcQ-HAkzCDSdyFg8lEOyFaLKVn5WvYhj5hdt-kzD2DwV-aGAA74tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=VW9qMlZVxHoPsq3FCPvx0JrYMbgd31cHJtUG20RiI2r1rcZGPi7mq5Iahbv7TPbsSd2XL3YbmnNmAFL4NcyDK4AgPUCurlY6yKZr3RyO1dD5M5gu2bEjRrt6xwXg82VPlNDp95hGOoHJUp4Kt2vYUx5mNyRCLztTr3mL7qDkEEvBHwVpWyXpYqU0YT1KuVIGoi8s4EcRRz6Mb-838tZy9kOBOjxNZ5E4XQ5ZwUD8v8B7pYJMim3ZiRlRB2oG54x6veAg6_JjbcS1Thxy2SDidNIdNvCy4gp4-eL1xBOfB7ql-n-LZzg43Xvwz48WKceWPh_LW9_vtcSJe0-7D58UZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=VW9qMlZVxHoPsq3FCPvx0JrYMbgd31cHJtUG20RiI2r1rcZGPi7mq5Iahbv7TPbsSd2XL3YbmnNmAFL4NcyDK4AgPUCurlY6yKZr3RyO1dD5M5gu2bEjRrt6xwXg82VPlNDp95hGOoHJUp4Kt2vYUx5mNyRCLztTr3mL7qDkEEvBHwVpWyXpYqU0YT1KuVIGoi8s4EcRRz6Mb-838tZy9kOBOjxNZ5E4XQ5ZwUD8v8B7pYJMim3ZiRlRB2oG54x6veAg6_JjbcS1Thxy2SDidNIdNvCy4gp4-eL1xBOfB7ql-n-LZzg43Xvwz48WKceWPh_LW9_vtcSJe0-7D58UZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCvTOFW8vMuq-iatDbQ-URCD5Vq6GJ_mhKyvylI-7Iygq7FMYSNt_1FCFVpcGBcwCEn5TeLTac0HTeetMQm3kv0cL7DqivYpAMf9folko_LsdGfjgQ4XcHtxdrkk7C403lWXoVd8AicY31JERCullXWYffmgGr7h-k5QRic9zPOeEGvX6as7-XjmYRow_CDg_gsO8BVVMySuYYjN5QxStRw12NsPJr5FoaAqve0THlZDzlPMpyDMczKZdHnBEJ0GdXz2ZnfkmMpZp3dmKvvhyXmv6bUj9QsxM3BZRPuuVxULnNb95_2TwaqOPWOa9I6YB3sbqM7a1iVa4ZpQtlbGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5KIBDF9AdhdWbMWaJRk5Eo6iLB_X3E3q6Mhw-g7QeucCYgmbl8I5CPzeSEJqlIF9hpCU4L74tb_vZLKDducD5yFllNpf5-AbafKEsXPzypEMRDLFtoqALsoxjxOLrbWXBpJW1MxybPHDoGRgI-C9TaFPkVwL2MfkQseg5jXpTLpPvIgOX0NXaWnRYDLYuKqxluK1pm7SJYglAKuskSPQcSySanYTZgVwSZBc5b4Fg-NdZVywbIE71p609hQB6uS3F__K5l4PJqDOw3k1LXdRAoZ-Je3kb5FoC3xha3VT4qZ7ABlJrzHChNf5FrXtv2NIPOSOPxnx__bY63HBP53tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY30bWYt3nJtdNOk8Chpt7iIbTpPq6-W7dhG1k9lw7vrSaBjdBvqQPxwX9L1ncCel5RwwPSNvP7x2hFK4eOrw3NEFVJADpBeqSVyoQILl3L72G0w5Je5ufzzzgMVJbX30ZZjnppthsP0T_f8A_Y-dvnY5RgsnpCYfH2MjOxw9pTeJF-g5zYYVNQWHZfcDob74JDdGoBSk7pfmKtFXvg2HmV8paxOn0o1Bel-TX43HHYqq-BsjkGTy_nE-R9fmVmp_nGVBknWPKGkTduWcL0ZW-G_PSzQf_qDtkBq6bTmsTVMjKoUU2AezCbQOE8XTpjtAF4hM9KYNkoWlitGcCEQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIZsthJ5yt64q8X8Mnp5fyB04F1a8kclA33r3dGgl-s-nUduoLGt_dE2jFO34t_n0ayNxCiRIyT2vViVuFmpIVrpjF_3iyT7BGw0wdOB4JGl8qVpQvKZC6_FQnHLY4FLFRYTxHwslFViwSbBdf9sx0vBxFZZxK1Jf8K64ogu1LkiD7RRuiDg26UbhRUAQSgi_-9PfcQose4DWRmDKoXOtcY7RH-sCMHMZsBymIH3BL8tqWhLsK1EckiOIbdx6PzRgWGzxQz7WvMagnegA1o07wweyMn0RfIT6KK_aFr1VFxCtFN14N_5C1eOTosZZMRSY4plautf8uu82QoIuUc0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=NgyMTsKv5AW7lma2lQnWFf-9JQUzKM9agyegaHnWGEgfTnjtnomZXeIYvhkCPTH4h653MU43ygd3E1F4M_XzX6NhDt6LD39QknK-9aHCRcUXUnRhJUv7SgF84wgDqX6nDZ8E6mqfnAa9PduEyyV028cWa19GFQgwsOCvnl-HCge6va7LNJB8P1fzev__Vr42-pzv9HWaE4UhExlekEp1DG5oE0NHfvIrl5Fz7JZlGJrzYvajLjzogFn_TTEsKrlx4A6QwX5fRcoS7NjfhLtq-FeMTsfuV8S1W3RG8OLYq72skwGcgnpKn_mRlv6RmKuW9bH_6kuinKLReP9Td0WaQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=NgyMTsKv5AW7lma2lQnWFf-9JQUzKM9agyegaHnWGEgfTnjtnomZXeIYvhkCPTH4h653MU43ygd3E1F4M_XzX6NhDt6LD39QknK-9aHCRcUXUnRhJUv7SgF84wgDqX6nDZ8E6mqfnAa9PduEyyV028cWa19GFQgwsOCvnl-HCge6va7LNJB8P1fzev__Vr42-pzv9HWaE4UhExlekEp1DG5oE0NHfvIrl5Fz7JZlGJrzYvajLjzogFn_TTEsKrlx4A6QwX5fRcoS7NjfhLtq-FeMTsfuV8S1W3RG8OLYq72skwGcgnpKn_mRlv6RmKuW9bH_6kuinKLReP9Td0WaQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=J74ZgxFwn1tFWyf6vdclU8zBGjSS8EJvgrOI843b9_q3UYDd77BMrUq3A2JtRxqFeNpAtljP1YSVkQ8WeNRNG6PsuRxRCc-Cqf2mRa7OfPFLtFxAW9WBEyqtIyKKwnY3QSNKVeDcNTpj_URPsGeQhFLo6jw_Dj376OBEbCCyS55GlEawFUAA8pnNxDsq-eVXPNbo8eFnfIs0zC2J29wF2f5oB8jce9J0itWkKbvdukVFUtljH7fv7aviGnEHB_H4zTh84uoTeb8nHtS-0bffkOgGA3wgapLKp8bA8VxwDRfnxQymunbqZqXbs7V85dlRZIz5cO-nJizm5VnKQqcMnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=J74ZgxFwn1tFWyf6vdclU8zBGjSS8EJvgrOI843b9_q3UYDd77BMrUq3A2JtRxqFeNpAtljP1YSVkQ8WeNRNG6PsuRxRCc-Cqf2mRa7OfPFLtFxAW9WBEyqtIyKKwnY3QSNKVeDcNTpj_URPsGeQhFLo6jw_Dj376OBEbCCyS55GlEawFUAA8pnNxDsq-eVXPNbo8eFnfIs0zC2J29wF2f5oB8jce9J0itWkKbvdukVFUtljH7fv7aviGnEHB_H4zTh84uoTeb8nHtS-0bffkOgGA3wgapLKp8bA8VxwDRfnxQymunbqZqXbs7V85dlRZIz5cO-nJizm5VnKQqcMnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e77RKYLTJmON9uPSyda2ZUEgNwyyrA7iv_O3I2nbbPrnSOVvWmgVL9E0pDc1b6fTt-94k7DbaAIDnnc6ZIXRn5_snHNEKt1EAnGjFBIEy6EJlm-E748GgodaWmiOLxIi45vpEZ9ks8Gwu85-A_pilEVqnwju2DXYLnQNyQF7oPgMnwo-lQAG6mbgjHW7g05LQCpFPEb57_exAzBc3J2AXV7q1zpCTRmdAj2QMCZrrn-0soE570J9OgTVu-p1-RP8ODWeyZhYRjEohBC08JGVPIqocwj949EkwDzvwyI7BRITlVWPjL9ETBTC2ydGc0xWs74Mn5e5y6y_OoPPvNHABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPdzVFvOvnkbz1AssRqmUWb5x3zEWgn9136GaN3jsXsGZ7HWzzS6umvrQS89m0xiVh_ddsdk43gtH4IjJIZmHH2MpOGIHoJ3yW5buaWwNKEdzGcIUz_W0uVfQX0N-E5XkTi5vY_gm25HAbE30BaS8CMc9E9sXQQHlXJFEVDqirLcydGbST8C0E_q2BV3vhNDC4u0jO0jlYneeFpykIVWAjWQwQYy5gplCSar51dtvwZzTvdxlcUcX3xOH933-TQm4NFQydK4dcZZk9_Fc_4rpr4W0Pie0tD8tp6sks602_FlffWvLpGdoKtQFHZb6eNBz4KEtvoCP0ytWHVp5WZBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsrMo7lvd7-txK7joxMiMD95_CTkAmRFiSjCFhv8mRuL1xOAuxSA7z1AGlnHZ6kBW7sDTYs-nxD_oVjanyYroxWTG_TisA7khq5tuOjg8vfPxuMpt2D2otqx7zl8-hlRUJ6SpL53CSCn745MBi88UdIQTJNhANDy2J8Z-j3uyJpIFBxfCkc6m8SBSTJviUuXc_ThMlwpNdUigWPOfQPK9-dH3E5KQEUgOjX1jq2cqS0dml6qOFJYCCAWuhiJGo6LGAIL3nDP-_fCxBtX7-yNlMIumYzpkhxjAnSPAGxzp3N-yYhMT-D7oLwLPlTFl4H82leAxQ6XIXfomqBtsn4nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOFcJ3GO4atfQ5QAajeWmlIV7Ww1DiifDxir9elHAEoJnS4N46myzOJqlIjxiQ8M1K-QAmrQHxO9U704nqfSph1f4ef3eWtQm8I-6M_1U56NplOAzOtOdSuVRBSTmEXvSvda0kYukGZN3rGitqX2-zgqp3kgxnzDl4bH1UCPTp6bQqNi91OwoCn118VySA_sTy_5ZzJRaFsLBHvlDbKc4pvn1HxvoIm4KYcwntGLo9IbA9jwwU1BYBZut6Sxh6COrCUmXBQDikArhTfUOuUmBQ9Ek7uqSz4NnLCPkC7Jy0Udc2NtbIzrVdSJQPC6zgMYvTP9gkyFi5GUR-QqsILytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=EjpYolb9JxVLppVEve5fRMHQNd3tk4EaAas9PA_WaBZJVIX-sPZkg-j8EZf3dsg4Xvqnegm4LfHAsvL7NGf7FWWYMxxGysrcH3MoFCa2Vopnkfgh7YKYEHMQiFaHwzEwPv_kbm_n9orE7qzhymBXoD8OIaazuirbkKBlavR-VuXBhDWJc9FuHkjIsZULMcCuWbxNprjE411KK01VQcg745SjvJWPFVtg5tTJpeFgbFwUi8Ebc27k38ojKZ8wBk11uzieqVYu_NVhdTVbQGw3ZooAxh1Xr3tw1zHiQuS2a6gggHBx5Li_Ye13a2Z_9csTN0M0VkDmsjoGJcaxC6d7ghUInR1owmn3Ccb_5awn-Vcp_G2NssVfO8dC7xliYEqwVpA8-9eGuvEOdrXU56EOgVipmqq2fwXuuHxMZH8nj9gN0RFb3zScBeufT1nhZE_Jzdq0KtsnwiLeVzON9ZXpSpS072ZqFYaa7CiFWTWJAOQmvgZszrRk6AgzAFXMBwDcNAr3aHGxOlWpo49S5JjqzULaoWekrB3NDc7F2oTxMt7D0_Zt4aUe4Qq1sm2kuhMkR73z2k5j8sSpJzeZwke-9BE7hyNtp4PTWL6y203toUPUBGD8TWNP3TY9PW6Jr7r5DSise_PolhhGtKdA0HvHOgAyWHTSxlvsMK-btN19GTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=EjpYolb9JxVLppVEve5fRMHQNd3tk4EaAas9PA_WaBZJVIX-sPZkg-j8EZf3dsg4Xvqnegm4LfHAsvL7NGf7FWWYMxxGysrcH3MoFCa2Vopnkfgh7YKYEHMQiFaHwzEwPv_kbm_n9orE7qzhymBXoD8OIaazuirbkKBlavR-VuXBhDWJc9FuHkjIsZULMcCuWbxNprjE411KK01VQcg745SjvJWPFVtg5tTJpeFgbFwUi8Ebc27k38ojKZ8wBk11uzieqVYu_NVhdTVbQGw3ZooAxh1Xr3tw1zHiQuS2a6gggHBx5Li_Ye13a2Z_9csTN0M0VkDmsjoGJcaxC6d7ghUInR1owmn3Ccb_5awn-Vcp_G2NssVfO8dC7xliYEqwVpA8-9eGuvEOdrXU56EOgVipmqq2fwXuuHxMZH8nj9gN0RFb3zScBeufT1nhZE_Jzdq0KtsnwiLeVzON9ZXpSpS072ZqFYaa7CiFWTWJAOQmvgZszrRk6AgzAFXMBwDcNAr3aHGxOlWpo49S5JjqzULaoWekrB3NDc7F2oTxMt7D0_Zt4aUe4Qq1sm2kuhMkR73z2k5j8sSpJzeZwke-9BE7hyNtp4PTWL6y203toUPUBGD8TWNP3TY9PW6Jr7r5DSise_PolhhGtKdA0HvHOgAyWHTSxlvsMK-btN19GTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feru5V1aN8iAuD67vd7KKUs5wABJ8Jdp9YbdogSxXpSNXFwG2na3V1blPOaJAlaP3yZUY1vAeh6y1-C-Ef8WjWvVTgUGi7zGvZIWNVJwZs-VYDEzC4TVIpEmA8USVDLrC7fHHR02jSIlFdtBaTvEE9Q587Aw8GSlrLA8FnehbJuKuNgvbfl6bj5MXgs4u27XCrEQKmW1XOsJOc9eHkkW0QrCjEVpZKp8mXZuH1y8xNd1wFOHdte0_AxSvUFNkoaNDleACcI_au8dqOaEF-006lz91Htn8HBkaaoQTJx0aDkl1sUJg8k32-76htpeRiD_e_U2FQMPSVXuz4NxROJKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNsa87udtFtmItcz8-7h-WvbZ8gF7FoHCAGuBOApk_Dkc3YpFGXMnwsIoWsjiZMcRh4Spd3uiViV4vvkEaRGjJD48mZHQLdBMfXd3GqA7oRkZjIJOIWPDZdbk0hLQC2sT7c8MfoaoMMFHkgt_BLe0eY45eQfhz1bYhzVx4wqGSK07CkmYe2NI3dfgcJsB9vfAPvJoD9gj4iW47n5JvV36zP2gVaH-1psP4IYyOyV4E1EAmsrM8UA9IgSC9nP-Oa1Xf9UmIb7t4BtJRSdcoIOeK6MD3UowF_TIHgywN75BT3R8X0DmcOprf_ph8x72UvmrI0f529NO940DvCbO3JTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_zWLWYl3qKvO9tW1bZCCwtREpQ2mKxmtF4_t66GnIYFPP1wIJpUXSZXQtN8ykqUxFux6raU7dTFus9ytXXFXtS2Z1z3fp4i_WQhzuYj-PduKfEffLZ1S5uMaa-RGgPFZIzlh7Eo4KrTzTKqHJEZaMMNAbqnKiL8MdY-TwPHQON73l5Wqavz-g-xm1522NLwYayphzslPRlBy-lIHftgIy55vFHUUucjLmHXH6kBjgoIIIZaiOrHUybBbDzYeSapB-g0OXKTvtLxFL69OywgJURxl8M6zht55PRXCmNj-CWWAdCYiZRq0ONIN2Al8nvcrOnerBHEBjbBDoPpskLqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiAmUGVp9eP2jDSivT0gXfKeg2a53sOw-wywvUjCI4LYDdFdkxanJ61dLyJ1UvwKpHUuTohoxtpBNi1AtAybjhpsPtQhOKk1bEzdFDezr5Tf7Ho1Yk74qqNA-DQBYaUXXj-KEU-tMQCLlGTdv6a9GbtGaaQn3BcLvRZws1XEBv7kHWIMyN0FOfu3d5toc8c4iUZF7uk-l971LOpT1ra-VR47xKC9Cu9gLJQC0pWT_u1XVGwCtQFUveBe6pQFdDeQVzW50C3kDTmflJmT0LAzjBbHLMT813Av5g2iPV19i2HPfFstvQBxMNmdvMdfls9a6q1jocq_b83i_XYIrYiwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLlQopx3mBIoO8HsXHOx51L8cSZeOEDQ4T95oENPtciElWBK15SXY1RmvvludPcDXBeIs9o2jukHyT13H3-nE8ZKRRxE5JJz3L21AuJj77s0VhCywusLS9gVXX9B5UpMtBGUm2-tLGQ-CCUafHO1b03amwCRMCfZqLwOsGLRG1gXBLenehVobUvGgAovphwV04GBoZHDGrpKMbdiyxbyiZhvBAt1F4wpK11ZsZ0Op3C3kTJ-oZgB-Z0WMfMK7zu4Bp0_c5p3WE3qLoiUxed4czGz7ktdv0odI0qKrQQkn3PSF7_JvLU46FGrsehJmRdCG46L6fh5eGcC6LW2Odf-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWfv3I20sdGM55ANa-BryCqd9wa4LzTja4ChdRYlzdU7mWiNhVbOeaSkirE7HGQiQmdqpVOFXhyKTfDMDPEQcTziesekjp0O5NKIGS_83GCWtrbMQl3ypONn0bbLoV3SvU0bvF-eUBJ3w-d0JkozcWiV91i-eZmemWsWnVRf3fdMOGP1FrOTe1iIZ5-YDW8LvwqbUw1xRoawbl9D5P2QpHxL7R9aIcPvHtvZNfsCxIJDGsApbrqrT4a7DFBOX2eJoLcsdcU6yIbQ3PP2NIGOiU6OWCFmR5ct1jyalOCMrF1YRWRpZZUaNf2MW0HSiUbio2ImbOL-89Yf1gcnJIHLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pibjvHXSSAURu7icAyCxwYoq3okCqxgT_V9hBf7uUoRyaOK_rsIpPjzH0KCbSoQ9DfMkZh6KMHVIWq5A4JdEG_HNKnkDI2nUAow-7QSFIjqROsXNyInUjE4-CefhVKRrzhvTAii0s1rnojW-bPIWeGSPhg2wMBicgQVNRMs-2IkLDDu37oQLyZi-JkQ7g1HQc4c9xgtyn-wDuj9hdRfk4gtSKD38JUaZJYmt-zLR1RUgrKwj4aMP0KqOr_ZRGNA1eHm6K40rBZinArNDxgdnniKksia3pzb9ssyczWc7zxqXDVdgHrZo_M7PHAn6uRP7AkW1BQSXpAYwFtC9Xpbivw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjIC9HMUlLJKfOoSpGsNUngWYB4_E83vWBcBkr9kpbtNhDey8cSBRWJFuBmOcVeyNjDj2RU4sqYh7LA77ft9uZrvuz_e6AhLS7P1K0zUcdgCCy6ayWKjsLlV0YtIp7Mfar9O6El_TS4VGTxcxINK6lkNuuLXfJTOc8lvjQKGkqyweELvTMCKyvIdYG6a92g9nlC0Y-JrADSzUAbm92kkPADPxwFdRx1uyJHvRC0KFAB3wMnqaMlTYa7RQ7MjHkERerLT4R95fz0qDukn7TFTo1B0U18tfYXJMclQ27KPLJbTJVv_3IaPcrgStHJGxdPbr_SiFuw3g9VfpiVlJ7M_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4fSDeRDD2-KPuRONhprkkwBtL68-VkUQ28UxyPVXobw-dY-yHIkjIqZPDU0AoIxnlQX4fI2lsgOuN0owedKGT51NV8pZiY3dzoUHmLoPztPCjpJAcgcDVeO5gZW8mTLn0TG4xq02fmyUTYXuoKLLa_ntnu5iRWfXlm7kdLfMw9HY9BzUdKH_l21zy393QYGCTr6Jj5aN8hZzlH-nuy_xpxrxa4e2ofkTY-A_kwQBjMRtQBhwDiBlaUWJ6mgJ_qzHcy14-7mjN8FD15dktidzdAyVjP66Ymh0pcnebiocjA1FlVQNqxLT5cFi4z4C7uXLCx1Asnjl6SdIxKVMfwkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSu-LlShi8wWxFfAd1c6j4k6ICeyARJcFYl5dBF1vtqKxbX8elOdn5DltZNfVbN1Go8NlFW8Pc9wbm9ieeE45hHATqY-LPY8vwAV6ZLukYAqZBLJJ-ftkjIsQIgrzqSYdJs_hXPblQU2zt7FNG_i9JADjwY5M7EyZf4hfdjQvOsdcLGFNBBwR5gbSPYhaTlQemvLs77elHzUpcf0738aEPSJ7_yC9iuQ6JohKf6Qr7Pr4FRoE2YYID5x2NB4-CeTY_KHVlpOv7mHypOQwIPUsSfQCmxzWcAAs5HyZzy6GmTH3Mc5_jjJcg5mqmsV4DfWkNJrDZUhKqYAajaqX3YLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=NldooNkd6mzKDZsCx40a5y4PYlkhJNe_IQ-3w9mNzDn4NCG5aVq_16GfDVKa8agwtYIEapwQYa7Ye-317NT0Y1Gt3hecCWTgSe3qwsleV_JPFI0reGzX3bnmvpw1m1saPVS4Vd8RzJ3klgJZxNrSlj8nW4I3kbq8gNNTkUOxPw6OgXgQH-34B8ezgaz0kfZWjnuLb1J6zRNfm5L4To0LhsTuqYLQbZXu50_2bfB73wKLxJbIKyYkW_RZvt5q68WCNjCNwNOVawuMHOUoRJKsIoszLSKKHgn278IbE9V2OXNWSgSea-CxhqwSOQmjCXlXKmhdkNR5ML0Ov-fT57-T-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=NldooNkd6mzKDZsCx40a5y4PYlkhJNe_IQ-3w9mNzDn4NCG5aVq_16GfDVKa8agwtYIEapwQYa7Ye-317NT0Y1Gt3hecCWTgSe3qwsleV_JPFI0reGzX3bnmvpw1m1saPVS4Vd8RzJ3klgJZxNrSlj8nW4I3kbq8gNNTkUOxPw6OgXgQH-34B8ezgaz0kfZWjnuLb1J6zRNfm5L4To0LhsTuqYLQbZXu50_2bfB73wKLxJbIKyYkW_RZvt5q68WCNjCNwNOVawuMHOUoRJKsIoszLSKKHgn278IbE9V2OXNWSgSea-CxhqwSOQmjCXlXKmhdkNR5ML0Ov-fT57-T-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0l2JufL_a3xIt-dfXqXDlV5btzwJdn3RH-lB0icQlDZJRP8rKdJWtpI2J1evdwOshZzCDmni1Myhg2dIA0hdODVONhcg0cr0ZodlQOjjwfrBYkHzl9Cg3ODZ3Vknp6AfiJ_uHbUDHwsLjwoe8lP2H_MTkXRvv3hXqA0eqkerHenxVZ8553_Uk0CVh7ISO8RXyvcEJf0oX_7_mh7ImPB4yCPMEKaUsEn5KB6d9y5iJhra_VBIEyj2qYbIaGjvlW6AEyK4ZhZKfpZ1SB7p5s7sucX22fpNB6izwf44D8o6h3YgzKYDMKJvU8ah8UxG-t9dP1I8re-drILVBms8Rl6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb0u2Gvoud5lDb66sfGyfWl7iADLOOAJl0EX08Ij2sBR-T7Pt6A7C-gM0bz4-2eMw3ztJ4d55pHP3l1GWQE2RGCa1PHyqfJrMR53apBRdE8QEfnFzCCmfB_yaGTD-Cd6d6vh-2Fiz1Wm5E6oS1EWQYxpPkdfVgTazp-24wXJkGo54KJxgnAfBEfQE09uyoyXTFLKrlEGZ6o8iP9WjKMbI5cnw9FngwH57GxOw2yf6w13tVF8MFw-nYgy0GJ_SgjhEhd0xUh5HGex0bGAXgUwewe_54BhVxjNuJpEUwKaBkjNE6yUvASQg-m18aPbkHK3tvz1r8zyNyLLdDAfWtl9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB4KhrIOrg3b1p8xDFcf20s_8DmsSN4kUmDCWojSFQij2sWaDrfBr4u1p-NDNM4jXG0ttaFoPNQMaOW_k5ildvXvEu6FrXlp9WDza4Obb9KUrf7_kLfzUgBT_iusaDaRS7Z-HG3zQYOvA4K-UMyi_wLpwU2qI7vRj9XgB8yURoJsB34NeVMsR-joxj9IzNbCJzBL-TrijzQ9sAq4jXSxt26zlJVIlRM4mrB_s03-6HlbvJP_egwLHz8E7JlCeCJkRTs_Q82mF17jFAgH8-HlIFluDIxQEoy6a6nz4HtrolpVldC1ntY8Lfr5Kwp1i9Xy4-W29N9YrQqdKjU8BZcRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Px7hSA5z4IQb2oS3BHmepWjvpJGfXXnerbWNF3bcGmGwh9Ur1QfGloDAsoUN7Lf53NqkaBr1FuOWU1a9AtdCscCTHA3uBQzWpb0l2tY4iRl2l7ZeBdN9C1MReLSukTXBPZEETpNfILOtTRb_Ln9AShdhfnRYPKp4LKXRbbq7dJFzsYkp1Jp_3pQUjqg2a14FQx5F4blwZbNzyoXP5_iYKji2DE0kQe5b-3ZuuOJFsfdf2NDCNes9SOR9bgk_zGvQNbKuiaBMd4OsGQlpX5A_X2YqOq2qkUsJkki5tRgKpAFiP8FucpxWNnqvGxj3A5tWAiuVBD_1F_XSsFBudWLAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4yoTnW-Oj3KfZENIML4ioBuE0rVLm8xxYmmESBHIqfT94Xd9ZuWMKE5tBeGu38x86TDzMFqXeOi3zmFW9OuUVWJ_DnpZOZctRjTKMaznIeIvVSZ53fQHtYJcI4NDndO-ZwHKgqeZnlqkFIoZSrqgIWOxk4NtxurFvjbsTlqHN4ttMGKwOu1UwZYJ_AW9nUvaM1PHTZX10FRJBbp4Vk2APLwYNEcHm3z35fWxo8S3QsYYNYd0kW9YvNXm0Hs1OoelJ4vOwFtoGp9zNChB2RFNyRx9jOdeoIZ9rVOUFaNYfHliPkhiQaiFPV4hA2sGOY08UV09WXJp9ad08x5IXlPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaAzz9ceykokK02CRvTxdIQp1IovqIrTf7s4wMjIh5awFWt98r2G5aafy_v0rpzv6V6gxPtgxK_Iy3PBgOAtrEC18K05xyPnD7Dnw7jry9ZjSxCKZgcaU_PsVGkQy7JMoKICFXOuWW-a816ggnTFE9oHpduyerp_Y6InYY5MypMPAq38X-YHKKkW1eoh4zAf9zSLPamKeV0LmuLxz-_OQ-hW9sn0eoLttSZUrXpQiO_bNmADxYHj9iCcIxwhOjYpp_5x8yrBTCrZuGR1RUVHEpf2fRy2G9Bj2ddZi8RKVk6kxpRD5wqxYv3bnI8WzijStT6Zd5Ns-hLORnoaLdh_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCGX6McJGPqskR4Di2fxf4hBZ-QVl8vbxC3sXDso--s6Ec-DMv7Tv0sNK2VPGIG7ujuL_zvpgnCBE13XtaO_Lsu0bmhYSCrqJZUdxzOxlHDwHhkxnpy0zX_QaxTBV9QMzMscPVo8rCAXs9duZ_KVMLhzDVah5rUyy3klR3Ib5n0W9wFBKy8r397yJHv7IFFZFXLDUP1vD9Q5a33mQ1BxMlRYWYEBebqjXqFebk9KoUBt5fS83NZ9y2RUfr-4-AU12C1v0AxLIF8rhHjfgivi6C6wh3_d1HSFbnsv9q9BAsaq58_oME9lnut0Xx8exSHn-XuU1bd3EVkGVgpswzhlBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=FZSe334v9LSO9SyuA1eCpK8aTZ5TfGQQTyE518-RmLKen7gXYGXK8MCnEayo43JJ0SmYCI2PdIcsa180EWxmbICMUVGTaU_RBDUKxqdJ8RUKHuC969AhIwxs5XkoumvNBPfIuvjL4wdmHvmaejHudpmzs7FAUEWJoFF49wierG10vhWkBKjg56sPHzHF6XMzLlZP1uaSebYmfS3nZfvBehnbLF9TLhUSotmHbq20R3_DVQmXSS4I60OO2EOX7NvXelXldmkuYtr-CZelVs1zSujW9Ou7XIxIBfr2XuTOaRxHSCDtWRYV3nsflwVwE8JkueBvozh1n4filOj5BNhcSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=FZSe334v9LSO9SyuA1eCpK8aTZ5TfGQQTyE518-RmLKen7gXYGXK8MCnEayo43JJ0SmYCI2PdIcsa180EWxmbICMUVGTaU_RBDUKxqdJ8RUKHuC969AhIwxs5XkoumvNBPfIuvjL4wdmHvmaejHudpmzs7FAUEWJoFF49wierG10vhWkBKjg56sPHzHF6XMzLlZP1uaSebYmfS3nZfvBehnbLF9TLhUSotmHbq20R3_DVQmXSS4I60OO2EOX7NvXelXldmkuYtr-CZelVs1zSujW9Ou7XIxIBfr2XuTOaRxHSCDtWRYV3nsflwVwE8JkueBvozh1n4filOj5BNhcSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pT1GAN_MA4lCpgQ1R_Ous0HbX59QqzKVpfa1ZKUO-PMUQAlfQJhDxSIAFBJwgx8bsxw9-hEya-9KWYofjHzGdThKw2hD5QPLcBPbZP2DKP-Ok3AxCRDkCit6QVYw68hUnu2I_CpD6ezhxqLBzXYzDRxo16cotKM5-176qYP5BEfslAYyimK2Wfj8UuK-q0JhH2fLLFWNja7i29O3aoBOFlwExelhy-cEywMkrq0JC-sntl3NeaKS2Qg4bx7HWN_ijCpoW5DJbHeOgjyObx3LqGWQMqhpBi4j-cBCfStpHXEdxvfcc9QlgGDFYzs4NNQAv2Ab24c4OjRnFNTSPin8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJ_4EeOkTa0aq1YNwvWqz8PkLuHLuSgZoxBviLzxPxwLf_8cR3UsT4V273WriWT1BBYLu-RHli9X5gT4BnPyFMZx_nhrWO3LcStYt1_hr2N78vKRqMZJgimjrp78zFtijT5ehwg7t3ShIANc0m04sSj_xTjxp7FS9z1RyIEnvxl4OzisuTRRprUbyMeHanA6mwpk06yDB_BMtw7-PCYz2pKAFDQlpaW3zTj8XHDiBLKNKuvvTpAaDsF-IfuwfFh-4fScctGjFh1BPmMTg5ELe22ZG84wmRh-Xzw7p1rWxgbTxdX-sG_Tnbv3uFgflTS1oTP7fvFRaxEJKUmYkFQ2zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxKWk_EFllpHBza6rvufuaH9el84LWMC4Fd0L38negvCXSoAgX9s5TAjNUcfTnaFmcupbRCSYTr8R0tcq_6bJiDszdJNsA2iihiF3UXNxIX5Dv5wpqmF_jo-OuKp1fjoGiSTMBH1Ryo50T9N5GB9hTrb6-wLp8OHVYXX2zxsomjtXadoKbOKOPVJjkhSq1nKEDXbk4CmQnIiV9RLbGSPAcGIrhacjKbZVFHqk9cVJmlJqn-0jvoXp9LSHvCP0oxb9GzTOMxjFkIXrZUc4E7TVyMbGy4bWCqiYJoZkEcYdZymgdq15VOgKMtJMTOrKk-ljlToiuoEKy5RLpFyoXtREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
