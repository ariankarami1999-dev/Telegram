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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7-UOeWJA0yiz7x2kQLrm_yZ4xT69f70umKrUnpwnG1c6zeE3i0jcK6AZoyNiCTIyoakI0smZauYFB_K-etcG0e3--PuhYdQXkbRRejJ5peoKsVI_zhGjD1CedW43UyP0f6GKzB1kpqnta39mNzBfssz4Z3v2T8YNKKEUlR1ndXmn_0NjbLHezSon7UufzVVMbM91Fkmq8XMDxPY1Y9wZLx0A34mLj1J0TGTW-63XuXSGJJjf2mkIEevjqc22RswzZt-RnWRsaLlPhcNVvF8ERWm_Mg_ZT9M6DH5QixXupVrmFQqgEkB-Regf5OoN17EiQIajx2XxIYEUmkH0S8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btYw0NczwZYUmkYN74TbDUNn1kX4Mbb5DZjxSqjTpurx-e20-2yFgl6kssbV3BY2tcga5ULwlaxmP8r-gMyqjgy_aVGJ3qU1cGJnEBWJLOXLbyZtthZ0Za25HbBXlZlzKB-o4p26PuDLoxtctH4-8St1XmwPWM8R9km_DlO9MsjRdO8yvMUe2Hz4l9YYFA3B5sO1tE0tR7L6g151YVKdemRlsdnhCBRsMQazaUA3wtn7YLcoYmz9JVGgx6oOV2Fuy9GsvOIbBLtKUsLLZVHZMb8WL-sPDbd-e7-UKka4Vw7TwrBSnYs-mqHduQYlf5VcZRqKJX0lAlUm88wiCqMj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFgdaa2H-cf29WByl-aBmfAkGI4sqyuX4hqxp6p1ulpzWXdwSJY3WdLBWZDJqqFKIooUHyr558l-WkFcCmkwe4ncXdGwbl8dP-CGn6-fB83eq-zedBCX7KiG7V4eZjGNrqkJkdtDAFQg7mfwTR3aHwnnqdF4p7Xfcnhy1tMCjfk-0ZaWOWw998oNs0tjWmgwX_Hlda3lp0bx1Ge9ekCsljxwkmc5o4mRt7PtGs19AUZebULpYd3u-YgS-skWM1E6vxTUx7ZJW8Jb3FL1x5Ou2Lt8kkbLrkcd09N9cxZE1Hqz6CnnMfp9MO1IjYolfErrHzOzQQr1xbG8GKuof-iNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFu_i15RVbGem7uacHCSrGVxoNHbDWoG6wsFlmMhhZqjvrCLilWpwE_TPpoUSK4zjZcuh4JmHeLS0e8e1Ch4dg4JoKG5ITw9al3ng26zzjRbHTZkGLkuAYiaBrWlQk0ZSH0pv8gDVR52E06ANOnfgVGw8zNpLCfuT_bhGocYsgM1jGGaaDKiUfTO8mds0R3SjoyE3ddN4EaSACbRE0rRPqrJIlKaShXh_w22psmZZ4sG8dYWHewTU8_359gBGGC7D70FxHIWR7x1HJeUKGhDYcbveXIEaTrGzVJZCj_Pj-tYtuiLSaf1OD9N4FN_qftwkYKM1oAJgibh60zBXGpLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXQcSvENmcRPhUU5W6GIBgqZjSpPw4qlqUcKJD6Z6Nt2y-4xwDOwQVup0gTgurw9C86Q8juEmB2JpkaqzxayJNPUaZdXGI_r4-Il8jpNdCKfDhRcz1Mb9KhOGbEidyojrbwtqAhSvxZ7iwNh0rLaZ2XcjONvaD83sRGb_ew2LUok3zBzorzBxh5LeBrqCVoZwIw9mxTdmQG-CyZGQ4BxMSgezVzKlZO6rpWmwQRXUdjOgb7Z7CzwzRIYTRq9PWkGk0PdDzczShdahBsx_7c4AALEpOoittUQB3U1gXsjGoGICyMOsZgLIWWS2CTxSgLvc9x-wlCx51NZwxCbOt1raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmLEzLfq2Ffmo_v6i9vqP4YwALoqRb0NXmvdXVsd1rz7gFH9YyD7OJGu7W7qcRV5CFJXCTcBa2rtr3vN4eHjjbsZSBuCXq0Mwef2Bmgb8yamMVLcCApxsmtVkKj2q4JCUx1dAXTx_CAp04UEerL5YBq2aJ2gkujHjyPSM2OhfRwbbZAOheNvs4AF7dyOvDXHxCUkFnDAxovmsSiYgy1hE-b4zkeLdXi0mu64HCvzwBk9w8PixKvBMfiaOslLHLpvOg4FHTY0erfzyqhUjknRXNS47s74IafN8mo2IPJ_TUNxC7uLJ6mp5Qf-v2cPLEzGxga0xy8OMr08Z99TzOw8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL4FweE67FhSd_0ASIVCf4Y0o-RYIOcVBHSLD4D10THtu7C1qnNQ1oppj9yZGfEuKEdSy11qkywJznQ6CoYmlj-lthyAQDJ6BB-IfooIQEk2TdBxRhasw_CwTlaA1uHtkp0w4Myo8CT5MZTObbxxT7j6aRKpQulOKlOQV3boJmt7mWyxICohY3fXZDsxECrrro_x2MqAc_smGm6Km1t6jb--IR9vP6Of_1V5vnKqNpkXfIWZAzh7NFqCqs7xpNE5f9ZK_NX8QyKMLzqodvQgxikjEh1q_EOqlM7SfP686MXMOVT46rSfpFepEFFkiVnC79zWPsfiC4WOdxnRoqi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASoU7LVcxUUnkYHU4fIdcQSVpbsuUr8SUpaQIUi5cQMrunjmcm3x19owsI01gOrHdaouH_reyZoTlalN45bDLziVy5O1jVub04MbT8NRELWDtulN9X7x9EI5Y2l1ksskp6g4xGYzG2uYwKgjYB8gjTEBiunwTOr-G1JYd_oUbqQ2uGM8WBabd_7iJqQ-85dYBF6z-iJn1JggXMD_BeHa07-vnPLBob3QcTIl0xOJqL6xO85hgs5mrr6xAwjcV5B1oUiHDnEluWUnhDJNQ9fnaP5_M0Ud-LR19BdQJM_WL8suP0sZCc5DdqNpEGoP7BuW2LWyCj0M3EmsuSWzDqABgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9DIiwd0svz27YWzjkKRgQvQaseeU0v6xxjntDqr5XUtD-Y_1Yk8t5RvNxvpw72ARiqsZ4Nx6VDu-opeV6JivaN70GjUs4_uelvsX9JaUqy35iTlE-GS7VNdLIFGKID5k4LjJUqmzPElLj6tbQgcf8AarDkFfSOcp4jboV2gKmgEOaZzgKPc8nSGR-wvkhEr2oKUiy32R9LG-Y5j4ut8LIxohX_7P9IV6M8Luo2eBKT90NGc2WI8iAnXp2urUekgxymL4GaJy_X04BjJxFZowW5vAvVRPLxjyzqbpOmPdrazVL03RoB5J9scIKITDgQWtXj-Gi3FrYRgVMarm48K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1V2opBIAWxDbcJ4g3EJYZS8QkMzxKDp1MQNH-EzUFPoK2r3rHDqtzPpbrkP3iLj7Uuvrrx7lgF8VQG3bMEgB219UpFWbQZtKiH794SygQEUkky-fH-qjelayq1h9TblVicTL9MhSdDIgd2RIjVA8AfFzbr94dpYKxkc73fhB2l00c-dqXqO3BLKx9Cl24BpNVQzemMfrFWEh3eJRP6rl6nfFr-KC0-BxbYrG86S_IqYtN4YeVvWJUQQUKk1Eac6UQ0kr7jznXL82XOwWhzsAAXLdIT2RmD9q02RT_p1uBvZZUmPMhu8w1dskhdMxm4mqzhraU5KI4vl-9K78WvVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr0yR4aeKeOQURdfOiMGUokdIVCwaEsPryvsSKXU3TTG5RJ677R4szkTzJwQBn2cHojRJERvrY922Rpx427yKuMGOSbHT09kytSUFNEkBp7kBklGizEygHFcHEWJgM5Kg0EzNa3w92aVk_LIIXlyARNXXkVQ54ck_7ucY3aw8_LvEAuMiXGx3b4ZAgbvCYQaDwvBsAWN5P7UHGgDAIfVHgtXCfrZVoAmQwiKI7nW36fCe7kLYLOSh441UVNCrKfZHGPBs9FgTTP4d_ZqEnLnlq1yc7X13-0PFIa_KQGPRwSsAoYg2SDWc3bmxH5FHCEd3RxVchMAF5TApq92EHw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaLAh3IiAILndiyJe7PwEbDpE94c_J2XLsZCvdIzPQNEHPXtrH7fiU1Q07qk43mCOam_ylQOUzyAYr1azB8PMt1H7yNtACJT5z-WDnZQkWwD-CgPlHAz6Pu_nARwKGkCBUrpYrVsDNZk_yy02zC4jTULpAz-J7NFyvXOc3wG0r_AjpZvk7XZ-r73h1--9iFPkSojYszoARzewpbeKo3hyfylRsAmynxOkl8WvvUxaZf8XEAR8kJSYiCSGCekQW0dX0T_fVg3_0TYjbcONd9hu5sW4SvxeaYCQgUjJWj64QTaGFsTMXIYXscBLUyW3r02vIl7ht1ynWEwQezwf1W8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Bda7Hl8nl-sQFy3N62aHzVjlBhVgys9nzN7GGXbRljVM9n5nTJ22pFU-kLgDCs8e_A7bEI5b5ZVfEixg_p1S4g4Wd3aI8B_FTESbdfbriy2zaU2LqkJJsBwbQTtOIeKyRl2xiil0AdgAoWkT4I3b8Qeq2F3z35WZZq9GDBiDyq5GOj11SUe00PSzwpjbGuQeFAZ1ppPNNcUnox0IJeq0ESP5XJqr2bsIB0t11fQ_E-2mnWOL-Hecjyzgn89ySFi2sadbbCkdJaKZ1AvZDwAjzxzV6t7kfJb7N8_nMGCYdHFSaSHHi9X7OKsGMy0xdZTgaXs02oxd4iDc-bsGUTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CflROHh8yk50lUIQpeWZ7eSVcU7WN9XbHeFzvTKj_POWXCo4GxY-iriwiMPkpDsQ2no-0nxOYc-KtLxn5IQfz4b_e82fwqi8kL6eFIcivYYyp9cXZ5KHpWqEh2ktdexTwt0nWYfriKV9lMD6lF7WQq1Bp7QQoyYxXaWTpf5-BPILQ4nWI63dqu6IbNJxt_sh0e6zCcQGCrg44jAxXHO8y9cgFIUo-IY3RSQhVk7xYoj_3IM87XHXcibPn5r_XoX9cQLKflCMkxcTzdTgJEjD3aoBbRtoVJrKPaeSp6kNHqsYRGSX4U7_HvlBjaa1Wijy59YfGIzpojP9vaWO2NAucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EqiKjt8VrOCgmuCD1NXFWhWs7hm-b2D7v5W227kQifFCZhjtNnCdEtNMkgRjBZ5g2WU-2Xdd8H-XX1idyM08OgXAtolr5xkirpfV0J5Ufb0I8nyg2s_ZpNQYNwvjI6KDF9yw2hIzREo3yshNVsMk_griqwiufpKSpqmq4Zi7mqwkB-B0GLqMlMzznhpVO8CbSgl1cARObypYnq-YichtfIl9OJDo1w5jiABHIVUrW3hm_a66oTU5MAXo1ir9p-uA9V-AN8XCt-MyTStWsDQLyvqn8ottLk38tk9B-ewB7KthxJdSPxdUyE5dULIp0bFaKXhqhUcWvSzenVBVXZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueQVm6RtqT0ayFNYVY28Lt1nGupixwNFqnqBf0Go7UjszpxZ62NXhipilZ0mBsVTes3qWgGf252sAIRouMH_GwnEnm2NAlt3xHLmGCAYfIYHqtuf6-N_friS0Q-kOwUh8ZrivjZaFWLaG2KdT9yWPQQgdRax71TTXOJF_pgtkKvIdZslmvm2Ro38hmxYovrsxZxYTVaxOsL33wnMUS8-3flZ1et4wla8DtlISswZLovFD0tTjah40g8JLE5AKllkZKMUIuTI0OAqS3zJSY1dU1j_zWvLo5-bmkIlTvZJ1vop-Ep_XlWC26Y8TgjVGBKVr6l9MowaUgOV8M4iyaiPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=WEpxWZvkSM7CjA6ZZJtjyUoNhaG0fDRJwNLj78h7zgYac5L4Z9UVDPBxMyUe1H6lFT2MEO07oybRI8qfDntMslGhYnxx8WRDMqyWrenI74MCPfQiww9AsFUrCbk5V4DDGfDT3C24x-7rr5i_7oJzRoGAdJ8RdHhdYMUQnGkyoLGkM0mCRV-bseoiW9-yx-ZwVfeHhj92wkUrhFN4Soal2bR2SnukbjKwYAD6iff6dQ9CEkS9yLGcdfoCuPCAc_R8c0ry1XgNZrM9gc2Bx9OWPoq57CjcKWIANTsYYwCKhUsPi5QO6hYbrf75uYHof987OeirwF-hda19611QlV6tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=WEpxWZvkSM7CjA6ZZJtjyUoNhaG0fDRJwNLj78h7zgYac5L4Z9UVDPBxMyUe1H6lFT2MEO07oybRI8qfDntMslGhYnxx8WRDMqyWrenI74MCPfQiww9AsFUrCbk5V4DDGfDT3C24x-7rr5i_7oJzRoGAdJ8RdHhdYMUQnGkyoLGkM0mCRV-bseoiW9-yx-ZwVfeHhj92wkUrhFN4Soal2bR2SnukbjKwYAD6iff6dQ9CEkS9yLGcdfoCuPCAc_R8c0ry1XgNZrM9gc2Bx9OWPoq57CjcKWIANTsYYwCKhUsPi5QO6hYbrf75uYHof987OeirwF-hda19611QlV6tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAfckIPctkyuNfjN-WXrss_LiY4JzQt-xPa7pTtSq60VR_3DRnUgDarTwoGvTX5iVO46uRlCZOBhEpd5zAPR7X4JvnT5SG-laPrmkQbdg3YxNlIulMv9Wz56C2RHp6xIk4RE2KW0-pN3nS0J797KpUGuH4i-ERnt-OA89ogS7TxrldQxgUD5VQ_hhe3cpqR05EH6DzBEqFWpwoGKAiNW2Sq5qWOge_62DZG45NSQuC6GpOoO8fXgtn5sq2Fj4LdTobsYOO5Wfr1WLtwFBrs7NGXI_NuATZ7G-ZVoBDsNioUp1PnUgcUbYDEfgOQnl97shfkqhVSdRROTwvxqkBZz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJtLX453BWhRydlUoN7GE6dtd0xqofIjF9iwImSPsdtmTqDA3tK01R7synRu82EkxAUPbJ6eK5L_E3xt8Nayxz4_rTfaN4_wbgh3CRjfPjrEXEPInYimoo3fg72LdXYvfE1Wejq5SYUKCzMg0lKkEOSM-CWc5Vw3DRZjudwGH-VkNmvQQwCZ7QwGBZ_FwKzwXwC7vsrQownG6blwP4OQ4-r0GBLnH1-pYQ1mKXeWRs-ZJ_oxz_A2X2vb5-wffHxjNjjsEXyyAjioHcX8POYLyQdl197c701_uK7Q7oQoq0kBdrFhBikcK1oSyi9piGXOaY8a2j0HrPSDAneNX4MOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=XCjyf-_PHk-bnHvYW9ZRNJoZtbuMqWKCGqABa1ftUVcHaCoCFgQFlyHxogKv-SXEZmmPbpswlDonAb3gDgEesMQGCwflDzrfV1pn_eY9bgE7I5ERKysszhbFoNXSx5GlGQ0_fL4bai0ZLUWCK_ICtEHoyPSNWjZzuI23WR2iNn3rIt16Ie98qKbaT8ZMMVOAWPF6WAxUcF-Zb4FQ6UU3gNG5psqEWHM0gGnJmvECf9pqcJnV8gZ0BwI1d019YppgaeIBP_ta1TChJmP8h4IQ_TM1VBXU0mjIfCgejhg_NGqJxtwTx7BI1RYy2ojCI4F9CS9xgdPBbBcENCRYyd7pRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=m-raVWwDxo6kCN4gWi0ztKQS0ILostn3NGg2043KawJFkBDRgsC68M6O8xYO-e4o8XhW4xmEZawxM-_YOHxfgH6p4G7EITywSsCRr0diKdm-bzG5gWcJDViTtHfQ5AVxAROtQRgP4pwRfrXw267lUd4FF2q_JkDMovS3yBLTa-hkHrr6VE9vfMHdxvK2O-1_wxM51j0ZNmTiogN9VBUWXrDaPQxmFEyC-nMYeAnZuPsGX_vuTMj8QwzVw-emK8EbJMBhufR4_OYL_wdH2Vug0CooRJdFztOQse-it9iA90bW5WpJ3mfIN46LII2B-_r0592Lt3ZLmJw59kVOUQQD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiYXOA2ylKG2Wy4W1r8fnbRsEtNo2r7YM0T-lUoMwR24YId92a8ry-ZrJs5MAmVuADkZl3BEoTcGiSXKT0PuoVJq8iyMSpR03bM3SCV43rSSpNojZv5FKXqpkJ-LNTY3k5ste-_GCT4R0yEbQr5XbIV_ucTa6PMTjL3fY7k66L6XLEr-K8Gvurl06CNplEdUanILVe38XlUp4s6Pj8QIWKcb2OHvKD9mAGelPFUcLC-EG3PNzyxZnIMCf6SXa06ytwpe1xiCevWUKuYF63dFNuSj7PCAYkTII5JCbxXNxKBfMh5ngBP4DGoqIFrUWQ46J1GOM_nx9amIyw_G7APW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU6S_NVN0UKblYyH7bn-sXmSDYU60KwpzfzvpdJfLLCK6Fa0HrDQjmaSmh67PypPxJhNgosh0wNHnmjNmSTYkhcXcvj8ND37_qzeUA1_NmMO0PkUn7BMhcRqiuPKkKn5vX2u2XS-7chaOcI02sIbww7NfyH5b7Gk2Zi3MmD4D714_fOkyzQbsF8HZeXh8W1wHFR9jB_CShNlj9t_FYDZDUytVjsUzkD9WIA-9sjzTJCzI4ZgQf3kQl3tRMJSiDHjVpBrf9-vcBGx2p5ApL6vhSrkqu1sgJ0-KSFsUaz6UdoYKm9UevQFwZ0TLL33vZo-pCLufM3UiDOTfXVOiAYN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=XQVCeFzm1ZzNEjA37wIZCKM3iCTxuY1cDIfHfq1Dhx9182sS_ffa1-r1SCuC_louy5wBMYYvFlN_QtH1-0-5756mZ1rnqKK0LN4D12aHrPWLxx4E6EgPsBF5sp_3c7Dc5rE5heI3y4yZYHIGlf93oavGhG2Hauqn_pNWwV41jXupXG94cSAy1jSACLvsNw1L0L8wf7taIRD8fBVVyBHGQn22hEVAC1moMefFPdmgIevIWnlo4nYZwps17ZEeiyEaTwEiG8uJqC0IJwYyjSn3Sonin7PlqV8nLRm9ISlZv60RyCEMekDwtCTjDqUKqtCktVofq6okNXZXw0gtGebhKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=XQVCeFzm1ZzNEjA37wIZCKM3iCTxuY1cDIfHfq1Dhx9182sS_ffa1-r1SCuC_louy5wBMYYvFlN_QtH1-0-5756mZ1rnqKK0LN4D12aHrPWLxx4E6EgPsBF5sp_3c7Dc5rE5heI3y4yZYHIGlf93oavGhG2Hauqn_pNWwV41jXupXG94cSAy1jSACLvsNw1L0L8wf7taIRD8fBVVyBHGQn22hEVAC1moMefFPdmgIevIWnlo4nYZwps17ZEeiyEaTwEiG8uJqC0IJwYyjSn3Sonin7PlqV8nLRm9ISlZv60RyCEMekDwtCTjDqUKqtCktVofq6okNXZXw0gtGebhKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=kO89tcTTZWwXFAfM-hR1H8k7zbUX6GwTsy1IJP7x3lZR4zDWRVc9-4nEvt3nSDSO9RAWXeK0cUEOqa5US0dOu1XqDzr9ATfjMrKrWOeA6i6PcDyfdQTs_p0ulFvBJjECxrJowYQDakdB6Tvp_nOSOT8TfHLShJgdlBkWKmnkZSkkcQCl2xZSly1LFj8EK5b40j1FGlL6DFBAWCf6smFY2o4hkLn3fhCJvR8IQklM8wLjtp0BzZLruBJcZcZ30dkTcninwxgpYAVJ30TkvieEHkBhegK5WCCl2nTOn_1cKxEz5bqU_i-Nq_BSPkGxD5IKNHohuxPMmMDxdT-Z12F0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=kO89tcTTZWwXFAfM-hR1H8k7zbUX6GwTsy1IJP7x3lZR4zDWRVc9-4nEvt3nSDSO9RAWXeK0cUEOqa5US0dOu1XqDzr9ATfjMrKrWOeA6i6PcDyfdQTs_p0ulFvBJjECxrJowYQDakdB6Tvp_nOSOT8TfHLShJgdlBkWKmnkZSkkcQCl2xZSly1LFj8EK5b40j1FGlL6DFBAWCf6smFY2o4hkLn3fhCJvR8IQklM8wLjtp0BzZLruBJcZcZ30dkTcninwxgpYAVJ30TkvieEHkBhegK5WCCl2nTOn_1cKxEz5bqU_i-Nq_BSPkGxD5IKNHohuxPMmMDxdT-Z12F0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKoJDfkNM9YMycimxyjmKBe16hXn-e912X565VyutQ9lcogeobvsjulCBvY5NKzgjiaXxgd--ucDbzsnp9ZhvdCAZzuznVKH6aZu5mVWt0_iWheakxOrkYSVijWs30OslNwZ8sGsivxLta3Pb5YTgIURwvesw94Gn6S5O8T6y9erM8aLBW8sP21GmSKY7cuvwpnReLSMhiC1bMIc0NPuYBRi-i39hBNO7xl6ypAUE5tsnefP99KpYvSndzlJ6W4fVnfXUofphuHHgMzqD6XR6PRoiHTFg0_sQZ-GN8BotU-ZoB_WP5_p4oJZKwH8l0nsDjTayAYAzQGyp5b5qiyOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX7dAYG-dlDXQb68RVbpFpRwV4pDji2Xfwxj6-j5WoutK3hVWr6Lk3RtUQ9l3BbPSdAG__LZwOqnxyicF32zQPecqac0Cv_dkPgvE7guW9OcFewnFLBFFJp-M2ZqqmghfZRdCyDiavvBbMUIzAcm4g7YM-8n_pkHVSwxeR1QPUN2G7TScnJalKecTnaCX_3_lT61YOKwSPNiaSbD5671hiYZSFvVgxcRxaayHrvWbgQnKPYOSae8LdGCDAxdZk46vElid4YrHGZonUjvbW24k_gH7bcw472Eu_4j7wa3Vg3ltWJk80DrF7Jb2EGAzePMqcTV8KvKnS0pMB6q5ygM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtudsIWShVTlevzYBiL9DYKd582-B5AbFukZitfH_c_n8o3IamcxNW_3FOWRc11_IWKpiRQ_QcZDxZ5-PAtqVKA2uC92BBCP97hI58vHqQmUwiOVJUatFuLlZCAfwLobVBH2JkJQUEkkQYWHeG7V0x7CFHHfEhdRIfNbLrFFkR_ymy62RWoSABPT6vlwi2H7ZKePpkKtANcxbiTZzcxYoRIcfCD3WbTmJSy5FvYo38BeNybuAKL_x09kWE8yZSbYjOzxuLsJeSysahH9uo7vKWvi4z00EAKfLUuMbJ4f98BZF774Wr4tRYbqmzLX5IZpt_FLIhlUg67GZFeZQ03JDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnRBgtTP-myAywUlkTRCFJLMk0iHnG5Zay6U7z596U0p3NPsOD198XgKlpjctYW16i1_FplwAfoVonAj9dEeHL-xUxKWbmZL-UhVYZNlYAhMuyoaA6BD2mefxGrHWVS7rmiyq8h9lKH9_oFGZuhHe49LSxS06RLok1SKwfDmsqsLJ6w4OWzbW9EqAPxYVNk4gjc8kXl8v8URxaXsn1k-7cnxRbdjmyi10Ia8EuzsQ0rpf0zitcDMCKxxkA-IFBaZaShBd5iUktF_-NziUtBEGWYYtOToA0xqULKx2O6bH3G7QmlR27krsa-z5Ihnz0elt-SlrBo_8wgRr9-DLVV5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr2ZuO1VJmfBY7kDP3NohOOBdVAFpEhAoTDpH4cR3vreMSTe5uMMQsn-hkx7dX34nEDrOnktk6t14orfJLjSZNh0F7rmXNSyboxnMFBAIUNgZTjhjLxecaI5r2llC6Imfzbr3-U7Ou6OHt8bX8AXPqkI9qs9Nl-2F4kcmtOV4xDgQhCbSpVyTt5hfSvRmCwHdqiHVKGBVLpRbUWegZzh9BFExvyr9brOQzppyC-L-FuQIrofgSOYhOh9IMXOiyFYV6nk9aSOYF3wWLEmBCLyCHHCWfHO5Jbyl3zS-AOIFrPc3jRgzyEAUSb7Ct5LMBm6Q7CW5S0XoTVY95eWb0-Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hOwNEjMZ3j1CDvWcLj7RpGfvXYe5Rjut6zT_AdEwT839drx4MzIMg5T3NW4WvKCvMP0on_9tbotO7llIn5KVefsF9V6hoopzEP4pm6WwMaOnggpDPUp1zIseemb9ak3HTd12ca3F4Ziovdu-rj7L8cpSyyvIlsIRCsF37eXaXhGODabvgPKsK1BeAzBWgM3e2EyR2EN67qUeD7eoYSEvXzQWm2ZH-7XMA-9HgAkbUo7hljdgcIxrsMsrJpd2XrhO-grx_WByi39dfHYiHZTE33-JqCRxvkyv5h_SKt85iaYQD2YfETS0Ov_zxV3MjCn6fmjwxiK0WlCKLgX-ILTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7J8KAAjmOw41nFZ25kL1CMmAjdsYPlBzacskJxPbw30tapZiEUmeAmkb8Jm7BinkXCrEwmHwlGPcJz2kwcbH3h9GVfUGac0gNqJinhaOtZlVTJeLn7gIdhwKG5uxdR2s-xYVCaWhN0gZ7HC6GX8nEyk2AdzMdOzslVr6k1k2di5IOvbUuJwRuHbPywCSEhK0GDK01151W6O6DcGyKzk7DOIkApD7BvsHVrWjcgoGyc4UV79AOfhGtoo2PztFvV1SwKf3NCRaR2yqOKFdqFIo9nUxcHqENaTKWh0sV6mtgAwlX6E2cBr6tPM14ccnr2QoY_oA8XJmxg64M2NxeE_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swFRy3RwZB4q-iyI6L6Ybh6iaTNnV0ES8Et-KMxb_d8DpeAGh2NgseZ-VtUJCGzF28nGl2VrxCV5DxhVoFvz4X0R9oSKPzNVI8bVjBRb89LmGCiLUqeTH7oFAZbUOZoyz5xGhJ3hSK4Wdqh4Bd13JnnwUGT2AvjviFqv0qBhhIfI3WMRftTKtqia23TdJ-jSS6Ii9SR-anhW1dAuFQFWE1mM50xcIm37dmm_3TVxECyGGaL5s7oulZnpq57A4_uWxQYgLnmo2Zc1PjKxZRNItCEdLIkC0b2bu0zucPv50R6sqI7A943cO8-h2gOwOxxz62fPAB8H5IG456EHcX0qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=q2kc8z1oHlr5VBUWVvwdr9ek4tOq5LvSdiI9Ste74EMBlaqkMzJR6ZNBqLbhmcwNuLMgq1_L8jcA7cJI7XYw-zOOmexrflu3beU71LJiMDieoIksy0tKflQkM9GyMbRilA7ZZPJ9pAUKaXCymAZXRC9hbKkmR5SZNaeglQJrDf8LDVfh7Lcd1rsTo7wTZFfhMgD7JZJLlInCYzQSGcg4zLFD4b1-Fwq8Bevv4ayJK0UpbYnezrwXaPxUnHJGL5_S73boqT3xetb1gAPlo4tapF7ElIP5_WVtlry7TOQRkQV9gw8sb9m7bPMG6Xp4VfrEXr_H3t1NmcTQc456skqePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=q2kc8z1oHlr5VBUWVvwdr9ek4tOq5LvSdiI9Ste74EMBlaqkMzJR6ZNBqLbhmcwNuLMgq1_L8jcA7cJI7XYw-zOOmexrflu3beU71LJiMDieoIksy0tKflQkM9GyMbRilA7ZZPJ9pAUKaXCymAZXRC9hbKkmR5SZNaeglQJrDf8LDVfh7Lcd1rsTo7wTZFfhMgD7JZJLlInCYzQSGcg4zLFD4b1-Fwq8Bevv4ayJK0UpbYnezrwXaPxUnHJGL5_S73boqT3xetb1gAPlo4tapF7ElIP5_WVtlry7TOQRkQV9gw8sb9m7bPMG6Xp4VfrEXr_H3t1NmcTQc456skqePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=nmG5eAQos36dQ1gpGOO-eUovs6IWw0dLJxNtSw3I07GxrkELuI-gZjns0Vg5rJp1BTwbV0GFEBgrQ6RW_tOYg3qlzsrY9Eng1Az7MnToZfVyljvaiOukQ9IAEs-TXijxW3NYhBHoBszDB1CKF93-eprVHq_xXI9u8cw726WL3vGp5y1VSy-XqJG-2pObKgD-QWzynZoPS87jMTPEz_v_6aluxRVWLPfQwfzHs_Z9HWXNxTS7nPDvcAusUWWCJ3-sZ7vhmcWndUQo9evt3PS_cFuIJyujxZhZrX7PQnjdYF_v1ky4DILhxDosGZfNVUKL9T0Knq4nXaG5DDqAaO4bZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=nmG5eAQos36dQ1gpGOO-eUovs6IWw0dLJxNtSw3I07GxrkELuI-gZjns0Vg5rJp1BTwbV0GFEBgrQ6RW_tOYg3qlzsrY9Eng1Az7MnToZfVyljvaiOukQ9IAEs-TXijxW3NYhBHoBszDB1CKF93-eprVHq_xXI9u8cw726WL3vGp5y1VSy-XqJG-2pObKgD-QWzynZoPS87jMTPEz_v_6aluxRVWLPfQwfzHs_Z9HWXNxTS7nPDvcAusUWWCJ3-sZ7vhmcWndUQo9evt3PS_cFuIJyujxZhZrX7PQnjdYF_v1ky4DILhxDosGZfNVUKL9T0Knq4nXaG5DDqAaO4bZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boe5I00hXrfiYlqfdQ-GbWoVOk5TfgdCwcFh0Y6ywM61ai_8idHsYJpHOY7FqdZKgGi1DjYHlP2QoTSejUF21GYhDvrDfDxNRI-4Cg6EurV-6RD0uctgImMzviS7GKjganRRYbzMzj1lYdYJqvPZoIDHDCTH3BzVmAV-8gWHC962Gm9_1YaqtnpgPLy70dX2OOx0Se7v5V0OtaZAeWpRUwVF20esWYBP3mv51kJeNivQRQgnjTEyJh4BbzjdubLf2l0OgYj0yJFEw_we68ZSeeJYC8C2I5OXRK6582n0D0QHZYTR08MUrFcmUtw8O0IaHVdnooUtEKbT-Xu8Lenjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_QyoLAi3V7G9fn4lqRgE9PscAwYFqfVY66sbX3akxTmGN7NczBGQBZJKFSbPgKuUNV9msJWE8vD_N1NKvUwBCkYBds1FEGe76XLTXQJt1USZh_RcbnMmC-1FaFYwEA_x0tY9Fegg2PhRhFUE56Zvq9at8DMmk2_WD4SQwCq-3mueMYRTJOuEPz_ezm1wMcNi1PqlkujttJ7kJ1RQM_jgXGpLj6YwOzA430HS0I2XKxEBEfj_7XlpltV67u_1k6zGTLG9pg4xXD9EGLp44J3tj-svYtOgqx7kaNaVRZkBAzT5icH8J1_v9fbkhPNf9t_CiwmHT2E-mtDPUq6jsif7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=K8TEt898U-36qmqWjJRr0ebQuQ3sBVotXkL4vehkyrck8JZ3-IrT3EOHezYqX_LpHO88SjH_UkfjjKhASRGPJx7vMYMBvepd0jtuhIBs_NyB-kXNXv3_aFlLciXQcwtKwwvVkxhjStRwKbq3ydG8tLRgALgKZvxi96atm4dz_iFsnnhjbruZ2218oNLMuLcefSsxYE1Xmck-b2lxyYLiZMSQHkrmNgqkmSjssGN18H88PfdskpNI46UbmlExviAJ49Hy4e3wS8qUi9e9eTE7I30Mq8XUrSIezENFpL91MuAVqBZ5rMvY9RWM67VVWugWBGZb5OOiuN36kZzmsLcgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=K8TEt898U-36qmqWjJRr0ebQuQ3sBVotXkL4vehkyrck8JZ3-IrT3EOHezYqX_LpHO88SjH_UkfjjKhASRGPJx7vMYMBvepd0jtuhIBs_NyB-kXNXv3_aFlLciXQcwtKwwvVkxhjStRwKbq3ydG8tLRgALgKZvxi96atm4dz_iFsnnhjbruZ2218oNLMuLcefSsxYE1Xmck-b2lxyYLiZMSQHkrmNgqkmSjssGN18H88PfdskpNI46UbmlExviAJ49Hy4e3wS8qUi9e9eTE7I30Mq8XUrSIezENFpL91MuAVqBZ5rMvY9RWM67VVWugWBGZb5OOiuN36kZzmsLcgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSD4o3xrAoaRPRZgIoArcX5gfKioeZGiXwyXwRmJwiYHJLHGDnLbjfsGMQDghxU7Dkg6UgpfD5kBpVXumT7GpUUNr0zaALvP0QSHZiC8uYdy7rcGjhle70rvq6ZpOZ1nqLaNdvCsPoSY5pp88zrB114Op0fdcTBLaS95UKop1Xe4E80Ukg-G93hXvpgM-TLpqH-AaUaLPzs2c4fjutjDCgxhjVmvtcD_uoSMH6X3ISQzFGWWkl_BWXaDR1M8eiQCy-sy4Kwbxxy8VgUqXvoKbE5b7L9EK_cxcMpXf8aC2ECovH6inuX5WQOCqcaPBreefjxGzn8wuCsl3nlBG0xUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHq7lRSomFR6f6u4dGcLH8inKOvtC1Mgd40crfUPMAGNGbcTugxLLs98K_c5re-AtJX5ACPjJO2E6ZLf42H0lYBJL1CIEXNAehTAGHH01L91uZx7YShKi_IwI92fgyLDaSm-aXileKGGTvYbLCTKXlxSo-SanZmDkCxlse3ZLs2sA9BwuVCfHEnHDuWFPJ2YsxLczNZThhfzV2HUqgGLindRRBdcEq4TG_8H2lH4i13oXOUy_haaZ8X5fpqAL3yDX2KIZ7lkRW1qbn4oJdvciYw0eCVRoHukRGsghVA7cDaoRS7VQaSqehIYJnJKxTq_MlSjhIGlpYlTYaEgX20YYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug9v_U0UPumZzgqw8HN7lXtgk68qI2IANbksdrbY_NMhFosGnc4tIZMcSvEzzUU7-nizAv54rnjmiN-nZMMO0J6Vg-RM_XtWXhcpFVzNov1sECSN-xN4L1Xq_OP8oBR8swYQluxykIE4UhWg5MaXb3ztaupfXeOTQlC01mVD5Xbyi8-7ARBmc6kiWdjsQP1DN7Tis6IsQCnuhcACdRMuCggU0GD7A73RYoV-vVMGwbV_U5kRf_hV5f4ltPWc-5xbDP0kO8JkKu-XYkKJSLaM1y9bfzLwL0uLHxZdG0TPHGKweyrjieRMAULAzwGw5zzueNbFy0FMVWlogKUnC_6EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4RIKMBL7f1Wd9otHIy1oTYpKBbRYdltmUKEldUjddytZ0eVHo2F7wbJ535TT4R8q6ajEje_O1Kn-WQMH35ubtwPgO0cMqqzITYKr7V7QXFoYngayHX3lnPEUBifrSB8lCHGMwedyAr7so8GpupBIw1qr0FUMBvaOdEshUp0OxJbw24YAoZKhQjyd0vHYGFEJ8gVWNNplMCEPyXrYqfe10_a3JBmH4u-Kiack1XzUHGvst6lVEd6Q3RXuX16wkV4yzW1iq4XrD5c_KxjE9eg1IDkJ8ncfS3fwiuFN66tOT69ZvB2cQQGdZJhHmHUrf74ufelF0ErJwSzac7gq5yy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZPaHtTY8o31pxNCfcs9PuiOFkMQsXSMWOK89irm_fe2lci5BwUOq3rlr0sa48V3oQ3SijG4Km_mJI7djmrMwpyPtyV5aAQdPmvCMO3_v1E7Fe01vTq3_RbPZJoS9lRw70cMHL4vHAV32cxoEOV7KMk8PLfvrTOAS0WUNYZ61g97M0M4Eja6taw6p0lhxmrOcSoGUOHV3mKIcF5Wih6LLWSkTNsv8kqL_hWsROKik3BlNkyzH-JQCkvoFiqu-M4G4KvRHo7UQbcl-BGu13GC-bKrcRj37l2ziRlIE3ERxzpBP7MDxjFfIdZHDtb0VEJ3KtxwuTu_3r1fOMyXZZki6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h30VYD3q-zIqvpHhCN01VxL1YaXIPHNtOUnrzkymOxhma4Keka3fQMzP_qM9lpG-Vkbekfc-OX1tBKNWlUtE4Dnb3AlSsDqEzuy94xGcspcP84TVsK5wWT26h0aHQMrC9MeddYVSbPLa_1_MvFcRl0LgAiH-PKYPptxblE5BI0WLqFGJUu09yTLM-xm-s5w-X8mYqBkzBQjmBuGuH4yIi3DMVLceQsX43-KrIfEu8RgaCtIYVfuNzNBzOSJ2kL4KNv5lTTNFRK-r7FjtDDf_DQml5FRe5wrXxt8wB0bXf80eynIv9Pexb_LJ9NZ3qx0HqdgO4qE7u6hjYMgMoAsPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALXyIcLJwKew4MUdb8CMx5mxzOZ4_wr8c9YKlhyQI1yPDHeUXoeNyzg3Ir8dRJANd3PBXwlLV9dCMXLO-_VvVporjDtOAPkAiticIAwRAiSRk4Kw75W_M_FaIvb-x7KvKUtucHugrKGcQ5EFreJqnOsIHMmJR1eNmOs8puRsEUIJB5NooiUHB1-hSb_UQbauirAglBuA92g4MOsZNCYYQ98MCXXiXJ9l-PXeZuLK3YKtN3uqU8mi4zvld75ZWOr28N-yDDoi8_8ZzTNUvfUgcF5eNX5o7sTH_8ndh_IWSLVoon-sb4EGKTGi2CRP3bDwmOSwFKq9k-RY2WNwRGcdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUSdqaVS9a40r-womch2rl1lCl-61vJt45eIzxVaJMG01Bv6xsliMmIFfrfYUaPRSceqMrY5LOSLU6oX4RVeeWSsSjLjkLVCuuzvwWluOhXJ_1KDugHRckr1ZzO-TGeh2-RIrgE2bGbVlXSQeUxHjF21CaJuTZa61bAMJnTok-odU4j5dT05vfM2Lg8ydtwLgAYwoBVepMCbpnHVhN0IMMQBDeh20xcpk2IdzI9qRrLhAwtciewWpum4TbXWkRheZfi6wRPRp6-NOLYyyuMtmTPSSztHK9InwrR4f9oQtosmAYIFFBy-OsDWxeAbm0xM8WO_RR7ePTWzQkD0MhKZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIppteGbp0bKECZlAdET6scw7NDQTbKulz9GkK20X4eoURqXdw_rtUTff93oLGLe20CLvywBZTPjlceUuOK-JKv_23E0_EoWMbHlIzfszmHCh1wrL_xw2f7_xk1Kn8kXxt1PBCqrfuXz3a83rCVQg3w2afob3Q5qQR6PPVDoOWe-JMbbO5Wja36Mvd5CCsXnW7h033bGbSureHyCq-TsRzHUeZtTlUChsWVUyQWtBtpcaz-si2A9hn-wO6dErbo413C9m7w4QMdw2GcPbYye5xr4MEcpOn89yI5h4JE9K_YdUtUulllm6RiNisCtoYRNBvXG3GngwkZfSXNIFr9m0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8D4YZ6yK2qi4v3J1oD51_GgAHEbju4B910zxcXyTtpnEZhUWCNpsxz1u2Cb0_CxAUR_L5PqU884XDMKFLX2u548t5ioF1VcsfE2rK-CZNwB3umfGB9peVDsSFslaGywytaWVHZRjxI063MiHoq9aX2BGNYfZuZIIbjeWTNhmO7bGaZ4xH0jdDwX4YA8Ha88-OzQjLzrzH6V_Sc-hCggcIGl5ON0EZcY1aybBsU_oPNxMIZAVoGXbX6wy9U0XN_iztT8f33t4CfaHRVZvZyu2rvrdhOTVWuUc08TjkpTcyTMfMuVZFNWoSqRtbiO3VCf_r6mqT_lsmt1I-yL6cSlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWZ0MosR-4kSal7sO-OZ6C2l1oSp_zJxBxu66P7gojZpGk10wPBwCD0qiyI62Yjqjyn5CtgYKZ2vwvLZmkQGQfyB9jxQkiml67FMMlss73ERs_J2-Qt5fyKOsBc2BKiDnmvtKosSeVslo0Vgzuf-x2_rWuvmiIaDrYltVTUXfK1ERmTivYNYESOahqNHXMACTZDqm6EW3ODOuUbG6tdoSiZYONrVRDxpI1CympcCNUqLATHngDLiNFaWhwkUyAe96qT2fGKGAYppP5u4zGCQ-z-LgZArEau_AwzQ97SxPDeoQ5ddi3n2OdVhd8H114pPu3qhVMVIfyeKqH4EiQc6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXqLzh_n-iLmb7le2DGXB944GOiJRduPC5JL-8Vo84ivH9SQsoIJXmLBsD2NthLbIVk2So_bfgG0GVeCFX0_Ysn5MDYRg-F5wRFU4AE3zFxQlwAetGVNu__7Be6YsMBKABx-sovfPY5AdS5jddVR85IUmnlOosC4NWdvW9qDdpt6Pef4IvKEy9TcOE2kQrGDK51AZfZ22tV4J19KqAEAZNBO3XE2BwMIsnmbcAi7-ndC4RKtnz_egjaBPECuU20PxHtBU7S8Ugep9OTEwNEMOcdHTj9DFY9TqT9bzKG09tPzYzx1FT3kErp59nct02217udp-v5wtGDgX6-O6GSsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciTEOrlO5TQe3Lb2gnYyAdJqXtXbGiuQ6nf4PKJkdA8DszbGFK7MHwBrKuxkiSaOsH7TXu1C1tyCx33p-2AWtiq9gOF7M81NUC7kZKjjhC9hT0g2OxKjZm3OG-0Ck2P6uIwfgmBbBzMrr4T1XZ8nCjDNauNRWliS1iWwPEIedwI1LEdtZuu5uPr7JeXpnrJSSQ6HlL3QljLtqmTwZ1X4MPdjdqjXRMhBFj3SYhOG7jx2y3TPwHpy9byj7kjMunTfTIPTSnoAHifBRabBep2ndWrwKDqaSNUp1wyF9Dnyjt8_pTb9HbtdqoDEaX_ST2d-Jg06tv9ckTYgLkidAIQZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc5BEj_uTfC0hAPxou2TKuUFGijGuDbuzED82pth0B7cqP7mTvDcH23lhU1gr7qgkZBrFs2S_pqTyZMToxwYB57go1vnSqHLlb4EOVZSDlc2j1ZCzRsVGmTmLSGyLypaLiAALG7c4y8clncdF65YrpGmc3JLYiot-e6YzlYyW-6hVf047xt-zZui5CEvqHZW7jKxFLCzgR58R0-Mrym4PbP4NRuabbjsoy6Eja_qgUjJ54SIWoF9g45rTAOvT_bu2Tk0Xc7qi0DWurSg0_o87eFX_fZOwON0ASZtpvWR4dHr4hzCnZPbx0Iy8PZysuKJBSNd0krME-vYqPxLKvtikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vns8bLpdUZJpEJ2rabNoeD4A2-e4TpaizlLGpnjcsNXI8GCDo6PPn5Pmb4G2Va0a57nacslRILdnpx9chxhmhcl27Or-22fI-qbeA8C2GLtyND1PX2UQ2mafi6P4c_N7KIFBAsHZnHmv9MZzbG6jiSfDY98ZQC5U6B-DPrF8iAN8V2qG245nSmWhOb4GbrhVNB8EneynG4QhkS_rePQPxiAQN9QIp7IBalxwkiKai-JFS4Y82Ip17Crkh3ARiQvfzpA7CbqCHq88E6ZqUsBEfhuJgKKgZ8e7lGVVjmy2j0TElLefSG0awWJsp7yDx66Hf-J8c6PXmMGOCfhzFbFw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtabSA2iyjdGldPBcASITL5Vf1Dg_eyiPaMkvRJPk7MsA47w9xoba1H4Qm_xuiUuPn5OK1H2R8B42xCyJKHl0je3T99zWWoBZ_S1d9QhNKaZhNnMZRRI7ZU8pAiXX3Xg-npNEWVbnxPtSZVxyCyhhdmki9cBGC918rIo-sm7KreBuctAGO8di057GQ9DJhArnCQIeYo1xULRkZe5R-6UDD_fCiPM_SZt4i3BXCptis1G_6yEgoNrkAmUGzJB_Wsidj_FndfgaknIgYNL9ipESzVv5XxyIi3JyUGbAnb8a6GzJcSsrHqxLdwa9UyLY7zJ-0MGPAQH2Aap6KZLgatjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpDKEqBTkcJSsaQoTwnbaHo1tgBoEE-GIqg0nwLEO8tmZdB_sVMCSN3WkXm3HRNX7JGx_YOAG0QUv6GsfMbETvkNR2F6YC4-ld7dw1bkw4wHE4PmoFGMF-PFM4n8RMBpCNiEdDZazoK-d7pBbB3k4lxyPYOa-kMbyIoCnFCZfbj6UBFHSqcmCXVj5qQL-npKTf4SQdzjPOERmTsB1SYXaNTA0v0FtBg0tGNXjxDKdxi-uwi23ItBJR5zRXa9iSQtLYgHVGrU_072ptE5MFznFAXvM1zbBIVHmkXHwjMMfSDg7wWjv0BAgg25j8-BsjmQA_gJYaRG7y4OhoMTLiVZ0WbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpDKEqBTkcJSsaQoTwnbaHo1tgBoEE-GIqg0nwLEO8tmZdB_sVMCSN3WkXm3HRNX7JGx_YOAG0QUv6GsfMbETvkNR2F6YC4-ld7dw1bkw4wHE4PmoFGMF-PFM4n8RMBpCNiEdDZazoK-d7pBbB3k4lxyPYOa-kMbyIoCnFCZfbj6UBFHSqcmCXVj5qQL-npKTf4SQdzjPOERmTsB1SYXaNTA0v0FtBg0tGNXjxDKdxi-uwi23ItBJR5zRXa9iSQtLYgHVGrU_072ptE5MFznFAXvM1zbBIVHmkXHwjMMfSDg7wWjv0BAgg25j8-BsjmQA_gJYaRG7y4OhoMTLiVZ0WbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UioQEAT-ytiTvUeKY-pLg2SUwF7lpCmnXSVFrk-Cs1RKQ8QID9E4sV3ZQ38no7zjejBCR_EGdes81wwKXnIKRZfSIpdHvukcuoxyZ1VXBwK7nYBcFu4vZazJgSoJu5R2Rwk9F7Wgx52gzMwh58XFWYwdG8r3NzSS7YJzNSE-Oght6JJh07DqBwwplUaGXKxL8P8lI4VNEDEoN2uuylmLPQuepnpcNVyNZq9rrLka4RRkpDtDjPJKD5ujL5lAGjm3tXlSDtKT8olj1uWJpfMzNZE7VIabwJes9DDBKccjmTM8o5iQWDnvG-l2E-een4wa4TvEt7v941bOc8QpZvYfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7hW8nJU6fiqKvfcyk103Ib3TQoK_hoBRwd52BMKpRhIxS0nhivXb_TyGWVLC-X7wk9wFr3t8GSmjwl8RCdjgglM4RhNZO7sgCLOC45Q6w7nr0f50tc-OyodQpMvTlps-_8s3g-YFSwnAYAEbpv2nexCJkjqZrwVq2xhlIxE9cnKUv7G4225rSGIT2tMhrWw714N6ki184tT60iVf2BJE4hD-mbPzM4e50_iImbrTxQCMtmG72pIcULadZTLk2gtUfpUH1XCeniiwGlp0lIeMToa5L26a3sJ94HMx70p7Y0sbSISTrrBRsaBVVZAh_mZXy-rBsZyCRXBNzGYbuJlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfb1LCX6S-Ts-Ch1WLDotMguZRhQbaJLOgruFHeVC1kFLQVqlcp57nVpLBtgPB2GDR2GRB38Y_Y8L9ixXGwos0z3oOoxvHrOxMNcYLn2dOb0_0rvusNHb7m6ieqg7IwOGwXhOz2KrdVpoDdTiFt4RWS9szS-Xq40MaKGTX_OpBbDArMTRLPtP4CTvkm81tS6x3SvVe2OfvuhTm2vdavEv-lUe14CWsIDZ42mWFxdCoRBZu138Eg9G2UK14b5g-DevdM-NfS91ybXEEhIPuxn1VMB5YF-nNQSXJIhjZ8F8CpbWCe3qg2KSbKNO04qiovPgJx0rbO2cj9aMPrWQJ9aaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=TQQFC0TnIzcTFVm5rfAzNgbMAcmKB09O6wT0iBRdVNwNoE_FmfyP1OgoOHvUVylLm73twpNYxFgj4mRMPCqP1380oQxLEzQt5T-ccNsshVk_0C-mxYz5p4qQ6iDprhtD53ikQO8otqsZV7wsG4l_-2x830763T5Vc-coJrSA2pZJUk9f1DrXBUUAWM_MB4_7aPiGIUBot0HQZ8NDqqZuatJmaG1RYyxKU9Z6msDA9_ZqpOGRPL9fok84osiZI4E1kEb_htfJMQKlN7ZqL3v1nnlFqTCzzylp-Pba7MV_NFo5zE1vJjKE-biINT3_HN7CWpZANUz2HSF6kOPJPEU3CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=TQQFC0TnIzcTFVm5rfAzNgbMAcmKB09O6wT0iBRdVNwNoE_FmfyP1OgoOHvUVylLm73twpNYxFgj4mRMPCqP1380oQxLEzQt5T-ccNsshVk_0C-mxYz5p4qQ6iDprhtD53ikQO8otqsZV7wsG4l_-2x830763T5Vc-coJrSA2pZJUk9f1DrXBUUAWM_MB4_7aPiGIUBot0HQZ8NDqqZuatJmaG1RYyxKU9Z6msDA9_ZqpOGRPL9fok84osiZI4E1kEb_htfJMQKlN7ZqL3v1nnlFqTCzzylp-Pba7MV_NFo5zE1vJjKE-biINT3_HN7CWpZANUz2HSF6kOPJPEU3CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=OmfFcuTmG4yh_YC3cR-ZS5DXp8J1saOJlmH6sTOSGEWvgpY_0Yd-9KARiK3rJjX-kLXYlzUa7GcTPtzcXVyaFh-I6Jdi_7s_lgF1wVrbjLCLvwXoau1KbLLMgHkcg35o6EtdcLml4pj2DwjSAx6ZehkNIisGlVXlRy2-A5nWFBLURy4srcSQ9oX5j6rmyBEwlo5B12AUgVyQIVEU0zAP5pS1zjPxOAGNVfcDncAfz0u-Bo1NhVvrCVwNCnOJkoTFEwovXhUZqeqR_T5aWdW1sfn5HELI_whTGpKKRqNdF17AKappCxUnd_MuLJadB5qp2blfnCkK36qBQEGznjjw4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=OmfFcuTmG4yh_YC3cR-ZS5DXp8J1saOJlmH6sTOSGEWvgpY_0Yd-9KARiK3rJjX-kLXYlzUa7GcTPtzcXVyaFh-I6Jdi_7s_lgF1wVrbjLCLvwXoau1KbLLMgHkcg35o6EtdcLml4pj2DwjSAx6ZehkNIisGlVXlRy2-A5nWFBLURy4srcSQ9oX5j6rmyBEwlo5B12AUgVyQIVEU0zAP5pS1zjPxOAGNVfcDncAfz0u-Bo1NhVvrCVwNCnOJkoTFEwovXhUZqeqR_T5aWdW1sfn5HELI_whTGpKKRqNdF17AKappCxUnd_MuLJadB5qp2blfnCkK36qBQEGznjjw4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5h7gWzHIirfj3IjsvebvLRtb2x-RfifDteNptTNma-yZm1RLVW1vzfxmNvcNrm6YDlK8emHVFGa6wA_Dm5Xr1KLSjdDsnUXfQV1U9gRkWMtWepjMLMXS2dir-ODrLAcJZqnVdddl9UN_TOdF4wRmeDg1e8eq-gBtg3nNOYh00F6PGFXu5EkU55PgrR5GP3KB0SF00O7fTZDLupoXRVbVQl36ghZNvvnuZGYr2SjPt9-6bC-1sUJaSgxQq5NfR6U3bmPUikpHWGQYK93WCK3a5-Gm0YbCmNe2wdddPCy__JS55TXlrAojkZKPKfK_ncy299c6YWKvUdV3B1IfRifbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZWIWB3m_VmIjuGo3FpqEDN0d9CQ7w1d_tAw3hMweToXuVm5Oi4CzQR1e5-gYEitRUuKkdP9Jxbu7i4kRxNAaOLcb57Lq9GDlvTxWpiUNsSibPR6lMeASFi_hJqFaGjyA4BulJVQnL9xZ-Eltp2bw5bnnqZMTmHhFEOv0St-L83wIB-VA3rURrx_B3LN6sees3v8yp8ysHIpDKESlJVW9LUakYtNM888GTRIKdoTIsYrLPARBKSx8NqHVVpEVKY8q-nC602he8rWjKo_shxHCnwt50wQX-t3EIeupERppiyga5LgB6cTD5f9R780WpztVASN9j_xT3NMfHZagDDiaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPYNNgNCraYSSTMWrznKy0CJFa9YGypegN9oTr1Lvxt-4ljbClkXQPsMI7wnbhYgIu4lauc3r_9K0yb_2reC6DUtBcSYYV5zI4J8O4bsEm-AwNpoEsDztfQxiuVaQuDtO46bfWlIDSApLG_K7CO5RA3msxe309wrdUNyMGMkdJVy9PzjKdS7qoHt2QfbQyVT1Qj5vs6MbelFgII799S2bdpoZoEw2z7N7EG3M-PZZKyBhjkbcx35FzrcumUUKP7MzVOhNgGhpKj7Gik4ze8mYdz0QjUwjSq397dFLpSMoVX7R_AKm6aRVmyBRM1-3iamRWt3sPUPxzt2Pg454wExtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv1xOm7CZo2Xs31lcJcIqjQC58Sp_l9FXsCb3AKqYml1ZBsyxb2LGiSe3ralpP-jZ8SgiDlcsCvGRJyUABTgUImZ_1YAK5pFbFFtcExRTDfVKgvPkj55SVpgXMijGdsSe2fEl9BWUnm2cXbkbWivOG5wrCDPGRBnSs6cjAWfuRDNN9W7QnOvGDNr9IZsjxNn4wsEiPq0x8X1sRiUQd_I2lQ7QTQf9hRcK25ox7AXOWWmIRXW_-_Ic0smjzHASjl5jo_HZUlffG8RNsUtbAPd2RJOW5FdZisV64SKikMu-Sz-gsUzleZyis609s30XU-dBLVLAhwIpQo5F6heIQStgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1P7OeTaEIbJlYQKF2XYmSvIK6pI02Jo3rJE8EtPZvZ3Yln0tBwLd5s1i4gqAU_oFleUHvxHCs9In3QW-LarEO8MyrDhGU3vZTL7OeLCqJpZdMBCFKgGY6CszoqkiRtcAVzD8LuuXtVHgIa9O0H1P4fE5gIUcnigGFo_5rnWC6Z8jUd6_LbkJNBycVGtvP_OZhePj5MZ3MLMrIZZ9xxyHvu02xpav51H3Yv6Xp_GodVrwfs8PDrKaXylREKkJx8-fiWpIXOJYfKHfxp0-TOIJdqOFmMe5zNxS5E6ylaVdG3NY0PwF_LV5VG_mJR7MyHRdSJ6r2IWXACn2TDt7NrKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlI4H8deMxiOwDx_EqPL6w7GAoMEsuZnK1NjuEgB5XXTdNjp4O96QUhs342Jm2XPNzb0oZctbYTDwQwLZ9ul8D8DN0Cj38lXZNReTGFgzYyy6_GiCEtlKEi4_4btv2G3NIrOYiB3GcLjNfYxFCdqxcl3vz1BovdDvGMHzr6ifT_r3oWxtwa5pAyKYEc-6NWxDnFkaWbdbZF31-qWpVb4_nQiwwhG5JiqJKUgorpwZoES6ZN3masF5Mzfwjsfofxxvocrj7Y67YSpbCmKv5PkCWIOqjfF5-RdI1-E4t6y6ixYkrXOrUoOugbA40On12-qq8z2VdfCzLV6OG7pYiwjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHsZREU85i5EaE4YA0EFUEjzN1FxJXXiHaFXLHbrBWOwmtzmPa-tMHKwk7qJ50yYZBBPb1qT22jB6NzgUgQnaVS3_AD5uZAyYj9dpLr-oxgpSqTjKBbQvXyhDkYeT5IUXKpNDaHV4UY72oTVAy296h6BCy5TSBGbRJ8L0TbaNKGMiqqRl272jMBAHxEwC9-HWywFlt_NS0qcHDoeSvYeICLrxWDT7jWbm6orNrGrkRYzNTB8SPrzFj9aLvj0zYGGw0REFTikD-S6A83So0Z4yvzPImh4P-S5Y_UPl3zIoogwGdQ6VgtPcoh-wjL-YbK_jasuPtji-PrmaLafTPqMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn0blsPCrHoKP0LRg70GpCSih971IUMxJAyivreRN09vq-tfNHRL5tmInF_bpAMNaC2al2G93HHA-HUlPNN8Ec4drqfRrjfD9ECEohYOlyzKcQecJ0I9AXqBhRNZKvhHhfMOHl2Mur6ORncno0CV7nMLz7r2pnWrXX7O8Iw1YEsckmDDx2x3gbBY_tQkANtp94LPUPnAkEei7WI8AlYkYEDHA8f6lEg4kjH9pHsDyrANt8x0U7etG9FalT5rM_5bnDObDp16xSnO969PaME-Tk4Nexq67IATFh_2Erl48cbWKf6spYOUvFYuQSt4jwL65wOBdHPvz3IhXalAYjHOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJfGkHHg9cdRCkLS0HIlV0nn9vPxi8pbUei2AGf8qtN4i6VcZb0krs5nxgNY0SS63x1M3dARyjvXUOG6EoHKOvqg1Tfo-cbENqU_Sr1NhjB4U1gYe10pjY4v_U2JirMvsboOGdO0p6hfRKBgMdH3vCEJbSkXNButU6RWgMWAm2teYbRJWfKb2Nl8FQwhsSudjRKmBFy0j9PIMDQd0cGZkx91frPNwZezHIipOfFBLNsnK1zwpNglMW9mBGwzzuwe9_Qo7aR4H45XJFrHItgT2SZ5JoZFoYcBAGbKtrjGbLXX86rM0V8-jDQLe2VsppSZ8wUpgdMjYDl8Y04DNOyrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GckHkl2x-BpSsa4umHCf5MSRKKs8hNuiZ_0lJ_UaqiHq9dhy4-QUlDQ79V3jdsgRG7cumxnJFckE6f_2DfwG6Gk4cdzwdqr2Kd0fZmfsWmxJV3V1F9f_ouzpdoKj6ZZJunPrCTriSR1aVKBIL8ZE54omih_pmmC-HvEs4c-2Sw48U8WkdB1wWMitSxeMSGOYJDUQyw52fMq97AhjX1sw44_KU2CcAg7ZkPwfp7nNc1ncPXfl2fBYt06_VBW5vnZfpvo6BGdqXecwQHE7SWwLGH2hnG1ZYPTkQ8XLgdXPoVTC3mU-tJq7d6f4l8cZ3tv8XN9ecipuz4tdCAzVY1yrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoCcNa8ItnHx5_FcOb8V7Zq7EOcVqOiCXHK0lz1UpSEx-iZXD1BRI2b-YPmpo-iTuGB2UDXHYR2RfC4dPGicdQOCJrKxQ8s6SyDkEi61A98FQTQ1fmxn-GQZ4ka6bejhSeoUpITCUD64k3CcSQ9kTloCeeHz5C_bRwBtnwp01lFjwRjBJDlpJcPB409x2qdMCjVUvg8lFhzDZQIimOt_2-xZVYF72oUiXsPikwAxq7wrk-ftcFr7UYC7QdzGAcVAaUl145vJgO3Kl6ET_9xkfc4pG0qLJ659QBxHfIVmFDPCWeWUo0ZRdzKWJqdr_4mbH6nBAheDv8xsvVCAindbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZSKEl0IcwkXCqLT3niOAhMiTP3R59gkmfh60plXgr_kWMPVVFVWKdm7rmQqXy2uWuusiko2wyr10uGH32rlAlyNb_n7FUDr9V0G1ZPBfraQNpVFh1n6n81nWI67T6Z9SymU7P820YyfdRYdWGjrx2meYuQhU8IX-pki8JiG83EDMayT-UrREOdHgIu1-XcLziMV5Do8lwR1LtDMdbH0wjTZzJPZ3At1ScmU9wiDcNUQjt2kAnl9ApoX1d0xYAbBfSNri8IWCp009MBfGtpL6nfmMNmZcSEqrtRpCaCrO0KjtmgF98c7iU_2LMG9IsY1TfVRvBox2EhTFDdB9bjc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O568pViJOaYglRM00y8pvu19T9m2F2z8wzzqd9u_SFv2pGFBSsrGplST_22snM2CB_bm8CcMzUTZ0lqKFkJ3CAxpjcNRXb_SFUvt4aB5wRtU_QbnpsXlz15oG54RJNE7gSs2j1r7HeM1TQ-iazmjfiRqhKcP1vnmmYa_HeNoL0JSgDT2p8L7_3qvwRdO0JzklTCayBHVXxlXKDdH56pG515w41v37TTmI2t5JMr2KslLncfoZaFoc-3YTI3hLV96bRqU8L20-Wa54BCOZTaM5AgvWdZcLBC050ne_En9Z8crSSvH46nW8tvUnsK5V5LicJPd-9i6vtp1QZd2fnH6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4AGcJ8d92EJGUYx1FaZJtgIImoPEzyZzOMWDQhgjjHnl4h7taZHC1zYE6JutIechPetKKLw-mZ11pis-oszQCOlwUN2GBmRfknmpnZGCSX3GuJcnUtdFX7ZlJwQPQovXYUnhbrqg0owXu1mK5wrRBm_u1HQiL_2ZhGJTQClzfXMphiYC45GE20kjIKtlbaolNLHotS0aybQq8r9ViaYNUQTSU_-WaRKihhRdX7lWBBceLJcoUDBrK3AWqX3YLDdmgaK47znnkATfa9eoyMBuvowMH5-u9JOzRc8IYGp_cM-YJ7BGEqb3H7ZYrRMZh8MIJ0mAN460sBlXp-V7S-pcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2WV6LKOyBiQXNBDkapgT6dvUoxWjiSK9VIkerfNXedzj1eEsY6ugjt3yIHVT5Fo72hsW9GSHdhXcQqKRyBaRI8tzA2T93ijEwx7F7sM__AFIAjhzkSFLdZRfKzJr4ihU15Nh_LIW5Gctb9f1PLjsldjCC_pNghQ4PglBft6qt9364b-MbPG7h39nTQm0K-PuRQo_oiTECV33cIO1DR9XDRcSt4r-3Gw23AO96DL0zPNxMqcspiUsqd2HesL3X5U2iWHe10FxvP-aVplO00uG1rNwWC1kNxdKrGx6hpVgjknFV1vdD8N_UlIsrd5ZrX1V74mvfPSbHm_vFefl9tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reEGeybv0dDY8Gka6zsUMsdsdX0REHPdNzj569mMUuu6L3myQ4-EH4OwBNTCeC5l-4bpwl1El8bxKE9pxzl8m9PVptiuQVZXWCAIPIkmP_dEtua88V9HZcWTBiuNLkZGMVVlwVXBa2MWffj-QcdjMXo8Y_DgzCHlyWRH4uQjUEYqDyAerTtJ6DRWdfKW-scDg87PNmxHtxlkW6Rl07hp2pvM7YcsAwFaQOLlq_fmzvdH7PCHunGQBcSDLlQVC0VduazY3YluuhG7-tucYun47qDWcte6Bu2AD5hO7IrSS4Y2w-2JthV9fCqFJa_h2i-E0XuY06lYI--gx8lLi5Xyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3TfJR9TgDuzUHcLaa_a0qQB0AC4VxjkGl0xtYavlIhTXSm1M5pBn2Ocism-wuzFi9IEZkl0zPeLaagkOdm0RvEf-EpZcnGbUTqgJSsATW66PGs06yKMRQJag05PVy73gIgFmigHH2PdF5pxU6LoKT_Wc8dz8Bl4BwSmJi8PKE2e6A_UvdFK1h23_1n4oMGL54ifxNdJM6R_cgoXyzzVpYqzE5L22KoeIWldzZVK80Za7LNFOKDOsOjuvApIHlMhf5kgP3eSQiuzYzf_Nz8BRRqMD4KHc1E9XLFyctFyp6KUZNlHYs1xLgUEktLtrOEUSE7aiwqPeyEb2zFhMrkYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep7c1goVMG7ZlWl6ZBMsOIWTT3SGibMS8HNl5AhMOqApitVIP__g4AaB-54ulb1M7R6sdAmsZlBglZwf0UBBn3nxMPyVbyZa2AlwPpJBTrNSQ2GvIJP0ByDA6y33L9j3FmdzeTghU0HGjKK-aKFlnt7PBw95qx87rkLt1x7PQye5uHMYwsxBH9b0L4Qvc1HFKRkDBgmrYYKzRHRUZ5VbvqFcZa_6nmdhdZxvQAt_MJ2lp2aUwqDqAifV2V509xAVr_I1hroXFxPxN_RBAH8cQ3JSHx-azg7e9aPI1z7Hl1U39ZKu40_brvPJxwkM8KF9U0ciBQr7g35mvyl3Ya_H2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1xEoEkDNhjCqM9IrfjKnT3p80wkUg0FGJ11O5yISTZVg8Z0KeV3CFMo54KZHMCOACggJiOw_CY6U3oFabbaCqTPwnjyaXQcVMbvyj9ex9PfU135MOiURGjLjC8WDGTrP1NZEEC1x357FlJoaEFsDvp0YtFemB3AEjvZJVlQ8wUYjoCgLVlHyhDp4Wxw_1gqHgWbq3T4rWSR9C-5R2BFaOoRQnVFcNAwhApvRF0M2LH3c4TaZRtlGabp3fz8ujzL5t4nLHmCWOocfED8COLRz0npHMNySuPeg8h7LixeaFALinN32ikhxDOOu-1NKTyS9JQPDImx2NQR_3XV27PGzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuDZTKsN5-LyAGlFzbUs-JgbTslH3YHOTT-rmT0Skn4XpB1mNJ8nrohqdmxgMlRnaNOXBhxBfYTQHy5VC1DEM7Nqa8CyvRgGAZhJwtZFM8lE8at76QYA_sIsn-jBUA8-JRHkPGY-F6eiqImDDqXyRDNn07pfmkO86fGfD2q7liAQFHXzVUXYOa3drDu4Mqy1yzYqla3qV4NP7K8WanQd2t8xW4Gbm1wV8AZtSLVBSgsYtlpyNBY8iKd-UlALe5M7RFEWL1e1d5lugL-h04clad9XdUHs1jMaPYVepoyn6MSL9hTFWZbVxnWadrHR5KHyMgZgVL1Ar41LVxJlgR-Xww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLHjIDk5vRP6bZCyoDYyLHqm-qDq-lD-qmQXSW45hOMo_COX7-57OgVsrYeq18kC8Plnd7xqdNd2depD_GqwDL763t4vWv7MKIYb0LYmWv0WUKRAeE_65B-7yJ6AA2NjvHL6ufZUv-IQj_jNQTyiR8IZa7hQGCP7DJrTYX9O_z5XM5E9fVVz5BvmY09WW_1OV-AaXQcZL-XjN3BG5I4dPDPyYEP9mPatw9yNixTrZzj-qwe2Xhp7SzBl3X1RuOJWV_cobr5CLJtbPOe_B5Uc4RRFS3enOkJBXkiBDK_kiKCKK_msPKC0V8tSxooiPs1J9-XiQrCCa3J2hjEI1KlCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=vyCVrQEVsUSpqlX0wW4lF0lXCIXJEcDNlUaWRMKmXqFxM72A2bkw2UvLRweHJLgr6chqrJdT3IRTuP8KQ_94ygNxMvFnJ8WxIx5kkjMvCv6w0R8dMfekzJtYw9inYZ3-wsId45l-Ceg65eqqiZHozSbcnIaxxytqwR27ncMdMXCfJ5Cl_D-ChtWdtDMeB1H_mHxrE_SQkfoAENhJKSXZVeEwm_s0CsSFLr78upCThbkOWpfOTGsRKkc-AsX-tXD5lnEspi_KqLUKY_6Kpr-edqgEYwuvfAivEso5ia-3x8OogewVfYT_PY4ej5eDj2kPNQNB0AQHR3T1f2EFy6VjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=vyCVrQEVsUSpqlX0wW4lF0lXCIXJEcDNlUaWRMKmXqFxM72A2bkw2UvLRweHJLgr6chqrJdT3IRTuP8KQ_94ygNxMvFnJ8WxIx5kkjMvCv6w0R8dMfekzJtYw9inYZ3-wsId45l-Ceg65eqqiZHozSbcnIaxxytqwR27ncMdMXCfJ5Cl_D-ChtWdtDMeB1H_mHxrE_SQkfoAENhJKSXZVeEwm_s0CsSFLr78upCThbkOWpfOTGsRKkc-AsX-tXD5lnEspi_KqLUKY_6Kpr-edqgEYwuvfAivEso5ia-3x8OogewVfYT_PY4ej5eDj2kPNQNB0AQHR3T1f2EFy6VjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyMitWAO-CnPb5yJXhM9rou78oP1VwnliYpxELHrRi_Of04boqUtJ1UtQeWPh0d9x3RET2rchEztqNzwYHwiV9ydqJFqJByj3fntLX9_cP6DB4-9WvQZgiMyrhHsXK2dht6oZWnnDUecERDIgyYgwVSCFx6nGYYAWsDbR2HS1ksW9saJ3LKw6rxIdlgz1teK0Jl8LvVHbchRedYNqb6hLipZFnWGXuG-pH5wGYIv-4gUj1yXyuXqN-joCigPHZBUdkipGFP3lY0t3z-XAnXNYlHI5kfpLDyxbrtLHkYfFo15doOb6cXYjhIq1HIbx_PIrxJ4j8eEJHucOHBD0a0zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVuEo3MFaXmWv1C8lJE9_8intlDDFIgEk0K4XTFuEIpAeMQn7_3RPcEoWtnRtdpS2Ds1WFy-w8fgH07gf6XP57QWZL8orVv-0pKSGwpKzKHpDepHeyIzoTtbOmzpD886cnPXgJyY_o--Ec0UE2RN7qZOJo9Oj7cRcCoJx8MaB0nwX696ZpbgRu7jmCuHMx5e_YyjnoElT7luvewOGhcxCUpnfdxDZDoAeW0TS3orXF0xAJSN-GIsnfY2EohhQEb0y86KRgqwV824BL7v_FcDOGUpYEENWwTdzgr1XlTYJTI3fyI7wPaDd1bhpsBA0pYK8FdoRicfTl4M_CNiFzPPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYXi3tXS1fp_ZjOUa4N2GvFjx1Q-6NllzoWnoL8WcO8JoU0AfrUo20f6dTHpMAEuK_WjRMKCMy3vgBEp-HZSXTrITTvLNiD5VbgY5n5rjrKiQzpii2pe0EtfG_yycfqPnM0IcRUHHYAhT0u5O7pcz6sCrtkXFQ37xW7UFbvcachGgDEvJs2rQ45ETq6OvCr8uaqb6EtmC5__wdRZuC2vQQWgoPhteqCGu2tngnyvdEWNhZ33TGXRI4GUj9uA3ExWMyfQz8heFJ_qls1_EEBOD1CiANXsw_dtnFKgOVE8Rn3KDncCgpcg2olckoQQ3Ef7cpH2kSYeq7DTQ-_VHI3q_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agQS85rjIlcPsnmVPqFQEYtLbZy_C3Ej20m7kY8VjajwruszuYoxAKbTWEql9j5Rc2g8lx0OMriISw0wNx1AQOJnEWSejTWe6XuDlUA2-BaZvCUemZs3chWTsho8vskO5ndcmN_CsUmGxdcJztOCmIKv12Bv2woLrPVDBaEfKsESrSdL2d90eqD0kBHBKgPkO_v6Vn41GvtyoHiPTXUk3qRsWVH7-z5A76hEBHcM115Gwb07HPz2A4YwSl4oWKaNRLgf5sa602d4EYJYPt00p4X4djp7sedWBsdPMckR-0NWalk4UvaPwEWMJRuIL9XtKsypPfbz9xMua4IAVmIjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhqCp3_CTbE4UNiVOgKqO1k9DGwg8j0aXoiwa5kupwX7UxxOoa-uMlU7CRl9Q1B3B3Mfu8vAbOWOmQMShBRMPEof1ybB-UVwz3i2oWCbr5bG8Xz9ifmAGhktryiIc9yCcz2efq2PianjTMNNEJLiVD2RY5SGJqCYzA27hbTt3pc8kfT-D8h1vtOuV2M9CYKksn-nkym_COnM5UHE6Ixj4FQoVOeIaNtPohSIbBpU37zbnN1b48-fBWQk1cSqRzk1tGTyTXcF04GZBCZp3aZ4Bcrc7Z4KCuzdo1THevj9w6yyMOb1eB4etXnbbfe3pNUk5wJH0xaAZ5u6hGLGsktGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfD03dD493HjnnkQwv4xtJfenbxLazLBgCOZbUS1TeJhdYXWUvugDsUMKIqNdbfAcpqMa8X1DcDzeXrUgE2APFsOfslGR_iCY09xHRDBpskpXEKjcJLN04MQ_agmfrnB3yDVZU-guEfT1T6z3hSiUtELA_wN9mWqsUwnXW9eUvxUpl5LvJOwVNy4mGwGYOTpGM_l36bIntqpGMOOUXy1TiI1nLRvsjPRWypiSPl0uKSAgcpYOiwONk3x3GRXGUZMzSmIuou2kiLHp8cJ0sguVb9QBStfWthjw5doIfh8Xr4aD2zwnop0suEvi8TRjbzW8XOrXagsG11MOvDpSY11pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqVdQjJ3gL6zFi1PUr60_K_wpfzEUEuoYSIutEpUp9z43G_aINHwkNffE8V4Vqy_mHl4BAcVYOu6g-x-5sT1YiLX-IAds-EQnCUjaSGSkywetcKUOBunyVKlhmEha69QYKu_fYHrCmhhHJRS0roRKJx2eJ2PdWpK-Z9w65aH3PEC3R-H6p_4D2y6KJCKJ0BEliuGUdchyYw1zwWFXTvh5Uo_URw3fnluEkj1qoz3wDz_81KnQQ0w7ZmbMP-W5sFzOu7onROIEP5LMZW2J2k19SNLJDHO7faV8HVWWbfG8saNn56QM_TQ8IuxT4pZvGErXVwsgkNhoUkqXnnbnYJvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhSRnlhE9NphcAcZJ5M3-fNSiwvhaM6KtjYYI_e9GgYHOdidwSDeWCU5OX3sx8t_gwAF_T72C5d3n5W7ixSDZfsY9XV4XK3bHMCBkvVLerOfJogpqPqskzbCWotOJA-_ud_6d_l9DxLzgZcTucsBCwt7xqXWFm594a_n5KrieDBf6TOp5Kd9R5fpGqgXf2jQ_0V2dEMMMRxNmWAZmrxtPdXl6wvFW0nud-OiyMrfKPtDKCZC79-95pwwvn-RIu8dzyKbKUbuf_RD9KRQJgzfvRZql_j1ureQf5v_yceDUK9Ukyl9VUiNukO6sdv2Azfn3S3gsRzNA_-kdQwiu_DqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=WPlc348D205uaaVB9QvdG64qvPpKBhdsmfU_UEQ3gXvTOX15TsMaZCPQpeV3ABIRAjRElwynr6i40tiuXaOyPs4prEtgFg0P_oHkPCWhIu8PJLRorQfrdyWW0noiabTe0cFK4KlUk7arY_zurVB0xvSd3--vtrIhTIqzRzGqgIKhhRJXJjXaWSzuaIe4thIn5vPabSRIQE0ETs6LjdFJ2Z-W7E8Le1nsJ1l-NSwe0KEAbZXIVMYYI5rif1f4CWCnL7CF6Oxb-IwoKDNGnmzsU2PNn1BavcJ5FqwmOQW1xey-aw9cAM4Gm5fOLa3U8JXkdJWTecTG3QbkX3wMQvEhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=WPlc348D205uaaVB9QvdG64qvPpKBhdsmfU_UEQ3gXvTOX15TsMaZCPQpeV3ABIRAjRElwynr6i40tiuXaOyPs4prEtgFg0P_oHkPCWhIu8PJLRorQfrdyWW0noiabTe0cFK4KlUk7arY_zurVB0xvSd3--vtrIhTIqzRzGqgIKhhRJXJjXaWSzuaIe4thIn5vPabSRIQE0ETs6LjdFJ2Z-W7E8Le1nsJ1l-NSwe0KEAbZXIVMYYI5rif1f4CWCnL7CF6Oxb-IwoKDNGnmzsU2PNn1BavcJ5FqwmOQW1xey-aw9cAM4Gm5fOLa3U8JXkdJWTecTG3QbkX3wMQvEhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbAzGw4T2I4fqSfz25dZYuQL2yvKDiD3QJj8qZK1_4fdnnWElXxQMft2TJaVFExwAfSPpilZmNXLWs8MZwUYo_0O-nn_acW12-Si1jU3GG9LngTZ_2E1XUX2XO0CVcUzgFBDgEPSuLjqs3YyPse1CVrVw-uVAsUHpJqRY1pDHgcsaZZOM5t61REZuaj5TE_OjLjEDnI3v-qGv-q0IiKQ6F2xjZI-kWJwCslgAr9fz9R_2v3T48CCwUiFYYyzrQDN47XaJYnP4NmVkopPBI47NBwUoNPxtTsDEooUctdlQ1wG57SXrrZEBtxF8q7CTt0vws9IevZJnF0fQEFgw-ELkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=XZpAYOmhHvCPpUFxL1t5IWtQQ-UtTgs1z9BC_RIcC1LulMfJNQYe0oMptHI_hJoeFIrcptM9TxI1asx-dbPT6FG1G57gAS35a9OlQDEZC9Od3abCRMAl4T9qwS53Qfh3hxSXD_5-kB3euOw3v6UmUjNjQ0k63-R2dqi6AqsshqsCuxVvxyfLf-bnL9NKUqPtL0pFsXFQZLmIfCzoMluEU-OL9niVstn5rWEnlnwvuCGIode4IyFRmTQD6o6IMBS9QqhkFU_ZYGDfy9u19RJS6-0orIOmqIcis_n5-ewrNZMAUjoa50RXR-QffZiebaOeYEm5s98L1EoQg9MAiYR5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=XZpAYOmhHvCPpUFxL1t5IWtQQ-UtTgs1z9BC_RIcC1LulMfJNQYe0oMptHI_hJoeFIrcptM9TxI1asx-dbPT6FG1G57gAS35a9OlQDEZC9Od3abCRMAl4T9qwS53Qfh3hxSXD_5-kB3euOw3v6UmUjNjQ0k63-R2dqi6AqsshqsCuxVvxyfLf-bnL9NKUqPtL0pFsXFQZLmIfCzoMluEU-OL9niVstn5rWEnlnwvuCGIode4IyFRmTQD6o6IMBS9QqhkFU_ZYGDfy9u19RJS6-0orIOmqIcis_n5-ewrNZMAUjoa50RXR-QffZiebaOeYEm5s98L1EoQg9MAiYR5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=qNHO5xfCMf10-OL6Mv9TDwoDL46jEs8xMzOFc_omD-WgEV3G49RTk67qskdULNOyjvUWq055MjtYDKMUEZvoX0uDg13BKvJvzkSMFis2mVQHgeVQtkswNGAhinI86AM7wNdDBU9ldTJ-VZgFn5R13HX_TZ9PWavTv_qQo7xAsD-coEnrMsWvXT0BYEDt9P0m1UlbJVGpcHPFBAG5HjBwB_4VZyGwijMYlPKHwX5YPET_Rt0SudQdT-RoUke84kZi0vpXJdX0iWLL_PzJSy_tH5a3NmWEML-eXc1wY-DsjhIfE05pLeT4t_O-r9rjWAncdMaJObDEAtjkLZ5QBogObYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=qNHO5xfCMf10-OL6Mv9TDwoDL46jEs8xMzOFc_omD-WgEV3G49RTk67qskdULNOyjvUWq055MjtYDKMUEZvoX0uDg13BKvJvzkSMFis2mVQHgeVQtkswNGAhinI86AM7wNdDBU9ldTJ-VZgFn5R13HX_TZ9PWavTv_qQo7xAsD-coEnrMsWvXT0BYEDt9P0m1UlbJVGpcHPFBAG5HjBwB_4VZyGwijMYlPKHwX5YPET_Rt0SudQdT-RoUke84kZi0vpXJdX0iWLL_PzJSy_tH5a3NmWEML-eXc1wY-DsjhIfE05pLeT4t_O-r9rjWAncdMaJObDEAtjkLZ5QBogObYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=QhSHM8VzT4Nt-tQX-aHH7b2dOtITLK8qwHgJeKSn9ggdW2dfBNtqz98D_MJ_wdAeeznri4lzv22fLEZt9Gj6OhkwYmCJoUWx6KseFmbN4FYoZsBcuexKXK64mSkA0ZCzcbUMLHsqDlkHenjxzBjJqgt8ytR6phSMDSb53D82g25y6mU8g1MdJIVM6JKvwKVROqoAnk0vnFzcGFnEsdCUQgXpkwmYuRAhcR4AFfHDz9GS5wVYBNUYlLR2dEx9xCVXBJ6M36bjwYcvPfi3jUqk9EfZDunkLSA57fNxej8ySvX6HcLTGTygHyxoeZLE6wMucDirORKd7tINHwx5WtqKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=QhSHM8VzT4Nt-tQX-aHH7b2dOtITLK8qwHgJeKSn9ggdW2dfBNtqz98D_MJ_wdAeeznri4lzv22fLEZt9Gj6OhkwYmCJoUWx6KseFmbN4FYoZsBcuexKXK64mSkA0ZCzcbUMLHsqDlkHenjxzBjJqgt8ytR6phSMDSb53D82g25y6mU8g1MdJIVM6JKvwKVROqoAnk0vnFzcGFnEsdCUQgXpkwmYuRAhcR4AFfHDz9GS5wVYBNUYlLR2dEx9xCVXBJ6M36bjwYcvPfi3jUqk9EfZDunkLSA57fNxej8ySvX6HcLTGTygHyxoeZLE6wMucDirORKd7tINHwx5WtqKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB2kMZO_KYTY-eIM7kIHfPOh_RPCHEIWWIi-XypkO9DP5MpFF0-B3qm0ZY9n5kKA0IUQO_dj9JpN9Z2ns89rxExFcIEsdHmGnWyQNZUO07CiUFA1qnzkcVByMy-6cJgiW9mYyzpyHHJUW43GYhJC5A1teteAezfhd5pwtpin752kTESdIOgn2bKHrrNyTlxv4UpfBbDSBePfCLWsPdWW2k2sdi9GCFXOe9HRXKjKVKZfIJK-irxGCQW9pejkPIxM3ou5aZhn7dbgqKMwP2kZY5-x3WYTi0ZccRXiHy8p722F5FibQfgtcU80gAie6CP0mwEn910oTjFTrZztyXylyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
