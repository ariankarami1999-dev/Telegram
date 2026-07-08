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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 18:23:08</div>
<hr>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFgdaa2H-cf29WByl-aBmfAkGI4sqyuX4hqxp6p1ulpzWXdwSJY3WdLBWZDJqqFKIooUHyr558l-WkFcCmkwe4ncXdGwbl8dP-CGn6-fB83eq-zedBCX7KiG7V4eZjGNrqkJkdtDAFQg7mfwTR3aHwnnqdF4p7Xfcnhy1tMCjfk-0ZaWOWw998oNs0tjWmgwX_Hlda3lp0bx1Ge9ekCsljxwkmc5o4mRt7PtGs19AUZebULpYd3u-YgS-skWM1E6vxTUx7ZJW8Jb3FL1x5Ou2Lt8kkbLrkcd09N9cxZE1Hqz6CnnMfp9MO1IjYolfErrHzOzQQr1xbG8GKuof-iNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFu_i15RVbGem7uacHCSrGVxoNHbDWoG6wsFlmMhhZqjvrCLilWpwE_TPpoUSK4zjZcuh4JmHeLS0e8e1Ch4dg4JoKG5ITw9al3ng26zzjRbHTZkGLkuAYiaBrWlQk0ZSH0pv8gDVR52E06ANOnfgVGw8zNpLCfuT_bhGocYsgM1jGGaaDKiUfTO8mds0R3SjoyE3ddN4EaSACbRE0rRPqrJIlKaShXh_w22psmZZ4sG8dYWHewTU8_359gBGGC7D70FxHIWR7x1HJeUKGhDYcbveXIEaTrGzVJZCj_Pj-tYtuiLSaf1OD9N4FN_qftwkYKM1oAJgibh60zBXGpLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXQcSvENmcRPhUU5W6GIBgqZjSpPw4qlqUcKJD6Z6Nt2y-4xwDOwQVup0gTgurw9C86Q8juEmB2JpkaqzxayJNPUaZdXGI_r4-Il8jpNdCKfDhRcz1Mb9KhOGbEidyojrbwtqAhSvxZ7iwNh0rLaZ2XcjONvaD83sRGb_ew2LUok3zBzorzBxh5LeBrqCVoZwIw9mxTdmQG-CyZGQ4BxMSgezVzKlZO6rpWmwQRXUdjOgb7Z7CzwzRIYTRq9PWkGk0PdDzczShdahBsx_7c4AALEpOoittUQB3U1gXsjGoGICyMOsZgLIWWS2CTxSgLvc9x-wlCx51NZwxCbOt1raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmLEzLfq2Ffmo_v6i9vqP4YwALoqRb0NXmvdXVsd1rz7gFH9YyD7OJGu7W7qcRV5CFJXCTcBa2rtr3vN4eHjjbsZSBuCXq0Mwef2Bmgb8yamMVLcCApxsmtVkKj2q4JCUx1dAXTx_CAp04UEerL5YBq2aJ2gkujHjyPSM2OhfRwbbZAOheNvs4AF7dyOvDXHxCUkFnDAxovmsSiYgy1hE-b4zkeLdXi0mu64HCvzwBk9w8PixKvBMfiaOslLHLpvOg4FHTY0erfzyqhUjknRXNS47s74IafN8mo2IPJ_TUNxC7uLJ6mp5Qf-v2cPLEzGxga0xy8OMr08Z99TzOw8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL4FweE67FhSd_0ASIVCf4Y0o-RYIOcVBHSLD4D10THtu7C1qnNQ1oppj9yZGfEuKEdSy11qkywJznQ6CoYmlj-lthyAQDJ6BB-IfooIQEk2TdBxRhasw_CwTlaA1uHtkp0w4Myo8CT5MZTObbxxT7j6aRKpQulOKlOQV3boJmt7mWyxICohY3fXZDsxECrrro_x2MqAc_smGm6Km1t6jb--IR9vP6Of_1V5vnKqNpkXfIWZAzh7NFqCqs7xpNE5f9ZK_NX8QyKMLzqodvQgxikjEh1q_EOqlM7SfP686MXMOVT46rSfpFepEFFkiVnC79zWPsfiC4WOdxnRoqi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASoU7LVcxUUnkYHU4fIdcQSVpbsuUr8SUpaQIUi5cQMrunjmcm3x19owsI01gOrHdaouH_reyZoTlalN45bDLziVy5O1jVub04MbT8NRELWDtulN9X7x9EI5Y2l1ksskp6g4xGYzG2uYwKgjYB8gjTEBiunwTOr-G1JYd_oUbqQ2uGM8WBabd_7iJqQ-85dYBF6z-iJn1JggXMD_BeHa07-vnPLBob3QcTIl0xOJqL6xO85hgs5mrr6xAwjcV5B1oUiHDnEluWUnhDJNQ9fnaP5_M0Ud-LR19BdQJM_WL8suP0sZCc5DdqNpEGoP7BuW2LWyCj0M3EmsuSWzDqABgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9DIiwd0svz27YWzjkKRgQvQaseeU0v6xxjntDqr5XUtD-Y_1Yk8t5RvNxvpw72ARiqsZ4Nx6VDu-opeV6JivaN70GjUs4_uelvsX9JaUqy35iTlE-GS7VNdLIFGKID5k4LjJUqmzPElLj6tbQgcf8AarDkFfSOcp4jboV2gKmgEOaZzgKPc8nSGR-wvkhEr2oKUiy32R9LG-Y5j4ut8LIxohX_7P9IV6M8Luo2eBKT90NGc2WI8iAnXp2urUekgxymL4GaJy_X04BjJxFZowW5vAvVRPLxjyzqbpOmPdrazVL03RoB5J9scIKITDgQWtXj-Gi3FrYRgVMarm48K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1V2opBIAWxDbcJ4g3EJYZS8QkMzxKDp1MQNH-EzUFPoK2r3rHDqtzPpbrkP3iLj7Uuvrrx7lgF8VQG3bMEgB219UpFWbQZtKiH794SygQEUkky-fH-qjelayq1h9TblVicTL9MhSdDIgd2RIjVA8AfFzbr94dpYKxkc73fhB2l00c-dqXqO3BLKx9Cl24BpNVQzemMfrFWEh3eJRP6rl6nfFr-KC0-BxbYrG86S_IqYtN4YeVvWJUQQUKk1Eac6UQ0kr7jznXL82XOwWhzsAAXLdIT2RmD9q02RT_p1uBvZZUmPMhu8w1dskhdMxm4mqzhraU5KI4vl-9K78WvVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr0yR4aeKeOQURdfOiMGUokdIVCwaEsPryvsSKXU3TTG5RJ677R4szkTzJwQBn2cHojRJERvrY922Rpx427yKuMGOSbHT09kytSUFNEkBp7kBklGizEygHFcHEWJgM5Kg0EzNa3w92aVk_LIIXlyARNXXkVQ54ck_7ucY3aw8_LvEAuMiXGx3b4ZAgbvCYQaDwvBsAWN5P7UHGgDAIfVHgtXCfrZVoAmQwiKI7nW36fCe7kLYLOSh441UVNCrKfZHGPBs9FgTTP4d_ZqEnLnlq1yc7X13-0PFIa_KQGPRwSsAoYg2SDWc3bmxH5FHCEd3RxVchMAF5TApq92EHw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaLAh3IiAILndiyJe7PwEbDpE94c_J2XLsZCvdIzPQNEHPXtrH7fiU1Q07qk43mCOam_ylQOUzyAYr1azB8PMt1H7yNtACJT5z-WDnZQkWwD-CgPlHAz6Pu_nARwKGkCBUrpYrVsDNZk_yy02zC4jTULpAz-J7NFyvXOc3wG0r_AjpZvk7XZ-r73h1--9iFPkSojYszoARzewpbeKo3hyfylRsAmynxOkl8WvvUxaZf8XEAR8kJSYiCSGCekQW0dX0T_fVg3_0TYjbcONd9hu5sW4SvxeaYCQgUjJWj64QTaGFsTMXIYXscBLUyW3r02vIl7ht1ynWEwQezwf1W8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Bda7Hl8nl-sQFy3N62aHzVjlBhVgys9nzN7GGXbRljVM9n5nTJ22pFU-kLgDCs8e_A7bEI5b5ZVfEixg_p1S4g4Wd3aI8B_FTESbdfbriy2zaU2LqkJJsBwbQTtOIeKyRl2xiil0AdgAoWkT4I3b8Qeq2F3z35WZZq9GDBiDyq5GOj11SUe00PSzwpjbGuQeFAZ1ppPNNcUnox0IJeq0ESP5XJqr2bsIB0t11fQ_E-2mnWOL-Hecjyzgn89ySFi2sadbbCkdJaKZ1AvZDwAjzxzV6t7kfJb7N8_nMGCYdHFSaSHHi9X7OKsGMy0xdZTgaXs02oxd4iDc-bsGUTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CflROHh8yk50lUIQpeWZ7eSVcU7WN9XbHeFzvTKj_POWXCo4GxY-iriwiMPkpDsQ2no-0nxOYc-KtLxn5IQfz4b_e82fwqi8kL6eFIcivYYyp9cXZ5KHpWqEh2ktdexTwt0nWYfriKV9lMD6lF7WQq1Bp7QQoyYxXaWTpf5-BPILQ4nWI63dqu6IbNJxt_sh0e6zCcQGCrg44jAxXHO8y9cgFIUo-IY3RSQhVk7xYoj_3IM87XHXcibPn5r_XoX9cQLKflCMkxcTzdTgJEjD3aoBbRtoVJrKPaeSp6kNHqsYRGSX4U7_HvlBjaa1Wijy59YfGIzpojP9vaWO2NAucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3EqiKjt8VrOCgmuCD1NXFWhWs7hm-b2D7v5W227kQifFCZhjtNnCdEtNMkgRjBZ5g2WU-2Xdd8H-XX1idyM08OgXAtolr5xkirpfV0J5Ufb0I8nyg2s_ZpNQYNwvjI6KDF9yw2hIzREo3yshNVsMk_griqwiufpKSpqmq4Zi7mqwkB-B0GLqMlMzznhpVO8CbSgl1cARObypYnq-YichtfIl9OJDo1w5jiABHIVUrW3hm_a66oTU5MAXo1ir9p-uA9V-AN8XCt-MyTStWsDQLyvqn8ottLk38tk9B-ewB7KthxJdSPxdUyE5dULIp0bFaKXhqhUcWvSzenVBVXZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAfckIPctkyuNfjN-WXrss_LiY4JzQt-xPa7pTtSq60VR_3DRnUgDarTwoGvTX5iVO46uRlCZOBhEpd5zAPR7X4JvnT5SG-laPrmkQbdg3YxNlIulMv9Wz56C2RHp6xIk4RE2KW0-pN3nS0J797KpUGuH4i-ERnt-OA89ogS7TxrldQxgUD5VQ_hhe3cpqR05EH6DzBEqFWpwoGKAiNW2Sq5qWOge_62DZG45NSQuC6GpOoO8fXgtn5sq2Fj4LdTobsYOO5Wfr1WLtwFBrs7NGXI_NuATZ7G-ZVoBDsNioUp1PnUgcUbYDEfgOQnl97shfkqhVSdRROTwvxqkBZz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJtLX453BWhRydlUoN7GE6dtd0xqofIjF9iwImSPsdtmTqDA3tK01R7synRu82EkxAUPbJ6eK5L_E3xt8Nayxz4_rTfaN4_wbgh3CRjfPjrEXEPInYimoo3fg72LdXYvfE1Wejq5SYUKCzMg0lKkEOSM-CWc5Vw3DRZjudwGH-VkNmvQQwCZ7QwGBZ_FwKzwXwC7vsrQownG6blwP4OQ4-r0GBLnH1-pYQ1mKXeWRs-ZJ_oxz_A2X2vb5-wffHxjNjjsEXyyAjioHcX8POYLyQdl197c701_uK7Q7oQoq0kBdrFhBikcK1oSyi9piGXOaY8a2j0HrPSDAneNX4MOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiYXOA2ylKG2Wy4W1r8fnbRsEtNo2r7YM0T-lUoMwR24YId92a8ry-ZrJs5MAmVuADkZl3BEoTcGiSXKT0PuoVJq8iyMSpR03bM3SCV43rSSpNojZv5FKXqpkJ-LNTY3k5ste-_GCT4R0yEbQr5XbIV_ucTa6PMTjL3fY7k66L6XLEr-K8Gvurl06CNplEdUanILVe38XlUp4s6Pj8QIWKcb2OHvKD9mAGelPFUcLC-EG3PNzyxZnIMCf6SXa06ytwpe1xiCevWUKuYF63dFNuSj7PCAYkTII5JCbxXNxKBfMh5ngBP4DGoqIFrUWQ46J1GOM_nx9amIyw_G7APW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU6S_NVN0UKblYyH7bn-sXmSDYU60KwpzfzvpdJfLLCK6Fa0HrDQjmaSmh67PypPxJhNgosh0wNHnmjNmSTYkhcXcvj8ND37_qzeUA1_NmMO0PkUn7BMhcRqiuPKkKn5vX2u2XS-7chaOcI02sIbww7NfyH5b7Gk2Zi3MmD4D714_fOkyzQbsF8HZeXh8W1wHFR9jB_CShNlj9t_FYDZDUytVjsUzkD9WIA-9sjzTJCzI4ZgQf3kQl3tRMJSiDHjVpBrf9-vcBGx2p5ApL6vhSrkqu1sgJ0-KSFsUaz6UdoYKm9UevQFwZ0TLL33vZo-pCLufM3UiDOTfXVOiAYN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKoJDfkNM9YMycimxyjmKBe16hXn-e912X565VyutQ9lcogeobvsjulCBvY5NKzgjiaXxgd--ucDbzsnp9ZhvdCAZzuznVKH6aZu5mVWt0_iWheakxOrkYSVijWs30OslNwZ8sGsivxLta3Pb5YTgIURwvesw94Gn6S5O8T6y9erM8aLBW8sP21GmSKY7cuvwpnReLSMhiC1bMIc0NPuYBRi-i39hBNO7xl6ypAUE5tsnefP99KpYvSndzlJ6W4fVnfXUofphuHHgMzqD6XR6PRoiHTFg0_sQZ-GN8BotU-ZoB_WP5_p4oJZKwH8l0nsDjTayAYAzQGyp5b5qiyOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX7dAYG-dlDXQb68RVbpFpRwV4pDji2Xfwxj6-j5WoutK3hVWr6Lk3RtUQ9l3BbPSdAG__LZwOqnxyicF32zQPecqac0Cv_dkPgvE7guW9OcFewnFLBFFJp-M2ZqqmghfZRdCyDiavvBbMUIzAcm4g7YM-8n_pkHVSwxeR1QPUN2G7TScnJalKecTnaCX_3_lT61YOKwSPNiaSbD5671hiYZSFvVgxcRxaayHrvWbgQnKPYOSae8LdGCDAxdZk46vElid4YrHGZonUjvbW24k_gH7bcw472Eu_4j7wa3Vg3ltWJk80DrF7Jb2EGAzePMqcTV8KvKnS0pMB6q5ygM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtudsIWShVTlevzYBiL9DYKd582-B5AbFukZitfH_c_n8o3IamcxNW_3FOWRc11_IWKpiRQ_QcZDxZ5-PAtqVKA2uC92BBCP97hI58vHqQmUwiOVJUatFuLlZCAfwLobVBH2JkJQUEkkQYWHeG7V0x7CFHHfEhdRIfNbLrFFkR_ymy62RWoSABPT6vlwi2H7ZKePpkKtANcxbiTZzcxYoRIcfCD3WbTmJSy5FvYo38BeNybuAKL_x09kWE8yZSbYjOzxuLsJeSysahH9uo7vKWvi4z00EAKfLUuMbJ4f98BZF774Wr4tRYbqmzLX5IZpt_FLIhlUg67GZFeZQ03JDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnRBgtTP-myAywUlkTRCFJLMk0iHnG5Zay6U7z596U0p3NPsOD198XgKlpjctYW16i1_FplwAfoVonAj9dEeHL-xUxKWbmZL-UhVYZNlYAhMuyoaA6BD2mefxGrHWVS7rmiyq8h9lKH9_oFGZuhHe49LSxS06RLok1SKwfDmsqsLJ6w4OWzbW9EqAPxYVNk4gjc8kXl8v8URxaXsn1k-7cnxRbdjmyi10Ia8EuzsQ0rpf0zitcDMCKxxkA-IFBaZaShBd5iUktF_-NziUtBEGWYYtOToA0xqULKx2O6bH3G7QmlR27krsa-z5Ihnz0elt-SlrBo_8wgRr9-DLVV5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr2ZuO1VJmfBY7kDP3NohOOBdVAFpEhAoTDpH4cR3vreMSTe5uMMQsn-hkx7dX34nEDrOnktk6t14orfJLjSZNh0F7rmXNSyboxnMFBAIUNgZTjhjLxecaI5r2llC6Imfzbr3-U7Ou6OHt8bX8AXPqkI9qs9Nl-2F4kcmtOV4xDgQhCbSpVyTt5hfSvRmCwHdqiHVKGBVLpRbUWegZzh9BFExvyr9brOQzppyC-L-FuQIrofgSOYhOh9IMXOiyFYV6nk9aSOYF3wWLEmBCLyCHHCWfHO5Jbyl3zS-AOIFrPc3jRgzyEAUSb7Ct5LMBm6Q7CW5S0XoTVY95eWb0-Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hOwNEjMZ3j1CDvWcLj7RpGfvXYe5Rjut6zT_AdEwT839drx4MzIMg5T3NW4WvKCvMP0on_9tbotO7llIn5KVefsF9V6hoopzEP4pm6WwMaOnggpDPUp1zIseemb9ak3HTd12ca3F4Ziovdu-rj7L8cpSyyvIlsIRCsF37eXaXhGODabvgPKsK1BeAzBWgM3e2EyR2EN67qUeD7eoYSEvXzQWm2ZH-7XMA-9HgAkbUo7hljdgcIxrsMsrJpd2XrhO-grx_WByi39dfHYiHZTE33-JqCRxvkyv5h_SKt85iaYQD2YfETS0Ov_zxV3MjCn6fmjwxiK0WlCKLgX-ILTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7J8KAAjmOw41nFZ25kL1CMmAjdsYPlBzacskJxPbw30tapZiEUmeAmkb8Jm7BinkXCrEwmHwlGPcJz2kwcbH3h9GVfUGac0gNqJinhaOtZlVTJeLn7gIdhwKG5uxdR2s-xYVCaWhN0gZ7HC6GX8nEyk2AdzMdOzslVr6k1k2di5IOvbUuJwRuHbPywCSEhK0GDK01151W6O6DcGyKzk7DOIkApD7BvsHVrWjcgoGyc4UV79AOfhGtoo2PztFvV1SwKf3NCRaR2yqOKFdqFIo9nUxcHqENaTKWh0sV6mtgAwlX6E2cBr6tPM14ccnr2QoY_oA8XJmxg64M2NxeE_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swFRy3RwZB4q-iyI6L6Ybh6iaTNnV0ES8Et-KMxb_d8DpeAGh2NgseZ-VtUJCGzF28nGl2VrxCV5DxhVoFvz4X0R9oSKPzNVI8bVjBRb89LmGCiLUqeTH7oFAZbUOZoyz5xGhJ3hSK4Wdqh4Bd13JnnwUGT2AvjviFqv0qBhhIfI3WMRftTKtqia23TdJ-jSS6Ii9SR-anhW1dAuFQFWE1mM50xcIm37dmm_3TVxECyGGaL5s7oulZnpq57A4_uWxQYgLnmo2Zc1PjKxZRNItCEdLIkC0b2bu0zucPv50R6sqI7A943cO8-h2gOwOxxz62fPAB8H5IG456EHcX0qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boe5I00hXrfiYlqfdQ-GbWoVOk5TfgdCwcFh0Y6ywM61ai_8idHsYJpHOY7FqdZKgGi1DjYHlP2QoTSejUF21GYhDvrDfDxNRI-4Cg6EurV-6RD0uctgImMzviS7GKjganRRYbzMzj1lYdYJqvPZoIDHDCTH3BzVmAV-8gWHC962Gm9_1YaqtnpgPLy70dX2OOx0Se7v5V0OtaZAeWpRUwVF20esWYBP3mv51kJeNivQRQgnjTEyJh4BbzjdubLf2l0OgYj0yJFEw_we68ZSeeJYC8C2I5OXRK6582n0D0QHZYTR08MUrFcmUtw8O0IaHVdnooUtEKbT-Xu8Lenjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_QyoLAi3V7G9fn4lqRgE9PscAwYFqfVY66sbX3akxTmGN7NczBGQBZJKFSbPgKuUNV9msJWE8vD_N1NKvUwBCkYBds1FEGe76XLTXQJt1USZh_RcbnMmC-1FaFYwEA_x0tY9Fegg2PhRhFUE56Zvq9at8DMmk2_WD4SQwCq-3mueMYRTJOuEPz_ezm1wMcNi1PqlkujttJ7kJ1RQM_jgXGpLj6YwOzA430HS0I2XKxEBEfj_7XlpltV67u_1k6zGTLG9pg4xXD9EGLp44J3tj-svYtOgqx7kaNaVRZkBAzT5icH8J1_v9fbkhPNf9t_CiwmHT2E-mtDPUq6jsif7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSD4o3xrAoaRPRZgIoArcX5gfKioeZGiXwyXwRmJwiYHJLHGDnLbjfsGMQDghxU7Dkg6UgpfD5kBpVXumT7GpUUNr0zaALvP0QSHZiC8uYdy7rcGjhle70rvq6ZpOZ1nqLaNdvCsPoSY5pp88zrB114Op0fdcTBLaS95UKop1Xe4E80Ukg-G93hXvpgM-TLpqH-AaUaLPzs2c4fjutjDCgxhjVmvtcD_uoSMH6X3ISQzFGWWkl_BWXaDR1M8eiQCy-sy4Kwbxxy8VgUqXvoKbE5b7L9EK_cxcMpXf8aC2ECovH6inuX5WQOCqcaPBreefjxGzn8wuCsl3nlBG0xUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHq7lRSomFR6f6u4dGcLH8inKOvtC1Mgd40crfUPMAGNGbcTugxLLs98K_c5re-AtJX5ACPjJO2E6ZLf42H0lYBJL1CIEXNAehTAGHH01L91uZx7YShKi_IwI92fgyLDaSm-aXileKGGTvYbLCTKXlxSo-SanZmDkCxlse3ZLs2sA9BwuVCfHEnHDuWFPJ2YsxLczNZThhfzV2HUqgGLindRRBdcEq4TG_8H2lH4i13oXOUy_haaZ8X5fpqAL3yDX2KIZ7lkRW1qbn4oJdvciYw0eCVRoHukRGsghVA7cDaoRS7VQaSqehIYJnJKxTq_MlSjhIGlpYlTYaEgX20YYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug9v_U0UPumZzgqw8HN7lXtgk68qI2IANbksdrbY_NMhFosGnc4tIZMcSvEzzUU7-nizAv54rnjmiN-nZMMO0J6Vg-RM_XtWXhcpFVzNov1sECSN-xN4L1Xq_OP8oBR8swYQluxykIE4UhWg5MaXb3ztaupfXeOTQlC01mVD5Xbyi8-7ARBmc6kiWdjsQP1DN7Tis6IsQCnuhcACdRMuCggU0GD7A73RYoV-vVMGwbV_U5kRf_hV5f4ltPWc-5xbDP0kO8JkKu-XYkKJSLaM1y9bfzLwL0uLHxZdG0TPHGKweyrjieRMAULAzwGw5zzueNbFy0FMVWlogKUnC_6EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4RIKMBL7f1Wd9otHIy1oTYpKBbRYdltmUKEldUjddytZ0eVHo2F7wbJ535TT4R8q6ajEje_O1Kn-WQMH35ubtwPgO0cMqqzITYKr7V7QXFoYngayHX3lnPEUBifrSB8lCHGMwedyAr7so8GpupBIw1qr0FUMBvaOdEshUp0OxJbw24YAoZKhQjyd0vHYGFEJ8gVWNNplMCEPyXrYqfe10_a3JBmH4u-Kiack1XzUHGvst6lVEd6Q3RXuX16wkV4yzW1iq4XrD5c_KxjE9eg1IDkJ8ncfS3fwiuFN66tOT69ZvB2cQQGdZJhHmHUrf74ufelF0ErJwSzac7gq5yy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h30VYD3q-zIqvpHhCN01VxL1YaXIPHNtOUnrzkymOxhma4Keka3fQMzP_qM9lpG-Vkbekfc-OX1tBKNWlUtE4Dnb3AlSsDqEzuy94xGcspcP84TVsK5wWT26h0aHQMrC9MeddYVSbPLa_1_MvFcRl0LgAiH-PKYPptxblE5BI0WLqFGJUu09yTLM-xm-s5w-X8mYqBkzBQjmBuGuH4yIi3DMVLceQsX43-KrIfEu8RgaCtIYVfuNzNBzOSJ2kL4KNv5lTTNFRK-r7FjtDDf_DQml5FRe5wrXxt8wB0bXf80eynIv9Pexb_LJ9NZ3qx0HqdgO4qE7u6hjYMgMoAsPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALXyIcLJwKew4MUdb8CMx5mxzOZ4_wr8c9YKlhyQI1yPDHeUXoeNyzg3Ir8dRJANd3PBXwlLV9dCMXLO-_VvVporjDtOAPkAiticIAwRAiSRk4Kw75W_M_FaIvb-x7KvKUtucHugrKGcQ5EFreJqnOsIHMmJR1eNmOs8puRsEUIJB5NooiUHB1-hSb_UQbauirAglBuA92g4MOsZNCYYQ98MCXXiXJ9l-PXeZuLK3YKtN3uqU8mi4zvld75ZWOr28N-yDDoi8_8ZzTNUvfUgcF5eNX5o7sTH_8ndh_IWSLVoon-sb4EGKTGi2CRP3bDwmOSwFKq9k-RY2WNwRGcdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUSdqaVS9a40r-womch2rl1lCl-61vJt45eIzxVaJMG01Bv6xsliMmIFfrfYUaPRSceqMrY5LOSLU6oX4RVeeWSsSjLjkLVCuuzvwWluOhXJ_1KDugHRckr1ZzO-TGeh2-RIrgE2bGbVlXSQeUxHjF21CaJuTZa61bAMJnTok-odU4j5dT05vfM2Lg8ydtwLgAYwoBVepMCbpnHVhN0IMMQBDeh20xcpk2IdzI9qRrLhAwtciewWpum4TbXWkRheZfi6wRPRp6-NOLYyyuMtmTPSSztHK9InwrR4f9oQtosmAYIFFBy-OsDWxeAbm0xM8WO_RR7ePTWzQkD0MhKZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIppteGbp0bKECZlAdET6scw7NDQTbKulz9GkK20X4eoURqXdw_rtUTff93oLGLe20CLvywBZTPjlceUuOK-JKv_23E0_EoWMbHlIzfszmHCh1wrL_xw2f7_xk1Kn8kXxt1PBCqrfuXz3a83rCVQg3w2afob3Q5qQR6PPVDoOWe-JMbbO5Wja36Mvd5CCsXnW7h033bGbSureHyCq-TsRzHUeZtTlUChsWVUyQWtBtpcaz-si2A9hn-wO6dErbo413C9m7w4QMdw2GcPbYye5xr4MEcpOn89yI5h4JE9K_YdUtUulllm6RiNisCtoYRNBvXG3GngwkZfSXNIFr9m0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8D4YZ6yK2qi4v3J1oD51_GgAHEbju4B910zxcXyTtpnEZhUWCNpsxz1u2Cb0_CxAUR_L5PqU884XDMKFLX2u548t5ioF1VcsfE2rK-CZNwB3umfGB9peVDsSFslaGywytaWVHZRjxI063MiHoq9aX2BGNYfZuZIIbjeWTNhmO7bGaZ4xH0jdDwX4YA8Ha88-OzQjLzrzH6V_Sc-hCggcIGl5ON0EZcY1aybBsU_oPNxMIZAVoGXbX6wy9U0XN_iztT8f33t4CfaHRVZvZyu2rvrdhOTVWuUc08TjkpTcyTMfMuVZFNWoSqRtbiO3VCf_r6mqT_lsmt1I-yL6cSlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWZ0MosR-4kSal7sO-OZ6C2l1oSp_zJxBxu66P7gojZpGk10wPBwCD0qiyI62Yjqjyn5CtgYKZ2vwvLZmkQGQfyB9jxQkiml67FMMlss73ERs_J2-Qt5fyKOsBc2BKiDnmvtKosSeVslo0Vgzuf-x2_rWuvmiIaDrYltVTUXfK1ERmTivYNYESOahqNHXMACTZDqm6EW3ODOuUbG6tdoSiZYONrVRDxpI1CympcCNUqLATHngDLiNFaWhwkUyAe96qT2fGKGAYppP5u4zGCQ-z-LgZArEau_AwzQ97SxPDeoQ5ddi3n2OdVhd8H114pPu3qhVMVIfyeKqH4EiQc6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXqLzh_n-iLmb7le2DGXB944GOiJRduPC5JL-8Vo84ivH9SQsoIJXmLBsD2NthLbIVk2So_bfgG0GVeCFX0_Ysn5MDYRg-F5wRFU4AE3zFxQlwAetGVNu__7Be6YsMBKABx-sovfPY5AdS5jddVR85IUmnlOosC4NWdvW9qDdpt6Pef4IvKEy9TcOE2kQrGDK51AZfZ22tV4J19KqAEAZNBO3XE2BwMIsnmbcAi7-ndC4RKtnz_egjaBPECuU20PxHtBU7S8Ugep9OTEwNEMOcdHTj9DFY9TqT9bzKG09tPzYzx1FT3kErp59nct02217udp-v5wtGDgX6-O6GSsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciTEOrlO5TQe3Lb2gnYyAdJqXtXbGiuQ6nf4PKJkdA8DszbGFK7MHwBrKuxkiSaOsH7TXu1C1tyCx33p-2AWtiq9gOF7M81NUC7kZKjjhC9hT0g2OxKjZm3OG-0Ck2P6uIwfgmBbBzMrr4T1XZ8nCjDNauNRWliS1iWwPEIedwI1LEdtZuu5uPr7JeXpnrJSSQ6HlL3QljLtqmTwZ1X4MPdjdqjXRMhBFj3SYhOG7jx2y3TPwHpy9byj7kjMunTfTIPTSnoAHifBRabBep2ndWrwKDqaSNUp1wyF9Dnyjt8_pTb9HbtdqoDEaX_ST2d-Jg06tv9ckTYgLkidAIQZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc5BEj_uTfC0hAPxou2TKuUFGijGuDbuzED82pth0B7cqP7mTvDcH23lhU1gr7qgkZBrFs2S_pqTyZMToxwYB57go1vnSqHLlb4EOVZSDlc2j1ZCzRsVGmTmLSGyLypaLiAALG7c4y8clncdF65YrpGmc3JLYiot-e6YzlYyW-6hVf047xt-zZui5CEvqHZW7jKxFLCzgR58R0-Mrym4PbP4NRuabbjsoy6Eja_qgUjJ54SIWoF9g45rTAOvT_bu2Tk0Xc7qi0DWurSg0_o87eFX_fZOwON0ASZtpvWR4dHr4hzCnZPbx0Iy8PZysuKJBSNd0krME-vYqPxLKvtikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vns8bLpdUZJpEJ2rabNoeD4A2-e4TpaizlLGpnjcsNXI8GCDo6PPn5Pmb4G2Va0a57nacslRILdnpx9chxhmhcl27Or-22fI-qbeA8C2GLtyND1PX2UQ2mafi6P4c_N7KIFBAsHZnHmv9MZzbG6jiSfDY98ZQC5U6B-DPrF8iAN8V2qG245nSmWhOb4GbrhVNB8EneynG4QhkS_rePQPxiAQN9QIp7IBalxwkiKai-JFS4Y82Ip17Crkh3ARiQvfzpA7CbqCHq88E6ZqUsBEfhuJgKKgZ8e7lGVVjmy2j0TElLefSG0awWJsp7yDx66Hf-J8c6PXmMGOCfhzFbFw8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtabSA2iyjdGldPBcASITL5Vf1Dg_eyiPaMkvRJPk7MsA47w9xoba1H4Qm_xuiUuPn5OK1H2R8B42xCyJKHl0je3T99zWWoBZ_S1d9QhNKaZhNnMZRRI7ZU8pAiXX3Xg-npNEWVbnxPtSZVxyCyhhdmki9cBGC918rIo-sm7KreBuctAGO8di057GQ9DJhArnCQIeYo1xULRkZe5R-6UDD_fCiPM_SZt4i3BXCptis1G_6yEgoNrkAmUGzJB_Wsidj_FndfgaknIgYNL9ipESzVv5XxyIi3JyUGbAnb8a6GzJcSsrHqxLdwa9UyLY7zJ-0MGPAQH2Aap6KZLgatjdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4GoDugcjpLrclRO9gUnBReWhYPKWkFQzz5sB60KVz0YYzRKddSOJAHhYflGZJL3dE1CPyrrHt2DWJN-TZXsqdrK_2vb0iGXmmfsAwsb3AhTrog_Ooxlb64A58RUG2P2W91pPv3p_ZmyuBcTQhA5i5RWU0K2gtkOHBXCsFqsdj29A-pIbwD3XXW6Fym1jOrgvTTO37KdjS_uFpQoKq9bHIZv6V3R7yr-CNJADYN75xhuyNVRqxA0tPyqhO-AX0vWIXsYFFytlobL-kW_hxhPngr6GayjQaI73U6qmKM-jA-N2kxN8RZozSfkKsX5S8-yXNUpyXzXevzyd_L08nehnaHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4GoDugcjpLrclRO9gUnBReWhYPKWkFQzz5sB60KVz0YYzRKddSOJAHhYflGZJL3dE1CPyrrHt2DWJN-TZXsqdrK_2vb0iGXmmfsAwsb3AhTrog_Ooxlb64A58RUG2P2W91pPv3p_ZmyuBcTQhA5i5RWU0K2gtkOHBXCsFqsdj29A-pIbwD3XXW6Fym1jOrgvTTO37KdjS_uFpQoKq9bHIZv6V3R7yr-CNJADYN75xhuyNVRqxA0tPyqhO-AX0vWIXsYFFytlobL-kW_hxhPngr6GayjQaI73U6qmKM-jA-N2kxN8RZozSfkKsX5S8-yXNUpyXzXevzyd_L08nehnaHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aRQatUzmjmmQfHRxHx6BtAAkUtTnMPBSWS0L8JbVxCRwSiVO2h5rLTnrF-mMPQ_XIP8ImGBZMD72VgOHmglagfumEcRN5fCsXMfH4VKkRoKsj6jMpU8a5z12Db6CJZeuGE9528mrQ9nuEsIcY7yCU8XM1-G0wS5yEWTbv0XXqz2suVCKeNGY9nNaq3lQx5GUwXqDoRhpzDxiSehBgS64D-2uuxZixO-Q4el8tBPhUtzcdnnto5J30yFrmjyxZ6bT-hjipzq88LUV93a2iDyFFuPHZme-y8BKscz9rUqxkN3rPypRyq8ykhd5jbfo_aoO4tHPrrYaklucErc4ukiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGsU5y9UxdRbuikPOYe1RvYc-l5zFXgaYxgDFe4evFW9MEbRKvwK7FZm-QaKwRJlTbKmSayaeMTPNlNxSZM0Cw2ImstdrJ3EGGLrFS1xoFXYnzg59Q6VOlRcDWCzSb4O2qzY5OSHwkFLiX-l5x9NkjDZf5MfjU7egp2E-SLi7eMGOuWpbxKSQLNKtu6eDllt1xedUxETBjR_FX2yfacmURT2lg0QK70DyOoKIUWDIAYTy634wkCfkLwIqFByMl24Y26npVImtDsePcoYF_Ox9mSkXrWrTmmwGJtq4i1vBTmLtqEWU0O0ArArASwlg8VM9eP-T4Ca5p8QU5r7o3Si-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ-dy5_eL1o3Ro3sV-QuokXgi1tlfMzmgxV34uqLu6S7ItyI5cMR1ZLYJO2eaYz6VkPJTa0my6PNxo73f3nnF78bnzPjrHbQX14a91b-_KTwsdRbkjusK27fu6yzChMXAkQ81oHQhT4H7b-Ur6zrtrrFegxQNWJ_9ygHgE-_VgJr4PmPtE1ZGAL-s2Eii5H8s4EJOZmiGA5c5mTthmpOE_hSLyDAKmHCIiba5PHFimsJ9VNpTeiEw-XX6qJ-ZeqwbmWl70hXiRZfe2w-NkpS60vx6Ac4nXYn9SkdTxS0ijdB4oXMja57C9uLjG_z5528J0eBqtB9bJ7ccpofZSHJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=MXuu03pZI2wwbgVyyjGkaLAb_6OinlOpRwFiF_ejNjfYl4lAWlOL9kHAf0DK-fMIDtVy2KtbO9ZpvSwX0FjFhbFcf2xb-3n6L2YH2SIyKLFFWgzH5DeQurbg5cGc5tUkB-VWWDn_wSsiSZcMwkdYztUotCeJLW-UhlAuapAc6FM4_hANuOYa9dsbo2YVvG1ae_CdQ5LQW12LHg08QmInUv5eyHuNYlYKNaAtbMmsO2wZ2rk2rEsewvCULmi-dY4incHKjBlcIpj3q5_uRgtLUvG7xj7RgN4rF27MvvyhjZCTFAj0ktwREU00NvPnWH3iuS4T4iHMJqvFA7PqGPnMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=MXuu03pZI2wwbgVyyjGkaLAb_6OinlOpRwFiF_ejNjfYl4lAWlOL9kHAf0DK-fMIDtVy2KtbO9ZpvSwX0FjFhbFcf2xb-3n6L2YH2SIyKLFFWgzH5DeQurbg5cGc5tUkB-VWWDn_wSsiSZcMwkdYztUotCeJLW-UhlAuapAc6FM4_hANuOYa9dsbo2YVvG1ae_CdQ5LQW12LHg08QmInUv5eyHuNYlYKNaAtbMmsO2wZ2rk2rEsewvCULmi-dY4incHKjBlcIpj3q5_uRgtLUvG7xj7RgN4rF27MvvyhjZCTFAj0ktwREU00NvPnWH3iuS4T4iHMJqvFA7PqGPnMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=loQOlu2qhgIGZBDm-DuXqxtjspXfGSX1w9dwBlC1Iu-TmKckf6lDzU9smCI-KuR5vAtWW0ASj2jqabDEc0mIwssL4ExtQvt15XExZ4Uc_lobvJ5HHjNjo5umcgpDvl87ngRMYslYPIhjSKG40gXUNogj0JKX7f2IuBnjEGT9AYpZCDCnmFvsR_79V02mu1rKNswkOTNMrquoEyc72viHxaveuujXyO-JNgcgygG2rndv6YyVsT2VdONsWXFquFK5rTMb-gJwPSx2tdLjfyhfDafSSSzNERkgoOkzbgECv0ntDQlku_folM0RnrikvXNMewgMIb52wr9YjHt4a3gzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=loQOlu2qhgIGZBDm-DuXqxtjspXfGSX1w9dwBlC1Iu-TmKckf6lDzU9smCI-KuR5vAtWW0ASj2jqabDEc0mIwssL4ExtQvt15XExZ4Uc_lobvJ5HHjNjo5umcgpDvl87ngRMYslYPIhjSKG40gXUNogj0JKX7f2IuBnjEGT9AYpZCDCnmFvsR_79V02mu1rKNswkOTNMrquoEyc72viHxaveuujXyO-JNgcgygG2rndv6YyVsT2VdONsWXFquFK5rTMb-gJwPSx2tdLjfyhfDafSSSzNERkgoOkzbgECv0ntDQlku_folM0RnrikvXNMewgMIb52wr9YjHt4a3gzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQZG9b44K7GINgIeVKOVQ1ITfRT37UGSIvWZp15S6VV7IqWF5Zmu6MTVS6vQXKn1EFJCFUPbCjIyPIDCPPPTNWW4lRhGSR4xlpByX_VEuLPFXzLRozaErCQUgcG-46zWMmTsxaFFT45o3U0vhuf6mPurhbAfBEuggBzVEW_oQdy5wZpHqA7JMv2BOklXku7kk1RwSX0xgvPrhUT4NDhBHTdXlRTnwbYfKjl6MLxkNRL_KdewWYDGg72XFOMpfdnVL_MsxGWVnq4F3lsWAIb6WnIgHbnaFgoIe9LHMQEnxpnj2mvRA1xuqv343cmjFz7KhAZEl3fjcg4HDAqVE0kN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfTrwKVyRAlk6HOksbxTu0X1qXej7qtwfvyM_CbVETfVAZfM6E2vvXEN38UArvIgho0ebb9DYj641sp6NuI-deUprZ9nP2Aw4Tf-0_1FPDitvJZx_WhtgPo38j6ATvWPYmWNGoLXoYjwE84jnRH9byOKXnP-FAZ31EBO5A26mbLrcPiMhHkpOw33aXS-E1VZqL9UCD95e_jOYFnaSKO7uV4UAe3p-7QfiHpUmMc649W7a6ihSoyoBFFZhpPktxGYnUey6BCFJBXAXRpFt89wZ-lfDxLIn_IK9OB6fZLsCdV_Mk__angyFBnvkkdu9nwp1fEhYV3TbM2WXzErNtlhjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjgpKECvZm4rWkRhGLLuL1bJ-1-r35kbvxzFyJf-VK21cEWwEZ8HNhwl83rifA7wCJKJUfhMdJxSHRpJXjs89dfSBUA921P_Qe2YOEpUvqSoIDdiEScq66M3qPNAW6UtHw22NQuI_nb4_AQpfVm27t-6OfRc8GUXpXZg1UtMzotJy7ZmYIKnN1nzl2qbLqS0jsLiZR1mNFUktLcje2vGcGaBTpobvxfq842hfrHLt24NGM4u4CbqcpVo_EB-_jT9wDMllM7YRSn3IVnCHn4NDOHJWubs_7nwdLu3MjlLf3FR-tJuyFzfrxvYm9Pzr20HFZoUc_YIoB6ZUD5VhzWAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpgkw9B3rSDHo2HjkU39KdLfIC_OPC8zQIHj6snYMNyVJpKMao4SPHxVRBAQujycZi8tUg9L4rPOOaF4mRaX9wLOZLyyuMNAIwRESc54rTNyCKWw2fADVQLb_qJh65VuNeBueiGZwrkBbS3JasKNKug1VvdFF7tggB8BFW76koNYQDKagR_ypYgZTcPLbw7K6hVQSUZa0Hi9muLHcopp2CeIfuVkoOTQD1Wjk5hVj2LNlJIoOjjgnIc_I0sof_BSm55k7l0YtoMuoYSM1ht7PlrU6TTmnGO7AKToPcqJj4er2bV-5sZdw2ShdO3egxAp2XHF0G1DL5-0R5LYiFmW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2q_JRI3ap2071iqHjBLtQbN6NHmk78_oAhsK1Hj1NE1tLwgnbzl2t3Nw_f2dgoryMx9w6AtqM2Thoi1V6sGYxTqTpUl0cFz1mKqbiqpQesWovBtvUMKwVlbxoMj8sl18jxBAmzj4QGtgtN70k4wEIzS6KESc5u9rE82WUwKuoBbP9rW0uesSe-dLi6HIvMoVg_BY6GSRMRxZOjXY59Aao7pXiK0JYPVowFnpc22RI79B4dlxnK_mShftvkytv-M7f6vGGo9_zWoOE89B0Mn3-vj1zO9BWYl4rBFF3qCQrvsL863aU6BxTFoRTjhTQrHoSvEf6N4CYdJfniBniKkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFIq6j1ey7oR6q-3v2CRb7os00dxXFj7JfadYkT11LFG2Jufe8zBsH7fXsHuXd_v2QPfq2GyFdMCew11Gak3XZSIdKarapqb9l1D4Io1j-5TPxwksRHwEVyNSGqraa2x_TJhrHTJCV5ErvqVUBhoy9-FFoRxYbPBgSfsVbbCu-kAgAcOGA-RFvSC2z9s6oxC4zeRNAcvXrNd4n5N551hh9qBB0BzxS0OMq9wsmah0cjfmIBRdIUMA5iFKe9YW_Wgnp0vRY119bRWqJ1cAJK0bcb-o5BL_IyBsvohqPDP-rJusKB0u3lzcHgDD0PpzdSq2LXbYWJ30hkwEXm5ix5vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA9_l8U7sTPECprgkYXli0iPFk9utaVdpLdacBzjW3vOA_kkzk41A0ghcslJ6oQEqbjiVMjjTZNd6ZvnJ2hlTDkQKd1Ssafn0NoqwY4YUz0D_---sWsj_XHXJOUtL-icGsnkOrMbFq6Z_MIyrTcU4_B1dKBA3-6jNkgP690cp5Scx8SQZpP5yfPmFrOAYS9W3BYFs4TXkyeEgHce4Ew7YeyHZd4W3Lhh3eDiHbn3D_uq5DK0i5q2ZT9lD9uYZO-3icaKfPSGaEUdfcPQi-hdrq_Vz0Qj6Oq9sAmmy1HUbiqYOU0MoCJbMCkR2PvjNzzX5VqL31FA9FKVB1oQdxvjKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqLOVDS_I4zRCbsSMIZmtKx5wTnHKAwO_S5EhDaVxuq_3lBsm9JmGIuO5BR396EpQXzN9kNF-AzmWNO0sIRMCcgG6ExxeFNJrK1Ebt-Nd3x4Cj6pzqeqbO2hpDiIMLbg-x8cOj_kfyeUO_ijcDXKVbkgvu7liOvlrFpDZKLTSUoaqfmDSAZRuxBf6czS4Pr_OeSyJz9ce0yBow_Fav4tw0E7CU7U1FGHRi2BPY0M9UxNtlOX9EFwD9CMHbWFaDytqzmZUVLbLtOKaw8HEOXKguIOMpT3xafPrXB0I0pHujLA2XXx6pCq1nwYDszCf3Bg-HvZjWT5wYTraJKUtd92XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MspHN-aQDOxTyF75gUlv0oLYpVv_P1Gn6klgVbfF1Z9HzsqRwgVGQD6NtFvg5CWr5qYIOKiu6gprqtpb6Z_Lk7u6AOhdt55nb7TLoUEJyWoyIjU4iAh33VGx6LmtemZEfOlY-_s_6bDvJOhohrpECiY3H1N3QF_RL38nu0-e9jblbKyLebhQ3bFyKizSnja3pWT23fJBig2znk4GBKF61CLv3rMUJhOoKw8mF18xZypaHwHAAbepqBwKW6CebCToqGClM0CfTfhB9vuDAC1EiPfYXQ3l8HWW2GcSqgBE_1U-JMudF25L4HXLtngCbchzBkBHjmoGgbkGCjl-yxV1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvL1RiB66CE6DTQGRo1SlQ6NX7cLvahX15yoXQxRWt0U6p0X6Bzzg2JlZ_X588QQGi5TxXHc1-6DCOZJwnokdyuZ1LplYfJspjKoT__HolrlA8u72LkuCJN5t3G7oZNVAGbnl9Q_d5NvdzrznOaBpQjObR7tAJzCeVASWBQCA8Hyc8IP4JvRO0zaw7TZ6sqwRvKmX4g-xXhdNI_RsOtIbMvtYIsjlzP8_wy_U7OhaypfaehJJEVdcHTwEo6nHrWoxWTpsaMDmP72e1hCmy_8h9Qwdprlt54ZxJyLJCAwDHdUlM2DcJEmwDfitWKoh2iQrXD1kWbMKru5lRl1k7--mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuqyP6lh-y_TEW3UvGWkzEIQrqG3iyrZB7f1YmtFFTPStCvPjUvVIETQ5PRUThz4ekBuPrRhDMrLvGug9zCiAmkLbOgBJPzL6oHmxHBOifgaI46XqFUYgdrsJJQYx1Qg8AISvcZjEB_UDpEryp-xh5EDzSBnfjPUM5Nm8UcjZQBL-xErZWaIayb0_86lWx88cehU1Z_xu72OlRmGkw2Coa_SWz5Gf0258ETqbgKvS1ESJfyCOZt_onDNok5CNid1bwviXblpcSxA-tlRFYxWsTOkWC0UQ4TFMYX2nXbFXFc9_1UyC2Swxode4MaZLxgp2gRyKOTjMT_mmHfvL_y9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHjvM-2adqsIAy1iBzSiVmgtTKm6HiNpUdDlHAYds9ib8nNaYiFYFlbK9ffoNrc-H4SEd4AeH4G6AEiqyzA1gAKAnvjdYYxL4lAECwzVR0vR8DRJpvlYGHwn-lzc037kETGT3DAsJwmY6G2wvgcgpJNkc4roY-QSsvrlyK7jFVU9q1AQfD3zmiQFBZ2V_tg29-vYzPO1yIUB3wt5ptCMqZlWillOF_SYW2O3QtOiOvZ2Bm6rq0egMEt-2J0Zq8L_twr7hZjXp6hr5zhCWjaTxOaSCpN77jYyKWkXRyW9KX1u76WSV1BD6Bi3yay-miWf6ZOkhE80eIDBwIqUrrVeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv6KInzn2fHAzQq0qOeoWyil6ABGs0Dc1IHC25csW8F12hzG2dtJg5ujefrL0z8wm3ilOSIsuA8BKmY_fQlIMDuA_luio2oC7O3H-VCKxdHt0ILMWyvzesGzWpPC4-xo1Np9aSDGHOKbEOiMIeUVeXge8WcEpQnRgdWhih6aNPQyHgGElzXB2D_uPzS2_BYv5b6QNSRjeskcjo74Sj_UuJXwwPNgRgk3ecCFfpfqYcslrXcAJPRYj_-wUgHy368ExJlsk_2YXQPS19oiDtNeeoIVG55U_J1OXBXECKCRGQli6st--FUXWu4mg3JY49hEKCVZMvnOlxl2rNjxKl1Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVIJH93PsMwlolPgy05nQNNf_mkxdTydJo6_3Wg8Rgh3lHAFGPnzJMh01fs6f1DgDyOT3tIycKZWuSvA0ONbY69sxItlZv3OruammSg2K1eujnahD-NvTzHgUfJ72yDbr6oUA8MkHnGVkYn7uZlZX3BrL0furWTLULqvzdxdlPYB3HBDYJnApYsmWz-okU8-Sv9ktNlQJNH1PF0N1zvjUl0ksOvWIbZB1XANNTKIK6qBP99x7Dh46oGYeGKQwwlVSsi4NqvF8t2uoh_Du6hYnH_afD7i1eO354VxQaik9cHN50mWX0d7y7BlXO-ZiqzKNuCTxH5F6iuBtKDwr0t5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2WV6LKOyBiQXNBDkapgT6dvUoxWjiSK9VIkerfNXedzj1eEsY6ugjt3yIHVT5Fo72hsW9GSHdhXcQqKRyBaRI8tzA2T93ijEwx7F7sM__AFIAjhzkSFLdZRfKzJr4ihU15Nh_LIW5Gctb9f1PLjsldjCC_pNghQ4PglBft6qt9364b-MbPG7h39nTQm0K-PuRQo_oiTECV33cIO1DR9XDRcSt4r-3Gw23AO96DL0zPNxMqcspiUsqd2HesL3X5U2iWHe10FxvP-aVplO00uG1rNwWC1kNxdKrGx6hpVgjknFV1vdD8N_UlIsrd5ZrX1V74mvfPSbHm_vFefl9tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIa8cGL-C91egSW_2sTFOb5JNebLw92n_GNwjKgRZg1o2EyKNscf0GSx4L2uTVRjTxOuzq1pdx48-iHUXkzSa41gEDPgXBFdPvj2FMET9fK0tzhnj6VbUmkcucBAX7a40ucOGsj6_pyXDtQAwHscLSIavCAH-kX0fPgdEJPLrsj7FmtQJ9b1Qnquh5A0v26tl32ARCz_uUlxXseVbJ5zYainx1QQMAtTyEqaKDioRTWZsphe-JDv9j3qUq92ylAdN4uydMOW3rvWqOCbFsIwPCaWnt3BN6En8mwAEwsxyKsE9pKNBQPDOGmVRZKAVgbG5-IpdgUjJfaLpbMq-17jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDCP_8-3j2TjHKv3JUpdPb-R9jsc-nTFXXegwbyLGN1qSSi1Tbl_RVhsBjYS54CErs8XNV4uwIDrXFj4GOmwsIcOVtDYlwpwfOcSILOcshejwVq0Y_JliLO08STTDbH-MvRaw-HJ00UnYjhRcgKgOptmlxU84lL-b9oZSLcFbnxAksiyixxw3e0wDHiQdSnVG8f_Jf5W7I7D8OOMlz1s1U88vcH8WDDBe9T2JMOTFaqjqcEqoeR8UnAHtDPTcuXA1A8Qb9JJklShfXX0H95ZZSU-R58xMXul41TVmuV1Cva1ldnf7rYym6rC1z5rziFhrN03Enex-zxb10tBmQ04QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjzZfdCut257pjYQ6mjLWC3kJWdLItJRrLoElWYnr8ebUEwKPxrS1AMnXgRhFTmUWpl8Z05_UJXq2bJy52ZucRNha0yPr-kkPiSTuJ1_2twtUUaaZKM2FQvpUZJo77McTiXo9MqaD9h7Wg86odTpesNS74AlsNC5odFj14vztsEmeyfPgTFXr2AVROEESNlR0WRycLB-vxyhxTbMAPs68pOf5FT54c3cwhw3k7tkEvIyJ7nMx5zBuEAh35B7bq5vh8VrhK6oP_uBhkhnXF_JOUTp_2YFSWyS1ZSNWLUiRD59h9ll88LU4G3Jf0drGOrIT4x-TVX5Nc2wmrWCTPbZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOwMeFnyDCybcQBA9RTqzbMLEkKkiNY6GNGk3GGMqzfSncvPg1SNZ9NFOl_Vqcnm5zkBTbaAKLhYSScgKnxfkblZzUDZg9wt8jucrwDcw1G9JgXgIWTl6ento4UIBAJhAX_TPjsOeWqRcjKPq0NkHqJeGmik2yB3DZ0H-dTMdh62jfPGuKdBbeoEjEtFwN2-l5oA4CmHhYTsZHwlL76glZbcnL7w74-pzd3fW6Rp03Xa_yA1m2Eb5roodt630FCpSmgPmZPFRobxC68Asul6tdWKOsmq2cZjHXT_kpqMCExZL-G5OJaLwlxGNQm6f0hE4vcM8IoAPl-HVrxn2WFHcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgG_mEwLAbDjYYMD-OoDJSjTTe5ZYZruPd8j8paIXRNRM0GXI4zlE_mUjehikfYIoiNA9WHxT1jezNV9uAYOSCrARobYHO8yWDKAtgWzO8iNqp5ka92B53v-1fNfogBnOKr-VvoVXxB0m44tahsp8P2hm_PJXPS4XzPhXSHEyaTSPz0Q5BzevLkKsWFeM9VtGy1247dZGJhnE9V0wF3PqRcqZw2gnFV8KmcdIXfMrL0WKCJ-g9X02zL2T3kgjpfIYIGqbz9ssC0pMLa2Jt2BSqrYbEWGydji2Z3m7q-NFMntn_qj7m_Boe6HUa0yrCB_uBoJ7KX0EfOzOrQLWhIXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W50KjikEW3vw09TSJ2UucWD8BI2KGDQVlNkOBj8ClSqLPAg97FUZM0fl2wKlBkiDQPZsMXr35ZBbEGMsqrXS8NJRNhItu58OCufNI3JbFNMVcYUkT9qzfHePYJ53IALdmU0b3BGQT6nca-5iAGWFS7pNBJvWpVk50yHXP6ihaFGXrVGQvcgt0hP9Sn14WCfv3tRZjps8qJJk36JvpQagh8FSUjqmodnU4CbjvHIr4ktQOgOjjs6xh8RgP1fxGEpkWWIh7uNkecsxaqT8ZnKLJTYOhxmqQNp_tjfVCi2kIb3ZlT4BrOnbnWx5i6Pct3UflBw0IQfaupPfrJ5RldyNeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=E-DXwQUEs2xIIYRtLfqFFMnp9f9CfBoKVQyR7yU5JjHdZBWsPxu9Sj14-GwbfnBgP3-N2m1jXFrfNTCAhiUTstqDSvTJBSz6JjMivDSX9J2QUnfVG5pSKfVXwznmMNfc0A8-XnwK4v0EHSuXZpZSRIC2PkoPRKUFWy-LZf0wbJW4sDRtRFuqrS8KHKMo_HddN76qRWHXmx6apnLNbxF8yEFYK3c8giGUbbiGBWJa5I4MdHeZyIR_Hc3h-50WU2EP35d-PW4l1YvcE9wvhiJA-SaFpmC0TaUXybdFCvXDuh-QeNbKFKUiZx58EQX7F6X72Od-rOKLihyIbe8Q8g73HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=E-DXwQUEs2xIIYRtLfqFFMnp9f9CfBoKVQyR7yU5JjHdZBWsPxu9Sj14-GwbfnBgP3-N2m1jXFrfNTCAhiUTstqDSvTJBSz6JjMivDSX9J2QUnfVG5pSKfVXwznmMNfc0A8-XnwK4v0EHSuXZpZSRIC2PkoPRKUFWy-LZf0wbJW4sDRtRFuqrS8KHKMo_HddN76qRWHXmx6apnLNbxF8yEFYK3c8giGUbbiGBWJa5I4MdHeZyIR_Hc3h-50WU2EP35d-PW4l1YvcE9wvhiJA-SaFpmC0TaUXybdFCvXDuh-QeNbKFKUiZx58EQX7F6X72Od-rOKLihyIbe8Q8g73HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUn5g1uUoVBmLQn4hljd0Jahew0Y2R9Xa7fDi-SIT04-fu3Vabsz6QpK5RjOTzFMhFS8hxjw6CgGrZ2O_-dWiruoL7si1cbX_HD4ynzOrZnQEwTy6VH1JIjPKbwFmuZxxcvPHGiNcfTyyv5fbQZ29neOCtFSAIS7DUCQNGBMS7bsIMqak_WhwgPZGA07IsPOjqR_CPxIBVLg-cITigkrAXxJ-hRnxyQ-8vsl76Xb-GN0adHXcLL73-8_Ofba8ymNMGSXQfN-Xixa1MZBPNm5T3yeWIe3tf5VbXeVbsU-rpbX0o86EzSei5i5mqYMSa4AF1ZQy_kplo-u4mNXhGHYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UstWtFtOsLWRuZYNV811p1MvAQIqZdyovxkjM0yDBqHB0RumanS34fC2R6oJHriBKZ_tJob6BEa4q7rbQXG0EpIRghUGW35xNL0g9VM8V-IXPAvk89WDt89Aw5NUPBMqlMFP2jVYccHCar1aDRYMgN_DL7sBFESjNOtfyvKnRbPOliw1bAmmW2f0JfRH_7CuZy-upauJ8aODxiLoeAJW93YdjzPMQ-QOCT4-TDczaLmof8J7Ib5eE8lO-iuITRX2CtBV3EAQD3N0KN2XxzTUivrwrkUkO0q2Ew36ItEP1DNUhcsgSN5G2FqzIVr-AJwjk6pgWtXvgAa62DD7AoJeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEefVs9JAWLZbJDoLJW3odXSZ_WES8sdx-I7PkquUDvpD6rZ0r69xZ5d6r8t7qpqJXo3SgcSRpnyjHBoEaJBC5QaCGUjXF8kxhdvZvEQbX_5J-raILZfwBdV_SlnE_0djgOEhN11XwkBouTzNss5GYdYYJ8yLm-h2zcoF0jLao7eOqAi2L25zjJFiSRyqotwdYqMud5immL3z_QoE3tD5EmC0SPW_3Qr7J8g1zOrCnvReLL6bc_YelEH3k2yzdx4g5FyHliUaSkWCCRpa1Rn1NSv3f5tPdtiJEWYNwB3kbGYd6KfpEWajNyztTsHDCXw93a11u_OIBtFxWWGnPDVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLjNlBlCopR-EpQazoyxAlGhZk0Ced8yUCflqvaBvmLXhjaMpkH7lrsh0Nu4pxm0og5M5gKHWdlE-ZumjWAL1FlLj7eUOirtfmn3ODR65T74d4irYKL7MnekvBjQNg4k1FM8PJmDCiRbLVguzXzXR9RoLM0hqwpfLcnkWjIoqRtdFreMC0-xyZIsYoLnoPJV92cjkR93YEzJacXx5gXO6VOLOmELDuyCjwjWzyf26OFLpdrJxRvmMzxDppgTH3PtuWptKh8OaRBtq3l-E0CAQa9fVGq3SaOP482N5gGShhS67TPMDfrxbhuOXQhBE2lBiDcviu8Wf6JxDrdY53D2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8zbEjqeriOzqdCMdbQJgOlQ_3wu_UXECbLNPIDUVm_aMhmUGGFUClKj4UU2Ngj3Dw2AUL5yO_IcEVHcpclpLPj_Vjyam8JiS_TBfo_z8Xj_hGDGPRI9HcRHHCnL2T46dw78whTVlWu9CVP9oBy-lo5kpqMWHZXZz8z8TjM_A3ZI9wkQYUJUI1GMxxagy32ycMPa4qKm-9JxBjv4UUHJ166c288ZPk7VjPl-CaqIj3KPymhYtqJOl-5CnGeGsic4ae78bMIsev0aN9KZGAA68GU--zB9GVU6SxQIECwBgUU2K1KHP5qvy3roqjRrIwrGjPxvR0y2-K8BePBPFOhgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd1_Qyag7YCDuTxFlH646dN9fb_J-L-Xa1X65otwT9d4fHsTqNVY7RYHil0G1mPCyfIP8K3pqo46wNj7_-cI5XcDeT751yf-iotbuBs7L2fnmO57leIOvAFq02ChG19Ooi5njrFjijehda11pLEDiMu64f95-i2r3iVf8KKVAoczKr411VS2Gkt5P5i3kPzMUZca8Jv-KkR_3BOJebKyzjTDQFBN4y-dK1lqiz00PMQwnCom-kBnsscJz2xGH-3vPKl4XJiZlKOdDJQyG-K23UQAPiLBAXZEmgAeY5mmbdVJffIWIUTffWDqAAAOwpRPHwPGH57FjApo9lynX9Lm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncq4B_VyU01UV4HJb5Eb_EWVyId9pfzx53CTGirruSfSPg9HLXK4PfYEMRpB6QyvPH60GZwCOJV3OFy8REPiw5xZcrGjNAjqa4k8r6YGPV6WElgflA1owT_YrX4OG8_EOwYzlcIQzcBI6juAh_Ny2fM4v29E4I76At2iAv98Cnnlzr84jNkw3LLFofd7upPhkrjPWqccp9y_6qd3yVBEVvGM6gji7Ob5WAxXOFDBXN4Z5Krm3BvOhfIIz8VrGCIOM1U4nxwgaLfNgT4phhG9MHy2bCPhb2_nsWcjDrBCRCaU53OT3CithYy_Ndws0tF164dbWpyu73Hdv0JxKKUQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyyRJlkUpeVYdeffuxv1un2w2ESrKQ6c36X4zuo3UzkXdGMK60CWzfRqflSfyzZlNnqqwsR25eG5-VxeA3THQR2cj2v6arXiYPL02uXc6w_uazR7FxEctPxdey0k8hX7wI4WsxLzn-HGWLnS_0x41GzTfeFfyFpA1s09UZ3qokBO769h4QU6wnHnu8I1o-38GT494imLzYbkRK2ZUjTsQgkszN3DsrYzLY5BioLTG3Sc_8tEtDWGmkhH2odfiHA7XnVQcNzKWVgaB4gQCnvikos9cXn7Or58YPN813IoPia8q1V2rUVCtoCE2eZRK-gx7Knj_S0gB8E-hyVmnHh1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=VtaQefwOVAXEnWJELn3iy--vgpvg5HkaH07zPIMuifiPC87L6GAuI64PucPgCnLDlpRCEqHIWkGsiWu8lJwOr1oVjw4yPghO3GvVEfErZyBmFoq21dYZKvBCZhfJz_pvAQ2PvfT8N2sVBUKVm06Ar_e2KX1sz3e10KjjqRl8mTNtPdK_gksVi9uFE-gufoAXCFbtHL0ciakM5wPa3HdWEidCRIq2rsyLsABoRxcKTOYP2siXGYMw7Sf8IlB3JhBq2vdRfbuyKwX1yBgd7dueacGkfVI4IT_867PL7Zqrr9t5wRzY6ZD6oJnXzfqE2jwnyVKtbjhWiHpzzfpTg1IRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=VtaQefwOVAXEnWJELn3iy--vgpvg5HkaH07zPIMuifiPC87L6GAuI64PucPgCnLDlpRCEqHIWkGsiWu8lJwOr1oVjw4yPghO3GvVEfErZyBmFoq21dYZKvBCZhfJz_pvAQ2PvfT8N2sVBUKVm06Ar_e2KX1sz3e10KjjqRl8mTNtPdK_gksVi9uFE-gufoAXCFbtHL0ciakM5wPa3HdWEidCRIq2rsyLsABoRxcKTOYP2siXGYMw7Sf8IlB3JhBq2vdRfbuyKwX1yBgd7dueacGkfVI4IT_867PL7Zqrr9t5wRzY6ZD6oJnXzfqE2jwnyVKtbjhWiHpzzfpTg1IRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZwjSQAYjewd0208h5H-FnS-gDZGgyNxUQWmsfgOQfN37MXV9tGEVTRjM3Zx2PUhLYDPx8UjcudkQ7drf7pPzbPDqL-ZhDaU3te-I5I1Nn1c2HlARidy4lKZ1FR3NLDQD4D0q5-uTjG5qamNy57K9sg382GefSMFRlAt7C1TpCkEotfClFxZbecI1g47suIp4TTzB5uVhVzrXrG3JRf2YcKjVVBKGVI7-gd4yhyO7iLYig_-kBG86rCq6MX8KaQqBDJzh_uRIACrmDkOK6WkRa5km-r5HXXXIX3n5P3DAu3kYvq2Q_nxEMn8NDQO6xKA46LNAu3qlc16NwcVoIhojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=rtLh991lNQ1R3sijf0HGET0YeAGiovDwrC67cqe39DBtPEvxeZ-qz6zgg-nQdmnky7hHtqGz69xNWP5mrNkyRPsXoou4-UHTk3LnmtJ-0MGyB60RaJV1wqw-Px30l9cNaF_Y9853HhcL5adqq_ClEhiFvfsSl13GyUKdvVHF4rMUbcMRZt4Uud2A2C4HOcDHYKHtyyJvyl032lsw2p-BCxw0AGRNJyBPHQa40IYNg-Vo9WYwAZSGyZgaS9U3642AFaHKfGy9X6ilRwFw2RRvXLmtKcOt-ARfJu82Q2-1JW6Qx4mEKr1I7PSD1r8Ke4ZWdrb4Gj-Q2Kxplava8Jq8Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=rtLh991lNQ1R3sijf0HGET0YeAGiovDwrC67cqe39DBtPEvxeZ-qz6zgg-nQdmnky7hHtqGz69xNWP5mrNkyRPsXoou4-UHTk3LnmtJ-0MGyB60RaJV1wqw-Px30l9cNaF_Y9853HhcL5adqq_ClEhiFvfsSl13GyUKdvVHF4rMUbcMRZt4Uud2A2C4HOcDHYKHtyyJvyl032lsw2p-BCxw0AGRNJyBPHQa40IYNg-Vo9WYwAZSGyZgaS9U3642AFaHKfGy9X6ilRwFw2RRvXLmtKcOt-ARfJu82Q2-1JW6Qx4mEKr1I7PSD1r8Ke4ZWdrb4Gj-Q2Kxplava8Jq8Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=kUg9ljbkfO9RmOnFPHUzWOoGs-0N4XkWjA3TDTzZa2_zxr7R_4uQ-kno8lXpkeBtSKIKdvdfg1MWOeOOrVmyq0gL3_7F3bRTdgGWK4SoMeFubHV5t0sPqZlHNZKRFwJXwlOUm95LBB_kvn3IOx_gGJYNpUNyKXv9eWvzNfM171kjgxibFa5bZ2SGoFhgHe-710iNmHLa5bbXdvZLqCLQB122x_ntiYNG770DpPlgb8lxbSU-Dm-1PFMNvX75AQEcQicIdVS0VHdTrdeTG4TQBPyW9YXTe1qH8VolNFni4in5ZJ7c7utF6_aZOAYe1X4osk48nzBJwN44lgizpkbtqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=kUg9ljbkfO9RmOnFPHUzWOoGs-0N4XkWjA3TDTzZa2_zxr7R_4uQ-kno8lXpkeBtSKIKdvdfg1MWOeOOrVmyq0gL3_7F3bRTdgGWK4SoMeFubHV5t0sPqZlHNZKRFwJXwlOUm95LBB_kvn3IOx_gGJYNpUNyKXv9eWvzNfM171kjgxibFa5bZ2SGoFhgHe-710iNmHLa5bbXdvZLqCLQB122x_ntiYNG770DpPlgb8lxbSU-Dm-1PFMNvX75AQEcQicIdVS0VHdTrdeTG4TQBPyW9YXTe1qH8VolNFni4in5ZJ7c7utF6_aZOAYe1X4osk48nzBJwN44lgizpkbtqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=JJJ_OmKhQIhRl8-yTtsBeKRVzZnNgYDtufxqqGpwybk56r0VzyfpCk3IT1wJNIrYsIotKLX7yEOQimxY9JH4vp31Igf0QRtd-HbXSJlQ2S65_QCdANNgAHvSOzbRDhCng_lysnA47k6sPtUJbu91hEBCbImIaskIvMEV9c-jP1OWs9XTCLsoeUDdcPa6egrJOjlvs_rdiwwzcS_Usj2j3hwBWh3Fq6nCigWVdcwXZb3puVNnhsN8yIQ7B_zmcs4pmhxc9cFPAVCMuH9gB7KleGPk_4ZSjUeJ1zvIHwi7ZR6kOfV-5Ph6hoRmsaKKzrkCCeHL4Dq9_efdZtr9YZKI_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=JJJ_OmKhQIhRl8-yTtsBeKRVzZnNgYDtufxqqGpwybk56r0VzyfpCk3IT1wJNIrYsIotKLX7yEOQimxY9JH4vp31Igf0QRtd-HbXSJlQ2S65_QCdANNgAHvSOzbRDhCng_lysnA47k6sPtUJbu91hEBCbImIaskIvMEV9c-jP1OWs9XTCLsoeUDdcPa6egrJOjlvs_rdiwwzcS_Usj2j3hwBWh3Fq6nCigWVdcwXZb3puVNnhsN8yIQ7B_zmcs4pmhxc9cFPAVCMuH9gB7KleGPk_4ZSjUeJ1zvIHwi7ZR6kOfV-5Ph6hoRmsaKKzrkCCeHL4Dq9_efdZtr9YZKI_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdpYRAYthU5xGy3D_8SET_J0P4gx9gRd6HGBExOZAaohEobbmFr1NQakoL5KXgzTMpoPQ847X4Cp-9SFrw3nYN1pJheheY9UDHk7-FrL89drg7Kii-nHiNwMZsJwLqKrlxlLH42AY-biFeKzJ6fcFRDkhYY8PjCLo8cwHyL6iUUL5OQ-D2QYBPacKBc6TciS-f--sFWWtvXz6XeBbvDYxOfOFzzX1SRJM4V1wUu0QdNtu9Efc4BhKOdJeAq9CavCLPO5LIiU--ts6JEQnkLV-evaXZaa3GqKwX-ClRmZncdw__VJVmW1oiudPBUfhzPOEl5Lo1Ul3niml6XF4tZs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPM55TASsGk1wDLEQqM3ztU3X4QvwFokPREpmDu7poGqKfuVqQRIlLArq2BCFlPJA9UIXTDa_kkDzEY7NimvKljnr1Kw4HTxcdsK-iRWZcilt74mEcv0lss8X204kQaEQ6Gk1t4KWgJbq2pXwVoU5tDw643ybubx-hG-OE2vtY-uT1LfXE0sUKg3_AIbiCBh4naiORQCCyFbJEWA_OkcepsFWipDnLoMdJ0QafeHIVWE7eb1NCI9Yf0OZZgdAmPzctYKrX1VeZt0V7W_5LhBMn0KFG24V7FmOd0Z-5HUmcSfGNY0sXxTiVdXMtfZ8Rk9sF9txlxOdWot6xT9wVUFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1GyTrI0zN8OAHKHFpOtils26Yiq22-_UQVOOylC15lNojcB4WeVTlPHoB4Jv-4OCobibjujZxYDCiMIPbCwnWQ2mWEICc6N34WkHo4jNcxY6WuCq16h1QKgd-2_Sg0vOOvZVXJFiU7yJspbrUmQzf2YVqb20KF3-NGrHX6xxsY0hxUZycYVnWXq7KjKiAvEyuicMrx1SBZOz4K8LCUWdsdM_23BvRi4fhcM_xII0yzV7j1ukVFI2Kzl54-3Y8UpOiJVWVAQOJJutYhnzR0oLqWGeRpjLZExmI46gWuPLIaybuCv_KVYa89hqAozzJwbfkYJQ0CWkCiqbH0MbcJGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p__keklBgzyNbYy1wDBwY6rE7S0TwcVDYOrv0LaCIW15V78CB9GAu7NajUQGwE-68GSD_bY3bB38VDonlnM3yThsUc77lMXwQcY_SIY-BrNXLcT0Mlkctc-Kln3daK5any9W4ARdMHlNGzda0mlDnv2Vp0gyPsSUo_9sbDOXURim7A7N528rHhaD_JTRK215CA7rMwOqpBAEwmWMsSgAkbyjOBbo0SLwyMD4GHl1bKZERdx9WiDvsDEZ_Q6lafe9CjgVNvDa0dkWjJs2ooN_scaTzCASv102H0-MTTR0rDlVPjLChWKOzms6p8CO3tZabjmb0TRo-hqsMhR6Dx35eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
