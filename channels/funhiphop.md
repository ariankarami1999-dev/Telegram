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
<img src="https://cdn4.telesco.pe/file/OXfZBxJXwcQA6tYk7B0UZw5IjDh_LArjxR3rICAipzw3hukEOejxiFFb4PXc68sVWrYuW3z3YjMXQyz-zGPH9EHElvtiKcKlW1glvfWolO-NbUVBapvobXd5uN0SnlDc32HkiYXj3f1sCjMAA9mSkk3tWA45KCtj1kE2l0VaMxymeaoYhXejGKsswmaupSrtRIaTUEtNAMikbtOgDXzkm1-cEXJ0lHyRxTrTHd151-fLRb4wrNZcEaeqACldGrN5LltsLTsGLNwpfOpWRNnO9EkK3xqpMgBPXXkiSHPsqngEOfjS4Jb9h8dsT93iwNaPA4y5oNKYJCouy86JB5X5zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 186K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clEGJ_EFK4AC_elgA03ar8a1Om_6s1d_S755zv3e59DgVSnaC_aUXRbajv5_5WAUklKpeMzoM4tW2vy7ozixCMRZrOR_HIbj7QRVsDCvbsMN-j2MQ65l24GYdUEvSdaDtepv_PO_k-67L8SGNtUnAhkWoT5nRUHZHitj0P61buP_vHkq5akbz165uy_GcZllcrsyocNjf9KIWA6nkSa48vsh5bV9qwUm4jtDHaP8OGr5XOrB1QP_-klofMGtDXNSpXlVbtZJIBQbHGoM_BJN3BNIrWKik5D1A9wAd5ZudRx7n-AXi3EQ-BPLzS7-wIhmb0_d4CwDv4eWzUzCmmbP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/funhiphop/79481" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osGwRmaIblYvmlYIaubyf2_HNWlobEl_fyg8sNwe4Fhtq0XqNxVEpXLIL8WqZ2Hfzx37PRwCb4P71EqSgY4VfyaktzMXtSFS4R9h7WXF6-isQuVPTvDyD55p6SnpiJGfi65447EJsyANLor0uUl3ocGDTsfJ_DNmEipjXarSw90tAtOYUzs_dwpw-Ej5n5R8DAqgOFq5bmM5VnsJ0gxCQciGhqhdbH7p0tmfchra0x_QAr6Zn4DmfXkBHc-EMap4uIS3E2DJtVKxpHZq3Bj8SF3bEFeLjMd3w4RHj6jY8FkAfkZbAdIMu52d4DJa12-7qjFRbvv5p7_BfEBrKMu4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/79480" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcyV0OYyvOGYiPzVCfafY4Q7vDcMG4CDym6h86bAFsGWRU3KfuCa7nt9Moe7klm9pBl4BpLihDvHF8HaJhdKluFQzVWOInucX_C6bFW2qiwa-7UXJEF_JBDgiYnHMNrI208VuMRCPFzAlYjRP90sQfn12_nWEXUitSTdBq8PXcY6lcPCtmFNBRmUSOG0CnNuTgN4mG4A5g-KL2aDB_gnB7qnfBrjsSvhXQNNcKYuJj1kp65jntV4tP6pFpVtSsGWB5askS0B6ebd1MXpLVgQiurXVGwbNARtHb1Ubog5AYs66d734RMFiUnZCvS0WDaIzgGzNimGHMEzi2aOH4hFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/79479" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/79478" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حماس قراره منحل بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/funhiphop/79477" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoNh_9IYQvIcv53o0U_Zhs8QJTLfvBdiwNAwPgKi0ck4Hm9u53-LKWH2hWhpoz9hX-4zcE_zs3prOfBGfC5Dd4t9D-i61e44D8fGl0FM0DofX30sgZIUEUu0HuUGNZorPOt7bg4HGLTUgsAE0TCTGCeBgJGa1Z9CteYKYRm9vggUgvyamqnbPSzbwkVdInB1YsxLgpX2MxqDFRxnKrU9j1A69FL8PqlmS5zWVrv9d1J35-JScQ-lOycWsnpoableKrHERhQ30ufnfgfYWcMIrXfSUSyYjiH-KYcLrdXfkcscwLwmhQCTUioCHu3TJlSIDB3GTYRZzxwjHQXI5zaUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت هر تیمی پوشیده اون تیم حذف شده
امشب هم که با کیت پرتغال میاد تو استادیوم
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/79476" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOzsceQjFuuxMiqJSolbVFJlkmZiPW29xVrI6_vadVWMs0gfiDyxtlM9qqso_euTioZeVSghjoF-2bTQhhqz5DGadsi2-_PFT9x0XEa_2k7mRDG5DbsUEoA6Fz_dwGbUMfdofn2HK5QJCxqLjGccGItg-KV9lYW6DvpunqjfM43rnhzjfxwfDAI4lNYTp9FYft6NAV8nP6rGT5M_ebCK16L6_JwmsgEqcSCV7ubdLnTZ_6vXySgSW0zXdURAYRPGnrk7eYud6yHQ7Kxsk6BKY5Qifl1O7EE4Ye7V__nA4ljjzvBAl1brsXi5YyCQXW6fQGncaHfWdExh0rBfeQUlAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/79475" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دیس جدید دکی به زنش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/79474" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddb338012.mp4?token=KmGxd5d6sUwfxZSeSnAUmiD9C3mjSGJbC9EeRuCK5oGU6XgN7F5fP4CKv038f4mNhC_nvteA4isZBiASUXeGmd5Dex2046n9Qvu6v1ocNznvJB-7GQSFLCHAHMOSPpe-w-QulRBKO-q0xTfKlhtAhjkwhIBfJssTcWj3UsYCqqN0bqFjuMq37EB-MwRyqe9V81fjO_do5ItUB1GtLg0O5hxLflVdY71_iqzsKoHotHDX0GrrNQgGTg9oMBvOcBrx-p4uDQoL_OOdSQCm-KcK3VK9hQLdH9bCKu4Y1OdtAkAusQuMv8CRHM8-ODW2ovx9gKJVEVpHr4Yp82NllUZU7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddb338012.mp4?token=KmGxd5d6sUwfxZSeSnAUmiD9C3mjSGJbC9EeRuCK5oGU6XgN7F5fP4CKv038f4mNhC_nvteA4isZBiASUXeGmd5Dex2046n9Qvu6v1ocNznvJB-7GQSFLCHAHMOSPpe-w-QulRBKO-q0xTfKlhtAhjkwhIBfJssTcWj3UsYCqqN0bqFjuMq37EB-MwRyqe9V81fjO_do5ItUB1GtLg0O5hxLflVdY71_iqzsKoHotHDX0GrrNQgGTg9oMBvOcBrx-p4uDQoL_OOdSQCm-KcK3VK9hQLdH9bCKu4Y1OdtAkAusQuMv8CRHM8-ODW2ovx9gKJVEVpHr4Yp82NllUZU7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس جدید دکی به زنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/79473" target="_blank">📅 17:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=QxpzEQ21HRbcT6XRweda9K5pBaWLV5uFKxkN-yyvOCu501FVG9abnZ-QN1UR1zx7qUQkBhd7E4dVu4gPHLvugzp3bvrnU3qNhA78t0tshS4hasFaB3elxZqk1nil1JKrWH8brqDrSzrQfWv5p_Xx_VTiEDlKbPZIWmr4fKPLLRKCxyM2kX6LOehpgaBMmkGFZkQCJWlYYQuvyTb8qoK9vH9Rfk_XmivS99onLerAtKzBBVcqUTHJvzWDoGgK_H0o6chdwa1kT7_WgPc6dACQnU3ezODD7gUMzn9Ix74uC6z_pGl3MUW1QCtpCy7ae9B13sRmN6pS2AAaSC0Ioh8YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=QxpzEQ21HRbcT6XRweda9K5pBaWLV5uFKxkN-yyvOCu501FVG9abnZ-QN1UR1zx7qUQkBhd7E4dVu4gPHLvugzp3bvrnU3qNhA78t0tshS4hasFaB3elxZqk1nil1JKrWH8brqDrSzrQfWv5p_Xx_VTiEDlKbPZIWmr4fKPLLRKCxyM2kX6LOehpgaBMmkGFZkQCJWlYYQuvyTb8qoK9vH9Rfk_XmivS99onLerAtKzBBVcqUTHJvzWDoGgK_H0o6chdwa1kT7_WgPc6dACQnU3ezODD7gUMzn9Ix74uC6z_pGl3MUW1QCtpCy7ae9B13sRmN6pS2AAaSC0Ioh8YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیر دیگه حرومزاده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/79472" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امروز روز جهانی بوسه نمیدونم چیچی آمیزه، به همین مناسبت روز دختر مبارک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/79471" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مندز و یامال کدوم سگین، امشب رقابت پدری با ویتینیا و نوسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/79470" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6FBNWKyvppr7fy5Jafb40n331fXN3zFdrCvMnAy8rO2V_0_y2MDY2VhiiNt8VvmF4j_PMu5SEm9W1iJaMGEHmrNXaOJpB3ClxbwgEnXvW3dvDDGLWUqvkbquqOuLiPAqyo1bbqzAr_y--fgDak_wKjT84sPkfC9pVX6POANiOqzXv04TaEi8AoCETXI7cjYECrhDl1q0v_MlCCKkLLGehkjk3zrodKUdHYMH2h3BICPme_ad9h0rXjZME2YszwmsrkdVzmZaTvv4s3CdwT6zgtt9DMu9uFXSgRicT4PKrCucE8wdTCh4r-YNz_N-py0GQf7oY5qLxvZidlEBqwlGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مناسبت ۲۰ تومن بکش رو بدهی دکی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79469" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCoNdpH5W2rs2dCrVHPASvCCBtHd-cwiAJ5AV97flKwWQBVxFpdyN1qjDRjxRAWi1LvCFncF1ognpeFlGv8VQgoAJOlnZ0IWeiKM_L3zqudwkHKx7xiefUaFuy_Jq_8O19AUtlDFs_-BfMPi28DVOFKtp4ZAbVUyxZtZfyXfO8gsl594sFBAhhinY69STK4HZo578LaygLcBhwVKJdlSLYqUuoTifVUsv5NR5BBNkHntGt8P4Paz3SvRfqKpdBuCU1PElPnWFz6rEBlo0uL-uFED9T23qjObOHYZnpB-WztMFacwVlkDUH-aJ9Ch3OSdcgIZeBNDcBmfHOBN0QCYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگ گنگ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79468" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqSPjUkkJliyClbobFEtwbPxbs5we8a9QxVk64CSRgBV00W2u3G8orW3XsW6kFjZLp4xWYd1wbHGDCVXnXgfW1Htm0acP7Xn46eNHW80nRUwrufQ4yWG0jbdnlYTPJatne9f5Cak4sFB-qyaH_lZ3JgT9AG1eg3UxD_UkZw-NHCEPqRbzWMzRTBFuJNhZdqLSWTCF-j6ootDPFg1gYX27u4uDn4nfMn-t6TKaRNbEhFD2YemPI4Yk2U5st-xGtSA3tEidJRnKeW7s_woWSDG41YGS8CYgAE9bVqZaLpNXyBA6RhaTnGQgoF1KyS1tnansxiNWw8PU583jAlRFgPDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام مجتبی بالاخره رویت شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79467" target="_blank">📅 13:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79465" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صبح امروز اسرائیل در طی یک بازی تدارکاتی دوستانه با دولت لبنان، حملاتی به مواضع حزب الله در جنوب لبنان انجام داد، این بازی با نتیجه یک بر صفر به نفع اسرائیل به پایان رسید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79464" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لاپورتا کصخل کینو بیار برا دو سه سال پولدار که شدی برو سراغ هالند</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79463" target="_blank">📅 13:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79462" target="_blank">📅 12:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGR0lOkS3jnTJFcAow4BroXvsDtT_fl8qC0ToqpZOTKiCw9erQK5juo69SE2RdGkjReUe-rLMOItznkvk2cifV8mcP88BmcIiGNf1iwZErc0z6mAYpA30llLugPDV6P64oEPML7FSuacUTDNy2mP3qoHKqi63xbGHdclp1ECfhZRbntssMV70qepqhYj6IwRyPQO_YLAEtGmenXOkp3MTXo4RZ8pgdeI7-dC7xretnPeTG0S4sVxkqH5zIIcfcFZe9-SPZf2Ovb8C9fagrzaKcF3v1nxlKjEHMs77mE_r46Y86oUGNPWuuMH7ymKNW-sH9CdTJeXN3-zDsHafUUdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79461" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میدونستید وایکینگا تورک بودن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79460" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حس میکنم نروژ انگلیس هم میبره</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79459" target="_blank">📅 12:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_eN76qsLU6BuUOVIg3_IszJcmj5c6UjU_bUgbRoV0_bTtfxdzQE3tVPcmqrdUeNmc0nHvTDM19LK8WDP3zhCSL4rx95YbHhR7XJ2bVQY28a76LQ0C6jYbRNtXdPdzM5Tx80K2HJOEk_dgHs6UDhtSoe5tCb268HzICYJL1JsiO4fH2dhg-5YbURoF99VRa2Ynt4zOHeLE8ExLotU5lnKFAKRAy5g_T0PRbDjBIpoQ6IgrzTbdlQ02oCv_cYjMsoTb4l0okg9u9rrzPLPXOVJ2viF0UXAqKTgEMSexclylxNLwcSNNk4K2Atn7t0DvIIjOvEL_Via4omKrnRvJw8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3g8_tl8Jz6x6wmVApG1qg3UHn3qmATg7mjvXasoLWurF2YWyfg-xkQUy8JG7sc-MjkRbx_sKNH3Zk3Q4YC1aUj5JFajy90FeA27vy7usFZ5-l_G2mV52XykpuwTQ3kQj-KXJa2W6iBIcyoeShY8_j_0Scdh_r3XPf-sfs870cXoczDMyVZReWxUUIQ5n6kT-bOMcBFGp7QpUgqbFCvdQOAUhXK1bamRqdpsEL61UCCZUg_R9w6EViEn-1Au7t5ZDtijINYjsoabmKIPx9RhpGR35PLtn65kpKeahKWEWgaYi_JK7MDjpMIb7zLDKL6mnrh0etZhl9-Iv3Zx5dg9Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا این حساب نیست نروژ دیشب 12 نفره بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79457" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2cV7gV56b15PkRhl5uWi1EcU4zmcNTVm2jptVv3V9k6rYZ2ZcSbLzEEN5EmKyp2lQvIXcDhJYPPr9838SFLrh1K0UVl8iGZcCzv8zTS0KumIkhkgNKAYoxqGr7Tl7jV7oP8fOHoeqd8r2no8xSGtnI_gRJ7AyVtLrvg6Ab8wizrqM_RlMdvREpm9PdUMRn_CPOd14vy-nNF3hYkTIwrWnmBUsM11O6CD6CD27MSOJROMA4CNyKs20JAbrCt7enBX7aCZrzjmbAtDMf1oaiNOzTM0I02aLjoryBJGXlqk4_M2OteYSnEgMupwnljxUZfXmA1S6TaSPD-lVHgNwEVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ ورد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDRmHiq1iMP5ezD48PY49L6FFQrsPtZAjWMdNUSlX8y9vO8TU3BBn7f7typIMmSA1W-VjotTEno4vBqgogpyk7LgruhDj5D61T9uQT6WwmHbvB6D2D4GYTnhgrhdo_E0KV5kXfZ3otUNUBvjITxAxhRSjrZkAElUs82OGaebGcKH8hbjZK_FVRTQu8Ot2-4sdnxTFbpiJcSk9V9M0mvCgSn3rq330u__n9ivcfGavg8qKVQwAjohwfuucDKL4eXe627Qi5lTsJoQGxz2mB8RDBo72VsA-tVk2rIAN0cHlD_nVhVb4B2n7DcwvyEF6asQwtLdpSNY-MW1iCzQl7uOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79455" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چه بازی بشه بازی رده‌بندی فرانسه نروژ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عجب بازی شده انگلیس و مکزیک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79453" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE2dkaafq0_xZGeIBRYOUXZchfd4XnDU4yyIh_j1myPfwL7O0mCPK7f3e95UYfNWx1R1VUIAeVnzS5PyHB1d5GsRhyfHZY7Cwyqjb7-V6cFPUZWOtIW7IpDoQbrJnvKmj7eZWgk9IqZ80K7Aw1bnDRo3Zf-CFAebG3Yw_-AXXyURqqySkj9vwmD5A5bWjWUqGr_ThzWtoYuAs9HbLWnY9jjEANVT7Xlnoo35wDIA_D0CXVJWRys5fZBE4aY7scScKddCfOkQ2CzD_5bcjZlaUQyoh4Gnr4dOfnf5umAptlE1i4CWFH7rLQs7Ux39z0h9cAB-561hZ5HJ5sc2u6S-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا تو امشب نباختی، ۸ سال پیش باختی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79451" target="_blank">📅 03:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استوری جدید علی آقا دایی خطاب به کارلتو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79450" target="_blank">📅 03:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONvL1CigMk5JUa-38YivW9d4t7mBoD6GXNdnpUgQZVFIgNDHm2kKd7Fl9DxsuggJsAVTYslkB9T8POcj0FfGR-aYvAhfkBb4UBQ7Jo5nC-pGbCptgE8JW1fafKV_uSS7Osn0edFs4YweEDlSIB8BVKn3LwlQajr7Vj9cOZd_bc6k_cDe4QGBCerNGr_86k1vZUUKYfSGykPGshms-ilSPjyiTluA1rDoajnMGWW-_gdvwL8a-oS-8s9qh3CwdgbjqLHm3FN3B4sVIeOLg-eN6A9_8QeUAEuuU2v1cp0_htpi14_tqCj-P4g_G0yoYd-1OOy31FBhCoTbbZ-E6sAGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79449" target="_blank">📅 02:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هالند وقتی تو سیتی بازی میکنه، بین بهتریناس و جلو هر تیمی که بازی کنن دست بالاتر رو دارن تقریبا، ولی تو نروژ این شرایط رو نداشته هیچوقت و همیشه بار تیم به دوش خودش بوده، دلیل این که قدر موقعیتش هاش رو میدونه هم سر همینه حس میکنم چون میدونه که جز خودش کسی نیست که جور اشتباهاتشو بکشه و ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79448" target="_blank">📅 02:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79447" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTZj14P5m5CEbYmjkA53m_HBq8-DyLAJ4Jbgog2q5KEvPPxjWCkmZFtK5Dqh4LSJzTd3oou2-iQ3tHarPq7i698ktj4YproeiYU6eNs6GfXSBqNyJdR6Gm6P2txw0UAub-YoWDUQ24nsoiTfihwol5moqhiTAR1PgLQDtP4E7Otu33bhSbaHfkesZ2O16MfGG1IdxgcjCITkScs6wraQxd0-IUIiBiVuaMUZWXL6p3uwsmqESuuf6Q-TfhsKH1Dxrl81lK1Zcb9WvzxDTR3X60clo9e5hMdGtfsrf_5xgdFKgl5NmPW1z1POI-fVRzeyIbsAadj3Ly2tZJ2BZayl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اندریک وقتی یک تنه رید به امید مردم یک کشور
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79446" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بازم چیزی از ارزش های نداشته‌ی نیمار کم نشد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79445" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیمار کصخل تیمت وقت نداره وایمیستی اونجا میخندی و کری میخونی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79444" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3nxo9q_12kiwU0pFk46xl2T9lmKtiZZTllv63N-M_L_dMvJ2NyyoAgF-0qvr_mkWYkpwrhMN0j1uSNZePDgvMihz9z_N3oKlIZH7xWST665fG9c-Rqd4chld19wWE3KT_rNamesx4eMT9f8PpaD5_Zi2fbYBY1eSSsGrP_F5j8D20ymk_OBWXl7Yd93Yaro6eILseyoHH0EOG7BXK2suMhlNRfdwrITc0E2XZygQrBRfhxA8f7jt1Vwd8aO2PUctnK97JfmH6lBxRaZ4_BqalVSd6okOjZcrhj6IjTwpCY03dq0RD5Irv9YI0UVhiIb4QexdXEEOkZC-ROpwhs8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم هالند هم رفت تو لیست برترین گلزن های این تورنمت کنار امباپه و پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79441" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ریدم هالند دبل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79439" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وینیسیوس
😂
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79438" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مهاجم خوب اینطوری کار رو در میاره
هالند تک موقعیت رو گل کرد اونور بازیکن های برزیل انواع و اقسام موقعیت های عالی رو به باد دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79437" target="_blank">📅 01:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیمار، شاهزاده فوتبال جهان که متاسفانه پادشاه نشد به بازی اومد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79434" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کارلتو این سبک کصشرشو تو تیم ملی برزیل هم اورده</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79429" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انگلیس به این فکر کرده که بعد بردن مکزیک چطوری قراره از مکزیک خارج بشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79428" target="_blank">📅 23:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رضا پهلوی یا مجتبی خامنه
❌
رضا پهلوی و مجتبی خامنه ای
✅
بیایید از آخرا فوتبالشون لذت ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79427" target="_blank">📅 22:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0tg0DJK3K69WWHHzz19kYaw4E9dUQGscYeYKm8TnqMUDNUG2ylwVp9wUmG-2dA5z4fhHOsR4TlzKTFv_aqCgepanuhUYg2Zcji6yIg_oOUfSTz4LW3VXezga91vXAolvDKVIF9jt-TIzKomKei4rSLcdYNe-u3vI21Qv-IrUQX_LJKRtn86RA31zuGbCunax-hgX_dTyS5SgpVe0nfeKGwmgXzcg6v8FZkO8Sud3xhLVpG23Jp1D4K-OUdw5eDe5N4ky4WlvDGMUOgvIHthYaytLf2eFHpxfcaB_rE5EWvAIc1JA-IVEhgXUhCSdfe88bfcH8D_bJNwik5Euk0OzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراماها توی ایکس از فان هیپ هاپ هم خنده دار ترن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79426" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH3pIOOaFZzCuazTGTXVhQaiv2oZX4hA8MoXTJrvepLd4IepRBWcqEOamjVLbxPQcGlY1Qf1CpteitYGPbd83yCrtjVjWk2YJ79zwgX2syecDDRsjOyyRJfCkgwA14wz5bCvrWrkVQ7F7VfGsMIDMyQByBs6Rhquzd5WGkTEJvFxV93ddW5ylUWcCZbYCaq5sj24uGrTys-a1XB59YkUI9H8FCBqJb8y72H58OW0GQMj29x52GP9ZBl__lYqfZ0sTlWiYw9FVrRl3MoHQGjCf9HqMSYyZtT-68gA4g2heUESJlJV9CnMhFMKYjvX1lYy3xBmqRwmZhH6x-KC3LagFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا،تو بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79425" target="_blank">📅 21:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بدنسازا شروع کردن به خوردن کِرم، چون تو هر ۱۰۰ گرمش ۵۰ گرم پروتئین داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79424" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi1z2w3LZPNTCff1iKA-A0wn_OcL-yUNS2wF6lSNjon445a0orxCHHhm3afJDWf_UP8guvnHUp47yE_2WoiJLx3K6AEtb2qIpaDLnffqBIeeMLbf8Nbo3hdIkFtswZCOx2tuQjkBZQBlfkFIt9hUugfgDo5PuoD3xt95lb4ziA2d2cKedUod65ouIG9LV2ldnEI3RNPqqrMWrAVSWoBwIBbQYlc_n6xyT3mAoJu3uMPrIErOQo6-AeYqH-ekmZ8G5Ksp62uRilJHa_CzJcHsNdNsx8TgOPqfjqZJY3_ncDcyVcGv5XJU0jiLyzCd7me8-u0Gt5ysjDrdhCQRMe-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بعضی مراحل GTA6 باید برا لوسیا مانیکور و پدیکور انجام بدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79423" target="_blank">📅 19:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79422" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اگه یامال جای اسپانیا مراکش رو انتخاب میکرد واقعا تیم سوپری میشدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79421" target="_blank">📅 19:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Du biat guta guuung
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79420" target="_blank">📅 19:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIULMnv-vlr3g6rbYF_lPFbTKR2yQJr4b6ST6VfgwcZ6pZd3552mFkl8t8X97X5Jo7NpIDkzI13ZaHApxjqBRtejJZF3V_mOx3-CgY9-P4lCZMTB6RpIxz9hqSfaNdDqJFwXZEc5eDtd0Gv_neyp7VyymMMvD92lr5qBQV2Buj48_YBCwY6EHELbmjZ0r72IDirZKlp8ChqmvPvCHVWkYCArjJw_WXV_iZdH6K_H70N2wNIffUUR0X9jIvtjNHytzzmZ67Zn-2xtU5_sugj8EeMpylmiuE9xVo7zznmYebuBESwsWwBeX7d1h8ONjMwmu8yr9gZcfllgjGObbwaLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79419" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LalXGVZOw9nnN_EmDH5C7vhmFEHmYzZ1W8Q3fL5kwZ8paUqfXnglOsiE1tlESycnT_N-oN1TGkx440XDAAFPN3U6rUWOgjcxtJ32ZfbkiFt1G_zslpfwBooWWlAkEpOTI0y2entCquPIOY2jkavQoF7R934O3FgxltuhL_2Zi5ZghV_NFrPuYqsZtxruInTHRIaUjrJhcPM6MPTFmfrEtmbUBJ8y7VMLVT3VuhpVGBwuKbxONceQs92lL8ie3-x3XrOXzdxE4bZtHyPLZua_Aba6-kKzzZhLRv5J75x8E12Wn46FS1hmTSpcPH2wHXDXYh09i8bChwJ88O4-TUL0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین تهی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79418" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmRQFTSsktgLtsGIlMkjkscwRRJVoNto4EwR1mhBc0KR1JFYsILJf0kMg7ealEzQnjrPRm4Qok-ajrhq-EOvn4Lq9gYjSdMDSNbqLtNVeRSRdzmrXKFI2CbzeQyL_3Po3EaEKzJsGLBDa2OsaiLm5xUOzujGBksrWN26v1G1Wpiqb4yNLfcKg1InxFMzS3V0l2N83DFZMQxVJJ1TPe3OM-lLP2NOXOhTW6nvPYxgrHEYM84tyD7w_OTIvC17K_kE-hTRvc_eZdWLkhTY5TVWupkUBfwLUnU4doOmudEBmgbTXo-cmDl2Tx1DIq4s8HAPFP3HNUZiV5m4ZFnPR6ufew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYHrRfT1Akihhs2Bg2j8mLQZoRxzbzm7iniLUitRovDb2QjGJF3_1RgmN8ZEEZDiTuxJ_3Wxo2LKQchQ2GSAdvYekwPiBCmYoU_nDYZ-ABcbVyIffT6LQFB5dLLSvmEM8nBUns-fm2DNhpoBCI_KlWBQrqw5-v3u3mavf977BugWhwvUyWST-Q5YWxHjPOC_iGpcNt8j1jH7O57DAV-XD6f6O1sns3mwzvbX6vr9mXD24kG3TqqN_D-TaVPOlhNPoADhOrW_awnUKIXd_KrBeKF21HogjlBywY2zVNbdNA31_Vc4zmjYjgnsHd0RNUXoxwmA45rTMBSE-xKHmBzJmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت جدید ووزینا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79416" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH9e_UO1pRb7vKqaWrqqmuYqi5P7j1IaWCSUFSQu03Et-3mAo_OH00ceX-7lDxzY1nEG_YmnWSavdIsSv6fpuHRZvEEenguRCORSePEUv2y1XWXm8pO6fIXC0AY4MwXjC8MJIJDZxPM2a_QL1saF7kSess2hs-UFDnBkMo2PLTkf7lJ8guj8sMe5Hl-dpc3LgKuAsDCFw4RMt07QMgl_7tEiKyRg2pu1JnN6r--bWC-SgFhRfAcYce-rumjKc3hmGd0yhdUv1RGPhSY3OoPDwRhqGyX9qRqV5psfmACygSrjhAeyaw2enf2pHRhTZk_RUxc54aWat1669hJu0q3Gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79415" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7XXW02ryHTCKMbCIAfszBX3GcSVowlNG8O8Y2H1uJZGKW-p9rHqRNWLEKG5t4XRkGpwZSzYIn9mlLgu93sufgOr0czJk0JrATurjgZlO--DMh0cQzCg4KRHPDtnXeIZhmx25kO9XKvRYOWbCb5kltONIVfQfMe_Q7CGLA8yuQMM2ZJMF09qCSAEN3VfTIiQszvWAD32PJgbrjLfQMwBz472rJnbHh2GJ5idwWkya1mTMeVzW7cOl4SBGk-9H4bk_FGdGdTnLBcsPu8YT_giSxTYTOJEp_MOAKulMTIIVl3rnQwKK1xtZGNogmhgwclLySVMs5mro_IA2RpJxb1oxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینو طارمی گفت مسخرش کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79414" target="_blank">📅 15:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFyzizIPImm9lJzcUWdJgzU9GKpXL0Sn2l1MlAm7FMVVsQHpTrRLM95ZRa7Io5LvgNgzKobYcyjkgGoyKgQts6TKB0_u-hicjd_ZI1ugsewSRTWxYVha6ZvxJui5gA2XrtC4aCEr2iwQuIGWqkrSQ7CRsA2hA2sSlE5hy_iZ2QWnlMy7RA0Y7_9BCSw0U2Fn06D-snzR80yaiOpX31V_C21NzqX3MvrkaIih38022uLdspGPsFphgKBtrDoPCh2I0IPc9pTfvlkZEXYZxIBBNfFBW2_THtWjm6uEXFp-5_RwZXLHRoFTYdd8GuU6h4EO05_7r7zPOIRBIHDC0-ZHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصکش تو بارسا از اسپاس ۴۰ سال هم جا میموند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79413" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=P5-MOoRrlqOqa6SUEyzFl1hv4jihrwcQ9DBFWfBloWk49LR-eTxDCmIPkQ4aUfNkLuTZ_ByY2oknsgk3Q7limqmhQZJziHwARAeYKdhS_fEQooqmWp0vpsVQGJzNwTQGFUlP3RaEnsYttx8S7Yxw0iny-3QsyFJlrpt-VSwxSTQ3un3XpmM5Z9AE4WSAqVcCeHa5Du_RMoyDa9G8yeGEL3evaL0dYWx-D45q2n28MbGImI6MJu42W-5YDqAE4aCqpV9-10pCEaeM4fRdU7OxP5AFTTL5JuoQLpaCARfnAH-g8A6c47Q9OWD09EHyHAudMi_k3MfcIrDGihKO0QJHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=P5-MOoRrlqOqa6SUEyzFl1hv4jihrwcQ9DBFWfBloWk49LR-eTxDCmIPkQ4aUfNkLuTZ_ByY2oknsgk3Q7limqmhQZJziHwARAeYKdhS_fEQooqmWp0vpsVQGJzNwTQGFUlP3RaEnsYttx8S7Yxw0iny-3QsyFJlrpt-VSwxSTQ3un3XpmM5Z9AE4WSAqVcCeHa5Du_RMoyDa9G8yeGEL3evaL0dYWx-D45q2n28MbGImI6MJu42W-5YDqAE4aCqpV9-10pCEaeM4fRdU7OxP5AFTTL5JuoQLpaCARfnAH-g8A6c47Q9OWD09EHyHAudMi_k3MfcIrDGihKO0QJHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای خاک به سرم این چه کار زشتیه
مراسم ایرانیای کانادا برا رهبر شهیدمون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79412" target="_blank">📅 14:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اومدم بگم بسه دیگه گاییدین از نسل یک مووآن کنید، نسل جدید گوش بدید، چشمم خورد به این پشیمون شدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79411" target="_blank">📅 14:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیشرو و اوج یه داداش دیگه داشتن اسمش امید قدر بود، اون زودتر فهمید تهش چه آبروریزیه از رپ کشید بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79410" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">علی اوج چقد پیر شده پسر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79409" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تداوم و وفاداری رو از پیشرو یاد بگیرید، ۲۵ سال گذشته از وقتی شروع کرده به موزیک خوندن، هیچوقت از کس دیگه ای جز امینم اسکی نرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79408" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpJ5uGsMg0YdfsHz605ZrGaZP7l7m92hHF3IoB2mOYeuMDQsFA73wNIhJV1GEgmMjxFnFNqvx-tdLMrgliUeuWQCDnSMgQjaICfbvcl-FYIayHkqBDEc_aaapfqbq8-SwEm7MPBlHlOQJ1Kw0nmQ9O-T1dA3ROmqUqDcfxxzM7LyhfbbUUyQkZ9-ukqX-5pEeohBk4koUjS8GSZkX4_pAlRjuiONCZuEzGeJ-qb-y94MTSYWmGyZXKS-bFZgXib9-l7jGuMI3Tzcq7NTWRN4VPBdunT9SF0kmREdp1lfax1hVhe0HnCS7_ShPypZKzdysnjuQ6R_TUv6QD2xIuVlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ch3QJwLtDmTofDg_L3BGf8P78uDw8AZe8oXvDWBcimzVzA4MzIqywrH0OPWeOQXuJkXdN8JJUmVEk1N6oxk8pz83gshqmPG5LajIp-MqB9xI9Qd9HI2MYbtzd2CJ49AF9fBTvg4cvl0JN-sb6ilxUyNKUOGuQOXahCkR3wfoQLZENVmUd4m5p5JrNfPkbLgMAeSe0Nqj-9O0kCKQI9n6F0iMZvYNAGY4H54bkxjJ2KvLbdyyov7F-NJAF6yMOQ71KcF1qpBp3HIIz-DTsXSTafFm9tZQySkd3YSl2NosJ46yjBiQBdV0UGWA53bmGnaKLhAQczGsJ9e5OqKsoJtOJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79406" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه لحظه حس کردم با ماشین زمان برگشتم سال ۸۵
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79402" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79401" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPH2FTwIKA4_qWmiqh89tEWtIFD4YU4X83MhGDpDlvND0RD58_SL9AfGpLBDRdAadMsAqByA1oHpJCndVwn6FCvp9vcN_I7zGUFBf9vGXvzmbkO5kmZc04aD8EIArRfpRHp8_BOXL8Y4H8cs45YaMjMkFgJoiIislxpAwxIIMisq1GTQUfYsI8BbcUh3s5YjgH2x2xDq8XBNlPJPf6zeUOP8IigM_uE-zwRYRl9X2cN66jrNlXTF0CGv9f79b4-LJbvcQn_-BssoN6X-j733-lpwunP3PlEHTnUU2gscouN-RlM4LZmvwtl7AjLctMYbXQtgotyt4fNF4_gqcbiRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79400" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC1ixuKumSAVM-_NOfOZRmdkVASpOuwjQDIfiaYW2q8vn2746JqAu21lmo-EN0a3BSmp2aU8VMBiZw1Lma1iMNgasAkiZGUQM4URam8nlN-SWa6FxmZ_JeKG6zonjMq5ueH5jeDkt4F-KnhGQ0IoWEhPUi7MkVwEkdaBDqmlkAc5AmjViUmbHPC8mPNcnfYj-02MLxwLz4l_tcHjLwHVW2iSyQx7OmIb8dO5vTqDMY3HDs41Y3su3ZAke84QVWXU78iHsqRbftS4PI_bM7r48QsmsiA24dN4ldJzxvJAbFAn6wfFAPunMbCfvCcnpuydX7PBVtgBKqoY2w4r16Jjnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربرد این اون وسط چیه؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79399" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awN2Hi5aOLoVOGrXJ8VXqI89AF9HUn7PdE7CBJVxtzmgQxUMs05n5Z2agbuns2kR5a9_sCuZVL16iIn9l8O42vkL8gS4O1QHekRzZ9haeXj5u1aOb5JYhuCc8QJ3epy5YiRUTiL3NG0zFjQo5aGjqU9kjZkq0ij8EPUeRicfsrUy5_GAXviIGjbzz9uPcQiiJQ83s3R3vG0E_n4wvH7UJwPbAeRDOoMvR14X4n38HDF-TezaefJawB3zyAfwmqi0BG4NuoYxic1k75ElZ9T-YNdoqnLt9yBmC5fNXT78A3r29mimXxHcE2ibD64HGn3R1K9nf3Tc6vmpn8pBzCW9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان تصمیم گرفت یه مربی خوب دیگرم بگا بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79398" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تارتار سرمربی پرسپولیس شد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79397" target="_blank">📅 13:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZB5BWjSEGrJzz6xwWYcIwKjVjHJwBSf_gcBo8Ky-7jGEZJrVkqZt2CDoFN_5FYrAYolJPxnJL5ljdm5YuQkgPe7qKm8IxTntRxrCiwx4FuOP7coJZYe4cq-HtQCjt2BcTxTCX6UurGoQ2r3jX9gcbA77bLBMY8t7v0JZ8KYPLo5DrfK49-rTfG5k_hcb2qLVR5NAx6CN5xJs6hnPg5_pxgPQqZKz_Y2Fo3M1BGfNc6y81fHRmZwk5241aujxmuipQjD09FyH5DGj8lpHFNLGxnCx90d5uK-NYpw21CqrEcBi_xOZj7jNPoEfBxFCyqHWgHEV8ea7hxcg1kNqGUlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MEGA BANGER
😊
😄
😜
💋
🙏
🔥
💥
🌈
☀️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79396" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPwD_mGfDkz73QDyiveVCr3OJgLOyxXQoDHxR2B7ZvqT6LsO4XlakunEDt0uxUPUNdIAVHD0VZkJdjtr-fDu43UXcEOM0SszpGoGG125_6YVqMHhAEVdVM3pRNxsvprjL7_U9RuLFTrt9gyEWgZq7Hm6AuF232KtECy0YJMT46TYEkb2eNfYHXvGEOenY0Fiu_ultGnnLV4ZtoByQWtvKDJgKTH4et3ZoBOyGT7LK16kTlWoleHARPGELrwTWFYsDc9jfkMG5w4g33rjy2GN8-snV_SGI9WM_3Ka-cKrj63o3doUpmYykOUFT1C17eoHTU5S1d63IgViLzDRmj8kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79395" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انگار بکام میخواد دروازه‌بان کیپ وردو بیاره اینترمیامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79394" target="_blank">📅 11:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chYc-3OD_RErQoG2q0VjOSPYiCSQGVWG_298Cbvw0545LFCYQObW7aMPl7P8WWaMEZ-8-ZJW1JJxAWpfvmoD51ckIUye50MxQOTkdYIM8JOOEJlKLRZN8xw1D6Am_2-mX0JdjCtOU3pv4CWC6CCf14NEzB98dA37kJ2cnWY91V4_Tw3qPH0t4uAYKhqyWRLa6I371qCmeEiG5x2uJmUgdgIB9hBNTaa79cvPUQ4aDPOzdoEKhkVq_4RSpKs4SJMF_KxLnhxqM-NTBj8GE-AUU7KhnwXqDXi3W6Qx0nFCnx4ba5reCJkH1MrXBlfsI6Cq78bRlfl1Y-o3ZLrWVH79Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه کصخل اگه ایوب بوعدی رو نگه میداشت حاضر بودم سر زندگیم ببندم که سه دوره پیاپی قهرمان جهان میشدن، تنها نقطه ضعفشون همین هافبک بود که ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79393" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh8Lj-1S5zkrVYLIuJ88h4KWD4_mI1b3Ljv4eU9AmSxxWLGpRIUisSbysMbSVWCCGnj3qb5WTVv21Gz5FipgA-LYSjJ3alPORxy_tV_955enAPOlUCk1IXgNSEaIeGk33mj4CpLxOoxhqsW8oassrspjYAn9jYvTqe4v14ndPxxE9EpRO8URq6mmaKerNb4wDGS7ztNfqCQY2OaCtVhd4SHnJOzIs-Pake6qOyqDdLG8PB8fPWt88uCFXPqbEhLCoOtnSUhKXBHs2GPJbElwiMdR7QbWip0jEeXOBXd6boSYWqaHtfrfZZCB5-G4JhptNYqv3MipIMuah9HMWGglwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی هادی چوپان با علی خامنه‌ای.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79392" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw5kF4A7r7UZ02GAMgQXGVwXrZ4mET8pVykpw9DRJUCchK0NjFqgvEkv_7MO_F87w3rg0jKkAc_kn8s_m-yMn5vBpqYBddy0lWV6oVk-7IxLfTx5RUXkH_FyiYtpVSB821cSaNatAiMLM33ZijiZWw6VVmhQ_t0tsf_xp0hhWJ9SeIgUdQf7vDbrTN39dWkLBe7ulswFJOtPR5OM0kY2r1hgxwndWauJcwob2b7FL7Ag0G2upS5ATtu-gKmsYJ_UNpGBjM0CKXKJ6ZSrRv8KMx3UezjAKtcqCbgJFXiWzlzTK4nugKk3bRBlA_2C0oVlRO517ln7gMr0G-bb9GeWEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79391" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwfM3SAJDjX6jrIuaodoMti0AGKhmmi-i70xxXcxpxxNc6rISC68_QEn5PXAvvZn0I1Speb0kQp-DDVA-k5ePbFXWiTR7VgvBizuxneAD_-zdiK_KDUEpewQGPvzLzhJu9YpF0rpBVh1ENB__ZJH-Peg7b7v0R4TiJcsHIEV9zVYhUfPISIQmPmJg9YjQlFwfvVnsU1Z6kxCuw5YPjpkRwwb4IvgF7m_Z83FF5qGtBdO6RR8-hBIlt2V-LlwNu-YMyjHU4divf0I5SxRU14HAkEjHUiWp1A3F287DUr36fhbKWoTtJQiuD2CcSdJeacektot0TwiPcPQA13VLbhQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستا هم داره بامزه میشه ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79390" target="_blank">📅 10:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چی میگههههههه این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79389" target="_blank">📅 10:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به جون خودم داور رو صفر کارت پاراگوئه بت زده بود</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79388" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF4FS_o4AnacEd3Utk6MOsHLHs4w90xTGfctOpZjdWgIIJcpa7BtQpO73suo7fIRZaT75gPP0M9HRUkL2cR98S1BsZMLG0aeIcS6qPx_Th1sY2ZYC0DoJ4bncFequaRZAft321lWPDbyil7ozdDgOQvL8neEKdee8Acw7Z-i07JFuO558Z28d78rFVcO1So70CwVwb9SmCewBcatJzeFIG09DYlgfayLyNhRTsQZ61xSwpK2v3kaU20sYAqAINtwByhQszzk7ZcP6U7W-zdjd8NMSmylG0-oMuBuT_vhjinPsp_guk0JleNn3o2rPFWdqxb0qEKyapGX7PKC7j_vCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید دوستان یاد مانی هیست افتادم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79384" target="_blank">📅 00:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klqUmOtO1Irg2L3j1x5ebmGmLjZgWGskb4wj1sZwDZjgrREw6VOmi5Hsozz88Q8ZrN_Sv5hJrr1jVaIJq3_mmbk5FvSqdyQukHKt2reJYwa1oFopASM5_PNL0eS_axtY-imcJc1QkAWPwG3LtlkZcy5A7uY3E47rI6AFgr2QX7URfwzPyeeHP2u-deflgvT36wYATAxZuk6lK69AM3CsYCk2oPlxsQ_8FqGXEExyParERnHGShh_gvAa4gyBifk022QFim7CqlgJI-peVxcaIQj-JhN9fVf2ldIA0F1Weewu-3fjkLq1WpfjHZo6TpaeIKJXgixiCVNBr7I13zyE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی قبل از یه آهنگی که قراره نهایت دو ماه تو ماشین ملت پلی شه و بعدش به خاطرات بپیونده:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79383" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9Qal5hIivZOayc_4EnYEvBlizj-wFXh8UJCd-KWUMX4E4QFODsk-7eYH-gZIDKmDtE-M_Cx_CP9gj-JvfVKveZ3ZoR1BArqO1VlsGY5qZRUdoGEPdMWf1zWxDfK1HN8C7GcfZRT7Jew04Pnxc6Mnck81qVebgcHKC-AefToqs5PwO1JP42I3t37ELfKZ0wvKzAk--RMWpole9l5YMEwPnTK0ASi0rqN4NcdmZ_vttMwj7cRQwji_AvHIXrQJ787s2gSIlT5ao0xR4FKC-V3GXZIA-C2kQAVNV757PsePJ1TwYFpPFbZztVNsjXYebceWfC2-JyOK0ixuUZFq514Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جور و بیداد کند عمر جوانان کوتاه
ای بزرگان وطن بهر خدا داد کنید
گر شد از جور شما خانهٔ موری ویران
خانهٔ خویش محال‌است که آباد کنید</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79382" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=e7ingOl1g16bdW9bL_7p5lNiQQ72fHkHK3ZHejWfSakGsoTb1fb8Up0hU_OtDI3auGqMpTGxrYGIftgUJADcsO-G8f1gaSQh7XYzXHjv1s8vOiKZpmpAbiUQtBGU1VesK5PDvCsWB1XD2qM1BJSH3ytopxSwY4Cms07FIqZtz-ZUqfNm3cX80aRilswqKTVq_ozeK6YzqThH_HtnuoEKAgrxzkWwZIGmqMoRpSwcLXS3_x4MaYcmtq_U_zTyzTb-VCfi0wKn1NK_aHwwGrreCb3ci6lGBpVT0yxp9mN_Z1-Xu4fmwD1e4Ovqb25ZF7TR4ik4lFQPQWgi-X58ztjQOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=e7ingOl1g16bdW9bL_7p5lNiQQ72fHkHK3ZHejWfSakGsoTb1fb8Up0hU_OtDI3auGqMpTGxrYGIftgUJADcsO-G8f1gaSQh7XYzXHjv1s8vOiKZpmpAbiUQtBGU1VesK5PDvCsWB1XD2qM1BJSH3ytopxSwY4Cms07FIqZtz-ZUqfNm3cX80aRilswqKTVq_ozeK6YzqThH_HtnuoEKAgrxzkWwZIGmqMoRpSwcLXS3_x4MaYcmtq_U_zTyzTb-VCfi0wKn1NK_aHwwGrreCb3ci6lGBpVT0yxp9mN_Z1-Xu4fmwD1e4Ovqb25ZF7TR4ik4lFQPQWgi-X58ztjQOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79381" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانادا پاره شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79380" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مراکش با امید گل ۰.۰۹ جلوعه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79379" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یه گل فوق العاده زد مراکش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79378" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8RouMj0SjnluhqlCKrUCHA9aqkcMUAO4WoX6kCmd4ikGKNMWShynlaiu6Tphf35emVql40XGRTBP8W6pFXpPvDrcVpDGMf79bP1pB9sKrJVEzhMvUOFL46rFD7zRRwPXlab2yWWtdYOQLG2uKKswyx4Pvljl_Amm5olLU8ZnqI9uPWENheQqBxK_4X_avSeJN8alyTcGEBwssPNjZBZUmR9y6NkvwkWhKcTFafFHOD-ZPVX2L3mPncKBZ4E99xWDKaXCy-vj7SzQyFtVAYUiwkDSkqtB5XwHD6DAm-EZ5zPtGLe-gpMPM7Y4DZ1l0HNFswQJ8jV9vxenErV4IJGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امثال توماج عادت دارند دستی که برای کمک به سمتشون دراز شده رو گاز بگیرند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79377" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku-O9uP4O-WhHkQeLp7gDmtGKVumRBJMOhVD_EvwrCWhrWwCKja7p8nPqZ7zsW_s02UYnsy5ApHBnplo3yN-9fT5zMFcUwnK4eyLRlbAP7giIk5UFuFfnTJ9c3akWPsVlH2hOuvRIqenGn7R6J_Pov9RHaSZ8FsUhmkd9Naz_I1Xn-HMjs_ca_T9yb4mvFy74Aiqzo30G-ztI5xf-DQQorvKXcaj2CUe8UEvwaOaLlm-3kKt9CFXNgmbsWHZOzmmn9b09lUAu8pp_Zfzbv5NYhB3Fld3Hsa-YvevUXCc_Rckfqs7oF4rOQr_ahTgr_WALz7UX4eKDpUicKVwEb2SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79376" target="_blank">📅 20:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCn1ftbOijSbmxal_Mc789tgSP6GZZYRlMNjwwSMF5Ob41olHtom-nL4EHwBSLIG7v6ZokO3o0m0giFUD2W_Bn_Ha5Nlb1t_L-1o2aRJ3SRJTIVvdCUk5KIaT-rZCKyqXX83afhKVYdds176TzL_wYsn5CEjBmiuCtC0wWIkvFaJYGP2-xV6ULiIFfNr1Lv4p4IhFlPRRaYdI9N69V9vR13e7GGoLRfg23KfMZC7tZ96ZXp3pzJtUR9W-2DRFvu2v0t6yzb8UDVIOHajDs7mMs1RhifguYLayrLxGoP-kZbZAcdyG2Dr127BVIIAbZK6kzgpva-bKBceDtfnug9csA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین بامرام.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79373" target="_blank">📅 19:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjFcb8DUuwleDKO6PaNjpD8BfXEGz8RQTOUG8po0c-HVqbaZSdareUg7Yy5LGqL23prvrZ2JwepdrnTAX9qEDdBEU6iX3TMLyt1fCT0NsUU_ipyDcYWUkfNa5GYKEYECz18zt7N6LQBoczIkDgzulYYr_J9GON5PCqKniUyBfvmNobQagaU6w_CuJ3yEXGud0xcL5wkSHWrWb2nJ10a2f4rCPmR4tSjZ2HZMW1HriMjPsnmOyE0Z3SXbo3gPvrDTpu4xrqNwpWTnPbZQXjg_s8XULQqvvgw1XSXSkNksZTgCxKskp7vt4LfG1fB34MrzKEZJO-z3VCv6cdNEs0EuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید رضا پهلوی:
به نمایندگان خارجی حاضر در تهران که برای سوگواری بر سر دیکتاتور درگذشته ایران، علی خامنه‌ای، گرد هم آمده‌اید: ایران در حال سوگواری برای او نیست.
ایران برای بیش از ۴۰ هزار پسر و دختر که در تاریخ‌های ۸ و ۹ ژانویه توسط خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به قتل رسیدند، در سوگ است.
این رژیم، مقادیر هنگفتی از ثروت مردم ایران را صرف برگزاری این نمایش تبلیغاتی می‌کند، در حالی که هیچ یک از رهبران دموکرات در آن حضور نداشتند.
آنچه امروز می‌بینید، ملتی نیست که برای حاکم خود در غم و اندوه است. این ملتی است که پر از خشم عادلانه‌ای است، و این خشم و شجاعت قهرمانانه، بقایای این رژیم جنایتکار را سرنگون خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79372" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPZJChVC26LrBcKbUKqsQ1Y7UacGVg1zjaMZKH2VzAIcXpuO75Uo6I74Jzhz1kKDalhnKFYfvs3rFueCX_drqV2NU4LY03Pna_diJ2FWeoT_rpACWb4uasm3ThbEIGsLihH2MvuefSutHok9DOMdyFjXKWTnBHLfgWVKiaVytUUrU1tI-L0vfblUoAkYIWc7D5azDQem3wkQ8HwoAXD_jwBHJ2sK26IAlt9tYqsQd5hFuIe4-3NqNwMeHpVn0JAAVs0vkJN-F0DvIHLVT2paGWLZB3SgP_wI1Fxu8dn5iaH_-lsmn9V_mCNyXDuASxjXUSILEhh9KhYDlV6l3kaoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی اونقدرا که جَو می‌دن باهوش و فهمیده نیست واقعا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79369" target="_blank">📅 18:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الان تو مراسم یهو یه پرده بزرگ و ضخیم اومد جلوی تابوت حضرت آقا، ما شروع به اعتراض کردیم که این چه وضعشه چرا تابوت رو از ما پنهان می‌کنید؟
💔
💔
💔
که مجری برامون توضیح داد به دلیل تابش آفتاب و وضعیت خیلی خاص پیکر حضرت آقا، مجبوریم فقط چند دقیقه تابوت رو به نمایش بذاریم و دوباره شب ساعت ۸ پرده‌ها کنار می‌رن تا دوباره بتونید جلوه‌ی نورانی این تابوت‌ها رو ببینید.
ما هم نگرانیمون برطرف شد و آروم شدیم:)))
🫠
🫠
🫠
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79368" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">العربیه الحدث:
دور جدید مذاکرات ایران و آمریکا ۲۰ تیر (یک روز بعد از تدفین رهبر شهیدمان
💔
) بین ویتکاف و کوشنر و باقرشاه و پروفسور عراقچی برگزار خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79367" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم  می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79366" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=DQ-MNkzuF23TaHW201PekzipXouLSdYKnghlJZ-vqH0DyNMFuln4lRkQY5LoN8rR70JwhMx85D34ZF9hWaKq_LtRUygUZoLO7Nt-883Wqsl8FQh7eAURiWDWroDT0qftwstI6mpWUfJdGJNjVuQjyJX0HUlCMErqhOW8Qvec6ngfpuJuYbucsaEEvbXep9OChr6oFb8KK2yTkuc0YkqhiPjybv58ey6PAUMqu_8PXFLtL3f3T_Pocqhydu1-1kucYtM1qH0rmWUzt5ojIvWP9_BFj0eV2ABr5Eoit-LT7QWj1PmMd-q5Z_MbrIdBjaOqX5NqNcnuzSTHL1VmHRWbEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=DQ-MNkzuF23TaHW201PekzipXouLSdYKnghlJZ-vqH0DyNMFuln4lRkQY5LoN8rR70JwhMx85D34ZF9hWaKq_LtRUygUZoLO7Nt-883Wqsl8FQh7eAURiWDWroDT0qftwstI6mpWUfJdGJNjVuQjyJX0HUlCMErqhOW8Qvec6ngfpuJuYbucsaEEvbXep9OChr6oFb8KK2yTkuc0YkqhiPjybv58ey6PAUMqu_8PXFLtL3f3T_Pocqhydu1-1kucYtM1qH0rmWUzt5ojIvWP9_BFj0eV2ABr5Eoit-LT7QWj1PmMd-q5Z_MbrIdBjaOqX5NqNcnuzSTHL1VmHRWbEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم
می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79365" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79364" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H27dRWEsYSp-YHe7VqiuLPk_c1fQakVZziZeWFMBwkGzY9-FS3-sDQAtrKzKirD6UrfgjgLZtHV0MOU_HCH1FzJ8e2Wt1Vdi_N4p_DJP8T6Vy_9qGclHt3LGnVmmiedAuuUN5v7fGu8R9LPWOLUj0UgZMTLj3eZRtmlqYbcHOCc9SeGbMQsMlhHidxmWhR93spMosVdWdbiC_89aE4T2WeLmnHDHQaC6aK-fZTkVymo1klDVzgeQQANIsASuGkHclS8N5nzk4YSJeTndQouHlRcSVpZfrmiipemmabNsV-i7m0SEiffUr-7qk-BC2O45K7gdBVP0Y0X3RTnTTxvTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو جنگ ۴۰ روزه سپاه در ازای هر یدونه موشکی که به اسرائیل می‌زد رندوم ۱۲ تا موشک و پهپاد می‌زد تو کردستان عراق.
بعد الان رئیس اقلیم کردستان برا تشییع اومده ایران و چنین شاهکاری رو خلق کرده.
من هر چی بخوام بگم فحش می‌خورم برا همین صرفا به این بسنده می‌کنم که ببینید ترامپ عجب نابغه‌ی درجه یکیه که به اینا کاملا اعتماد کرد اون همه تجهیزات رو راحت داد دستشون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79363" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9yKYs1YPMOg4k9jUyKaZwRLvwWiWoH1ho9aI9BBd0MmYV7a1BcP6xtd6eGUqlEKbRIIO5yULgh6UhPyVeqHoiNMG-Z6NqNusjNdW3LY_P6qvXl98pPnrGbV39zHWbsnQoEIXqOs87LNUVAk0GCU_TzqLz5NS2cuT7xChiytzw1rUo4w2MMVB5HDfWI748r1JycFaZUUyCVr6vig8QQNugbEoEErqF4aLmzYWBZ0mjKcmusYoPCpZL4M5bUE9oQkMXdFWctcHjrRVE8yZvTXGaqx9NRb0WNg6EfzuMhrch1lyiWX6pA4e58leJ_Ub6v6xfVKMZ5nvPfU1p4T_vNSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تسلیت به پدیده به کون ها
دریک رو صعود مراکش بت زده، کپشن زده که میخواد از نحس بودنش به نفع کانادا استفاده کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79362" target="_blank">📅 15:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۱۴۱۱ هم دکی پول ویناکو پس میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79361" target="_blank">📅 14:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH6y5LuRl8sgybds--nnsDrLDnNXGla-sQiTvPrf-sh_FDf3EsFlUBz4VgYSrJQ-vfW16GgKk1ftJEJasCzXmMwdVVrWnnw6CkuTFDexU-QHeX-X40e-boKYsIef6ml7gu4kJ-jysQZ1gwuZGqHGUMk-GPUMhTrV7G-DNmdP78Bx12CtCYhUtoBpd0S3eY6LhH1ulnfGO8tJfY4hMdcWRlR_HFaCJy2iPvu8ihH22KNKarOvPnyN4ss8LOvBh8bDQ7NHw9vea1AzqYhg8tnjhEqxsevL4-ZczjiY9pUficbkK1L9y8VLYlMJKbtkgdX7bmX4T6k-07GgirB7V29rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره، سال ۱۴۱۰ هم امام زمان ظهور میکنه رضا پهلوی حکومتو تحویل امام زمان میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79360" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCGnNIvYHYIQU2ekhdr2zfoOrQtJ3OWPfo3hJn8uQDd8fRRLET5QFArti7zByeX-JBzbtsHeJpXNlnnCboIDY8TCmKC8X_Yb7SjW1LD7kXu2CQr_gbVgDgFoH9meOyj0Rg1aVI_jtWko1enSil32y4xbkIdQOe45BYB6wOd7C7Lm0yvN_gIPJQLXaK4LHKIfdeD5zOXl33lu3vsB0_CNcV6FnIxwd00vzFwMUY5GhcWqC6RZVIBZTbsVlfd7JI1zA8HfmOA0XkInb7nRGs2OOWqN0s37F257d4Wu5P1WhI2E1ZmVjhHvcOu--iwqCAmvyVlWzRtcN5h3rgY9JkzjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلش نمی‌زد فکرم هزار جا میرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79359" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">توماج صالحی از امثال شهبازی هم بیناموس تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79357" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
