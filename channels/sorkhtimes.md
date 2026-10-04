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
<img src="https://cdn4.telesco.pe/file/AfMrgG01xJH-MwcF9HJdRs_4JsjKxzD-mmumJ8ecONi6I6JaVJQrOnT-B4m3H2upesWEwqCUMqOv8cSEXvIuS7uzuCxSG7LWIWrArohJuWh9iIcciLD88EoUFB1pWwlBAaKSXuGze-4mDn9N6SzHh3ZxTFpXSe0KLx-7kcwHlv5rvu5TWja07ZR9Xdx9uULkMyfK93NLMcU4E6DzsDDdinBtwA-5oeFPKKB-UDCSPpxsTB2IC6rgX15Ikfe9OLYdcsz4sZSiqlAEbVspH9d7PiuaF8qgIWCxJ5FxLtc3vX6fXzn90Xb5TXO_KZdKWqTdy7Ct7Huo6maFZBYaEfzNAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/140917" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/140916" target="_blank">📅 15:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQRzQSc9BOZL-cpQABWqYsGp0SvbA_Qr2ko2ygVG5UcYE8qk2PBkJsbps6SyQ05B36GW7tILg6Tc_M_SNAVeAeduJEFe3yU4XWfAytQb_DI8muLEryqFSLmMXdXTzelqvFiQSZebK1bLyePn4S3GHTNf5yapzmpCwmUKY2yEmmFMmdMMgeIxSkxw9PCzul9ljiCglmylyceZNHFMXHraYRY0KEBJp_peIZ7KmJXqKpzoWxdxVy8jhiLLK65csoT8YWO0GlVneB17swDcPWgfiuB-UuFCmUv_2QeYQ_iC6dvXOGO0DikS0Sw6SvidSE9HWRfuqZznvClSPes-ZXn2jMH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b62ce8f42.mp4?token=NQPrCC5It4CnvgO6WabqMuq0INZCh0_sPqRW-Keh2AW4z3GE8nsFtykbdwx7WD9xp7CmFETWgWyJUN1RULP0LniloSPB7Yl1zKCA8HY6Wkd05VZojx2Oi1cxszEG3yn_d6ETIYjm8prwvNEulkAfwXpFTYjY26x6BxwkUukmuI3L5Tf08YB4mnct09Qj9P9Wnsn1Y2jqlH8EjCZI0XfdNLBVkD0bH8EgLRdlIR21k1ER2pl5_5LuA5UoVKBrqGlspXsikM94-sNUc3I3S2fFfTptCf7GnYyugAHaj2xpNUHhRIxX1ppOMuAQJlxevZphEnK5L4SGUJJDNN9IeljnQRzQSc9BOZL-cpQABWqYsGp0SvbA_Qr2ko2ygVG5UcYE8qk2PBkJsbps6SyQ05B36GW7tILg6Tc_M_SNAVeAeduJEFe3yU4XWfAytQb_DI8muLEryqFSLmMXdXTzelqvFiQSZebK1bLyePn4S3GHTNf5yapzmpCwmUKY2yEmmFMmdMMgeIxSkxw9PCzul9ljiCglmylyceZNHFMXHraYRY0KEBJp_peIZ7KmJXqKpzoWxdxVy8jhiLLK65csoT8YWO0GlVneB17swDcPWgfiuB-UuFCmUv_2QeYQ_iC6dvXOGO0DikS0Sw6SvidSE9HWRfuqZznvClSPes-ZXn2jMH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تاج: سهمیه ما برای سال آینده 3+1 است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/140915" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇵🇹
نشریه رکورد پرتغال : محمدجواد حسین نژاد در آستانه انتقال به ریو آوه قرار دارد
💵
مبلغ انتقال : 1/4 میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/SorkhTimes/140914" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
تاج: آزادی باید مسقف بشه؛ شرط AFC!
❌
❌
حالا سؤال اینه؛ سقف‌زدن آزادی چند سال زمان می‌بره؟ ۲، ۳ یا ۴ سال؟ وعده آذرماه هم که ظاهراً منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/140913" target="_blank">📅 13:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/140912" target="_blank">📅 13:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=LZ1MglzJA2GVqn76xjA4yw8ZuKXY2lIRFT5VtyNhpHXKhQvIcSjS53ZSCulcNMDpe53r40E5nFpjrPoDofbIn4V5tGZRTLGFRN3siwat54fWbZYrZzP0r_2PgXomgT8ng8dVfXuABTpYPqsZffmRUu-E2upPVjmZt9VdeAua1eayPf__WnKhM076s1jJw_KZ0_o90DXYF4rRdinvQI5TxcOcdcv3oTCBUBiWXvGcK4q16S4eOPNmz0WpT_sReBsDVf_uAi7SRTc8LYSjlm3E-rn3WiI7_hrF00Ok9V0XByX2GAu_RUdsaRSJ6hZf6zmciBVchVxujXiXQMk6s52vcGd6kHhqpzrDLcVddaM5kggvwUeb3L0dC5JW_25sT1itXidvGGzfN4oxugNFMbWIeMJYyuHOWICAFzGqTwg6qmKqUFK_Ws4vT5UTR2nwks-5UnvrvczVXcv_7kthBFDpiesv50SjeDxKYRrWUx60ASRpWNlX9aPBnJHZfrECnY9RdVtpPwYHTeaviKPkFghJhnpE5VYrJ2WUozQ03yHAPPqaL3WjVgs9ielxL9YTzM3x6ksJsMmUf4Iw8jT9Oi0nJoeXDckP_JZ0t0HPHppogVFHoCEjWi7GOAQXVLOxUDbjddyh-7t4MW8fx25DQKBskocKjG_eJy_56jdF5J4sfEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db93cfbe3.mp4?token=LZ1MglzJA2GVqn76xjA4yw8ZuKXY2lIRFT5VtyNhpHXKhQvIcSjS53ZSCulcNMDpe53r40E5nFpjrPoDofbIn4V5tGZRTLGFRN3siwat54fWbZYrZzP0r_2PgXomgT8ng8dVfXuABTpYPqsZffmRUu-E2upPVjmZt9VdeAua1eayPf__WnKhM076s1jJw_KZ0_o90DXYF4rRdinvQI5TxcOcdcv3oTCBUBiWXvGcK4q16S4eOPNmz0WpT_sReBsDVf_uAi7SRTc8LYSjlm3E-rn3WiI7_hrF00Ok9V0XByX2GAu_RUdsaRSJ6hZf6zmciBVchVxujXiXQMk6s52vcGd6kHhqpzrDLcVddaM5kggvwUeb3L0dC5JW_25sT1itXidvGGzfN4oxugNFMbWIeMJYyuHOWICAFzGqTwg6qmKqUFK_Ws4vT5UTR2nwks-5UnvrvczVXcv_7kthBFDpiesv50SjeDxKYRrWUx60ASRpWNlX9aPBnJHZfrECnY9RdVtpPwYHTeaviKPkFghJhnpE5VYrJ2WUozQ03yHAPPqaL3WjVgs9ielxL9YTzM3x6ksJsMmUf4Iw8jT9Oi0nJoeXDckP_JZ0t0HPHppogVFHoCEjWi7GOAQXVLOxUDbjddyh-7t4MW8fx25DQKBskocKjG_eJy_56jdF5J4sfEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهقانی ناظر AFC در امور استانداردسازی استادیوم‌ها
✅
باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/140911" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiCGERakCuCRAKcJ70vQizUNpuufCXQiBzD1XyPjixhKauzWgzfTpBIWovW65BEwcuMG29gC22oE1z6v-v6BPbuxaXz3YASb6FnR31DzvDETGYGNR7UXViec1jGcdwKV2lDcO2mnAJlzBFU_2DlHscm1LgpM22XTuqRDy-8Ud9mjU6i-rgCPrdqwGalac2ve9XgG6dkFJQeNnYKbXOeYClLSFbRwRWA9SabS3ut24NNWkKWvC1yQrdDR7P4hADMASBROjz5vBqrk5Id4GtwTSB-AXmSVP677-36921jxZb7LLNs12bHuIBXIlYx7lRgxJVHb02aS8lLwsH2FFY_ECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد سلسائو با وایکینگ‌ها؛ پرتغال در برابر نروژ، یک شب پر از هیجان!
🔥
⚡️
[
پرتغال
🇵🇹
🆚
🇳🇴
نروژ
]
⚽️
پرتغال با تکیه بر مالکیت توپ و کیفیت بالای خط حمله، معمولاً مقابل تیم‌های فیزیکی هم موقعیت‌های زیادی خلق می‌کند. نروژ اما با قدرت درگیری، انتقال سریع و تهدید دائمی در یک‌سوم هجومی می‌تواند بازی را برای سلسائو سخت کند. سناریوی محتمل، بازی نزدیک در نیمه اول و افزایش موقعیت‌ها در ادامه است؛ گل در هر دو نیمه سناریوی جذابی به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SorkhTimes/140910" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
تارتار هنوز به یاسین سلمانی امیدواره
🔻
مهدی تارتار این روزها تمرینات ویژه‌ای برای یاسین سلمانی در نظر گرفته و قصد دارد این بازیکن را دوباره به روزهای خوبش برگرداند
🔻
گفته می‌شود تارتار به اطرافیانش گفته اگر تا پایان نیم‌فصل اول نتواند سلمانی را به شرایط…</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/140909" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw1YQ3GLUbtB-52Sya4T5LTgJaZMK-_WICJ6tjXBmG3sLh1hAPJAu5L57RUbX1fmufvccindwXCuWBEosGG8Hq2IV0QTCv7ohHKvHWae9tq8YIrfpfgHRsM1tBWM3-u8oMk0bxxnOdp38pKZSbnXU0HCPn6IWKaB5uFwqPa87wTRwhO_H4lm71qwwb30DbHKRyCQbOCNdj322jVUOH4xeiQ6L6uS8m0BoJv_7KVf4ibaq9WDdkK8wezCuWM24ECj_NT-2zvfq83dSGiwZ3LnkYw_VuqxuNQk46X3UG0EadnqJY68PbmTb9pZqiEjaa51GS_WBzgp52DuYcIitI7DcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
باشگاه پرسپولیس طی روزهای اخیر درگیر تمدید قرارداد سه بازیکن مهم خود یعنی نیازمند، اورونوف و کنعانی‌زادگان است که تاکنون موفق به توافق با دو نفر از آنها شده است که اون نفر باقی مانده اورونوفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/140908" target="_blank">📅 13:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
❌
❌
❌
❌
ادعای برگ ریزون یه خبرنگار ورزشی: یه زن اعتراف کرده که باهمخوابی باچند داور برخی اتفاقات فوتبال ایران را باآنها هماهنگ کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/140907" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
حمید ابراهیمی خبرنگار ورزش سه: یه معاوضه دیگه بین پرسپولیس و گل گهر شکل گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140906" target="_blank">📅 10:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHtyK1waXEcnXr48FZ0qawj_1OpH8gMiLGCEzBFIzLcR-qoF0XfKAZeh-NC6W5GNEW7fXhMqNU25vVLSulucCxfFK4pab7dl1-dwOkqguK87fiqTMKkuyAGF1rRNOFSE6SYYKL7LR3wfSz4HyA8Qn9fPzrBrdnbBnRKC6gflvoabF0TcQOzxjC5WNf2ndFv-WIZxdYT8Olod_ah2h-76rD6-Dh3KDTZXB64kVyMkSXQ0O9PgD3yXSx0AFDrlunH9iFfYNqdx73-IhTeVRJ_WC0vIvhPpngjwovIJzUwqrS-VxNxze9qnzagJWca0G5sF_P-qgjbi3E5WIi8LUkQR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
بازی دوستانه تیم ملی که قرار بود در مقابل تیم‌های گینه استوایی یا گینه بیسائو برگزار شود به دلیل محدودیت پروازی و غیبت بازیکنان حریف لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140905" target="_blank">📅 10:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره  و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140904" target="_blank">📅 10:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAzhteIX_E-5ljSn_cmQnUmaBcwFy-fpaEgZHE_lQBwncSgleDIsUHKUYyYaIfYhdRVNETAESwbj5E2BLNWHyAzBh0XXVnT0tGtpaaGTHO0wd4dLRk7wuEXgl4ZGVuzVFqZV_mI5GVisouAKzuux247KPTGdPCAhITjI11kk22YyUkTtAWki0DgEoulVMFhDZKVpIAYhkms91vZ1cg_-oJ7wkYrWziOBhAdHcyc5SxMstLtkHz6Y0Syljtvrk30ZTJ6rcgGLOFqN6iLtqU5TlD7myG3o5ehoYh3x0GzCbbgVGFR7Atr0Gf5QNG-Usml7GJRQGqZ0VCiLm5IblVmiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
پرسپولیس امروز استراحت داره
و از دوشنبه تمریناتش شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140903" target="_blank">📅 09:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
بهترین لحظات پرسپولیس در لیگ قهرمانان آسیا در سال های اخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/140902" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvk8JSV6tGd6Qq6XYKDch5PQDpnQpPc-pFXR9g5TvLvJL8rv2mYGrukvnpmAK-ku9p1faoOqUlMj9pw-cqQCriQQlaw9eZYEhJgR67ubXwxEXtpZWetpSJYaje6bK-4hIJbhQe8Tbb2KYmTrHIiix8wijTs1ZfvVSUcvDDuPBL11Jxg2SSOxVN67rTMXhzuwe-BtpijOVrnfUJDLJ5Hcbwo21gcSmFgTRId8sPWSPDOS7zESooseDy0Pm-8JCotbOePargWKZ_8F6l8mxi3072SxN6y17YLHkrT6oCU1fIF03rTFvKWwPzd9KhKaGdENWrGyONowfqrQIpT4iFIBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140901" target="_blank">📅 09:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">■ دیگه دنبال لینک سایت برای ورود نگرد!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140900" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140899" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
از این پس امیرحسین محمودی در پست پشت مهاجم بازی خواهد کرد/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140898" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
دیدار تیم‌های زنان پرسپولیس و استقلال در ورزشگاه کاظمی با استفاده از سیستم VAR برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140897" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140896">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FizFpYGUNdptJcQX8GwtwkbhyX1-073pZYQIAFBiKIVHXPR087oDQPpCNScS73PAVG2PAQ1x7sTIQUdx1XZ1a-M_hQDSI1EFQy9Qhu9TR1ibySHj5x9fux2NW8iuLH4KegzzUd0er_7LvOLTyAkEKWMJVK33FRsaRd5ZwUd-mf8gJwbNe5hup_IiQUxHd7mvCTmxpDhMvr1x2jWokHMg9Kgqv0tW-WzNdtfBhfuF_jsh4R0g9jw-uzPt17iI8oqAxtzRdZ-2mMEmAfs7_0cZlvRxLHUgeqIC7SgKjPkmRtARpXYnWmQL68Ns6sg8xYlAHd1rKFNKDpk9aYSLxIwdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⁉️
‼️
یحیی گل محمدی به دلیل اینکه باشگاه دهوک یکماه در پرداخت دستمزد خودش و بازیکنانش تاخیر داشته اعتصاب کرده و تمرینات تیم شو تعطیل کرده:))))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140896" target="_blank">📅 23:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140895">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
✅
احمد دنیا مالی وزیر ورزش:
✅
✅
فدراسیون های ناموفق رو حتی شده تعلیق کنم میکنم. این همه هزینه کردن که هیچ افتخاری کسب نکنن؟
✅
✅
گفته می شود حکم اخراج قلعه نویی توسط وزیر ورزش صادر شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140895" target="_blank">📅 22:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140894">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏆
🏆
اشک شوق قهرمانی و معافیت از سربازی
❌
❌
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
❌
❌
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140894" target="_blank">📅 22:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140893">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
گفته میشه که یحیی گل محمدی هم یکی از گزینه های جایگزینی امیر قلعه نویی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140893" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140892">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsznJx3Q_rYaj2rVrI46q83EjDX3zkHJxutNEQMb_3QuctuT9Myp0WQtedOSNzvlhhaD72PUOvDG_grOtvxzwKLW-mKnc8TDPDJZM_5XlK7zOAWwTnpaf5W-Hto_MN4FQqTE2QulX5IwypsMimPPgczpBaRHpdYQnpfgrWgcHmZwxJHfj3A_minXwsHKq_cL_jUPjwU6nXsDMJV7X2L0G3vtZaMdeJh-5zwU2k3l3c5tLIERRt_WqjMTkXRb6voG0RFByFzDCx9RFeJqY0IZJ58IAlRHF87g-NedMiqPo_Qw_10Lkos5EypFY4Nts586Xs464-BTf4_FrE5byi2lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
محمدرضا مجیدی، مدیر ورزشگاه تختی: چمن طبیعی برای ورزشگاه تختی کاشته می‌‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140892" target="_blank">📅 22:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140891">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iplBdUIVHx3DRKMOxnhuPUxkkE3rRId38a2qZy2TqzCWQFPP98CoXXCZ17sWIv_wyomoGnmQZOYhFB2tOOs3PODib3nXRcr1nXI8xuojZkwpPDkKn52MSGoV-HBhLObGif1nMkOkwC7rOgB92TWGvXVnw2LcnhZCYZo0sjspuW6eajLWOeHcQgYGq8OM7NrNjXj1laxQv6meVh7OjiiU8F-JK410hNYDWAvSd4A9K0-KPidIp0KVXnjireBLzivfG0LTUEmnDhX9s0fALDprYTzAXgV8nFLdGF-tdZuU3XBMXjfgsJ6RUuiNi0mSzsHSJ6nSqqGMAE05DLdBoUHMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک قدم تا سومین برد؛ لاروخا آماده‌ی شکار!
[
اسپانیا
🇪🇸
🆚
🇨🇿
جمهوری‌چک
]
⚽️
اسپانیا با ۶ امتیاز و ۷ گل در دو بازی، شروعی کاملاً هجومی داشته؛ چک اما فقط یک گل زده و هر دو دیدار را واگذار کرده است. میانگین مالکیت اسپانیا حدود ۶۳٪ است و در ۲۰ بازی اخیرش به‌طور میانگین ۲.۶ گل زده؛ در مقابل میانگین ۱.۶ گل برای چک ثبت شده. اسپانیا در دو بازی اخیر خود پیروز بوده و لامین یامال در هر دو مسابقه گل زده است. با توجه به حجم موقعیت‌سازی و اختلاف آماری دو تیم، سناریوی بازی می‌تواند برتری اسپانیا همراه با حداقل ۲ گل باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140891" target="_blank">📅 21:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140890">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140890" target="_blank">📅 21:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140889">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
۲ گزینه پرسپولیس برای لیگ دو
✅
✅
پرسپولیس بعد از ناکامی در راه‌اندازی تیم «ب»، حالا دنبال خرید امتیاز یک تیم لیگ دوییه. پادیاب خلخال یا شایان دیزل شیراز در صورت توافق، امتیاز تیم به تهران منتقل میشه و زیر نظر پرسپولیس فعالیت می‌کنه.
✅
فارس
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140889" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140888">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB8uIJF-n94VgC8MyB_xswg4yKwnfB5_OeyfY-4TXHn89Ngnjeq_waR6nAbaKKnNcO06lsQ5ro34aXvleShUrJOSpkgUZEUFsNChXdnWEVxFvjEkEmNZyiZgThJ9jiGEugLFkULCM640ww6JWIqtp_3zJVtCNyDlRJ0GgIiG8WxggJfCE9_BCnvPR65xgEAgkPcOn1Ds3Zo--97GaRSEdR8UraF7Nkt0CMoRlFCuCWAbXNWEjoPeXo2QGdknRGNfhcqVYXkA1gdkh1T1OeEIie0ew-YtXfFyNkQV-mmzxxZDaAIUu2dS8u2yF9LhVaY5vxaWsKqPtKfUYw944fcLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
علی علیپور بعد از سپری کردن دوران مصدومیت به تمرینات گروهی پرسپولیس بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140888" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140887">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✖️
✖️
محمودی و صادقی کماکان از آماده ترین بازیکنان تمرینات پرسپولیس هستند
✅
✅
هر دو به همراه زارع در دفاع از بهترین های بازی دیروز مقابل گل گهر بودند.
✅
✅
باتوجه به مصدومیت ها به احتمال زیاد این دو بازیکن در بازی های آتی برای سرخپوشان به میدان خواهند رفت.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140887" target="_blank">📅 20:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140886">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140886" target="_blank">📅 18:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140885">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⭕️
⭕️
بخاطر کمبود گاز ، از اول آبان به مدیران ابلاغ کردن کلاس ها و مدارس غیر حضوری و مجازیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140885" target="_blank">📅 18:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140884">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140884" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140883">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✖️
✖️
شنیده میشود که رای کمیته استیناف نیز در پرونده آسانی تایید رای کمیته انضباطی بوده و پرسپولیس موفق به محکوم شدن این بازیکن نبوده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ﻿</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140883" target="_blank">📅 18:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140882">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140882" target="_blank">📅 18:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140881">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140881" target="_blank">📅 18:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMOTAoySO7xJ3Ii9ja1UyIv5znp64TbA1XzrNvKa_N9-eAspeYzHkMtrM9-SHmuPO7wqNdNJDjFPUolOEgaYTPeW6rt8b02cZN9QyFJvVhBNKO3XLxfxSkg-MEK6860lj20C-mSwIiwhmrvqcTviMvy6IBQNJZ3tv9nE9qZ0n9GhmarLnQuWKRoDOBTecwbqrbq7-Kd8hbXozq9lqYdwHHiHfOfpo3i3onKJ6Q7reSQgkGBRgrDCFRO9nEZ0_KSW3y-SA_TbvCZMULWI2tEs1AFdjU7ha8FLkWzokYVad5YMsjuTpwzScnWViuV5uYISXEn7zNJ5iT5LdmbGYG5oxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کاروان ایران با 19 طلا، 18 نقره و 15 برنز و کسب مقام‌ششم مسابقات آسیایی ناگویا رو تموم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140880" target="_blank">📅 16:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140879" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140878" target="_blank">📅 16:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeWcuQ2jRh2O4Cf_3tm8BlAipQ033ggO_gkGVbo1p5uiBK9IZOs2p5HR9A72toQHl7VLSEMrg3qe_UBfhFTDUz-FL9S1xAxmJt2dLoI6L0yBTx8n0tfIQbmIR7JZzd-nsQZjHRx1GwNakuf_oZ55P9_FApOiZTjkVGOUXCnbpus4SQgw6M6N4Zt0uUhMcKBfDMQfg3eB5Nq2nNlZ_hmUZChBSMqTBeZUCEr_Wzhu8j_H9EHSXhMuvIrBcepUS2Y-QUx0xkv0OuqIk4iqeIgmKvc-mmT2tjKQa-r1meSOj7br7HQpdQNz0tBzDiHzpKFyW5P3_c0wZJAQHcMk6qGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
SPAIN -
❤️
CZECHIA
⏰
Tonight 22:15
🏟
Municipal Carlos Tartiere
🇪🇺
اسپانیا با ۹ برد متوالی و پیروزی ۴-۱ مقابل کرواسی وارد این دیدار شده؛ یامال هم با دبل اخیرش همچنان مهم‌ترین تهدید خط حمله است. چک بعد از شکست ۲-۰ برابر انگلیس و اخراج پاول شولتس، از نظر نتیجه و اعتمادبه‌نفس شرایط متفاوتی دارد و مقابل مالکیت و پرس اسپانیا احتمالاً عقب‌تر بازی می‌کند. احتمال می‌رود اسپانیا کنترل و فشار تدریجی روی دفاع چک بگذارد؛ اگر گل اول زود برسد، بازی می‌تواند به سمت برد با اختلاف و کلین‌شیت اسپانیا برود.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140877" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DDZK1lZZpZHw55zYRxwj4LJ2nF5cqr3V4Swiz6NpGp_ytycB2Pb7gm4XshyJdhZCQkYNtjikhQSZgcYWDrlBfotomqxcNahA_D7PBlzOqJLSD2tRxcKO0rNJlHikNwRfOImxuGuIOrYJ7omGy0Td9Gy8iALySOOakdGvShDcVKbRHPPT4nZvCCWuC1Dguaxa3DtHrvJXG8uwBmU9RS4ED6RK6lEKGY5_opsjupEQszwIcuF4-MfvDzNRzZARv4_e2zhDmabYJgQPUpCQiDZT-k1jB2lRLxh9yIxUIjEqAV-i7S-2p1jmMQsVYMJkAHUznpAPEv5OxxEV1JQZZ4-8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
تیم ملی والیبال ایران با غلبه بر تیم ملی ژاپن مدال طلای بازی‌های آسیایی ناگویا رو به دست آورد
ایران ۳ - ۱ ژاپن
🇮🇷
۲۸ | ۱۹ | ۲۵| ۲۶
🇯🇵
۲۶ | ۲۵| ۲۱| ۲۴
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140876" target="_blank">📅 15:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
خلاصه بازی پرسپولیس و گل گهر سیرجان
✅
پ.ن چه کاشته ای زد یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140875" target="_blank">📅 15:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
والیبالیست‌های ایران به فینال ناگویا رسیدند
🏐
تیم ملی والیبال ایران در نیمه‌نهایی بازی‌های آسیایی ناگویا با نتیجه 3-0 پاکستان را شکست داد و فینالیست شد.
🇮🇷
25 | 25 | 25
🇵🇰
13 | 15 | 11  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140874" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
غیبت عالیشاه برابر پرسپولیس/ ستاره سابق سرخ‌ها کجا بود؟
❌
امید عالیشاه در دیدار دوستانه گل‌گهر و پرسپولیس نه در ترکیب تیمش قرار گرفت و نه روی نیمکت نشست.
❌
❌
گویا عالیشاه در ورزشگاه حضور داشته و به دلیل مصدومیت جزئی در رختکن در حال گرفتن ماساژ بوده است. این…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140873" target="_blank">📅 14:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
عالیشاه امروز اصلا نزدیک نیمکت‌ تیم نشده! و هیچ سلام و احوال پرسی با هیچکدام از بازیکنان و کادرفنی پرسپولیس نداشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140872" target="_blank">📅 13:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140871" target="_blank">📅 13:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140870" target="_blank">📅 13:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqY6aCcJhFIbm9mzvY5M_qP6pfoRyuBaD0WRNCYbZE0HITsOiNezo7UKrqiHMfudzI6zXQgaZouPl30gGenOQlZp1m2seFAMHNQzkN7k5zp76bNLP3M0YnJ-PFYLOl21rCvgbdIPbtIL-l4j5panF5V8Ex862onoxkrZGE0tL24pSNngQ6fkPKCy63DaI7mObyXxr9Xe2XioPik6qqaATEr8UAKtIYvPm4BvE1QBLb30K-3iBjoa0bWqUO7DKXxnQbLK4Nr_X5USe_KpF-fNthhInBG2xOb-cvJsYBlFTMW32UfQV9tIMuFGtbeguCzX32eoKUjVnjG1UiiRDmRwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
زمان بازگشت قلی‌زاده به میادین
◽️
بر اساس پیش‌بینی کادر پزشکی باشگاه لخ پوزنان، قلی‌زاده می‌تواند پیش از پایان سال ۲۰۲۶ و در اواسط آذرماه دوباره به میادین برگردد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140869" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBKR9fS9gUWT6rZuqNsDZ6ma3SX-o1vUaDHElsHPToI93MFokWayMcZCQ8i88-fb1H2l6GRSF9T-Q_sQJAB60xfQRHltX92l8hKCo85xxtMIvZwLFEHQdGZrRpYYu4IoM98dMaN31OD6-IWp5zsqkhaNzyirQ8dnktU3IDKfZqtN9ihpMHkfw7ftjV8TzTxtBQ0sk4iwcPrO7yiZJSOl15o5obq_q_BM1TU1LVLHDBRijDB_pNjyS7jxuZCATUlhTQO-x5xfLjDqViR2vGqCnN_whyF2IE-7CFHuEdkn7et0VaeX-Qv4AQ7chhEnNH13j2CsewnH2nN2ucS6I0EoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از ورزش سه
🚨
زوج خط حمله پرسپولیس مقابل صنعت نفت آبادان رو ایگور سرگیف و پوریا شهر آبادی تشکیل خواهند داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140868" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⚪️
⚪️
محمدحسین صادقی امروز علاوه بر گلی که زد، عملکرد درخشانی در ترکیب پرسپولیس داشت و ممکن است در بازی‌های بعدی لیگ به او بازی بیشتری برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140867" target="_blank">📅 09:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140866" target="_blank">📅 09:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
✅
گرا: از پرسپولیس نمی‌روم؛ از زندگی در تهران راضی‌ام
‼️
✅
✅
گرا در در گفت‌وگو با «Nemzeti Sport» درباره مصدومیتش گفت پس از مشکل کف پا و انجام MRI و تصویربرداری، شرایطش بهتر شده است. او درباره شایعه جدایی از پرسپولیس هم تأکید کرد یک سال دیگر قرارداد دارد و…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140865" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqBxu84Vqt9B7WUE2OVIWvtVrwrGQUDLrAZDWNSDLO7l2cje3Xr3I31aDFRmrpA0CRv_oetdAO1DWh7IgUXT47ueFJmGY7M9TVolEtdzF1imW-Te9z9XmO_BSCfhcgBpc9CeQO60iBKSzokXYIDEEMg8gTEklmgu57OL58WdPNZCfFSI7Jvabub7pSClvoyQpxRXkYQHcf7_XwiNoJP0AAll1xp14BZeSStzf5h4eCV5eD_cZOIpCTUuNN_ZUZ_ASHh8z-wbXcS5FRessN6PfWrjIzKoCRmjTHvXB8Ld7PSO2WgpYTK4UljFQUKTJS44cwBW2p6_E-k1jHXef1VylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140864" target="_blank">📅 09:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anzWoyvnSLH_L7VY9kc-vMARBpc2KE99z_fHnoxd7FFdiNF0OALsQPNj0c-iVt4ymKe8TOVME0_mMh22YbG98HsX_zgAapsy6hUQXTmPx7VKReN2uOcUYMwcgY49gBNWmU6ZOpnXceyq5oHwmqEKkysx6BASNzb8NBkZYM1bLxpF0VRVgf7wzv4Ik9rd1BDofEVZ-Zz5Rmw_YhzVc2BCOFsvPeKJWt6slwj1s72bJr8jA50CFqEx9NJvaOaiNtYbLO8B_9xppVs3i0qjg0PdNNX-3-pv7VMtp25yXyJCxtUO-lu9-KczIicrGOFUtkxsR28jW2xeJFDQnAmoeoFnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
CROATIA -
❤️
ENGLAND
⏰
Saturday 19:30
🏟
Stadion HNK Rijeka
🇪🇺
کرواسی برای کنترل بازی روی مالکیت و گردش توپ در میانه زمین حساب می‌کند، اما انگلیس با سرعت بالای انتقال و کیفیت نفرات هجومی می‌تواند در ضدحملات خطرناک باشد. تجربه و کنترل کرواسی در کنار قدرت هجومی انگلیس، این مسابقه را به یک نبرد نزدیک تبدیل می‌کند؛ احتمال موقعیت‌سازی برای هر دو تیم بالاست و گلزنی دو طرف سناریوی جذابی به نظر می‌رسد.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140863" target="_blank">📅 01:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140862" target="_blank">📅 01:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
غندی پور، مهاجم ایرانی شباب الاهلی امارات، به دلیل مخالفت باشگاهش نتوانست به اردوی تیم فوتبال امید در ژاپن ملحق شود. طبق قانون با آغاز پنجره فیفادی از ۳۱ شهریور باشگاه‌ها موظف هستند بازیکنان خود را در اختیار تیم‌های ملی قرار دهند
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140861" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
پیشنهاد پاختاکور به مهاجم پرسپولیس؛ سرخ‌پوشان اجازه جدایی ندادند
✖️
✖️
بر اساس گزارش چمپیونات ازبکستان، باشگاه پاختاکور در نقل‌وانتقالات تابستانی مذاکراتی را برای جذب دوباره سرگیف انجام داده بود اما باشگاه پرسپولیس با جدایی این مهاجم مخالفت کرده است. …</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140860" target="_blank">📅 00:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
در نیمه نخست و در دقیقه ۳۹، شوت زمینی محکم محمد عمری را دروازه‌بان حریف دفع کرد که توپ برگشتی را محمدمهدی محبی به گل تبدیل کرد.
🔴
در نیمه دوم و در دقیقه ۶۶، حمله ترکیبی سرخپوشان با پاس شهرآبادی به محمدحسین صادقی رسید که او بعد از جا گذاشتن یک مدافع با…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140859" target="_blank">📅 00:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✖️
✖️
بی اعتنایی عالیشاه به تارتار و حدادی
🔴
بر خلاف سیامک نعمتی که قبل بازی تدارکاتی امروز پرسپولیس و گل گهر، به سمت مدیریت و کادر فنی پرسپولیس رفت، امید عالیشاه ترجیح داد، برای احوال پرسی جلو نرود.
🔴
از اینکه باشگاه او را در لیست خروج قرار داد همچنان ناراحت…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140858" target="_blank">📅 00:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
ورزش سه: امید عالیشاه به باشگاه اجازه نداد امروز مراسم بدرقه و تجلیل ازش برگزار کنن و تندیس باشگاه رو هم قبول نکرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140857" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140856" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140855" target="_blank">📅 23:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140854" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✖️
✖️
شماره ۷ رونالدو واگذار شد
🔹
پرتغالی ها خیلی زود جایگزین کریستیانو رونالدو را انتخاب کردند و رافائل لیائو شماره ۷ را برتن خواهد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140853" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140852" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140851" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
پایان بازی / 3 برد از 3 بازی بدون گل خورده
❌
پرسپولیس 1 _ 0 وارش نوشهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140850" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
✔️
خبرگزاری فارس:
🗣
شادمهر عقیلی مهر میاد ایران کنسرت میزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140849" target="_blank">📅 21:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140848" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=XvPJmt1fBvEAK5XXnL4-JlhvQg210Xl3SZV3lf-o_4vZMZUuqLRglXJbNg8LQGvTgPkyYxkBqdooIMZkCLdkBghsq6PzLmBHvB0y0kOuzciWkC5C-4FZ9C91s2CWcYVmIY-F2QqtZwnD7nlPI5T429A8ZrRFp1FRwHiWVYztiFdMcy2njhoe4tlfg3iAsnFunR71u-rtkBrAtYZsyktUF9v7yk1u85zXBFcFnrT_zp_Baj015J1P3S_QX-oeWO1Sgt995Fjr92W-xlIAT0TNT2HrD16_dEzrwx_rjKWx8j7MgC9FrdsrDQQBKMP15U7LSdERr2NTTmlYQZ_Gsw0A4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=XvPJmt1fBvEAK5XXnL4-JlhvQg210Xl3SZV3lf-o_4vZMZUuqLRglXJbNg8LQGvTgPkyYxkBqdooIMZkCLdkBghsq6PzLmBHvB0y0kOuzciWkC5C-4FZ9C91s2CWcYVmIY-F2QqtZwnD7nlPI5T429A8ZrRFp1FRwHiWVYztiFdMcy2njhoe4tlfg3iAsnFunR71u-rtkBrAtYZsyktUF9v7yk1u85zXBFcFnrT_zp_Baj015J1P3S_QX-oeWO1Sgt995Fjr92W-xlIAT0TNT2HrD16_dEzrwx_rjKWx8j7MgC9FrdsrDQQBKMP15U7LSdERr2NTTmlYQZ_Gsw0A4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140847" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
حاج صفی: بهانه نمی آورم اما چمن بازی با ازبکستان و روسیه خیلی بد بود. از مردم بابت پاس اشتباهی که مقابل ازبکستان دادم عذرخواهی می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140846" target="_blank">📅 21:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140845" target="_blank">📅 21:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140844" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0RpKR6Nifd9vaYp7USmtSsTIYVYVkUyawH9pi-w1yMya-PG9SviqR5qVvA5hE9oauLm3ZfDbRPgGwfkgjPkW4WD4Y5ECvWcIyQuGhbJ3GWfa3UKMB9CXmn6r7YJTZ0qEMM9tlFpijlyWaiFM7NXZotTlGZwolZWhBv3mQm1KmxajDYS4TWd_aZDmAAo7xyDkr1UJu9_3KpOL0akS5GsYOlacsfWYqNg2l-1YMy19bNPfHzSZgFoNgzD45CQUNEwQXogOsUknCqK-fosIX_CM3IUA20JKuXxu7dMo--zqQgTHCipoah4V0TdMDkbqVi9QMGKUcs0nCVcVbFkiONwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
FRANCE -
❤️
ITALY
⏰
Tonight 22:15
🏟
Stade de France
🇪🇺
فرانسه با دو برد ۱-۰ مقابل ترکیه و بلژیک، از نظر ساختار دفاعی و کنترل بازی شروع خوبی داشته؛ ایتالیا هم بعد از شکست برابر بلژیک با برد ۴-۱ مقابل ترکیه واکنش نشان داده است. غیبت امباپه از قدرت هجومی فرانسه کم می‌کند، اما حضور دمبله، دوئه و اولیسه همچنان تنوع زیادی در حمله ایجاد می‌کند.
با توجه به فرم اخیر دو تیم و میزبانی فرانسه، احتمال برد خروس‌ها با اختلاف نزدیک و گل پایین خیلی محتمل هست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140843" target="_blank">📅 20:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzTAwoTR_N0vM5-VgJBhFCluSx9_g_ELrq14e430kOgAQnFLAESoRsKs1nGoZ333kOFDu_rkzLczsaevptIYrLVzFnPZdVQ25GB_DfGxpbbR3CtkyQKgyenjb0cCC3q2Rj--ukRtm04v9DJXzR__J99tnAaAmYEpsMSwUpQ94RCwrgRLXlxiteyx75bhYa2V5to41F0G4Jm2WwXVaryHeTgQ8hxPWjZ-FCbpyuYaCzWcv7Xqq0BtWsRZrLG5VbLSeyJd95IMG1MLlbuJ8e60f7XtxctmtCZWu_NJNCTNwtZF2wdeT2EtSTNzLO-g2Wwz5unNn8XZ48onZ18UyTCr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140842" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVSBDpvjFUsJBOYLbJXk61U0uRUYLIS7sLehuUUkowXlkv7Lt3GTGPIoXoABTyFQVT70eXJeq0gc54PI_BUyoReJ2z7bpp6-clUh8DWtsLILt_VmDMk_1bZz0afMAwIksJoZv4Jn2oLcwhYqVx2babBdBUgaQgeJvLZJj95xvARH_355BqZ3Q3d-l4vDjEH4mDi9mh6iy7UdCofvsvrk31dkf4qKxGPSJmuRZrPrs8pavLfzpc-l8GSZj6jhqLKPP5XlPOt7Vstfuk0QGLrwIUDnmGHixtowECV-rXF8aqKg6J3VYhvVwWA472f0K4fdeax8tWRaEuO6adNVsGKATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
کاپیتان پرسپولیس در دیدار دوستانه امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140841" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول  پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140840" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140839" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.  #دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140838" target="_blank">📅 18:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-eMfufIAVbO9vJlB1fc2mv-usdTydQyZZGcUcIy9LY65olX7D9RAcbWzKamWmElJnEHpY6tw0qA4l1KbX-Sb4XIzqHrikRyUaHSMij6thubmtg69LP94gjPAHi9Ajx3DfgaxYZ8gYBoz8SR9-FTLNVok8QkaxLtJtVtcbuVKuMNmhvgnYfbnNPo-pz7t2g1BA0i4B7AB59NRGRu0xoUhp0S9KZuE1UukqhfkQmGitP63j4f-zd0iKsf8PqWHwTpHqQOoxP71JvM1aPmnJA-4LFm6i3rtIFcNUlZ2DFOaM8m2zTx4UBix0YyYwcAhGEwGXvGHMgmVOBNEvY_NdwWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.
#دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140837" target="_blank">📅 18:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwR8aA07c2YANj9GaZk_iURxLQFXBONXb41xI750qBjQYXJJSl96eEz2m6SC9DhF43kye6UpQQjbkvlbZi4KlUYTOUFjvRPqjByWhyiZygSekQ5ZB7joXGyuqna5vL7T4SrhQRzwtEMcNEwTZ8MyBzanhPYYLsaz8Zgh96EgJzZcNkD9AyY9W_eNKeAlye9cNYd86Xr1_T5qFA8-Wauifch2qae8fllaBH7exzIoLg03ULNzfJg-86Pnd8o2Azq-KK9ds6ZxVkhedu0gnJMov4r-tFyCxwRJD0lAsvZZvJPMsVkC5FzHrNRe-PJx9or4JzLSilivBFooi6AxiZjpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😀
سخنگوی فدراسیون: قلعه‌نویی از باختن بدش میاد به خاطر همین بعد باخت جلو ازبکستان اعتصاب غذایی کرد و چیزی نخورد
🗿
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140836" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f945d97990.mp4?token=EAll5vDxXgS8JP8HFweljQP8ViuAHFPBL3obWNET_IPM71VR14jXieAvMHj3x5lvXARTjljB6hqOPgIzprc0nmxzK_9wCcLuLHazdQBL9vFqe_RvDfmGtU1vUtwXpC5oJSSnCWjiMFG3VH1LSPQeemXCidNRsmOXev4jld5KPb-t0ZIslkXpPeX61ePKVpUHlYqVGyICAh9fWQsV_02NDw0FurL0Spd2KqxF5kbvObX4Syq-5REKjrkwJymBvI8VJtKxx-yI7IkEK_T4yEsRERnqJkP2N1jnSjDGb8v9BRgZ4Z72agA8tQKjiMpp7YbcCa-NwGRrRH0ENBFMgIRdmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f945d97990.mp4?token=EAll5vDxXgS8JP8HFweljQP8ViuAHFPBL3obWNET_IPM71VR14jXieAvMHj3x5lvXARTjljB6hqOPgIzprc0nmxzK_9wCcLuLHazdQBL9vFqe_RvDfmGtU1vUtwXpC5oJSSnCWjiMFG3VH1LSPQeemXCidNRsmOXev4jld5KPb-t0ZIslkXpPeX61ePKVpUHlYqVGyICAh9fWQsV_02NDw0FurL0Spd2KqxF5kbvObX4Syq-5REKjrkwJymBvI8VJtKxx-yI7IkEK_T4yEsRERnqJkP2N1jnSjDGb8v9BRgZ4Z72agA8tQKjiMpp7YbcCa-NwGRrRH0ENBFMgIRdmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول
پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140835" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHGthlW1qylDoOfIk7AeNrANfBs83oO6TGJwlenx9fMkr6uoyvKfEvOl37fly6dPz1oK4YD4THzDn_ZVitF72D0RU0L5gjsFkNK5dzkEVGcAC7F03VmQZvlkHNWPq9i5RI-sVWN0aXg6Yh5Z_eEkOaU5BANUI72yXS8fZGDrqFaI-KDFzgDjprPKA3ZSZyyvZtqaOvPQbBIeoqdfCtkB6cMRu5H682H3py4cH4grqHBtl3nuQ_mUsK4IILr-UPzDvA3OIQkIMHosfFkXqnzWLSN3zdWT2G4_D7HsviylCBH7O0U-xJMfqIciEZ3_otfEulfq-lZt1RBFHC3rPohuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پایان نیمه نخست دیدار تدارکاتی
✅
پرسپولیس یک ـ گل‌گهر صفر
✅
گل: محمدمهدی محبی (۳۹)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140834" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=ajffs0eXJkfdiD0W6uCCkKrLnXWOQKz9yjv5nJQCe_urKlYxj2zljImU0g_QN1QfmWAHZW4NPURhDGzGkMryu2T2txR3cvEPT-t6sC9XwLKCn4Z5Ac013MTvIfkNQEJy4HFa18-QHhr55ZrgRCPlnO6vPct16Fr4sGDMl0L_MU8eufzOc8vTjmkOHk4j8PgsDvqCFUXtvtoK2cp1-UwYYpoxq-CtzCe6wnYsmZH7GHos6X_1l8Qy6Ir-V9C7lXNLRv9a0BF6AF0Rh07KLfzzIaYgV2EbC1yrTPUK3kD5qsaXkeIv07C-qyQXPwWU-aHEyolajhQQFIubOSc45jgbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=ajffs0eXJkfdiD0W6uCCkKrLnXWOQKz9yjv5nJQCe_urKlYxj2zljImU0g_QN1QfmWAHZW4NPURhDGzGkMryu2T2txR3cvEPT-t6sC9XwLKCn4Z5Ac013MTvIfkNQEJy4HFa18-QHhr55ZrgRCPlnO6vPct16Fr4sGDMl0L_MU8eufzOc8vTjmkOHk4j8PgsDvqCFUXtvtoK2cp1-UwYYpoxq-CtzCe6wnYsmZH7GHos6X_1l8Qy6Ir-V9C7lXNLRv9a0BF6AF0Rh07KLfzzIaYgV2EbC1yrTPUK3kD5qsaXkeIv07C-qyQXPwWU-aHEyolajhQQFIubOSc45jgbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حاشیه‌های پیش از آغاز دیدار تدارکاتی پرسپولیس ـ گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140833" target="_blank">📅 16:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=EfUehWZxScRM67jEjjVUvZava4T194FrSkpZjBIC0bWz2azT_79NkaAUZ8IP4HOF5YoAbGiC7Ng-2deJUNS284lnIYaR7lCq3KM3ESz7-XijTo3m-hlIucnoKCHpvwb4oTdBmu8vwAO7sX2TgnZToRn4URKHnzbs5c0s5zeNQm11S_-qLf-knZ_Taoi6GRjJRs1nX-Kq7UG2v9ZB9MLH8Sge4Kzgkh1i93JK6dwU_I7CS1mpg9jMMU7xsxfw9GNSkO26cFvwyDdJoFmi8VwSuZ6chz1xZETbVIXTo8ZUEaURuVSOqOTIh45oITO-jvrQWTwvtjjLC-g3mwlSrboNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=EfUehWZxScRM67jEjjVUvZava4T194FrSkpZjBIC0bWz2azT_79NkaAUZ8IP4HOF5YoAbGiC7Ng-2deJUNS284lnIYaR7lCq3KM3ESz7-XijTo3m-hlIucnoKCHpvwb4oTdBmu8vwAO7sX2TgnZToRn4URKHnzbs5c0s5zeNQm11S_-qLf-knZ_Taoi6GRjJRs1nX-Kq7UG2v9ZB9MLH8Sge4Kzgkh1i93JK6dwU_I7CS1mpg9jMMU7xsxfw9GNSkO26cFvwyDdJoFmi8VwSuZ6chz1xZETbVIXTo8ZUEaURuVSOqOTIh45oITO-jvrQWTwvtjjLC-g3mwlSrboNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140832" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNx9qKa6-JcEx7uuo0Gupn6BEGxqFjsdRmGzqCsMSyI8dX8yHWUqOQGqXjOaAmn7zXjieBv87u_jsEn8B9wO35TU7opH45zPwJrrDd0Wm3UnCx8xr3tSGn9jap1kklPSbrj2rJjOwtsIYPG7PJFKvpvqxc2beW_a_i4ydf5Lgb4Rd2UXwfxJb-P7TPVBb5GUOI_QTVJhlwo9xJJ0DlOiyNzFi5Ol1RnjLH65tRLvpvnSqowVKQNrSi5zi4iIOwvK3q77vtxMQyCJFgwYWonVs1-NZ4C56szrnZJyZ4rHyGa4HsdH8z3tmo-uY_k6roz67b0z8IqDYdUhDsWKRTOYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است
.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140831" target="_blank">📅 15:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140830" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7gURkmePZrkBvt8zguVtGM3VSEVXPBkMJ8xFMgVv6rZI-rBeqI4que0022IxD73GgVQgkFEZfX76aHMG0HNthtjAq34vXj4IhVUr-Al2j50Nx4Bd5vBD5P-obOhXnthN8NaHqBuLJG2ft0DaxYkeRSz9LbSK4ImPn3eOInMNlKjt_A28KPtDrClRtXUVCKa6zSSLwnB5DDskzVYD_ororXTPl9CU504Yolsqk76v4gtvw0VQsWAqONM0-qAnTlk3rWrjc8PEdKbGySM9IGbCQyp3dDPcu-93a8OYTcf3UAbLwBJvairg2Ht9azZs-TM3rYa43J3fXa9SqZQFivdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول مدالی لحظه‌ای بازی‌های آسیایی ناگویا
✅
ایران با 15 طلا، 17 نقره و 13 برنز تا این لحظه در رده ششم ایستاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140829" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApM2LpDwDDgrlD3vKW8K5e1HLGEMPHpNc526cLkVS1963HibI-jyFDcANINr6NHSUZmNqUZFCyQLK1JTwVh-sYqOmZQ8v1zvPwFGAYxtmReG0JVy8Q5E_KlBcZQLz_u0N1UgjDM2M3ddoW_I7J_2Q4eZb4W2LCeldS8QhFttP5NKQosKd7yBL-PA2xlMtofPAredCWNh4Icg69NX0xYgbpsmfAdweKTK25YulmhRS8lhod1GMUTDahxyoN_OA-y7n1UWLklakJEI3JmUydqsPJyg1W7nfpmtCHDL9xYaA__Q-_k8J1Ncv0HMVvNZrH9cvnsR0UMT_sQuu9HHgcCJFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EApM2LpDwDDgrlD3vKW8K5e1HLGEMPHpNc526cLkVS1963HibI-jyFDcANINr6NHSUZmNqUZFCyQLK1JTwVh-sYqOmZQ8v1zvPwFGAYxtmReG0JVy8Q5E_KlBcZQLz_u0N1UgjDM2M3ddoW_I7J_2Q4eZb4W2LCeldS8QhFttP5NKQosKd7yBL-PA2xlMtofPAredCWNh4Icg69NX0xYgbpsmfAdweKTK25YulmhRS8lhod1GMUTDahxyoN_OA-y7n1UWLklakJEI3JmUydqsPJyg1W7nfpmtCHDL9xYaA__Q-_k8J1Ncv0HMVvNZrH9cvnsR0UMT_sQuu9HHgcCJFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
✔️
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140828" target="_blank">📅 14:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140827">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqRCguh5hP1kxwGJseHOjaYngTS5UovS5L1-1GdDXDcPLUxqCio42ZEzVY4e0PpbR5Xgu6doeGRifi3RDk2KJIzI7O4tjuipts55k8yGrGA5OhIuioaDGWMD-84I-UFlIwnFibOD-dOwBFMiRrs_73A0lB0QGLUNI9UP8T7ZAkWOt-x0lpqKDnhiQmxeABkp9SvvBTEUQERRD3NG7EIyJ4ORlW8CzVTCNJOR6SWPQ_e68tKNJFLf8f7_lv55ZhZ7snEACRoB3IgaH9o6cefESWy5aQYN5ZscktqZePF4b27qoGYr4gzbf8aa5DUI4S8Bk1Aj_dK1Gv3MfHBm30tzfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
چهره خندان و شاداب جلالی در تمرین روز گذشته
❤️
✅
ابوالفضل جلالی مشکلی برای همراهی سرخپوشان در دیدار با صنعت نفت ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140827" target="_blank">📅 14:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140826">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBqnyYC2d4xH7BhrRRoLL9PCXettq9XrMaB1Y1u-ZkGJ9j-yr-0oDPQApoCHSpSJHUCmx2C_OGONLqtbLmMvIlmz4ZXJoSOkMlGoL4R6oNzgFSTWHRfEAp8GCMutb2XmM8qm77xpFSfbONb7ZRHWvxb_5px6woIi_IO_0uDlRxkazqgW0EEcEMVaoYIrTyqII7l8mrIVRonunajsNnHWy9F_y-kmJLtXOD5-5JVlc1XIbM6c92bQK0H3DPP9xQZej9n0tAkxzMNmguKRfvNcS96IvpJIQ_mT0n1yW0tHgrKX_PkqYfi6TXaJWGxkWEvx3cHiusiCPHKygEfSx645Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد خروس‌ها و آتزوری؛ جایی برای عقب‌نشینی نیست!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇮🇹
ایتالیا
]
⚽️
فرانسه با وجود غیبت امباپه، از نظر عمق ترکیب و کیفیت هجومی دست بالاتری دارد؛ مخصوصاً با بازیکنانی مثل اولیسه و دوئه. ایتالیا بعد از برد پرگل مقابل ترکیه روحیه خوبی دارد و می‌تواند با بازی فشرده کار را برای فرانسه سخت کند. با توجه به فرم دو تیم، انتظار یک بازی نسبتاً نزدیک با موقعیت‌های محدود و احتمال گل در نیمه دوم منطقی است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140826" target="_blank">📅 14:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140825" target="_blank">📅 12:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
تیم والیبال ایران جلوی تیم دهه چندم اندونزی زانو زده و بازی به ست پنجم کشیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140824" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140823" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: منافع ملی؟
✔️
شکایت از آسانی را تا آخر پیگیری می‌کنیم!
✅
یکی‌از مدیران پرسپولیس مدعی شد هیچ توجهی به درخواست علی تاجرنیا ندارند و شکایت از یاسر آسانی را تا زمان رسیدن به نتیجه پیگیری خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140822" target="_blank">📅 11:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvSivYQt8KDglve2bbOO-zoryV-a5rGwRJ6wMCK7URzAOONYM5EkKcdkcYmCaEmkd98VQY7KqFQYWffPEhx2AijFiWj7l899b0YzlFuEAIFhqufQ8jxUHSy0qmE9XJ5jI5HsGZGvw9rFOyEE2vOQYtUL8bXBdIO98kShNzjSGUTjHl-e-dDQ5_zB3IuE04nVRxfV3TkhAWQOk-yOZlLgTfsHt5R0-SVrigIsIVm5O_1HnEey2xRpeFP9qvyWxNnsm8u-2XEYKngUFmtzMF0stxVY9xGJ1v8dVaXjCu5RuCXezsHAQuAwqJHLSQRiFW-4qvRtqbcK7g4p9b1hQZg59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
⚽️
👀
‼️
فکت عجیب ؛ مهدی طارمی در شش بازی اخیر خود در تیم ملی، نه گلی زده و نه پاس گلی ارسال کرده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140821" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140820" target="_blank">📅 09:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140819" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-TdeuxOkx_y9BTaOhNMIZON-ijPerB51IQbpX6Qd8CIyOWgE8Plb1nrfosbdl9BE13OUjEvSS_YC5UWkvSwz4rYHNuYQhLjbBFmPsBXNKz0pPUZ96sQwZDOZ10RbVezHxC9LUcy2Tjqhhdwtg0lMzH2apHK08X9Eg50QeBmUqbdRcya9vrLNwR2W1t8ag5CKMd0YnzkjV0yT-MDZziJQttZxihXM8pBzG-l2_f2PHC5BK4KFVVrPPlXxeIgpl_TayFwxMCHfzri9DHMytD1wzkC8Y3tiDP-77SFH_VDGscUTyDo2iqlbR6ohk6nkS2WlaNBnA-eXk2t7oy5bpD7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امروز تیم بانوان با زنان نوشهر بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140818" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
