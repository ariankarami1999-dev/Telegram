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
<img src="https://cdn4.telesco.pe/file/fGpM3Wtb8_UP4XsjmRS75dQQ48LrT8duiDKIfJ6iDAuETtFfK3h3QaJFHWfVnkhrQTukCCFqS7LoiVPlg7maYb1SsWj-bv0WbC7Is8qx6jPmWGFegXpBtgAGXECi-0cpqBhHNxlW6QZLmgcti1SWRR0KBdrAJo216T4y4zYFuj6Sao1pnGNsrjUoiLn1Ujf1PTbdwgyqBPh0w-q-xzZMrpcAOsVCtKKKGFnCS0RoKXBLOZp4klKLpjG1FHj45XcZvX755183CDoFpJ6U9CzaqeW5tfNnEPbnZhJbS0kb_VaesrQiSH1E4h4oth1W5BL9pANlsOWzGUnzbOhkFtn3pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 17:34:53</div>
<hr>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ذوالقدر دبیر شورای عالی امنیت ملی:  تا آمریکا رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد.
🔴
شورای عالی امنیت ملی هرگز کوتاه نخواهد آمد؛ چه در جنگ و چه در مذاکره
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/140584" target="_blank">📅 17:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNY_SIkMessTBrPCP8x7CTYWq7ivqZgAr0vL9f-PU4Bv4Kz5lCHMT3p8Y9wzyf4XvDAka8LOwlnxIDWWBRJRGB-8Fi_-Xbf2v_DlW1F0pkwOAluYQE8Nbc2P7mzbDmmUDUbR5v8UEArjR0zzqo-Ij9eJZx_ABIpl09Z4t_7r3KiySd0pohfPU1u7V_mfMvgeDFt_xNKUNwsaLFhigg5hh6WTAk6rzVPFL91YfeGhiJENOOVkk2UyHfowMxRLzXkhBWtKRzzTP508qBzhzrx2b-EoiG5-74TIFU5YkO4RoHqjyU12c3PPn2jYMU3WEwI74uZQpbeoUee5zIlKxNkEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140583" target="_blank">📅 16:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pKRvx_TnUizMRO7k80SwjeAb16o3L0p2XfSnkLLb-8h5fpSlc1lA0yzSf6g1OCRwG2vTqMnZLv7FoJrlsPsOba-kTZ3p7NL3bCgn3D1rZmeDkyk7oI1d9Psnq1DRkwwrQLniG0xglb8QlKs_0VCTXfao43lJlsled0yALLJU33r_0Hhf-5f_GvvUw5y--d_IKQiPmMTORWV1omJbeRiP3ZpHvnnvu0hvItVTKBzi_hsgsFKgt5dwAQl6X77YDvKajyphHIJJqzSeff5bn4Avk04zF1VScmj1a-hV3MCeXCItqw8k8eEGhlPVC6m2pLTAT_vz-Q7PM8ebfOq92okRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XquywMmR4y_vJQdPPXHV1po6jVPg0s0H8MdHAeS1YPV67c3_Ir1RshRorelcmNOKAcRKNMVvfxidq45iU7kcuidLDoJTa1yNlHhnbH-7Ao8NhR_7h29CW1v0QUthM8f6BeB4rr0YLZMCO62-ap5CfoNFGZ05oKjnGmGCVXKZXuxNaEDg2RtZxwQSs6Jax1-3Lywb6OZi838zXTUn6U_guFEYvg-J10wYZjcyWiOe8zXRQNreiEPXiH4lnj34CLbMIijDfGReHXaMUQOvSvE7xuiQ8Mux3OVkNreBg4447BBwN8sYEspOvNm84SXWsT9IZ7Ply8kblgeI0iG4YnkSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W2W-A6ql6oGnQwwbLLp3leAUdNy9ZnXFciMmfOeaPYsZ0lMGOZXSm-IHI5yOlt3ExMDUSm_VXgmtbiXsw6xQyLcJRp1CmF3KnL6A_9bz5VAkZ3R6ao2hkzgnfa4yW13gbAK6ZmN9ktQ_Hxo60mGyLkore2JEGDuisIuY8dHqRUxpIX7A6ZY50uznSaf2A6fFevKhu9WauSZImDJTg_V4HX8ahHbPdOg0eB_SWTGgBGtQmJoTAHawRKOlQJVBMnvdyNTBGIiicE7ASHRT_jmEgD17OCUApngfjNXN8VYADLugnGv4pL9nNi9tAGU10lVsaViu2VlaeHW6tIdJ1LnChw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
استوری های عجیب مژده نظری بازیکن تیم ملی بسکتبال ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140580" target="_blank">📅 16:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی 9500
ممبر از کایی ۵۰.۰۰۰
⚡️
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140579" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
بی‌بی‌سی: عربستان سعودی، خرید شرکت بزرگ بازی‌های ویدیویی، الکترونیک آرتز (EA) به ارزش ۵۵ میلیارد دلار را به پایان رساند. این اقدام باعث می‌شود که شرکت منتشرکننده بازی‌هایی مانند Battlefield، EA Sports FC، The Sims، Apex Legends، Mass Effect و Need for Speed، پس از ۳۶ سال فعالیت به عنوان یک شرکت سهامی عام، به یک شرکت خصوصی تبدیل شود.
🔴
این معامله همچنین نگرانی‌هایی را در میان منتقدان در مورد نفوذ رو به رشد عربستان سعودی در صنعت بازی ایجاد کرده است. سوالاتی در مورد احتمال سانسور، مسیر خلاقانه آینده فرنچایزهای EA و استفاده این کشور از سرمایه‌گذاری‌های بزرگ در صنعت سرگرمی برای بهبود تصویر بین‌المللی خود، با وجود سابقه ضعیف آن در زمینه حقوق بشر، مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/140578" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cc4ef375.mp4?token=gjQN559eI71oMfa1QmX7P_Sl10bsvtqOXvhM4TRtW5SLUJ5c1tYpin-G9cdAbIBlyRuLeOXZHjxOpEx6UDHZnG-DiBD-_dLMKmWUrxMgmAtC91Fu2UNP6M7Z-eG2ZRzIIZw15hbZRGaqa1Yca1pLnoiCeBTQbsYgVPYS2fsGWNaUWTyRWlsKvtpcjkjp0OEF9D_G9HeYUodWwzFrwRWBoHQQia5IGaW8lM--JtUg4jgKSuafXMO1qP7eDFQecGdJXD6LsLtIcvzvafCqd1hRqIrw3tZis21yEEV0LMEvkXsF2Xnle5M1TmUCFWxloEqdnpWmwA1Lb8hLL--AloyL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cc4ef375.mp4?token=gjQN559eI71oMfa1QmX7P_Sl10bsvtqOXvhM4TRtW5SLUJ5c1tYpin-G9cdAbIBlyRuLeOXZHjxOpEx6UDHZnG-DiBD-_dLMKmWUrxMgmAtC91Fu2UNP6M7Z-eG2ZRzIIZw15hbZRGaqa1Yca1pLnoiCeBTQbsYgVPYS2fsGWNaUWTyRWlsKvtpcjkjp0OEF9D_G9HeYUodWwzFrwRWBoHQQia5IGaW8lM--JtUg4jgKSuafXMO1qP7eDFQecGdJXD6LsLtIcvzvafCqd1hRqIrw3tZis21yEEV0LMEvkXsF2Xnle5M1TmUCFWxloEqdnpWmwA1Lb8hLL--AloyL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌ توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140577" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj449LwGSxP4n2NM9tRDW4SSdZ6mlrcubDDlkE2rP9GJCzKT3rQTmbXRQl5OCLcP0Mz-fITuEPkgKYO8u8kfzPrgm-HV--coBoB-OFxTjSLlhZX4xE1sZi9S5_MDxOf_mAoM-UYn0A_pg5bzIVbmpdHeMzJ_nPMbIyNWRWulDTrSeud9jkSq0YBwUJBMGlLOcrYwbo6X0Ccl32t5KF4VcOGZbGYFEDJVwbVpTiH-PrNyqPYeXhual7cu-3Ib4MFlw7JvBwq7G2HT07eMOfylDbbUGiA3TVlXVvqak5xpRR4XG9heO5Bz8n3xb5VKRMSs5OqLXILYugP_9t8KelKI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر سقوط قدرت خرید: قیمت یک جک؛ معادل ۱۸ سال حقوق یک کارگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140576" target="_blank">📅 16:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7edca33567.mp4?token=HNUzTc8O3CPySQQ0_xwR8kjhrWomx8ZKYYsfgCkYisWuv2mBGPKV7BAsxcEYAvJTgsUJQ19gg6bCUNy9EMS4mtUEUDEFkSwvseUi62OSij4lDnSCXg0HpZEhCjxp0HNPT4ybwptZ2J4E8gi26W48qKoocs8uda2PxTy1dmgFiUnwx-wA8tSNguYctcTlOlVgfpuI5IVaVC3KMhfkUZo-pSFJq_OeALnxplPHsyAvx1GwmF8BoKz5pC_AMyKihEoOGRVLchsq5aBFxSxrfDPhPYi0DRkDrkFthdG7GnofJ6_sI_3727pAE-FnmQSBoJqjbKHre_6QBrDIV-9qYrcV2l-P3KnL16ZbOcQ0HOWE9PX8Yfg5xW9e2ISkDv7DfejeDfUMU9qKRULCcCp9kys4CLGuuG3kNTZUbIaJtfTSr2If50CYZCluCJMkgO8ItCbk6oy9EPA5Rin6UWCKdmh3lrd7lFshDoUsTbpWht_Ytgk-5JBPR34jJfnFYrIqwrRD7le7gNZHCHXCFWHrobx1dtbFkuWtXo8FSon2SH2xTz-i1y__DvZMgaT0uCGF4LSHqLJSTUxhND4MA4djhmpQu5ll6RVwAr8ftqOVLbVsGAhlERqcU21Z-zzk1d31Z5AYMtjI-VVkkJbCp024kH2V0vH0JgfDdKrbgJYtdyXhi2I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7edca33567.mp4?token=HNUzTc8O3CPySQQ0_xwR8kjhrWomx8ZKYYsfgCkYisWuv2mBGPKV7BAsxcEYAvJTgsUJQ19gg6bCUNy9EMS4mtUEUDEFkSwvseUi62OSij4lDnSCXg0HpZEhCjxp0HNPT4ybwptZ2J4E8gi26W48qKoocs8uda2PxTy1dmgFiUnwx-wA8tSNguYctcTlOlVgfpuI5IVaVC3KMhfkUZo-pSFJq_OeALnxplPHsyAvx1GwmF8BoKz5pC_AMyKihEoOGRVLchsq5aBFxSxrfDPhPYi0DRkDrkFthdG7GnofJ6_sI_3727pAE-FnmQSBoJqjbKHre_6QBrDIV-9qYrcV2l-P3KnL16ZbOcQ0HOWE9PX8Yfg5xW9e2ISkDv7DfejeDfUMU9qKRULCcCp9kys4CLGuuG3kNTZUbIaJtfTSr2If50CYZCluCJMkgO8ItCbk6oy9EPA5Rin6UWCKdmh3lrd7lFshDoUsTbpWht_Ytgk-5JBPR34jJfnFYrIqwrRD7le7gNZHCHXCFWHrobx1dtbFkuWtXo8FSon2SH2xTz-i1y__DvZMgaT0uCGF4LSHqLJSTUxhND4MA4djhmpQu5ll6RVwAr8ftqOVLbVsGAhlERqcU21Z-zzk1d31Z5AYMtjI-VVkkJbCp024kH2V0vH0JgfDdKrbgJYtdyXhi2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو آمل یک شخص فضول رفته به یکی گیر داده که چرا پوششت اینه
🔴
اما فارغ از بحث پوشش طرف، نکته جالب اینجاست که این شخص به اصطلاح آمر معروف به چه اجازه‌ای از ناموس مردم فیلم میگیره و پخش میکنه؟
🔴
این زن فضول سپس میگوید من اطلاعاتی هستم و پدرتو درمیارم و حسابی تهدید میکند و قانون هم طبق معمول مشمول این اشخاص فضول و بد دهن نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140575" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H522K9NQcConrHEWk083YMA1uusHfFVz_QRYpTuLF2qlaxagYw7tDQWt9QY2Nmbok1avW4foURE4XDMEC0fHtpDPNvSYnhkDc4hpCNZzNxc_QyBUb46-KUvr65Cykk6xxs9WZDV3MLPk0D1mgnRYdv7l3nO9Lq3veaUoDdcD2g9VNnZkPAagkRVnqqQvYIJ-0vuSjD3bfMRuz4mc5PDe8hYfMWCGiEgA8H2zveVSIU6znVbG1_g8pRc8SEwEKvLap7PJYnki1UNYltMewis3h5dWORuRri20urE4Sp7Od6f9pvQnJJIijs6zpPeS3nQbWjjvLK7NX5Je6scT68SGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیلاری کلینتون: کاخ سفید ترامپ شبیه کاخ‌های صدام در زمان سقوط است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140574" target="_blank">📅 15:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان:
ما ایران را مسئول عواقب اتفاقات آتی در خاورمیانه می‌دانیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140573" target="_blank">📅 15:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc109ca33f.mp4?token=ADdwE3cV5XIVWEPqomgOCC51A-_HXwHkhTWW-IqsZWpnPB00NHF6Ig_ATfPVmguCZXNY4A3XkqZTDvr395qmF4e1fXi_H9NlLA3J0x7TBf4Q20Jc2YpBnjzGAiUMnlm6y7j9GV6VtM3r22eEfI0gHQjwuPWEZx7VjZgvoMvf3gGF4yUtDECeZKd1uBYYWGN3pFzFzq4pwKdeRihKkokrnmCx4NCnjaWWX6xErfUt5tWrBDHYOE8HM120sRmlWByK0IygfqnAd174qk9MUsRTzPHqXnn5z4T_PxoGZxF1d3bNfamgSROQaaluCOctaEripS3VmoCzbFvEAg9KUd3NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc109ca33f.mp4?token=ADdwE3cV5XIVWEPqomgOCC51A-_HXwHkhTWW-IqsZWpnPB00NHF6Ig_ATfPVmguCZXNY4A3XkqZTDvr395qmF4e1fXi_H9NlLA3J0x7TBf4Q20Jc2YpBnjzGAiUMnlm6y7j9GV6VtM3r22eEfI0gHQjwuPWEZx7VjZgvoMvf3gGF4yUtDECeZKd1uBYYWGN3pFzFzq4pwKdeRihKkokrnmCx4NCnjaWWX6xErfUt5tWrBDHYOE8HM120sRmlWByK0IygfqnAd174qk9MUsRTzPHqXnn5z4T_PxoGZxF1d3bNfamgSROQaaluCOctaEripS3VmoCzbFvEAg9KUd3NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اجرای حرکت میشِنِری توسط یکی از جان فدا‌ها و اعلام آمادگی جهت جنگ با دشمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140572" target="_blank">📅 15:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d4ccba468.mp4?token=c3ysabUJuXz-bMJ1S5IXzzsm6wrQU5nD_ZPKtmBJZasGYlLRYz7S49rTk0UH4-Q_y4_yYDptTc7tnwgcQtii3il3qC6pP7n0UmzN42v3a-NCmcHIUOTeCNIE97qlMdtI75iaKmn1W-lNr2S-cS5oLESIJlgmGnETuGXITXlvzjEeGR1m7DEI-6JtI9kGuhwe2lgXTg5ayQ4RuD7xTKqQFjmhaZqwnjQl08iQyVboN1Q5BQbZRlF8rHFuAwtmRAf963TImfJCI7xVYycaeHPYIUeUBXiWavZsxpPK8zwl82KGzz5AEkz3jDse50xEa7yD6aU4ddjNmUd9kJY1VcYl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d4ccba468.mp4?token=c3ysabUJuXz-bMJ1S5IXzzsm6wrQU5nD_ZPKtmBJZasGYlLRYz7S49rTk0UH4-Q_y4_yYDptTc7tnwgcQtii3il3qC6pP7n0UmzN42v3a-NCmcHIUOTeCNIE97qlMdtI75iaKmn1W-lNr2S-cS5oLESIJlgmGnETuGXITXlvzjEeGR1m7DEI-6JtI9kGuhwe2lgXTg5ayQ4RuD7xTKqQFjmhaZqwnjQl08iQyVboN1Q5BQbZRlF8rHFuAwtmRAf963TImfJCI7xVYycaeHPYIUeUBXiWavZsxpPK8zwl82KGzz5AEkz3jDse50xEa7yD6aU4ddjNmUd9kJY1VcYl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان خطاب به خبرنگاران: امروز کمک و همراهی شما برای ایجاد وحدت و انسجام بسیار مهم است/ باید مشترکات را برجسته کنیم نه اشکالات را
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140571" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ادعای جدید محمدباقر خرازی:
‏
🔴
کلیپ‌ها جعلی و ساخته هوش‌مصنوعی است
‏
🔴
من این حرف‌ها را نزدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140570" target="_blank">📅 15:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ba74d22b.mp4?token=CO4F_R-NY_76Msnh-l9aORwAkkzH5UeP3B3JUhBnUv8ymLfZS-USzAiZx-GIc9qwluTG7pahNvxArtkU3qSbV13Ahd9OWgkH5j25EdryOseU3Tn8PzqNqbstdT3R0yrzVP8-0Z7Zinj0eVJ4j2Mft36rY6xYVCb5tDN1XVfS6ovLRC3kii02qH5ZrNt6nTjjFPIx3g5WEvuQtuDxe6GUQYgt6MWc0KYZh4nC8KxKOX1LE3pJF5TH7zuXFysoLZRFLyR0-506jUTIKuV7haIPVMI4qrF3cBXa5rWuFj1dYFKjUyDh7oWzL-Pc-nT2whtWoEVfn3YPxWn7Ntq9DN40Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ba74d22b.mp4?token=CO4F_R-NY_76Msnh-l9aORwAkkzH5UeP3B3JUhBnUv8ymLfZS-USzAiZx-GIc9qwluTG7pahNvxArtkU3qSbV13Ahd9OWgkH5j25EdryOseU3Tn8PzqNqbstdT3R0yrzVP8-0Z7Zinj0eVJ4j2Mft36rY6xYVCb5tDN1XVfS6ovLRC3kii02qH5ZrNt6nTjjFPIx3g5WEvuQtuDxe6GUQYgt6MWc0KYZh4nC8KxKOX1LE3pJF5TH7zuXFysoLZRFLyR0-506jUTIKuV7haIPVMI4qrF3cBXa5rWuFj1dYFKjUyDh7oWzL-Pc-nT2whtWoEVfn3YPxWn7Ntq9DN40Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: آمریکایی‌ها از بند تفاهم‌نامه درباره تنگه هرمز تخلف کردند ما هم پاسخ‌شان را دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140569" target="_blank">📅 15:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244d29c341.mp4?token=vq-wu-JoXILkh0Ozzo_WQfb19AbzTitc1eg5cw9aERjfGGEKf_GVRSCJYX_qDEPjQ93bH6UFLcwHtF3FB7z9ntLw-vR6nhauFxWFyB_9NHX-wXwSZpJDM2YFFGsf5A0n55ixu6KBukQ2HXTXziHnJo_qTblnOZz8Z6bmS30MTWO_azdM1ZXNVC5jY389gbf7wRKMVe2kSqZYjIfzkIypgpoXypGNbFlptPHTMM2MorI_7he8MqDcTxjAF3n-dog4MKW-4WNAQXrELNEjJLo0gEE7myaXGPAJbVpk0iUWB2tqAS7O29866LMvdAIS7JyQO5BIpzNYjQDRYFLGQH-eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244d29c341.mp4?token=vq-wu-JoXILkh0Ozzo_WQfb19AbzTitc1eg5cw9aERjfGGEKf_GVRSCJYX_qDEPjQ93bH6UFLcwHtF3FB7z9ntLw-vR6nhauFxWFyB_9NHX-wXwSZpJDM2YFFGsf5A0n55ixu6KBukQ2HXTXziHnJo_qTblnOZz8Z6bmS30MTWO_azdM1ZXNVC5jY389gbf7wRKMVe2kSqZYjIfzkIypgpoXypGNbFlptPHTMM2MorI_7he8MqDcTxjAF3n-dog4MKW-4WNAQXrELNEjJLo0gEE7myaXGPAJbVpk0iUWB2tqAS7O29866LMvdAIS7JyQO5BIpzNYjQDRYFLGQH-eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور: اگر صنوف و تولیدکنندگان همکاری نمی‌‌کردند وضع خیلی بدتر از این می‌شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140568" target="_blank">📅 15:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052d786f4b.mp4?token=KXbb2XM20y1RydX0sS6GcZsHlVPcWUx03WcZGw2ZTJteDW-TPeR-unHtjif-SIiC2Crg1-a1mRdHb9OnybYJBDmIutmSt7bWFc7v-9dQYoC9NUDzIvml__wuKSswdazgO43tWD4FyZ9eXTmToeLN6zVrJ5-AC0NT0d7esG3CLPP1dYXYTiQtWkpdXoHLsJuTm6HoYsXQzU4MCThUWUI9Bs5TqyuVWYBnNHpPriwwM_lrTsEMeIUOVIRIJIPVazs6E48Lspy0c0JMpxRNVmhSIF9QALjpnLJnM1v2Kwfjxln0LKN5YUGlX8O13NAxfHaRFCHcrzCf_h1_tGOM9JVkoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052d786f4b.mp4?token=KXbb2XM20y1RydX0sS6GcZsHlVPcWUx03WcZGw2ZTJteDW-TPeR-unHtjif-SIiC2Crg1-a1mRdHb9OnybYJBDmIutmSt7bWFc7v-9dQYoC9NUDzIvml__wuKSswdazgO43tWD4FyZ9eXTmToeLN6zVrJ5-AC0NT0d7esG3CLPP1dYXYTiQtWkpdXoHLsJuTm6HoYsXQzU4MCThUWUI9Bs5TqyuVWYBnNHpPriwwM_lrTsEMeIUOVIRIJIPVazs6E48Lspy0c0JMpxRNVmhSIF9QALjpnLJnM1v2Kwfjxln0LKN5YUGlX8O13NAxfHaRFCHcrzCf_h1_tGOM9JVkoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تسنیم با انتشار این کلیپ نوشت: پخش تصاویری از رهبر برای اولین بار
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140567" target="_blank">📅 15:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140566">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQRrRm1zWBdwzLW4DxO-__Rz9hmMSNeYqFyPHvO14XJ9cjUA2sB0W6GSobm1KH92P3t9pCXTlaImHel9rRTdWioKFEMfWzx6OdQGZ2oiJJgH0FIUM3be-2xfnQ5BitC3xO_V2Fa8s5Mj_gfEAxRuButl8zIry5nbrswZ6k4NXnx7wBgoBwbjL02l2KC4FFDyqVmW3EcE7FDwZ-UBiehLJeRjPq_y5Xj3Odv_ql7PyV7GuP4dR8eRLX_A5GWgB7ZSaJGwxxrwZq2HXqziQ3otw_8O_wWBLoFCGQFUhf8JR_mg9ifjXaDzD8EWK6p2joQNa00jmymt27vQwebm4vC2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بارزانی، رئیس اقلیم کردستان عراق:
ما رابطه‌ای با اسرائیل نداریم و سیاست خارجه بر عهده دولت عراق است.
🔴
ما رابطه خیلی خوبی با سوریه داریم و در حال گسترش روابط با ترکیه نیز هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140566" target="_blank">📅 15:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140565">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سقوط آسانسور در میدان آرژانتین تهران/ ۹ نفر مصدوم شدند
‏
🔴
سخنگوی اورژانس تهران:یک مورد حادثه سقوط آسانسور امروز (شنبه) در ساعت ۱۲:۳۷ دقیقه در خیابان احمد قصیر میدان آرژانتین، رخ داد.
‏
🔴
تاکنون ۹ نفر مصدوم به ما اعلام شده است و خبر تکمیلی متعاقباً اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140565" target="_blank">📅 14:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140564">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عراقچی: تفاهم با عمان به‌معنی بازگشایی تنگه هرمز نیست
🔴
وزیر خارجه درباره مذاکرات عمان برای تعیین تردد در تنگه هرمز: مذاکرات در حال انجام است و با توجه به پیچیدگی‌های فنی، تعیین مسیر موقت در حال انجام است و به نظرم بسیار به نتیجه نهایی نزدیک هستیم.
🔴
البته این اقدام به نشانه بازگشایی تنگه هرمز نیست و بازگشایی تنگه هرمز منوط به شرایط دیگر و جبران نقض تفاهم‌نامه از سوی آمریکا است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140564" target="_blank">📅 14:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140563">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u4xp5QRVYPbu3ox0xOppGvtseGRfsDW3sivHsh_beNjjOIPT57p1sthtnfZuR-PZW6BQmfqAOF5hR2BFk6lCzUDiSqVBfs37fASHeqPa4JtEETb9JpqZK7GMx5p5ILLolho5iHST_KYYmThLBi45IYovZMsfULu8_ZES4HOVlp2R-9DYI_iRPRPeRqpA4gqvNOKPeaqL0nYnfFJ_Lh8Yu1H-TzQ9j_KtNPiePrhVIM1GWWqaT8R1qvRRDw16rmGwkWKQrJr7bHFeTibPo_MVRDQmWVFBaEVXSDXYH3x2FGyPJQ178eFw29NGozUG7B1wVjv-oNPxM7zomH1QEoYv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر امروز ماهواره کوپرنیک از وضعیت دریاچه ارومیه و مقایسه با زمان مشابه سال قبل که نشون میده به نسبت پارسال وضع دریاچه خیلی بهتر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140563" target="_blank">📅 14:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae13d0a2a.mp4?token=uIgd5VsNjJsBWlFiKLJ4cMYNUPO_txBM8JngS5r_jluf2zRstnWxUHExWZswXvp-hshb360Idq7Da5HPyDji5BgS-FTuh_QkhbUR50UW3DkdeN4onRYta8Slbf14gDE04DRnHfKK1VHexE4dw4koxErhYkIpxgRI9aVordMffUe6xZWvcHk8qOrCaMEjrfrZCG9glVGSh09umN83N_oGjkYfWC-QbnbPfDqTRv8heqNjykK-sgyDcmAibJThhgsZQ0Y2PbzSRzsxjsslL8tw34NZUCm361nZRnxojs3QzD8rMsH3xsQmPLGhQqJwqkh-3EFMFojyD-0i2SYGKlQRFGS9u33zi1VMANvAmwZjCb_PDb7mDDecUg565a-I3jrWTBj52z7XmMDmR4kFpNIyoyYFjnCkBJZdSpZFLEg6jlLa8iTWr-TwsBkDGDSkBGjlZgeNH8we9WnJFxHzTsU-KFHWnCtS4vF3Vjpcbn9yMnDm1_RmWBvdNzjjAuvf0hwmwgaQdgL6yOYuZIcNnAQL6qwGpa-Imxp5LRQHtM46Oxa_-frC_ixU7qTjTqwK8dGL_OcvaW2XNcBBceUDoOGzBsz9SI6MvTaqdrVDTDQ60frp_jYneFc3DJDKhyULlkiQSi3j2e_VUEihEt44cQaEEJI3ZBEnAWnNFbBSGKdO0Fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae13d0a2a.mp4?token=uIgd5VsNjJsBWlFiKLJ4cMYNUPO_txBM8JngS5r_jluf2zRstnWxUHExWZswXvp-hshb360Idq7Da5HPyDji5BgS-FTuh_QkhbUR50UW3DkdeN4onRYta8Slbf14gDE04DRnHfKK1VHexE4dw4koxErhYkIpxgRI9aVordMffUe6xZWvcHk8qOrCaMEjrfrZCG9glVGSh09umN83N_oGjkYfWC-QbnbPfDqTRv8heqNjykK-sgyDcmAibJThhgsZQ0Y2PbzSRzsxjsslL8tw34NZUCm361nZRnxojs3QzD8rMsH3xsQmPLGhQqJwqkh-3EFMFojyD-0i2SYGKlQRFGS9u33zi1VMANvAmwZjCb_PDb7mDDecUg565a-I3jrWTBj52z7XmMDmR4kFpNIyoyYFjnCkBJZdSpZFLEg6jlLa8iTWr-TwsBkDGDSkBGjlZgeNH8we9WnJFxHzTsU-KFHWnCtS4vF3Vjpcbn9yMnDm1_RmWBvdNzjjAuvf0hwmwgaQdgL6yOYuZIcNnAQL6qwGpa-Imxp5LRQHtM46Oxa_-frC_ixU7qTjTqwK8dGL_OcvaW2XNcBBceUDoOGzBsz9SI6MvTaqdrVDTDQ60frp_jYneFc3DJDKhyULlkiQSi3j2e_VUEihEt44cQaEEJI3ZBEnAWnNFbBSGKdO0Fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنکسی : تموم احترام و تشکری که از طرف آلمان داریم، آلمان واقعاً کمک کرده و لهستان هم کمک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140562" target="_blank">📅 14:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
زلنسکی : چه کسی موشک‌های رهگیر ضدبالستیک و سامانه‌های مربوط به اون رو تولید می‌کنه؟ در درجه اول، آمریکا
🔴
آیا آمریکا می‌تونه به ما کمک کنه؟ داریم این موضوع رو بررسی می‌کنیم
🔴
آیا هر ماه تعدادی موشک تو اختیار ما قرار می‌دهند؟ بله، ما توافق‌هایی در این زمینه داریم
🔴
آیا این تعداد برای نیازهای ما کافیه؟ خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140561" target="_blank">📅 14:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
زلنکسی : ما خوشحال می‌شیم اگه مسیر صربستان برای پیوستن به اتحادیه اروپا سریع‌تر بشه
🔴
همه ما تو اروپا باید بر پایه احترام متقابل و روابط دوطرفه و سودمند، تا جای ممکن با هم همکاری کنیم
🔴
مهمه که هر ملت اروپایی از اتحادیه اروپا این پیام روشن رو دریافت کنه که وجودش در اروپا مهمه و اروپا نباید هیچ کشوری رو از دست بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/140560" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWaNkhtZ8p3VnVyYAMzJiJRNvPk-RaUWdHYCfL3ajqB4N_Brvbo9Jt-9bQC4xLfn3Eh7uGVwazk3IMTjnh3YRUxIeml1AEOuAiMY_K-WWUWkAzd0f1Oj5DuWZiK8DEZk_VLhA_GMNlnAx7RGc1G7GHfGjlc_88oQml9vpyli9bd1I1K6EeQEGpM2CQ5CPl5ffaWmY2yo2QCMHHwfJGrApOGmnY89FPIF0m7XaYNw6G8OWoNGl9QHRnIhMPtlVeUkA6CmiAoUAkEMlmNYpx9F9f50znJsoREHoZ33_2xrwXcL3LYidMviugyIGhJJEz4_P3owvMYP8Q5jQpHZxgbk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قدرتمندترین ارتش دنیا واسشون خبردار وایساده بود ولی خب اونا عاشق آفتابه بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140559" target="_blank">📅 14:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK8s41OuIznmmen9V9Zjjatk8jvkYMnKSWRJf92PAtRnH5Q0065pIYjBb9acu8Ikv_yF6JJ_u8Zle4nHvnrBsdv8VtSkjTLpxNwT3uXJNa1eoGmyu57jxp3exyXq76enmosiPCDUyu34pL_sMDd7Iydbm6by1NmX6wrAaAd0HHwAEGcfiL3Ka90NNfftUGwwrbRg6qJPZA9JhMnc0KWmIXdo9drp0XborKjFMveokbX0ed81jySiDPx7HPDAyphctbmbaghxjAIKGtHal38DujK3nJOI_TuGTiOPCXwis0RjdYl8oyQWpJHh3hWob4BsCVwbWJouiISiPrZ83TCA4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
چندی پیش خورخه مسی، پدر لیونل مسی درگذشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140558" target="_blank">📅 14:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
غریب آبادی، معاون وزیر خارجه: در اثر تصمیمات برخی کشورهای ساحلی، پای بیگانگان دارد به منطقه خزر باز می‌شود!
🔴
تصویب کنوانسیون خزر، به معنای از دست رفتن منافع ایران نیست.
🔴
این کنوانسیون، حضور نیروهای مسلحی که به کشورهای عضو تعلق ندارند را در دریای خزر ممنوع کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140557" target="_blank">📅 14:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پرونده کلثوم اکبری به کجا رسید؟ / سخنگوی قوه قضاییه: رای به زودی صادر می‌شود
🔴
اصغر جهانگیر، سخنگوی قوه قضاییه: حکم ۱۰ فقره قصاص برای کلثوم اکبری صادر شده است و رای پرونده کلثوم اکبری به زودی صادر می‌شود. از حیث مباشرت در قتل عمدی به ۱۰ فقره قصاص نفس به صورت مستقل در حق اولیای دم که مطالبه قصاص کنند، برای او صادر شده است.
🔴
یکی از اولیای دم رضایت داده و دیگری درخواست دیه کرده است. در مورد اعتراض خانواده‌ها یا خود متهم، ۲۰ روز برای اعتراض فرصت دارند. و
اعتراض در دیوان عالی کشور رسیدگی خواهد شد.
🔴
بعد از رسیدگی در دیوان عالی کشور و قطعیت رای، اطلاع‌رسانی کامل صورت خواهد گرفت. همه اموال منقول و غیرمنقول او مشمول مصادره قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140556" target="_blank">📅 14:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرگزاری امارات: یک کشتی متعلق به شرکت ادنوک امروز هنگام عبور از تنگه هرمز هدف موشک قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140555" target="_blank">📅 14:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی سپاه: بازگشایی تنگه هرمز منوط به پذیرش شروط ایران از سوی آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140554" target="_blank">📅 13:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت دفاع روسیه : نیروهای ما شهرک ایوانیوکا تو استان خارکیف اوکراین رو تصرف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140553" target="_blank">📅 13:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue2HhOyHueBdFkBPtmrz4d_aAUntTn1E-sJdfHmBAaki6_crTP3ABN8zMlYqRwPECCVVim1JErhWyyzkWzqvqNlbMahbCaF3bOSKtKJzigAH1batglDkPFaJzkVYjQ29Vzy5r0KDCmhd4Q0p50skzhu5mpgdV9ftv_9HuOx1nuPUWw5BPv24CRASMq0x9ttqWp7RzH3sgdW9aJPEKmkF78J6r4jV7cu4O3wV3dyVNCE47uIMpfnB5e2ae1zRJN66ZVQjZb42z1oRHGQfrZwrpw1KPDtrzcah6GnHA9zT8iiW8_ke-ct2MP1ca44QGgxVazzFjv6DarKHoJ3kfl2jpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس راه اصفهان : امروز تو جاده کاشان-شاهین شهر یه کامیون داشت با نهایت سرعت از ماشینا سبقت میگرفت، ایست دادیم بهش زد کنار دیدیم یه بچه ی ۸ سالست که خودش تنها داره رانندگی میکنه، بهش گفتیم پدرت کجاست؟ گفت خونه خوابه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140552" target="_blank">📅 13:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhvvuQF4jSdEOXF6DvQJ3pOPrDTH20O9xrKeR3voLOyOepWPoXJ8a09AG1S64XYi20kdoqet-h41hEtRXNtVtsQh8KaRF1K51uuiDrf4-now7lUZSRaGam3EdQaclSngoQcpX08TypdG5WRBWc2y9qN1x0jK7GOCGGD1OFD0ik4iZ3pgAPtVhqwHaFHWKwXyPO_Cawc_fs_M5ogQ9b8wggPWtRaeZs6qJQpBLJeXaHUSfqv0AAtyniakUOS9BrnyVDhJhRf1rqrGkHy1clvaHoTe-kcb-5VywFkOJW07POFEULlbudW2xY_ybzTQdZ78JWCe_oWxdEuDvqxP5VCfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد زیادی از هواپیماهای تانکر سوخت‌رسان آمریکایی از ایالات متحده و اروپا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140551" target="_blank">📅 13:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlOj5Blh1N_mGDhCTcL5Jnr8m3LJajfRzhVz1ML3u1GkrQgotPBIKHtBWZrmydcBwaySsuHTLb3PMbNWrOLNsra9XNf41oxztXDDOougq_s8lNgTHoVglFZd-eJgP0MhE_nz1a4tAoKS_mSixn5olcL12lrC3jNs8K-jI9bMd2prQ5Tgkdvr6W_aQLGf5BvG2cFfLDb44Lp7BGowh0KEsC8QYXZ23mhcC4vq_6kw4yjuJRSQ9jp-gN5CN0fecoUiCNRTFCkkuuur93-weq0HVlYOWls7s_Ugsylczbwa4fRpuwa8Ckv04ggD5HPpXIdhkVa5KWR5yxKVtAiQlaEQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۲ هزار واحدی به ۵ میلیون و ۵۲۰ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140550" target="_blank">📅 13:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قیمت دلار امروز با کاهش نسبت به روز گذشته، به ۱۸۷ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140549" target="_blank">📅 13:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قوه قضاییه : خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140548" target="_blank">📅 13:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X80WwohjfC6SiRxOxznXBUk4wlEqFQsHct0E982SpchYzcQ0KlDK7LB7LFq5HGJMn7o0g9gFcrSjtYWjM4uGiAt2y5aOroMH_lHzwuREh8CCXWtywyp7S9tgo5fhr8AFXBjdASMJHFXWYJqHREEQstG4x8eDWCboOQeHh8aIw8MnsoC2IzfCnLjVySxb3VfXHO5x5MXVnw_ZO2WR1uxs1yqEq1mL0YtfgCMyZroHPKzhs-TdFivA1PMfmPFpUgDU0Z_BtQih7ymvlz68kb2iIE1rm4kflpYGJBIOPY6o4mC1S3Wkl6UzKXjNyECpymhDWXlxXkAtCNqNjnbHHxu-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گفته می‌شود پیش از بازی آرژانتین مقابل اردن در مرحله گروهی این رقابت‌ها، فردی با فرودگاه دالاس تماس گرفته و تهدید کرده بود که به همراه دو نفر دیگر با سلاح و مواد منفجره دست‌ساز وارد ورزشگاه خواهد شد و مشخصاً از مسی به‌عنوان هدف اصلی یاد کرده بود.
🔴
طبق گزارش پلیس، مسی بیشترین میزان تهدیدها را در جام جهانی ۲۰۲۶ دریافت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140547" target="_blank">📅 13:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر نفت عراق: گفتگوهایی با ایران برای اجازه دادن به صادرات نفت عراق جریان دارد اما تاکنون اجرایی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140546" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae231ad695.mp4?token=E9EXUFxha60x6AdBmNL5LHARq7in9ttaa9xcNdswQV68FdoIh-yrykdLW6qRDo-HwtqAr8zLRICDt2lxeBxdIIPuWhw0lCRqSX6B1ez-sBQXUMMZymOeJlKGCD1aPq1nztI9xcRRYr-1USzD0kR6eSBmd5qpU_QldmTy1GVj5WkPgciVrJ8A-5rQ8yOhrrDrF092cXcf2R1Cics-AvX7L9_m4qZ565i8TWrIif6Tz4Nup5EAXq1rdKuoLmPzKVwgf-fUVYno8hKvO5h2dCA5gbPAG9oQu064yi2x1mpvsVZ0EB2OJtr3oIMbxbRwDPBz6a1diWXIh-uPAVOGAd0Y9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae231ad695.mp4?token=E9EXUFxha60x6AdBmNL5LHARq7in9ttaa9xcNdswQV68FdoIh-yrykdLW6qRDo-HwtqAr8zLRICDt2lxeBxdIIPuWhw0lCRqSX6B1ez-sBQXUMMZymOeJlKGCD1aPq1nztI9xcRRYr-1USzD0kR6eSBmd5qpU_QldmTy1GVj5WkPgciVrJ8A-5rQ8yOhrrDrF092cXcf2R1Cics-AvX7L9_m4qZ565i8TWrIif6Tz4Nup5EAXq1rdKuoLmPzKVwgf-fUVYno8hKvO5h2dCA5gbPAG9oQu064yi2x1mpvsVZ0EB2OJtr3oIMbxbRwDPBz6a1diWXIh-uPAVOGAd0Y9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جت نیروی هوایی اسرائیل در حال پرواز بر فراز جنوب لبنان در ارتفاع پایین و پرتاب منور مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140545" target="_blank">📅 13:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR5FmzrMu3RpNpEgSlPvcWvOGaGJdo1iUHsljAwc9ce8vuDjlqpo14L1Efn47SBISs0GfSPFYurL1N2YugkGtNsFgzf9djLT6mjDonoFmFUxQVJDbGgjepRfUKIMbsJEb0d706O3MPK3NmPv3NJrxCuaJQ4jseQ7Xsqup3FiCV4rsjldeKfvuyYl2fAV4O85Dy4xvItRHgWPGYsGd2dJ2ig5C-WEHdvl6-awrwMtRTZGlg4cKMFP64lPlbRnBLEUSjR0GHsm78CEseVjp16neQa0PVtGWKLnbGD9slvRzCh3SIYTVIcpgUAHn5pbZbe5I5MMz0Yw1nbe5THn3GG82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل از دیشب تا صبح حملات بسیار گسترده‌ای را بی وقفه به جنوب لبنان انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140544" target="_blank">📅 13:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dimQRpb3lfF_jSBl_y1nz5Bcm1WN49RiUZtD2hM84R53em8RslcuZRVQM9xEAc2N1ARm0gZIa_SKGqbGaYg_3epg4bnUblPNxagJkgnfvzWt8WXuoylN9cyG-WIM9cCxFVQrPq1F3AAZXMlNjAeYXz5EocLay4gT-NFKoh0ydGM9E-KxlHoQGvu-vcK6teSGpE42U3a12Mn6JcZVmW6cOu4mwMwXbIRJ9qE3IrO9E6J1uoHb9FObtQ-fyh7jK4g7VKKpGXVqAhhDO_MgDeydy-n6IV-hWxsesGufIxkEYe_YtB9cNY6zKyp52aGYoJHPMfOHfZvypfNVLJbnJaSc0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه زاویه لیبی اعلام کرد که یک پهپاد اوایل روز شنبه به مخزن سوخت پالایشگاه نفت در شمال شرقی این کشور برخورد کرد و باعث نشت سوخت شد، اما هیچ تلفات جانی یا آتش‌سوزی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140543" target="_blank">📅 13:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrWHud4Uqcdwz7bNVFdXNBYqFqcaegKz2FC-634F59wPGqKl9XXGehifpwuUVxwhg8kmlmLmbRarzliew4Rha2TfD7WwZklmQ7U5hKSjecRUqk6KPspKu2oorQYPuMGwCi70HuiTkLsWAchL80HPvSKmM-Mp7o6Pdy7JdaYdLwWUmmIh6GbwRnyzcYzmGXVn5MHs100U66T35TVVywFDNiUGVnnPnwmbw3loEAe8dhveEkFEWkEzUgAAI50KqEUIjeVFQnsbFV6Lo1lQsXgZFSSrC8EClo4Lvi6kB-8w51dSQajuK9Tg4ZHTIndRBYeoZyD97hxlKGimVwbNpb4c-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولایتی: نیروهای خارجی، عامل اصلی ناامنی، باید منطقه را ترک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140542" target="_blank">📅 13:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سنای آمریکا لایحه موقت جلوگیری از تعطیلی دولت را تصویب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140541" target="_blank">📅 12:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی کمیسیون بهداشت مجلس:
حذف ارز دارو می‌تونه ۱۴۰۶ رو به «سال کشتار بیماران» تبدیل کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140540" target="_blank">📅 12:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4976267c0d.mp4?token=jSGJ37tsbOnqKRmxfMgXAVSle5WBadgbqZLkw8N5FBWpDfpheq20xnmvqA39A1WA20rQAMwoKcKID0bMtQlwn8EzDnWbu38pILTFXYC21W7D17yyUdNr84p2dqlvblQEfswj90N5yWCah7_nF2YUk6eErZXF9FbhD6TKBNo50tXIImzLGWYrY6QDjkv7l4hux0PobJzPbdZD5I_B_Q1LNRvI5Tx8XcMX1l2cK1FMoWaKr9vKU3RXFwDMBbAIDVUl1XXcoUwuH-GOxeCqLO0PROdL-pdq5LQkN0DAZWElrvN3Ots52vAN7Mo__vDwEKBxulmiv7yZs0P9Ab4fhxxP-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4976267c0d.mp4?token=jSGJ37tsbOnqKRmxfMgXAVSle5WBadgbqZLkw8N5FBWpDfpheq20xnmvqA39A1WA20rQAMwoKcKID0bMtQlwn8EzDnWbu38pILTFXYC21W7D17yyUdNr84p2dqlvblQEfswj90N5yWCah7_nF2YUk6eErZXF9FbhD6TKBNo50tXIImzLGWYrY6QDjkv7l4hux0PobJzPbdZD5I_B_Q1LNRvI5Tx8XcMX1l2cK1FMoWaKr9vKU3RXFwDMBbAIDVUl1XXcoUwuH-GOxeCqLO0PROdL-pdq5LQkN0DAZWElrvN3Ots52vAN7Mo__vDwEKBxulmiv7yZs0P9Ab4fhxxP-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیل‏ ️جان بولتون: پوتین احساس می‌کند ترامپ در جنگ با ایران ضعیف و ترسیده شده است،روسیه آماده حمله به ناتو است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140539" target="_blank">📅 12:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
۱۱ سناتور دموکرات آمریکایی با ارائه قطعنامه‌ای در کنگره، خواستار خروج نیروهای مسلح این کشور از هرگونه عملیات نظامی علیه ایران شدند.
🔴
«جان آمریکایی‌ها از دست رفته است. قیمت بنزین و کودهای شیمیایی به‌شدت افزایش یافته و ذخایر تسلیحاتی ارتش ما تحلیل رفته است» این اظهارات سناتور آمریکایی جان هیکنلوپر در پیامی در ایکس است. او در ادامه نوشت «به این جنگ پایان دهید. همین حالا».
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140538" target="_blank">📅 12:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=LL5ppmrmRtJlj8V9y_ujiCTZl-t25rr3ybWom01OKFXmUIIEJDwiwLlSfj690QP1X1G5HTZgAU9ZMMap8QUvYwYctkBMMaqXOSBOr9mk2zvoqXVf4yZUGbjUOiQFVqQWeXEWEqMmk9bo5PYdlKvLozNtQaps8JtPXHqZuUq9Af1aq_lUGaxFpluTw-nnuEChpMHTjkEgiNd5ztfkATUPDNgc4fb4_f78HBacc4IhB-nFY61j6KihxSKqsMQezQlh8NAkOUUlZNOCVKEa8dUkeI-xCUvPU65yTYxLNbsvjZCuMWvoxz33_TAWtGFl2vW2j5BxIn_8U2un_CmQsjOxdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=LL5ppmrmRtJlj8V9y_ujiCTZl-t25rr3ybWom01OKFXmUIIEJDwiwLlSfj690QP1X1G5HTZgAU9ZMMap8QUvYwYctkBMMaqXOSBOr9mk2zvoqXVf4yZUGbjUOiQFVqQWeXEWEqMmk9bo5PYdlKvLozNtQaps8JtPXHqZuUq9Af1aq_lUGaxFpluTw-nnuEChpMHTjkEgiNd5ztfkATUPDNgc4fb4_f78HBacc4IhB-nFY61j6KihxSKqsMQezQlh8NAkOUUlZNOCVKEa8dUkeI-xCUvPU65yTYxLNbsvjZCuMWvoxz33_TAWtGFl2vW2j5BxIn_8U2un_CmQsjOxdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری جالب از برخورد رعد و برق به ساختمان مرکز تجارت جهانی اسپیرز در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140536" target="_blank">📅 12:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پزشکیان: کسانی که فاجعه هولناک بمباران اتمی هیروشیما را محکوم می‌کنند، باید ذهنیتی که امروز در آمریکا حاکم است و تهدید به تخریب زیرساخت‌های غیر نظامی می‌کند را هم محکوم کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140535" target="_blank">📅 12:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل گزارش داد هشدار امنیتی درباره احتمال نفوذ افراد مسلح به شهرک «عفرین» در کرانه باختری صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140533" target="_blank">📅 12:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع روسیه از حمله پهپادی به یک کشتی «حامل تسلیحات» ارتش اوکراین در شرق اودسا، بزرگ‌ترین شهر ساحلی دریای سیاه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140532" target="_blank">📅 11:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
جهانگیر، سخنگوی قوه قضاییه: رأی مصادره تمام اموال منقول و غیرمنقول ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140531" target="_blank">📅 11:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yroy7z7WUjJ8-R2j7mxAIGeHKA6fTDfJ-IvTS1G8Sb5pOrLaROmoTK9sooccRN9u8vMEAZQmBNIwqZCJOQGOx8aBXdxpdkLI--aSWDq4_28nzKkt7btQbk2DeB7FghuMG_wb-XZuhvtFYEiQp4PVmVoIr7MM5s6UDzvwP6h3KAP5XqzYuZtnDxdZSMt8E2znEzi_WbSxsfxd3Vg6k1Z8RYQ_BQLUs1SSx-Rm5XDZIOmgO4JOZSh-3FCjTtAlLEWOPxalXPX9Rn8WyOPg50NljEInYzDKkjU-6jjpw9mt0xscC-Ako14eg6-lY6YH_4zTgjyGLTkmnSeO7e70VyovHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیمرو در رستوران‌ها یه 2میلیون رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140530" target="_blank">📅 11:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کپلر: صادرات نفت عربستان پس از اعلام محاصره یمن از بیش از ۴ میلیون بشکه در روز به کمتر از یک میلیون بشکه کاهش یافته و بارگیری نفت در ینبع نیز به صفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140529" target="_blank">📅 11:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efb71292a2.mp4?token=F-i-3KSvYGjTqElMHegQRCabQAVRKATK-l9jJ6_ri3H2e7LuGoPd-A2N7xAttKvkqwj-BkiUFBEO3f9cb3Gshsf3r1w0FE0uIJaP39IGPfW7xJvTiOvkOMLimabWjUIs8W-r9e7iyKT1I2v5yO6xDC34_cSk3ruFp3t2bOG0JlhV3IYWlkhXlTFSbKp3_E0lDaiz93uo2beKzibDlovxYXEo09GzwSTl1aKohKSGHvpIQk7KIxLCqy-6JezQdRbDl2n9iNo7QBUsQI6J40Y_gQ9f_LaCBkjDPNxa1IgkG6ckXXhCogeqj_dGsPC0Y52GZSWlwj4zfTLna6BynSrm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efb71292a2.mp4?token=F-i-3KSvYGjTqElMHegQRCabQAVRKATK-l9jJ6_ri3H2e7LuGoPd-A2N7xAttKvkqwj-BkiUFBEO3f9cb3Gshsf3r1w0FE0uIJaP39IGPfW7xJvTiOvkOMLimabWjUIs8W-r9e7iyKT1I2v5yO6xDC34_cSk3ruFp3t2bOG0JlhV3IYWlkhXlTFSbKp3_E0lDaiz93uo2beKzibDlovxYXEo09GzwSTl1aKohKSGHvpIQk7KIxLCqy-6JezQdRbDl2n9iNo7QBUsQI6J40Y_gQ9f_LaCBkjDPNxa1IgkG6ckXXhCogeqj_dGsPC0Y52GZSWlwj4zfTLna6BynSrm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون وزارت بهداشت: حمله به لامرد با بمب های فسفری بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140528" target="_blank">📅 11:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6e59b058.mp4?token=tlVf6u2AOOzrrB9UWylTvU-1LRbuvhK4U7Z8N9ad4Kr15-nhr98gm59Qhv4znKR0me2VijIF5jjY5fsPtj0vFTQxiuMwWqzw76QAZe1PWCuTthkddUuvitSCYd2JknXo4IUDIheqV9Z_Bzhfc876G5L5-xDI6rG7HVDGTAuOum6LKmfhCnJDN1qOrkcPPCcAsCJuBrEBXvGF_QGoIWQOZyBWcvf6TrQcNU4xUCEHVfpQ1gXNK_ZmLnJ2KEgyf0FYNaFfH4XhjOm7QeTKmhg0PWwSJXheanKYU5Rp19wpTd5fCAwj1vmHB9FCHqwi60_WJeCNZe6KLn91gkTn9bIhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6e59b058.mp4?token=tlVf6u2AOOzrrB9UWylTvU-1LRbuvhK4U7Z8N9ad4Kr15-nhr98gm59Qhv4znKR0me2VijIF5jjY5fsPtj0vFTQxiuMwWqzw76QAZe1PWCuTthkddUuvitSCYd2JknXo4IUDIheqV9Z_Bzhfc876G5L5-xDI6rG7HVDGTAuOum6LKmfhCnJDN1qOrkcPPCcAsCJuBrEBXvGF_QGoIWQOZyBWcvf6TrQcNU4xUCEHVfpQ1gXNK_ZmLnJ2KEgyf0FYNaFfH4XhjOm7QeTKmhg0PWwSJXheanKYU5Rp19wpTd5fCAwj1vmHB9FCHqwi60_WJeCNZe6KLn91gkTn9bIhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهمات سرگردان
RAM-2X
اوکراین، پدافند هوایی متحرک روسیه رو هدف گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140527" target="_blank">📅 11:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=RL_Qfo4xqb7dXCI-wT43_N6-7utxr8AUUYiFAsLTKRY-Z8RcqrQh7MVnVG5D3v72Kk02-aXCYUwdhdaLCESvvwI8M7UNrDGZJS10EuHZm8GDtP10yyASMla97PWBPGD2or88jNvKFjrgSkAbno9J4gX_Lxk3wSYBPBkGPGiO5SpRBsELX-X5Juqw-4PBcjCBSxINssBQpmInf0kSzUcWIRaXhm0oF6_yK2unsCLHrjKjlAv6AyfmCdNnukMORGBJ2UkdCuGx6gHPpzyb1xfackaT6waHAdXPkxykfg30uIfQ8CKM3aJLv1P9yU0_xBsF42iE6m31x4xT5pVc2p4Mmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=RL_Qfo4xqb7dXCI-wT43_N6-7utxr8AUUYiFAsLTKRY-Z8RcqrQh7MVnVG5D3v72Kk02-aXCYUwdhdaLCESvvwI8M7UNrDGZJS10EuHZm8GDtP10yyASMla97PWBPGD2or88jNvKFjrgSkAbno9J4gX_Lxk3wSYBPBkGPGiO5SpRBsELX-X5Juqw-4PBcjCBSxINssBQpmInf0kSzUcWIRaXhm0oF6_yK2unsCLHrjKjlAv6AyfmCdNnukMORGBJ2UkdCuGx6gHPpzyb1xfackaT6waHAdXPkxykfg30uIfQ8CKM3aJLv1P9yU0_xBsF42iE6m31x4xT5pVc2p4Mmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک ارزشی: این چه وضع حجابه آقای پزشکیان؟ من هروقت بیرون میرم تحریک میشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140526" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
واکنش بانک مرکزی به ادعای ترامپ درباره تورم ایران: تورم قبل از جنگ ۴۶ درصد و در حال حاضر ۶۱ درصد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140525" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز: اصابت یک پهپاد به مخزن پالایشگاه شهر الزاویه در لیبی باعث نشت شد و این نشت اکنون تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140524" target="_blank">📅 11:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الجزیره: بعید است که عمان گفت‌وگوهای خود با ایران را بدون هماهنگی با آمریکا انجام داده باشد
🔴
واشنگتن‌ از مفاد توافق احتمالی بر سر تنگه هرمز، آگاهی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140523" target="_blank">📅 11:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: در ارتباط با اسرائیل، همه دولت‌های مسلمان باید متحد شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140522" target="_blank">📅 10:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز: قیمت نفت روز جمعه به شدت افزایش یافت، زیرا معامله‌گران همچنان در حال واکنش به ابهامات پیرامون تنگه هرمز و مذاکرات ایران و عمان بودند
🔴
نفت در پایان معاملات در این روز، ۸۳.۵۵ دلار شد، یعنی حدود ۵.۷ درصد صعود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140520" target="_blank">📅 10:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_nDiZnwFar4iVWcooDEMGC0XtDTet3SaTEjUKBOvX2F8VaGBl4bRCizUdt1IgfQ2e56XVw3CuyfsWbAQMGdyyZN_60KqL7gX78-eYr67aA7CktSjU-aj_lxSw82FEvkeX_5rs27vRmysOMN0PpXqzf5gQUDgpL_baqvCRtv7cPySBGgC79RSyDfEqKQAytrmDrmV1vy8AcGrdlocHwtB5NxeKTlPEBgFm2CCU6eRjfNSYhOGlYUAjZAeBD0XYM8ZxOhAUlvGKPdtuaUH13HosDVEPgZeBfGyNnBquy4YdpRerTMVcWELa-L0gyBMInGtydUunW0RREq2sZ6kvO0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به اطراف تپه علی الطاهر در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140519" target="_blank">📅 10:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e96kk0BMI4jfwJv4e_nVJUiHJZQvTjdDJzdgdw0DPlqrdz9bXy9BwBJuYQlErbyuDXcOh-7oPK5dahEFoU3oc2RbrvvtSEElnh9-boo0a9yKpbFW_vvg8etCRwEplag9mc8coyrkJfnF4j4FUd60HxOrXZAJp49B64JtXsD7jZ6G_ZDxNHvP0wS6Mv4FR8HW6IOeRBRmbLh1ZXmg3OxxWxnh8FjeMeLLOqihhPioVStZub2r2FpcuU7MUVmJwSwmkajjQqq_MfbDw4VNrp61_PrzY4xz0D4X2XS9HpvDyG2PbJX8HtMdOB5vU2S90iUsqqpS64nUJ7k5Npxkkjn9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بایدن حتی یه هندیکپ ۱۰۰ هم نیست.
🔴
(یعنی حتی نمیتواند توپ را بزند)
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140518" target="_blank">📅 10:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ساختمان‌های مرتفع و برج‌های شهر ریاض به مناسبت امضای «توافق‌ مکه» با پرچم‌های سعودی، ترکیه و پاکستان تزیین شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140517" target="_blank">📅 10:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بخشی از بگومگوی ناصر هادیان و فواد ایزدی درباره رای گیری در شعام درباره تفاهمنامه
🔴
اظهارات عجیب فواد ایزدی: آمریکایی‌ها تهدیدات سردار حاجی زاده را باور نکردند؛ ایران بعد از جنگ ۱۲ روزه به آن تهدیدها عمل نکرد!
🔴
ترامپ ما را مسخره می‌کرد
🔴
اعضای شورای عالی امنیت ملی روی مقاله ظریف اجماع کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140516" target="_blank">📅 10:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت دفاع روسیه: ۸۳ پهپاد اوکراینی صبح امروز بر فراز چندین منطقه از جمله مسکو سرنگون شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140515" target="_blank">📅 10:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
الجزیره: تردد کشتی‌ها در تنگه هرمز طی این هفته باز هم کاهش یافت
🔴
بر اساس داده‌های تردد دریایی، روز پنجشنبه تنها ۸ کشتی تجاری از تنگه هرمز و ۲۶ کشتی از باب‌المندب عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140514" target="_blank">📅 10:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
عطریانفر: به‌کارگیری به موقع دیپلماسی، تهدید‌ها را به فرصت بدل می‌سازد
🔴
بی‌تردید قدرنشناسی، فحاشی و سنگ‌اندازی نسبت به مسئولان، موجب دلسردی می‌شود
🔴
رقابت‌های سیاسی باید به گونه‌ای مدیریت شود که تصویری از ناتوانی در تصمیم‌گیری ترسیم نشود، زیرا این موضوع دشمن را به اتخاذ سیاست‌های سخت‌گیرانه‌تر تشویق می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140513" target="_blank">📅 10:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL4s5hIJm_0hLGB6t6nuQc5rzQYgjZYSNzw1ywixNwlrd0bhmfzQn0GE3gy9_ZBf_XREW-87GeeoBMgTS_8joMLPBxMBBVKbsQ2e96_YH3cYi3CXr68U1Xd5kLEydsmDyqaF4OcOQGqor20lTbQtWWe9OCpIZpUd3VvUmGA9dkvhN_LwjoBARTNG_btF_LQiWUtgMvSelqRpPz0c3o-3ycY9xZ2swYN9-M7jvMHJH7KVD1ZqEeA--I-1oCp_EElP2nQA43E6GmepGQvAo8UnS_k_D3rOXJs6z4N1dnUMwucsTDECMgGApctyrbsJzWc25zYntIhDN3KHkg3NcSFq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع آمریکا، دسترسی امنیتی "فرانک کندال"، وزیر سابق نیروی هوایی، را لغو کرد و او را به افشای اطلاعات محرمانه درباره نقص‌های امنیتی هواپیمای "ایرفورس وان" که  قطر به ترامپ هدیه داده بود، متهم کرد.
🔴
کندال این اتهام را رد می‌کند و می‌گوید که به او اطلاع داده نشده است که چه اطلاعاتی را به طور مدنظر افشا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140512" target="_blank">📅 09:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ofgQz8ETCd8rIcnPHtwkqj-GHxaCJlV6ICRxK43lNKntF1vF6KBuajdI7hkzv-9Wvwfax9fVz42MJxwEvEu8TAVih4CYwhYR9bNWU9zAweX6LUo3r0pzkAqAN7gofO-yafc3wfJSr-k-hfDLr5Mw4go6OS4SEPH4HnaW-AsE5A0uSc12DWhMUiqIwzL48Z1xbaaiIESPoK8rwwabDsyyeW5EKuB7tDeCdoszpWOCyghBFVWi2_UN9U4_NCXHU3suzrO8A8dZfG5p8sM7Yyms1NVeJoRWbDN0S4XrzAn1LuE2j9c0_mcJ9BMUV3cRZU98qM7-JcEbttnCeE9WwWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلزله ۵.۶ ریشتری آلاسکا را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140511" target="_blank">📅 09:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ای‌بی‌سی به نقل از مقام‌های آمریکایی گزارش داد توافق موقت ایران و عمان برای بازگشایی تنگه هرمز قرار است ۶۰ روز اجرا شود؛ دوره‌ای که هم‌زمان مذاکرات برای ترتیبات بلندمدت هرمز و پرونده هسته‌ای ادامه خواهد یافت.
🔴
به گفته این منابع، جزئیات هنوز نهایی نشده است. آمریکا خواهان آزادی کامل کشتیرانی است و با هر سازوکاری که به ایران اجازه دریافت عوارض یا صدور مجوز عبور برای کشتی‌ها بدهد، مخالفت می‌کند.
🔴
پس اختلاف فقط بر سر بازگشایی هرمز نیست؛ دعوا بر سر قواعد عبور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140510" target="_blank">📅 09:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78924983a9.mp4?token=Py73qai4NejphXncxDpH82YyjUfDXiiTttJC9-tfOnmqvHYirlss8yimazeepD7Qncisg4JU9uZreZFRhhdQQ1MFrWI_U2CFP9gHFWHq5mj7hJmd6DvUBOsi2zm6AKNDaE5WjB80PuDoPrsAJqBsWGFRLMDTIZsAsXq91__dbJdG5VunHncbi0t4z_APCZ0atGBRI2gBRIb9HIdIvTNCx0P-zSf09Wiz4XYB0ijRqYlBTIECO1cmgrWsXEflJ1J8ZkZNvwHv2Jw9I807psUttyfIANJ6qAPdUryDusT7YmyDfAfdcpkf-Wp2WDd6Z910Dx1_C5AmfAPV4aKLmz4lKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78924983a9.mp4?token=Py73qai4NejphXncxDpH82YyjUfDXiiTttJC9-tfOnmqvHYirlss8yimazeepD7Qncisg4JU9uZreZFRhhdQQ1MFrWI_U2CFP9gHFWHq5mj7hJmd6DvUBOsi2zm6AKNDaE5WjB80PuDoPrsAJqBsWGFRLMDTIZsAsXq91__dbJdG5VunHncbi0t4z_APCZ0atGBRI2gBRIb9HIdIvTNCx0P-zSf09Wiz4XYB0ijRqYlBTIECO1cmgrWsXEflJ1J8ZkZNvwHv2Jw9I807psUttyfIANJ6qAPdUryDusT7YmyDfAfdcpkf-Wp2WDd6Z910Dx1_C5AmfAPV4aKLmz4lKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ترامپ: لاولی ایسلامیک ریپابلیک آف ایران
!.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140509" target="_blank">📅 09:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
اکسیوس: گفت‌وگوی ترامپ و بن سلمان در مورد ایران و تنگه هرمز
🔴
اکسیوس از گفتگوی ترامپ و بن سلمان در مورد ایران و تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140508" target="_blank">📅 09:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140507">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رسانه‌های عبری:  مهاجرت ثروتمندان اسرائیل طی سال‌های ۲۰۱۹ تا ۲۰۲۴ دو برابر شده و سالانه ۷۰۰ میلیون شِکِل از درآمدهای خزانه اسرائیل می‌کاهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140507" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سی‌ان‌ان: ژنرال کین درباره پیامدهای بمباران گسترده ایران به ترامپ هشدار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140506" target="_blank">📅 08:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwq2Hj7mDzAlDr1wZXmZ_lsB0eql0wjnU6mPF5GCOCZgyfH-6yG7QNjNwyOPd4rsGwfmuLJDAk1jBc-ErM5Zn2xRMTl_kbjVvWZVhomdQp2KF6qNsBG_2IINPAex-nnR7Z5JPa6b3mUY3D_R9FPIeQ7W4TF6eHKZXhsUod7hFrZO74krd4rE13AYAYYhbuxSLdNR7aGQFGkU58i--FtrfPgXw36NNou6YBhdvcFsdu0P2Ug5i8cPsS_5AfSE-UH3O6phtpcHyeSqSh9znoaWZEy-oASvc3MNVHo6ZYoEueyP9rme-sQLj5I29oqJskx-jOIk51DmNZ-zM3gAD5Nn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی تخصصی در زمینه مبارزه با آلودگی ناشی از نفت و اطفای حریق، در حال فعالیت در منطقه‌ای است که یک تانکر نفت در تنگه هرمز مورد هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140505" target="_blank">📅 08:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAXnGtWxR1b8_8cIl0yie-4zn8GLM5q4tgK1vlXeo6SgZ7Mbz_nruIGX4iV8RXSWkkkUVa5KpmqhmMKuQAvxhie8VlpnzcamhA6-E4PCApNBAL22Co7ibhat1i8oUDr9L_4L7t18_l1dDADKasYqw_T2QH4oJ0gKK-lzxV4JeA3YkQTGtdE-9lm9GiQCBjhMgOIR8HVbw1782grBYBcs9RorOmAg0d0OoNtJgKZMmf4E1TYO0vE3jV27slkL1G3qhYJpbvmD-24KfWe1Gobnx3093zCfpJxPmCj1ryOjDYQ0xicuMwT3Vww3mPXFHbu9o7TnG51vTJ2Ad4jGUnG7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش‌های منابع عربی حاکی از حمله به جده، عربستان سعودی است و به همین علت هواپیماهای غیرنظامی از فرود در فرودگاه جده خودداری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/140504" target="_blank">📅 08:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حمله حسین شریعتمداری به پیمان سه‌گانه پاکستان، عربستان، ترکیه / سران این سه کشور در قتل‌عام غزه دست داشتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/140503" target="_blank">📅 08:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194ac9d25.mp4?token=kSUtLKcltGjxHhNM_tzbpTDg7WvyVnK3c5nvEBWEQg-P1kEOhi8y9tWdEr7Cuz6gnTAFL3xbnP9QbJmP46peQJoq2osw2dVaALdO_MuS50AZp2hY5_5DrXXHi6VOTfpJhhaaBb9GqdVbSxjwdIj7nc1z97XpNveJxCNprJ8_l1MyUqsi85AQ1OSdH5iBnsCsYhPfZm6PugGfhyfur2gJmThHjRx4RFWyPOZCP4T1m2OU-HxJGdFGddjhQtU7V_Ur2cUJ_IXjo1dxG6emG5MkWYKGHBTceY6fLv9pV9eIpA6UQp1geET_2XQzGBPyN8141K3WIoMiDtFPiA3gi0CCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194ac9d25.mp4?token=kSUtLKcltGjxHhNM_tzbpTDg7WvyVnK3c5nvEBWEQg-P1kEOhi8y9tWdEr7Cuz6gnTAFL3xbnP9QbJmP46peQJoq2osw2dVaALdO_MuS50AZp2hY5_5DrXXHi6VOTfpJhhaaBb9GqdVbSxjwdIj7nc1z97XpNveJxCNprJ8_l1MyUqsi85AQ1OSdH5iBnsCsYhPfZm6PugGfhyfur2gJmThHjRx4RFWyPOZCP4T1m2OU-HxJGdFGddjhQtU7V_Ur2cUJ_IXjo1dxG6emG5MkWYKGHBTceY6fLv9pV9eIpA6UQp1geET_2XQzGBPyN8141K3WIoMiDtFPiA3gi0CCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویر ماهواره‌ای نشون می‌دن که یه کشتی توی تنگه هرمز داره در آتیش می‌سوزه و این موضوع تایید شده.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/140502" target="_blank">📅 08:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g69BC5B0LT3ooOy0kQwJ_4c1VsIJ99Og77rclGLyqlKX3Af-H1sJNbdJx3tzbEi2CdlO5HHBtYd_aXUh0ijq-3ZSoW5ojSDpgIjTaM6iQkgFYxDeHzXB55pRO3qXhpVQVC0kKUJwS1WnJSBtQ4TDKG3TLGHmfK5qVgcbXHNYtXDQynPnzEUuTpsZy_-oh5Hk79oNN6Ym2wtKwbkcoUSYoqjBUadtNVctl5gtwRZbTPoDIoQ8LGWBooQK31_3RgIWX0uaiwlqUIK_68f_qY_B_JwcyRcsEamX5PpLLUOIR0BVggpl5rBPVB63a3xA9kUzm9RRJmUbZCE0neR62BRJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی ان ان: ژنرال دن کین، رئیس ستاد مشترک ارتش، به طور خصوصی به مقامات ارشد دولت ترامپ روشن کرده است که ایالات متحده باید «راه فرار» از جنگ با ایران پیدا کند، زیرا معتقد است گزینه‌های نظامی موجود برای تشدید درگیری ممکن است نتیجه عکس داشته باشد.
در حالی که کین به ترامپ اطمینان داده است که ارتش ایالات متحده «قطعاً می‌تواند آن‌ها را نابود کند» اگر دستور داده شود، او همچنین بر محدودیت‌های نیروی نظامی، نگرانی‌ها درباره کاهش ذخایر مهمات ایالات متحده و خطرات یک درگیری طولانی‌مدت تأکید کرده است.
در نتیجه، مقامات به طور فزاینده‌ای درباره یافتن «راه فراری» بحث کرده‌اند که به دولت اجازه دهد تنش‌ها را کاهش دهد و در عین حال ادعای پیشرفت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/alonews/140501" target="_blank">📅 01:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
در یکی از بزرگ ترین قراداد های نظامی تاریخ خاورمیانه، ایالات متحده مجوز فروش 5250 موشک رهگیر از نوع پاتریوت و تاد به بحرین، کویت، قطر و امارات متحده عربی را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/140500" target="_blank">📅 00:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8192485a22.mp4?token=WIi_u00m9IxjSwyey2NKAXCdmwJncrL8I-stTyLNHWdYiCHMO8tok3E1bk1NbXZ4iaErLGaUWIXRsK0SdOMr-lsUVCB77gmKmTJXOTOuR6NiS9oZlDTmwy3Tde2c0lsLBp2pdYUkM5Glq1oukn3k95axM0dxpEwOzbnm2dmXdysGbO-0bNN9VLFhf_7IKio5nAtSqDvvEYAnr9PqiDymPIXsfN-LnqS9D_DlMwesZw2FFMGiEuaA8DKEHIeB6phyhKcB4mAc4J-o6MycnQbo0wYPg7mYS6IYffnfCHM_CNlZ8ppbSWA8NDELXMoc4LdzEwUWWwhgQ4EqexvxBCaSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خطاب به خبرنگار‌ها:
ما یه جنگ بزرگ رو درپیش داریم و بنظرم بهانه‌ی خوبیه واسه اینکه اینجارو زودتر ترک کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/140499" target="_blank">📅 00:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd08a7bff2.mp4?token=KMAAD6JDsySYr9lzsxrQlr1xvwLkgfZqFC1V1ElUHDCdMRzEYuYK5-7MkQndxLeYjvJ5h1rTKWoK4VfQiivlvju6gHc58jXoI_ET1WSJJrSTQrOiZi49W3hpOezoL0qRfKRO1RTdIytxGIlJl7_jQam8dSYIWQr3mA2uHNSsMC1oaS0ASccEyqzyj4zUaiZ8ily8tK-BIaagPbF7ez6dt-_PxOQcJRVc070GbYrE39goFFqU9V68U13toa4uUcR3zO62U3668RcnpKuooVAnUOplhCAmgACOaIMm6fqTULc14HiaVOyix9W7qLEFK-3Xi130wMizIs9DmvWmEfUwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت دونالد ترامپ با هواپیمای نیروی هوایی یک از پایگاه مشترک اندروز به مقصد فرودگاه شهری موریستاون در نیوجرسی حرکت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/140498" target="_blank">📅 00:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422b0ac1f.mp4?token=t6hcNDN8gJzG7vgHH5S1kPmrFY2fVV2MEClmB_Y-DX4kKJh8saSc-4ew2Mtyy8N8NgAno3u2HThNPdT-V0wa1OhicRXLBtHdzxAkrEDPLDvpzFNNewiZpseh-fzZGCFJGAJrCa-6aHP6U_TmDsmFMRyzfeyK2D72UrGQqNdz6aga6rqqAQqN7n-g7A9jjrtw3siQ4o29D2gkBESQGWgXKgdKbBEh78jgmwysGnv3hJytzgkABRlf4yWtMIeufN0ufWlRYYq63JqU4jfD9odWLYC3aBDELmPRYmIzeFeOjeVQPo53ktho6SkAFbu1xox6O0loHAscz3HFornzAL9prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: اوضاع مردم خوبه و تفریح و همه چی سرجاشه و همه راضین
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/140497" target="_blank">📅 00:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEyTt4ib_beIvHPquV763HvxCvs31-k6fDa1y_vPo0kTlLIVj8x_PjEjkBYfzbUXHjo7IgpDOgF7vRhKQ0b3r2wHRR-GqBBlecaxxFTuyT619l1AEXedsbXPTlD8AgyAUGarpI-GS3-KCm1ObWCmyq50axtX1yRAGdedlEEBfb9BRBXljy7e7og0y3StgoURD7wZCWtzjBVpfW_OLAZ2IlTi8PZingukcGWoet-9PJS3YxWd054Jqrd9ucxawiKvRjKiRn5kNKZA7BhKRpqlkeVL6bTN-TL8DbAxZqmsDNmUqqOCtC2t6C6VG_CQvmEg3R-MreI74Q9kdP140aVFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
یک ملوان آمریکایی در مرکز اطلاعات رزمی ناوشکن یواس‌اس میسون (DDG 87) در حال گشت‌زنی در آب‌های منطقه‌ای است تا از محاصره بنادر و مناطق ساحلی ایران توسط ایالات متحده حمایت کند.
تا امروز، نیروهای سنتکام 51 کشتی تجاری را تغییر مسیر داده، 2 کشتی را از کار انداخته و 2 کشتی دیگر را توقیف کرده‌اند تا از رعایت مقررات اطمینان حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/140496" target="_blank">📅 00:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAXplt8s8dTemStZ7USvdxkUwJsfIg6pSXI0_f-s-oPIFtRcMWJlgHD0bx0De6jMZMrHOeeOZxMJvzTqSndptEyJZS_JyBn2SdyD1VcuB7Q1TWDFLaxUWp1ge0ndhY-BZuLNmI3YzY6kBM9UDbz9RabZ7Wzwli2YWGBol_Df9N7qjt_mc24BErQwLWuO2GoJUiCvN1U787GBBJdCuWr7qLBtF1GXJua37xg275E12FsPDVcemVTPcyFclHfmf5FBRZzL5ce7WX9i0HBjv6M71P7k2pzdy4dpLexTIUUM36LVrxflkQoPPmOQKYoayLri774sBu0w1XWTElpWgYEdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/140495" target="_blank">📅 00:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/140494" target="_blank">📅 00:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVIkEFcSmriHDOpdfCCc31Y0bW9M37Cgkbn2X_-_fIrA3zLRm2Hx_yaO9bkDsEocXfqnNv_QZ7JkLc6_YnDIu7HM5K2VdOuyvIAc074G1B1B0wgYornCLYB1L9IeEES2zSX1feiAX3Z3JWQdr0WZhnbp8Qwq3SHgmkEqareUHt9xMqohLeYs-lEH887H5i2BofUSOJzqwzQQEbla0YJNWOAH9bbkZkDXji2n-UL3dbH4ofVuCVAGNIb5BQZaU9NaJc_IV41FxLYi_dgN_sz6V4-rff37mwTL1tLbnaBYBi5VTyKILpJPoO6khBiGUxiMzxXYvS8HIsTl9_sB86YlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش تعداد سوخت‌رسان‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/140493" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXCZEN8NNBPAUVoglpI90drsmydygkLwmX_TAxShnsABdIysKpGbuN5d-nvzmGfuQCMns7n1HMOBBCkXcFPFlqqNHz13kK_3fGk_j8Ynrs-8aGSVf526CQMfdIwsko1NV-lCwZ8FoMs2G1uaAaCHyLgfFMSFFl2zY5zWZJj1SPHf82QxB6i_lMN76KAfdAN8FzPjcfdQQlmWDjteiNwdES6aJQWVqbZ0iZmz57FEOh7e2FkJtV0DT65Sxc1oEJ04iznaPKnPOIFVhc5FsmmyZAKPAYyxkZx31YL9VCgMEFPVfFU7anSK1PGC4BweALVU8saKjhQc-MWxKZnOTk0J2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با برخاستن هواپیمای هشدار دهنده و کنترل زودهنگام هوابرد E-3G بین کویت و بحرین، چندین هواپیمای سوخت‌گیری از پایگاه‌های ایالات متحده برخاستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/140492" target="_blank">📅 23:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سازمان ملل: منتظر نتایج مذاکرات درباره تنگه هرمز هستیم
🔴
معاون سخنگوی سازمان ملل متحد اعلام کرد که این نهاد بین المللی در انتظار نتایج مذاکرات میان ایران و عمان درباره تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/140491" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHHeZWEAeBTpDkfusPrrb6qCDG7ZzLXEvJvS8plX_PAxPJ3sr1UgEQZXu3dRHulGFW5BaMgkdui2soo-OkGxOpdhRAXTdOI5VbJwvYXkM9UR3xx_iJVEkoHw3WCACdE3q6LC6aNVoXst-oMtcJnepEHOuh577BkZaf02HtEcgnoRFn1L3wjzaUQ8CGKeqj3knLawtTMezHX6v1myux9BHboL_8sKUptGKfPw3SqHXV9AEV0WdW4vOPDyiXqBWr6cB4CbjeiJVnRaE0bajGy2TaUgTPIpEFaImQHsNequHJqERBBvIIhXNbEP6YQGbfZaCg_mxXEGD_OIJXUlJHs4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت هوایی قابل توجه آمریکا بر فراز تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/140490" target="_blank">📅 23:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/140489" target="_blank">📅 23:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOLKSxAk-va0W6-oprfYHiZphHnz9_xC_F4zSw9vKfPtDm9Kpf6K_RM_YkdTC9kzHM8JzMcK1tpvvO2dBvOZ0jLdZzN_8bwYEsZQ4YSR1z0Ao0CvKrbHPo0eXfyKuzl94SSj68evSZRhqZIk43FBuV_WTKc9O7WMI6U8-t3HD5OxyL_OvshwjSZgZzIQsNMODcIr4tpkmAEsSYJ3SFYp4rRN3W_MsX-SdNsHoskQGiU2H-bU1qo-LTHP1TLcsevtvpo9jLKKFATGF-wLtpRSbnM4Uhov6Di3m_ptdmZJKciOdh8FBcf6M7T_yfJTBGUxp_pKUm1FGrTev0i9kuFO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقایقی قبل مختار توسط صهیونیست‌ها کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/140488" target="_blank">📅 23:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آبان تتر هم به لیست صرافی های تحریم شده امریکا اضافه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/140487" target="_blank">📅 23:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
دستگاه اطلاعاتی آمریکا درباره ماجرای فرودگاه لایپزیش در آلمان
سی‌ان‌ان: دستگاه اطلاعاتی آمریکا مدعی شد که پهپاد حامل مواد منفجره که چهارشنبه شب در فرودگاه لایپزیش در آلمان کشف شد، متعلق به سرویس‌های اطلاعاتی روسیه بوده است.
🔴
بنابر این ادعا، این پهپاد حامل مواد منفجره بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/140486" target="_blank">📅 23:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78924983a9.mp4?token=sLXRBiUeXmwvHHNLVWnVg-VkywXNKdoOOE8zXQBfSTtgMR89eRLLOo4EPskXXiJSroMuS5C2ez3QgnHJmbT2YI4tNOvvCowk_Hz4ufXznSQKUFzQ-nT9D7kR2NmGDCdpAq6r95esK17KCMZGgdhmCyufHGjORofnraIK_bT3j45L3lyAXbb62DBp3cnzrDCVhwk9Y_uRnDukz6qHQrlk7Jg5HR-etGma7Bb7_TALkr6bOw5A7RHru6rLWFA6rcHLqH5d56jOhMW5AhlIIofbFKSUKHLZ736KtS_cpv5BXLPU22S-wm7lhkGMOYHjyCuQt4E7KPZWwECMhS67jhft9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: لاولی ایسلامیک ریپابلیک آف ایران
🔴
جمهوری اسلامی ایران دوست داشتنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/140485" target="_blank">📅 23:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889f666c39.mp4?token=o7fuNb7ZU9jsW9wX8DWCUT4e4xE1nXtvMFNZkg9Wzs3O80H48jnnBdZkC_z1427oMUDYN1NfpeG5DLrwr-7c05j6aXi9GlVwaqs9L_Mvcx3lLNhQjRM8ohKkEy64DBROeDokRRrH2SDUmYeBsRpiDPK1rS3bBGx6aLfCMouo-e49LtPfoPTh5MD9nGLbtmfx0JBY5-juCXDnw77nBNwWZSjC66rMYWHGJ2AkkPi8KJxpa-ZhUOKcSa7aIUHV0eaaSq7h0X40lM40wDeYehetBGOwj6z-Vj8EkHLZvZV20-nW_7hf2D6IFPpGGwEOP_MH_CQERxTNT0IFHKaRLFx63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
برگزاری نماز جماعت وسط خیابونای لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/140484" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/140483" target="_blank">📅 23:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1qaZneA-HFhFicbOONDyeq8EIdckkvjwGNywaISv9dSOuYSIHDGS0AqoNc0fhj-ppFOO5S1MdKOeNcIZaaNhJ6FWy8UtOsHYWQXHQ8HeXRC6N-AfGmUdd1whW72fLJrsEB4yxTNQ4FaIRSHfphf0yrBd2lxWzjmF-4axYAEe-itrzpiZ09udHUEzOyqO1uAuottYxtdyJ9Br9vCwXzA6Nm4r1CTzGbRXlHo97eTCAdRBxo2zT0WvHETqUrgNXvLIG1b3eixz7-yaq2_aylfFhLzCaR2aSHvBEy7jcvH6TV0Q3LR7qbLmSkaHULnEejY2KATBIWWpPpOVe2gSrh1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خرازی: باید ابتدا اروپا رو فتح کنیم بعد از راه دریا به آمریکا بریم و اونجا رو اسلامی کنیم
🔴
همزمان میتوتیم به شرق آسیا هم لشکرکشی کنیم
🔴
یک لشکر هم میتونیم به استرالیا روانه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/140482" target="_blank">📅 23:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین در صربستان با وویچ، رئیس‌جمهور صربستان، دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/140481" target="_blank">📅 23:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca22d0550c.mp4?token=duFwZupb_AZsiagLGRIz1oJXSNhKJSM6BHfex0QGw6mIRsmdVwXE1yvd2ED1vJNpdXNF22SgLjIJDbZbITdP9ZtZzQiy7Gwuakz4_-lCTpAnjx40kaTILuINXpfko4mNHA1GeGEHFQU5RnLgtj6IDdgYsX0RS6ivXWc-SkEVSDHJre_h87SaC_li8KaGUlmKdNxb8bfStaZWOTXPzopkzpwTGZHiwIrKwlKH0zxovfk0_SMHrvApIXhuZkKtme33V3wo0ITQIxh2mOxcgMbHPkNOCFk9_m-LEs52plWlo7M-sIgOrf6ECG62LiKohjKHtSfDkIfBnoeJrVLLs250iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما این‌قدر آدم داریم که من کل روز اینجا می‌مانم. اگر می‌توانید سریع بروید، ممنون می‌شوم چون ما یک جنگ برای پیگیری داریم، باشه؟ این بهانه من برای کمی زودتر از اینجا خارج شدن است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/140480" target="_blank">📅 23:11 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
